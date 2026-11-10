# Translator - Source.rpy
# ----------------------------------------------------------------------------------------------------
# TRANSLATOR TOOL  —  reads and rewrites the real game/tl/<lang>/**.rpy files.
# ----------------------------------------------------------------------------------------------------
# A save NEVER regenerates a file: it finds the one block that owns this line, replaces that block's
# statement line, and writes everything else back byte-for-byte. Hand-written comments, ordering and
# blank lines survive, so the tool can share a file with a translator working in a text editor.
#
# The replacement line is produced by the engine's own `Say.get_code()` with a filter, which is exactly
# what the Ren'Py launcher uses — so quoting, escapes, attributes and flags come out identical.
# ----------------------------------------------------------------------------------------------------

init -5 python in tltool:

    import shutil

    # ------------------------------------------------------------------------------------------------
    # File primitives
    # ------------------------------------------------------------------------------------------------

    def tl_path(entry, language):
        """Where this line's translation lives: tl/<lang>/ mirroring the source file's own path."""
        p = os.path.join(config.gamedir, config.tl_directory, language, entry.rel.replace("/", os.sep))
        if p.endswith(".rpym"):
            p = p[:-1]
        return p

    def _lines(path):
        # Read as plain utf-8 so a leading BOM survives the round trip untouched.
        if not os.path.exists(path):
            return None
        f = open(path, "r", encoding="utf-8")
        try:
            return f.read().split("\n")
        finally:
            f.close()

    def _write(path, lines):
        d = os.path.dirname(path)
        if d and not os.path.isdir(d):
            os.makedirs(d)
        f = open(path, "w", encoding="utf-8")
        try:
            f.write("\n".join(lines))
        finally:
            f.close()

    def _new_file():
        # Same opening the Ren'Py launcher writes, so a tool-made file looks like a generated one.
        return [chr(0xFEFF) + "# " + "TODO" + ": Translation updated at " + time.strftime("%Y-%m-%d %H:%M"), ""]

    def _body_end(lines, head):
        """First line after the block that opened at `head` — a block ends at the next unindented line."""
        k = head + 1
        while k < len(lines):
            s = lines[k]
            if s.strip() and not s[:1].isspace():
                break
            k += 1
        return k

    def _indent_of(line):
        return re.match(r"^\s*", line).group(0) or "    "

    # ------------------------------------------------------------------------------------------------
    # Dialogue blocks
    # ------------------------------------------------------------------------------------------------

    def _say_code(entry, says, text):
        """The .rpy source line for this say, with `text` swapped in — engine quoting, not ours."""
        for i, s in says:
            if i == entry.idx:
                return s.get_code(lambda _: text)
        who = (entry.who + " ") if entry.who else ""
        return who + renpy.translation.encode_say_string(text)

    def _default_says(entry):
        dn = renpy.game.script.translator.default_translates.get(entry.key)
        return dn, (node_says(dn) if dn is not None else [])

    def write_say(entry, language, text):
        path = tl_path(entry, language)
        lines = _lines(path)
        created = lines is None
        if created:
            lines = _new_file()

        dn, says = _default_says(entry)
        ident = entry.key.replace(".", "_")
        head = re.compile(r"^translate\s+" + re.escape(language) + r"\s+" + re.escape(ident) + r"\s*:\s*$")

        at = None
        for i, ln in enumerate(lines):
            if head.match(ln.rstrip()):
                at = i
                break

        if at is None:
            # No block for this line yet — append one shaped exactly like a generated block.
            if lines and lines[-1].strip():
                lines.append("")
            lines.append("# %s:%d" % (dn.filename if dn else entry.rel, dn.linenumber if dn else entry.line))
            lines.append("translate %s %s:" % (language, ident))
            lines.append("")
            for i, s in says:
                lines.append("    # " + s.get_code())
            if says:
                for i, s in says:
                    lines.append("    " + (s.get_code(lambda _: text) if i == entry.idx else s.get_code()))
            else:
                lines.append("    # " + entry.original)
                lines.append("    " + _say_code(entry, says, text))
            lines.append("")

        else:
            # Replace only the statement line this entry owns; the `# original` comments stay put.
            end = _body_end(lines, at)
            stmts = [k for k in range(at + 1, end)
                     if lines[k].strip() and not lines[k].lstrip().startswith("#")]
            code = _say_code(entry, says, text)
            if entry.idx < len(stmts):
                k = stmts[entry.idx]
                lines[k] = _indent_of(lines[k]) + code
            else:
                lines.insert(end, "    " + code)

        _write(path, lines)
        return path, created

    # ------------------------------------------------------------------------------------------------
    # String pairs (menu choices, UI text)
    # ------------------------------------------------------------------------------------------------

    def _string_path(entry, language):
        """Patch the file that already declares this string for the language.

        Ren'Py refuses to load two `old` entries for the same string, so writing a pair into the mirrored
        file when it already lives elsewhere would break the language on its next load.
        """
        loc = string_loc(language, entry.key)
        if loc:
            for cand in (loc[0], _unelide(loc[0])):
                if cand and os.path.exists(cand):
                    return os.path.normpath(os.path.abspath(cand))
        return tl_path(entry, language)

    def _unelide(fn):
        try:
            return renpy.lexer.unelide_filename(fn)
        except Exception:
            return None

    def write_string(entry, language, text):
        path = _string_path(entry, language)
        lines = _lines(path)
        created = lines is None
        if created:
            lines = _new_file()

        q_old = renpy.translation.quote_unicode(entry.key)
        q_new = renpy.translation.quote_unicode(text)
        old_line = 'old "%s"' % q_old

        at = None
        for i, ln in enumerate(lines):
            if ln.strip() == old_line:
                at = i
                break

        if at is not None:
            for k in range(at + 1, min(at + 6, len(lines))):
                if lines[k].lstrip().startswith("new "):
                    lines[k] = _indent_of(lines[k]) + 'new "%s"' % q_new
                    break
            else:
                lines.insert(at + 1, '    new "%s"' % q_new)

        else:
            # Add the pair to this file's strings block, creating the block when it has none.
            hdr = re.compile(r"^translate\s+" + re.escape(language) + r"\s+strings\s*:\s*$")
            bi = None
            for i, ln in enumerate(lines):
                if hdr.match(ln.rstrip()):
                    bi = i
            if bi is None:
                if lines and lines[-1].strip():
                    lines.append("")
                lines.append("translate %s strings:" % language)
                lines.append("")
                end = len(lines)
            else:
                end = _body_end(lines, bi)
            lines[end:end] = ["    # %s:%d" % (entry.rel, entry.line),
                              '    old "%s"' % q_old,
                              '    new "%s"' % q_new,
                              ""]

        _write(path, lines)

        try:
            renpy.game.script.translator.strings[language].translation_loc.setdefault(entry.key, (path, 0))
        except Exception:
            pass

        return path, created

    # ------------------------------------------------------------------------------------------------
    # Save / revert
    # ------------------------------------------------------------------------------------------------

    def save(auto=False):
        """Write the draft to disk and to the running game."""
        global status
        if sel is None or lang is None:
            status = "Pick a language first."
            renpy.restart_interaction()
            return

        text = draft
        try:
            if sel.kind == "string":
                path, created = write_string(sel, lang, text)
            else:
                path, created = write_say(sel, lang, text)
            overrides[(sel.kind, lang, sel.key, sel.idx)] = text
            live = live_apply(sel, lang, text)
            invalidate()
            status = renpy.translate_string("%s -> %s%s") % (renpy.translate_string("Autosaved" if auto else "Saved"), rel_path(path),
                                     "" if live else renpy.translate_string("   (reload to see it in game)"))
        except Exception as e:
            status = renpy.translate_string("SAVE FAILED: %s") % e

        renpy.restart_interaction()

    def revert():
        """Throw the draft away and go back to what is stored for this line right now."""
        global draft, status
        if sel is not None:
            draft = sel.text_or_original(lang)
            bump()
            status = "Reverted."
        renpy.restart_interaction()

    def use_original():
        """Fill the box with the original line — it already carries every tag in the right place."""
        global draft, status
        if sel is not None:
            draft = sel.original
            bump()
            status = "Filled the box with the original."
        renpy.restart_interaction()

    def to_clipboard(text, what="Text"):
        """Put text on the system clipboard, for pasting outside the game."""
        global status
        try:
            scrap = renpy.pygame_sdl2.scrap
            scrap.put(scrap.SCRAP_TEXT, (text or "").encode("utf-8"))
            status = renpy.translate_string("%s copied to the clipboard.") % what
        except Exception as e:
            status = renpy.translate_string("Clipboard unavailable: %s") % e
        renpy.restart_interaction()

    # ------------------------------------------------------------------------------------------------
    # New language — generate the whole tl/<code> tree from the game's own text.
    # ------------------------------------------------------------------------------------------------

    def ask_new_language():
        # A screen action cannot open an interaction, so the prompt runs in its own context.
        code = renpy.invoke_in_new_context(
            renpy.input, "New language code — the folder name under game/tl/ (e.g. fr, de, pt):", length=24)
        if code:
            new_language(code)

    def new_language(code):
        global status
        code = (code or "").strip()
        if not code or re.search(r"[^A-Za-z0-9_-]", code):
            status = "Bad language code."
            renpy.restart_interaction()
            return

        t = renpy.game.script.translator
        buckets = {}

        def bucket(src):
            p = os.path.join(config.gamedir, config.tl_directory, code, rel_path(src).replace("/", os.sep))
            if p.endswith(".rpym"):
                p = p[:-1]
            return buckets.setdefault(p, [])

        # Dialogue: one block per line, seeded with the original text so nothing reads as missing.
        blocks = 0
        for fn, items in t.file_translates.items():
            if _skip(fn):
                continue
            for label, node in items:
                if (node.identifier, code) in t.language_translates:
                    continue
                says = node_says(node)
                if not says:
                    continue
                out = bucket(fn)
                out.append("# %s:%d" % (node.filename, node.linenumber))
                out.append("translate %s %s:" % (code, node.identifier.replace(".", "_")))
                out.append("")
                for i, s in says:
                    out.append("    # " + s.get_code())
                for i, s in says:
                    out.append("    " + s.get_code())
                out.append("")
                blocks += 1

        # Menu choices: one strings block per file.
        existing = string_table(code)
        for fn, items in t.additional_strings.items():
            if _skip(fn):
                continue
            rows = [(l, s) for l, s in items if s not in existing]
            if not rows:
                continue
            out = bucket(fn)
            out.append("translate %s strings:" % code)
            out.append("")
            for line, s in rows:
                q = renpy.translation.quote_unicode(s)
                out.append("    # %s:%d" % (rel_path(fn), line))
                out.append('    old "%s"' % q)
                out.append('    new "%s"' % q)
                out.append("")
                blocks += 1

        for path, body in buckets.items():
            lines = _lines(path)
            if lines is None:
                lines = _new_file()
            elif lines and lines[-1].strip():
                lines.append("")
            _write(path, lines + body)

        t.languages.add(code)
        set_lang(code)
        status = renpy.translate_string("Created '%s': %d blocks in %d files. Reload the game to load them.") % (code, blocks, len(buckets))
        renpy.restart_interaction()

    # ------------------------------------------------------------------------------------------------
    # Export — a clean copy of the language folder, ready to send to the dev.
    # ------------------------------------------------------------------------------------------------

    def export(language):
        global status
        try:
            src = os.path.join(config.gamedir, config.tl_directory, language)
            if not os.path.isdir(src):
                status = renpy.translate_string("Nothing to export: %s has no tl folder.") % language
                renpy.restart_interaction()
                return

            dst = os.path.join(config.basedir, "translation-%s-%s" % (language, time.strftime("%Y%m%d-%H%M")))
            # Source only — .rpyc is rebuilt by the engine and just bloats the hand-off.
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns("*.rpyc", "*.rpymc", "__pycache__"))
            reveal(dst)
            status = renpy.translate_string("Exported to %s") % os.path.basename(dst)
        except Exception as e:
            status = renpy.translate_string("EXPORT FAILED: %s") % e
        renpy.restart_interaction()

    def reveal(path):
        try:
            import webbrowser
            webbrowser.open("file:///" + os.path.abspath(path).replace("\\", "/"))
        except Exception:
            pass

    def open_tl_folder():
        global status
        if lang:
            reveal(os.path.join(config.gamedir, config.tl_directory, lang))
            status = renpy.translate_string("Opened tl/%s") % lang
        renpy.restart_interaction()
