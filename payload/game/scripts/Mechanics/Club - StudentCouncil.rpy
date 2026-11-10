# ----------------------------------------------------------------------------------------------------
label club_studentcouncil:
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_119
    scene studentcouncil_bg
    show studentcouncil_wsco_body
    show studentcouncil_wsco_face 0
    show studentcouncil_wkuu_body
    show studentcouncil_wkuu_face 0
    show studentcouncil_wkuu_eye d
    with fade

    # ----------------------------------------------------------------------------------------------------
    # Intro
    # ----------------------------------------------------------------------------------------------------
    stop BGM fadeout 3
    show studentcouncil_wkuu_eye u
    show studentcouncil_wsco_face 1
    wrin "Hello {nm}[fnamehero]{/nm}{w=[wt2]}, in what the Student Council can help you?"
    # ----------------------------------------------------------------------------------------------------


    show studentcouncil_wsco_face 0

    label club_studentcouncil_start:

        show studentcouncil_wkuu_eye u
        menu:
            "⭐ Quests" if Club_IsMember("hero", "stco"):
                call club_studentcouncil_quest from _call_club_studentcouncil_quest

            "💰 Request funding" if Club_IsMember("hero", "stco") and Get_ClubRep("stco", "hero") >= CLUB_FUNDING_REP_REQ and club_stco_money >= CLUB_FUNDING_AMOUNT:
                call club_studentcouncil_funding from _call_club_studentcouncil_funding

            "Ask about the club":
                if "club_stco_about" not in wrin_know:
                    hero "I'd like to know more about the Student Council."
                    $ wrin_know.append("club_stco_about")
                else:
                    hero "Could you explain me again about the Student Council?"

                show studentcouncil_wkuu_eye d
                show studentcouncil_wsco_face 1
                wrin "Sure.{w=[wt2]} We were given the job of managing more trivial matters of the school.{w=[wt3]} We help students who need help and keep an eye on the most problematic ones."
                wrin "In the first case{w=[wt1]}, we do our best to help those who request help with any problem related to school or that is hindering their school performance.{w=[wt3]} If you want help with anything{w=[wt1]}, consider counting on us."
                wrin "We also opened some requests to people outside the council, so that more people can support. If you have teaching skills{w=[wt1]}, you can give tutoring classes.{w=[wt2]} Just request here.{w=[wt2]} We should observe your performance{w=[wt1]}, then dedicate a portion of the club's budget to make a token payment to you according to your class performance."
                wrin "In the second case{w=[wt1]}, we let students who may cause problems under surveillance{w=[wt2]}; we give warnings to those who cause small problems{w=[wt2]}; in case of more serious violations{w=[wt1]}, we can give suspension or even expulsion from the school.{w=[wt2]} If you have a complaint about someone{w=[wt1]}, especially with evidence{w=[wt1]}, report it here.{w=[wt2]} If not{w=[wt1]}, stay out of trouble."

                show studentcouncil_wsco_face 0
                mind "(I see{w=[wt1]}, you guys perform the duties of the principal while she plays Solitaire on the computer.)"
                jump club_studentcouncil_start

            "Ask to leave the club" if Club_IsMember("hero", "stco"):
                hero "I'd like to leave the Student Council."

                show studentcouncil_wkuu_eye d
                show studentcouncil_wsco_face 1
                wrin "It's a shame.{w=[wt3]} But we'll respect your choices."

                $ msg.msg(renpy.translate_string("You left a club: [C_Dat]Student Council[C_Off]"))
                $ Club_Leave("hero", "stco")
                $ club_stco_hero_rep = 0

                jump club_studentcouncil_start

            "Ask to join the club" if not Club_IsMember("hero", "stco"):
                hero "I'd like to join the Student Council."

                show studentcouncil_wkuu_eye d
                show studentcouncil_wsco_face 1
                wrin "Good{w=[wt2]}, we still have a spot for you.{w=[wt2]} Your class does not yet have a vice president, so you will fill that position.{w=[wt3]} Just fill out this document."

                show studentcouncil_wsco_face 0

                $ a_event_1 = "{b}Club Register:{/b} Student Council{pr}"
                wrin "[C_Pos]Bonus:[C_Off] your academic choices carry more weight, and you earn more money by doing Student Council activities.{pr}[C_Neg]Onus:[C_Off] reduces the gain of intimacy, love, and lust of students outside the Student Council.{fast}"
                menu:
                    wrin "[C_Pos]Bonus:[C_Off] your academic choices carry more weight, and you earn more money by doing Student Council activities.{pr}[C_Neg]Onus:[C_Off] reduces the gain of intimacy, love, and lust of students outside the Student Council.{fast}"
                    "Accept":
                        $ Club_Join("hero", "stco")
                        $ msg.msg(renpy.translate_string("You joined a club: [C_Dat]Student Council[C_Off]"))
                        hero "Done."

                        show studentcouncil_wsco_face 1
                        wrin "Welcome, {nm}[fnamehero] [lnamehero]{/nm}.{w=[wt2]} You'll be of great help."

                        show studentcouncil_wsco_face 0
                    "Deny":
                        hero "Sorry.{w=[wt2]} I changed my mind."

                jump club_studentcouncil_start

            "Report someone" if 0 > 1:
                menu:
                    "Return":
                        jump club_studentcouncil_start

            "Apply for tutoring lessons" if perk_skl_tut >= 1:
                hero "I'm here to apply as a study monitor for today."

                show studentcouncil_wkuu_eye d
                show studentcouncil_wsco_face 1
                wrin "Sure{w=[wt1]}, you have been performing well during class.{w=[wt2]} It will be of great help."

                show studentcouncil_wsco_face 0
                $ group_tutor = "study"

            "Apply for swimming lessons" if perk_skl_tut >= 1 and  perk_skl_swm >= 1:
                hero "I'm here to apply as a swimming monitor for today."

                show studentcouncil_wkuu_eye d
                show studentcouncil_wsco_face 1
                wrin "Sure{w=[wt1]}, you have been performing well during swimming class.{w=[wt2]} It will be of great help."

                show studentcouncil_wsco_face 0
                $ group_tutor = "swimming"

            "Return":
                hero "Sorry.{w=[wt2]} Nevermind."
                jump show_ui

    show studentcouncil_wkuu_eye u
    show studentcouncil_wkuu_face 1
    wkuu "Preference?"

    show studentcouncil_wkuu_face 0
    if group_tutor == "study":
        menu:
            "{image=icon_wnei} {nm}[fnamewnei] [lnamewnei]{/nm}":
                $ a_event_0 = "wnei"
            "{image=icon_wdis} {nm}[fnamewdis] [lnamewdis]{/nm}" if wdis_quest_1 >= 1:
                $ a_event_0 = "wdis"
            "{image=icon_wgal} {nm}[fnamewgal] [lnamewgal]{/nm}" if wgal_quest_1 >= 1:
                $ a_event_0 = "wgal"
            "Random":
                $ a_event_0 = []
                $ a_event_0.append("wnei")
                if wdis_quest_1 >= 1:
                    $ a_event_0.append("wdis")
                if wgal_quest_1 >= 1:
                    $ a_event_0.append("wgal")
                $ a_event_0 = renpy.random.choice(a_event_0)

    elif group_tutor == "swimming":
        menu:
            "{image=icon_wsis} {nm}[fnamewsis] [lnamestep]{/nm}":
                $ a_event_0 = "wsis"
            "{image=icon_wota} {nm}[fnamewota] [lnamewota]{/nm}" if wota_quest_1 >= 1:
                $ a_event_0 = "wota"
            "Random":
                $ a_event_0 = []
                $ a_event_0.append("wsis")
                if wota_quest_1 >= 1:
                    $ a_event_0.append("wota")  
                $ a_event_0 = renpy.random.choice(a_event_0)
    scene bg_0
    with dissolve

    # ----------------------------------------------------------------------------------------------------
    if group_tutor == "study":
    # ----------------------------------------------------------------------------------------------------
        $ hero_wear = "school"
        $ hero_map = "School - Library"

        scene socializing_class_bg library

        if a_event_0 == "wdis":
            menu:
                "Play minigame":
                    jump action_tutoring_start
                "Run simple stat gaining":
                    show socializing_class_wdis

        if a_event_0 == "wgal":
            show socializing_class_wgal

        if a_event_0 == "wnei":
            show socializing_class_wnei

        show socializing_class_hero teaching
        show socializing_class_fg library
        with Dissolve(2)

        $ check_stat()
        $ a_event_1 = (gametimehour * 60) + gametimemin
        $ a_event_2 = (1 + int(Club_IsMember("hero", "stco"))) * (perk_skl_tut*2) * (1.0 + (perk_int_mem * (0.5 + (stat_int*0.005)))) * (1.0 + (perk_cha_per * (0.25 + (stat_cha*0.0025)))) * (0.75 + (personality[3]/100))
        $ a_event_3 = round(a_event_1/120 * (a_event_2/2), 2) # Money
        $ a_event_4 = round(2 + (a_event_2 * 0.1), 2) # Love
        $ a_event_5 = round(((1080 - a_event_1) / 100), 2) # Intimacy
        $ gametimemin += 1080 - a_event_1

        if a_event_0 == "wnei":

            $ money += a_event_3
            $ msg.msg(renpy.translate_string("money [C_Pos]+$[a_event_3][C_Off]"))
            $ add_stat("wnei", "love", round(a_event_4, 2))
            $ add_stat("hero", "cha_soc", round(a_event_4, 2))
            $ add_stat("wnei", "inti", round(a_event_5, 2))

        elif a_event_0 == "wgal":

            $ money += a_event_3
            $ msg.msg(renpy.translate_string("money [C_Pos]+$[a_event_3][C_Off]"))
            $ add_stat("wgal", "love", round(a_event_4, 2))
            $ add_stat("hero", "cha_soc", round(a_event_4, 2))
            $ add_stat("wgal", "inti", round(a_event_5, 2))

        elif a_event_0 == "wdis":

            $ money += a_event_3
            $ msg.msg(renpy.translate_string("money [C_Pos]+$[a_event_3][C_Off]"))
            $ add_stat("wdis", "love", round(a_event_4, 2))
            $ add_stat("hero", "cha_soc", round(a_event_4, 2))
            $ add_stat("wdis", "inti", round(a_event_5, 2))

        pause

        jump show_ui

    # ----------------------------------------------------------------------------------------------------
    elif group_tutor == "swimming":
    # ----------------------------------------------------------------------------------------------------

        scene action_tutor_swim_bg pool

        if a_event_0 == "wsis":
            show action_tutor_swim_wsis_bg

        show action_tutor_swim_hero

        if a_event_0 == "wota":
            show action_tutor_swim_wota

        if a_event_0 == "wsis":
            show action_tutor_swim_wsis_fg

        with Dissolve(2)

        $ check_stat()
        $ hero_wear = "school"
        $ hero_map = "School - Swimming Pool"
        $ a_event_1 = (gametimehour * 60) + gametimemin
        $ a_event_2 = (1 + int(Club_IsMember("hero", "stco"))) * (perk_skl_tut*2) * (1.0 + (perk_skl_swm * (0.5 + (stat_phy*0.005)))) * (1.0 + (perk_cha_per * (0.25 + (stat_cha*0.0025)))) * (0.75 + (personality[3]/100))
        $ a_event_3 = round(a_event_1/120 * (a_event_2/2), 2) # Money
        $ a_event_4 = round(2 + (a_event_2 * 0.1), 2) # Love
        $ a_event_5 = round(((1080 - a_event_1) / 100), 2) # Intimacy
        $ gametimemin += 1080 - a_event_1

        if a_event_0 == "wsis":

            $ wsis_know.append("HangOut_Swim_Day")

            $ money += a_event_3
            $ msg.msg(renpy.translate_string("money [C_Pos]+$[a_event_3][C_Off]"))
            $ add_stat("wsis", "love", round(a_event_2, 2))
            $ add_stat("hero", "cha_soc", round(a_event_2, 2))

            if perk_cha_sex >= 1:
                $ add_stat("wsis", "lust", round(a_event_4, 2))

            $ add_stat("wsis", "inti", round(a_event_5, 2))

        elif a_event_0 == "wota":

            #$ wota_know.append("HangOut_Swim")

            $ money += a_event_3
            $ msg.msg(renpy.translate_string("money [C_Pos]+$[a_event_3][C_Off]"))
            $ add_stat("wota", "love", round(a_event_2, 2))
            $ add_stat("hero", "cha_soc", round(a_event_2, 2))

            if perk_cha_sex >= 1:
                $ add_stat("wota", "lust", round(a_event_4, 2))

            $ add_stat("wota", "inti", round(a_event_5, 2))

        pause
        call gametime from _call_gametime_77
        call hide_ui from _call_hide_ui_120
        hide screen fx_morning
        hide screen fx_afternoon
        hide screen fx_night
        $ stat_hyg = 100
        $ hero_needs[0] = True
        $ msg.msg(renpy.translate_string("You are clean."))

        jump show_ui

# ----------------------------------------------------------------------------------------------------
label club_studentcouncil_funding: # Draw from the SC treasury (rep-gated; first-pass SC-only)
# ----------------------------------------------------------------------------------------------------
    hero "The Council could spare some funds for what I'm working on, right?"

    show studentcouncil_wkuu_eye d
    show studentcouncil_wsco_face 1
    wrin "Given how much you've done for us{w=[wt1]}, that's fair.{w=[wt2]} I'll release [C_Itm][CLUB_FUNDING_AMOUNT][C_Off] from the budget."

    show studentcouncil_wsco_face 0
    $ Add_ClubMoney("stco", -CLUB_FUNDING_AMOUNT)
    $ add_stat("hero", "money", CLUB_FUNDING_AMOUNT, False)
    $ msg.msg(renpy.translate_string("[C_Dat]Student Council[C_Off] funded you: [C_Pos]+") + renpy.translate_string(str(str(CLUB_FUNDING_AMOUNT))) + renpy.translate_string("[C_Off] (treasury now ") + renpy.translate_string(str(str(club_stco_money))) + ")")
    jump club_studentcouncil_start

# ----------------------------------------------------------------------------------------------------
label club_studentcouncil_quest: # Student Council Quests
# ----------------------------------------------------------------------------------------------------
    #call hide_ui

    hero "Is there something I can help?"

    show studentcouncil_wkuu_eye d
    show studentcouncil_wsco_face 1

    # club_stco_quest_1 — shower quest: 0 none/offer · 1 active (find+fix) · 2 fixed (report) · 3 reported today
    if club_stco_quest_1 == 1:
        # Task already handed out and not yet resolved — don't double-assign it.
        wrin "You've still got that [C_Dat]girls' locker room[C_Off] shower to fix{w=[wt1]}, remember?{w=[wt2]} Go on{w=[wt1]}, before it floods the hallway."

        show studentcouncil_wsco_face 0
        mind "(Right{w=[wt1]}, better get that done before someone wonders why I keep loitering near it.)"
        jump club_studentcouncil_start

    if club_stco_quest_1 == 2:
        # Shower fixed — HERO reports it back to the Council.
        hero "That broken shower in the [C_Dat]girls' locker room[C_Off]?{w=[wt2]} Fixed.{w=[wt2]} It was a cracked joint{w=[wt1]}, I tightened it up{w=[wt1]}, no more leak."

        show studentcouncil_wkuu_eye u
        show studentcouncil_wsco_face 1
        wrin "Already?{w=[wt2]} That was fast.{w=[wt3]} Thank you{w=[wt1]}, {nm}[fnamehero]{/nm}{w=[wt1]}, that's a real help to the Council."

        show studentcouncil_wsco_face 0
        # Reward lands through the new club-rep path; the Council covers the parts from its treasury.
        $ add_stat("hero", "club_stco", CLUB_SHOWER_REP)
        $ Add_ClubMoney("stco", -CLUB_SHOWER_PARTS)
        $ club_stco_quest_1 = 3
        $ msg.msg(renpy.translate_string("You reported the repaired shower to the [C_Dat]Student Council[C_Off]."))
        $ msg.msg(renpy.translate_string("The Council covered the parts: [C_Dat]Student Council[C_Off] treasury [C_Neg]-") + renpy.translate_string(str(str(CLUB_SHOWER_PARTS))) + renpy.translate_string("[C_Off]"))
        jump club_studentcouncil_start

    if club_stco_quest_1 == 3:
        wrin "Thanks again for sorting out that shower today.{w=[wt2]} Enjoy the dry floor."

        show studentcouncil_wsco_face 0
        jump club_studentcouncil_start

    wrin "Actually{w=[wt1]}, yes.{w=[wt2]} One of the showers in the [C_Dat]girls' locker room[C_Off] gave out{w=[wt1]}, water's leaking all over the floor.{w=[wt3]} Maintenance won't send anyone until next week{w=[wt1]}, and we can't leave it flooding.{w=[wt2]} You're handy with that sort of thing{w=[wt1]}, aren't you?"

    show studentcouncil_wsco_face 0

    menu:
        wrin "Actually{w=[wt1]}, yes.{w=[wt2]} One of the showers in the [C_Dat]girls' locker room[C_Off] gave out{w=[wt1]}, water's leaking all over the floor.{w=[wt3]} Maintenance won't send anyone until next week{w=[wt1]}, and we can't leave it flooding.{w=[wt2]} You're handy with that sort of thing{w=[wt1]}, aren't you?{fast}"

        "Accept the repair task":
            $ club_stco_quest_1 = 1
            $ hero_locker_f_access = True
            hero "Sure.{w=[wt2]} I'll go fix it."

            show studentcouncil_wkuu_eye u
            show studentcouncil_wsco_face 1
            wrin "Great.{w=[wt2]} Knock before you head in{w=[wt1]}, and be quick about it{w=[wt2]}, the Council's trusting you with this."

            show studentcouncil_wsco_face 0
            $ msg.msg(renpy.translate_string("Quest: repair the broken shower in the [C_Dat]Female Locker Room[C_Off]. It's now reachable from the courtyard, pool, and sport court."))

        "Decline for now":
            hero "Maybe later{w=[wt1]}, I've got a few things to handle first."

            show studentcouncil_wsco_face 1
            wrin "Don't take too long{w=[wt2]}, the floor won't dry itself."

            show studentcouncil_wsco_face 0

    jump club_studentcouncil_start
