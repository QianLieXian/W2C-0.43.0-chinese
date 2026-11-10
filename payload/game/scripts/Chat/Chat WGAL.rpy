# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wgal_show:

    if wgal_love < 0:
        $ wgal_mood = "O2"
    elif wgal_love < 30:
        $ wgal_mood = "A2"
    elif wgal_love < 60:
        $ wgal_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_4

    show WGAL at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wgal_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewgal][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wgal")))))

    if Get_ActivityName("wgal") in ["at class"]:
        jump show_ui

    else:
        return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wgal_interact_end:
    if "interacting_hero" in wgal_know:
        $ wgal_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wgal_interact_start:
    call hide_ui from _call_hide_ui_30
    call wgal_show_activity from _call_wgal_show_activity
    $ wgal_inti = min(char_inti_cap, wgal_inti)
    call hide_ui from _call_hide_ui_31
    call wgal_show from _call_wgal_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wgal_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if hero_map == wgal_map:
        pass

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wgal_interact_check:
    # Save current outfit before any updates
    $ wgal_wear_keep = wgal_wear

    call gametime from _call_gametime_14
    call hide_ui from _call_hide_ui_32

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wgal_wear != wgal_wear_keep:
        $ wgal_wear = wgal_wear_keep

    call wgal_show from _call_wgal_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    if gametimehour >= 18:
        wgal "Er{w=[wt2]}, The chat is cool and all{w=[wt2]}, but I{w=[wt2]}, like{w=[wt2]}, have to go now, you know?{w=[wt3]} So see ya."
        $ hero_fx = 0
        jump wgal_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Get_MapName("wgal", "at class"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "wgal"):
            $ wgal_mood = "O1"
            wgal "Ugh{w=[wt2]}, like{w=[wt2]}, teacher's here already?{w=[wt3]} Hmph.{nw}"

            show WGAL at RC
            show WGAL at OR_slow
            show HERO at OR_slow
            wgal "Ugh{w=[wt2]}, like{w=[wt2]}, teacher's here already?{w=[wt3]} Hmph.{fast}{w=[wt2]} Later{w=[wt2]}, loser."

            jump wgal_interact_end

        else:
            $ wgal_mood = "O1"
            wgal "Ugh{w=[wt2]}, I{w=[wt2]}, like{w=[wt2]}, totally need to get to class now.{w=[wt3]} Such a drag."

            if Get_MapName("wgal", "at class") == Get_MapName(None, "school", "class_1b"):
                menu:
                    "Go together":
                        $ hero_mood = "A1"
                        hero "I'm heading there too.{w=[wt2]} Let's go!"
                        
                        $ wgal_mood = "O2"
                        wgal "Ugh{w=[wt2]}, just don't{w=[wt2]}, like{w=[wt2]}, walk too close or anything.{w=[wt3]} You'll embarrass me."
                        
                        $ hero_mood = "O1"
                        hero "I'm just walking to class."
                        
                        $ wgal_mood = "O1"
                        wgal "Yeah{w=[wt2]}, yeah.{w=[wt3]} That's{w=[wt2]}, like{w=[wt2]}, totally what I said, idiot.{w=[wt2]} C'mon then."
                        
                        scene bg_0
                        with dissolve

                        $ hero_map = wgal_map
                        call gametime from _call_gametime_15
                        call check_playermap from _call_check_playermap_4
                        call hide_ui from _call_hide_ui_33
                        show WGAL at RC
                        show HERO at LC
                        with dissolve
                        
                        $ wgal_mood = "O1"
                        wgal "Okay{w=[wt2]}, like{w=[wt2]}, you can go now."

                        jump wgal_interact_end
                        
                    "Let her go":
                        pass

            $ hero_mood = "A1"
            hero "See you!"
            
            $ wgal_mood = "O1"
            wgal "Yeah{w=[wt2]}, whatever."
            
            show WGAL at RC
            show WGAL at OR_slow
            pause(1.5)

        jump wgal_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wgal_know:
        $ a_event_0 = renpy.random.random()

        if renpy.random.random() < (0.5+(wgal_love*0.003)):
            jump initiative_wgal

        else:
            wgal "So{w=[wt2]}, what else?"

    # ----------------------------------------------------------------------------------------------------
    # WGAL is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wgal") in ["eating"]:
        "{nm}[fnamewgal]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamewgal]{/nm} is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wgal") from _call_circletable_3

                while Get_ActivityName("wgal") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_4
                call gametime from _call_gametime_16
                
                jump wgal_interact_start

            "Return":
                jump wgal_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_0 = renpy.random.random()
        if wgal_love < 0:
            if a_event_0 < 1/5:
                wgal "What, loser?{w=[wt3]} Did you lose something in my face?"
            elif a_event_0 < 2/5:
                wgal "Ohh, serious?{w=[wt2]} Do you really have no one else to bother?{w=[wt3]} Get lost, loser."
            elif a_event_0 < 3/5:
                wgal "Ugh{w=[wt2]}, like{w=[wt2]}, what do you want, loser?{w=[wt3]} Can't you see I'm{w=[wt2]}, like{w=[wt2]}, totally busy for you?"
            elif a_event_0 < 4/5:
                wgal "Oh em gee{w=[wt2]}, it's the walking fashion disaster.{w=[wt3]} What{w=[wt2]}, did you get lost on your way to Loserville?"
            else:
                wgal "Seriously?{w=[wt3]} You again?{w=[wt3]} Don't you have{w=[wt2]}, like{w=[wt2]}, anyone else to bother?{w=[wt3]} As if I'd waste my time on you."

        elif wgal_love < 30:
            if a_event_0 < 1/7:
                wgal "Hmm?"
            elif a_event_0 < 2/7:
                wgal "What?"
            elif a_event_0 < 3/7:
                wgal "..."
            elif a_event_0 < 4/7:
                wgal "Um{w=[wt2]}, yeah?{w=[wt2]} What do you want?"
            elif a_event_0 < 5/7:
                wgal "Ugh{w=[wt2]}, it's you.{w=[wt3]} Make it quick, 'kay?{w=[wt3]} I've got important people to see."
            elif a_event_0 < 6/7:
                wgal "Like{w=[wt2]}, do you need something?{w=[wt3]} Or are you just here to admire my fabulousness?"
            else:
                wgal "Oh great{w=[wt2]}, it's the charity case.{w=[wt3]} What{w=[wt2]}, need fashion advice or something?"

        elif wgal_love < 60:
            if a_event_0 < 1/4:
                wgal "Hey{w=[wt2]}, it's you.{w=[wt3]} Like{w=[wt2]}, what's up?"
            elif a_event_0 < 2/4:
                wgal "Oh{w=[wt2]}, hey there.{w=[wt2]} You're kinda looking{w=[wt2]}, like{w=[wt2]}, less tragic than usual, I guess."
            elif a_event_0 < 3/4:
                wgal "{bt}Well... Well...{/bt}{w=[wt3]} If it isn't my favorite dog.{w=[wt3]} The paws, dear.{w=[wt2]} C'mon!"
            else:
                wgal "So{w=[wt2]}, any juicy gossip?"

        else:
            if a_event_0 < 1/5:
                wgal "{bt}Hey there... ~❤{/bt}"
            elif a_event_0 < 2/5:
                wgal "{bt}Dork...! ~❤{/bt}{w=[wt3]}"
            elif a_event_0 < 3/5:
                wgal "{bt}Hi, loser! ~❤{/bt}{w=[wt3]} Came to bask in my fabulous presence?"
            elif a_event_0 < 4/5:
                wgal "{bt}Well, hellooo! ~❤{/bt}{w=[wt3]} You're looking particularly non-loserish today.{w=[wt2]} What's your secret?"
            else:
                wgal "{bt}Heeey...! ~❤{/bt}{w=[wt2]} Wanna{w=[wt2]}, like{w=[wt2]}, hang out or whatever?{w=[wt4]} I mean{w=[wt2]}, if you're not too busy being a total dork, of course."

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wgal_interact:
    call hide_ui from _call_hide_ui_34
    if "interacting_hero" not in wgal_know:
        $ wgal_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wgal_interact_chat
        "Touch" if not is_specialevent:
            jump wgal_interact_touch
        "Hang out":
            jump wgal_interact_hangout
        "Give item" if not is_specialevent:
            jump wgal_interact_gift
        "Return":
            jump wgal_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wgal_interact_gift:
    $ a_item_8 = "wgal"
    $ a_item_9 = 2
    $ a_item_6 = "wgal_interact"
    call UI_give_Item from _call_UI_give_Item_5

label wgal_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wgal_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wgal_interact_touch:
    menu:
        "Hug":
            label wgal_interact_touch_hug:
                pass

            if not "Hug_Enough" in wgal_know:
                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.33:
                    scene bg_2 pink
                elif a_event_0 <= 0.66:
                    scene bg_2 yellow
                else:
                    scene bg_2 flowers

                $ wgal_know.append("Hug")
                $ a_event_0 = sum(1 for get_id in wgal_know if get_id =="Hug")
                $ wgal_fx = 1

                if perk_cha_sex >= 1:                
                    $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm}'s  lust {color=#32FF32}+")+str(2 * perk_cha_sex * lustadd_wgal)[:4])
                    $ wgal_lust += 2 * perk_cha_sex * lustadd_wgal

                if (wgal_inti >= char_inti_cap/2) and (wgal_love >= 50) and a_event_0 < 2:

                    show action_wgal_hug3
                    with dissolve

                    $ add_stat("wgal", "love", 1/a_event_0)
                    $ add_stat("hero", "cha_sex", (1/a_event_0)/2)

                    pause

                elif (wgal_inti >= char_inti_cap/2):

                    show action_wgal_hug2
                    with dissolve

                    $ wgal_know.append("Hug_Enough")
                    $ add_stat("wgal", "love", 0.5/a_event_0)
                    $ add_stat("hero", "cha_sex", (0.5/a_event_0)/2)

                    $ a_event_0 = renpy.random.random()
                    if a_event_0 <= 0.33:
                        wgal "{bt}Okay... Okay...{/bt}{w=[wt2]} Now{w=[wt1]}, like{w=[wt1]}, {bt}get lost{/bt}."
                    elif a_event_0 <= 0.66:
                        wgal "{aw}Ugh...{/aw}{w=[wt2]} Nice to see you too virgin.{w=[wt2]} Now{w=[wt1]}, like{w=[wt1]}, get lost okay?"
                    else:
                        wgal "{aw}Ugh...{/aw}{w=[wt2]} Okay{w=[wt2]}, just once.{w=[wt2]} Now control your virgin hormones."

                else:

                    $ wgal_know.append("Hug_Enough")
                    show action_wgal_hug1
                    with dissolve

                    $ a_event_0 = renpy.random.random()
                    if a_event_0 <= 0.25:
                        wgal "{aw}Ugh, what was it?{w=[wt2]} Your virgin hormones got out of control?{/aw}"
                    elif a_event_0 <= 0.50:
                        wgal "Does the virgin want to feel what it's like to hug a woman?{w=[wt2]} Disgusting...!"
                    else:
                        if "WSIS_IS_Acquaintance" in wgal_know:
                            wgal "{aw}Ugh...!{/aw}{w=[wt2]} Why don't you go hug that little bitch friend of yours?"
                        elif "WSIS_IS_Sister" in wgal_know:
                            wgal "{aw}Ugh...!{/aw}{w=[wt2]} Why don't you go hug that little bitch sister of yours?"
                        elif "WSIS_IS_Stepsister" in wgal_know:
                            wgal "{aw}Ugh...!{/aw}{w=[wt2]} Why don't you go hug that little bitch step-sister of yours?"
                        else: # "WSIS_IS_Girlfriend" in wgal_know
                            wgal "{aw}Ugh...!{/aw}{w=[wt2]} Does your little bitch girlfriend know that you're going after real women behind her back?"

                call gamecheck from _call_gamecheck_7
                call hide_ui from _call_hide_ui_35
                call wgal_show from _call_wgal_show_2

                $ gametimemin += 10
                $ add_stat("wgal", "inti", 0.1)

            else:
                show HERO at CC_average
                pause(0.2)
                $ wgal_mood = "O3"
                $ hero_mood = "O1"
                show HERO at Stay

                wgal "{aw}Ugh!{/aw}{w=[wt2]}{nw}"

                show HERO at LC_slow

                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.33:
                    wgal "{aw}Ugh!{/aw}{fast} Enough of all the clinging, okay?"
                elif a_event_0 <= 0.66:
                    wgal "{aw}Ugh!{/aw}{fast} Can you control your virginity urges for once!?{w=[wt2]} Thank you!"
                else:
                    wgal "{aw}Ugh!{/aw}{fast} Enough for you, virgin.{w=[wt2]} Get lost."

                jump wgal_interact



        "Return":
            jump wgal_interact

    jump wgal_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wgal_interact_hangout:
    menu:
        "Return":
            jump wgal_interact

    $ gametimemin += 30
    jump wgal_interact_check

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
label wgal_interact_chat:
    menu:
        "Ask how she is" if not "Talk_How" in wgal_know:
            $ hero_mood = "A1"
            # ----------------------------------------------------------------------------------------------------
            # Asking at morning
            # ----------------------------------------------------------------------------------------------------
            if gametimehour >= 8 and gametimehour < 12:

                hero "How are you {nm}[fnamewgal]{/nm}?"

                if wgal_love < 25:
                    $ wgal_mood = "O1"
                    wgal "Well{w=[wt2]}, my day was kind of starting well{w=[wt2]}, but then you showed up."
                    $ hero_mood = "O1"
                    hero "{aw}Ehhh!?{/aw}"

                elif wgal_love < 50:
                    $ wgal_mood = "A1"
                    wgal "Fine{w=[wt2]}, and you?"
                    hero "Me too. Thanks!"

                else:
                    $ wgal_mood = "A1"
                    wgal "I'm much better now, and you?"
                    hero "Well{w=[wt2]}, I can say that too, I guess."
                    wgal "Of course you're{w=[wt2]}, like{w=[wt2]}, {bt}much better{/bt} now.{w=[wt3]} I can even see your eyes shining, you fool!"

            # ----------------------------------------------------------------------------------------------------
            # Asking after morning
            # ----------------------------------------------------------------------------------------------------
            elif gametimehour >= 12 and gametimehour < 18:

                hero "Hey{w=[wt2]}, how was your day?"

                if wgal_love < 25:
                    $ wgal_mood = "O1"
                    wgal "It was doing fine until you came."
                    $ hero_mood = "O1"
                    hero "{aw}Ehhh!?{/aw}"

                elif wgal_love < 50:
                    $ wgal_mood = "A1"
                    wgal "Fine{w=[wt2]}, and yours?"
                    hero "Mine too. Thanks!"

                else:
                    $ wgal_mood = "A1"
                    wgal "Nothing really interesting.{w=[wt3]} I mean{w=[wt2]}, I'm better now, you know?"
                    hero "Yeah{w=[wt2]}, you're welcome.{w=[wt3]} I'm here for you."
                    $ wgal_mood = "A4"
                    wgal "{lg}Ba Ha Ha Ha...{/lg}{w=[wt2]} Idiot!"

            # ----------------------------------------------------------------------------------------------------
            # Asking at any other time
            # ----------------------------------------------------------------------------------------------------
            else:
                hero "How are you doing?"

                if wgal_love < 25:
                    $ wgal_mood = "O1"
                    wgal "Well{w=[wt2]}, I was doing fine until you came."
                    $ hero_mood = "O1"
                    hero "{aw}Ehhh!?{/aw}"

                elif wgal_love < 50:
                    $ wgal_mood = "A1"
                    wgal "Fine{w=[wt2]}, and you?"
                    hero "Me too.{w=[wt2]} Thanks!"

                else:
                    $ wgal_mood = "A1"
                    wgal "I'm much better now{w=[wt2]}, and you?"
                    hero "Well{w=[wt2]}, I can say that too, I guess."
                    wgal "Of course you're{w=[wt2]}, like{w=[wt2]}, {bt}much better{/bt} now.{w=[wt3]} I can even see your eyes shining, you fool!"

            $ wgal_know.append("Talk")
            $ wgal_know.append("Talk_How")
            $ add_stat("wgal", "love", 0.5)
            $ add_stat("hero", "cha_soc", 0.5)

        "Talk about someone":
            menu:
                "{image=icon_wsis} {nm}[fnamewsis] [lnamestep]{/nm}" if not "Talk_Char_WSIS" in wgal_know:
                    $ wgal_know.append("Talk_Char_WSIS")

                    if not "WGAL_BG_WSIS_1" in hero_know:
                        $ hero_know.append("WGAL_BG_WSIS_1")
                        $ msg.msg(renpy.translate_string("You know {nm}[fnamewgal]{/nm} a little more"))
                        $ add_stat("wgal", "inti", 1)

                        $ hero_mood = "A2"
                        hero "Sorry to ask{w=[wt2]}, but{w=[wt2]}, why you and {nm}[fnamewsis]{/nm} seems to hate each other so much?{w=[wt3]} You girls kinda seem to have been through a lot."

                        $ wgal_mood = "O1"
                        wgal "Hunf!{w=[wt3]} Going through a lot is a just little compared to what I went through with that little bitch.{w=[wt3]} I considered her my friend{w=[wt2]}, we used to hang out{w=[wt2]}, talk a lot{w=[wt2]}, and sometimes I spent the day at her house.{w=[wt3]} Her mother's a super lovely person{w=[wt2]}, but she{w=[wt2]}, like{w=[wt2]}, she's a super fake bitch!"

                        $ hero_mood = "O1"
                        wgal "Look{w=[wt2]}, I don't know how much you trust her{w=[wt2]}, but I wouldn't be surprised if you do.{w=[wt3]} She's a wolf in sheep's clothes after all.{w=[wt3]} But{w=[wt2]}, like{w=[wt2]}, It's good you know that little bitch stabs you in the back when you least expect it."
                        hero "W{w=[wt1]}-wait!{w=[wt2]} Hold on!{w=[wt2]} Are we talking about the same person?"

                        $ wgal_mood = "A2"
                        wgal "{nm}[fnamewsis] [lnamestep]{/nm}.{w=[wt3]} Wasn't that the person you asked about?{w=[wt2]} You know{w=[wt2]}, the little bitch with pink hair and tin tooth.{w=[wt3]} Know her?{w=[wt3]} If it wasn't{w=[wt2]}, then{w=[wt2]}, like{w=[wt2]}, sorry to compare that person to such a whore, okay?{w=[wt3]} Seriously{w=[wt2]}, I don't know who did you ask about{w=[wt2]}, but this person didn't deserve that comparison."
                        wgal "But{w=[wt2]}, look{w=[wt2]}, I'm glad I made a mistake{w=[wt2]}, cos just thinking about that bitch was already getting on my nerves.{w=[wt3]} So that means I can avoid talking about her, right?"

                        $ wgal_mood = "O1"
                        hero "Well{w=[wt1]}-{nw}"

                        $ wgal_mood = "A2"
                        wgal "Oh{w=[wt1]}, thank you!{w=[wt3]} I'm glad you understand."

                    elif not "WGAL_BG_WSIS_2" in hero_know:

                        $ hero_mood = "O1"
                        hero "I'm sorry to bring this up again.{w=[wt3]} I just can't get what you told me out of my head.{w=[wt3]} W{w=[wt1]}-well{w=[wt2]}, huh{w=[wt2]}, what did {nm}[fnamewsis]{/nm} do to make you hate her so much?"

                        if not (wgal_inti >= min(20, char_inti_cap)) or not (wgal_love >= 25):
                            $ wgal_mood = "O3"
                            wgal "That's none of your business, loser.{w=[wt3]} Who do you think you are to make me tell you such a personal thing of my life?{w=[wt4]} Like{w=[wt2]}, get lost, okay?"
                            hero "S{w=[wt1]}-sorry{w=[wt2]}, I didn't mean to."
                            wgal "Yeah, yeah.{w=[wt3]} Whatever."
                            if not (wgal_inti >= min(20, char_inti_cap)):
                                mind "(She doesn't seem to feel close enough to me to have this kind of conversation.)"
                            elif not (wgal_love >= 25):
                                mind "(She doesn't seem to like me enough to have this kind of conversation.)"

                        else:

                            $ wgal_mood = "O2"
                            $ hero_know.append("WGAL_BG_WSIS_2")
                            $ msg.msg(renpy.translate_string("You know {nm}[fnamewgal]{/nm} a little more"))
                            $ add_stat("wgal", "inti", 1)

                            wgal "{w=[wt1]}.{w=[wt1]} .{w=[wt1]} .{w=[wt4]} {bt}(sigh){/bt}.{w=[wt4]} Fine.{w=[wt4]} I used to like a guy{w=[wt2]}, and this little bitch hit on him even though I was into him.{w=[wt4]} That's it.{w=[wt3]} Satisfied?"
                            hero "Oh.{w=[wt2]} Sorry for that.{w=[wt3]} S{w=[wt1]}-so{w=[wt2]}, you two had a fight and never spoke again?"

                            $ wgal_mood = "O3"
                            wgal "Oh{w=[wt2]}, of course you wasn't satisfied.{w=[wt3]} Why did I even ask?{w=[wt3]} But{w=[wt2]}, like{w=[wt3]}, {bt}OOOBVIOUSLY...!{/bt}{w=[wt2]} {bt}Duuuh...!{/bt}{w=[wt4]} Why do you think I would keep talking to a person who claims to be my friend and stabs me in the back?{w=[wt3]} I know you're stupid{w=[wt2]}, but this must be too much even for you, right?{w=[wt3]} Like{w=[wt2]}, I really hope so!"
                            hero "Okay, okay.{w=[wt2]} I got it."
                            wgal "So{w=[wt2]}, what else?{w=[wt3]} Are you also gonna ask me who the boy is and meddle even more in my life or can we forget about that already?"
                            hero "Ehh!?{w=[wt2]} So he's someone I know?"
                            wgal "{pa}OH{w=[wt2]}, GOD!{w=[wt3]} STOP!{/pa}{w=[wt4]} I've told you too much, okay?{w=[wt3]} You know?{w=[wt2]} I already regretted talking to you!{w=[wt3]} So please{w=[wt2]}, can you at least forget about it for once!?!?"
                            hero "Well{w=[wt1]}-{nw}"
                            wgal "{bt}Thank you!{/bt}{w=[wt3]} I knew you'd understand."

                    else:
                        hero "You know?{w=[wt2]} I think you and {nm}[fnamewsis]{/nm} must have been through some kind of misunderstanding.{w=[wt3]} I'd be happy if you girls got back together."
                        wgal "There’s no such thing as a disagreement with knowing that a slut went out with the guy you were into.{w=[wt3]} Like{w=[wt2]}, you can’t deny a fact.{w=[wt3]} Either you do something about it or you pretend it’s okay{w=[wt2]}, which{w=[wt2]}, like{w=[wt2]}, is not my case, obviously.{w=[wt4]} And enough about meddling in my life, okay?"

                "Return":
                    jump wgal_interact_chat

        "Return":
            jump wgal_interact

    $ add_stat("wgal", "inti", 0.2)
    $ gametimemin += 20
    jump wgal_interact_check

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_wgal:
    $ wgal_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------------------------------------------------------------------------------------------------
    # Ask about HERO's life with roomates
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wgal_inti*0.01) and not any(get_id.startswith("Talk_6") for get_id in wgal_know) and ("WSIS_IS_Sister" in wgal_know or "WSIS_IS_Stepsister" in wgal_know):

        if not "HERO_BG_MoveBackIn" in wgal_know: # wgal doesn't know that hero lived back with WSIS and WMOM recently.

            if "WSIS_IS_Sister" in wgal_know:
                wgal "So{w=[wt2]}, like{w=[wt2]}, do you live with that bitchy sister of yours?{w=[wt3]} Like{w=[wt2]}, I was already studying with her and didn't know you a few years ago, you know."
            elif "WSIS_IS_Stepsister" in wgal_know:
                wgal "So{w=[wt2]}, like{w=[wt2]}, do you live with that bitchy stepsister of yours?{w=[wt3]} Like{w=[wt2]}, I was already studying with her and didn't know you a few years ago, you know."

            menu:
                "Tell you lived in the countryside":
                    $ wgal_know.append("HERO_BG_Countryside") # wgal memory stores that hero lived in the countryside.
                    $ wgal_know.append("HERO_BG_MoveBackIn") # wgal memory stores that hero lived back with WSIS and WMOM recently.
                    $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} knows you a little more"))
                    $ add_stat("wgal", "inti", 1)

                    hero "Actually{w=[wt2]}, we only used to live together in childhood{w=[wt2]}, but I moved to the countryside and ended up spending all my adolescence there.{w=[wt3]} Just recently I came back to city and now I'm living with her again."
                    wgal "Oh, nice!{w=[wt2]} That makes sense.{w=[wt2]} You do really look like a bumpkin! {bt}Ba Ha Ha Ha...{/bt}{w=[wt4]} That's probably why you attract the trust of weirdos like {nm}[fnamehprv]{/nm}.{w=[wt3]} Like{w=[wt2]}, his behavior kinda looks like that of an animal that follows a herd.{w=[wt3]} Or maybe{w=[wt2]}, like{w=[wt2]}, that giant head of his is a pumpkin!{w=[wt3]} At the end of the day{w=[wt1]}, you leave the countryside but the countryside doesn't leave you."

                "Just tell that you moved back in now":
                    $ wgal_know.append("HERO_BG_MoveBackIn") # wgal memory stores that hero lived back with WSIS and WMOM recently.
                    $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} knows you a little more"))
                    $ add_stat("wgal", "inti", 0.5)

                    hero "Well{w=[wt2]}, some things happened and we only recently moved back in together."
                    if "WGAL_BG_WSIS_1" in hero_know:
                        wgal "I get it.{w=[wt4]} No offense{w=[wt2]}, but{w=[wt2]}, like{w=[wt2]}, your family seems really weird.{w=[wt3]} You have nothing to do with each other{w=[wt2]}, both in appearance and personality, I guess."
                    else:
                        $ hero_know.append("WGAL_BG_WSIS_1")
                        $ msg.msg(renpy.translate_string("You know {nm}[fnamewgal]{/nm} a little more"))
                        $ add_stat("wgal", "inti", 1)

                        wgal "I get it.{w=[wt4]} I used to talk to {nm}[fnamewsis]{/nm}{w=[wt2]}, go to her house and all stuff like that.{w=[wt3]} So{w=[wt2]}, like{w=[wt2]}, I kinda know your family, I guess.{w=[wt3]} And{w=[wt2]}, no offense{w=[wt2]}, but{w=[wt2]}, like{w=[wt2]}, you guys seems really weird.{w=[wt3]} You have nothing to do with each other{w=[wt2]}, both in appearance and personality, I guess."

                "Don't choose":
                    jump initiative_wgal_return

        if "WSIS_IS_Sister" in wgal_know:
            wgal "So{w=[wt2]}, how is life living with your mother and sister again?{w=[wt3]} Must be {bt}SUPER{/bt} weird, right?"

        elif "WSIS_IS_Stepsister" in wgal_know:
            wgal "So{w=[wt2]}, how is life living with your stepmother and stepsister again?{w=[wt3]} Must be {bt}SUPER{/bt} weird, right?"

        menu:
            "Good":
                $ wsis_bonus += 10
                $ msg.msg(renpy.translate_string("+ 10% bonus for next interations with {nm}[fnamewsis]{/nm}"))
                $ wgal_know.append("Talk_6_1") # wgal memory stores that hero answered 3rd option of dialogue 6
                hero "Well{w=[wt2]}, we've got a lot of memories together{w=[wt2]}, so it wasn't too hard to adjust my life.{w=[wt3]} Actually, it feels like home."
                wgal "Good for you, I guess.{w=[wt3]} Not everyone gets that, you know.{w=[wt3]} As long as you're not{w=[wt2]}, like{w=[wt2]}, a total weirdo at home too."

            "Bad":
                $ add_stat("wgal", "love", 1)
                $ add_stat("hero", "cha_soc", 1)
                $ wgal_know.append("Talk_6_2") # wgal memory stores that hero answered 3rd option of dialogue 6
                hero "Actually{w=[wt2]}, I'd rather not have to live with them again.{w=[wt3]} But I didn't have many options."
                wgal "Yeah{w=[wt2]}, I get it.{w=[wt3]} Must suck, right?{w=[wt3]} Family's a pain in the ass.{w=[wt3]} Mine {bt}TOTALLY{/bt} sucks{w=[wt2]}, and yet{w=[wt2]}, I didn't want to be in your shoes living with that little bitch.{w=[wt3]} Feel bad for you, dude."
                hero "Well{w=[wt2]}, we are trying to get along."
                wgal "Yeah, yeah.{w=[wt3]} I used to try to do that too{w=[wt2]}, but{w=[wt2]}, you know?{w=[wt4]} I gave up.{w=[wt3]} So{w=[wt2]}, like{w=[wt2]}, good luck!{w=[wt2]} You'll need it."

            "Neither":
                $ wsis_bonus += 5
                $ msg.msg(renpy.translate_string("+ 5% bonus for next interations with {nm}[fnamewsis]{/nm}"))
                $ add_stat("wgal", "love", 0.5)
                $ add_stat("hero", "cha_soc", 0.5)
                $ wgal_know.append("Talk_6_3") # wgal memory stores that hero answered 1st option of dialogue 6

                hero "It's been an adjustment{w=[wt2]}, but {nm}[hero_about_wmom]{/nm} have been really supportive.{w=[wt4]} I think we're all still getting used to living together again."
                wgal "Must be awkward.{w=[wt3]} Bet you have{w=[wt2]}, like{w=[wt2]}, {bt}A TON{/bt} of weird moments."
                hero "M{w=[wt1]}-maybe there have been some{w=[wt2]}, but we're managing.{w=[wt3]} It's kinda nice to have them around, I guess."
                wgal "Yeah, yeah.{w=[wt3]} Family can be a pain{w=[wt2]}, but{w=[wt2]}, like{w=[wt2]}, good for you, I guess."

            "Don't choose":
                jump initiative_wgal_return

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wgal_inti*0.02) and not any(get_id.startswith("HERO_Dated") for get_id in wgal_know):

        wgal "So{w=[wt2]}, have you ever dated?{w=[wt2]} Or{w=[wt2]}, like{w=[wt2]}, at least know what it's like to kiss someone?{w=[wt3]} Like{w=[wt2]}, dating your own hand doesn't count, obviously!"

        $ hero_fx = 1
        $ hero_mood = "O1"

        menu:
            wgal "So, have you ever dated? Or, like, at least know what it's like to kiss someone? Like, dating your own hand doesn't count, obviously.{fast}"
            
            "Deny":
                $ wgal_know.append("HERO_Dated_N")
                $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} knows you a little more"))
                $ add_stat("wgal", "inti", 0.5)
                hero "N{w=[wt1]}-No{w=[wt2]}, I've never dated before."

                $ wgal_mood = "A4"
                show WGAL at Laugh
                wgal "{lg}Ba Ha Ha Ha...{/lg}{w=[wt4]}{nw}"

                $ wgal_mood = "A2"
                show WGAL at RC
                wgal "{lg}Ba Ha Ha Ha...{/lg}{fast} Of course you didn't, virgin.{w=[wt2]} I just asked to see your reaction."

            "Confirm":
                $ wgal_know.append("HERO_Dated_Y")
                $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} knows you a little more"))
                $ add_stat("wgal", "inti", 0.5)
                hero "W{w=[wt1]}-well{w=[wt2]}, y{w=[wt1]}-yes{w=[wt2]}, I kinda dated a girl once."

                $ wgal_mood = "A2"
                wgal "Yeah, yeah.{w=[wt2]} An inflatable doll, right?"
                hero "Of course not!"
                wgal "Yeah.{w=[wt1]} As if."

    # ----------------------------------------------------------------------------------------------------
    # Ask HERO's girl preference
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wgal_inti*0.02) and sum(1 for get_id in wgal_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wgal_know if get_id.startswith("HERO_N_Girl")) < 4:
        wgal "So{w=[wt2]}, what kind of girl is your type?{nw}"

        menu:
            wgal "So, what kind of girl is your type?{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in wgal_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in wgal_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in wgal_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in wgal_know if "Personality_" in get_id)

                # Appearance Likes(Y)/Dislikes(N)
                $ a_event_1 = wgal_know
                $ a_event_3 = "initiative_wgal_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_4

                # Store the answer if one was given
                if _return:
                    $ wgal_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} knows you a little more"))
                $ add_stat("wgal", "inti", 0.5)

                if _return in ["Breast_2", "Breast_3", "Personality_5", "Personality_11", "HairSize_4", "HairSize_5"]: # Match - medium/big breasts, outgoing, visually diligent, medium-long hair
                    $ add_stat("wgal", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ wgal_mood = "A3"
                    wgal "Of course{w=[wt1]}, virgin.{w=[wt2]} Nice try.{w=[wt3]} Like{w=[wt2]}, maybe in your dreams you can date a girl like that."

                elif _return in ["Personality_12", "Personality_6", "Breast_0", "Breast_1", "HairSize_0", "HairSize_1"]: # Opposite match - sloppy, shy, flat/tiny breasts, short/bald hair
                    $ add_stat("wgal", "bonus", -10)
                    $ wgal_mood = "O1"
                    wgal "Yeah{w=[wt2]}, that's nice for you.{w=[wt3]} Like{w=[wt2]}, maybe someone like this is on your level."

                else: # Others
                    $ wgal_mood = "A1"
                    wgal "Well{w=[wt2]}, not such a charming kind of person{w=[wt2]}, but{w=[wt2]}, like{w=[wt2]}, not bad, right?{w=[wt2]} If you weren't{w=[wt2]}, like{w=[wt2]}, totally a loser{w=[wt2]}, maybe you could even date someone like this, I guess."

            "Don't choose":
                jump initiative_wgal_return

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:
        wgal "Well{w=[wt2]}, so{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Nah{w=[wt2]}, nevermind."
        jump wgal_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("wgal", "inti", 0.20)
    jump wgal_interact_check

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wgal_return:

    call hero_n_answer from _call_hero_n_answer_4

    wgal "Yeah{w=[wt2]}, of course.{w=[wt3]} What else could I expect?"
    jump wgal_interact
