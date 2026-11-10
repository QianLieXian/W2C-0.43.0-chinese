# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wcou_show:

    if wcou_love <= -20:
        $ wcou_mood = "O2"
    elif wcou_love < 0:
        $ wcou_mood = "A2"
    elif wcou_love >= 0:
        $ wcou_mood = "A1"
    $ hero_mood = "A1"

    if wcou_wear == "under":
        $ hero_fx = 2
    elif hero_fx == 2:
        $ hero_fx = 1
    elif hero_fx == 1:
        $ hero_fx = 0

    show WCOU at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wcou_interact_end:
    if "interacting_hero" in wcou_know:
        $ wcou_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    if "About_INTI" in wcou_know:
        $ wcou_know.remove("About_INTI")
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wcou_interact_start:
    $ wcou_inti = min(char_inti_cap, wcou_inti)
    call hide_ui from _call_hide_ui_12
    call wcou_show from _call_wcou_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
# None Yet

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wcou_interact_check:
    # Save current outfit before any updates
    $ wcou_wear_keep = wcou_wear

    call gametime from _call_gametime_6
    call hide_ui from _call_hide_ui_13

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wcou_wear != wcou_wear_keep:
        $ wcou_wear = wcou_wear_keep

    call wcou_show from _call_wcou_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    if gametimehour >= 20 and hero_map == "Office Building - Doctor's Office" and hero_quest_3 >= 3:
        wcou "That's enough for today, handsome.{w=[wt3]} Time to head home.{w=[wt2]} Come on{w=[wt2]}, I'll give you a ride.{w=[wt2]} Wouldn't want my favorite boy walking alone when I can personally escort you."

        menu:
            "Accept":
                hero "Thanks, [C_Nam][fnamewcou][C_Off].{w=[wt2]} That'd be great."
                wcou "Perfect!{w=[wt2]}{nw}"
                show WCOU at OL_heavy
                wcou "Perfect!{w=[wt2]}{fast} Let's go, tiger.{w=[wt3]} I've got the car waiting outside."
                show HERO at OL_heavy
                jump wcou_quest_1
                
            "Refuse":
                hero "Thanks, [C_Nam][fnamewcou][C_Off].{w=[wt2]} But you don't need to worry.{w=[wt2]} I'll just walk home."
                wcou "Really, dear?{w=[wt2]} That's okay then.{w=[wt2]} You know when and where to find me when you need."
                jump wcou_interact_end

    elif gametimehour >= 21 or not hero_map == wcou_map:
        wcou "It's time to go, babe.{w=[wt2]} You know when and where to find me when you need."

        jump wcou_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wcou_know:
        $ a_event_0 = renpy.random.random()
        wcou "I'm here for you."

        jump wcou_interact

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        if hero_quest_3 == 2:
            stop BGM fadeout 5
            wcou "{bt}Welcum babe ❤{/bt}{w=[wt2]} I'm glad you came!{w=[wt2]} I have good news and bad news about your exam results.{w=[wt3]} Which do you want to hear first?"

            $ hero_mood = "O1"
            $ a_event_0 = round((money*99999999)+1000000000, 2)
            mind "(Good and bad news?{w=[wt2]} This is making me apprehensive.){nw}"
            menu:
                mind "(Good and bad news?{w=[wt2]} This is making me apprehensive.){fast}"
                "Start with good news":
                    hero "T{w=[wt1]}-the good news{w=[wt2]}, I guess."
                    wcou "The good news is that there is a treatment for your condition!{w=[wt3]} So there's a way to reverse this!!"
                    hero "{pa}EHHH!?!?{/pa}{w=[wt3]} {aw}W{w=[wt1]}-Wait!{w=[wt2]} That was the good news?{w=[wt2]} And what's the bad one!?{/aw}"
                    wcou "Well{w=[wt2]}, currently{w=[wt1]}, treatment is extremely expensive.{w=[wt3]} I'd say it's around {color=#A2FF64}$[a_event_0]{/color}."

                "Start with bad news":
                    hero "T{w=[wt1]}-the bad news{w=[wt2]}, I guess."
                    wcou "The bad news is that you have a special condition{w=[wt2]}, and the treatment for that is extremely expensive.{w=[wt3]} I'd say it's around {color=#A2FF64}$[a_event_0]{/color}."
                    hero "{pa}EHHH!?!?{/pa}{w=[wt4]} {aw}O{w=[wt1]}-Okay.{w=[wt3]} That was just the bad news, right?{w=[wt3]}{pr}There's still a good one, right?{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt3]}R{w=[wt1]}-right?{/aw}"
                    wcou "{bt}Right! ❤{/bt}"
                    $ hero_mood = "A2"
                    hero "So{w=[wt1]}, what's the good one?"
                    wcou "The good one is that even though this is expensive{w=[wt1]}, it still exists!"

            hero "{w=[wt2]}.{w=[wt2]}.{w=[wt2]}.{w=[wt4]}{nw}"
            play BGM "audio/W2C - Fun.mp3"
            hero "...{fast} {pa}EEEEEHHHHHHHHHHHHHHH!?!?!?{/pa}{w=[wt4]}{pr}{aw}Is it really possible to afford something like this!?{w=[wt4]}{pr} W{w=[wt1]}-wait!{w=[wt2]} You gave me both news and didn't even tell me what I had!!!{/aw}"

            stop BGM fadeout 3
            wcou "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Oh!{w=[wt2]} You're right!{w=[wt2]}{nw}"

            play BGM "audio/W2C - MainTheme (EPIC).mp3" fadein 3
            wcou "... Oh! You're right!{fast} Let me explain.{w=[wt3]} You have a rare genetic variation that creates extremely effective antibodies against any external bodies{w=[wt3]}, such as viruses{w=[wt1]}, bacteria{w=[wt1]}, and fungi.{w=[wt3]} Therefore{w=[wt1]}, it is practically impossible for you to acquire any type of disease.{w=[wt2]} If you have never been sick{w=[wt1]}, so now you know why."
            wcou "On the other hand{w=[wt1]}, these same antibodies sterilize you{w=[wt2]}, as they prevent your reproductive system from producing sperm.{w=[wt2]} This means that you cannot get any girl pregnant after sexual intercourse.{w=[wt3]} However{w=[wt1]}, you can ejaculate and feel arousal normally.{w=[wt2]} Nothing changes in this regard."
            wcou "You can just have sex as much as you want without running the risk of impregnate anyone or getting any diseases!{w=[wt4]} So{w=[wt1]}, that's it!"
            hero "..."
            wcou "Oh{w=[wt2]}, sorry babe!{w=[wt3]} I should have used more informal terms.{w=[wt2]} It's just a bad habit of mine.{w=[wt3]} In short.{w=[wt3]} You're like a sex machine!{w=[wt1]} You can go cuming in every vagina you can!{pr}{gg}Tee-hee... ❤{/gg}"
            hero "{aw}T{w=[wt1]}-that wasn't the case!{/aw}{w=[wt2]} I just don't really know what to feel."
            wcou "Well{w=[wt1]}, I'm here for you, you know?{w=[wt2]} We can keep doing spermograms to see how your situation is going.{w=[wt3]} But this is a matter for another time.{w=[wt1]}{nw}"

            show WCOU at CC_slow
            wcou "Well{w=[wt1]}, I'm here for you, you know?{w=[wt2]} We can keep doing spermograms to see how your situation is going.{w=[wt3]} But this is a matter for another time.{fast}{w=[wt3]} Here.{w=[wt2]}{nw}"

            play SE1 "JingleRight.ogg"
            $ msg.msg(renpy.translate_string("Main Quest Completed"))
            show WCOU at RC_slow
            wcou "Well, I'm here for you, you know? We can keep doing spermograms to see how your situation is going. But this is a matter for another time. Here.{fast}{w=[wt2]} This is your medical report.{w=[wt3]} That's it for today babe! ❤"

            $ hero_quest_3 = 3

            hide screen fx_afternoon
            hide screen fx_night
            hide screen fx_morning
            show splashscreen3 with Fade(0.5,0,3)
            pause

            hide splashscreen3 with fade

        else:
            $ a_event_0 = renpy.random.random()
            wcou "So{w=[wt1]}, how can I help you, {bt}hmmm...?{/bt}"

        jump wcou_interact

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wcou_interact:
    if "interacting_hero" not in wcou_know:
        $ wcou_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wcou_interact_chat
        "Touch" if not is_specialevent:
            jump wcou_interact_touch
        "Hang out" if hero_quest_3 >= 3:
            jump wcou_interact_hangout
        #"Give item" if not is_specialevent:
            #jump wcou_interact_gift
        "Return":
            jump wcou_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wcou_interact_gift:
    $ a_item_8 = "wcou"
    $ a_item_9 = 0
    $ a_item_6 = "wcou_interact"
    call UI_give_Item from _call_UI_give_Item_2

label wcou_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wcou_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wcou_interact_touch:
    menu:
        "Hug" if is_specialevent == False:
            if "Hug" in wcou_know:
                wcou "Enough for now, babe."
                jump wcou_interact

            else:
                label wcou_interact_touch_hug:
                    pass

                call hide_ui from _call_hide_ui_14
                hide screen fx_night
                hide screen fx_afternoon
                hide screen fx_morning

                $ a_event_0 = renpy.random.random()

                if a_event_0 > 0.66:
                    scene bg_2 pink
                elif a_event_0 > 0.33:
                    scene bg_2 yellow
                else:
                    scene bg_2 flowers
                show bg_fx0
                show action_wcou_hug_body
                show action_wcou_hug_outfithero common1
                show action_wcou_hug_outfitwcou party
                show action_wcou_hug_hand
                with dissolve

                $ wcou_know.append("Hug")

                $ add_stat("wcou", "love", 1)
                $ add_stat("hero", "cha_sex", 1)

                pause

                call gamecheck from _call_gamecheck_2
                call hide_ui from _call_hide_ui_15
                call wcou_show from _call_wcou_show_2

            $ gametimemin += 10
            $ add_stat("wcou", "inti", 0.1)

            jump wcou_interact_check

        "Return":
            jump wcou_interact

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wcou_interact_hangout:
    menu:
        "Do a spermogram" if not "Spermogram" in wcou_know:
            $ a_event_1 = 2
            hero "W{w=[wt1]}-well{w=[wt2]}, I'd like to do another spermogram."
            wcou "{bt}Is that so? ❤{/bt}{w=[wt3]} So let's do it!{w=[wt3]} I need to collect your semen to do some scientific experiments."

            $ hero_mood = "O1"
            hero "{aw}Ehhh...!?{/aw}"
            wcou "{aw}Hurry up!!{/aw}{w=[wt2]} Remove your clothes and lie on the stretcher.{w=[wt3]} I'm going to take a bottle."
            jump wcou_office2_spermogram

        "Return":
            jump wcou_interact

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
label wcou_interact_chat:
    menu:
        "Ask about your exam":
            if hero_quest_3 >= 3:
                hero "Can you explain to me again about the results of my exam?"
                wcou "Sure.{w=[wt2]} You have a rare genetic variation that creates extremely effective antibodies.{w=[wt3]} What makes you practically immune to any type of disease{w=[wt2]}, but also prevent your reproductive system from producing sperm.{w=[wt2]} That said{w=[wt2]}, you can bathe girls with your cum without the risk of becoming daddy."
                #wcou "The equipment needed to treat this specific condition is still very expensive, but it may be possible to reverse this with the advancement of technology in the future. For now, I recommend that you enjoy it a lot!"
            else:
                hero "When will my exam results be ready?"
                wcou "Don't think too much about it babe{w=[wt1]}, I already told you that I'll warn you when it's ready.{w=[wt2]} So{w=[wt1]}, remember:{w=[wt2]} {b}No need to worry about when next updates will come.{w=[wt2]} Cos updates aways comes at the right time.{/b}"

        "Ask how to get money":
            hero "Would you know of somewhere I can work?{w=[wt2]} How can I get money?"
            wcou "For now{w=[wt1]}, I think a good option for you would be to improve your attributes.{w=[wt3]} I know that your school rewards students with the best performance for helping those with the worst.{w=[wt3]} Why don't you look for the [C_Dat]Student Council[C_Off]? Maybe students with [C_Dat]tutoring[C_Off] skill can be paid to give tutoring classes."
            wcou "Maybe you can even teach someone to swim if you have [C_Dat]swimming[C_Off] skill.{w=[wt3]} Also remember that's always good to improve your [C_Dat]performance[C_Off] and your [C_Dat]knowledge[C_Off] as well{w=[wt1]}, so you can get even better results in your activities."

        "Ask how to get sex" if hero_quest_3 >= 3:
            $ hero_fx = 1
            $ hero_mood = "A1"
            hero "How can I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Y{w=[wt1]}-you know{w=[wt2]}, practice if my non-babies cum works?"
            wcou "I bet there already are some cool babes on your school dying to help you in that.{w=[wt2]} Maybe they just don't know you well.{w=[wt3]} Why don't you take a dip in your swim trunks in the pool at your school at a time when there aren't many people around?{w=[wt2]} About 18pm I'd say!"

            $ hero_mood = "O1"
            hero "D{w=[wt1]}-do you think it will work?"
            wcou "Of course!{w=[wt3]} And you better have a good [C_Dat]Sensuality[C_Off] skill for when you do it so you not make a fool of yourself when the time comes."

        "Ask for help with someone":
            if not "About_INTI" in wcou_know:
                hero "I think I need help with someone."
                wcou "Sure!{w=[wt2]} Problems dealing with people?{w=[wt2]} Trying to get into some girl panties?"
            $ a_event_0 = 0
            label wcou_interact_chat_inti:
                pass
            if a_event_0 == 0:
                menu:
                    "{image=icon_wcou} {nm}[fnamewcou] [lnamerela]{/nm}":
                        if not "About_INTI" in wcou_know:
                            $ hero_mood = "O2"
                            $ hero_fx = 1
                            hero "{aw}I{w=[wt1]}-It's you!{/aw}"
                            $ hero_mood = "O1"
                            wcou "What do you mean babe?{w=[wt2]} I'm already yours, you know?"
                        menu:
                            "Relationship" if not "About_INTI_WCOU" in wcou_know:
                                $ hero_mood = "A2"
                                hero "How can I grow relationship with you?"
                                wcou "{bt}Hmmm...?{/bt}{w=[wt2]} Do you want us to be even closer?{w=[wt3]} {bt}How lovely...! ❤{/bt}{w=[wt4]} Well{w=[wt1]}, that's super simple babe!{w=[wt2]} If you keep telling me everything about you, and doing what I tell you to do, maybe I'll make a room in my schedule so we can do more things together."
                                $ wcou_bonus += 20
                                $ msg.msg(renpy.translate_string("[C_Pos]+ 20% bonus[C_Off] for next interations with {nm}[fnamewcou]{/nm}"))
                                $ wcou_know.append("About_INTI_WCOU")

                            "Hug":
                                if not "Hug" in wcou_know:
                                    jump wcou_interact_touch_hug
                                elif "Hug" in wcou_know:
                                    wcou "Enough for now, babe."
                                    jump wcou_interact_check

                            "Have Sex":
                                $ hero_mood = "O2"
                                $ hero_fx = 2
                                hero "{aw}I{w=[wt1]}-I wanna have s{w=[wt1]}-sex with you!!!{/aw}"
                                wcou "{bt}Awwn...{/bt}{w=[wt2]} So you wanna get into my panties babe?{w=[wt1]} {gg}Tee-hee...{/gg}{w=[wt3]} I love how sincere you are!{w=[wt2]} But everything has it own time.{w=[wt2]} Let's not rush things too much.{w=[wt1]} {gg}Tee-hee...{/gg}"
                                $ hero_mood = "O1"
                                hero "Okay{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."
                                if not "Hug" in wcou_know:
                                    $ wcou_mood = "A2"
                                    wcou "{bt}Ohh...! ❤{/bt}{w=[wt2]} Don't make that face!{w=[wt3]} {bt}Come here! ❤{/bt}"
                                    jump wcou_interact_touch_hug

                    "{image=icon_wsis} {nm}[fnamewsis] [lnamestep]{/nm}" if not "About_INTI_WSIS" in wcou_know:
                        hero "How can I grow relationship with {nm}[hero_about_wsis]{/nm}?"
                        if wsis_inti >= char_inti_cap:
                            wcou "Well{w=[wt1]}, I think you already have as much intimacy as possible with her, don't you?{w=[wt3]} Maybe now you just need to enjoy each other's company."
                        elif wsis_inti < 10:
                            wcou "Oh{w=[wt1]}, my lil hot cousin is someone so hard to deal with, huh?{w=[wt3]} I assure you that behind that thick shell there is a cute princess eager to receive all your love inside her{w=[wt2]}, {bt}if you know what I mean...!{/bt}{w=[wt3]} For now{w=[wt1]}, just try to be there for her whenever you can.{w=[wt2]} And respect the distance she establishes between you.{w=[wt2]} I'm sure you'll be close very soon."

                        $ wsis_bonus += 20
                        $ msg.msg(renpy.translate_string("[C_Pos]+ 20% bonus[C_Off] for next interations with {nm}[fnamewsis]{/nm}"))
                        $ wcou_know.append("About_INTI_WSIS")

                    "{image=icon_wmom} {nm}[fnamewmom] [lnamestep]{/nm}" if not "About_INTI_WMOM" in wcou_know:
                        hero "How can I grow relationship with {nm}[hero_about_wmom]{/nm}?"
                        if wmom_inti >= char_inti_cap:
                            wcou "Well{w=[wt1]}, I think you already have as much intimacy as possible with her, don't you?{w=[wt3]} Maybe now you just need to enjoy each other's company."
                        elif wmom_inti < 10:
                            wcou "Oh babe{w=[wt1]}, {nm}Auntie [fnamewmom]{/nm} is quite busy, isn't she?{w=[wt2]} I think if you wake up early you can keep her company before she goes to work.{w=[wt2]} Don't take your eyes off her on Sunday!"

                        $ wmom_bonus += 20
                        $ msg.msg(renpy.translate_string("[C_Pos]+ 20% bonus[C_Off] for next interations with {nm}[fnamewmom]{/nm}"))
                        $ wcou_know.append("About_INTI_WMOM")

                    "{image=icon_wnei} {nm}[fnamewnei] [lnamewnei]{/nm}" if not "About_INTI_WNEI" in wcou_know:
                        hero "How can I grow relationship with {nm}[fnamewnei]{/nm}?"
                        if wnei_inti >= char_inti_cap:
                            wcou "Well{w=[wt1]}, I think you already have as much intimacy as possible with her, don't you?{w=[wt3]} Maybe now you just need to enjoy each other's company."
                        elif wnei_inti < 10:
                            wcou "{bt}Awnnn...{/bt}{w=[wt2]} That cute little hot babe!{w=[wt3]} It shouldn't be too difficult, right?{w=[wt2]} {bt}She is so adorable!{/bt}{w=[wt3]} But I know her parents are overprotective{w=[wt1]}, so you may need to earn their trust in the future.{w=[wt3]} For now{w=[wt1]}, just enjoy the moments you can spend together."

                        $ wnei_bonus += 20
                        $ msg.msg(renpy.translate_string("[C_Pos]+ 20% bonus[C_Off] for next interations with {nm}[fnamewnei]{/nm}"))
                        $ wcou_know.append("About_INTI_WNEI")

                    "Other":
                        $ a_event_0 = 1
                        jump wcou_interact_chat_inti

                    "Return":
                        if not "About_INTI" in wcou_know:
                            hero "N{w=[wt1]}-nevermind."
                            wcou "Don't be shy babe!"
                        jump wcou_interact_chat

            elif a_event_0 == 1:
                menu:
                    "{image=icon_wpre} {nm}[fnamewpre] [lnamewpre]{/nm}" if not "About_INTI_WPRE" in wcou_know:
                        if "wpre" in wcou_know:
                            hero "How can I grow relationship with {nm}[fnamewpre]{/nm}?"
                        else:
                            hero "I think I want to get closer to a girl at my school."
                            wcou "That's cool babe!{w=[wt2]} Tell me everything you know about her."

                            $ hero_mood = "A2"
                            hero "Sure.{w=[wt2]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

                            show bg_0 with dissolve
                            $ wcou_know.append("wpre")
                            $ msg.msg(renpy.translate_string("{nm}[fnamewcou]{/nm} knows a little more about your acquaintances"))
                            $ add_stat("wcou", "inti", 0.5)
                            pause(1)
                            hide bg_0 with Dissolve(1)

                            hero "Sure. Well... {mind}(. . .){/mind}{fast} And that's it."
                            wcou "{bt}What a plain and admirable girl!{/bt}{w=[wt2]} She seems to be so hardworking!{w=[wt3]} I greatly admire the dedication of someone who seeks to improve their life through hard work.{w=[wt3]} I already liked her a lot babe!{w=[wt2]} I will certainly help you get her to bed!"
                            $ hero_fx = 2
                            $ hero_mood = "O1"
                            hero "{aw}Ehhh...!?{/aw}"

                        if wpre_inti >= char_inti_cap:
                            wcou "Well{w=[wt1]}, I think you already have as much intimacy as possible with her, don't you?{w=[wt3]} Maybe now you just need to enjoy each other's company."
                        elif wpre_inti < 10:
                            wcou "From what you told me{w=[wt1]}, she seems to be extremely intelligent when it comes to studies and general knowledge{w=[wt2]}, but completely innocent when it comes to social interaction, right?{w=[wt3]} {bt}Ohh{w=[wt2]}, I'd love to test that innocence!{/bt}{w=[wt2]} I think that's what you should do for now. Just keep talking to her when you find her."

                        elif wpre_inti < 20:
                            wcou "For now{w=[wt1]}, just try to be there for her when you can.{w=[wt2]} It's very likely that this girl is overworking herself{w=[wt1]}, and at some point she may break down."

                        $ wpre_bonus += 20
                        $ msg.msg(renpy.translate_string("[C_Pos]+ 20% bonus[C_Off] for next interations with {nm}[fnamewpre]{/nm}"))
                        $ wcou_know.append("About_INTI_WPRE")

                    "{image=icon_wota} {nm}[fnamewota] [lnamewota]{/nm}" if not "About_INTI_WOTA" in wcou_know:
                        if "wota" in wcou_know:
                            hero "How can I grow relationship with {nm}[fnamewota]{/nm}?"
                        else:
                            hero "I think I want to get closer to a girl at my school."
                            wcou "That's cool babe!{w=[wt2]} Tell me everything you know about her."

                            $ hero_mood = "A2"
                            hero "Sure.{w=[wt2]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

                            show bg_0 with dissolve
                            $ wcou_know.append("wota")
                            $ msg.msg(renpy.translate_string("{nm}[fnamewcou]{/nm} knows a little more about your acquaintances"))
                            $ add_stat("wcou", "inti", 0.5)
                            pause(1)
                            hide bg_0 with Dissolve(1)

                            hero "Sure. Well... {mind}(. . .){/mind}{fast} And that's it."
                            wcou "Ohhh{w=[wt1]}, Interesting!{w=[wt2]} A girl who hides in her own fantasy world.{w=[wt3]} I would {bt}love{/bt} to talk to her!{w=[wt2]} I'd even make a special therapy session discount for her! ❤{w=[wt3]} But let's leave that for another time."

                        if wota_inti >= char_inti_cap:
                            wcou "Well{w=[wt1]}, I think you already have as much intimacy as possible with her, don't you?{w=[wt3]} Maybe now you just need to enjoy each other's company."
                        elif wota_inti < 10:
                            wcou "From what you told me{w=[wt1]}, she doesn't seem like she's difficult to deal with.{w=[wt2]} Maybe she just needs someone to talk to.{w=[wt2]} How about helping her learn to swim?"

                        $ wota_bonus += 20
                        $ msg.msg(renpy.translate_string("[C_Pos]+ 20% bonus[C_Off] for next interations with {nm}[fnamewota]{/nm}"))
                        $ wcou_know.append("About_INTI_WOTA")

                    "{image=icon_wdis} {nm}[fnamewdis] [lnamewdis]{/nm}" if not "About_INTI_WDIS" in wcou_know:
                        if "wdis" in wcou_know:
                            hero "How can I grow relationship with {nm}[fnamewdis]{/nm}?"
                        else:
                            hero "I think I want to get closer to a girl at my school."
                            wcou "That's cool babe!{w=[wt2]} Tell me everything you know about her."

                            $ hero_mood = "A2"
                            hero "Sure.{w=[wt2]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

                            show bg_0 with dissolve
                            $ wcou_know.append("wdis")
                            $ msg.msg(renpy.translate_string("{nm}[fnamewcou]{/nm} knows a little more about your acquaintances"))
                            $ add_stat("wcou", "inti", 0.5)
                            pause(1)
                            $ wcou_mood = "A3"
                            hide bg_0 with Dissolve(1)

                            hero "Sure. Well... {mind}(. . .){/mind}{fast} And that's it."
                            wcou "{pa}Ehhh!?{w=[wt3]} So do you know a girl like that!?{w=[wt3]}{/pa} She's exactly the kind of person I need as my assistant!{w=[wt3]} I will definitely help you get closer to her!{w=[wt2]} Then will you help me bring her here, deal?"
                            hero "W{w=[wt1]}-well{w=[wt2]}, s{w=[wt1]}-seems fair{w=[wt2]}, I guess."

                        if wdis_inti >= char_inti_cap:
                            wcou "Well{w=[wt1]}, I think you already have as much intimacy as possible with her, don't you?{w=[wt3]} Maybe now you just need to enjoy each other's company."
                        elif wdis_inti < 10:
                            wcou "From what you told me{w=[wt1]}, it seems like she is someone who is extremely sensitive and easy to deal with.{w=[wt3]} To get closer to her{w=[wt1]}, just keep keeping in touch whenever you can for now!"

                        $ wdis_bonus += 20
                        $ msg.msg(renpy.translate_string("[C_Pos]+ 20% bonus[C_Off] for next interations with {nm}[fnamewdis]{/nm}"))
                        $ wcou_know.append("About_INTI_WDIS")

                    "{image=icon_wgal} {nm}[fnamewgal] [lnamewgal]{/nm}" if not "About_INTI_WGAL" in wcou_know:
                        if "wgal" in wcou_know:
                            hero "How can I grow relationship with {nm}[fnamewgal]{/nm}?"
                        else:
                            hero "I think I want to get closer to a girl at my school."
                            wcou "That's cool babe!{w=[wt2]} Tell me everything you know about her."

                            $ hero_mood = "A2"
                            hero "Sure.{w=[wt2]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

                            show bg_0 with dissolve
                            $ wcou_know.append("wgal")
                            $ msg.msg(renpy.translate_string("{nm}[fnamewcou]{/nm} knows a little more about your acquaintances"))
                            $ add_stat("wcou", "inti", 0.5)
                            pause(1)
                            hide bg_0 with Dissolve(1)

                            hero "Sure. Well... {mind}(. . .){/mind}{fast} And that's it."
                            wcou "Oh{w=[wt1]}, so she's a very arrogant and difficult girl to deal with, isn't she?{w=[wt3]} She probably seeks to be close to people who have high social status.{w=[wt2]} If you really want to get close to her{w=[wt1]}, you better prepare your wallet!"
                            $ hero_mood = "O1"

                        if wgal_inti >= char_inti_cap:
                            wcou "Well{w=[wt1]}, I think you already have as much intimacy as possible with her, don't you?{w=[wt3]} Maybe now you just need to enjoy each other's company."
                        elif wgal_inti < 10:
                            wcou "From what you told me{w=[wt1]}, It seems like there isn't much that can be done for now.{w=[wt3]} I suggest you continue talking to her and improving your charisma."

                        $ wgal_bonus += 20
                        $ msg.msg(renpy.translate_string("[C_Pos]+ 20% bonus[C_Off] for next interations with {nm}[fnamewgal]{/nm}"))
                        $ wcou_know.append("About_INTI_WGAL")

                    "Other":
                        $ a_event_0 = 0
                        jump wcou_interact_chat_inti

                    "Return":
                        if not "About_INTI" in wcou_know:
                            hero "N{w=[wt1]}-nevermind."
                            wcou "Don't be shy babe!"
                        jump wcou_interact_chat

            $ gametimemin += 20

        "Return":
            jump wcou_interact

    $ wcou_know.append("About_INTI")
    $ wcou_know.append("Talk")
    $ gametimemin += 10
    call gametime from _call_gametime_7
    jump wcou_interact_check

# ----------------------------------------------------------------------------------------------------
# End
# ----------------------------------------------------------------------------------------------------
jump wcou_interact_end

# ----------------------------------------------------------------------------------------------------
# Render
# ----------------------------------------------------------------------------------------------------
image action_wcou_hug_hand:
    "action_wcou_hug_hand 1"
    0.15
    "action_wcou_hug_hand 2"
    0.15
    "action_wcou_hug_hand 3"
    0.15
    "action_wcou_hug_hand 4"
    0.15
    "action_wcou_hug_hand 5"
    0.15
    "action_wcou_hug_hand 4"
    0.15
    "action_wcou_hug_hand 3"
    0.15
    "action_wcou_hug_hand 2"
    0.15
    repeat

# ----------------------------------------------------------------------------------------------------
# Spermogram
# ----------------------------------------------------------------------------------------------------
label wcou_office2_spermogram:
    stop BGM fadeout 4
    scene wcou_office_bg 6
    show wcou_office6_wcou a
    show wcou_office6_herobody
    show wcou_office6_herobagbg
    show wcou_office6_herodick 0a
    show wcou_office6_herobagfg
    with Fade(1,0,3)

    play BGM "audio/W2C - SexyVibes.mp3"

    hide wcou_office6_wcou
    hide wcou_office6_herobody
    hide wcou_office6_herobagbg
    hide wcou_office6_herodick
    hide wcou_office6_herobagfg
    show wcou_office6_wcou b
    show wcou_office6_herobody
    show wcou_office6_wcouarm b
    show wcou_office6_herobagbg
    show wcou_office6_herodick 0a
    show wcou_office6_herobagfg
    with Dissolve(1)

    wcou "So{w=[wt2]}, let's start!"
    
    $ a_event_2 = 11
    $ a_event_4 = 23
    $ a_event_6 = 1

    scene wcou_office_bg 6
    show wcou_office6_wcou c1
    with Dissolve(1)


    $ BalloonFly_Difficult = 3
    $ BalloonFly_T = 2
    show screen hero_lust_bar
    call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_2
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_3
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_4
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_5
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_6
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_7
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_8
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_9
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 0.5
    show wcou_office6_wcou c1
    $renpy.pause(1,hard=True)
    $ a_event_4 += 2
    show wcou_office6_wcou c1
    call Minigame_BalloonFly_Explode from _call_Minigame_BalloonFly_Explode

    $ a_event_2 = 12
    $ config.allow_skipping = True
    show wcou_office6_wcoufg c2
    wcou "{bt}Hmmm...{/bt}{w=[wt3]} So you won't surrender to my hand, huh?{w=[wt1]} {gg}Tee-Hee...{/gg}{w=[wt4]} I'll put a little more effort then."

    play BGM "audio/W2C - Intensity.mp3"

    $ BalloonFly_Difficult = 5
    $ BalloonFly_T = 2
    hide wcou_office6_wcoufg
    show screen hero_lust_bar
    if a_event_4 >= 35:
        show wcou_office6_wcou d1
        $ a_event_6 = 2
    else:
        show wcou_office6_wcou c1
        $ a_event_6 = 0
    with Dissolve(1)

    if a_event_4 >= 35:
        while hero_lust < 100:
            call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_10
            $renpy.pause(1,hard=True)
            $ a_event_4 += 1
            $ BalloonFly_Difficult += 0.25
            show wcou_office6_wcou d1
    else:
        while hero_lust < 100:
            call wcou_checkup2_paudurecimento from _call_wcou_checkup2_paudurecimento_11
            $renpy.pause(1,hard=True)
            $ a_event_4 += 0.5
            $ BalloonFly_Difficult += 0.25
            show wcou_office6_wcou c1

    jump wcou_checkup2_ejaculacimento

label wcou_office2_end:
    if a_event_6 == 2:
        scene bg_1
        with Dissolve(3)
        pause(1)

        $ add_stat("wcou", "lust", a_event_4)
        image wcou_office6_spermogram2 = Movie(play="images/Scene/WCOU - Office/wcou_office 6d.webm", loop=True)
        show wcou_office6_spermogram2
        if wcou_lust >= 80:
            show wcou_office 6d_cum
        with Dissolve(3)

        $ hero_lust = 0
        $ msg.msg(renpy.translate_string("{nm}You{/nm} came, and your lust reset."))
        $ add_stat("wcou", "lust", a_event_4)
        if wcou_lust >= 80:
            $ wcou_lust = 0
            $ msg.msg(renpy.translate_string("{nm}[fnamewcou]{/nm} came, and her lust reset."))
        $ add_stat("wcou", "love", a_event_4/10)
        $ add_stat("wcou", "inti", a_event_4/10)
        pause
        stop BGM fadeout 3
        scene bg_0
        with Dissolve(3)
        play BGM "audio/W2C - Satisfaction.mp3"

    elif a_event_1 <= 1:
        stop BGM fadeout 3
        scene bg_0
        with Dissolve(1)
        play BGM "audio/W2C - Satisfaction.mp3"

        if hero_lust >= 100:
            $ hero_lust = 0
            $ msg.msg(renpy.translate_string("{nm}You{/nm} came, and your lust reset."))

        $ add_stat("wcou", "love", a_event_4/10)
        $ add_stat("wcou", "inti", 2)

    else:
        stop BGM fadeout 3
        scene bg_1
        with Dissolve(3)
        play BGM "audio/W2C - Satisfaction.mp3"
        pause(1)
        show wcou_office6_spermogram1
        with Dissolve(3)

        $ hero_lust = 0
        $ msg.msg(renpy.translate_string("{nm}You{/nm} came, and your lust reset."))
        $ add_stat("wcou", "lust", a_event_4)
        if wcou_lust >= 80:
            $ wcou_lust = 0
            $ msg.msg(renpy.translate_string("{nm}[fnamewcou]{/nm} came, and her lust reset."))
        $ add_stat("wcou", "love", a_event_4/10)
        $ add_stat("wcou", "inti", a_event_4/10)
        pause
        scene bg_0
        with Dissolve(2)

    call gamecheck from _call_gamecheck_3
    call hide_ui from _call_hide_ui_16
    call wcou_show from _call_wcou_show_3
    $ gametimemin += 60
    $ add_stat("wcou", "inti", 1)
    $ wcou_know.append("Spermogram")
    jump wcou_interact_check

label wcou_checkup2_ejaculacimento:
    if a_event_2 >= 11:
        call Minigame_BalloonFly_Explode from _call_Minigame_BalloonFly_Explode_1
    hide screen hero_lust_bar
    hide screen Minigame_BalloonFly
    with Dissolve(2)
    $renpy.pause(1,hard=True)
    mind "(I can't hold anymore..!)"
    pause
    jump wcou_office2_end

label wcou_checkup2_paudurecimento:

    if a_event_2 == 11 and hero_lust >= 100:
        call Minigame_BalloonFly_Explode from _call_Minigame_BalloonFly_Explode_2
        call wcou_checkup2_ejaculacimento from _call_wcou_checkup2_ejaculacimento
    elif a_event_2 == 11 and hero_lust < 100:
        call Minigame_BalloonFly_Explode from _call_Minigame_BalloonFly_Explode_3
        call Minigame_BalloonFly from _call_Minigame_BalloonFly
    elif a_event_2 == 12 and hero_lust >= 100:
        call Minigame_BalloonFly_Explode from _call_Minigame_BalloonFly_Explode_4
        call wcou_checkup2_ejaculacimento from _call_wcou_checkup2_ejaculacimento_1
    elif a_event_2 == 12 and hero_lust < 100:
        call Minigame_BalloonFly_Explode from _call_Minigame_BalloonFly_Explode_5
        call Minigame_BalloonFly from _call_Minigame_BalloonFly_1

    return
