# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wdis_show:

    if wdis_love <= -20:
        $ wdis_mood = "O2"
    elif wdis_love < 0:
        $ wdis_mood = "A2"
    elif wdis_love >= 0:
        $ wdis_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_3

    show WDIS at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wdis_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewdis][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wdis")))))

    if Get_ActivityName("wdis") in ["at class"]:
        jump show_ui

    else:
        return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wdis_interact_end:
    if "interacting_hero" in wdis_know:
        $ wdis_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wdis_interact_start:
    call hide_ui from _call_hide_ui_24
    call wdis_show_activity from _call_wdis_show_activity
    $ wdis_inti = min(char_inti_cap, wdis_inti)
    call hide_ui from _call_hide_ui_25
    call wdis_show from _call_wdis_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wdis_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if hero_map == wdis_map:
        pass

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wdis_interact_check:
    # Save current outfit before any updates
    $ wdis_wear_keep = wdis_wear

    call gametime from _call_gametime_11
    call hide_ui from _call_hide_ui_26

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wdis_wear != wdis_wear_keep:
        $ wdis_wear = wdis_wear_keep

    call wdis_show from _call_wdis_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    if gametimehour >= 18:
        $ wdis_mood = "O2"
        wdis "Uh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I think I{w=[wt2]}, um{w=[wt2]}, will need to go now.{w=[wt3]} It's not that I d{w=[wt1]}-don't want to talk to you, okay?{w=[wt2]} I mean{w=[wt2]}, I hope we can hang out more often.{w=[wt2]} I mean{w=[wt2]}, if you want to.{w=[wt3]} So{w=[wt2]}, g{w=[wt1]}-good bye."
        $ hero_mood = "A2"
        $ wdis_mood = "A2"
        hero "Bye, {nm}[fnamewdis]{/nm}.{w=[wt2]} See ya!"
        $ hero_fx = 0
        jump wdis_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Get_MapName("wdis", "at class"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "wdis"):
            $ wdis_mood = "O2"
            $ wdis_fx = 1
            wdis "O{w=[wt1]}-oh no{w=[wt2]}, c{w=[wt1]}-class is starting!{w=[wt3]} I{w=[wt1]}, um{w=[wt2]}, I need to get to my seat before the teacher{w=[wt1]}-{nw}"
            
            show WDIS at RC
            show WDIS at OR_fast
            show HERO at OR_fast
            wdis "O{w=[wt1]}-oh no{w=[wt2]}, c{w=[wt1]}-class is starting!{w=[wt3]} I{w=[wt1]}, um{w=[wt2]}, I need to get to my seat before the teacher{w=[wt1]}-{fast}{w=[wt1]} {bt}Eek!{/bt}"
            
            jump wdis_interact_end

        else:
            $ wdis_mood = "O2"
            $ wdis_fx = 1
            wdis "Oh gosh{w=[wt2]}, oh gosh{w=[wt2]}, it's class time!{w=[wt3]} I{w=[wt1]}, um{w=[wt2]}, I should probably{w=[wt1]}-{w=[wt2]} I mean{w=[wt1]}, we should go to class now{w=[wt2]}, right?"

            if Get_MapName("wdis", "at class") == Get_MapName(None, "school", "class_1b"):
                menu:
                    "Go together":
                        $ hero_mood = "A2"
                        hero "Want to walk together?"
                        
                        $ wdis_mood = "O3"
                        $ wdis_fx = 2
                        wdis "R{w=[wt1]}-really!?{w=[wt3]} Y{w=[wt1]}-you'd walk with someone like me?{w=[wt3]} I{w=[wt1]}, um{w=[wt2]}, I'm so clumsy though{w=[wt2]}, I might trip and{w=[wt1]}-{w=[wt2]} but{w=[wt1]}, um{w=[wt2]}, yes!{w=[wt2]} Thank you so much!"
                        
                        $ hero_mood = "A2"
                        $ hero_mood = "A2"
                        hero "It's no problem."
                        
                        $ wdis_mood = "A2"
                        $ wdis_fx = 1
                        wdis "{lg}Ehe he he...{/lg}{w=[wt2]} I{w=[wt1]}, um{w=[wt2]}, I'll try not to embarrass you!"
                        
                        scene bg_0
                        with dissolve

                        $ hero_map = wdis_map
                        call gametime from _call_gametime_12
                        call check_playermap from _call_check_playermap_3
                        call hide_ui from _call_hide_ui_27
                        show WDIS at RC
                        show HERO at LC
                        with dissolve
                        
                        $ wdis_mood = "O2"
                        $ wdis_fx = 1
                        wdis "T{w=[wt1]}-thank you again!{w=[wt2]} I'm sorry for being so{w=[wt1]}-"
                        
                        $ hero_mood = "A1"
                        hero "It's fine.{w=[wt2]} See you."
                        
                        $ wdis_mood = "A2"
                        $ wdis_fx = 1
                        wdis "{gg}Ehe he...{/gg}"

                        jump wdis_interact_end
                        
                    "Let her go":
                        pass

            $ hero_mood = "A1"
            hero "Need to do something first.{w=[wt2]} See you!"
            
            $ wdis_mood = "O1"
            $ wdis_fx = 1
            
            wdis "O{w=[wt1]}-okay!{w=[wt3]} I{w=[wt1]}, um{w=[wt2]}{nw}"
            
            show WDIS at RC
            show WDIS at OL_average

            wdis "O{w=[wt1]}-okay!{w=[wt3]} I{w=[wt1]}, um{w=[wt2]}{fast}, I better hurry before I{w=[wt1]}-{nw}"

            $ hero_mood = "O1"
            play SE1 "Slip.ogg"
            wdis "O{w=[wt1]}-okay!{w=[wt3]} I{w=[wt1]}, um{w=[wt2]}, I better hurry before I{w=[wt1]}-{fast} {bt}OHHHH...!{/bt}{nw}"

            play SE1 "Hit2.mp3"
            wdis "O{w=[wt1]}-okay!{w=[wt3]} I{w=[wt1]}, um{w=[wt2]}, I better hurry before I{w=[wt1]}- {bt}OHHHH...!{/bt}{fast}"

        jump wdis_interact_end

    # ----------------------------------------------------------------------------------------------------
    # WDIS is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wdis") in ["eating"]:
        "{nm}[fnamewdis]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamewdis]{/nm} is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wdis") from _call_circletable_2

                while Get_ActivityName("wdis") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_3
                call gametime from _call_gametime_13
                
                jump wdis_interact_start

            "Return":
                jump wdis_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wdis_know:
        $ a_event_0 = renpy.random.random()

        # ----------------------------------------------------------------------------------------------------
        # Bring Up A Topic
        # ----------------------------------------------------------------------------------------------------
        if renpy.random.random() < (0.2 + (wdis_love * 0.003)):
            jump initiative_wdis

        # ----------------------------------------------------------------------------------------------------
        # Common
        # ----------------------------------------------------------------------------------------------------
        elif a_event_0 > 1/4:
            wdis "Uh{w=[wt2]}, you know?{w=[wt2]} Sorry for acting too weird."
        elif a_event_0 > 2/4:
            $ wdis_mood = "A2"
            wdis "H{w=[wt1]}-hey{w=[wt2]}, I wanna say that{w=[wt2]}, um{w=[wt2]}, you know?{w=[wt2]} T{w=[wt1]}-thank you for spending time with someone like me."
        elif a_event_0 > 3/4:
            $ wdis_mood = "A2"
            wdis "S{w=[wt1]}-so{w=[wt2]}, well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Um{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} S{w=[wt1]}-sorry{w=[wt2]}, I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm j{w=[wt1]}-just trying to bring up something to talk about.{w=[wt2]} {gg}He-He...{/gg}"
        else:
            $ wdis_mood = "A2"
            wdis "Well{w=[wt2]}, if I{w=[wt2]}, um{w=[wt2]}, say something t{w=[wt1]}-too stupid{w=[wt2]}, j{w=[wt1]}-just ignore, okay?{w=[wt2]} I just use to do that sometimes."


    # ----------------------------------------------------------------------------------------------------
    # Start Conversation
    # ----------------------------------------------------------------------------------------------------
    #elif "initiative" in wdis_know:
        #wdis "Um{w=[wt2]}, excuse me{w=[wt2]}, I{w=[wt1]}-I hope it's okay to ask{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I mean{w=[wt2]}, if it's not{w=[wt2]}, I'll{w=[wt2]}, like{w=[wt2]}, totally understand{w=[wt2]}, but{w=[wt2]}, um{w=[wt2]}, would we maybe{w=[wt2]}, um{w=[wt2]}, hang out a little?{w=[wt2]} N{w=[wt1]}-not that you have to{w=[wt2]}, I mean{w=[wt2]}, it's totally fine if you don't want to!{w=[wt1]} He-he..."

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_0 = renpy.random.random()
        if wdis_love <= 0:
            wdis "Oh{w=[wt2]}, it's you."
        elif wdis_love < 50:
            wdis "H{w=[wt1]}-hi!"
        elif wdis_love >= 50:
            if a_event_0 < 1/2:
                $ a_event_1 = str(fnamehero[:1])
                wdis "{aw}{nm}[a_event_1]{/nm}-{nm}[a_event_1]{/nm}-{nm}[fnamehero]{/nm}?{/aw}"
            else:
                wdis "{aw}H{w=[wt1]}-h{w=[wt1]}-hi...{/aw}"

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wdis_interact:
    call hide_ui from _call_hide_ui_28
    if "interacting_hero" not in wdis_know:
        $ wdis_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wdis_interact_chat
        "Touch" if not is_specialevent:
            jump wdis_interact_touch
        "Hang out":
            jump wdis_interact_hangout
        "Give item" if not is_specialevent:
            jump wdis_interact_gift
        "Return":
            jump wdis_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wdis_interact_gift:
    $ a_item_8 = "wdis"
    $ a_item_9 = 0
    $ a_item_6 = "wdis_interact"
    call UI_give_Item from _call_UI_give_Item_4

label wdis_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wdis_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wdis_interact_touch:
    menu:
        "Hug":
            label wdis_interact_touch_hug:
                pass

            $ wdis_know.append("Hug")
            $ a_event_0 = sum(1 for buceta in wdis_know if buceta =="Hug")
            $ wdis_fx = 1

            $ a_event_1 = renpy.random.random()
            if a_event_1 <= 0.33:
                scene bg_2 pink
            elif a_event_1 <= 0.66:
                scene bg_2 yellow
            else:
                scene bg_2 flowers

            show action_wdis_hug 1
            with dissolve

            show action_wdis_hug 2

            if perk_cha_sex >= 1:                
                $ msg.msg(renpy.translate_string("{nm}[fnamewdis]{/nm}'s  lust {color=#32FF32}+")+str(2 * perk_cha_sex * lustadd_wdis)[:4])
                $ wdis_lust += 2 * perk_cha_sex * lustadd_wdis

            if a_event_0 == 1:

                $ add_stat("wdis", "love", 2/a_event_0)
                $ add_stat("hero", "cha_sex", (2/a_event_0)/2)

                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.25:
                    wdis "Thank you for being nice to a girl like me."
                elif a_event_0 <= 0.50:
                    wdis "You're so kind."
                elif a_event_0 <= 0.75:
                    wdis "You know what?{w=[wt2]} I think you're{w=[wt1]}, uhh{w=[wt1]}, k{w=[wt1]}-kinda sweet to me.{w=[wt3]} Thank you."
                else:
                    wdis "I k{w=[wt1]}-kinda like this.{w=[wt3]} You're cute."

            elif a_event_0 <= (wdis_inti/char_inti_cap) + (wdis_love * 0.01) + (wdis_lust * 0.01):

                $ add_stat("wdis", "love", 1/a_event_0)
                $ add_stat("hero", "cha_sex", (1/a_event_0)/2)

                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.25:
                    wdis "Huh?{w=[wt2]} It's o{w=[wt1]}-okay{w=[wt2]}, you can hug me whenever you feel lonely."
                elif a_event_0 <= 0.50:
                    wdis "I'm glad you don't mind hugging a girl like me."
                elif a_event_0 <= 0.75:
                    wdis "W{w=[wt1]}-well{w=[wt1]}, okay.{w=[wt2]} I don't mind being like this with you if that's what you want."
                else:
                    wdis "Uhh{w=[wt2]}, you seem to like hugging me.{w=[wt2]} T{w=[wt1]}-that's okay.{w=[wt2]} I j{w=[wt1]}-just don't know how to react."

            else:

                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.25:
                    wdis "H{w=[wt1]}-hey{w=[wt2]}, s{w=[wt1]}-sorry for asking{w=[wt1]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Y{w=[wt1]}-you're not a pervert, right?"
                elif a_event_0 <= 0.50:
                    wdis "W{w=[wt1]}-well{w=[wt2]}, I think it's kind of embarrassing to be hugging so much.{w=[wt2]} But if you're okay with that{w=[wt1]}, that's fine.{w=[wt2]} You don't have to worry about what I said."
                elif a_event_0 <= 0.75:
                    wdis "Hmmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I think you're{w=[wt2]}, uhh{w=[wt2]}, pressing m{w=[wt1]}-my breasts too much."
                else:
                    wdis "You know?{w=[wt3]} If s{w=[wt1]}-someone sees us hugging so much{w=[wt2]}, they might t{w=[wt1]}-think otherwise."

        "Return":
            jump wdis_interact

    show action_wdis_hug 1
    "{nw}"

    call gamecheck from _call_gamecheck_6
    call hide_ui from _call_hide_ui_29
    call wdis_show from _call_wdis_show_2
    $ gametimemin += 10
    $ add_stat("wdis", "inti", 0.1)
    jump wdis_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wdis_interact_hangout:
    menu:
        "Return":
            jump wdis_interact

    $ add_stat("wdis", "inti", 0.3)
    $ gametimemin += 30
    jump wdis_interact_check

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
label wdis_interact_chat:
    menu:
        "Ask how she is" if not "Talk_How" in wdis_know:
            $ hero_mood = "A1"
            $ wdis_mood = "A1"

            # ----------------------------------------------------------------------------------------------------
            # No Special Event
            # ----------------------------------------------------------------------------------------------------
            # else:
            hero "How are you doing?"

            if wdis_love < 25:
                wdis "I'm f{w=[wt1]}-fine.{w=[wt2]} T{w=[wt1]}-thanks for asking!"

            elif wdis_love < 50:
                wdis "I'm f{w=[wt1]}-fine.{w=[wt2]} T{w=[wt1]}-thank you for asking!{w=[wt3]} Well{w=[wt2]}, uhh{w=[wt2]}, w{w=[wt1]}-what about you?"
                hero "I'm fine too.{w=[wt2]} Thanks!"

            else:
                wdis "W{w=[wt1]}-well{w=[wt2]}, You know?{w=[wt2]} I'm always fine when I am with you.{w=[wt3]} S{w=[wt1]}-so{w=[wt2]}, T{w=[wt1]}-thank you for being with me!"
                hero "Know that I’m here for you."
                wdis "Mhm! ❤"

            $ wdis_know.append("Talk")
            $ wdis_know.append("Talk_How")
            $ add_stat("wdis", "love", 0.5)
            $ add_stat("hero", "cha_soc", 0.5)

        "Return":
            jump wdis_interact

    $ add_stat("wdis", "inti", 0.2)
    $ gametimemin += 20
    jump wdis_interact_check

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_wdis:
    $ wdis_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    if renpy.random.random() < (wdis_inti*0.02) and sum(1 for buceta in wdis_know if buceta.startswith("HERO_Y_Girl")) + sum(1 for buceta in wdis_know if buceta.startswith("HERO_N_Girl")) < 4:

        wdis "Well, I was wondering... Um, w-what kind of girl is your type? I mean... It's t-totally fine if you don't wanna answer something like that! Maybe I'm just being too nosy, {gg}He-He...{/gg}"

        # Count already answered categories
        $ a_breast_count = sum(1 for get_id in wdis_know if "Breast_" in get_id)
        $ a_hair_count = sum(1 for get_id in wdis_know if "HairSize_" in get_id)
        $ a_eye_count = sum(1 for get_id in wdis_know if "EyeShape_" in get_id)
        $ a_personality_count = sum(1 for get_id in wdis_know if "Personality_" in get_id)

        # Appearance Likes(Y)/Dislikes(N)
        $ a_event_1 = wdis_know
        $ a_event_3 = "initiative_wdis_return"
        call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_3

        # Store the answer if one was given
        if _return:
            $ wdis_know.append("HERO_Y_Girl_" + _return)

        if a_event_4 == 2:
            $ wdis_mood = "A3"
            $ add_stat("wdis", "love", 0.25)
            $ add_stat("hero", "cha_soc", 0.25)
            wdis "Ehhh!? F-for real? S-so, that's the type of girl you like? I-I mean... Not that I'm trying to, uh, suggest anything! I'm j-just saying, {gg}He-He...{/gg}"
        elif a_event_4 == 1:
            $ wdis_mood = "A1"
            wdis "Well, that's kinda interesting, I guess, {gg}He-He...{/gg}"
        else:
            $ wdis_mood = "O1"
            wdis "This type of girl seems to be much more interesting, doesn't it? Of course that's the type of girl you would like, right? {gg}He-He...{/gg}"

        $ gametimemin += 20
        $ add_stat("wdis", "inti", 0.20)
        jump wdis_interact

    #elif renpy.random.random() < (wdis_inti*0.01):
        #wdis "S-so, I was wondering, what's your favorite kind of movie? I mean... I'm just curious..."

# ----------------------------------------------------------------------------------------------------
# Random Chitchat
# ----------------------------------------------------------------------------------------------------
    else:

        $ a_event_0 = renpy.random.random()

        if a_event_0 > 0.75:
            $ wdis_mood = "A2"
            wdis "Uh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I{w=[wt1]}-I was just wondering{w=[wt2]}, do you ever{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} um{w=[wt2]}, think about{w=[wt2]}, like{w=[wt2]}, dumb things?{w=[wt2]} L{w=[wt1]}-like{w=[wt2]}, really dumb?{w=[wt2]} Because{w=[wt2]}, you know{w=[wt2]}, I do that all the time.{w=[wt2]} {gg}He-He...{/gg}{w=[wt3]} S{w=[wt1]}-sorry.{w=[wt2]} Forget what I just said, please."
            jump initiative_wdis_heroanswer2

        elif a_event_0 > 0.5:
            $ wdis_mood = "A2"
            wdis "You know{w=[wt2]}, I heard someone say 'the sky's the limit'{w=[wt2]}, but{w=[wt2]}, you know{w=[wt2]}, um{w=[wt2]}, I don't really think the sky can limit something.{w=[wt3]} I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} There must be much more than that{w=[wt2]}, I guess.{w=[wt2]} I don't know.{w=[wt2]} Sorry."
            jump initiative_wdis_heroanswer1

        elif a_event_0 > 0.25:
            $ wdis_mood = "A2"
            wdis "You know{w=[wt2]}, I heard people say 'love is blind'{w=[wt2]}, but{w=[wt2]}, um{w=[wt2]}, does that mean{w=[wt2]}, like{w=[wt2]}, you can't see the person you love?{w=[wt4]} Cos{w=[wt2]}, you know?{w=[wt2]} I think that sounds kinda scary."
            jump initiative_wdis_heroanswer1

        else:
            $ wdis_mood = "A2"
            wdis "Well, um, n-nevermind."

    $ gametimemin += 10
    $ add_stat("wdis", "inti", 0.10)
    jump wdis_interact

# ----------------------------------------------------------------------------------------------------
label initiative_wdis_heroanswer1:
    $ hero_mood = "A2"
    hero "Well...{w=[wt1]}-{nw}"

    $ wdis_mood = "O2"
    wdis "{aw}P{w=[wt1]}-please{w=[wt2]}, just forget what I said!{/aw}"

# ----------------------------------------------------------------------------------------------------
label initiative_wdis_heroanswer2:
    $ hero_mood = "O1"
    hero "{aw}Ehhh...?{/aw}"

    $ gametimemin += 10
    $ add_stat("wdis", "inti", 0.10)
    jump wdis_interact

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wdis_return:

    call hero_n_answer from _call_hero_n_answer_3

    wdis "O{w=[wt1]}-oh{w=[wt2]}, sure!{w=[wt3]} I'm sorry for asking! {gg}He-He...{/gg}"
