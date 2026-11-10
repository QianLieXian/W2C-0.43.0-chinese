# ----------------------------------------------------------------------------------------------------
label memory_game:
# ----------------------------------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_136
    menu:
        "Player{fast}"
        "0":
            $ a_event_1 = 0
        "1":
            $ a_event_1 = 1
        "2":
            $ a_event_1 = 2
        "3":
            $ a_event_1 = 3
    menu:
        "CPU{fast}"
        "1":
            $ a_event_2 = 1
        "2":
            $ a_event_2 = 2
        "3":
            $ a_event_2 = 3
        "4":
            $ a_event_2 = 4

    menu:
        "NPC{fast}"

        "0":
            call screen minigame_memory(a_event_1, a_event_2)

        "1":
            call screen minigame_memory_coop(a_event_1, a_event_2, ["wnei", "wsis"])

    jump show_ui

# ----------------------------------------------------------------------------------------------------
init python:
# ----------------------------------------------------------------------------------------------------
    def generate_cards(card_amount):
        # Emoji-only identity. Colors were dropped because recent Ren'Py
        # versions no longer recolor these glyphs, so "same emoji, different
        # color" pairs looked identical and made the game unfair. The pool
        # must hold at least as many distinct symbols as the maximum pair
        # count (current grid cap is 10*5 = 50 cards => 25 pairs).
        symbols = [
            "♥", "♦", "♣", "♠", "★",
            "🍓", "🍁", "🍄", "🥕", "🥒",
            "🐵", "🐶", "🐺", "🐱", "🦁",
            "🐯", "🦒", "🦊", "🦝", "🐮",
            "🐷", "🐗", "🐭", "🐹", "🐰",
            "🐻", "🐨", "🐼", "🐸", "🍑",
            "🐴", "🍌", "🐔", "🐲", "🐒", "🍆",
            "🍎", "🍊", "🍋", "🍇", "🍉",
            "🍒", "🍍", "🥝", "🌽", "🌷",
            "🍕", "🍔", "🍩", "🍪", "🚗",
            "🚀", "⚽", "🎸", "💎",
            "🌞", "🌙", "🔥", "⭐",
        ]
        pairs_needed = card_amount // 2
        chosen = renpy.random.sample(symbols, pairs_needed)
        cards = []
        for symbol in chosen:
            cards.append([symbol, "deselected", "visible"])
            cards.append([symbol, "deselected", "visible"])
        renpy.random.shuffle(cards)
        return cards

    def memory_select_card(cards, selected_cards, card_index):
        cards[card_index][1] = "selected"
        selected_cards.append(card_index)

    def memory_deselect_cards(cards, selected_cards):
        if len(selected_cards) == 2:
            for card in cards:
                if card[1] == "selected":
                    card[1] = "deselected"
        selected_cards[:] = []

    def memory_hide_matches(cards, selected_cards):
        cards[selected_cards[0]][2] = "hidden"
        cards[selected_cards[1]][2] = "hidden"
        selected_cards[:] = []

# ----------------------------------------------------------------------------------------------------
style memory_button:
# ----------------------------------------------------------------------------------------------------
    background "#3232327D"
    hover_background "#00000064"
    xsize 150
    ysize 150
    size 50
    xalign 0.5
    yalign 0.5

# ----------------------------------------------------------------------------------------------------
style memory_button_text:
# ----------------------------------------------------------------------------------------------------
    color "#C8C8C8"
    hover_color "#FFFFFF"
    size 50
    xalign 0.5
    yalign 0.5

# ----------------------------------------------------------------------------------------------------
screen minigame_memory(var_pla=0, var_cpu=1, var_txt=None, var_mod="classic", var_tim=30, var_sca=1):
# ----------------------------------------------------------------------------------------------------
    # Initialize screen variables
    default game_started = False
    # effective_cpu mirrors var_cpu but grows by var_sca after each completed board in continuous mode; row counts read from it instead of var_cpu.
    default effective_cpu = var_cpu
    default card_rows_h = min(10, (effective_cpu + 1) * 2)  # Horizontal: max 10
    default card_rows_v = min(5, effective_cpu + 1)  # Vertical: max 5
    default card_amount = card_rows_h * card_rows_v
    default actual_card_amount = card_amount if card_amount % 2 == 0 else card_amount - 1
    default cards = generate_cards(actual_card_amount)
    default selected_cards = []
    default hidden_cards = 0
    default match_found = False
    default points = 0
    default peek_uses = 1 if var_pla >= 2 else 0
    default peek_active = True if var_pla >= 1 else False
    default correct_streak = 0
    default fail_streak = 0
    # Continuous-mode countdown; ignored in classic mode.
    default time_left = float(var_tim) if var_tim else 0.0

    # --------------------------------------------------
    # Preparation Screen
    # --------------------------------------------------
    if not game_started:
        frame:
            background "#000000C8"
            xysize (1920,1080)
            vbox:
                xalign 0.5
                yalign 0.5
                label renpy.translate_string("{size=+80}{b}Memory Game{/b}{/size}") xalign 0.5
                vbox:
                    xalign 0.5
                    xysize (960, 400)
                    if var_txt == None:
                        if var_mod == "continuous":
                            text renpy.translate_string("Score as many matches as you can before time runs out! Each cleared board grows the grid for the next round, and your score, streak, and peeks all carry over.")
                            text renpy.translate_string("\n{color=#FFAF64}Time:{/color} [var_tim]s")
                        else:
                            text renpy.translate_string("Match pairs of identical cards by clicking on them. Each successful match earns you points based on your streak. Failed attempts cost points based on consecutive failures. Complete all pairs to finish!")
                        if var_pla >= 1:
                            text renpy.translate_string("\n{color=#64FF64}Advantages:{/color}")
                            if var_pla >= 1:
                                text renpy.translate_string("• Start with 5 seconds to view all cards")
                            if var_pla >= 2:
                                text renpy.translate_string("• 1 peek button (reveals all cards for 5 seconds)")
                            if var_pla >= 3:
                                text renpy.translate_string("• Gain +1 peek for every 3 consecutive matches")
                    else:
                        text var_txt
                text renpy.translate_string("[C_Dat]{size=+40}{b}Click to start!{/b}[C_Off]") xalign 0.5

        key "mouseup_1" action [SetScreenVariable("game_started", True)]
    
    # --------------------------------------------------
    # Game Started
    # --------------------------------------------------
    else:
        # Left sidebar - Buttons
        frame:
            at alpha_dissolve
            xalign 0.0
            yalign 0.0
            xsize 200
            ysize 1080
            background "#00000080"
            
            vbox:
                xalign 0.5
                spacing 20
                xsize 200
                ysize 1080
                
                # Top buttons
                vbox:
                    xalign 0.5
                    yalign 0.0
                    spacing 15

                    if var_mod == "continuous":
                        $ _time_disp = "{:.1f}".format(time_left)
                        text renpy.translate_string("Time\n[_time_disp]s") style "memory_button_text" size 30 xalign 0.5
                        bar value time_left range float(var_tim) xsize 180 ysize 16 xalign 0.5

                    text renpy.translate_string("Score\n[points]") style "memory_button_text" size 35 xalign 0.5

                    if correct_streak > 0:
                        text renpy.translate_string("Streak\n{color=#64FF64}[correct_streak]{/color}") size 25 xalign 0.5

                    if fail_streak > 0:
                        text renpy.translate_string("Fails\n{color=#FF6464}[fail_streak]{/color}") size 25 xalign 0.5

                    if peek_uses > 0 and not peek_active:
                        textbutton renpy.translate_string("Peek\n([peek_uses])"):
                            xalign 0.5
                            xsize 180
                            ysize 100
                            action [
                                SetScreenVariable("peek_active", True),
                                SetScreenVariable("peek_uses", peek_uses - 1)
                            ]
                            style "memory_button"
                            text_style "memory_button_text"
                            text_size 30
                
                # Bottom quit button
                null height 600
                
                textbutton renpy.translate_string("Quit"):
                    xalign 0.5
                    yalign 1.0
                    xsize 180
                    ysize 80
                    action Return(points)
                    style "memory_button"
                    text_style "memory_button_text"
                    text_size 35
        
        # Right area - Cards
        frame:
            at alpha_dissolve
            xpos 200
            yalign 0.0
            xsize 1720
            ysize 1080
            background "#00000000"
            
            grid card_rows_h card_rows_v:
                xalign 0.5
                yalign 0.5
                spacing 10
                
                for i in range(card_amount):
                    if i < actual_card_amount:
                        $ card = cards[i]
                        button:
                            style "memory_button"
                            
                            if card[1] == "deselected" and card[2] == "visible":
                                if peek_active:
                                    text str(card[0]) size 100 xalign 0.5 yalign 0.5
                                else:
                                    text "?" size 100 xalign 0.5 yalign 0.5
                                sensitive If(len(selected_cards) != 2, True, False)
                                action [
                                    Function(memory_select_card, cards, selected_cards, i),
                                    If(peek_active, SetScreenVariable("peek_active", False), NullAction())
                                ]
                            elif card[1] == "selected" and card[2] == "visible":
                                text str(card[0]) size 100 xalign 0.5 yalign 0.5
                            else:
                                fixed:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 5
                                    text str(card[0]) size 100 xalign 0.5 yalign 0.5
                                    text renpy.translate_string("[C_Pos]✔[C_Off]") size 75 xalign 0.95 yalign 0.05
                    else:
                        null

        # Game logic
        python:
            if len(selected_cards) == 2 and cards[selected_cards[0]][0] == cards[selected_cards[1]][0]:
                match_found = True
            elif len(selected_cards) == 2:
                match_found = False

        if match_found and len(selected_cards) == 2:
            timer 0.01 action [
                Function(memory_hide_matches, cards, selected_cards),
                Play("SE1", "BeepRight.ogg"),
                SetScreenVariable("hidden_cards", hidden_cards + 2),
                SetScreenVariable("match_found", False),
                SetScreenVariable("correct_streak", correct_streak + 1),
                SetScreenVariable("fail_streak", 0),
                SetScreenVariable("points", points + (1 + correct_streak)),
                If(var_pla >= 3 and (correct_streak + 1) % 3 == 0, 
                    SetScreenVariable("peek_uses", peek_uses + 1), 
                    NullAction())
            ] repeat False
        elif len(selected_cards) == 2 and not match_found:
            $ point_loss = 0.5 * fail_streak if fail_streak > 0 else 0
            $ new_points = max(0, points - point_loss)
            timer 0.01 action [
                Play("SE1", "BeepWrong.ogg"),
            ] repeat False
            timer 0.5 action [
                Function(memory_deselect_cards, cards, selected_cards),
                SetScreenVariable("fail_streak", fail_streak + 1),
                SetScreenVariable("correct_streak", 0),
                SetScreenVariable("points", new_points)
            ] repeat False
        
        if hidden_cards >= actual_card_amount:
            if var_mod == "continuous":
                # Bump difficulty, regenerate the board, keep score/streak/timer.
                $ _new_cpu = effective_cpu + var_sca
                $ _new_h = min(10, (_new_cpu + 1) * 2)
                $ _new_v = min(5, _new_cpu + 1)
                $ _new_amount = _new_h * _new_v
                $ _new_actual = _new_amount if _new_amount % 2 == 0 else _new_amount - 1
                timer 0.5 action [
                    Play("SE2", "JingleRight.ogg"),
                    SetScreenVariable("effective_cpu", _new_cpu),
                    SetScreenVariable("card_rows_h", _new_h),
                    SetScreenVariable("card_rows_v", _new_v),
                    SetScreenVariable("card_amount", _new_amount),
                    SetScreenVariable("actual_card_amount", _new_actual),
                    SetScreenVariable("cards", generate_cards(_new_actual)),
                    SetScreenVariable("hidden_cards", 0),
                    SetScreenVariable("selected_cards", []),
                    SetScreenVariable("match_found", False),
                    SetScreenVariable("peek_active", True if var_pla >= 1 else False),
                ] repeat False
            else:
                timer 0.01 action Return(points) repeat False

        # Continuous-mode countdown — Return(points) the moment time runs out.
        if var_mod == "continuous":
            if time_left <= 0:
                timer 0.01 action Return(points) repeat False
            else:
                timer 0.1 repeat True action SetScreenVariable("time_left", max(0.0, time_left - 0.1))

        if peek_active:
            timer 5.0 action SetScreenVariable("peek_active", False) repeat False

    modal True

# ----------------------------------------------------------------------------------------------------
init python:
# ----------------------------------------------------------------------------------------------------
    def get_npc_intelligence(var_npc):
        """Get intelligence value from var_npc parameter"""
        if isinstance(var_npc, (int, float)):
            return var_npc
        elif isinstance(var_npc, str):
            return stat_value(var_npc, "int")
        elif isinstance(var_npc, list):
            # Return list of intelligences
            return [get_npc_intelligence(npc) for npc in var_npc]
        return 0
    
    def get_npc_memory_slots(intelligence):
        """Calculate how many cards an NPC can remember based on intelligence (0-100)"""
        return int((intelligence / 100.0) * 6)
    
    def add_to_npc_memory(npc_memory, card_index, card_value, max_slots):
        """Add a card to NPC memory with smart forgetting logic"""
        if max_slots == 0:
            return
        
        # Don't add if already in memory
        for mem_card in npc_memory:
            if mem_card[0] == card_index:
                return
        
        # Find pairs in current memory
        pairs_in_memory = []
        unpaired_in_memory = []
        
        for i, mem_card in enumerate(npc_memory):
            has_pair = False
            for j, other_card in enumerate(npc_memory):
                if i != j and mem_card[1] == other_card[1]:
                    has_pair = True
                    if i not in pairs_in_memory and j not in pairs_in_memory:
                        pairs_in_memory.extend([i, j])
                    break
            if not has_pair:
                unpaired_in_memory.append(i)
        
        # Check if new card makes a pair with existing memory
        makes_pair_with = None
        for i, mem_card in enumerate(npc_memory):
            if mem_card[1] == card_value:
                makes_pair_with = i
                break
        
        # Add the new card
        new_card = (card_index, card_value)
        
        # If memory is not full, just add
        if len(npc_memory) < max_slots:
            npc_memory.append(new_card)
        else:
            # Memory is full, need to forget something
            # If all cards have pairs (or all -1 if odd number), keep pairs until matched
            if len(unpaired_in_memory) == 0 or (len(unpaired_in_memory) == 1 and len(npc_memory) % 2 == 1):
                # All paired, don't add new card unless it makes a pair
                if makes_pair_with is not None:
                    # Find first unpaired or oldest card to remove
                    npc_memory.pop(0)
                    npc_memory.append(new_card)
            else:
                # Remove first unpaired card (but not the one that pairs with new card)
                for i in unpaired_in_memory:
                    if makes_pair_with is None or i != makes_pair_with:
                        npc_memory.pop(i)
                        npc_memory.append(new_card)
                        break
    
    def remove_from_npc_memory(npc_memory, card_index1, card_index2):
        """Remove matched pair from NPC memory"""
        npc_memory[:] = [card for card in npc_memory if card[0] != card_index1 and card[0] != card_index2]

    def remove_matched_from_all_npcs(npc_memories, card_index1, card_index2):
        """Remove matched pair from all NPC memories"""
        for mem in npc_memories:
            remove_from_npc_memory(mem, card_index1, card_index2)
    
    def npc_find_pair_in_memory(npc_memory):
        """Find a known pair in NPC memory"""
        for i, card1 in enumerate(npc_memory):
            for j, card2 in enumerate(npc_memory):
                if i != j and card1[1] == card2[1]:
                    return (card1[0], card2[0])
        return None
    
    def npc_make_turn(cards, npc_memory, selected_cards):
        """NPC makes a turn - returns True if successful match, False otherwise"""
        # First, check if NPC knows a pair
        pair = npc_find_pair_in_memory(npc_memory)
        
        if pair:
            # Play the known pair
            first_card = pair[0]
            second_card = pair[1]
            
            # Select first card
            memory_select_card(cards, selected_cards, first_card)
            return ("select", first_card)
        else:
            # Pick a random unmatched card that's not in memory
            available_cards = []
            for i, card in enumerate(cards):
                if card[2] == "visible":
                    # Check if this card is already in memory
                    in_memory = False
                    for mem_card in npc_memory:
                        if mem_card[0] == i:
                            in_memory = True
                            break
                    if not in_memory:
                        available_cards.append(i)
            
            # If no unknown cards, just pick any visible card
            if not available_cards:
                available_cards = [i for i, card in enumerate(cards) if card[2] == "visible"]
            
            if available_cards:
                card_index = renpy.random.choice(available_cards)
                memory_select_card(cards, selected_cards, card_index)
                return ("select", card_index)
        
        return None

# ----------------------------------------------------------------------------------------------------
screen minigame_memory_coop(var_pla=1, var_cpu=1, var_npc=50, var_txt=None):
# ----------------------------------------------------------------------------------------------------
    # Initialize screen variables
    default game_started = False
    default card_rows_h = min(10, (var_cpu + 1) * 2)  # Horizontal: max 10
    default card_rows_v = min(5, var_cpu + 1)  # Vertical: max 5
    default card_amount = card_rows_h * card_rows_v
    default actual_card_amount = card_amount if card_amount % 2 == 0 else card_amount - 1
    default cards = generate_cards(actual_card_amount)
    default selected_cards = []
    default hidden_cards = 0
    default match_found = False
    default points = 0
    default peek_uses = 1 if var_pla >= 2 else 0
    default peek_active = False
    default correct_streak = 0
    default fail_streak = 0
    
    # NPC setup
    default npc_list = var_npc if isinstance(var_npc, list) else [var_npc]
    default npc_intelligences = [get_npc_intelligence(npc) for npc in npc_list]
    default npc_memory_slots = [get_npc_memory_slots(intel) for intel in npc_intelligences]
    default npc_memories = [[] for _ in npc_list]
    
    # Turn management
    default current_turn = 0
    default total_players = 1 + len(npc_list)
    default npc_turn_delay = 0
    default npc_action_state = "idle"
    default npc_first_card = None
    
    # --------------------------------------------------
    # Preparation Screen
    # --------------------------------------------------
    if not game_started:
        frame:
            background "#000000C8"
            xysize (1920,1080)
            vbox:
                xalign 0.5
                yalign 0.5
                label renpy.translate_string("{size=+80}{b}Memory Game - Co-Op{/b}{/size}") xalign 0.5
                vbox:
                    xalign 0.5
                    xysize (960, 400)
                    if var_txt == None:
                        text renpy.translate_string("Work together with your partner(s) to match all pairs! Take turns selecting cards. A successful match lets you continue; a failed match passes the turn to the next player.")
                        if var_pla >= 1:
                            text renpy.translate_string("\n{color=#64FF64}Your Advantages:{/color}")
                            if var_pla >= 1:
                                text renpy.translate_string("• Start with 5 seconds to view all cards")
                            if var_pla >= 2:
                                text renpy.translate_string("• 1 peek button (reveals all cards for 5 seconds)")
                            if var_pla >= 3:
                                text renpy.translate_string("• Gain +1 peek for every 3 consecutive team matches")
                    else:
                        text var_txt
                text renpy.translate_string("[C_Dat]{size=+40}{b}Click to start!{/b}[C_Off]") xalign 0.5
        
        key "mouseup_1" action [SetScreenVariable("game_started", True), SetScreenVariable("peek_active", True)]
    
    # --------------------------------------------------
    # Game Started
    # --------------------------------------------------
    else:
        # Left sidebar - Buttons
        frame:
            at alpha_dissolve
            xalign 0.0
            yalign 0.0
            xsize 200
            ysize 1080
            background "#00000080"
            
            vbox:
                xalign 0.5
                spacing 20
                xsize 200
                ysize 1080
                
                # Turn indicator with image
                vbox:
                    xalign 0.5
                    spacing 10
                    
                    # Character image
                    python:
                        if current_turn == 0:
                            turn_image = "images/UI/OC_HERO.webp"
                        else:
                            npc_index = current_turn - 1
                            npc_id = npc_list[npc_index]
                            if isinstance(npc_id, str):
                                turn_image = "images/UI/OC_" + npc_id.upper() + ".webp"
                            else:
                                turn_image = "images/UI/OC_NONE.webp"
                        
                        # Check if image exists, otherwise use OC_NONE
                        try:
                            renpy.loadable(turn_image)
                        except:
                            turn_image = "images/UI/OC_NONE.webp"
                    
                    image turn_image:
                        xalign 0.5
                        xysize (150, 150)
                    
                    # Turn text
                    if current_turn == 0:
                        text renpy.translate_string("{color=#64FF64}Your\nTurn{/color}") size 30 xalign 0.5
                    else:
                        python:
                            npc_index = current_turn - 1
                            npc_id = npc_list[npc_index]
                            if isinstance(npc_id, str):
                                # Get character name using fname variable
                                turn_name = eval("fname" + npc_id) if renpy.has_screen("fname" + npc_id) or "fname" + npc_id in globals() else npc_id.capitalize()
                            else:
                                turn_name = "NPC " + str(current_turn)
                        
                        text renpy.translate_string("{color=#FFFF64}") + turn_name + "\nTurn{/color}" size 28 xalign 0.5
                
                # Stats
                vbox:
                    xalign 0.5
                    spacing 15
                    
                    text renpy.translate_string("Score\n[points]") style "memory_button_text" size 35 xalign 0.5
                    
                    if correct_streak > 0:
                        text renpy.translate_string("Streak\n{color=#64FF64}[correct_streak]{/color}") size 25 xalign 0.5
                    
                    if fail_streak > 0:
                        text renpy.translate_string("Fails\n{color=#FF6464}[fail_streak]{/color}") size 25 xalign 0.5
                    
                    if peek_uses > 0 and not peek_active and current_turn == 0:
                        textbutton renpy.translate_string("Peek\n([peek_uses])"):
                            xalign 0.5
                            xsize 180
                            ysize 100
                            action [
                                SetScreenVariable("peek_active", True),
                                SetScreenVariable("peek_uses", peek_uses - 1)
                            ]
                            style "memory_button"
                            text_style "memory_button_text"
                            text_size 30
                
                # Bottom quit button
                null height 150
                
                textbutton renpy.translate_string("Quit"):
                    xalign 0.5
                    yalign 1.0
                    xsize 180
                    ysize 80
                    action Return(points)
                    style "memory_button"
                    text_style "memory_button_text"
                    text_size 35
        
        # Right area - Cards
        frame:
            at alpha_dissolve
            xpos 200
            yalign 0.0
            xsize 1720
            ysize 1080
            background "#00000000"
            
            grid card_rows_h card_rows_v:
                xalign 0.5
                yalign 0.5
                spacing 10
                
                for i in range(card_amount):
                    if i < actual_card_amount:
                        $ card = cards[i]
                        button:
                            style "memory_button"
                            
                            if card[1] == "deselected" and card[2] == "visible":
                                if peek_active:
                                    text str(card[0]) size 100 xalign 0.5 yalign 0.5
                                else:
                                    text "?" size 100 xalign 0.5 yalign 0.5
                                
                                if current_turn == 0:
                                    sensitive If(len(selected_cards) != 2, True, False)
                                    action [
                                        Function(memory_select_card, cards, selected_cards, i),
                                        If(peek_active, SetScreenVariable("peek_active", False), NullAction())
                                    ]
                                else:
                                    sensitive False
                                    
                            elif card[1] == "selected" and card[2] == "visible":
                                text str(card[0]) size 100 xalign 0.5 yalign 0.5
                            else:
                                fixed:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 5
                                    text str(card[0]) size 100 xalign 0.5 yalign 0.5
                                    text renpy.translate_string("[C_Pos]✔[C_Off]") size 75 xalign 0.95 yalign 0.05
                    else:
                        null

        # NPC AI Logic
        if current_turn > 0 and len(selected_cards) < 2:
            $ npc_index = current_turn - 1
            $ npc_mem = npc_memories[npc_index]
            $ npc_slots = npc_memory_slots[npc_index]
            
            if npc_action_state == "idle":
                $ npc_action_state = "selecting_first"
                $ npc_turn_delay = 1.0
            elif npc_action_state == "selecting_first" and npc_turn_delay <= 0:
                python:
                    pair = npc_find_pair_in_memory(npc_mem)
                    if pair:
                        first_idx = pair[0]
                    else:
                        available = []
                        for idx, c in enumerate(cards):
                            if c[2] == "visible":
                                is_in_memory = False
                                for m in npc_mem:
                                    if m[0] == idx:
                                        is_in_memory = True
                                        break
                                if not is_in_memory:
                                    available.append(idx)
                        
                        if not available:
                            available = [idx for idx, c in enumerate(cards) if c[2] == "visible"]
                        first_idx = renpy.random.choice(available) if available else None
                    
                    if first_idx is not None:
                        memory_select_card(cards, selected_cards, first_idx)
                        npc_first_card = first_idx
                        for mem_idx, mem in enumerate(npc_memories):
                            add_to_npc_memory(mem, first_idx, cards[first_idx][0], npc_memory_slots[mem_idx])
                        npc_action_state = "waiting"
                        npc_turn_delay = 1.0
            elif npc_action_state == "waiting" and npc_turn_delay <= 0:
                $ npc_action_state = "selecting_second"
                $ npc_turn_delay = 1.0
            elif npc_action_state == "selecting_second" and npc_turn_delay <= 0:
                python:
                    pair = npc_find_pair_in_memory(npc_mem)
                    if pair and npc_first_card == pair[0]:
                        second_idx = pair[1]
                    elif pair and npc_first_card == pair[1]:
                        second_idx = pair[0]
                    else:
                        available = [idx for idx, c in enumerate(cards) if c[2] == "visible" and idx not in selected_cards]
                        second_idx = renpy.random.choice(available) if available else None
                    
                    if second_idx is not None:
                        memory_select_card(cards, selected_cards, second_idx)
                        for mem_idx, mem in enumerate(npc_memories):
                            add_to_npc_memory(mem, second_idx, cards[second_idx][0], npc_memory_slots[mem_idx])
                        npc_action_state = "idle"
            
            if npc_turn_delay > 0:
                timer 0.1 repeat True action SetScreenVariable("npc_turn_delay", max(0, npc_turn_delay - 0.1))
        
        # Player card memory for NPCs
        python:
            if current_turn == 0 and len(selected_cards) > 0:
                for card_idx in selected_cards:
                    card_val = cards[card_idx][0]
                    for mem_idx, mem in enumerate(npc_memories):
                        already_known = any(m[0] == card_idx for m in mem)
                        if not already_known:
                            add_to_npc_memory(mem, card_idx, card_val, npc_memory_slots[mem_idx])

        # Match check
        python:
            if len(selected_cards) == 2 and cards[selected_cards[0]][0] == cards[selected_cards[1]][0]:
                match_found = True
            elif len(selected_cards) == 2:
                match_found = False

        if match_found and len(selected_cards) == 2:
            timer 0.5 action [
                Function(memory_hide_matches, cards, selected_cards),
                Play("SE1", "BeepRight.ogg"),
                SetScreenVariable("hidden_cards", hidden_cards + 2),
                SetScreenVariable("match_found", False),
                SetScreenVariable("correct_streak", correct_streak + 1),
                SetScreenVariable("fail_streak", 0),
                SetScreenVariable("points", points + (1 + correct_streak)),
                If(var_pla >= 3 and (correct_streak + 1) % 3 == 0, 
                    SetScreenVariable("peek_uses", peek_uses + 1), 
                    NullAction()),
                Function(remove_matched_from_all_npcs, npc_memories, selected_cards[0], selected_cards[1]),
            ] repeat False
        elif len(selected_cards) == 2 and not match_found:
            $ point_loss = 0.5 * fail_streak if fail_streak > 0 else 0
            $ new_points = max(0, points - point_loss)
            timer 0.5 action [
                Play("SE1", "BeepWrong.ogg"),
            ] repeat False
            timer 1.5 action [
                Function(memory_deselect_cards, cards, selected_cards),
                SetScreenVariable("fail_streak", fail_streak + 1),
                SetScreenVariable("correct_streak", 0),
                SetScreenVariable("points", new_points),
                SetScreenVariable("current_turn", (current_turn + 1) % total_players),
                SetScreenVariable("npc_action_state", "idle"),
            ] repeat False
        
        if hidden_cards >= actual_card_amount:
            timer 0.5 action Return(points) repeat False
        
        if peek_active:
            timer 5.0 action SetScreenVariable("peek_active", False) repeat False
            python:
                for i, card in enumerate(cards):
                    if card[2] == "visible":
                        for mem_idx, mem in enumerate(npc_memories):
                            add_to_npc_memory(mem, i, card[0], npc_memory_slots[mem_idx])

    modal True
