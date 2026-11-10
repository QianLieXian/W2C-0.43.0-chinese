# Translator - Screen.rpy
# ----------------------------------------------------------------------------------------------------
# TRANSLATOR TOOL  —  the UI: Browse (find the line), View (see the shot), Edit (write the translation).
# ----------------------------------------------------------------------------------------------------
# The tool sets its own text sizes instead of inheriting the game's: a translator reads dozens of lines at
# a glance and needs density a dialogue-sized font cannot give. Every style here is `tl_`-prefixed so it
# stays out of the host game's way.
#
# Three details are deliberate, not stylistic:
#   1. The edit box is `tl_field`, not `input` — the tag-colouring, click-to-caret field from
#      "Translator - Field.rpy". Everything else about it is Ren'Py's own input statement.
#   2. The field is reached through two alternating `use tl_draft` branches. Ren'Py hands a rebuilt input
#      its predecessor as `replaces`, which copies the old content over the new default; an untaken `if`
#      branch loses its cache, so alternating is what makes a replaced draft actually appear.
#   3. Widget ids from a `use`d screen still register on the top-level screen, so tag insertion can find
#      the live field with renpy.get_widget("translator", "tl_input") whichever branch built it.
# ----------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------
    # UI-side helpers
    # ------------------------------------------------------------------------------------------------

init -5 python in tltool:

    def tags_in(text):
        """Every tag and variable the original uses, in order, deduplicated — clickable in Edit mode."""
        out = []
        for m in TAG_RE.finditer(text or ""):
            t = m.group(0)
            if t not in out:
                out.append(t)
        return out

    def tag_groups():
        out = []
        for row in renpy.store.TL_TAGS:
            if row[0] not in out:
                out.append(row[0])
        return out

    def tags_of(group):
        return [r for r in renpy.store.TL_TAGS if r[0] == group]

    def insert(a, b=None):
        """Drop text in at the caret. With a closing half, the caret lands between the two — and with a
           selection, the two halves go around it, which is what makes select-then-click-{b} work."""
        w = renpy.get_widget("translator", input_id())
        if w is None:
            return
        i, j = w.selection() or (w.caret_pos, w.caret_pos)
        w.sel_anchor = w.sel_point = None
        inside = w.content[i:j]
        new = w.content[:i] + a + inside + (b or "") + w.content[j:]
        w.caret_pos = i + len(a) + len(inside)
        w.update_text(new, True)
        set_draft(new)
        renpy.restart_interaction()

    def row_label(entry):
        """`[speaker] original` for the browser list, already escaped and clipped."""
        who = entry.who or (renpy.translate_string("choice") if entry.kind == "string" else renpy.translate_string("narration"))
        return esc("[%s] " % who) + preview(entry.original, 112)

    def folder_label(row):
        # "." is the game root; spell that out rather than showing a bare dot.
        name = renpy.translate_string("(game root)") if row[0] == "." else row[0]
        return ("▼ " if row[0] not in collapsed else "▶ ") + esc(name)

    def file_label(row):
        return esc(row[0].split("/")[-1].rsplit(".rpy", 1)[0])

    def count_of(row):
        return renpy.translate_string("%d/%d") % (row[1], row[2])

    def tone(row):
        """Green once a file or folder is fully translated, red while anything is still missing."""
        return "tl_done_text" if row[2] and row[1] >= row[2] else "tl_todo_text"

    def count_label():
        d, t = progress()
        return renpy.translate_string("%d / %d translated") % (d, t)

    ENTRY_STYLE = {"done": "tl_done", "same": "tl_same", "none": "tl_todo"}
    ENTRY_MARK = {"done": "+", "same": "=", "none": "-"}

    def entry_tone(entry, sub=False):
        """Three states here, unlike the file panel: green rewritten, yellow still a verbatim copy of the
           original, red nothing stored at all."""
        return ENTRY_STYLE[entry.state(lang)] + ("_sub" if sub else "_text")

    def entry_mark(entry):
        return ENTRY_MARK[entry.state(lang)]

    def autosave_label():
        return ("[X]" if autosave_on() else "[  ]").replace("[", "[[") + renpy.translate_string(" Autosave")

    def status_line():
        # The status line doubles as the hint bar whenever there is nothing to report.
        if status:
            return esc(status)
        return "line: left-click = view, right-click = edit   ·   folder: left-click = fold, right-click = filter"


    # ------------------------------------------------------------------------------------------------
    # Styles
    # ------------------------------------------------------------------------------------------------

style tl_frame is default:
    background "#141414F2"
    padding (14, 12)

style tl_text is default:
    color "#DCDCDC"
    size 24
    outlines []

style tl_dim is tl_text:
    color "#8C8C8C"

style tl_head is tl_text:
    color "#FFFFFF"
    size 28
    bold True

style tl_button is default:
    background "#2D2D2DFF"
    hover_background "#4B4B4BFF"
    selected_background "#B4143CFF"
    selected_hover_background "#D2325AFF"
    padding (12, 6)

style tl_button_text is tl_text:
    color "#C8C8C8"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    size 23

style tl_row is tl_button:
    background "#1E1E1EE6"
    hover_background "#323232FF"
    selected_background "#50283CFF"
    padding (12, 5)

style tl_folder is tl_row:
    background "#28282DE6"
    hover_background "#3C3C46FF"
    selected_background "#50283CFF"
    padding (10, 7)

style tl_done_text is tl_button_text:
    color "#64D264"
    hover_color "#8CFF8C"
    selected_color "#8CFF8C"

style tl_todo_text is tl_button_text:
    color "#E66464"
    hover_color "#FF8C8C"
    selected_color "#FF8C8C"

style tl_same_text is tl_button_text:
    color "#D2BE46"
    hover_color "#FFF08C"
    selected_color "#FFF08C"

style tl_input is tl_text:
    color "#FFFFFF"
    size 32

style tl_sub is tl_dim:
    size 21

style tl_done_sub is tl_sub:
    color "#468C46"
    hover_color "#64B464"
    selected_color "#64B464"

style tl_todo_sub is tl_sub:
    color "#A05050"
    hover_color "#C87878"
    selected_color "#C87878"

style tl_same_sub is tl_sub:
    color "#8C8040"
    hover_color "#B4A55A"
    selected_color "#B4A55A"

    # Rows carry their own bottom margin instead of vbox spacing, so each one occupies exactly
    # TL_ROW_H and the virtualised spacers line up with the scroll position.
style tl_entry is tl_row:
    bottom_margin 3

style tl_say is tl_text:
    color "#F0F0F0"
    size 32



    # ------------------------------------------------------------------------------------------------
    # Root
    # ------------------------------------------------------------------------------------------------

screen translator():

    modal True
    zorder TL_ZORDER

    if tltool.mode == "browse":
        add "#0A0A0AFF"
    else:
        use tl_stage

    if tltool.mode == "edit":
        add TL_SCRIM

    use tl_topbar

    if tltool.mode == "browse":
        use tl_browse

    elif tltool.mode == "view":
        use tl_view

    elif tltool.sel is not None:

        # ---------------- Edit mode, inline so get_widget can reach the input ----------------

        frame:
            style "tl_frame"
            xalign 0.5
            ypos 148
            xsize 1720
            background "#000000A0"
            text tltool.meta(tltool.sel) style "tl_dim"

            # The translation itself: white, mid-screen, over the scrim.
        frame:
            style "tl_frame"
            xalign 0.5
            ypos 204
            xsize 1720
            ysize 350
            background "#00000064"

                # Ren'Py hands a rebuilt input its predecessor as `replaces`, which copies the OLD content
                # over the new default — so moving to another line would keep the previous translation.
                # An untaken `if` branch loses its screen-language cache, so alternating between two uses
                # guarantees a genuinely fresh input whenever the draft is replaced from outside.
            if tltool.gen % 2:
                use tl_draft
            else:
                use tl_draft

            # Tags the original uses — click one to place it at the caret.
        hbox:
            xalign 0.5
            ypos 566
            spacing 6
            text renpy.translate_string("in original:") style "tl_dim" yalign 0.5
            for t in tltool.tags_in(tltool.sel.original)[:16]:
                textbutton tltool.esc(t):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.insert, t)

            # Full palette, grouped.
        frame:
            style "tl_frame"
            xalign 0.5
            ypos 610
            xsize 1720
            ysize 250
            background "#0A0A0AC8"
            viewport:
                scrollbars "vertical"
                mousewheel True
                vscrollbar_xsize 12
                vbox:
                    spacing 4
                    for g in tltool.tag_groups():
                        hbox:
                            spacing 5
                            text g style "tl_dim" yalign 0.5 xminimum 110
                            for tag_row in tltool.tags_of(g):
                                textbutton tag_row[1]:
                                    style "tl_button"
                                    text_style "tl_button_text"
                                    action Function(tltool.insert, tag_row[2], tag_row[3])

            # Reference, sitting where the game's own dialogue bar sits.
        frame:
            style "tl_frame"
            xalign 0.5
            ypos 872
            xsize 1720
            ysize 186
            background "#000000D2"
            vbox:
                spacing 6
                hbox:
                    spacing 6
                    text renpy.translate_string("reference:") style "tl_dim" yalign 0.5
                    textbutton renpy.translate_string("original"):
                        style "tl_button"
                        text_style "tl_button_text"
                        action Function(tltool.set_ref, None)
                        selected tltool.ref_lang is None
                    for l in tltool.languages():
                        if l != tltool.lang:
                            textbutton l:
                                style "tl_button"
                                text_style "tl_button_text"
                                action Function(tltool.set_ref, l)
                                selected tltool.ref_lang == l
                    if tltool.sel.who:
                        text tltool.esc("— " + tltool.sel.who) style "tl_dim" yalign 0.5
                text tltool.colorize(tltool.sel.text_or_original(tltool.ref_lang)) style "tl_say"

        key "game_menu" action Function(tltool.set_mode, "view")
        key "alt_K_s" action Function(tltool.save)
        key "alt_K_RIGHT" action Function(tltool.step, 1)
        key "alt_K_LEFT" action Function(tltool.step, -1)


    # The editable field itself. Kept in its own screen only so the two branches above can share it.
screen tl_draft():

    tl_field:
        id "tl_input"
        default tltool.draft
        changed tltool.set_draft
        multiline True
        copypaste True
        length 4000
        xmaximum 1660
        style "tl_input"


    # ------------------------------------------------------------------------------------------------
    # Reconstructed shot
    # ------------------------------------------------------------------------------------------------

screen tl_stage():

    add "#000000FF"

        # No placement here on purpose: each layer already carries the image_placement style and its
        # own `at` transforms, exactly as Ren'Py composes a shown image.
    for d in tltool.stage_for(tltool.sel):
        add d


    # ------------------------------------------------------------------------------------------------
    # Top bar
    # ------------------------------------------------------------------------------------------------

screen tl_topbar():

        # Two rows on purpose: a game with a dozen languages plus the edit buttons overruns 1920px on
        # one line, and the overflow silently eats Close and Export off the right edge.
    frame:
        style "tl_frame"
        xfill True
        ysize TL_TOPBAR
        background "#0A0A0AF0"

        vbox:
            spacing 6

                # Row 1 — where you are, and the way out.
            hbox:
                spacing 6

                text renpy.translate_string("TRANSLATOR") style "tl_head" yalign 0.5

                textbutton renpy.translate_string("Browse"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.set_mode, "browse")
                    selected tltool.mode == "browse"
                textbutton renpy.translate_string("View"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.set_mode, "view")
                    selected tltool.mode == "view"
                    sensitive tltool.sel is not None
                textbutton renpy.translate_string("Edit"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.set_mode, "edit")
                    selected tltool.mode == "edit"
                    sensitive tltool.sel is not None

                null width 18
                if tltool.mode != "browse":
                    textbutton renpy.translate_string("< prev"):
                        style "tl_button"
                        text_style "tl_button_text"
                        action Function(tltool.step, -1)
                    textbutton renpy.translate_string("next >"):
                        style "tl_button"
                        text_style "tl_button_text"
                        action Function(tltool.step, 1)
                textbutton renpy.translate_string("Next untranslated"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.next_todo)

                null width 18
                textbutton renpy.translate_string("tl folder"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.open_tl_folder)
                textbutton renpy.translate_string("Export"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.export, tltool.lang)
                textbutton renpy.translate_string("Close"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.close_tool)

                # Row 2 — language, and what you can do to the line you are on.
            hbox:
                spacing 6

                text renpy.translate_string("lang:") style "tl_dim" yalign 0.5
                for l in tltool.languages():
                    textbutton l:
                        style "tl_button"
                        text_style "tl_button_text"
                        action Function(tltool.set_lang, l)
                        selected tltool.lang == l
                textbutton renpy.translate_string("+ new"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.ask_new_language)

                if tltool.mode == "edit":
                    null width 18
                    textbutton renpy.translate_string("Save (alt+S)"):
                        style "tl_button"
                        text_style "tl_button_text"
                        action Function(tltool.save)
                    textbutton tltool.autosave_label():
                        style "tl_button"
                        text_style "tl_button_text"
                        action ToggleField(persistent, "tl_autosave")
                        selected persistent.tl_autosave
                    textbutton tltool.atomic_label():
                        style "tl_button"
                        text_style "tl_button_text"
                        action ToggleField(persistent, "tl_atomic")
                        selected persistent.tl_atomic
                    textbutton renpy.translate_string("Revert"):
                        style "tl_button"
                        text_style "tl_button_text"
                        action Function(tltool.revert)
                    textbutton renpy.translate_string("Use original"):
                        style "tl_button"
                        text_style "tl_button_text"
                        action Function(tltool.use_original)
                    textbutton renpy.translate_string("Copy"):
                        style "tl_button"
                        text_style "tl_button_text"
                        action Function(tltool.to_clipboard, tltool.draft, "Translation")
                    textbutton renpy.translate_string("Copy orig."):
                        style "tl_button"
                        text_style "tl_button_text"
                        action Function(tltool.to_clipboard, tltool.sel.original if tltool.sel else "", "Original")

            text tltool.status_line() style "tl_dim"

    if tltool.mode == "browse":
        key "game_menu" action Function(tltool.close_tool)


    # ------------------------------------------------------------------------------------------------
    # Browse
    # ------------------------------------------------------------------------------------------------

screen tl_browse():

        # One panel: files grouped under their folder, each section foldable. Green once a file is fully
        # translated, red while anything in it is still missing, so progress reads at a glance.
    frame:
        style "tl_frame"
        xpos 20
        ypos 148
        xsize 460
        ysize 912
        vbox:
            spacing 4
            text renpy.translate_string("FILES") style "tl_head"
            viewport:
                scrollbars "vertical"
                mousewheel True
                vscrollbar_xsize 12
                vbox:
                    spacing 2

                    textbutton renpy.translate_string("- everything -"):
                        style "tl_row"
                        text_style "tl_button_text"
                        xfill True
                        action [Function(tltool.set_folder, None), Function(tltool.set_file, None)]
                        selected tltool.folder is None and tltool.cur_file is None

                    for frow in tltool.tree():

                        button:
                            style "tl_folder"
                            xfill True
                            action Function(tltool.toggle_folder, frow[0])
                            alternate [Function(tltool.set_folder, frow[0]), Function(tltool.set_file, None)]
                            selected tltool.folder == frow[0] and tltool.cur_file is None
                            hbox:
                                spacing 6
                                text tltool.folder_label(frow) style tltool.tone(frow) xminimum 290
                                text tltool.count_of(frow) style tltool.tone(frow)

                        if frow[0] not in tltool.collapsed:
                            for fr in frow[3]:
                                button:
                                    style "tl_row"
                                    xfill True
                                    action Function(tltool.set_file, fr[0])
                                    selected tltool.cur_file == fr[0]
                                    hbox:
                                        spacing 6
                                        null width 10
                                        text tltool.file_label(fr) style tltool.tone(fr) xminimum 276
                                        text tltool.count_of(fr) style tltool.tone(fr)

    vbox:
        xpos 500
        ypos 148
        spacing 10

        frame:
            style "tl_frame"
            xsize 1400
            hbox:
                spacing 10
                text renpy.translate_string("search") style "tl_dim" yalign 0.5
                frame:
                    background "#000000B4"
                    xsize 570
                    padding (10, 6)
                    input:
                        id "tl_search"
                        default tltool.search
                        changed tltool.set_search
                        copypaste True
                        length 80
                        style "tl_text"
                textbutton renpy.translate_string("All"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.set_only, "all")
                    selected tltool.only == "all"
                textbutton renpy.translate_string("TODO"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.set_only, "todo")
                    selected tltool.only == "todo"
                textbutton renpy.translate_string("Done"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.set_only, "done")
                    selected tltool.only == "done"
                textbutton renpy.translate_string("Copies"):
                    style "tl_button"
                    text_style "tl_button_text"
                    action Function(tltool.set_only, "same")
                    selected tltool.only == "same"
                text tltool.count_label() style "tl_dim" yalign 0.5

            # Scrolls the whole result set, but only builds the rows on screen — see tltool.list_window.
        frame:
            style "tl_frame"
            xsize 1400
            ysize TL_LIST_H + 24
            viewport:
                yadjustment tltool.list_adj()
                scrollbars "vertical"
                mousewheel True
                draggable True
                vscrollbar_xsize 12
                vbox:
                    spacing 0
                    $ win = tltool.list_window()
                    null height win[0]
                    for e in win[1]:
                        button:
                            style "tl_entry"
                            xsize 1360
                            ysize 64
                            action Function(tltool.open_entry, e, False)
                            alternate Function(tltool.open_entry, e, True)
                            selected tltool.sel is e
                            hbox:
                                spacing 10
                                text tltool.entry_mark(e) style tltool.entry_tone(e) yalign 0.5 xminimum 20
                                vbox:
                                    spacing 0
                                    text tltool.row_label(e) style tltool.entry_tone(e)
                                    text tltool.preview(e.current(tltool.lang) or "(not translated)", 118) style tltool.entry_tone(e, True)
                    null height win[2]


    # ------------------------------------------------------------------------------------------------
    # View
    # ------------------------------------------------------------------------------------------------

screen tl_view():

    if tltool.sel is not None:

        frame:
            style "tl_frame"
            xalign 0.5
            ypos 148
            xsize 1720
            background "#000000A0"
            text tltool.meta(tltool.sel) style "tl_dim"

            # The line as a player meets it — rendered, not quoted: variables filled in and tags acted
            # on, so what stands here is what the scene will show. Edit mode keeps the source visible.
        button:
            xalign 0.5
            ypos 824
            xsize 1720
            ysize 236
            background "#000000C8"
            hover_background "#0A0A0AD2"
            padding (24, 18)
            action Function(tltool.set_mode, "edit")
            vbox:
                spacing 6
                if tltool.sel.who:
                    text tltool.esc(tltool.sel.who) style "tl_head"
                tl_line tltool.rendered(tltool.sel.text_or_original(tltool.lang)) style "tl_say"

    key "game_menu" action Function(tltool.set_mode, "browse")
