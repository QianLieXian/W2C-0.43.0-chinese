# Translator - Field.rpy
# ----------------------------------------------------------------------------------------------------
# TRANSLATOR TOOL  —  the text field: coloured tags, mouse caret, selection, whole-tag and word erase.
# ----------------------------------------------------------------------------------------------------
# Ren'Py's own `input` is a Text with a caret spliced into it: it paints every character alike, only ever
# leaves the caret where the keyboard left it, selects nothing, and erases one character at a time. A
# translator wants the opposite of all four — tags have to stand apart from the words, the caret has to
# land where the mouse clicked, dragging has to select, and `{w=[wt1]}` has to go in one keystroke.
#
# Two things the engine does not offer are built here from the laid-out glyphs Ren'Py keeps for its own
# hyperlink rectangles: which character a screen point is on (offsets()), and where on screen a range of
# characters sits (selection_rects()). Everything the mouse does rests on those two.
#
# TLInput subclasses Input, and the `tl_field` screen statement puts it in Edit mode's place. Both are
# declared in a `python early` block because a screen-language statement has to exist before the screen
# using it is PARSED, which happens at load time — long before any init block runs. Ren'Py loads script
# files in path order, so this file's name sorting ahead of "Translator - Screen.rpy" is what holds that.
# ----------------------------------------------------------------------------------------------------

python early in tltool:

    # Bound once here rather than reached through `renpy.` on every call: this runs inside the event loop.
    _behavior = renpy.display.behavior
    _pygame = renpy.pygame_sdl2

    # The glyph Ren'Py lays out for a displayable inside text — here, always the caret. It stands for no
    # character at all, which is what the offset map below has to know.
    _OBJECT = 0xFFFC

    class TLInput(_behavior.Input):
        """Ren'Py's input field with the four things a translation box needs it to do."""

        # The selection runs from the anchor (where the drag began) to the point (where it is now), in
        # either direction. Both None means nothing is selected.
        sel_anchor = None
        sel_point = None
        dragging = False

        # Multi-click tracking: how many clicks the current run is up to, and when and where it started.
        clicks = 0
        click_st = -99.0
        click_at = (0, 0)

        def __init__(self, *args, **kwargs):

            # Ren'Py rebuilds an input whenever a keyword of its screen statement changes — which the
            # draft does on every keystroke — and hands the old one over as `replaces`. It carries the
            # content and the caret across itself but knows nothing of a selection, so that comes here
            # or typing one character would drop it. Assigned before super(), which ends by laying the
            # text out and would otherwise draw one frame with the selection missing.
            old = kwargs.get("replaces")

            if isinstance(old, TLInput):
                self.sel_anchor, self.sel_point = old.sel_anchor, old.sel_point
                self.dragging = old.dragging
                self.clicks, self.click_st, self.click_at = old.clicks, old.click_st, old.click_at

            super(TLInput, self).__init__(*args, **kwargs)

        def update_text(self, new_content, editable, check_size=False):
            """Rebuilds the visible text. Same shape as Ren'Py's, except the content goes through
               markup_split() so tags come out coloured instead of flat."""

            # Ren'Py reads interface.text_editing straight; there is no interface before the first frame,
            # which a field built during init would meet.
            interface = renpy.display.interface
            edit = interface.text_editing if interface is not None else None

            old_content = self.content

            if new_content != self.content or editable != self.editable or edit:
                renpy.display.render.redraw(self, 0)

            self.editable = editable

            caret = self.style.caret
            if caret is None:
                caret = self.caret

                # Text mid-composition in the IME — how a dead key or an accent arrives on Windows.
            if edit:
                self.edit_text = edit.text
                parts = (
                    edit.text[:edit.start],
                    edit.text[edit.start:edit.start + edit.length],
                    edit.text[edit.start + edit.length:],
                )
                edit_text = "".join(
                    "{u=%d}%s{/u}" % (2 if i == 1 else 1, brace(p)) for i, p in enumerate(parts) if p
                )
            else:
                self.edit_text = ""
                edit_text = ""

            def set_content(content):
                if editable:
                    head, tail = markup_split(content, self.caret_pos, self.selection(), self.style.color)
                    caret_content = head + [edit_text, caret] + tail
                else:
                    head, tail = markup_split(content, None)
                    caret_content = head + tail

                if not content:
                    caret_content.append("{space=1}")

                self.set_text(caret_content)

                if isinstance(self.caret, _behavior.CaretBlink):
                    self.caret.st_base = self.caret.st
                    renpy.display.render.redraw(self.caret, 0)

            set_content(new_content)

            if check_size and self.pixel_width:
                w, _h = self.size()
                if w > self.pixel_width:
                    self.caret_pos = self.old_caret_pos
                    set_content(old_content)
                    return

            if new_content != old_content:
                self.content = new_content

                if self.changed:
                    self.changed(new_content)

        def event(self, ev, x, y, st):

            if not self.editable:
                return super(TLInput, self).event(ev, x, y, st)

            if self.mouse(ev, x, y):
                raise renpy.display.core.IgnoreEvent()

            span = self.selection()

                # Copy takes the selection when there is one. Everything else about copying is Ren'Py's.
            if span and self.copypaste and _behavior.map_event(ev, "input_copy"):
                _pygame.scrap.put(_pygame.scrap.SCRAP_TEXT, self.content[span[0]:span[1]].encode("utf-8"))
                raise renpy.display.core.IgnoreEvent()

                # Any other keystroke ends the selection — by replacing it, erasing it, or just dropping it.
            if span and ev.type in (_pygame.KEYDOWN, _pygame.TEXTINPUT):
                if self.overwrite(ev, span):
                    raise renpy.display.core.IgnoreEvent()

                # A tag is one thing: erasing over `{w=[wt1]}` takes the tag, not its last bracket.
            if atomic_on():
                cut = None

                if _behavior.map_event(ev, "input_backspace"):
                    cut = tag_span(self.content, self.caret_pos, True)
                elif _behavior.map_event(ev, "input_delete"):
                    cut = tag_span(self.content, self.caret_pos, False)

                if cut is not None:
                    self.replace(cut[0], cut[1], "")
                    raise renpy.display.core.IgnoreEvent()

                # CTRL+erase takes one word, with a tag, a variable or punctuation stopping it like a space.
            cut = None

            if _behavior.map_event(ev, "input_delete_word"):
                cut = word_span(self.content, self.caret_pos, True)
            elif _behavior.map_event(ev, DEL_WORD_RIGHT):
                cut = word_span(self.content, self.caret_pos, False)

            if cut is not None:
                self.replace(cut[0], cut[1], "")
                raise renpy.display.core.IgnoreEvent()

                # CTRL+arrow moves exactly as far as CTRL+erase would take, so a tag or a variable stops
                # the caret instead of being stepped over the way Ren'Py's own whitespace jump does.
            back = _behavior.map_event(ev, "input_jump_word_left")

            if self.arrowkeys and (back or _behavior.map_event(ev, "input_jump_word_right")):
                step = word_span(self.content, self.caret_pos, back)

                    # No span means the caret is already against an edge it may not cross. The event is
                    # still ours: letting it through would hand the jump back to Ren'Py, which counts
                    # spaces only and would walk straight over the tag we just stopped at.
                if step is not None:
                    self.caret_pos = step[0] if back else step[1]
                    self.update_text(self.content, self.editable)

                renpy.display.render.redraw(self, 0)
                raise renpy.display.core.IgnoreEvent()

            return super(TLInput, self).event(ev, x, y, st)

        def mouse(self, ev, x, y):
            """Caret, drag-select and multi-click. True when the event was ours and nothing else gets it."""

            if ev.type == _pygame.MOUSEMOTION:
                if not self.dragging:
                    return False

                    # A button released off the window never reaches us; the motion after it says so.
                held = getattr(ev, "buttons", None)
                if held is not None and not held[0]:
                    self.dragging = False
                    return False

                pos = self.caret_at(x, y, clamp=True)
                if pos is not None and pos != self.sel_point:
                    self.sel_point = self.caret_pos = pos
                    self.update_text(self.content, self.editable)
                    renpy.display.render.redraw(self, 0)

                return True

            if ev.type == _pygame.MOUSEBUTTONUP and ev.button == 1 and self.dragging:
                # Swallowed on purpose: a drag that ends over a button must not also press the button.
                self.dragging = False
                return True

            if ev.type != _pygame.MOUSEBUTTONDOWN or ev.button != 1:
                return False

            pos = self.caret_at(x, y)
            if pos is None:
                return False

                # A run of clicks has to stay in one place as well as keep up the pace, or dragging the
                # mouse across the line and clicking again would read as a double. Timed off the wall
                # clock rather than the displayable's own `st`, which restarts whenever a keystroke
                # rebuilds the field and would make the click after typing look instantaneous.
            now = renpy.display.core.get_time()
            near = abs(x - self.click_at[0]) < 6 and abs(y - self.click_at[1]) < 6
            quick = (now - self.click_st) < renpy.store.TL_MULTICLICK
            self.clicks = (self.clicks % 3) + 1 if (near and quick) else 1
            self.click_st, self.click_at = now, (x, y)

            if self.clicks == 3:
                self.sel_anchor, self.sel_point = 0, len(self.content)
                self.caret_pos = len(self.content)

            elif self.clicks == 2:
                self.sel_anchor, self.sel_point = select_span(self.content, pos)
                self.caret_pos = self.sel_point

            else:
                self.sel_anchor, self.sel_point = pos, None
                self.caret_pos = pos
                self.dragging = True

            self.update_text(self.content, self.editable)
            renpy.display.render.redraw(self, 0)
            return True

        def overwrite(self, ev, span):
            """Applies one keystroke to a selection: typing and pasting replace it, erasing removes it,
               moving the caret gives it up, and anything else leaves it exactly as it was.

            The last case is the one worth stating. A keystroke is not one event — holding shift, or any
            other modifier, is a KEYDOWN all of its own, and only a key that does something to the text or
            the caret may touch the selection. Anything else has to pass through untouched, or the shift
            in front of a capital letter would throw the selection away before the letter arrived.

            Returns True when the event has nothing left to do.
            """

            erase = any(_behavior.map_event(ev, k) for k in ERASE_KEYS)

                # SDL announces a typed character twice: a KEYDOWN carrying no text, then the TEXTINPUT
                # that actually holds it. Acting on the KEYDOWN would drop the selection while leaving
                # its words in place, and the character would land beside them instead of over them —
                # so leave it entirely alone and let the TEXTINPUT behind it do the replacing.
            if not erase and ev.type == _pygame.KEYDOWN and renpy.display.interface.text_event_in_queue():
                return False

            if erase or (
                ev.type == _pygame.TEXTINPUT
                or (self.copypaste and _behavior.map_event(ev, "input_paste"))
                or (self.multiline and _behavior.map_event(ev, "input_next_line"))
                or (ev.type == _pygame.KEYDOWN and ev.unicode and ord(ev.unicode[0]) >= 32)
            ):
                self.sel_anchor = self.sel_point = None
                self.replace(span[0], span[1], "")

                # Erasing was the whole job; typing and pasting still have their own text to put in.
                return bool(erase)

                # Moving the caret gives the selection up. Dropping it has to lay the text out again:
                # the highlight is recomputed every frame, but the flipped colours under it live in the
                # markup, and would otherwise stay behind on a field with nothing selected any more.
            if any(_behavior.map_event(ev, k) for k in MOVE_KEYS):
                self.sel_anchor = self.sel_point = None
                self.update_text(self.content, self.editable)
                renpy.display.render.redraw(self, 0)

            return False

        def replace(self, a, b, text):
            """Swaps content[a:b] for `text` and leaves the caret after it."""
            self.old_caret_pos = self.caret_pos
            self.caret_pos = a + len(text)
            self.update_text(self.content[:a] + text + self.content[b:], self.editable)
            renpy.display.render.redraw(self, 0)

        def selection(self):
            """The selected range as (start, end), or None when nothing is selected."""
            if self.sel_anchor is None or self.sel_point is None or self.sel_anchor == self.sel_point:
                return None

            a, b = sorted((self.sel_anchor, self.sel_point))
            return (max(0, a), min(b, len(self.content)))

        def render(self, width, height, st, at):
            rv = super(TLInput, self).render(width, height, st, at)

            bands = self.selection_rects()
            if not bands:
                return rv

                # Ren'Py has no text tag for a background, so the highlight is painted under the finished
                # text render rather than described in the markup. The text itself is colour-flipped in
                # markup_split(), which is what keeps it legible on top of this.
            out = renpy.display.render.Render(rv.width, rv.height)
            fill = renpy.color.Color(renpy.store.TL_SELECT_COLOR)

            for bx, by, bw, bh in bands:
                band = renpy.display.render.Render(bw, bh)
                band.fill(fill)
                out.blit(band, (bx, by))

            out.blit(rv, (0, 0))
            out.text_input = getattr(rv, "text_input", False)
            return out

        def selection_rects(self):
            """One rectangle per line of the selection, in this displayable's own coordinates."""

            span = self.selection()
            layout = self.get_layout()

            if span is None or layout is None or not layout.lines:
                return []

            a, b = span
            offsets = self.offsets(layout)
            out = []

            for line in layout.lines:
                lo = hi = None

                for g in line.glyphs:
                    i = offsets.get(id(g))
                    if i is None or g.character == _OBJECT or not (a <= i < b):
                        continue
                    lo = g.x if lo is None else min(lo, g.x)
                    hi = g.x + g.advance if hi is None else max(hi, g.x + g.advance)

                if lo is None or hi <= lo:
                    continue

                bx, by = layout.unscale_pair(lo + layout.xoffset, line.y + layout.yoffset)
                bw, bh = layout.unscale_pair(hi - lo, line.height)
                out.append((int(bx), int(by), max(1, int(round(bw))), max(1, int(round(bh)))))

            return out

        def caret_at(self, x, y, clamp=False):
            """The content offset under a point on screen, or None when the click missed the text.

            Ren'Py keeps no map from pixel to character, so this reads the laid-out glyphs back: pick the
            line the y falls in, then the glyph the x falls in, and take the nearer of its two edges.
            `clamp` is for a drag, which has to keep tracking after the mouse leaves the text.
            """

                # Mid-composition the IME's own glyphs sit in the line and the offsets no longer line up.
            if self.edit_text:
                return None

            layout = self.get_layout()
            if layout is None or not layout.lines:
                return None

                # Glyph coordinates are drawable-resolution and shifted by the outline border, while a
                # point from the event loop is virtual — the same conversion the hyperlink rects make.
            scale = layout.oversample
            sx = x * scale - layout.xoffset
            sy = y * scale - layout.yoffset

            last = layout.lines[-1]
            slack = 8 * scale

            if not clamp and (sy < -slack or sy > last.y + last.height + slack):
                return None

            line = last
            for l in layout.lines:
                if sy < l.y + l.height:
                    line = l
                    break

            offsets = self.offsets(layout)
            after = None

            for g in line.glyphs:
                i = offsets.get(id(g))
                if i is None or g.character == _OBJECT:
                    continue
                if sx < g.x + g.advance / 2.0:
                    return min(i, len(self.content))
                after = i + 1

            if after is None:
                after = offsets.get(id(line.glyphs[0]), 0) if line.glyphs else 0

            return min(after, len(self.content))

        def offsets(self, layout):
            """Every laid-out glyph mapped back to the content offset it came from.

            Within a paragraph glyphs run one per character — an escaped `{{` is still one glyph, and a
            colour tag is none at all. The caret is a zero-width displayable glyph standing for no
            character, and each paragraph break swallows exactly one newline.
            """

            out = {}
            paragraphs = self.content.split("\n")
            base = 0

            for p, glyphs in enumerate(layout.paragraph_glyphs):
                column = 0

                for g in glyphs:
                    out[id(g)] = base + column
                    if g.character != _OBJECT:
                        column += 1

                if p < len(paragraphs):
                    base += len(paragraphs[p]) + 1

            return out


    def safe_text(*args, **kwargs):
        """A Text that renders broken markup instead of raising on it.

        View mode paints a real line of the game's own dialogue, and a game has lines whose tags do not
        balance — this project ships two. In a scene Ren'Py raises on them; in a preview of arbitrary
        source text that would take the whole tool down, so here the bad tag is shown as the literal
        characters it is. `safe` is a Text argument with no screen-language keyword, hence the wrapper.
        """
        kwargs.setdefault("safe", True)
        return renpy.text.text.Text(*args, **kwargs)


    # `tl_field` is `input` with our class behind it, `tl_line` is `text` with the above behind it.
    # copy_properties keeps every keyword each screen statement already accepts, so both are drop-in.
    renpy.register_sl_displayable("tl_field", TLInput, "input", 0, replaces=True).copy_properties("input")
    renpy.register_sl_displayable("tl_line", safe_text, "text", 0, scope=True, replaces=True).copy_properties("text")


init -5 python in tltool:

    # A tag, or a variable substitution. Everything the tool treats as one indivisible thing: the palette
    # inserts these, the field colours them, and erasing takes one whole.
    TAG_RE = re.compile(r"(\{[^{}]*\}|\[[A-Za-z_][\w.]*\])")

    # Just the variable half of it, for finding the "[wt1]" inside a "{w=[wt1]}".
    VAR_RE = re.compile(r"\[[A-Za-z_][\w.]*\]")

    # Ren'Py's keymap names CTRL+BACKSPACE ("input_delete_word") but has nothing for CTRL+DELETE, so the
    # word erase to the right is matched on its own keysym.
    DEL_WORD_RIGHT = ("osctrl_K_DELETE", "osctrl_KP_DELETE")

    # The two things a keystroke can do to a selection, by Ren'Py keymap name. Everything absent from
    # both — every modifier, every shortcut, every key the field does not act on — leaves it standing.
    ERASE_KEYS = (
        "input_backspace", "input_delete", "input_delete_word", "input_delete_full",
    ) + DEL_WORD_RIGHT

    MOVE_KEYS = (
        "input_left", "input_right", "input_up", "input_down", "input_home", "input_end",
        "input_jump_word_left", "input_jump_word_right",
    )

    def brace(s):
        # Only "{" doubles inside the field: it runs with substitution off, so "[" is already literal.
        return (s or "").replace("{", "{{")

    def edge(out, a, b, delimiter, inside):
        """One bracketed thing: its two delimiters in `delimiter`, everything between them in `inside`."""
        out.append((a, a + 1, delimiter))
        if b - 1 > a + 1:
            out.append((a + 1, b - 1, inside))
        out.append((b - 1, b, delimiter))

    def invert(color):
        """A colour with its channels flipped. White comes back black, which is what keeps selected text
           readable against the highlight however the tag palette is coloured."""
        rgba = renpy.color.Color(color) if color is not None else None

        if rgba is None:
            return "#000000"

        r, g, b, a = rgba
        return "#%02x%02x%02x%02x" % (255 - r, 255 - g, 255 - b, a)

    def flip(spans, select, base):
        """The same runs, cut again at the selection's edges, with everything inside it colour-flipped.
           A run with no colour of its own is flipped from `base`, the style colour it would have used."""
        a, b = select
        out = []

        for x, y, color in spans:
            for lo, hi, chosen in (
                (x, min(y, a), color),
                (max(x, a), min(y, b), invert(color or base)),
                (max(x, b), y, color),
            ):
                if hi > lo:
                    out.append((lo, hi, chosen))

        return out

    def tag_spans(s, select=None, base=None):
        """The line cut into runs of one colour each: bright delimiters, soft insides, plain words None.

        The runs come back in order and cover the whole string, so the read-only markup and the edit box
        walk one segmentation and differ only in how they escape it. With `select`, the runs are cut once
        more at that range's edges and the part inside comes back inverted.
        """

        tag_c, tag_in = renpy.store.TL_TAG_COLOR, renpy.store.TL_TAG_TEXT_COLOR
        var_c, var_in = renpy.store.TL_VAR_COLOR, renpy.store.TL_VAR_TEXT_COLOR

        out = []
        at = 0

        for m in TAG_RE.finditer(s):
            a, b = m.span()

            if a > at:
                out.append((at, a, None))

            if s[a] == "[":
                edge(out, a, b, var_c, var_in)

            else:
                out.append((a, a + 1, tag_c))

                    # A variable inside a tag keeps the variable's own colours, so "{w=[wt1]}" reads as
                    # the two nested things it is rather than one undifferentiated blob.
                inner = a + 1
                for v in VAR_RE.finditer(s, a + 1, b - 1):
                    if v.start() > inner:
                        out.append((inner, v.start(), tag_in))
                    edge(out, v.start(), v.end(), var_c, var_in)
                    inner = v.end()

                if b - 1 > inner:
                    out.append((inner, b - 1, tag_in))

                out.append((b - 1, b, tag_c))

            at = b

        if at < len(s):
            out.append((at, len(s), None))

        return flip(out, select, base) if select else out

    def char_class(content, i):
        """Which of the three things the character at `i` is: 0 blank, 1 a break character, 2 a word."""
        ch = content[i]

        if ch.isspace():
            return 0

        return 1 if ch in renpy.store.TL_BREAK_CHARS else 2

    def word_runs(content, a, b):
        """A stretch of plain text cut at the break characters: each run of them stands on its own, and
           the words between them — their blanks and all — come back one run each."""

        out = []
        at = a
        run = None

        for i in range(a, b):
            hit = char_class(content, i) == 1

            if run is not None and hit != run:
                out.append((at, i))
                at = i

            run = hit

        if b > at:
            out.append((at, b))

        return out

    def word_span(content, pos, back):
        """What a CTRL+erase at `pos` takes: the blanks the caret sits against, plus the one word, tag,
           variable or run of punctuation behind them. None when that side of the caret is empty.

        A tag, a variable and a break character each stop the erase the way a space does, so CTRL+BACKSPACE
        at the end of "hi, {i}there" takes "there" and leaves the tag standing, and one more takes the tag.
        """

        end = len(content)

        if (pos <= 0) if back else (pos >= end):
            return None

        i = pos
        while ((i > 0) if back else (i < end)) and content[i - 1 if back else i].isspace():
            i += -1 if back else 1

            # The edges the erase may not cross: a tag or variable it has reached goes whole, and one the
            # caret sits inside is erased within, never across its own delimiters.
        lo, hi = 0, end

        for a, b in (m.span() for m in TAG_RE.finditer(content)):
            if back and b == i:
                return (a, pos)

            if not back and a == i:
                return (pos, b)

            if a < i < b:
                lo, hi = a + 1, b - 1
                break

            if b <= i:
                lo = b
            else:
                hi = a
                break

        j = i

        if back:
            if i <= lo:
                return (lo, pos) if pos > lo else None

            kind = char_class(content, i - 1)
            while j > lo and char_class(content, j - 1) == kind:
                j -= 1

            return (j, pos)

        if i >= hi:
            return (pos, hi) if hi > pos else None

        kind = char_class(content, i)
        while j < hi and char_class(content, j) == kind:
            j += 1

        return (pos, j)

    def select_span(content, pos):
        """What a double click takes: a whole tag or variable when the click landed inside one, and
           otherwise the stretch of plain text between the tags, variables and punctuation around it."""

        runs = []
        last = 0

        for m in TAG_RE.finditer(content):
            if m.start() > last:
                runs.extend(word_runs(content, last, m.start()))
            runs.append(m.span())
            last = m.end()

        if last < len(content):
            runs.extend(word_runs(content, last, len(content)))

        for a, b in runs:
            if a <= pos < b:
                return (a, b)

        return runs[-1] if runs else (0, 0)

    def colorize(s):
        """A read-only line as markup — tags tinted, every other character shown exactly as written."""
        s = s or ""
        out = []

        for a, b, color in tag_spans(s):
            piece = esc(s[a:b])
            out.append("{color=%s}%s{/color}" % (color, piece) if color else piece)

        return "".join(out)

    def rendered(s):
        """The line the way a player meets it: variables filled in, tags left live for Ren'Py to act on.

        View mode shows the finished sentence rather than its source, so `[C_Nam][fnamehero][C_Off]` is
        the name in the name colour. A line naming something the store has not got right now falls back
        to its source text — a preview is never worth an exception. Either way the result is final text,
        so its brackets are escaped: another substitution pass would chew on a value's own brackets.
        """

        s = s or ""

        try:
            s = renpy.substitute(s, translate=False)
        except Exception:
            pass

        return s.replace("[", "[[")

    def markup_split(content, caret, select=None, base=None):
        """The field's content as coloured markup, cut into the halves before and after the caret.

        A tag the caret sits inside keeps its colour: both halves reach one Text as a single token stream,
        so a {color} span opened in the first half stays open across the caret and closes in the second.
        `caret` is None for a field that is not being edited; `select` and `base` are the selected range
        and the style colour, and colour-flip the selection.
        """

        head, tail = [], []

        def put(s, start):
            # Text starting at content offset `start`, dropped on whichever side of the caret it falls.
            if caret is None or caret <= start:
                tail.append(brace(s))
            elif caret >= start + len(s):
                head.append(brace(s))
            else:
                head.append(brace(s[:caret - start]))
                tail.append(brace(s[caret - start:]))

        for a, b, color in tag_spans(content, select, base):
            if color is None:
                put(content[a:b], a)
                continue

            (head if (caret is not None and caret > a) else tail).append("{color=%s}" % color)
            put(content[a:b], a)
            (head if (caret is not None and caret >= b) else tail).append("{/color}")

        return head, tail

    def tag_span(content, pos, back):
        """The (start, end) of the tag an erase at `pos` takes whole, or None for a plain character."""
        for m in TAG_RE.finditer(content):
            if back and m.end() == pos and m.start() < pos:
                return m.span()
            if not back and m.start() == pos:
                return m.span()
        return None

    def atomic_on():
        return bool(renpy.game.persistent.tl_atomic)

    def atomic_label():
        return ("[X]" if atomic_on() else "[  ]").replace("[", "[[") + " Whole tags"
