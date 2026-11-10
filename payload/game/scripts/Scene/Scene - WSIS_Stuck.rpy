# ---------------------------------------------------------------------------
label wsis_scene_stuck: # Step-Bro, Help!
# ---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_202

    stop BGM fadeout 1

    # --------------------------------------------------
    # 1. HERO finds WSIS stuck in the washing machine
    # --------------------------------------------------
    scene action_laundry_stuck_1_bg home_kitchen
    show action_laundry_stuck_1_wsis_body
    if wsis_wear != None:
        show action_laundry_stuck_1_wsis_wear towel
    show fx_light
    with fade

    $ msg.msg(renpy.translate_string("You find [C_Nam][fnamewsis][C_Off] in a very... peculiar situation."))
    mind "(Is [C_Nam][hero_about_wsis][C_Off]'s head stuck inside the washing machine!?)"

    menu:
        "Help her":
            pass

        "Just return":
            play BGM "audio/W2C - GoodVibes.mp3"
            jump show_ui

    # The scene is committed — it can only play once per day from here.
    $ wsis_stuck_done = True

    play BGM "audio/W2C - Adrenaline.mp3"

    hero "Uh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} [C_Nam][hero_to_wsis][C_Off]?{w=[wt2]} Are you okay down there?"
    wsis "{aw}Ugh...!{w=[wt2]} You...!{/aw}{w=[wt2]}, {bt}sure...!{/bt}{w=[wt3]} I just decided to live as a worm and put myself inside a hole{w=[wt3]} Could I be any better than this?{w=[wt2]} I'm more than okay!"
    hero "Oh{w=[wt2]}, I see.{w=[wt3]} Have a good day then!"
    wsis "{aw}No!{w=[wt2]} Don't leave me like this!!!{/aw}"
    hero "But you just said..."
    wsis "Please, [C_Nam][wsis_to_hero][C_Off]{w=[wt2]}, help!{w=[wt3]} {aw}I'm stuck in the washing machine!{/aw}"
    hero "How did you even{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} You know what{w=[wt2]}, never mind."
    wsis "{aw}Ugh...!{/aw} I was trying to get my clothes from this shit and can't get back!{w=[wt3]} Just{w=[wt1]} get me OUT of here!"
    hero "Alright{w=[wt2]}, alright.{w=[wt2]} Hold still."

    # --------------------------------------------------
    # 2. HERO helps her — three escalating Thug of War pulls
    # --------------------------------------------------
    $ a_event_1 = round((perk_phy_str + 1) * (1 + stat_phy * 0.01), 2)
    $ a_event_0 = 1 # current pull level (1 -> 2 -> 3)

    label wsis_scene_stuck_pull:

        scene action_laundry_stuck_2_bg home_kitchen
        if a_event_0 == 1:
            show action_laundry_stuck_2_char_body 1
            show action_laundry_stuck_2_wsis_wear 1_towel
            show action_laundry_stuck_2_hero_wear 1_home
        elif a_event_0 == 2:
            show action_laundry_stuck_2_char_body 2
            show action_laundry_stuck_2_wsis_wear 2_towel
            show action_laundry_stuck_2_hero_wear 2_home
        else:
            show action_laundry_stuck_2_char_body 3
            show action_laundry_stuck_2_wsis_wear 3_towel
            show action_laundry_stuck_2_hero_wear 3_home
        show fx_light
        with dissolve

        if a_event_0 == 1:
            hero "On three! One{w=[wt1]}, two{w=[wt1]}, {b}THREE!{/b}"
        elif a_event_0 == 2:
            wsis "{aw}It moved! Keep going, don't you dare stop!{/aw}"
        else:
            hero "Almost there! One{w=[wt1]} more{w=[wt1]} {b}PULL!{/b}"

        # Opponent grip gets stronger every pull.
        call screen minigame_thugofwar(var_pla=a_event_1, var_npc=(1 + a_event_0))

        if _return == "Win":
            play SE1 "JingleRight.ogg"
            $ add_stat("hero", "phy_str", 3)
            if a_event_0 < 3:
                $ a_event_0 += 1
                jump wsis_scene_stuck_pull
            # else: 3rd pull won -> fall through to the payoff

        else:
            # Failed a pull — HERO loses his grip, she stays stuck for today.
            play SE1 "JingleWrong.ogg"
            scene action_laundry_stuck_1_bg home_kitchen
            show action_laundry_stuck_1_wsis_body
            if wsis_wear != None:
                show action_laundry_stuck_1_wsis_wear towel
            show fx_light
            with dissolve

            hero "{aw}Agh!{w=[wt1]} my grip slipped!{/aw}"
            wsis "{aw}You WEAKLING! Now my neck hurts even more!{/aw}"
            $ add_stat("wsis", "inti", 0.5)
            $ gametimemin += 10
            call gametime from _call_gametime_126
            play BGM "audio/W2C - GoodVibes.mp3"
            jump show_ui

    # --------------------------------------------------
    # 3. Third pull won — she pops free
    # --------------------------------------------------
    $ renpy.pause(1, hard=True)
    play SE1 "Slip.ogg"

    scene action_laundry_stuck_3_bg home_kitchen
    show action_laundry_stuck_3_char_body
    show action_laundry_stuck_3_wsis_face s0
    show action_laundry_stuck_3_hero_face s0
    show fx_light
    with hpunch

    play BGM "audio/W2C - GoodVibes.mp3"

    pause

    $ wsis_fx = 2
    $ hero_fx = 2
    $ wsis_mood = "O1"
    $ hero_mood = "A2"

    scene bg_home diningroom
    show HERO at LC
    show WSIS at RC
    with fade

    wsis "{cps=20}Haaah...{/cps}{w=[wt2]} I'm{w=[wt1]} free..."
    hero "Told you I'd get you out.{w=[wt2]} You alright?"
    wsis "...{w=[wt2]} Yeah.{w=[wt2]} T{w=[wt1]}-thanks, [C_Nam][wsis_to_hero][C_Off]."
    hero "Maybe next time leave the laundry to me, hm?"

    $ wsis_mood = "O2"
    wsis "{aw}Shut up!{/aw}{w=[wt4]} But{w=[wt2]}, fine.{w=[wt3]} Whatever."

    $ add_stat("wsis", "inti", 3)
    $ add_stat("wsis", "love", 2)
    $ add_stat("wsis", "lust", 3)
    $ gametimemin += 15
    call gametime from _call_gametime_127

    jump show_ui
