# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wgot_show:

    if wgot_love <= -20:
        $ wgot_mood = "O2"
    elif wgot_love < 0:
        $ wgot_mood = "A2"
    elif wgot_love >= 0:
        $ wgot_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_5

    show WGOT at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wgot_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewgot][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wgot")))))

    if Get_ActivityName("wgot") in ["at class"]:
        jump show_ui

    else:
        return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wgot_interact_end:
    if "interacting_hero" in wgot_know:
        $ wgot_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wgot_interact_start:
    call hide_ui from _call_hide_ui_36
    call wgot_show_activity from _call_wgot_show_activity
    $ wgot_inti = min(char_inti_cap, wgot_inti)
    call hide_ui from _call_hide_ui_37
    call wgot_show from _call_wgot_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wgot_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if hero_map == wgot_map:
        pass

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wgot_interact_check:
    # Save current outfit before any updates
    $ wgot_wear_keep = wgot_wear

    call gametime from _call_gametime_17
    call hide_ui from _call_hide_ui_38

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wgot_wear != wgot_wear_keep:
        $ wgot_wear = wgot_wear_keep

    call wgot_show from _call_wgot_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    if gametimehour >= 18: # Went home
        $ wgot_mood = "O1"
        wgot "I must depart now.{w=[wt3]} The shadows grow longer, and there are preparations I must attend to before the darkness consumes all.{w=[wt3]} Farewell for now."
        $ hero_fx = 0
        jump wgot_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Get_MapName("wgot", "at class"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "wgot"):
            $ wgot_mood = "O1"
            wgot "Ah{w=[wt2]}, the academic prison beckons once more.{w=[wt4]} How beautifully tragic...{w=[wt3]} Another day of shared suffering.{nw}"

            show WGOT at RC
            show WGOT at OR_slow
            wgot "Ah{w=[wt2]}, the academic prison beckons once more.{w=[wt4]} How beautifully tragic...{w=[wt3]} Another day of shared suffering.{fast} Farewell."

            jump wgot_interact_end

        else:
            $ wgot_mood = "O1"
            wgot "The darkness beckons...{w=[wt4]} Time to return to our classroom tomb.{w=[wt4]} How drearily mundane."

            if Get_MapName("wgot", "at class") == Get_MapName(None, "school", "class_1b"):
                menu:
                    "Go together":
                        $ hero_mood = "A1"
                        hero "I'm heading there too.{w=[wt2]} Let's go."
                        
                        $ wgot_mood = "A1"
                        wgot "Very well{w=[wt2]}, let us walk this melancholy path together."
                        
                        scene bg_0
                        with dissolve

                        $ hero_map = wgot_map
                        call gametime from _call_gametime_18
                        call check_playermap from _call_check_playermap_5
                        call hide_ui from _call_hide_ui_39
                        show WGOT at RC
                        show HERO at LC
                        with dissolve
                        
                        $ wgot_mood = "A1"
                        wgot "The bell tolls for us all.{w=[wt4]} Until we meet again in this theater of tedium if we're alive."

                        jump wgot_interact_end
                        
                    "Let her go":
                        pass

            $ hero_mood = "A1"
            hero "Need to do something first.{w=[wt2]} See you!"
            
            $ wgot_mood = "O1"
            
            show WGOT at RC
            show WGOT at OR_slow
            wgot "Farewell."

        jump wgot_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wgot_know:
        $ a_event_0 = renpy.random.random()

        # Brings an interactive subject
        if renpy.random.random() < (0.2 + (wgot_love * 0.003)):
            jump initiative_wgot

        # Do a random comment
        elif renpy.random.random() > (0.5 + (wgot_love * 0.002)):
            $ a_event_0 = renpy.random.random()
            if a_event_0 < 1/13:
                wgot "Wait{w=[wt2]}, I know that ghost that passed by there.{w=[wt3]} {nm}Grandma?{/nm}"
            elif a_event_0 < 2/15:
                wgot "Wait{w=[wt2]}, I know that ghost that passed by there.{w=[wt3]} {nm}Grandpa?{/nm}"
            elif a_event_0 < 3/15:
                wgot "Wait{w=[wt2]}, I know that ghost that passed by there.{w=[wt3]} {nm}Uncle?{/nm}"
            elif a_event_0 < 4/15:
                wgot "Wait{w=[wt2]}, I know that ghost that passed by there.{w=[wt3]} {nm}Auntie?{/nm}"
            elif a_event_0 < 5/15:
                wgot "Wait{w=[wt2]}, I know that ghost that passed by there.{w=[wt3]} {nm}Father?{/nm}"
            elif a_event_0 < 6/15:
                wgot "Wait{w=[wt2]}, I know that ghost that passed by there.{w=[wt2]} {nm}Mother?{/nm}"
            elif a_event_0 < 7/15:
                wgot "Do you also hear the whispers?{w=[wt3]} No?{w=[wt3]} How fortunate for you."
            elif a_event_0 < 8/15:
                wgot "I was drawing a raven earlier.{w=[wt3]} They're misunderstood creatures, don't you think?"
            elif a_event_0 < 9/15:
                wgot "The rain forecasted for tomorrow will be perfect for sitting alone with a book."
            elif a_event_0 < 10/15:
                wgot "This morning I found a dead moth by my window.{w=[wt3]} I gave it a proper burial."
            elif a_event_0 < 11/15:
                wgot "Did you notice how the clouds today resemble the faces of the departed?{w=[wt3]} No?{w=[wt3]} Just me, then."
            elif a_event_0 < 12/15:
                wgot "The world is filled with beauty and decay simultaneously."
            elif a_event_0 < 13/15:
                wgot "I watched a butterfly die this morning.{w=[wt3]} Its wings were so delicate at the end."
            elif a_event_0 < 14/15:
                wgot "The piano in the music room plays by itself sometimes.{w=[wt3]} Only I seem to notice."
            else:
                wgot "The world is both beautiful and tragic.{w=[wt3]} Much like this conversation, perhaps."

        # Do a random comment based on love stat
        else:
            $ a_event_0 = renpy.random.random()
            if wgot_love < 10:
                $ wgot_mood = "O1"
                if a_event_0 < 1/6:
                    wgot "Do you feel the chill in the air?{w=[wt2]} Maybe it's just my presence."
                elif a_event_0 < 2/6:
                    wgot "I apologize if my presence troubles you."
                elif a_event_0 < 3/6:
                    wgot "I sense you have more to say.{w=[wt3]} Speak, if you wish."
                elif a_event_0 < 4/6:
                    wgot "I'm not accustomed to conversations lasting this long."
                elif a_event_0 < 5/6:
                    wgot "Don't you feel strange?{w=[wt3]} No pain in your heart?"
                else:
                    wgot "I apologize if my presence troubles you.{w=[wt3]} You may leave whenever you wish."

            elif wgot_love < 40:
                $ wgot_mood = "O1"
                if a_event_0 < 1/5:
                    wgot "You're quite peculiar."
                elif a_event_0 < 2/5:
                    wgot "I find myself not entirely opposed to continuing our conversation."
                elif a_event_0 < 3/5:
                    wgot "I'm rarely engaged in conversation for this long."
                elif a_event_0 < 4/5:
                    wgot "I overheard someone call me 'creepy' again today.{w=[wt3]} At least you don't seem to mind."
                else:
                    wgot "Not entirely unpleasant to talk with you."

            elif wgot_love < 70:
                $ wgot_mood = "A1"
                if a_event_0 < 1/6:
                    wgot "Your company is surprisingly tolerable."
                elif a_event_0 < 2/6:
                    wgot "I find myself not wishing for this interaction to end just yet.{w=[wt3]} How unusual."
                elif a_event_0 < 3/6:
                    wgot "I rarely enjoy conversation, yet{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Here we are."
                elif a_event_0 < 4/6:
                    wgot "Perhaps... I could show you some of my sketchbook drawings later?"
                elif a_event_0 < 5/6:
                    wgot "I saw a crow following you earlier.{w=[wt3]} That's a good sign... from my perspective, at least."
                else:
                    wgot "The darkness seems less oppressive when we speak."

            else:
                $ wgot_mood = "A1"
                if a_event_0 < 1/10:
                    wgot "I find comfort in your presence."
                elif a_event_0 < 2/10:
                    wgot "The shadows seem to retreat when you're near."
                elif a_event_0 < 3/10:
                    wgot "I'd be pleased if we could continue our conversation."
                elif a_event_0 < 4/10:
                    wgot "I feel strange when I'm with you."
                elif a_event_0 < 5/10:
                    wgot "Strange{w=[wt2]}, you make me feel comfortable."
                elif a_event_0 < 6/10:
                    wgot "I started a new painting last night.{w=[wt3]} There's more color in it than usual.{w=[wt3]} I wonder why."
                elif a_event_0 < 7/10:
                    wgot "Thank you for not finding my presence disturbing.{w=[wt3]} It means more than you know."
                elif a_event_0 < 8/10:
                    wgot "I found myself smiling while thinking about our last conversation.{w=[wt3]} It was... unfamiliar."
                elif a_event_0 < 9/10:
                    wgot "I watched the sunrise today.{w=[wt3]} For once, the beginning of something didn't fill me with dread."
                else:
                    wgot "Thank you for being here with me."

    # ----------------------------------------------------------------------------------------------------
    # WGOT is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wgot") in ["eating"]:
        "{nm}[fnamewgot]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamewgot]{/nm} is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wgot") from _call_circletable_4

                while Get_ActivityName("wgot") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_5
                call gametime from _call_gametime_19
                
                jump wgot_interact_start

            "Return":
                jump wgot_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_0 = renpy.random.random()

        if wgot_love < 10:
            $ wgot_mood = "O1"
            if a_event_0 < 1/6:
                wgot "Oh{w=[wt2]}, I didn't expect anyone to approach me.{w=[wt3]} Most people prefer to keep their distance."
            elif a_event_0 < 2/6:
                wgot "Misfortune tends to follow those who draw too near to me.{w=[wt3]} Perhaps you should reconsider."
            elif a_event_0 < 3/6:
                wgot "Have you come to witness the sorrowful aura that surrounds me?{w=[wt3]} Or is there some other purpose to your visit?"
            elif a_event_0 < 4/6:
                wgot "Have you lost your way?{w=[wt3]} People rarely seek me out intentionally."
            elif a_event_0 < 5/6:
                wgot "I was just contemplating the inevitable decay of all things.{w=[wt3]} Did you need something?"
            else:
                wgot "How peculiar that you would seek me out.{w=[wt3]} Are you perhaps drawn to the shadows as I am?"

        elif wgot_love < 40:
            $ wgot_mood = "O1"
            if a_event_0 < 1/8:
                wgot "Oh{w=[wt2]}, hello.{w=[wt3]} I didn't expect company today."
            elif a_event_0 < 2/8:
                wgot "Ah{w=[wt2]}, it's you.{w=[wt3]} The fates must have aligned for our paths to cross again."
            elif a_event_0 < 3/8:
                wgot "I was just contemplating the ephemeral nature of existence.{w=[wt3]} But I suppose that can wait."
            elif a_event_0 < 4/8:
                wgot "Oh{w=[wt2]}, it's you again.{w=[wt3]} Your persistence is... notable."
            elif a_event_0 < 5/8:
                wgot "Oh{w=[wt2]}, hey.{w=[wt3]} I was watching that spider weave its web.{w=[wt3]} There's artistry in its patient work."
            elif a_event_0 < 6/8:
                wgot "Your footsteps sound different from others.{w=[wt3]} Less... hesitant."
            elif a_event_0 < 7/8:
                wgot "I was just contemplating how fragile human connections are.{w=[wt3]} Yet here you are again."
            else:
                wgot "The tarot cards suggested I might encounter someone today.{w=[wt3]} I didn't expect it would be you."

        elif wgot_love < 70:
            $ wgot_mood = "A1"
            if a_event_0 < 1/9:
                wgot "Hello...{w=[wt3]} Your presence is... not unwelcome.{w=[wt3]} I was just working on a new sketch."
            elif a_event_0 < 2/9:
                wgot "I sensed someone approaching, and somehow knew it was you.{w=[wt3]} How{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} interesting."
            elif a_event_0 < 3/9:
                wgot "The darkness seems a bit less oppressive today.{w=[wt3]} Perhaps it's because you're here."
            elif a_event_0 < 4/9:
                wgot "I've been working on a new painting.{w=[wt3]} Perhaps{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} you'd like to see it sometime?"
            elif a_event_0 < 5/9:
                wgot "I was just thinking about our last conversation.{w=[wt3]} It lingered in my mind."
            elif a_event_0 < 6/9:
                wgot "The weather today reminds me of a dream I had.{w=[wt3]} You were there, I think."
            elif a_event_0 < 7/9:
                wgot "I'm glad you're here.{w=[wt3]} The voices quiet when you're near."
            elif a_event_0 < 8/9:
                wgot "I find myself{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} pleased to see you.{w=[wt3]} That doesn't happen often with people."
            else:
                wgot "Oh{w=[wt2]}, hello.{w=[wt3]} I was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} hoping I might see you today."

        else:
            $ wgot_mood = "A1"
            $ wgot_fx = 1
            if a_event_0 < 1/9:
                wgot "Oh!{w=[wt3]} I was just thinking about you."
            elif a_event_0 < 2/9:
                wgot "Your arrival brings a rare moment of brightness to my day."
            elif a_event_0 < 3/9:
                wgot "The world seems less cruel when you're near."
            elif a_event_0 < 4/9:
                wgot "I appreciate your company more than I can express."
            elif a_event_0 < 5/9:
                wgot "I was hoping our paths might cross today.{w=[wt3]} The universe can be merciful sometimes."
            elif a_event_0 < 6/9:
                wgot "Oh!{w=[wt3]} I was just thinking about you.{w=[wt3]} It's as if you heard my thoughts."
            elif a_event_0 < 7/9:
                wgot "I found myself looking for you earlier.{w=[wt3]} How strange that you've appeared."
            elif a_event_0 < 8/9:
                wgot "I brought an extra book today.{w=[wt3]} I thought{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} perhaps you might want to read together?"
            else:
                wgot "I found myself less interested in tragedy in my readings lately.{w=[wt3]} I wonder why."
            $ wgot_fx = 0

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wgot_interact:
    call hide_ui from _call_hide_ui_40
    if "interacting_hero" not in wgot_know:
        $ wgot_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wgot_interact_chat
        "Touch" if not is_specialevent:
            jump wgot_interact_touch
        "Hang out":
            jump wgot_interact_hangout
        "Give item" if not is_specialevent:
            jump wgot_interact_gift
        "Return":
            jump wgot_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wgot_interact_gift:
    $ a_item_8 = "wgot"
    $ a_item_9 = 0
    $ a_item_6 = "wgot_interact"
    call UI_give_Item from _call_UI_give_Item_6

label wgot_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wgot_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wgot_interact_touch:
    menu:
        "Hug":
            label wgot_interact_touch_hug:
                pass

            $ wgot_know.append("Hug")
            $ a_event_0 = sum(1 for buceta in wgot_know if buceta =="Hug")
            $ wgot_fx = 1

            $ a_event_1 = renpy.random.random()
            if a_event_1 <= 0.33:
                scene bg_2 pink
            elif a_event_1 <= 0.66:
                scene bg_2 yellow
            else:
                scene bg_2 flowers

            show action_wgot_hug 1a
            with dissolve

            show action_wgot_hug 1b

            $ add_stat("wgot", "love", 2/a_event_0)
            $ add_stat("hero", "cha_sex", (2/a_event_0)/2)

            $ a_event_0 = renpy.random.random()
            if a_event_0 <= 0.25:
                wgot "Hm?{w=[wt2]} Is this a farewell?"
            elif a_event_0 <= 0.50:
                wgot "Would you trying to pass on your luck to me?{w=[wt2]} How fascinating{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Thank you.{w=[wt2]} I hope you survive this direct contact."
            elif a_event_0 <= 0.75:
                wgot "Oh{w=[wt2]}, that was unexpected.{w=[wt2]} How peculiar{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Your arms are so warm and welcoming{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Just like{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} A coffin."
            else:
                wgot "Despite everything I told you{w=[wt2]}, your carnal desires still speak louder.{w=[wt3]} How fascinatingly terrible"

            show action_wgot_hug 1a with None

        "Return":
            jump wgot_interact

    call gamecheck from _call_gamecheck_8
    call hide_ui from _call_hide_ui_41
    call wgot_show from _call_wgot_show_2
    $ gametimemin += 10
    $ add_stat("wgot", "inti", 0.1)
    jump wgot_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wgot_interact_hangout:
    menu:
        "Return":
            jump wgot_interact

    $ gametimemin += 30
    jump wgot_interact_check

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
label wgot_interact_chat:
    menu:
        "Ask how she is" if not "Talk_How" in wgot_know:
            $ hero_mood = "A1"
            $ wgot_mood = "O1"
            
            hero "How are you doing today, {nm}[fnamewgot]{/nm}?"
            
            $ a_event_0 = renpy.random.random()
            
            # ----------------------------------------------------------------------------------------------------
            # wgot_love < 10 - She feels uncomfortable with herself and with HERO's presence
            # ----------------------------------------------------------------------------------------------------
            if wgot_love < 10:
                if a_event_0 < 1/5:
                    wgot "As I always am.{w=[wt3]} Existing."
                elif a_event_0 < 2/5:
                    wgot "Just existing."
                elif a_event_0 < 3/5:
                    wgot "My state of being is largely irrelevant."
                elif a_event_0 < 4/5:
                    wgot "I don't know."
                else:
                    wgot "The shadows and I maintain our usual arrangement.{w=[wt3]} They embrace, I endure."

                hero "Oh... I see..."

                $ a_event_0 = renpy.random.random()

                if a_event_0 < 1/3:
                    wgot "Thank you for asking, though it's not necessary to concern yourself with my well-being."
                elif a_event_0 < 2/3:
                    wgot "Thanks for your concern."
                else:
                    wgot "Your inquiry is appreciated."
            
            # ----------------------------------------------------------------------------------------------------
            # wgot_love < 40 - She feels a bit more comfortable, starting to accept HERO's presence
            # ----------------------------------------------------------------------------------------------------
            elif wgot_love < 40:
                if a_event_0 < 1/5:
                    wgot "I'm adequate.{w=[wt3]} The day has been neither particularly bleak nor unexpectedly bright.{w=[wt3]} And you?"
                elif a_event_0 < 2/5:
                    wgot "I found a quiet moment among the chaos today.{w=[wt3]} So I suppose I'm acceptable.{w=[wt4]} Thank you for asking.{w=[wt4]} What about you?"
                elif a_event_0 < 3/5:
                    wgot "The world continues its relentless march forward, and I with it.{w=[wt3]} I appreciate your inquiry.{w=[wt4]} What about you?"
                elif a_event_0 < 4/5:
                    wgot "I'm surviving.{w=[wt3]} Which is all one can really hope for, isn't it?{w=[wt4]} How are you faring?"
                else:
                    wgot "Today has been... less oppressive than most.{w=[wt3]} I'm managing.{w=[wt3]} Your concern is appreciated.{w=[wt4]} And how are you doing?"

                hero "I'm doing fine, thanks for asking."

                if renpy.random.random() < 1/2:
                    wgot "Quite impressive."
                else:
                    wgot "Impressive."
            
            # ----------------------------------------------------------------------------------------------------
            # wgot_love < 70 - She accepts HERO and feels more comfortable expressing herself
            # ----------------------------------------------------------------------------------------------------
            elif wgot_love < 70:
                $ wgot_mood = "A1"
                if a_event_0 < 0.2:
                    wgot "I'm actually feeling somewhat at peace today.{w=[wt3]} It's an unfamiliar sensation, but not unwelcome.{w=[wt3]} Thank you for asking.{w=[wt4]} And you?"
                elif a_event_0 < 0.4:
                    wgot "I find myself in a contemplative mood.{w=[wt3]} Not mournful{w=[wt2]}, simply thoughtful.{w=[wt4]} And yourself?"
                elif a_event_0 < 0.6:
                    wgot "The weight on my shoulders seems a bit lighter today.{w=[wt3]} I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} okay.{w=[wt3]} It's kind of you to inquire.{w=[wt4]} What about you?"
                elif a_event_0 < 0.8:
                    wgot "I woke with fewer shadows clinging to my thoughts this morning.{w=[wt3]} It's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} nice.{w=[wt4]} I hope you're well?"
                else:
                    wgot "I feel{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} present.{w=[wt3]} More anchored than usual.{w=[wt3]} Your company contributes to that{w=[wt1]}, I think.{w=[wt4]} How are you faring?"
                
                hero "I'm glad to hear that. I'm doing well too."

                if renpy.random.random() < 1/2:
                    wgot "Quite impressive."
                else:
                    wgot "Impressive."
            
            # ----------------------------------------------------------------------------------------------------
            # wgot_love >= 70 - She loves HERO and feels safe with him
            # ----------------------------------------------------------------------------------------------------
            else:
                $ wgot_mood = "A1"
                if a_event_0 < 0.2:
                    wgot "I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} better{w=[wt2]}, now that you're here.{w=[wt4]} Your presence has a calming effect I've come to value.{w=[wt4]} I hope you're doing fine too."
                elif a_event_0 < 0.4:
                    wgot "Seeing you improves my day further.{w=[wt3]} Thank you for asking.{w=[wt4]} I hope you're fine too."
                elif a_event_0 < 0.6:
                    wgot "I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} strange.{w=[wt3]} Can't stop thinking about you.{w=[wt4]} But I hope you're doing well."
                elif a_event_0 < 0.8:
                    wgot "The darkness recedes when you're near.{w=[wt3]} I'm well{w=[wt2]}, thank you.{w=[wt4]} Better for seeing you.{w=[wt4]} I hope you're doing well too."
                else:
                    wgot "A little strange{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} In a comfortable way.{w=[wt3]} That's how you make me feel.{w=[wt4]} How are you?{w=[wt4]} I hope you're doing fine too."
                
                hero "I'm doing great.{w=[wt3]} It's always nice to see you too."
                
                $ wgot_fx = 1
                wgot "Oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm really glad for that."
                $ wgot_fx = 0
            
            $ wgot_know.append("Talk")
            $ wgot_know.append("Talk_How")
            $ add_stat("wgot", "love", 0.5)
            $ add_stat("hero", "cha_soc", 0.5)

        "Talk about someone":
            menu:
                # WPRE
                "{image=icon_wpre} {nm}[fnamewpre]{/nm}" if not "Talk_Char_WPRE" in wgot_know:
                    $ wgot_know.append("Talk_Char_WPRE")
                    $ hero_mood = "A2"
                    hero "What have you observed about {nm}[fnamewpre]{/nm}?"

                    $ a_event_0 = renpy.random.random()

                    if a_event_0 < 1/3:
                        $ wgot_mood = "A1"
                        wgot "Her posture tells a story of burden.{w=[wt3]} The way her shoulders curve slightly forward after school hours{w=[wt2]}, as if bearing an invisible weight.{w=[wt4]} Yet each morning she arrives with spine straight as a ruler{w=[wt2]}, determination renewed."
                        
                        $ hero_mood = "A2"
                        hero "You think she's overworking herself?"
                        
                        $ wgot_mood = "A2"
                        wgot "The evidence suggests as much.{w=[wt3]} Her eyes betray exhaustion that makeup cannot conceal.{w=[wt4]} During lunch{w=[wt2]}, while others socialize{w=[wt2]}, she reviews notes or completes assignments.{w=[wt3]} No moment wasted.{w=[wt4]} How admirable{w=[wt2]}, yet how tragic."
                        
                        $ hero_mood = "O1"
                        hero "Maybe she just takes her studies seriously?"
                        
                        $ wgot_mood = "O1"
                        wgot "Perhaps.{w=[wt3]} But notice her hands.{w=[wt3]} The slight tremor when she raises them in class.{w=[wt4]} The ink stains that never fully wash away.{w=[wt3]} The paper cuts adorning her fingers like macabre jewelry.{w=[wt4]} These are not merely signs of academic devotion{w=[wt2]}, but of someone who has transformed labor into identity.{w=[wt3]} A beautiful martyrdom to ambition."

                    elif a_event_0 < 2/3:
                        $ wgot_mood = "A1"
                        wgot "Admirable.{w=[wt2]} Her very image highlights how dedicated she is.{w=[wt3]} Her braids are perfect mathematical constructs.{w=[wt3]} Observe the symmetry{w=[wt2]}, the precisely equal tension.{w=[wt4]} Not a single hair permitted to rebel against its assigned position.{w=[wt3]} Much like her approach to existence.{w=[wt3]} It must require significant time to achieve such perfection."

                        wgot "Yet she never arrives late.{w=[wt3]} This suggests she rises before dawn{w=[wt2]}, sacrificing sleep for presentation.{w=[wt4]} The braid serves as external manifestation of her internal state{w=[wt2]}, controlled{w=[wt2]}, precise{w=[wt2]}, painfully orderly."

                    else:
                        $ wgot_mood = "A1"
                        wgot "She arrives precisely fifteen minutes before first bell.{w=[wt3]} Never fourteen.{w=[wt4]} Never sixteen.{w=[wt3]} Fifteen minutes devoted to preparation.{w=[wt4]} Books arranged on desk.{w=[wt3]} Notes reviewed.{w=[wt4]} Pencils sharpened to identical length."
                        
                        $ hero_mood = "A2"
                        hero "Wooow! That's very precise! You've timed her?"
                        
                        $ wgot_mood = "A2"
                        wgot "Time is the one currency equally distributed yet inequally utilized.{w=[wt4]} Her routine never varies.{w=[wt4]} Such devotion to routine suggests a mind that finds security in controllable variables amidst life's chaos.{w=[wt3]} The fifteen minutes represent not merely preparation{w=[wt2]}, but affirmation of identity.{w=[wt4]} How elegantly she has constructed meaning from mundane chronology."

                # HPRV
                "{image=icon_hprv} {nm}[fnamehprv]{/nm}" if not "Talk_Char_HPRV" in wgot_know:
                    $ wgot_know.append("Talk_Char_HPRV")

                    if not "WGOT_BG_HPRV_1" in hero_know:
                        $ hero_know.append("WGOT_BG_HPRV_1")

                        $ hero_mood = "A2"
                        hero "What do you think about {nm}[fnamehprv]{/nm}?"
                        
                        $ wgot_mood = "O1"
                        wgot "A tragically necessary evil.{w=[wt3]} Thanks to him{w=[wt2]}, I find myself forever vigilant{w=[wt2]}, keeping my legs closed at all times.{w=[wt3]} A macabre dance of modesty to avoid becoming his next victim.{w=[wt4]} How tragically exhausting."

                        $ hero_mood = "O2"
                        hero "W{w=[wt1]}-what do you mean?"
                    
                        $ wgot_mood = "O1"
                        wgot "I've observed his ritual from my vantage point in the shadows.{w=[wt3]} The tragedy of his existence unfolds daily as he performs his calculated dance.{w=[wt3]} The poor unfortunate soul behind him{w=[wt1]}, {nm}[fnamewlaz]{/nm}{w=[wt2]}, his primary victim{w=[wt2]}, bears the brunt of his visual transgressions.{w=[wt4]} He drops his pen with such rehearsed precision.{w=[wt4]} Such dedication to his craft."

                        $ hero_mood = "O1"
                        hero "Wait{w=[wt2]}, you mean he does that on purpose?"

                        $ wgot_mood = "O1"
                        wgot "How beautifully naive you are.{w=[wt3]} Of course it's intentional.{w=[wt3]} I've noticed he sometimes manages to peer at {nm}[fnamewdel]{/nm}'s undergarments as well.{w=[wt3]} Though I find a certain poetic justice in his suffering.{w=[wt3]} Doomed to forever seek that which remains just beyond his reach.{w=[wt4]} Besides, I find his futile attempts... somewhat amusing to observe."

                    elif not "WGOT_BG_HPRV_2" in hero_know:
                        $ hero_know.append("WGOT_BG_HPRV_2")

                        $ hero_mood = "A2"
                        hero "Do you think {nm}[fnamehprv]{/nm} still been{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} persistent with his hobby?"

                        $ wgot_mood = "A2"
                        wgot "He possesses a remarkable resilience.{w=[wt3]} A trait that would be admirable if not so misguided.{w=[wt4]} Did you know that once the redhead from class 1A threatened him?"

                        $ hero_mood = "O1"
                        hero "Oh{w=[wt2]}, it's {nm}[fnamehriv]{/nm}!{w=[wt3]} They certainly don't get along at all." id wgot_interact_chat_1f117c70_1

                        $ wgot_mood = "A1"
                        wgot "He cornered our pervert after catching him staring at some girls during lunch.{w=[wt3]} It seemed as though physical violence was imminent.{w=[wt4]} But then, the most deliciously ironic thing happened."
                        
                        wgot "{nm}[fnamewdel]{/nm} appeared{w=[wt2]}, like a valkyrie of chaos{w=[wt2]}, and declared quite loudly{w=[wt2]}, '{aw}Who do you think you are to treat my punching bag!?{/aw}'{w=[wt4]} Then she proceeded to hit {nm}[fnamehprv]{/nm} herself while cursing the redhead.{w=[wt3]} It was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} magnificent in its absurdity." id wgot_interact_chat_d9fe64eb_1

                        $ hero_mood = "A4"
                        hero "Oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I don't really know if I feel bad or not for him."

                    else:
                        $ hero_mood = "A1"
                        hero "What do you have to say about {nm}[fnamehprv]{/nm}?"

                        $ a_event_0 = renpy.random.random()

                        if a_event_0 < 1/5:
                            $ wgot_mood = "A1"
                            wgot "We are similar.{w=[wt3]} In our mutual voyeurism{w=[wt2]}, {nm}[fnamehprv]{/nm} and I share a strange kinship.{w=[wt3]} Two observers circling the same subjects from vastly different orbits.{w=[wt4]} While he hungers for glimpses of forbidden flesh{w=[wt2]}, I dissect the shadows cast by the soul."
                            
                            $ wgot_mood = "A2"
                            wgot "We both consume what others unknowingly offer.{w=[wt4]} His gaze violates the physical{w=[wt2]}; mine penetrates the metaphysical.{w=[wt3]} Both intrusions remain largely undetected by our subjects.{w=[wt4]} The difference lies in what we seek to satisfy his carnal appetite versus my existential curiosity."
                            
                            $ wgot_mood = "O1"
                            wgot "Perhaps that's why I find him oddly fascinating rather than merely repulsive.{w=[wt3]} We are two sides of the same tarnished coin{w=[wt2]}, forever watching{w=[wt2]}, never truly participating.{w=[wt4]} How beautifully, tragically familiar."

                        elif a_event_0 < 2/5:
                            $ wgot_mood = "O1"
                            wgot "I find it curious that despite his obsession, he never seems satisfied.{w=[wt3]} The glimpses he steals only feed a hunger that grows with each morsel.{w=[wt4]} Perhaps that's the true punishment for his perversion{w=[wt2]}, the insatiable nature of his desires."

                            wgot "His eyes betray a deeper melancholy when he thinks no one is watching.{w=[wt3]} I sometimes wonder if he realizes the futility of his pursuits.{w=[wt4]} The ephemeral glimpses he steals can never satisfy the void within."

                            $ wgot_mood = "O1"
                            wgot "But the most fascinating aspect of his existence is the dichotomy between his shameless actions and his fragile soul.{w=[wt3]} When confronted{w=[wt2]}, he withers like a flower in winter's first frost.{w=[wt4]} Such a beautifully tragic contradiction."
                            
                            $ hero_mood = "A2"
                            hero "I guess everyone has their contradictions."
                            
                            $ wgot_mood = "A2"
                            wgot "Indeed.{w=[wt3]} Perhaps his perversion is merely a shield against the unbearable loneliness of existence.{w=[wt3]} Or perhaps he's simply a deviant.{w=[wt4]} Both possibilities hold their own macabre charm."
                            
                            $ hero_mood = "A2" 
                            hero "You really observe people closely, don't you?"
                            
                            $ wgot_mood = "A1"
                            wgot "The darkened corners provide the perfect vantage point for studying humanity's little tragedies.{w=[wt3]} There's a certain elegance to the way {nm}[fnamehprv]{/nm} orchestrates his falls.{w=[wt3]} A practiced performer of depravity.{w=[wt4]} I almost admire the dedication, if not the craft itself.{w=[wt4]} Almost."

                        elif a_event_0 < 3/5:
                            $ wgot_mood = "A1"
                            wgot "We both have lunch here in the classroom.{w=[wt3]} He brings the same egg sandwich wrapped in wax paper every day.{w=[wt3]} Not the typical convenience store fare one might expect.{w=[wt4]} He arranges each component with surprising care before eating."
                            
                            $ hero_mood = "A2"
                            hero "I see.{w=[wt4]} The classroom seems like a very peaceful place to eat{w=[wt2]}, away from stares and judgment.{w=[wt4]} Knowing he has skills in the kitchen is quite interesting{w=[wt2]}, I guess there's always more to people than we initially see."
                            
                            $ wgot_mood = "A2"
                            wgot "I wonder if he cooks them himself.{w=[wt4]} Such domestic capabilities would add another unexpected layer to his otherwise predictable existence.{w=[wt3]} Perhaps{w=[wt2]}, the care in its preparation suggests someone at home still believes in his redemption.{w=[wt3]} How touchingly hopeful."

                        elif a_event_0 < 4/5:
                            $ wgot_mood = "A2"
                            wgot "He seems to have an interest in literature and science{w=[wt2]}, but has difficulty with mathematics.{w=[wt3]} I've observed him reading science fiction novels at the library.{w=[wt3]} His taste isn't entirely terrible."

                            $ wgot_mood = "A1"
                            wgot "During literature discussions{w=[wt2]}, his eyes light up.{w=[wt3]} Particularly when discussing the romantic poets.{w=[wt4]} He never contributes{w=[wt2]}, but his attention becomes absolute.{w=[wt3]} A hint that beneath his crude exterior lies a soul capable of appreciating beauty."
                            
                            $ hero_mood = "A2"
                            hero "Everyone connects with something meaningful, I guess."

                            $ wgot_mood = "O1"
                            wgot "Yes.{w=[wt3]} However{w=[wt2]}, he struggles terribly with mathematics.{w=[wt3]} I've watched him stare at the same equation for an entire study period{w=[wt2]}, his frustration a palpable cloud around him.{w=[wt4]} There's something beautifully tragic about witnessing someone confront the limits of their comprehension."
                            
                            $ hero_mood = "A2"
                            hero "Maybe he needs some help with studying."
                            
                            $ wgot_mood = "A2"
                            wgot "Perhaps."

                        else:
                            $ wgot_mood = "O1"
                            wgot "His handwriting is surprisingly elegant.{w=[wt3]} Flowing cursive that seems to belong to another century{w=[wt2]}, another soul entirely.{w=[wt4]} Such refinement amid his otherwise crude existence.{w=[wt3]} These contradictions are what make humans so tragically interesting."
                            
                            $ hero_mood = "A2"
                            hero "People are often more complex than they appear."
                            
                            $ wgot_mood = "A1"
                            wgot "Indeed.{w=[wt3]} We are all collections of conflicting impulses and forgotten talents.{w=[wt4]} His calligraphy suggests a childhood of strict discipline.{w=[wt3]} One wonders what shaped him thus."

                "{image=icon_wdis} {nm}[fnamewdis]{/nm}" if not "Talk_Char_WDIS" in wgot_know:
                    $ wgot_know.append("Talk_Char_WDIS")
                    $ hero_mood = "A2"
                    hero "What do you think about {nm}[fnamewdis]{/nm}?"

                    $ a_event_0 = renpy.random.random()

                    if a_event_0 < 1/5:
                        $ wgot_mood = "A1"
                        wgot "She's just like me.{w=[wt3]} Maybe worse.{w=[wt4]} In her, I see a reflection of my own cursed existence."
                        
                        $ hero_mood = "A2"
                        hero "I'm not sure I follow. You both seem quite different to me."
                        
                        $ wgot_mood = "A2"
                        wgot "We are kindred spirits of catastrophe.{w=[wt3]} The difference lies in the radius of our destruction.{w=[wt3]} Her chaos remains largely self-contained{w=[wt2]}, a personal apocalypse that rarely extends beyond her immediate surroundings.{w=[wt3]} Mine spread like a contagion to all living things nearby."
                        
                        $ hero_mood = "A2"
                        hero "That sounds a bit extreme."
                        
                        $ wgot_mood = "O1"
                        wgot "The truth remains that both {nm}[fnamewdis]{/nm} and I walk paths of perpetual misfortune.{w=[wt4]} Perhaps that is why I find a strange comfort in her presence.{w=[wt3]} There's solace in shared suffering, even when the sufferers remain unaware of their connection."

                    elif a_event_0 < 2/5:
                        $ wgot_mood = "A1"
                        wgot "Her gaze frequently wanders to the athletic redhead from class 1A.{w=[wt4]} The hunger in her eyes is both obvious and painful to witness.{w=[wt3]} A moth drawn to a flame that will surely consume it."
                        
                        $ hero_mood = "A2"
                        hero "Oh... It must be {nm}[fnamehriv]{/nm}."
                        
                        $ wgot_mood = "O1"
                        wgot "Her eyes follow him with the devotion of a sunflower tracking the sun across the sky.{w=[wt4]} The tragedy of unrequited affection is as old as humanity itself.{w=[wt3]} Her particular version is especially poignant{w=[wt2]}, as she lacks even the self-awareness to hide her feelings.{w=[wt4]} Her heart is as exposed as her undergarments during her frequent falls.{w=[wt3]} Both revealed without her knowledge or consent."

                    elif a_event_0 < 3/5:
                        $ wgot_mood = "A1"
                        wgot "She harbors a curious duality in her relationship with nature's creatures.{w=[wt3]} An affinity for mammals and birds{w=[wt2]}, yet a primal terror of insects.{w=[wt4]} I've observed her spending lunch periods with that stray tabby cat in the courtyard. {w=[wt3]} She brings it scraps of her lunch{w=[wt2]}, speaking to it in hushed tones as if sharing secrets with a confidant.{w=[wt4]} Her tenderness is... unexpectedly beautiful."
                        
                        $ wgot_mood = "A1"
                        wgot "Yet observe her near the school garden when insects take flight.{w=[wt3]} She becomes a portrait of pure terror.{w=[wt4]} Once, a single butterfly sent her fleeing across the courtyard{w=[wt2]}, screaming as though pursued by death itself.{w=[wt4]} How fascinating that such innocuous creatures can reduce her to such primal fear."
                        
                        $ hero_mood = "A2"
                        hero "Well, lots of people are afraid of bugs. That's pretty common, I think."
                        
                        $ wgot_mood = "A2"
                        wgot "Society makes no sense{w=[wt2]}, their reactions transcend ordinary logic.{w=[wt4]} Or perhaps she sees in small mammals a reflection of her own vulnerability.{w=[wt4]} Either way{w=[wt2]}, it's a glimpse into the fragile ecosystem of her soul."
                        
                        $ wgot_mood = "A1"
                        wgot "Indeed.{w=[wt3]} The feline tolerates her affections with notable patience.{w=[wt4]} A remarkable contrast to its reaction to my presence.{w=[wt3]} When I approach{w=[wt2]}, it arches its back and flees as if pursued by death itself.{w=[wt4]} Which{w=[wt2]}, in a sense{w=[wt2]}, it is."

                    elif a_event_0 < 4/5:
                        $ wgot_mood = "A1"
                        wgot "Her mind seems perpetually adrift.{w=[wt3]} During lectures{w=[wt2]}, she stares at the blackboard with such intensity{w=[wt2]}, yet absorbs nothing.{w=[wt4]} I've watched her eyes glaze over while her body remains perfectly still{w=[wt2]}, a living statue amidst the classroom chaos."
                        
                        $ hero_mood = "A2"
                        hero "You think she has trouble focusing?"
                        
                        $ wgot_mood = "A1"
                        wgot "More than mere trouble.{w=[wt3]} It's as if her thoughts exist in a parallel dimension to our reality.{w=[wt4]} When called upon{w=[wt2]}, she startles as though waking from a deep slumber{w=[wt2]}, even with her eyes wide open."
                        
                        $ hero_mood = "A2"
                        hero "That must make studying difficult for her."
                        
                        $ wgot_mood = "A2"
                        wgot "Undoubtedly.{w=[wt3]} Her notebook pages remain pristine{w=[wt2]}, save for elaborate doodles in the margins.{w=[wt4]} She requires constant redirection{w=[wt2]}, a lighthouse keeper to guide her wandering ship back to shore.{w=[wt3]} Perhaps what she truly needs is not just assistance{w=[wt2]}, but genuine motivation{w=[wt2]}... a reason to remain anchored in our shared reality."
                        
                        $ hero_mood = "O1"
                        hero "That sounds more intense than ordinary daydreaming."
                        
                        $ wgot_mood = "O1"
                        wgot "Indeed.{w=[wt3]} I sometimes wonder if her frequent retreats into fantasy are a response to her reality.{w=[wt4]} A self-protective mechanism{w=[wt2]}, perhaps.{w=[wt3]} The mind creating sanctuary when the body fails it so consistently.{w=[wt4]} There's a certain poetry to that form of escape."

                    else:
                        $ wgot_mood = "A1"
                        wgot "Each morning, she arrives precariously balanced upon a bicycle.{w=[wt3]} The sight is both mesmerizing and terrifying{w=[wt2]}, like watching a tightrope walker in a strong wind.{w=[wt4]} I find myself holding my breath until she reaches the bike rack."
                        
                        $ hero_mood = "O1"
                        hero "That seems dangerous for someone as clumsy as her.{w=[wt3]} Has she ever fallen?"
                        
                        $ wgot_mood = "A2"
                        wgot "Curiously{w=[wt2]}, I have yet to witness such a catastrophe.{w=[wt3]} Though logic dictates it must occur with alarming frequency.{w=[wt4]} Perhaps she reserves her most spectacular falls for routes beyond my observation."
                        
                        $ hero_mood = "A2"
                        hero "Maybe she's actually really good at biking? People can surprise you with unexpected talents."
                        
                        $ wgot_mood = "A1"
                        wgot "An intriguing hypothesis.{w=[wt3]} Perhaps her body finds harmony in motion that eludes her while stationary.{w=[wt4]} Or perhaps she exists in a state of perfect chaos{w=[wt2]}, where disaster is so imminent that it paradoxically never arrives.{w=[wt3]} How beautifully precarious."

                "{image=icon_wota} {nm}[fnamewota]{/nm}" if not "Talk_Char_WOTA" in wgot_know:
                    $ wgot_know.append("Talk_Char_WOTA")
                    $ hero_mood = "A2"
                    hero "What about {nm}[fnamewota]{/nm}? She sits at the front, right?"

                    $ wgot_mood = "A1"
                    wgot "Ah, the one who dwells between worlds.{w=[wt3]} Her reality is delightfully fractured.{w=[wt4]} I've heard her muttering incantations beneath her breath.{w=[wt3]} She believes she channels dark forces, yet her aura glows with innocence.{w=[wt3]} How wonderfully contradictory."

                    $ hero_mood = "A2"
                    hero "You sound like you might get along with her."

                    $ wgot_mood = "A1"
                    wgot "Perhaps.{w=[wt3]} Though our darkness springs from different wells.{w=[wt3]} Mine flows from the acceptance of mortality and decay.{w=[wt4]} Hers from a desperate desire to transcend this mundane existence.{w=[wt3]} Still, I find her commitment to her delusions... admirable.{w=[wt3]} She wears her fantasy like I wear my shroud of melancholy.{w=[wt4]} We are not so different, she and I."

                    $ hero_mood = "A2"
                    hero "You should talk to her sometime."

                    $ wgot_mood = "O1"
                    wgot "Maybe in time.{w=[wt3]} I fear my presence might wither her fantasy garden.{w=[wt3]} Plants die in my proximity, you know.{w=[wt3]} I wonder if imaginary constructs fare better or worse?"

                "{image=icon_wric} {nm}[fnamewric]{/nm}" if not "Talk_Char_WRIC" in wgot_know:
                    $ wgot_know.append("Talk_Char_WRIC")
                    $ hero_mood = "A2"
                    hero "What are your thoughts on {nm}[fnamewric]{/nm}?"

                    $ wgot_mood = "O1"
                    wgot "The gilded cage houses the most desperate bird.{w=[wt4]} I've watched her parade her wealth like armor.{w=[wt3]} Each diamond a shield against genuine connection.{w=[wt3]} How tragic to value what rusts and fades."

                    $ hero_mood = "A2"
                    hero "That's pretty harsh. You don't like her?"

                    $ wgot_mood = "O1"
                    wgot "Like and dislike are such shallow concepts.{w=[wt3]} I find her existence... educational.{w=[wt4]} She surrounds herself with glittering objects yet radiates emptiness.{w=[wt3]} I see how her eyes search the room for validation.{w=[wt3]} How she straightens her posture when attention turns her way.{w=[wt4]} Her loneliness calls to me like a distant funeral bell."

                    $ hero_mood = "O1"
                    hero "I didn't realize you'd noticed so much about her."

                    $ wgot_mood = "A1"
                    wgot "I observe much while speaking little.{w=[wt3]} The privileged often cast the longest shadows.{w=[wt3]} Hers stretches far, yet offers no true darkness.{w=[wt3]} Just... emptiness disguised as superiority.{w=[wt3]} Perhaps one day she'll realize wealth cannot purchase peace in the grave."

                "{image=icon_wgal} {nm}[fnamewgal]{/nm}" if not "Talk_Char_WGAL" in wgot_know:
                    $ wgot_know.append("Talk_Char_WGAL")
                    $ hero_mood = "A2"
                    hero "Have you formed any opinions about {nm}[fnamewgal]{/nm} yet?"

                    $ wgot_mood = "O1"
                    wgot "The one who shines with reflected light.{w=[wt4]} She crafts a persona of perfection while her eyes betray her exhaustion.{w=[wt3]} How tiring to maintain such a facade.{w=[wt3]} Like watching someone slowly suffocate beneath a beautiful mask."

                    $ hero_mood = "A2"
                    hero "You think she's fake?"

                    $ wgot_mood = "O1"
                    wgot "We all wear masks.{w=[wt3]} Hers is simply more carefully constructed than most.{w=[wt4]} I've seen how her smile doesn't reach her eyes.{w=[wt3]} How her laughter changes pitch depending on her audience.{w=[wt3]} She fears authenticity more than death itself.{w=[wt4]} A fascinating specimen of self-deception."

                    $ hero_mood = "O1"
                    hero "I don't think she'd appreciate that assessment."

                    $ wgot_mood = "A1"
                    wgot "Few appreciate truth's cold embrace.{w=[wt3]} I don't judge her harshly for it.{w=[wt3]} We all have our methods of navigating life's brief journey.{w=[wt3]} Hers involves constructing an illusion of status.{w=[wt3]} Perhaps it brings her comfort.{w=[wt4]} Though I wonder if she remembers who lies beneath the performance."
                
                "Return":
                    jump wgot_interact_chat

        "Return":
            jump wgot_interact

    $ add_stat("wgot", "inti", 0.2)
    $ gametimemin += 20
    jump wgot_interact_check

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_wgot:
    $ wgot_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wgot_inti*0.02) and not any(get_id.startswith("HERO_Dated") for get_id in wgot_know):

        $ wgot_mood = "O1"
        wgot "I've been wondering about something.{w=[wt3]} It's perhaps too personal{w=[wt1]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Have you ever dated someone?"

        $ hero_fx = 1
        $ hero_mood = "O1"

        menu:
            wgot "I've been... wondering about something. It's perhaps too personal, but... Have you ever dated someone?{fast}"
            
            "Deny":
                $ wgot_know.append("HERO_Dated_N")
                $ msg.msg(renpy.translate_string("{nm}[fnamewgot]{/nm} knows you a little more"))
                $ add_stat("wgot", "inti", 0.5)

                hero "N{w=[wt1]}-No{w=[wt2]}, I've never dated before."

                if wgot_love < 40:
                    $ wgot_mood = "O1"
                    wgot "I see.{w=[wt3]} Perhaps some of us are destined to walk our paths alone.{w=[wt3]} The petals fall from the rose whether it has been held or not."
                else:
                    $ wgot_mood = "A1"
                    wgot "How curious.{w=[wt3]} Someone like you{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I would have thought{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Well{w=[wt2]}, nevermind.{w=[wt3]} Sometimes the most beautiful flowers bloom unseen{w=[wt1]}, I suppose."
                    $ wgot_fx = 1
                    $ wgot_fx = 0

            "Confirm":
                $ wgot_know.append("HERO_Dated_Y")
                $ msg.msg(renpy.translate_string("{nm}[fnamewgot]{/nm} knows you a little more"))
                $ add_stat("wgot", "inti", 0.5)

                hero "W{w=[wt1]}-well{w=[wt2]}, y{w=[wt1]}-yes{w=[wt2]}, I kinda dated a girl once."

                if wgot_love < 40:
                    $ wgot_mood = "O1"
                    wgot "I see.{w=[wt3]} You've experienced the inevitable pain that follows connection."
                    hero "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Kind of."
                    wgot "Understandable.{w=[wt3]} All endings carry their own quiet tragedy."
                else:
                    $ wgot_mood = "O1"
                    wgot "Oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Of course.{w=[wt3]} Someone like you would naturally have such experiences.{w=[wt3]} I hope it brought you more joy than sorrow{w=[wt2]}, even if temporary."
                    hero "It was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} an experience{w=[wt1]}, for sure."
                    wgot "Yes.{w=[wt3]} Such is the nature of human connection.{w=[wt3]} Fleeting{w=[wt2]}, but meaningful nonetheless."

            "Don't choose":
                jump initiative_wgot_return

    # ----------------------------------------------------------------------------------------------------
    # Ask HERO's girl preference
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wgot_inti*0.02) and sum(1 for get_id in wgot_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wgot_know if get_id.startswith("HERO_N_Girl")) < 4:
        $ wgot_mood = "O1"
        wgot "There's something I've been curious about.{w=[wt3]} Though perhaps it's too mundane a question.{w=[wt3]} What type of person you might find{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Attractive?{nw}"

        menu:
            wgot "There's something I've been curious about. Though perhaps it's too mundane a question. What type of person you might find... Attractive?{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in wgot_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in wgot_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in wgot_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in wgot_know if "Personality_" in get_id)

                # Appearance Likes(Y)/Dislikes(N)
                $ a_event_1 = wgot_know
                $ a_event_3 = "initiative_wgot_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_5

                # Store the answer if one was given
                if _return:
                    $ wgot_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg(renpy.translate_string("{nm}[fnamewgot]{/nm} knows you a little more"))
                $ add_stat("wgot", "inti", 0.5)

                if _return in ["Personality_2", "Personality_6", "HairSize_5", "HairSize_6", "Breast_2", "EyeShape_4", "EyeShape_5"]: # Match - dispirited, shy/timid, long hair, medium breasts, downturned/deep set eyes
                    $ add_stat("wgot", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ wgot_mood = "A1"
                    $ wgot_fx = 1

                    if wgot_love < 40:
                        wgot "Oh.{w=[wt3]} That's interesting.{w=[wt3]} I find myself surprised by your answer."
                    else:
                        wgot "I see.{w=[wt3]} How unexpected.{w=[wt3]} I wouldn't have thought{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Well{w=[wt2]}, preferences are curious things{w=[wt2]}, aren't they?"
                    $ wgot_fx = 0

                elif _return in ["Personality_1", "Personality_5", "HairSize_0", "HairSize_1", "HairSize_2", "EyeShape_1"]: # Opposite match - energetic, outgoing, short/bald hair, round eyes
                    $ add_stat("wgot", "bonus", -10)
                    $ wgot_mood = "O1"
                    if wgot_love < 40:
                        wgot "How interesting.{w=[wt3]} That makes sense."
                    else:
                        wgot "Of course.{w=[wt3]} Most are drawn to the light, not the shadows.{w=[wt3]} It's the natural way of things."

                else: # Others
                    $ wgot_mood = "A1"
                    if wgot_love < 40:
                        wgot "I see.{w=[wt3]} There's a certain poetry in your preference.{w=[wt3]} Not what I expected, but intriguing."
                    else:
                        wgot "Your taste has a certain depth to it.{w=[wt3]} More substance than most.{w=[wt3]} It's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} refreshing."

            "Don't choose":
                jump initiative_wgot_return

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:
        $ wgot_mood = "O1"
        $ a_event_0 = renpy.random.random()
        
        if wgot_love < 50:
            if a_event_0 < 1/4:
                wgot "Forgive me.{w=[wt3]} Sometimes my thoughts drift into the void.{w=[wt3]} The silence grows heavy{w=[wt2]}, and I forget what I meant to say."
            elif a_event_0 < 2/4:
                wgot "The shadows whispered something to me{w=[wt2]}, but it's gone now.{w=[wt3]} Like mist before the morning sun."
            elif a_event_0 < 3/4:
                wgot "I had a question{w=[wt2]}, but perhaps it's better left unasked.{w=[wt3]} Some things are better left to uncertainty."
            else:
                wgot "My mind wanders sometimes to places others cannot follow.{w=[wt3]} I apologize for the momentary lapse."

        else:
            if a_event_0 < 1/3:
                wgot "I was going to ask you something{w=[wt1]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Perhaps another time.{w=[wt3]} When the moment feels right."
            elif a_event_0 < 2/3:
                wgot "Words can be so fragile sometimes.{w=[wt3]} They crumble before they can be spoken.{w=[wt3]} Maybe it's for the best."
            else:
                wgot "I find myself{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} hesitating.{w=[wt3]} Some questions seem too intrusive{w=[wt2]}, even when curiosity lingers."

        jump wgot_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("wgot", "inti", 0.20)
    jump wgot_interact_check

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wgot_return:

    call hero_n_answer from _call_hero_n_answer_5

    $ wgot_mood = "O1"
    $ a_event_0 = renpy.random.random()
    
    if a_event_0 < 1/6:
        wgot "I shouldn't have asked.{w=[wt3]} Some questions are like opening graves{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Better left undisturbed."
    elif a_event_0 < 2/6:
        wgot "Of course.{w=[wt3]} My inquiries tend to make others uncomfortable.{w=[wt3]} I apologize."
    elif a_event_0 < 3/6:
        wgot "The silence holds its own answer.{w=[wt3]} Sometimes what remains unsaid speaks volumes."
    elif a_event_0 < 4/6:
        wgot "Please, don't worry.{w=[wt3]} Some thoughts aren't meant to be shared.{w=[wt3]} I understand."
    elif a_event_0 < 5/6:
        wgot "I value your honesty.{w=[wt3]} Better no answer than one forced by social obligation."
    else:
        wgot "It was presumptuous of me to ask.{w=[wt3]} Your boundaries are to be respected{w=[wt2]}, not questioned."
    
    jump wgot_interact
