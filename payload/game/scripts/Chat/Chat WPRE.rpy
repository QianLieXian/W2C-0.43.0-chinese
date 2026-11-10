# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wpre_show:

    if wpre_love <= -20:
        $ wpre_mood = "O2"
    elif wpre_love < 0:
        $ wpre_mood = "A2"
    elif wpre_love >= 0:
        $ wpre_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_10

    show WPRE at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wpre_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewpre][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wpre")))))

    if Get_ActivityName("wpre") in ["at class"]:
        jump show_ui

    else:
        return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wpre_interact_end:
    if "interacting_hero" in wpre_know:
        $ wpre_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wpre_interact_start:
    call hide_ui from _call_hide_ui_72
    call wpre_show_activity from _call_wpre_show_activity
    $ wpre_inti = min(char_inti_cap, wpre_inti)
    call hide_ui from _call_hide_ui_73
    call wpre_show from _call_wpre_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wpre_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if hero_map == wpre_map:
        pass

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wpre_interact_check:
    # Save current outfit before any updates
    $ wpre_wear_keep = wpre_wear

    call gametime from _call_gametime_34
    call hide_ui from _call_hide_ui_74

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wpre_wear != wpre_wear_keep:
        $ wpre_wear = wpre_wear_keep

    call wpre_show from _call_wpre_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------------------------------------------------------------------------------------------------
    # Check if is Special Event: Exploring The School
    # ----------------------------------------------------------------------------------------------------
    if hero_quest_2 == 1:
        if not "hallway2" in scenestep and not "courtyard" in scenestep and not "library" in scenestep:
            wpre "Please, lead the way.{w=[wt2]} I'm looking forward to explore the school with you!"

        elif "hallway2" in scenestep and "courtyard" in scenestep and "library" in scenestep:
            wpre "I'm grateful for your company.{w=[wt2]} I believe we made a great use of this initial time.{w=[wt2]} How about we go to the classroom?"

        elif ("courtyard" in scenestep and "library" in scenestep):
            wpre "How about we go upstairs?"

        elif ("courtyard" in scenestep and "hallway2" in scenestep):
            wpre "How about we know the library?"

        elif ("hallway2" in scenestep and "library" in scenestep):
            wpre "How about we take a look at the back area of the school?"

        else:
            wpre "I'm grateful for your company, {nm}[fnamehero]{/nm}.{w=[wt3]} May I ask what direction shall we proceed in now?"
        jump wpre_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    # At work in the grocery store
    if (gametimehour >= 15 and gametimehour < 20) and gametimeweek in ["Monday", "Wednesday", "Friday"]:
        wpre "I apologize, but I'm currently on duty at the grocery store. Perhaps we could converse later?"
        jump wpre_interact_end

    # Studying
    elif (gametimehour >= 20 or gametimehour < 6) and not gametimeweek == "Saturday":
        wpre "I'm terribly sorry, but I need to focus on my studies right now. May we speak another time?"
        jump wpre_interact_end

    # Changed map
    elif gametimehour >= 18:
        wpre "I apologize{w=[wt2]}, but I have some matters to attend to right now.{w=[wt3]} Perhaps we can continue our conversation another time?"
        $ hero_fx = 0
        jump wpre_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Get_MapName("wpre", "at class"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "wpre"):
            $ wpre_mood = "A2"
            wpre "Oh{w=[wt2]}, class is starting.{w=[wt3]} We should head to our seats."

            $ hero_mood = "A1"
            hero "Right{w=[wt2]}, let's go."
            
            $ wpre_mood = "A1"
            wpre "After you."

            jump wpre_interact_end

        else:
            $ wpre_mood = "A2"
            wpre "It's time for class.{w=[wt3]} Shall we head there together?"

            menu:
                "Go together":
                    $ hero_mood = "A2"
                    hero "Sure{w=[wt2]}, let's go."
                    
                    $ wpre_mood = "A2"
                    wpre "Wonderful.{w=[wt3]} I find walking with classmates helps maintain punctuality."
                    
                    scene bg_0
                    with dissolve

                    $ hero_map = wpre_map
                    call gametime from _call_gametime_35
                    call check_playermap from _call_check_playermap_19
                    call hide_ui from _call_hide_ui_75
                    show WPRE at RC
                    show HERO at LC
                    with dissolve
                    
                    $ wpre_mood = "A1"
                    wpre "Have a good class, {nm}[fnamehero]{/nm}."

                    jump wpre_interact_end
                    
                "Let her go":
                    pass
            
            $ hero_mood = "A1"
            hero "I have something to do first."

            $ wpre_mood = "O2"
            wpre "Understood.{w=[wt3]} Just{w=[wt2]}, please be careful not to neglect your studies.{w=[wt3]} As class president{w=[wt2]}, I worry about my classmates' attendance."
            
            $ hero_mood = "A1"
            hero "I'll be fine{w=[wt2]}, thanks."
            
            $ wpre_mood = "A2"
            wpre "Of course.{w=[wt2]} See you later then."
            
            show WPRE at RC
            show WPRE at OR_slow
            pause(1.5)

        jump wpre_interact_end

    # ----------------------------------------------------------------------------------------------------
    # WPRE is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wpre") in ["eating"]:
        "{nm}[fnamewpre]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamewpre]{/nm} is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wpre") from _call_circletable_8

                while Get_ActivityName("wpre") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_11
                call gametime from _call_gametime_36

                jump wpre_interact_start

            "Return":
                jump wpre_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wpre_know:
        $ a_event_0 = renpy.random.random()

        if renpy.random.random() < (0.2 + (wpre_love * 0.003)):
            jump initiative_wpre

        elif wpre_love < 0:
            $ wpre_mood = "A2"
            if a_event_0 < 1/4:
                wpre "Pardon me for asking{w=[wt2]}, but is there anything else I can assist you with?"
            elif a_event_0 < 2/4:
                wpre "I hope I'm not being rude{w=[wt2]}, but I have a rather tight schedule today."
            elif a_event_0 < 3/4:
                wpre "While I appreciate your company{w=[wt2]}, I must remind you that we both have academic obligations to fulfill."
            else:
                wpre "Pardon me{w=[wt2]}, but is there a specific matter you wished to discuss?"

        elif wpre_love < 50:
            $ wpre_mood = "A1"
            if a_event_0 < 1/9:
                wpre "I truly appreciate your company, {nm}[fnamehero]{/nm}.{w=[wt3]} Your presence is most refreshing."
            elif a_event_0 < 2/9:
                wpre "If I may say so{w=[wt2]}, our conversations are always enlightening.{w=[wt3]} I'm grateful for your time."
            elif a_event_0 < 3/9:
                wpre "I hope I'm not being a bother{w=[wt2]}, but I do enjoy our interactions immensely."
            elif a_event_0 < 4/9:
                wpre "Your dedication to self-improvement is admirable, {nm}[fnamehero]{/nm}.{w=[wt3]} It's truly inspiring."
            elif a_event_0 < 5/9:
                wpre "It's always a great pleasure to talk to you, {nm}[fnamehero]{/nm}."
            elif a_event_0 < 6/9:
                wpre "By the way{w=[wt2]}, I hope your studies are progressing well.{w=[wt2]} Remember, diligence is key to success."
            elif a_event_0 < 7/9:
                wpre "It's important to maintain a balance between academic pursuits and social interactions.{w=[wt2]} I'm still learning that myself."
            elif a_event_0 < 8/9:
                wpre "I must say{w=[wt2]}, I find our conversations quite enlightening.{w=[wt3]} It's refreshing to interact with someone who values effort."
            else:
                wpre "If you're having trouble with any subjects{w=[wt2]}, please don't hesitate to ask for assistance.{w=[wt3]} I'd be more than happy to help."

        else:
            $ wpre_mood = "A1"
            if a_event_0 < 1/4:
                wpre "Oh my{w=[wt2]}, I hope I'm not blushing.{w=[wt3]} It's just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} your presence makes me a bit flustered."
            elif a_event_0 < 2/4:
                wpre "I must admit{w=[wt2]}, I find your company quite enjoyable.{w=[wt3]} I hope that's not too forward of me to say."
            elif a_event_0 < 3/4:
                wpre "You know{w=[wt2]}, I've been thinking{w=[wt2]}, Perhaps we could study together sometime?{w=[wt3]} If you'd like, of course!"
            else:
                wpre "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I really appreciate your friendship, {nm}[fnamehero]{/nm}.{w=[wt3]} It means a lot to me."

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_0 = renpy.random.random()

        if not "Greeting" in wpre_know:
            $ wpre_know.append("Greeting")
            if gametimehour >= 5 and gametimehour < 12:
                if a_event_0 < 1/3:
                    wpre "Good morning, {nm}[fnamehero]{/nm}.{w=[wt2]} I hope your day is off to a pleasant start."
                elif a_event_0 < 2/3:
                    wpre "Ah{w=[wt1]}, {nm}[fnamehero]{/nm}!{w=[wt2]} A very good morning to you."
                else:
                    wpre "Good morning, {nm}[fnamehero]{/nm}."
                hero "Good morning, {nm}[fnamewpre]{/nm}."

            elif gametimehour >= 12 and gametimehour < 18:
                if a_event_0 < 1/3:
                    wpre "Good afternoon, {nm}[fnamehero]{/nm}.{w=[wt2]} I hope your day has been productive so far."
                elif a_event_0 < 2/3:
                    wpre "Ah{w=[wt1]}, {nm}[fnamehero]{/nm}!{w=[wt2]} I hope this afternoon finds you well."
                else:
                    wpre "Good afternoon, {nm}[fnamehero]{/nm}."
                hero "Good afternoon, {nm}[fnamewpre]{/nm}."

            elif gametimehour >= 18:
                if a_event_0 < 1/3:
                    wpre "Good evening, {nm}[fnamehero]{/nm}.{w=[wt2]} I hope you've had a fulfilling day."
                elif a_event_0 < 2/3:
                    wpre "Ah{w=[wt1]}, {nm}[fnamehero]{/nm}!{w=[wt2]} A pleasant evening to you."
                else:
                    wpre "Good evening, {nm}[fnamehero]{/nm}."
                hero "Good evening, {nm}[fnamewpre]{/nm}."

        elif wpre_love < 10: # wpre doesn't really likes hero
            if a_event_0 < 1/5:
                wpre "Oh, hello {nm}[fnamehero]{/nm}.{w=[wt2]} How may I be of assistance?"
            elif a_event_0 < 2/5:
                wpre "Greetings, {nm}[fnamehero]{/nm}.{w=[wt2]} Is there something you need help with?"
            elif a_event_0 < 3/5:
                wpre "Good day, {nm}[fnamehero]{/nm}.{w=[wt2]} I hope you're faring well."
            elif a_event_0 < 4/5:
                wpre "Oh, hello.{w=[wt2]} Is there something I can assist you with?"
            else:
                wpre "Yes?{w=[wt2]} How may I be of service?"

        elif wpre_love < 40: # wpre likes hero
            if a_event_0 < 1/6:
                wpre "It's a pleasure to see you, {nm}[fnamehero]{/nm}."
            elif a_event_0 < 2/6:
                wpre "Oh, {nm}[fnamehero]{/nm}!{w=[wt2]} I'm glad you're here."
            elif a_event_0 < 3/6:
                wpre "Oh!{w=[wt2]} Hello, {nm}[fnamehero]{/nm}.{w=[wt3]} How may I assist you?"
            elif a_event_0 < 4/6:
                wpre "Good day, {nm}[fnamehero]{/nm}.{w=[wt2]} I hope your studies are progressing well."
            elif a_event_0 < 5/6:
                wpre "Greetings, {nm}[fnamehero]{/nm}."
            else:
                wpre "Hello there!{w=[wt2]} Can I help you with anything?"

        elif wpre_love < 60: # wpre kinda loves hero
            if a_event_0 < 1/5:
                wpre "Ah, {nm}[fnamehero]{/nm}!{w=[wt2]} Your presence always brightens my day."
            elif a_event_0 < 2/5:
                wpre "{nm}[fnamehero]{/nm}!{w=[wt2]} I was just thinking about you."
            elif a_event_0 < 3/5:
                wpre "Oh my!{w=[wt2]} {nm}[fnamehero]{/nm}, you startled me.{w=[wt3]} But I'm glad you're here."
            elif a_event_0 < 4/5:
                wpre "Hello, {nm}[fnamehero]{/nm}!{w=[wt2]} I hope I'm not being too forward{w=[wt2]}, but I was hoping we might chat."
            else:
                wpre "{nm}[fnamehero]{/nm}!{w=[wt2]} What a delightful surprise.{w=[wt3]} How are you today?"

        else: # wpre loves hero
            if a_event_0 < 1/7:
                wpre "{nm}[fnamehero]{/nm}!{w=[wt3]} You know?{w=[wt2]} I was just thinking about you.{w=[wt2]} {gg}Hee-hee...{/gg}"
            elif a_event_0 < 2/7:
                wpre "Oh{w=[wt2]}, {nm}[fnamehero]{/nm}!{w=[wt2]} Your timing is impeccable.{w=[wt3]} I was hoping to see you."
            elif a_event_0 < 3/7:
                wpre "{nm}[fnamehero]{/nm}!{w=[wt2]} Your visit brings me such joy."
            elif a_event_0 < 4/7:
                wpre "{nm}[fnamehero]{/nm}?{w=[wt3]} I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm always happy to see you."                  
            elif a_event_0 < 5/7:
                wpre "{gg}Hee-hee...{/gg}{w=[wt2]} Oh{w=[wt1]}, pardon me!{w=[wt3]} I'm just pleased to see you, {nm}[fnamehero]{/nm}."
            elif a_event_0 < 6/7:
                wpre "{nm}[fnamehero]{/nm}!{w=[wt3]} I was just thinking about you."
            else:
                wpre "{nm}[fnamehero]{/nm}{w=[wt2]}, you always seem to appear when I'm thinking of you."

        jump wpre_interact

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wpre_interact:
    call hide_ui from _call_hide_ui_76
    if "interacting_hero" not in wpre_know:
        $ wpre_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wpre_interact_chat
        "Touch" if not is_specialevent:
            jump wpre_interact_touch
        "Hang out":
            jump wpre_interact_hangout
        "Give item" if not is_specialevent:
            jump wpre_interact_gift
        "Return":
            jump wpre_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wpre_interact_gift:
    $ a_item_8 = "wpre"
    $ a_item_9 = 0
    $ a_item_6 = "wpre_interact"
    call UI_give_Item from _call_UI_give_Item_11

label wpre_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wpre_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wpre_interact_touch:
    menu:
        "Hug":
            label wpre_interact_touch_hug:
                pass

            if not "Hug_Enough" in wpre_know:
                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.33:
                    scene bg_2 pink
                elif a_event_0 <= 0.66:
                    scene bg_2 yellow
                else:
                    scene bg_2 flowers

                $ wpre_know.append("Hug")
                $ a_event_0 = sum(1 for buceta in wpre_know if buceta =="Hug")
                $ wpre_fx = 1

                if perk_cha_sex >= 1:                
                    $ msg.msg(renpy.translate_string("{nm}[fnamewpre]{/nm}'s  lust {color=#32FF32}+")+str(2 * perk_cha_sex * lustadd_wpre)[:4])
                    $ wpre_lust += 2 * perk_cha_sex * lustadd_wpre

                if (wpre_inti >= char_inti_cap/2) and (wpre_love >= 50) and a_event_0 < 2:

                    show action_wpre_hug
                    with dissolve

                    $ add_stat("wpre", "love", 2/a_event_0)
                    $ add_stat("hero", "cha_sex", (2/a_event_0)/2)

                    pause

                else:

                    show action_wpre_hug
                    with dissolve

                    $ wpre_know.append("Hug_Enough")
                    $ add_stat("wpre", "love", 1/a_event_0)
                    $ add_stat("hero", "cha_sex", (1/a_event_0)/2)

                    $ a_event_0 = renpy.random.random()
                    if a_event_0 <= 0.33:
                        wpre "U{w=[wt1]}-uhh{w=[wt2]}, well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I{w=[wt1]}-I'm still not used to physical contact."
                    elif a_event_0 <= 0.66:
                        wpre "{aw}Ehhh!?{/aw}{w=[wt3]} S{w=[wt1]}-sorry{w=[wt2]}, don't know how to react to this so suddenly"
                    else:
                        wpre "O{w=[wt1]}-oh!{w=[wt4]} uh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} ..."

                call gamecheck from _call_gamecheck_15
                call hide_ui from _call_hide_ui_77
                call wpre_show from _call_wpre_show_2

                $ gametimemin += 10
                $ add_stat("wpre", "inti", 0.1)

            else:
                show HERO at CC_average
                pause(0.2)
                show WPRE at RR_average

                $ wpre_mood = "O2"
                wpre "Please don't.{w=[wt2]}{nw}"

                $ hero_mood = "O1"
                show HERO at Stay

                wpre "Please don't.{fast}{w=[wt3]}{nw}"

                show HERO at LC_slow

                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.33:
                    wpre "Please don't.{fast} I'm still not used to it.{w=[wt2]} My apologies.{nw}"
                elif a_event_0 <= 0.66:
                    wpre "Please don't.{fast} My apologies.{w=[wt2]} I still don't feel so comfortable with physical contact.{w=[wt2]} I hope you understand.{nw}"
                else:
                    wpre "Please don't.{fast} Sorry{w=[wt2]}, I need a little break.{w=[wt2]} Physical contact is still too much for me to handle.{nw}"

                show WPRE at RC_slow

                if a_event_0 <= 0.33:
                    wpre "Please don't. I'm still not used to it.{w=[wt2]} My apologies.{fast}"
                elif a_event_0 <= 0.66:
                    wpre "Please don't. My apologies.{w=[wt2]} I still don't feel so comfortable with physical contact.{w=[wt2]} I hope you understand.{fast}"
                else:
                    wpre "Please don't. Sorry{w=[wt2]}, I need a little break.{w=[wt2]} Physical contact is still too much for me to handle.{fast}"
                jump wpre_interact_check

        "Return":
            jump wpre_interact

    jump wpre_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wpre_interact_hangout:
    menu:
        "Return":
            jump wpre_interact

    $ gametimemin += 30
    jump wpre_interact_check

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
label wpre_interact_chat:
    menu:
        "Ask how she is" if not "Talk_How" in wpre_know:
            $ hero_mood = "A1"
            $ a_event_0 = renpy.random.random()
            hero "How are you doing today, {nm}[fnamewpre]{/nm}?"
            # ----------------------------------------------------------------------------------------------------
            # Asking in the morning
            # ----------------------------------------------------------------------------------------------------
            if gametimehour >= 8 and gametimehour < 12:

                # Well rested
                if wpre_los < 10:
                    if renpy.random.random() < 0.5 and wpre_inti >= char_inti_cap/2:
                        $ wpre_mood = "A1"
                        wpre "Actually{w=[wt2]}, I'm quite excited!{w=[wt2]} Thank you for asking!{w=[wt3]} I've been writting in my free time{w=[wt2]}, that's something that makes me feel alive."
                    elif a_event_0 < 1/4:
                        $ wpre_mood = "A1"
                        wpre "I'm doing fine!{w=[wt1]} {gg}Hee-hee...{/gg}{w=[wt3]} Thank you for asking, {nm}[fnamehero]{/nm}."
                    elif a_event_0 < 2/4:
                        $ wpre_mood = "A1"
                        wpre "I'm doing well!{w=[wt3]} Thank you for asking, {nm}[fnamehero]{/nm}.{w=[wt3]} I woke up early and had time to review my notes before classes."
                    elif a_event_0 < 3/4:
                        $ wpre_mood = "A1"
                        wpre "I'm feeling quite refreshed today, {nm}[fnamehero]{/nm}.{w=[wt2]} Thank you for asking!{w=[wt3]} I managed to get a good night's sleep{w=[wt2]}, which is always beneficial."
                    else:
                        $ wpre_mood = "A1"
                        wpre "I'm doing fine{w=[wt2]}, thank you.{w=[wt3]} I've already completed my morning tasks and I'm ready for the day ahead."

                # Getting tired
                elif wpre_los < 50:
                    if renpy.random.random() < 0.5 and wpre_inti >= char_inti_cap/2:
                        $ wpre_mood = "A2"
                        wpre "Well{w=[wt2]}, I’m a little full of things to do{w=[wt2]}, but doing fine.{w=[wt1]} {gg}Hee-hee...{/gg}{w=[wt3]} Thank you for asking!"
                    elif a_event_0 < 1/4:
                        $ wpre_mood = "A1"
                        wpre "I'm doing fine{w=[wt2]}, thank you{w=[wt2]}, {nm}[fnamehero]{/nm}!"
                    elif a_event_0 < 2/4:
                        $ wpre_mood = "A1"
                        wpre "I'm doing alright{w=[wt2]}, thank you{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} Just a bit busy{w=[wt1]} {gg}Hee-hee...{/gg}"
                    elif a_event_0 < 3/4:
                        $ wpre_mood = "A1"
                        wpre "I'm fine{w=[wt2]}, thank you for your concern.{w=[wt3]} There's quite a lot to do{w=[wt2]}, but I'm staying on top of things."
                    else:
                        $ wpre_mood = "A1"
                        wpre "I'm doing well{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} Thank you."

                # Tired
                elif wpre_los < 90:
                    if renpy.random.random() < 0.5 and wpre_inti >= char_inti_cap/2:
                        call wpre_interact_chat_burnout_1 from _call_wpre_interact_chat_burnout_1
                    elif a_event_0 < 2/4:
                        $ wpre_mood = "O1"
                        wpre "I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} managing{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} There's a lot on my plate{w=[wt2]}, but I'm doing my best to keep up."
                    elif a_event_0 < 3/4:
                        $ wpre_mood = "O1"
                        wpre "I appreciate you asking{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} It's been quite challenging lately{w=[wt2]}, but I'm persevering."
                    else:
                        $ wpre_mood = "O1"
                        wpre "Thank you for your concern{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} I must admit{w=[wt2]}, I'm feeling rather tired{w=[wt2]}, but I'll continue to do my best."

                # On the verge of collapse
                else:
                    if wpre_inti >= char_inti_cap/2:
                        call wpre_interact_chat_burnout_2 from _call_wpre_interact_chat_burnout_2
                    elif a_event_0 < 1/4:
                        $ wpre_mood = "O1"
                        wpre "I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                        $ wpre_mood = "A2"
                        wpre "I'm...{fast} fine{w=[wt2]} Thank you."
                    elif a_event_0 < 2/4:
                        $ wpre_mood = "O1"
                        wpre "I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                        $ wpre_mood = "A2"
                        wpre "I'm...{fast} fine{w=[wt1]} {gg}Hee-hee...{/gg}{nw}"
                    elif a_event_0 < 3/4:
                        $ wpre_mood = "O1"
                        wpre "Thank you for asking{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                        $ wpre_mood = "A2"
                        wpre "Thank you for asking{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} I'm...{fast} fine."
                    else:
                        $ wpre_mood = "O1"
                        wpre "I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                        $ wpre_mood = "A2"
                        wpre "I'm...{fast} doing okay{w=[wt1]}, Thank you!"

            # ----------------------------------------------------------------------------------------------------
            # Asking at any other time
            # ----------------------------------------------------------------------------------------------------
            else:
                # Well rested
                if wpre_los < 10:
                    if renpy.random.random() < 0.5 and wpre_inti >= char_inti_cap/2:
                        $ wpre_mood = "A1"
                        wpre "I'm doing quite well{w=[wt2]}, thank you for asking.{w=[wt3]} I've been making progress on a personal writing project{w=[wt2]}, which has been very fulfilling."
                    elif a_event_0 < 1/3:
                        $ wpre_mood = "A1"
                        wpre "I'm doing fine{w=[wt2]}, thank you, {nm}[fnamehero]{/nm}.{w=[wt3]} I hope you're having a good day as well."
                    elif a_event_0 < 2/3:
                        $ wpre_mood = "A1"
                        wpre "I'm doing well{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} I've managed to stay on top of my responsibilities today."
                    else:
                        $ wpre_mood = "A1"
                        wpre "I'm quite alright{w=[wt2]}, thank you for asking.{w=[wt3]} It's been a productive day so far."

                # Getting tired
                elif wpre_los < 50:
                    if renpy.random.random() < 0.5 and wpre_inti >= char_inti_cap/2:
                        $ wpre_mood = "A2"
                        wpre "I'm managing well{w=[wt2]}, thank you."
                    elif a_event_0 < 1/3:
                        $ wpre_mood = "A2"
                        wpre "I'm doing fine{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} There's quite a lot to do{w=[wt2]}, but I'm handling it."
                    elif a_event_0 < 2/3:
                        $ wpre_mood = "A2"
                        wpre "I'm alright{w=[wt2]}, thank you for asking.{w=[wt3]} Just a bit busy lately{w=[wt1]}, {gg}Hee-hee...{/gg}"
                    else:
                        $ wpre_mood = "A1"
                        wpre "I'm doing well enough{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} Thank you for your concern."

                # Tired
                elif wpre_los < 90:
                    if wpre_inti >= char_inti_cap/2:
                        call wpre_interact_chat_burnout_1 from _call_wpre_interact_chat_burnout_1_1
                    elif a_event_0 < 1/4:
                        $ wpre_mood = "A2"
                        wpre "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} doing well{w=[wt2]}, thank you."
                    elif a_event_0 < 2/4:
                        $ wpre_mood = "A2"
                        wpre "I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} fine{w=[wt2]}, thank you for asking."
                    elif a_event_0 < 3/4:
                        $ wpre_mood = "A2"
                        wpre "I appreciate your concern, {nm}[fnamehero]{/nm}.{w=[wt3]} I{w=[wt2]}, Well{w=[wt2]}, I'm fine. "
                    else:
                        $ wpre_mood = "A2"
                        wpre "Thank you for asking{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} I'm doing fine."

                # On the verge of collapse
                else:
                    if wpre_inti >= char_inti_cap/2:
                        call wpre_interact_chat_burnout_2 from _call_wpre_interact_chat_burnout_2_1
                    elif a_event_0 < 1/4:
                        $ wpre_mood = "O1"
                        wpre "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                        $ wpre_mood = "A2"
                        wpre "I'm...{fast} managing{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} There's a lot to do{w=[wt2]}, but please don't worry about me.{w=[wt3]} How can I assist you today?"
                    elif a_event_0 < 2/4:
                        $ wpre_mood = "O1"
                        wpre "I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                        $ wpre_mood = "A2"
                        wpre "I'm...{fast} fine{w=[wt2]}, thank you for asking{w=[wt2]}, {nm}[fnamehero]{/nm}."
                    elif a_event_0 < 3/4:
                        $ wpre_mood = "O1"
                        wpre "Thank you for your concern{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                        $ wpre_mood = "A2"
                        wpre "Thank you for your concern{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} I'm...{fast} managing."
                    else:
                        $ wpre_mood = "O1"
                        wpre "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
                        $ wpre_mood = "A2"
                        wpre "I'm...{fast} doing my best{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} Is there anything I can help you with?"

            $ wpre_know.append("Talk")
            $ wpre_know.append("Talk_How")
            $ add_stat("wpre", "love", 0.5)
            $ add_stat("hero", "cha_soc", 0.5)

        "Return":
            jump wpre_interact

    $ add_stat("wpre", "inti", 0.2)
    $ gametimemin += 20
    jump wpre_interact_check

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_wpre:
    $ wpre_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wpre_inti*0.02) and not any(get_id.startswith("HERO_Dated") for get_id in wpre_know):

        wpre "If I may ask, {nm}[fnamehero]{/nm}{w=[wt2]}, have you ever been in a romantic relationship before?{w=[wt2]} I apologize if this question is too personal."

        $ hero_fx = 1
        $ hero_mood = "O1"

        menu:
            wpre "If I may ask, {nm}[fnamehero]{/nm}... Have you ever been in a romantic relationship before? I apologize if this question is too personal.{fast}"
            
            "Deny":
                $ wpre_know.append("HERO_Dated_N")
                $ msg.msg(renpy.translate_string("{nm}[fnamewpre]{/nm} knows you a little more"))
                $ add_stat("wpre", "inti", 0.5)
                hero "N{w=[wt1]}-No{w=[wt2]}, I've never dated before."
                $ wpre_mood = "A1"
                wpre "I see.{w=[wt2]} Many people focus on other aspects of life before entering into relationships.{w=[wt2]} I totally understand you."

            "Confirm":
                $ wpre_know.append("HERO_Dated_Y")
                $ msg.msg(renpy.translate_string("{nm}[fnamewpre]{/nm} knows you a little more"))
                $ add_stat("wpre", "inti", 0.5)
                hero "W{w=[wt1]}-well{w=[wt2]}, y{w=[wt1]}-yes{w=[wt2]}, I kinda dated a girl once."
                $ wpre_mood = "A1"
                wpre "I see.{w=[wt2]} I hope it was a positive experience for you.{w=[wt3]} Relationships seems to be something quite complicated, right?"

    # ----------------------------------------------------------------------------------------------------
    # Ask HERO's girl preference
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wpre_inti*0.02) and sum(1 for get_id in wpre_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wpre_know if get_id.startswith("HERO_N_Girl")) < 4:
        wpre "Pardon me for asking{w=[wt2]}, but I'm curious{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} What qualities do you find appealing in a potential romantic partner?{nw}"

        menu:
            wpre "Pardon me for asking, but I'm curious... What qualities do you find appealing in a potential romantic partner?{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in wpre_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in wpre_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in wpre_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in wpre_know if "Personality_" in get_id)

                # Appearance Likes(Y)/Dislikes(N)
                $ a_event_1 = wpre_know
                $ a_event_3 = "initiative_wpre_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_10

                # Store the answer if one was given
                if _return:
                    $ wpre_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg(renpy.translate_string("{nm}[fnamewpre]{/nm} knows you a little more"))
                $ add_stat("wpre", "inti", 0.5)

                if _return in ["Personality_9", "Personality_8", "Personality_3", "Breast_2", "Breast_3", "HairSize_4", "HairSize_5"]: # Match - intelligent, chaste, kind, medium/big breasts, medium-long hair
                    $ add_stat("wpre", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ wpre_mood = "A3"
                    wpre "Is that so?{w=[wt3]} I mean{w=[wt2]}, t{w=[wt1]}-thank you for answering!{w=[wt3]} I'm glad for know you a little more!{w=[wt2]} {gg}Hee-hee...{/gg}"

                elif _return in ["Personality_7", "Personality_10", "Breast_4", "Breast_5", "HairSize_0", "HairSize_1"]: # Opposite match - pervert, stupid, huge breasts, bald/short hair
                    $ add_stat("wpre", "bonus", -10)
                    $ wpre_mood = "O1"
                    wpre "I see{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} W{w=[wt1]}-well{w=[wt2]}, I'm s{w=[wt1]}-sorry for asking."

                else: # Others
                    $ wpre_mood = "A1"
                    wpre "I see.{w=[wt2]} That's quite interesting.{w=[wt3]} Thank you for answering."

            "Don't choose":
                jump initiative_wpre_return

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:
        wpre "I apologize.{w=[wt2]} I seem to have lost my train of thought.{w=[wt3]} Was there something you wanted to discuss?"
        jump wpre_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("wpre", "inti", 0.20)
    jump wpre_interact_check

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wpre_return:

    call hero_n_answer from _call_hero_n_answer_8

    wpre "That's perfectly fine!{w=[wt2]} Please don't feel pressured to answer if you're not comfortable."
    jump wpre_interact

# ----------------------------------------------------------------------------------------------------
# Answer Tired
# ----------------------------------------------------------------------------------------------------
label wpre_interact_chat_burnout_1:
    $ add_stat("wpre", "inti", 0.5)
    $ wpre_mood = "O2"
    wpre "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm struggling a bit{w=[wt2]}, to be honest.{w=[wt3]} But please don't worry about me{w=[wt2]}, I'll find a way to manage everything."
    hero "A{w=[wt1]}-are you sure?"
    wpre "Oh my{w=[wt2]} I'm really sorry for making you worry, {nm}[fnamehero]{/nm}.{w=[wt3]} I’m just complaining too much{w=[wt1]} {gg}Hee-hee...{/gg}{w=[wt3]} Please don't worry too much about that, okay?"
    hero "Well{w=[wt2]}, if you say so..."
    wpre "Sure!{w=[wt2]} Thank you for your concern."
    return

# ----------------------------------------------------------------------------------------------------
# Answer Very Tired
# ----------------------------------------------------------------------------------------------------
label wpre_interact_chat_burnout_2:
    $ add_stat("wpre", "inti", 0.5)
    $ wpre_mood = "O2"
    if renpy.random.random() < 0.5:
        wpre "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I don't know how much longer I can keep this up, {nm}[fnamehero]{/nm}.{w=[wt3]} I mean{w=[wt2]}, I'll manage to.{w=[wt3]} Don't worry about that.{w=[wt3]} T{w=[wt1]}-thank you for your concern."
    elif renpy.random.random() < 0.5:
        wpre "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Sorry, {nm}[fnamehero]{/nm}.{w=[wt3]} I don't know."
    else:
        wpre "Well, I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."
    hero "Wow{w=[wt2]}, You look very tired!{w=[wt3]} I think you better have a good rest!"
    $ wpre_mood = "A2"
    wpre "I can't.{w=[wt3]} I still have important things to finish.{w=[wt3]} I made a commitment to do this.{w=[wt3]} I can’t be selfish right now."
    hero "Wait{w=[wt2]}, are you serious?{w=[wt3]} Looks like you’re about to pass out any minute!"
    wpre "{gg}Hee-hee{/gg}{w=[wt2]} I’m glad you care about me.{w=[wt2]} It means so much.{w=[wt3]} Thank you.{w=[wt4]} I promise I’ll rest as soon as I finish everything, okay?{w=[wt3]} Just please don't worry anymore."
    mind "(She’s on the verge of collapse.{w=[wt3]} I need to take charge of some of her activities to take some of her burden off.)"
    return
