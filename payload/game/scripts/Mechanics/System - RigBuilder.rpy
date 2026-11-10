# System - RigBuilder.rpy
# ----------------------------------------------------------------------------------------------------
# RIG BUILDER  —  moment composer + FK rig animation engine, plus a test-only visual authoring tool (see "Plan - Moment Composer.md").
# ----------------------------------------------------------------------------------------------------
# ENGINE: one data-driven system — ordered layers (explicit z, INDEPENDENT of the hierarchy so bones can interleave by depth) + a bone hierarchy + Forward-Kinematics rotation + optional damped-spring secondary motion.
#
# A "moment" is defined in Rig_Moments as an ordered list of bones, each a 4-tuple:
#     (name, parent, pivot, z)
#   - name   : short bone name; full image tag = prefix + name  (+ " <n>" for the face bone).
#   - parent : bone whose rotation this bone inherits (Forward Kinematics). None = root.
#   - pivot  : (X, Y) absolute rotation anchor on the 1920x1080 stage. None = static (no own rotation, but still inherits its parent's rotation).
#   - z      : draw order, INDEPENDENT of parent, so bones from different branches can interleave.
# Each bone's image is a full-canvas 1920x1080 layer; most parts are drawn in place (transparent elsewhere). A part authored off-position can be nudged by an optional per-bone start offset in the moment's "offsets" map (X,Y from the image top-left), applied BEFORE rotation. Pivots are absolute canvas pixels.
#
# Rendering: every bone is a full-canvas part already in place; we only rotate it about its pivot. Each bone's FK chain (its own rotation-about-pivot plus every ancestor's) is FLATTENED to ONE net rotation (2D angles add) + a folded translation, then realized with a SINGLE Transform: anchor = own_pivot, pos = translation + R(phi).own_pivot, transform_anchor=True, rotate=phi. A lone bone reduces to Transform(anchor=pivot, pos=pivot, rotate=angle) -- the proven primitive. Flattening (no stacked/nested Transforms) avoids the placement+pivot corruption that stacking two anchored Transforms causes, and uses no (I-R)^-1 division so it is numerically stable. Bones stay independent in z order.
#
# TOOL: the Rig Builder screen (test-only, reached from a bedroom action button when is_test) lets you pick a part, DRAG it to set its start offset, CLICK to set its pivot, fine-nudge both, test rotation and a demo animation, and EXPORT the resulting offsets/pivots as code.
#
# Static moment data -> `define` (save-safe; see the renpy-builder skill). Pose/geometry-edit state is transient runtime data, never serialized into saves.

define Rig_Moments = {
    "wmom_yoga3": {
        "prefix": "wmom_yoga3_",
        "bones": [
            # name          parent      pivot          z
            ("bg",          None,       None,          0),
            ("wmombg",      None,       (943, 505),    10),
            ("wmombgc",     "wmombg",   None,          17),
            ("wmombgl",     "wmombg",   (925, 325),    15),
            ("wmombgr",     "wmombg",   (925, 325),    16),
            ("wmom_lleg",   "wmombg",   (722, 401),    20),
            ("wmom_rleg",   "wmombg",   (1102, 275),   21),
            ("wmommg",      None,       None,          12),
            ("wmom_ltit",   "wmommg",   (730, 539),    18),
            ("wmom_rtit",   "wmommg",   (1129, 454),   19),
            ("wmomfg",      None,       (974, 783),    30),
            ("wmomface",    "wmomfg",   None,          31),
        ],
        "face_bone": "wmomface",          # this bone's image takes an expression number attribute
        "faces": {"good": 1, "hurt": 2, "pain": 3},
        "springy": ["wmombgl", "wmombgr", "wmom_ltit", "wmom_rtit"],  # secondary-motion (jiggle) bones
        "offsets": {                       # per-bone start-position shift (image top-left), applied before rotation
            "wmom_lleg": (-858, -118),
            "wmom_rleg": (796, -218),
        },
    },
}

init python:
    import math as _math
    import os as _os

    def build_rig(moment_id, pose, face=1, pivots=None, offsets=None):
        # Compose a moment: draw every bone in z order. Each part is a full-canvas image ALREADY in place; we only ROTATE it about its pivot (never reposition), after an optional start offset.
        #   pose : dict bone_name -> angle in degrees (missing = 0).
        #   face : expression number for the moment's face_bone.
        #   pivots/offsets : optional {bone: (x, y)} overrides used by the Rig Builder; None = data.
        data = Rig_Moments[moment_id]
        prefix = data["prefix"]
        idx = {b[0]: b for b in data["bones"]}
        if offsets is None:
            offsets = data.get("offsets", {})
        ordered = sorted(data["bones"], key=lambda b: b[3])

        layers = []
        for (name, parent, pivot, z) in ordered:
            if name == data.get("face_bone"):
                img = "%s%s %d" % (prefix, name, int(face))
            else:
                img = "%s%s" % (prefix, name)
            disp = renpy.displayable(img)

            # Optional start-position shift: BAKE it by compositing the part at (ox,oy) into a clean full-canvas frame, so the part is an ordinary in-place layer and pivots stay absolute.
            ox, oy = offsets.get(name, (0, 0))
            if ox != 0 or oy != 0:
                disp = Composite((1920, 1080), (int(ox), int(oy)), disp)

            # FK chain pivots affecting this bone: own (innermost) first, then ancestors up to root.
            ops = []
            cur = name
            while cur is not None:
                cb = idx[cur]
                if cb[2] is not None:
                    piv = pivots[cur] if (pivots is not None and cur in pivots) else cb[2]
                    ops.append((piv, float(pose.get(cur, 0.0))))
                cur = cb[1]

            if ops:
                # Flatten the whole chain to ONE rotation: net angle phi (2D rotations add) + folded translation (tx,ty). Fold W = L_op . W with b_new = R(ang).b_old + (P - R(ang).P).
                phi = 0.0
                tx = 0.0
                ty = 0.0
                for (piv, ang) in ops:
                    phi += ang
                    th = _math.radians(ang)
                    c = _math.cos(th)
                    s = _math.sin(th)
                    px = float(piv[0])
                    py = float(piv[1])
                    lbx = px - (c * px - s * py)
                    lby = py - (s * px + c * py)
                    tx, ty = (c * tx - s * ty + lbx, s * tx + c * ty + lby)
                # Realize that affine with the PROVEN single primitive (no transform stacking, no division -> stable): rotate phi about the bone's own pivot (anchor), and place that anchor at pos = translation + R(phi).own_pivot. A lone bone -> pos == own_pivot.
                own = ops[0][0]
                thf = _math.radians(phi)
                cf = _math.cos(thf)
                sf = _math.sin(thf)
                posx = tx + (cf * own[0] - sf * own[1])
                posy = ty + (sf * own[0] + cf * own[1])
                # IMPORTANT: Ren'Py reads a FLOAT position as a fraction of the parent and an INT as pixels. anchor/pos MUST be ints (absolute pixels) or the part flies far off-screen.
                disp = Transform(child=disp,
                                 anchor=(int(round(own[0])), int(round(own[1]))),
                                 pos=(int(round(posx)), int(round(posy))),
                                 transform_anchor=True, rotate=phi)

            layers.append(disp)

        return Fixed(*layers)

    def rig_spring_step(angles, vel, targets, dt=0.033, stiffness=120.0, damping=16.0):
        # Damped-spring integrate `angles` toward `targets` (mutated in place) for secondary motion.
        # `vel` holds per-bone angular velocity between frames.
        for k, tgt in targets.items():
            a = angles.get(k, 0.0)
            v = vel.get(k, 0.0)
            v += (stiffness * (tgt - a) - damping * v) * dt
            a += v * dt
            angles[k] = a
            vel[k] = v


# ====================================================================================================
# RIG BUILDER — test-only visual authoring + animation tool
# ====================================================================================================

init python:

    RB_MOMENT = "wmom_yoga3"   # moment the builder currently edits
    RB_PANEL_W = 500           # control-panel width (the stage catcher avoids this right-edge strip)

    def rig_builder_init():
        st = store
        data = Rig_Moments[RB_MOMENT]
        base_off = data.get("offsets", {})
        st.rb_t = 0.0
        st.rb_playing = False
        st.rb_face = 1
        st.rb_slider = {}     # per rotatable bone: 0..90 (neutral 45 -> angle 0)
        st.rb_angle = {}      # per rotatable bone: rendered angle (what build_rig reads)
        st.rb_vel = {}        # per rotatable bone: spring velocity
        st.rb_offsets = {}    # per bone: [x, y] start offset (live-editable copy of data)
        st.rb_pivots = {}     # per rotatable bone: [x, y] pivot (live-editable copy of data)
        for (name, parent, piv, z) in data["bones"]:
            st.rb_offsets[name] = list(base_off.get(name, (0, 0)))
            if piv is not None:
                st.rb_slider[name] = 45.0
                st.rb_angle[name] = 0.0
                st.rb_vel[name] = 0.0
                st.rb_pivots[name] = list(piv)
        st.rb_grab = None             # rotation-handle drag (animation test)
        st.rb_grab_base = 0.0
        st.rb_grab_mouse0 = 0.0
        st.rb_dbg_mode = None         # None / "move" / "pivot"
        st.rb_sel = "wmombg"          # selected bone for editing
        st.rb_dbg_active = False      # currently dragging (move mode)
        st.rb_mouse0 = (0, 0)
        st.rb_ref0 = (0, 0)
        st.rb_panel_hidden = False
        st.rb_export_text = ""

    def rb_demo_targets(t):
        # Gentle looping breathing/stretch so FK + jiggle are visible in motion.
        s = _math.sin(t * 1.4)
        s2 = _math.sin(t * 1.4 - 0.7)
        return {
            "wmombg":    3.5 * s,
            "wmomfg":    2.5 * _math.sin(t * 1.4 + 0.4),
            "wmom_lleg": 5.0 * _math.sin(t * 0.9),
            "wmom_rleg": -5.0 * _math.sin(t * 0.9),
            "wmombgl":   4.0 * s2,
            "wmombgr":   -4.0 * s2,
            "wmom_ltit": 6.0 * s2,
            "wmom_rtit": -6.0 * s2,
        }

    def _rb_rot_about(x, y, cx, cy, deg):
        # Rotate (x,y) about (cx,cy) by `deg` clockwise (matches Ren'Py's y-down rotate).
        th = _math.radians(deg)
        c = _math.cos(th); s = _math.sin(th)
        dx = x - cx; dy = y - cy
        return (cx + c * dx - s * dy, cy + s * dx + c * dy)

    def rb_pivot_screen(bone):
        # Current on-screen position of a bone's pivot = its rest pivot moved by all ANCESTOR rotations (a bone's own rotation keeps its own pivot fixed). Mirrors how build_rig composes transforms, so the marker/handle follow the joint as the parent moves.
        st = store
        idx = {b[0]: b for b in Rig_Moments[RB_MOMENT]["bones"]}
        piv = st.rb_pivots.get(bone)
        if piv is None:
            return None
        x, y = float(piv[0]), float(piv[1])
        cur = idx[bone][1]   # walk parents up to the root
        while cur is not None:
            cb = idx[cur]
            cpiv = st.rb_pivots.get(cur, cb[2])
            if cpiv is not None:
                x, y = _rb_rot_about(x, y, cpiv[0], cpiv[1], st.rb_angle.get(cur, 0.0))
            cur = cb[1]
        return (x, y)

    def rb_tick():
        # Per-frame update while the builder is open: debug drag, then rotation-handle drag, then pose.
        st = store
        data = Rig_Moments[RB_MOMENT]
        dt = 1.0 / 30.0

        # Debug: drag selected part (move) or follow mouse (pivot).
        if st.rb_dbg_active and st.rb_sel is not None:
            mx, my = renpy.get_mouse_pos()
            if st.rb_dbg_mode == "move":
                st.rb_offsets[st.rb_sel] = [int(round(st.rb_ref0[0] + (mx - st.rb_mouse0[0]))),
                                            int(round(st.rb_ref0[1] + (my - st.rb_mouse0[1])))]
            elif st.rb_dbg_mode == "pivot" and st.rb_sel in st.rb_pivots:
                st.rb_pivots[st.rb_sel] = [int(mx), int(my)]

        # Animation: rotation-handle drag (only when no debug mode is active).
        if st.rb_dbg_mode is None and st.rb_grab is not None:
            piv = rb_pivot_screen(st.rb_grab)
            if piv is not None:
                mx, my = renpy.get_mouse_pos()
                ang = _math.degrees(_math.atan2(my - piv[1], mx - piv[0]))
                st.rb_slider[st.rb_grab] = max(0.0, min(90.0, st.rb_grab_base + (ang - st.rb_grab_mouse0) + 45.0))

        if st.rb_playing:
            st.rb_t += dt
        demo = rb_demo_targets(st.rb_t) if st.rb_playing else {}

        springy = set(data.get("springy", []))
        spring_targets = {}
        for (name, parent, piv, z) in data["bones"]:
            if piv is None:
                continue
            tgt = (st.rb_slider.get(name, 45.0) - 45.0) + demo.get(name, 0.0)
            if name in springy:
                spring_targets[name] = tgt
            else:
                st.rb_angle[name] = tgt
        rig_spring_step(st.rb_angle, st.rb_vel, spring_targets, dt)

    def rb_handle_toggle(name):
        st = store
        if st.rb_grab == name:
            st.rb_grab = None
            return
        piv = rb_pivot_screen(name)
        if piv is None:
            return
        mx, my = renpy.get_mouse_pos()
        st.rb_grab = name
        st.rb_grab_base = st.rb_slider.get(name, 45.0) - 45.0
        st.rb_grab_mouse0 = _math.degrees(_math.atan2(my - piv[1], mx - piv[0]))

    def rb_select(name):
        store.rb_sel = name
        store.rb_dbg_active = False

    def rb_set_mode(mode):
        store.rb_dbg_mode = mode
        store.rb_dbg_active = False
        store.rb_grab = None
        if mode is not None:
            # Edit geometry at rest, so on-screen pivots equal canvas pivots and clicks map directly.
            store.rb_playing = False
            rb_reset_pose()

    def rb_stage_click():
        # In a debug mode, a click on the stage acts on the selected part.
        st = store
        if st.rb_dbg_mode is None or st.rb_sel is None:
            return
        if st.rb_dbg_mode == "pivot":
            if st.rb_sel in st.rb_pivots:
                mx, my = renpy.get_mouse_pos()
                st.rb_pivots[st.rb_sel] = [int(mx), int(my)]
            return
        # move: click to grab, move mouse to drag, click again to drop.
        if not st.rb_dbg_active:
            st.rb_dbg_active = True
            st.rb_mouse0 = renpy.get_mouse_pos()
            st.rb_ref0 = tuple(st.rb_offsets.get(st.rb_sel, [0, 0]))
        else:
            st.rb_dbg_active = False

    def rb_nudge(which, d):
        st = store
        if st.rb_sel is None:
            return
        if which in ("ox", "oy"):
            o = st.rb_offsets.setdefault(st.rb_sel, [0, 0])
            o[0 if which == "ox" else 1] += d
        elif which in ("px", "py") and st.rb_sel in st.rb_pivots:
            p = st.rb_pivots[st.rb_sel]
            p[0 if which == "px" else 1] += d

    def rb_reset_pose():
        st = store
        for k in list(st.rb_slider.keys()):
            st.rb_slider[k] = 45.0
            st.rb_angle[k] = 0.0
            st.rb_vel[k] = 0.0
        st.rb_grab = None
        st.rb_t = 0.0

    def rb_export():
        st = store
        data = Rig_Moments[RB_MOMENT]
        out = []
        out.append("# ---- RIG BUILDER EXPORT : %s ----" % RB_MOMENT)
        out.append('# offsets map (paste into Rig_Moments["%s"]["offsets"]):' % RB_MOMENT)
        out.append('"offsets": {')
        for (name, parent, piv, z) in data["bones"]:
            o = st.rb_offsets.get(name, [0, 0])
            ox, oy = int(round(o[0])), int(round(o[1]))
            if ox or oy:
                out.append('    "%s": (%d, %d),' % (name, ox, oy))
        out.append("},")
        out.append("")
        out.append("# pivots (update each bone tuple's pivot field):")
        for (name, parent, piv, z) in data["bones"]:
            if name in st.rb_pivots:
                p = st.rb_pivots[name]
                out.append("#   %s -> (%d, %d)" % (name, int(round(p[0])), int(round(p[1]))))
        raw = "\n".join(out)

        wrote = False
        try:
            fh = open(_os.path.join(config.basedir, "rig_builder_export.txt"), "w")
            fh.write(raw)
            fh.close()
            wrote = True
        except Exception as e:
            raw += "\n# (file write failed: %s)" % e

        st.rb_export_text = raw.replace("{", "{{").replace("[", "[[")   # escape for safe on-screen display
        renpy.log(raw)
        renpy.notify(renpy.translate_string("Exported to rig_builder_export.txt") if wrote else renpy.translate_string("Export done (file write failed; see log)"))


screen rig_builder():
    modal True

    add "#1b1b1bff"
    add build_rig(RB_MOMENT, rb_angle, rb_face, pivots=rb_pivots, offsets=rb_offsets)

    timer (1.0 / 30.0) action Function(rb_tick) repeat True

    # Debug click-catcher: covers the stage but NOT the panel strip (so panel buttons always work).
    # When the panel is hidden it covers the whole stage.
    if rb_dbg_mode is not None:
        button:
            xpos 0
            ypos 0
            xysize ((1920, 1080) if rb_panel_hidden else (1920 - RB_PANEL_W - 24, 1080))
            background None
            action Function(rb_stage_click)

    # Green pivot marker for the selected bone — follows the joint as ancestors rotate.
    if rb_sel in rb_pivots:
        add Solid("#33ff33") xysize (16, 16) xpos int(rb_pivot_screen(rb_sel)[0]) ypos int(rb_pivot_screen(rb_sel)[1]) anchor (0.5, 0.5)

    # Rotation handle for the SELECTED bone only (animate mode) — keeps the stage uncluttered.
    if rb_dbg_mode is None and rb_sel in rb_pivots:
        button:
            xpos int(rb_pivot_screen(rb_sel)[0])
            ypos int(rb_pivot_screen(rb_sel)[1])
            xanchor 0.5
            yanchor 0.5
            xysize (36, 36)
            background ("#ff5050e0" if rb_grab == rb_sel else "#46a0ffe0")
            action Function(rb_handle_toggle, rb_sel)

    # Show-panel button when the panel is hidden.
    if rb_panel_hidden:
        textbutton renpy.translate_string("◂ Panel"):
            xalign 1.0
            yalign 0.0
            xmargin 10
            ymargin 10
            text_size 18
            action SetVariable("rb_panel_hidden", False)

    # ---- Control panel ----
    if not rb_panel_hidden:
        frame:
            xalign 1.0
            yalign 0.0
            xmargin 8
            ymargin 8
            xpadding 14
            ypadding 12
            background "#000000e0"
            xsize RB_PANEL_W
            ysize 1062

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                xfill True

                vbox:
                    spacing 8
                    xfill True

                    hbox:
                        xfill True
                        text renpy.translate_string("RIG BUILDER") size 22 yalign 0.5
                        textbutton renpy.translate_string("Hide ▸") xalign 1.0 text_size 14 action SetVariable("rb_panel_hidden", True)

                    text renpy.translate_string("Selected: [rb_sel]") size 16 color "#ffcc55"

                    # --- Part picker ---
                    vpgrid:
                        cols 2
                        spacing 6
                        for _b in Rig_Moments[RB_MOMENT]["bones"]:
                            textbutton renpy.translate_string("[_b[0]]"):
                                xysize (222, 36)
                                text_size 14
                                background ("#7a5d00" if rb_sel == _b[0] else "#2e2e2e")
                                action Function(rb_select, _b[0])

                    null height 4

                    # --- Setup mode ---
                    text renpy.translate_string("— SETUP —") size 16 color "#ffcc55"
                    hbox:
                        spacing 6
                        textbutton renpy.translate_string("Move part") xysize (150, 38) text_size 15 background ("#7a5d00" if rb_dbg_mode == "move" else "#2e2e2e") action Function(rb_set_mode, "move")
                        textbutton renpy.translate_string("Set pivot") xysize (150, 38) text_size 15 background ("#7a5d00" if rb_dbg_mode == "pivot" else "#2e2e2e") action Function(rb_set_mode, "pivot")
                        textbutton renpy.translate_string("Off") xysize (90, 38) text_size 15 background ("#7a5d00" if rb_dbg_mode is None else "#2e2e2e") action Function(rb_set_mode, None)
                    if rb_dbg_mode == "move":
                        text renpy.translate_string("Click the stage to grab the part, move the mouse, click again to drop.") size 12 color "#aaaaaa"
                    elif rb_dbg_mode == "pivot":
                        text renpy.translate_string("Click the stage to place the selected part's pivot (green dot).") size 12 color "#aaaaaa"

                    text renpy.translate_string("offset:  [rb_offsets[rb_sel][0]], [rb_offsets[rb_sel][1]]") size 15
                    hbox:
                        spacing 6
                        textbutton renpy.translate_string("X −10") xysize (74, 34) text_size 14 action Function(rb_nudge, "ox", -10)
                        textbutton renpy.translate_string("X −1") xysize (66, 34) text_size 14 action Function(rb_nudge, "ox", -1)
                        textbutton renpy.translate_string("X +1") xysize (66, 34) text_size 14 action Function(rb_nudge, "ox", 1)
                        textbutton renpy.translate_string("X +10") xysize (74, 34) text_size 14 action Function(rb_nudge, "ox", 10)
                    hbox:
                        spacing 6
                        textbutton renpy.translate_string("Y −10") xysize (74, 34) text_size 14 action Function(rb_nudge, "oy", -10)
                        textbutton renpy.translate_string("Y −1") xysize (66, 34) text_size 14 action Function(rb_nudge, "oy", -1)
                        textbutton renpy.translate_string("Y +1") xysize (66, 34) text_size 14 action Function(rb_nudge, "oy", 1)
                        textbutton renpy.translate_string("Y +10") xysize (74, 34) text_size 14 action Function(rb_nudge, "oy", 10)

                    if rb_sel in rb_pivots:
                        text renpy.translate_string("pivot:  [rb_pivots[rb_sel][0]], [rb_pivots[rb_sel][1]]") size 15
                        hbox:
                            spacing 6
                            textbutton renpy.translate_string("X −10") xysize (74, 34) text_size 14 action Function(rb_nudge, "px", -10)
                            textbutton renpy.translate_string("X −1") xysize (66, 34) text_size 14 action Function(rb_nudge, "px", -1)
                            textbutton renpy.translate_string("X +1") xysize (66, 34) text_size 14 action Function(rb_nudge, "px", 1)
                            textbutton renpy.translate_string("X +10") xysize (74, 34) text_size 14 action Function(rb_nudge, "px", 10)
                        hbox:
                            spacing 6
                            textbutton renpy.translate_string("Y −10") xysize (74, 34) text_size 14 action Function(rb_nudge, "py", -10)
                            textbutton renpy.translate_string("Y −1") xysize (66, 34) text_size 14 action Function(rb_nudge, "py", -1)
                            textbutton renpy.translate_string("Y +1") xysize (66, 34) text_size 14 action Function(rb_nudge, "py", 1)
                            textbutton renpy.translate_string("Y +10") xysize (74, 34) text_size 14 action Function(rb_nudge, "py", 10)

                    textbutton renpy.translate_string("■ EXPORT CODE → rig_builder_export.txt") xysize (470, 40) text_size 15 background "#244a24" action Function(rb_export)
                    if rb_export_text:
                        frame:
                            xfill True
                            ysize 180
                            background "#111111"
                            viewport:
                                scrollbars "vertical"
                                mousewheel True
                                text rb_export_text size 12

                    null height 6

                    # --- Animation test ---
                    text renpy.translate_string("— ANIMATE —") size 16 color "#55ccff"
                    text renpy.translate_string("Blue dot = rotation handle for the selected part (SETUP must be Off).") size 12 color "#aaaaaa"
                    hbox:
                        spacing 8
                        textbutton ("⏸ Pause" if rb_playing else "▶ Play demo") xysize (150, 38) text_size 15 action ToggleVariable("rb_playing")
                        textbutton renpy.translate_string("Reset pose") xysize (150, 38) text_size 15 action Function(rb_reset_pose)
                    hbox:
                        spacing 8
                        text renpy.translate_string("Face:") size 15 yalign 0.5
                        textbutton renpy.translate_string("good") xysize (90, 34) text_size 14 background ("#7a5d00" if rb_face == 1 else "#2e2e2e") action SetVariable("rb_face", 1)
                        textbutton renpy.translate_string("hurt") xysize (90, 34) text_size 14 background ("#7a5d00" if rb_face == 2 else "#2e2e2e") action SetVariable("rb_face", 2)
                        textbutton renpy.translate_string("pain") xysize (90, 34) text_size 14 background ("#7a5d00" if rb_face == 3 else "#2e2e2e") action SetVariable("rb_face", 3)
                    for _b in Rig_Moments[RB_MOMENT]["bones"]:
                        if _b[2] is not None:
                            hbox:
                                spacing 8
                                text renpy.translate_string("[_b[0]]") size 13 yalign 0.5 xsize 130
                                bar value DictValue(rb_slider, _b[0], 90) xsize 300 yalign 0.5

                    null height 8
                    textbutton renpy.translate_string("✖ Close") xysize (160, 42) text_size 17 background "#4a2424" action Return()


# Entry point — called from the test-only bedroom action button (UI.rpy), gated by is_test.
label rig_builder:
    $ rig_builder_init()
    call screen rig_builder
    return
