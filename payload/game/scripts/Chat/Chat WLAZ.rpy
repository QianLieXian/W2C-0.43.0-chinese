# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wlaz_show:

    if wlaz_love <= 10:
        $ wlaz_mood = "O1"
    elif wlaz_love >= 0:
        $ wlaz_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_6

    show WLAZ at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wlaz_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewlaz][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wlaz")))))

    if Get_ActivityName("wlaz") in ["at class"]:
        jump show_ui

    else:
        return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wlaz_interact_end:
    if "interacting_hero" in wlaz_know:
        $ wlaz_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wlaz_interact_start:
    call hide_ui from _call_hide_ui_42
    call wlaz_show_activity from _call_wlaz_show_activity
    $ wlaz_inti = min(char_inti_cap, wlaz_inti)

    $ msg.msg(renpy.translate_string("Content Unavailable"))
    jump show_ui
    
    call hide_ui from _call_hide_ui_43
    call wlaz_show from _call_wlaz_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wlaz_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if hero_map == wlaz_map:
        pass

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wlaz_interact_check:
    # Save current outfit before any updates
    $ wlaz_wear_keep = wlaz_wear

    call gametime from _call_gametime_20
    call hide_ui from _call_hide_ui_44

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wlaz_wear != wlaz_wear_keep:
        $ wlaz_wear = wlaz_wear_keep

    call wlaz_show from _call_wlaz_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    if gametimehour >= 18: # Went home
        $ a_event_0 = renpy.random.random()
        if a_event_0 < 1/3:
            wlaz "Raid starts soon.{w=[wt3]} Gotta log in.{w=[wt3]} Can't keep the guild waiting.{w=[wt3]} Well{w=[wt2]}, I could{w=[wt2]}, but{w=[wt2]}, effort."
        elif a_event_0 < 2/3:
            wlaz "Time to clock out.{w=[wt3]} Got a game to finish.{w=[wt3]} Been stuck on this boss for days.{w=[wt3]} Meh."
        else:
            wlaz "Battery's almost dead.{w=[wt3]} Need to recharge me and the console.{w=[wt3]} See ya."
        $ hero_fx = 0
        jump wlaz_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Get_MapName("wlaz", "at class"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "wlaz"):
            $ wlaz_mood = "O1"
            wlaz "What a drag...{w=[wt4]} Class time.{w=[wt3]} Guess I should{w=[wt2]}, like{w=[wt2]}, head over.{nw}"

            show WLAZ at RC
            show WLAZ at OR_slow
            show HERO at OR_slow
            wlaz "What a drag...{w=[wt4]} Class time.{w=[wt3]} Guess I should{w=[wt2]}, like{w=[wt2]}, head over.{fast}{w=[wt2]} Later."

            jump wlaz_interact_end

        else:
            $ wlaz_mood = "O1"
            wlaz "Meh{w=[wt2]}, class time.{w=[wt4]} Too much effort to care{w=[wt2]}, but{w=[wt2]}, whatever.{w=[wt3]} Will you go too?"

            if Get_MapName("wlaz", "at class") == Get_MapName(None, "school", "class_1b"):
                menu:
                    "Go together":
                        $ hero_mood = "A1"
                        hero "Yes.{w=[wt2]} Let's go!{w=[wt2]} C'mon!"
                        
                        $ wlaz_mood = "O1"
                        wlaz "Chill out{w=[wt2]}, we'll get there when we get there.{w=[wt3]} No need to speedrun this."
                        
                        scene bg_0
                        with dissolve

                        $ hero_map = wlaz_map
                        call gametime from _call_gametime_21
                        call check_playermap from _call_check_playermap_6
                        call hide_ui from _call_hide_ui_45
                        show WLAZ at RC
                        show HERO at LC
                        with dissolve
                        
                        $ wlaz_mood = "A1"
                        wlaz "{gg}Heh...!{/gg}{w=[wt2]} We did it!{w=[wt3]} GG EZ!"

                        jump wlaz_interact_end
                        
                    "Let her go":
                        pass

            $ hero_mood = "A1"
            hero "Need to do something first.{w=[wt2]} See you!"
            
            $ wlaz_mood = "O1"
            wlaz "{bt}Yeah... yeah...{/bt}{w=[wt4]} Loading...{w=[wt4]} ...Okay{w=[wt2]}, going now."
            
            show WLAZ at RC
            show WLAZ at OR_slow
            pause(1.5)

        jump wlaz_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wlaz_know:
        $ a_event_0 = renpy.random.random()

        # Brings an interactive subject
        if renpy.random.random() < (0.2 + (wlaz_love * 0.003)):
            jump initiative_wlaz

        # Do a random comment
        elif renpy.random.random() > (0.5 + (wlaz_love * 0.002)):
            $ a_event_0 = renpy.random.random()
            if a_event_0 < 1/4:
                $ wlaz_mood = "A1"
                wlaz "Found this neat exploit.{w=[wt3]} Cut my homework time in half.{w=[wt3]} Work smarter... not harder."
            elif a_event_0 < 2/4:
                $ wlaz_mood = "A1"
                wlaz "Loading...{w=[wt3]} Sorry, brain buffering.{w=[wt3]} What were we talking about?"
            elif a_event_0 < 3/4:
                $ wlaz_mood = "A1"
                wlaz "There's always a shortcut for effort."
            else:
                $ wlaz_mood = "A1"
                wlaz "Got new DLC last night.{w=[wt3]} Played till 4AM.{w=[wt3]} Worth it.{w=[wt3]} Kinda."

    # ----------------------------------------------------------------------------------------------------
    # WLAZ is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wlaz") in ["eating"]:
        "{nm}[fnamewlaz]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamewlaz]{/nm} is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wlaz") from _call_circletable_5

                while Get_ActivityName("wlaz") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_6
                call gametime from _call_gametime_22
                
                jump wlaz_interact_start

            "Return":
                jump wlaz_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_0 = renpy.random.random()
        
        if wlaz_love <= 0:
            $ wlaz_mood = "A1"
            if a_event_0 < 1/3:
                wlaz "Oh.{w=[wt3]} It's you.{w=[wt3]} 'Sup."
            elif a_event_0 < 2/3:
                wlaz "Mm.{w=[wt3]} Hey."
            else:
                wlaz "..."
                $ wlaz_mood = "A1"
                wlaz "...{fast}Oh, you're talking to me?{w=[wt3]} My bad."
        
        elif wlaz_love < 50:
            $ wlaz_mood = "A1"
            if a_event_0 < 1/3:
                wlaz "Hey.{w=[wt3]} What's up?"
            elif a_event_0 < 2/3:
                wlaz "Oh, it's you.{w=[wt3]} Cool."
            else:
                wlaz "{bt}Waaah...{/bt}{w=[wt3]} Hey there."
        
        else:
            $ wlaz_mood = "A1"
            if a_event_0 < 1/3:
                wlaz "Hey, you.{w=[wt3]} Good timing.{w=[wt3]} Was getting bored."
            elif a_event_0 < 2/3:
                wlaz "Oh, hey there!"
            else:
                wlaz "Hey!{w=[wt3]} Wanna play?"
        
        $ wlaz_fx = 0

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wlaz_interact:
    call hide_ui from _call_hide_ui_46
    if "interacting_hero" not in wlaz_know:
        $ wlaz_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wlaz_interact_chat
        "Touch" if not is_specialevent:
            jump wlaz_interact_touch
        "Hang out":
            jump wlaz_interact_hangout
        "Give item" if not is_specialevent:
            jump wlaz_interact_gift
        "Return":
            jump wlaz_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wlaz_interact_gift:
    $ a_item_8 = "wlaz"
    $ a_item_9 = 0
    $ a_item_6 = "wlaz_interact"
    call UI_give_Item from _call_UI_give_Item_7

label wlaz_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wlaz_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wlaz_interact_touch:
    menu:
        "Return":
            jump wlaz_interact
    
    jump wlaz_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wlaz_interact_hangout:
    menu:
        "Return":
            jump wlaz_interact

    $ gametimemin += 30
    jump wlaz_interact_check

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
label wlaz_interact_chat:
    menu:
        "Return":
            jump wlaz_interact

    $ add_stat("wlaz", "inti", 0.2)
    $ gametimemin += 20
    jump wlaz_interact_check

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_wlaz:
    $ wlaz_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wlaz_inti*0.02) and not any(get_id.startswith("HERO_Dated") for get_id in wlaz_know):

        $ wlaz_mood = "A1"
        wlaz "Random question.{w=[wt3]} Ever dated anyone?{w=[wt3]} Just curious."

        $ hero_fx = 1
        $ hero_mood = "O1"
        menu:
            wlaz "Random question. Ever dated anyone? Just curious.{fast}"
            
            "Deny":
                $ wlaz_know.append("HERO_Dated_N")
                $ msg.msg(renpy.translate_string("{nm}[fnamewlaz]{/nm} knows you a little more"))
                $ add_stat("wlaz", "inti", 0.5)

                hero "N-no, I haven't really dated anyone before."

                $ wlaz_mood = "A1"
                wlaz "I get you.{w=[wt3]} Too much effort.{w=[wt3]} The whole dating thing.{w=[wt3]} People expect stuff.{w=[wt3]} Sounds exhausting."

            "Confirm":
                $ wlaz_know.append("HERO_Dated_Y")
                $ msg.msg(renpy.translate_string("{nm}[fnamewlaz]{/nm} knows you a little more"))
                $ add_stat("wlaz", "inti", 0.5)

                hero "Y-yeah, I dated someone before."

                $ wlaz_fx = 1
                $ wlaz_mood = "A2"
                wlaz "Well{w=[wt2]}, makes sense, I guess."

                $ wlaz_fx = 0

            "Don't choose":
                jump initiative_wlaz_return

    # ----------------------------------------------------------------------------------------------------
    # Ask HERO's girl preference
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wlaz_inti*0.02) and sum(1 for get_id in wlaz_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wlaz_know if get_id.startswith("HERO_N_Girl")) < 4:
        $ wlaz_mood = "A1"
        wlaz "So...{w=[wt3]} What's your type?{w=[wt3]} Girl-wise, I mean.{w=[wt3]} Just idle curiosity.{nw}"

        menu:
            wlaz "So... What's your type? Girl-wise, I mean. Just idle curiosity.{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in wlaz_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in wlaz_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in wlaz_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in wlaz_know if "Personality_" in get_id)

                # Appearance Likes(Y)/Dislikes(N)
                $ a_event_1 = wlaz_know
                $ a_event_3 = "initiative_wlaz_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_6

                # Store the answer if one was given
                if _return:
                    $ wlaz_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg(renpy.translate_string("{nm}[fnamewlaz]{/nm} knows you a little more"))
                $ add_stat("wlaz", "inti", 0.5)

                if _return in ["Personality_2", "Personality_6", "Breast_2", "Breast_3", "HairSize_4", "HairSize_5"]: # Match - dispirited (lazy), timid, medium/big breasts, medium-long hair
                    $ add_stat("wlaz", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ wlaz_mood = "A1"
                    $ wlaz_fx = 1
                    wlaz "Huh.{w=[wt3]} Interesting."
                    $ wlaz_fx = 0

                elif _return in ["Personality_1", "Personality_11", "HairSize_0", "HairSize_1", "Breast_0"]: # Opposite match - energetic, visually diligent, short/bald hair, flat
                    $ add_stat("wlaz", "bonus", -10)
                    $ wlaz_mood = "A2"
                    wlaz "I see..."

                else: # Others
                    $ wlaz_mood = "A2"
                    wlaz "Well{w=[wt2]}, can't argue with that."

            "Don't choose":
                jump initiative_wlaz_return

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:
        $ wlaz_mood = "A1"
        $ a_event_0 = renpy.random.random()
        
        if wlaz_love < 50:
            if a_event_0 < 1/6:
                wlaz "Was gonna ask you something.{w=[wt3]} Forgot what.{w=[wt3]} Meh.{w=[wt3]} Probably wasn't important."
            elif a_event_0 < 2/6:
                wlaz "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Nah.{w=[wt3]} Never mind."
            elif a_event_0 < 3/6:
                wlaz "{bt}Waaah...{/bt}{w=[wt3]} Sorry.{w=[wt3]} Had a thought.{w=[wt3]} Lost it.{w=[wt3]} Too much effort to remember."
            elif a_event_0 < 4/6:
                wlaz "Thinking's hard.{w=[wt3]} Let's just...{w=[wt3]} not."
            elif a_event_0 < 5/6:
                wlaz "Had something to ask you.{w=[wt3]} Brain buffering.{w=[wt3]} Maybe later.{w=[wt3]} If I remember.{w=[wt3]} Probably won't."
            else:
                wlaz "Almost had a thought there.{w=[wt3]} Gone now.{w=[wt3]} Like a rare spawn that got away."

        jump wlaz_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("wlaz", "inti", 0.20)
    jump wlaz_interact_check

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wlaz_return:

    call hero_n_answer from _call_hero_n_answer_6

    $ wlaz_mood = "A1"
    $ a_event_0 = renpy.random.random()
    
    if a_event_0 < 1/5:
        wlaz "Fair enough."
    elif a_event_0 < 2/5:
        wlaz "Whatever.{w=[wt3]} Just making conversation."
    elif a_event_0 < 3/5:
        wlaz "Touchy subject?{w=[wt3]} My bad.{w=[wt3]} Moving on."
    elif a_event_0 < 4/5:
        wlaz "That's cool.{w=[wt3]} Questions are overrated anyway."
    else:
        wlaz "Don't worry{w=[wt2]}, I was just saying whatever."
    
    jump wlaz_interact
