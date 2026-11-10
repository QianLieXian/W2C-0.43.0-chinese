# ----------------------------------------------------------------------------------------------------
init python:
# ----------------------------------------------------------------------------------------------------

    # --------------------------------------------------
    # Constants
    # --------------------------------------------------

    # 56-cell clockwise main path as (col, row) on a 15x15 grid
    LUDO_MAIN_PATH = [
        # Left arm top row, going right [0-5]
        (0,6), (1,6), (2,6), (3,6), (4,6), (5,6),
        # Corner into top arm [6]
        (6,6),
        # Up top-arm left col [7-12]
        (6,5), (6,4), (6,3), (6,2), (6,1), (6,0),
        # Top row right [13-14]
        (7,0), (8,0),
        # Down top-arm right col [15-19]
        (8,1), (8,2), (8,3), (8,4), (8,5),
        # Corner into right arm [20]
        (8,6),
        # Right arm top row, going right [21-25]
        (9,6), (10,6), (11,6), (12,6), (13,6),
        # Right col down [26-28]
        (14,6), (14,7), (14,8),
        # Right arm bottom row, going left [29-33]
        (13,8), (12,8), (11,8), (10,8), (9,8),
        # Corner into bottom arm [34]
        (8,8),
        # Down bottom-arm right col [35-40]
        (8,9), (8,10), (8,11), (8,12), (8,13), (8,14),
        # Bottom row left [41-42]
        (7,14), (6,14),
        # Up bottom-arm left col [43-47]
        (6,13), (6,12), (6,11), (6,10), (6,9),
        # Corner into left arm [48]
        (6,8),
        # Left arm bottom row, going left [49-53]
        (5,8), (4,8), (3,8), (2,8), (1,8),
        # Left col up [54-55]
        (0,8), (0,7),
    ]

    LUDO_COLORS = {
        "red": {
            "spawns": [(1,1), (4,1), (1,4), (4,4)],
            "start_idx": 1,
            "home_entry_idx": 1,
            "home_lane": [(1,7), (2,7), (3,7), (4,7), (5,7), (6,7)],
            "hex": "#FF4444",
            "hex_dark": "#AA2222",
        },
        "blue": {
            "spawns": [(10,1), (13,1), (10,4), (13,4)],
            "start_idx": 15,
            "home_entry_idx": 15,
            "home_lane": [(7,1), (7,2), (7,3), (7,4), (7,5), (7,6)],
            "hex": "#4444FF",
            "hex_dark": "#2222AA",
        },
        "yellow": {
            "spawns": [(10,10), (13,10), (10,13), (13,13)],
            "start_idx": 29,
            "home_entry_idx": 29,
            "home_lane": [(13,7), (12,7), (11,7), (10,7), (9,7), (8,7)],
            "hex": "#FFDD44",
            "hex_dark": "#AA9922",
        },
        "green": {
            "spawns": [(1,10), (4,10), (1,13), (4,13)],
            "start_idx": 43,
            "home_entry_idx": 43,
            "home_lane": [(7,13), (7,12), (7,11), (7,10), (7,9), (7,8)],
            "hex": "#44DD44",
            "hex_dark": "#22AA22",
        },
    }

    LUDO_NPC_PREFS = {
        "wnei": ["yellow", "green", "blue", "red"],
        "wsis": ["red", "blue"],
        "hine": ["blue", "yellow"],
        "hprv": ["green", "blue"],
        "hriv": ["blue", "red"],
        "wdan": ["red"],
        "wdel": ["red"],
        "wdis": ["red"],
        "wgal": ["red"],
        "wgot": ["blue"],
        "wlaz": ["green", "yellow", "red", "blue"],
        "wota": ["yellow"],
        "wpre": ["green"],
        "wric": ["red"],
        "wuza": ["red"],
    }

    LUDO_COLOR_ORDER = ["red", "blue", "yellow", "green"]

    # --------------------------------------------------
    # Helper Functions
    # --------------------------------------------------

    def _ludo_assign_colors(players, hero_color=None):
        """Assign colors to players. hero_color is pre-assigned if provided."""
        assignments = {}
        available = list(LUDO_COLOR_ORDER)

        if hero_color and "hero" in players:
            assignments["hero"] = hero_color
            available.remove(hero_color)

        npcs = [p for p in players if p != "hero"]
        npc_tiers = {}
        for npc in npcs:
            npc_tiers[npc] = LUDO_NPC_PREFS.get(npc, [])

        max_tier = max((len(v) for v in npc_tiers.values()), default=0)

        for tier in range(max_tier):
            tier_wants = {}
            for npc in npcs:
                if npc in assignments:
                    continue
                prefs = npc_tiers[npc]
                if tier < len(prefs) and prefs[tier] in available:
                    color = prefs[tier]
                    if color not in tier_wants:
                        tier_wants[color] = []
                    tier_wants[color].append(npc)

            for color, contenders in tier_wants.items():
                if color not in available:
                    continue
                best_tier_contenders = []
                for c in contenders:
                    c_prefs = npc_tiers[c]
                    c_tier = c_prefs.index(color) if color in c_prefs else 999
                    best_tier_contenders.append((c_tier, c))
                best_tier_contenders.sort(key=lambda x: x[0])
                best_level = best_tier_contenders[0][0]
                top = [c for t, c in best_tier_contenders if t == best_level]
                winner = renpy.random.choice(top)
                assignments[winner] = color
                available.remove(color)

        for npc in npcs:
            if npc not in assignments and available:
                color = renpy.random.choice(available)
                assignments[npc] = color
                available.remove(color)

        return assignments

    def _ludo_hero_compete_color(hero_color, npcs):
        """50/50 contest when hero picks a color an NPC wants as primary."""
        return renpy.random.random() < 0.5

    def _ludo_init_game(players, pawn_count, color_assignments):
        """Build the game state dictionary."""
        player_list = []
        for code in players:
            color = color_assignments[code]
            pawns = []
            for i in range(pawn_count):
                pawns.append({
                    "state": "spawn",
                    "path_idx": -1,
                    "home_idx": -1,
                    "spawn_slot": i,
                    "total_steps": 0,
                })
            player_list.append({
                "code": code,
                "color": color,
                "pawns": pawns,
                "score": 0,
                "bonus_six": 0.0,
            })
        return {
            "players": player_list,
            "current_turn": 0,
            "dice_value": None,
            "phase": "roll",
            "extra_turn": False,
            "winner": None,
        }

    def _ludo_roll_dice():
        return renpy.random.randint(1, 6)

    def _ludo_pawn_colrow(pawn, color_data):
        """Get (col, row) for a pawn based on its state."""
        if pawn["state"] == "spawn":
            return color_data["spawns"][pawn["spawn_slot"]]
        elif pawn["state"] == "active":
            return LUDO_MAIN_PATH[pawn["path_idx"] % 56]
        elif pawn["state"] == "home":
            if pawn["home_idx"] < len(color_data["home_lane"]):
                return color_data["home_lane"][pawn["home_idx"]]
            return (7, 7)
        elif pawn["state"] == "finished":
            return (7, 7)
        return (7, 7)

    def _ludo_is_wall_at(game_state, col_row, exclude_player=None):
        """True if 2+ same-color pawns at position (wall)."""
        for pi, player in enumerate(game_state["players"]):
            if pi == exclude_player:
                continue
            color_data = LUDO_COLORS[player["color"]]
            count = 0
            for pawn in player["pawns"]:
                if pawn["state"] in ("active", "home"):
                    pos = _ludo_pawn_colrow(pawn, color_data)
                    if pos == col_row:
                        count += 1
            if count >= 2:
                return True
        return False

    def _ludo_check_kill(game_state, moving_player_idx, target_colrow):
        """Check if an opponent single pawn is at target. Returns (player_idx, pawn_idx) or None."""
        for pi, player in enumerate(game_state["players"]):
            if pi == moving_player_idx:
                continue
            color_data = LUDO_COLORS[player["color"]]
            pawns_at = []
            for pawn_i, pawn in enumerate(player["pawns"]):
                if pawn["state"] == "active":
                    pos = _ludo_pawn_colrow(pawn, color_data)
                    if pos == target_colrow:
                        pawns_at.append(pawn_i)
            if len(pawns_at) == 1:
                return (pi, pawns_at[0])
        return None

    def _ludo_calc_target(pawn, dice, color_data):
        """Calculate destination. Returns (zone, idx) or None."""
        if pawn["state"] == "active":
            start = pawn["path_idx"]
            home_entry = color_data["home_entry_idx"]

            # Pawn must complete a full loop (56 steps) before entering home
            can_enter_home = (pawn["total_steps"] + dice) >= 56

            if start == home_entry:
                steps_to_home = 0
            elif start < home_entry:
                steps_to_home = home_entry - start
            else:
                steps_to_home = (56 - start) + home_entry

            if can_enter_home and dice > steps_to_home:
                home_steps = dice - steps_to_home - 1
                if home_steps > 6:
                    return None
                elif home_steps == 6:
                    return ("finished", 6)
                elif home_steps <= 5:
                    return ("home", home_steps)
                else:
                    return None
            else:
                # Stay on main path
                new_idx = (start + dice) % 56
                return ("main", new_idx)

        elif pawn["state"] == "home":
            new_home = pawn["home_idx"] + dice
            if new_home == 6:
                return ("finished", 6)
            elif new_home < 6:
                return ("home", new_home)
            else:
                bounce = 12 - new_home
                if bounce < 0:
                    return None
                return ("home", bounce)

        return None

    def _ludo_get_valid_moves(game_state, player_idx):
        """Returns [(pawn_idx, move_type), ...] for valid moves."""
        player = game_state["players"][player_idx]
        color_data = LUDO_COLORS[player["color"]]
        dice = game_state["dice_value"]
        moves = []

        for pi, pawn in enumerate(player["pawns"]):
            if pawn["state"] == "spawn":
                if dice == 6:
                    own_at_start = sum(1 for p in player["pawns"] if p["state"] == "active" and p["path_idx"] == color_data["start_idx"])
                    if own_at_start < 2:
                        moves.append((pi, "release"))

            elif pawn["state"] == "active" or pawn["state"] == "home":
                target = _ludo_calc_target(pawn, dice, color_data)
                if target is None:
                    continue

                zone, idx = target
                if zone == "main":
                    target_pos = LUDO_MAIN_PATH[idx]
                    # Wall only blocks landing on it, NOT passing through
                    if _ludo_is_wall_at(game_state, target_pos, exclude_player=player_idx):
                        continue
                    moves.append((pi, "move"))

                elif zone == "home" or zone == "finished":
                    moves.append((pi, "move"))

            elif pawn["state"] == "finished":
                continue

        return moves

    def _ludo_execute_move(game_state, player_idx, pawn_idx, move_type):
        """Execute a move. Returns events dict."""
        player = game_state["players"][player_idx]
        color_data = LUDO_COLORS[player["color"]]
        pawn = player["pawns"][pawn_idx]
        events = {"kill": None, "wall": False, "finished": False}

        if move_type == "release":
            pawn["state"] = "active"
            pawn["path_idx"] = color_data["start_idx"]
            pawn["home_idx"] = -1
            start_pos = LUDO_MAIN_PATH[color_data["start_idx"]]
            kill = _ludo_check_kill(game_state, player_idx, start_pos)
            if kill:
                events["kill"] = kill
                killed_pawn = game_state["players"][kill[0]]["pawns"][kill[1]]
                killed_pawn["state"] = "spawn"
                killed_pawn["path_idx"] = -1
                killed_pawn["home_idx"] = -1
                killed_pawn["total_steps"] = 0

        elif move_type == "move":
            dice = game_state["dice_value"]
            target = _ludo_calc_target(pawn, dice, color_data)
            pawn["total_steps"] += dice
            if target:
                zone, idx = target
                if zone == "main":
                    pawn["path_idx"] = idx
                    pawn["state"] = "active"
                    target_pos = LUDO_MAIN_PATH[idx]
                    kill = _ludo_check_kill(game_state, player_idx, target_pos)
                    if kill:
                        events["kill"] = kill
                        killed_pawn = game_state["players"][kill[0]]["pawns"][kill[1]]
                        killed_pawn["state"] = "spawn"
                        killed_pawn["path_idx"] = -1
                        killed_pawn["home_idx"] = -1
                        killed_pawn["total_steps"] = 0
                    own_at_pos = sum(1 for p in player["pawns"] if p["state"] == "active" and _ludo_pawn_colrow(p, color_data) == target_pos)
                    if own_at_pos >= 2:
                        events["wall"] = True

                elif zone == "home":
                    pawn["state"] = "home"
                    pawn["home_idx"] = idx
                    pawn["path_idx"] = -1

                elif zone == "finished":
                    pawn["state"] = "finished"
                    pawn["path_idx"] = -1
                    pawn["home_idx"] = -1
                    player["score"] += 1
                    events["finished"] = True

        return events

    def _ludo_compute_move_path(pawn, dice, color_data, move_type):
        """Compute list of (col, row) cells the pawn visits step by step."""
        path = []

        if move_type == "release":
            path.append(LUDO_MAIN_PATH[color_data["start_idx"]])
            return path

        if pawn["state"] == "active":
            current_idx = pawn["path_idx"]
            home_entry = color_data["home_entry_idx"]
            can_enter_home = (pawn["total_steps"] + dice) >= 56

            if current_idx == home_entry:
                steps_to_home = 0
            elif current_idx < home_entry:
                steps_to_home = home_entry - current_idx
            else:
                steps_to_home = (56 - current_idx) + home_entry

            if can_enter_home and dice > steps_to_home:
                # Steps on main path up to and including home entry
                for step in range(1, steps_to_home + 1):
                    idx = (current_idx + step) % 56
                    path.append(LUDO_MAIN_PATH[idx])
                # Steps into home lane
                remaining = dice - steps_to_home - 1
                for hi in range(remaining + 1):
                    if hi < len(color_data["home_lane"]):
                        path.append(color_data["home_lane"][hi])
                    elif hi == 6:
                        path.append((7, 7))
            else:
                # Stay on main path
                for step in range(1, dice + 1):
                    idx = (current_idx + step) % 56
                    path.append(LUDO_MAIN_PATH[idx])

        elif pawn["state"] == "home":
            current_home = pawn["home_idx"]
            new_home = current_home + dice

            if new_home <= 6:
                for step in range(1, dice + 1):
                    hi = current_home + step
                    if hi < len(color_data["home_lane"]):
                        path.append(color_data["home_lane"][hi])
                    elif hi == 6:
                        path.append((7, 7))
            else:
                # Forward to center
                for step in range(1, 6 - current_home + 1):
                    hi = current_home + step
                    if hi < len(color_data["home_lane"]):
                        path.append(color_data["home_lane"][hi])
                path.append((7, 7))
                # Bounce back from center
                overshoot = new_home - 6
                for step in range(1, overshoot + 1):
                    hi = 6 - step
                    if 0 <= hi < len(color_data["home_lane"]):
                        path.append(color_data["home_lane"][hi])

        return path

    def _ludo_pawn_progress(pawn, color_data):
        """Get how many steps a pawn has advanced from its start position."""
        if pawn["state"] == "home":
            return 56 + pawn["home_idx"]
        elif pawn["state"] == "active":
            start = color_data["start_idx"]
            if pawn["path_idx"] >= start:
                return pawn["path_idx"] - start
            else:
                return (56 - start) + pawn["path_idx"]
        return 0

    def _ludo_npc_plan_a(game_state, player_idx, valid_moves):
        """Smart AI. Priority: kill > release on 6 > exact finish > most-progress active pawn > random."""
        player = game_state["players"][player_idx]
        color_data = LUDO_COLORS[player["color"]]
        dice = game_state["dice_value"]

        # 1. Kill enemy pawn — prefer the one with most walk progress
        kill_options = []
        for pi, mtype in valid_moves:
            if mtype == "move":
                pawn = player["pawns"][pi]
                target = _ludo_calc_target(pawn, dice, color_data)
                if target and target[0] == "main":
                    target_pos = LUDO_MAIN_PATH[target[1]]
                    kill = _ludo_check_kill(game_state, player_idx, target_pos)
                    if kill:
                        kp = game_state["players"][kill[0]]
                        kc = LUDO_COLORS[kp["color"]]
                        kprog = _ludo_pawn_progress(kp["pawns"][kill[1]], kc)
                        kill_options.append((pi, kprog))
        if kill_options:
            kill_options.sort(key=lambda x: x[1], reverse=True)
            return (kill_options[0][0], "move")

        # 2. Release a pawn from base if dice is 6
        if dice == 6:
            releases = [(pi, mt) for pi, mt in valid_moves if mt == "release"]
            if releases:
                return renpy.random.choice(releases)

        # 3. Exact finish — move any pawn that reaches the center tile this turn
        for pi, mtype in valid_moves:
            if mtype == "move":
                pawn = player["pawns"][pi]
                target = _ludo_calc_target(pawn, dice, color_data)
                if target and target[0] == "finished":
                    return (pi, mtype)

        # 4. Move the most-progress active pawn (outside safe area / home lane)
        active_options = []
        seen_pi = set()
        for pi, mtype in valid_moves:
            if mtype == "move" and pi not in seen_pi:
                pawn = player["pawns"][pi]
                if pawn["state"] == "active":
                    seen_pi.add(pi)
                    prog = _ludo_pawn_progress(pawn, color_data)
                    active_options.append((pi, prog))
        if active_options:
            active_options.sort(key=lambda x: x[1], reverse=True)
            return (active_options[0][0], "move")

        # 5. Random valid move (covers home-lane advancement and other edge cases)
        return renpy.random.choice(valid_moves)

    def _ludo_npc_plan_b(game_state, player_idx, valid_moves):
        """Dumb AI. Release > 50% random move > finish > random move."""
        player = game_state["players"][player_idx]
        color_data = LUDO_COLORS[player["color"]]
        dice = game_state["dice_value"]

        # 1. Release a random pawn if dice is 6
        releases = [(pi, mt) for pi, mt in valid_moves if mt == "release"]
        if releases:
            return renpy.random.choice(releases)

        # 2. 50% chance of moving a random pawn
        if renpy.random.random() < 0.5:
            return renpy.random.choice(valid_moves)

        # 3. Finish if exact dice
        for pi, mtype in valid_moves:
            if mtype == "move":
                pawn = player["pawns"][pi]
                target = _ludo_calc_target(pawn, dice, color_data)
                if target and target[0] == "finished":
                    return (pi, mtype)

        # 4. Move a random pawn
        return renpy.random.choice(valid_moves)

    def _ludo_npc_choose(game_state, player_idx, valid_moves):
        """NPC AI: uses character intelligence to decide between Plan A (smart) and Plan B (dumb)."""
        player = game_state["players"][player_idx]
        char_code = player["code"]

        # Get intelligence stat (0-100) to determine Plan A chance
        try:
            intel = stat_value(char_code, "int", 50)
        except:
            intel = 50

        intel_chance = max(0.0, min(1.0, intel / 100.0))

        if renpy.random.random() < intel_chance:
            return _ludo_npc_plan_a(game_state, player_idx, valid_moves)
        else:
            return _ludo_npc_plan_b(game_state, player_idx, valid_moves)

    def _ludo_check_game_over(game_state):
        """Returns winner's code or None."""
        pawn_count = len(game_state["players"][0]["pawns"])
        for player in game_state["players"]:
            if player["score"] >= pawn_count:
                return player["code"]
        return None

    def _ludo_get_gaming(npc_code):
        """Return the NPC's gaming archetype ('competitive', 'noob', 'social') or None."""
        if npc_code == "hero":
            return None
        return getattr(store, npc_code + "_gaming", None)

    def _ludo_apply_love_for_player_kill(game_state, killed_player_idx):
        """Player just killed an NPC pawn. Update love for all NPCs based on archetype.
        - competitive: +0.1 if own pawn killed, +0.2 if another NPC's pawn killed
        - noob: -0.1 if own pawn killed, +0.2 if another NPC's pawn killed
        - social: -0.05 if own pawn killed, no change otherwise"""
        for pi, player in enumerate(game_state["players"]):
            code = player["code"]
            if code == "hero":
                continue
            archetype = _ludo_get_gaming(code)
            if archetype is None:
                continue
            own_pawn_killed = (pi == killed_player_idx)
            if archetype == "competitive":
                add_stat(code, "love", 0.1 if own_pawn_killed else 0.2)
            elif archetype == "noob":
                add_stat(code, "love", -0.1 if own_pawn_killed else 0.2)
            elif archetype == "social":
                if own_pawn_killed:
                    add_stat(code, "love", -0.05)

    def _ludo_apply_love_for_npc_kill_player(game_state, killer_idx):
        """An NPC pawn just killed the hero. Reward the killer based on archetype.
        - competitive: +0.1 (good fight)
        - noob:        +0.2 (loves winning)
        - social:      no change"""
        code = game_state["players"][killer_idx]["code"]
        archetype = _ludo_get_gaming(code)
        if archetype == "competitive":
            add_stat(code, "love", 0.1)
        elif archetype == "noob":
            add_stat(code, "love", 0.2)

    def _ludo_apply_love_for_player_finish(game_state, hero_idx):
        """Player just got a pawn to the center. Every competitive NPC
        gains a flat +0.5 love (no scaling)."""
        for player in game_state["players"]:
            code = player["code"]
            if code == "hero":
                continue
            if _ludo_get_gaming(code) == "competitive":
                add_stat(code, "love", 0.5)

    def _ludo_apply_love_for_npc_finish(game_state, npc_idx):
        """A competitive NPC just got a pawn to the center. Their victory
        is meaningful when the player has scored, so reward scales with
        hero_score: +0.5 * hero_score. No effect if hero_score == 0."""
        npc = game_state["players"][npc_idx]
        code = npc["code"]
        if _ludo_get_gaming(code) != "competitive":
            return
        hero_score = 0
        for p in game_state["players"]:
            if p["code"] == "hero":
                hero_score = p["score"]
                break
        if hero_score > 0:
            add_stat(code, "love", 0.5 * hero_score)

    def _ludo_advance_turn(game_state):
        """Advance to next player's turn, or same player if dice was 6."""
        if game_state["dice_value"] == 6:
            game_state["extra_turn"] = True
        else:
            game_state["extra_turn"] = False
            game_state["current_turn"] = (game_state["current_turn"] + 1) % len(game_state["players"])
        game_state["phase"] = "roll"
        game_state["dice_value"] = None

    def _ludo_get_pixel_pos(col, row, board_x, board_y, cell_size):
        """Grid (col, row) to pixel (x, y) center position."""
        x = board_x + col * cell_size + cell_size / 2.0
        y = board_y + row * cell_size + cell_size / 2.0
        return (int(x), int(y))

    def _ludo_get_stack_offset(index_in_stack, total_stacked):
        """Small pixel offset for overlapping pawns."""
        if total_stacked <= 1:
            return (0, 0)
        offsets = [(-8, -8), (8, -8), (-8, 8), (8, 8)]
        if index_in_stack < len(offsets):
            return offsets[index_in_stack]
        return (0, 0)

    def _ludo_get_pawns_at(game_state, col_row, anim_pi=-1, anim_pai=-1, anim_pos=None):
        """Get list of (player_idx, pawn_idx) at a given position, accounting for animation."""
        result = []
        for pi, player in enumerate(game_state["players"]):
            color_data = LUDO_COLORS[player["color"]]
            for pawn_i, pawn in enumerate(player["pawns"]):
                if pawn["state"] in ("spawn", "active", "home"):
                    # Use animation position for the animated pawn
                    if pi == anim_pi and pawn_i == anim_pai and anim_pos is not None:
                        pos = anim_pos
                    else:
                        pos = _ludo_pawn_colrow(pawn, color_data)
                    if pos == col_row:
                        result.append((pi, pawn_i))
        return result

    def _ludo_get_player_name(code):
        """Get display name for a player code."""
        if code == "hero":
            var_name = "fnamehero"
        else:
            var_name = "fname" + code
        try:
            name = globals().get(var_name, code.capitalize())
            if name:
                return name
            return code.capitalize()
        except:
            return code.capitalize()

# ----------------------------------------------------------------------------------------------------
screen minigame_ludo(var_pla=["hero", "wsis", "wnei"], var_paw=4, var_txt=None):
# ----------------------------------------------------------------------------------------------------

    # --------------------------------------------------
    # Screen variables
    # --------------------------------------------------
    default ludo_phase = "prep"
    default ludo_game = None
    default ludo_color_assignments = {}
    default ludo_hero_color = None
    default ludo_hero_lost_colors = []
    default ludo_valid_moves = []
    default ludo_message = ""
    default ludo_npc_state = "idle"
    default ludo_event_timer = 0.0
    default ludo_result = None
    default ludo_tick = 0

    # Animation variables
    default ludo_anim_active = False
    default ludo_anim_path = []
    default ludo_anim_idx = 0
    default ludo_anim_pi = -1
    default ludo_anim_pai = -1
    default ludo_anim_delay = 0.0
    default ludo_anim_move_type = ""

    # Player-tunable settings
    default ludo_pawn_count = var_paw
    default ludo_instant = False

    # Board layout constants
    $ panel_width = 500
    $ board_size = 1080 - 20
    $ cell_size = board_size / 15.0
    $ board_x = panel_width + (1920 - panel_width - board_size) // 2
    $ board_y = 10
    $ pawn_size = int(board_size / 22)
    $ hero_playing = "hero" in var_pla

    # ==========================================
    # Phase: Preparation (color select + rules)
    # ==========================================
    if ludo_phase == "prep":
        # NPC-only: auto-assign colors once
        if not hero_playing and not ludo_color_assignments:
            python:
                ludo_color_assignments = _ludo_assign_colors(var_pla)

        add "images/Mechanics/Ludo/ludo_board.webp":
            xysize (board_size, board_size)
            pos (board_x, board_y)
            alpha 0.3

        frame:
            background "#000000D8"
            xysize (1920, 1080)

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 25

                label renpy.translate_string("{size=+60}{b}Ludo{/b}{/size}") xalign 0.5

                # Player portraits with color (gray if not yet assigned)
                hbox:
                    xalign 0.5
                    spacing 30
                    for p_code in var_pla:
                        $ p_img = "images/UI/OC_" + p_code.upper() + ".webp"
                        $ p_name = _ludo_get_player_name(p_code)
                        vbox:
                            spacing 5
                            add p_img:
                                xysize (100, 100)
                                xalign 0.5
                            if p_code in ludo_color_assignments:
                                $ p_hex = LUDO_COLORS[ludo_color_assignments[p_code]]["hex"]
                                text renpy.translate_string("{color=") + p_hex + "}{b}" + p_name + "{/b}{/color}":
                                    xalign 0.5
                                    size 22
                            else:
                                text renpy.translate_string("{color=#888888}") + p_name + "{/color}":
                                    xalign 0.5
                                    size 22

                # Rules text (scrollable)
                viewport:
                    xalign 0.5
                    xysize (800, 250)
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    vbox:
                        xsize 780
                        spacing 5
                        if var_txt is None:
                            text renpy.translate_string("{size=+2}Roll a 6 to release a pawn from your base. Move your pawns clockwise around the board. Land on an opponent's pawn to send it back to base. Get all your pawns to the center to win!{/size}") xalign 0.5
                            text renpy.translate_string("\n{color=#64FF64}Rules:{/color}") xalign 0.5
                            text renpy.translate_string("• Roll 6 = release a pawn + extra turn") xalign 0.5
                            text renpy.translate_string("• Landing on an enemy sends them home") xalign 0.5
                            text renpy.translate_string("• Two of your pawns on same spot = wall (blocks enemies)") xalign 0.5
                            text renpy.translate_string("• First to get all {color=#FFD964}{b}[ludo_pawn_count]{/b}{/color} pawns to center wins!") xalign 0.5
                        else:
                            text var_txt xalign 0.5

                # Pawn-count selector (only meaningful before init; locked once color picked)
                $ count_locked = bool(ludo_color_assignments)
                hbox:
                    xalign 0.5
                    spacing 12
                    text renpy.translate_string("Pawns each:") yalign 0.5 size 24
                    for n in (1, 2, 3, 4):
                        $ is_sel = (ludo_pawn_count == n)
                        button:
                            xysize (50, 50)
                            yalign 0.5
                            if is_sel:
                                background "#FFD964"
                            else:
                                background "#444444"
                            hover_background "#FFB000"
                            hover_sound None
                            activate_sound None
                            sensitive (not count_locked)
                            action SetScreenVariable("ludo_pawn_count", n)
                            if is_sel:
                                text str(n) xalign 0.5 yalign 0.5 color "#000000" size 26
                            else:
                                text str(n) xalign 0.5 yalign 0.5 color "#FFFFFF" size 26
                if count_locked:
                    text renpy.translate_string("{color=#888888}{size=-3}(locked once a color is picked){/size}{/color}") xalign 0.5

                # Color selection or Click to start
                $ all_assigned = (len(ludo_color_assignments) == len(var_pla))

                if hero_playing and "hero" not in ludo_color_assignments:
                    # Hero hasn't picked a color yet
                    text renpy.translate_string("{size=+5}Choose your color:{/size}") xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 40
                        $ taken_colors = list(ludo_color_assignments.values())
                        for color_name in LUDO_COLOR_ORDER:
                            if color_name not in taken_colors:
                                $ cdata = LUDO_COLORS[color_name]
                                button:
                                    xysize (120, 80)
                                    background cdata["hex"]
                                    hover_background cdata["hex_dark"]
                                    hover_sound None
                                    activate_sound None
                                    action Function(_ludo_hero_pick_color, color_name, var_pla)
                                    text renpy.translate_string("{b}") + color_name.capitalize() + "{/b}":
                                        xalign 0.5
                                        yalign 0.5
                                        color "#FFFFFF"

                    if ludo_hero_lost_colors:
                        text renpy.translate_string("{color=#FF6464}That color was contested and you lost! Pick another.{/color}") xalign 0.5

                elif all_assigned:
                    # All colors assigned - ready to start
                    text renpy.translate_string("[C_Dat]{size=+40}{b}Click to start!{/b}[C_Off]") xalign 0.5

        # Click to start (only when all players have colors)
        if len(ludo_color_assignments) == len(var_pla):
            key "mouseup_1" action [
                SetScreenVariable("ludo_game", _ludo_init_game(var_pla, ludo_pawn_count, ludo_color_assignments)),
                SetScreenVariable("ludo_phase", "game"),
            ]

    # ==========================================
    # Phase: Game
    # ==========================================
    elif ludo_phase == "game" and ludo_game is not None:

        $ cur_turn = ludo_game["current_turn"]
        $ cur_player = ludo_game["players"][cur_turn]
        $ cur_code = cur_player["code"]
        $ cur_color = cur_player["color"]
        $ is_hero_turn = (cur_code == "hero")
        $ game_phase = ludo_game["phase"]

        # --------------------------------------------------
        # Board
        # --------------------------------------------------
        add "images/Mechanics/Ludo/ludo_board.webp":
            xysize (board_size, board_size)
            pos (board_x, board_y)

        # --------------------------------------------------
        # Render all pawns
        # --------------------------------------------------
        for pi in range(len(ludo_game["players"])):
            $ gp = ludo_game["players"][pi]
            $ gp_color = gp["color"]
            $ gp_cdata = LUDO_COLORS[gp_color]
            $ gp_code = gp["code"]

            for pawn_i in range(len(gp["pawns"])):
                $ pw = gp["pawns"][pawn_i]

                if pw["state"] != "finished":
                    # Use animation position if this pawn is being animated
                    if ludo_anim_active and pi == ludo_anim_pi and pawn_i == ludo_anim_pai:
                        if ludo_anim_idx < len(ludo_anim_path):
                            $ pw_colrow = ludo_anim_path[ludo_anim_idx]
                        else:
                            $ pw_colrow = _ludo_pawn_colrow(pw, gp_cdata)
                    else:
                        $ pw_colrow = _ludo_pawn_colrow(pw, gp_cdata)

                    # Compute stacking with animation awareness
                    if ludo_anim_active:
                        $ pw_stack = _ludo_get_pawns_at(ludo_game, pw_colrow, ludo_anim_pi, ludo_anim_pai, ludo_anim_path[ludo_anim_idx] if ludo_anim_idx < len(ludo_anim_path) else None)
                    else:
                        $ pw_stack = _ludo_get_pawns_at(ludo_game, pw_colrow)
                    $ pw_stack_idx = 0
                    for si in range(len(pw_stack)):
                        if pw_stack[si][0] == pi and pw_stack[si][1] == pawn_i:
                            $ pw_stack_idx = si

                    $ pw_offset = _ludo_get_stack_offset(pw_stack_idx, len(pw_stack))
                    $ pw_px = _ludo_get_pixel_pos(pw_colrow[0], pw_colrow[1], board_x, board_y, cell_size)
                    $ pw_x = pw_px[0] - pawn_size // 2 + pw_offset[0]
                    $ pw_y = pw_px[1] - pawn_size // 2 + pw_offset[1]
                    $ pw_img = "images/UI/OC_" + gp_code.upper() + ".webp"

                    # Check if this pawn is a valid move target for hero
                    $ pw_is_valid = False
                    if is_hero_turn and game_phase == "choose" and not ludo_anim_active:
                        for vm in ludo_valid_moves:
                            if vm[0] == pawn_i and pi == cur_turn:
                                $ pw_is_valid = True

                    if pw_is_valid:
                        button:
                            pos (pw_x - 4, pw_y - 4)
                            xysize (pawn_size + 8, pawn_size + 8)
                            background gp_cdata["hex"]
                            hover_background "#FFFFFF"
                            hover_sound None
                            activate_sound None
                            action [
                                Function(_ludo_start_hero_anim, ludo_game, cur_turn, pawn_i, [mt for pi2, mt in ludo_valid_moves if pi2 == pawn_i][0]),
                            ]
                            add pw_img:
                                xysize (pawn_size, pawn_size)
                                xalign 0.5
                                yalign 0.5
                    else:
                        frame:
                            pos (pw_x - 3, pw_y - 3)
                            xysize (pawn_size + 6, pawn_size + 6)
                            background gp_cdata["hex_dark"] + "80"
                            add pw_img:
                                xysize (pawn_size, pawn_size)
                                xalign 0.5
                                yalign 0.5

        # --------------------------------------------------
        # Left Panel: Player info + Dice & Controls
        # --------------------------------------------------
        frame:
            background "#000000B0"
            xpos 0
            ypos 0
            xsize panel_width
            ysize 1080

            vbox:
                xalign 0.5
                yalign 0.0
                spacing 12
                xsize panel_width - 20
                yoffset 15

                text renpy.translate_string("{size=+15}{b}Ludo{/b}{/size}") xalign 0.5

                # --- Player list ---
                for pi in range(len(ludo_game["players"])):
                    $ lp = ludo_game["players"][pi]
                    $ lp_hex = LUDO_COLORS[lp["color"]]["hex"]
                    $ lp_active = (pi == cur_turn)
                    $ lp_img = "images/UI/OC_" + lp["code"].upper() + ".webp"
                    $ lp_name = _ludo_get_player_name(lp["code"])

                    frame:
                        xsize panel_width - 30
                        xalign 0.5
                        if lp_active:
                            background lp_hex + "40"
                        else:
                            background "#00000040"
                        padding (10, 8)

                        hbox:
                            spacing 12
                            yalign 0.5

                            add lp_img:
                                xysize (55, 55)
                                yalign 0.5

                            vbox:
                                spacing 3
                                text renpy.translate_string("{color=") + lp_hex + "}{b}" + lp_name + "{/b}{/color}" size 22
                                text renpy.translate_string("Score: ") + str(lp["score"]) + "/" + str(ludo_pawn_count) size 18
                                if lp_active:
                                    text renpy.translate_string("{color=#FFFF64}◄ Turn{/color}") size 14

                # --- Separator ---
                null height 5
                frame:
                    xsize panel_width - 40
                    ysize 2
                    xalign 0.5
                    background "#FFFFFF30"
                null height 5

                # --- Current turn: portrait + dice + controls ---
                $ cp_img = "images/UI/OC_" + cur_code.upper() + ".webp"
                $ cp_hex = LUDO_COLORS[cur_color]["hex"]

                hbox:
                    xalign 0.5
                    spacing 20
                    yalign 0.5

                    # Current player portrait
                    vbox:
                        spacing 5
                        add cp_img:
                            xysize (90, 90)
                            xalign 0.5
                        text renpy.translate_string("{color=") + cp_hex + "}{b}" + _ludo_get_player_name(cur_code) + "{/b}{/color}":
                            xalign 0.5
                            size 20

                    # Dice display
                    if ludo_game["dice_value"] is not None:
                        frame:
                            yalign 0.5
                            xysize (100, 100)
                            background "#FFFFFF"
                            text renpy.translate_string("{color=#000000}{size=+50}{b}") + str(ludo_game["dice_value"]) + "{/b}{/size}{/color}":
                                xalign 0.5
                                yalign 0.5
                    else:
                        frame:
                            yalign 0.5
                            xysize (100, 100)
                            background "#FFFFFF40"
                            text renpy.translate_string("{color=#FFFFFF40}{size=+50}{b}?{/b}{/size}{/color}"):
                                xalign 0.5
                                yalign 0.5

                # --- Controls & Messages ---
                if is_hero_turn and game_phase == "roll" and ludo_npc_state == "idle" and not ludo_anim_active:
                    textbutton renpy.translate_string("{b}Roll!{/b}"):
                        xalign 0.5
                        xsize 200
                        ysize 60
                        background "#44AA44"
                        hover_background "#66CC66"
                        hover_sound None
                        activate_sound None
                        text_color "#FFFFFF"
                        text_size 28
                        text_xalign 0.5
                        text_yalign 0.5
                        action [
                            Play("SE1", "ButtonCLICK.ogg"),
                            SetScreenVariable("ludo_game", _ludo_do_roll(ludo_game)),
                            SetScreenVariable("ludo_valid_moves", []),
                            SetScreenVariable("ludo_npc_state", "post_roll"),
                            SetScreenVariable("ludo_event_timer", 1.0),
                        ]

                elif is_hero_turn and ludo_npc_state == "post_roll":
                    $ rolled_val = ludo_game["dice_value"]
                    if rolled_val == 6:
                        text renpy.translate_string("{color=#64FF64}{size=+5}{b}You rolled a 6!{/b}{/size}{/color}") xalign 0.5
                    else:
                        text renpy.translate_string("{color=#FFFF64}{size=+5}Rolled: [rolled_val]{/size}{/color}") xalign 0.5

                elif game_phase == "choose" and is_hero_turn and not ludo_anim_active:
                    text renpy.translate_string("{color=#FFFF64}Choose a pawn{/color}") xalign 0.5 size 20

                elif game_phase == "roll" and not is_hero_turn:
                    text renpy.translate_string("{color=#AAAAAA}Thinking...{/color}") xalign 0.5 size 18

                if ludo_game["extra_turn"]:
                    text renpy.translate_string("{color=#64FF64}Extra Turn!{/color}") xalign 0.5 size 18

                if ludo_message:
                    text renpy.translate_string("{size=+2}") + ludo_message + "{/size}" xalign 0.5 text_align 0.5

                # --- Instant-mode toggle ---
                null height 8
                textbutton ("{b}⚡ Instant: ON{/b}" if ludo_instant else "⚡ Instant: OFF"):
                    xalign 0.5
                    xsize 200
                    ysize 40
                    if ludo_instant:
                        background "#FFB000"
                        hover_background "#FFD964"
                        text_color "#000000"
                    else:
                        background "#444444"
                        hover_background "#666666"
                        text_color "#FFFFFF"
                    hover_sound None
                    activate_sound None
                    text_size 18
                    text_xalign 0.5
                    text_yalign 0.5
                    action ToggleScreenVariable("ludo_instant")

        # --------------------------------------------------
        # Turn Logic
        # --------------------------------------------------

        # --- Animation step processing ---
        if ludo_anim_active and ludo_anim_delay <= 0:
            python:
                if ludo_instant:
                    # Skip the walk: jump pawn directly to its destination
                    ludo_anim_idx = len(ludo_anim_path) - 1
                if ludo_anim_idx < len(ludo_anim_path) - 1:
                    ludo_anim_idx += 1
                    renpy.play("audio/SE/Bounce3.mp3", "SE1")
                    ludo_anim_delay = renpy.random.uniform(0.05, 0.15)
                else:
                    # Animation done - execute the actual move
                    events = _ludo_execute_move(ludo_game, ludo_anim_pi, ludo_anim_pai, ludo_anim_move_type)
                    mover_code = ludo_game["players"][ludo_anim_pi]["code"]
                    if events.get("kill"):
                        renpy.play("BeepWrong.ogg", "SE2")
                        ki = events["kill"]
                        killed_name = _ludo_get_player_name(ludo_game["players"][ki[0]]["code"])
                        ludo_message = "{color=#FF6464}" + killed_name + "'s pawn sent home!{/color}"
                        if mover_code == "hero":
                            _ludo_apply_love_for_player_kill(ludo_game, ki[0])
                        elif ludo_game["players"][ki[0]]["code"] == "hero":
                            _ludo_apply_love_for_npc_kill_player(ludo_game, ludo_anim_pi)
                    elif events.get("finished"):
                        renpy.play("JingleRight.ogg", "SE2")
                        ludo_message = "{color=#64FF64}" + _ludo_get_player_name(mover_code) + " scored!{/color}"
                        if mover_code == "hero":
                            _ludo_apply_love_for_player_finish(ludo_game, ludo_anim_pi)
                        else:
                            _ludo_apply_love_for_npc_finish(ludo_game, ludo_anim_pi)
                    elif ludo_anim_move_type == "release":
                        renpy.play("BeepRight.ogg", "SE1")
                    ludo_anim_active = False
                    ludo_npc_state = "post_move"
                    ludo_event_timer = 0.5

        # --- Hero post-roll: compute valid moves ---
        if is_hero_turn and ludo_npc_state == "post_roll" and ludo_event_timer <= 0 and not ludo_anim_active:
            python:
                ludo_valid_moves = _ludo_get_valid_moves(ludo_game, cur_turn)
                if len(ludo_valid_moves) == 0:
                    ludo_message = "{color=#FF6464}No valid moves!{/color}"
                    ludo_npc_state = "no_moves"
                    ludo_event_timer = 0.8
                elif len(ludo_valid_moves) == 1:
                    mv = ludo_valid_moves[0]
                    _ludo_start_anim(ludo_game, cur_turn, mv[0], mv[1])
                else:
                    ludo_game["phase"] = "choose"
                    ludo_npc_state = "idle"

        # --- Post-move (both hero and NPC) ---
        if ludo_npc_state == "post_move" and ludo_event_timer <= 0 and not ludo_anim_active:
            python:
                winner = _ludo_check_game_over(ludo_game)
                if winner:
                    ludo_game["winner"] = winner
                    ludo_phase = "result"
                    ludo_npc_state = "idle"
                else:
                    _ludo_advance_turn(ludo_game)
                    ludo_valid_moves = []
                    ludo_message = ""
                    ludo_npc_state = "wait_next"
                    ludo_event_timer = 0.05

        # --- No moves (both hero and NPC) ---
        if ludo_npc_state == "no_moves" and ludo_event_timer <= 0 and not ludo_anim_active:
            python:
                _ludo_advance_turn(ludo_game)
                ludo_valid_moves = []
                ludo_message = ""
                ludo_npc_state = "wait_next"
                ludo_event_timer = 0.05

        # --- Wait for next turn (forces fresh render cycle so $ variables update) ---
        if ludo_npc_state == "wait_next" and ludo_event_timer <= 0:
            $ ludo_npc_state = "idle"

        # --- NPC turn: start rolling ---
        if not is_hero_turn and game_phase == "roll" and ludo_npc_state == "idle" and not ludo_anim_active:
            $ ludo_npc_state = "npc_rolling"
            $ ludo_event_timer = 0.5

        # --- NPC roll ---
        if not is_hero_turn and ludo_npc_state == "npc_rolling" and ludo_event_timer <= 0:
            python:
                renpy.play("ButtonCLICK.ogg", "SE1")
                ludo_game = _ludo_do_roll(ludo_game)
                ludo_valid_moves = _ludo_get_valid_moves(ludo_game, cur_turn)
                if len(ludo_valid_moves) == 0:
                    ludo_message = "{color=#AAAAAA}" + _ludo_get_player_name(cur_code) + ": No moves{/color}"
                    ludo_npc_state = "no_moves"
                    ludo_event_timer = 0.8
                else:
                    ludo_npc_state = "npc_choosing"
                    ludo_event_timer = 0.8

        # --- NPC choose and animate ---
        if not is_hero_turn and ludo_npc_state == "npc_choosing" and ludo_event_timer <= 0 and not ludo_anim_active:
            python:
                choice = _ludo_npc_choose(ludo_game, cur_turn, ludo_valid_moves)
                if choice:
                    _ludo_start_anim(ludo_game, cur_turn, choice[0], choice[1])

        # --- Tick timer ---
        timer 0.05 repeat True action [
            SetScreenVariable("ludo_tick", ludo_tick + 1),
            If(ludo_instant, SetScreenVariable("ludo_event_timer", 0.0), []),
            If(ludo_instant, SetScreenVariable("ludo_anim_delay", 0.0), []),
            If(ludo_event_timer > 0, SetScreenVariable("ludo_event_timer", max(0.0, ludo_event_timer - 0.05)), []),
            If(ludo_anim_active and ludo_anim_delay > 0, SetScreenVariable("ludo_anim_delay", max(0.0, ludo_anim_delay - 0.05)), []),
        ]

    # ==========================================
    # Phase: Result
    # ==========================================
    elif ludo_phase == "result" and ludo_game is not None:
        add "images/Mechanics/Ludo/ludo_board.webp":
            xysize (board_size, board_size)
            pos (board_x, board_y)
            alpha 0.2

        frame:
            background "#000000D8"
            xysize (1920, 1080)

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 25

                $ winner_code = ludo_game["winner"]
                $ winner_img = "images/UI/OC_" + winner_code.upper() + ".webp"
                $ winner_name = _ludo_get_player_name(winner_code)

                $ winner_hex = "#FFFFFF"
                for wp in ludo_game["players"]:
                    if wp["code"] == winner_code:
                        $ winner_hex = LUDO_COLORS[wp["color"]]["hex"]

                add winner_img:
                    xysize (200, 200)
                    xalign 0.5

                text renpy.translate_string("{color=") + winner_hex + "}{size=+40}{b}" + winner_name + "{/b}{/size}{/color}" xalign 0.5
                text renpy.translate_string("{size=+30}{b}Winner!{/b}{/size}") xalign 0.5

                null height 20

                text renpy.translate_string("{b}Final Scores:{/b}") xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 40
                    for rp in ludo_game["players"]:
                        $ rp_hex = LUDO_COLORS[rp["color"]]["hex"]
                        $ rp_img = "images/UI/OC_" + rp["code"].upper() + ".webp"
                        vbox:
                            spacing 5
                            add rp_img:
                                xysize (80, 80)
                                xalign 0.5
                            text renpy.translate_string("{color=") + rp_hex + "}" + _ludo_get_player_name(rp["code"]) + "{/color}" xalign 0.5 size 20
                            text str(rp["score"]) + "/" + str(ludo_pawn_count) xalign 0.5 size 22

                null height 20
                text renpy.translate_string("[C_Dat]{size=+30}{b}Click to continue{/b}[C_Off]") xalign 0.5

        python:
            ludo_result = [ludo_game["winner"], ludo_pawn_count]

        key "mouseup_1" action Return(ludo_result)

    modal True

# ----------------------------------------------------------------------------------------------------
init python:
# ----------------------------------------------------------------------------------------------------

    def _ludo_do_roll(game_state):
        """Roll dice and store in game state. Returns the modified game_state.
        Stuck-in-base players accumulate +5% per pawn-in-base toward forcing a 6
        next turn; any 6 (natural or forced) resets the streak."""
        cur_idx = game_state["current_turn"]
        player = game_state["players"][cur_idx]
        bonus = player.get("bonus_six", 0.0)

        if bonus > 0.0 and renpy.random.random() < bonus:
            dice = 6
        else:
            dice = _ludo_roll_dice()
        game_state["dice_value"] = dice

        in_base = sum(1 for p in player["pawns"] if p["state"] == "spawn")
        all_in_base = (in_base == len(player["pawns"]))

        if dice == 6:
            player["bonus_six"] = 0.0
        elif all_in_base:
            player["bonus_six"] = bonus + 0.05 * in_base

        return game_state

    def _ludo_start_anim(game_state, player_idx, pawn_idx, move_type):
        """Start pawn movement animation. Sets screen variables via current_screen scope.
        Must return None so Function() doesn't dismiss the screen."""
        player = game_state["players"][player_idx]
        color_data = LUDO_COLORS[player["color"]]
        pawn = player["pawns"][pawn_idx]

        path = _ludo_compute_move_path(pawn, game_state["dice_value"], color_data, move_type)

        cs = renpy.current_screen()
        if cs is None:
            return
        scope = cs.scope
        scope["ludo_anim_active"] = True
        scope["ludo_anim_path"] = path
        scope["ludo_anim_idx"] = 0
        scope["ludo_anim_pi"] = player_idx
        scope["ludo_anim_pai"] = pawn_idx
        scope["ludo_anim_move_type"] = move_type
        scope["ludo_anim_delay"] = renpy.random.uniform(0.05, 0.15)
        scope["ludo_npc_state"] = "animating"
        # Play first step sound
        if len(path) > 0:
            renpy.play("audio/SE/Bounce3.mp3", "SE1")
        renpy.restart_interaction()

    def _ludo_start_hero_anim(game_state, player_idx, pawn_idx, move_type):
        """Start hero pawn animation from button click.
        Must return None so Function() doesn't dismiss the screen."""
        # Guard: Ren'Py can fire this action again from the same rendered frame before a re-draw. The dict mutation persists across those rapid calls, so checking it here is the only reliable way to block a double-move.
        if game_state["phase"] != "choose":
            return
        game_state["phase"] = "moving"
        _ludo_start_anim(game_state, player_idx, pawn_idx, move_type)

    def _ludo_hero_pick_color(color_name, players):
        """Handle hero color selection with turn-based NPC competition.
        When hero loses, all NPCs also lock in their picks for this round.
        Must return None so Function() doesn't dismiss the screen."""
        cs = renpy.current_screen()
        if cs is None:
            return
        scope = cs.scope

        current = dict(scope.get("ludo_color_assignments", {}))
        lost = list(scope.get("ludo_hero_lost_colors", []))
        taken = set(current.values())
        available = [c for c in LUDO_COLOR_ORDER if c not in taken]
        unassigned_npcs = [p for p in players if p != "hero" and p not in current]

        # Each unassigned NPC picks their top available preference
        contester = None
        for npc in unassigned_npcs:
            prefs = LUDO_NPC_PREFS.get(npc, [])
            npc_top = None
            for pref in prefs:
                if pref in available:
                    npc_top = pref
                    break
            if npc_top == color_name:
                contester = npc
                break

        hero_won = True
        if contester:
            hero_won = renpy.random.random() < 0.5

        if hero_won:
            # Hero gets the color, assign all remaining NPCs
            current["hero"] = color_name
            for npc in unassigned_npcs:
                if npc not in current:
                    prefs = LUDO_NPC_PREFS.get(npc, [])
                    avail = [c for c in LUDO_COLOR_ORDER if c not in current.values()]
                    assigned = False
                    for pref in prefs:
                        if pref in avail:
                            current[npc] = pref
                            assigned = True
                            break
                    if not assigned and avail:
                        current[npc] = renpy.random.choice(avail)
            scope["ludo_color_assignments"] = current
            scope["ludo_hero_color"] = color_name
        else:
            # Hero lost - contesting NPC gets the color
            current[contester] = color_name
            lost.append(color_name)
            # All other unassigned NPCs also pick their top preference now
            for npc in unassigned_npcs:
                if npc not in current:
                    prefs = LUDO_NPC_PREFS.get(npc, [])
                    avail = [c for c in LUDO_COLOR_ORDER if c not in current.values()]
                    assigned = False
                    for pref in prefs:
                        if pref in avail:
                            current[npc] = pref
                            assigned = True
                            break
                    if not assigned and avail:
                        current[npc] = renpy.random.choice(avail)
            scope["ludo_color_assignments"] = current
            scope["ludo_hero_lost_colors"] = lost
            # If only one color left, auto-assign hero
            hero_remaining = [c for c in LUDO_COLOR_ORDER if c not in current.values()]
            if len(hero_remaining) == 1:
                current["hero"] = hero_remaining[0]
                scope["ludo_color_assignments"] = current
                scope["ludo_hero_color"] = hero_remaining[0]

        renpy.restart_interaction()
