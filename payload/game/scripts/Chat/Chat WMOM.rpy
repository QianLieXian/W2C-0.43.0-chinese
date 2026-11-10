# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wmom_show:

    if wmom_love <= -20:
        $ wmom_mood = "O2"
    elif wmom_love < 0:
        $ wmom_mood = "A2"
    elif wmom_love >= 0:
        $ wmom_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_7

    if wmom_wear == "under":
        $ hero_fx = 2

    show WMOM at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wmom_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewmom][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wmom")))))

    if Get_ActivityName("wmom") in ["staying", "cleaning", "reading"]:
        return

    elif Get_ActivityName("wmom") in ["eating"]:
        jump show_ui

    elif Get_ActivityName("wmom") in ["changing"]:
        scene wmom_actview2_bg_1
        show wmom_actview2_bg_2
        show wmom_actview2_wmom_body
        show wmom_actview2_wmom_face o0
        show fx_light:
            blend "add"
        with fade
        pause
        show wmom_actview2_wmom_face o1

        pause(1)

        hero "{aw}S{w=[wt1]}-sorry!{w=[wt2]} I should have knocked!{/aw}"

        if wmom_inti >= 20:
            show wmom_actview2_wmom_face a1
            wmom "Oh{w=[wt2]}, [wmom_to_hero]!{w=[wt2]} Come here!{w=[wt2]} Can you help me to take my bra off?"

            show wmom_actview2_wmom_face a0 with None

            scene wmom_actview3_bg
            show wmom_actview3_char_body 1
            show wmom_actview3_hero_wear 1_home
            show wmom_actview3_hero_face s0
            show wmom_actview3_wmom_face a0
            show fx_light:
                blend "add"
            with fade
            pause

            play SE1 "Bounce5.mp3"

            show wmom_actview3_char_body 2
            show wmom_actview3_hero_wear 2_home
            show wmom_actview3_wmom_face a0
            with dissolve

            pause

            show wmom_actview3_wmom_face a1

            wmom "{bt}Ahhh...{/bt}{w=[wt2]} Way better...!{w=[wt3]} Thank you, [wmom_to_hero]!"

            $ add_stat("wmom", "love", 1)
            $ add_stat("wmom", "inti", 1)
            $ add_stat("hero", "cha_soc", 1)

            show wmom_actview3_wmom_face a0 with None

            $ gametimemin += 10

        scene bg_0 with dissolve

        jump show_ui

    elif Get_ActivityName("wmom") in ["masturbating"]:
        scene bg_0
        show action_masturbate_bg wmom_bedroom wmom_1
        show fx_light
        pause
        show action_masturbate_bg wmom_bedroom wmom_2

    elif Get_ActivityName("wmom") in ["sleeping"]:
        if wmom_lust >= 50:
            scene bg_0
            show action_masturbate_bg wmom_bedroom wmom_1
            show fx_light
            pause
            show action_masturbate_bg wmom_bedroom wmom_2
        else:
            scene wmom_massage1_bg
            show wmom_massage1_wmom
            show wmom_massage1_face a0
        pause
        jump show_ui

    elif Get_ActivityName("wmom") in ["changing"]:
        scene wmom_is_changing_1_bg
        pause

        hero "Oops{w=[wt2]}, sorry!"
        jump show_ui

    elif Get_ActivityName("wmom") in ["exercising"]:
        scene wmom_yoga1_bg
        show wmom_yoga1_wmom 0
        with Dissolve(2)

        show wmom_yoga1_wmom 1
        wmom "What a surprise, {nm}[wmom_to_hero]{/nm}!{w=[wt2]} Wanna join me to my yoga workout?"

        show wmom_yoga1_wmom 0 with None

        menu:
            wmom "What a surprise, {nm}[wmom_to_hero]{/nm}! Wanna join me to my yoga workout?{fast}"

            "Accept":
                show wmom_yoga1_wmom 0
                hero "Sure!"

                show wmom_yoga1_wmom 1
                wmom "Go wear a more comfortable outfit {nm}[wmom_to_hero]{/nm}.{w=[wt2]} I'll wait for you!"
                show wmom_yoga1_wmom 0
                hero "I won't take long."
                call hide_ui from _call_hide_ui_47
                scene bg_0
                with Dissolve(1)
                jump wmom_yoga_0_0

            "Refuse":
                show wmom_yoga1_wmom 0
                hero "Oh, sorry.{w=[wt2]} I can't join you now."

                show wmom_yoga1_wmom 1
                wmom "{aw}Ehhh...?{/aw}{w=[wt2]} {bt}So sad...{/bt}{w=[wt3]} By the way{w=[wt2]}, you can join me whenever you have time {nm}[wmom_to_hero]{/nm}!"

        show wmom_yoga1_wmom 0 with None

        scene bg_0
        with dissolve

        jump wmom_interact_end

    elif wmom_activity_current == "cooking":
        scene wmom_actview1_bg
        show wmom_actview1_wmom_body
        show wmom_actview1_wmom_wear_1 under
        if wmom_wear == "home":
            show wmom_actview1_wmom_wear_2 home
        elif wmom_wear == "sleep":
            show wmom_actview1_wmom_wear_2 sleep
        elif wmom_wear == "casual":
            show wmom_actview1_wmom_wear_2 casual
        show wmom_actview1_wmom_head
        show fx_light:
            blend "add"
        with fade

        menu:
            "Talk":
                pass

            "Hug":
                $ a_event_0 = "HugBack"
                jump wmom_interact_touch_hug

            "Return":
                jump show_ui

    hero "Hi, [C_Nam][hero_to_wmom][C_Off]."

    call check_playermap from _call_check_playermap_7
    call hide_ui from _call_hide_ui_48
    show WMOM at RC
    show HERO at LC
    with fade
    return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wmom_interact_end:
    if "interacting_hero" in wmom_know:
        $ wmom_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wmom_interact_start:
    call hide_ui from _call_hide_ui_49
    call wmom_show_activity from _call_wmom_show_activity
    $ wmom_inti = min(wmom_inti_cap, wmom_inti)
    call hide_ui from _call_hide_ui_50
    call wmom_show from _call_wmom_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wmom_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if Check_CharSameMap("hero","wmom"):
        pass

    # ----------------------------------------------------------------------------------------------------
    # Is on bed about to sleep
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero","home","hallway") and gametimehour == 20:
        if "interacting_hero" not in wmom_know:
            scene bg_0 with dissolve
            jump wmom_massage

    # ----------------------------------------------------------------------------------------------------
    # Is not there
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero","home","hallway") and not (gametimehour <= 5 or gametimehour >= 21):
        play SE1 "DoorKnock.ogg"
        pause 0.2
        play SE1 "DoorKnock.ogg"
        pause 0.2
        play SE1 "DoorKnock.ogg"
        pause 1.0

        if Check_CharInMap("hero","home","bedroom_wmom"):
            play SE1 "DoorOpen1.ogg"
            $ Set_CharMap("hero", "home", "wmom_bedroom")
            scene bg_home bedroom wmom with fade
        else:
            mind "(I think she isn't here.)"
            jump wmom_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Is sleeping
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero","home","hallway") and (gametimehour <= 5 or gametimehour >= 21):
        play SE1 "DoorKnock.ogg"
        pause 0.2
        play SE1 "DoorKnock.ogg"
        pause 0.2
        play SE1 "DoorKnock.ogg"
        pause 1.0

        mind "(I think she's sleeping.)"
        jump wmom_interact_end

    jump wmom_interact_check

# ----------------------------------------------------------------------------------------------------
# Check Screen
# ----------------------------------------------------------------------------------------------------
label wmom_screen_check:
    $ a_event_0 = wmom_wear
    call check_playermap from _call_check_playermap_8
    call hide_ui from _call_hide_ui_51
    $ wmom_wear = a_event_0
    call wmom_show from _call_wmom_show_1
    return

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wmom_interact_check:
    # Save current outfit before any updates
    $ wmom_wear_keep = wmom_wear

    call gamecheck from _call_gamecheck_9
    call gametime from _call_gametime_23
    call hide_ui from _call_hide_ui_52

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wmom_wear != wmom_wear_keep:
        $ wmom_wear = wmom_wear_keep

    call wmom_show from _call_wmom_show_2

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    # Lunch
    if (gametimehour == 10 and gametimemin >= 30) or (gametimehour == 11):
        wmom "Mama needs to prepare our lunch now, okay {nm}[wmom_to_hero]{/nm}?"
        jump wmom_interact_end

    # Going to work
    elif (not Check_CharSameMap("hero","wmom")) and Check_CharInMap("hero","home","living_room") and not Check_CharInMap("wmom","home") and not gametimeweek == "Sunday":
        wmom "Breakfast is ready, {nm}[wmom_to_hero]{/nm}!{w=[wt2]} I have to go now.{w=[wt1]}{nw}"
        show WMOM at LC_slow
        wmom "Breakfast is ready, {nm}[wmom_to_hero]{/nm}! I have to go now.{fast} Keep your sis company, okay?{w=[wt1]}{nw}"
        play SE1 "Kiss.ogg"
        wmom "Breakfast is ready, {nm}[wmom_to_hero]{/nm}! I have to go now. Keep your sis company, okay? (Kiss){fast}{w=[wt1]}{nw}"
        $ hero_fx = 1
        show WMOM at OL_slow
        wmom "Breakfast is ready, {nm}[wmom_to_hero]{/nm}! I have to go now. Keep your sis company, okay? (Kiss){fast}{w=[wt1]} {pr}{bt}Bye Bye!{/bt}"
        $ hero_fx = 0
        jump wmom_interact_end

    # Sleeping
    elif Get_ActivityName("wmom") in ["sleeping"]:
        wmom "It's time for mommy to sleep, {nm}[wmom_to_hero]{/nm}.{w=[wt3]} Don't stay up too late, okay?"
        hero "Good night {nm}[hero_to_wmom]{/nm}."
        wmom "Good night {nm}[wmom_to_hero]{/nm}."
        $ Set_CharMap("hero", "home", "hallway")
        jump wmom_interact_end

    # Changed map
    elif (not Check_CharSameMap("hero","wmom")) and (not Check_CharInMap("hero","home","hallway")):
        wmom "Mommy needs to leave now, {nm}[wmom_to_hero]{/nm}."
        jump wmom_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Special Event: Dinner
    # ----------------------------------------------------------------------------------------------------
    if gametimeday == 1 and gametimehour >= 18 and is_specialevent == True and not "WMOM" in scenestep:
        wmom "Are you having fun, {nm}[wmom_to_hero]{/nm}?"

    # ----------------------------------------------------------------------------------------------------
    # Special Event: Grocery Store
    # ----------------------------------------------------------------------------------------------------
    elif hero_quest_1 < 3 and (gametimehour >= 12 and gametimehour <= 17):
        wmom "{bt}Ara ara...{/bt}{w=[wt2]} Go call your sis to the grocery store {nm}[wmom_to_hero]{/nm}!"
        jump wmom_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wmom_know:
        call wmom_screen_check from _call_wmom_screen_check
        $ a_event_0 = renpy.random.random()

        # ----------------------------------------------------------------------------------------------------
        # Bring Up A Topic
        # ----------------------------------------------------------------------------------------------------
        if renpy.random.random() < (0.2 + (wmom_love * 0.003)):
            jump initiative_wmom

        # ----------------------------------------------------------------------------------------------------
        # No hug today
        # ----------------------------------------------------------------------------------------------------
        elif renpy.random.random() < 0.5 and not "Hug" in wmom_know:
            if a_event_0 < 1/4:
                wmom "Oh {nm}[wmom_to_hero]{/nm}{w=[wt2]}, come here!{w=[wt3]} Mama missed you so much!"
            elif a_event_0 < 2/2:
                wmom "{bt}Hm..?{/bt}{w=[wt3]} Where's mama's hug?"
            elif a_event_0 < 3/4:
                wmom "{bt}Ara Ara...{/bt}{w=[wt2]} Aren't you forgetting anything?"
            else:
                wmom "I don't think you gave me a hug today."
            menu:
                "Hug":
                    jump wmom_interact_touch_hug
                "Refuse":
                    hero "W{w=[wt1]}-well{w=[wt2]}, let's leave it for another time."
                    wmom "{aw}Ehhh...!?{/aw}{w=[wt3]} Stop being so shy!"

        # ----------------------------------------------------------------------------------------------------
        # Hug today
        # ----------------------------------------------------------------------------------------------------
        elif renpy.random.random() < 0.2 and "Hug" in wmom_know:
            if a_event_0 < 1/2:
                wmom "{bt}Ara ara...{/bt}{w=[wt2]} I love my big boy's hug!"
            else:
                wmom "Don't be ashamed to give me another hug whenever you want, okay {nm}[wmom_to_hero]{/nm}?"

        # ----------------------------------------------------------------------------------------------------
        # WMOM is talking with HERO
        # ----------------------------------------------------------------------------------------------------
        elif renpy.random.random() < 0.2 and "Talk" in wmom_know:
            if a_event_0 < 1/3:
                wmom "Mama loves talking to you {nm}[wmom_to_hero]{/nm}."
            if a_event_0 < 2/3:
                wmom "{bt}Ara ara...{/bt}{w=[wt2]} I still wanna know more about you {nm}[wmom_to_hero]{/nm}."
            else:
                wmom "{bt}Ara ara...{/bt}{w=[wt2]} That was an interesting topic, right {nm}[wmom_to_hero]{/nm}?"

        # ----------------------------------------------------------------------------------------------------
        # Common
        # ----------------------------------------------------------------------------------------------------
        elif a_event_0 < 1/6:
            wmom "{bt}Ara ara...{/bt}{w=[wt2]} have I told you today that I love you?"
        elif a_event_0 < 2/6:
            wmom "{bt}Ara ara...{/bt}{w=[wt2]} Look at my big boy...!"
        elif a_event_0 < 3/6:
            wmom "By the way{w=[wt2]}, thank you for spending time with me {nm}[wmom_to_hero]{/nm}!"
        elif a_event_0 < 4/6:
            wmom "You know what?{w=[wt2]} I'm so glad you're back {nm}[wmom_to_hero]{/nm}!{w=[wt3]} I love you!"
        elif a_event_0 < 5/6:
            wmom "You know what?{w=[wt2]} I'm happy that we are spending time together again!"
        else:
            wmom "I love these moments we spend together {nm}[wmom_to_hero]{/nm}."

        jump wmom_interact

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_0 = renpy.random.random()
        if not "Greeting" in wmom_know:
            $ wmom_know.append("Greeting")
            if gametimehour >= 5 and gametimehour < 12:
                if "HERO_2_Fridge" in wmom_know:

                    $ wmom_know.remove("HERO_2_Fridge")
                    $ add_stat("wmom", "love", 1)
                    $ add_stat("wmom", "inti", 1)
                    $ add_stat("hero", "cha_soc", 1)

                    $ wmom_fx = 1
                    $ wmom_mood = "A2"

                    if a_event_0 < 1/5:
                        wmom "Good morning, {nm}[wmom_to_hero]{/nm}!{w=[wt3]} Oh my{w=[wt2]}, I noticed the fridge is fuller today!{w=[wt3]} Did you go shopping yesterday?{w=[wt4]} {bt}Ara ara...{/bt}{w=[wt2]} You really shouldn't be spending your money on us like that."
                        
                        $ hero_mood = "A2"
                        hero "It's no big deal, {nm}[hero_to_wmom]{/nm}.{w=[wt3]} I just wanted to help out."
                        
                        $ wmom_mood = "A3"
                        wmom "Such a thoughtful boy!{w=[wt3]} But you know{w=[wt1]}, I can handle the grocery shopping.{w=[wt3]} You should save your money for things you want.{w=[wt4]} Still{w=[wt2]}, it does help tremendously.{w=[wt3]} Come here, sweetheart."

                    elif a_event_0 < 2/5:
                        wmom "{bt}Ara ara...{/bt}{w=[wt2]} Someone was busy shopping, I see!{w=[wt3]} The fridge looks so much better now, {nm}[wmom_to_hero]{/nm}!{w=[wt4]} But honey{w=[wt2]}, you don't have to spend your allowance on groceries.{w=[wt3]} That's my responsibility."
                        
                        $ hero_mood = "A2"
                        hero "I don't mind helping out, {nm}[hero_to_wmom]{/nm}."
                        
                        $ wmom_mood = "O1"
                        wmom "But{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"

                        $ wmom_mood = "A2"
                        wmom "But...{fast} Nevermind, {nm}[wmom_to_hero]{/nm}.{w=[wt2]} We're a family, right?{w=[wt3]} I'm so blessed to have you back with us.{w=[wt4]} I promise I'll make you a special breakfast with some of these ingredients!{w=[wt3]} But first{w=[wt1]}, come give {nm}mommy{/nm} a hug!"

                    elif a_event_0 < 3/5:
                        wmom "Good morning, {nm}[wmom_to_hero]{/nm}!{w=[wt3]} {bt}Ara ara...{/bt}{w=[wt2]}, I was so surprised when I opened the fridge this morning!{w=[wt4]} All those new groceries!{w=[wt3]} You shouldn't have, {nm}[wmom_to_hero]{/nm}{w=[wt2]}, really."
                        
                        $ wmom_mood = "O1"
                        wmom "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I hope you didn't spend too much.{w=[wt3]} Things must be so expensive these days.{w=[wt4]} But I admit it's a huge help.{w=[wt3]} Things have been a little{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Well{w=[wt2]}, never mind that."
                        
                        $ hero_mood = "A2"
                        hero "Is everything okay, {nm}[hero_to_wmom]{/nm}?"
                        
                        $ wmom_mood = "A2"
                        wmom "Oh!{w=[wt2]} Of course, sweetheart!{w=[wt3]} Everything's perfect now that you're here!{w=[wt4]} And you're so thoughtful too!{w=[wt3]} Come here{w=[wt2]}, you deserve a big hug!"

                    elif a_event_0 < 4/5:
                        wmom "Oh, {nm}[wmom_to_hero]{/nm}!{w=[wt3]} I was just thinking about you!{w=[wt3]} I saw what you did with the fridge.{w=[wt3]} You shouldn't have worried about that!{w=[wt4]} {bt}Ara ara...{/bt}{w=[wt2]} Such a responsible young man you've become!"
                        
                        $ hero_mood = "A2"
                        hero "I just picked up a few things.{w=[wt3]} No big deal."
                        
                        $ wmom_mood = "A2"
                        wmom "For me that was already a lot, {nm}[wmom_to_hero]{/nm}.{w=[wt2]} Thank you.{w=[wt4]} {bt}Awnn...{/bt}{w=[wt2]} {nm}Mommy{/nm} is so lucky to have her big boy back home!{w=[wt3]} Come here{w=[wt2]}, let me show you how much I appreciate your help!"
                        
                    else:
                        wmom "{bt}Ara ara...{/bt}{w=[wt2]} Good morning, {nm}Sunshine{/nm}!{w=[wt3]} What a surprise I had this morning!{w=[wt4]} The fridge looked so full today!{w=[wt3]} Did you do that, {nm}[wmom_to_hero]{/nm}?"
                        
                        $ hero_mood = "A2"
                        hero "Oh{w=[wt2]}, yeah{w=[wt2]}, I thought we could use some more food.{w=[wt3]} Hope that's okay."
                        
                        $ wmom_mood = "A2"
                        wmom "Okay?{w=[wt3]} It's more than okay, honey!{w=[wt4]} Though I feel a little guilty.{w=[wt3]} I invited you to live with us{w=[wt2]}, and here you are spending your money on household things.{w=[wt3]} That should be my job."
                        
                        $ wmom_mood = "O1"
                        wmom "Things have been a bit{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} tight lately with work{w=[wt2]}, but I was managing.{w=[wt4]} I didn't want you or {nm}[fnamewsis]{/nm} to worry about anything."
                        
                        $ hero_mood = "A2"
                        hero "You don't have to handle everything alone anymore, {nm}[hero_to_wmom]{/nm}.{w=[wt3]} I'm here now."
                        
                        $ wmom_mood = "A2"
                        wmom "Oh, sweetheart!{w=[wt3]} What would I do without you?{w=[wt4]} Come here and let me hug my wonderful {nm}[wmom_to_hero]{/nm}!"
                        
                    jump wmom_interact_touch_hug

                elif a_event_0 < 1/3:
                    wmom "{bt}Ara ara...{/bt}{w=[wt2]} Good morning {nm}[wmom_to_hero]{/nm}!"
                elif a_event_0 < 2/3:
                    wmom "Nice to see you {nm}[wmom_to_hero]{/nm}.{w=[wt3]} Good morning!"
                else:
                    wmom "Oh{w=[wt1]}, {nm}[wmom_to_hero]{/nm}.{w=[wt2]} Good morning!"
                hero "Good morning {nm}[hero_to_wmom]{/nm}."

            elif gametimehour >= 12 and gametimehour < 18:
                if a_event_0 < 1/3:
                    wmom "{bt}Ara ara...{/bt}{w=[wt2]} Good afternoon {nm}[wmom_to_hero]{/nm}!"
                elif a_event_0 < 2/3:
                    wmom "Nice to see you {nm}[wmom_to_hero]{/nm}.{w=[wt3]} Good afternoon!"
                else:
                    wmom "Oh{w=[wt1]}, {nm}[wmom_to_hero]{/nm}.{w=[wt3]} Good afternoon!"
                hero "Good afternoon {nm}[hero_to_wmom]{/nm}."

            elif gametimehour >= 18 and gametimehour < 22:
                if a_event_0 < 1/3:
                    wmom "{bt}Ara ara...{/bt}{w=[wt2]} Good evening {nm}[wmom_to_hero]{/nm}!"
                elif a_event_0 < 2/3:
                    wmom "Nice to see you {nm}[wmom_to_hero]{/nm}.{w=[wt3]} Good evening!"
                else:
                    wmom "Oh{w=[wt1]}, {nm}[wmom_to_hero]{/nm}.{w=[wt3]} Good evening!"
                hero "Good evening {nm}[hero_to_wmom]{/nm}."

        elif gametimehour <= 7 and gametimehour >= 5 and gametimeweek == "Sunday":
            wmom "Today mama can give you full attention!{w=[wt2]} {gg}Tee-Hee...{/gg}"

        elif gametimeday == 2 and gametimehour <= 7 and gametimehour >= 5:
            wmom "Are you looking forward to know your new school?{w=[wt2]} You need to go with your sister on the first day, since you don't know the place.{w=[wt2]} So please don't be late and keep her company, okay?"

        elif gametimehour <= 7 and gametimehour >= 5:
            wmom "The breakfast is about done, and I'll need to leave soon.{w=[wt2]} So, wait your sister and keep her company, okay?"

        elif (renpy.random.random() * (wmom_inti*0.01)) < 0.05:
            if a_event_0 < 1/3:
                wmom "{bt}Ara ara...{/bt}{w=[wt2]} I'm so glad you're back {nm}[wmom_to_hero]{/nm}!{w=[wt3]} I love you."
            elif a_event_0 < 2/3:
                wmom "{bt}Ara ara...{/bt}{w=[wt2]} I'm so glad you're back!{w=[wt3]} I love you {nm}[wmom_to_hero]{/nm}."
            else:
                wmom "{bt}Ara ara...{/bt}{w=[wt2]} I'm so glad my big boy is back!{w=[wt3]} I love you."

        elif (renpy.random.random() * (wmom_inti*0.01)) < 0.1:
            if a_event_0 < 0.5:
                wmom "Did you missed mama too {nm}[wmom_to_hero]{/nm}?"
            else:
                wmom "Oh, {nm}[wmom_to_hero]{/nm}.{w=[wt2]} I still don't believe you are back."
        else:
            if a_event_0 < 1/4:
                wmom "Hi {nm}[wmom_to_hero]{/nm}!{w=[wt2]} What can I do for you?"
            elif a_event_0 < 2/4:
                wmom "Wanna chat {nm}[wmom_to_hero]{/nm}?"
            elif a_event_0 < 3/4:
                wmom "Hello {nm}[wmom_to_hero]{/nm}!"
            else:
                wmom "Hi {nm}[wmom_to_hero]{/nm}!"

        jump wmom_interact

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wmom_interact:
    call hide_ui from _call_hide_ui_53
    call wmom_screen_check from _call_wmom_screen_check_1
    if "interacting_hero" not in wmom_know:
        $ wmom_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wmom_interact_chat
        "Touch" if not is_specialevent:
            jump wmom_interact_touch
        "Meet" if wnei_quest_6 >= 1: # if wmom_inti >= 50
            jump wmom_interact_meet
        "Hang out":
            jump wmom_interact_hangout
        "Give item" if not is_specialevent:
            jump wmom_interact_gift
        "Return":
            jump wmom_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wmom_interact_gift:
    $ a_item_8 = "wmom"
    $ a_item_9 = 0
    $ a_item_6 = "wmom_interact"
    call UI_give_Item from _call_UI_give_Item_8

label wmom_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wmom_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wmom_interact_touch:
    menu:
        "Hug" if is_specialevent == False:
            label wmom_interact_touch_hug:
                pass

            $ X_spd = 4
            $ X_pos = -165
            $ X_pos2 = -85
            $ Y_pos = -530
            $ X_pos2 = 30
            $ Y_pos2 = -40
            $ Z_Rot = 10

            if a_event_0 == "HugBack":
                scene wmom_actview1_hug_bg
                show wmom_actview1_hug_char_body
                show wmom_actview1_hug_hero_wear_bg home
                if wmom_wear == "under":
                    show wmom_actview1_hug_wmom_wear under
                elif wmom_wear == "sleep":
                    show wmom_actview1_hug_wmom_wear sleep
                else: # "casual" missing
                    show wmom_actview1_hug_wmom_wear home
                show wmom_actview1_hug_hero_wear_fg home
                show wmom_actview1_hug_hero_face a0
                show wmom_actview1_hug_wmom_face o0
                show fx_light

            else:
                $ a_event_0 = renpy.random.random()
                if a_event_0 > 0.66:
                    scene bg_2 pink
                elif a_event_0 > 0.33:
                    scene bg_2 yellow
                else:
                    scene bg_2 flowers
                show bg_fx0
                show action_wmom_hug_body

                if hero_wear == "sport":
                    show action_wmom_hug_outfithero sport
                else:
                    show action_wmom_hug_outfithero home

                if wmom_wear == "home":
                    show action_wmom_hug_outfitwmom home
                elif wmom_wear == "casual":
                    show action_wmom_hug_outfitwmom casual
                elif wmom_wear == "sport":
                    show action_wmom_hug_outfitwmom sport
                elif wmom_wear == "under":
                    show action_wmom_hug_outfitwmom under
                show action_wmom_hug_hand at PatHand

            with dissolve

            $ wmom_know.append("Hug")
            $ a_event_0 = 3 / sum(1 for buceta in wmom_know if buceta == "Hug")

            if perk_cha_sex >= 1:
                $ add_stat("wmom", "lust", 2)

            $ add_stat("wmom", "love", a_event_0)
            $ add_stat("hero", "cha_sex", a_event_0)

            pause

            call gamecheck from _call_gamecheck_10
            call hide_ui from _call_hide_ui_54
            call wmom_show from _call_wmom_show_3

            $ gametimemin += 20
            $ add_stat("wmom", "inti", 0.2)

            jump wmom_interact_check

        "Return":
            jump wmom_interact


# ----------------------------------------------------------------------------------------------------
label wmom_interact_meet: # Invite Options
# ----------------------------------------------------------------------------------------------------
    menu:
        "Reunion on Neighbor's {pr}[C_Dat](⏰ Sunday - 10:00-12:59)[C_Off]" if wnei_quest_6 >= 1 and "wmom" not in wnei_quest_7:

            if "Neighbors_Reunion" in wmom_know:
                hero "So{w=[wt2]}, will you go with me to the neighbor's house Sunday?"

                if Check_TaskCompletion("clean_home") >= 100 and Check_TaskCompletion("wash_home") >= 100 and gametimeweek == "Saturday":
                    wmom "Of course, [C_Nam][wmom_to_hero][C_Off]!{w=[wt2]} I'm so proud of you.{w=[wt3]} You took care of the house chores for your dear mama! ~❤️{w=[wt1]} {gg}Tee-hee...{/gg}"

                elif Check_TaskCompletion("clean_home") >= 90 and Check_TaskCompletion("wash_home") >= 90:
                    wmom "Oh, [C_Nam][wmom_to_hero][C_Off]...{w=[wt2]} You managed to leave the house very clean!{w=[wt3]} I'm so proud of you!{w=[wt2]} Sure!{w=[wt2]} If it keeps this clean on Sunday{w=[wt2]}, we'll go together!"

                else:
                    wmom "Well{w=[wt2]}, we agreed you'd take care of the house cleaning for that.{w=[wt3]} Remember, [C_Nam][wmom_to_hero][C_Off]?{w=[wt2]} If the house gets clean on Sunday{w=[wt2]}, we'll go together!"

            else:
                $ wmom_know.append("Neighbors_Reunion")
                $ msg.msg(renpy.translate_string("[C_Nam][fnamewmom][C_Off] is invited to [C_Dat]Neighbor's Reunion[C_Off]"))

                hero "[C_Nam][fnamewnei][C_Off]'s parents are inviting us to have lunch with them this Sunday.{w=[wt3]} Let's go!"
                wmom "Oh, [C_Nam][wmom_to_hero][C_Off]{w=[wt2]}, that'd be so nice!{w=[wt3]} I'd love to.{w=[wt2]} But I'm so busy!{w=[wt3]} Sunday is the only day I have to do my chores."
                hero "Well{w=[wt2]}, at least you won't need to cook!{w=[wt2]} We're going to eat there."
                wmom "{gg}Tee-hee...{/gg}{w=[wt2]} I still need to clean the house and wash the clothes.{w=[wt3]} Sunday is the only day I have to do these chores, [C_Nam][wmom_to_hero][C_Off].{w=[wt2]} Don't worry, [C_Nam][wmom_to_hero][C_Off]!{w=[wt2]} Call your sis and have fun{w=[wt2]}, you two!{w=[wt3]} Send my regards to my dear neighbors!"
                hero "You should go too.{w=[wt2]} I bet [C_Nam]Mrs. [lnamewnei][C_Off] is dying to talk to you!{w=[wt3]} What if I take care of the house chores for you?"
                wmom "Ohhh, [C_Nam][wmom_to_hero][C_Off]...{w=[wt2]} You're so precious...{w=[wt2]} Seriously!{w=[wt2]} Well...{w=[wt2]} Okay{w=[wt2]}, if the house and clothes are clean by Sunday{w=[wt2]}, we'll go together.{w=[wt3]} Deal?"
                hero "Deal!"

        "Return":
            jump wmom_interact
            
    jump wmom_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wmom_interact_hangout:
    menu:
        "Offer massage" if gametimehour >= 20 and Check_CharInMap("hero","home","bedroom_wmom") and is_specialevent == False:
            hero "Would you like a massage?"
            $ wmom_mood = "A2"
            wmom "{bt}Ara ara...{/bt}{w=[wt2]} You're so sweet, {nm}[wmom_to_hero]{/nm}!{w=[wt3]} How could I say no to something like that?{w=[wt1]} {gg}Tee-hee...{/gg}{w=[wt4]} Please, do it!{w=[wt2]} Mommy could really use that right now."
            jump wmom_massage_1

        "Help her cooking" if Get_ActivityName("wmom") in ["cooking"] and is_specialevent == False:
            hero "Let me help you prepare the breakfast!"
            wmom "{bt}Ara Ara...{w=[wt2]} My big boy is such a helpful son!{/bt}{w=[wt3]} I appreciate it, {nm}[wmom_to_hero]{/nm}!{w=[wt2]} Let's get to it then!"
            scene bg_0
            with Dissolve(1)

            pause(1)
            $ add_stat("wmom", "inti", 1)

            $ a_event_0 = wmom_wear
            $ a_event_1 = 0

            while Get_ActivityName("wmom") in ["cooking"] and a_event_1 < 240:
                $ gametimemin += 10
                $ a_event_1 += 10
                call gametime from _call_gametime_24

            $ wmom_wear = a_event_0
            
            scene bg_home livingroom
            call wmom_show from _call_wmom_show_4
            with Dissolve(1)

            jump wmom_interact_check

        "Have a family meeting" if gametimeday == 1 and gametimehour >= 18 and is_specialevent == True and not "WMOM" in scenestep:
            $ scenestep.insert(1, "WMOM")
            $ wmom_quest[1] = 1
            $ hero_mood = "A1"
            hero "Thank you for this party, {nm}[hero_to_wmom]{/nm}.{w=[wt2]} This is all amazing!"
            wmom "{bt}Ara ara...{/bt}{w=[wt2]} That's not all yet, {nm}[wmom_to_hero]{/nm}!{w=[wt3]} I still wanna do a surprise for you!{w=[wt2]} I mean{w=[wt2]}, maybe it's not exactly for you{w=[wt1]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} To Mom!"
            hero "That's cool!{w=[wt2]} Would you like me to talk to her on the phone?"
            wmom "Exactly, {nm}[wmom_to_hero]{/nm}!{w=[wt2]} She'd be so happy to speak with you...!{w=[wt3]} It's been so long after all!"
            hero "Of course!{w=[wt1]} Let's do that!"
            wmom "Alright, {nm}[wmom_to_hero]{/nm}!{w=[wt2]} Let's go call the girls too!"
            jump scenestep_0_4_call

        "Invite to watch TV" if Check_CharInMap("hero","home","living_room") and is_specialevent == False and not "HangOut_WatchTV" in wmom_know:
            $ wmom_know.append("HangOut_WatchTV")
            call action_watchtv("wmom") from _call_action_watchtv

        "Return":
            jump wmom_interact

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
label wmom_interact_chat:
    menu:
        "Ask how she is" if not "Talk_How" in wmom_know:
            # ----------------------------------------------------------------------------------------------------
            # Asking at early morning
            # ----------------------------------------------------------------------------------------------------
            if gametimehour <= 7:
                hero "Did you sleep well, {nm}[hero_to_wmom]{/nm}?"
                
                # WMOM received a massage from HERO
                if "WMOM_is_massaged" in wmom_know:
                    $ wmom_mood = "A3"
                    wmom "Oh, {nm}[wmom_to_hero]{/nm}{w=[wt2]}, I slept like a baby thanks to your wonderful massage!{w=[wt3]} What a magic hands my big boy have!~❤{w=[wt1]} {gg}Tee-hee...{/gg}"
                    hero "I'm glad it helped, {nm}[hero_to_wmom]{/nm}.{w=[wt3]} How's your back feeling now?"
                    wmom "Much better, {nm}[wmom_to_hero]{/nm}.{w=[wt3]} You're such a caring boy.{w=[wt2]} Mama loves you!"

                # WMOM and HERO slept together
                elif "WMOM_Hangout_Sleep" in wmom_know:
                    $ wmom_mood = "A2"
                    wmom "{bt}Ara ara...{/bt}{w=[wt3]} I slept very well, {nm}[wmom_to_hero]{/nm}.{w=[wt3]} Having my big boy close by made me feel so safe and warm!~❤"
                    hero "That's good to hear, {nm}[hero_to_wmom]{/nm}.{w=[wt2]} I'm glad you slept well."
                    wmom "You're such a sweetheart.{w=[wt3]} I hope I didn't snore or hog the blankets!{w=[wt1]} {gg}Tee-hee...{/gg}"

                # WMOM is having back pain
                else:
                    if wmom_quest[0] < 1:
                        $ wmom_mood = "A2"
                        wmom "Oh, {nm}[wmom_to_hero]{/nm}{w=[wt2]} , you're so sweet to ask!{w=[wt3]} Actually{w=[wt2]}, I had a bit of trouble sleeping.{w=[wt3]} My back was acting up again."
                        hero "I'm sorry to hear that.{w=[wt3]} Is there anything I can do to help?"
                        wmom "Just you asking means the world to me, darling.{w=[wt3]} Don't need to worry about Mama, okay?{w=[wt2]} I'll be fine."
                    else:
                        jump wmom_interact_chat_backache_1
                    jump wmom_interact_chat_backache_2

            # ----------------------------------------------------------------------------------------------------
            # Asking at any other time
            # ----------------------------------------------------------------------------------------------------
            else:
                hero "How are you today, {nm}[hero_to_wmom]{/nm}?"
                
                # WMOM is having back pain
                if not "WMOM_is_massaged" in wmom_know:
                    label wmom_interact_chat_backache_1:
                        if wmom_quest[0] < 1:
                            $ wmom_mood = "A2"
                            wmom "Oh, {nm}[wmom_to_hero]{/nm}, you're so attentive!{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'm not feeling my best today.{w=[wt3]} My back has been giving me trouble again."
                            hero "I'm sorry to hear that, {nm}[hero_to_wmom]{/nm}. Is there anything I can do to help?"
                            wmom "You're such a sweetheart, {nm}[wmom_to_hero]{/nm}.{w=[wt3]} Just having you here makes everything better.{w=[wt2]} Don't worry about me, okay?"
                        else:
                            $ wmom_mood = "O1"
                            wmom "Well, {nm}[wmom_to_hero]{/nm}{w=[wt2]}, my back has been giving me trouble again."
                    
                            label wmom_interact_chat_backache_2:
                                if perk_skl_msg == 1: # Massage skill learned (lvl 1)
                                    menu:
                                        "Offer a massage":
                                            if wmom_quest[0] < 1:
                                                $ wmom_quest[0] = 1
                                                hero "Actually, {nm}[hero_to_wmom]{/nm}, I've been learning some massage techniques. Would you like me to try and help with your back pain?"
                                                $ add_stat("wmom", "love", 1)
                                                $ add_stat("hero", "cha_soc", 1)
                                                $ wmom_mood = "A2"
                                                wmom "Oh my!{w=[wt2]} That's so thoughtful of you, darling!{w=[wt3]} I'd love a massage from my sweet boy.{w=[wt2]} Maybe later this evening, if you're not too busy?"
                                                hero "Of course, {nm}[hero_to_wmom]{/nm}. I'm happy to help."
                                            else:
                                                hero "How about I give you a massage later? It might help with your back pain."
                                                $ add_stat("wmom", "love", 1)
                                                $ add_stat("hero", "cha_soc", 1)
                                                $ wmom_quest[0] = 1
                                                $ wmom_mood = "A2"
                                                wmom "Oh, {nm}[wmom_to_hero]{/nm}!{w=[wt2]} You're such a thoughtful boy!{w=[wt3]} I'd love that, thank you."
                                        "Don't offer":
                                            hero "I hope you feel better soon, {nm}[hero_to_wmom]{/nm}. Let me know if there's anything I can do."
                                            wmom "Thank you, honey. You're such a good boy."
                
                # It's sunday
                elif gametimeweek == "Sunday":
                    $ wmom_mood = "A3"
                    wmom "Oh, it's being wonderful, {nm}[wmom_to_hero]{/nm}!{w=[wt3]} Even better now that you asked."
                    hero "Glad to hear that, {nm}[hero_to_wmom]{/nm}!"
                
                # It's not sunday
                else:
                    $ wmom_mood = "A2"
                    wmom "A bit challenging, {nm}[wmom_to_hero]{/nm}.{w=[wt3]} But just talking to you makes me feel better already! {gg}Tee-hee...{/gg}"
                    hero "I'm glad you're doing fine, {nm}[hero_to_wmom]{/nm}."

            $ wmom_know.append("Talk_How")

        "Chat about her activities" if gametimehour <= 12 or gametimehour >= 18 and is_specialevent == False:
            $ hero_mood = "A1"
            hero "What do you usually do, {nm}[hero_to_wmom]{/nm}?"
            wmom "I work as a maid in a house during the week, {nm}[wmom_to_hero]{/nm}.{w=[wt2]} I leave the breakfast ready for {nm}[fnamewsis]{/nm} and go to work.{w=[wt2]} Sustaining the house is not easy{w=[wt1]}, but I manage everything very bravely!{w=[wt3]} Now that my beloved darling is here{w=[wt1]}, I have more reasons to push my effort!"
            wmom "I still have all my Sundays free{w=[wt3]}, so you can have your mom full time for you!{w=[wt3]} I'd really love your company for my afternoon yoga workouts!"
            $ hero_mood = "A2"
            mind "(It looks like {nm}[hero_about_wmom]{/nm}'s life got too hard without my father support{w=[wt2]}, and [hero_about_wsis] doesn't seem to help her yet{w=[wt2]}, so {nm}[hero_about_wmom]{/nm} is doing more than she can to sustain this big house my father bought{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I better look for some ways to earn money so I won't be a burden.)"

        "Return":
            jump wmom_interact

    $ wmom_know.append("Talk")
    $ gametimemin += 20
    $ add_stat("wmom", "inti", 0.2)
    jump wmom_interact_check

# ----------------------------------------------------------------------------------------------------
# End
# ----------------------------------------------------------------------------------------------------
jump wmom_interact_end

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_wmom:
    $ wmom_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wmom_inti*0.02) and not any(get_id.startswith("HERO_Dated") for get_id in wmom_know):

        wmom "So, {nm}[wmom_to_hero]{/nm},{w=[wt2]} what about your life in the countryside?{w=[wt3]} Did my big boy met any nice girl?{w=[wt2]} Hmmm?{w=[wt3]} Mama wanna know everything! ~❤"

        $ hero_fx = 1
        $ hero_mood = "O1"

        menu:
            wmom "So, {nm}[wmom_to_hero]{/nm}, what about your life in the countryside? Did my big boy met any nice girl? Hmmm? Mama wanna know everything! ~❤{fast}"
            
            "Deny":
                $ wmom_know.append("HERO_Dated_N")
                $ msg.msg(renpy.translate_string("{nm}[fnamewmom]{/nm} knows you a little more"))
                $ add_stat("wmom", "inti", 0.5)
                hero "N{w=[wt1]}-No{w=[wt2]}, I've never dated before."
                $ wmom_mood = "O2"
                wmom "{aw}Ehhh...?{/aw} Is that really so, {nm}[wmom_to_hero]{/nm}? Even someone so handsome like my big guy!? These country girls doesn't know what they were loosing!{nw}"
                $ wmom_mood = "A1"
                wmom "{aw}Ehhh...?{/aw}{w=[wt3]} Is that really so, {nm}[wmom_to_hero]{/nm}?{w=[wt3]} Even someone so handsome like my big guy!?{w=[wt3]} These country girls doesn't know what they were loosing!{w=[wt2]}{fast} I'm sure it must rain girl for you here in city!{w=[wt1]} {gg}Tee-hee...{/gg}"

            "Confirm":
                $ wmom_know.append("HERO_Dated_Y")
                $ msg.msg(renpy.translate_string("{nm}[fnamewmom]{/nm} knows you a little more"))
                $ add_stat("wmom", "inti", 0.5)
                hero "W{w=[wt1]}-well{w=[wt2]}, y{w=[wt1]}-yes{w=[wt2]}, I kinda dated a girl once."
                $ wmom_mood = "A3"
                wmom "{gg}Tee-hee...{/gg}{w=[wt3]} My little {nm}[wmom_to_hero]{/nm} is growing up so fast!{w=[wt3]} Just remember, mama is always here if you need any{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Advice ~❤"

    # ----------------------------------------------------------------------------------------------------
    # Ask HERO's girl preference
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wmom_inti*0.02) and sum(1 for get_id in wmom_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wmom_know if get_id.startswith("HERO_N_Girl")) < 4:
        wmom "So. {nm}[wmom_to_hero]{/nm}{w=[wt2]}, mama wanna know more about you.{w=[wt3]} Do any kind of girl catches your eye?{nw}"

        menu:
            wmom "So. {nm}[wmom_to_hero]{/nm}, mama wanna know more about you. Do any kind of girl catches your eye?{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in wmom_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in wmom_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in wmom_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in wmom_know if "Personality_" in get_id)

                # Appearance Likes(Y)/Dislikes(N)
                $ a_event_1 = wmom_know
                $ a_event_3 = "initiative_wmom_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_7

                # Store the answer if one was given
                if _return:
                    $ wmom_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg(renpy.translate_string("{nm}[fnamewmom]{/nm} knows you a little more"))
                $ add_stat("wmom", "inti", 0.5)

                if _return in ["Breast_3", "Breast_4", "Breast_5", "HairSize_4", "HairSize_5", "Personality_3"]: # Match - big breasts, medium-long hair, kind personality
                    $ add_stat("wmom", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ wmom_mood = "A3"
                    wmom "{bt}Ara ara {nm}[wmom_to_hero]{/nm}...{/bt}{w=[wt2]} {gg}Tee-hee...{/gg}{w=[wt3]} Maybe mama is beating young girls in this regard, huh?"

                elif _return in ["Breast_0", "Breast_1", "HairSize_0", "HairSize_1", "HairSize_2", "Personality_4", "Personality_2"]: # Opposite match - flat/tiny breasts, short hair, aggressive/dispirited
                    $ add_stat("wmom", "bonus", -10)
                    $ wmom_mood = "A1"
                    wmom "{bt}Ara ara...{/bt}{w=[wt2]} That seems to be a strong point, huh?"

                else: # Others
                    $ wmom_mood = "A1"
                    wmom "{bt}Ara ara...{/bt}{w=[wt2]} That's quite interesting, {nm}[wmom_to_hero]{/nm}!"

            "Don't choose":
                jump initiative_wmom_return

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:
        wmom "{gg}Tee-hee...{/gg}{w=[wt2]} Mama got lost in thought for a moment!{w=[wt3]} Is the age coming?"
        jump wmom_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("wmom", "inti", 0.2)
    jump wmom_interact_check

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wmom_return:
    hero "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Well{w=[wt2]}, I'm not sure how to answer that right now."
    wmom "That's okay, sweetie.{w=[wt2]} Maybe you've got a lot on your mind lately, huh?.{w=[wt3]} Just know mama is always here if you want to talk!"
    jump wmom_interact
