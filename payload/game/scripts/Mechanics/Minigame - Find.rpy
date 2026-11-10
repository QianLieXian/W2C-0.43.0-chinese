init python:
    from collections import Counter as _FindCounter

    _FIND_DIR_COMPONENTS = {
        "any":         ("any",),
        "front":       ("front",),
        "back":        ("back",),
        "left":        ("left",),
        "right":       ("right",),
        "front_left":  ("front", "left"),
        "front_right": ("front", "right"),
        "back_left":   ("back", "left"),
        "back_right":  ("back", "right"),
    }

    def _find_char_path(char_id, wear):
        suffix = ("_" + wear) if wear else ""
        return "images/Mechanics/Figures/char/char_{:02d}{}.webp".format(char_id, suffix)

    def _find_pick_wear(mark_wear):
        if not mark_wear:
            return ""
        if len(mark_wear) == 1:
            return mark_wear[0]
        return renpy.random.choice(list(mark_wear))

    def _find_split_direction(d):
        # Returns (fb, lr) where fb is "front"/"back"/"any"/None and lr is "left"/"right"/None.
        comps = _FIND_DIR_COMPONENTS.get(d, (d,))
        fb = None
        lr = None
        for c in comps:
            if c == "any":
                return ("any", None)
            if c in ("front", "back"):
                fb = c
            elif c in ("left", "right"):
                lr = c
        return (fb, lr)

    def _find_pose_match(char_pose, char_look, mark_direction_list):
        # Prefer a no-flip match across any listed direction; fall back to
        # flipping when the only compatible direction requires a mirror.
        flip_option = None
        for d in mark_direction_list:
            fb, lr = _find_split_direction(d)
            if fb == "any":
                # Any-direction marks randomize flip for visual variety.
                return (True, renpy.random.random() < 0.5)

            # Side-only direction ("left"/"right"): pose must be the matching
            # side, or the opposite side (mirrored).
            if fb is None and lr is not None:
                if char_pose == lr:
                    return (True, False)
                if (lr == "left" and char_pose == "right") or (lr == "right" and char_pose == "left"):
                    if flip_option is None:
                        flip_option = (True, True)
                continue

            # Front/back (possibly diagonal): pose must match the front/back part.
            if char_pose != fb:
                continue

            if lr is None:
                # Pure "front" or "back" — pose match, no side preference.
                return (True, False)

            # Diagonal: use the char's look direction to decide the side.
            if char_look == lr:
                return (True, False)
            if char_look in ("left", "right"):
                if flip_option is None:
                    flip_option = (True, True)
                continue
            # char_look is not horizontal (front/back/down) — sprite has no
            # clear side bias, so accept without flipping.
            return (True, False)

        if flip_option is not None:
            return flip_option
        return (False, False)

    def _find_act_match(char_acts, mark_actions):
        for a in char_acts:
            if a in mark_actions:
                return True
        return False

    def _find_compat(char_data, mark):
        if not _find_act_match(char_data.get("act", []), mark.get("action", [])):
            return None
        ok, flip = _find_pose_match(
            char_data.get("pose", "front"),
            char_data.get("look", "front"),
            mark.get("direction", ["any"]),
        )
        if not ok:
            return None
        wear = _find_pick_wear(mark.get("wear", []))
        return (flip, wear)

    def _find_partner_flip(char_look, current_mark, partner_mark, base_flip):
        if char_look not in ("left", "right"):
            return base_flip
        partner_side = "right" if partner_mark["X"] >= current_mark["X"] else "left"
        effective_look = char_look
        if base_flip:
            effective_look = "left" if char_look == "right" else "right"
        if effective_look != partner_side:
            return not base_flip
        return base_flip

    def _find_parse_map(map_name):
        parts = map_name.rsplit("_", 1)
        if len(parts) == 2 and parts[1].isdigit():
            return parts[0], int(parts[1]) / 100.0
        return map_name, 0.15

    def _find_get_map_data(map_name):
        return getattr(store, "Map_{}_Data".format(map_name), {})

    def _find_map_max(map_name):
        # Maximum simultaneous characters a map supports = number of "mark_*"
        # placement slots defined in its Map_..._Data dict.
        return sum(1 for n in _find_get_map_data(map_name) if n.startswith("mark_"))

    def _find_generate_layout(map_name, char_count):
        map_data = _find_get_map_data(map_name)
        if not map_data:
            return ([], 0)

        fig = dict(getattr(store, "Figure_Data", {}))

        char_ids_by_chat = {0: [], 1: [], 2: []}
        char_id_to_name = {}
        for name, data in fig.items():
            try:
                cid = int(name.split("_")[1])
            except (IndexError, ValueError):
                continue
            char_id_to_name[cid] = name
            chat = data.get("chat", 2)
            char_ids_by_chat.setdefault(chat, []).append(cid)

        for v in char_ids_by_chat.values():
            renpy.random.shuffle(v)

        mark_names = [n for n in map_data.keys() if n.startswith("mark_")]
        renpy.random.shuffle(mark_names)

        occupied = {}
        used_counts = _FindCounter()
        partners_needed = []

        def place(mark_name, cid, wear, flip):
            m = map_data[mark_name]
            occupied[mark_name] = (m["X"], m["Y"], cid, wear, flip)
            used_counts[cid] += 1

        def pick_char(chat_val, mark, allow_reuse=False):
            candidates = list(char_ids_by_chat.get(chat_val, []))
            if not allow_reuse:
                candidates = [c for c in candidates if used_counts[c] == 0]
            renpy.random.shuffle(candidates)
            if allow_reuse:
                candidates.sort(key=lambda c: used_counts[c])
            for cid in candidates:
                data = fig.get(char_id_to_name.get(cid, ""))
                if not data:
                    continue
                result = _find_compat(data, mark)
                if result is not None:
                    flip, wear = result
                    return (cid, flip, wear)
            return None

        # Phase A: chat=1 on linked marks
        linked_marks = [n for n in mark_names if map_data[n].get("link")]
        for mname in linked_marks:
            if len(occupied) >= char_count:
                break
            if mname in occupied:
                continue
            picked = pick_char(1, map_data[mname])
            if picked is None:
                continue
            cid, flip, wear = picked
            place(mname, cid, wear, flip)
            partner = map_data[mname]["link"]
            partners_needed[:] = [p for p in partners_needed if p[0] != mname]
            if partner not in occupied and not any(p[0] == partner for p in partners_needed):
                partners_needed.append((partner, mname))

        # Phase B: chat=0 on any compatible mark (prefer non-linked, avoid reserved)
        def empty_marks_sorted():
            empty = [n for n in mark_names if n not in occupied]
            reserved = set(p[0] for p in partners_needed)
            non_linked = [n for n in empty if not map_data[n].get("link") and n not in reserved]
            linked_free = [n for n in empty if map_data[n].get("link") and n not in reserved]
            reserved_list = [n for n in empty if n in reserved]
            return non_linked + linked_free + reserved_list

        for cid in list(char_ids_by_chat.get(0, [])):
            if len(occupied) >= char_count:
                break
            if used_counts[cid] > 0:
                continue
            data = fig.get(char_id_to_name.get(cid, ""))
            if not data:
                continue
            for mname in empty_marks_sorted():
                if mname in occupied:
                    continue
                result = _find_compat(data, map_data[mname])
                if result is not None:
                    flip, wear = result
                    place(mname, cid, wear, flip)
                    partners_needed[:] = [p for p in partners_needed if p[0] != mname]
                    break

        # Phase C1: chat=2 fills partner slots for lonely chat=1 anchors
        for partner_mname, anchor_mname in list(partners_needed):
            if len(occupied) >= char_count:
                break
            if partner_mname in occupied:
                continue
            mark = map_data[partner_mname]
            picked = pick_char(2, mark)
            if picked is None:
                continue
            cid, flip, wear = picked
            data = fig.get(char_id_to_name.get(cid, ""), {})
            flip = _find_partner_flip(data.get("look", "front"), mark, map_data[anchor_mname], flip)
            place(partner_mname, cid, wear, flip)

        # Phase C2: chat=2 fills remaining empty marks
        for cid in list(char_ids_by_chat.get(2, [])):
            if len(occupied) >= char_count:
                break
            if used_counts[cid] > 0:
                continue
            data = fig.get(char_id_to_name.get(cid, ""))
            if not data:
                continue
            for mname in mark_names:
                if mname in occupied:
                    continue
                result = _find_compat(data, map_data[mname])
                if result is not None:
                    flip, wear = result
                    place(mname, cid, wear, flip)
                    break

        # Reserve a target char from those placed exactly once. Phase D
        # will refuse to duplicate it, guaranteeing the player has an
        # unambiguous click target. Pick uniformly among count==1 chars so
        # the target is fair; fall back to the least-placed char if every
        # placed char already has duplicates (unlikely, but safe).
        placed_cids = [c for c in used_counts if used_counts[c] > 0]
        unique_cids = [c for c in placed_cids if used_counts[c] == 1]
        if unique_cids:
            target_cid = renpy.random.choice(unique_cids)
        elif placed_cids:
            min_count = min(used_counts[c] for c in placed_cids)
            target_cid = renpy.random.choice(
                [c for c in placed_cids if used_counts[c] == min_count]
            )
        else:
            target_cid = None

        # Phase D: reuse pool until var_cnt reached or no progress.
        # Pick least-used char globally across all chat types so the pool
        # stays balanced — but exclude target_cid so it stays unique.
        reusable = []
        for cv in (0, 1, 2):
            reusable.extend(c for c in char_ids_by_chat.get(cv, []) if c != target_cid)
        while len(occupied) < char_count:
            empty = [n for n in mark_names if n not in occupied]
            if not empty:
                break
            renpy.random.shuffle(empty)
            progress = False
            for mname in empty:
                if len(occupied) >= char_count:
                    break
                renpy.random.shuffle(reusable)
                reusable.sort(key=lambda c: used_counts[c])
                for cid in reusable:
                    data = fig.get(char_id_to_name.get(cid, ""))
                    if not data:
                        continue
                    result = _find_compat(data, map_data[mname])
                    if result is not None:
                        flip, wear = result
                        place(mname, cid, wear, flip)
                        progress = True
                        break
            if not progress:
                break

        placed = [occupied[n] for n in mark_names if n in occupied]
        if target_cid is not None:
            target_idx = next(
                (i for i, p in enumerate(placed) if p[2] == target_cid), 0
            )
        else:
            target_idx = 0
        return placed, target_idx

    def _find_new_round(map_name, char_count):
        placed, target_idx = _find_generate_layout(map_name, char_count)
        if not placed:
            return ([(960, 540, 1, "", False)], 0)
        return (placed, target_idx)

#---------------------------------------------------------------------------
screen minigame_find(var_map="School_005", var_cnt=20, var_tio=0, var_tim=None, var_txt=None, var_mod="classic", var_sco=0, var_sca=5):
#---------------------------------------------------------------------------
    default game_started = False
    default click_ready = False
    default score = var_sco * 1.0
    default timer_current = var_tio
    # effective_cnt scales up in continuous mode (each completed round adds
    # var_sca, capped at the map's mark_* count).
    default effective_cnt = var_cnt
    default round_data = _find_new_round(var_map, effective_cnt)
    default effective_tim = (15 if (var_mod == "continuous" and var_tim is None) else var_tim)

    $ char_zoom = _find_parse_map(var_map)[1]
    $ char_scaled = int(1080 * char_zoom)
    $ positions = round_data[0]
    $ target_idx = round_data[1]
    $ target_pos = positions[target_idx]
    $ target_char_id = target_pos[2]
    $ target_wear = target_pos[3]
    $ target_flip = target_pos[4]
    $ target_path = _find_char_path(target_char_id, target_wear)
    $ target_xzoom = -1.0 if target_flip else 1.0

    # --------------------------------------------------
    # Preparation Screen
    # --------------------------------------------------
    if not game_started:
        add "images/Mechanics/Figures/Map_{}.webp".format(var_map)

        frame:
            background "#000000C8"
            xysize (1920, 1080)
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                label renpy.translate_string("{size=+80}{b}Find{/b}{/size}") xalign 0.5
                vbox:
                    xalign 0.5
                    xysize (960, 400)
                    if var_txt == None:
                        if var_mod == "continuous":
                            text renpy.translate_string("{size=+10}Find the highlighted character in the scene! Each correct find scores a point. Wrong clicks lose half a point. Find as many as you can before time runs out!{/size}") xalign 0.5
                        else:
                            text renpy.translate_string("{size=+10}Find the highlighted character in the scene! Click on them to score. Be careful — clicking the wrong spot will cost you!{/size}") xalign 0.5
                    else:
                        text renpy.translate_string("{size=+10}[var_txt]{/size}") xalign 0.5
                text renpy.translate_string("[C_Dat]{size=+40}{b}Click to start!{/b}[C_Off]") xalign 0.5

        key "mousedown_1" action [SetScreenVariable("game_started", True), SetScreenVariable("click_ready", False)]

    # --------------------------------------------------
    # Game Started
    # --------------------------------------------------
    else:
        if not click_ready:
            timer 1.0 action SetScreenVariable("click_ready", True)

        if effective_tim != None and click_ready:
            timer 1 repeat True action [
                If(timer_current < effective_tim,
                    true=(SetScreenVariable("timer_current", timer_current + 1)),
                    false=(Return(score)),
                )
            ]

        # Background
        add "images/Mechanics/Figures/Map_{}.webp".format(var_map)

        # Character sprites (sorted by Y so lower characters appear in front)
        for pos_data in sorted(positions, key=lambda p: p[1]):
            $ p_cx = pos_data[0]
            $ p_cy = pos_data[1]
            $ p_id = pos_data[2]
            $ p_wear = pos_data[3]
            $ p_flip = pos_data[4]
            $ p_path = _find_char_path(p_id, p_wear)
            $ p_xzoom = -1.0 if p_flip else 1.0
            add p_path:
                zoom char_zoom
                xzoom p_xzoom
                anchor (0.5, 1.0)
                pos (p_cx, p_cy)

        if click_ready:
            # Miss catcher
            if var_mod == "classic":
                button:
                    xysize (1920, 1080)
                    pos (0, 0)
                    background None
                    hover_background None
                    action Return(score - 0.5)
            else:
                button:
                    xysize (1920, 1080)
                    pos (0, 0)
                    background None
                    hover_background None
                    action [
                        Play("SE2", "BeepWrong.ogg"),
                        SetScreenVariable("score", score - 0.5),
                    ]

            # Target hotspot (bottom-center anchored)
            $ hit_pad = 25
            $ hit_w = char_scaled + hit_pad * 2
            $ hit_h = char_scaled + hit_pad * 2
            $ hit_x = target_pos[0] - char_scaled // 2 - hit_pad
            $ hit_y = target_pos[1] - char_scaled - hit_pad

            if var_mod == "classic":
                button:
                    xysize (hit_w, hit_h)
                    pos (hit_x, hit_y)
                    background None
                    hover_background None
                    action Return(score + 1)
            else:
                # Each correct find: +0.5 score and bump effective_cnt by
                # var_sca (capped at the map's max), then regenerate the layout.
                $ _find_next_cnt = min(_find_map_max(var_map), effective_cnt + var_sca)
                button:
                    xysize (hit_w, hit_h)
                    pos (hit_x, hit_y)
                    background None
                    hover_background None
                    action [
                        Play("SE2", "JingleRight.ogg"),
                        SetScreenVariable("score", score + 0.5),
                        SetScreenVariable("effective_cnt", _find_next_cnt),
                        SetScreenVariable("round_data", _find_new_round(var_map, _find_next_cnt)),
                    ]

        # --------------------------------------------------
        # UI Display
        # --------------------------------------------------
        frame:
            background "#000000C8"
            padding (10, 10) xysize (220, 400) xalign 0.0 yalign 0.0 xoffset 10 yoffset 10

            hbox:
                xalign 0.5 yalign 0.0 spacing 0

                if effective_tim != None:
                    vbar value timer_current range effective_tim ymaximum 380 xoffset 160 yalign 0.5

                vbox:
                    xalign 0.0 spacing 5
                    text renpy.translate_string("{b}Find:{/b}") xalign 0.5

                    add target_path:
                        zoom 0.25
                        xzoom target_xzoom
                        xalign 0.5

                    if var_mod == "continuous":
                        text renpy.translate_string("{b}Score:{/b} [score]") xalign 0.5

    modal True
