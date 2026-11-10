# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wuza_show:

    if wuza_love <= 10:
        $ wuza_mood = "O1"
    elif wuza_love >= 0:
        $ wuza_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_13

    show WUZA at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wuza_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewuza][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wuza")))))

    if Get_ActivityName("wuza") in ["at class"]:
        jump show_ui

    else:
        return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wuza_interact_end:
    if "interacting_hero" in wuza_know:
        $ wuza_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wuza_interact_start:
    call hide_ui from _call_hide_ui_97
    call wuza_show_activity from _call_wuza_show_activity
    $ wuza_inti = min(char_inti_cap, wuza_inti)

    $ msg.msg(renpy.translate_string("Content Unavailable"))
    jump show_ui
    
    call hide_ui from _call_hide_ui_98
    call wuza_show from _call_wuza_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wuza_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if hero_map == wuza_map:
        pass

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wuza_interact_check:
    # Save current outfit before any updates
    $ wuza_wear_keep = wuza_wear

    call gametime from _call_gametime_46
    call hide_ui from _call_hide_ui_99

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wuza_wear != wuza_wear_keep:
        $ wuza_wear = wuza_wear_keep

    call wuza_show from _call_wuza_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    if gametimehour >= 18: # Went home
        $ a_event_0 = renpy.random.random()
        if a_event_0 < 1/4 and "WUZA_BG_ORPHANAGE" in hero_know:
            $ wuza_mood = "A3"
            wuza "Oh shoot, I gotta run!{w=[wt2]} The kids at the orphanage are waiting for me to organize their evening exercises!{w=[wt3]} {pa}THEY LOVE IT WHEN I TEACH THEM SPORTS!{/pa}"
        elif a_event_0 < 2/4 and "WUZA_Y_SPORT" in hero_know:
            $ wuza_mood = "A3"
            wuza "Damn, look at the time!{w=[wt2]} I've got training to do!{w=[wt3]} {bt}Gotta go...! Gotta go...!{/bt}{w=[wt2]} If I miss a day, my muscles will start crying!"
        elif a_event_0 < 3/4 and "WUZA_KNOW_WDEL" in hero_know:
            $ wuza_mood = "A1"
            wuza "I promised {nm}[fnamewdel]{/nm} I'd meet her after school!{w=[wt3]} Better not be late or she'll give me that look again.{w=[wt2]} {gg}Gee-Hee-Hee...{/gg}{w=[wt2]} Catch ya tomorrow, buddy!"
        else:
            $ wuza_mood = "A3"
            wuza "Oh man, I gotta bounce!{w=[wt3]} Got important things to do, places to be, energy to burn!{w=[wt3]} {bt}See ya...! See ya...!{/bt}"
        $ hero_fx = 0
        jump wuza_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Get_MapName("wuza", "at class"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "wuza"):
            $ wuza_mood = "A4"
            wuza "{pa}OH YEAH!!!{/pa}{w=[wt2]} CLASS TIME{w=[wt2]}, {bt}BRO...!{/bt}{nw}"

            show WUZA at RC
            show WUZA at OR_fast
            show HERO at OR_fast
            wuza "{pa}OH YEAH!!!{/pa}{w=[wt2]} CLASS TIME{w=[wt2]}, {bt}BRO...!{/bt}{fast}{w=[wt2]} {bt}LET'S GO...! LET'S GO...!{/bt}"

            jump wuza_interact_end

        else:
            $ wuza_mood = "A4"
            wuza "{pa}YO!!!{/pa}{w=[wt2]} Time to head to class{w=[wt2]}, {bt}BRO...!{/bt}{w=[wt3]} {bt}HURRY UP...! HURRY UP...!{/bt}"

            if Get_MapName("wuza", "at class") == Get_MapName(None, "school", "class_1b"):
                menu:
                    "Go together":
                        $ hero_mood = "A2"
                        hero "Sure.{w=[wt2]} Let's go!"
                        
                        $ wuza_mood = "A4"
                        wuza "{pa}OH YEAH!!!{/pa}{w=[wt3]} {bt}LET'S GO TOGETHER{w=[wt2]}, BRO...!{/bt}{w=[wt2]} Last one there is a rotten egg!{w=[wt2]} {lg}CHA HA HA HA!!!{/lg}{nw}"
                        
                        show WUZA at RC
                        show WUZA at OR_fast
                        show HERO at OR_fast
                        wuza "{pa}OH YEAH!!!{/pa}{w=[wt3]} {bt}LET'S GO TOGETHER{w=[wt2]}, BRO...!{/bt}{w=[wt2]} Last one there is a rotten egg!{w=[wt2]} {lg}CHA HA HA HA!!!{/lg}{fast}"
                        
                        scene bg_0
                        with dissolve

                        $ hero_map = wuza_map
                        call gametime from _call_gametime_47
                        call check_playermap from _call_check_playermap_30
                        call hide_ui from _call_hide_ui_100
                        show WUZA at RC
                        show HERO at LC
                        with dissolve
                        
                        $ wuza_mood = "A4"
                        wuza "That was a good sprint{w=[wt2]}, BRO!{w=[wt3]} See ya inside!{w=[wt2]} {lg}CHA HA HA HA!!!{/lg}"

                        jump wuza_interact_end
                        
                    "Let her go":
                        pass

            $ hero_mood = "A1"
            hero "Need to do something first.{w=[wt2]} See you!"
            
            $ wuza_mood = "A1"
            show WUZA at RC
            show WUZA at OR_slow
            wuza "{bt}Booo...!{w=[wt2]} Truant...! Truant...!{/bt}"

        jump wuza_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wuza_know:
        $ a_event_0 = renpy.random.random()

        # Brings an interactive subject
        if renpy.random.random() < (0.2 + (wuza_love * 0.003)):
            jump initiative_wuza

        # Do a random comment
        elif renpy.random.random() > (0.5 + (wuza_love * 0.002)):
            $ a_event_0 = renpy.random.random()
            if a_event_0 < 1/5:
                $ wuza_mood = "A1"
                wuza "Man, I'm starving!{w=[wt3]} Could eat a whole buffet right now.{w=[wt3]} All this talking burns calories, you know?"
            elif a_event_0 < 2/5:
                $ wuza_mood = "A3"
                wuza "Did you see that new equipment they got in the gym?{w=[wt3]} {pa}IT'S GONNA BE AMAZING TO TRY IT OUT!{/pa}"
            elif a_event_0 < 3/5 and "WUZA_KNOW_WDEL" in hero_know:
                $ wuza_mood = "A2"
                wuza "{nm}[fnamewdel]{/nm} taught me a cool drum pattern another day.{w=[wt3]} She got all mad when I broke another one of her sticks though.{w=[wt3]} I really suck at that!{w=[wt1]} {gg}Gee-Hee-Hee...{/gg}"
            elif a_event_0 < 4/5:
                $ wuza_mood = "A3"
                wuza "You ever notice how the best ideas come when you're moving?{w=[wt3]} Standing still is for statues!{w=[wt2]} {bt}Move it...! Move it...!{/bt}"
            elif a_event_0 < 4/5:
                $ wuza_mood = "A1"
                wuza "Man, I'm getting so hungry just standing here talking!{w=[wt3]} My stomach's gonna start doing its own workout soon!{w=[wt2]} {gg}Gee-Hee-Hee...{/gg}"
            elif a_event_0 < 4/5:
                $ wuza_mood = "A4"
                wuza "{bt}You're pretty cool...! Pretty cool...! Yeeeeahhh...!{/bt}"
            elif a_event_0 < 4/5:
                $ wuza_mood = "A1"
                wuza "We should totally hang out more!{w=[wt3]} I need more friends who don't run away when I get excited about stuff!"
            elif a_event_0 < 4/5:
                $ wuza_mood = "A1"
                wuza "You know what?{w=[wt2]} {bt}You're a nice buddy...! Nice buddy...!{/bt}"
            else:
                $ wuza_mood = "A1"
                wuza "Hanging out with you is like a good warm-up.{w=[wt3]} Gets me all energized and happy!{w=[wt2]} {gg}Gee-Hee-Hee...{/gg}"

    # ----------------------------------------------------------------------------------------------------
    # WUZA is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wuza") in ["eating"]:
        "{nm}[fnamewuza]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamewuza]{/nm} is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wuza") from _call_circletable_11

                while Get_ActivityName("wuza") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_14
                call gametime from _call_gametime_48
                
                jump wuza_interact_start

            "Return":
                jump wuza_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_0 = renpy.random.random()

        if wuza_love < 10:
            $ wuza_mood = "A1"
            if a_event_0 < 1/4:
                wuza "Hey there!{w=[wt2]} What's up?{w=[wt3]} You look like you could use some excitement in your day!"
            elif a_event_0 < 2/4:
                wuza "Oh, hi!{w=[wt3]} Wanna hang out?{w=[wt3]} I've got so much energy right now!"
            elif a_event_0 < 3/4:
                wuza "New friend alert!{w=[wt3]} {gg}Gee-Hee-Hee...{/gg}{w=[wt2]} What are we doing today?"
            else:
                wuza "Hey buddy!{w=[wt3]} Perfect timing!{w=[wt3]} I was just about to do something awesome!"

        elif wuza_love < 40:
            $ wuza_mood = "A3"
            if a_event_0 < 1/5:
                wuza "There you are!{w=[wt3]} I was hoping I'd run into someone cool today!"
            elif a_event_0 < 2/5:
                wuza "Hey!{w=[wt2]} {bt}Over here...! Over here...!{/bt}{w=[wt3]} Glad you showed up!"
            elif a_event_0 < 3/5:
                wuza "Yo!{w=[wt2]} You're just in time!{w=[wt3]} I was about to burst with all this energy!"
            elif a_event_0 < 4/5:
                wuza "Hey you!{w=[wt3]} {gg}Gee-Hee-Hee...{/gg}{w=[wt2]} Great to see ya!"
            else:
                wuza "Perfect timing!{w=[wt3]} I was just thinking I needed someone fun to talk to!"

        elif wuza_love < 70:
            $ wuza_mood = "A3"
            if a_event_0 < 1/4:
                wuza "Hey, it's my favorite person!{w=[wt3]} Just the one I wanted to see!"
            elif a_event_0 < 2/4:
                wuza "There you are!{w=[wt3]} My day just got a whole lot better!{w=[wt2]} {gg}Gee-Hee-Hee...{/gg}"
            elif a_event_0 < 3/4:
                wuza "Hey!{w=[wt2]} I was hoping you'd show up!{w=[wt3]} {bt}So happy...! So happy...!{/bt}"
            else:
                wuza "Well look who it is!{w=[wt3]} {gg}Gee-Hee-Hee...{/gg}{w=[wt2]} I've been waiting for you to show up!"

        else:
            $ wuza_mood = "A4"
            $ wuza_fx = 1
            if a_event_0 < 1/4:
                wuza "{pa}HEEEEY!{/pa}{w=[wt2]} Just the person I wanted to see most!{w=[wt3]} This is gonna be great!"
            elif a_event_0 < 2/4:
                wuza "There you are!{w=[wt3]} My day wasn't complete without seeing you!{w=[wt2]} {gg}Gee-Hee-Hee...{/gg}"
            elif a_event_0 < 3/4:
                wuza "Hey!{w=[wt2]} I've been thinking about you!{w=[wt3]} {bt}So happy...! So happy...!{/bt}"
            else:
                wuza "My favorite person in the whole school!{w=[wt3]} {gg}Gee-Hee-Hee...{/gg}{w=[wt2]} I'm so glad you're here!"
            $ wuza_fx = 0

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wuza_interact:
    call hide_ui from _call_hide_ui_101
    if "interacting_hero" not in wuza_know:
        $ wuza_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wuza_interact_chat
        "Touch" if not is_specialevent:
            jump wuza_interact_touch
        "Hang out":
            jump wuza_interact_hangout
        "Give item" if not is_specialevent:
            jump wuza_interact_gift
        "Return":
            jump wuza_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wuza_interact_gift:
    $ a_item_8 = "wuza"
    $ a_item_9 = 0
    $ a_item_6 = "wuza_interact"
    call UI_give_Item from _call_UI_give_Item_14

label wuza_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wuza_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wuza_interact_touch:
    menu:
        "Return":
            jump wuza_interact
    
    jump wuza_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wuza_interact_hangout:
    menu:
        "Return":
            jump wuza_interact

    $ gametimemin += 30
    jump wuza_interact_check

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
label wuza_interact_chat:
    menu:
        "Return":
            jump wuza_interact

    $ add_stat("wuza", "inti", 0.2)
    $ gametimemin += 20
    jump wuza_interact_check

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_wuza:
    $ wuza_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wuza_inti*0.02) and not any(get_id.startswith("HERO_Dated") for get_id in wuza_know):

        $ wuza_mood = "A1"
        wuza "{bt}Hey buddy...! Hey buddy...!{/bt}{w=[wt2]} I've been wondering!{w=[wt3]} Have you ever have a girlfriend?{w=[wt2]} {bt}Tell me...! Tell me...!{/bt}"

        $ hero_fx = 1
        $ hero_mood = "O1"

        menu:
            wuza "{bt}Hey buddy...! Hey buddy...!{/bt}{w=[wt2]} I've been wondering!{w=[wt3]} Have you ever have a girlfriend?{w=[wt2]} {bt}Tell me...! Tell me...!{/bt}{fast}"
            
            "Deny":
                $ wuza_know.append("HERO_Dated_N")
                $ msg.msg(renpy.translate_string("{nm}[fnamewuza]{/nm} knows you a little more"))
                $ add_stat("wuza", "inti", 0.5)

                hero "N-no{w=[wt2]}, I've never really dated anyone before."

                $ wuza_mood = "A3"
                wuza "{aw}Ehhh...?{/aw}{w=[wt2]} For real?"
                
                hero "Y{w=[wt1]}-yes."
                
                wuza "So my buddy is just super picky, huh?{w=[wt3]} You're absolutelly right!{w=[wt2]} No boring chick for you! {bt}Yeeeah!!!{/bt}"

            "Confirm":
                $ wuza_know.append("HERO_Dated_Y")
                $ msg.msg(renpy.translate_string("{nm}[fnamewuza]{/nm} knows you a little more"))
                $ add_stat("wuza", "inti", 0.5)

                hero "Y-yeah{w=[wt2]}, I've dated before."

                $ wuza_mood = "A1"
                wuza "{gg}Gee-Hee-Hee...{/gg} I knew that!{w=[wt3]} You're super cool!"

    # ----------------------------------------------------------------------------------------------------
    # Ask HERO's girl preference
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wuza_inti*0.02) and sum(1 for get_id in wuza_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wuza_know if get_id.startswith("HERO_N_Girl")) < 4:
        $ wuza_mood = "A1"
        wuza "Hey!{w=[wt2]} I've been super curious!{w=[wt3]} What kind of girls do you like?{w=[wt3]} You know, like what makes you go {pa}WOW{/pa} when you see a girl?{nw}"

        menu:
            wuza "Hey! I've been super curious! What kind of girls do you like? You know, like what makes you go {pa}WOW{/pa} when you see a girl?{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in wuza_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in wuza_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in wuza_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in wuza_know if "Personality_" in get_id)

                # Appearance Likes(Y)/Dislikes(N)
                $ a_event_1 = wuza_know
                $ a_event_3 = "initiative_wuza_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_13

                # Store the answer if one was given
                if _return:
                    $ wuza_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg(renpy.translate_string("{nm}[fnamewuza]{/nm} knows you a little more"))
                $ add_stat("wuza", "inti", 0.5)

                if _return in ["Personality_1", "Personality_5", "Breast_2", "Breast_3", "HairSize_3", "HairSize_4"]: # Match - energetic, outgoing, medium/big breasts, short-medium hair (athletic)
                    $ add_stat("wuza", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ wuza_mood = "A3"
                    $ wuza_fx = 1
                    wuza "Wait, for real?{w=[wt3]} {gg}Gee-Hee-Hee...{/gg}{w=[wt3]} That's, um, interesting!{w=[wt3]} {bt}So interesting...! So interesting...!{/bt}"
                    $ wuza_fx = 0

                elif _return in ["Personality_2", "Personality_6", "Breast_0", "HairSize_0", "HairSize_6"]: # Opposite match - dispirited, shy, flat breasts, bald or very long hair
                    $ add_stat("wuza", "bonus", -10)
                    $ wuza_mood = "A1"
                    wuza "Huh, that's not what I expected!{w=[wt3]} But that's cool!{w=[wt3]} Everyone's got their own thing, right?{w=[wt2]} {gg}Gee-Hee-Hee...{/gg}"

                else: # Others
                    $ wuza_mood = "A1"
                    wuza "Oh yeah?{w=[wt3]} That's pretty cool!{w=[wt3]} I know some girls like that!{w=[wt2]} {lg}CHA HA HA HA!!!{/lg}"

            "Don't choose":
                jump initiative_wuza_return

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:
        $ wuza_mood = "A1"
        $ a_event_0 = renpy.random.random()
        
        if a_event_0 < 1/3:
            wuza "Oh!{w=[wt2]} I was gonna ask you something, but then I got distracted by that bird!{w=[wt3]} Did you see it?{w=[wt2]} It was so fast!{w=[wt3]} {bt}So fast...! So fast...!{/bt}"
        elif a_event_0 < 2/3:
            wuza "I had this super important question, but now I can't remember what it was!{w=[wt3]} {lg}CHA HA HA HA!!!{/lg}{w=[wt2]} My brain's always racing faster than my mouth!"
        else:
            wuza "Wait, what was I saying?{w=[wt3]} Oh man, I totally lost my train of thought!{w=[wt1]} {lg}CHA HA HA HA!!!{/lg}"

        jump wuza_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("wuza", "inti", 0.20)
    jump wuza_interact_check

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wuza_return:

    call hero_n_answer from _call_hero_n_answer_9

    $ wuza_mood = "A1"
    $ a_event_0 = renpy.random.random()
    
    if a_event_0 < 1/5:
        wuza "{aw}Ehhh...?{/aw}{w=[wt2]} {bt}Boring...! Boring...!{/bt}{w=[wt2]} {gg}Gee-Hee-Hee...{/gg}"
    elif a_event_0 < 2/5:
        wuza "Aww c'mon!{w=[wt2]} You can't just zone out when I'm all excited to hear your answer!{w=[wt2]} {bt}Not fair...! Not fair...!{/bt}"
    elif a_event_0 < 3/5:
        wuza "{aw}Bleeeeh!{/aw}"
    elif a_event_0 < 4/5:
        wuza "{bt}So mysterious...! So mysterious...!{/bt}{w=[wt2]} Or maybe just shy, huh?{w=[wt2]} {gg}Gee-Hee-Hee...{/gg}"
    else:
        wuza "{pa}TIMEOUT!{/pa}{w=[wt2]} This isn't how the conversation game works!{w=[wt3]} You're supposed to answer when I ask something!{w=[wt2]} {bt}Try again...! Try again...!{/bt}"
        
    jump wuza_interact
