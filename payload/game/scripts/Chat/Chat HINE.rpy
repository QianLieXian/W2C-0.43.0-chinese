# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label hine_show:

    if hine_love <= -20:
        $ hine_mood = "O2"
    elif hine_love < 0:
        $ hine_mood = "A2"
    elif hine_love >= 0:
        $ hine_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust

    show HINE at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label hine_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamehine][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("hine")))))

    if Get_ActivityName("hine") in ["at class"]:
        jump show_ui

    else:
        return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label hine_interact_end:
    if "interacting_hero" in hine_know:
        $ hine_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label hine_interact_start:
    call hide_ui from _call_hide_ui
    call hine_show_activity from _call_hine_show_activity
    $ hine_inti = min(char_inti_cap, hine_inti)

    $ msg.msg(renpy.translate_string("Content Unavailable"))
    jump show_ui

    call hide_ui from _call_hide_ui_1
    call hine_show from _call_hine_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label hine_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if hero_map == hine_map:
        pass

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label hine_interact_check:
    # Save current outfit before any updates
    $ hine_wear_keep = hine_wear

    call gametime from _call_gametime
    call hide_ui from _call_hide_ui_2

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if hine_wear != hine_wear_keep:
        $ hine_wear = hine_wear_keep

    call hine_show from _call_hine_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    if gametimehour >= 18: # Went home
        hine "Sorry bro{w=[wt2]}, I have to go now. Good bye!"
        $ hero_fx = 0
        jump hine_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Get_MapName("hine", "at class"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "hine"):
            $ hine_mood = "O1"
            hine "...Class.{w=[wt4]} Tch{w=[wt2]}, whatever."

            $ hero_mood = "A1"
            hero "You heading to class?"
            
            $ hine_mood = "O1"
            hine "Not like I have a choice{w=[wt2]}, normie.{w=[wt4]} Parents would kill me if I{w=[wt2]}, you know{w=[wt2]}, actually skipped.{w=[wt4]} Not that I care about their opinion or anything{w=[wt2]}, it's just{w=[wt1]}-{nw}"
            
            show HINE at RC
            show HINE at OR_slow
            show HERO at OR_slow
            hine "Not like I have a choice{w=[wt2]}, normie.{w=[wt4]} Parents would kill me if I{w=[wt2]}, you know{w=[wt2]}, actually skipped.{w=[wt4]} Not that I care about their opinion or anything{w=[wt2]}, it's just{w=[wt1]}-{fast}{w=[wt2]} {bt}...Whatever.{/bt}"

            jump hine_interact_end

        else:
            $ hine_mood = "O1"
            hine "...Tch.{w=[wt4]} Class.{w=[wt4]} Great.{w=[wt3]} Just{w=[wt2]}, perfect."

            if Get_MapName("hine", "at class") == Get_MapName(None, "school", "class_1b"):
                menu:
                    "Go together":
                        $ hero_mood = "A1"
                        hero "Let's go!"
                        
                        $ hine_mood = "O2"
                        hine "Tch{w=[wt2]}, yeah."
                        
                        scene bg_0
                        with dissolve

                        $ hero_map = hine_map
                        call gametime from _call_gametime_1
                        call check_playermap from _call_check_playermap
                        call hide_ui from _call_hide_ui_3
                        show HINE at RC
                        show HERO at LC
                        with dissolve
                        
                        $ hine_mood = "O1"
                        hine "So{w=[wt2]}, see you."

                        jump hine_interact_end
                        
                    "Let him go":
                        pass

            $ hero_mood = "A1"
            hero "See you!"
            
            $ hine_mood = "O1"
            hine "...Yeah.{w=[wt3]} Whatever."
            
            show HINE at RC
            show HINE at OR_slow
            pause(1.5)

        jump hine_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in hine_know:
        $ a_event_0 = renpy.random.random()

        if renpy.random.random() < (0.5+(hine_love*0.003)):
            jump initiative_hine

        # Doesn't really like HERO
        elif hine_love <= 0:
            if a_event_0 < 1/3:
                $ hine_mood = "A2"
                hine "Oh{w=[wt2]}, it's you, man."
            elif a_event_0 < 2/3:
                $ hine_mood = "A2"
                hine "H{w=[wt1]}-hi."
            else:
                $ hine_mood = "O1"
                hine "Uh{w=[wt2]}, yeah.{w=[wt2]} What is it?"

        # Have Item: Smartphone
        elif renpy.random.random() > 0.25 and "HINE_Item_Phone" in hine_know:
            if a_event_0 < 1/3:
                $ hine_mood = "A1"
                hine "By the way{w=[wt2]}, I just discovered this awesome app that adds jiggle physics to any photo!{w=[wt3]} It's for{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} scientific research, of course!"
                hero "I don't think that's what they mean by 'citizen science', {nm}[fnamehine]{/nm}."
            elif a_event_0 < 2/3:
                $ hine_mood = "A4"
                hine "By the way{w=[wt2]}, life's great when you have a smartphone!{w=[wt3]} I'm working on a revolutionary filter that can detect and enhance{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {bt}specific areas of interest{/bt} in photos!"
                hero "I'm pretty sure that's illegal, {nm}[fnamehine]{/nm}."
            else:
                $ hine_mood = "A3"
                hine "I remembered something{w=[wt2]}, check this out!{w=[wt3]} I've set up my phone to make a 'boing' sound every time I take a picture.{w=[wt3]} It really captures the essence of the moment, you know?"
                hero "I don't even want to know what kind of pictures you're taking..."

        # Have Item: Binoculars
        elif renpy.random.random() > 0.25 and "HINE_Item_Binocular" in hine_know:
            if a_event_0 < 1/2:
                $ hine_mood = "A3"
                hine "These binoculars are a game-changer!{w=[wt3]} I can now appreciate the {bt}fine details{/bt} of{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} architecture from a safe distance!"
                hero "I doubt you're looking at buildings, {nm}[fnamehine]{/nm}."
            else:
                $ hine_mood = "A1"
                hine "Dude{w=[wt2]}, I've been tracking the migratory patterns of{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {bt}local wildlife{/bt}.{w=[wt3]} It seems that they tend to gather near the girls' locker room."
                hero "That's not wildlife{w=[wt2]}, that's an invasion of privacy!"

        # Likes HERO
        elif hine_love < 50:
            $ hine_mood = "A1"
            if a_event_0 < 1/3:
                hine "Anyway{w=[wt2]}, it's good to talk to someone who understands you."
            elif a_event_0 < 2/3:
                hine "You know{w=[wt2]}, stopping to think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} you really seem lucky to be around so many pretty girls."
            else:
                hine "You know, we should hang out more. I could teach you the art of{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} people-watching!"

        # Trully admires HERO
        else:
            $ hine_mood = "A1"
            if a_event_0 < 1/5:
                hine "You might as well introduce me to some hot friends."
            elif a_event_0 < 2/5:
                hine "Anyway{w=[wt2]}, if you know of any party with hot girls{w=[wt1]}, do not forget to call me."
            elif a_event_0 < 3/5:
                hine "Stopping to think{w=[wt2]}, sometimes I think the girls' swim uniform could be a little smaller and with more transparent fabric.{w=[wt3]} I think we should make a petition for that."
            elif a_event_0 < 4/5:
                hine "Anyway{w=[wt2]}, know we are brothers man.{w=[wt3]} Count on me for anything!"
            else:
                hine "Man{w=[wt2]}, life is good when you have a wingman who gets you!{w=[wt3]} We're gonna conquer this school{w=[wt2]}, one{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} heart at a time!"

    # ----------------------------------------------------------------------------------------------------
    # HINE is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("hine") in ["eating"]:
        "{nm}[fnamehine]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamehine]{/nm} is spending time at a courtyard table{fast}"
            "Join him":
                scene bg_0
                with Dissolve(1)
                pause(0.5)

                while Get_ActivityName("hine") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait
                call gametime from _call_gametime_2
                
                jump hine_interact_start

            "Return":
                jump hine_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_0 = renpy.random.random()

        # Doesn't really like HERO
        if hine_love <= 0:
            if a_event_0 < 1/4:
                $ hine_mood = "A2"
                hine "Oh{w=[wt2]}, it's you, man."
            elif a_event_0 < 2/4:
                $ hine_mood = "A2"
                hine "H{w=[wt1]}-hi."
            elif a_event_0 < 3/4:
                $ hine_mood = "O1"
                hine "Uh{w=[wt2]}, what do you want?"
            else:
                $ hine_mood = "A2"
                hine "Oh{w=[wt2]}, hey.{w=[wt3]} Didn't see you there."

        # Likes HERO
        elif hine_love < 50:
            if a_event_0 < 1/4:
                $ hine_mood = "A1"
                hine "Hey, dude!"
            elif a_event_0 < 2/4:
                $ hine_mood = "A1"
                hine "Hey, man!{w=[wt3]}  Let's talk!"
            elif a_event_0 < 3/4:
                $ hine_mood = "A3"
                hine "Yo!{w=[wt2]} Perfect timing{w=[wt2]}, I was just about to start my{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} observations!"
            else:
                $ hine_mood = "A1"
                hine "What's up, man?{w=[wt3]} Seen anything interesting lately?{w=[wt1]} {gg}Hehehe...{/gg}"

        # Trully admires HERO
        else:
            if a_event_0 < 1/4:
                $ hine_mood = "A1"
                hine "Nice to see you, bro!"
            elif a_event_0 < 2/4:
                $ hine_mood = "A1"
                hine "Heey, man!"
            elif a_event_0 < 3/4:
                $ hine_mood = "A3"
                hine "My main man!{w=[wt2]} Ready for another day of{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} research?"
            else:
                $ hine_mood = "A4"
                hine "Bro!{w=[wt2]} You're just in time.{w=[wt3]} I was about to call you to my daily{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} aesthetic appreciation session!"

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label hine_interact:
    call hide_ui from _call_hide_ui_4
    if "interacting_hero" not in hine_know:
        $ hine_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump hine_interact_chat
        "Touch" if not is_specialevent:
            jump hine_interact_touch
        "Hang out":
            jump hine_interact_hangout
        #"Give item" if not is_specialevent:
            #jump hine_interact_gift
        "Return":
            jump hine_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label hine_interact_gift:
    $ a_item_8 = "hine"
    $ a_item_9 = 0
    $ a_item_6 = "hine_interact"
    call UI_give_Item from _call_UI_give_Item

label hine_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump hine_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label hine_interact_touch:
    menu:
        "Hug":
            label hine_interact_touch_hug:
                pass

            $ hine_know.append("Hug")
            $ a_event_0 = sum(1 for buceta in hine_know if buceta =="Hug")
            $ hine_fx = 1

            $ a_event_1 = renpy.random.random()
            scene bg_2 yellow

            if a_event_0 == 1:

                show action_hine_hug 1a
                with dissolve

                show action_hine_hug 1b

                $ add_stat("hine", "love", 2/a_event_0)
                $ add_stat("hero", "cha_sex", 2/a_event_0)

                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.25:
                    hine "You're the best, bro!"
                elif a_event_0 <= 0.50:
                    hine "Man{w=[wt2]}, you're like the brother I never had!"
                elif a_event_0 <= 0.75:
                    hine "Nothing beat us!"
                else:
                    hine "Hey!{w=[wt2]} {gg}He-he...{/gg}"

                show action_hine_hug 1a with None

                call gamecheck from _call_gamecheck
                call hide_ui from _call_hide_ui_5
                call hine_show from _call_hine_show_2
                $ gametimemin += 10
                $ add_stat("hine", "love", 0.1)

            else:

                show action_hine_hug 2a
                with dissolve

                show action_hine_hug 2b

                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.25:
                    hine "Hey, bro, What's up?"
                elif a_event_0 <= 0.50:
                    hine "Bro code section 5, paragraph 3: {i}One bro hug per day, unless someone died or your team won the championship{/i}."
                elif a_event_0 <= 0.75:
                    hine "I support your life choices and all, but my heart belongs to the curves of the feminine form. Exclusively."
                else:
                    show action_hine_hug 2a
                    hine "???"

                show action_hine_hug 2a with None

        "Return":
            jump hine_interact
    
    jump hine_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label hine_interact_hangout:
    menu:
        "Return":
            jump hine_interact

    $ gametimemin += 30
    jump hine_interact_check

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
label hine_interact_chat:
    menu:
        "Ask how he is" if not "Talk_How" in hine_know:
            $ hero_mood = "A1"
            $ a_event_0 = renpy.random.random()
            # ----------------------------------------------------------------------------------------------------
            # Asking in the morning
            # ----------------------------------------------------------------------------------------------------
            if gametimehour >= 8 and gametimehour < 12:

                hero "How are you doing today, {nm}[fnamehine]{/nm}?"

                # ----------------------------------------------------------------------------------------------------
                # Common
                # ----------------------------------------------------------------------------------------------------
                if a_event_0 < 1/8:
                    $ hine_mood = "O1"
                    hine "Well{w=[wt2]}, not that good so far.{w=[wt3]} I haven't been able to capture any nice scenes.{nw}"
                    $ hine_mood = "A1"
                    hine "Well, not that good so far. I haven't been able to capture any nice scenes.{fast} But don't worry, bro!{w=[wt2]} The day is just beginning!"
                    $ hero_mood = "O1"
                    hero "W{w=[wt1]}-well, I'm not really worried about that."

                elif a_event_0 < 2/8:
                    $ hine_mood = "O1"
                    hine "Man{w=[wt2]}, I overslept and missed the morning jog of the girls' in my neighborhood.{w=[wt3]} What a waste of prime viewing time!"
                    $ hero_mood = "O1"
                    hero "Please don't go to jail for doing anything creepy."

                elif a_event_0 < 3/8:
                    $ hine_mood = "A1"
                    hine "Oh{w=[wt2]}, I woke up kinda inspired, bro{w=[wt2]}, I had the wildest dream{w=[wt2]}, where I was surrounded by bouncing{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {bt}marshmallows{/bt}!{w=[wt3]} Yeah, marshmallows!"
                    hero "Right{w=[wt2]}, 'marshmallows'.{w=[wt3]} Got it."

                elif a_event_0 < 4/8:
                    $ hine_mood = "A1"
                    hine "Feeling inspired!{w=[wt3]} I'm writing a thesis on the correlation between skirt length and wind speed.{w=[wt3]} It's for science, you know!"
                    hero "I'm pretty sure that's not how science works."

                elif a_event_0 < 5/8:
                    $ hine_mood = "A3"
                    hine "Amazing!{w=[wt3]} Life is beautiful, my friend!{w=[wt3]} Every morning is a new opportunity to appreciate the{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {bt}wonders of nature{/bt}!"
                    hero "Why do I get the feeling we're not talking about actual nature?"

                elif a_event_0 < 6/8:
                    $ hine_mood = "A1"
                    hine "I'm doing alright.{w=[wt2]} The view's been{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} satisfactory so far{w=[wt2]}, if you know what I mean.{w=[wt1]} {gg}Hehehe...{/gg}"
                    hero "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} think I get the picture."

                elif a_event_0 < 7/8:
                    $ hine_mood = "A3"
                    hine "{bt}My man!{/bt}{w=[wt3]} The day is looking beautiful{w=[wt1]}, almost as beautiful as the ladies walking by.{w=[wt3]} Speaking of which{w=[wt2]}, did you see that girl who just passed?{w=[wt3]} The aerodynamics of that skirt were fascinating!"
                    hero "Uh{w=[wt2]}, I didn't really notice..."
                    hine "You gotta keep your eyes open, buddy!{w=[wt3]} There's beauty all around us!"
                else:
                    $ hine_mood = "A3"
                    hine "Fantastic, bro!{w=[wt3]} I've been working on my X-ray vision.{w=[wt3]} Turns out, it's all about the power of imagination! {gg}Hehehe...{/gg}"
                    hero "That's not a real thing, {nm}[fnamehine]{/nm}. And it's creepy."

            # ----------------------------------------------------------------------------------------------------
            # Asking in the afternoon
            # ----------------------------------------------------------------------------------------------------
            elif gametimehour >= 12 and gametimehour < 18:

                hero "How's your day going, {nm}[fnamehine]{/nm}?"

                # ----------------------------------------------------------------------------------------------------
                # HINE doesn't have a smartphone
                # ----------------------------------------------------------------------------------------------------
                if renpy.random.random() > 0.5 and not "HINE_Item_Phone" in hine_know:
                    if a_event_0 < 1/2:
                        $ hine_mood = "O1"
                        hine "I'm in a mixture of happiness and sadness{w=[wt1]}, bro.{w=[wt2]} I got the pleasure of witnessing a dream view.{w=[wt3]} It was the perfect angle{w=[wt2]}, the perfect position{w=[wt2]}, and worst of all{w=[wt2]}, the wind was so constant that the viewing time was also perfect!"
                        hero "Wait wait wait...{w=[wt4]} If everything was so perfect{w=[wt2]}, then what was the problem?"
                        hine "Hm?{w=[wt2]} Isn't it obvious?{w=[wt3]} If I had a smartphone I could have capture it.{w=[wt3]} Now it only exists in my memory."
                        hero "I knew I shouldn't have asked."

                    else:
                        $ hine_mood = "A2"
                        hine "Thanks for asking, man.{w=[wt3]} Well{w=[wt1]}, I've been better.{w=[wt3]} You know{w=[wt2]}, still can't raise enough money to buy a new phone.{w=[wt3]} My parents have already told me that they will not buy a new one and that I should get a job."
                        $ hero_mood = "A2"
                        hero "I see.{w=[wt3]} I hope you get that soon."

                # ----------------------------------------------------------------------------------------------------
                # HINE has smartphone
                # ----------------------------------------------------------------------------------------------------
                elif renpy.random.random() > 0.5 and "HINE_Item_Phone" in hine_know:
                    if a_event_0 < 1/4:
                        $ hine_mood = "A3"
                        hine "Fine, man!{w=[wt3]} Been practicing my photography skills!{w=[wt3]} I've mastered the art of the quick-draw snapshot.{w=[wt3]} {bt}Stealth mode activated!{/bt}"
                        hero "Maybe find a less creepy hobby?"
                    elif a_event_0 < 2/4:
                        $ hine_mood = "A1"
                        hine "Bro{w=[wt1]}, I just installed a dating app that can match you based on {bt}body type preferences{/bt}!{w=[wt3]} That doesn't seem awesome?{w=[wt3]} Imagine me going out with some hot girl I met in this app!"
                        hero "Cool!{w=[wt2]} So you got to meet someone?"
                        $ hine_mood = "O1"
                        hine "{aw}Ehh...?{/aw}{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt3]}N{w=[wt1]}-no{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Nobody's liked me so far."
                    elif a_event_0 < 3/4:
                        $ hine_mood = "A3"
                        hine "Just discovered some cool slow-motion video effects on my phone!{w=[wt3]} This changes {bt}everything{/bt}! {gg}Hehehe...{/gg}"
                        hero "Please use that responsibly{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} On second thought{w=[wt2]}, don't use it at all."
                    else:
                        $ hine_mood = "A1"
                        hine "It's going pretty well!{w=[wt3]} I've documented a sightings of an almost side-boob!"
                        hero "You really shouldn't be{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} documenting that stuff, you know."

                # ----------------------------------------------------------------------------------------------------
                # HINE has binoculars
                # ----------------------------------------------------------------------------------------------------
                elif renpy.random.random() > 0.5 and "HINE_Item_Binocular" in hine_know:
                    if a_event_0 < 1/3:
                        $ hine_mood = "O1"
                        hine "{pa}Disaster struck!{/pa}{w=[wt3]} I realized I didn't bring my binoculars today.{w=[wt3]} Now how am I supposed to{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} birdwatch?"
                        $ hero_mood = "O1"
                        hero "Something tells me you didn't want to see 'birds'"
                    elif a_event_0 < 2/3:
                        $ hine_mood = "A3"
                        hine "Awesome, my man!{w=[wt3]} I could see{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {bt}stars{/bt} even in broad daylight!"
                        hero "I have a feeling those 'stars' are wearing skirts, {nm}[fnamehine]{/nm}."
                    else:
                        $ hine_mood = "A4"
                        hine "Amazing!{w=[wt3]} I've just discovered a new species!{w=[wt3]} I call it the '{bt}Bountiful Boobus Maximus{/bt}'!{w=[wt3]} Last spotted near the sport court field!"
                        hero "That's it{w=[wt2]}, I'm confiscating those binoculars."

                # ----------------------------------------------------------------------------------------------------
                # Common
                # ----------------------------------------------------------------------------------------------------
                else:
                    if a_event_0 < 1/6:
                        $ hine_mood = "A1"
                        hine "Fine, man!{w=[wt3]} Just had a brilliant idea!{w=[wt3]} I'm going to petition for 'Casual Friday' to be changed to 'Bikini Friday'!{w=[wt3]} For{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} climate change awareness!"
                        hero "I don't think that's going to fly, {nm}[fnamehine]{/nm}."

                    elif a_event_0 < 2/6:
                        $ hine_mood = "A4"
                        hine "Today's been great!{w=[wt3]} I've been compiling a list of the best water fountain locations in school.{w=[wt3]} You know, for{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {bt}hydration purposes{/bt}!"
                        hero "I'm afraid to ask why you need that list..."

                    elif a_event_0 < 3/6:
                        $ hine_mood = "A3"
                        hine "Living the dream, buddy!{w=[wt3]} Every day is an opportunity to appreciate the beauty that surrounds us!{w=[wt3]} {bt}Especially when it's bouncing{/bt}! {gg}Hehehe...{/gg}"
                        hero "You really need to work on your subtlety, {nm}[fnamehine]{/nm}."

                    elif a_event_0 < 4/6:
                        $ hine_mood = "O1"
                        hine "Meh{w=[wt2]}, it's been average.{w=[wt3]} Not enough bouncing{w=[wt1]}, if you catch my drift."
                        $ hero_mood = "O1"
                        hero "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Don't think I want to catch that drift."

                    elif a_event_0 < 5/6:
                        $ hine_mood = "A1"
                        hine "Bro, I'm on fire today!{w=[wt3]} I've developed a new technique for{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {bt}stretching{/bt}. Want me to demonstrate on that group of girls over there?"
                        hero "Please don't.{w=[wt3]} I don't want to be associated with whatever you're planning."

                    else:
                        $ hine_mood = "A4"
                        hine "Oh man{w=[wt2]}, {bt}it's been great!{/bt}{w=[wt3]} The wind gave me a magnificent view a few moments ago!{w=[wt3]} I love nature! "
                        hero "Maybe we should change the subject."

            # ----------------------------------------------------------------------------------------------------
            # Asking at any other time
            # ----------------------------------------------------------------------------------------------------
            else:
                hero "How are you doing, {nm}[fnamehine]{/nm}?"

                # ----------------------------------------------------------------------------------------------------
                # Common
                # ----------------------------------------------------------------------------------------------------
                if a_event_0 < 1/5:
                    $ hine_mood = "A3"
                    hine "Been working on my pickup lines!{w=[wt3]} How about this one:{w=[wt3]} 'Are you a camera? Because every time I look at you, I smile!'{w=[wt3]} Smooth, right?"
                    hero "Maybe stick to being silent, {nm}[fnamehine]{/nm}."

                elif a_event_0 < 2/5:
                    $ hine_mood = "A3"
                    hine "Well{w=[wt2]}, just exploring new horizons.{w=[wt3]} Life's an adventure, my friend!{w=[wt3]} Always seeking new heights{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} and depths{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} and curves! {bt}Especially the curves{/bt}!"
                    hero "You never cease to amaze me, {nm}[fnamehine]{/nm}. And not in a good way."

                elif a_event_0 < 3/5:
                    $ hine_mood = "O1"
                    hine "Eh{w=[wt2]}, could be better.{w=[wt3]} The scenery hasn't been very stimulating today{w=[wt1]}, if you know what I mean."
                    $ hero_mood = "O1"
                    hero "I'm not sure I want to know what you mean."

                elif a_event_0 < 4/5:
                    $ hine_mood = "A1"
                    hine "Not bad{w=[wt2]}, not bad.{w=[wt3]} Just been people-watching.{w=[wt3]} You'd be amazed at what you can see if you look closely enough!{w=[wt1]} {gg}Hehehe...{/gg}"
                    hero "I think I'll pass on that{w=[wt2]}, thanks."

                else:
                    $ hine_mood = "A3"
                    hine "Living the dream, my friend!{w=[wt3]} You know{w=[wt3]}, I've been thinking about becoming a fashion photographer.{w=[wt3]} I've got a real eye for{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} aesthetics, you know?"
                    hero "Maybe you should rethink that career path."
                    hine "Nonsense!{w=[wt3]} I've got a real talent for capturing beauty!"

            $ hine_know.append("Talk")
            $ hine_know.append("Talk_How")
            $ add_stat("hine", "love", 2/a_event_0)
            $ add_stat("hero", "cha_soc", 2/a_event_0)

        "Talk about somewhere":
            menu:
                "School":
                    $ hero_mood = "A2"
                    hero "What do you think about our school?"

                    $ a_event_0 = renpy.random.random()
    
                    if a_event_0 < 1/2:
                        $ hine_mood = "A3"
                        hine "The schoolyard, my friend, is an excellent place to admire the beauty of nature!{w=[wt3]} The way the sunlight filters through the trees creates the most magnificent views!{w=[wt4]} Especially from certain angles looking up at the balcony!{w=[wt3]} Hehehe..."
                        
                        $ hero_mood = "O2"
                        hero "Don't even start with that.{w=[wt3]} I'm not lending you my phone again so you can use the camera to peek under girls' skirts on the balcony."
                        
                        $ hine_mood = "A1"
                        hine "That's perfectly fine!{w=[wt3]} I don't need to borrow your phone anymore.{w=[wt4]} After that day, some people did look suspicious of me, but I couldn't let such a perfect view go to waste!{w=[wt3]} I just wanted your company, you know?{w=[wt4]} One of us looks while the other keeps watch!{w=[wt3]} The perfect system!"

                        if "HINE_PHONE_BROKEN" in hero_know and not "HINE_NEW_PHONE" in hero_know and not "HERO_GAVE_PHONE_TO_HINE" in hero_know:
                            $ hine_mood = "O1"
                            hine "As soon as I get a new phone, I'll handle the documentation myself.{w=[wt3]} It's an important scientific endeavor, after all!{w=[wt3]} Hehehe..."
                        
                        elif "HINE_NEW_PHONE" in hero_know:
                            $ hine_mood = "A3"
                            hine "Besides, I already got a new phone!{w=[wt3]} So we don't need to worry about that part anymore.{w=[wt4]} We can take turns being the lookout!{w=[wt3]} What do you say?{w=[wt3]} Partners in appreciation?{w=[wt3]} Hehehe..."
                        
                        elif "HERO_GAVE_PHONE_TO_HINE" in hero_know:
                            $ hine_mood = "A3"
                            hine "I already have the phone you gave me!{w=[wt3]} It doesn't make sense that we aren't in this together now.{w=[wt4]} You've already invested in the cause!{w=[wt3]} Think of all the magnificent views we could document!{w=[wt3]} Hehehe..."
                    
                    else:
                        $ hine_mood = "A1"
                        hine "If you ever need to escape from an angry girl{w=[wt1]}, the boys' locker room is your sanctuary.{w=[wt3]} Not that I need it, of course!{w=[wt4]} But there are two exits on opposite sides{w=[wt1]}, making it good to lose pursuers.{w=[wt3]} Perfect escape route!"
                        
                        $ hero_mood = "O1"
                        hero "That plan didn't seem very effective the first time I saw you.{w=[wt3]} I remember seeing you with a black eye sitting on the locker room floor with a girl standing over you."
                        
                        $ hine_mood = "O1"
                        hine "T{w=[wt1]}-that time doesn't count!{w=[wt3]} {nm}[fnamewgal]{/nm} was with {nm}[fnamehriv]{/nm}!{w=[wt4]} He's the real problem in everything!{w=[wt3]} That brute actually told her she could follow him in there!{w=[wt3]} Talk about breaking the sacred sanctuary rules!"
                        
                        $ hine_mood = "A1" 
                        hine "Although{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} thinking about it now{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Maybe the boys' locker room is also a good place to bring girls!{w=[wt3]} Since there are so few guys at this school{w=[wt1]}, it's usually empty.{w=[wt3]} Perfect privacy if you know the right times!"

                        if wsuk_quest_1 >= 1:
                            $ hero_mood = "A3"
                            $ hero_fx = 1
                            hero "Oh{w=[wt1]}, yeah{w=[wt2]}, that's true!!!"
                            
                            $ hine_mood = "O1" 
                            $ hine_fx = 1
                            hine "{w=[wt2]}.{w=[wt2]}.{w=[wt2]}.{w=[wt3]} W{w=[wt1]}-wait{w=[wt2]}, {aw}what!?!?{/aw}"

                            $ hero_mood = "A2"
                            $ hero_fx = 2
                            hero "N{w=[wt1]}-nothing!{w=[wt2]} J{w=[wt1]}-just saying you're right about the locker room usually being empty!{w=[wt1]} {gg}He-he...{/gg}"

                        else:
                            $ hero_mood = "A2"
                            hero "If you say so..."

                "Beach":
                    $ hero_mood = "A2"
                    hero "Ever been to the beach around here?"

                    # Information about beach dating spots and viewing opportunities
                    $ hine_mood = "A3"
                    hine "The beach is my summer research facility!{w=[wt1]} {gg}He-he...{/gg}{w=[wt3]} There's this perfect spot near the rocky outcrop on the north side.{w=[wt3]} If you bring binoculars for 'bird watching,' you can see the main swimming area perfectly!{w=[wt3]} The lifeguard never checks there!"
                    
                    $ hero_mood = "O1"
                    hero "That sounds{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} illegal."
                    
                    $ hine_mood = "A1"
                    hine "Appreciating nature is never illegal, my friend!{w=[wt3]} But if you're looking for a more social approach{w=[wt1]}, the beach volleyball courts are always looking for players.{w=[wt3]} Even if you're terrible{w=[wt1]}, girls will still let you join because they need even teams.{w=[wt4]} And volleyball means jumping!{w=[wt2]} Lots and lots of jumping!{w=[wt1]} {gg}He-he...{/gg}"

                "Shopping Mall":
                    $ hero_mood = "A2"
                    hero "Do you go to the mall often?"

                    $ a_event_0 = renpy.random.random()

                    if a_event_0 < 1/2:
                        $ hine_mood = "A3"
                        hine "The mall is a paradise of observation opportunities!{w=[wt1]} {gg}He-he...{/gg} {w=[wt3]} Have you noticed all those corridors on the upper floors?{w=[wt3]} The ones with the glass handrails?{w=[wt3]} It's absolutely perfect!"
                        
                        $ hine_mood = "A1"
                        hine "If you stand at just the right spot on the first floor, you can see right up when girls walk by up there!{w=[wt4]} The architects were either complete geniuses or fellow men of culture!{w=[wt3]} I've mapped out all the prime viewing locations.{w=[wt3]} For scientific purposes, of course!"
                        
                        $ hero_mood = "O1"
                        hero "I should have known that's where this was going..."
                        
                        $ hine_mood = "A2"
                        hine "Knowledge is meant to be shared, my friend!{w=[wt4]} The food court has the best vantage points.{w=[wt3]} Just don't be too obvious or security might ask questions.{w=[wt3]} Not that I know from experience or anything."
                    
                    else:
                        $ hine_mood = "O1"
                        hine "After that unfortunate accident with my previous phone{w=[wt1]}, I had to visit the mall to find a replacement.{w=[wt3]} The electronics store there is absolutely amazing!{w=[wt4]} They have everything!{w=[wt3]} Phones with amazing zoom capabilities{w=[wt1]}, miniature cameras{w=[wt1]}, all sorts of gadgets that could be useful for{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} s{w=[wt1]}-studying nature!"
                        
                        $ hine_mood = "A3"
                        hine "They even have these tiny camera devices that can be attached to—{w=[wt2]}{nw}"
                        
                        $ hine_mood = "O1"
                        hine "They even have these tiny camera devices that can be attached to—{w=[wt2]}{fast} I mean{w=[wt2]}, they have lots of normal{w=[wt2]}, everyday electronics too!{w=[wt3]} Nothing suspicious at all!{w=[wt4]} But a true connoisseur would appreciate their selection.{w=[wt3]} Absolutely top-notch!"
                        
                        $ hero_mood = "O1"
                        hero "Oh{w=[wt2]}, I see..."

        "Return":
            jump hine_interact

    $ add_stat("hine", "inti", 0.2)
    $ gametimemin += 20
    jump hine_interact_check

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_hine:
    $ hine_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (hine_inti*0.02) and not any(get_id.startswith("HERO_Dated") for get_id in hine_know):

        hine "You know{w=[wt2]}, I'm curious now.{w=[wt3]} Have you ever dated?"

        $ hero_fx = 1
        $ hero_mood = "O1"
        menu:
            hine "You know, I'm curious now. Have you ever dated?{fast}"
            
            "Deny":
                $ hine_know.append("HERO_Dated_N")
                $ msg.msg(renpy.translate_string("{nm}[fnamehine]{/nm} knows you a little more"))
                $ add_stat("hine", "inti", 0.25)

                hero "N{w=[wt1]}-No{w=[wt2]}, I've never dated before."

                $ hine_mood = "O2"
                hine "{pa}So you're just like me!?{/pa}"

                $ hero_mood = "A1"
                hero "Please don't say that again.{w=[wt2]} I'm offended."

            "Confirm":
                $ hine_know.append("HERO_Dated_Y")
                $ msg.msg(renpy.translate_string("{nm}[fnamehine]{/nm} knows you a little more"))
                $ add_stat("hine", "inti", 0.25)

                hero "W{w=[wt1]}-well{w=[wt2]}, y{w=[wt1]}-yes{w=[wt2]}, I kinda dated a girl once."

                $ hine_mood = "O2"
                hine "{pa}Please{w=[wt2]}, accept me as your apprendice{w=[wt1]}, master!{/pa}"
                hero "{aw}W{w=[wt1]}-what!?{/aw}"

    # ----------------------------------------------------------------------------------------------------
    # Ask HERO's girl preference
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (hine_inti*0.02) and sum(1 for get_id in hine_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in hine_know if get_id.startswith("HERO_N_Girl")) < 4:
        hine "So{w=[wt2]}, what kind of girl catches your attention?{w=[wt2]} I'm curious what your standards are.{nw}"

        menu:
            hine "So, what kind of girl catches your attention? I'm curious what your standards are.{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in hine_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in hine_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in hine_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in hine_know if "Personality_" in get_id)

                # Appearance Likes(Y)/Dislikes(N)
                $ a_event_1 = hine_know
                $ a_event_3 = "initiative_hine_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl

                # Store the answer if one was given
                if _return:
                    $ hine_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg(renpy.translate_string("{nm}[fnamehine]{/nm} knows you a little more"))
                $ add_stat("hine", "inti", 0.5)

                if _return in ["Personality_9", "Personality_5", "Personality_4", "Personality_11"]: # Match - intelligent, outgoing, aggressive, visually diligent
                    $ add_stat("hine", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ hine_mood = "A3"
                    hine "Oh! I see you're a man of culture as well."

                elif _return in ["Personality_6", "Personality_2", "Personality_10", "Personality_12"]: # Opposite match - shy/timid, dispirited, stupid, sloppy
                    $ add_stat("hine", "bonus", -10)
                    $ hine_mood = "O1"
                    hine "{aw}Ehh...?{/aw}{w=[wt2]} Really? That's what you're into?"

                else: # Others
                    $ hine_mood = "A1"
                    hine "Well{w=[wt2]}, it makes sense{w=[wt2]}, but{w=[wt2]}, well{w=[wt2]}, yeah{w=[wt2]}, ok.{w=[wt3]} Each has their own preference, right?"

            "Don't choose":
                jump initiative_hine_return

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:
        hine "You know{w=[wt2]}, What if{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Nah{w=[wt2]}, I better not say what I was gonna say if I don't wanna go to jail."
        hero "{aw}Ehhh!?{/aw}"
        jump hine_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("hine", "inti", 0.20)
    jump hine_interact_check

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_hine_return:

    call hero_n_answer from _call_hero_n_answer

    hine "{aw}Ehhh...!?{/aw}{w=[wt3]} Not fair!"
    jump hine_interact
