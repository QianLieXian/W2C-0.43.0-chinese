# Translator - Stage.rpy
# ----------------------------------------------------------------------------------------------------
# TRANSLATOR TOOL  —  rebuilds the picture that was on screen when a line runs, for View mode.
# ----------------------------------------------------------------------------------------------------
# A translator guesses a line's meaning from what they can see, so View mode reconstructs the shot:
# scan the line's own source file upward for the last `scene`, then replay every `show`/`hide` between
# that scene and the line. Result is a plain list of displayables the screen stacks in order.
#
# It composes each layer the way Ren'Py's own `show` does — ImageReference(name, style="image_placement")
# wrapped in each `at` transform, in order — so `show hero at LL` lands where the game puts it. That is
# also why the screen adds these with no placement properties of its own: the style and the transforms
# already carry the placement, and overriding it would move every sprite to the middle.
#
# An `at` transform is only applied once every expression inside its ATL is checked to evaluate right
# now. A transform reading state this session never set (`transform X: xpos X_pos`) would otherwise
# raise mid-render and take the whole tool down; those are skipped, and the caption says how many.
#
# The scan itself is deliberately a HEURISTIC, not an interpreter: it reads one file top-down and does
# not follow `call`/`jump`, branches, or loops. TL_EVAL is what handles `show expression <code>`.
# ----------------------------------------------------------------------------------------------------

init -5 python in tltool:

    import renpy.atl as _atl        # `as` binds only the alias, so the store's `renpy` stays exports

    _stage_cache = {}
    _stage_error = {}
    _stage_skip = {}        # entry key -> how many `at` transforms were judged unsafe to apply
    _stage_held = {}        # entry key -> how many were held still because they loop forever

    STMT = re.compile(r"^\s*(scene|show|hide)\s+(\S.*?)\s*$")

    # Clause keywords that end the image name and start something else.
    _KW = ("as", "at", "behind", "onlayer", "zorder", "with")

    # ------------------------------------------------------------------------------------------------
    # Statement parsing
    # ------------------------------------------------------------------------------------------------

    def _scan_split(text, stop):
        """Split on `stop` characters that sit outside quotes and brackets, so an expression survives."""
        out, start, depth, quote = [], 0, 0, None
        i = 0
        while i < len(text):
            c = text[i]
            if quote:
                if c == "\\":
                    i += 2
                    continue
                if c == quote:
                    quote = None
            elif c in "\"'":
                quote = c
            elif c in "([{":
                depth += 1
            elif c in ")]}":
                depth -= 1
            elif depth == 0 and c in stop:
                out.append((start, i))
                start = i + 1
            i += 1
        out.append((start, len(text)))
        return [text[a:b].strip() for a, b in out]

    def _clauses(rest):
        """{None: image spec, 'at': ..., 'as': ...} for one show/scene statement."""
        out = {}
        kw = None
        start = 0
        depth = 0
        quote = None
        i = 0
        n = len(rest)

        while i < n:
            c = rest[i]
            if quote:
                if c == "\\":
                    i += 2
                    continue
                if c == quote:
                    quote = None
                i += 1
                continue
            if c in "\"'":
                quote = c
            elif c in "([{":
                depth += 1
            elif c in ")]}":
                depth -= 1
            elif depth == 0 and c.isspace():
                j = i + 1
                while j < n and rest[j].isspace():
                    j += 1
                k = j
                while k < n and not rest[k].isspace():
                    k += 1
                if rest[j:k] in _KW:
                    out.setdefault(kw, rest[start:i].strip())
                    kw = rest[j:k]
                    start = i = k
                    continue
            i += 1

        out.setdefault(kw, rest[start:].strip())
        return out

    # ------------------------------------------------------------------------------------------------
    # `at` transforms
    # ------------------------------------------------------------------------------------------------

    def _expr_ok(expr, ctx):
        if expr is None:
            return True
        try:
            renpy.python.py_eval(expr, locals=ctx)
            return True
        except Exception:
            return False

    def _exprs_ok(value, ctx):
        if isinstance(value, (list, tuple)):
            return all(_exprs_ok(v, ctx) for v in value)
        return _expr_ok(value, ctx) if isinstance(value, str) else True

    def _atl_safe(node, ctx, depth=0):
        """True when every expression inside this ATL evaluates now, so applying it cannot raise later."""
        if depth > 12:
            return False

        if isinstance(node, _atl.RawBlock):
            return all(_atl_safe(s, ctx, depth + 1) for s in node.statements)

        if isinstance(node, _atl.RawMultipurpose):
            for name, exprs in node.properties:
                if not _exprs_ok(exprs, ctx):
                    return False
            for pair in node.expressions:
                if not _exprs_ok(pair, ctx):
                    return False
            for name, exprs in node.splines:
                if not _exprs_ok(exprs, ctx):
                    return False
            return _expr_ok(node.duration, ctx) and _expr_ok(node.circles, ctx)

        if isinstance(node, _atl.RawParallel):
            return all(_atl_safe(b, ctx, depth + 1) for b in node.blocks)

        if isinstance(node, _atl.RawChoice):
            return all(_expr_ok(c, ctx) and _atl_safe(b, ctx, depth + 1) for c, b in node.choices)

        if isinstance(node, _atl.RawOn):
            return all(_atl_safe(b, ctx, depth + 1) for b in node.handlers.values())

        if isinstance(node, _atl.RawChild):
            return all(_atl_safe(c, ctx, depth + 1) for c in node.children)

        if isinstance(node, _atl.RawRepeat):
            return _expr_ok(node.repeats, ctx)

        if isinstance(node, _atl.RawTime):
            return _expr_ok(node.time, ctx)

        if isinstance(node, _atl.RawContainsExpr):
            return _expr_ok(node.expression, ctx)

        if isinstance(node, _atl.RawFunction):
            return _expr_ok(node.expr, ctx)

        if isinstance(node, _atl.RawEvent):
            return True

        # Something this walker does not know about — refuse rather than risk a render-time crash.
        return False

    def _atl_loops(node, depth=0):
        """True when this ATL repeats forever — a preview that never settles is hard to read against."""
        if depth > 12:
            return False

        if isinstance(node, _atl.RawRepeat):
            return node.repeats is None

        for kids in (getattr(node, "statements", None), getattr(node, "blocks", None),
                     getattr(node, "children", None)):
            if kids and any(_atl_loops(k, depth + 1) for k in kids):
                return True

        if isinstance(node, _atl.RawChoice):
            return any(_atl_loops(b, depth + 1) for c, b in node.choices)

        if isinstance(node, _atl.RawOn):
            return any(_atl_loops(b, depth + 1) for b in node.handlers.values())

        return False

    def _at_transforms(at_expr):
        """(transforms to apply, number skipped as unsafe, number held still) for an `at` clause."""
        if not at_expr:
            return [], 0, 0

        out, skipped, held = [], 0, 0
        for e in _scan_split(at_expr, ","):
            if not e:
                continue
            try:
                t = renpy.python.py_eval(e)
            except Exception:
                skipped += 1
                continue

            atl = getattr(t, "atl", None)
            if atl is not None:
                ctx = getattr(getattr(t, "context", None), "context", None)
                if not _atl_safe(atl, ctx):
                    skipped += 1
                    continue
                if not renpy.store.TL_ANIMATE and _atl_loops(atl):
                    held += 1
                    continue

            out.append(t)
        return out, skipped, held

    def _apply(d, transforms):
        for t in transforms:
            try:
                if isinstance(t, renpy.display.motion.Transform):
                    d = t(child=d)
                else:
                    d = t(d)
            except Exception:
                pass
        return d

    # ------------------------------------------------------------------------------------------------
    # Image resolution
    # ------------------------------------------------------------------------------------------------

    def _image_ref(name):
        # style="image_placement" is what puts an untransformed image at the bottom centre, as `show` does.
        return renpy.display.image.ImageReference(name, style="image_placement")

    def _resolve(spec):
        """(tag, displayable) for an image name — or a live-evaluated `expression`, when that works."""
        if not spec:
            return None, None

        if spec.split(None, 1)[0] == "expression":
            if not renpy.store.TL_EVAL:
                return None, None
            try:
                v = renpy.python.py_eval(spec.split(None, 1)[1])
            except Exception:
                return None, None
            if isinstance(v, str):
                return v.split()[0], _image_ref(tuple(v.split()))
            try:
                return None, renpy.easy.displayable(v)
            except Exception:
                return None, None

        parts = spec.split()
        tag = parts[0]
        while parts:
            if renpy.has_image(tuple(parts), exact=True):
                return tag, _image_ref(tuple(parts))
            parts = parts[:-1]
        return tag, None

    # ------------------------------------------------------------------------------------------------
    # The scan
    # ------------------------------------------------------------------------------------------------

    def stage_for(entry):
        """Displayables, bottom to top, that best represent the shot this line is spoken over."""
        if entry is None:
            return []

        key = (entry.src, entry.line)
        if key in _stage_cache:
            return _stage_cache[key]

        out = []
        skipped = held = 0
        try:
            f = open(entry.src, "r", encoding="utf-8", errors="replace")
            try:
                src = f.read().split("\n")
            finally:
                f.close()

            end = max(0, min(entry.line, len(src)) - 1)

            # Walk back to the last `scene` — everything before it was wiped off the stage anyway.
            top = 0
            for i in range(end, -1, -1):
                m = STMT.match(src[i])
                if m and m.group(1) == "scene":
                    top = i
                    break

            layers = []     # (tag, displayable), in draw order
            for i in range(top, end + 1):
                m = STMT.match(src[i])
                if not m:
                    continue

                kind = m.group(1)
                cl = _clauses(m.group(2))
                tag, d = _resolve(cl.get(None))
                tag = cl.get("as") or tag

                if d is not None:
                    transforms, miss, hold = _at_transforms(cl.get("at"))
                    skipped += miss
                    held += hold
                    d = _apply(d, transforms)

                if kind == "scene":
                    layers = []
                    if d is not None:
                        layers.append((tag, d))
                elif kind == "show":
                    layers = [x for x in layers if x[0] is None or x[0] != tag]
                    if d is not None:
                        layers.append((tag, d))
                elif kind == "hide":
                    layers = [x for x in layers if x[0] != tag]

            out = [d for t, d in layers]

        except Exception as err:
            _stage_error[key] = "%s: %s" % (type(err).__name__, err)
            out = []

        _stage_cache[key] = out
        _stage_skip[key] = skipped
        _stage_held[key] = held
        return out

    def stage_summary(entry):
        """One line for the UI, so the translator knows whether to trust what they are looking at."""
        if entry is None:
            return ""

        n = len(stage_for(entry))
        key = (entry.src, entry.line)

        err = _stage_error.get(key)
        if err:
            return renpy.translate_string("stage rebuild failed - ") + err
        if not n:
            return "no image found for this line"

        rv = renpy.translate_string("%d layer%s reconstructed") % (n, "" if n == 1 or renpy.game.preferences.language == "zh" else "s")
        skipped = _stage_skip.get(key) or 0
        if skipped:
            rv += renpy.translate_string(", %d transform%s skipped") % (skipped, "" if skipped == 1 or renpy.game.preferences.language == "zh" else "s")
        held = _stage_held.get(key) or 0
        if held:
            rv += renpy.translate_string(", %d held still") % held
        return rv

