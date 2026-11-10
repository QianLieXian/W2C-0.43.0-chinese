# Translator - Data.rpy
# ----------------------------------------------------------------------------------------------------
# TRANSLATOR TOOL  —  index + live-apply layer.  Portable: nothing here knows about the host game.
# ----------------------------------------------------------------------------------------------------
# Everything lives in the "tltool" store, so it never collides with host-game names and is never saved.
# Two kinds of text are indexed side by side, because a translator needs both:
#   1. "say"    — dialogue lines. The engine holds them as `translate <lang> <id>:` blocks of AST nodes,
#                 registered for EVERY language at load time, so we can read and mutate them directly.
#   2. "string" — menu choices and UI text, as `old`/`new` pairs. `translate <lang> strings:` parses into
#                 an Init block of TranslateString nodes rather than a TranslateBlock, so there is nothing
#                 to find in translator.block; the pairs run at startup into translator.strings[lang],
#                 which is filled for EVERY language and carries the tl file each pair came from.
# ----------------------------------------------------------------------------------------------------

init -5 python in tltool:

    # No `import renpy` here: every store already binds `renpy` to renpy.exports, and importing the
    # package would shadow it — losing has_image, get_widget, show_screen and the rest of the API.
    import os
    import re
    import time

    config = renpy.config

    # ------------------------------------------------------------------------------------------------
    # Tool state. Plain module attributes, so none of it is ever written into a player's save.
    # ------------------------------------------------------------------------------------------------
    mode      = "browse"    # browse | view | edit
    lang      = None        # language being translated
    ref_lang  = None        # language shown as reference (None = the original text)
    entries   = []          # every indexed Entry, sorted by file then line
    folders   = []          # sorted folder list, for the left column
    folder    = None        # selected folder (None = all)
    cur_file  = None        # selected file (None = all in folder)
    search    = ""          # search box content
    only      = "all"       # all | todo | done
    sel       = None        # Entry currently opened in view/edit mode
    draft     = ""          # Edit mode input content
    gen       = 0           # bumped when the draft is replaced from outside; flips the screen's input branch
    status    = ""          # last action message, shown in the tool top bar

    # Edits made this session: (kind, lang, key, idx) -> text. Consulted before the engine own tables,
    # so the tool always shows what was typed even if a live AST update was refused.
    overrides = {}

    _visible  = []          # cached result of the current filters
    _vkey     = None        # the filter combination _visible was built for
    by_file   = {}          # rel path -> its entries, grouped once at build time
    collapsed = set()       # folders whose file list is folded away in the browser
    _tree     = []          # cached folder/file panel with counts
    _tkey     = None
    _prog     = (0, 0)      # cached translated/total for the current filters
    _pkey     = None
    _indexed  = False       # the index is built once, on whatever asks for it first
    _lstats   = {}          # language -> (translated, total) over the WHOLE game, for host menus
    _lkey     = None
    _adj      = None        # the browser list's scroll position, kept across screen rebuilds

    # ------------------------------------------------------------------------------------------------
    # Small helpers
    # ------------------------------------------------------------------------------------------------

    def input_id():
        # Stable: the screen always registers the live input under this id, whichever branch built it.
        return "tl_input"

    def bump():
        global gen
        gen += 1

    def set_draft(s):
        global draft
        draft = s

    def preview(s, n=110):
        """One escaped, single-line, clipped copy of a line — safe to drop straight into a button."""
        s = " ".join((s or "").splitlines())
        if len(s) > n:
            s = s[:n - 1] + "…"
        return esc(s)

    def meta(entry):
        """The `file:line  identifier - stage` caption shown above View and Edit."""
        if entry is None:
            return ""
        return esc("[%s:%d]  %s   ·   %s" % (entry.rel, entry.line, entry.key, stage_summary(entry)))

    def esc(s):
        # Text headed for a screen: brace and bracket must be doubled or Ren'Py reads them as markup.
        return (s or "").replace("{", "{{").replace("[", "[[")

    def rel_path(path):
        # Game-relative, forward-slashed path — the identity a translator recognises.
        try:
            return os.path.relpath(path, config.gamedir).replace("\\", "/")
        except Exception:
            return os.path.basename(path or "")

    def node_says(node):
        # A translate block holds a list of statements; a TranslateSay IS the say statement itself.
        if isinstance(node, renpy.ast.TranslateSay):
            return [(0, node)]
        out = []
        for i, n in enumerate(getattr(node, "block", None) or []):
            if isinstance(n, renpy.ast.Say):
                out.append((i, n))
        return out

    def languages():
        # Every language with a tl/ folder or a translate block; tiny set, cheap to rebuild each call.
        out = set(renpy.game.script.translator.languages)
        out.discard(None)
        out.discard("None")
        return sorted(out)

    def _skip(path):
        # Skip anything outside game/, the tl/ mirrors themselves, and whatever TL_IGNORE names.
        if not path:
            return True
        rel = rel_path(path)
        if rel.startswith("..") or rel.startswith(config.tl_directory + "/"):
            return True
        for i in renpy.store.TL_IGNORE:
            if i in rel:
                return True
        return False

    # ------------------------------------------------------------------------------------------------
    # Entry — one editable piece of text.
    # ------------------------------------------------------------------------------------------------

    class Entry(object):

        def __init__(self, kind, src, line, key, idx=0, who=None, original=""):
            self.kind     = kind        # "say" | "string"
            self.src      = src         # absolute path of the file the text was written in
            self.line     = line        # line number in that file
            self.key      = key         # say: the translate identifier | string: the original text
            self.idx      = idx         # which say inside a multi-statement translate block
            self.who      = who         # speaker, for say lines
            self.original = original    # the untranslated text
            self.rel      = rel_path(src)
            self.dir      = os.path.dirname(self.rel) or "."

        def current(self, language):
            """The text stored for `language`, or None when this line has no translation yet."""
            if language is None:
                return self.original

            ov = overrides.get((self.kind, language, self.key, self.idx))
            if ov is not None:
                return ov

            if self.kind == "string":
                return string_table(language).get(self.key)

            node = renpy.game.script.translator.language_translates.get((self.key, language))
            if node is None:
                return None
            for i, say in node_says(node):
                if i == self.idx:
                    return say.what
            return None

        def state(self, language):
            """"none", "same", or "done".

            A stored line counts as translated even when it reads exactly like the original — plenty of
            lines genuinely need no change. "same" exists only so the browser can flag those for a
            second look; it still counts as done everywhere a count is taken.
            """
            t = self.current(language)
            if t is None or not t.strip():
                return "none"
            if t == self.original:
                return "same"
            return "done"

        def done(self, language):
            return self.state(language) != "none"

        def text_or_original(self, language):
            t = self.current(language)
            return self.original if t is None else t

    # ------------------------------------------------------------------------------------------------
    # Index
    # ------------------------------------------------------------------------------------------------

    def string_table(language):
        """The live old -> new map for a language. Mutating it changes what the game says immediately."""
        try:
            return renpy.game.script.translator.strings[language].translations
        except Exception:
            return {}

    def string_loc(language, key):
        """(file, line) the pair was read from, so a save patches the file that already owns it."""
        try:
            return renpy.game.script.translator.strings[language].translation_loc.get(key)
        except Exception:
            return None

    def build_index():
        """Walk the engine translation registry once and flatten it into a sorted list of entries."""
        global entries, folders

        t = renpy.game.script.translator
        out = []

        # 1. Dialogue: every implicit/explicit translate block, already grouped by its source file.
        for fn, items in t.file_translates.items():
            if _skip(fn):
                continue
            for label, node in items:
                for i, say in node_says(node):
                    out.append(Entry("say", fn, say.linenumber, node.identifier, i, say.who, say.what))

        # 2. Menu choices, which the parser collects per file as (line, text) pairs.
        seen = set()
        for fn, items in t.additional_strings.items():
            if _skip(fn):
                continue
            for line, text in items:
                if text in seen:
                    continue
                seen.add(text)
                out.append(Entry("string", fn, line, text, 0, None, text))

        # 3. Any other UI string some language already has a pair for (screens, common, ...).
        for language in languages():
            for old in string_table(language):
                if old in seen:
                    continue
                seen.add(old)
                out.append(Entry("string", _unmirror(string_loc(language, old)), 0, old, 0, None, old))

        out.sort(key=lambda e: (e.dir, e.rel, e.line, e.key))
        entries = out
        folders = sorted(set(e.dir for e in out))

        by_file.clear()
        for e in out:
            by_file.setdefault(e.rel, []).append(e)
        invalidate()
        return len(out)

    def _unmirror(loc):
        """tl/<lang>/X.rpy -> the game file it mirrors, so UI strings file under their source.

        Translation trees do not always agree on where common.rpy and screens.rpy sit — one language may
        nest them under scripts/ — and the engine's own UI strings mirror renpy/common, which has no file
        in game/ at all. When the mirrored path is not a real source file, fall back to the bare name so
        the same string lands in one place no matter which language the tool read it from.
        """
        fn = (loc[0] if isinstance(loc, tuple) else loc) or ""
        p = fn.replace("\\", "/")
        m = re.search(r"(?:^|/)" + re.escape(config.tl_directory) + r"/[^/]+/(.*)$", p)
        rel = (m.group(1) if m else p.split("game/")[-1]).replace("/", os.sep)

        full = os.path.join(config.gamedir, rel)
        if os.path.exists(full):
            return full
        return os.path.join(config.gamedir, os.path.basename(rel))

    # ------------------------------------------------------------------------------------------------
    # Filtering — recomputed only when a filter actually changes, since screens redraw constantly.
    # ------------------------------------------------------------------------------------------------

    def invalidate():
        global _vkey, _tkey, _pkey
        _vkey = _tkey = _pkey = None
        if _adj is not None:
            _adj.value = 0

    def tree():
        """[(folder, done, total, [(file, done, total), ...])] — the merged folder/file panel."""
        global _tree, _tkey
        key = (lang, len(overrides), len(entries))
        if key == _tkey:
            return _tree

        groups = {}
        for f in sorted(by_file):
            rows = by_file[f]
            groups.setdefault(rows[0].dir, []).append((f, sum(1 for e in rows if e.done(lang)), len(rows)))

        out = []
        for d in folders:
            files = groups.get(d, [])
            out.append((d, sum(x[1] for x in files), sum(x[2] for x in files), files))

        _tree, _tkey = out, key
        return out

    def toggle_folder(d):
        """Fold a section away. Purely a view state — it never changes what the list is filtered to."""
        if d in collapsed:
            collapsed.discard(d)
        else:
            collapsed.add(d)
        renpy.restart_interaction()

    def visible():
        global _visible, _vkey
        key = (folder, cur_file, search.lower(), only, lang, len(overrides))
        if key == _vkey:
            return _visible

        q = search.lower()
        out = []
        for e in entries:
            if folder is not None and e.dir != folder:
                continue
            if cur_file is not None and e.rel != cur_file:
                continue
            if only == "todo" and e.done(lang):
                continue
            if only == "done" and not e.done(lang):
                continue
            if only == "same" and e.state(lang) != "same":
                continue
            if q:
                hay = e.original + " " + (e.who or "") + " " + e.key + " " + (e.current(lang) or "")
                if q not in hay.lower():
                    continue
            out.append(e)

        _visible, _vkey = out, key
        return out

    def list_adj():
        """The list's own scroll adjustment, so a rebuild never loses the reader's place."""
        global _adj
        if _adj is None:
            _adj = renpy.display.behavior.Adjustment(changed=lambda v: renpy.restart_interaction())
        return _adj

    def list_window():
        """(top spacer px, rows to build, bottom spacer px).

        The list holds thousands of lines, and building a button for every one of them would cost more
        each frame than the whole rest of the tool. Only the rows actually on screen are built; the two
        spacers stand in for the rest so the scrollbar still measures the real list.
        """
        rows = visible()
        n = len(rows)
        h = renpy.store.TL_ROW_H
        per = int(renpy.store.TL_LIST_H // h) + 2

        first = max(0, int(list_adj().value // h) - 1)
        first = min(first, max(0, n - 1))
        last = min(n, first + per)
        return first * h, rows[first:last], max(0, (n - last) * h)

    def scroll_to(i):
        """Put row i in view, a third of the way down, so its neighbours stay readable."""
        h = renpy.store.TL_ROW_H
        adj = list_adj()

        # Reading back an adjustment clamps to its range, and the viewport only re-derives that on its
        # next render — so set the range for the list we have now, or a jump into a longer list is cut short.
        span = max(0, len(visible()) * h - renpy.store.TL_LIST_H)
        adj.range = span
        adj.value = min(max(0, i * h - int(renpy.store.TL_LIST_H // 3)), span)

    def sel_index():
        rows = visible()
        try:
            return rows.index(sel)
        except ValueError:
            return -1

    def progress():
        global _prog, _pkey
        key = (folder, cur_file, search.lower(), only, lang, len(overrides))
        if key != _pkey:
            rows = visible()
            _prog, _pkey = (sum(1 for e in rows if e.done(lang)), len(rows)), key
        return _prog

    def ensure_index():
        """Build the index once, for callers outside the tool that just want a number out of it."""
        global _indexed
        if not _indexed:
            build_index()
            _indexed = True
        return len(entries)

    def lang_stats(language):
        """(translated, total) for a whole language — "how far along is this one?" for a host-game menu.

        progress() answers the same question for whatever the browser is filtered to; this one always
        counts every indexed line, so every language is measured against the same total. A screen asks
        for this on every redraw, so the answer is cached until the index or the session's edits change.
        """
        global _lstats, _lkey

        ensure_index()

        key = (len(entries), len(overrides))
        if key != _lkey:
            _lstats, _lkey = {}, key

        if language not in _lstats:
            _lstats[language] = (sum(1 for e in entries if e.done(language)), len(entries))
        return _lstats[language]

    # ------------------------------------------------------------------------------------------------
    # Live apply — make the running game use the new text without a restart.
    # ------------------------------------------------------------------------------------------------

    def _name_node(node):
        # Runtime-built nodes still need a unique script name, or rollback trips over them.
        s = renpy.game.script
        node.name = ("tltool", int(time.time()) & 0xFFFFFFFF, s.serial)
        s.serial += 1
        s.namemap[node] = node

    def _live_say(entry, language, text):
        t = renpy.game.script.translator

        node = t.language_translates.get((entry.key, language))
        if node is not None:
            for i, say in node_says(node):
                if i == entry.idx:
                    say.what = text
                    return True

        # No block for this line yet (a language started from scratch) — build one and register it.
        try:
            dn = t.default_translates[entry.key]
            block = []
            for i, s in node_says(dn):
                ns = renpy.ast.Say(
                    (s.filename, s.linenumber), s.who, text if i == entry.idx else s.what, s.with_,
                    interact=s.interact, attributes=s.attributes,
                    arguments=s.arguments, temporary_attributes=s.temporary_attributes)
                _name_node(ns)
                block.append(ns)
            tn = renpy.ast.Translate((dn.filename, dn.linenumber), entry.key, language, block)
            _name_node(tn)
            renpy.ast.chain_block(tn.block, dn.after)
            t.language_translates[(entry.key, language)] = tn
            return True
        except Exception:
            return False

    def _live_string(entry, language, text):
        # This dict IS what renpy.translate_string reads, so writing to it takes effect at once.
        table = string_table(language)
        if table is None:
            return False
        table[entry.key] = text
        return True

    def live_apply(entry, language, text):
        if entry.kind == "string":
            return _live_string(entry, language, text)
        return _live_say(entry, language, text)

    # ------------------------------------------------------------------------------------------------
    # The line on screen — so the tool can open straight onto whatever the player is reading.
    # ------------------------------------------------------------------------------------------------

    def _abs_rel(fn):
        """A game-relative path for a node filename, which the parser hands back in elided form."""
        if not fn:
            return None
        if not os.path.isabs(fn):
            fn = _unelide(fn) or fn
        return rel_path(fn)

    def current_entry():
        """The indexed line the game is sitting on right now, or None when it is not showing dialogue.

        Two ways in, because neither covers every case alone:

          1. The translate identifier the running Translate node put on the context. This is the index's
             own key, so it is exact — and it is the only thing that works once a translation is active,
             because the statement actually executing then lives in tl/<lang>/, not in the file the index
             is built from.
          2. Failing that, where the statement is written. Entries are keyed on the original file and
             line anyway, so this matches directly — it just cannot see through a translated block.
        """
        ensure_index()

        try:
            ctx = renpy.game.context()
        except Exception:
            return None

        ident = getattr(ctx, "translate_identifier", None)
        if ident:
            rows = [e for e in entries if e.kind == "say" and e.key == ident]
            if rows:
                # One block can hold several says; prefer the one whose text is actually on screen.
                what = getattr(renpy.store, "_last_say_what", None)
                for e in rows:
                    if e.original == what:
                        return e
                return rows[0]

        try:
            node = renpy.game.script.lookup(ctx.current) if ctx.current is not None else None
        except Exception:
            node = None

        if node is not None:
            rel = _abs_rel(getattr(node, "filename", None))
            line = getattr(node, "linenumber", None)
            if rel and line:
                for e in entries:
                    if e.line == line and e.rel == rel:
                        return e

        return None

    # ------------------------------------------------------------------------------------------------
    # Open / navigate
    # ------------------------------------------------------------------------------------------------

    def open_tool(at_current=False):
        """Open the tool. With at_current, land in Edit mode on the line the player is reading."""
        global mode, lang, status
        if not _indexed:
            status = renpy.translate_string("Indexed %d lines.") % ensure_index()
        if lang is None:
            langs = languages()
            cur = renpy.game.preferences.language
            lang = cur if cur in langs else (langs[0] if langs else None)
        mode = "browse"

        if at_current:
            e = current_entry()
            if e is not None:
                # open_entry leaves mode on "edit" and seeds the draft; scrolling the browser to the same
                # row means backing out of the line lands on it in the list instead of at the top.
                open_entry(e, edit=True)
                i = sel_index()
                if i >= 0:
                    scroll_to(i)
                status = "Editing the line on screen."
            else:
                status = "No dialogue line on screen — opened the browser instead."

        renpy.show_screen("translator")
        renpy.restart_interaction()

    def close_tool():
        flush()
        renpy.hide_screen("translator")
        renpy.restart_interaction()

    def set_lang(language):
        global lang, ref_lang, draft, status
        flush()
        lang = language

        # The line on screen belongs to the old language — re-seed the box, or you would be typing the
        # previous language's text into the new one.
        if sel is not None:
            draft = sel.text_or_original(lang)
            bump()

        # A reference pointing at the language now being edited would just mirror the box.
        if ref_lang == language:
            ref_lang = None

        invalidate()
        status = renpy.translate_string("Editing: %s") % language
        renpy.restart_interaction()

    def set_folder(d):
        global folder, cur_file
        folder, cur_file = d, None
        invalidate()

    def set_file(f):
        global cur_file
        cur_file = f
        invalidate()

    def set_search(s):
        global search
        search = s or ""
        invalidate()
        renpy.restart_interaction()

    def set_ref(language):
        global ref_lang
        ref_lang = language
        renpy.restart_interaction()

    def set_only(v):
        global only
        only = v
        invalidate()

    def autosave_on():
        return bool(renpy.game.persistent.tl_autosave)

    def flush():
        """Autosave point. Writing on every keystroke would rewrite the file hundreds of times per line,
           so the draft is committed when you leave the line instead — stepping, switching mode, or closing."""
        if not autosave_on() or sel is None or lang is None:
            return
        if draft != sel.text_or_original(lang):
            save(auto=True)

    def open_entry(entry, edit=False):
        global sel, mode, draft
        flush()
        sel = entry
        draft = entry.text_or_original(lang)
        mode = "edit" if edit else "view"
        bump()
        renpy.restart_interaction()

    def set_mode(m):
        global mode, draft
        flush()
        if m == "edit" and sel is not None:
            draft = sel.text_or_original(lang)
            bump()
        mode = m
        renpy.restart_interaction()

    def step(delta):
        """Move to the next/previous line of the current filtered list, staying in the same mode."""
        rows = visible()
        if sel is None or not rows:
            return
        i = max(0, min(max(0, sel_index()) + delta, len(rows) - 1))
        open_entry(rows[i], mode == "edit")
        scroll_to(i)

    def next_todo():
        """Jump to the next line here that still needs work, wrapping once around the list."""
        global status
        rows = visible()
        if not rows:
            return

        start = sel_index() + 1
        order = list(range(start, len(rows))) + list(range(0, max(0, start)))
        for i in order:
            if not rows[i].done(lang):
                wrapped = i < start
                open_entry(rows[i], mode == "edit")
                scroll_to(i)
                if wrapped:
                    status = "Wrapped around to the first line still untranslated."
                return

        status = "Nothing left untranslated in this list."
        renpy.restart_interaction()
