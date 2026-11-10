# ==================================================
# Crafting Orchestrator
# Generic multi-crafter, multi-recipe organizer that dispatches sub-minigames
# (Balance, Sequence, Precision, ThugOfWar) for individual recipe steps.
#
# Public API: `call minigame_crafting(var_typ=..., var_rrc=[...], ...)`
#   Returns (completed_recipe_ids, qualities) via _return.
# ==================================================

init python:

    # --------------------------------------------------
    # Recipe / step lookup
    # --------------------------------------------------
    def _craft_get_steps(recipe_id):
        """Return the cook_steps for a recipe, or a legacy fallback assembled
        from cook_tool / cook_ingn / cook_ingo on a counter."""
        if recipe_id not in item_data:
            return []
        data = item_data[recipe_id].get("data", {})
        if "cook_steps" in data:
            return list(data["cook_steps"])
        steps = []
        for tool in data.get("cook_tool", []):
            steps.append({"id": "use_" + tool, "blk": "counter", "pre": [], "use": tool, "req": True, "cnt": 1, "mg": None})
        for ingn in data.get("cook_ingn", []):
            steps.append({"id": "add_" + ingn, "blk": "counter", "pre": [], "use": ingn, "req": True, "cnt": 1, "mg": None})
        for ingo in data.get("cook_ingo", []):
            steps.append({"id": "add_" + ingo, "blk": "counter", "pre": [], "use": ingo, "req": False, "cnt": 1, "mg": None})
        steps.append({"id": "assemble_" + recipe_id, "blk": "counter", "pre": [], "use": None, "req": True, "cnt": 1, "mg": None})
        return steps

    def _craft_step_required_field(step):
        """A step is required by default unless explicitly marked req=False."""
        return step.get("req", True)

    # --------------------------------------------------
    # Inventory adapter (works on a list of inventory ids)
    # --------------------------------------------------
    def _craft_inv_has_item(item_id, var_inv):
        for inv_name in var_inv:
            inv = getattr(store, inv_name, None)
            if inv is None:
                continue
            if CountItem_Inventory(item_id, inv) > 0:
                return True
        return False

    def _craft_inv_consume(item_id, var_inv):
        for inv_name in var_inv:
            inv = getattr(store, inv_name, None)
            if inv is None:
                continue
            it = GetItem_Inventory(item_id, inv)
            if it is not None:
                RemItem_Inventory(it, inv)
                return True
        return False

    def _craft_step_required(step, var_rrc):
        if not var_rrc:
            return False
        return any(rid in var_rrc for rid in step.get("recipes", []))

    # --------------------------------------------------
    # Active recipes & action pool
    # --------------------------------------------------
    def _craft_filter_recipes_by_type(typ):
        ids = []
        if typ == "cooking":
            for rid, rdata in item_data.items():
                d = rdata.get("data", {})
                if "cook_steps" in d or "cook_ingn" in d:
                    ids.append(rid)
        return ids

    def _craft_active_recipes(typ, rrc, arc, var_inv, var_ing):
        if rrc:
            return list(rrc)
        if arc == "any":
            candidates = _craft_filter_recipes_by_type(typ)
        else:
            candidates = list(arc)
        result = []
        for rid in candidates:
            if rid not in item_data:
                continue
            d = item_data[rid].get("data", {})
            ingn = d.get("cook_ingn", [])
            if all(_craft_inv_has_item(i, var_inv) for i in ingn):
                result.append(rid)
        return result

    def _craft_build_pool(typ, rrc, arc, var_inv, var_ing):
        recipes = _craft_active_recipes(typ, rrc, arc, var_inv, var_ing)
        pool = {}
        for rid in recipes:
            for step in _craft_get_steps(rid):
                key = step["id"]
                if key not in pool:
                    s = dict(step)
                    s["recipes"] = [rid]
                    pool[key] = s
                else:
                    if step["cnt"] > pool[key]["cnt"]:
                        pool[key]["cnt"] = step["cnt"]
                    if rid not in pool[key]["recipes"]:
                        pool[key]["recipes"].append(rid)
        return list(pool.values())

    def _craft_available_actions(pool, progress, crafter_state, var_blk, var_inv, var_rrc=None):
        result = []
        for step in pool:
            if progress.get(step["id"], 0) >= step["cnt"]:
                continue
            ok = True
            for pre_id in step["pre"]:
                pre_step = next((s for s in pool if s["id"] == pre_id), None)
                if pre_step is None or progress.get(pre_id, 0) < pre_step["cnt"]:
                    ok = False
                    break
            if not ok:
                continue
            if step.get("use") and not _craft_step_required(step, var_rrc) and not _craft_inv_has_item(step["use"], var_inv):
                continue
            if step["blk"] != "any" and step["blk"] not in var_blk:
                continue
            result.append(step)
        return result

    def _craft_available_for(crafter_id, pool, progress, crafter_state, var_blk, var_inv, var_rrc=None, excluded_step_ids=None, blocked_indices=None):
        """Available actions for a specific crafter with block-exclusivity filtering.
        blocked_indices is a set of block INDICES (not names) that are occupied."""
        result = []
        for step in pool:
            if progress.get(step["id"], 0) >= step["cnt"]:
                continue
            ok = True
            for pre_id in step["pre"]:
                pre_step = next((s for s in pool if s["id"] == pre_id), None)
                if pre_step is None or progress.get(pre_id, 0) < pre_step["cnt"]:
                    ok = False
                    break
            if not ok:
                continue
            if step.get("use") and not _craft_step_required(step, var_rrc) and not _craft_inv_has_item(step["use"], var_inv):
                continue
            if step["blk"] != "any" and step["blk"] not in var_blk:
                continue
            if excluded_step_ids and step["id"] in excluded_step_ids:
                continue
            if blocked_indices and step["blk"] != "any":
                free = any(i for i, b in enumerate(var_blk) if b == step["blk"] and i not in blocked_indices)
                if not free:
                    continue
            result.append(step)
        return result

    # --------------------------------------------------
    # State mutation
    # --------------------------------------------------
    def _craft_move_to_block(crafter_id, target_blk, crafter_state, var_blk):
        if target_blk == "any":
            return
        for i, blk in enumerate(var_blk):
            if blk == target_blk:
                crafter_state[crafter_id]["block"] = i
                return

    def _craft_apply_step(step, crafter_id, success, progress, var_inv, crafter_state, var_blk, var_rrc=None):
        _craft_move_to_block(crafter_id, step["blk"], crafter_state, var_blk)
        if step.get("use") and success and not _craft_step_required(step, var_rrc):
            _craft_inv_consume(step["use"], var_inv)
        if success:
            progress[step["id"]] = progress.get(step["id"], 0) + 1

    def _craft_recipe_done(recipe_id, progress):
        for step in _craft_get_steps(recipe_id):
            if _craft_step_required_field(step) and progress.get(step["id"], 0) < step["cnt"]:
                return False
        return True

    def _craft_recipe_quality(recipe_id, progress):
        steps = _craft_get_steps(recipe_id)
        opt_total = sum(1 for s in steps if not _craft_step_required_field(s))
        opt_done = sum(1 for s in steps if not _craft_step_required_field(s) and progress.get(s["id"], 0) >= s["cnt"])
        return 50 + int(50 * opt_done / max(1, opt_total))

    # --------------------------------------------------
    # NPC AI
    # --------------------------------------------------
    def _stats_for_minigame(mg):
        if mg is None:
            return ["phy", "int"]
        name = mg[0] if isinstance(mg, tuple) else mg
        if name in ("thugofwar", "balance"):
            return ["phy"]
        if name in ("sequence", "precision"):
            return ["int"]
        return ["phy", "int"]

    def _craft_npc_pick(npc_id, available, just_picked_id=None):
        candidates = [a for a in available if a["id"] != just_picked_id]
        if not candidates:
            return None
        def _score(action):
            return sum(stat_value(npc_id, s) for s in _stats_for_minigame(action["mg"]))
        candidates.sort(key=lambda a: (-_score(a), -a["cnt"], not _craft_step_required_field(a), renpy.random.random()))
        return candidates[0]

    def _craft_npc_resolve(npc_id, action, progress, var_inv, crafter_state, var_blk, var_rrc=None):
        if action is None:
            return
        stats = _stats_for_minigame(action["mg"])
        relevant = stat_value(npc_id, stats[0]) if stats else 0
        success = renpy.random.random() < min(0.95, 0.4 + 0.05 * relevant)
        _craft_apply_step(action, npc_id, success, progress, var_inv, crafter_state, var_blk, var_rrc)

    def _craft_npc_pass(step_id, action_pool, progress, var_inv, crafter_state, var_blk, var_crf, var_rrc=None):
        available = _craft_available_actions(action_pool, progress, crafter_state, var_blk, var_inv, var_rrc)
        for npc_id in var_crf[1:]:
            npc_pick = _craft_npc_pick(npc_id, available, step_id)
            _craft_npc_resolve(npc_id, npc_pick, progress, var_inv, crafter_state, var_blk, var_rrc)
            if npc_pick is not None:
                available = [a for a in available if a["id"] != npc_pick["id"] or progress.get(a["id"], 0) < a["cnt"]]

    def _craft_compute_npc_choices(var_crf, pool, progress, crafter_state, var_blk, var_inv, player_chosen_id, var_rrc=None):
        """Compute NPC choices for the choice turn, avoiding player's choice and each other.
        Uses block indices so that duplicate block names (e.g. two counters) stay independently available."""
        if len(var_crf) <= 1:
            return {}
        choices = {}
        claimed_indices = set()
        excluded_ids = set()
        if player_chosen_id:
            excluded_ids.add(player_chosen_id)
            player_step = next((s for s in pool if s["id"] == player_chosen_id), None)
            if player_step and player_step["blk"] != "any":
                idx = next((i for i, b in enumerate(var_blk) if b == player_step["blk"] and i not in claimed_indices), None)
                if idx is not None:
                    claimed_indices.add(idx)
        for npc_id in var_crf[1:]:
            npc_available = _craft_available_for(npc_id, pool, progress, crafter_state, var_blk, var_inv, var_rrc, excluded_step_ids=set(excluded_ids), blocked_indices=set(claimed_indices))
            npc_pick = _craft_npc_pick(npc_id, npc_available)
            choices[npc_id] = npc_pick
            if npc_pick:
                excluded_ids.add(npc_pick["id"])
                if npc_pick["blk"] != "any":
                    idx = next((i for i, b in enumerate(var_blk) if b == npc_pick["blk"] and i not in claimed_indices), None)
                    if idx is not None:
                        claimed_indices.add(idx)
        return choices

    def _craft_apply_npc_choices(npc_choices, progress, var_inv, crafter_state, var_blk, var_rrc=None):
        """Resolve pre-computed NPC choices after player finishes their action."""
        for npc_id, action in npc_choices.items():
            _craft_npc_resolve(npc_id, action, progress, var_inv, crafter_state, var_blk, var_rrc)

    def _craft_apply_mark(new_sid, var_crf, action_pool, progress, crafter_state, var_blk, var_inv, var_rrc):
        # Refresh the preview state (NPC choices + visual block positions) when
        # the player marks an action. Called from the action button so the store
        # is updated before any screen re-evaluates, eliminating the one-click
        # lag that comes from updating it inside the UI screen body.
        store._craft_npc_choices_preview = _craft_compute_npc_choices(
            var_crf, action_pool, progress, crafter_state, var_blk, var_inv, new_sid, var_rrc
        )
        store._craft_visual_blocks = _craft_visual_positions(
            var_crf, crafter_state, var_blk, new_sid, store._craft_npc_choices_preview, action_pool
        )

    # --------------------------------------------------
    # Camera math
    # --------------------------------------------------
    def _craft_bg_paths(typ, scn):
        # Background layers back-to-front: '{typ}_bg_{n}_{scn}.webp', falling back
        # to '{typ}_bg_{n}_any.webp'. Layer 0 renders behind layer 1, etc.
        # Returns list of (path, width).
        result = []
        for n in range(10):
            for candidate in (
                "images/Mechanics/Crafting/{}_bg_{}_{}.webp".format(typ, n, scn),
                "images/Mechanics/Crafting/{}_bg_{}_any.webp".format(typ, n),
            ):
                if renpy.loadable(candidate):
                    try:
                        w = renpy.image_size(candidate)[0]
                    except Exception:
                        w = 1920
                    result.append((candidate, w))
                    break
        return result

    def _craft_viewport_offset(var_blk, focal_block):
        n = len(var_blk)
        B = 640
        if n <= 3 or focal_block <= 0:
            return 0
        if focal_block >= n - 1:
            return -(n - 3) * B
        return -(focal_block - 1) * B

    def _craft_bg_x(var_blk, focal_block, bg_w):
        # Per-layer scroll offset — a layer narrower than the viewport stays put,
        # giving automatic parallax (e.g. a 1920 sky behind a wider scene).
        n = len(var_blk)
        W = 1920
        if bg_w <= W or n <= 3:
            return 0
        return -int((bg_w - W) * focal_block / max(1, n - 1))

    # --------------------------------------------------
    # Image lookup with fallbacks
    # --------------------------------------------------
    def _craft_fg_for_block(typ, scn, blk):
        candidates = [
            "images/Mechanics/Crafting/{}_fg_{}_{}.webp".format(typ, scn, blk),
            "images/Mechanics/Crafting/{}_fg_{}_{} {}.webp".format(typ, scn, blk, scn),
            "images/Mechanics/Crafting/{}_fg_any_{}.webp".format(typ, blk),
        ]
        for path in candidates:
            if renpy.loadable(path):
                return path
        return candidates[-1]

    def _craft_char_image(typ, char_id, variant=1):
        # Use the character's default sprite (e.g. "HERO", "WSIS") defined in Spriteset.rpy.
        name = char_id.upper()
        if renpy.has_image(name, exact=True):
            return name
        return None

    def _craft_oc_path(char_id):
        if char_id is None:
            return None
        for variant in [char_id.upper(), char_id]:
            path = "images/UI/OC_{}.webp".format(variant)
            if renpy.loadable(path):
                return path
        return None

    def _craft_initial_block(char_id, var_blk, typ):
        # Crafters spread across blocks at start, hero anchored to block 0.
        return 0

    def _craft_add_overlays(typ, pool, progress, var_blk):
        """Return list of (block_index, image_path) for completed steps that have an 'add' value.
        For each block, the last completed step's 'add' image wins (represents current state)."""
        result = {}
        for step in pool:
            add_val = step.get("add")
            if not add_val:
                continue
            if progress.get(step["id"], 0) <= 0:
                continue
            blk = step["blk"]
            idx = next((i for i, b in enumerate(var_blk) if b == blk), None)
            if idx is not None:
                result[idx] = "images/Mechanics/Crafting/{}_add_{}.webp".format(typ, add_val)
        return list(result.items())

    # --------------------------------------------------
    # Display formatting (human-readable labels)
    # --------------------------------------------------
    def _craft_step_label(step):
        name = step.get("name")
        if name:
            return name
        return step["id"].replace("_", " ").capitalize()

    def _craft_step_button_label(step, progress):
        name = _craft_step_label(step)
        cnt = step.get("cnt", 1)
        if cnt > 1:
            done = progress.get(step["id"], 0)
            return "{} ({}/{})".format(name, done, cnt)
        return name

    def _craft_recipe_name(recipe_id):
        if recipe_id in item_data:
            return item_data[recipe_id].get("name", recipe_id)
        return recipe_id

    def _craft_recipe_progress(recipe_id, progress):
        steps = _craft_get_steps(recipe_id)
        total = len(steps)
        done = sum(1 for s in steps if progress.get(s["id"], 0) >= s["cnt"])
        return done, total

    def _craft_step_status_line(step, progress):
        name = _craft_step_label(step)
        cnt = step.get("cnt", 1)
        done = min(cnt, progress.get(step["id"], 0))
        marker = "✔" if done >= cnt else "○"
        if cnt > 1:
            suffix = " ({}/{})".format(done, cnt)
        else:
            suffix = ""
        if not _craft_step_required_field(step):
            suffix += " (optional)"
        return "{} {}{}".format(marker, name, suffix)

    def _craft_toggle_set(s, item):
        if item in s:
            s.discard(item)
        else:
            s.add(item)

    def _craft_quality_stars(quality, max_stars=5):
        filled = int(quality / 100.0 * max_stars)
        filled = max(0, min(max_stars, filled))
        return "★" * filled + "☆" * (max_stars - filled)

    def _craft_group_by_block(actions):
        """Group actions by block, preserving first-seen order."""
        seen_blks = []
        groups = {}
        for step in actions:
            blk = step["blk"]
            if blk not in groups:
                groups[blk] = []
                seen_blks.append(blk)
            groups[blk].append(step)
        return [(b, groups[b]) for b in seen_blks]

    def _craft_action_icon_path(step_id, player_chosen_id, npc_choices_now, var_crf):
        """Return OC icon path for whichever character has claimed this action, or None."""
        if step_id == player_chosen_id:
            return _craft_oc_path(var_crf[0]) if var_crf else None
        for nid, s in npc_choices_now.items():
            if s and s["id"] == step_id:
                return _craft_oc_path(nid)
        return None

    def _craft_visual_positions(var_crf, crafter_state, var_blk, player_chosen_id, npc_choices_now, pool):
        """Compute display block indices based on current choices.
        Characters with a chosen action move to their target block;
        others stay at their current block, shuffling to avoid collisions."""
        positions = {}
        claimed = set()

        # First pass: characters with an explicit block choice
        for cid in var_crf:
            step = None
            if cid == var_crf[0]:
                if player_chosen_id:
                    step = next((s for s in pool if s["id"] == player_chosen_id), None)
            else:
                step = npc_choices_now.get(cid)
            if step and step["blk"] != "any":
                idx = next((i for i, b in enumerate(var_blk) if b == step["blk"] and i not in claimed), None)
                if idx is not None:
                    positions[cid] = idx
                    claimed.add(idx)

        # Second pass: characters with no choice — keep current block or find nearest free one
        for cid in var_crf:
            if cid in positions:
                continue
            cur = crafter_state[cid]["block"]
            if cur not in claimed:
                positions[cid] = cur
                claimed.add(cur)
            else:
                idx = next((i for i in range(len(var_blk)) if i not in claimed), cur)
                positions[cid] = idx
                claimed.add(idx)

        return positions

    # --------------------------------------------------
    # Sub-minigame parameter resolver (returns kwargs for call_screen)
    #
    # mg field on a step is one of:
    #   None                                  -> no minigame (instant resolution)
    #   ("name",)                             -> use sub-minigame's own defaults
    #   ("name", None)                        -> same as above
    #   ("name", {"var_pla": 2, "var_npc":1}) -> kwargs forwarded as-is
    #   ("name", {"var_pla": lambda c: ...})  -> callable values are invoked
    #                                            with the crafter id at runtime
    # --------------------------------------------------
    def _craft_resolve_minigame_args(step, crafter_id):
        mg = step.get("mg")
        if mg is None:
            return None, None
        mg_name = mg[0]
        raw_args = mg[1] if len(mg) > 1 else None
        if not isinstance(raw_args, dict):
            return mg_name, {}
        resolved = {}
        for k, v in raw_args.items():
            resolved[k] = v(crafter_id) if callable(v) else v
        return mg_name, resolved

    def _craft_minigame_success(mg_name, result):
        if mg_name == "thugofwar":
            return (result == "Win") or (isinstance(result, (int, float)) and result > 0)
        if mg_name == "balance":
            return (result == 1) or (isinstance(result, (int, float)) and result >= 0.5)
        if mg_name == "sequence":
            return (result == "Win") or (isinstance(result, (int, float)) and result > 0)
        if mg_name == "precision":
            return isinstance(result, int) and result >= 1
        return True

    # --------------------------------------------------
    # Session end / output
    # --------------------------------------------------
    def _craft_finalize(recipes_active, progress, var_inv):
        completed = []
        qualities = []
        primary_inv = getattr(store, var_inv[0], None) if var_inv else None
        for rid in recipes_active:
            if _craft_recipe_done(rid, progress):
                q = _craft_recipe_quality(rid, progress)
                if primary_inv is not None:
                    AddItem_Inventory(rid, 1, q, primary_inv)
                completed.append(rid)
                qualities.append(q)
        return completed, qualities


# Smooth 0.5s slide to a new xpos. Reused across screen re-evaluations so the
# sprite/bg interpolates from its current position to the new target.
transform _craft_slide_x(target):
    ease 0.5 xpos target


# ==================================================
# Scene screen — renders bg + foreground blocks + crafters only.
# Shown non-modally for the whole crafting session so it stays visible
# behind both the orchestrator UI and any sub-minigame call_screen.
# ==================================================
screen minigame_crafting_scene(var_typ="cooking", var_crf=["hero"], var_scn="LivingRoom", var_blk=["sink", "counter", "counter"], crafter_state=None):
    tag crafting_scene
    zorder -10

    # Direct access (not getattr) so Ren'Py tracks _craft_visual_blocks as a
    # dependency — the scene re-renders the moment the player marks an action.
    $ _vblk = _craft_visual_blocks or {}
    $ _focal_block = _vblk.get(var_crf[0], crafter_state[var_crf[0]]["block"]) if crafter_state and var_crf else 0
    $ _focal_block = 0 if _focal_block is None else _focal_block
    $ viewport_offset = _craft_viewport_offset(var_blk, _focal_block)

    for _bg_path, _bg_w in _craft_bg_paths(var_typ, var_scn):
        $ _bg_layer_x = _craft_bg_x(var_blk, _focal_block, _bg_w)
        add _bg_path at _craft_slide_x(_bg_layer_x):
            yalign 0.0

    fixed:
        xsize 1920
        ysize 1080

        for cid in var_crf:
            $ cb = _vblk.get(cid, crafter_state[cid]["block"])
            $ char_path = _craft_char_image(var_typ, cid, 1)
            $ char_x = cb * 640 + viewport_offset + 320
            if char_path:
                add char_path at _craft_slide_x(char_x):
                    xanchor 0.5

        for i, blk in enumerate(var_blk):
            $ block_x = i * 640 + viewport_offset
            add _craft_fg_for_block(var_typ, var_scn, blk) at _craft_slide_x(block_x):
                yalign 1.0

        for blk_idx, add_path in _craft_add_overlays(var_typ, _craft_action_pool, _craft_progress, var_blk):
            $ add_x = blk_idx * 640 + viewport_offset
            add add_path at _craft_slide_x(add_x):
                yalign 1.0



# ==================================================
# UI screen — pure renderer; Returns chosen step / "done" / "quit"
# ==================================================
screen minigame_crafting_ui(
    var_typ="cooking",
    var_crf=["hero"],
    var_scn="LivingRoom",
    var_blk=["sink", "counter", "counter"],
    var_inv=["inventory", "inventory_fridge"],
    var_rrc=None,
    var_arc="any",
    var_txt=None,
    action_pool=None,
    progress=None,
    crafter_state=None,
    recipes_active=None,
    any_action_taken=False,
    show_prep=True,
    expanded_recipes=None,
):

    default game_started = (not show_prep)
    default player_chosen_id = None

    modal True

    # --------------------------------------------------
    # Preparation Screen (first call only)
    # --------------------------------------------------
    if not game_started:
        frame:
            background "#000000C8"
            xysize (1920, 1080)
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                label renpy.translate_string("{size=60}{b}Crafting{/b}{/size}") xalign 0.5
                vbox:
                    xalign 0.5
                    xysize (960, 400)
                    if var_txt == None:
                        text renpy.translate_string("{size=40}Pick an action each turn. Select an action then press Do Action to begin. NPC crafters choose and act in parallel.{p}{p}⚠{b}Warning{/b}⚠{p}This minigame is a prototype. Currently, it just finishes when you prepare the barbecue, even if rice is still not ready, what may leave it with bad quality. For better results, make sure you prepare the rice before the barbecue, and all optional actions{/size}") xalign 0.5 justify True
                    else:
                        text renpy.translate_string("{size=40}[var_txt]{/size}") xalign 0.5
                text renpy.translate_string("[C_Dat]{size=50}{b}Click to start!{/b}[C_Off]") xalign 0.5

        key "mousedown_1" action SetScreenVariable("game_started", True)

    # --------------------------------------------------
    # Game state
    # --------------------------------------------------
    else:
        $ available_actions = _craft_available_actions(action_pool, progress, crafter_state, var_blk, var_inv, var_rrc)
        $ any_remaining = any(progress.get(s["id"], 0) < s["cnt"] for s in action_pool)
        $ all_required_done = (not recipes_active) or all(_craft_recipe_done(r, progress) for r in recipes_active)
        $ npc_choices_now = _craft_npc_choices_preview or {}
        $ player_chosen_step = next((s for s in action_pool if s["id"] == player_chosen_id), None) if player_chosen_id else None

        if any_action_taken and (not any_remaining or (var_rrc and all_required_done)):
            # Session done
            $ _craft_completed_preview = [r for r in recipes_active if _craft_recipe_done(r, progress)]
            frame:
                background "#000000E0"
                xysize (1920, 1080)
                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 30
                    label renpy.translate_string("{size=60}{b}Done!{/b}{/size}") xalign 0.5
                    if _craft_completed_preview:
                        for rid in _craft_completed_preview:
                            $ rname = _craft_recipe_name(rid)
                            $ rquality = _craft_recipe_quality(rid, progress)
                            $ rstars = _craft_quality_stars(rquality)
                            $ ricon = item_data.get(rid, {}).get("icon")
                            hbox:
                                xalign 0.5
                                spacing 16
                                if ricon and renpy.loadable(ricon):
                                    add ricon yalign 0.5
                                text renpy.translate_string("{size=50}[C_Pos][rname][C_Off] [rstars]{/size}") yalign 0.5
                    else:
                        text renpy.translate_string("{size=50}[C_Neg]No recipes completed.[C_Off]{/size}") xalign 0.5
                    text renpy.translate_string("[C_Dat]{size=45}{b}Click to continue{/b}[C_Off]") xalign 0.5

            key "mousedown_1" action Return("done")

        elif (not any_action_taken) and (not action_pool):
            # Empty-state: nothing to cook
            frame:
                background "#000000E0"
                xysize (1920, 1080)
                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 30
                    label renpy.translate_string("{size=60}{b}Nothing to cook{/b}{/size}") xalign 0.5
                    text renpy.translate_string("{size=40}No active recipe matches the available ingredients.{/size}") xalign 0.5
                    textbutton renpy.translate_string("{size=45}[C_Dat]Quit[C_Off]{/size}") xalign 0.5 action Return("quit")

        else:
            # Right-side panel
            frame:
                xalign 1.0
                yalign 0.0
                xoffset -100
                xsize 680
                ysize 1080
                background "#00000090"
                padding (12, 12)

                vbox:
                    xfill True
                    spacing 8

                    # ----- Actions -----
                    text renpy.translate_string("{size=55}{b}Actions{/b}{/size}") xalign 0.0

                    if player_chosen_id is not None:
                        textbutton renpy.translate_string("{size=45}{b}▶ Do Action{/b}{/size}"):
                            xalign 0.0
                            xfill True
                            action Return((player_chosen_step, npc_choices_now))

                    viewport:
                        xsize 656
                        ysize 380
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        vbox:
                            xfill True
                            spacing 4
                            $ grouped_actions = _craft_group_by_block(available_actions)
                            for blk_name, blk_steps in grouped_actions:
                                text renpy.translate_string("{size=45}{b}— [blk_name] —{/b}{/size}") xalign 0.0
                                for step in blk_steps:
                                    $ sid = step["id"]
                                    $ icon_p = _craft_action_icon_path(sid, player_chosen_id, npc_choices_now, var_crf)
                                    $ btn_lbl = _craft_step_button_label(step, progress)
                                    $ is_chosen = (sid == player_chosen_id)
                                    $ _new_sid = None if is_chosen else sid
                                    button:
                                        xfill True
                                        action [
                                            SetScreenVariable("player_chosen_id", _new_sid),
                                            Function(_craft_apply_mark, _new_sid, var_crf, action_pool, progress, crafter_state, var_blk, var_inv, var_rrc),
                                        ]
                                        hbox:
                                            spacing 6
                                            if icon_p:
                                                add icon_p:
                                                    xsize 48
                                                    ysize 48
                                                    fit "contain"
                                                    yalign 0.5
                                            else:
                                                text "⭐" size 40 yalign 0.5
                                            text renpy.translate_string("{size=40}[btn_lbl]{/size}") xalign 0.0 yalign 0.5

                    null height 8

                    # ----- Recipes -----
                    text renpy.translate_string("{size=55}{b}Recipes{/b}{/size}") xalign 0.0

                    viewport:
                        xsize 656
                        ysize 380
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        vbox:
                            xfill True
                            spacing 4
                            for rid in recipes_active:
                                $ rname = _craft_recipe_name(rid)
                                $ rdone, rtotal = _craft_recipe_progress(rid, progress)
                                textbutton renpy.translate_string("{size=40}[rname] [[[rdone]/[rtotal]]{/size}"):
                                    xalign 0.0
                                    action Function(_craft_toggle_set, expanded_recipes, rid)
                                if rid in expanded_recipes:
                                    vbox:
                                        xfill True
                                        spacing 2
                                        for s in _craft_get_steps(rid):
                                            $ status = _craft_step_status_line(s, progress)
                                            text renpy.translate_string("{size=40}  [status]{/size}") xalign 0.0


# ==================================================
# Public label — drives the crafting session loop
# ==================================================
label minigame_crafting(var_typ="cooking", var_crf=["hero"], var_scn="LivingRoom", var_blk=["sink", "counter", "counter"], var_inv=["inventory", "inventory_fridge"], var_ing="any", var_rrc=None, var_arc="any", var_txt=None):

    python:
        _craft_action_pool          = _craft_build_pool(var_typ, var_rrc, var_arc, var_inv, var_ing)
        _craft_progress             = {step["id"]: 0 for step in _craft_action_pool}
        _craft_crafter_state        = {c: {"block": _craft_initial_block(c, var_blk, var_typ), "busy": False} for c in var_crf}
        _craft_recipes_active       = _craft_active_recipes(var_typ, var_rrc, var_arc, var_inv, var_ing)
        _craft_any_action_taken     = False
        _craft_show_prep            = True
        _craft_expanded_recipes     = set(_craft_recipes_active)
        _craft_npc_choices_preview  = _craft_compute_npc_choices(var_crf, _craft_action_pool, _craft_progress, _craft_crafter_state, var_blk, var_inv, None, var_rrc)
        _craft_visual_blocks        = _craft_visual_positions(var_crf, _craft_crafter_state, var_blk, None, _craft_npc_choices_preview, _craft_action_pool)

    show screen minigame_crafting_scene(var_typ=var_typ, var_crf=var_crf, var_scn=var_scn, var_blk=var_blk, crafter_state=_craft_crafter_state)

label _craft_session_loop:

    python:
        # Fresh preview at the start of each turn — no player choice yet, but
        # NPCs already have a tentative pick visible behind the UI.
        _craft_npc_choices_preview = _craft_compute_npc_choices(var_crf, _craft_action_pool, _craft_progress, _craft_crafter_state, var_blk, var_inv, None, var_rrc)
        _craft_visual_blocks       = _craft_visual_positions(var_crf, _craft_crafter_state, var_blk, None, _craft_npc_choices_preview, _craft_action_pool)

    call screen minigame_crafting_ui(var_typ=var_typ, var_crf=var_crf, var_scn=var_scn, var_blk=var_blk, var_inv=var_inv, var_rrc=var_rrc, var_arc=var_arc, var_txt=var_txt, action_pool=_craft_action_pool, progress=_craft_progress, crafter_state=_craft_crafter_state, recipes_active=_craft_recipes_active, any_action_taken=_craft_any_action_taken, show_prep=_craft_show_prep, expanded_recipes=_craft_expanded_recipes)

    $ _craft_show_prep = False
    $ _craft_result = _return

    if _craft_result == "quit":
        hide screen minigame_crafting_scene
        return ([], [])

    if _craft_result == "done":
        $ _craft_completed, _craft_qualities = _craft_finalize(_craft_recipes_active, _craft_progress, var_inv)
        hide screen minigame_crafting_scene
        return (_craft_completed, _craft_qualities)

    # _craft_result is (step_dict, npc_choices_dict)
    $ _craft_step, _craft_npc_choices = _craft_result
    $ _craft_any_action_taken = True
    $ _craft_crafter = var_crf[0]

    python:
        _craft_move_to_block(_craft_crafter, _craft_step["blk"], _craft_crafter_state, var_blk)
        if _craft_step.get("use") and not _craft_step_required(_craft_step, var_rrc):
            _craft_inv_consume(_craft_step["use"], var_inv)

    # Run sub-minigame (or instant resolution if mg is None)
    $ _craft_mg_name, _craft_mg_kwargs = _craft_resolve_minigame_args(_craft_step, _craft_crafter)
    $ _craft_success = True

    if _craft_mg_name == "thugofwar":
        call screen minigame_thugofwar(**_craft_mg_kwargs)
        $ _craft_success = _craft_minigame_success("thugofwar", _return)
    elif _craft_mg_name == "balance":
        call screen minigame_balance(**_craft_mg_kwargs)
        $ _craft_success = _craft_minigame_success("balance", _return)
    elif _craft_mg_name == "sequence":
        call screen minigame_sequence(**_craft_mg_kwargs)
        $ _craft_success = _craft_minigame_success("sequence", _return)
    elif _craft_mg_name == "precision":
        call screen minigame_precision(**_craft_mg_kwargs)
        $ _craft_success = _craft_minigame_success("precision", _return)

    python:
        if _craft_success:
            _craft_progress[_craft_step["id"]] = _craft_progress.get(_craft_step["id"], 0) + 1
        _craft_apply_npc_choices(_craft_npc_choices, _craft_progress, var_inv, _craft_crafter_state, var_blk, var_rrc)

    jump _craft_session_loop
