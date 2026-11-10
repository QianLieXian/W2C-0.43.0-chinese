# Translator - Config.rpy
# ----------------------------------------------------------------------------------------------------
# TRANSLATOR TOOL  —  in-game translation editor for Ren'Py 8.x.  THIS IS THE ONLY FILE YOU EDIT.
# ----------------------------------------------------------------------------------------------------
# INSTALL: copy the whole "tools/Translator" folder anywhere inside your game/ folder. Nothing else.
#
# OPEN IT:
#   1. Hotkey        — TL_KEY below, from any screen, while TL_ENABLED is on.
#   2. Your own menu — drop this single line into any screen you already have:
#          textbutton _("Translator") action TranslatorTool()
#
# WHAT IT EDITS: game/tl/<language>/**.rpy — the very files the Ren'Py launcher generates. A save
# rewrites only that one line's block, leaves the rest of the file byte-for-byte alone, and applies
# the new text to the running game so you see it without restarting.
#
# See ReadMe.md next to this file for the full rundown.
# ----------------------------------------------------------------------------------------------------

    # Master switch. Set False (or gate on your own dev flag) to keep the tool out of a player build.
define TL_ENABLED = True

    # Global hotkey that opens the tool. Set to None to disable the hotkey and use TranslatorTool() only.
define TL_KEY = "shift_K_t"

    # Stacking order of the tool against the host game's own screens. Deliberately far above anything a
    # game is likely to use: overlay screens (quick menus, notification toasts, debug HUDs) are shown on
    # the same layer as the tool and commonly claim zorders in the hundreds or low thousands, and any one
    # of them drawing over the editor makes it unusable. Only lower this if the host game has something
    # that genuinely must stay on top.
define TL_ZORDER = 30000

    # Scrim painted over the game image in Edit mode, so the translation text stays readable.
define TL_SCRIM = "#000000C8"

    # Height of one row in the browser list, and of the list itself. The list is virtualised against
    # these two numbers: only the rows on screen are built, so a 7000-line game scrolls like a small one.
define TL_ROW_H = 67
define TL_LIST_H = 810

    # Autosave commits the line you are on when you leave it. Remembered between sessions.
default persistent.tl_autosave = False

    # Colours the Edit box and the reference bar paint tags and variables in: the bright pair for the
    # delimiters themselves, the soft pair for whatever sits inside them. A variable inside a tag —
    # "{w=[wt1]}" — keeps the variable pair, so the two nest the way they read.
define TL_TAG_COLOR = "#FF00FF"
define TL_TAG_TEXT_COLOR = "#FF96FF"
define TL_VAR_COLOR = "#FF9600"
define TL_VAR_TEXT_COLOR = "#FFC896"

    # Selection: the highlight painted behind selected characters, and the window two clicks have to
    # land inside to count as a double (a third inside the same window makes it a triple). Selected text
    # is drawn with its colours flipped, so it stays legible against the highlight whatever colour it is.
define TL_SELECT_COLOR = "#00FFFF"
define TL_MULTICLICK = 0.35

    # Characters that stand between words. A double click selects up to one of them, and CTRL+BACKSPACE
    # or CTRL+DELETE erases up to one, the same way a tag or a variable stops both. Apostrophes are left
    # out on purpose, so "don't" counts as one word.
define TL_BREAK_CHARS = ',.;:!?¡¿…"“”«»()[]{}<>/\|-–—*+=&%#@~^$'

    # Treats a tag or a variable as one character while erasing: backspace over "{w=[wt1]}" takes the
    # whole tag rather than its last bracket. Toggled from the Edit toolbar, remembered between sessions.
default persistent.tl_atomic = True

    # Height of the two-row top bar. Every panel below it is positioned from this.
define TL_TOPBAR = 140

    # View mode evaluates `show expression <code>` in the game's own store to rebuild composed shots.
    # Turn off if your game's image expressions have side effects.
define TL_EVAL = True

    # Whether looping `at` transforms run in the preview. Off by default: a sprite that never settles is
    # hard to read a line against. One-shot transforms always play and settle either way.
define TL_ANIMATE = False

    # Source files the tool should never list (matched as substrings of the game-relative path).
define TL_IGNORE = ["tools/Translator/"]

    # ------------------------------------------------------------------------------------------------
    # TAG PALETTE  —  the clickable bar in Edit mode.
    # Each row is: (group, label, open, close)
    #   open  : text inserted at the caret.
    #   close : optional closing text; when given, both are inserted and the caret lands between them.
    # The palette is click-only on purpose. It used to carry a keysym per row, but shift+digit and
    # ctrl+digit are how a keyboard types symbols and accents, and the tool would eat them mid-sentence.
    # Replace this whole table with your own game's tags — nothing else in the tool refers to it.
    # ------------------------------------------------------------------------------------------------
define TL_TAGS = [

        # Pacing — this game paces dialogue with {w=[wtN]} pauses instead of literal "...".
    ("Pause",   "0.2s",     "{w=[wt1]}",    None),
    ("Pause",   "0.4s",     "{w=[wt2]}",    None),
    ("Pause",   "0.7s",     "{w=[wt3]}",    None),
    ("Pause",   "1.0s",     "{w=[wt4]}",    None),
    ("Pause",   "wait",     "{w}",          None),
    ("Pause",   "no wait",  "{nw}",         None),
    ("Pause",   "fast",     "{fast}",       None),
    ("Pause",   "break",    "{p}",          None),

        # Colors — [C_*] variables, so a color always ends with [C_Off].
    ("Color",   "off",      "[C_Off]",      None),
    ("Color",   "name",     "[C_Nam]",      "[C_Off]"),
    ("Color",   "date",     "[C_Dat]",      "[C_Off]"),
    ("Color",   "good",     "[C_Pos]",      "[C_Off]"),
    ("Color",   "bad",      "[C_Neg]",      "[C_Off]"),
    ("Color",   "person",   "[C_Per]",      "[C_Off]"),
    ("Color",   "item",     "[C_Itm]",      "[C_Off]"),
    ("Color",   "note",     "[C_Not]",      "[C_Off]"),
    ("Color",   "button",   "[C_But]",      "[C_Off]"),
    ("Color",   "unseen",   "[C_Unv]",      "[C_Off]"),
    ("Color",   "mind",     "[C_Mnd]",      "[C_Off]"),
    ("Color",   "dark",     "[C_Drk]",      "[C_Off]"),

        # Emotion — the game's custom text tags; each wraps the words it acts on.
    ("Emotion", "awkward",  "{aw}",         "{/aw}"),
    ("Emotion", "bounce",   "{bt}",         "{/bt}"),
    ("Emotion", "laugh",    "{lg}",         "{/lg}"),
    ("Emotion", "giggle",   "{gg}",         "{/gg}"),
    ("Emotion", "scare",    "{sc}",         "{/sc}"),
    ("Emotion", "panic",    "{pa}",         "{/pa}"),
    ("Emotion", "thought",  "{mind}",       "{/mind}"),
    ("Emotion", "name",     "{nm}",         "{/nm}"),

        # Style — plain Ren'Py formatting.
    ("Style",   "bold",     "{b}",          "{/b}"),
    ("Style",   "italic",   "{i}",          "{/i}"),
    ("Style",   "under",    "{u}",          "{/u}"),
    ("Style",   "strike",   "{s}",          "{/s}"),
    ("Style",   "para",     "{pr}",         None),
]


    # Drop-in action for other devs: `textbutton _("Translator") action TranslatorTool()` in any screen.
init -4 python:

    class TranslatorTool(Action):
        """Opens the in-game Translator tool.

        at_current=True opens Edit mode on the line the player is reading, which is what the hotkey
        wants — you press it because THIS line is wrong. It falls back to the browser wherever there is
        no dialogue on screen (menus, the main menu), so it is always safe to pass.
        """

        def __init__(self, at_current=False):
            self.at_current = at_current

        def __call__(self):
            tltool.open_tool(at_current=self.at_current)

        def get_sensitive(self):
            return TL_ENABLED


    # Global hotkey, added as an overlay so it answers on every screen without touching the host game.
screen tl_hotkey():

    if TL_ENABLED and TL_KEY:
        key TL_KEY action TranslatorTool(at_current=True)

init 999 python:
    if "tl_hotkey" not in config.overlay_screens:
        config.overlay_screens.append("tl_hotkey")
