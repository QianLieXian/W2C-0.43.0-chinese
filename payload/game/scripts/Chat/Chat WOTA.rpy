# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wota_show:

    if wota_love < 25:
        $ wota_mood = "O1"
    elif wota_love >= 0:
        $ wota_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_9

    show WOTA at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wota_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewota][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wota")))))

    if Get_ActivityName("wota") in ["at class"]:
        jump show_ui

    else:
        return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wota_interact_end:
    if "interacting_hero" in wota_know:
        $ wota_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wota_interact_start:
    call hide_ui from _call_hide_ui_66
    call wota_show_activity from _call_wota_show_activity
    $ wota_inti = min(char_inti_cap, wota_inti)
    call hide_ui from _call_hide_ui_67
    call wota_show from _call_wota_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wota_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if hero_map == wota_map:
        pass

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wota_interact_check:
    # Save current outfit before any updates
    $ wota_wear_keep = wota_wear

    call gametime from _call_gametime_31
    call hide_ui from _call_hide_ui_68

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wota_wear != wota_wear_keep:
        $ wota_wear = wota_wear_keep

    call wota_show from _call_wota_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    if gametimehour >= 18:
        wota "Sorry{w=[wt2]}, evil forces are suppressing my presence in this world.{w=[wt3]} It seems that I shall return to my dimension for now.{w=[wt3]} Be careful."
        $ hero_fx = 0
        jump wota_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Get_MapName("wota", "at class"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "wota"):
            $ wota_mood = "O1"
            wota "The sacred hour approaches!{w=[wt3]} I must return to my designated chamber{w=[wt2]}, lest the dark forces notice my absence!"

            $ hero_mood = "O1"
            hero "You mean class?"
            
            $ wota_mood = "A4"
            wota "Silence{w=[wt2]}, mortal!{w=[wt3]} You dare question my rituals?{nw}"

            show WOTA at RC
            show WOTA at OR_slow
            wota "Silence{w=[wt2]}, mortal!{w=[wt3]} You dare question my rituals?{fast}{w=[wt2]} {bt}Mu Hu Hu Hu...{/bt}"

            jump wota_interact_end

        else:
            $ wota_mood = "O1"
            wota "Tch{w=[wt2]}, the academic prison calls.{w=[wt3]} My powers must be contained within those walls once more."

            menu:
                "Go together":
                    $ hero_mood = "A2"
                    hero "I'll walk with you."
                    
                    $ wota_mood = "A1"
                    wota "Baka...!{w=[wt3]} You wish to accompany the wielder of forbidden knowledge?{w=[wt3]} Very well{w=[wt2]}, but stay close.{w=[wt2]} My cursed aura may attract unwanted attention!"
                    
                    $ hero_mood = "A2"
                    hero "...Sure."
                    
                    scene bg_0
                    with dissolve

                    $ hero_map = wota_map
                    call gametime from _call_gametime_32
                    call check_playermap from _call_check_playermap_18
                    call hide_ui from _call_hide_ui_69
                    show WOTA at RC
                    show HERO at LC
                    with dissolve
                    
                    $ wota_mood = "A1"
                    wota "Now{w=[wt2]}, begone!{w=[wt3]} Before my classmates witness us together and suspect our forbidden alliance!{w=[wt2]} {bt}Mu Hu Hu Hu...{/bt}"

                    jump wota_interact_end
                    
                "Let her go":
                    pass

            $ hero_mood = "A1"
            hero "Need to do something first.{w=[wt2]} See you!"
            
            $ wota_mood = "A1"
            wota "{bt}Hmph...{/bt}{w=[wt2]} So you're planning something.{w=[wt3]}{nw}"

            $ wota_mood = "O1"
            show WOTA at RC
            show WOTA at OR_slow
            wota "{bt}Hmph...{/bt}{w=[wt2]} So you're planning something.{w=[wt3]}{fast} I knew it."

        jump wota_interact_end

    # ----------------------------------------------------------------------------------------------------
    # WOTA is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wota") in ["eating"]:
        "{nm}[fnamewota]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamewota]{/nm} is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wota") from _call_circletable_7

                while Get_ActivityName("wota") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_10
                call gametime from _call_gametime_33
                
                jump wota_interact_start

            "Return":
                jump wota_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wota_know:
        $ a_event_0 = renpy.random.random()

        if renpy.random.random() < (0.2 + (wota_love * 0.003)):
            jump initiative_wota

        elif wota_love < 0:
            $ wota_mood = "O1"
            if a_event_0 < 1/4:
                wota "Anything else?{w=[wt2]} You're messing up my plans."
            elif a_event_0 < 2/4:
                wota "So{w=[wt2]}, I'm on an important mission now.{w=[wt3]} If you have nothing else to say{w=[wt1]}, I have to go."
            elif a_event_0 < 3/4:
                wota "Well{w=[wt2]}, I don't have time for social interactions.{w=[wt3]} If you don't have anything important to say, I need to get back to my job."
            else:
                wota "Look{w=[wt2]}, why don't you interact with other humans?{w=[wt2]} I'm k{w=[wt1]}-kinda busy right now."

        elif wota_love < 50:
            $ wota_mood = "O1"
            if a_event_0 < 1/4:
                wota "Anyway{w=[wt2]}, you better be improving in your hero quest."
            elif a_event_0 < 2/4:
                wota "But that's not important{w=[wt2]}, what is important is that the Demon King is about to ressurrect and we shall be prepared."
            elif a_event_0 < 3/4:
                wota "By the way{w=[wt2]}, I think it would be better if you bring men to your harem instead of girls."
                $ add_stat("wota", "lust", 1)
            else:
                wota "By the way{w=[wt2]}, come to think of it{w=[wt2]}, boys love is something completely manly.{w=[wt3]} There is nothing more manly than a sword fight!{w=[wt2]} W{w=[wt1]}-well{w=[wt2]}, you know{w=[wt2]}, just think about it."
                $ add_stat("wota", "lust", 1)

        else:
            $ wota_mood = "O1"
            if a_event_0 < 1/4:
                wota "Hey{w=[wt2]}, stop looking at me like this{w=[wt1]}, {aw}baka...{/aw}"
            elif a_event_0 < 2/4:
                wota "Anyway{w=[wt2]}, S{w=[wt1]}-stop thinking lewd things about me!{w=[wt2]} {aw}Baka!!{/aw}"
            elif a_event_0 < 3/4:
                wota "Look{w=[wt2]}, I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Damn{w=[wt2]}, I never thought I'd say that{w=[wt2]}, but{w=[wt2]}, maybe I wouldn't really feel like shipping you with another boy anymore.{w=[wt3]} Even if it would still be super interesting and hot."
            else:
                wota "By the way{w=[wt2]}, I'm watching you!{w=[wt3]} You better not be planning on bringing me to your harem."
            $ add_stat("wota", "lust", 1)

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_0 = renpy.random.random()

        if wota_lust < 25: # wota is not horny
            if wota_love < 0: # wota doesn't really like hero
                $ wota_mood = "O1"
                if a_event_0 < 1/5:
                    wota "Hm?{w=[wt2]} Can't you see I'm in the middle of a critical incantation to ward off the Normie Plague?"
                elif a_event_0 < 2/5:
                    wota "Hmph.{w=[wt2]} Another NPC trying to initiate a dialogue tree.{w=[wt3]} How predictable."
                elif a_event_0 < 3/5:
                    wota "What?{w=[wt2]} Did you mistake me for some common side character?"
                elif a_event_0 < 4/5:
                    wota "Do you need something?"
                else:
                    wota "What?"

            elif wota_love < 30: # wota likes hero
                $ wota_mood = "A1"
                if a_event_0 < 1/5:
                    if renpy.random.random() < 1/3:
                        wota "Oh!{w=[wt2]} {nm}[fnamehero]-kun{/nm}!"
                    elif renpy.random.random() < 2/3:
                        wota "Yoo!{w=[wt2]} {nm}[fnamehero]-kun{/nm}!"
                    else:
                        wota "Hey!{w=[wt2]} {nm}[fnamehero]-kun{/nm}!"
                elif a_event_0 < 2/5:
                    if renpy.random.random() < 1/3:
                        wota "Yoo!"
                    elif renpy.random.random() < 2/3:
                        wota "Hey there!"
                    else:
                        wota "Hey!"
                elif a_event_0 < 3/5:
                    $ wota_mood = "O1"
                    wota "{aw}Shhh!{/aw}{w=[wt2]} Not so loud!{w=[wt2]} The walls have ears, you know.{w=[wt4]} And sometimes tentacles."
                elif a_event_0 < 4/5:
                    wota "Hey there!{w=[wt2]} Want to help me organize my yaoi collection?"
                else:
                    $ wota_mood = "O1"
                    wota "Eep!{w=[wt2]} D{w=[wt1]}-don't sneak up on me like that!{w=[wt3]} I almost used my ultimate defense spell on you!"

            elif wota_love < 60: # wota kinda loves hero
                $ wota_mood = "A1"
                if a_event_0 < 1/5:
                    wota "Hi{w=[wt1]}, {nm}[fnamehero]-kun{/nm}!"
                elif a_event_0 < 2/5:
                    $ wota_mood = "O1"
                    wota "I t{w=[wt1]}-thought you weren't coming.{w=[wt2]} What took you so long to get here?{w=[wt2]} {aw}Baka!!!{/aw}"
                elif a_event_0 < 3/5:
                    wota "Hey{w=[wt2]}, I was just thinking about yo{w=[wt1]}{nw}"
                    $ wota_mood = "O1"
                    wota "Hey, I was just thinking about yo{fast}- I mean{w=[wt2]}, about y{w=[wt1]}-your next mission!"
                elif a_event_0 < 4/5:
                    wota "The stars have aligned!{w=[wt3]} Your arrival was foretold in the ancient manga prophecies!"
                else:
                    wota "Hello, {nm}[fnamehero]-kun{/nm}!{w=[wt2]} I was just reading this totally normal manga.{w=[wt3]} Not BL at all!{w=[wt2]} Nope!"

            else: # wota loves hero
                $ wota_mood = "A1"
                $ wota_fx = 1
                if a_event_0 < 1/5:
                    wota "{nm}[fnamehero]-kun{/nm}?{w=[wt3]} {aw}I{w=[wt1]}-I think I have some t{w=[wt1]}-time for you... ❤{/aw}"
                elif a_event_0 < 2/5:
                    wota "H{w=[wt1]}-hi{w=[wt1]}, {nm}[fnamehero]-kun{/nm}!"                    
                elif a_event_0 < 3/5:
                    wota "{aw}Kyaa~❤{/aw}{w=[wt2]} {nm}[fnamehero]-kun{/nm}!"
                elif a_event_0 < 4/5:
                    wota "{aw}❤ O{w=[wt1]}-oh!{/aw}{w=[wt2]} {nm}[fnamehero]-kun{/nm}!{w=[wt3]} I was just practicing a love confession scene.{w=[wt3]} F{w=[wt1]}-for a friend{w=[wt1]}, of course!{w=[wt3]} Yeah{w=[wt1]}, that's it!"
                else:
                    wota "{aw}❤ Ah{/aw}{w=[wt1]}, {nm}[fnamehero]-kun{/nm}!{w=[wt3]} I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I had a vision of us holding hands!{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt1]}In another dimension, of course!{w=[wt2]} {aw}Baka!{/aw}"
                $ wota_fx = 0

        elif wota_lust < 50: # wota is kinda horny
            if wota_love < 0: # wota doesn't really like hero
                $ wota_mood = "O1"
                if a_event_0 < 1/5:
                    wota "I don't have time for you now.{w=[wt2]} I'm in the middle of an important{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Ritual."
                elif a_event_0 < 2/5:
                    wota "Hmph.{w=[wt2]} Your presence is making it hard to concentrate on my{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Studies."
                elif a_event_0 < 3/5:
                    wota "Ugh{w=[wt2]}, why are you here?{w=[wt2]} I'm in the middle of a very intense{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Meditation session."
                elif a_event_0 < 4/5:
                    wota "What now?{w=[wt2]} I'm trying to focus on m{w=[wt1]}-my inner energy.{w=[wt3]} Yeah{w=[wt2]}, that's it."
                else:
                    wota "Begone!{w=[wt2]} Can't you see I'm in the middle of a critical incantation to ward off the Normie Plague?"

            elif wota_love < 30: # wota likes hero
                $ wota_mood = "O1"
                if a_event_0 < 1/5:
                    $ wota_mood = "O2"
                    wota "{bt}Kyaaa ~❤{/bt}{w=[wt2]} {nm}[fnamehero]-kun{/nm}?"
                elif a_event_0 < 2/5:
                    $ wota_mood = "O2"
                    wota "{aw}Eep!{/aw}{w=[wt2]} {nm}[fnamehero]-kun{/nm}!{w=[wt3]} Don't look at me{w=[wt1]}, my magical girl outfit isn't ready yet!"
                elif a_event_0 < 3/5:
                    wota "Ah{w=[wt1]}, {nm}[fnamehero]-kun{/nm}!{w=[wt2]} I was just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} exercising.{w=[wt3]} Yeah{w=[wt2]}, that's why I'm all flushed!"
                elif a_event_0 < 4/5:
                    wota "Don't look at me like this.{w=[wt3]} I won't be part of your harem{w=[wt1]}, {aw}baka!{/aw}"
                else:
                    $ wota_mood = "O2"
                    wota "{aw}❤ D{w=[wt1]}-damn it{/aw}.{w=[wt3]} My magical senses are tingling."

        else: # wota is extremely horny
            if wota_love < 0: # wota doesn't really like hero
                $ wota_mood = "O2"
                if a_event_0 < 1/5:
                    wota "Be brief!{w=[wt2]} I need to go to the bathroom.{w=[wt4]} For an important mission, of course!"
                elif a_event_0 < 2/5:
                    wota "W{w=[wt1]}-what are you looking at!?{w=[wt2]} Of course I'm not sweating{w=[wt2]}, it's just the excess of my power that is being released!"
                elif a_event_0 < 3/5:
                    wota "Shut up!{w=[wt2]} I'm red just cos I'm carrying a powerful energy!"
                elif a_event_0 < 4/5:
                    wota "D{w=[wt1]}-don't come any closer!{w=[wt3]} My m{w=[wt1]}-mana is almost flowing out...!"
                else:
                    wota "I don't have time for you now!{w=[wt3]} I need to{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} release this excess magical energy!{w=[wt4]} Alone!"

            else: # wota likes hero
                $ wota_mood = "O2"
                if a_event_0 < 1/5:
                    wota "{bt}Kyaaa ~❤{/bt}{w=[wt2]} {nm}[fnamehero]-kun{/nm}!{w=[wt3]} Your aura is so {bt}big and hard{/bt} today{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} It's making me dizzy!~❤"
                elif a_event_0 < 2/5:
                    wota "Oh{w=[wt1]}, {nm}[fnamehero]-kun{/nm}{w=[wt2]}, maybe I need to check your pecs.{w=[wt3]} To see if you keep exercising right, of course!{w=[wt3]} It's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I{w=[wt1]}-important to your mission!"
                elif a_event_0 < 3/5:
                    wota "{aw}❤ O{w=[wt1]}-oh my{/aw}... Is it hot in here, or is t{w=[wt1]}-that your big power?"
                elif a_event_0 < 4/5:
                    $ wota_mood = "A1"
                    wota "Are you training well?{w=[wt3]} I can’t see straight{w=[wt2]}, your c{w=[wt1]}-clothes are getting in the way."
                else:
                    wota "I w{w=[wt1]}-wonder if you'd help me with a v{w=[wt1]}-very special{w=[wt2]}, uhh{w=[wt2]}, mana transfer ritual ~❤?"

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wota_interact:
    call hide_ui from _call_hide_ui_70
    if "interacting_hero" not in wota_know:
        $ wota_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wota_interact_chat
        "Touch" if not is_specialevent:
            jump wota_interact_touch
        "Hang out":
            jump wota_interact_hangout
        "Give item" if not is_specialevent:
            jump wota_interact_gift
        "Return":
            jump wota_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wota_interact_gift:
    $ a_item_8 = "wota"
    $ a_item_9 = 0
    $ a_item_6 = "wota_interact"
    call UI_give_Item from _call_UI_give_Item_10

label wota_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wota_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wota_interact_touch:
    menu:
        "Hug":
            label wota_interact_touch_hug:
                pass

            if not "Hug_Enough" in wota_know:
                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.33:
                    scene bg_2 pink
                elif a_event_0 <= 0.66:
                    scene bg_2 yellow
                else:
                    scene bg_2 flowers

                $ wota_know.append("Hug")
                $ a_event_0 = sum(1 for get_id in wota_know if get_id =="Hug")
                $ wota_fx = 1

                if perk_cha_sex >= 1:
                    $ add_stat("wota", "lust", 2)

                if (wota_inti >= char_inti_cap/2) and (wota_love >= 50) and a_event_0 < 2:

                    show action_wota_hug 1
                    with dissolve

                    show action_wota_hug 2

                    $ add_stat("wota", "love", 2/a_event_0)
                    $ add_stat("hero", "cha_sex", (2/a_event_0)/2)

                    $ a_event_0 = renpy.random.random()
                    if a_event_0 <= 0.25:
                        wota "Damn...{w=[wt3]} I f{w=[wt1]}-feel like I'm giving in to your control.{w=[wt3]} You bastard{w=[wt2]}, what kind of power do you have!?"
                    elif a_event_0 <= 0.50:
                        wota "All right.{w=[wt3]} M{w=[wt1]}-maybe a hero needs a little support on his journey."
                    elif a_event_0 <= 0.75:
                        wota "Pervert."
                    else:
                        wota "Baka."

                else:

                    show action_wota_hug 1
                    with dissolve

                    show action_wota_hug 2

                    $ wota_know.append("Hug_Enough")
                    $ add_stat("wota", "love", 1/a_event_0)
                    $ add_stat("hero", "cha_sex", (1/a_event_0)/2)

                    $ a_event_0 = renpy.random.random()
                    if a_event_0 <= 0.25:
                        wota "{aw}Ehhh!?{/aw}{w=[wt4]} Hunf...!{w=[wt3]} Know that I know what you want okay?{w=[wt2]} Don't go thinking that I will be part of your harem."
                    elif a_event_0 <= 0.50:
                        wota "{aw}Ehhh!?{/aw}{w=[wt4]} D{w=[wt1]}-Damn{w=[wt2]}, I can barely see your moves.{w=[wt3]} You really are a threat to good girls."
                    elif a_event_0 <= 0.75:
                        wota "{aw}Ehhh!?{/aw}{w=[wt4]} H{w=[wt1]}-how...!?{w=[wt2]} I just let my guard down for only half a hundredth of seconds, and you could see through it!{w=[wt2]} Damn it!{w=[wt2]} I seem to have underestimated you."
                    else:
                        wota "{aw}Ehhh!?{/aw}{w=[wt4]} {bt}AHEM!{/bt}{w=[wt4]} Of course I can predict your every move.{w=[wt2]} I just allowed you to do it.{w=[wt3]} Which doesn't mean I'm in agreement with anything else you think of doing beyond that!"

                show action_wota_hug 1
                "{nw}"

                call gamecheck from _call_gamecheck_14
                call hide_ui from _call_hide_ui_71
                call wota_show from _call_wota_show_2

                $ gametimemin += 10
                $ add_stat("wota", "inti", 0.1)

            else:
                show HERO at CC_average
                pause(0.4)
                $ X_pos = 1500
                $ X_spd = 0.35
                show WOTA at X_X

                $ wota_mood = "O1"
                wota "{aw}AHA!!!{/aw}{w=[wt1]}{nw}"

                $ hero_mood = "O1"
                show HERO at Stay

                wota "{aw}AHA!!!{/aw}{fast}{w=[wt4]}{nw}"

                $ wota_mood = "A1"
                show HERO at LC_slow
                show WOTA at RC_heavy

                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.33:
                    wota "{aw}AHA!!!{/aw}{fast} You didn't think I'd predict your threatening moves, did you?{w=[wt2]} You thought wrong.{w=[wt3]} I can feel your pervert instincts emanating from your soul."
                elif a_event_0 <= 0.66:
                    wota "{aw}AHA!!!{/aw}{fast} A mere mortal like you will need much more than that to catch me in such an inferior technique.{w=[wt3]} I didn't even have to use 1%% of my power."
                else:
                    wota "{aw}AHA!!!{/aw}{fast} You're gonna need a lot more than that to catch me.{w=[wt2]} Maybe two hundred years from now."

                jump wota_interact

        "Return":
            jump wota_interact

    jump wota_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wota_interact_hangout:
    menu:
        "Return":
            jump wota_interact

    $ gametimemin += 30
    jump wota_interact_check

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
label wota_interact_chat:
    menu:
        "Ask how she is" if not "Talk_How" in wota_know:
            $ hero_mood = "A1"
            $ wota_mood = "O1"

            # ----------------------------------------------------------------------------------------------------
            # No Special Event
            # ----------------------------------------------------------------------------------------------------
            # else:
            hero "How are you doing?"

            $ wota_mood = "O1"
            wota "My condition is not important.{w=[wt2]} So{w=[wt1]}, don't worry about me{w=[wt2]}, just focus on your mission."

            $ hero_mood = "A2"
            hero "{aw}Ehhh?{/aw}{w=[wt3]} So{w=[wt1]}, what's my mission?"
            wota "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Uhh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"

            $ a_event_0 = renpy.random.random()
            $ wota_mood = "A1"

            if a_event_0 <= 0.33:
                $ add_stat("wota", "lust", 1)
                wota "W-well... Uhh...{fast} You need to propose to {nm}[fnamehriv]{/nm} and impregnate him!!!"

                $ hero_mood = "O1"
                hero "{aw}What!?{/aw}"

                $ wota_mood = "O1"
                wota "Hunf!{w=[wt2]} Don't be so stingy!{w=[wt2]} It's for the world's good."

                $ hero_mood = "A1"
                hero "Sorry world.{w=[wt2]} Abandon mission."

                $ wota_mood = "O2"
                wota "{bt}Ehhh...!?{/bt}"

            elif a_event_0 <= 0.66:
                wota "W-well... Uhh...{fast} You have to prevent the demon king from awakening."

                $ hero_mood = "A2"
                hero "How do I do that?"
                wota "Maybe you can hide his alarm clock."

                $ hero_mood = "A1"
                hero "That makes sense.{w=[wt3]} I'll see what I can do."

            else:
                wota "W-well... Uhh...{fast} For now you just need to improve your stats{w=[wt1]}, I guess."

                $ hero_mood = "A1"
                hero "Well{w=[wt2]}, I think I'm kinda doing that."

            $ wota_know.append("Talk")
            $ wota_know.append("Talk_How")
            $ add_stat("wota", "love", 0.5)
            $ add_stat("hero", "cha_soc", 0.5)

        "Return":
            jump wota_interact

    $ add_stat("wota", "inti", 0.2)
    $ gametimemin += 20
    jump wota_interact_check

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_wota:
    $ wota_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wota_inti*0.02) and not any(get_id.startswith("HERO_Dated") for get_id in wota_know):

        wota "The cosmic energies compel me to ask{w=[wt2]}, have you ever{w=[wt2]}, uhh{w=[wt2]}, engaged in the ancient ritual known as d{w=[wt1]}-dating?{w=[wt3]} Of course I'm asking j{w=[wt1]}-just for the mission!"

        $ hero_fx = 1
        $ hero_mood = "O1"

        menu:
            wota "The cosmic energies compel me to ask, have you ever, uhh, engaged in the ancient ritual known as d-dating? Of course I'm asking j-just for the mission!{fast}"
            "Deny":
                $ wota_know.append("HERO_Dated_N")
                $ msg.msg(renpy.translate_string("{nm}[fnamewota]{/nm} knows you a little more"))
                $ add_stat("wota", "inti", 0.5)

                hero "N{w=[wt1]}-No{w=[wt2]}, I've never dated before."

                $ wota_fx = 1
                $ wota_mood = "A4"

                wota "{lg}Mu hu hu hu...{/lg}{w=[wt2]} As expected of a chosen one!{w=[wt3]} Your power must have been sealed to protect the world from its immense strength!{w=[wt3]} {size=-5}Though I wonder what your romance stats are like...{/size}"
                hero "What was that?"

                $ wota_fx = 2
                wota "N{w=[wt1]}-nothing!{w=[wt2]} I was just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Calculating the probability of a romantic subplot in your future!"

            "Confirm":
                $ wota_know.append("HERO_Dated_Y")
                $ msg.msg(renpy.translate_string("{nm}[fnamewota]{/nm} knows you a little more"))
                $ add_stat("wota", "inti", 0.5)

                hero "W{w=[wt1]}-well{w=[wt2]}, y{w=[wt1]}-yes{w=[wt2]}, I kinda dated a girl once."

                $ wota_fx = 1
                $ wota_mood = "O1"
                wota "{aw}Ehhh!?!?{/aw}{w=[wt3]} {size=-5}For a moment I thought I could trust you.{w=[wt2]} Damn Normie!{/size}"
                hero "Ehh?{w=[wt3]} Sorry?"

                $ wota_mood = "A1"
                wota "N{w=[wt1]}-nothing at all!{w=[wt2]} Just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} contemplating this chapter in your dating sim adventure!"

            "Don't choose":
                jump initiative_wota_return

        jump wota_interact_check

    # ----------------------------------------------------------------------------------------------------
    # Ask HERO's girl preference
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wota_inti*0.02) and sum(1 for get_id in wota_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wota_know if get_id.startswith("HERO_N_Girl")) < 4:
        wota "So{w=[wt2]}, In a hypothetical situation{w=[wt1]}, where you{w=[wt2]}, let's say{w=[wt2]}, might have to choose a partner to{w=[wt2]}, uhh{w=[wt2]}, have a r{w=[wt1]}-romantic relationship with{w=[wt3]}, well{w=[wt2]}, w{w=[wt1]}-what kind of person would you hope her to be?{nw}"

        menu:
            wota "So, In a hypothetical situation, where you, let's say, might have to choose a partner to, uhh, have a r-romantic relationship with, well, w-what kind of person would you hope her to be?{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in wota_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in wota_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in wota_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in wota_know if "Personality_" in get_id)

                # Appearance Likes(Y)/Dislikes(N)
                $ a_event_1 = wota_know
                $ a_event_3 = "initiative_wota_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_9

                # Store the answer if one was given
                if _return:
                    $ wota_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg(renpy.translate_string("{nm}[fnamewota]{/nm} knows you a little more"))
                $ add_stat("wota", "inti", 0.5)

                if _return in ["Personality_9", "Personality_6", "Breast_1", "Breast_2", "HairSize_4", "HairSize_5"]: # Match - intelligent, shy, small/medium breasts, medium-long hair (anime-like)
                    $ add_stat("wota", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ wota_mood = "A3"
                    wota "{aw}Ehhh!?{/aw}{w=[wt2]} D{w=[wt1]}-don't get any ideas baka!{w=[wt3]} I m{w=[wt1]}-mean{w=[wt2]}, {aw}AHEM!{/aw}{w=[wt3]} {lg}Mu hu hu hu...{/lg}{w=[wt2]} Your taste aligns with the prophecy!"

                elif _return in ["Personality_5", "Personality_10", "Breast_4", "Breast_5", "HairSize_0", "HairSize_1"]: # Opposite match - outgoing (normie), stupid, huge breasts, bald/short hair
                    $ add_stat("wota", "bonus", -10)
                    $ wota_mood = "O1"
                    wota "Hmpf!{w=[wt2]} Your taste is clearly corrupted by normie influences."

                else: # Others
                    $ wota_mood = "A1"
                    wota "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} P{w=[wt1]}-perhaps there's hope for you in this realm after all."

            "Don't choose":
                jump initiative_wota_return

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:        
        $ a_event_0 = renpy.random.random()
        if renpy.random.random() < ((wota_lust*0.7)+(perk_cha_sex*0.3/3)):
            wota "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."
            $ msg.msg(renpy.translate_string("{nm}[fnamewota]{/nm} doesn't know what to say. This made her think of something perverted."))
            $ add_stat("wota", "lust", 1)
        elif a_event_0 < 1/3:
            wota "You know{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Nevermind.{w=[wt2]} I was about to tell you a universal secret.{w=[wt2]} But you don't have enough power to face such reality."
        elif a_event_0 < 2/3:
            wota "Hunf!{w=[wt2]} I was going to tell you something extremely important.{w=[wt2]} But you interrupted me and I forgot.{w=[wt2]} See?{w=[wt2]} It's all your fault{w=[wt2]}, baka!"
        else:
            wota "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} What was I going to say again?{w=[wt3]} I think some evil enemy must be erasing my memories."
        jump wota_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("wota", "inti", 0.20)
    jump wota_interact_check


# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wota_return:

    call hero_n_answer from _call_hero_n_answer_7

    $ wota_mood = "O1"
    $ a_event_0 = renpy.random.random()

    if a_event_0 < 1/3:
        wota "Your indecision only proves that your character sheet is incomplete."
    elif a_event_0 < 2/3:
        wota "Baka!{w=[wt2]} How do you expect to face the elder gods with such uncertainty?"
    else:
        wota "Hunf!{w=[wt2]} Then there’s nothing to do about it, right?{w=[wt3]} Perhaps you need to embark on a quest to discover your true self before you can answer such profound questions!"

    jump wota_interact
