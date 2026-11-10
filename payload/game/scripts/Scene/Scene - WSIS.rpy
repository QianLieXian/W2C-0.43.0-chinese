image wsis_wrestling_1_vid 1_common = Movie(play="images/Scene/WSIS - Action/wsis_wrestling_1_vid 1_common.webm", loop=True)
image wsis_wrestling_1_vid 2_common = Movie(play="images/Scene/WSIS - Action/wsis_wrestling_1_vid 2_common.webm", loop=True)

# ---------------------------------------------------------------------------
label wsis_hit(wsis_wear="home", hero_wear="home", scene_skip=None, buceta=None):
# ---------------------------------------------------------------------------

    stop BGM fadeout 1
    if scene_skip == None:
        scene bg_0
        with Dissolve(3)
    else:
        pause(1)

    play BGM "audio/W2C - Adrenaline.mp3"

    if scene_skip == None:
        show wsis_punch_1_wsis_body 1
        if wsis_wear == "home":
            show wsis_punch_1_wsis_wear 1_home
        elif wsis_wear == "under":
            show wsis_punch_1_wsis_wear 1_under
        elif wsis_wear == None:
            show wsis_punch_1_wsis_wear 1_none
        with Dissolve(1)

    $ var_pla = round(1 + (stat_phy * 0.02), 2)

    menu:
        "Defend Yourself{pr}{size=-10}[C_Not]{b}💪 Arrow Click 💪{/b}{pr}Difficult Level: 1.0, Your Level: [var_pla]{pr}{/size}" if (renpy.variant("pc") or renpy.variant("web")):
            $ buceta = 2

        "Dodge" if renpy.variant("mobile"):
            $ buceta = 1

        "Stay Still{pr}{size=-10}[C_Not]Just get hit and reduce [C_Nam][fnamewsis][C_Off] rage[C_Off]{/size}":
            $ buceta = 0

    scene bg_1
    if scene_skip == None:
        show wsis_punch_1_wsis_body 2
        if wsis_wear == "home":
            show wsis_punch_1_wsis_wear 2_home
        elif wsis_wear == "under":
            show wsis_punch_1_wsis_wear 2_under
        elif wsis_wear == None:
            show wsis_punch_1_wsis_wear 2_none
        with Dissolve(2)

    play SE1 "Hit1.mp3"
    show wsis_punch_1_wsis_body 3
    if wsis_wear == "home":
        show wsis_punch_1_wsis_wear 3_home
    elif wsis_wear == "under":
        show wsis_punch_1_wsis_wear 3_under
    elif wsis_wear == None:
        show wsis_punch_1_wsis_wear 3_none
    with dissolve

    if buceta == 2:
        pass
    elif buceta == 1:
        jump wsis_hit_win
    elif buceta == 0:
        jump wsis_hit_lose

    call screen minigame_sequence(time_pass=(1 / (1 + (stat_phy_agi * 0.01))), var_tim=int(15 * (1 + (perk_phy_agi * 0.5))), count_arrow=4)
    $ renpy.block_rollback()

    if _return == "Win":
        label wsis_hit_win:
            $ add_stat("hero", "phy_agi", 4)

        play SE1 "Slip.ogg"

        scene bg_2 sparking
        show wsis_punch_2_hero_body 1 at LC
        if hero_wear == "home":
            show wsis_punch_2_hero_wear 1_home at LC
        show wsis_punch_2_hero_body 1 at RC_fast
        if hero_wear == "home":
            show wsis_punch_2_hero_wear 1_home at RC_fast
        show wsis_punch_2_wsis_body 1
        if wsis_wear == "home":
            show wsis_punch_2_wsis_wear 1_home
        elif wsis_wear == "under":
            show wsis_punch_2_wsis_wear 1_under
        elif wsis_wear == None:
            show wsis_punch_2_wsis_wear 1_none
        with hpunch

        pause

        play SE1 "JingleRight.ogg"

        return "Win"

    else:
        label wsis_hit_lose:
            pass

        $ zoomT1 = 0
        $ zoomX1 = 0.6
        $ zoomY1 = 0.5
        $ zoomS1 = 1
        $ alpha1 = 1

        $ zoomT2 = 5
        $ zoomX2 = zoomX1
        $ zoomY2 = zoomY1
        $ zoomS2 = 2
        $ alpha2 = 0

        play SE1 "Hit1.ogg"

        scene bg_2 sparking
        show wsis_punch_2_bg 1 at ZoomSTXYA
        show wsis_punch_2_hero_body_bg 1 at CC
        if hero_wear == "home":
            show wsis_punch_2_hero_wear_bg 1_home at CC
        show wsis_punch_2_wsis_body 1

        if wsis_wear == "home":
            show wsis_punch_2_wsis_wear 1_home
        elif wsis_wear == "under":
            show wsis_punch_2_wsis_wear 1_under
        elif wsis_wear == None:
            show wsis_punch_2_wsis_wear 1_none

        show wsis_punch_2_hero_body_fg 1 at CC
        if hero_wear == "home":
            show wsis_punch_2_hero_wear_fg 1_home at CC
        show wsis_punch_2_fg 1 at ZoomSTXYA
        show wsis_punch_2_hero_body_bg 1 at RC_heavy
        if hero_wear == "home":
            show wsis_punch_2_hero_wear_bg 1_home at RC_heavy
        show wsis_punch_2_hero_body_fg 1 at RC_heavy
        if hero_wear == "home":
            show wsis_punch_2_hero_wear_fg 1_home at RC_heavy
        with hpunch

        pause

        play SE1 "JingleWrong.ogg"

        return "Lose"

    pause
    return

# ---------------------------------------------------------------------------
label wsis_quest_1_kitchen: # Late night kitchen encounter before overeating
# ---------------------------------------------------------------------------

    stop BGM fadeout 3

    scene bg_0 with Dissolve(1)

    play BGM "audio/W2C - Tranquility.mp3"

    scene wsis_midnightlunch_1_bg
    show wsis_midnightlunch_1_wsis_body 1
    show wsis_midnightlunch_1_wsis_wear 1_common
    show fx_light:
        blend "add"
    with Dissolve(1)

    # HERO enters kitchen at late night, sees WSIS looking in the fridge

    mind "([C_Nam][hero_about_wsis][C_Off] is searching something in the fridge.)"

    show wsis_midnightlunch_1_hero_body 1
    show wsis_midnightlunch_1_hero_wear 1_common
    show wsis_midnightlunch_1_hero_face 1a0
    hide fx_light
    show fx_light:
        blend "add"
    with dissolve

    show wsis_midnightlunch_1_hero_face 1a1
    hero "Hey, [C_Nam][hero_about_wsis][C_Off]!{nw}"

    show wsis_midnightlunch_1_wsis_body 2
    show wsis_midnightlunch_1_wsis_wear 2_common
    show wsis_midnightlunch_1_wsis_face 2o0
    show wsis_midnightlunch_1_wsis_fg 2
    show wsis_midnightlunch_1_hero_face 1a1
    hide fx_light
    show fx_light:
        blend "add"
    hero "Hey, [C_Nam][hero_about_wsis][C_Off]!{fast}{w=[wt2]} Looking for something to eat?"

    # WSIS jumps, startled, holding a strawberry yogurt
    show wsis_midnightlunch_1_wsis_face 2o1
    show wsis_midnightlunch_1_hero_face 1a0
    
    wsis "No, idiot.{w=[wt2]} I opened the fridge to see if there were any penguins stuck inside!"

    show wsis_midnightlunch_1_wsis_face 2o0 with None

    menu:
        "Cook together":
            jump wsis_quest_1_kitchen_cook

        "Eat together":            
            call gametime_wait(21, 0) from _call_gametime_wait_26
            jump wsis_quest_1_kitchen_eat

        "Leave":
            show wsis_midnightlunch_1_hero_face 1a1
            hero "Understandable.{w=[wt2]} Have a good day."

            show wsis_midnightlunch_1_hero_face 1a0 with None
            jump show_ui

    jump show_ui

# ---------------------------------------------------------------------------
label wsis_quest_1_kitchen_cook2shop: # Cooking Together
# ---------------------------------------------------------------------------
    wsis "Are you idiot or what?{w=[wt4]} We don't have ingredients for that here!"

    menu:
        wsis "Are you idiot or what? We don't have ingredients for that here!{fast}"

        "Go shopping":
            hero "Let's buy the ingredients!"
            wsis "Fine"
            call action_walk from _call_action_walk_3
            jump wsis_grocerystore
        
        "Cancel":
            hero "Well, nevermind."
            jump show_ui

# ---------------------------------------------------------------------------
label wsis_quest_1_kitchen_cook(buceta=False): # Cooking Together
# ---------------------------------------------------------------------------

    if buceta == False:
        show wsis_midnightlunch_1_wsis_face 2o0
        show wsis_midnightlunch_1_hero_face 1a1
        hero "Let's cook something!"
        
        show wsis_midnightlunch_1_wsis_face 2o1
        show wsis_midnightlunch_1_hero_face 1a0
        wsis "Why would I cook something with you, idiot?"
        
        show wsis_midnightlunch_1_wsis_face 2o0
        show wsis_midnightlunch_1_hero_face 1a1
        hero "To eat."
        
        show wsis_midnightlunch_1_wsis_face 2o1
        show wsis_midnightlunch_1_hero_face 1a0
        wsis "{aw}OH, SHUT UP!!!{/aw}{w=[wt4]} What you wanna make?"

        show wsis_midnightlunch_1_wsis_face 2o0
        show wsis_midnightlunch_1_hero_face 1a0
        with None

    else:
        scene wsis_midnightlunch_1_bg
        show wsis_midnightlunch_1_wsis_body 2
        show wsis_midnightlunch_1_wsis_wear 2_common
        show wsis_midnightlunch_1_wsis_face 2o0
        show wsis_midnightlunch_1_wsis_fg 2
        show wsis_midnightlunch_1_hero_body 1
        show wsis_midnightlunch_1_hero_wear 1_common
        show wsis_midnightlunch_1_hero_face 1a0
        show fx_light:
            blend "add"
        with dissolve

    menu:
        "{aw}OH, SHUT UP!!!{/aw} What you wanna make?{fast}"
        
        "Fried Egg":
            hero "Let's make [C_Itm]Fried Egg[C_Off]!"
            if (sum(1 for item in inventory_fridge if item.item_id == "Eat_Farm_Egg") >= 2):
                $ a_event_2 = "Eat_Meal_EggFried"
                $ a_event_5 = ["oil", "tool", "Eat_Farm_Egg", "Eat_Farm_Egg"] # Recipe List
                wsis "Fine."
            else:
                $ item_sale.append("Eat_Farm_Egg")
                $ item_sale.append("Eat_Farm_Egg")
                jump wsis_quest_1_kitchen_cook2shop
        
        "Ham Sandwich" if 0 > 1: # Disable
            hero "How about [C_Itm]Ham Sandwich[C_Off]?"
            if (sum(1 for item in inventory_fridge if item.item_id == "Eat_Farm_Bread") >= 2) and (sum(1 for item in inventory_fridge if item.item_id == "Eat_Farm_Cheese") >= 2) and (sum(1 for item in inventory_fridge if item.item_id == "Eat_Meat_Presunto") >= 2):
                $ a_event_2 = "Eat_Snack_SandwichCheeseHam"
                $ a_event_5 = ["oil", "tool", "Eat_Farm_Bread", "Eat_Farm_Bread", "Eat_Farm_Cheese", "Eat_Farm_Cheese", "Eat_Meat_Presunto", "Eat_Meat_Presunto"] # Recipe List
                wsis "Fine."
            else:
                jump wsis_quest_1_kitchen_cook2shop
        
        "Cancel":
            hero "Well, nevermind."
            jump show_ui
    
    stop BGM fadeout 5
    wsis "Alright! Let's gather everything we need."

    scene bg_0 with Dissolve(2)

    play BGM "audio/W2C - Fun.mp3"
    
    # ===== INGREDIENT GATHERING MINIGAME =====
    
    # Initial setup
    $ a_event_1 = 0 # WSIS position
    $ a_event_3 = [] # Items collected so far
    $ a_event_4 = "" # Item name (string)
    $ a_event_6 = [1,2,3] # Check Done

    $ a_event_1 = renpy.random.choice(a_event_6)

    # Loop until all items are collected
    # while not all(item in a_event_3 for item in a_event_5):
    while not (all(a_event_3.count(item) >= a_event_5.count(item) for item in set(a_event_5))):

        scene cooking_homekitchen_bg
        show cooking_homekitchen_fridge 0
        
        # WSIS animations based on position
        if a_event_1 == 1: # Searching fridge
            show cooking_homekitchen_fridge 1 # open fridge
            show cooking_homekitchen_wsis_body fridge
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear fridge_sleep
            else:
                show cooking_homekitchen_wsis_wear fridge_common
            
        elif a_event_1 == 2: # Searching low cabinet
            show cooking_homekitchen_wsis_body cabinet_low
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear cabinet_low_sleep
            else:
                show cooking_homekitchen_wsis_wear cabinet_low_common
            
        elif a_event_1 == 3: # Trying to reach high cabinet
            show cooking_homekitchen_wsis_body cabinet_high_1
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear cabinet_high_1_sleep
            else:
                show cooking_homekitchen_wsis_wear cabinet_high_1_common
            
        elif a_event_1 == 4: # Searching high cabinet (with chair)
            show cooking_homekitchen_wsis_body cabinet_high_2
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear cabinet_high_2_sleep
            else:
                show cooking_homekitchen_wsis_wear cabinet_high_2_common
            
        else: # Out of screenfridge
            show cooking_homekitchen_wsis_body cabinet_low at OR
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear cabinet_low_sleep at OR
            else:
                show cooking_homekitchen_wsis_wear cabinet_low_common at OR

        show fx_light:
            blend "add"
        with dissolve

        pause(0.5)
        
        # Player choice menu
        menu:
            "What to do?{fast}"
            
            "Check [C_Nam][fnamewsis][C_Off]" if (a_event_1 not in [5, 6, 7, 8]):
                if a_event_1 == 1:
                    scene wsis_midnightlunch_1_bg
                    show wsis_midnightlunch_1_wsis_body 1
                    show wsis_midnightlunch_1_wsis_wear 1_common
                    show fx_light:
                        blend "add"
                    with fade

                    pause

                    scene cooking_homekitchen_bg
                    show cooking_homekitchen_fridge 1
                    show cooking_homekitchen_wsis_body fridge
                    if Get_NPCWear("wsis") == "sleep":
                        show cooking_homekitchen_wsis_wear fridge_sleep
                    else:
                        show cooking_homekitchen_wsis_wear fridge_common
                    show fx_light:
                        blend "add"
                    with fade

                if a_event_1 == 2:
                    scene cooking_homekitchen_low_bg
                    show cooking_homekitchen_low_wsis_body
                    if Get_NPCWear("wsis") == "sleep":
                        show cooking_homekitchen_low_wsis_wear sleep
                    else:
                        show cooking_homekitchen_low_wsis_wear common
                    show cooking_homekitchen_low_wsis_head 1
                    show cooking_homekitchen_low_wsis_face 1
                    show fx_light:
                        blend "add"
                    with fade

                    pause

                    mind "(She looks cute when she's focused...)"

                    show cooking_homekitchen_low_wsis_head 2
                    show cooking_homekitchen_low_wsis_face 2o0
                    with dissolve

                    $ add_stat("wsis", "lust", 0.5)
                    $ add_stat("wsis", "rage", 0.5)
                    show cooking_homekitchen_low_wsis_face 2o1

                    wsis "Stop staring at me and help!"

                    show cooking_homekitchen_low_wsis_face 2o0
                    hero "S-sorry!"

                    scene cooking_homekitchen_bg
                    show cooking_homekitchen_fridge 0
                    show cooking_homekitchen_wsis_body cabinet_low
                    if Get_NPCWear("wsis") == "sleep":
                        show cooking_homekitchen_wsis_wear cabinet_low_sleep
                    else:
                        show cooking_homekitchen_wsis_wear cabinet_low_common
                    show fx_light:
                        blend "add"
                    with fade

                if a_event_1 == 3:
                    scene cooking_homekitchen_high1_bg
                    show cooking_homekitchen_high1_hero_body 1 at OpacityX(0)
                    show cooking_homekitchen_high1_hero_wear 1common at OpacityX(0)
                    show cooking_homekitchen_high1_hero_face 1a0 at OpacityX(0)
                    show cooking_homekitchen_high1_wsis_body 1
                    if Get_NPCWear("wsis") == "sleep":
                        show cooking_homekitchen_high1_wsis_wear 1sleep
                    else:
                        show cooking_homekitchen_high1_wsis_wear 1common
                    show cooking_homekitchen_high1_wsis_face 1o0
                    show fx_light:
                        blend "add"
                    with fade
                    $ X_spd = 0.5
                    menu:
                        "Lift her up":
                            scene cooking_homekitchen_high1_bg
                            show cooking_homekitchen_high1_both_body 2
                            if Get_NPCWear("wsis") == "sleep":
                                show cooking_homekitchen_high1_wsis_wear 2sleep
                            else:
                                show cooking_homekitchen_high1_wsis_wear 2common
                            show cooking_homekitchen_high1_hero_wear 2common
                            show cooking_homekitchen_high1_hero_face 2a0
                            show cooking_homekitchen_high1_wsis_face 2o1
                            show fx_light:
                                blend "add"
                            with dissolve

                            show cooking_homekitchen_high1_wsis_face 2o2
                            show cooking_homekitchen_high1_hero_face 2a1
                            hero "Let me help you!"

                            $ add_stat("wsis", "lust", 0.5)

                            show cooking_homekitchen_high1_hero_face 2a0

                            if wsis_inti >= 30 and wsis_quest_2 == 0:
                                stop BGM fadeout 3
                                show cooking_homekitchen_high1_wsis_face 2o3
                                show cooking_homekitchen_high1_hero_face 2s1
                                wsis "{pa}GET OFF ME!!!{/pa}"

                                jump wsis_quest_5

                            elif wsis_inti < 20: #20
                                stop BGM fadeout 3
                                $ add_stat("wsis", "rage", 3)
                                show cooking_homekitchen_high1_wsis_face 2o3
                                show cooking_homekitchen_high1_hero_face 2s1
                                wsis "{pa}GET OFF ME!!!{/pa}"

                                if wsis_rage >= 20:
                                    call wsis_hit(scene_skip=False) from _call_wsis_hit_2
                                    stop BGM fadeout 3
                                    if _return == "Win":
                                        $ add_stat("wsis", "inti", 1)
                                        hero "W-wait! S-sorry!"
                                    else:
                                        $ add_stat("wsis", "rage", -2)
                                        hero "{aw}Ugh...!{/aw}"
                                    wsis "You better not dare lay those hands on me again!"

                                else:
                                    show cooking_homekitchen_high1_wsis_face 2o2
                                    show cooking_homekitchen_high1_hero_face 2s2
                                    hero "S-sorry!"
                                play BGM "audio/W2C - Fun.mp3" fadein 3

                            else:
                                show cooking_homekitchen_high1_wsis_face 2o1
                                wsis "{aw}W-what are you doing!?{/aw}"

                                show cooking_homekitchen_high1_wsis_face 2o2 with None

                                # Test:
                                    # $ stat_phy = 4.07
                                    # $ perk_phy_str = 1
                                    # $ a_event_6 = round((0.5 + (perk_phy_str * perk_phy_str * 0.5)) * (1 + (stat_phy * 0.01)), 2)
                                #$ a_event_6 = round(0.025 * ((20 + ((3 + (perk_phy_str * 2)) * (3 + (perk_phy_str * 2)))) * (1 + (stat_phy * 0.01))), 2)
                                #$ a_event_7 = round(((20 + ((3 + (perk_phy_str * 2)) * (3 + (perk_phy_str * 2)))) * (1 + (stat_phy * 0.01))), 2)
                                #$ a_event_8 = round((19*wsis_size*wsis_size), 2)
                                #$ a_event_9 = round((round((19*wsis_size*wsis_size), 2)/30), 2)
                                if round(((20 + ((3 + (perk_phy_str * 2)) * (3 + (perk_phy_str * 2)))) * (1 + (stat_phy * 0.01))), 2) >= round((19*wsis_size*wsis_size), 2):
                                    call screen minigame_thugofwar(var_pla=(round(0.025 * ((20 + ((3 + (perk_phy_str * 2)) * (3 + (perk_phy_str * 2)))) * (1 + (stat_phy * 0.01))), 2)), var_npc=(round((round((19*wsis_size*wsis_size), 2)/30), 2)), var_tim=5)
                                    $ renpy.pause(1, hard=True)
                                    if _return == "Win":
                                        play SE1 "Slip.ogg"
                                        show cooking_homekitchen_high1_both_body 3
                                        show cooking_homekitchen_high1_hero_wear 3common
                                        if Get_NPCWear("wsis") == "sleep":
                                            show cooking_homekitchen_high1_wsis_wear 3sleep
                                        else:
                                            show cooking_homekitchen_high1_wsis_wear 3common
                                        show cooking_homekitchen_high1_wsis_face 3o0
                                        show cooking_homekitchen_high1_hero_face 3
                                        with dissolve

                                        $ add_stat("wsis", "inti", 1)
                                        $ add_stat("wsis", "love", 1)
                                        $ add_stat("wsis", "lust", 1)
                                        $ a_event_3.append("oil")
                                        $ msg.msg(renpy.translate_string("You helped [C_Nam][fnamewsis][C_Off] get [C_Itm]butter[C_Off]"))

                                        pause

                                    elif _return == "Lose":
                                        show cooking_homekitchen_high1_hero_face 2s2
                                        hero "{aw}Ugh...{/aw} Y-you're too heavy."

                                        show cooking_homekitchen_high1_hero_face 2s0
                                        show cooking_homekitchen_high1_wsis_face 2o3
                                        wsis "{pa}WHAT?!{/pa}"

                                        show cooking_homekitchen_high1_wsis_face 2o2 with None

                                        call wsis_hit(scene_skip=False) from _call_wsis_hit_3
                                        if _return == "Win":
                                            wsis "I'll let it pass this time. But you better watch your tongue!"
                                            jump wsis_quest_1_kitchen_cook_liftup_win
                                        elif _return == "Lose":
                                            wsis "This is for you to learn to control your tongue!"
                                            jump wsis_quest_1_kitchen_cook_liftup_lose

                                    elif _return == "TimeUp":
                                        show cooking_homekitchen_high1_hero_face 2s1
                                        show cooking_homekitchen_high1_wsis_face 2o3
                                        wsis "{aw}Ugh...! Let go of me!{/aw}"

                                        show cooking_homekitchen_high1_wsis_face 2o2 with None

                                        call wsis_hit(scene_skip=False) from _call_wsis_hit_4
                                        if _return == "Win":
                                            wsis "I'll let it pass this time. But you better control your perverted impulses!"
                                            jump wsis_quest_1_kitchen_cook_liftup_win
                                        elif _return == "Lose":
                                            wsis "This is for you to learn to control your perverted impulses!"
                                            jump wsis_quest_1_kitchen_cook_liftup_lose
                                else:
                                    $ msg.msg(renpy.translate_string("Oops! [C_Nam][fnamewsis][C_Off] seems to be too heavy for you."))
                                    show cooking_homekitchen_high1_hero_face 2s1
                                    hero "{aw}Ugh...{/aw} Y-you're too heavy."
                                    wsis "{pa}WHAT?!{/pa}"
                                    call wsis_hit(scene_skip=False) from _call_wsis_hit_5
                                    if _return == "Win":
                                        wsis "I'll let it pass this time. But you better watch your tongue!"
                                        label wsis_quest_1_kitchen_cook_liftup_win:
                                            $ add_stat("wsis", "inti", 1)

                                    elif _return == "Lose":
                                        wsis "This is for you to learn to control your tongue!"
                                        label wsis_quest_1_kitchen_cook_liftup_lose:
                                            $ add_stat("wsis", "rage", -1)
                        
                        "Take the item":
                            $ X_spd = 0.1
                            show cooking_homekitchen_high1_hero_body 1 at Opacity2
                            show cooking_homekitchen_high1_hero_wear 1common at Opacity2
                            show cooking_homekitchen_high1_hero_face 1a0 at Opacity2
                            with dissolve

                            show cooking_homekitchen_high1_hero_face 1a1
                            hero "Leave it to me!"

                            if (sum(1 for item in a_event_3 if item == "oil") < 1):
                                if a_event_2 == "Eat_Meal_EggFried":
                                    $ a_event_4 = renpy.random.choice(["Butter", "Cooking Oil"])
                                    if a_event_4 == "Butter":
                                        $ RemItem_Inventory("Ingredient_Cook_Butter", inventory_id=inventory_fridge)
                                    if a_event_4 == "Cooking Oil":
                                        $ RemItem_Inventory("Ingredient_Cook_Oil", inventory_id=inventory_fridge)
                                elif a_event_2 == "Eat_Snack_SandwichCheeseHam":
                                    $ a_event_4 = "Butter"
                                    $ RemItem_Inventory("Ingredient_Cook_Butter", inventory_id=inventory_fridge)
                                $ msg.msg(renpy.translate_string("[C_Nam]You[C_Off] found [C_Itm][a_event_4][C_Off]"))
                                $ a_event_3.append("oil")
                                $ add_stat("wsis", "love", 0.5)
                            else:
                                $ msg.msg(renpy.translate_string("[C_Nam]You[C_Off] didn't find anything"))

                            show cooking_homekitchen_high1_hero_face 1a0
                            show cooking_homekitchen_high1_wsis_face 1o1
                            wsis "{aw}Tch...!{/aw} Show off."

                            show cooking_homekitchen_high1_wsis_face 1o0 with None
                        
                        "Leave":
                            pass

                    pause

                    scene cooking_homekitchen_bg
                    show cooking_homekitchen_fridge 0
                    show cooking_homekitchen_wsis_body cabinet_high_1
                    if Get_NPCWear("wsis") == "sleep":
                        show cooking_homekitchen_wsis_wear cabinet_high_1_sleep
                    else:
                        show cooking_homekitchen_wsis_wear cabinet_high_1_common
                    show fx_light:
                        blend "add"
                    with fade

                if a_event_1 == 4:
                    scene cooking_homekitchen_high2_bg
                    show cooking_homekitchen_high2_wsis_body
                    if Get_NPCWear("wsis") == "sleep":
                        show cooking_homekitchen_high2_wsis_wear sleep
                    else:
                        show cooking_homekitchen_high2_wsis_wear common
                    show cooking_homekitchen_high2_wsis_head 1
                    show cooking_homekitchen_high2_wsis_face 2o0 at OpacityX(0)
                    show fx_light:
                        blend "add"
                    with dissolve

                    pause

                    show cooking_homekitchen_high2_wsis_head 2
                    show cooking_homekitchen_high2_wsis_face 2o0 at OpacityX(1)
                    with dissolve

                    $ add_stat("wsis", "lust", 0.5)
                    $ add_stat("wsis", "rage", 0.5)

                    show cooking_homekitchen_high2_wsis_face 2o1
                    wsis "Will you do anything too or just look!?"

                    show cooking_homekitchen_high2_wsis_face 2o0
                    hero "{gg}Hee-hee...{/gg}"

                    scene cooking_homekitchen_bg
                    show cooking_homekitchen_fridge 0
                    show cooking_homekitchen_wsis_body cabinet_high_2
                    if Get_NPCWear("wsis") == "sleep":
                        show cooking_homekitchen_wsis_wear cabinet_high_2_sleep
                    else:
                        show cooking_homekitchen_wsis_wear cabinet_high_2_common
                    show fx_light:
                        blend "add"
                    with fade
            
            "Open fridge" if a_event_1 != 1:
                show cooking_homekitchen_fridge 1
                if a_event_2 == "Eat_Meal_EggFried" and (sum(1 for item in a_event_3 if item == "Eat_Farm_Egg") < 2):
                    $ RemItem_Inventory("Eat_Farm_Egg", inventory_id=inventory_fridge)
                    $ a_event_3.append("Eat_Farm_Egg")
                    $ msg.msg(renpy.translate_string("[C_Nam]You[C_Off] found [C_Itm]Egg[C_Off]"))
                    $ add_stat("wsis", "love", 0.5)
                elif a_event_2 == "Eat_Snack_SandwichCheeseHam" and (sum(1 for item in a_event_3 if item == "Eat_Farm_Bread") < 2):
                    $ RemItem_Inventory("Eat_Farm_Bread", inventory_id=inventory_fridge)
                    $ a_event_3.append("Eat_Farm_Bread")
                    $ msg.msg(renpy.translate_string("[C_Nam]You[C_Off] found [C_Itm]Bread[C_Off]"))
                    $ add_stat("wsis", "love", 0.5)
                elif a_event_2 == "Eat_Snack_SandwichCheeseHam" and (sum(1 for item in a_event_3 if item == "Eat_Farm_Cheese") < 2):
                    $ RemItem_Inventory("Eat_Farm_Cheese", inventory_id=inventory_fridge)
                    $ a_event_3.append("Eat_Farm_Cheese")
                    $ msg.msg(renpy.translate_string("[C_Nam]You[C_Off] found [C_Itm]Cheese[C_Off]"))
                    $ add_stat("wsis", "love", 0.5)
                elif a_event_2 == "Eat_Snack_SandwichCheeseHam" and (sum(1 for item in a_event_3 if item == "Eat_Meat_Presunto") < 2):
                    $ RemItem_Inventory("Eat_Meat_Presunto", inventory_id=inventory_fridge)
                    $ a_event_3.append("Eat_Meat_Presunto")
                    $ msg.msg(renpy.translate_string("[C_Nam]You[C_Off] found [C_Itm]Presunto[C_Off]"))
                    $ add_stat("wsis", "love", 0.5)
                else:
                    $ msg.msg(renpy.translate_string("[C_Nam]You[C_Off] didn't find anything"))
                
            "Open low cabinet" if a_event_1 != 2:
                if (sum(1 for item in a_event_3 if item == "tool") < 1):
                    if a_event_2 == "Eat_Meal_EggFried":
                        $ RemItem_Inventory("Tool_Cook_PanFry", inventory_id=inventory_fridge)
                        $ a_event_3.append("tool")
                        $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] found [C_Itm]Frying Pan[C_Off]"))
                    elif a_event_2 == "Eat_Snack_SandwichCheeseHam":
                        $ RemItem_Inventory("Tool_Cook_Knife", inventory_id=inventory_fridge)
                        $ a_event_3.append("tool")
                        $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] found [C_Itm]Cooking Knife[C_Off]"))
                    $ add_stat("wsis", "love", 0.5)
                else:
                    $ msg.msg(renpy.translate_string("[C_Nam]You[C_Off] didn't find anything"))
                
            "Open high cabinet" (a_event_1 in [1, 2]):
                if (sum(1 for item in a_event_3 if item == "oil") < 1):
                    if a_event_2 == "Eat_Meal_EggFried":
                        $ a_event_4 = renpy.random.choice(["Butter", "Cooking Oil"])
                        if a_event_4 == "Butter":
                            $ RemItem_Inventory("Ingredient_Cook_Butter", inventory_id=inventory_fridge)
                        if a_event_4 == "Cooking Oil":
                            $ RemItem_Inventory("Ingredient_Cook_Oil", inventory_id=inventory_fridge)
                    elif a_event_2 == "Eat_Snack_SandwichCheeseHam":
                        $ a_event_4 = "Butter"
                        $ RemItem_Inventory("Ingredient_Cook_Butter", inventory_id=inventory_fridge)
                    $ msg.msg(renpy.translate_string("[C_Nam]You[C_Off] found [C_Itm][a_event_4][C_Off]"))
                    $ add_stat("wsis", "love", 0.5)
                    $ a_event_3.append("oil")
                else:
                    $ msg.msg(renpy.translate_string("[C_Nam]You[C_Off] didn't find anything"))
            
            "Wait":
                pass

        #scene cooking_homekitchen_bg
        show cooking_homekitchen_fridge 0

        # Determine WSIS's next action (if not already moving)
        if a_event_1 == 1: # Searching fridge
            show cooking_homekitchen_fridge 1
            if a_event_2 == "Eat_Meal_EggFried" and (sum(1 for item in a_event_3 if item == "Eat_Farm_Egg") < 2):
                $ RemItem_Inventory("Eat_Farm_Egg", inventory_id=inventory_fridge)
                $ a_event_3.append("Eat_Farm_Egg")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] found [C_Itm]Egg[C_Off]"))
            elif a_event_2 == "Eat_Snack_SandwichCheeseHam" and (sum(1 for item in a_event_3 if item == "Eat_Farm_Bread") < 2):
                $ RemItem_Inventory("Eat_Farm_Bread", inventory_id=inventory_fridge)
                $ a_event_3.append("Eat_Farm_Bread")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] found [C_Itm]Bread[C_Off]"))
            elif a_event_2 == "Eat_Snack_SandwichCheeseHam" and (sum(1 for item in a_event_3 if item == "Eat_Farm_Cheese") < 2):
                $ RemItem_Inventory("Eat_Farm_Cheese", inventory_id=inventory_fridge)
                $ a_event_3.append("Eat_Farm_Cheese")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] found [C_Itm]Cheese[C_Off]"))
            elif a_event_2 == "Eat_Snack_SandwichCheeseHam" and (sum(1 for item in a_event_3 if item == "Eat_Meat_Presunto") < 2):
                $ RemItem_Inventory("Eat_Meat_Presunto", inventory_id=inventory_fridge)
                $ a_event_3.append("Eat_Meat_Presunto")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] found [C_Itm]Presunto[C_Off]"))
            else:
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] didn't find anything"))
                $ a_event_6.remove(1)
                if a_event_6 != []:
                    $ a_event_1 = renpy.random.choice(a_event_6)

        elif a_event_1 == 2: # Searching low cabinet
            if (sum(1 for item in a_event_3 if item == "tool") < 1):
                if a_event_2 == "Eat_Meal_EggFried":
                    $ RemItem_Inventory("Tool_Cook_PanFry", inventory_id=inventory_fridge)
                    $ a_event_3.append("tool")
                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] found [C_Itm]Frying Pan[C_Off]"))
                elif a_event_2 == "Eat_Snack_SandwichCheeseHam":
                    $ RemItem_Inventory("Tool_Cook_Knife", inventory_id=inventory_fridge)
                    $ a_event_3.append("tool")
                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] found [C_Itm]Cooking Knife[C_Off]"))
            else:
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] didn't find anything"))
            $ a_event_6.remove(2)
            if a_event_6 != []:
                $ a_event_1 = renpy.random.choice(a_event_6)

        elif a_event_1 == 3: # Trying to reach high cabinet
            if (sum(1 for item in a_event_3 if item == "oil") < 1):
                $ a_event_1 = 5 # Leaving
                
                show cooking_homekitchen_wsis_body walking_r_1 at CC
                if Get_NPCWear("wsis") == "sleep":
                    show cooking_homekitchen_wsis_wear walking_r_1_sleep at cc
                else:
                    show cooking_homekitchen_wsis_wear walking_r_1_common at CC
                show cooking_homekitchen_wsis_body walking_r_1 at RR_slow
                if Get_NPCWear("wsis") == "sleep":
                    show cooking_homekitchen_wsis_wear walking_r_1_sleep at RR_slow
                else:
                    show cooking_homekitchen_wsis_wear walking_r_1_common at RR_slow
                pause(1)
            else:
                $ a_event_6.remove(3)
                if a_event_6 != []:
                    $ a_event_1 = renpy.random.choice(a_event_6)

        elif a_event_1 == 4: # Searching high cabinet (with chair)
            if (sum(1 for item in a_event_3 if item == "oil") < 1):
                if a_event_2 == "Eat_Meal_EggFried":
                    $ a_event_4 = renpy.random.choice(["Butter", "Cooking Oil"])
                    if a_event_4 == "Butter":
                        $ RemItem_Inventory("Ingredient_Cook_Butter", inventory_id=inventory_fridge)
                    if a_event_4 == "Cooking Oil":
                        $ RemItem_Inventory("Ingredient_Cook_Oil", inventory_id=inventory_fridge)
                elif a_event_2 == "Eat_Snack_SandwichCheeseHam":
                    $ a_event_4 = "Butter"
                    $ RemItem_Inventory("Ingredient_Cook_Butter", inventory_id=inventory_fridge)
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] found [C_Itm][a_event_4][C_Off]"))
                $ a_event_3.append("oil")
            else:
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] didn't find anything"))
            $ a_event_6.remove(3)
            $ a_event_1 = 6
            show cooking_homekitchen_wsis_body walking_r_2 at CC
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear walking_r_2_sleep at cc
            else:
                show cooking_homekitchen_wsis_wear walking_r_2_common at CC
            show cooking_homekitchen_wsis_body walking_r_2 at RR_slow
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear walking_r_2_sleep at RR_slow
            else:
                show cooking_homekitchen_wsis_wear walking_r_2_common at RR_slow
            pause(1)
            
        elif a_event_1 == 5: # Coming with chair
            $ a_event_1 = 4
            show cooking_homekitchen_wsis_body walking_l_2 at RR
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear walking_l_2_sleep at RR
            else:
                show cooking_homekitchen_wsis_wear walking_l_2_common at RR
            show cooking_homekitchen_wsis_body walking_l_2 at CC_slow
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear walking_l_2_sleep at CC_slow
            else:
                show cooking_homekitchen_wsis_wear walking_l_2_common at CC_slow
            pause(1)
            
        elif a_event_1 == 6: # Coming
            if a_event_6 != []:
                $ a_event_1 = renpy.random.choice(a_event_6)
            show cooking_homekitchen_wsis_body walking_l_1 at RR
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear walking_l_1_sleep at RR
            else:
                show cooking_homekitchen_wsis_wear walking_l_1_common at RR
            show cooking_homekitchen_wsis_body walking_l_1 at CC_slow
            if Get_NPCWear("wsis") == "sleep":
                show cooking_homekitchen_wsis_wear walking_l_1_sleep at CC_slow
            else:
                show cooking_homekitchen_wsis_wear walking_l_1_common at CC_slow
            pause(1)

        else:
            if a_event_6 != []:
                $ a_event_1 = renpy.random.choice(a_event_6)

        # Update WSIS's next action for next loop

    call gametime_wait(22, 0) from _call_gametime_wait_27
    # All items collected!
    scene bg_0 with Dissolve(1)
    $ msg.msg(renpy.translate_string("All ingredients and tools collected!"))    

    pause

    $ inventory_home_table = []

    if a_event_2 == "Eat_Meal_EggFried":
        $ AddItem_Inventory("Ingredient_Cook_Butter", 1, inventory_id=inventory_home_table)
        $ AddItem_Inventory("Eat_Farm_Egg", 2, inventory_id=inventory_home_table)

    elif a_event_2 == "Eat_Snack_SandwichCheeseHam":
        $ inventory_home_table.append(Item("Ingredient_Cook_Butter"))
        $ inventory_home_table.append(Item("Eat_Farm_Bread"))
        $ inventory_home_table.append(Item("Eat_Farm_Cheese"))
        $ inventory_home_table.append(Item("Eat_Meat_Presunto"))
        $ inventory_home_table.append(Item("Eat_Farm_Bread"))
        $ inventory_home_table.append(Item("Eat_Farm_Cheese"))
        $ inventory_home_table.append(Item("Eat_Meat_Presunto"))
    call gamecheck from _call_gamecheck_34
    call hide_ui from _call_hide_ui_191

    image cooking_homekitchen_cooking_hero_arm_body 1a:
        contains:
            "cooking_homekitchen_cooking_hero_arm_body 1_a"
        contains:
            "cooking_homekitchen_cooking_hero_arm_wear 1common_a"

    image cooking_homekitchen_cooking_hero_arm_body 1b:
        contains:
            "cooking_homekitchen_cooking_hero_arm_body 1_b"
        contains:
            "cooking_homekitchen_cooking_hero_arm_wear 1common_b"

    image cooking_homekitchen_cooking_hero_arm_body 1c:
        contains:
            "cooking_homekitchen_cooking_hero_arm_body 1_c"
        contains:
            "cooking_homekitchen_cooking_hero_arm_wear 1common_c"

    image cooking_homekitchen_cooking_hero_arm_body 1d:
        contains:
            "cooking_homekitchen_cooking_hero_arm_body 1_d"
        contains:
            "cooking_homekitchen_cooking_hero_arm_wear 1common_d"

    image cooking_homekitchen_cooking_hero_arm_body 1e:
        contains:
            "cooking_homekitchen_cooking_hero_arm_body 1_e"
        contains:
            "cooking_homekitchen_cooking_hero_arm_wear 1common_e"

    image cooking_homekitchen_cooking_hero_arm_body 1_ani:
        "cooking_homekitchen_cooking_hero_arm_body 1a"
        0.15
        "cooking_homekitchen_cooking_hero_arm_body 1b"
        0.15
        "cooking_homekitchen_cooking_hero_arm_body 1c"
        0.15
        "cooking_homekitchen_cooking_hero_arm_body 1d"
        0.15
        "cooking_homekitchen_cooking_hero_arm_body 1e"
        0.15
        repeat

    $ a_event_0 = 0 # step
    $ a_event_1 = 0 # light
    $ a_event_2 = -1 # 🔥butter
    $ a_event_3 = [-1, 0, 0] # 🔥egg, +egg, mix
    $ a_event_4 = 0 # stir
    $ a_event_5 = 0 # wait
    $ a_event_6 = -1 # 🔥fryier
    $ a_event_7 = 0 # score

    scene cooking_homekitchen_cooking_bg
    show cooking_homekitchen_cooking_hero_body 1
    show cooking_homekitchen_cooking_hero_wear 1common
    show cooking_homekitchen_cooking_hero_arm_body 1a
    show cooking_homekitchen_cooking_hero_face 1a0
    show cooking_homekitchen_cooking_wsis_body 1
    if Get_NPCWear("wsis") == "sleep":
        show cooking_homekitchen_cooking_wsis_wear 1sleep
    else:
        show cooking_homekitchen_cooking_wsis_wear 1common
    show cooking_homekitchen_cooking_wsis_face 1o0
    show cooking_homekitchen_cooking_mg 0
    show fx_light:
        blend "add"
    with Dissolve(1)

    jump wsis_quest_1_kitchen_cook_prepare

label wsis_quest_1_kitchen_cook_prepare:
    $ a_event_0 = 0
    $ a_event_4 = 0

    show cooking_homekitchen_cooking_hero_arm_body 1a
    show cooking_homekitchen_cooking_hero_face 1a0
    show cooking_homekitchen_cooking_wsis_face 1o0

    label wsis_quest_1_kitchen_cook_prepare_options:
        pass

    menu:
        "Check [C_Nam][fnamewsis][C_Off]":
            menu:
                "Ask for her preference" if Check_CharSameMap("hero", "wsis"):
                    if a_event_3[0] == -1:
                        show cooking_homekitchen_cooking_hero_face 1a1
                        show cooking_homekitchen_cooking_wsis_face 1o0
                        hero "How do you like the egg?"
                        show cooking_homekitchen_cooking_hero_face 1a0
                        show cooking_homekitchen_cooking_wsis_face 1o1
                        wsis "Well toasted and mixed!"
                        show cooking_homekitchen_cooking_hero_face 1a1
                        show cooking_homekitchen_cooking_wsis_face 1o0
                        hero "Okay!"
                    else:
                        show cooking_homekitchen_cooking_hero_face 1a1
                        show cooking_homekitchen_cooking_wsis_face 1o0
                        hero "How is it going?"
                        show cooking_homekitchen_cooking_hero_face 1a0
                        show cooking_homekitchen_cooking_wsis_face 1o1
                        if a_event_3[0] <= 1:
                            wsis "No! Too liquid. {aw}Yuuuck!{/aw}"
                        elif a_event_3[0] >= 5:
                            wsis "How do you think it's going, idiot!? You burned it!"
                        elif a_event_3[2] != 1:
                            if a_event_3[0] >= 1 and a_event_3[0] < 2:
                                wsis "Still ugly. I like it mixed."
                            elif a_event_3[0] >= 3 and a_event_3[0] < 4:
                                wsis "It's not mixed."
                            elif a_event_3[0] >= 4 and a_event_3[0] < 5:
                                wsis "It's okay, but you didn't mixed..."
                        else:
                            if a_event_3[0] >= 1 and a_event_3[0] < 2:
                                wsis "Not yet!"
                            elif a_event_3[0] >= 3 and a_event_3[0] < 4:
                                wsis "Well... just a little more, I guess..."
                            elif a_event_3[0] >= 4 and a_event_3[0] < 5:
                                wsis "It's just right. Turn the burner off!"

                "Ask for advice" if Check_CharSameMap("hero", "wsis"):
                    show cooking_homekitchen_cooking_hero_face 1a1
                    show cooking_homekitchen_cooking_wsis_face 1o0
                    if a_event_0 == 0:
                        hero "How do I start?"
                    elif a_event_0 >= 1:
                        if renpy.random.random() < 1/4:
                            hero "So, what do I do now?"
                        elif renpy.random.random() < 2/4:
                            hero "What about now?"
                        elif renpy.random.random() < 3/4:
                            hero "What else?"
                        else:
                            hero "And now?"
                    show cooking_homekitchen_cooking_hero_face 1a0
                    show cooking_homekitchen_cooking_wsis_face 1o1
                    if a_event_1 == 0:
                        wsis "Uh, w-well, I think you should turn on the burner"
                    elif a_event_2 == 0:
                        wsis "Uh, maybe, the butter...?"
                    elif a_event_3[0] == 0:
                        wsis "The eggs, idiot!"
                    elif a_event_3[0] == 1:
                        wsis "Add the other egg, idiot. I won't be sharing mine with you!"
                    else:
                        if renpy.random.random() < 1/4:
                            wsis "Don't ask me!"
                        elif renpy.random.random() < 2/4:
                            wsis "How will I know?"
                        elif renpy.random.random() < 3/4:
                            wsis "Shut up! You're the cooker!"
                        else:
                            wsis "Figure it out!"

                "Return":
                    pass

        "Turn on the burner" if a_event_1 == 0:
            $ a_event_0 += 1
            $ a_event_1 = 1
            show cooking_homekitchen_cooking_mg 1:
                blend "add"

        "Turn off the burner" if a_event_1 == 1:
            $ a_event_0 += 1
            $ a_event_1 = 0
            show cooking_homekitchen_cooking_mg 0

        "Add Item":
            menu:
                "Use [C_Itm]Butter[C_Off]" if (any(buceta.item_id == "Ingredient_Cook_Butter" for buceta in inventory_home_table)):
                    $ a_event_0 += 1
                    $ a_event_2 = 1
                    python:
                        for buceta in inventory_home_table:
                            if buceta.item_id == "Ingredient_Cook_Butter":
                                inventory_home_table.remove(buceta)
                                break
                    $ msg.msg(renpy.translate_string("You passed [C_Itm]Butter[C_Off] on the [C_Itm]Frying Pan[C_Off]"))
                    
                "Use [C_Itm]Egg[C_Off]" if (any(buceta.item_id == "Eat_Farm_Egg" for buceta in inventory_home_table)):
                    $ a_event_0 += 1
                    $ a_event_3[1] += 1
                    if a_event_3[0] <= 0 or (any(buceta.item_id == "Eat_Meal_EggFried" for buceta in inventory_home_table)):
                        $ a_event_3[0] = 0
                    else:
                        $ a_event_3[0] = int(a_event_3[0]/2)
                    python:
                        for buceta in inventory_home_table:
                            if buceta.item_id == "Eat_Farm_Egg":
                                inventory_home_table.remove(buceta)
                                break
                    $ msg.msg(renpy.translate_string("You added an [C_Itm]Egg[C_Off] on the [C_Itm]Frying Pan[C_Off]"))

                "Return":
                    pass
            
        "Prepare":
            menu:
                "Wait":
                    $ a_event_0 += 1
                    $ a_event_5 = 1
                "Stir the [C_Itm]Frying Pan[C_Off]":
                    $ a_event_0 += 1
                    $ a_event_5 = 1
                    $ a_event_4 = 1
                    show cooking_homekitchen_cooking_hero_arm_body 1_ani
                "Mix the [C_Itm]Egg[C_Off]" if a_event_3[1] >= 1:
                    $ a_event_0 += 1
                    $ a_event_5 = 1
                    $ a_event_3[2] += 1
                "Return":
                    pass
            
        "Finish":
            $ a_event_0 = -1
            show cooking_homekitchen_cooking_hero_face 1a1
            hero "Done!"

    show cooking_homekitchen_cooking_hero_face 1a0
    show cooking_homekitchen_cooking_wsis_face 1o0

    if a_event_0 == -1:
        if a_event_1 >= 1:
            if a_event_3[0] <= 0:
                show cooking_homekitchen_cooking_wsis_face 1o1
                wsis "{aw}You haven't done anything!!!{/aw}"
            else:
                show cooking_homekitchen_cooking_wsis_face 1o1
                wsis "What are you saying, idiot!? Turn off the burner!"
            $ a_event_0 = 0

        elif (any(buceta.item_id == "Eat_Farm_Egg" for buceta in inventory_home_table)) and not (any(buceta.item_id == "Eat_Meal_EggFried" for buceta in inventory_home_table)):
            $ a_event_0 = 0
            if a_event_3[0] < 0:
                show cooking_homekitchen_cooking_wsis_face 1o1
                wsis "{aw}You haven't done anything!!!{/aw}"
            else:
                call wsis_quest_1_kitchen_cook_prepare_addegg from _call_wsis_quest_1_kitchen_cook_prepare_addegg

        elif (any(buceta.item_id == "Eat_Meal_EggFried" for buceta in inventory_home_table)) and (any(buceta.item_id == "Eat_Farm_Egg" for buceta in inventory_home_table)):
            $ a_event_0 = 0
            show cooking_homekitchen_cooking_wsis_face 1o1
            wsis "Now do the other one!"

        elif (any(buceta.item_id == "Eat_Meal_EggFried" for buceta in inventory_home_table)) and a_event_3[0] <= 0:
            $ a_event_0 = 0
            show cooking_homekitchen_cooking_wsis_face 1o1
            wsis "{aw}You haven't done anything!!!{/aw}"

        else:
            show cooking_homekitchen_cooking_wsis_face 1o1
            wsis "Let's eat!"

            show cooking_homekitchen_cooking_wsis_face 1o0
            $ gametimemin = a_event_9
            $ a_event_9 = 0 # gametimemin
            call wsis_quest_1_kitchen_cook_prepare_addegg from _call_wsis_quest_1_kitchen_cook_prepare_addegg_1
            call wsis_quest_1_kitchen_eat_table(buceta=True) from _call_wsis_quest_1_kitchen_eat_table

    elif a_event_5 != 0:
        $ a_event_5 = 0
        $ a_event_9 += 0.5
        if a_event_1 == 0:
            if a_event_6 == -1:
                show cooking_homekitchen_cooking_wsis_face 1o1
                wsis "What are you waiting for, idiot!? The burner isn't even turned on!"

                show cooking_homekitchen_cooking_hero_face 1a1
                show cooking_homekitchen_cooking_wsis_face 1o0
                hero "Calm down!"
            else:
                pause(1)
                $ a_event_6 = max(0, a_event_6-1)
                if a_event_6 <= 0:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Frying Pan[C_Off] is no longer hot"))
                elif a_event_6 <= 2:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Frying Pan[C_Off] has cooled down, and now it is normally hot"))
                elif a_event_6 <= 3:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Frying Pan[C_Off] has cooled down, but it's still very hot"))
                elif a_event_6 >= 4:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Frying Pan[C_Off] has cooled down, but it's still extremelly hot"))
        else:
            pause(1)
            $ a_event_6 += a_event_1
            if a_event_6 <= 3:
                $ msg.msg(renpy.translate_string("The [C_Itm]Frying Pan[C_Off] is heating."))
            elif a_event_6 <= 4:
                $ msg.msg(renpy.translate_string("The [C_Itm]Frying Pan[C_Off] is heating too much!"))
            elif a_event_6 >= 5:
                $ msg.msg(renpy.translate_string("The [C_Itm]Frying Pan[C_Off] is burning!"))
            if a_event_2 >= 0: # Butter
                $ a_event_2 += a_event_1
                if a_event_2 <= 1:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Butter[C_Off] melted."))
                elif a_event_2 >= 1 and a_event_2 < 4:
                    pass
                elif a_event_2 >= 4 and a_event_2 <= 5:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Butter[C_Off] is evaporating."))
                elif a_event_2 > 5:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Butter[C_Off] evaporated."))
            if a_event_3[0] >= 0: # Egg
                $ a_event_3[0] += a_event_1
                if a_event_3[0] <= 1:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Egg[C_Off] seems liquid."))
                elif a_event_3[0] >= 1 and a_event_3[0] < 2:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Egg[C_Off] seems pasty."))
                elif a_event_3[0] >= 3 and a_event_3[0] < 4:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Egg[C_Off] seems rubbery."))
                elif a_event_3[0] >= 4 and a_event_3[0] < 5:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Egg[C_Off] seems toasted."))
                elif a_event_3[0] >= 5:
                    $ msg.msg(renpy.translate_string("The [C_Itm]Egg[C_Off] seems burned."))

        if a_event_1 >= 1:
            if a_event_3[0] >= 3:
                show cooking_homekitchen_cooking_wsis_face 1o1
                wsis "{bt}Ohhh...!{/bt} I think it's just right!"
            elif a_event_3[0] >= 4:
                show cooking_homekitchen_cooking_wsis_face 1o1
                wsis "What are you doing, idiot? Turn off the burner!"
            elif a_event_3[0] >= 5:
                show cooking_homekitchen_cooking_wsis_face 1o1
                if (any(buceta.item_id == "Eat_Farm_Egg" for buceta in inventory_home_table)):
                    $ add_stat("wsis", "rage", 1)
                    wsis "You stupid! You burned it! This one will be yours. Do it right this time!"
                elif any(item.item_id == "Eat_Meal_EggFried" and item.quality in [5, 4, 3] for item in inventory_home_table):
                    $ add_stat("wsis", "rage", 0.5)
                    wsis "You burned it! This one will be yours. I'll take the other one!"
                else:
                    $ add_stat("wsis", "rage", 2)
                    wsis "You stupid! You messed up all the eggs!!!"

    jump wsis_quest_1_kitchen_cook_prepare
    jump show_ui

# ---------------------------------------------------------------------------
label wsis_quest_1_kitchen_cook_prepare_addegg: # Add Egg
# ---------------------------------------------------------------------------
    # Egg Stage
    if (a_event_3[0] >= 3 and a_event_3[0] < 5):
        $ a_event_7 += 2
    elif (a_event_3[0] >= 2 and a_event_3[0] < 5):
        $ a_event_7 += 1.5
    elif (a_event_3[0] >= 1 and a_event_3[0] < 5):
        $ a_event_7 += 0.5
    else:
        $ a_event_7 -= 1

    # Egg Mix
    if a_event_3[2] == 1:
        $ a_event_7 += 0.5


    # Butter
    if (a_event_2 >= 1 and a_event_2 < 5):
        $ a_event_7 += 0.5
    else:
        $ a_event_7 -= 0.5

    # Fryier
    if (a_event_6 >= 1 and a_event_6 < 5):
        $ a_event_7 += 0.5
    else:
        $ a_event_7 -= 0.5

    if a_event_3[1] == 1:
        if a_event_7 >= 3:
            $ AddItem_Inventory("Eat_Meal_EggFried", 1, 5, inventory_id=inventory_home_table)
        elif a_event_7 >= 2:
            $ AddItem_Inventory("Eat_Meal_EggFried", 1, 4, inventory_id=inventory_home_table)
        elif a_event_7 >= 1:
            $ AddItem_Inventory("Eat_Meal_EggFried", 1, 3, inventory_id=inventory_home_table)
        elif a_event_7 >= 0:
            $ AddItem_Inventory("Eat_Meal_EggFried", 1, 2, inventory_id=inventory_home_table)
        else:
            $ AddItem_Inventory("Eat_Meal_EggFried", 1, 1, inventory_id=inventory_home_table)

    elif a_event_3[1] == 2 and (any(buceta.item_id == "Eat_Meal_EggFried" for buceta in inventory_home_table)):
        if a_event_7 >= 3:
            $ AddItem_Inventory("Eat_Meal_EggFried", 1, 5, inventory_id=inventory_home_table)
        elif a_event_7 >= 2:
            $ AddItem_Inventory("Eat_Meal_EggFried", 1, 4, inventory_id=inventory_home_table)
        elif a_event_7 >= 1:
            $ AddItem_Inventory("Eat_Meal_EggFried", 1, 3, inventory_id=inventory_home_table)
        elif a_event_7 >= 0:
            $ AddItem_Inventory("Eat_Meal_EggFried", 1, 2, inventory_id=inventory_home_table)
        else:
            $ AddItem_Inventory("Eat_Meal_EggFried", 1, 1, inventory_id=inventory_home_table)

    elif a_event_3[1] == 2 and not (any(buceta.item_id == "Eat_Meal_EggFried" for buceta in inventory_home_table)):
        if a_event_7 >= 3:
            $ AddItem_Inventory("Eat_Meal_EggFried", 2, 5, inventory_id=inventory_home_table)
        elif a_event_7 >= 2:
            $ AddItem_Inventory("Eat_Meal_EggFried", 2, 4, inventory_id=inventory_home_table)
        elif a_event_7 >= 1:
            $ AddItem_Inventory("Eat_Meal_EggFried", 2, 3, inventory_id=inventory_home_table)
        elif a_event_7 >= 0:
            $ AddItem_Inventory("Eat_Meal_EggFried", 2, 2, inventory_id=inventory_home_table)
        else:
            $ AddItem_Inventory("Eat_Meal_EggFried", 2, 1, inventory_id=inventory_home_table)

    $ msg.msg(renpy.translate_string("[C_Itm]Fryed Eggs[C_Off] on table!"))

    $ a_event_0 = 0 # step
    $ a_event_1 = 0 # light
    $ a_event_2 -= -1 # 🔥butter
    $ a_event_3[0] = -1 # 🔥egg
    $ a_event_3[2] = 0 # mix
    $ a_event_4 = 0 # stir
    $ a_event_5 = 0 # wait
    $ a_event_6 = -1 # 🔥fryier
    $ a_event_7 = 0 # score

    return

# ---------------------------------------------------------------------------
label wsis_quest_1_kitchen_eat: # Eating Together
# ---------------------------------------------------------------------------

    show wsis_midnightlunch_1_wsis_face 2o0
    show wsis_midnightlunch_1_hero_face 1a1
    hero "Cool!{w=[wt2]} Lemme join you!"

    show wsis_midnightlunch_1_wsis_face 2o1
    show wsis_midnightlunch_1_hero_face 1a0
    wsis "Hmph!{w=[wt2]} Just get what you want and leave me alone."

    show wsis_midnightlunch_1_wsis_face 2o0 with None

    scene wsis_midnightlunch_2_bg
    show wsis_midnightlunch_2_hero_body 1
    show wsis_midnightlunch_2_hero_wear 1_common
    show wsis_midnightlunch_2_hero_face 1a0
    show wsis_midnightlunch_2_wsis_body 1
    show wsis_midnightlunch_2_wsis_wear 1_common
    show fx_light:
        blend "add"
    with fade
    # HERO notices the yogurt

    stop BGM fadeout 3

    show wsis_midnightlunch_2_hero_face 1a1
    hero "Oh{w=[wt2]}, strawberry yogurt!"

    show wsis_midnightlunch_2_hero_face 1a0 with None

    scene wsis_midnightlunch_2_bg
    show wsis_midnightlunch_2_yogurt 1
    show wsis_midnightlunch_2_hero_body 2
    show wsis_midnightlunch_2_hero_wear 2_common
    show wsis_midnightlunch_2_hero_face 2s0
    show wsis_midnightlunch_2_wsis_body 2
    show wsis_midnightlunch_2_wsis_wear 2_common
    show wsis_midnightlunch_2_wsis_face 2o0
    show fx_light:
        blend "add"
    with dissolve

    play BGM "audio/W2C - Stupidity.mp3"

    show wsis_midnightlunch_2_wsis_face 2o1
    wsis "Get off!{w=[wt2]} These are mine!!"
    
    show wsis_midnightlunch_2_wsis_face 2o0
    show wsis_midnightlunch_2_hero_face 2s1
    hero "{aw}Ehhh...?{/aw}{w=[wt2]} Come on{w=[wt2]}, can't you share just one?"
    
    show wsis_midnightlunch_2_wsis_face 2o1
    show wsis_midnightlunch_2_hero_face 2s0
    wsis "No way!{w=[wt2]} Find your own food, you stupid!"

    show wsis_midnightlunch_2_wsis_face 2o0 with None
    
    menu:                
        "Accept":
            $ add_stat("wsis", "love", -2)

            show wsis_midnightlunch_2_hero_face 2s1
            hero "{bt}Fine... Fine...{/bt}"

            show wsis_midnightlunch_2_hero_face 2s0 with None
            call wsis_quest_1_kitchen_eat_table(buceta="wsis_sick") from _call_wsis_quest_1_kitchen_eat_table_1
            jump show_ui
        
        "Insist":            
            call gametime_wait(22, 0) from _call_gametime_wait_28
            show wsis_midnightlunch_2_hero_face 2s1
            hero "Come on{w=[wt2]}, there are two of them.{w=[wt3]} Give me one!"
            
            show wsis_midnightlunch_2_wsis_face 2o1
            show wsis_midnightlunch_2_hero_face 2s0
            wsis "No way!{w=[wt2]} Drink water! I want both!"
            
            # HERO reaches for the yogurt WSIS is holding
            
            show wsis_midnightlunch_2_wsis_face 2o0
            show wsis_midnightlunch_2_hero_face 2s1
            hero "{bt}Just a little bit...{/bt}"
            
            show wsis_midnightlunch_2_wsis_face 2o1
            show wsis_midnightlunch_2_hero_face 2s0
            wsis "I said NO!"
            
            show wsis_midnightlunch_2_wsis_face 2o0
            show wsis_midnightlunch_2_hero_face 2s0
            with None
            
            play SE1 "Water Splash 3.mp3"

            show wsis_midnightlunch_2_yogurt 2
            with hpunch

            # The yogurt container breaks/opens, splashing on both of them
            scene wsis_midnightlunch_2_bg
            show wsis_midnightlunch_2_hero_body 3
            show wsis_midnightlunch_2_hero_wear 3_common
            show wsis_midnightlunch_2_wsis_body 3
            show wsis_midnightlunch_2_wsis_wear 3_common
            show wsis_midnightlunch_2_wsis_face 3o1
            show wsis_midnightlunch_2_wsis_fg 3
            hide fx_light
            show fx_light:
                blend "add"
            with hpunch
            
            $ add_stat("wsis", "lust", 2)

            pause
            
            show wsis_midnightlunch_2_wsis_face 3o2
            wsis "LOOK WHAT YOU DID, YOU STUPID!{w=[wt2]} NOW YOU'LL PAY!"
            
            show wsis_midnightlunch_2_wsis_face 3o0 with None
            # WSIS tries to punch HERO

            if wsis_inti >= 30 and wsis_quest_2 == 0:
                jump wsis_quest_5

            call wsis_hit("home", "home") from _call_wsis_hit_6
            
            if _return == "Win":
                # HERO dodges and grabs her hands

                $ X_spd = 10

                scene wsis_midnightlunch_3_bg
                show wsis_midnightlunch_3_hero_body 1 at RR
                show wsis_midnightlunch_3_hero_wear 1_common at RR
                show wsis_midnightlunch_3_wsis_body 1 at RR
                show wsis_midnightlunch_3_wsis_wear 1_common at RR
                show wsis_midnightlunch_3_hero_body 1 at CC_X
                show wsis_midnightlunch_3_hero_wear 1_common at CC_X
                show wsis_midnightlunch_3_wsis_body 1 at CC_X
                show wsis_midnightlunch_3_wsis_wear 1_common at CC_X
                show fx_light:
                    blend "add"
                with Fade(0.5, 0, 1)
                
                hero "Hey{w=[wt2]}, calm down!{w=[wt3]} It was an accident!"
                
                # WSIS pushes HERO toward the couch and climbs on top to continue fighting
                
                wsis "Accident my ass!{w=[wt2]} You did that on purpose!{nw}"
                show wsis_midnightlunch_3_hero_body 1 at CC_fast
                show wsis_midnightlunch_3_hero_wear 1_common at CC_fast
                show wsis_midnightlunch_3_wsis_body 2 at CC_fast
                show wsis_midnightlunch_3_wsis_wear 2_common at CC_fast
                wsis "Accident my ass! You did that on purpose!{fast}"

                play SE1 "Slip.ogg"

                show wsis_midnightlunch_3_hero_body 2 at CC
                show wsis_midnightlunch_3_hero_wear 2_common at CC
                with hpunch

                hero "W{w=[wt1]}-wait!{nw}"

                play SE1 "Slip.ogg"

                hide wsis_midnightlunch_3_hero_body
                hide wsis_midnightlunch_3_hero_wear
                show wsis_midnightlunch_3_wsis_body 3 at CC
                show wsis_midnightlunch_3_wsis_wear 3_common at CC
                hero "W-wait!{fast}"
                
                jump wsis_wrestling_sofa
            
            else:
                stop BGM fadeout 6
                scene bg_0
                show wsis_punch_3_hero_body 1
                show wsis_punch_3_hero_wear 1_common
                with Fade(0.5, 0, 1)

                hero "{aw}Ugh...!{/aw}"

                wsis "Serves you right{w=[wt2]}, you perverted moron!"

                scene bg_0
                with Dissolve(3)
                play BGM "audio/W2C - Tranquility.mp3"

                jump show_ui

    jump show_ui

# ---------------------------------------------------------------------------
label wsis_wrestling_sofa: # Wrestling scene on the sofa
# ---------------------------------------------------------------------------

    scene wsis_wrestling_1_bg home_livingroom
    show wsis_wrestling_1_char_body 1
    show wsis_wrestling_1_wsis_wear 1_common
    show wsis_wrestling_1_hero_wear 1_common
    show wsis_wrestling_1_wsis_face 1o0
    show wsis_wrestling_1_wsis_fg 1
    show wsis_wrestling_1_hero_head 1
    show fx_light:
        blend "add"
    with dissolve

    $ var_tio = 0
    $ var_tim = 5
    $ var_bao = 20
    $ var_bam = 40
    $ var_npc = round(1, 2)
    $ var_pla = round((0.5 + (perk_phy_str * 0.5)) * (1 + (stat_phy * 0.02)), 2)
    $ a_event_3 = 1 / var_pla

    menu:
        "Defend Yourself{pr}{size=-10}[C_Not] {b}💪 Thug Of War 💪{/b}{pr}Difficult Level: [var_npc], Your Level: [var_pla]{/size}":
            show wsis_wrestling_1_vid 1_common
            hide fx_light
            show fx_light:
                blend "add"
            call screen minigame_thugofwar_1()
            $ renpy.block_rollback()
            hide wsis_wrestling_1_vid 1_common

    if _return == "Lose":
        play SE1 "Hit1.ogg"

        scene wsis_wrestling_1_bg home_livingroom
        show wsis_wrestling_1_char_body 4
        show wsis_wrestling_1_hero_wear 4_common
        show wsis_wrestling_1_wsis_wear 4_common
        show wsis_wrestling_1_wsis_face 4o0
        show wsis_wrestling_1_wsis_fg 4
        show fx_light:
            blend "add"
        with hpunch

        pause

        stop BGM fadeout 5

        scene bg_0
        with Dissolve(1)

        play SE1 "JingleWrong.ogg"

        show wsis_punch_3_hero_body 1
        show wsis_punch_3_hero_wear 1_common
        with Dissolve(1)

        pause

        scene bg_0
        with Dissolve(3)

        call gametime from _call_gametime_117

        play BGM "audio/W2C - Tranquility.mp3"

        jump show_ui

    play SE1 "JingleRight.mp3"
    $ renpy.pause(delay=0.5, hard=True)

    show wsis_wrestling_1_char_body 2
    show wsis_wrestling_1_wsis_wear 2_common
    show wsis_wrestling_1_hero_wear 2_common
    show wsis_wrestling_1_wsis_face 2o0
    show wsis_wrestling_1_wsis_fg 2
    with dissolve
    # WSIS is on top of HERO on the couch, trying to hit him while he holds her hands

    show wsis_wrestling_1_wsis_face 2o1
    wsis "Let me go so I can punch your stupid face!"
    
    show wsis_wrestling_1_wsis_face 2o0
    hero "You need to calm down!"
    
    show wsis_wrestling_1_wsis_face 2o1
    wsis "I'll only calm down when I beat your jerk face up!"
    
    show wsis_wrestling_1_wsis_face 2o0
    hero "B{w=[wt1]}-but this position is..."
    
    show wsis_wrestling_1_wsis_face 2o1
    wsis "Shut up and let me punch you!!!"

    show wsis_wrestling_1_wsis_face 2o0 with None

    call gametime_wait(22, 0) from _call_gametime_wait_29
    $ var_tio = 0
    $ var_tim = 10
    $ var_bao = 50
    $ var_bam = 100
    $ var_npc = round(1, 2)
    $ var_pla = round((0.5 + (perk_phy_str * 0.5)) * (1 + (stat_phy * 0.02)), 2)
    $ a_event_3 = 1 / var_pla

    menu:
        "Defend Yourself{pr}{size=-10}[C_Not]{b}💪 Thug Of War 💪{/b}{pr}Difficult Level: [var_npc], Your Level: [var_pla]{pr}Win ([C_Pos]+💕[C_Off]); Resist ([C_Pos]+🔥[C_Off])[C_Off]{/size}":
            show wsis_wrestling_1_vid 2_common
            hide fx_light
            show fx_light:
                blend "add"
            call screen minigame_thugofwar_2()
            $ renpy.block_rollback()
            hide wsis_wrestling_1_vid 2_common

    if _return == "Lose":
        stop BGM

        play SE1 "Hit1.ogg"

        scene wsis_wrestling_1_bg home_livingroom
        show wsis_wrestling_1_char_body 4
        show wsis_wrestling_1_hero_wear 4_common
        show wsis_wrestling_1_wsis_wear 4_common
        show wsis_wrestling_1_wsis_face 4o0
        show wsis_wrestling_1_wsis_fg 4
        show fx_light:
            blend "add"
        with hpunch

        pause

        stop BGM fadeout 5

        scene bg_0
        with Dissolve(1)

        play SE1 "JingleWrong.ogg"

        show wsis_punch_3_hero_body 1
        show wsis_punch_3_hero_wear 1_common
        with Dissolve(1)

        pause

        scene bg_0
        with Dissolve(3)

        play BGM "audio/W2C - Tranquility.mp3"

        jump show_ui

    elif _return == "Win":
        play SE1 "JingleRight.mp3"

        show wsis_wrestling_1_wsis_face 2o0
        hero "{aw}P{w=[wt1]}-please{w=[wt1]}, stop!{w=[wt2]} I don't wanna fight.{w=[wt2]} I'm sorry for that!{/aw}"

        $ add_stat("wsis", "love", 2)
        
        show wsis_wrestling_1_wsis_face 2o1
        wsis "Hmph{w=[wt2]}, so you better clean that mess you did before I lose the rest of my patience!"
        
        show wsis_wrestling_1_wsis_face 2o0
        hero "{bt}Fine... Fine...{/bt}"

        jump wsis_quest_1_kitchen_eat_table

    else:
        play SE1 "JingleRight.mp3"
        $ renpy.pause(delay=0.5, hard=True)
        stop BGM fadeout 3
        
        # They struggle, WSIS moving around trying to break free
            
        # During the struggle, WSIS's movements cause HERO to become aroused
        
        # WSIS feels something poking her from below

        play SE1 "Grow.mp3"

        show wsis_wrestling_1_char_body 3
        show wsis_wrestling_1_wsis_wear 3_common
        show wsis_wrestling_1_hero_wear 3_common
        show wsis_wrestling_1_wsis_face 3s1
        show wsis_wrestling_1_wsis_fg 3
        with Dissolve(1)

        play SE1 "Wow1.mp3"

        pause
        $ add_stat("wsis", "lust", 3)

        play BGM "audio/W2C - Adrenalust.mp3"
        
        hero "{aw}S{w=[wt1]}-sorry!{w=[wt2]} I couldn't help it{w=[wt2]}, y{w=[wt1]}-you were moving too much!{/aw}"

        # WSIS gets embarrassed and doesn't know how to react
        
        show wsis_wrestling_1_wsis_face 3s0
        wsis "..."
        
        # WSIS is flustered, her face red
        
        hero "{aw}Well{w=[wt2]}, c{w=[wt1]}-could you get off me?{/aw}"
        
        show wsis_wrestling_1_wsis_face 3o1
        wsis "H{w=[wt1]}-huh...?{w=[wt2]} I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} S{w=[wt1]}-Sure.{w=[wt3]} Stop bossing me around!"
        
        show wsis_wrestling_1_wsis_face 3s0 with None
        
        jump wsis_quest_1_kitchen_eat_table

# ---------------------------------------------------------------------------
label wsis_grocerystore: # Common Grocery Store Event
# ---------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_192

    play BGM "audio/W2C - Tranquility.mp3"

    scene sd1_grocerystore_4_bg
    show sd1_grocerystore_4_wsis 1
    with Dissolve(1)

    mind "(So{w=[wt2]}, we're here again.{w=[wt3]} Time to see what we have to buy.{w=[wt4]} Do I check [C_Nam][hero_to_wsis][C_Off] or just go to the cashier?)"

    menu:
        "Check [C_Nam][fnamewsis][C_Off]":
            pass

        "Go to the cashier":
            $ a_event_1 = 0
            jump wsis_grocerystore_cashier
    
    show sd1_grocerystore_4_wsis 2
    show sd1_grocerystore_4_wsis_face o1
    with dissolve
    wsis "Are you going to come or not?"

    show sd1_grocerystore_4_wsis_face o0
    "{nw}"

    scene sd1_grocerystore_5_bg
    show sd1_grocerystore_5_wsis_body
    show sd1_grocerystore_5_wsis_head 1
    with Fade(1,0,2)

    hero "So, [C_Nam][hero_to_wsis][C_Off] What do we have this time?"
    wsis "Looks like they've renewed their stock."

    show sd1_grocerystore_5_wsis_head 2
    show sd1_grocerystore_5_wsis_face o0
    with dissolve

    show sd1_grocerystore_5_wsis_face o1
    wsis "What do you want to buy?"

    show sd1_grocerystore_5_wsis_face o0
    hero "Well{w=[wt2]}, I don't know yet.{w=[wt2]} Let's keep looking."  

    hide sd1_grocerystore_5_wsis_face
    hide sd1_grocerystore_5_wsis_body
    hide sd1_grocerystore_5_wsis_head
    show sd1_grocerystore_5_wsis
    with dissolve

    pause

    mind "(Yes, [C_Nam][hero_to_wsis][C_Off],{w=[wt2]} let's just make sure we'll keep looking everything! ❤)"
    
    hide sd1_grocerystore_5_wsis
    show sd1_grocerystore_5_wsis_body
    show sd1_grocerystore_5_wsis_head 1
    with dissolve

    show sd1_grocerystore_5_wsis_head 2
    show sd1_grocerystore_5_wsis_face o0
    with dissolve

    wsis "Hmp!"
    mind "(Oops!)"

    play SE1 "Boing1.mp3"
    scene sd1_grocerystore_6_bg
    show sd1_grocerystore_6_fg
    with hpunch

    wsis "{aw}Ugh!{/aw}{w=[wt2]} Stop staring at me and get out!"

    scene sd1_grocerystore_7_bg
    show sd1_grocerystore_7_wsis_body
    show sd1_grocerystore_7_wsis_fg 1
    with Fade(1,0,1)

    pause

    show sd1_grocerystore_7_wsis_fg 2
    show sd1_grocerystore_7_wsis_face o0
    with dissolve

    show sd1_grocerystore_7_wsis_fg 3 with dissolve
    show sd1_grocerystore_7_wsis_face o1
    wsis "Look{w=[wt2]}, the prices on this shelf are a bit faded.{w=[wt3]} No one would be able to read them."

    show sd1_grocerystore_7_wsis_face o0 with None
    show sd1_grocerystore_7_wsis_fg 2 with dissolve
    hero "{bt}Ehhh...?{/bt}{w=[wt2]} Are you sure you're not the one who needs to increase the prescription on your glasses?"

    show sd1_grocerystore_7_wsis_face o1
    wsis "Shut up!{w=[wt3]} Of course you can't see anything too!"

    show sd1_grocerystore_7_wsis_face o0
    hero "You should know that I am very proud of my eyesight.{w=[wt3]} I can see things very well that no one knows I am seeing!"

    show sd1_grocerystore_7_wsis_face o1
    wsis "Hmph!{w=[wt2]} So take a look by yourself and tell me what you see!"

    scene sd1_grocerystore_8_bg
    show sd1_grocerystore_8_wsis_bg
    show sd1_grocerystore_8_wsis_mouth o0
    show sd1_grocerystore_8_wsis_fg
    with fade

    pause
    
    show sd1_grocerystore_8_wsis_mouth o1
    wsis "So? Are you going to tell me what number I couldn't see or not?"

    show sd1_grocerystore_8_wsis_mouth o0
    hero "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm still very proud of my eyesight for all I can see{w=[wt2]}, but maybe we should tell someone to change that price tag.{w=[wt2]} It's kinda faded, don't you think?"
    
    show sd1_grocerystore_8_wsis_mouth o1
    wsis "I have a better idea.{w=[wt2]} Let's go shopping before I can't control myself and start punching you right here.{w=[wt3]} What do you think?"

    show sd1_grocerystore_8_wsis_mouth o0
    hero "M{w=[wt1]}-maybe it's a great idea!"

    $ add_stat("wsis", "inti", 0.3)
    $ a_event_1 = 30

    label wsis_grocerystore_cashier:
        pass

    $ gametimemin += a_event_1 # Advance time
    $ wsis_know.append("HangOut_Groceries")

    $ add_stat("wsis", "inti", (a_event_1*0.01))

    scene bg_grocerystore with fade
    call screen UI_Menu_Inventory_Shop
    call action_walk from _call_action_walk_4
    #$ a_item_5 = "show_ui"
    #$ _skipping = False
    #call UI_buy_Item
    #$ _skipping = True

    jump show_ui

# ---------------------------------------------------------------------------
label wsis_sleeping: # Sleeping With Unlocked Door
# ---------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_193
    if wsis_map == "Home - Step-sis' bedroom" and wnei_map != wsis_map:
        scene wsis_badsleep3_bg
        show wsis_badsleep3_wsisbody
        show wsis_badsleep3_wsisoutfit pajama
        with Fade(0.25,0.25,2)
        pause
        mind "(I better let her rest now.)"

    elif wsis_map == "Home - Step-sis' bedroom" and wnei_map == wsis_map:
        scene wsis_girlsnight2_bg
        show wsis_girlsnight2_wsis_wnei
        if gametimehour >= 6 and gametimehour < 18:
            show wsis_girlsnight2_fx morning:
                blend "add"
        else:
            show wsis_girlsnight2_fx night:
                blend "add"
        with Fade(0.5,0,2)
        pause
        mind "(Looks like [C_Nam][hero_about_wsis][C_Off] got a really comfy pillow.)"

    scene bg_0 with dissolve
    jump goto_home_hallway

# ---------------------------------------------------------------------------
label wsis_quest_1_kitchen_eat_table(buceta=False, buceta_hero=[], buceta_wsis=[]): # Taking Her To Her Room
# ---------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_194

    stop BGM fadeout 8
    scene bg_0
    with Dissolve(2)

    if buceta == True:
        scene sitting_bg home_diningroom 1
        show sitting_mg home_diningroom
        show sitting_wsis_body 1 at RC
        show sitting_wsis_wear 1home at RC
        show sitting_hero_body 3 at LL
        show sitting_hero_wear 3home at LL
        show sitting_fg home_diningroom
        show fx_light:
            blend "add"
        with Dissolve(2)

        show sitting_hero_body 3 at CC_slow
        show sitting_hero_wear 3home at CC_slow

        "Here!"

        label wsis_quest_1_kitchen_eat_table_serve:
            menu:
                "Serve yourself":
                    call screen UI_Menu_Inventory_Transfer(invtop=inventory_home_table, invbot=buceta_hero, topname="Kitchen", botname="[C_Nam][fnamehero][C_Off] dish")
                    jump wsis_quest_1_kitchen_eat_table_serve

                "Serve [C_Nam][fnamewsis][C_Off]":
                    call screen UI_Menu_Inventory_Transfer(invtop=inventory_home_table, invbot=buceta_wsis, topname="Kitchen", botname="[C_Nam][fnamewsis][C_Off] dish")
                    jump wsis_quest_1_kitchen_eat_table_serve

                "continue":
                    pass

            if not any(xerequita.item_id == "Eat_Meal_EggFried" for xerequita in buceta_wsis) and any(xerequita.item_id == "Eat_Meal_EggFried" for xerequita in buceta_hero):
                wsis "You take it just for yourself! Where's mine!?"
                jump wsis_quest_1_kitchen_eat_table_serve
            elif not any(xerequita.item_id == "Eat_Meal_EggFried" for xerequita in buceta_wsis) and not any(xerequita.item_id == "Eat_Meal_EggFried" for xerequita in buceta_hero):
                wsis "Hurry up! Take the dishes!"
                jump wsis_quest_1_kitchen_eat_table_serve
            elif any(xerequita.item_id == "Eat_Meal_EggFried" for xerequita in buceta_wsis) and not any(xerequita.item_id == "Eat_Meal_EggFried" for xerequita in buceta_hero) and any(xerequita.item_id == "Eat_Meal_EggFried" for xerequita in inventory_home_table):
                wsis "If you don't want that one, just give me!"
                jump wsis_quest_1_kitchen_eat_table_serve
            elif any(xerequita.item_id == "Eat_Meal_EggFried" for xerequita in buceta_wsis) and not any(xerequita.item_id == "Eat_Meal_EggFried" for xerequita in buceta_hero) and not any(xerequita.item_id == "Eat_Meal_EggFried" for xerequita in inventory_home_table):
                wsis "Hmm? Really? Both for me?"
                menu:
                    "Confirm":
                        hero "Yes, you can eat both!"
                        wsis "{aw}Hmph...!{/aw} so don't tell I didn't ask!"
                        $ buceta = "wsis_2both"
                    "Deny":
                        hero "Sorry, I did it wrong!"
                        wsis "So hurry up and take yours before I change my mind, idiot!"
                        jump wsis_quest_1_kitchen_eat_table_serve

    scene sitting_bg home_diningroom 1
    show sitting_mg home_diningroom
    if buceta == "wsis_2both":
        show sitting_hero_body 1 at LC
        show sitting_hero_wear 1home at LC
        show sitting_hero_face 1a0 at LC
    else:
        show sitting_hero_body 2 at LC
        show sitting_hero_wear 2home at LC
    show sitting_wsis_body 2 at RC
    show sitting_wsis_wear 2home at RC
    show sitting_fg home_diningroom
    show fx_light:
        blend "add"
    with dissolve

    $ add_stat("wsis", "inti", 1)

    if buceta != False and not buceta_wsis==[]:
        label wsis_quest_1_kitchen_eat_table_eat:
            if any(xerequita.item_id == "Eat_Meal_EggFried" and xerequita.quality == 5 for xerequita in buceta_hero):
                $ stat_phy_bonus += 20
                $ msg.msg(renpy.translate_string("You ate [C_Itm]Fried Egg ([C_Dat]✦✦✦✦✦[C_Off])[C_Off] and received nutrients."))
                $ msg.msg(renpy.translate_string("[C_Pos]20% bonus[C_Off] for PHY gaining"))
            elif any(xerequita.item_id == "Eat_Meal_EggFried" and xerequita.quality == 4 for xerequita in buceta_hero):
                $ stat_phy_bonus += 10
                $ msg.msg(renpy.translate_string("You ate [C_Itm]Fried Egg ([C_Dat]✦✦✦✦[C_Off][C_Drk]✦[C_Off])[C_Off] and received nutrients."))
                $ msg.msg(renpy.translate_string("[C_Pos]10% bonus[C_Off] for PHY gaining"))
            elif any(xerequita.item_id == "Eat_Meal_EggFried" and xerequita.quality == 3 for xerequita in buceta_hero):
                $ stat_phy_bonus += 5
                $ msg.msg(renpy.translate_string("You ate [C_Itm]Fried Egg ([C_Dat]✦✦✦[C_Off][C_Drk]✦✦[C_Off])[C_Off] and received nutrients."))
                $ msg.msg(renpy.translate_string("[C_Pos]5% bonus[C_Off] for PHY gaining"))
            elif any(xerequita.item_id == "Eat_Meal_EggFried" and xerequita.quality == 2 for xerequita in buceta_hero):
                $ msg.msg(renpy.translate_string("You ate [C_Itm]Fried Egg ([C_Dat]✦✦[C_Off][C_Drk]✦✦✦[C_Off])[C_Off]. No nutrients received."))
            elif any(xerequita.item_id == "Eat_Meal_EggFried" and xerequita.quality == 1 for xerequita in buceta_hero):
                $ stat_phy_bonus -= 20
                $ msg.msg(renpy.translate_string("You ate [C_Itm]Fried Egg ([C_Dat]✦[C_Off][C_Drk]✦✦✦✦[C_Off])[C_Off]. No nutrients received."))
                $ msg.msg(renpy.translate_string("[C_Neg]-20% bonus[C_Off] for PHY gaining"))
            python:
                for xereca in buceta_hero:
                    if xereca.item_id == "Eat_Meal_EggFried":
                        buceta_hero.remove(xereca)
                        break

            if any(xerequita.item_id == "Eat_Meal_EggFried" and xerequita.quality == 5 for xerequita in buceta_wsis):
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] ate [C_Itm]Fried Egg ([C_Dat]✦✦✦✦✦[C_Off])[C_Off] and received nutrients."))
                $ add_stat("wsis", "love", 5)
                wsis "That's so good!"
            elif any(xerequita.item_id == "Eat_Meal_EggFried" and xerequita.quality == 4 for xerequita in buceta_wsis):
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] ate [C_Itm]Fried Egg ([C_Dat]✦✦✦✦[C_Off][C_Drk]✦[C_Off])[C_Off] and received nutrients."))
                $ add_stat("wsis", "love", 3)
                wsis "That's good!"
            elif any(xerequita.item_id == "Eat_Meal_EggFried" and xerequita.quality == 3 for xerequita in buceta_wsis):
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] ate [C_Itm]Fried Egg ([C_Dat]✦✦✦[C_Off][C_Drk]✦✦[C_Off])[C_Off] and received nutrients."))
                wsis "Ugh... That's bad!"
            elif any(xerequita.item_id == "Eat_Meal_EggFried" and xerequita.quality == 2 for xerequita in buceta_wsis):
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] ate [C_Itm]Fried Egg ([C_Dat]✦✦[C_Off][C_Drk]✦✦✦[C_Off])[C_Off]. No nutrients received."))
                $ add_stat("wsis", "love", -3)
                wsis "Yuck...! That's terrible!"
            elif any(xerequita.item_id == "Eat_Meal_EggFried" and xerequita.quality == 1 for xerequita in buceta_wsis):
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] bit [C_Itm]Egg ([C_Dat]✦[C_Off][C_Drk]✦✦✦✦[C_Off])[C_Off] and threw it away. No nutrients received."))
                $ add_stat("wsis", "love", -5)
                wsis "{aw}Blergh...!{/aw} What is that!?"
            python:
                for xereca in buceta_wsis:
                    if xereca.item_id == "Eat_Meal_EggFried":
                        buceta_wsis.remove(xereca)
                        break
            if len(buceta_wsis) >= 1:
                wsis "Next one!"
                $ buceta = "wsis_sick"
                jump wsis_quest_1_kitchen_eat_table_eat

    if buceta == "wsis_sick":
        "You and [C_Nam][fnamewsis][C_Off] had a lunch together.{w=[wt3]} But it seems she ate too much and got a stomachache and dizziness.{w=[wt3]} You decided to take her to her room."
        jump wsis_quest_1_0
    else:
        "You and [C_Nam][fnamewsis][C_Off] had a lunch together."
        jump show_ui

# ---------------------------------------------------------------------------
label wsis_quest_1_0: # Taking Her To Her Room
# ---------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_195

    stop BGM fadeout 8
    scene bg_0
    with Dissolve(2)

    play BGM "audio/W2C - Awkward.mp3" 

    scene wsis_badsleep1_bg
    show wsis_badsleep1_body 1
    if Get_NPCWear("wsis") == "casual":
        show wsis_badsleep1_outfit 1_party
    else: # if Get_NPCWear("wsis") == "home":
        show wsis_badsleep1_outfit 1_common
    show wsis_badsleep1_hero 1o0
    show wsis_badsleep1_wsis 1o0
    with Dissolve(2)

    show wsis_badsleep1_wsis 1o1
    wsis "I don't need your help that much, moron!"

    show wsis_badsleep1_hero 1o1
    show wsis_badsleep1_wsis 1o0
    hero "Haven't you said you were dazed?"

    show wsis_badsleep1_hero 1o0
    show wsis_badsleep1_wsis 1o1
    wsis "Hunf!{w=[wt2]} Whatev-{nw}"

    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off]'s  lust {color=#32FF32}+")+str((3 + (perk_cha_sex * 3)) * lustadd_wsis)[:4])
    $ wsis_lust += (3 + (perk_cha_sex * 3)) * lustadd_wsis

    play SE1 "Slip.ogg"
    wsis "Hunf!{w=[wt2]} Whatev-{fast}{w=0.1}{nw}"
    play SE2 "Moan1.mp3"

    hide wsis_badsleep1_wsis
    hide wsis_badsleep1_hero
    show wsis_badsleep1_body 1a
    if Get_NPCWear("wsis") == "casual":
        show wsis_badsleep1_outfit 1a_party
    else: # if Get_NPCWear("wsis") == "home":
        show wsis_badsleep1_outfit 1a_common

    pause(0.1)

    show wsis_badsleep1_body 1b
    if Get_NPCWear("wsis") == "casual":
        show wsis_badsleep1_outfit 1b_party
    else: # if Get_NPCWear("wsis") == "home":
        show wsis_badsleep1_outfit 1b_common

    pause(0.1)

    hide wsis_badsleep1_body
    hide wsis_badsleep1_outfit
    show wsis_badsleep1_wsishair
    show wsis_badsleep1_wsisarm 1
    show wsis_badsleep1_body 2
    if Get_NPCWear("wsis") == "casual":
        show wsis_badsleep1_outfit 2_party
    else: # Get_NPCWear("wsis") == "home":
        show wsis_badsleep1_outfit 2_common
    show wsis_badsleep1_wsis 2o1
    show wsis_badsleep1_hero 2o0
    show wsis_badsleep1_fg

    pause(0.5)

    hide wsis_badsleep1_fg
    hide wsis_badsleep1_wsis
    hide wsis_badsleep1_hero
    show wsis_badsleep1_herofx 1
    show wsis_badsleep1_wsisfx 1
    show wsis_badsleep1_wsis 2o1
    show wsis_badsleep1_hero 2o0
    show wsis_badsleep1_fg
    with dissolve

    show wsis_badsleep1_hero 2o1
    show wsis_badsleep1_wsis 2o0
    hero "Sorry!{w=[wt2]} I didn't mean to..."

    show wsis_badsleep1_hero 2o2
    show wsis_badsleep1_wsis 2o2
    wsis "{pa}YOU{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/pa}{nw}"

    show wsis_badsleep1_wsis 2s0
    show wsis_badsleep1_hero 2s0

    play SE1 "X_Gag1.mp3"

    show wsis_badsleep1_wsisfx 2
    with Dissolve(0.25)
    hide wsis_badsleep1_wsisarm
    show wsis_badsleep1_herofx 2
    show wsis_badsleep1_wsisarm 2
    with dissolve
    pause

    show wsis_badsleep1_hero 2o1
    hero "{aw}We better hurry up!{/aw}"

    scene bg_0
    with Dissolve(1)
    play SE1 "DoorOpen2.ogg"
    $renpy.pause(1, hard=True)
    play SE1 "CompartmentOpen.mp3"

    scene wsis_badsleep2_bg
    show wsis_badsleep2_wsisbody 1
    if Get_NPCWear("wsis") == "casual":
        show wsis_badsleep2_wsisoutfit party
    else: # if Get_NPCWear("wsis") == "home":
        show wsis_badsleep2_wsisoutfit common
    show wsis_badsleep2_hero 2
    with Dissolve(1)

    play SE1 "Vomit1.mp3"
    $renpy.pause(0.5, hard=True)
    play SE1 "Vomit2.mp3"
    $renpy.pause(2, hard=True)

    mind "(This situation was not quite what I expected tonight.{w=[wt2]} This scene is so...){nw}"

    menu:
        mind "(This situation was not quite what I expected tonight. This scene is so...){fast}"
        "Disgusting":
            play SE1 "Vomit3.mp3"
            show wsis_badsleep2_wsisbody at Shake2
            show wsis_badsleep2_wsisoutfit at Shake2
            pause(0.25)
            show wsis_badsleep2_hero 1
            with dissolve
            mind "(This situation was not quite what I expected tonight. This scene is so{fast} disgusting{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Yuck...!)"
            show wsis_badsleep2_hero 2
            with dissolve

        "Hot":
            if Get_NPCWear("wsis") == "home":
                mind "(This situation was not quite what I expected tonight. This scene is so{fast} hot{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} How can such a lean girl have a so big and round ass!?)"
            elif Get_NPCWear("wsis") == "casual":
                mind "(This situation was not quite what I expected tonight. This scene is so{fast} hot{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} How can such a lean girl have a so big and round ass!?{w=[wt3]} I'm grateful that she decided to wear these shorts today.)"

    show wsis_badsleep2_wsisbody 2
    show wsis_badsleep2_wsisface o0
    with Dissolve(1)

    show wsis_badsleep2_wsisface o1
    wsis "I'm better now.{w=[wt2]} Just a little tired."

    show wsis_badsleep2_wsisface o0
    hero "Just by precaution{w=[wt1]}, is there any remedies for stomach here?"
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
    show wsis_badsleep2_wsisface o1
    wsis "...{fast} I think mom keeps some in one of the kitchen cabinets.{w=[wt2]} But don't worry about that.{w=[wt2]} I just need to sleep."
    
    show wsis_badsleep2_wsisface o0
    hero "No{w=[wt1]}, you need to wake up better tomorrow.{w=[wt2]} Just go brush your teeth and lie down, and I'm gonna get it for you."
    
    show wsis_badsleep2_wsisface o0
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{nw}" 
    show wsis_badsleep2_wsisface o1
    wsis "...{fast} Okay.{w=[wt2]} T{w=[wt1]}-thank you.{w=[wt1]}{nw}"    
    show wsis_badsleep2_wsisface o0
    wsis "... Okay. T-thank you.{fast}"

    scene bg_0
    with Dissolve(2)
    $ wsis_act[1] = "sleeping"

    mind "(Found it!{w=[wt2]} Time to hurry and get back to [C_Nam][hero_about_wsis][C_Off] so she can rest.{w=[wt3]} Well{w=[wt1]}, she was quite tired.{w=[wt2]} I better come in without a noise{w=[wt1]}, so if she is sleeping it'll be better to let her sleep.)"

    if wsis_lust>=50:

        stop BGM fadeout 3

        scene wsis_masturbate_hero with Dissolve(3)
        mind "({aw}Ehhh...!?{/aw})"

        play BGM "audio/W2C - Intensity.mp3"

        show wsis_moan

        $ Speed = 1
        $ a_event_0 = 0
        $ a_event_1 = 0
        $ a_event_2 = 0
        $ a_event_3 = 0
        $ a_event_4 = 0
        $ a_event_5 = 0
        $ a_event_6 = 0
        $ a_event_7 = 0
        show screen wsis_masturbate1

        scene wsis_masturbate_bg
        show wsis_masturbate_mg 1
        show 2SIS breathe
        show wsis_masturbate_fx shadow:
            blend "multiply"
        show wsis_masturbate_fx light:
            blend "add"
        with Fade(0.5,0,3)

        pause

        mind "(Did she completely forgot that I was going back here?{w=[wt3]} No!{w=[wt2]} She looks kinda sleepy and probably don't even realize what she's doing!{w=[wt2]} I better forget about the medicines and just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}. K{w=[wt1]}-keep watching without making noise.{w=[wt2]} Just to make sure she's fine, of course!)"

        pause
        $ Speed = 2
        pause
        $ Speed = 3
        pause
        hide screen wsis_masturbate1
        show screen wsis_masturbate2

        play SE1 "JingleRight.ogg"
        if preferences.vibration == True:
            $ renpy.vibrate(1.5)
        $ wsis_lust = 0
        $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] came, and her lust reset."))
        $ xp_now += 25
        $ msg.msg(renpy.translate_string("XP [C_Pos]+ 25[C_Off]."))
        $ add_stat("wsis", "inti", 3)
        play SE2 renpy.random.choice(["Moan/A lvl3 (1).ogg", "Moan/A lvl3 (2).ogg", "Moan/A lvl3 (4).ogg", "Moan/A lvl3 (5).ogg", "Moan/A lvl3 (8).ogg"])

        pause(1)

        play SE2 renpy.random.choice(["Moan/A lvl7 (1).mp3", "Moan/A lvl7 (2).mp3", "Moan/A lvl7 (3).mp3"])

        pause(1)

        show wsis_masturbate_mg 2 with Dissolve(1)

        pause
        scene bg_0 with Dissolve(3)
        hide screen wsis_masturbate2

        mind "(I'd better get out of here quietly before she remembers the door is not closed and decides to look back and kill me.{w=[wt4]} Wow{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I think it'll be hard to sleep after having seen this wonder.{w=[wt3]} But{w=[wt2]}, even more harder than that is something else down here.{w=[wt3]} Anyway{w=[wt1]}, I will certainly sleep happily today.)"

    else:

        scene wsis_badsleep3_bg
        show wsis_badsleep3_wsisbody
        show wsis_badsleep3_wsisoutfit pajama
        with Dissolve(2)

        mind "(Did she sleep?)"

        #$personality[0] = "Hentai"

        if personality[0]=="Hentai":
            hero "[C_Nam][hero_about_wsis][C_Off]?{w=[wt3]} {bt}Yooo...?{/bt}{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Can you hear me?{w=[wt3]} No...?{w=[wt4]} You know{w=[wt1]}, I can't avoid looking at that big and fat ass of yours.{w=[wt2]} So{w=[wt1]}, I hope you don't mind that I try to look at different angles, okay?{w=[wt4]} {mind}(Well{w=[wt1]}, if I'm alive after this comment it means she really slept.{w=[wt3]} I better let her rest and check if she's okay in the early morning.){/mind}"

        elif personality[0]=="Kind":
            hero "[C_Nam][hero_about_wsis][C_Off]?{w=[wt3]} {bt}Yooo...?{/bt}{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Can you hear me?{w=[wt3]} No...?{w=[wt4]} You know{w=[wt1]}, I think you should stop calling me moron and start admitting that you love me and I'm the coolest person in the world.{w=[wt4]} {mind}(Well{w=[wt1]}, if I'm alive after this comment it means she really slept.{w=[wt3]} I better let her rest and check if she's okay in the early morning.){/mind}"
        else:
            hero "[C_Nam][hero_about_wsis][C_Off]?{w=[wt3]} {bt}Yooo...?{/bt}{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Can you hear me?{w=[wt3]} No...?{w=[wt4]} You know{w=[wt1]}, I think you need to stop eating that much{w=[wt2]}, otherwise{w=[wt1]}, your fat ass will continue to grow fatter and fatter!{w=[wt4]} {mind}(Well{w=[wt1]}, if I'm alive after this comment it means she really slept.{w=[wt3]} I better let her rest and check if she's okay in the early morning.){/mind}"

        $ add_stat("wsis", "love", 1)
        $ add_stat("wsis", "inti", 1)
        scene bg_0 with Dissolve(2)

    if wsis_quest_4 < 1:
        $ wsis_quest_4 = 1
    $ wsis_know.append("WSIS_is_sick")
    $ wsis_bedroom_lock = False
    $ gametimemin += 60
    call gametime from _call_gametime_118
    call goto_home_hallway from _call_goto_home_hallway_2
    $ StartAct("wsis", ("sleeping", 8*60), True)
    jump show_ui

# ---------------------------------------------------------------------------
screen wsis_masturbate1():
    timer 0.01 repeat True action If(a_event_1<5, true=(SetVariable("a_event_1", a_event_1+(0.05*Speed*Speed))), false=(SetVariable("a_event_1", 1)))

    timer 0.01 repeat True action [
    SetVariable("wsis_lust", wsis_lust + (0.01 * Speed * Speed)),
    If(a_event_3==0, true=(SetVariable("a_event_2", a_event_2+(0.001*Speed*Speed*Speed)), If(a_event_2>=(1/9)*(Speed*Speed), true=(SetVariable("a_event_3", 1))))),
    If(a_event_3==1, true=(SetVariable("a_event_2", a_event_2-(0.001*Speed*Speed*Speed)), If(a_event_2<=0, true=(SetVariable("a_event_3", 0))))),
    ]

    timer 0.01 repeat True action [
    If(a_event_5==0, true=(SetVariable("a_event_4", a_event_4+(0.005*Speed*Speed)), If(a_event_4>=(1/3)*(Speed), true=(SetVariable("a_event_5", 1))))),
    If(a_event_5==1, true=(SetVariable("a_event_4", a_event_4-(0.005*Speed*Speed)), If(a_event_4<=0, true=(SetVariable("a_event_5", 0))))),
    ]

    timer 0.5 repeat True action [
        If(not renpy.music.is_playing(channel="SE2"),
            
            true = [
                If(Speed==1,
                    true = [
                        Play("SE2", renpy.random.choice(["Moan/A lvl1 (1).ogg", "Moan/A lvl1 (2).ogg", "Moan/X lvl1 (1).ogg", "Moan/X lvl1 (2).ogg", "Moan/X lvl1 (3).ogg", "Moan/X lvl1 (4).ogg", "Moan/X lvl1 (5).ogg", "Moan/X lvl1 (6).ogg", "Moan/Z lvl1 (1).ogg", "Moan/Z lvl1 (2).ogg", "Moan/Z lvl1 (3).ogg", "Moan/Z lvl1 (4).ogg", "Moan/Z lvl1 (5).ogg"])),
                        ]),
                
                If(Speed==2,
                    true = [
                        Play("SE2", renpy.random.choice(["Moan/A lvl2 (1).ogg", "Moan/A lvl2 (2).ogg", "Moan/A lvl2 (3).ogg", "Moan/A lvl2 (4).ogg", "Moan/A lvl2 (5).ogg", "Moan/A lvl2 (6).ogg", "Moan/A lvl2 (7).ogg", "Moan/X lvl2 (1).ogg", "Moan/X lvl2 (2).ogg", "Moan/X lvl2 (3).ogg", "Moan/X lvl2 (4).ogg", "Moan/X lvl2 (5).ogg", "Moan/X lvl2 (6).ogg", "Moan/X lvl2 (7).ogg"])),
                        ]),
                
                If(Speed>=3,
                    true = [
                        Play("SE2", renpy.random.choice(["Moan/A lvl3 (1).ogg", "Moan/A lvl3 (2).ogg", "Moan/A lvl3 (3).ogg", "Moan/A lvl3 (4).ogg", "Moan/A lvl3 (5).ogg", "Moan/A lvl3 (6).ogg", "Moan/A lvl3 (7).ogg", "Moan/A lvl3 (8).ogg", "Moan/X lvl3 (1).ogg", "Moan/X lvl3 (2).ogg"])),
                        ]),
    
                ])]

    vbar value wsis_lust range 100 xpos 25 ypos 25 xmaximum 100 ymaximum 1030

# ---------------------------------------------------------------------------
screen wsis_masturbate2():
    timer 0.01 repeat True action [
    If(a_event_5==0 and a_event_0<7, true=(SetVariable("a_event_4", a_event_4+(0.1*Speed)), If(a_event_4>0 and a_event_0<7, true=(SetVariable("a_event_5", 1), SetVariable("a_event_0", a_event_0 + 1))))),
    If(a_event_5>=1 and a_event_0<7, true=(SetVariable("a_event_4", a_event_4-(0.1*Speed)), If(a_event_4<=0 and a_event_0<7, true=(SetVariable("a_event_5", 0))))),
    ]

    timer 0.01 repeat True action If(a_event_0>=7, true= SetVariable("a_event_1", max(0, a_event_1-0.1)))
    timer 0.01 repeat True action If(a_event_0>=7, true= SetVariable("a_event_2", max(0, a_event_2-0.01)))
    timer 0.01 repeat True action [
    If(a_event_5==0 and a_event_0>=7, true=(SetVariable("a_event_4", a_event_4+(0.005*Speed)), If(a_event_4>=1 and a_event_0>=7, true=(SetVariable("a_event_5", 1))))),
    If(a_event_5==1 and a_event_0>=7, true=(SetVariable("a_event_4", a_event_4-(0.005*Speed)), If(a_event_4<=0 and a_event_0>=7, true=(SetVariable("a_event_5", 0))))),
    ]
    timer 0.01 repeat True action If(a_event_0>=7, true= SetVariable("a_event_6", min(1, a_event_6+0.01)))
    timer 0.01 repeat True action If(a_event_0>=7, true= SetVariable("a_event_7", min(1, a_event_7+0.01)))

# ---------------------------------------------------------------------------
label wsis_quest_1_1: # Waking Her Up
# ---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_196
    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night

    $ wsis_know.remove("WSIS_is_sick")
    $ wsis_know.append("WSIS_Quest_1_1")
    $ wsis_know.append("WakeUp")
    $ gametimemin += 20
    mind "(Is she still sleeping?...{w=[wt3]} I better check if she's okay...)"

    play SE1 "DoorOpen1.ogg"
    $ Set_CharMap("hero", "home", "bedroom_wsis")
    scene bg_0
    with Dissolve(1)

    hero "{aw}E{w=[wt1]}-excuse me...{w=[wt2]} I{w=[wt1]}-I'm going in...{/aw}"
    
    scene wsis_wakeup1_bg
    show wsis_wakeup1_wsisbodybg 1
    show wsis_wakeup1_wsisbody 1
    show wsis_wakeup1_herobody 1 at OL
    show wsis_wakeup1_herobody 1 at CC_slow
    with Dissolve(3)

    mind "(I'm not doing anything wrong{w=[wt4]}, right?{w=[wt4]} Okay{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Here goes nothing!)"

    $X_spd = 0.2
    $X_pos = 3
    $X_rot = 0.2

    hide wsis_wakeup1_herobody
    show wsis_wakeup1_heroarm 2 at XLoop_Move
    show wsis_wakeup1_herobody 2

    $X_pos = 1
    $X_rot = 0.1
    show wsis_wakeup1_wsisbodybg 1 at XLoop_Rotate
    with Dissolve(1)

    if perk_cha_sex>=1:                
        $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off]'s  lust {color=#32FF32}+")+str(0.5 * perk_cha_sex * lustadd_wsis)[:4])
        $ wsis_lust += 0.5 * perk_cha_sex * lustadd_wsis

    $ a_event_0 = str(hero_to_wsis[:1])
    hero "{aw}W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.[a_event_0!c]-{w=[wt1]}{color=#64C8FF}[hero_to_wsis]{/color}?...{/aw}"

    play SE2 "Moan - Soft.mp3"
    hide wsis_wakeup1_wsisbodybg
    hide wsis_wakeup1_heroarm
    show wsis_wakeup1_wsisbody 2
    show wsis_wakeup1_herobody 3
    show wsis_wakeup1_herofx 1
    with Dissolve(1)
    pause(2)

    mind "(.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}I don't know if I'll survive when she opens her eyes{w=[wt2]}, but I'm grateful to have lived so far.{w=[wt3]} Yes{w=[wt2]}, my life was certainly worth it!!)"

    pause (0.5)
    show wsis_wakeup1_wsisbody 3
    show wsis_wakeup1_wsisface3 o0
    with Dissolve(1)

    pause (0.5)
    wsis "..."
    show wsis_wakeup1_wsisface3 o1
    show wsis_wakeup1_herofx 2
    with Dissolve(1)
    wsis "!!!"

    hero "{aw}W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} G{w=[wt1]}-good mor{w=[wt1]}-{/aw}{nw}"

    play SE1 "Hit1.ogg"
    hide wsis_wakeup1_herofx
    hide wsis_wakeup1_wsisface3
    show wsis_wakeup1_wsisbody 4
    show wsis_wakeup1_herobody 4

    if personality[0]=="Hentai":
        wsis "You pervert!{w=[wt2]} What do you think you're doing in my room!?"
    else:
        wsis "What do you think you're doing in my room!?"

    show wsis_wakeup1_wsisbody 5
    show wsis_wakeup1_wsisface5 o0
    show wsis_wakeup1_herobody 5a
    show wsis_wakeup1_herofx 3
    with dissolve

    hero "I was worried about last night and came to see if you were fine!"

    show wsis_wakeup1_herobody 5b

    if not personality[0]=="Hentai":
        $ add_stat("wsis", "love", 1)
        $ add_stat("hero", "cha_soc", 1)

        show wsis_wakeup1_wsisface5 o1
        wsis "Huh?..."
    else:
        show wsis_wakeup1_wsisface5 s0
        wsis "{bt}Hmmm...{/bt}"

    scene bg_0
    with Dissolve(1.5)

    pause(0.5)
    $ add_stat("wsis", "inti", 1)
    pause(1)

    $ wsis_quest_4 = 2
    $ Set_CharMap("hero", "home", "bedroom_wsis")

    $ StartAct("wsis", ("sleeping", 0), True)
    call gamecheck from _call_gamecheck_35
    jump wsis_interact_start
    #jump wsis_interact_check

# ---------------------------------------------------------------------------
label wsis_watchingtv: # Watching TV
# ---------------------------------------------------------------------------

    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night

    scene wsis_watchingtv_bg 1
    show wsis_watchingtv1_wsisbody 1
    show wsis_watchingtv1_wsisface 1o0
    show wsis_watchingtv1_wsisfg 1
    with fade

    "[C_Nam][fnamewsis][C_Off] is watching TV{nw}"
    menu:
        "[C_Nam][fnamewsis][C_Off] is watching TV{fast}"
        "Join her":
            pass
        "Return":
            jump show_ui

    hero "Hey, [C_Nam][hero_to_wsis][C_Off].{w=[wt2]} Can I join you?"

    show wsis_watchingtv1_wsisface 1o1
    wsis "Whatever."

    show wsis_watchingtv1_wsisbody 2
    show wsis_watchingtv1_wsisface 2o0
    show wsis_watchingtv1_wsisfg 2
    show wsis_watchingtv1_herobody
    show wsis_watchingtv1_heroface a0
    with Dissolve(1)
    pause(0.5)

    show wsis_watchingtv1_heroface a1
    hero "What's kind of channel is this?{w=[wt2]} I've never seen it!"

    show wsis_watchingtv1_wsisface 2o1
    show wsis_watchingtv1_heroface a0
    wsis "It's not channel, you moron.{w=[wt2]} It's from NetFux."

    show wsis_watchingtv1_wsisface 2o0
    show wsis_watchingtv1_heroface a1
    hero "NetFux?"

    show wsis_watchingtv1_wsisface 2o1
    show wsis_watchingtv1_heroface a0
    wsis "It's a streaming service.{w=[wt2]} There are a lot of series and movies{w=[wt1]}, and you just select what you wanna watch."

    show wsis_watchingtv1_wsisface 2o0
    show wsis_watchingtv1_heroface a1
    hero "Wow!{w=[wt3]} So you can choose whatever you wanna watch?{w=[wt2]} Is that possible?"

    show wsis_watchingtv1_wsisface 2a1
    show wsis_watchingtv1_heroface a2
    wsis "{gg}Fuu-Fuu-Fuu...{/gg}{w=[wt2]} You're really a bumpkin, aren't you?"

    show wsis_watchingtv1_wsisface 2a0
    show wsis_watchingtv1_heroface a2
    mind "(Damn it.{w=[wt2]} Does she only get in a good mood with me when she is mocking me?)"

    scene bg_0
    with Dissolve(2)

    $ a_event_1 = (gametimehour * 60) + gametimemin
    $ a_event_2 = (17 - gametimehour)/10
    $ gametimemin += 1020 - a_event_1
    $ add_stat("wsis", "inti", a_event_2)

    $ wsis_quest[7] = 1
    call gametime from _call_gametime_119
    jump show_ui

# ---------------------------------------------------------------------------
label wsis_quest_4: # Hang out in the park
# ---------------------------------------------------------------------------

    $ config.menu_include_disabled = False
    $ hero_mood = "A1"
    $ wsis_mood = "O1"
    $ wsis_fx = 0
    $ hero_fx = 0
    $ wsis_wear = "school"

    scene bg_park
    show HERO at OL
    show WSIS at OL
    show HERO at RC_heavy
    show WSIS at LC_heavy
    with Dissolve(2)

    wsis "Wait{w=[wt1]}, let's rest a little here."

    $ hero_mood = "A2"
    hero "Eh...?{w=[wt2]} We're already almost there!"

    $ wsis_mood = "O2"
    wsis "Ugh, can't you be less selfish at least once?{w=[wt2]} My foot hurts!"
    hero "Hey{w=[wt1]}, hold up!{w=[wt2]} I didn't know."
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Sorry."

    $ hero_mood = "A4"
    hero "{bt}Ohhh...?{/bt}{w=[wt2]} Did I hear it right?"

    $ wsis_mood = "O3"
    $ hero_mood = "O1"
    wsis "{pa}Ugh!{/pa}{w=[wt2]} Why don't you just shut up when I'm trying to be nice with you!?{w=[wt3]} You know?{w=[wt2]} You can go without me!{w=[wt2]} I don't give a shit!!!{nw}"
    show WSIS at OL_heavy
    wsis "{pa}Ugh!{/pa} Why don't you just shut up when I'm trying to be nice with you!? You know? You can go without me! I don't give a shit!!!{fast}"
    mind "(What? Why does she always ends up treating me like that...?)"
    show HERO at OL_heavy
    mind "{nw}"

    # ---------------------------------------------------------------------------

    stop BGM fadeout 2
    scene bg_0
    with Dissolve(2)
    play BGM "audio/W2C - Memories.mp3" fadein 3

    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night

    scene scen_1_hangoutpark1
    show scen_1_hangoutpark1_z1 a
    show scen_1_hangoutpark1_z2
    show scen_1_hangoutpark1_z3heroeyebrows 2
    show scen_1_hangoutpark1_z3heroeyes 2
    show scen_1_hangoutpark1_z3heromouth o0
    show scen_1_hangoutpark1_z4wsis1 o0
    with Dissolve(3)
    
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"
    show scen_1_hangoutpark1_z4wsis1 o1
    wsis "...{fast} Why did you come?"

    show scen_1_hangoutpark1_z3heromouth o1
    show scen_1_hangoutpark1_z4wsis1 o0
    hero "Of course I wouldn't go home and leave you alone with your foot injured."

    show scen_1_hangoutpark1_z3heromouth o0
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
    show scen_1_hangoutpark1_z4wsis1 o1
    wsis "...{fast} It's not a big deal.{w=[wt2]} I just stepped on a pothole a while ago.{w=[wt2]} Why do you act as if you care so much?"

    show scen_1_hangoutpark1_z3heroeyes 3
    show scen_1_hangoutpark1_z3heromouth o1
    show scen_1_hangoutpark1_z3heroeyebrows 1
    show scen_1_hangoutpark1_z4wsis1 o0
    hero "What makes you say that?"
    
    show scen_1_hangoutpark1_z3heromouth o0
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
    show scen_1_hangoutpark1_z4wsis1 o1
    wsis "...{fast} Never mind.{w=[wt2]} I'm just stressed.{w=[wt2]} Maybe I just need to swing a little bit."

    show scen_1_hangoutpark1_z4wsis1 o0
    show scen_1_hangoutpark1_z3heromouth a1
    show scen_1_hangoutpark1_z3heroeyebrows 2
    hero "{gg}Fuu-Fuu-Fuu...{/gg}{w=[wt2]} In this case..."

    show scen_1_hangoutpark1_z4wsis1 o3
    show scen_1_hangoutpark1_z3heromouth a0
    show scen_1_hangoutpark1_z3heroeyebrows 3
    wsis "What?"

    scene scen_1_hangoutpark2a
    with dissolve

    hero "{bt}{size=60}...SWIIING!!!{/size}{/bt}"
    wsis "{aw}H{w=[wt1]}-heeey!{w=[wt2]} Stop it!{/aw}"
    hero "What?{w=[wt2]} I can not hear you!{w=[wt2]} Are you telling me to push harder?"
    wsis "{bt=a5-s0.5-p10}{sc=1}{size=50}Nooooo!!!{/size}{/sc}{/bt}"
    hero "{bt}{size=60}So here we go!!!{/size}{/bt}"

    scene scen_1_hangoutpark2b
    with Dissolve(2)

    $ add_stat("wsis", "love", 1)
    $ add_stat("hero", "cha_soc", 1)
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off]'s  love {color=#32FF32}+")+str(1 * loveadd_wsis)[:4])

    scene bg_1
    with Dissolve(2)

    $ add_stat("wsis", "inti", 1)
    pause(1)

    scene scen_1_hangoutpark1
    show scen_1_hangoutpark1_z1 a
    show scen_1_hangoutpark1_z2
    show scen_1_hangoutpark1_z3heroeyebrows 1
    show scen_1_hangoutpark1_z3heroeyes 2
    show scen_1_hangoutpark1_z3heromouth a0
    show scen_1_hangoutpark1_z4wsis1 a0
    with Dissolve(3)


    hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
    show scen_1_hangoutpark1_z3heroeyebrows 2
    show scen_1_hangoutpark1_z3heromouth a1
    hero "...{fast} Hey, [C_Nam][hero_to_wsis][C_Off]{w=[wt2]}, this park hasn't changed at all, has it?{w=[wt3]} It's exactly the same place we used to come in childhood!"
    show scen_1_hangoutpark1_z3heromouth a0
    wsis "{w=[wt2]}.{w=[wt2]}.{w=[wt2]}.{w=[wt2]}{nw}"
    show scen_1_hangoutpark1_z4wsis1 a1
    wsis "...{fast} So{w=[wt1]}, do you remember?"
    show scen_1_hangoutpark1_z4wsis1 a0
    show scen_1_hangoutpark1_z3heromouth a1
    hero "Of course I do!{w=[wt2]} Daddy used to bring us here every week, didn't he?"
    show scen_1_hangoutpark1_z3heromouth a0
    show scen_1_hangoutpark1_z4wsis1 o0
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}{nw}"
    show scen_1_hangoutpark1_z4wsis1 o1
    wsis "...{fast} I missed him so much{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."
    show scen_1_hangoutpark1_z4wsis1 o0
    show scen_1_hangoutpark1_z3heromouth o0
    show scen_1_hangoutpark1_z3heroeyes 3
    hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}{nw}"
    show scen_1_hangoutpark1_z3heromouth o1
    show scen_1_hangoutpark1_z3heroeyebrows 1
    hero "...{fast} Indeed..."
    show scen_1_hangoutpark1_z3heromouth o2
    show scen_1_hangoutpark1_z4wsis1 o1
    wsis "I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I see him as my real father{w=[wt2]}, since the man who brought me into the world never had the courage to acknowledge me, you know?{w=[wt3]} S{w=[wt1]}-sorry for bringing this up!{w=[wt1]} I just..."
    show scen_1_hangoutpark1_z3heromouth a1
    show scen_1_hangoutpark1_z3heroeyes 2
    show scen_1_hangoutpark1_z3heroeyebrows 2
    show scen_1_hangoutpark1_z4wsis1 o0
    hero "You don't need to worry!{w=[wt2]} I know how much you like Daddy{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Actually{w=[wt2]}, I used to be kinda jealous of that!"
    show scen_1_hangoutpark1_z3heroeyes 2
    show scen_1_hangoutpark1_z3heromouth a0
    show scen_1_hangoutpark1_z4wsis1 a1
    wsis "{gg}Hee-hee{/gg}{w=[wt4]} But we used to play a lot, didn't we?..."
    show scen_1_hangoutpark1_z3heromouth a1
    show scen_1_hangoutpark1_z4wsis1 a0
    hero "Huh{w=[wt2]}, it really was...?{w=[wt3]} It seems that you fought with me more than you played.{w=[wt3]}{nw}"

    show scen_1_hangoutpark1_z3heroeyes 3
    hero "Huh, it really was...? It seems that you fought with me more than you played.{fast} Not that it has changed much, right?"
    show scen_1_hangoutpark1_z4wsis1 o0
    show scen_1_hangoutpark1_z3heromouth a0
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
    show scen_1_hangoutpark1_z4wsis1 o1
    wsis "...{fast} So{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} T{w=[wt1]}-that's how do you feel?{w=[wt3]} I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'm sorry..."

    show scen_1_hangoutpark1_z1 b
    hide scen_1_hangoutpark1_z4wsis1
    hide scen_1_hangoutpark1_z2
    show scen_1_hangoutpark1_z4wsis2 o0
    show scen_1_hangoutpark1_z4wsis2fg 1
    show scen_1_hangoutpark1_z3heroeyes 1
    show scen_1_hangoutpark1_z3heromouth o1
    show scen_1_hangoutpark1_z3herofx 1
    show scen_1_hangoutpark1_z2
    with Dissolve(2)

    stop BGM fadeout 4

    show scen_1_hangoutpark1_z4wsis2 o1
    wsis "I think you're right.{w=[wt3]} Perhaps I was never a good person.{w=[wt3]} People may be right for avoiding me."

    play BGM "audio/W2C - Romance.mp3" fadein 4
    show scen_1_hangoutpark1_z4wsis2 o0

    mind "(What is this?{w=[wt3]} [C_Nam][hero_about_wsis!c][C_Off] got so sweet as soon as she entered a state of self-awareness!{w=[wt3]} And now she's kinda{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Cute!{w=[wt4]} What's this{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Feeling...!?)"

    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"
    wsis "...{fast} !!!{w=[wt1]}{nw}"

    show scen_1_hangoutpark1_z4wsis2fg 2
    with Dissolve(1)
    hide scen_1_hangoutpark1_z4wsis2
    hide scen_1_hangoutpark1_z4wsis2fg
    show scen_1_hangoutpark1_z1 a
    show scen_1_hangoutpark1_z4wsis1 a1
    show scen_1_hangoutpark1_z4wsis1fx 1
    with dissolve

    wsis "W{w=[wt1]}-well!...{w=[wt2]} The ache passed a little.{w=[wt2]} L{w=[wt1]}-Let's go back home!"
    show scen_1_hangoutpark1_z4wsis1 a0
    if stat_cha>=10:
        $ wsis_mood = "O3"
        $ wsis_fx = 2
        show scen_1_hangoutpark1_z3heromouth o3
        hero "W{w=[wt1]}-wait!{w=[wt2]} Listen!"
        show scen_1_hangoutpark1_z3heromouth o2
        wsis "Hm?"
        show scen_1_hangoutpark1_z3heroeyebrows 3
        show scen_1_hangoutpark1_z3heromouth o3
        show scen_1_hangoutpark1_z3herofx 2
        hero "Sometimes I'll do things that probably will make you upset.{w=[wt3]} Maybe it will be just to tease you{w=[wt2]}, or maybe cos I'm very stupid to understand things{w=[wt2]}, but I do really want us to get along.{w=[wt2]} I like the way you are and don't care if people don't!"

        show scen_1_hangoutpark1_z4wsis1 o3
        show scen_1_hangoutpark1_z3heromouth o2
        show scen_1_hangoutpark1_z3heroeyebrows 2
        wsis "{pa}Ahhh{w=[wt2]} SHUT UP!!!{/pa}{w=[wt3]}{pr}{aw}What’s with the sappy lines all of a sudden!?{w=[wt2]} W{w=[wt1]}-We must return home!{/aw}"
    else:
        $ wsis_mood = "A1"
        $ wsis_fx = 1

    scene bg_park
    show HERO at OR
    show WSIS at OR
    with dissolve

    $ hero_mood = "O1"
    $ hero_fx = 1
    $ X_spd = 2.5
    show WSIS at OL_X
    show HERO at RC_X

    hero "W{w=[wt1]}-wait!{w=[wt1]}-{w=[wt1]}{nw}"
    wsis "HURRY UP!!!"

    show HERO at OL_X
    hero "That's not fair.{w=[wt3]} Oh, shit."
    window hide
    stop BGM fadeout 4

    $ wsis_wear = "school"
    $ gametimehour += 1
    call goto_home_livingroom from _call_goto_home_livingroom_6
    scene bg_0
    with Dissolve(1)

    $ wsis_quest_1 = 1
    $ wsis_inti_cap = char_inti_req_date
    $ msg.msg(renpy.translate_string("⭐ Intimacy cap increased"))

    pause(1)
    $ add_stat("wsis", "love", 2)
    $ add_stat("hero", "cha_soc", 2)
    pause(1)
    $ add_stat("wsis", "inti", 1)
    pause(1)

    jump show_ui

# ---------------------------------------------------------------------------
label wsis_quest_5: # Unspoken Wounds
# ---------------------------------------------------------------------------
    $ is_specialevent = True

    stop BGM fadeout 4

    scene bg_0 with Dissolve(1)
    scene bg_1
    show wsis_slap_1_char 1
    show fx_light
    with Dissolve(2)

    pause

    play SE1 "Hit4.mp3"
    show wsis_slap_1_char 2
    show fx_hit 1 at Hit_XYZ(0.4, 0.3, 0.1)
    with None

    if Check_CharInMap("hero", "home", "living_room"):
        scene wsis_slap_1_bg kitchen
    elif Check_CharInMap("hero", "home", "bedroom_wsis"):
        scene wsis_slap_1_bg bedroom_wsis
    else:
        scene bg_1
    show wsis_slap_1_char 3
    show fx_light
    with Dissolve(3)

    pause

    play BGM "audio/W2C - Drama.mp3"
    
    if Check_CharInMap("hero", "home", "living_room"):
        scene wsis_slap_1_bg kitchen
    elif Check_CharInMap("hero", "home", "bedroom_wsis"):
        scene wsis_slap_1_bg bedroom_wsis
    else:
        scene bg_1
    show wsis_slap_1_hero 3
    show wsis_slap_1_hero_face 3o0
    show wsis_slap_1_wsis 3
    show wsis_slap_1_wsis_face 3o0
    show fx_light
    with Dissolve(1)

    pause

    show wsis_slap_1_wsis_face 3o1
    wsis "{aw}{b}ENOUGH{/b}!{/aw}{w=[wt3]} Don't you {b}dare{/b} think you have the right to do whatever you want{w=[wt1]}, whenever you want!{w=[wt3]} You better know your place!"

    show wsis_slap_1_wsis_face 3o0
    show wsis_slap_1_hero_face 3o1
    hero "W{w=[wt1]}-What{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} What was that for!?{w=[wt3]} Isn't that a bit much...?{w} I didn't think{w=[wt1]}-{nw}"

    show wsis_slap_1_wsis_face 3o1
    show wsis_slap_1_hero_face 3o0
    wsis "{aw}{b}OF COURSE YOU DIDN'T THINK{/b}!{/aw}{w=[wt3]} You never {b}THINK{/b} about anything other than yourself!{w=[wt3]} You just assume you can do whatever you want without considering how others feel{w=[wt1]}, right!?"

    show wsis_slap_1_wsis_face 3o0
    show wsis_slap_1_hero_face 3o1
    hero "I'm sorry{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I don't understand{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}"
    
    hero "Why are you acting like this?{w=[wt3]} Ever since I got back{w=[wt1]}, I've been trying to get along with you{w=[wt1]}, and you're always treating me so badly{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}"
    
    hero "Just when I thought we were starting to get along{w=[wt1]}, you freak out{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} What did I do to you?"

    show wsis_slap_1_wsis_face 3o1
    show wsis_slap_1_hero_face 3o0
    wsis "Trying to get along with me{w=[wt1]}, you say?{w=[wt3]} Don't act as if it's something you really care about!"
    
    wsis "You only pretend to care because you needed to live with us again!{w=[wt3]} But you never really gave a shit about anyone but yourself{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} It's just more convenient for you now than to avoid me with all your forces!"
    
    show wsis_slap_1_wsis_face 3o0
    show wsis_slap_1_hero_face 3o1
    hero "What!?{w=[wt3]} Why?{w=[wt3]} Why are you saying that!?"

    show wsis_slap_1_wsis_face 3o1
    show wsis_slap_1_hero_face 3o0
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}Sure{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Of course you wouldn't remember when we talked a few years ago on the internet, right?{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} That meant nothing to you except an opportunity to show the contempt you felt for me, right?"

    show wsis_slap_1_wsis_face 3o0
    show wsis_slap_1_hero_face 3o1
    hero "That's not true!{w=[wt3]} Of course I felt the same way by talking to you!{w=[wt3]} What are you saying?"
    
    show wsis_slap_1_wsis_face 3o1
    show wsis_slap_1_hero_face 3o0
    wsis "I was so happy{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Pathetically happy{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} I've missed you so much{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} I missed our games{w=[wt1]}, our laughs{w=[wt1]}, everything{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}"
    
    wsis "But you{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} you acted so {b}cold{/b}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} You barely answered my messages{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} You never even cared about how I was doing{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} And then{w=[wt2]}, you just come back as if nothing happened{w=[wt2]}, and just keeps testing the limits of what you can do.{w=[wt3]} But I'm not going to let you have that freedom with me{w=[wt1]}, you stupid jerk!"

    show wsis_slap_1_wsis_face 3o0
    show wsis_slap_1_hero_face 3o1
    hero "That doesn't make sense!{w=[wt3]} I've always doing my best for we to get well...!"
    
    show wsis_slap_1_wsis_face 3o1
    show wsis_slap_1_hero_face 3o0
    wsis "{aw}What!?{/aw}{w=[wt3]} Okay{w=[wt1]}, so you're going to play dumb and try to shift the blame onto me{w=[wt1]}, right?{w=[wt3]}{nw}"

    show wsis_slap_1_wsis 4
    hide wsis_slap_1_wsis_face
    
    wsis "{aw}What!?{/aw}{w=[wt3]} Okay{w=[wt1]}, so you're going to play dumb and try to shift the blame onto me{w=[wt1]}, right?{w=[wt3]}{fast} Fine!{w=[wt3]} Let's play your game{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{nw}"

    show wsis_slap_1_wsis 5
    show wsis_slap_1_wsis_face 3o1
    hide fx_light
    show fx_light
    
    wsis "{aw}What!?{/aw}{w=[wt3]} Okay{w=[wt1]}, so you're going to play dumb and try to shift the blame onto me{w=[wt1]}, right?{w=[wt3]} Fine!{w=[wt3]} Let's play your game{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{fast} Here{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} How do you explain this?{w=[wt3]} Here's the conversation!{w=[wt3]} What now!?"

    show wsis_slap_1_wsis 3
    show wsis_slap_1_wsis_face 3o0
    show wsis_slap_1_hero 5
    show wsis_slap_1_hero_face 5o2
    with dissolve

    call screen fakeboob_messenger(chat="wsis_1", cell_fg="Menu_FG_WSIS", cell_wp="DL_CatsAndStars", cell_xpos=1200) with Dissolve(2)
    
    show wsis_slap_1_wsis_face 3o1
    show wsis_slap_1_hero_face 5o0
    wsis "So{w=[wt2]}, this refreshed your memory?{w=[wt3]} Does this look like you were happy to see me!?{w=[wt3]} Or are you gonna tell me that wasn't you?"

    stop BGM fadeout 6

    show wsis_slap_1_wsis_face 3o0
    show wsis_slap_1_hero_face 5o1
    hero "What?{w=[wt3]} That's weird{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Well{w=[wt2]}, I don't know what to say.{w=[wt3]} I really don't remember that I said that to you like this{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} This is really my account{w=[wt2]}, and I remember to have sent these messages{w=[wt1]}, I guess{w=[wt2]}, but{w=[wt2]}, huh{w=[wt2]}, I'm sure I never would act like that!{w=[wt3]} That doesn't make sense."

    show wsis_slap_1_hero 4
    show wsis_slap_1_hero_face 4o1
    hero "Wait{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I recently downloaded it on my phone{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{nw}"

    show wsis_slap_1_hero 5
    show wsis_slap_1_hero_face 5o3
    hero "Wait{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I recently downloaded it on my phone{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{fast}{w=[wt3]} You can see{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Just a minute{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"

    show wsis_slap_1_hero_face 5o1
    hero "Wait{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I recently downloaded it on my phone{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{fast}{w=[wt3]} You can see{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Just a minute{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{fast} Here!"

    show wsis_slap_1_hero 3
    show wsis_slap_1_hero_face 3o0
    show wsis_slap_1_wsis 5
    with dissolve
    
    play BGM "audio/W2C - Memories.mp3" fadein 15

    call screen fakeboob_messenger(chat="wsis_2") with Dissolve(2)

    stop BGM fadeout 3

    scene bg_1 with Dissolve(3)
    
    play BGM "audio/W2C - Romance.mp3"
    
    $ X_spd = 15
    $ Z_alp = 0.25

    scene bg_1
    show fx_parallax dirt at Parallax
    show wsis_slap_2_wsis
    with Dissolve(3)

    pause

    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}"

    hero "I'm sorry{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I didn't really understand what happened. But I was really happy talking to you again that day. And very sad when I realized I'd lost you twice."

    wsis "{aw}Stop!!!{/aw}{w=[wt3]} I'm so sorry!!!"

    show wsis_slap_2_hero 1 with dissolve

    pause (0.5)

    show wsis_slap_2_hero 2 with dissolve    

    hero "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Can I hug you...?"

    if Check_CharInMap("hero", "home", "living_room"):
        scene wsis_slap_3_bg kitchen
    elif Check_CharInMap("hero", "home", "bedroom_wsis"):
        scene wsis_slap_3_bg bedroom_wsis
    else:
        scene bg_1
        show fx_parallax dirt at Parallax
    show wsis_slap_3_char 1
    show wsis_slap_3_wsis_face 1o0
    show wsis_slap_3_hero_face 1o0
    show fx_light
    with Fade(1, 0, 5, color="#FFF")

    pause

    show wsis_slap_3_hero_face 1o1
    hero "I admit{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I was afraid of seeing you again{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I thought you didn't want to see me.{w=[wt3]} Or even hated me{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} and I never really understood why."

    hero "But{w=[wt2]}, anyway{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} When I saw you again{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Yeah{w=[wt1]}, it wasn't under the best circumstances{w=[wt1]}, right? {gg}He he...{/gg}{w=[wt4]} But{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I couldn't help but feel happy.{w=[wt3]} I'm really happy to be back with you{w=[wt1]}, [C_Nam][hero_to_wsis][C_Off]."
    
    show wsis_slap_3_hero_face 1o0
    show wsis_slap_3_wsis_face 1o1
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}I'm sorry{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I didn't even consider that!{w=[wt3]} I just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I just assumed the worst!"
    
    wsis "{aw}Forgive me!{/aw}{w=[wt3]} Please!{w=[wt3]} Forgive me, [C_Nam][wsis_to_hero][C_Off]!{w=[wt3]} I'm the worst!"

    show wsis_slap_3_wsis_face 1o0 with None

    show wsis_slap_3_char 2
    with dissolve
    
    show wsis_slap_3_hero_face 1o1
    show wsis_slap_3_wsis_face 1o0
    hero "Hey{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} you{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} you called me [C_Nam][wsis_to_hero][C_Off] again."

    show wsis_slap_3_hero_face 1o0
    show wsis_slap_3_wsis_face 1o1
    wsis "'Cause you're my [C_Nam][wsis_to_hero][C_Off]{w=[wt1]}, idiot."
    
    show wsis_slap_3_hero_face 1o1
    show wsis_slap_3_wsis_face 1o0
    hero "So{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'm glad we're okay now.{w=[wt3]} I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} My cheek still hurts{w=[wt1]}, but{w=[wt1]}, well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w} At least we're{w=[wt1]}-{nw}"

    show wsis_slap_3_char 3
    show wsis_slap_3_hero_face 3o0
    show wsis_slap_3_wsis_face 3b0
    with Dissolve(2)

    pause
    
    show wsis_slap_3_char 2
    show wsis_slap_3_hero_face 1o0
    show wsis_slap_3_wsis_face 1o0
    with dissolve

    show wsis_slap_3_wsis_face 1o1
    wsis "{aw}T{w=[wt1]}-To heal faster{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} B{w=[wt1]}-But don't get used to it!{/aw}"

    show wsis_slap_3_hero_face 1o1
    show wsis_slap_3_wsis_face 1o0
    hero "S{w=[wt1]}-Sure{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}"

    show wsis_slap_3_hero_face 1o0
    show wsis_slap_3_wsis_face 1o1
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}[C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {size=-10}I love you{/size}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}"

    show wsis_slap_3_wsis_face 1o0

    menu:
        wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}[C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {size=-10}I love you{/size}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{fast}"

        "Say you love her":
            show wsis_slap_3_char 4
            hide wsis_slap_3_hero_face
            show wsis_slap_3_wsis_face 4o0
            with Dissolve(1)

            $ add_stat("wsis", "love", 2)

            hero "I love you too{w=[wt1]}, [C_Nam][hero_to_wsis][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}"

            show wsis_slap_3_wsis_face 4o1
            wsis "{aw}Hmph...!{w=[wt3]} Y{w=[wt1]}-you really better do{w=[wt2]}, idiot.{/aw}"

            show wsis_slap_3_wsis_face 4o0 with None
            
        "Kiss her":
            show wsis_slap_3_char 5
            show wsis_slap_3_hero_face 5b0
            show wsis_slap_3_wsis_face 5b0
            with Dissolve(1)
            
            $ add_stat("wsis", "lust", 2)

            pause

            play SE1 "Hit1.ogg"

            scene bg_1
            show wsis_slap_4_char 1
            show fx_light
            with vpunch

            show wsis_slap_4_char 2 with dissolve

            scene bg_1
            show wsis_slap_4_wsis
            show wsis_slap_4_hero
            show fx_light
            
            $ wsis_fx = 2
            $ wsis_mood = "A2"
            wsis "{aw}W{w=[wt1]}-what are you doing, pervert!?{/aw}"

        "Just hug her tight":
            show wsis_slap_3_char 4 
            hide wsis_slap_3_hero_face
            show wsis_slap_3_wsis_face 4o0
            with Dissolve(1)

            pause
    
    # Stats update
    $ add_stat("wsis", "love", 2)
    $ add_stat("wsis", "inti", 2)
    $ add_stat("hero", "cha_soc", 2)

    $ wsis_quest_2 = 1  # Mark that confrontation happened
    $ msg.msg(renpy.translate_string("You feel like your relationship with {nm}[fnamewsis]{/nm} has taken a big step forward"))

    scene bg_0 with Dissolve(2)
    
    $ is_specialevent = False

    $ gametimemin += 20
    call gametime from _call_gametime_120
    
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# FAKEBOOB MESSENGER SCREEN
# ----------------------------------------------------------------------------------------------------
screen fakeboob_messenger(chat="wsis_1", cell_fg="Menu_FG", cell_wp=None, cell_xpos=100):
    modal True
    zorder 100
    
    hbox:
        xpos cell_xpos
        frame:
            background None
            xpadding 0
            ypadding 0
            xsize 620
            ysize 1080
            #add Solid("#000000aa")
            if cell_wp==None:
                add AlphaMask(
                    Fixed(
                        Transform(Cell_Img(cellbg[a_menu_3]),
                            zoom = Cell_WZoom(cellbg[a_menu_3], cellwz),
                            xalign = (cellwx/100),
                            yalign = (cellwy/100)),
                            xysize=(620, 1080) # Size of the masked area
                    ),
                    "images/UI/CellphoneBG/Menu_Mask_2.webp"
                )
            else:
                add AlphaMask(
                    Fixed(
                        Transform("images/UI/CellphoneBG/"+str(cell_wp)+".webp",
                            zoom = 0.9 + (cellwz/25),
                            xalign = 0.5,
                            yalign = 0.5),
                            xysize=(620, 1080) # Size of the masked area
                    ),
                    "images/UI/CellphoneBG/Menu_Mask_2.webp"
                )

            use fakeboob_messenger_screen(chat)

            add "images/UI/CellphoneBG/Menu_MG_3.webp"
            add "images/UI/CellphoneBG/" + cell_fg + ".webp"
            
            hbox:
                xalign 0.5
                yalign 0.9
                spacing 50
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                    action None
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                    action None
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                    action None

# ----------------------------------------------------------------------------------------------------
# CHAT LOG DATA
# ----------------------------------------------------------------------------------------------------

init python:
    def get_fakeboob_chat(chat_id):
        """Returns chat log data based on chat_id"""
        
        # ----------------------------------------------------------------------------------------------------
        # WSIS POINT OF VIEW - She sees HERO's failed messages on left, her messages on right
        # ----------------------------------------------------------------------------------------------------
        if chat_id == "wsis_1":
            return {
                "viewer": fnamewsis,
                "other_user": fnamehero,
                "messages": [
                    {"type": "date", "text": "Winter 7, 4 years ago"},
                    
                    {"type": "msg", "side": "right", "delivered": True, "sender": fnamewsis,
                     "text": "[wsis_to_hero]! *^* I finally found you, idiot!"},
                    
                    {"type": "msg", "side": "left", "delivered": True, "sender": fnamehero,
                     "text": "hey [fnamewsis!l]"},
                    
                    {"type": "msg", "side": "right", "delivered": True, "sender": fnamewsis,
                     "text": "How are you doing? I missed you :c"},

                    {"type": "msg", "side": "left", "delivered": True, "sender": fnamehero,
                     "text": "fine"},
                    
                    {"type": "msg", "side": "right", "delivered": True, "sender": fnamewsis,
                     "text": "So cold"},
                    {"type": "msg", "side": "right", "delivered": True,
                     "text": "Hey :/"},
                    {"type": "msg", "side": "right", "delivered": True,
                     "text": "Why are you acting like this?"},
                    
                    {"type": "date", "text": "Winter 8, 4 years ago"},
                    
                    {"type": "msg", "side": "right", "delivered": True, "sender": fnamewsis,
                     "text": "Are you upset with me?"},
                    {"type": "msg", "side": "right", "delivered": True,
                     "text": "Sorry for saying you're an idiot. It was not in a bad way :c"},
                    
                    {"type": "date", "text": "Winter 9, 4 years ago"},
                    
                    {"type": "msg", "side": "right", "delivered": True, "sender": fnamewsis,
                     "text": "Hey, [wsis_to_hero]..."},
                    {"type": "msg", "side": "right", "delivered": True,
                     "text": "I wanna see you again"},
                    {"type": "msg", "side": "right", "delivered": True,
                     "text": "I wish you would come here :c"},
                    
                    {"type": "date", "text": "Winter 21, 4 years ago"},

                    {"type": "msg", "side": "left", "delivered": True, "sender": fnamehero,
                     "text": "itd be really fool, dont you think? hahaha"},
                    {"type": "msg", "side": "left", "delivered": True,
                     "text": "of course i would hate doing it!"},
                    {"type": "msg", "side": "left", "delivered": True,
                     "text": "good bye!"},
                    
                    {"type": "msg", "side": "right", "delivered": True, "sender": fnamewsis,
                     "text": "So that's it? Fine then!"},
                ]
            }
        
        # ----------------------------------------------------------------------------------------------------
        # HERO POINT OF VIEW - He sees WSIS's messages on left, his failed messages on right
        # ----------------------------------------------------------------------------------------------------
        elif chat_id == "wsis_2":
            return {
                "viewer": fnamehero,
                "other_user": fnamewsis,
                "messages": [
                    {"type": "date", "text": "Winter 7, 4 years ago"},
                    
                    {"type": "msg", "side": "left", "delivered": True, "sender": fnamewsis,
                     "text": "[wsis_to_hero]! *^* I finally found you, idiot!"},
                    
                    {"type": "msg", "side": "right", "delivered": True, "sender": fnamehero,
                     "text": "hey [fnamewsis!l]"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "[hero_to_wsis!l]"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "its nice to talk to you again!"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "how are you doing?"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "how is [hero_about_wmom!l]?"},
                    
                    {"type": "msg", "side": "left", "delivered": True, "sender": fnamewsis,
                     "text": "How are you doing? I missed you :c"},
                    
                    {"type": "msg", "side": "right", "delivered": False, "sender": fnamehero,
                     "text": "i missed you too"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "thats why i created this account here in the lan-house"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "but still dont understand this internet thing"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "im glad it worked hahaha"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "i and dad are fimr"},
                    {"type": "msg", "side": "right", "delivered": True,
                     "text": "fine"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "theres no day we dont remember and talk about you"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "i promisse ill visit you again when i save enough money!"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "why don't you come to visit us?"},
                    
                    {"type": "msg", "side": "left", "delivered": True, "sender": fnamewsis,
                     "text": "so cold"},
                    
                    {"type": "msg", "side": "right", "delivered": False, "sender": fnamehero,
                     "text": "hahaha... of course its not! if it gets cold, your [wsis_to_hero!l] warms you with his embrace"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "hey, [hero_to_wsis!l]. my time in the lan-house is finishing. things got a little hard here on countryside but i promisse you that when i get money again ill come back again to talk to you, ok? missed you, [hero_to_wmom!l], and [fnamewnei!l]. let me know how you are doing next time. love you!!!!!!111"},
                    
                    {"type": "msg", "side": "left", "delivered": True, "sender": fnamewsis,
                     "text": "Hey :/"},
                    {"type": "msg", "side": "left", "delivered": True,
                     "text": "Why are you acting like this?"},
                    
                    {"type": "date", "text": "Winter 8, 4 years ago"},
                    
                    {"type": "msg", "side": "left", "delivered": True, "sender": fnamewsis,
                     "text": "Are you upset with me?"},
                    {"type": "msg", "side": "left", "delivered": True,
                     "text": "Sorry for saying you're an idiot. It was not in a bad way :c"},
                    
                    {"type": "date", "text": "Winter 9, 4 years ago"},
                    
                    {"type": "msg", "side": "left", "delivered": True, "sender": fnamewsis,
                     "text": "Hey, [wsis_to_hero]..."},
                    {"type": "msg", "side": "left", "delivered": True,
                     "text": "I wanna see you again"},
                    {"type": "msg", "side": "left", "delivered": True,
                     "text": "I wish you would come here :c"},
                    
                    {"type": "date", "text": "Winter 21, 4 years ago"},
                    
                    {"type": "msg", "side": "right", "delivered": False, "sender": fnamehero,
                     "text": "hi, [hero_to_wsis!l]! sorry for taking so long to showing up. of course im not upset with you. i was just saving a little money to get here again and talk to you."},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "seeing you again is what i want most! maybe itd better to save more money to expend a time with you in the city than paying this thing here"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "you know, it took almost 1 hour for this chat to load!"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "the guy here said the internet signal still dont work well here"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "and that people usually just come to play a shooting game"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "obviously id never waste the chance i have to talk to you and play a game instead, right?"},
                    {"type": "msg", "side": "right", "delivered": True,
                     "text": "itd be really fool, dont you think? hahaha"},
                    {"type": "msg", "side": "right", "delivered": True,
                     "text": "of course i would hate doing it!"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "love you, [hero_to_wsis!l]!"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "im dying to see you again. i probably won't appear here for a while, okay? so i save money to visit and spend a few days with you. i'd love to see how you are now. the photo thing does not load here but im sure you are even more cute!"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "i wish you, [hero_about_wmom!l], and [fnamewnei!l] a merry christmas!"},
                    {"type": "msg", "side": "right", "delivered": True,
                     "text": "good bye!"},
                    
                    {"type": "msg", "side": "left", "delivered": True, "sender": fnamewsis,
                     "text": "So that's it? Fine then!"},
                    
                    {"type": "date", "text": "Summer 15, 3 years ago"},
                    
                    {"type": "msg", "side": "right", "delivered": False, "sender": fnamehero,
                     "text": "hey, [hero_to_wsis!l]! just came here to say that some things have happened in the winter and i needed to spend what i got. but please dont worry. your [wsis_to_hero!l] won't give up!"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "tell me how you're doing please! love you so much!"},
                    
                    {"type": "date", "text": "Winter 28, 3 years ago"},
                    
                    {"type": "msg", "side": "right", "delivered": False, "sender": fnamehero,
                     "text": "sorry if i worried you, [hero_to_wsis!l]. i need to tell the truth. dad got a disease and the treatment is proving very costly, both financially and in terms of lifestyle. i need to take care of him for a while, so i wont be able to keep my promise to visit you anytime soon. so please be patient, things will certainly get better and ill be able to give you a hug! i miss you so much... i hope you had a wonderful christmas, and that next year will be very good for all of you."},
                    
                    {"type": "date", "text": "Fall 14, 2 years ago"},
                    
                    {"type": "msg", "side": "right", "delivered": False, "sender": fnamehero,
                     "text": "[hero_to_wsis!l]. we found out that dad's illness is incurable. so, i'll need to spend some time with him. but don't worry. everything will be okay."},
                    
                    {"type": "date", "text": "Winter 2, 2 years ago"},
                    
                    {"type": "msg", "side": "right", "delivered": False, "sender": fnamehero,
                     "text": "why you don't answer me anymore?"},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "sorry, i'm sure it's something I must be doing wrong here, hahaha..."},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "im not reading your messages, but just wanna tell you everything will be okay."},
                    
                    {"type": "date", "text": "Spring 4, 1 year ago"},
                    
                    {"type": "msg", "side": "right", "delivered": False, "sender": fnamehero,
                     "text": "hey, [hero_to_wsis!l]. i told dad that i was talking to you. he asked me to tell you he missed you so much and is sorry for not saying goodbye."},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "he got a little worse, and i ended up needing to stay close to him every time."},
                    {"type": "msg", "side": "right", "delivered": False,
                     "text": "i don't know if you're upset with me or i'm doing something wrong with this computer thing. i dont know if ill have time to come here again. just came to tell you i love you so much and will do my best to see you again when i can. best wishes, by your dear [wsis_to_hero!l]!"},
                ]
            }
        
        # Default fallback
        else:
            return {
                "viewer": "Unknown",
                "other_user": "Unknown",
                "messages": [
                    {"type": "date", "text": "No chat data available"}
                ]
            }

screen fakeboob_messenger_screen(chat="", status="offline"):
    
    # Get chat data
    $ chat_data = get_fakeboob_chat(chat)
    
    # Main messenger window
    frame:
        xalign 0.500
        yalign 0.325
        xsize 540
        ysize 825
        background "#FFFFFFAA"
        padding (5, 5, 5, 5)
        
        vbox:
            spacing 0
            
            # ----------------------------------------------------------------------------------------------------
            # HEADER
            # ----------------------------------------------------------------------------------------------------
            frame:
                xfill True
                ysize 140
                background "#0064C8"
                padding (25, 25)
                    
                vbox:
                    spacing 2
                    xalign 0.5
                    yalign 0.5
                    
                    text renpy.translate_string("{b}FakeBooB Messenger{/b}") size 40 xalign 0.5
                
                    hbox:
                        spacing 30
                        xalign 0.5
                        yalign 0.5
                        text renpy.translate_string("{b}[chat_data['other_user']]{/b}") color "#000000"
                        if status == "offline":
                            text renpy.translate_string("{b}● Offline{/b}") color "#969696"
                        else:
                            text renpy.translate_string("{b}● Online{/b}") color "#009600"
            
            # ----------------------------------------------------------------------------------------------------
            # SCROLLABLE CHAT AREA
            # ----------------------------------------------------------------------------------------------------
            frame:
                xfill True
                yfill True
                background None
                padding (0, 0, 0, 0)
                
                viewport:
                    id "fakeboob_viewport"
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    yinitial 0.0
                    
                    vbox:
                        spacing 0
                        xfill True
                        
                        # Add some top padding
                        null height 20
                        
                        # ----------------------------------------------------------------------------------------------------
                        # RENDER MESSAGES DYNAMICALLY
                        # ----------------------------------------------------------------------------------------------------
                        for msg in chat_data["messages"]:
                            if msg["type"] == "date":
                                use FakeMes(message=msg["text"], side="system")
                            
                            elif msg["type"] == "msg":
                                if "sender" in msg:
                                    use FakeMes(
                                        message=msg["text"],
                                        side=msg["side"],
                                        delivered=msg["delivered"],
                                        sender=msg["sender"]
                                    )
                                else:
                                    use FakeMes(
                                        message=msg["text"],
                                        side=msg["side"],
                                        delivered=msg["delivered"]
                                    )
                        
                        # Add some bottom padding
                        null height 20
                        
                        # FOOTER
                        frame:
                            xfill True
                            ysize 70
                            background "#f8f8f8"
                            padding (20, 15)
                            
                            hbox:
                                spacing 20
                                xalign 0.5
                                yalign 0.5
                                
                                textbutton renpy.translate_string("Close"):
                                    style "fakeboob_close_button"
                                    action Return()

# ----------------------------------------------------------------------------------------------------
# MESSAGE COMPONENTS
# ----------------------------------------------------------------------------------------------------

screen FakeMes(message="", side="system", delivered=True, sender=""):
    if sender != "":
        frame:
            background None
            xsize 512
            xpadding 0
            if side == "left":
                text renpy.translate_string("{b}[sender]{/b}") color "#191919" xalign 0.0
            elif side == "right":
                text renpy.translate_string("{b}[sender]{/b}") color "#191919" xalign 1.0

    if side == "system":
        frame:
            xalign 0.5
            background None
            padding (15, 8)
            xmaximum 600
            text message:
                style "fakeboob_system_text"
                xalign 0.5

    elif side == "left":
        frame:
            background "#FFFFFFAA"
            padding (10, 0)
            xsize 450
            hbox:
                spacing 15
                if delivered:
                    text "✔" color "#00FF00" size 40 yalign 0.0
                text message color "#323232" size 40

    elif side == "right":
        if delivered == True:
            frame:
                background "#96FF96AA"
                padding (80, 0, 0, 0)
                xsize 450
                xalign 1.0
                hbox:
                    spacing 15
                    xalign 1.0
                    text message color "#009600" size 40 text_align 1.0
                    if delivered:
                        text "✔" color "#00FF00" size 40 yalign 0.0

        else:
            frame:
                background "#FF9696AA"
                padding (80, 0, 0, 0)
                xsize 450
                xalign 1.0
                hbox:
                    spacing 15
                    xalign 1.0
                    text message color "#960000" size 40 text_align 1.0
                    text "🕐" color "#FF0000" size 40 yalign 0.0

    null height 5

# ----------------------------------------------------------------------------------------------------
# STYLES
# ----------------------------------------------------------------------------------------------------

style fakeboob_back_button:
    background "#ffffff33"
    hover_background "#ffffff55"
    padding (15, 10)
    
style fakeboob_back_button_text:
    color "#ffffff"
    size 30
    font "DejaVuSans.ttf"
    bold True

style fakeboob_username:
    size 30
    font "DejaVuSans.ttf"
    bold True

style fakeboob_message_text:
    size 40
    font "DejaVuSans.ttf"
    line_spacing 2

style fakeboob_system_text:
    color "#555555"
    size 30
    font "DejaVuSans.ttf"
    italic True
    text_align 0.5

style fakeboob_close_button:
    background "#3b5998"
    hover_background "#2d4373"
    padding (30, 12)

style fakeboob_close_button_text:
    color "#ffffff"
    size 30
    font "DejaVuSans.ttf"
    bold True

style fakeboob_footer_text:
    color "#666666"
    size 30
    font "DejaVuSans.ttf"
    italic True
