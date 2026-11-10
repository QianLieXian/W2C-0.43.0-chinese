# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wnei_show:

    if wnei_love <= -20:
        $ wnei_mood = "O2"
    elif wnei_love < 0:
        $ wnei_mood = "O1"
    elif wnei_love >= 0:
        $ wnei_mood = "A2"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_8

    show WNEI at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wnei_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewnei][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wnei")))))

    if Get_ActivityName("wnei") in ["staying", "gaming", "playing", "drawing", "at break", "at club"]:
        return

    if Get_ActivityName("wnei") in ["at class"]:
        jump show_ui

    if Get_ActivityName("wnei") in ["sleeping"] and Check_CharInMap("wnei", "neighbor"):
        if perk_int_per > 0:
            $ msg.msg(renpy.translate_string("You used your [C_Not]Perception[C_Off]"))
        scene wnei_actview1_bg
        show wnei_actview1_sleeping_wnei_body 1
        show wnei_actview1_sleeping_wnei_wear 1_under
        show wnei_actview1_fg at OpacityX(1/(1 + (perk_int_per/3)))
        show fx_light:
            blend "add"
        with fade

        if gametimehour == 6 and gametimeday > 2 and gametimeweek not in ["Saturday", "Sunday"]:
            menu:
                "Call her":
                    show screen phone_call
                    pause
                    show wnei_actview1_sleeping_wnei_body 2
                    show wnei_actview1_sleeping_wnei_wear 2_under
                    with dissolve
                    pause
                    show wnei_actview1_sleeping_wnei_body 3
                    show wnei_actview1_sleeping_wnei_wear 3_under
                    with dissolve
                    play SE1 "JingleRight.mp3"
                    hide screen phone_call
                    pause

                    wnei "Hmm...?"
                    hero "Hey, I'm here on the window!"
                    scene wnei_meetwmam_1_bg 1
                    show wnei_meetwmam_1_wnei_body 1
                    show wnei_meetwmam_1_wnei_face o0
                    show wnei_meetwmam_1_mg at OpacityX(1)
                    show wnei_meetwmam_1_fg at OpacityX(0.50)
                    show wnei_meetwmam_1_hero_body
                    show fx_light:
                        blend "add"
                    with fade

                    show wnei_meetwmam_1_wnei_face o1
                    wnei "{bt}Waaaaah...{/bt}{w=[wt3]} Mornin'...!"

                    show wnei_meetwmam_1_wnei_face o0
                    hero "Hurry up!{w=[wt3]} Let's go to school together!"

                    show wnei_meetwmam_1_wnei_face o1
                    wnei "{bt}Kay...{/bt}"

                    show wnei_meetwmam_1_wnei_face o0 with None
                    $ StartAct("wnei", [("bathing", 10), (("changing", "school"), 10), ("eating", 10), (("moving", "home"), 10)], True)

                "Return":
                    pass
        else:
            pause

        jump show_ui

    elif (Get_ActivityName("wnei") in ["changing"]) and Check_CharInMap("wnei", "neighbor"):
        scene wnei_actview1_bg
        if wnei_activity_current == ("changing", "home"):
            show wnei_actview1_dressing_wnei_body 1
            show wnei_actview1_dressing_wnei_wear_1 1_under
            show wnei_actview1_dressing_wnei_wear_2 1_home
        elif wnei_activity_current == ("changing", "school"):
            show wnei_actview1_dressing_wnei_body 2
            show wnei_actview1_dressing_wnei_wear_1 2_under
            show wnei_actview1_dressing_wnei_wear_2 2_school
        else:
            show wnei_actview1_dressing_wnei_body 3
            show wnei_actview1_dressing_wnei_wear_1 3_under
            show wnei_actview1_dressing_wnei_wear_2 3_home
            show wnei_actview1_dressing_wnei_wear_2 3_school
        show wnei_actview1_fg
        show fx_light:
            blend "add"
        with fade

    pause
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wnei_interact_end:
    if "interacting_hero" in wnei_know:
        $ wnei_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wnei_interact_start:
    call hide_ui from _call_hide_ui_55
    call wnei_show_activity from _call_wnei_show_activity
    $ wnei_inti = min(wnei_inti_cap, wnei_inti)
    call hide_ui from _call_hide_ui_56
    call wnei_show from _call_wnei_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
# None Yet

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wnei_interact_check:
    # Save current outfit before any updates
    $ wnei_wear_keep = wnei_wear

    call gamecheck from _call_gamecheck_11
    call gametime from _call_gametime_25
    call check_playermap from _call_check_playermap_9
    call hide_ui from _call_hide_ui_57

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wnei_wear != wnei_wear_keep:
        $ wnei_wear = wnei_wear_keep

    call wnei_show from _call_wnei_show_1

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    if (gametimeday == 1 and (gametimehour >= 12 and gametimehour <= 13)) or not Check_CharSameMap("hero", "wnei"):

        if Check_IfActivity("wnei", "watching TV"):
            $ wnei_mood = "A1"
            wnei "Hey!{w=[wt2]} Let's watch TV!"
            menu:
                "Watch TV":
                    hero "Sure, let's go!"
                "Return":
                    hero "Well, I don't know."
                    wnei "Hunf! Boring!"

        elif Check_IfActivity("wnei", ("moving", "school")):
            wnei "Let's go to school!"

        elif Check_TimeStr("school_class") and Check_CharInMap("wnei", "school"): # Class Time
            if Check_CharSameMap("hero", "wnei"):
                $ hero_mood = "A2"
                hero "Oh{w=[wt2]}, I need to leave.{w=[wt3]} It's time for your class."

                $ wnei_mood = "O1"
                wnei "Why don't you stay here in class with me?{w=[wt3]} It'll be super duper more fun!!!"

                $ hero_mood = "O1"
                hero "Cos the teacher is already giving me a dirty look.{w=[wt3]} See ya!"
                $ Set_CharMap("hero", "school", "hallway_2")
                jump wnei_interact_end

            else:
                $ wnei_mood = "O2"
                wnei "Oops{w=[wt2]}, gotta run now.{w=[wt3]} Class is starting!"

                if Get_MapName("wsis", "at class") == Get_MapName(None, "school", "class_1a"):
                    menu:
                        "Accompany her":
                            $ hero_mood = "A2"
                            hero "Want me to walk with you?"
                            
                            $ wnei_mood = "A4"
                            wnei "{bt}YEAHHH!!!{/bt}{w=[wt3]} Let's go together!{w=[wt2]}{nw}"

                            show WNEI at RC
                            show WNEI at OR_slow
                            wnei "{bt}YEAHHH!!!{/bt}{w=[wt3]} Let's go together!{w=[wt2]}{fast} {bt}The last one to arrive eats ostrich poop!{/bt} {lg}Shi hi hi hi...{/lg}"
                            
                            show HERO at OR_slow
                            $ hero_mood = "O1"
                            hero "Wait, that's not what accompaniment means!"
                        
                            scene bg_0
                            with dissolve

                            $ hero_map = wnei_map
                            call gametime from _call_gametime_26
                            call check_playermap from _call_check_playermap_10
                            call hide_ui from _call_hide_ui_58
                            show WNEI at RC
                            show HERO at LC
                            with dissolve

                            $ hero_mood = "O1"
                            hero "So, see ya!"
                            wnei "See yaaa!"

                            jump wnei_interact_end
                            
                        "Let her go":
                            pass

                $ hero_mood = "A1"
                hero "Better hurry then."
                
                show WNEI at RC
                
                $ wnei_mood = "A4"
                wnei "I'm faster than the {bt}THUNDEEEER...!{/bt}{nw}"

                show WNEI at OR_average
                wnei "I'm faster than the {bt}THUNDEEEER...!{/bt}{fast}{w=[wt2]} {bt}Bye bye...!{/bt}"

        elif Get_ActivityName("wnei") in ["playing", "gaming", "studying"] and Check_CharInMap("hero", "school", False) == Check_CharInMap("wnei", "school", False):
            $ a_event_1 = renpy.substitute(Get_MapName("wnei", False))
            wnei "Let's go to the [a_event_1]!"
            menu:
                "Follow her":
                    $ hero_map = wnei_map
                    call check_playermap from _call_check_playermap_11
                    #call hide_ui
                    #call wnei_show
                    jump wnei_interact_check
                "Keep":
                    pass

        else:
            $ a_event_1 = renpy.random.random()
            if a_event_1 < 0.5:
                $ wnei_mood = "O1"
                wnei "Oh no!{w=[wt2]} Time went by so fast...!{w=[wt3]} I think I need to go."
            else:
                $ wnei_mood = "A1"
                wnei "Oops!{w=[wt2]} Need to go now!{w=[wt3]} {bt}See you later alligator!{/bt}"

        if "interacting_hero" in wnei_know:
            $ wnei_know.remove("interacting_hero")
        if wnei_is_flw:
            $ wnei_is_flw = False
            $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} is no longer following you"))
        jump wnei_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Get Interaction In Special Event
    # ----------------------------------------------------------------------------------------------------
    elif is_specialevent == True and gametimehour >= 18 and gametimehour <= 20:
        wnei "What will we do?"
        jump wnei_interact

    # ----------------------------------------------------------------------------------------------------
    # WNEI is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wnei") in ["eating"]:
        "{nm}[fnamewnei]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamewnei]{/nm} is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wnei") from _call_circletable_6

                while Get_ActivityName("wnei") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_7
                call gametime from _call_gametime_27
                
                jump wnei_interact_start

            "Return":
                jump wnei_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wnei_know:
            $ a_event_1 = renpy.random.random()

            if renpy.random.random() < (0.2+(wnei_love*0.003)):
                if sum(1 for get_id in wnei_know if get_id =="Talk") >= 2:
                    wnei "We already talked too much.{w=[wt2]} Let's do something fun now!"
                else:
                    jump initiative_wnei

            elif a_event_1 < 0.1 and "Talk" in wnei_know:
                $ wnei_mood = "A4"
                wnei "{nm}[fnamehero]{/nm}{w=[wt1]}, what'll we do now?"

            elif renpy.random.random() < 0.2 and  wsis_map == wnei_map:
                $ wnei_mood = "A2"
                wnei "Look at {nm}[fnamewsis]{/nm}.{w=[wt2]} Her hair is so super duper cool!"

            elif renpy.random.random() < 0.2 and "PatHead" in wnei_know:
                $ a_event_1 = renpy.random.random()
                if a_event_1 < 1/5:
                    $ wnei_mood = "A4"#
                    wnei "{gg}Tee-hee...{/gg}{w=[wt3]} I felt like you were praising me."
                elif a_event_1 < 2/5:
                    $ wnei_mood = "A4"
                    wnei "You find me a good girl, don't ya?{w=[wt4]} Know what?{w=[wt2]} {bt}I'm a super duper good girl!{/bt}"
                elif a_event_1 < 3/5:
                    $ wnei_mood = "A4"
                    wnei "{bt}I love head pat!{/bt}"
                elif a_event_1 < 4/5:
                    $ wnei_mood = "A3"
                    wnei "{bt}I'm a good girl... Nananananaanaa...{/bt}"
                else:
                    $ wnei_mood = "A4"
                    wnei "{gg}Tee-hee...{/gg}{w=[wt2]} Head pat is so comfortable!"

            elif renpy.random.random() < 0.2 and not any(get_id.startswith("Hug") for get_id in wnei_know):
                $ a_event_1 = renpy.random.random()
                if a_event_1 < 1/2:
                    $ wnei_mood = "A2"
                    wnei "When you feel lonely, you can hug me."
                else:
                    $ wnei_mood = "O2"
                    wnei "People use to squeeze me all the time.{w=[wt3]}{nw}"
                    $ wnei_mood = "A3"
                    wnei "People use to squeeze me all the time.{fast} I'm glad you're not like that!{w=[wt2]}{nw}"
                    $ wnei_mood = "A4"
                    wnei "People use to squeeze me all the time. I'm glad you're not like that!{fast} {gg}Tee-hee...{/gg}"

            elif renpy.random.random() < 0.4 and "Hug_Hour" in wnei_know:
                $ a_event_1 = renpy.random.random()
                if a_event_1 < 1/3:
                    $ wnei_mood = "A2"
                    wnei "When you feel lonely, I'll be here for ya!"
                elif a_event_1 < 2/3:
                    $ wnei_mood = "A3"
                    wnei "Ya'll never ever feel lonely with me here{w=[wt2]}, cos I'm super duper cool!"
                else:
                    $ wnei_mood = "A1"
                    wnei "You are very warm.{w=[wt2]} When I get cold, I'll come to you."

            elif renpy.random.random() < 0.2 and "Hug_Enough" in wnei_know:
                $ a_event_1 = renpy.random.random()
                if a_event_1 < 1/3:
                    $ wnei_mood = "O1"
                    wnei "My boobas are already hurting from you squeezing me so much!"
                elif a_event_1 < 2/3:
                    $ wnei_mood = "O1"
                    wnei "You squeezed me too much{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Why people do that?"
                else:
                    $ wnei_mood = "O1"
                    wnei "I think my boobas are crushed."

            else:
                $ a_event_1 = renpy.random.random()
                if a_event_1 < 1/4:
                    $ wnei_mood = "O2"
                    wnei "Hey{w=[wt2]}, ya got kinda big, uh?"
                elif a_event_1 < 2/4:
                    $ wnei_mood = "A1"
                    wnei "What do you wanna do?"
                elif a_event_1 < 3/4:
                    $ wnei_mood = "A2"
                    wnei "Know what?{w=[wt2]} I kinda missed talking to you."
                else:
                    $ wnei_mood = "A2"
                    wnei "Glad yar back."

            jump wnei_interact

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_1 = renpy.random.random()

        if a_event_1 < 1/4:
            $ wnei_mood = "O2"
            wnei "Hey{w=[wt2]}, ya got kinda big, uh?"
        elif a_event_1 < 2/4:
            $ wnei_mood = "A1"
            wnei "What do you wanna do?"
        elif a_event_1 < 3/4:
            $ wnei_mood = "A2"
            wnei "Know what?{w=[wt2]} I kinda missed talking to you."
        else:
            $ wnei_mood = "A2"
            wnei "Glad yar back."

        jump wnei_interact

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wnei_interact:
    call hide_ui from _call_hide_ui_59
    if "interacting_hero" not in wnei_know:
        $ wnei_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            if sum(1 for get_id in wnei_know if get_id =="Talk") >= 2:
                $ wnei_mood = "O1"
                wnei "Ehhh...?{w=[wt2]} Enough of chatting! Let's do something fun!"
                jump wnei_interact
            else:
                jump wnei_interact_chat
        "Touch" if not is_specialevent:
            jump wnei_interact_touch
        "Meet" if date_active == False:
            jump wnei_interact_meet
        "Hang out":
            jump wnei_interact_hangout
        "Give item" if not is_specialevent:
            jump wnei_interact_gift
        "Return":
            jump wnei_interact_end

# ----------------------------------------------------------------------------------------------------
# Meet Options
# ----------------------------------------------------------------------------------------------------
label wnei_interact_meet:
    menu:
        "Date (Prototype)" if wnei_inti >= 40 and gametimeweek in ["Saturday", "Sunday"]:
            hero "What about we go to the beach?"
            wnei "{bt}That's cool!!!{/bt}{w=[wt4]} But{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I need to get a new bikini first."
            hero "Then, let's buy it on the Shopping Mall!"
            wnei "{bt}Let's go!!!{/bt}"
            call date_wnei_stationery from _call_date_wnei_stationery_1
            call date_wnei_fashion from _call_date_wnei_fashion_1
            $ gametimehour = 23
            call gametime from _call_gametime_131

        "Return":
            jump wnei_interact

    jump wnei_interact_check

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wnei_interact_gift:
    $ a_item_8 = "wnei"
    $ a_item_9 = 0
    $ a_item_6 = "wnei_interact"
    call UI_give_Item from _call_UI_give_Item_9

label wnei_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wnei_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wnei_interact_touch:
    menu:
        "Pat head":
            $ X_spd = 1
            $ X_pos = -85
            $ Y_pos = -545
            $ X_pos2 = -60
            $ Y_pos2 = -20
            $ Z_Rot = -10
            $ a_event_0 = 0
            $ a_event_1 = 0
            $ a_event_2 = renpy.random.random()

            show screen wnei_pat
            with Fade(0.5, 0, 1, color="#FFF")


            $ renpy.pause()

            label wnei_interact_touch_headpat:

                if "PatHead_Hour" in wnei_know:
                    $ wnei_know.remove("PatHead_Hour")
                    $ wnei_know.append("PatHead")
                    $ add_stat("wnei", "love", 0.5)
                    $ add_stat("hero", "cha_sex", 0.5)

                    hide screen wnei_pat
                    with dissolve

                elif "PatHead_Day" in wnei_know:
                    $ wnei_know.remove("PatHead_Day")
                    $ wnei_know.append("PatHead")
                    $ add_stat("wnei", "love", 1.5)
                    $ add_stat("hero", "cha_sex", 1.5)

                    hide screen wnei_pat
                    with dissolve

                elif not any(get_id.startswith("PatHead") for get_id in wnei_know):
                    $ wnei_know.append("PatHead")
                    $ add_stat("wnei", "love", 2)
                    $ add_stat("hero", "cha_sex", 2)

                    hide screen wnei_pat
                    with dissolve

                hide screen wnei_pat
                call gamecheck from _call_gamecheck_12
                call hide_ui from _call_hide_ui_60
                call wnei_show from _call_wnei_show_2
                $ wnei_fx = 1

                $ gametimemin += 10
                $ add_stat("wnei", "inti", 0.1)

                jump wnei_interact_check

            #$ X_pos = 1000
            #show HERO at X_average
            #$ renpy.pause(1.5, hard=True)
            #show HERO at LC_slow
            #jump wnei_interact_touch

        "Hug":
            label wnei_interact_touch_hug:

                $ a_event_0 = renpy.random.random()
                if a_event_0 < 0.5:
                    scene bg_2 pink
                elif a_event_0 < 0.5:
                    scene bg_2 yellow
                else:
                    scene bg_2 flowers
                show bg_fx0

                if not "Hug_Enough" in wnei_know:
                    show action_wnei_hug2_body

                    if not "Hug" in wnei_know:
                        show action_wnei_hug2_face 1

                        if perk_cha_sex >= 1:
                            $ add_stat("wnei", "lust", 2)

                        $ add_stat("wnei", "love", 1)
                        $ add_stat("hero", "cha_sex", 1)

                    else:
                        show action_wnei_hug2_face 2

                        if perk_cha_sex >= 1:
                            $ add_stat("wnei", "lust", 2)

                        $ add_stat("wnei", "love", 0.2)
                        $ add_stat("hero", "cha_sex", 0.2)

                    if wnei_wear == "school":
                        show action_wnei_hug2_outfitwnei school
                    elif wnei_wear == "school_sport":
                        show action_wnei_hug2_outfitwnei school_sport
                    elif wnei_wear == "school_swim":
                        show action_wnei_hug2_outfitwnei school_swim
                    else:
                        show action_wnei_hug2_outfitwnei common1
                    if hero_wear == "school":
                        show action_wnei_hug2_outfithero school
                    elif hero_wear == "school_sport":
                        show action_wnei_hug2_outfithero school_sport
                    elif hero_wear == "school_swim":
                        show action_wnei_hug2_outfithero school_swim
                    else:
                        show action_wnei_hug2_outfithero common1
                    with dissolve

                    if "Hug" in wnei_know:
                        $ a_event_1 = renpy.random.random()

                        if a_event_1 < 0.2:
                            show action_wnei_hug2_face 3
                            wnei "Ya kinda like hugging me, huh?"
                        elif a_event_1 < 0.4:
                            show action_wnei_hug2_face 3
                            wnei "Hmm...?{w=[wt2]} Did ya missed me?"
                        elif a_event_1 < 0.6:
                            show action_wnei_hug2_face 3
                            wnei "Are ya feelin' alone?{w=[wt4]} Okay{w=[wt2]}, just a little more."
                        elif a_event_1 < 0.8:
                            show action_wnei_hug2_face 3
                            wnei "Okay{w=[wt2]}, we can hug just a little more."
                        else:
                            show action_wnei_hug2_face 3
                            wnei "Hey{w=[wt2]}, don't press me too much!"

                        show action_wnei_hug2_face 2

                    if renpy.random.random() > (0.1+(wnei_love*0.008)):
                        $ wnei_know.append("Hug_Enough")

                else:
                    show action_wnei_hug3_body
                    show action_wnei_hug3_face 1
                    if wnei_wear == "school":
                        show action_wnei_hug3_outfitwnei school
                    elif wnei_wear == "school_sport":
                        show action_wnei_hug3_outfitwnei school_sport
                    elif wnei_wear == "school_swim":
                        show action_wnei_hug3_outfitwnei school_swim
                    else:
                        show action_wnei_hug3_outfitwnei common1
                    if hero_wear == "school":
                        show action_wnei_hug3_outfithero school
                    elif hero_wear == "school_sport":
                        show action_wnei_hug3_outfithero school_sport
                    elif hero_wear == "school_swim":
                        show action_wnei_hug3_outfithero school_swim
                    else:
                        show action_wnei_hug3_outfithero common1
                    with dissolve

                    $ a_event_1 = renpy.random.random()
                    if a_event_1 < 0.1:
                        show action_wnei_hug3_face 2
                        wnei "{bt}Enough... Enough...{/bt}"
                    elif a_event_1 < 0.2:
                        show action_wnei_hug3_face 2
                        wnei "{bt}Boring... Boring...{/bt}"
                    elif a_event_1 < 0.3:
                        show action_wnei_hug3_face 2
                        wnei "Why people treat me like that?"
                    elif a_event_1 < 0.4:
                        show action_wnei_hug3_face 2
                        wnei "Well{w=[wt2]}, I'm not a pillow, you know?"
                    elif a_event_1 < 0.5:
                        show action_wnei_hug3_face 2
                        wnei "Don't ya think we've had enough of hugs?"

                    show action_wnei_hug3_face 1

                pause

                call gamecheck from _call_gamecheck_13
                call hide_ui from _call_hide_ui_61
                call wnei_show from _call_wnei_show_3
                $ wnei_fx = 1

                $ wnei_know.append("Hug")
                $ gametimemin += 10
                $ add_stat("wnei", "inti", 0.1)

                jump wnei_interact_check

        "Return":
            jump wnei_interact

# ----------------------------------------------------------------------------------------------------
# Interact Chat
# ----------------------------------------------------------------------------------------------------
label wnei_interact_chat:
    menu:
        "Ask how she is" if not "Talk_How" in wnei_know:
            $ hero_mood = "A1"
            # ----------------------------------------------------------------------------------------------------
            # Asking at early morning
            # ----------------------------------------------------------------------------------------------------
            if gametimehour <= 7:
                hero "Did you sleep well?"
                wnei "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Don't know{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I think I'm still sleepy."

            # ----------------------------------------------------------------------------------------------------
            # Asking after afternoon
            # ----------------------------------------------------------------------------------------------------
            elif gametimehour >= 17:
                # ----------------------------------------------------------------------------------------------------
                # HERO gave WNEI tutoring lessons
                # ----------------------------------------------------------------------------------------------------
                if "HangOut_Teach_Day" in wnei_know:
                    $ wnei_know.remove("HangOut_Teach_Day")
                    $ wnei_know.append("HangOut_Teach")
                    $ add_stat("wnei", "love", 1)
                    $ add_stat("hero", "cha_soc", 1)

                    hero "What did you think of the monitoring class?"
                    $ wnei_mood = "O1"
                    wnei "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Study is not much fun.{w=[wt3]}{nw}."
                    $ wnei_mood = "A1"
                    wnei "Hmm... Study is not much fun.{fast} But with you is cool!"
                    $ hero_mood = "A2"
                    hero "Well{w=[wt2]}, I'm glad you didn't find it that bad{w=[wt2]}, I guess.{w=[wt3]} Anyway{w=[wt2]}, you know you can count on me whenever you need me."

                else:
                    hero "Hey{w=[wt2]}, how was your day?"
                    $ wnei_mood = "A3"                
                    wnei "{bt}FUUUUN!!!{/bt}"
                    $ hero_mood = "A2"
                    hero "You know you need to study too, right?"
                    $ wnei_mood = "O1"                
                    wnei "{bt}Ehhhh...!?{/bt}{w=[wt3]} I don't need to!{w=[wt2]} I'm super duper smart!"

            # ----------------------------------------------------------------------------------------------------
            # Asking at any other time
            # ----------------------------------------------------------------------------------------------------
            else:
                $ hero_mood = "A1"
                hero "Hey, {nm}[fnamewnei]{/nm},{w=[wt1]} how have you been?"

                $ wnei_mood = "A4"
                wnei "I'm super duper fine!{w=[wt1]} {lg}Shi hi hi hi...{/lg}"

                if gametimeday == 1:
                    hero "That's cool!{w=[wt1]} You seem to be as excited as ever!"
                    wnei "It's cos you're back'!{w=[wt3]} {nm}Miss. [fnamewmom]{/nm} said you'll go to same school as me and {nm}[fnamewsis]{/nm}!{w=[wt2]} {pr}{bt}NOW WE CAN DO ALOTTA FUN THINGS TOGETHER!!!{/bt}{w=[wt3]} we'll go to school in the morning...{w=[wt2]} we'll play games...{w=[wt2]} we'll sleep together..."
                    $ hero_mood = "O1"
                    $ hero_fx = "1"
                    hero "{aw}W{w=[wt1]}-Wait...{w=[wt2]} What!?{/aw}"
                    $ wnei_mood = "A1"
                    wnei "Uh?{w=[wt2]} What what?"
                    hero "{aw}W{w=[wt1]}-why w{w=[wt1]}-w{w=[wt1]}-ould we{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{/aw}{nw}"
                    $ hero_fx = "2"
                    hero "{aw}W-why w-w-ould we...{fast} Sleep together!?...{/aw}"
                    $ wnei_mood = "A2"                
                    wnei "Ah!{w=[wt3]} That?{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} We'll kinda sleep very close from now on, right?{w=[wt3]} That means we'll sleep together then!"
                    $ hero_fx = "1"
                    mind "(I'm not sure if she considered sleeping {b}together{/b} but in different rooms or is planning something else.{w=[wt3]} Well{w=[wt1]}, it's better to not say anything for now and wait.)"

            $ wnei_know.append("Talk")
            $ wnei_know.append("Talk_How")
            $ add_stat("wnei", "love", 0.5)
            $ add_stat("hero", "cha_soc", 0.5)

        "Ask about hobbies" if is_specialevent == False:
            $ wnei_know.append("Talk")
            $ hero_mood = "A1"
            hero "What do you usually do, {nm}[fnamewnei]{/nm}?"
            $ wnei_mood = "A4"
            wnei "{bt}{b}EVERYTHING FUN!!!{/b}{/bt}{w=[wt2]} I dance...{w=[wt2]} I watch cartoons on TV...{w=[wt2]} I play games...{w=[wt2]} And now that ya're here, I can go out!!!"
            if wnei_quest[0] < 1:
                $ wnei_quest[0] = 1
                $ hero_mood = "O1"
                hero "Huh?{w=[wt2]} So you couldn't go out before?"
                $ wnei_mood = "O1"
                wnei "Papa don't lemme go out with my friends.{w=[wt3]} He says I'm too naive and people will take advantage of me{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                $ wnei_mood = "A1"
                wnei "Papa don't lemme go out with my friends. He says I'm too naive and people will take advantage of me...{fast} But{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                $ wnei_mood = "A2"
                wnei "Papa don't lemme go out with my friends. He says I'm too naive and people will take advantage of me... But...{fast} Now ya're here, and he has known ya since we were kids.{w=[wt2]}{nw}"
                $ wnei_mood = "A4"
                wnei "Papa don't lemme go out with my friends. He says I'm too naive and people will take advantage of me... But... Now ya're here, and he has known ya since we were kids.{fast} So now I'm sure he won't mind!"
                $ hero_mood = "A1"
                hero "That's cool, {nm}[fnamewnei]{/nm}!{w=[wt1]} let's enjoy our time then! {w=[wt3]}{nw}"
                mind "That's cool, {nm}[fnamewnei]{/nm}! let's enjoy our time then!{fast} (I agree with absolutely everything her 'papa' said,{w=[wt1]} including that I can be trusted, of course!{w=[wt3]} I'm so reliable that he had his daughter's room built next to mine!!{w=[wt1]} Oh, god{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} This man is really my hero...)"
            else:
                hero "Cool!{w=[wt2]} When and where can I see you?"
                $ wnei_mood = "A1"

                if gametimeday >= 2:
                    wnei "Well{w=[wt2]}, I think you can find me at school every week day until afternoon. I run at the sport court on Mondays; Wednesday; and Fridays. Don't worry! I'll visit ya at weekend when I wake up!"
                else:
                    wnei "Don't really know yet{w=[wt2]}, I need to know what I can do in the new school."

        "Ask about which sports she does" if wnei_quest[0] >= 1 and 0 > 1 and is_specialevent == False:
            $ wnei_know.append("Talk")
            $ hero_mood = "A1"
            $ wnei_mood = "A1"
            hero "What kind of sports do you do at school?"
            $ wnei_mood = "A3"
            wnei "Ah!...{w=[wt2]} Our school allows us to participate in two clubs!{w=[wt1]} and that's what I do!{w=[wt3]} I'm in two clubs!{w=[wt1]} the sports club and the swimming club!{w=[wt3]} why don't ya join me!?{w=[wt1]} it'd be very fun!!!"
            hero "That's cool!{w=[wt1]} I'll take a look at your clubs then!{w=[wt2]}{nw}"
            mind "That's cool! I'll take a look at your clubs then!{fast} (Wow{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} so, the school have a pool and a sports court?{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} it seems interesting!)"

        "Return":
            jump wnei_interact

    $ hero_fx = 0
    $ hero_mood = "A1"
    $ gametimemin += 20
    $ add_stat("wnei", "inti", 0.20)
    jump wnei_interact_check

jump wnei_interact_end

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wnei_interact_hangout:
    menu:
        "Train" if Check_CharInMap("hero", "home") and not is_specialevent and (stat_ene >= 10 and times_phy < 1) and (((20 + ((3 + (perk_phy_str * 2)) * (3 + (perk_phy_str * 2)))) * (1 + (stat_phy * 0.01))) >= (21*wnei_size*wnei_size)):

            hero "Wanna help me in my weight training?"
            wnei "Let's go!{w=[wt2]} Until you become super duper powerful!"

            scene bg_0
            with dissolve

            $ Set_CharMap("hero", "home", "bedroom_hero")
            $ Set_CharMap("wnei", "home", "bedroom_hero")
            call check_playermap from _call_check_playermap_12
            call hide_ui from _call_hide_ui_62
            call wnei_show from _call_wnei_show_4

            hero "Let's start!"

            $ times_phy += 2

            scene training_phy_2_bg
            show training_phy_2_hero
            show fx_light:
                blend "add"
            with fade

            $ add_stat("hero", "phy", 2)
            $ add_stat("hero", "ene", -7)
            $ add_stat("hero", "hyg", -(10 + (stat_hyg * 0.3)))
            $ add_stat("wnei", "hyg", -(10 + (stat_hyg * 0.3)))
            $ add_stat("wnei", "inti", 1.2)
            $ add_stat("wnei", "love", 1)
            $ StartAct("wnei", (("staying", "bedroom_hero"), 30), True)

            pause

            $ gametimemin += 30
            call gametime from _call_gametime_28

        "Dance" if Check_CharInMap("hero", "home") and perk_skl_dnc >= 0 and not is_specialevent:
            menu:
                "Dance (OLD)":
                    label wnei_interact_hangout_dance_start:
                        pass
                    hero "Let's dance!"
                    if "DanceEnough" in wnei_know:
                        wnei "{bt}Ehhhh...!?{/bt}{w=[wt3]} Enough dancing for today!"
                        jump wnei_interact
                    elif Check_CharInMap("hero", "home", "living_room"):
                        wnei "{bt}SUUURE!!!{/bt}{w=[wt3]} What kind of music do you want me to play for us?"
                    else:
                        wnei "{bt}SUUURE!!!{/bt}{w=[wt3]} Let's go to the living room!"
                        $ Set_CharMap("hero", "home", "living_room")
                        $ Set_CharMap("wnei", "home", "living_room")
                        call check_playermap from _call_check_playermap_13
                        call hide_ui from _call_hide_ui_63
                        call wnei_show from _call_wnei_show_5
                        wnei "What kind of music do you want me to play for us?"

                    $ a_event_2 = renpy.music.get_playing("BGM")
                    $ a_event_3 = renpy.random.choice(["WNEI_DANCE a", "WNEI_DANCE w", "WNEI_DANCE d", "WNEI_DANCE s"])
                    $ _skipping = False

                    menu:
                        "Sunrise Serenade":
                            stop BGM
                            $ minigamestep = 0.10
                            $ a_event_1 = 104
                            play BGM "audio/Dance - Sunrise Serenade.mp3" noloop

                        "Bubblegum Skies":
                            stop BGM
                            $ minigamestep = 0.10
                            $ a_event_1 = 116
                            play BGM "audio/Dance - Bubblegum Skies.mp3" noloop

                        "Axé" if 0 > 1:
                            stop BGM
                            $ minigamestep = 0.0795
                            $ a_event_1 = 156
                            play BGM "audio/Dance - Axé.mp3"

                        "Forró" if 0 > 1:
                            stop BGM
                            $ minigamestep = 0.154
                            $ a_event_1 = 101
                            play BGM "audio/Dance - Forró.mp3"

                        "Cumbia" if 0 > 1:
                            stop BGM
                            $ minigamestep = 0.154
                            $ a_event_1 = 102
                            play BGM "audio/Dance - Cumbia.mp3"

                        "Cute Pop (Fast Tempo)" if 0 > 1:
                            stop BGM
                            $ minigamestep = 0.10
                            $ a_event_1 = 104
                            play BGM "audio/Dance - Pop (FAST).mp3"

                        "Cute Pop (Average Tempo)" if 0 > 1:
                            stop BGM
                            $ minigamestep = 0.15
                            $ a_event_1 = 115
                            play BGM "audio/Dance - Pop (AVERAGE).mp3"

                        "Cute Pop (Slow Tempo)" if 0 > 1:
                            stop BGM
                            $ minigamestep = 0.20
                            $ a_event_1 = 92
                            play BGM "audio/Dance - Pop (SLOW).mp3"

                    while not (renpy.music.is_playing("BGM")):
                        $ msg.msg(renpy.translate_string("Loading Music..."))
                        $ renpy.pause(1, hard=True)

                    $ _skipping = True
                    $ gametimesec = 0.1
                    show BG_DanceFloor with dissolve
                    call gametimesec from _call_gametimesec
                    call screen dance_screen("hero", "wnei", 1) with dissolve
                    $ renpy.pause(hard=True)

                    label wnei_interact_hangout_dance_end:
                        if "Dance" in wnei_know:
                            $ wnei_know.append("DanceEnough")
                            $ wnei_know.remove("Dance")
                        else:
                            $ wnei_know.append("Dance")
                        stop BGM fadeout 1

                    hide BG_DanceFloor
                    with dissolve

                    play BGM "audio/W2C - Tranquility.mp3"

                    $ a_event_3 = round(a_event_0*((a_event_1/minigamestep)/500000), 2)

                    if a_event_3 > 0:
                        $ add_stat("wnei", "love", 2 + a_event_3)
                        $ add_stat("hero", "cha_per", 2 + a_event_3)

                    $ a_event_4 = a_event_1/4
                    $ gametimemin += round(a_event_4)
                    $ add_stat("wnei", "inti", a_event_4/100)

                    if a_event_0 >= (a_event_1 * 3):
                        wnei "{bt}You're so good at this!!!{/bt} you need to teach me some of your moves!"
                    elif a_event_0 >= a_event_1:
                        wnei "{bt}That was cool!!!{/bt} You're good at this, huh?"
                    elif a_event_0 > 0:
                        wnei "You're doing well. We just need to practice more!"
                    else:
                        wnei "{lg}Shi Hi Hi...{/lg} You dance very weird!"

                "Dance (NEW)":
                    label wnei_interact_hangout_dance_bpm_start:
                        pass
                    hero "Let's dance!"
                    if "DanceEnough" in wnei_know:
                        wnei "{bt}Ehhhh...!?{/bt}{w=[wt3]} Enough dancing for today!"
                        jump wnei_interact
                    elif Check_CharInMap("hero", "home", "living_room"):
                        wnei "{bt}SUUURE!!!{/bt}{w=[wt3]} What kind of music do you want me to play for us?"
                    else:
                        wnei "{bt}SUUURE!!!{/bt}{w=[wt3]} Let's go to the living room!"
                        $ Set_CharMap("hero", "home", "living_room")
                        $ Set_CharMap("wnei", "home", "living_room")
                        call check_playermap from _call_check_playermap_14
                        call hide_ui from _call_hide_ui_64
                        call wnei_show from _call_wnei_show_6
                        wnei "What kind of music do you want me to play for us?"

                    $ a_event_2 = renpy.music.get_playing("BGM")
                    $ _skipping = False

                    python:
                        a_menu_0 = [(Dance_Songs[s]["title"], s) for s in Dance_Songs]
                        a_event_5 = renpy.display_menu(a_menu_0)

                    # The conductor plays the track itself once the lead-in ends.
                    stop BGM
                    $ minigamestep = Dance_Songs[a_event_5]["anim_step"]
                    $ a_event_1 = Dance_Songs[a_event_5]["length"]

                    $ _skipping = True
                    $ gametimesec = 0.1

                    # Phones get the still backdrop — the animated one costs them the frame rate.
                    $ a_event_6 = "BG_DanceFloor_Flat" if Dance_MultiLane() else "BG_DanceFloor"
                    show expression a_event_6 as dancebg with dissolve
                    call gametimesec from _call_gametimesec_1

                    # Rules first, then the track. Screen assets decode while the player reads the rules — loading them mid-song was the main mobile chop.
                    $ Dance_PredictAssets("hero", "wnei")
                    call screen dance_preview_bpm(a_event_5) with dissolve
                    call screen dance_screen_bpm("hero", "wnei", a_event_5)
                    $ renpy.pause(hard=True)

                    label wnei_interact_hangout_dance_end_bpm:
                        $ Dance_StopPredictAssets("hero", "wnei")
                        if "Dance" in wnei_know:
                            $ wnei_know.append("DanceEnough")
                            $ wnei_know.remove("Dance")
                        else:
                            $ wnei_know.append("Dance")
                        stop BGM fadeout 1

                    hide dancebg
                    with dissolve

                    play BGM "audio/W2C - Tranquility.mp3"

                    # Same reward math as the old path, so both variants pay out identically.
                    $ a_event_3 = round(a_event_0*((a_event_1/minigamestep)/500000), 2)

                    if a_event_3 > 0:
                        $ add_stat("wnei", "love", 2 + a_event_3)
                        $ add_stat("hero", "cha_per", 2 + a_event_3)

                    $ a_event_4 = a_event_1/4
                    $ gametimemin += round(a_event_4)
                    $ add_stat("wnei", "inti", a_event_4/100)

                    if a_event_0 >= (a_event_1 * 3):
                        wnei "{bt}You're so good at this!!!{/bt} you need to teach me some of your moves!"
                    elif a_event_0 >= a_event_1:
                        wnei "{bt}That was cool!!!{/bt} You're good at this, huh?"
                    elif a_event_0 > 0:
                        wnei "You're doing well. We just need to practice more!"
                    else:
                        wnei "{lg}Shi Hi Hi...{/lg} You dance very weird!"

        "Ask to follow you" if wnei_is_flw == False and is_specialevent == False and 0 > 1:
            $ wnei_mood = "A3"
            hero "Follow me!"
            wnei "Yaaay!"
            $ wnei_is_flw = True
            $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} is now following you"))
            jump wnei_interact_end
            
        "Dismiss" if wnei_is_flw == True:
            $ wnei_is_flw = False
            $ wnei_mood = "O1"
            hero "I need to do something now..."
            wnei "Ahh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."
            jump wnei_interact_end

        "Invite to watch TV" if is_specialevent == False and Check_CharInMap("wnei", "home") and not Get_ActivityName("wnei") in ["watching tv"]:
            $ hero_mood = "A1"
            hero "Let's watch TV!"

            if wnei_quest_1 >= 1:
                if not "HangOut_WatchTV" in wnei_know:
                    wnei "Let's go!"
                    if not Check_CharInMap("wnei", "home", "living_room"):
                        $ Set_CharMap("hero", "home", "living_room")
                        $ Set_CharMap("wnei", "home", "living_room")
                    $ wnei_know.append("HangOut_WatchTV")
                    call action_watchtv("wnei") from _call_action_watchtv_1
                else:
                    $ wnei_mood = "O1"
                    wnei "Enough of TV!{w=[wt3]} Let's do something fun!"


            else:
                if (gametimeweek == "Saturday" or gametimeweek == "Sunday") and (gametimehour >= 9 and gametimehour <= 11):
                    $ wnei_mood = "A3"

                    $ wnei_know.append("HangOut_WatchTV")
                    $ add_stat("wnei", "love", 1)
                    $ add_stat("hero", "cha_soc", 1)

                    if Check_CharInMap("wnei", "home", "living_room"):
                        wnei "{bt}{b}SURE!!!{/b}{/bt}{w=[wt3]} I'll show you the best cartoon channel!"
                    else:
                        wnei "{bt}{b}SURE!!!{/b}{/bt}{w=[wt3]} Let's go to the living room!"
                        $ Set_CharMap("hero", "home", "living_room")
                        $ Set_CharMap("wnei", "home", "living_room")
                        call check_playermap from _call_check_playermap_15
                        call hide_ui from _call_hide_ui_65
                        call wnei_show from _call_wnei_show_7
                        wnei "I'll show you the best cartoon channel!"

                    jump wnei_quest_0_0
                    $ wnei_is_flw = False

                else:
                    $ wnei_mood = "A1"
                    wnei "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} There's just boring things on TV now.{w=[wt3]} I usually come to watch TV with {nm}[fnamewsis]{/nm} after 9am{w=[wt2]}, when there's super duper cool stuff!"

        "Invite her to go home with you" if gametimehour == 16 and Check_CharInMap("hero", "school"):
            hero "Wanna walk home together?"
            wnei "Sure!{w=[wt2]}{nw}"
            show WNEI at OR_slow
            wnei "Sure!{fast} Lemme call Papa so that he won't come pick me up!"
            scene bg_0
            with dissolve
            if not hero_wear == "school":
                scene bg_0
                with dissolve
                $ hero_wear = "school"
                $ wnei_wear = "school"
                $ msg.msg(renpy.translate_string("You dressed your school uniform."))
                pause(1)

            if wnei_quest_2 < 1:
                jump wnei_quest_2a

            else:
                jump wnei_quest_2b

        "Swim" if hero_map == "School - Swimming Pool" and ((gametimehour < 16) or (gametimehour == 16 and gametimemin < 30)):
            scene socializing_pool_bg 1
            show socializing_pool_wnei
            show socializing_pool_hero listening
            with Fade(1,0,1)

            $ msg.msg(renpy.translate_string("You and {nm}[fnamewnei]{/nm} spend all the afternoon in the swimming area"))

            pause

            scene swimming_test_wnei with Dissolve(1)

            $ hero_fx = 0
            $ hero_mood = "A1"
            $ a_event_0 = 990 - (gametimehour*60)
            call gametime_wait(16, 30) from _call_gametime_wait_8
            $ add_stat("wnei", "love", 60)
            $ add_stat("wnei", "inti", 60)

            pause

            scene bg_0 with Dissolve(1)

            call gametime from _call_gametime_29
            call check_playermap from _call_check_playermap_16
            jump wnei_interact_check

        "Jog" if hero_map == "School - Sports Court" and ((gametimehour < 16) or (gametimehour == 16 and gametimemin < 30)):

            scene socializing_jogging_bg sportcourt
            show socializing_jogging_hero_body 1
            show socializing_jogging_hero_wear 1_school_sport
            show socializing_jogging_hero_face 1a0
            show socializing_jogging_wnei_body 1
            show socializing_jogging_wnei_wear 1_school_sport
            show fx_light:
                blend "add"
            with Fade(1,0,1)

            $ msg.msg(renpy.translate_string("You and {nm}[fnamewnei]{/nm} spend all the afternoon in the sports court"))

            pause

            $ hero_fx = 0
            $ hero_mood = "A1"
            $ a_event_0 = 990 - (gametimehour*60)
            call gametime_wait(16, 30) from _call_gametime_wait_9
            $ add_stat("wnei", "love", 60)
            $ add_stat("wnei", "inti", 60)

            pause

            scene bg_0 with Dissolve(1)

            call gametime from _call_gametime_30
            call check_playermap from _call_check_playermap_17
            jump wnei_interact_check

        "Play a game" if gametimeday == 1 and gametimehour >= 18 and is_specialevent == True and not "WNEI" in scenestep:
            $ scenestep.insert(1, "WNEI")
            $ hero_mood = "A1"
            hero "How about we play something?"
            $ wnei_mood = "A3"
            wnei "{bt=a2-s1-p30}{b}YAAAY!{/b}{/bt}{w=[wt2]} {bt=a3-s1-p20}{b}LET'S GO!!!{/b}{/bt}{w=[wt2]} {bt=a4-s1-p10}{b}IT'LL BE SUPER DUPER FUN!!!{/b}{/bt}"
            $ hero_mood = "A2"
            hero "But I didn't even say what game it was."
            $ wnei_mood = "O2"
            wnei "Oh{w=[wt2]}, That's true!!!{w=[wt3]} What game will we play?"
            hero "Well{w=[wt1]}, I don't know.{w=[wt3]} I didn't bring anything from the countryside{w=[wt2]}, and I still haven't seen what's here to play.{w=[wt3]} I think it's better to ask {nm}[hero_about_wsis]{/nm}."
            $ wnei_mood = "A4"
            wnei "{bt=a2-s1-p25}{b}SUPER DUPER COOL IDEA!!!{/b}{/bt}{nw}{w=[wt2]}"
            show WNEI at OL_average
            wnei "{bt=a2-s1-p25}{b}SUPER DUPER COOL IDEA!!!{/b}{/bt}{fast} {bt=a4-s1-p10}{b}I'LL CALL HER RIGHT NOW!!!{/b}{/bt}"
            hero "{w=[wt1]}. {w=[wt1]}. {w=[wt1]}."

            scene bg_0
            with Dissolve(1)
            $ add_stat("hero", "cha_soc", 2)
            $ add_stat("wnei", "love", 1)
            $ add_stat("wsis", "love", 1)

            scene minigame_boardgamefloor_bg living_room
            show minigame_boardgamefloor_wnei a0
            show minigame_boardgamefloor_wsis a0
            with Dissolve(1)

            pause

            show minigame_boardgamefloor_wnei a1
            wnei "{bt=a2-s1-p25}YAAAY{/bt}{w=[wt1]}, {bt=a2-s1-p50}{b}I WON!!!{/b}{/bt}{w=[wt2]} {bt=a4-s1-p10}TAKE THAT, NOOBS!{/bt}{w=[wt2]}{vspace=15}{bt=a4-s1-p10}{size=60}{b}I'M THE QUEEN!!!{/b}{/size}{/bt}"
            show minigame_boardgamefloor_wnei a0
            show minigame_boardgamefloor_wsis a0
            hero "That was amazing, {nm}[fnamewnei]{/nm}!{w=[wt1]} Congratulations!"
            $a_event_0 = str((int(stat_int * 0.5) + 5))
            show minigame_boardgamefloor_wnei a0
            show minigame_boardgamefloor_wsis a1
            wsis "Yes{w=[wt1]}, congratulations!{w=[wt2]} With that{w=[wt1]}, the score now is:{w=[wt2]}{vspace=1}{nm}[fnamehero]{/nm}:{w=[wt1]} [a_event_0]{w=[wt3]}; {nm}[fnamewsis]{/nm}:{w=[wt1]} 19{w=[wt3]}; {nm}[fnamewnei]{/nm}:{w=[wt1]} 1.{w=[wt4]} {vspace=1}You're the best!"
            show minigame_boardgamefloor_wnei a0
            show minigame_boardgamefloor_wsis a0
            hero "{aw}H{w=[wt1]}-hey!{w=[wt2]} What about what we agreed about letting her have some fun times too!?{/aw}"

            scene bg_home livingroom
            with Fade(2,0,1)
            jump wnei_interact_end

        "Return":
            jump wnei_interact

jump wnei_interact_check

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_wnei:
    $ wnei_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    #elif a_event_0 < 0.1 and "Hero_DickSize" not in wnei_know:
        #wnei "How big is your lollipop now?"
        #hero "Eh!?"

    # ----------------------------------------------------------------------------------------------------
    # Ask what's HERO favorite color
    # ----------------------------------------------------------------------------------------------------
    elif a_event_0 < (wnei_inti*0.004) and not any(get_id.startswith("HERO_F_Color") for get_id in wnei_know):
        # Hero's favorite color
        wnei "What's your favorite color?{nw}"
        menu:
            wnei "What's your favorite color?{fast}"

            "Red":
                $ hero_mood = "A1"
                hero "It's red!"

                $ wnei_know.append("HERO_F_Color_Red")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", -0.1)
                $ add_stat("hero", "cha_soc", -0.1)

                $ wnei_mood = "O1"
                wnei "{aw}Yuck...!{/aw}{w=[wt2]} It reminds me blood.{w=[wt3]} Or{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Ketchup!{w=[wt3]} {aw}YUUUCK...!{/aw}"
                hero "Interesting.{w=[wt2]} Looks like you're more disgusted by ketchup than blood!"
                wnei "Oh no!{w=[wt2]} Stop repeating these words.{w=[wt2]} I'm already starting to feel bad."
                hero "Ketbloop!{w=[wt2]} Bloodshup!"

                $ wnei_mood = "A4"
                wnei "{lg}Shi Hi Hi Hi...{/lg}{w=[wt3]} You managed to create things on a level of disgust super duper beyond normal!{w=[wt2]} {aw}Yuuuck...!{/aw}"

            "Orange":
                $ hero_mood = "A1"
                hero "It's orange!"

                $ wnei_know.append("HERO_F_Color_Orange")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", 0.1)
                $ add_stat("hero", "cha_soc", 0.1)

                $ wnei_mood = "A3"
                wnei "I LUV ORANGE!{w=[wt3]} That's the color of orange soda!{w=[wt2]} {bt}Hmmm...{/bt}"

                $ hero_mood = "O2"
                hero "Hmm?{w=[wt2]} Why it needs to be soda?{w=[wt2]} Why not just orange?"

                $ wnei_mood = "A1"
                wnei "Cos orange soda is orange!"

                $ hero_mood = "A1"
                hero "But orange is orange!"

                $ wnei_mood = "O1"
                wnei "Huh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                $ wnei_mood = "O2"
                wnei "Huh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{fast} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                $ wnei_mood = "A1"
                wnei "Huh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{fast} There are green oranges{w=[wt1]}, but there aren't green orange sodas!{w=[wt2]} That means it's more memorable to remember the orange soda than the fruit!"

                $ hero_mood = "A2"
                hero "Ok{w=[wt2]}, now you broke my arguments."

                $ hero_mood = "A1"
                $ wnei_mood = "A2"
                wnei "You didn't have a chance.{w=[wt3]} My IQ is over 9000!"

                $ wnei_mood = "A4"
                hero "{b}Then answer me this one:{/b}{w=[wt4]} Is orange orange because of orange{w=[wt2]}, or is orange orange because of orange?"

                $ wnei_mood = "O1"
                wnei "Hunf...!{w=[wt2]} Isn't that obvious?{w=[wt2]} Orange is orange cos of the orange{w=[wt2]}, {bt}duuuh...!{/bt}"

                $ wnei_mood = "A4"
                $ hero_mood = "O1"
                hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Well{w=[wt2]}, now I can see it clearly.{w=[wt2]} It seems like my power didn't even reach your feet.{w=[wt2]} Damn it{w=[wt1]}, I can't even see your moves!!!{w=[wt4]} Alright{w=[wt1]}, I accept my defeat."
                wnei "{bt}Fu-hu-huuu...{/bt}{w=[wt2]} Train harder!"

            "Yellow":
                $ hero_mood = "A1"
                hero "It's yellow!"

                $ wnei_know.append("HERO_F_Color_Yellow")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", 0.25)
                $ add_stat("hero", "cha_soc", 0.25)

                $ wnei_mood = "A3"
                wnei "THAT'S A SUPER DUPER COOL COLOR!{w=[wt2]} I LUV YELLOW!"
                hero "It must be because you are a very very happy person.{w=[wt4]} I mean{w=[wt2]}, A super duper happy person!"

                $ wnei_mood = "A4"
                wnei "{lg}Shi Hi Hi Hi...{/lg}{w=[wt3]} Yeah!!{w=[wt2]} I'm a super duper power blaster happy person!!!"
                hero "Ohh!!{w=[wt2]} That's so much happiness."

            "Green":
                $ hero_mood = "A1"
                hero "It's green!"

                $ wnei_know.append("HERO_F_Color_Green")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)

                $ wnei_mood = "A2"
                wnei "Green, huh?{w=[wt2]} Does it remind you the countryside?"
                hero "K{w=[wt1]}-kind of."

                $ wnei_mood = "A1"
                wnei "Ya're cute bumpkin!{w=[wt2]} {gg}Tee-hee...{/gg}"

                $ hero_mood = "O1"
                hero "{aw}Heey!{/aw}"

            "Teal":
                $ hero_mood = "A1"
                hero "It's teal!"

                $ wnei_know.append("HERO_F_Color_Teal")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)

                $ wnei_mood = "A1"
                wnei "That's the color of my old toothbrush."

                $ hero_mood = "O1"
                hero "Oh...{w=[wt2]} What a great thing to represent my favorite color, huh?{w=[wt2]} Thanks!"

                $ wnei_mood = "A3"
                wnei "{bt}Ya're welcum!{/bt}"

            "Blue":
                $ hero_mood = "A1"
                hero "It's blue!"

                $ wnei_know.append("HERO_F_Color_Blue")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)

                $ wnei_mood = "O1"
                wnei "Is that cos ya're a boy?"
                hero "No.{w=[wt2]} It's cos it's blue."
                wnei "But it's blue cos ya're a boy and boys like blue?"
                hero "No!{w=[wt2]} It's blue cos blue is blue and I like blue!"
                wnei "{aw}E{w=[wt1]}-ehh!?{/aw}{w=[wt3]} .{w=[wt2]}.{w=[wt2]}.{w=[wt2]}{nw}"
                wnei "{aw}E{w=[wt1]}-ehh!?{/aw}{w=[wt3]} .{w=[wt2]}.{w=[wt2]}.{w=[wt2]} {bt}Ohhh...!{/bt}{w=[wt3]} Gotcha!{w=[wt3]} In that case, it's all right then!"

            "Purple/Violet":
                $ hero_mood = "A1"
                hero "It's purple!"

                $ wnei_know.append("HERO_F_Color_Purple")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)

                wnei "The color of grape jelly! Or lollipop!"
                hero "Oh{w=[wt1]}, you only remember sweets, huh?{w=[wt2]} No healthy things?"
                wnei "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I don't know{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} It's kinda hard to think in purple things that are not grape and flowers."

                if perk_int_mem >= 1:
                    hero "Oh{w=[wt2]}, that's right!{w=[wt3]} Purple is kind of a rare color in nature.{w=[wt3]} This just must be common in flowers because it makes they stand out more among the green and become more attractive to pollinators."

                    $ add_stat("wnei", "love", perk_int_mem * 0.5)
                    $ add_stat("hero", "cha_soc", perk_int_mem * 0.5)

                    wnei "{pa}SO COOL!{/pa}{w=[wt2]} {bt}Ya're so smart!{/bt} Now I love purple and violet!"

                else:
                    hero "Well{w=[wt2]}, there's eggplant and sweet potato!"
                    wnei "{aw}Yuuuck...!{/aw}{w=[wt2]} I prefer grape jelly and lollipop."
                    hero "Ok{w=[wt1]}, let's go with that then."

            "Pink":
                $ hero_mood = "A1"
                hero "It's pink!"

                $ wnei_know.append("HERO_F_Color_Pink")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", 0.1)
                $ add_stat("hero", "cha_soc", 0.1)

                wnei "{lg}Shi Hi Hi Hi...{/lg}{w=[wt2]} Weird!{w=[wt2]} That's a girls color!"
                hero "But I like girls."
                wnei ".{w=[wt2]}.{w=[wt2]}.{w=[wt4]} Well{w=[wt2]}, in that case{w=[wt2]}, it's all right then, right?"
                hero "Sure!{w=[wt2]} After all{w=[wt2]}, there's a lot of cool things girls have that are pink."
                wnei "Hmmm...?{w=[wt3]} Like what?"
                hero "{aw}E{w=[wt1]}-ehh!?{/aw}{w=[wt3]} W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w} Like-{w=[wt1]}{nw}"
                wnei "{pa}COTTON CANDY!{/pa} Gals like cotton candy!{pr}{bt}I LUV COTTON CANDY! I LUV PINK!{/bt}"
                hero "Y{w=[wt1]}-yeah!{w=[wt2]} That!{w=[wt2]} cotton candy{w=[wt1]}, of course!"

            "Gray":
                $ hero_mood = "A1"
                hero "It's gray!"                

                $ wnei_know.append("HERO_F_Color_Gray")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", 0.25)
                $ add_stat("hero", "cha_soc", 0.25)

                wnei "{bt}Ehhh...!?{w=[wt2]} Weeeird!{/bt}"
                hero "It's not!{w=[wt2]} This world is too colorful.{w=[wt2]} It needs more gray!{w=[wt2]} Gray reminds of the future!"
                wnei "No!{w=[wt2]} It just reminds boring and not cool things.{w=[wt2]} Like{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Huh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} The polution!"
                hero "Exactly!{w=[wt2]} The polution is the future!"
                wnei "{bt}Noooo...!{/bt}"

            "Don't choose":
                jump initiative_wnei_return

    # ----------------------------------------------------------------------------------------------------
    # Ask what kind of games HERO likes
    # ----------------------------------------------------------------------------------------------------
    elif a_event_0 < (wnei_inti*0.006) and not (("HERO_Y_Act_Videogame" in wnei_know) and ("HERO_Y_Act_Sport" in wnei_know) and ("HERO_Y_Act_Boardgame" in wnei_know)):
        # Hero favorite games
        wnei "What kind of games do you like to play?{nw}"
        menu:
            wnei "What kind of games do you like to play?{fast}"

            "Videogames":
                hero "I'm a huge fan of videogames.{w=[wt2]} There's nothing like immersing yourself in a fantasy world and going on epic adventures!"

                $ wnei_know.append("HERO_Y_Act_Videogame")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", 0.25)
                $ add_stat("hero", "cha_soc", 0.25)
                $ stat_int_bonus += 3
                $ msg.msg(renpy.translate_string("{color=#FF3232}3% bonus{/color} for INT gaining"))

                wnei "You're right!{w=[wt2]} That super duper fun!!{w=[wt2]} I love videogames so much that Pappa sold my videogame so I could focus on studies."
                hero "Oh no{w=[wt1]}, that's terrible!{w=[wt2]} But hey{w=[wt1]}, maybe I can invite you to play videogames with me sometime."
                wnei "{pa}REALLY!?{/pa}{w=[wt3]} That would be AMAZING!{w=[wt3]} Where's your videogame!?{w=[wt2]} Let's play right now!!!"
                hero "I haven't one yet"
                wnei "..."

            "Sports/Physical Competitions":
                hero "I kinda like real physical activities."

                $ wnei_know.append("HERO_Y_Act_Sport")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", 0.25)
                $ add_stat("hero", "cha_soc", 0.25)
                $ stat_phy_bonus += 3
                $ msg.msg(renpy.translate_string("{color=#FF3232}3% bonus{/color} for PHY gaining"))

                wnei "Heh{w=[wt2]}, I bet you can't beat me in a race!"
                hero "{bt}Ohhh...?{/bt}{w=[wt2]} Was that a challenge?{w=[wt2]} I don't think I would lose to someone so shorty."
                wnei "Hunf!{w=[wt2]} I've been training my super duper blast speed.{w=[wt3]} Don't complain if you end up swallowing dust{w=[wt1]}, gotcha?{w=[wt3]} Also{w=[wt2]}, who are you calling shorty?{w=[wt2]} I'm BIG!"
                hero "{lg}Ha Ha Ha...{/lg}{w=[wt2]} {bt}Sorry Sorry...{/bt}{w=[wt2]} Y{w=[wt1]}-yeah{w=[wt1]}, you're kinda big in some parts."
                wnei "Huh...?{w=[wt2]} What parts?"
                hero "Oh{w=[wt1]}, well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} y{w=[wt1]}-your{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} your enthusiasm!{w=[wt3]} It's super duper big{w=[wt1]}, right!"
                wnei "YEAH!{w=[wt2]} COS I'M SUPER DUPER COOL!!!"

            "Card and board games":
                hero "I love getting together with friends and family to play card and board games!{w=[wt2]} It's all about strategy{w=[wt1]}, luck{w=[wt1]}, and good company!"

                $ wnei_know.append("HERO_Y_Act_Boardgame")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", 0.25)
                $ add_stat("hero", "cha_soc", 0.25)
                $ stat_cha_bonus += 3
                $ msg.msg(renpy.translate_string("{color=#32FF32}3% bonus{/color} for CHA gaining"))

                wnei "{aw}WE DO NEED TO PLAY THAT!{/aw}{w=[wt3]} You know what?{w=[wt2]} I bet {nm}[fnamewsis]{/nm} may have some board games we could play with her!"
                hero "That sounds like a plan!"
                wnei "{bt}YAY!{/bt}{w=[wt3]} I'll go ask {nm}[fnamewsis]{/nm} if she's up for a game night!{w=[wt2]} It's gonna be super duper fun!"

            "Don't choose":
                jump initiative_wnei_return

    # ----------------------------------------------------------------------------------------------------
    # Ask what kind of movies HERO likes
    # ----------------------------------------------------------------------------------------------------
    elif a_event_0 < (wnei_inti*0.008) and not any(get_id.startswith("HERO_Y_Theme") for get_id in wnei_know):
        # Hero's favorite movies
        wnei "What kind of movies do you like to watch?{nw}"
        label initiative_wnei_HERO_Y_Theme:
            pass
        menu:
            wnei "What kind of movies do you like to watch?{fast}"
            "Action":
                hero "Hmmm{w=[wt1]}, Those with a lot of adrenaline!{w=[wt2]} A punch here{w=[wt1]}, a kick there{w=[wt1]}, a chase here{w=[wt1]}, an explosion there{w=[wt1]}, and things like that.{w=[wt3]} Kinda like{w=[wt1]}, movies where the protagonist solves things instead of crying, you know?"

                $ wnei_know.append("HERO_Y_Theme_Action")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", 0.25)
                $ add_stat("hero", "cha_soc", 0.25)

                wnei "{bt}SURE!{/bt}{w=[wt3]} Like those with super duper frenetic movement{w=[wt1]}, but which arrive at a moment and stay in slow motion for the background thing to explode while the hero slowly walks towards the camera like a boss!"
                hero "Exactly!"

            "Drama/Romance":
                hero "I think I like romantic dramas.{w=[wt2]} They kind of convey a beautiful idea that is being lost nowadays.{w=[wt3]} It's good to see love conquer all{w=[wt1]}, even in the most difficult times."

                $ wnei_know.append("HERO_Y_Theme_Romance")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", 0.25)
                $ add_stat("hero", "cha_soc", 0.25)

                wnei "{bt}Awwn...{/bt}{w=[wt2]} that's cute!{w=[wt3]} Super duper boring, but cute!"

            #"Sci-Fi":
                #hero "Sci-fi!{w=[wt2]} Nothing beats getting lost in a world of futuristic technology.{w=[wt2]} The futuristic settings{w=[wt1]}, the mind-bending concepts—it's like exploring the unknown from the comfort of my couch."

                #$ wnei_know.append("HERO_Y_Theme_SciFi")
                #$ msg.msg("{nm}[fnamewnei]{/nm} knows you a little more")
                #$ add_stat("wnei", "inti", 0.5)
                #$ add_stat("wnei", "love", -0.25)
                #$ add_stat("hero", "cha_soc", -0.25)

                #wnei "Hmm{w=[wt1]}, is that really so?{w=[wt4]} Sci-Fi seems boring to me."

            #"Comedy":
                #hero "I enjoy a good laugh{w=[wt1]}, so comedy classics are my go-to choice!{w=[wt2]} The slapstick humor and witty one-liners always crack me up."

                #$ wnei_know.append("HERO_Y_Theme_Comedy")
                #$ msg.msg("{nm}[fnamewnei]{/nm} knows you a little more")
                #$ add_stat("wnei", "inti", 0.5)
                #$ add_stat("wnei", "love", 0.25)
                #$ add_stat("hero", "cha_soc", 0.25)

                #wnei "{gg}Tee-hee-hee...{/gg}{w=[wt1]} Laughter is the best medicine, they say! That's like having a friend who's always there to make you smile!"
                #hero "There's nothing like a good laugh! Comedy shows always brighten up my day and lift my spirits."

            "Horror/Mystery":
                hero "I kinda like horror thrillers!{w=[wt2]} The suspense{w=[wt1]}, the jump scares{w=[wt1]}, it's all part of the adrenaline rush!"

                $ wnei_know.append("HERO_Y_Theme_Horror")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", -0.25)
                $ add_stat("hero", "cha_soc", -0.25)

                wnei "{aw}Eek!!{/aw}{w=[wt2]} Horror movies!?{w=[wt2]} Not cool!{w=[wt1]} Not cool!{w=[wt1]} It makes me scared!"
                hero "Of course it does.{w=[wt2]} That's the point!"
                wnei "{bt}Not cool...!{w=[wt2]} Not Cool...!{/bt}"

            "Anime/Cartoon":
                hero "I kinda like animations.{w=[wt2]} They awaken a certain childhood nostalgia in me and even give me a feeling of a heartwarming welcome away from reality.{w=[wt3]} It's as if we can disconnect from the real world and forget about our problems."

                $ wnei_know.append("HERO_Y_Theme_Anime")
                $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                $ add_stat("wnei", "inti", 0.5)
                $ add_stat("wnei", "love", 0.5)
                $ add_stat("hero", "cha_soc", 0.5)

                wnei "{bt}YEAH!{/bt}{w=[wt2]} It's like living in a world where anything is possible!{w=[wt2]} {bt}I LUV ANIME!{/bt}{w=[wt2]} I wanted to be a magical girl{w=[wt1]}, like those who have cute stylish clothes and have very very super duper power powerful superpowers!!!"
                hero "So do you like cosplay?"
                wnei "{pa}LUUUV!!!{/pa}{w=[wt3]} On the weekends{w=[wt1]}, I usually come here to hang out with {nm}[fnamewsis]{/nm}, dressing up as magical girls and trying on cool clothes.{w=[wt2]} It's a super duper cool girls night!{w=[wt3]} You really should join us!"
                hero "B{w=[wt1]}-but I'm not a girl."
                wnei "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Oh.{w=[wt3]} You're right.{w=[wt3]} No deal then.{w=[wt3]} You can be left out."
                hero "{bt}Geez...!{/bt}"

            "Porn" if not a_event_0 == 69:
                hero "W{w=[wt1]}-well{w=[wt1]}, I don't really know I should say it."
                wnei "Hmm?{w=[wt2]} Why?"
                hero "M{w=[wt1]}-maybe you don't like the same kind of movie I like."
                wnei "{bt}Ehhh...!?{/bt}{w=[wt2]} Now you made me curious!{w=[wt3]} Tell me!!{w=[wt2]} I bet could watch it together!"
                hero "{aw}Ehhh!?!?{/aw}"
                wnei "What's with this reaction?{w=[wt2]} Come on{w=[wt1]}, say it!{w=[wt2]} What are these movies like?"
                menu:
                    "Say":
                        hero "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} kind of{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} There's usually a guy who gets together with a woman.{w=[wt3]} At the beginning they talk{w=[wt2]}, the conversation must necessarily be meaningless{w=[wt2]}, and the actors must necessarily not know how to talk.{w=[wt2]} Then{w=[wt1]}, suddenly{w=[wt1]}, they start to get naked{w=[wt1]}, and{w=[wt1]}, well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Do some things."
                        wnei "{lg}Shi Hi Hi Hi...{/lg}{w=[wt2]} So weeeird!{w=[wt3]} Why does these movies needs to be like that?"
                        hero "Cos the plot doesn't matter{w=[wt1]}, I guess."
                        wnei "{aw}Ehhh...?{/aw}{w=[wt3]} And what things do they do naked?"
                        hero "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} M{w=[wt1]}-make babies!{w=[wt2]} But without actually making a baby.{w=[wt2]} J{w=[wt1]}-just training, you know."
                        wnei "{bt}Ehhh...?{/bt}{w=[wt2]} So weird...!{w=[wt3]} Why do they{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"

                        $ wnei_know.append("HERO_Y_Theme_Porn")
                        $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                        $ add_stat("wnei", "inti", 0.5)
                        $ add_stat("wnei", "love", -0.5)
                        $ add_stat("hero", "cha_soc", -0.5)

                        wnei "Ehhh...? So weird...! Why do they...{fast}{pr}{pa}EHHH!?!?{/pa}{w=[wt4]} I got what you meant!{w=[wt2]} You watch indecent movies!{w=[wt2]} {aw}Uuugh!{w=[wt2]} That's disgusting!{w=[wt3]} You're a pervert.{/aw}"
                        hero "H{w=[wt1]}-hey!{w=[wt2]} It was you who insisted that I say it!"
                        wnei "{bt}Peeervert...!{w=[wt2]} Peeervert...!{w=[wt2]} La la la la la la...{/bt}"

                    "Choose another thing instead":
                        hero "W{w=[wt1]}-well..."
                        $ a_event_0 = 69
                        jump initiative_wnei_HERO_Y_Theme

            "Don't choose":
                jump initiative_wnei_return

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO likes pop music
    # ----------------------------------------------------------------------------------------------------
    elif a_event_0 < 0.1 and Check_CharInMap("hero", "home", "living_room"):
        if not "DanceEnough" in wnei_know:
            #$ a_event_1 = [get_id for get_id in wnei_know if "HERO_Y_Music" in get_id]
            #wnei "You prefer a_event_1"

            if "HERO_Y_Music_Pop" in wnei_know:
                pass

            elif "HERO_N_Music_Pop" in wnei_know:
                $ wnei_mood = "O1"
                wnei "Uhh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} You don't really like pop, right?{w=[wt2]} I'm bet I can convince you to like it!"
                $ hero_mood = "A1"
                hero "Well{w=[wt2]}, you can try, I guess."

            else:
                $ wnei_mood = "A2"
                wnei "Hey{w=[wt1]}, do you like pop music?{nw}"

                menu:
                    wnei "Hey{w=[wt1]}, do you like pop music?{fast}"

                    "Confirm":
                        $ add_stat("wnei", "love", 0.25)
                        $ add_stat("hero", "cha_soc", 0.25)
                        $ wnei_know.append("HERO_Y_Music_Pop")
                        $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                        $ add_stat("wnei", "inti", 0.5)
                        $ hero_mood = "A3"
                        hero "Sure!{w=[wt2]} I love catchy tunes and upbeat rhythms!"

                        $ hero_mood = "A1"
                        $ wnei_mood = "A3"
                        wnei "{bt}I LUUUV THAT TOO!{/bt}{w=[wt2]} Makes me wanna dance all day!{w=[wt3]} I should show you my super duper cool moves!"
                        hero "So why don't you show me now?{w=[wt2]} I'd love to see!"

                    "Deny":
                        $ wnei_know.append("HERO_N_Music_Pop")
                        $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                        $ add_stat("wnei", "inti", 0.5)
                        $ hero_mood = "A2"
                        hero "W{w=[wt1]}-well{w=[wt2]}, not much."
                        $ wnei_mood = "O1"
                        wnei "{bt}Ehhh...!?{/bt}{w=[wt3]} Saaad!{w=[wt2]} But I bet I can convince you to like it!"
                        hero "Well{w=[wt2]}, you can try, I guess."

                    "Don't choose":
                        jump initiative_wnei_return

            # ----------------------------------------------------------------------------------------------------
            # Ask to dance together
            # ----------------------------------------------------------------------------------------------------
            $ wnei_mood = "A4"
            wnei "{pa}What about we dance together!?{/pa}{w=[wt3]} I have some cool pop songs on my phone that I could play here for us!{w=[wt3]} There are music with different speeds!"
            menu:
                wnei "{pa}What about we dance together!?{/pa}{w=[wt3]} I have some cool pop songs on my phone that I could play here for us!{w=[wt3]} There are music with different speeds!{fast}"
                "Accept":
                    if perk_skl_dnc >= 1:
                        $ add_stat("wnei", "love", 0.25)
                        $ add_stat("hero", "cha_soc", 0.25)
                        jump wnei_interact_hangout_dance_start

                    else:                        
                        $ hero_mood = "A2"
                        hero "I'm not good at dancing{w=[wt2]}, I better just see your moves for now."
                        wnei "So{w=[wt1]}, check it out!"

                        $ wnei_mood = "A1"
                        show WNEI at Dance1
                        pause

                        wnei "Come on!{w=[wt2]} Try it too!"

                        $ hero_fx = 1
                        $ hero_mood = "O1"

                        hero "{aw}E{w=[wt1]}-ehhh...?{w=[wt3]} S{w=[wt1]}-sure!{/aw}"

                        $ wnei_mood = "A4"
                        show HERO at Dance1
                        pause
                        show WNEI at ResetXYZ
                        show WNEI at RC
                        $ renpy.pause(0.1, hard=True)
                        show HERO at ResetXYZ
                        show HERO at LC

                        $ add_stat("wnei", "love", 0.25)
                        $ add_stat("hero", "cha_soc", 0.25)

                        wnei "THAT WAS FUN!!!"

                        $ gametimemin += 10
                        $ add_stat("wnei", "inti", 0.10)

                "Reject":
                    $ hero_mood = "A2"
                    $ wnei_mood = "O1"
                    hero "Well{w=[wt1]}, I kinda don't really feel like it."

                    if "HERO_N_Music_Pop" in wnei_know:
                        $ add_stat("wnei", "love", -0.25)
                        $ add_stat("hero", "cha_soc", -0.25)
                    else:
                        $ add_stat("wnei", "love", -0.1)

                    wnei "{bt}Booo...!{/bt}{w=[wt3]} You boring!{w=[wt3]} {bt}Booo...!{/bt}"

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    elif a_event_0 < 1 and Check_CharInMap("hero", "home", "living_room"):
        if not any(get_id.startswith("HERO_Dated") for get_id in wnei_know):

            wnei "Did ya have a girlfriend were you lived?"

            $ hero_fx = 1
            $ hero_mood = "O1"
            menu:
                wnei "Did ya have a girlfriend were you lived? {fast}"
                
                "Deny":
                    $ a_event_1 = 0
                    $ wnei_know.append("HERO_Dated_N")
                    $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                    $ add_stat("wnei", "inti", 0.5)
                    hero "N{w=[wt1]}-No{w=[wt2]}, I've never dated before."

                    $ wnei_mood = "O1"                    
                    wnei "{bt}Ohh...!{/bt}{w=[wt3]} So I bet there were only super duper boring girls there{w=[wt2]}, then ya got bored cos ya were looking for a super super cool gal{w=[wt2]}, like{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{nw}"

                    $ wnei_mood = "A3"                    
                    wnei "{bt}Ohh...!{/bt}{w=[wt3]} So I bet there were only super duper boring girls there{w=[wt2]}, then ya got bored cos ya were looking for a super super cool gal{w=[wt2]}, like{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{fast} Dunno!{w=[wt2]} What kinda girl do you like?"

                    hero "W{w=[wt1]}-well{w=[wt2]}, Maybe someone like..."

                "Confirm":
                    $ a_event_1 = 1
                    $ wnei_know.append("HERO_Dated_Y")
                    $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                    $ add_stat("wnei", "inti", 0.5)
                    hero "W{w=[wt1]}-well{w=[wt2]}, y{w=[wt1]}-yes{w=[wt2]}, I kinda dated a girl once."

                    $ wnei_mood = "O2"
                    wnei "{pa}Ohh...!{/pa}{w=[wt4]}{nw}"

                    $ wnei_mood = "A3"
                    wnei "{pa}Ohh...!{/pa}{w=[wt4]}{fast} Is that so?{w=[wt2]} How was she like?"
                    hero "W{w=[wt1]}-well{w=[wt2]}, She was like..."

                "Don't choose":
                    jump initiative_wnei_return

        # ----------------------------------------------------------------------------------------------------
        # Ask HERO's girl preference
        # ----------------------------------------------------------------------------------------------------
        elif sum(1 for get_id in wnei_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wnei_know if get_id.startswith("HERO_N_Girl")) < 4:
            wnei "Hey!{w=[wt2]} Tell me more 'bout what kind of girl do you like!{w=[wt2]} Maybe I can introduce ya to some cool friends!{nw}"

            menu:
                wnei "Hey! Tell me more 'bout what kind of girl do you like! Maybe I can introduce ya to some cool friends!{fast}"

                "Answer":
                    $ hero_mood = "A1"
                    hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                    # Count already answered categories
                    $ a_breast_count = sum(1 for get_id in wnei_know if "Breast_" in get_id)
                    $ a_hair_count = sum(1 for get_id in wnei_know if "HairSize_" in get_id)
                    $ a_eye_count = sum(1 for get_id in wnei_know if "EyeShape_" in get_id)
                    $ a_personality_count = sum(1 for get_id in wnei_know if "Personality_" in get_id)

                    # Appearance Likes(Y)/Dislikes(N)
                    $ a_event_1 = wnei_know
                    $ a_event_3 = "initiative_wnei_return"
                    call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_8

                    # Store the answer if one was given
                    if _return:
                        $ wnei_know.append("HERO_Y_Girl_" + _return)

                    $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} knows you a little more"))
                    $ add_stat("wnei", "inti", 0.5)

                    if _return in ["Breast_0", "Breast_1", "HairSize_2", "HairSize_3", "Personality_1", "Personality_3", "EyeShape_1"]: # Match - flat/tiny breasts, short hair, energetic, kind, round eyes (cute)
                        $ add_stat("wnei", "bonus", 10)
                        $ add_stat("hero", "cha_soc", 0.5)
                        $ wnei_mood = "A3"
                        wnei "{bt}WOOOAH{w=[wt2]}, COOL!!!{/bt}{w=[wt4]} I'm sure you'll find a super duper cool girl like that here in the city!{w=[wt2]} Cos ya're a super duper cool dude!"

                    elif _return in ["Breast_4", "Breast_5", "Personality_2", "Personality_9", "HairSize_5", "HairSize_6"]: # Opposite match - huge breasts, dispirited, intelligent, very long hair
                        $ add_stat("wnei", "bonus", -10)
                        $ wnei_mood = "O1"
                        wnei "Hmmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Guess it doesn't make the girl look so cool{w=[wt4]} But no problem!{w=[wt2]} Ya're a super duper cool dude and I'm sure you will easily find a girl the way you like somewhere!{w=[wt3]} After all{w=[wt2]}, there's a lotta not cool girls here in the city!"

                    else: # Others
                        $ wnei_mood = "A1"
                        wnei "Cool!{w=[wt2]} I'm sure you'll find a super duper cool girl like that here in the city!{w=[wt2]} Cos ya're a super duper cool dude!"

                "Don't choose":
                    jump initiative_wnei_return

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:
        wnei "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Nah{w=[wt2]}, nevermind!"
        jump wnei_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("wnei", "inti", 0.20)
    jump wnei_interact_check

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wnei_return:
    hero "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Well{w=[wt2]}, I don't know{w=[wt2]}. I can't think of an answer to this right now."
    wnei "{bt}Ehhh...?{/bt}{w=[wt3]} Maybe you're gettin' old and yar head is stoppin' workin'!"
    hero "{aw}Ehh!?{/aw}"

# ----------------------------------------------------------------------------------------------------
# Touch Options
# ----------------------------------------------------------------------------------------------------
screen wnei_pat():
    timer 0.1 repeat True action [SetVariable("a_event_1", max(0, min(100, a_event_1 + a_event_0))), If(a_event_1 < 100, false=Jump("wnei_interact_touch_headpat"))]

    modal True
    key "mousedown_1" action SetVariable("a_event_0", 5)
    key "mouseup_1" action SetVariable("a_event_0", -0.5)

    if a_event_2 > 0.66:
        image "bg_2 pink"
    elif a_event_2 > 0.33:
        image "bg_2 yellow"
    else:
        image "bg_2 flowers"

    image "bg_fx1"

    if a_event_0 <= 0:
        image "action_wnei_pat_wnei_bg"
    else:
        image "action_wnei_pat_wnei_bg" at PatHead

    image "action_wnei_pat_wnei_body"

    if wnei_wear == "school":
        image "action_wnei_pat_outfitwnei school"
    elif wnei_wear == "school_swim":
        image "action_wnei_pat_outfitwnei school_swim"
    elif wnei_wear == "school_sport":
        image "action_wnei_pat_outfitwnei school_sport"
    else:
        image "action_wnei_pat_outfitwnei common1"

    if a_event_0 <= 0:
        image "action_wnei_pat_wnei_fg"
        image "action_wnei_pat_wnei_face 1"
        if a_event_1 >= 60:
            image "action_wnei_pat_wnei_fx"
    else:
        image "action_wnei_pat_wnei_fg" at PatHead
        image "action_wnei_pat_wnei_face 2" at PatHead
        if a_event_1 >= 60:
            image "action_wnei_pat_wnei_fx" at PatHead

    image "action_wnei_pat_hero_body"

    if hero_wear == "school":
        image "action_wnei_pat_outfithero school"
    elif hero_wear == "school_swim":
        image None
    elif hero_wear == "school_sport":
        image "action_wnei_pat_outfithero school_sport"
    else:
        image "action_wnei_pat_outfithero common1"
    if a_event_0 <= 0:
        image "action_wnei_pat_hero_hand"
    else:
        image "action_wnei_pat_hero_hand" at PatHand

    vbox:
        xpos 25
        ypos 25
        vbar:
            xysize(150,150)
            value AnimatedValue(a_event_1, 100, delay=1)
            left_bar "gui/CustomBar/LoveMin.webp" at Zoom_2
            right_bar "gui/CustomBar/LoveMax.webp"
