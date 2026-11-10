# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wsis_show:

    # call circletable

    #$ add_stat("wsis", "love", 10)
    #return

    if a_event_3 == int:
        if a_event_3 >= 100 and is_specialevent == False:
            $ wsis_mood = "O4"
    elif wsis_love <= -20:
        $ wsis_mood = "O2"
    elif wsis_love <= 10:
        $ wsis_mood = "O1"
    elif wsis_love <= 30:
        $ wsis_mood = "A1"
    elif wsis_love > 30:
        $ wsis_mood = "A2"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_12

    show WSIS at RC
    show HERO at LC
    with dissolve

    if wnei_is_flw == True and is_specialevent == False and gametimeday == 1:
        show WNEI at OL
        show WNEI at LL_slow

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wsis_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wsis")))))

    if ((Get_ActivityName("wsis") in ["staying", "studying", "cleaning", "gaming", "at break"]) or
        (Check_CharInMap("wsis", "school") and Get_ActivityName("wsis") in ["staying", "studying", "cleaning", "drawing", "gaming", "at break"])):
        return

    elif Get_ActivityName("wsis") in ["hanging clothes", "collecting clothes"]: # Condition 2.6c. Checking of WSIS' clothes condition might be missing

        if "towel" not in wsis_achiev_wear:
            $ msg.msg(renpy.translate_string("👕 Style sprite unlocked for [C_Nam][fnamewsis][C_Off]"))
            $ wsis_achiev_wear.append("towel")

        # Stuck Meme requires high intimacy and is once-per-day; otherwise the simpler Waiting moment.
        if wsis_inti >= char_inti_req_date and not wsis_stuck_done:
            jump wsis_scene_stuck

        else:
            scene action_laundry_wait_1_bg home_kitchen
            show action_laundry_wait_1_wsis_body
            show action_laundry_wait_1_wsis_wear towel
            show action_laundry_wait_1_wsis_face o0
            show fx_light
            with dissolve

            show action_laundry_wait_1_wsis_face o1
            wsis "What!?"

            show action_laundry_wait_1_wsis_face o0 with None

            menu:
                "Talk":
                    pass

                "Return":
                    jump show_ui

    elif wsis_activity_current in [("changing", "school")]:
        label wsis_show_activity_changing:
            pass
        scene wsis_is_changing_2_bg bedroom
        show wsis_is_changing_2_wsis_body 1
        show wsis_is_changing_2_wsis_wear 1_school
        show wsis_is_changing_2_wsis_head 1
        show fx_light
        with dissolve

        pause

        show wsis_is_changing_2_wsis_head 2

        pause

        hero "S{w=[wt1]}-sorry{w=[wt2]}, I didn't know you were..."

        if wsis_quest_10 >= 1:
            call goto_home_hallway from _call_goto_home_hallway_5
            jump show_ui
            #scene bg_home_bedroom_wsis
            #call wsis_show from _call_wsis_show
            #call wsis_interact from _call_wsis_interact

        else:
            call wsis_hit("under") from _call_wsis_hit
            if _return == "Win":
                $ gametimemin += 10
                wsis "{aw}Ugh, get out!{/aw}"
            elif _return == "Lose":
                $ gametimemin += 20
                wsis "Get out if you don't want other!"
            $ add_stat("wsis", "inti", 0.5)
            $ Set_CharMap("hero", "home", "hallway")

            play BGM "audio/W2C - Tranquility.mp3"
            jump show_ui

    elif Get_ActivityName("wsis") in ["changing", "watching tv", "bathing", "at class"]:
        jump show_ui

    elif Get_ActivityName("wsis") in ["sleeping"]:
        if wsis_map == wnei_map:
            scene wsis_sleepover_2_bg
            show wsis_sleepover_2_wsis_wnei
            if gametimehour >= 18 or gametimehour <= 5:
                show wsis_sleepover_2_fx night:
                    blend "multiply"
            else:
                show wsis_sleepover_2_fx morning:
                    blend "add"
        else:
            scene wsis_badsleep3_bg
            show wsis_badsleep3_wsisbody
            if wsis_wear == "sleep":
                show wsis_badsleep3_wsisoutfit pajama

        pause
        
        if wsis_quest_4 >= 1 and "WSIS_is_sick" in wsis_know and gametimehour < 9:
            menu:
                "Wake her up":
                    jump wsis_quest_1_1
                "Return":
                    pass
        jump show_ui

    elif Get_ActivityName("wsis") in ["drawing"]:
        scene wsis_is_drawing_1_bg
        show wsis_is_drawing_1_wsis_body 1
        show wsis_is_drawing_1_wsis_wear 1_under
        if wsis_wear == "sleep":
            show wsis_is_drawing_1_wsis_wear 1_sleep
        else:
            show wsis_is_drawing_1_wsis_wear 1_home
        show fx_light

        menu:
            "Hug" if not is_specialevent:

                play SE1 "Bounce5.mp3"
                play SE2 renpy.random.choice(["Moan/A lvl0 (1).ogg", "Moan/A lvl2 (6).ogg", "Moan/A lvl2 (7).ogg", "Moan/A lvl3 (1).ogg", "Moan/A lvl3 (4).ogg", "Moan/A lvl3 (5).ogg"])

                scene wsis_is_drawing_1_bg
                show wsis_is_drawing_1_wsis_body 2
                show wsis_is_drawing_1_wsis_wear 2_under
                if wsis_wear == "sleep":
                    show wsis_is_drawing_1_wsis_wear 2_sleep
                else:
                    show wsis_is_drawing_1_wsis_wear 2_home
                show wsis_is_drawing_1_hero_wear 2_home
                show fx_light
                with dissolve

                pause

                $ add_stat("wsis", "inti", 2)
                $ add_stat("wsis", "lust", 3)

                hero "{bt}Hey, [C_Nam][hero_to_wsis][C_Off]...!{/bt}"

                if wsis_inti >= 20:
                    wsis "What are you doing, pervert!?"

                    if wsis_inti >= 40 and wsis_quest_2 == 0:
                        jump wsis_quest_5
                    $ gametimemin += 10

                else:
                    play SE1 "Hit1.mp3"

                    scene bg_2 sparking
                    show wsis_punch_4_wsis_body 1
                    show wsis_punch_4_wsis_wear 1home
                    show fx_rainbow:
                        blend "add"
                    with dissolve

                    play SE1 "Hit1.ogg"

                    scene bg_2 sparking
                    show wsis_punch_2_bg 1 at ZoomSTXYA_X1(zoomT1=0, zoomT2=5, zoomX1=-320, zoomX2=-640, zoomY1=-100, zoomY2=-400, zoomS1=1, zoomS2=2, alpha1=1, alpha2=0)
                    show wsis_punch_5_wsis_body 1 at CC
                    show wsis_punch_5_wsis_wear 1home at CC
                    show wsis_punch_5_hero_body 1 at CC
                    show wsis_punch_5_hero_wear 1home at CC
                    show wsis_punch_5_hero_body 1 at RC_heavy
                    show wsis_punch_5_hero_wear 1home at RC_heavy
                    show wsis_punch_2_fg 1 at ZoomSTXYA_X1(zoomT1=0, zoomT2=5, zoomX1=-320, zoomX2=-640, zoomY1=-100, zoomY2=-400, zoomS1=1, zoomS2=2, alpha1=1, alpha2=0)
                    show fx_rainbow:
                        blend "add"
                    with dissolve

                    pause

                    scene bg_0
                    with Dissolve(1)

                    play SE1 "JingleWrong.ogg"

                    show wsis_punch_3_hero_body 1
                    show wsis_punch_3_hero_wear 1_common
                    with Dissolve(1)

                    $ gametimemin = 60
                    jump show_ui

            "Talk":
                pass

            "Return":
                jump show_ui

        hero "Hey, [C_Nam][hero_to_wsis][C_Off]!{w=[wt2]} What are you doing?"

        call check_playermap from _call_check_playermap_21
        call hide_ui from _call_hide_ui_84
        show WSIS at RC
        show HERO at LC
        with fade
        return

    pause

    call check_playermap from _call_check_playermap_22
    call hide_ui from _call_hide_ui_85
    show WSIS at RC
    show HERO at LC
    with fade
    return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wsis_interact_end:
    if hero_map == "Home - Step-sis' bedroom":
        show HERO at OL_slow
        show WSIS at LL_slow
        if wsis_map == hero_map:
            $ a_event_0 = renpy.random.random()
            call wsis_upset_check from _call_wsis_upset_check
            if not (a_event_3 >= 100 and is_specialevent == False):
                if a_event_0 < 0.25:
                    wsis "So{w=[wt1]}, bye."
                elif a_event_0 < 0.5:
                    wsis "{aw}Shoo! Shoo!{/aw}"
                elif a_event_0 < 0.75:
                    wsis "Nothing else?{w=[wt2]} So, out of my room."
                else:
                    wsis "Ok{w=[wt1]}, time for you to go."
        $ wsis_bedroom_lock = True
        $ hero_map = "Home - Hallway"
        play SE1 "DoorOpen1.ogg"
    if "interacting_hero" in wsis_know:
        $ wsis_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wsis_interact_start:
    call hide_ui from _call_hide_ui_86
    call wsis_show_activity from _call_wsis_show_activity
    call wsis_upset_check from _call_wsis_upset_check_1
    call wsis_show from _call_wsis_show_1

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wsis_bedroom_check:
    # ----------------------------------------------------------------------------------------------------
    # The door is locked
    # ----------------------------------------------------------------------------------------------------
    if map_lock_bedroom_wsis == True and hero_map == "Home - Hallway" and not wsis_map == hero_map:
        # ----------------------------------------------------------------------------------------------------
        # HERO knocks the door
        # ----------------------------------------------------------------------------------------------------
        play SE1 "DoorKnock.ogg"
        pause 0.2
        play SE1 "DoorKnock.ogg"
        pause 0.2
        play SE1 "DoorKnock.ogg"
        pause 0.2

        # ----------------------------------------------------------------------------------------------------
        # HERO hasn't on Living Room before
        # ----------------------------------------------------------------------------------------------------
        if hero_quest_1 == 0:
            if personality[1] > 70:
                if wsis_quest_2 >= 1:
                    wsis "Hey, [C_Nam][wsis_to_hero][C_Off]!{w=[wt1]} I'm changing right now.{w=[wt2]} Can you wait a bit?"
                else:
                    wsis "{aw}Is it you, you moron?{w=[wt1]} Go away!{w=[wt2]} I'm busy now!{/aw}"
            else:
                wsis "{aw}I'm busy now!{/aw}"
            hero "O{w=[wt1]}-okay{w=[wt1]}, sorry.{w=[wt2]} {mind}(She must be changing.){/mind}"
            jump wsis_interact_end

        # ----------------------------------------------------------------------------------------------------
        # She isn't in bedroom
        # ----------------------------------------------------------------------------------------------------
        if wsis_map != "Home - Step-sis' bedroom":
            mind "(I think she isn't here.)"
            jump wsis_interact_end

        # ----------------------------------------------------------------------------------------------------
        # She's sleeping
        # ----------------------------------------------------------------------------------------------------
        elif wsis_map == "Home - Step-sis' bedroom" and map_lock_bedroom_wsis == True and wsis_act[1] == "sleeping":
            mind "(I think she's sleeping.)"
            jump wsis_interact_end

        # ----------------------------------------------------------------------------------------------------
        # She's upset
        # ----------------------------------------------------------------------------------------------------
        elif a_event_3 >= 100 and is_specialevent == False:
            mind "(I think she's upset.{w=[wt3]} I better give her time to calm down.)"
            jump wsis_interact_end

        # ----------------------------------------------------------------------------------------------------
        # She is in bedroom and opens the door
        # ----------------------------------------------------------------------------------------------------
        else:
            call wsis_bedroom_open from _call_wsis_bedroom_open
            jump wsis_interact_end

    # ----------------------------------------------------------------------------------------------------
    # The door is opened
    # ----------------------------------------------------------------------------------------------------
    elif map_lock_bedroom_wsis == False and hero_map == "Home - Hallway" and wsis_map == "Home - Step-sis' bedroom" and (gametimehour > 20 or gametimehour < 6) and wsis_act[1] == "sleeping":
        # ----------------------------------------------------------------------------------------------------
        # She is sleeping at late night
        # ----------------------------------------------------------------------------------------------------
        jump wsis_sleeping

    elif map_lock_bedroom_wsis == False and hero_map == "Home - Hallway" and wsis_map == "Home - Step-sis' bedroom":

        call wsis_bedroom_open from _call_wsis_bedroom_open_1

        hero "{aw}E{w=[wt1]}-excuse me...{/aw}"
        jump wsis_interact_end

    elif hero_map == "Home - Hallway" and not wsis_map == "Home - Step-sis' bedroom":

        mind "(She's not here.)"
        jump wsis_interact_end

    else:
        call wsis_interact_check from _call_wsis_interact_check

label wsis_bedroom_open:
    # ----------------------------------------------------------------------------------------------------
    # Open Door
    # ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_87
    play SE1 "DoorOpen1.ogg"
    $ hero_map = "Home - Step-sis' bedroom"
    call check_playermap from _call_check_playermap_23

    call wsis_interact_start from _call_wsis_interact_start

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wsis_interact_check:

    # Save current outfit before time update
    $ wsis_wear_keep = wsis_wear
    
    call gamecheck from _call_gamecheck_17

    # Update game time (this may trigger schedule changes that affect wearing)
    call gametime from _call_gametime_40

    call hide_ui from _call_hide_ui_88

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wsis_wear != wsis_wear_keep:
        $ wsis_wear = wsis_wear_keep

    call wsis_show from _call_wsis_show_2
    call wsis_upset_check from _call_wsis_upset_check_2

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    # Upset
    if a_event_3 >= 100 and is_specialevent == False:
        if wsis_quest_2 >= 1:
            wsis "I need some space right now, [C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Please."
        else:
            wsis "Leave me alone!"
        jump wsis_interact_end

    # Special Event
    elif Get_ActivityName("wsis") in "changing":
        wsis "{aw}Shoo! Shoo!{/aw}{w=[wt2]} I need to change!"
        jump wsis_interact_end

    # Special Event
    elif is_specialevent == True and gametimeday == 1 and gametimehour == 12:
        wsis "Oh{w=[wt2]}, lunch is ready.{w=[wt2]}{nw}"

        show WSIS at OL_slow
        wsis "Oh{w=[wt2]}, lunch is ready.{w=[wt2]}{fast} No time for chitchat."
        jump wsis_interact_end

    # Too late to chat
    elif hero_map == "Home - Step-sis' bedroom" and (gametimehour >= 20 or gametimehour <= 5):
        if wsis_quest_2 >= 1:
            wsis "It's getting late, [C_Nam][wsis_to_hero][C_Off].{w=[wt2]} We should both get some rest."
        else:
            wsis "Isn't it time for you to go away?"
        #if (wsis_inti < 20 and wsis_love < 60): # ???
        jump wsis_interact_end

    elif hero_map == "Home - Step-sis' bedroom" and gametimehour == 7 and gametimemin < 30:
        wsis "Hey{w=[wt2]}, I'll shower now.{w=[wt2]}{nw}"
        show WSIS at LL_average
        show HERO at OL_slow
        $ hero_mood = "O1"
        wsis "Hey, I'll shower now.{fast} {aw}Shoo! Shoo!{/aw}{w=[wt4]}{nw}"
        $ hero_map = "Home - Hallway"
        play SE1 "DoorOpen1.ogg"
        wsis "{nw}"
        jump wsis_interact_end

    elif hero_map == "Home - Step-sis' bedroom" and gametimehour >= 9 and gametimehour <= 11 and wnei_map == "Home - Living room":
        wsis "I think i listened [C_Nam][fnamewnei][C_Off]'s voice downstairs.{w=[wt2]} I'm going there."
        show WSIS at OL_slow
        hero "So let's-{nw}"
        show HERO at OL_average
        $ hero_map = "Home - Hallway"
        play SE1 "DoorOpen1.ogg"
        wsis "{sc}{b}Hurry!!!{/b}{/sc}{w=[wt4]}{nw}"
        jump wsis_interact_end

    elif hero_map == "Home - Step-sis' bedroom" and gametimehour >= 9 and gametimehour <= 11 and wnei_map == "Home - Step-sis' bedroom":
        wsis "Don't you think you're too comfortable here?{w=[wt2]} cmon,{w=[wt1]} we're going downstairs!"
        show WNEI at CC_slow
        wnei "Let's go!!!"
        show HERO at OL_average
        show WNEI at OL_average
        show WSIS at OL_slow
        $ hero_map = "Home - Hallway"
        play SE1 "DoorOpen1.ogg"
        wsis "{sc}{b}Hurry!!!{/b}{/sc}{w=[wt4]}{nw}"
        jump wsis_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Check_CharInMap("wsis", "school"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "wsis"):
            show WSIS at LC_average
            wsis "Teacher is already here.{nw}"

            #show WSIS at LL
            show WSIS at RR_slow
            show HERO at OR_slow
            wsis "Teacher is already here.{fast}{w=[wt1]} {bt}Shoo...! Shoo...!{/bt}"
            $ Set_CharMap("hero", "school", "hallway_2")

        else:
            $ wsis_mood = "O1"
            wsis "Tch...{w=[wt2]} I need to go to class now."

            if Get_MapName("wsis", "at class") == Get_MapName(None, "school", "class_1a"):
                menu:
                    "Accompany her":
                        $ hero_mood = "A1"
                        hero "I'll walk with you."

                        if wsis_quest_2 >= 1:
                            $ wsis_mood = "A1"
                            $ wsis_fx = 1
                            wsis "Hmph{w=[wt1]}, you better hurry up then!"

                        else:
                            $ wsis_mood = "O2"
                            wsis "{aw}W{w=[wt1]}-What!?{/aw}{w=[wt2]} I don't need an escort, moron!"

                            $ hero_mood = "A2"
                            hero "I'm going that way anyway."

                            $ wsis_mood = "O1"
                            $ wsis_fx = 1
                            wsis "Hunf...{w=[wt2]} {aw}Fine...!{/aw}{w=[wt3]} But don't walk so close to me!{w=[wt2]} People might get the wrong idea."
                        
                        scene bg_0
                        with dissolve

                        $ hero_map = wsis_map
                        call gametime from _call_gametime_41
                        call check_playermap from _call_check_playermap_24
                        call hide_ui from _call_hide_ui_89
                        show WSIS at RC
                        show HERO at LC
                        with dissolve
                        
                        $ wsis_mood = "O1"
                        wsis "Now {bt}Shoo...! Shoo...!{/bt}"

                        jump wsis_interact_end
                        
                    "Let her go":
                        pass

            $ hero_mood = "A1"
            hero "See you later."
            
            $ wsis_mood = "O1"
            wsis "Whatever."

        jump wsis_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif not Check_CharSameMap("hero", "wsis") and Get_ActivityName("wsis") in ["moving"] and (gametimehour == 7) and gametimeweek in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    # ----------------------------------------------------------------------------------------------------
        wsis "So, hurry up!{w=[wt2]} We're late to school!"

    # ----------------------------------------------------------------------------------------------------
    elif not Check_CharSameMap("hero", "wsis"): # Else
    # ----------------------------------------------------------------------------------------------------
        if wsis_quest_2 >= 1:
            wsis "Need to do something.{w=[wt2]} Talk to you later, [C_Nam][wsis_to_hero][C_Off]."
        else:
            wsis "So, moron.{w=[wt2]} No time to chitchat now.{w=[wt2]} See ya."
        jump wsis_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Dinner Special Event
    # ----------------------------------------------------------------------------------------------------
    elif gametimeday == 1 and gametimehour >= 18 and is_specialevent == True and not "WSIS" in scenestep:
        if wsis_quest_2 >= 1:
            wsis "Hey, [C_Nam][wsis_to_hero][C_Off]!{w=[wt2]} Come on, the food looks really good!"
        else:
            wsis "Hey moron!{w=[wt2]} if you don't hurry, I'll eat all of these myself."

    # ----------------------------------------------------------------------------------------------------
    # After first dialogue
    # ----------------------------------------------------------------------------------------------------
    elif "GameIntro" in wsis_know:
        $ wsis_know.remove("GameIntro")
        $ wsis_mood = "O1"
        $ hero_mood = "O1"
        hero "Hey,{w=[wt1]} sorry about earlier.{w=[wt2]} I did not mean that.{w=[wt2]} Can we talk?"
        wsis "Hunf!...{w=[wt1]} whatever..."

        if wnei_map == hero_map:
            wnei "Hmm?{w=[wt2]} What happened?"
            $ wsis_fx = 2
            $ wsis_mood = "O2"
            wsis "N{w=[wt1]}-NOTHING!"
            $ wsis_fx = 0
            $ wsis_mood = "O1"

    # ----------------------------------------------------------------------------------------------------
    # Before breakfast
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "home", "living_room") and gametimehour <= 7:
        if hero_wear == "school" and hero_needs[0] == True:
            if wsis_quest_2 >= 1:
                wsis "Come on, [C_Nam][wsis_to_hero][C_Off]!{w=[wt1]} We should get going soon."
            else:
                wsis "Hurry up!{w=[wt1]} I don't wanna be late because of you!"

        elif hero_wear == "school":
            if wsis_quest_2 >= 1:
                wsis "Hey, [C_Nam][wsis_to_hero][C_Off].{w=[wt2]} You should eat something before we go."
            else:
                wsis "Hey, moron.{w=[wt2]} If you don't eat your breakfast{w=[wt1]}, I'll eat yours."

        else:
            $ wsis_mood = "O2"
            if wsis_quest_2 >= 1:
                wsis "Aren't you going to change into your uniform?{w=[wt3]} We need to leave soon."
            else:
                wsis "Huh!?{w=[wt2]} Aren't you going to wear your uniform?{w=[wt3]} If you do not hurry I'll leave without you!"

    # ----------------------------------------------------------------------------------------------------
    # WSIS is watching TV
    # ----------------------------------------------------------------------------------------------------
    elif wsis_act[1] == "watching TV":
        jump wsis_watchingtv

    # ----------------------------------------------------------------------------------------------------
    # WSIS is drawing
    # ----------------------------------------------------------------------------------------------------
    elif wsis_act[1] == "drawing":
        scene bg_1
        with fade
        "[C_Nam][fnamewsis][C_Off] is drawing{nw}"
        menu:
            "[C_Nam][fnamewsis][C_Off] is drawing{fast}"
            "Join her":
                scene bg_0
                with Dissolve(1)
                pause(0.5)
                jump wsis_watchingtv
            "Return":
                jump wsis_interact_end

    # ----------------------------------------------------------------------------------------------------
    # WSIS is studying
    # ----------------------------------------------------------------------------------------------------
    elif wsis_act[1] == "studying":
        scene bg_1
        with fade
        "[C_Nam][fnamewsis][C_Off] is studying{nw}"
        menu:
            "[C_Nam][fnamewsis][C_Off] is studying{fast}"
            "Join her":
                scene bg_0
                with Dissolve(1)
                pause(0.5)
                jump wsis_watchingtv
            "Return":
                jump wsis_interact_end

    # ----------------------------------------------------------------------------------------------------
    # WSIS is playing video game
    # ----------------------------------------------------------------------------------------------------
    elif wsis_act[1] == "playing video game":
        scene bg_1
        with fade
        "[C_Nam][fnamewsis][C_Off] is playing video game{nw}"
        menu:
            "[C_Nam][fnamewsis][C_Off] is playing video game{fast}"
            "Join her":
                scene bg_0
                with Dissolve(1)
                pause(0.5)
                jump wsis_watchingtv
            "Return":
                jump wsis_interact_end

    # ----------------------------------------------------------------------------------------------------
    # WSIS is at School - Frontyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school") and gametimehour >= 12:
        wsis "What do you want?{w=[wt2]} I'm about to go home."
        menu:
            wsis "What do you want? I'm about to go home.{fast}"
            "Stay at school":
                hero "Okay{w=[wt1]}, I think I'll stay here a little more."
                wsis "Right.{w=[wt2]} See ya!"
                jump wsis_interact_end

            "Invite her to hang out at school":
                hero "Don't go.{w=[wt3]} Let's hang out here!"

                if wsis_inti < 10:
                    wsis "Why would I stay here with you{w=[wt1]}, idiot?"
                    hero "{bt}Ehhh...?{/bt}"

                else:
                    if wsis_quest_2 >= 1:
                        wsis "O{w=[wt1]}-okay{w=[wt2]}, what we're gonna do?"
                    else:
                        wsis "Hmph.{w=[wt2]} It's not like I have anything better to do{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} What do you wanna do here?"

                    call goto_school_sportcourt from _call_goto_school_sportcourt
                    call check_playermap from _call_check_playermap_25
                    call hide_ui from _call_hide_ui_90

                    scene socializing_jogging_bg sportcourt
                    show socializing_jogging_hero_body 1
                    show socializing_jogging_hero_wear 1_school_sport
                    show socializing_jogging_hero_face 1a0
                    show socializing_jogging_wsis_body 1
                    show socializing_jogging_wsis_wear 1_school_sport
                    show socializing_jogging_wsis_face 1o0
                    show socializing_jogging_wsis_fg 1
                    show fx_light
                    with Dissolve(2)

                    pause

                    call goto_school_pool from _call_goto_school_pool
                    call check_playermap from _call_check_playermap_26
                    call hide_ui from _call_hide_ui_91

                    scene studying_swimming_2_bg
                    show studying_swimming_2_wsis
                    show studying_swimming_2_hero
                    with Dissolve(2)

                    pause

                    scene socializing_pool_bg 1
                    show socializing_pool_hero talking
                    show socializing_pool_wsis
                    with Fade(1,0,2)

                    pause

                    $ a_event_0 = 1080 - ((gametimehour * 60) + gametimemin)
                    $ gametimemin += a_event_0
                    $ add_stat("wsis", "inti", 0)
                    $ add_stat("wsis", "love", 0)
                    call gametime from _call_gametime_42

                    call goto_school_pool from _call_goto_school_pool_1
                    call check_playermap from _call_check_playermap_27
                    call hide_ui from _call_hide_ui_92

                    $ wsis_wear = "school_swim"
                    $ hero_wear = "school_swim"

                    show HERO at LC
                    show WSIS at RC

                    hero "That was fun!"

                    if wsis_quest_2 < 1:
                        wsis "Whatever.{w=[wt2]} Let's go home."

                    scene bg_0 with Dissolve(1)

                    scene action_walk_bg street
                    show action_walk_hero_body 1
                    show action_walk_hero_wear 1school
                    if wsis_inti < 10:
                        show action_walk_wsis_body 1
                        show action_walk_wsis_wear 1school
                    else:
                        show action_walk_wsis_body 2
                        show action_walk_wsis_wear 2school
                    with Dissolve(2)
                    pause

                    scene bg_0 with Dissolve(1)

                    $ hero_wear = "common1"

                    call goto_home_livingroom from _call_goto_home_livingroom
                    call check_playermap from _call_check_playermap_28
                    call hide_ui from _call_hide_ui_93

                    call gametime from _call_gametime_43

                jump wsis_interact_end


            "Go with her":
                label wsis_interact_hangout_gohome:
                    hero "Wait for me!"
                    wsis "Hunf{w=[wt2]}, hurry up then!"
                    show HERO at OL_slow
                    show WSIS at OL_slow

                    scene bg_0
                    with Dissolve(1)

                    $ gametimemin += 60
                    $ add_stat("wsis", "inti", 0.6)
                    $ StartAct("wsis", (("moving", "home"), 0), True)
                    call gametime from _call_gametime_44

                    scene action_walk_bg street
                    show action_walk_hero_body 1
                    show action_walk_hero_wear 1school
                    if wsis_inti < 10:
                        show action_walk_wsis_body 1
                        show action_walk_wsis_wear 1school
                    else:
                        show action_walk_wsis_body 2
                        show action_walk_wsis_wear 2school
                    with Dissolve(2)
                    pause
                    scene bg_0
                    with Dissolve(1)

                    if wsis_inti >= 10:
                        jump wsis_quest_4
                    else:
                        scene bg_home livingroom
                        with dissolve
                        $ hero_wear = "common1"
                        call goto_home_livingroom from _call_goto_home_livingroom_1
                        jump show_ui

    # ----------------------------------------------------------------------------------------------------
    # WSIS is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wsis") in ["eating"]:
        "[C_Nam][fnamewsis][C_Off] is spending time at a courtyard table{nw}"
        menu:
            "[C_Nam][fnamewsis][C_Off] is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wsis") from _call_circletable_10

                while Get_ActivityName("wsis") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_13
                call gametime from _call_gametime_45
                
                jump wsis_interact_start

            "Return":
                jump wsis_interact_end

    # ----------------------------------------------------------------------------------------------------
    # WSIS is in date
    # ----------------------------------------------------------------------------------------------------
    elif date_active == True:
        $ a_event_0 = renpy.random.random()

        if 0 > 1: # Just for organization
            pass

        elif date_spi >= 80: # Date is very spicy
            if a_event_0 < 1/6:
                $ wsis_fx = 2
                $ wsis_mood = "O1"
                wsis "{aw}D{w=[wt1]}-don't look so pleased with yourself!{/aw}{w=[wt3]} I know exactly what you're thinking about right now."
            elif a_event_0 < 2/6:
                $ wsis_fx = 2
                $ wsis_mood = "O2"
                wsis "We are {b}never{/b} telling [C_Nam]Mom[C_Off] about today.{w=[wt3]} Not one word{w=[wt1]}, [C_Nam][wsis_to_hero][C_Off]."
            elif a_event_0 < 3/6:
                $ wsis_fx = 2
                $ wsis_mood = "O2"
                wsis "My heart still hasn't calmed down{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {aw}and that's entirely your fault!{/aw}"
            elif a_event_0 < 4/6:
                $ wsis_fx = 2
                $ wsis_mood = "O1"
                wsis "[C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} d{w=[wt1]}-don't you think we're crossing the line...?"
            elif a_event_0 < 5/6:
                $ wsis_fx = 2
                $ wsis_mood = "O1"
                wsis "L{w=[wt1]}-look at what we've being done today{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} How will I look at the mirror now...?"
            else:
                $ wsis_fx = 2
                $ wsis_mood = "O1"
                wsis "I can't even look at you right now.{w=[wt3]} Say something normal{w=[wt1]}, quick!"

        elif date_rom >= 80: # Date is very romantic
            if a_event_0 < 1/5:
                $ wsis_fx = 1
                $ wsis_mood = "A1"
                wsis "This is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} nice.{w=[wt3]} {aw}Don't make me say it twice!{/aw}"
            elif a_event_0 < 2/5:
                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "You planned all of this{w=[wt1]}, didn't you?{w=[wt3]} {aw}Idiot...!{/aw}"
            elif a_event_0 < 3/5:
                $ wsis_fx = 1
                $ wsis_mood = "A1"
                wsis "T{w=[wt1]}-thank you for today, [C_Nam][wsis_to_hero][C_Off]."
            elif a_event_0 < 4/5:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "I don't want this day to end..."
            else:
                $ wsis_fx = 2
                $ wsis_mood = "A2"
                wsis "I think I can stay with you just a little longer{w=[wt2]}, if you insist..."

        elif date_fun >= 80: # Date is very fun
            if a_event_0 < 1/5:
                $ wsis_mood = "A3"
                wsis "I haven't had this much fun since{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}{nw}"
                $ wsis_mood = "O2"
                wsis "I haven't had this much fun since{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}{fast} {aw}f{w=[wt1]}-forget it!{/aw}"
            elif a_event_0 < 2/5:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "{aw}Ugh...!{/aw}{w=[wt2]} I d{w=[wt1]}-don't wanna go home."
            elif a_event_0 < 3/5:
                $ wsis_fx = 1
                $ wsis_mood = "A1"
                wsis "{aw}D{w=[wt1]}-don't go thinking I'm having fun being with you or anything like that, you idiot!{w=[wt2]} I'm just laughing at you.{/aw}"
            elif a_event_0 < 4/5:
                $ wsis_fx = 1
                $ wsis_mood = "A1"
                wsis "L{w=[wt1]}-let's keep hanging out j{w=[wt1]}-just a little more...?{w=[wt3]} Not that I'm enjoying stay with you or anything, idiot!{w=[wt3]} It's just that you seems very happy and I can stay a little longer if you want.{w=[wt3]} That's it!"
            else:
                $ wsis_fx = 1
                $ wsis_mood = "A1"
                wsis "We s{w=[wt1]}-should do it more times.{w=[wt4]} I{w=[wt1]}-I mean{w=[wt2]}, I could go with you again if you insist!"

        elif date_spi >= 60: # Date is spicy
            if a_event_0 < 1/6:
                $ wsis_fx = 2
                $ wsis_mood = "O1"
                wsis "{aw}You're a pervert!{/aw}"
            elif a_event_0 < 2/6:
                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "W{w=[wt1]}-what do you want{w=[wt2]}, you pervert?"
            elif a_event_0 < 3/6:
                $ wsis_fx = 2
                $ wsis_mood = "O2"
                wsis "{aw}Hmph...!{/aw} I{w=[wt1]}-I can see you had bad intentions from the start."
            elif a_event_0 < 4/6:
                $ wsis_fx = 2
                $ wsis_mood = "O2"
                wsis "[C_Nam][wsis_to_hero][C_Off]{w=[wt2]}, y{w=[wt1]}-you b{w=[wt1]}-better don't cross the limits!"
            elif a_event_0 < 5/6:
                $ wsis_fx = 2
                $ wsis_mood = "O2"
                wsis "[C_Nam][wsis_to_hero][C_Off]{w=[wt2]}, I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} feeling weird..."
            else:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "S{w=[wt1]}-stop grinning like that.{w=[wt2]} You're making me feel weird..."

        elif date_rom >= 60: # Date is romantic
            if a_event_0 < 1/6:
                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "It's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} it's kind of nice out here."
            elif a_event_0 < 2/6:
                $ wsis_fx = 1
                $ wsis_mood = "A1"
                wsis "Don't get used to this{w=[wt1]}, okay?{w=[wt3]} I'm only in a good mood today.{w=[wt2]} That's it!"
            elif a_event_0 < 3/6:
                $ wsis_fx = 1
                $ wsis_mood = "O2"
                wsis "Y{w=[wt1]}-yes.{w=[wt2]} It's being nice.{w=[wt2]} So what?"
            elif a_event_0 < 4/6:
                $ wsis_fx = 1
                $ wsis_mood = "O2"
                wsis "It's being nice.{w=[wt2]} Just don't be so full of yourself!"
            elif a_event_0 < 5/6:
                $ wsis_fx = 1
                $ wsis_mood = "O2"
                wsis "D{w=[wt1]}-don't go thinking I'm feeling good with you or anything{w=[wt2]}, you idiot!"
            else:
                $ wsis_mood = "O2"
                wsis "Why are you looking at me with that fool face as if you're thinking I'm enjoying your company or anything, you idiot?{w=[wt3]} {aw}Hmph...!{/aw}"

        elif date_fun >= 60: # Date is fun
            if a_event_0 < 1/5:
                $ wsis_mood = "A1"
                wsis "Okay{w=[wt2]}, this beats sitting at home grinding the same dungeon all afternoon."
            elif a_event_0 < 2/5:
                $ wsis_mood = "A3"
                wsis "Okay{w=[wt2]}, getting out of home is not that bad, I suppose."
            elif a_event_0 < 3/5:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "Fine{w=[wt1]}, fine{w=[wt2]}, I'm having fun.{w=[wt3]} {aw}Happy now?{/aw}"
            elif a_event_0 < 4/5:
                $ wsis_mood = "A2"
                wsis "So{w=[wt2]}, what's next, [C_Nam][wsis_to_hero][C_Off]?"
            else:
                $ wsis_mood = "A1"
                wsis "{aw}Hmph...!{/aw}{w=[wt3]} You're not terrible to hang out with.{w=[wt2]} {aw}Sometimes!{/aw}"

        elif date_spi >= 30: # Date is getting spicy
            if a_event_0 < 1/4:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "You've been sneaking looks at me all day.{w=[wt3]} Pervert!"
            elif a_event_0 < 2/4:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "Y{w=[wt1]}-you'd better not have any ulterior motives for this today."
            elif a_event_0 < 3/4:
                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "You seem too bold today.{w=[wt3]} I'll keep an eye on you."
            else:
                $ wsis_mood = "O2"
                wsis "I know that face.{w=[wt2]} You're having pervert ideas!"

        elif date_rom >= 30: # Date is getting romantic
            if a_event_0 < 1/5:
                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "You keep making that fool face."
            elif a_event_0 < 2/5:
                $ wsis_mood = "A1"
                wsis "It's being kinda nice today.{w=[wt3]} So what?"
            elif a_event_0 < 3/5:
                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "{bt}Fine... Fine...{/bt}{w=[wt3]} I{w=[wt1]}-I guess I don't really hate walking around with you."
            elif a_event_0 < 4/5:
                $ wsis_mood = "A1"
                wsis "D{w=[wt1]}-don't get wrong ideas, idiot.{w=[wt3]} It's not that bad.{w=[wt2]} Just that."
            else:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "Stop smiling at me like that{w=[wt2]}, I can't think straight."

        elif date_fun >= 30: # Date is getting fun
            if a_event_0 < 1/4:
                $ wsis_mood = "A1"
                wsis "Alright{w=[wt1]}, I'll admit it{w=[wt2]}, this isn't the worst way to spend the day."
            elif a_event_0 < 2/4:
                $ wsis_mood = "A2"
                wsis "Where to next?{w=[wt3]} And don't make me pick{w=[wt1]}, you're the one who dragged me here."
            elif a_event_0 < 3/4:
                $ wsis_mood = "A1"
                wsis "Not bad{w=[wt1]}, [C_Nam][wsis_to_hero][C_Off].{w=[wt3]} Not good either{w=[wt1]}, but not bad."
            else:
                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "I might be enjoying this a little.{w=[wt3]} {aw}A {b}little{/b}!{/aw}"

        # Still no good score
        elif wsis_love >= 60: # Absolutelly In love
            if a_event_0 < 1/6:
                $ wsis_mood = "A1"
                wsis "What will we do now, [C_Nam][wsis_to_hero][C_Off]?"
            elif a_event_0 < 2/6:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "[C_Nam][wsis_to_hero][C_Off]{w=[wt2]}, C{w=[wt1]}-can you stop looking at me like this?{w=[wt3]} {aw}It's embarrassing!{/aw}"
            elif a_event_0 < 3/6:
                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "I still can't believe I said yes to this{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {aw}don't make me regret it!{/aw}"
            elif a_event_0 < 4/6:
                $ wsis_fx = 1
                $ wsis_mood = "A1"
                wsis "You'd better be paying attention to me today{w=[wt1]}, [C_Nam][wsis_to_hero][C_Off]."
            elif a_event_0 < 5/6:
                $ wsis_fx = 2
                $ wsis_mood = "O1"
                wsis "{aw}S{w=[wt1]}-stand a little further away!{/aw}{w=[wt3]} Someone from school could be here."
            else:
                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "If you get bored of me{w=[wt1]}, just say it.{w=[wt3]} {aw}Not that I'd care!{/aw}"

        elif wsis_love >= 30: # Kinda In Love
            if a_event_0 < 1/6:
                wsis "I'm only here because you insisted, of course.{w=[wt3]} Y{w=[wt1]}-you'd better not waste my time!"
            elif a_event_0 < 2/6:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "D{w=[wt1]}-don't look at me like this, idiot!{w=[wt2]} It's embarrassing...!"
            elif a_event_0 < 3/6:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "Don't go thinking too highly of yourself just because I agreed to go out with you, you idiot!{w=[wt4]} I'm just doing you a favor."
            elif a_event_0 < 4/6:
                $ wsis_fx = 1
                $ wsis_mood = "O1"
                wsis "So{w=[wt2]}, how long are we just staying out here?"
            elif a_event_0 < 5/6:
                $ wsis_mood = "A2"
                wsis "Don't get any strange ideas just because I'm here with you. {aw}Hmph...!{/aw}"
            else:
                $ wsis_fx = 1
                $ wsis_mood = "O2"
                wsis "If you make me regret coming{w=[wt2]}, you're going home alone."

        else:
            if a_event_0 < 1/5:
                wsis "So{w=[wt2]}, you dragged me out of home just to chitchat, huh?"
            elif a_event_0 < 2/5:
                wsis "Can we go back home now?"
            elif a_event_0 < 3/5:
                $ wsis_mood = "O1"
                wsis "Are we done here?{w=[wt3]} I had things to do today."
            elif a_event_0 < 4/5:
                $ wsis_mood = "O2"
                wsis "You'd better have a plan{w=[wt1]}, because standing around isn't one."
            elif a_event_0 < 4/5:
                $ wsis_mood = "O1"
                wsis "What?{w=[wt2]} Will we move on or not?"
            else:
                $ wsis_mood = "O1"
                wsis "You didn't get me to go out of home just to stand here doing nothing, did you?"

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wsis_know:
        
        if wsis_quest_2 >= 1 and renpy.random.random() < (10.15+(wsis_love*0.002)): # Initiative: can start topics after Quest 5
            jump initiative_wsis

        elif renpy.random.random() < 0.2:
            pass

        else:
            $ a_event_0 = renpy.random.random()

            if personality[0] == "Hentai" and a_event_0 > renpy.random.random() * 4:
                wsis "S{w=[wt1]}-Stop staring at me with these pervert eyes!"

            elif wsis_love < 30: # detached
                if a_event_0 < 1/6:
                    wsis "Can I go back to what I was doing?"
                elif a_event_0 < 2/6:
                    wsis "Can I go back to my things now?"

                elif wsis_quest_2 >= 1:
                    if a_event_0 < 4/6:
                        wsis "So{w=[wt2]}, anything else you need?"
                    else:
                        wsis "Is there anything else, [C_Nam][wsis_to_hero][C_Off]?"

                elif a_event_0 < 3/6:
                    wsis "So{w=[wt2]}, don't you get tired of pestering me?"
                elif a_event_0 < 4/6:
                    wsis "Anything else?{w=[wt2]} If you don't you have anything better to do{w=[wt1]}, I have."
                elif a_event_0 < 5/6:
                    wsis "Ok{w=[wt2]}, will you leave me alone now or there's something else?"
                else:
                    wsis "What else?{w=[wt2]} Can I go now?"

            elif wsis_love < 60: # friendly - starting to feel something
                if wsis_quest_2 >= 1:
                    # After reconciliation - warmer, more open
                    if a_event_0 < 1/6:
                        wsis "So{w=[wt2]}, anything else, [C_Nam][wsis_to_hero][C_Off]?"
                    elif a_event_0 < 2/6:
                        wsis "Did you need something else?"
                    elif a_event_0 < 3/6:
                        $ wsis_fx = 1
                        wsis "I{w=[wt1]}, uhh{w=[wt2]}, I don't mind talking more{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} if you want."
                    elif a_event_0 < 4/6:
                        wsis "What's up?"
                    elif a_event_0 < 5/6:
                        $ wsis_fx = 1
                        wsis "Y{w=[wt1]}-you can stay a bit longer if you want."
                    else:
                        wsis "Something on your mind, [C_Nam][wsis_to_hero][C_Off]?"
                else:
                    # Before reconciliation - less aggressive but still guarded
                    if a_event_0 < 1/5:
                        wsis "What?"
                    elif a_event_0 < 2/5:
                        wsis "Something else?"
                    elif a_event_0 < 3/5:
                        wsis "Hm?"
                    elif a_event_0 < 4/5:
                        wsis "Need something?"
                    else:
                        wsis "What is it?"

            elif wsis_love >= 60: # in love - intense feelings
                if wsis_quest_2 >= 1:
                    # After reconciliation - openly affectionate but still gets embarrassed
                    if a_event_0 < 1/8:
                        $ wsis_fx = 1
                        wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I like spending time with you, [C_Nam][wsis_to_hero][C_Off]."
                    elif a_event_0 < 2/8:
                        $ wsis_fx = 2
                        wsis "Y{w=[wt1]}-you don't have to go yet{w=[wt1]}, do you?"
                    elif a_event_0 < 3/8:
                        $ wsis_fx = 1
                        wsis "Want to stay a little longer?{w=[wt2]} I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I don't mind."
                    elif a_event_0 < 4/8:
                        $ wsis_fx = 2
                        wsis "{aw}I{w=[wt1]}-It's not like I want you to stay longer or anything!{/aw}{w=[wt3]} But{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} if you want to."
                    elif a_event_0 < 5/8:
                        wsis "Hey, [C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} thanks for being here."
                    elif a_event_0 < 6/8:
                        $ wsis_fx = 1
                        wsis "Is there anything else you want to do together?"
                    elif a_event_0 < 7/8:
                        $ wsis_fx = 2
                        wsis "You're not getting bored of me, right?{w=[wt3]} {aw}N{w=[wt1]}-not that I care!{/aw}"
                    else:
                        $ wsis_fx = 1
                        wsis "I'm glad you're here, [C_Nam][wsis_to_hero][C_Off]."
                else:
                    # Before reconciliation - very flustered, conflicted feelings
                    if personality[0] == "Hentai":
                        $ wsis_fx = 2
                        wsis "W{w=[wt1]}-why are you looking at me like that!?"
                    else:
                        if a_event_0 < 1/4:
                            $ wsis_fx = 1
                            wsis "H{w=[wt1]}-hey."
                        elif a_event_0 < 2/4:
                            $ wsis_fx = 2
                            wsis "{aw}W{w=[wt1]}-what are you staring at!?{/aw}"
                        elif a_event_0 < 3/4:
                            wsis "Something else?"
                        else:
                            $ wsis_fx = 1
                            wsis "Uhm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} what?"

            else:
                wsis "Hm?"

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        if wsis_quest_2 >= 1:
            if wsis_love <= -20:
                wsis "What do you need, [C_Nam][wsis_to_hero][C_Off]?{w=[wt2]} I'm not really in the mood right now..."

            elif wsis_love <= 20:
                if personality[0] == "Hentai":
                    wsis "Hey{w=[wt1]}, [C_Nam][wsis_to_hero][C_Off]{w=[wt2]}.{w=[wt2]} What's up?"
                else:
                    wsis "Hey, [C_Nam][wsis_to_hero][C_Off].{w=[wt2]} Need something?"

            elif wsis_love <= 40:
                if personality[0] == "Hentai":
                    wsis "H{w=[wt1]}-hey{w=[wt1]}, what do you need?"
                else:
                    wsis "Hey, [C_Nam][wsis_to_hero][C_Off]!"

            elif wsis_love >= 60:
                if personality[0] == "Hentai":
                    wsis "You're hopeless{w=[wt1]}, you know?..."
                else:
                    wsis "H{w=[wt1]}-hey, [C_Nam][wsis_to_hero][C_Off]"

            else:
                wsis "What's up?"

        else:
            if wsis_love <= -20:
                wsis "Why don't you get out of my face, you jerk?"

            elif wsis_love <= 20:
                if personality[0] == "Hentai":
                    wsis "What do you want, pervert?"
                else:
                    wsis "What do you want, moron?"

            elif wsis_love <= 40:
                if personality[0] == "Hentai":
                    wsis "S{w=[wt1]}-Stop staring at me with these pervert eyes!"
                else:
                    wsis "Hey!"

            elif wsis_love >= 60:
                if personality[0] == "Hentai":
                    wsis "You're hopeless{w=[wt1]}, you know?..."
                else:
                    wsis "H{w=[wt1]}-hey, [C_Nam][wsis_to_hero][C_Off]"
                    
            else:
                wsis "What's up?"

    jump wsis_interact

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wsis_interact:
    call hide_ui from _call_hide_ui_94
    if "interacting_hero" not in wsis_know:
        $ wsis_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            if sum(1 for buceta in wsis_know if buceta =="Talk") >= 3 and wsis_quest_2 == 0:
                $ wsis_mood = "O1"
                wsis "Enough of chitchatting{w=[wt1]}, don't you think?"
                jump wsis_interact
            else:
                jump wsis_interact_chat
        "Touch" if not is_specialevent:
            jump wsis_interact_touch
        "Meet" if wsis_inti_cap >= char_inti_req_date and date_active == False:
            jump wsis_interact_meet
        "Hang out" if date_active == False:
            jump wsis_interact_hangout
        "Give item" if not is_specialevent:
            jump wsis_interact_gift
        "Return":
            jump wsis_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wsis_interact_gift:
    $ a_item_8 = "wsis"
    $ a_item_9 = 0
    $ a_item_6 = "wsis_interact"
    call UI_give_Item from _call_UI_give_Item_13

label wsis_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wsis_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wsis_interact_touch:
    menu:
        "Pat head" if wsis_to_hero == "Big Bro" and wsis_inti > 999:
            if not any(buceta.startswith("PatHead") for buceta in wsis_know):
                $ wsis_know.append("PatHead")

                if perk_cha_sex >= 1:
                    $ add_stat("wsis", "lust", 2)

                $ add_stat("wsis", "love", 2)
                $ add_stat("hero", "cha_sex", 2)

                hide screen wsis_pat
                with dissolve

            hide screen wsis_pat

            $ wsis_fx = 1
            $ gametimemin += 10
            $ add_stat("wsis", "inti", 0.1)

            jump wsis_interact_check

        "Hug":

            label wsis_interact_touch_hug:

                if wsis_inti < (personality[1]*0.05):
                    $ a_event_0 = 1
                    call wsis_reaction from _call_wsis_reaction

                elif not "Hug_Enough" in wsis_know:

                    call hide_ui from _call_hide_ui_95

                    $ wsis_know.append("Hug")
                    $ a_event_0 = sum(1 for buceta in wsis_know if buceta =="Hug")
                    $ wsis_fx = 1

                    if perk_cha_sex >= 1:
                       $ add_stat("wsis", "lust", 2)
                    $ add_stat("wsis", "love", 2/a_event_0)
                    $ add_stat("hero", "cha_sex", 2/a_event_0)

                    $ a_event_0 = renpy.random.random()
                    if a_event_0 <= 0.33:
                        scene bg_2 pink
                    elif a_event_0 <= 0.66:
                        scene bg_2 yellow
                    else:
                        scene bg_2 flowers
                    show bg_fx0
                    show action_wsis_hug_body
                    if hero_wear == "school":
                        show action_wsis_hug_outfithero school
                    else:
                        show action_wsis_hug_outfithero common1
                    if wsis_wear == "school":
                        show action_wsis_hug_outfitwsis school
                    elif wsis_wear == "sleepwear":
                        show action_wsis_hug_outfitwsis sleepwear
                    else:
                        show action_wsis_hug_outfitwsis common1
                    show action_wsis_hug_face o0
                    show action_wsis_hug_fx
                    show action_wsis_hug_glasses
                    with dissolve
                    pause

                    if (intimacy_tier("wsis") < 2 or wsis_love < 50) or sum(1 for buceta in wsis_know if buceta =="Hug") >= 2:
                        $ wsis_know.append("Hug_Enough")
                        show action_wsis_hug_face o1

                        if "WSIS_is_horny_1" in wsis_know and renpy.random.random() < (wsis_lust * 0.005):
                            $ wsis_know.remove("Hug_Enough")
                            wsis "{aw}Y{w=[wt1]}-you're hopeless{w=[wt1]}, you know that?{/aw}"
                        else:
                            wsis "Ok.{w=[wt2]} Now go off!"
                        show action_wsis_hug_face o0 with dissolve

                    call gamecheck from _call_gamecheck_18
                    call hide_ui from _call_hide_ui_96
                    call wsis_show from _call_wsis_show_3
                    $ gametimemin += 10
                    $ add_stat("wsis", "inti", 0.1)

                else:
                    $ a_event_0 = 1
                    call wsis_reaction from _call_wsis_reaction_1

            jump wsis_interact_check

        "Return":
            jump wsis_interact


# ----------------------------------------------------------------------------------------------------
label wsis_interact_meet: # Invite Options
# ----------------------------------------------------------------------------------------------------
    menu:
        "Reunion on Neighbor's {pr}[C_Dat](⏰ Sunday - 10:00-12:59)[C_Off]" if wnei_quest_6 >= 1 and "wsis" not in wnei_quest_7:

            if "Neighbors_Reunion" in wsis_know:
                hero "So{w=[wt2]}, will you come with me to the neighbor's house Sunday?"

                if Check_TaskCompletion("homework_wsis") >= 100 and gametimeweek == "Saturday":
                    if wsis_quest_2 >= 1:
                        $ wsis_mood = "A2"
                        $ wsis_fx = 1
                        wsis "Yeah{w=[wt2]}, I finished all my homework!{w=[wt3]} Thanks to you, [C_Nam][wsis_to_hero][C_Off].{w=[wt2]} So{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I guess we can go together."
                    else:
                        $ wsis_mood = "A1"
                        wsis "Hmph.{w=[wt2]} My homework's done{w=[wt2]}, so I guess I have no excuse now.{w=[wt3]} Fine{w=[wt2]}, let's go."

                else:
                    if wsis_quest_2 >= 1:
                        $ wsis_mood = "O1"
                        wsis "I still have a lot of homework to finish{w=[wt2]}, remember?{w=[wt3]} If it's all done by Sunday{w=[wt2]}, then we'll go together."
                    else:
                        $ wsis_mood = "O2"
                        wsis "We agreed you'd help me with my homework first.{w=[wt3]} Remember?{w=[wt2]} Get it done by Sunday{w=[wt2]}, then we'll talk."

            else:
                $ wsis_know.append("Neighbors_Reunion")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] is invited to [C_Dat]Neighbor's Reunion[C_Off]"))

                hero "[C_Nam][fnamewnei][C_Off]'s parents are inviting us to have lunch with them this Sunday.{w=[wt3]} Let's go!"

                if wsis_quest_2 >= 1:
                    $ wsis_mood = "O1"
                    wsis "Eh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I don't know{w=[wt2]}, [C_Nam][wsis_to_hero][C_Off].{w=[wt3]} You know I'm not really into{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} those kinds of gatherings."
                    hero "Come on{w=[wt2]}, it'll be fun!{w=[wt2]} And [C_Nam][fnamewnei][C_Off] would love to have you there."
                    $ wsis_mood = "O2"
                    wsis "{bt}Mmm...{/bt}{w=[wt2]} I still have a ton of homework to finish for next week.{w=[wt3]} I really should stay home and work on that."
                    hero "What if I help you with your homework?{w=[wt2]} Then you'd have time to come."
                    $ wsis_mood = "A1"
                    $ wsis_fx = 1
                    wsis "W{w=[wt1]}-wait{w=[wt2]}, really?{w=[wt3]} You'd do that for me?"
                    $ hero_mood = "A2"
                    hero "Of course!{w=[wt2]} We're family{w=[wt2]}, right?"
                    $ wsis_mood = "A2"
                    $ wsis_fx = 2
                    wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Okay{w=[wt2]}, fine.{w=[wt3]} If you finish my homework by Sunday{w=[wt2]}, I'll go with you.{w=[wt2]} Deal?"
                    hero "Deal!"
                    $ wsis_mood = "A1"
                    wsis "But don't mess it up{w=[wt2]}, okay?{w=[wt2]} I actually need good grades on that."

                else:
                    $ wsis_mood = "O1"
                    wsis "A lunch reunion?{w=[wt3]} Ugh{w=[wt2]}, no thanks.{w=[wt2]} You know those things aren't my style."
                    hero "Come on{w=[wt2]}, it won't be that bad.{w=[wt2]} [C_Nam][fnamewnei][C_Off] really wants you there."
                    $ wsis_mood = "O2"
                    wsis "I have a bunch of homework to finish anyway.{w=[wt3]} So{w=[wt2]}, no."
                    hero "What if I help you with your homework?{w=[wt2]} Then you'd be free to come."
                    $ wsis_mood = "O1"
                    wsis "Why would you do that?"
                    $ hero_mood = "A1"
                    hero "Because I want you to come.{w=[wt2]} Simple as that."
                    $ wsis_mood = "A1"
                    wsis "Hmph.{w=[wt3]} Fine.{w=[wt2]} If you finish my homework by Sunday{w=[wt2]}, I'll consider going.{w=[wt2]} Don't screw it up{w=[wt2]}, though."

        "Go out to the [C_Map]Shopping[C_Off] {pr}[C_Dat](⏰ 08:00-15:59)[C_Off]" if not "Date_Shopping" in wsis_know and wsis_inti >= char_inti_req_date and (gametimehour >= 8 and gametimehour < 16) and gametimeweek in ["Saturday", "Sunday"]:
            call date_invite("wsis", "shopping") from _call_date_invite

        "Return":
            jump wsis_interact

    jump wsis_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wsis_interact_hangout:
    menu:
        "Watch movie together" if is_specialevent == False and (gametimehour >= 20 and gametimehour <= 22):
            jump wsis_movie_1

        "Cook together" if is_specialevent == False and Check_CharInMap("hero", "home", "living_room") and (gametimehour >= 13 and gametimehour <= 21):
            $ hero_mood = "A1"
            hero "Let's cook something!"

            $ wsis_mood = "O1"
            if wsis_quest_2 >= 1:
                wsis "You want to cook together?{w=[wt2]} Well{w=[wt1]}, I guess that could be fun."
            else:
                wsis "Why would I cook something with you, idiot?"

            show HERO at OL_slow
            hero "To eat."

            show WSIS at OL_average
            if wsis_quest_2 >= 1:
                wsis "Alright{w=[wt2]}, what do you want to make?"
            else:
                wsis "{aw}OH, SHUT UP!!!{/aw}{w=[wt4]} What you wanna make?"
            call wsis_quest_1_kitchen_cook(buceta=True) from _call_wsis_quest_1_kitchen_cook
            jump show_ui

        "Have dinner" if gametimeday == 1 and gametimehour >= 18 and is_specialevent == True and not "WSIS" in scenestep:
            $ scenestep.insert(1, "WSIS")
            hero "Let's call [C_Nam][hero_about_wmom][C_Off] and [C_Nam][fnamewnei][C_Off] to have dinner before you eat everything."
            $ wsis_mood = "A1"
            wsis "Heh!{w=[wt1]} You better hurry! Cos I won't wait for anyone!{nw}"
            $ hero_mood = "A2"
            wsis "Heh!{w=[wt1]} You better hurry! Cos I won't wait for anyone!{fast}"

            scene scen_1_nightcelebration_wsis_bg
            show scen_1_nightcelebration_wsis_wmom o0
            show scen_1_nightcelebration_wsis_wsis o0
            show screen WSIS_EatSFX
            with Fade(0.5,0.5,2)

            show scen_1_nightcelebration_wsis_wmom o1
            wmom "Hey, Sweetie{w=[wt1]}, I know it's super yummy and all, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} We don't need to eat everything today, you know?{w=[wt3]} You might get a stomach ache!"

            show scen_1_nightcelebration_wsis_wmom o0
            show scen_1_nightcelebration_wsis_wsis o0
            wsis "{aw}(crunch crunch...){/aw}{fast}{w=[wt4]}{nw}"

            $ a_event_0 = 1
            show scen_1_nightcelebration_wsis_wsis o1
            wsis "{aw}(crunch crunch...){/aw}{fast} Don't worry, Mom!{w=[wt2]}{nw}"

            $ a_event_0 = 0
            show scen_1_nightcelebration_wsis_wsis o0
            wsis "{aw}(crunch crunch...){/aw} Don't worry, Mom! {aw}(crunch crunch...){/aw}{fast}{w=[wt4]}{nw}"

            $ a_event_0 = 1
            show scen_1_nightcelebration_wsis_wsis o1
            wsis "{aw}(crunch crunch...){/aw} Don't worry, Mom! {aw}(crunch crunch...){/aw}{fast}{pr}I'll eat just...{w=[wt2]}{nw}"

            $ a_event_0 = 0
            show scen_1_nightcelebration_wsis_wsis o0
            wsis "{aw}(crunch crunch...){/aw} Don't worry, Mom! {aw}(crunch crunch...){/aw}{pr}I'll eat just... {aw}(crunch crunch...){/aw}{fast}{w=[wt4]}{nw}"

            $ a_event_0 = 1
            show scen_1_nightcelebration_wsis_wsis o1
            wsis "{aw}(crunch crunch...){/aw} Don't worry, Mom! {aw}(crunch crunch...){/aw}{pr}I'll eat just... {aw}(crunch crunch...){/aw}{fast}{w=[wt4]} a little bit more...!{w=[wt2]}{nw}"

            $ a_event_0 = 0
            show scen_1_nightcelebration_wsis_wsis o0
            wsis "{aw}(crunch crunch...){/aw} Don't worry, Mom! {aw}(crunch crunch...){/aw}{pr}I'll eat just... {aw}(crunch crunch...){/aw} a little bit more...! {aw}(crunch crunch...){/aw}{fast}"

            hide screen WSIS_EatSFX
            $ add_stat("wsis", "love", 1)
            $ add_stat("wnei", "love", 1)
            $ add_stat("wmom", "love", 1)
            $ add_stat("hero", "cha_soc", 3)

            scene bg_home livingroom
            with Fade(1,0,2)
            jump wsis_interact_end

        "Eat together" if is_specialevent == False and Check_CharInMap("hero", "home", "living_room") and hero_needs[1] == False:
            if ((gametimehour >= 7 and gametimehour < 8) and not (gametimehour == 7 and gametimemin > 50)): # Breakfast at 7:00 - 7:49
                hero "Let's have breakfast!"

            elif ((gametimehour == 11 and gametimemin >= 30) and not (gametimehour == 12 and gametimemin < 30)): # Lunch at 11:30 - 12:29
                hero "Let's have lunch!"

            elif ((gametimehour == 17 and gametimemin >= 30) and not (gametimehour == 18 and gametimemin < 30)): # Dinner at 17:30 - 18:29
                hero "Let's have dinner!"

            else:
                hero "Let's eat something!"

            if wsis_quest_2 >= 1:
                wsis "Sure, [C_Nam][wsis_to_hero][C_Off].{w=[wt2]} Let's eat!"
            else:
                wsis "Shut up and just hurry up to eat before I take your part too!"
            #$ wsis_mood = "O3"
            #wsis "Hey!{w=[wt1]} Why are you taking the larger piece!?"
            #$ hero_mood = "O1"
            #hero "Listen...{w=[wt2]} I even thought you had a black hole in your belly to eat that much...{w=[wt2]} But after last night I realized that your real problem is the gluttony.{w=[wt2]} So be mindful next time."
            #$ wsis_mood = "O4"
            #$ wsis_fx = 1
            #wsis "{pa}S{w=[wt1]}-Shut up!{/pa}"

            call action_eat from _call_action_eat
            call check_playermap from _call_check_playermap_29
            jump wsis_interact_check

        "Go to school together" if gametimehour == 6 or (gametimehour <= 7 and gametimemin == 0) and Check_CharInMap("hero", "living_room") and not gametimeweek == "Saturday" and not gametimeweek == "Sunday":
            if not hero_wear == "school":
                show bg_0
                with dissolve
                show HERO at OL
                $ hero_wear = "school"
                hide bg_0
                with Dissolve(2)
                show HERO at LC_slow
            hero "Let's go to school."
            wsis "Hurry up then!"
            scene bg_0
            with Dissolve(1)
            call action_walk(a="hero", b="wsis", c=20) from _call_action_walk
            $ StartAct("wsis", (("moving", "school"), 20), True)
            $ Set_CharMap("wsis", "school", "facade")
            $ Set_CharMap("hero", "school", "facade")
            $ gametimemin += 20

            jump schoolday_1_0

        "Go home together" if gametimehour == 12 and Check_CharInMap("hero", "school") and Check_CharSameMap("hero", "wsis"): # She waits at school 12:00-12:59
            jump wsis_interact_hangout_gohome

        "Invite to watch TV" if is_specialevent == False and Check_CharInMap("wsis", "home") and not Get_ActivityName("wsis") in ["watching tv"]:
                $ hero_mood = "A1"
                $ wnei_mood = "A3"
                $ wsis_mood = "O1"
                hero "Let's watch TV!"

                if wnei_quest_1 == 0 and Check_CharInMap("wnei", "home"):
                    $ add_stat("wsis", "love", 1)
                    $ add_stat("hero", "cha_soc", 1)
                    wsis "I{w=[wt1]}-it's {b}NOT{/b} cos you're inviting me!{w=[wt2]} but cos {bt}I want to{/bt},{w=[wt1]} got it?"
                    show WNEI at OL
                    show WNEI at CC_slow
                    wnei "Cmon!!!{w=[wt3]} I'll show you the best cartoon channel!"

                    jump wnei_quest_0_0

                else:
                    wsis "There's nothing interesting on TV."
                    jump wsis_interact_check

        "Invite to the grocery store" if ((gametimehour >= 13 and gametimehour < 18 and is_specialevent == True) or (gametimehour >= 13 and gametimehour <= 20 and is_specialevent == False)) and not Check_CharInMap("wsis", "school"):
            if (hero_quest_1 == 2 and is_specialevent == True):
                jump scenestep_0_2

            else:
                hero "Let's get some goodies at the grocery!"

                if "HangOut_Groceries" in wsis_know:
                    $ wsis_mood = "O1"
                    wsis "Hmph{w=[wt2]}, we already went today.{w=[wt3]} Go alone!"
                    jump wsis_interact_check

                else:
                    $ wsis_mood = "O1"
                    if wsis_quest_2 >= 1:
                        wsis "Sure, [C_Nam][wsis_to_hero][C_Off].{w=[wt2]} Just let me change my clothes first, okay?"
                    else:
                        wsis "Hmph{w=[wt2]}, what can you do without me?{w=[wt4]} {bt}Fine... Fine...{/bt}{w=[wt2]} I'll just change my clothes."

                    $ hero_mood = "A2"
                    hero "You're fine,{w=[wt1]} come on!"

                    $ wsis_mood = "O2"
                    if wsis_quest_2 >= 1:
                        wsis "No way!{w=[wt1]} I'm not going out dressed like this.{w=[wt2]} Just wait a moment."
                    else:
                        wsis "Shut up, moron!{w=[wt1]} I won't go out dressed like this."
                    if wsis_map == "Home - Step-sis' bedroom":
                        window hide
                        $ hero_mood = "O1"
                        $ wsis_mood = "O2"
                        show HERO at MoveOUT_L
                        show WSIS at LC
                        with ease
                        wsis "{bt}Shoo!{w=[wt1]} Shoo!{w=[wt1]} Hurry!!!{/bt}"
                        $ hero_map = "Home - Hallway"
                        play SE1 "DoorBam.ogg"

                        show WSIS at LC
                        $ wsis_mood = "A2"
                        $ wsis_fx = "1"
                        with Dissolve(1)
                        pause(1)

                    else:
                        show WSIS at MoveOUT_L
                        pause 1

                    stop BGM fadeout 3
                    scene bg_0
                    with Dissolve(1)
                    scene action_walk_bg street
                    show action_walk_hero_body 1
                    show action_walk_hero_wear 1home
                    if wsis_inti < 10:
                        show action_walk_wsis_body 1
                        show action_walk_wsis_wear 1casual
                    else:
                        show action_walk_wsis_body 2
                        show action_walk_wsis_wear 2casual
                    with Dissolve(2)
                    pause
                    scene bg_0
                    with Dissolve(1)
                    jump wsis_grocerystore

        "Return":
            jump wsis_interact

# ----------------------------------------------------------------------------------------------------
# Interact Chat
# ----------------------------------------------------------------------------------------------------
label wsis_interact_chat:
    menu:
        "Ask how she is" if not "Talk_How" in wsis_know:
            # ----------------------------------------------------------------------------------------------------
            # Asking at early morning
            # ----------------------------------------------------------------------------------------------------
            if gametimehour <= 7:

                hero "Did you sleep well?"

                # ----------------------------------------------------------------------------------------------------
                # WSIS is sick
                # ----------------------------------------------------------------------------------------------------
                if "WSIS_is_sick" in wsis_know:
                    wsis "I don't feel very well today..."
                    hero "{aw}Ehh!?...{/aw}{w=[wt2]} what are you feeling?"
                    wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I think I got a cold..."
                    hero "You need to rest!"
                    wsis "Oh{w=[wt1]}, you don't say...?"

                # ----------------------------------------------------------------------------------------------------
                # HERO and WSIS slept together
                # ----------------------------------------------------------------------------------------------------
                elif "wsis_quest_???" in wsis_know:
                    wsis "M{w=[wt1]}-mhm."

                # ----------------------------------------------------------------------------------------------------
                # HERO helped her on previous night
                # ----------------------------------------------------------------------------------------------------
                elif "WSIS_Quest_1_1" in wsis_know:
                    $ wsis_know.remove("WSIS_Quest_1_1")
                    wsis "S{w=[wt1]}-sure{w=[wt2]}, I'm fine now.{w=[wt2]} T{w=[wt1]}-Thanks."
                    hero "My pleasure.{w=[wt2]} I'm glad to know that!"

                # ----------------------------------------------------------------------------------------------------
                # Common
                # ----------------------------------------------------------------------------------------------------
                else:
                    if wsis_love < 20:
                        if wsis_quest_2 >= 1:
                            wsis "Yeah, I slept fine.{w=[wt2]} Thanks for asking."
                        else:
                            wsis "Of course, moron.{w=[wt2]} Now stop bothering me!"
                    elif wsis_love < 40:
                        wsis "Sure{w=[wt2]}, thanks"
                    elif wsis_love < 60:
                        wsis "Sure.{w=[wt2]} What about you?"
                        hero "Me too. Thanks!"
                        if wsis_quest_2 >= 1:
                            wsis "That's good to hear."
                        else:
                            wsis "Then{w=[wt1]}, shut up and stop bothering me!"
                    elif wsis_love >= 60:
                        wsis "M{w=[wt1]}-mhm! A{w=[wt1]}-and you?"
                        hero "Me too.{w=[wt2]} Thanks!"

            # ----------------------------------------------------------------------------------------------------
            # Asking after afternoon
            # ----------------------------------------------------------------------------------------------------
            elif gametimehour >= 17:

                # ----------------------------------------------------------------------------------------------------
                # HERO gave WSIS tutoring lessons
                # ----------------------------------------------------------------------------------------------------
                if "HangOut_Swim_Day" in wsis_know:
                    $ wsis_know.remove("HangOut_Swim_Day")
                    $ wsis_know.append("HangOut_Swim")
                    $ add_stat("wsis", "love", 1)
                    $ add_stat("hero", "cha_soc", 1)
                    if perk_cha_sex >= 1:
                        $ add_stat("wsis", "lust", 0.5)

                    hero "Did you enjoy swimming today?"
                    wsis "Eh{w=[wt1]}, it was n{w=[wt1]}-not so bad."
                    hero "You get the hang of things pretty fast.{w=[wt3]} Anyway{w=[wt2]}, you know you can count on me whenever you need me."
                    if wsis_quest_2 >= 1:
                        wsis "Thanks, [C_Nam][wsis_to_hero][C_Off].{w=[wt2]} I appreciate it."
                    else:
                        wsis "Hunf!{w=[wt2]} Don't be so full of yourself moron!"

                else:
                    hero "Hey{w=[wt2]}, how was your day?"
                    wsis "Nothing interesting..."

            # ----------------------------------------------------------------------------------------------------
            # Asking at any other time
            # ----------------------------------------------------------------------------------------------------
            else:
                hero "How are you today?"
                if wsis_love < 20:
                    wsis "Fine."
                elif wsis_love < 40:
                    wsis "Fine{w=[wt1]}, thanks."
                elif wsis_love < 60:
                    wsis "I'm fine{w=[wt1]}, and you?"
                    hero "Me too.{w=[wt2]} Thanks!"
                elif wsis_love >= 60:
                    wsis "F{w=[wt1]}-fine! A{w=[wt1]}-and you?"
                    hero "Me too.{w=[wt2]} Thanks!"

            $ wsis_know.append("Talk")
            $ wsis_know.append("Talk_How")
            $ add_stat("wsis", "love", 0.5)
            $ add_stat("hero", "cha_soc", 0.5)

        "Ask about her hobbies" if not "Talk_Hobbie" in wsis_know:
            hero "So{w=[wt1]}, what kind of things do you usually do?"

            $ a_event_0 = renpy.random.random()

            if renpy.random.random() > 0.75 and "WSIS_Y_Act_Videogame" in hero_know:
                wsis "N{w=[wt1]}-nothing interesting...{w=[wt2]} J{w=[wt1]}-just playing games on pc..."
                $ hero_mood = "A3"
                hero "Cool!{w=[wt2]} You could show me some cool games to play, [C_Nam][hero_to_wsis][C_Off]!"
                $ wsis_fx = "1"
                if wsis_quest_2 >= 1:
                    wsis "W{w=[wt1]}-well{w=[wt2]}, maybe sometime{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} If you're interested."
                else:
                    wsis "{aw}A{w=[wt1]}-As if I'm gonna l{w=[wt1]}-let you use my PC, moron!{/aw}"
            elif renpy.random.random() > 0.5 and "WSIS_Y_Act_Draw" in hero_know:
                wsis "W{w=[wt1]}-well{w=[wt2]}, I usually spend time drawing when I have nothing to do."
                hero "We should draw together more often."
                $ wsis_fx = "1"
                if wsis_quest_2 >= 1:
                    wsis "Y{w=[wt1]}-yeah{w=[wt2]}, maybe we could do that sometime."
                    hero "That'd be great! I'd love to see more of your work."
                    wsis "S{w=[wt1]}-sure."
                else:
                    wsis "Hunf! You are quite invasive, don't you think?"
                    hero "Stop being mean! I just like to spend time with you!"
                    wsis "Whatever."
            elif renpy.random.random() > 0.25 and "WSIS_Y_Act_Dance" in hero_know:
                $ wsis_fx = "1"
                wsis "W{w=[wt1]}-well{w=[wt2]}, you know{w=[wt1]}, I kinda like dancing sometimes."
                hero "Yeah{w=[wt1]}, it was very cool to see!"
                $ wsis_fx = "2"
                if wsis_quest_2 >= 1:
                    wsis "{aw}S{w=[wt1]}-stop it!{/aw}"
                    hero "Don't be shy!{w=[wt2]} You really have a knack for that."
                    wsis "{aw}Ok!{w=[wt1]} Ok!{w=[wt1]} I get it!{w=[wt1]} That's enough!{/aw}"
                else:
                    wsis "{aw}Shut up!{/aw}"
                    hero "Don't be shy!{w=[wt2]} You really have a knack for that."
                    wsis "{aw}Ok!{w=[wt1]} Ok!{w=[wt1]} I understood!{w=[wt1]} Now shut up!{/aw}"
            else:
                wsis "N{w=[wt1]}-nothing interesting...{w=[wt2]} J{w=[wt1]}-just watching TV..."
                $ hero_mood = "O1"
                hero "Really?...{w=[wt2]} Didn't you go out on this vacation?"
                wsis "No..."
                hero "Ehh!?..."
                wsis "I have no reasons to go out{w=[wt1]}, and I have a PC in my room!{w=[wt2]} That's all I need."
                $ hero_mood = "A3"
                hero "Oh...{w=[wt1]} Don't worry, [C_Nam][hero_to_wsis][C_Off]{w=[wt3]}, I must take you somewhere nice now that I'm here!"
                $ wsis_fx = "1"
                if wsis_quest_2 >= 1:
                    wsis "W{w=[wt1]}-well{w=[wt2]}, maybe{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} if you really want to."
                else:
                    wsis "{aw}A{w=[wt1]}-As if I wanna g{w=[wt1]}-go out with you, moron!{/aw}"

            $ wsis_know.append("Talk_Hobbie")
            $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] talked about her hobbies"))
            $ add_stat("wsis", "inti", 1)
            $ add_stat("wsis", "love", 1)
            $ add_stat("hero", "cha_soc", 1)

        "Compliment" if not "Compliment" in wsis_know:
            label wsis_interact_chat_compliment:
                pass
            menu:
                "Personality" if "Talk" in wsis_know:
                    menu:
                        "Aggressive/Combative":
                            $ wsis_know.append("HERO_Y_Girl_Data_Personality_4")
                            hero "You know{w=[wt2]}, I kinda like that strong personality of yours."
                        "Friendly/Lovely" if wsis_love >= 60:
                            $ wsis_know.append("HERO_Y_Girl_Data_Personality_3")
                            hero "I know that behind that mask you are a very caring person.{w=[wt2]} I like this side of yours.{w=[wt2]} It's cute!"
                        "Diligent" if hero_quest_1 >= 3:
                            $ wsis_know.append("HERO_Y_Girl_Data_Personality_11")
                            hero "When we were at the convenience store{w=[wt1]}, I noticed that you were very mindful and thorough in considering what the best options would be for [C_Nam][hero_about_wmom][C_Off] and [C_Nam][fnamewnei][C_Off].{w=[wt2]} That's really nice of you!"
                        "Timid/Shy" if wsis_inti > 10:
                            $ wsis_know.append("HERO_Y_Girl_Data_Personality_6")
                            hero "You know{w=[wt2]}, I think this shy way of yours is very cute."
                        "Chaste/Decent" if wsis_inti > 10:
                            $ wsis_know.append("HERO_Y_Girl_Data_Personality_8")
                            hero "You know{w=[wt2]}, I think decent women like you are kind of in short supply these days.{w=[wt2]} I'm glad you're like that."

                            $ wsis_mood = "O2"
                            wsis "{aw}Ehhh!?{/aw}{w=[wt2]} W{w=[wt1]}-what makes you think that about me?"
                            menu:
                                "She seems reserved":
                                    hero "W{w=[wt1]}-well{w=[wt2]}, C{w=[wt1]}-cos you seems to be very reserved sometimes.{w=[wt2]} {gg}He-He...{/gg}"
                                "She wear modest panties":
                                    hero "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} It's just that women your age generally wear sexier panties{w=[wt2]}, and you still wear cute ones."
                                    $ add_stat("wsis", "love", 1)
                                    $ add_stat("wsis", "lust", 1)
                                    $ add_stat("hero", "cha_soc", 1)
                                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off]'s  lust {color=#32FF32}+")+str(1 * lustadd_wsis)[:4])
                                    $ a_event_0 = 2
                                    call wsis_reaction from _call_wsis_reaction_2
                        "Return":
                            jump wsis_interact_chat_compliment

                    $ add_stat("wsis", "love", 2)
                    $ add_stat("hero", "cha_soc", 2)

                    $ wsis_mood = "O2"
                    $ wsis_fx = 1
                    if wsis_quest_2 >= 1:
                        wsis "W{w=[wt1]}-What's with the sudden compliment!?{w=[wt2]} You're embarrassing me."
                        $ hero_mood = "A1"
                        hero "I just wanted to let you know!"
                        wsis "W{w=[wt1]}-well{w=[wt2]}, thanks{w=[wt1]}, I guess."
                    else:
                        wsis "W{w=[wt1]}-What is that out of the blue!?{w=[wt2]} Has your stupidity already started to get out of control or what?"
                        $ hero_mood = "O1"
                        hero "{aw}Ehhh...?{/aw}{w=[wt2]} Stop being mean!"
                        wsis "What can I do?{w=[wt2]} Sometimes you just seem too idiot!"

                "Attributes" if wsis_inti > 999:
                    menu:
                        "Intelligence":
                            jump wsis_interact_chat_compliment
                        "Drawing skill" if "WSIS_Y_Act_Draw" in hero_know:
                            jump wsis_interact_chat_compliment
                        "Dancing skill" if "WSIS_Y_Act_Dance" in hero_know:
                            jump wsis_interact_chat_compliment
                        "Return":
                            jump wsis_interact_chat_compliment

                    $ add_stat("wsis", "love", 2)
                    $ add_stat("hero", "cha_soc", 2)

                "Sexual appearance":
                    menu:
                        "Butt":
                            $ wsis_know.append("HERO_Y_Girl_Data_Butt_4")
                            hero "Hey [C_Nam][hero_to_wsis][C_Off]{w=[wt2]}, you got a pretty hot big ass, huh?"
                        "Breasts":
                            $ wsis_know.append("HERO_Y_Girl_Data_Breast_1")
                            hero "Hey [C_Nam][hero_to_wsis][C_Off]{w=[wt2]}, you got nice tits, huh?"
                        "Return":
                            jump wsis_interact_chat_compliment

                    $ add_stat("wsis", "lust", 2)
                    $ add_stat("hero", "cha_soc", 2)

                    if wsis_inti >= min(80, wsis_inti_cap) + (personality[1]*0.1):
                        $ wsis_fx = "1"
                        wsis "{aw}S{w=[wt1]}-s{w=[wt1]}-stop harassing me{w=[wt1]}, you p{w=[wt1]}-pervert!!!{/aw}"
                        hero "It's not that.{w=[wt2]} I just wanted to compliment your beauty!"
                        $ wsis_fx = "2"
                        if wsis_quest_2 >= 1:
                            wsis "{aw}O{w=[wt1]}-ok{w=[wt2]}, g{w=[wt1]}-g{w=[wt1]}-got it!{/aw}{w=[wt3]} Just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} don't say things like that so suddenly!"
                        else:
                            wsis "{aw}O{w=[wt1]}-ok{w=[wt2]}, g{w=[wt1]}-g{w=[wt1]}-got it!{/aw}{w=[wt3]} {pa}NOW{w=[wt1]} S{w=[wt1]}-SHUT UP!!!{/pa}"

                    else:
                        $ wsis_fx = "2"
                        $ wsis_mood = "O4"
                        wsis "{pa}WHAT DID YOU JUST SAY!?{/pa}"
                        $ hero_mood = "O1"
                        hero "I{w=[wt1]}-I j{w=[wt1]}-just wanted to compliment your beauty!"
                        $ a_event_0 = 3
                        call wsis_reaction from _call_wsis_reaction_3

                "Beauty appearance":
                    menu:
                        "Hairstyle":
                            hero "I like your hair.{w=[wt2]} It looks very cool!"

                        "Face":
                            hero "You know{w=[wt2]}, You got very beautiful{w=[wt2]}, [C_Nam][hero_to_wsis][C_Off]!"

                        "Return":
                            jump wsis_interact_chat_compliment

                    $ add_stat("wsis", "love", 2)
                    $ add_stat("hero", "cha_soc", 2)

                    $ wsis_fx = "1"
                    if wsis_quest_2 >= 1:
                        wsis "{aw}W{w=[wt1]}-where is that coming from so suddenly!?{/aw}"
                        hero "I just wanted to let you know!"
                        $ wsis_fx = "2"
                        wsis "{aw}W{w=[wt1]}-well{w=[wt2]}, t{w=[wt1]}-thanks{w=[wt1]}, I guess{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}{/aw}"
                    else:
                        wsis "{aw}W{w=[wt1]}-where is that coming from so suddenly!?{w=[wt2]}{pr}It's not like I enjoy getting your compliments or anything, idiot!{/aw}"
                        hero "Huh?...{w=[wt2]} It's not that...{w=[wt2]} It's just that it fits you really well!"
                        $ wsis_fx = "2"
                        wsis "{aw}O{w=[wt1]}-ok{w=[wt1]}-k{w=[wt2]},{/aw} {aw}I g{w=[wt1]}-g{w=[wt1]}-got it!{/aw}{w=[wt3]} {aw}NOW{w=[wt1]} {b}S{w=[wt1]}-SHUT UP!!!{/b}{/aw}"

                "Return":
                    jump wsis_interact_chat

            $ wsis_know.append("Compliment")

        "Talk about someone":
            menu:
                "{image=icon_wmom} [C_Nam][fnamewmom][C_Off]" if not "Talk_Char_WMOM" in wsis_know:
                    $ wsis_know.append("Talk_Char_WMOM")

                    $ a_event_0 = renpy.random.random()

                    # 25% chance to ask about WMOM's wellbeing (5/20 slots)
                    if a_event_0 < 5/20:
                        $ hero_mood = "A2"
                        hero "How is [C_Nam][hero_to_wmom][C_Off] doing?"

                        if wsis_quest_2 < 1: # Hostile tone
                            $ wsis_mood = "A1"
                            wsis "She's fine{w=[wt1]}, I guess.{w=[wt2]} Why are you asking me?"
                            hero "Just wondering."
                            wsis "Whatever."
                        else: # Friendly tone
                            $ wsis_mood = "A2"
                            if a_event_0 < 1/20:
                                $ wsis_fx = 1
                                wsis "Mom's been working really hard lately{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She comes home exhausted every day."
                                $ hero_mood = "O1"
                                hero "Is she okay?"
                                wsis "Y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She says she's fine{w=[wt2]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I worry sometimes{w=[wt1]}, you know?"
                            elif a_event_0 < 2/20:
                                $ wsis_fx = 1
                                wsis "She's been working really long hours{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Sometimes she doesn't get home until late."
                                hero "That must be tough on her."
                                wsis "Y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I wish I could help more."
                            elif a_event_0 < 3/20:
                                wsis "Mom's doing okay.{w=[wt2]} She's always busy with work{w=[wt2]}, but she seems happy when she's home."
                                $ hero_mood = "A2"
                                hero "That's good to hear."
                                $ wsis_fx = 1
                                wsis "Y{w=[wt1]}-yeah."
                            elif a_event_0 < 4/20:
                                $ wsis_fx = 1
                                wsis "She's been really stressed with work lately."
                                $ hero_mood = "O1"
                                hero "Should we do something to help her relax?"
                                $ wsis_fx = 2
                                $ wsis_mood = "A2"
                                wsis "T{w=[wt1]}-that would be nice."
                            else: # 4/20 to 5/20
                                wsis "Mom seems to be doing well.{w=[wt2]} She's always cheerful even when she's tired."
                                $ hero_mood = "A2"
                                hero "She's really strong."
                                $ wsis_fx = 1
                                wsis "Yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She really is."

                    # 75% chance for WSIS's relationship with WMOM (15/20 slots)
                    else:
                        $ hero_mood = "A2"
                        hero "What do you think about [C_Nam][hero_about_wmom][C_Off]?"

                        $ wsis_mood = "A2"

                        if wsis_quest_2 < 1: # Hostile tone
                            if a_event_0 < 7/20:
                                wsis "She's fine.{w=[wt2]} Why do you care what I think?"
                            elif a_event_0 < 9/20:
                                wsis "Mom is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Mom.{w=[wt2]} That's all."
                                hero "That's it?"
                                wsis "What else do you want me to say?{w=[wt2]} Stop interrogating me!"
                            elif a_event_0 < 11/20:
                                wsis "She's good to me.{w=[wt2]} Now stop asking weird questions!"
                            elif a_event_0 < 13/20:
                                wsis "Why are you asking about her?{w=[wt2]} Just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} leave me alone!"
                            else: # 13/20 to 15/20
                                wsis "She takes care of me.{w=[wt2]} That's all you need to know."

                        else: # Friendly, more open
                            if a_event_0 < 7/20:
                                $ wsis_fx = 1
                                wsis "Mom is the best!{w=[wt2]} She's always so caring and works so hard for us."
                                $ hero_mood = "A2"
                                hero "Yeah, she really is amazing."
                                $ wsis_fx = 2
                                wsis "I really appreciate everything she does{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Sometimes I wish I could help her more."
                            elif a_event_0 < 9/20:
                                $ wsis_fx = 1
                                wsis "After the divorce{w=[wt1]}, Mom worked so hard to take care of me."
                                $ hero_mood = "A1"
                                hero "That must have been difficult."
                                $ wsis_mood = "A2"
                                wsis "There were times when things were really tough{w=[wt2]}, but she never complained.{w=[wt2]} She just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} kept going."
                                $ hero_mood = "A2"
                                hero "That's really admirable."
                                $ wsis_fx = 2
                                wsis "Y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She's my role model{w=[wt1]}, honestly."
                            elif a_event_0 < 11/20:
                                wsis "I wish I could be as strong as Mom someday."
                                $ hero_mood = "A2"
                                hero "You're plenty strong already, [C_Nam][hero_to_wsis][C_Off]."
                                $ wsis_fx = 1
                                wsis "{aw}S{w=[wt1]}-stop saying embarrassing things!{/aw}"
                            elif a_event_0 < 13/20:
                                wsis "Sometimes I worry Mom is working too hard{w=[wt1]}, you know?"
                                $ hero_mood = "O1"
                                hero "Yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I've noticed that too."
                                $ wsis_fx = 1
                                wsis "We should{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} try to help her out more when we can."
                            else: # 13/20 to 15/20
                                wsis "I'm really grateful we have Mom in our lives."
                                $ hero_mood = "A2"
                                hero "Me too."
                                $ wsis_fx = 1
                                $ wsis_mood = "A2"
                                wsis "She's been through so much{w=[wt2]}, but she never gave up on us."

                    $ add_stat("wsis", "inti", 0.2)

                "{image=icon_wnei} [C_Nam][fnamewnei][C_Off]" if not "Talk_Char_WNEI" in wsis_know:
                    $ wsis_know.append("Talk_Char_WNEI")
                    $ hero_mood = "A2"
                    hero "What do you think about [C_Nam][fnamewnei][C_Off]?"

                    $ a_event_0 = renpy.random.random()
                    $ wsis_mood = "A2"

                    if wsis_quest_2 < 1: # Hostile tone
                        if a_event_0 < 1/5:
                            $ wsis_fx = 1
                            wsis "She's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} nice.{w=[wt2]} Why are you asking?"
                            hero "Just curious."
                            wsis "Whatever."
                        elif a_event_0 < 2/5:
                            wsis "We get along fine.{w=[wt2]} Now stop asking about everyone!"
                        elif a_event_0 < 3/5:
                            wsis "She comes over sometimes.{w=[wt2]} That's all you need to know."
                        elif a_event_0 < 4/5:
                            wsis "Why do you care about my friendships?{w=[wt2]} Stop being nosy!"
                        else:
                            $ wsis_fx = 1
                            wsis "She's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} my best friend.{w=[wt2]} Don't make it weird."

                    else: # Friendly, open about best friend
                        if a_event_0 < 1/5:
                            $ wsis_fx = 1
                            wsis "[C_Nam][fnamewnei][C_Off] is my best friend!{w=[wt2]} She's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} the only person who doesn't judge me{w=[wt1]}, you know?"
                            $ hero_mood = "A2"
                            hero "That's really special."
                            $ wsis_fx = 2
                            $ wsis_mood = "A2"
                            wsis "Y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She really likes me for who I am."
                        elif a_event_0 < 2/5:
                            $ wsis_fx = 1
                            wsis "She comes over every Saturday and stays until Sunday.{w=[wt2]} We have our girl's night on Saturday!"
                            $ hero_mood = "A2"
                            hero "Girl's night?"
                            $ wsis_fx = 2
                            $ wsis_mood = "A2"
                            wsis "Y{w=[wt1]}-yeah!{w=[wt2]} We play games{w=[wt2]}, watch movies{w=[wt2]}, eat snacks{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} It's really fun!"
                            if wsis_quest_2 >= 1:
                                wsis "Maybe{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} you could join us sometime{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} if you want."
                                $ hero_mood = "A3"
                                hero "Really? That'd be great!"
                                $ wsis_fx = 2
                                wsis "{aw}D{w=[wt1]}-don't get too excited!{/aw}{w=[wt2]} I said {i}maybe{/i}!"
                        elif a_event_0 < 3/5:
                            wsis "[C_Nam][fnamewnei][C_Off] is the only friend who truly understands me."
                            $ hero_mood = "A2"
                            hero "She seems really loyal to you."
                            $ wsis_fx = 1
                            $ wsis_mood = "A2"
                            wsis "Yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She's never judged me for being{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} the way I am."
                            wsis "Everyone else at school thinks I'm weird or aggressive{w=[wt2]}, but she just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} accepts me."
                        elif a_event_0 < 4/5:
                            $ wsis_fx = 1
                            wsis "We've been doing our weekend sleepovers for a while now.{w=[wt2]} It's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} something I really look forward to."
                            $ hero_mood = "A2"
                            hero "What do you two usually do?"
                            $ wsis_mood = "A2"
                            wsis "We talk about everything{w=[wt2]}, play games{w=[wt2]}, watch movies{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} It's nice to have someone to spend time with like that."
                        else:
                            $ wsis_fx = 1
                            wsis "I'm really grateful for [C_Nam][fnamewnei][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She's the best friend I could ask for."
                            $ hero_mood = "A2"
                            hero "You two seem really close."
                            $ wsis_fx = 2
                            $ wsis_mood = "A2"
                            wsis "Y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} really special to me."

                    $ add_stat("wsis", "inti", 0.2)

                "{image=icon_wcou} [C_Nam][fnamewcou][C_Off]" if not "Talk_Char_WCOU" in wsis_know:
                    $ wsis_know.append("Talk_Char_WCOU")
                    $ hero_mood = "A2"
                    hero "What do you think about [C_Nam][fnamewcou][C_Off]?"

                    $ a_event_0 = renpy.random.random()
                    $ wsis_mood = "A1"

                    if wsis_quest_2 < 1: # Hostile tone
                        if a_event_0 < 1/5:
                            wsis "She's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} fine.{w=[wt2]} Why?"
                            hero "Just asking."
                            wsis "Whatever."
                        elif a_event_0 < 2/5:
                            wsis "She's smart{w=[wt1]}, I guess.{w=[wt2]} Stop asking about everyone!"
                        elif a_event_0 < 3/5:
                            wsis "She's family.{w=[wt2]} That's it."
                        elif a_event_0 < 4/5:
                            $ wsis_fx = 1
                            wsis "She's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} weird sometimes{w=[wt1]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} whatever."
                        else:
                            wsis "Why do you care?{w=[wt2]} She's just our cousin."

                    else: # Friendly, more details
                        if a_event_0 < 1/5:
                            $ wsis_fx = 1
                            wsis "[C_Nam][fnamewcou][C_Off] is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} really smart.{w=[wt2]} Like{w=[wt1]}, genius-level smart."
                            $ hero_mood = "A2"
                            hero "You admire her?"
                            $ wsis_mood = "A2"
                            wsis "Y{w=[wt1]}-yeah{w=[wt2]}, I do{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She's accomplished so much."
                            $ wsis_fx = 2
                            $ wsis_mood = "A1"
                            wsis "But{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} she's also{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} kind of strange in some ways."
                        elif a_event_0 < 2/5:
                            $ wsis_fx = 1
                            wsis "She's very competent{w=[wt2]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I don't really feel comfortable around her sometimes."
                            $ hero_mood = "A1"
                            hero "Why not?"
                            $ wsis_fx = 2
                            wsis "She's just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} too open about certain things{w=[wt1]}, you know?{w=[wt2]} Too{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} sensual and free."
                            wsis "Meanwhile I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} not like that at all."
                        elif a_event_0 < 3/5:
                            wsis "Sometimes I go to [C_Nam][fnamewcou][C_Off] when I'm not feeling well.{w=[wt2]} She's really good at taking care of people."
                            $ hero_mood = "A2"
                            hero "That's good to know."
                            $ wsis_fx = 1
                            $ wsis_mood = "A1"
                            wsis "But{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} there's something{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} off about her sometimes."
                            hero "Off how?"
                            $ wsis_fx = 2
                            wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I don't know how to explain it{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} be careful around her{w=[wt1]}, okay?"
                        elif a_event_0 < 4/5:
                            $ wsis_fx = 1
                            wsis "[C_Nam][fnamewcou][C_Off] is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I admire her intelligence{w=[wt2]}, but she can be really weird about things."
                            $ hero_mood = "A1"
                            hero "Weird how?"
                            $ wsis_fx = 2
                            $ wsis_mood = "A1"
                            wsis "The way she talks{w=[wt2]}, the way she looks at people{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} It's like."
                            wsis "Like she's analyzing you{w=[wt2]}, studying you{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} It makes me uncomfortable."
                        else:
                            $ wsis_fx = 1
                            $ wsis_mood = "O1"
                            wsis "I think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} [C_Nam][fnamewcou][C_Off] might not be entirely{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} normal."
                            $ hero_mood = "A1"
                            hero "What do you mean?"
                            $ wsis_fx = 2
                            wsis "I don't know{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Sometimes the way she acts{w=[wt2]}, it's like{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} she doesn't feel things the same way other people do."
                            wsis "Just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} watch yourself around her{w=[wt1]}, okay?"
                            mind "(What is she trying to tell me{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}?)"

                    $ add_stat("wsis", "inti", 0.2)

                "{image=icon_wgma} [C_Nam][fnamewgma][C_Off]" if not "Talk_Char_WGMA" in wsis_know:
                    $ wsis_know.append("Talk_Char_WGMA")
                    $ hero_mood = "A2"
                    hero "What do you think about [C_Nam][fnamewgma][C_Off]?"

                    $ a_event_0 = renpy.random.random()
                    $ wsis_mood = "A1"

                    if wsis_quest_2 < 1: # Hostile tone
                        if a_event_0 < 1/5:
                            wsis "She's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} our grandmother.{w=[wt2]} What else?"
                        elif a_event_0 < 2/5:
                            wsis "She's fine.{w=[wt2]} Why are you asking?"
                            hero "Just curious."
                            wsis "Whatever."
                        elif a_event_0 < 3/5:
                            wsis "She can be{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} difficult.{w=[wt2]} That's all I'll say."
                        elif a_event_0 < 4/5:
                            wsis "Stop asking about everyone!{w=[wt2]} She's just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} grandma."
                        else:
                            $ wsis_fx = 1
                            wsis "She's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} not easy to deal with sometimes."

                    else: # Friendly, honest about difficulties
                        if a_event_0 < 1/5:
                            $ wsis_fx = 1
                            $ wsis_mood = "A2"
                            wsis "I love [C_Nam][fnamewgma][C_Off]{w=[wt2]}, I really do{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} But she's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} not exactly easy to deal with."
                            $ hero_mood = "A1"
                            hero "What do you mean?"
                            $ wsis_fx = 2
                            $ wsis_mood = "O1"
                            wsis "She says the most{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} inappropriate things sometimes!{w=[wt2]} Like{w=[wt2]}, {i}really{/i} inappropriate."
                            wsis "It's so embarrassing."
                        elif a_event_0 < 2/5:
                            $ wsis_fx = 1
                            wsis "When things got tough after the divorce{w=[wt2]}, I spent a lot of time at [C_Nam][fnamewgma][C_Off]'s place."
                            $ hero_mood = "A2"
                            hero "That must have been nice."
                            $ wsis_mood = "A2"
                            wsis "It was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She always knew how to cheer me up{w=[wt1]}, even if."
                            $ wsis_fx = 2
                            $ wsis_mood = "O1"
                            wsis "Even if she said really weird and perverted stuff sometimes."
                        elif a_event_0 < 3/5:
                            $ wsis_mood = "A2"
                            wsis "[C_Nam][fnamewgma][C_Off] makes the {sc=1}{b}best{/b}{/sc} cookies!{w=[wt2]} That's one thing I'll always treasure about her."
                            $ hero_mood = "A3"
                            hero "Maybe I should ask her for the recipe!"
                            $ wsis_fx = 1
                            $ wsis_mood = "O1"
                            wsis "{aw}N{w=[wt1]}-no way!{/aw}{w=[wt2]} First{w=[wt2]}, it's a family secret.{w=[wt2]} Second{w=[wt2]}, you'll have to listen to her{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} stories."
                            hero "Stories?"
                            $ wsis_fx = 2
                            wsis "Trust me{w=[wt2]}, you don't want to know."
                        elif a_event_0 < 4/5:
                            $ wsis_fx = 1
                            wsis "I respect [C_Nam][fnamewgma][C_Off] a lot{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She's been through so much and raised Mom and [C_Nam][fnamewcou][C_Off]'s mother."
                            $ hero_mood = "A2"
                            hero "She sounds strong."
                            $ wsis_fx = 2
                            $ wsis_mood = "O1"
                            wsis "She is{w=[wt2]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} she has absolutely {sc=1}{b}no{/b}{/sc} filter!{w=[wt2]} She'll say anything that comes to mind."
                            wsis "It's really embarrassing sometimes."
                        else:
                            $ wsis_mood = "A2"
                            wsis "I treasure the memories I have with [C_Nam][fnamewgma][C_Off]."
                            $ hero_mood = "A2"
                            hero "That's sweet."
                            $ wsis_fx = 1
                            $ wsis_mood = "A1"
                            wsis "But{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} visiting her can be{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} exhausting.{w=[wt2]} She's not easy to keep up with."

                    $ add_stat("wsis", "inti", 0.2)

                "{image=icon_wgal} [C_Nam][fnamewgal][C_Off] & {image=icon_hriv} [C_Nam][fnamehriv][C_Off]" if "WSIS_BG_WGAL_2" in hero_know and "WSIS_BG_HRIV_2" in hero_know:
                        if not "WSIS_BG_FRIENEMIES" in hero_know:
                            $ hero_mood = "A2"
                            hero "Sorry for asking{w=[wt2]}, but what exactly made you, [C_Nam][fnamewgal][C_Off], and [C_Nam][fnamehriv][C_Off] hate each other so much?"

                            if not (wsis_inti >= min(30, wsis_inti_cap)) or not (wsis_love >= 40):
                                $ wsis_mood = "O1"
                                wsis "Nothing{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I still don't feel ready to talk about the details."
                                if not (wsis_inti >= min(30, wsis_inti_cap)):
                                    mind "(She doesn't seem to feel close enough to me to have this kind of conversation.)"
                                elif not (wsis_love >= 40):
                                    mind "(She doesn't seem to like me enough to have this kind of conversation.)"

                            else:
                                label wsis_interact_chat_revelation_1:
                                    $ hero_know.append("WSIS_Revelation")
                                    $ msg.msg(renpy.translate_string("Character backstory revealed"))
                                    $ hero_know.append("WSIS_BG_FRIENEMIES")
                                    $ msg.msg(renpy.translate_string("You know [C_Nam][fnamewsis][C_Off] a little more"))
                                    $ add_stat("wsis", "inti", 1)

                                    $ wsis_mood = "O1"
                                    $ wsis_fx = 0
                                    wsis "Hmph...!{w=[wt3]} Okay.{w=[wt4]} I guess I'll tell you everything."
                                    $ hero_mood = "A2"
                                    hero "Only if you're comfortable."
                                    $ wsis_fx = 1
                                    $ wsis_mood = "O2"
                                    wsis "No{w=[wt2]}, I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I need to get this off my chest."
                                    wsis "{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}The three of us{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} me{w=[wt2]}, [C_Nam][fnamewgal][C_Off]{w=[wt2]}, and [C_Nam][fnamehriv][C_Off].{w=[wt3]} We used to be friends{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Close friends."
                                    $ hero_mood = "O1"
                                    hero "All three of you?"
                                    $ wsis_fx = 2
                                    $ wsis_mood = "O1"
                                    wsis "Y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} We hung out together{w=[wt2]}, studied together.{w=[wt3]} I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Back then{w=[wt2]}, [C_Nam][fnamehriv][C_Off] and [C_Nam][fnamewgal][C_Off] started dating.{w=[wt2]} They were going to the cinema together.{w=[wt3]} But on the day{w=[wt2]}, [C_Nam][fnamewgal][C_Off] got sick and couldn't go."
                                    $ hero_mood = "A1"
                                    hero "So{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}?"
                                    $ wsis_fx = 2
                                    $ wsis_mood = "O1"
                                    wsis "He asked me to go with him instead.{w=[wt3]} He said he'd already talked to [C_Nam][fnamewgal][C_Off] and that she was okay with it.{w=[wt3]} He insisted it would be just as friends{w=[wt2]}, nothing more.{w=[wt3]} And that he had already bought 2 tickets and didn't want to feel alone."
                                    wsis "He insisted so much{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I thought it wouldn't be a problem and went with him.{w=[wt2]} But during the movie{w=[wt2]}, he started flirting with me{w=[wt2]}, saying that I was the one he really loved and wanted to be with{w=[wt2]}, not [C_Nam][fnamewgal][C_Off]."
                                    $ hero_mood = "O2"
                                    wsis "I was already feeling bad for having gone.{w=[wt3]} I kept refusing his approaches{w=[wt2]}, over and over{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} But he kept insisting until I get up and leave the movie theater."
                                    wsis "But when I were leaving{w=[wt2]}, he{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} he got desperate.{w=[wt3]} He realized he wasn't going to get what he wanted{w=[wt2]}, so{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} he tried to force me!"
                                    $ hero_mood = "O3"
                                    hero "He {i}what{/i}!?"
                                    wsis "He grabbed me{w=[wt2]}, tried to kiss me{w=[wt2]}, tried to{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} touch me."
                                    $ hero_mood = "O3"
                                    hero "{pa}That bastard!{/pa}"
                                    $ wsis_fx = 2
                                    $ wsis_mood = "O2"
                                    wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I kicked him as hard as I could{w=[wt2]}, broke free{w=[wt2]}, and ran away."
                                    $ hero_mood = "O1"
                                    hero "Did he{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} did he hurt you?"
                                    $ wsis_mood = "O1"
                                    $ wsis_fx = 1
                                    wsis "No{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I got away before{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} before he could do anything worse.{w=[wt4]} Then started calling me a tease{w=[wt2]}, saying I led him on{w=[wt2]}, that I was {i}asking for it{/i}"
                                    wsis "So{w=[wt2]}, that's when I saw his true side{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} The mask came off."
                                    $ hero_mood = "O1"
                                    hero "Did you tell anyone?"
                                    $ wsis_fx = 2
                                    $ wsis_mood = "O1"
                                    wsis "I told [C_Nam][fnamewgal][C_Off]{w=[wt2]}, but she blamed me{w=[wt2]}, and humiliated me in front of the class{w=[wt2]}, saying that I was the slut who hit on friends' boyfriends.{w=[wt3]} I beat her until she passed out."
                                    hero "After everything you had endured for her{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} It's sad that it ended like this."
                                    wsis "It didn't.{w=[wt3]} I beat her until she passed out.{w=[wt3]} So we're even now."
                                    hero "Oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I see..."
                                    wsis "Well{w=[wt2]}, girls started to avoid me after that.{w=[wt3]} And I started to disgust boys.{w=[wt3]} But I was too ashamed{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I thought{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} maybe it was my fault for going."
                                    $ hero_mood = "O1"
                                    hero "It wasn't your fault!{w=[wt2]} None of it was and you didn't deserve any of it!{w=[wt3]} People just think they can judge what they don't know."
                                    $ wsis_fx = 2
                                    wsis "That's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} The same thing [C_Nam][fnamewnei][C_Off] told me.{w=[wt2]} You are the only ones I can count.{w=[wt3]} Thank you."
                        else:
                            hero "Well{w=[wt2]}, sorry to bring this up again{w=[wt2]}, but could you explain the problem you had with [C_Nam][fnamewgal][C_Off] and [C_Nam][fnamehriv][C_Off] again?"
                            jump wsis_interact_chat_revelation_1

                "{image=icon_wgal} [C_Nam][fnamewgal][C_Off]" if not "Talk_Char_WGAL" in wsis_know and wgal_quest_1 == 1:
                    $ wsis_know.append("Talk_Char_WGAL")

                    if wsis_quest_2 < 1: # Hostile phase
                        $ hero_mood = "A2"
                        hero "What do you think about [C_Nam][fnamewgal][C_Off]?"
                        $ wsis_mood = "O2"
                        wsis "I don't want to talk about {i}her{/i}."
                        hero "Why not?"
                        wsis "Just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} drop it, okay?{w=[wt2]} I'm not in the mood!"

                    else: # Friendly phase
                        if not "WSIS_BG_WGAL_1" in hero_know:
                            $ hero_know.append("WSIS_BG_WGAL_1")
                            $ msg.msg(renpy.translate_string("You know [C_Nam][fnamewsis][C_Off] a little more"))
                            $ add_stat("wsis", "inti", 1)

                            $ hero_mood = "A1"
                            hero "I've noticed you and [C_Nam][fnamewgal][C_Off] don't seem to get along."
                            $ wsis_mood = "O2"
                            $ wsis_fx = 0
                            wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}We used to be friends.{w=[wt2]} {i}Used to{/i}."
                            hero "What happened?"
                            $ wsis_fx = 1
                            $ wsis_mood = "O3"
                            wsis "She showed her true colors{w=[wt1]}, that's what!{w=[wt2]} She turned out to be a fake{w=[wt2]}, two-faced."
                            $ hero_mood = "O1"
                            hero "That's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} harsh."
                            $ wsis_fx = 2
                            wsis "She {i}deserves{/i} it."

                        elif not "WSIS_BG_WGAL_2" in hero_know:
                            if not (wsis_inti >= min(20, wsis_inti_cap)) or not (wsis_love >= 25):
                                $ hero_mood = "A1"
                                hero "Can you tell me more about what happened with [C_Nam][fnamewgal][C_Off]?"
                                $ wsis_mood = "O1"
                                wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I don't really want to talk about it."
                                if not (wsis_inti >= min(20, wsis_inti_cap)):
                                    mind "(She doesn't seem to feel close enough to me to have this kind of conversation.)"
                                elif not (wsis_love >= 25):
                                    mind "(She doesn't seem to like me enough to have this kind of conversation.)"
                            else:
                                $ hero_know.append("WSIS_Revelation")
                                $ msg.msg(renpy.translate_string("Character backstory revealed"))
                                $ hero_know.append("WSIS_BG_WGAL_2")
                                $ msg.msg(renpy.translate_string("You know [C_Nam][fnamewsis][C_Off] a little more"))
                                $ add_stat("wsis", "inti", 1)

                                $ hero_mood = "A1"
                                hero "You said she showed her true colors{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} What happened?"
                                $ wsis_mood = "O1"
                                $ wsis_fx = 0
                                wsis "{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}We{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} We used to be close friends."
                                $ hero_mood = "O1"
                                hero "You and [C_Nam][fnamewgal][C_Off]?"
                                $ wsis_fx = 1
                                $ wsis_mood = "O2"
                                wsis "Y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} We spent a lot of time together{w=[wt2]}, shared secrets."
                                wsis "But then{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} something happened between us."
                                $ hero_mood = "A1"
                                hero "Something involving a guy?"
                                $ wsis_fx = 2
                                $ wsis_mood = "O3"
                                wsis "How did you{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Yes{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} There was a guy."
                                $ wsis_mood = "O2"
                                $ wsis_fx = 1
                                wsis "She liked him{w=[wt2]}, and{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} things got complicated."
                                wsis "She blamed me for something that wasn't my fault{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She refused to believe me."
                                wsis "And after that{w=[wt2]}, she started spreading rumors{w=[wt2]}, calling me a traitor."
                                $ hero_mood = "O1"
                                hero "That's terrible."
                                $ wsis_fx = 2
                                $ wsis_mood = "O1"
                                wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I don't want to give the details yet{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} It's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} too painful."
                                $ hero_mood = "A1"
                                hero "That's okay.{w=[wt2]} Take your time."
                                $ wsis_fx = 2
                                wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}Thanks."

                        else:
                            $ a_event_0 = renpy.random.random()
                            $ wsis_mood = "O2"

                            if a_event_0 < 1/3:
                                $ hero_mood = "A1"
                                hero "Still thinking about [C_Nam][fnamewgal][C_Off]?"
                                wsis "I hate that she gets to act like nothing happened."
                            elif a_event_0 < 2/3:
                                wsis "We'll never be friends again.{w=[wt2]} I'd rather die than trust her."
                            else:
                                wsis "She's a fake.{w=[wt2]} Everything about her is a lie."

                    $ add_stat("wsis", "inti", 0.2)

                "{image=icon_hriv} [C_Nam][fnamehriv][C_Off]" if not "Talk_Char_HRIV" in wsis_know and hriv_quest[0] == 1:
                    $ wsis_know.append("Talk_Char_HRIV")
                    $ hero_mood = "A2"
                    hero "What do you think about [C_Nam][fnamehriv][C_Off]?"

                    if wsis_quest_2 < 1: # Hostile phase
                        $ wsis_mood = "O2"
                        wsis "He's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Don't make me talk about him."
                        hero "Why?"
                        wsis "Just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} stop asking!"

                    else: # Friendly phase
                        if "WSIS_Revelation" in wsis_know:
                            call wsis_interact_revelation from _call_wsis_interact_revelation

                        elif not "WSIS_BG_HRIV_1" in hero_know:
                            $ hero_know.append("WSIS_Revelation")
                            $ msg.msg(renpy.translate_string("Character backstory revealed"))
                            $ hero_know.append("WSIS_BG_HRIV_1")
                            $ msg.msg(renpy.translate_string("You know [C_Nam][fnamewsis][C_Off] a little more"))
                            $ add_stat("wsis", "inti", 1)

                            $ wsis_mood = "O2"
                            $ wsis_fx = 0
                            wsis "[C_Nam][fnamehriv][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} He's the worst jerk in school."
                            $ hero_mood = "O1"
                            hero "Worse than [C_Nam][fnamehprv][C_Off]?"
                            $ wsis_fx = 1
                            $ wsis_mood = "O3"
                            wsis "Way worse!{w=[wt2]} [C_Nam][fnamehprv][C_Off] is just a fool who's obvious about what he is.{w=[wt3]} [C_Nam][fnamehriv][C_Off] is a real jerk{w=[wt2]} He {i}pretends{/i} to be a good guy{w=[wt2]}, but behind this mask hides someone egocentric and manipulative{w=[wt2]}, capable of using people as he sees fit."
                            $ hero_mood = "O1"
                            hero "Well{w=[wt2]}, he really seemed that way when I first met him."
                            $ wsis_mood = "O1"
                            wsis "You know nothing.{w=[wt3]} Everything you saw in the locker room doesn't even come close to the demon he's capable of being."
                            hero "Eh...?{w=[wt3]} What makes you say that?"
                            wsis "Never mind.{w=[wt3]} I don't wanna talk about him."

                        elif not "WSIS_BG_HRIV_2" in hero_know:
                            if not (wsis_inti >= min(20, wsis_inti_cap)) or not (wsis_love >= 25):
                                $ wsis_mood = "O1"
                                wsis "He's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} disgusting.{w=[wt2]} I don't want to talk about it."
                                if not (wsis_inti >= min(20, wsis_inti_cap)):
                                    mind "(She doesn't seem to feel close enough to me to have this kind of conversation.)"
                                elif not (wsis_love >= 25):
                                    mind "(She doesn't seem to like me enough to have this kind of conversation.)"
                            else:
                                $ hero_know.append("WSIS_Revelation")
                                $ msg.msg(renpy.translate_string("Character backstory revealed"))
                                $ hero_know.append("WSIS_BG_HRIV_2")
                                $ msg.msg(renpy.translate_string("You know [C_Nam][fnamewsis][C_Off] a little more"))
                                $ add_stat("wsis", "inti", 1)

                                $ hero_mood = "A1"
                                hero "You said you know nothing about him{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} but it seems like there's more to it."
                                $ wsis_mood = "O1"
                                $ wsis_fx = 0
                                wsis "{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}We{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} We used to be friends."
                                $ hero_mood = "O1"
                                hero "Friends?{w=[wt2]} You and [C_Nam][fnamehriv][C_Off]?"
                                $ wsis_fx = 1
                                $ wsis_mood = "O2"
                                wsis "Y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I used to admire him{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} He was talented{w=[wt2]}, charismatic."
                                wsis "But then{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} he started insisting we should be{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} more than friends."
                                $ hero_mood = "A1"
                                hero "And you didn't want that?"
                                $ wsis_fx = 2
                                $ wsis_mood = "O3"
                                wsis "No!{w=[wt2]} I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I told him I didn't see him that way{w=[wt2]}, but he wouldn't accept it!"
                                wsis "He kept pushing{w=[wt2]}, insisting{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} And that's when I realized."
                                $ wsis_mood = "O2"
                                $ wsis_fx = 1
                                wsis "He only treats girls well when he has{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {i}ulterior motives{/i}.{w=[wt2]} Once he realizes he won't get what he wants{w=[wt2]}, he."
                                $ hero_mood = "O1"
                                hero "What did he do?"
                                $ wsis_fx = 2
                                $ wsis_mood = "O1"
                                wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I don't want to give details{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Not yet."
                                $ hero_mood = "A1"
                                hero "That's okay.{w=[wt2]} Take your time."
                                $ wsis_fx = 2
                                wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}Thanks."

                        else:
                            $ a_event_0 = renpy.random.random()
                            $ wsis_mood = "O1"

                            if a_event_0 < 1/5:
                                $ hero_mood = "A1"
                                hero "How are things with [C_Nam][fnamehriv][C_Off] at school?"
                                $ wsis_mood = "O2"
                                wsis "He's always trying to apologize{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Like that would fix anything!"
                            elif a_event_0 < 2/5:
                                $ hero_mood = "A1"
                                hero "Is [C_Nam][fnamehriv][C_Off] still bothering you?"
                                $ wsis_mood = "O2"
                                $ wsis_fx = 1
                                wsis "He keeps trying to talk to me{w=[wt2]}, trying to get close.{w=[wt3]} He thinks if he's nice enough{w=[wt2]}, I'll forget who he really is."
                                $ hero_mood = "O1"
                                hero "But you won't."
                                $ wsis_fx = 2
                                wsis "Never.{w=[wt2]} I know what he's capable of."
                            elif a_event_0 < 3/5:
                                $ wsis_mood = "O2"
                                $ wsis_fx = 1
                                wsis "He's still trying to act like nothing happened.{w=[wt3]} He probably thinks if enough time passes{w=[wt2]}, I'll just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} move on.{w=[wt2]} But I won't."
                            elif a_event_0 < 4/5:
                                $ hero_mood = "A1"
                                hero "Do you have to see [C_Nam][fnamehriv][C_Off] often at school?"
                                $ wsis_mood = "O1"
                                $ wsis_fx = 1
                                wsis "I stay as far away from him as possible.{w=[wt3]} But he keeps trying to approach me{w=[wt2]}, trying to regain my trust. {w=[wt2]} But he'll never have it again."
                            else:
                                $ wsis_mood = "O2"
                                $ wsis_fx = 1
                                wsis "Sometimes he tries to approach{w=[wt2]}, when no one is near{w=[wt2]}, saying he's sorry{w=[wt2]}, that he made a mistake{w=[wt2]}, and other bullshits.{w=[wt3]} He's disgusting."

                    $ add_stat("wsis", "inti", 0.2)

                "{image=icon_wric} [C_Nam][fnamewric][C_Off]" if not "Talk_Char_WRIC" in wsis_know and wric_quest_1 == 1:
                    $ wsis_know.append("Talk_Char_WRIC")
                    $ hero_mood = "A2"
                    hero "What do you think about [C_Nam][fnamewric][C_Off]?"

                    if wsis_quest_2 < 1: # Hostile phase
                        $ wsis_mood = "O2"
                        wsis "{aw}Hmph...!{/aw}{w=[wt2]} I already told everything you need to know about her."
                        hero "You just said she is a problem.{w=[wt2]} I don't get it."

                        $ a_event_0 = renpy.random.random()

                        if a_event_0 < 1/3:
                            wsis "She's just a arrogant blonde bitch."
                        elif a_event_0 < 2/3:
                            wsis "It doesn't matter.{w=[wt2]} Just stay away from her!"
                        else:
                            wsis "'Cause as I said{w=[wt2]}, she's problem.{w=[wt2]} Is it too hard to understand?"

                    else: # Friendly phase
                        if not "WSIS_BG_WRIC_1" in hero_know and 0 > 1: # Unavailable
                            $ hero_know.append("WSIS_BG_WRIC_1")
                            $ msg.msg(renpy.translate_string("You know [C_Nam][fnamewsis][C_Off] a little more"))
                            $ add_stat("wsis", "inti", 1)

                            $ wsis_mood = "O2"
                            $ wsis_fx = 0
                            wsis "[C_Nam][fnamewric][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She's the worst person at school.{w=[wt2]} Period."
                            $ hero_mood = "O1"
                            hero "That's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} strong words.{w=[wt2]} What happened?"
                            $ wsis_fx = 1
                            $ wsis_mood = "O3"
                            wsis "Mom works at her house{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} as a maid."
                            $ hero_mood = "O1"
                            hero "Oh."
                            wsis "Mom thought it would be nice if we met{w=[wt2]}, since we go to the same school."
                            wsis "But we both{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} We're both too proud{w=[wt1]}, I guess.{w=[wt2]} We immediately clashed."
                            $ hero_mood = "A1"
                            hero "I see."
                            $ wsis_fx = 2
                            $ wsis_mood = "O3"
                            wsis "And then{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} then she had the {i}audacity{/i} to threaten me!"
                            wsis "She said if I didn't treat her well{w=[wt2]}, she'd tell her father to {sc=1}{b}fire Mom{/b}{/sc}!"

                        elif not "WSIS_BG_WRIC_2" in hero_know:
                            if not (wsis_inti >= min(20, wsis_inti_cap)) or not (wsis_love >= 25):
                                $ wsis_mood = "O1"
                                wsis "She's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} a problem.{w=[wt2]} That's all."
                                if not (wsis_inti >= min(20, wsis_inti_cap)):
                                    mind "(She doesn't seem to feel close enough to me to have this kind of conversation.)"
                                elif not (wsis_love >= 25):
                                    mind "(She doesn't seem to like me enough to have this kind of conversation.)"
                            else:
                                $ hero_know.append("WSIS_BG_WRIC_2")
                                $ msg.msg(renpy.translate_string("You know [C_Nam][fnamewsis][C_Off] a little more"))
                                $ add_stat("wsis", "inti", 1)

                                $ hero_mood = "O1"
                                hero "What happened after she threatened you?"
                                $ wsis_mood = "O3"
                                $ wsis_fx = 0
                                wsis "I told her{w=[wt2]}, if she {i}ever{/i} did that{w=[wt2]}, I'd make her {sc=1}{b}regret it{/b}{/sc}."
                                wsis "I told her I'd hit her{w=[wt2]}, that I'd do things that would make her {i}wish{/i} she never said that."
                                $ hero_mood = "O1"
                                hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}"
                                $ wsis_fx = 1
                                $ wsis_mood = "O2"
                                wsis "Now she's afraid of me.{w=[wt2]} Good.{w=[wt2]} She should be."
                                wsis "Nobody threatens my Mom's job.{w=[wt2]} {sc=1}{b}Nobody{/b}{/sc}."
                                $ hero_mood = "A1"
                                hero "I understand{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} You were protecting [C_Nam][hero_about_wmom][C_Off]."
                                $ wsis_fx = 2
                                $ wsis_mood = "O1"
                                wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}Yeah."

                        else:
                            $ a_event_0 = renpy.random.random()
                            $ wsis_mood = "O2"

                            if a_event_0 < 1/3:
                                $ hero_mood = "A1"
                                hero "Still having problems with [C_Nam][fnamewric][C_Off]?"
                                wsis "She stays away from me now.{w=[wt2]} As she should."
                            elif a_event_0 < 2/3:
                                wsis "I can't stand her.{w=[wt2]} Everything about her annoys me."
                            else:
                                wsis "She's a spoiled princess who thinks money can solve everything."

                    $ add_stat("wsis", "inti", 0.2)

                "{image=icon_hprv} [C_Nam][fnamehprv][C_Off]" if not "Talk_Char_HPRV" in wsis_know and hprv_quest_1 == 1:
                    $ wsis_know.append("Talk_Char_HPRV")
                    $ hero_mood = "A2"
                    hero "What do you think about [C_Nam][fnamehprv][C_Off]?"

                    $ a_event_0 = renpy.random.random()
                    $ wsis_mood = "O1"

                    if wsis_quest_2 < 1: # Hostile phase
                        wsis "That pervert?{w=[wt2]} Ugh{w=[wt1]}, why would you even ask?"
                        hero "Just curious."
                        wsis "Well{w=[wt1]}, don't be!"

                    else: # Friendly phase - 5 random variations
                        if a_event_0 < 1/5:
                            $ wsis_fx = 1
                            wsis "Ugh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} [C_Nam][fnamehprv][C_Off]."
                            $ hero_mood = "A1"
                            hero "Not a fan?"
                            wsis "He's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} such a pervert!{w=[wt2]} Always trying to peek at girls' skirts and stuff."
                            $ hero_mood = "O1"
                            hero "That's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} pretty bad."
                            $ wsis_fx = 2
                            $ wsis_mood = "O2"
                            wsis "I have to be extra careful around him!{w=[wt2]} It's so annoying!"
                        elif a_event_0 < 2/5:
                            $ hero_mood = "A1"
                            hero "Has he ever{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} tried anything with you?"
                            $ wsis_fx = 1
                            wsis "A few times{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} but I shut him down pretty quickly."
                        elif a_event_0 < 3/5:
                            $ wsis_mood = "O1"
                            wsis "I still can't believe the school hasn't done anything about him."
                            $ hero_mood = "O1"
                            hero "Yeah{w=[wt1]}, that's concerning."
                            $ wsis_fx = 1
                            wsis "Every girl in school has complained about him{w=[wt2]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} nothing changes."
                        elif a_event_0 < 4/5:
                            $ wsis_mood = "O1"
                            $ wsis_fx = 1
                            wsis "Guys like [C_Nam][fnamehprv][C_Off] are the worst."
                            $ hero_mood = "A1"
                            hero "At least he's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} obvious about it?"
                            $ wsis_mood = "O2"
                            wsis "That doesn't make it {i}better{/i}!{w=[wt2]} It just means he has no shame!"
                        else:
                            $ wsis_fx = 1
                            wsis "At least I know to stay away from [C_Nam][fnamehprv][C_Off] now."
                            $ hero_mood = "A2"
                            hero "That's good."
                            $ wsis_mood = "O1"
                            wsis "I learned my lesson after{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} after the first time he tried something."
                            wsis "Now I always keep my distance."

                    $ add_stat("wsis", "inti", 0.2)

                "Return":
                    jump wsis_interact_chat

            $ gametimemin += 20
            jump wsis_interact_check

        "Return":
            jump wsis_interact

    $ wsis_know.append("Talk")
    $ gametimemin += 20
    $ add_stat("wsis", "inti", 0.2)
    jump wsis_interact_check

# ----------------------------------------------------------------------------------------------------
label wsis_interact_revelation: # Revelation
# ----------------------------------------------------------------------------------------------------
    $ msg.msg(renpy.translate_string("No more daily revelations available"))
    $ a_event_0 = renpy.random.random()
    if a_event_0 < 1/5:
        wsis "{aw}Hmph...!{/aw} I already said too much."
    elif a_event_0 < 2/5:
        wsis "{aw}Shut up!{/aw}{w=[wt2]} You won't make me say anything more."
    elif a_event_0 < 3/5:
        wsis "I already told you a lot today."
    elif a_event_0 < 4/5:
        wsis "You already asked too much for today.{w=[wt2]} Be quiet!"
    else:
        wsis "Enough gossip for today."

# ----------------------------------------------------------------------------------------------------
# Reaction
# ----------------------------------------------------------------------------------------------------
label wsis_upset_check:
    $ a_event_2 = 0
    $ a_event_2 -= (personality[1] * 0.02)
    if wsis_to_hero == "Lil Bro":
        $ a_event_2 += 1
    $ a_event_3 = (25 - (a_event_2 * 5)) * sum(1 for buceta in wsis_know if buceta =="Upset")

    return

label wsis_reaction:
    if a_event_0 == 1: # HERO tried to hug WSIS too early
        #$ wsis_know.append("Upset")
        #$ msg.msg("[C_Nam][fnamewsis][C_Off]'s anger {color=#32FF32}+"+str(round((25 - (a_event_2 * 5)) * sum(1 for buceta in wsis_know if buceta =="Upset"), 2))[:4]+"%{/color}. You better not piss her off")
        #call wsis_upset_check

        if a_event_3 < 100:
            if wsis_inti < 10 and personality[1] > 50:
                show HERO at CC_average
                pause(0.2)
                $ wsis_mood = "O3"
                wsis "{aw}DON'T{/aw}{nw}"
                $ hero_mood = "O1"
                show HERO at Stay
                wsis "{aw}DON'T{fast} YOU DARE TAKE ANOTHER STEP{w=[wt1]}, YOU PERVERT!{/aw}{w=[wt1]}{nw}"
                show HERO at LC_slow
                wsis "{aw}DON'T YOU DARE TAKE ANOTHER STEP, YOU PERVERT!{/aw}{fast}"

            else:
                wsis "Get off!"

            $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] doesn't feel like you're intimate enough for that"))
            jump wsis_interact
        else:
            $ wsis_mood = "O3"
            wsis "{pa}UGH!!!{/pa}{w=[wt2]} {aw}You are annoying!{/aw}"
            jump wsis_interact_end

    if a_event_0 == 2: # HERO tried to kiss WSIS too early or said something inconvenient
        $ wsis_know.append("Upset")
        $ wsis_know.append("Upset")
        $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off]'s anger {color=#32FF32}+")+str(round((25 - (a_event_2 * 5)) * sum(1 for buceta in wsis_know if buceta =="Upset"), 2))[:4]+renpy.translate_string("%{/color}. You better not piss her off"))
        call wsis_upset_check from _call_wsis_upset_check_3

        if a_event_3 < 100:
            $ wsis_mood = "O3"
            wsis "Okay{w=[wt2]}, listen{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} I will let this pass this time.{w=[wt3]} But I'll {b}NOT{/b} admit that you treat me like this.{w=[wt2]} Understood?"
            hero "Y{w=[wt1]}-yes.{w=[wt2]} I{w=[wt1]}-I'm sorry."
            $ wsis_mood = "O1"
            wsis "{bt}Hunf...!{/bt}{w=[wt2]} Good."
        else:
            $ wsis_mood = "O3"
            $ wsis_fx = 2
            wsis "That's enough.{w=[wt2]} You're really a jerk!"
            jump wsis_interact_end

    if a_event_0 == 3: # HERO did something extremelly inconvenient
        $ wsis_know.append("Upset")
        $ wsis_know.append("Upset")
        $ wsis_know.append("Upset")
        $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off]'s anger {color=#32FF32}+")+str(round((25 - (a_event_2 * 5)) * sum(1 for buceta in wsis_know if buceta =="Upset"), 2))[:4]+renpy.translate_string("%{/color}. You better not piss her off"))
        call wsis_upset_check from _call_wsis_upset_check_4

        if a_event_3 < 100:
            $ wsis_mood = "O3"
            wsis "Okay{w=[wt2]}, listen{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} I will let this pass this time.{w=[wt3]} But I'll {b}NOT{/b} admit that you treat me like this.{w=[wt2]} Understood?"
            hero "Y{w=[wt1]}-yes.{w=[wt2]} I{w=[wt1]}-I'm sorry."
            $ wsis_mood = "O1"
            wsis "{bt}Hunf...!{/bt}{w=[wt2]} Good."
        else:
            $ wsis_mood = "O3"
            wsis "You better not dare to address me, you jerk!"
            jump wsis_interact_end

    jump wsis_interact_check

# ----------------------------------------------------------------------------------------------------
# End
# ----------------------------------------------------------------------------------------------------
jump wsis_interact_end

# ----------------------------------------------------------------------------------------------------
# Initiative - WSIS starts conversations (only after quest 5)
# ----------------------------------------------------------------------------------------------------
label initiative_wsis:
    $ wsis_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wsis_inti*0.008) and renpy.random.random() < (wsis_love*0.008) and not any(get_id.startswith("HERO_Dated") for get_id in wsis_know):
        $ wsis_fx = 1
        $ wsis_mood = "A1"
        wsis "[C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Did you{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} ever date anyone in the countryside?{nw}"

        menu:
            wsis "[wsis_to_hero]... Did you... ever date anyone in the countryside?{fast}"

            "No":
                $ wsis_know.append("HERO_Dated_N")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.5)
                $ add_stat("hero", "cha_soc", 0.5)

                hero "No, I never dated anyone."

                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "R{w=[wt1]}-really?{w=[wt3]} Not even once?"

                $ hero_mood = "A1"
                hero "Nope.{w=[wt2]} I guess I was waiting for the right person."

                $ wsis_fx = 2
                wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}I see."

            "Yes":
                $ wsis_know.append("HERO_Dated_Y")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", -0.25)
                $ add_stat("hero", "cha_soc", -0.25)

                hero "Yeah, I dated someone once."

                $ wsis_mood = "O1"
                wsis "Oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} So you had a girlfriend."

                $ hero_mood = "A1"
                hero "It didn't work out though.{w=[wt2]} We went our separate ways."

                $ wsis_fx = 1
                $ wsis_mood = "A1"
                wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I see."

            "Don't choose":
                jump initiative_wsis_return

    # ----------------------------------------------------------------------------------------------------
    # Ask HERO's girl preference
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wsis_inti*0.008) and renpy.random.random() < (wsis_love*0.008) and sum(1 for get_id in wsis_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wsis_know if get_id.startswith("HERO_N_Girl")) < 4:
        $ wsis_fx = 2
        $ wsis_mood = "A2"
        wsis "S{w=[wt1]}-so{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} W{w=[wt1]}-what kind of girls do you like?{nw}"

        menu:
            wsis "S-so... W-what kind of girls do you like?{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think."

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in wsis_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in wsis_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in wsis_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in wsis_know if "Personality_" in get_id)

                # Appearance Likes(Y) / Dislikes(N)
                $ a_event_1 = wsis_know
                $ a_event_3 = "initiative_wsis_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_12

                # Store the answer if one was given
                if _return:
                    $ wsis_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)

                if _return in ["Breast_1", "HairSize_4", "HairSize_5", "EyeShape_3", "Personality_4", "Personality_8", "Personality_9"]: # Match
                    $ add_stat("wsis", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ wsis_fx = 2
                    $ wsis_mood = "A2"
                    wsis "{aw}T{w=[wt1]}-that's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} that's exactly{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}{/aw}"

                    $ hero_mood = "A2"
                    hero "Hm?"

                    $ wsis_fx = 2
                    wsis "{aw}N{w=[wt1]}-nothing!{/aw}{w=[wt2]} Forget it!"

                elif _return in ["Breast_3", "Breast_4", "Breast_5", "HairSize_0", "HairSize_1", "HairSize_2", "Personality_3", "Personality_7", "Personality_10"]: # Opposite match
                    $ add_stat("wsis", "bonus", -10)
                    $ wsis_mood = "O1"
                    wsis "Hmph!{w=[wt2]} I guess everyone has their preferences."

                else: # Others
                    $ wsis_mood = "A1"
                    wsis "I see{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} That's interesting."

            "Don't choose":
                jump initiative_wsis_return

    # ----------------------------------------------------------------------------------------------------
    # Ask what's HERO favorite color
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wsis_inti*0.005) and not any(get_id.startswith("HERO_F_Color") for get_id in wsis_know):
        $ wsis_mood = "A1"
        wsis "Hey{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} What's your favorite color?{nw}"
        menu:
            wsis "Hey... What's your favorite color?{fast}"

            "Red":
                $ hero_mood = "A1"
                hero "I'd say red!"

                $ wsis_know.append("HERO_F_Color_Red")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.1)
                $ add_stat("hero", "cha_soc", 0.1)

                $ wsis_mood = "A1"
                wsis "Red, huh?{w=[wt2]} It's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} bold, I guess."

            "Blue":
                $ hero_mood = "A1"
                hero "Blue.{w=[wt2]} It's calming."

                $ wsis_know.append("HERO_F_Color_Blue")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.25)
                $ add_stat("hero", "cha_soc", 0.25)

                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "Blue is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} nice.{w=[wt2]} I like that color too."

            "Green":
                $ hero_mood = "A1"
                hero "Green, definitely.{w=[wt2]} It reminds me of nature."

                $ wsis_know.append("HERO_F_Color_Green")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.1)
                $ add_stat("hero", "cha_soc", 0.1)

                $ wsis_mood = "A1"
                wsis "Green{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} That's a refreshing choice."

            "Purple":
                $ hero_mood = "A1"
                hero "Purple!{w=[wt2]} It's unique."

                $ wsis_know.append("HERO_F_Color_Purple")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.5)
                $ add_stat("hero", "cha_soc", 0.5)

                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "{aw}P{w=[wt1]}-purple!?{/aw}{w=[wt3]} That's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} that's my favorite color too."

                $ hero_mood = "A2"
                hero "Really?{w=[wt2]} We have something in common then!"

                $ wsis_fx = 2
                wsis "{aw}I{w=[wt1]}-it's not that special!{/aw}{w=[wt2]} Lots of people like purple!"

            "Don't choose":
                jump initiative_wsis_return

    # ----------------------------------------------------------------------------------------------------
    # Ask what kind of games HERO likes
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wsis_inti*0.005) and not (("HERO_Y_Act_Videogame" in wsis_know) and ("HERO_Y_Act_Sport" in wsis_know) and ("HERO_Y_Act_Boardgame" in wsis_know)):
        $ wsis_mood = "A1"
        wsis "So{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} what kind of games do you like?{nw}"
        menu:
            wsis "So... what kind of games do you like?{fast}"

            "Videogames":
                hero "I really enjoy videogames.{w=[wt2]} They're a great way to relax and have adventures."

                $ wsis_know.append("HERO_Y_Act_Videogame")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.75)
                $ add_stat("hero", "cha_soc", 0.5)
                $ add_stat("hero", "bonus_int", 5)

                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "V{w=[wt1]}-videogames?{w=[wt3]} I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I play them sometimes too."

                $ hero_mood = "A3"
                hero "Really?{w=[wt2]} Maybe we could play together sometime!"

                $ wsis_fx = 2
                wsis "{aw}M{w=[wt1]}-maybe{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} If I feel like it!{/aw}"

            "Sports/Physical Activities":
                hero "I like staying active with sports and physical activities."

                $ wsis_know.append("HERO_Y_Act_Sport")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.25)
                $ add_stat("hero", "cha_soc", 0.5)
                $ add_stat("hero", "bonus_phy", 5)

                $ wsis_mood = "A1"
                wsis "That's healthy, I guess.{w=[wt2]} Better than being lazy all day."

                $ hero_mood = "A1"
                hero "What about you?{w=[wt2]} Do you exercise?"

                $ wsis_fx = 1
                wsis "S{w=[wt1]}-sometimes{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Not that it's any of your business!"

            "Board and card games":
                hero "I enjoy board and card games.{w=[wt2]} They're fun to play with others."

                $ wsis_know.append("HERO_Y_Act_Boardgame")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.5)
                $ add_stat("hero", "cha_soc", 0.5)
                $ add_stat("hero", "bonus_cha", 5)

                $ wsis_mood = "A1"
                wsis "Board games, huh?{w=[wt2]} I have some in my room."

                $ hero_mood = "A2"
                hero "We should play together sometime!"

                $ wsis_fx = 1
                wsis "W{w=[wt1]}-well{w=[wt2]}, if [C_Nam][fnamewnei][C_Off] wants to play{w=[wt1]}, maybe."

            "Don't choose":
                jump initiative_wsis_return

    # ----------------------------------------------------------------------------------------------------
    # Ask what kind of movies HERO likes
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wsis_inti*0.005) and not any(get_id.startswith("HERO_Y_Theme") for get_id in wsis_know):
        $ wsis_mood = "A1"
        wsis "What kind of movies do you watch?{nw}"
        label initiative_wsis_HERO_Y_Theme:
            pass
        menu:
            wsis "What kind of movies do you watch?{fast}"

            "Action":
                hero "I'm into action movies.{w=[wt2]} Explosions, fights, all that adrenaline."

                $ wsis_know.append("HERO_Y_Theme_Action")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.25)
                $ add_stat("hero", "cha_soc", 0.25)

                $ wsis_mood = "A1"
                wsis "Action, huh?{w=[wt2]} Pretty typical for guys."

                $ hero_mood = "A1"
                hero "What about you?"

                $ wsis_fx = 1
                wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I don't mind them either."

            "Drama/Romance":
                hero "I actually enjoy dramas and romance stories.{w=[wt2]} They have depth and emotion."

                $ wsis_know.append("HERO_Y_Theme_Romance")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.75)
                $ add_stat("hero", "cha_soc", 0.75)

                $ wsis_fx = 2
                $ wsis_mood = "A2"
                wsis "{aw}R{w=[wt1]}-really!?{/aw}{w=[wt3]} Most guys hate those."

                $ hero_mood = "A1"
                hero "I think they're beautiful.{w=[wt2]} What's wrong with that?"

                $ wsis_fx = 1
                wsis "N{w=[wt1]}-nothing{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} It's actually{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} kind of nice."

            "Horror/Mystery":
                hero "Horror and mystery movies.{w=[wt2]} I like the suspense and trying to figure things out."

                $ wsis_know.append("HERO_Y_Theme_Horror")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.5)
                $ add_stat("hero", "cha_soc", 0.5)

                $ wsis_mood = "O1"
                wsis "Never really watched something like this.{w=[wt3]} But I have curiosity.{w=[wt3]} I wanna try to watch one someday."

                $ hero_mood = "A2"
                hero "Are you afraid of horror movies?"

                $ wsis_fx = 1
                $ wsis_mood = "O2"
                wsis "{aw}I{w=[wt1]}-I'm not!{/aw}{w=[wt3]} I just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} prefer other genres!"

            "Anime/Animation":
                hero "I like anime and animated movies.{w=[wt2]} The art styles are amazing."

                $ wsis_know.append("HERO_Y_Theme_Anime")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.5)
                $ add_stat("hero", "cha_soc", 0.5)

                $ wsis_fx = 1
                $ wsis_mood = "A2"
                wsis "Anime?{w=[wt3]} I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I watch some too."

                $ hero_mood = "A3"
                hero "Really?{w=[wt2]} What's your favorite?"

                $ wsis_fx = 2
                wsis "{aw}T{w=[wt1]}-that's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'll tell you later maybe!{/aw}"

            "Don't choose":
                jump initiative_wsis_return

    # ----------------------------------------------------------------------------------------------------
    # Ask about HERO's childhood memories
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wsis_inti*0.005) and not any(get_id.startswith("HERO_Memory") for get_id in wsis_know):
        $ wsis_fx = 1
        wsis "Hey, [C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Do you remember when we were kids?"

        $ hero_mood = "A1"
        hero "Of course! We had some great times together."

        $ wsis_fx = 2
        $ wsis_mood = "A2"
        wsis "Y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} What's your favorite memory from back then?{nw}"

        menu:
            wsis "Y-yeah... What's your favorite memory from back then?{fast}"

            "Playing together":
                hero "I loved when we used to play together in the backyard.{w=[wt2]} You were always so competitive!"

                $ wsis_know.append("HERO_Memory_Playing")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.5)
                $ add_stat("hero", "cha_soc", 0.5)

                $ wsis_fx = 2
                $ wsis_mood = "A2"
                wsis "{aw}I{w=[wt1]}-I wasn't competitive!{/aw}{w=[wt3]} I just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} didn't like losing to you!"

                $ hero_mood = "A2"
                hero "{gg}Heh...{/gg}{w=[wt2]} That's exactly what competitive means."

                $ wsis_fx = 1
                wsis "W{w=[wt1]}-whatever{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Those were{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} fun times."

            "Family dinners":
                hero "I really miss those family dinners when everyone was together.{w=[wt2]} Mom's cooking{w=[wt1]}, everyone laughing{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} It felt so warm."

                $ wsis_know.append("HERO_Memory_Dinners")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 0.75)
                $ add_stat("hero", "cha_soc", 0.75)

                $ wsis_fx = 2
                $ wsis_mood = "A2"
                wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}Yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I miss that too."

                $ hero_mood = "A1"
                hero "At least we're together again now, right?"

                $ wsis_fx = 1
                wsis "Y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'm glad you're back, [C_Nam][wsis_to_hero][C_Off]."

            "Your smile":
                hero "Honestly?{w=[wt2]} I always loved your smile.{w=[wt2]} You used to smile so much more back then."

                $ wsis_know.append("HERO_Memory_Smile")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knows you a little more"))
                $ add_stat("wsis", "inti", 0.5)
                $ add_stat("wsis", "love", 1)
                $ add_stat("hero", "cha_soc", 1)

                $ wsis_fx = 2
                $ wsis_mood = "A2"
                wsis "{aw}W{w=[wt1]}-what kind of answer is that!?{/aw}{w=[wt3]} You're so embarrassing."

                $ hero_mood = "A1"
                hero "It's the truth though.{w=[wt2]} I'd like to see you smile more often again."

                $ wsis_fx = 2
                wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'll try."

    # ----------------------------------------------------------------------------------------------------
    # Share a recent thought or feeling
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wsis_inti*0.005) and renpy.random.random() < (wsis_love*0.005):
        $ wsis_fx = 1
        $ wsis_mood = "A2"

        $ a_event_1 = renpy.random.random()

        if a_event_1 < 0.25:
            wsis "[C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I've been thinking{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'm glad you came back."

            $ hero_mood = "A1"
            hero "Me too, [C_Nam][hero_to_wsis][C_Off]."

            $ wsis_fx = 1
            wsis "Things are{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} better now."

        elif a_event_1 < 0.5:
            wsis "You know{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I was really lonely before you came back."

            $ hero_mood = "O1"
            hero "I'm sorry I wasn't there for you."

            $ wsis_fx = 2
            wsis "{aw}T{w=[wt1]}-that's not what I meant!{/aw}{w=[wt3]} I just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'm happy now.{w=[wt2]} That's all."

        elif a_event_1 < 0.75:
            wsis "I've been trying to be less{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} mean to you{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Is it working?"

            $ hero_mood = "A2"
            hero "You're doing great, [C_Nam][hero_to_wsis][C_Off].{w=[wt2]} I can tell you're trying."

            $ wsis_fx = 1
            $ wsis_mood = "A2"
            wsis "G{w=[wt1]}-good."

        else:
            wsis "Sometimes I wonder what would have happened if{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} if we had stayed together back then."

            $ hero_mood = "A1"
            hero "We're together now.{w=[wt2]} That's what matters."

            $ wsis_fx = 1
            wsis "Yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} You're right."

        $ add_stat("wsis", "inti", 0.2)
        $ add_stat("wsis", "love", 0.5)
        $ add_stat("hero", "cha_soc", 0.5)

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:
        $ wsis_mood = "A1"
        wsis "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Never mind.{w=[wt2]} I forgot what I was going to say."
        jump wsis_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("wsis", "inti", 0.2)
    jump wsis_interact

# ----------------------------------------------------------------------------------------------------
# Player didn't answer initiative question
# ----------------------------------------------------------------------------------------------------
label initiative_wsis_return:
    hero "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'm not sure how to answer that right now."
    $ wsis_mood = "A1"
    wsis "That's okay.{w=[wt2]} You don't have to answer if you don't want to."
    jump wsis_interact

screen WSIS_EatSFX():
    timer 1 repeat True action If(a_event_0 == 0, true=Play("SE1", renpy.random.choice(["Eat1.mp3","Eat2.mp3","Eat3.mp3","Eat4.mp3","Eat5.mp3","Eat6.mp3","Eat7.mp3"])))
