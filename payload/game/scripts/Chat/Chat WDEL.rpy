# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wdel_show:

    if wdel_love <= -20:
        $ wdel_mood = "O2"
    elif wdel_love < 0:
        $ wdel_mood = "A2"
    elif wdel_love >= 0:
        $ wdel_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_2

    show WDEL at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wdel_show_activity:
    $ msg.msg(renpy.translate_string("[C_Nam][fnamewdel][C_Off] is ") + renpy.translate_string(str(str(Get_ActivityName("wdel")))))

    if Get_ActivityName("wdel") in ["at class"]:
        jump show_ui

    else:
        return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wdel_interact_end:
    if "interacting_hero" in wdel_know:
        $ wdel_know.remove("interacting_hero")
        $ msg.msg(renpy.translate_string("Finish talking"))
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wdel_interact_start:
    call hide_ui from _call_hide_ui_17
    call wdel_show_activity from _call_wdel_show_activity
    $ wdel_inti = min(char_inti_cap, wdel_inti)
    call hide_ui from _call_hide_ui_18
    call wdel_show from _call_wdel_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wdel_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if hero_map == wdel_map:
        pass

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wdel_interact_check:
    # Save current outfit before any updates
    $ wdel_wear_keep = wdel_wear

    call gametime from _call_gametime_8
    call hide_ui from _call_hide_ui_19

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wdel_wear != wdel_wear_keep:
        $ wdel_wear = wdel_wear_keep

    call wdel_show from _call_wdel_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------------------------------------------------------------------------------------------------
    # Is Unavailable
    # ----------------------------------------------------------------------------------------------------
    if gametimehour >= 18: # Went home
        $ a_event_0 = renpy.random.random()
        if a_event_0 < 2/5 and "WDEL_BG_FAMILY_1" in hero_know:
            $ wdel_mood = "O1"
            wdel "Tch!{w=[wt2]} Gotta bail and help my old man at the shop.{w=[wt3]} Those bikes ain't gonna fix themselves!{w=[wt3]} Later, asshole!"
        elif a_event_0 < 4/5 and "WDEL_Y_DRUMS" in hero_know:
            $ wdel_mood = "A1"
            wdel "Oi!{w=[wt2]} Time's up!{w=[wt3]} Got band practice to get to!{w=[wt3]} These drums ain't gonna beat themselves.{w=[wt3]} LET'S ROCK another time, got it?"
        else:
            $ wdel_mood = "A1"
            wdel "Fuck!{w=[wt2]} Look at the time!{w=[wt3]} Got stuff to handle, ya hear?{w=[wt3]} Don't get your panties in a twist, I'll see ya tomorrow, bro!"
        $ hero_fx = 0
        jump wdel_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Get_MapName("wdel", "at class"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "wdel"):
            $ wdel_mood = "O1"
            wdel "Ah shit{w=[wt2]}, teacher's here already.{w=[wt3]} Was thinking about ditching{w=[wt2]}, but whatever.{nw}"

            show WDEL at RC
            show WDEL at OR_slow
            show HERO at OR_slow
            wdel "Ah shit{w=[wt2]}, teacher's here already.{w=[wt3]} Was thinking about ditching{w=[wt2]}, but whatever.{fast}{w=[wt2]} {gg}Heh!{/gg}"

            jump wdel_interact_end

        else:
            $ wdel_mood = "O1"
            wdel "Tch{w=[wt2]}, class time{w=[wt2]}, huh?{w=[wt3]} What a pain in the ass.{w=[wt3]} Thinking about skipping{w=[wt2]}, got it?"

            if Get_MapName("wdel", "at class") == Get_MapName(None, "school", "class_1b"):
                menu:
                    "Go together":
                        $ hero_mood = "A1"
                        hero "Come on{w=[wt2]}, let's just go."
                        
                        $ wdel_mood = "A2"
                        wdel "{gg}Heh!{/gg}{w=[wt2]} But that fat ass teacher better not pisses me off."
                        
                        $ hero_mood = "O1"
                        hero "Hey hey...!{w=[wt2]} Just try not to cause trouble this time."
                        
                        $ wdel_mood = "A4"
                        wdel "{lg}GAH HA HA HA...!{/lg}{w=[wt2]} No promises, dumbass!{w=[wt2]} Come on!"
                        
                        scene bg_0
                        with dissolve

                        $ hero_map = wdel_map
                        $ hero_mood = "A1"
                        $ wdel_mood = "A1"
                        
                        call gametime from _call_gametime_9
                        call check_playermap from _call_check_playermap_2
                        call hide_ui from _call_hide_ui_20
                        show WDEL at RC
                        show HERO at LC
                        with dissolve
                        
                        wdel "Alright{w=[wt2]}, later!"

                        jump wdel_interact_end
                        
                    "Let her go":
                        pass

            $ hero_mood = "A1"
            hero "See you!"
            
            $ wdel_mood = "A1"
            
            show HERO at LC
            show WDEL at RC
            show WDEL at CC_average
            wdel "Sure!{w=[wt2]}{nw}"

            $ hero_mood = "O1"
            $ wdel_mood = "A3"

            play SE1 "Hit1.ogg"            
            show WDEL at CC
            show WDEL at Hit_L
            show HERO at Hurt_L
            wdel "Sure!{w=[wt2]}{fast} See ya, dumbass!{nw}"

            show WDEL at OL_slow
            wdel "Sure!{w=[wt2]} See ya, dumbass!{fast}"

        jump wdel_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Comment After A Interaction
    # ----------------------------------------------------------------------------------------------------
    elif "interacting_hero" in wdel_know:
        $ a_event_0 = renpy.random.random()

        # Brings an interactive subject
        if renpy.random.random() < (0.2 + (wdel_love * 0.003)):
            jump initiative_wdel

        # Do a random comment
        elif renpy.random.random() > (0.5 + (wdel_love * 0.002)):
            $ a_event_0 = renpy.random.random()
            if a_event_0 < 1/9:
                wdel "These teachers can kiss my ass!{w=[wt3]} School's just a prison with homework instead of hard labor.{w=[wt3]} The real shit happens outside these walls!"
            elif a_event_0 < 2/10:
                $ wdel_mood = "A1"
                wdel "Heh{w=[wt2]}, you're not as much of a pussy as I thought.{w=[wt3]} Kinda refreshing around here."
            elif a_event_0 < 3/10:
                $ wdel_mood = "A1"
                wdel "Pop music is for weak-ass posers.{w=[wt3]} Real music should feel like getting punched in the gut and loving it!{w=[wt3]} {lg}GAH HA HA HA...{/lg}"
            elif a_event_0 < 4/10 and "WDEL_BG_FAMILY_1" in hero_know:
                $ wdel_mood = "A1"
                wdel "My bike's acting up again.{w=[wt3]} Gonna have to tear it down this weekend.{w=[wt3]} Nothin' better than the smell of motor oil, ya hear?"
            elif a_event_0 < 5/10 and "WDEL_BG_FAMILY_1" in hero_know:
                $ wdel_mood = "A1"
                wdel "You should come by the shop sometime.{w=[wt3]} My old man's always sayin' I need to bring more friends around.{w=[wt3]} He's cool, for a dad."
            elif a_event_0 < 6/10:
                $ wdel_mood = "O1"
                wdel "One minute you're dozing off in class{w=[wt3]}, the next minute the teacher is saying{w=[wt2]}, {i}'You're going to fail if you keep slacking off'{/i}.{w=[wt4]}{nw}"
                $ wdel_mood = "A3"
                wdel "One minute you're dozing off in class{w=[wt3]}, the next minute the teacher is saying{w=[wt2]}, {i}'You're going to fail if you keep slacking off'{/i}.{w=[wt4]}{fast} Heh{w=[wt2]}, bullshit!{w=[wt3]} Grandpa naps all day{w=[wt1]}, and they call it '{aw}resting in peace{/aw}'."
            elif a_event_0 < 7/10:
                $ wdel_mood = "A1"
                wdel "Been tryin' to teach {nm}[fnamewuza]{/nm} how to play drums{w=[wt1]}, but the asshole keeps breaking my sticks!"
            elif a_event_0 < 8/10:
                $ wdel_mood = "A1"
                wdel "What's the last thing to go through a bug's mind when it hits a motorcycle windshield?{w} ITS ASS!{w=[wt2]} {lg}GAH HA HA HA...{/lg}"
            elif a_event_0 < 9/10:
                $ wdel_mood = "A1"
                wdel "Life is like a box of chocolates.{w=[wt3]} It doesn't last as long for fat people!{w=[wt3]} {lg}GAH HA HA HA...{/lg}"
            else:
                $ wdel_mood = "O1"
                wdel "Some assholes tried starting shit with me on the way here.{w=[wt3]} Let's just say they'll think twice before messing with a girl who can throw a proper punch!{w=[wt2]} Heh!"

    # ----------------------------------------------------------------------------------------------------
    # WDEL is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wdel") in ["eating"]:
        "{nm}[fnamewdel]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamewdel]{/nm} is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wdel") from _call_circletable_1

                while Get_ActivityName("wdel") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_2
                call gametime from _call_gametime_10
                
                jump wdel_interact_start

            "Return":
                jump wdel_interact_end

    # ----------------------------------------------------------------------------------------------------
    # Welcum Message
    # ----------------------------------------------------------------------------------------------------
    else:
        $ a_event_0 = renpy.random.random()
        
        if a_event_0 < 1/6:
            $ wdel_mood = "A1"
            wdel "Yo{w=[wt2]}, what's up, bro?"
        elif a_event_0 < 2/6:
            $ wdel_mood = "A1"
            wdel "Oi!{w=[wt2]} You lookin' for me?"
        elif a_event_0 < 3/6:
            $ wdel_mood = "A1"
            wdel "Hey, dude!{w=[wt2]} Got somethin' interestin' goin' on?"
        elif a_event_0 < 4/6:
            $ wdel_mood = "A1"
            wdel "What brings ya over to my territory, huh?"
        elif a_event_0 < 5/6:
            $ wdel_mood = "A1"
            wdel "Hey, dumbass!"
        else:
            $ wdel_mood = "A1"
            wdel "Hey, asshole!"
        $ wdel_fx = 0

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wdel_interact:
    call hide_ui from _call_hide_ui_21
    if "interacting_hero" not in wdel_know:
        $ wdel_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wdel_interact_chat
        "Touch" if not is_specialevent:
            jump wdel_interact_touch
        "Hang out":
            jump wdel_interact_hangout
        "Give item" if not is_specialevent:
            jump wdel_interact_gift
        "Return":
            jump wdel_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wdel_interact_gift:
    $ a_item_8 = "wdel" # Character ID
    $ a_item_9 = 0
    $ a_item_6 = "wdel_interact" # Return location
    call UI_give_Item from _call_UI_give_Item_3

label wdel_interact_gift_receive(reaction):
    $ a_event_0 = renpy.random.random()
    if reaction == "Accept":        
        if match_level == "perfect":
            $ wdel_mood = "A3"
            if wdel_love >= 50:
                $ wdel_mood = "A1"
                $ wdel_fx = 1
                if a_event_0 < 1/3:
                    wdel "Huh?{w=[wt2]} For me?{w=[wt2]} Huh{w=[wt2]}, t{w=[wt1]}-that's so cool...!{w=[wt4]} Thank you!"
                elif a_event_0 < 2/3:
                    wdel "This is for me?{w=[wt4]} That's all I wanted.{w=[wt3]} T{w=[wt1]}-thank you!"
                else:
                    wdel "{aw}Ehhh...!?{/aw} W{w=[wt1]}-what's up, bro?{w=[wt2]} Are you trying to get into my panties?"
                    hero "{aw}EHHH!?{/aw}"
                    wdel "Just kidding.{w=[wt2]} T{w=[wt1]}-thanks!"
            else:
                if a_event_0 < 1/3:
                    wdel "Wow, dude{w=[wt2]}, that's so cool!{w=[wt3]} You rock!!!"
                elif a_event_0 < 2/3:
                    wdel "Oh shit, really?{w=[wt2]} For me?{w=[wt3]} That's dope, man!{w=[wt2]} Thanks!"
                else:
                    wdel "Yooo, this is sick!{w=[wt3]} Thanks, bro!{w=[wt2]} I owe you one!"

        elif match_level == "great":
            $ wdel_mood = "A1"
            if wdel_love >= 50:
                if a_event_0 < 1/3:
                    wdel "Oh, nice!{w=[wt2]} This is pretty cool, man!{w=[wt3]} Thanks!"
                elif a_event_0 < 2/3:
                    wdel "Hey, I like this!{w=[wt2]} Good pick, [C_Nam][fnamehero][C_Off]!{w=[wt3]} Appreciate it!"
                else:
                    wdel "Ohhh, this is neat!{w=[wt2]} You know my style, dude!{w=[wt3]} Thanks!"
            else:
                if a_event_0 < 1/2:
                    wdel "That's nice, bro!{w=[wt2]} Thanks!"
                else:
                    wdel "Hey, cool!{w=[wt2]} Thanks, man!{w=[wt2]} This is pretty rad!"
            
        else:
            $ wdel_mood = "A1"
            if a_event_0 < 1/3:
                wdel "Hey, thanks man!{w=[wt2]} This is pretty cool!"
            elif a_event_0 < 2/3:
                wdel "Oh, nice!{w=[wt2]} Not bad at all!{w=[wt2]} Thanks, dude!"
            else:
                wdel "Huh, alright!{w=[wt2]} I can work with this!{w=[wt2]} Thanks, bro!"
    
    elif reaction == "Reject":
        $ wdel_mood = "A2"
        if wdel_love >= 50:
            if a_event_0 < 1/3:
                wdel "Uh{w=[wt2]}, this ain't really my thing, man."
            elif a_event_0 < 2/3:
                wdel "Dude{w=[wt2]}, no offense, but what am I supposed to do with this?"
            else:
                wdel "Bro{w=[wt2]}, you sure you got the right person?"
        else:
            if a_event_0 < 1/4:
                wdel "{bt}Ehhh...?{/bt}{w=[wt3]} You gay, man?"
            elif a_event_0 < 2/4:
                wdel "{aw}Ewww...{/aw}{w=[wt2]} Point that shit over there, man."
            elif a_event_0 < 3/4:
                wdel "Hm?{w=[wt2]} What I'm supposed to do with that?"
            else:
                wdel "Yeahhh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm gonna have to pass on that, chief."
    
    else: # "Already"
        $ wdel_mood = "A1"
        if wdel_love >= 50:
            if a_event_0 < 1/2:
                wdel "Haha, dude!{w=[wt2]} I already have one of those!{w=[wt3]} But hey, thanks for thinking of me!"
            else:
                wdel "Hey man{w=[wt2]}, I already got this one!"
        else:
            if a_event_0 < 1/2:
                wdel "I already have it, dude."
            else:
                wdel "Yeah{w=[wt2]}, I got one already, man."

    $ gametimemin += 5
    jump wdel_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wdel_interact_touch:
    menu:
        "Hug":
            label wdel_interact_touch_hug:
                pass

            $ wdel_know.append("Hug")
            $ a_event_0 = sum(1 for buceta in wdel_know if buceta =="Hug")
            $ wdel_fx = 1

            if a_event_0 == 1:

                $ a_event_1 = renpy.random.random()
                if a_event_1 <= 0.33:
                    scene bg_2 pink
                elif a_event_1 <= 0.66:
                    scene bg_2 yellow
                else:
                    scene bg_2 flowers

                show action_wdel_hug 1a
                with dissolve

                show action_wdel_hug 1b

                if perk_cha_sex >= 1:                
                    $ msg.msg(renpy.translate_string("{nm}[fnamewdel]{/nm}'s  lust {color=#32FF32}+")+str(2 * perk_cha_sex * lustadd_wdel)[:4])
                    $ wdel_lust += 2 * perk_cha_sex * lustadd_wdel

                $ add_stat("wdel", "love", 2/a_event_0)
                $ add_stat("hero", "cha_sex", 2/a_event_0)

                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.25:
                    wdel "Whoa there, buddy!{w=[wt1]} {lg}GAH HA HA HA...{/lg}{w=[wt2]} Feeling brave today, aren't we?{w=[wt2]} I like that energy!"
                elif a_event_0 <= 0.50:
                    wdel "What's up, dumbass?"
                elif a_event_0 <= 0.75:
                    wdel "Yeah!{w=[wt2]} {aw}LET'S ROCK!{/aw}"
                else:
                    wdel "Whoa Whoa Whoa!{w=[wt2]} Coming in hot, aren't ya?{w=[wt1]} {lg}GAH HA HA HA...{/lg}{w=[wt2]} You're alright, asshole!"

                show action_wdel_hug 1a with None

                call gamecheck from _call_gamecheck_4
                call hide_ui from _call_hide_ui_22
                call wdel_show from _call_wdel_show_2
                $ gametimemin += 10
                $ add_stat("wdel", "inti", 0.1)

            else:

                scene bg_2 sparking
                show action_wdel_hug2_wdel 1 at RC
                show action_wdel_hug2_wdel 1 at CC_average
                show action_wdel_hug2_hero 1 at LC
                show action_wdel_hug2_hero 1 at CC_average

                pause(0.5)

                play SE1 "Hit1.ogg"

                hide action_wdel_hug2_hero
                hide action_wdel_hug2_wdel
                show action_wdel_hug2b at vpunch

                pause(0.5)

                play SE1 "Hit1.ogg"

                $ Y_spd = 0.25
                $ Y_pos = 1000

                hide action_wdel_hug2b
                show action_wdel_hug2_wdel 2
                show action_wdel_hug2_hero 2 at Y_Move

                pause(0.25)

                play SE1 "Hit2.mp3"

                pause(0.25)

                show action_wdel_hug2c
                hide action_wdel_hug2_wdel
                hide action_wdel_hug2_hero
                with dissolve

                show action_wdel_hug2d

                $ a_event_0 = renpy.random.random()
                if a_event_0 <= 0.25:
                    wdel "Enough for you, asshole!"
                elif a_event_0 <= 0.50:
                    wdel "Did that hurt?{w=[wt2]} Good."
                elif a_event_0 <= 0.75:
                    wdel "What am I{w=[wt2]}, your teddy bear?{w=[wt2]} Control your cock, dude!"
                else:
                    wdel "Don't push your luck, wimp!"

                show action_wdel_hug2c with None

                call gamecheck from _call_gamecheck_5
                call hide_ui from _call_hide_ui_23
                call wdel_show from _call_wdel_show_3

        "Return":
            jump wdel_interact
    
    jump wdel_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wdel_interact_hangout:
    menu:
        "Return":
            jump wdel_interact

    $ gametimemin += 30
    jump wdel_interact_check

# ----------------------------------------------------------------------------------------------------
# Dialogue Options
# ----------------------------------------------------------------------------------------------------
label wdel_interact_chat:
    menu:
        "Talk about somewhere":
            menu:
                "School":
                    $ hero_mood = "A1"
                    hero "What do you think about our highschool?"

                    $ a_event_0 = renpy.random.random()

                    if a_event_0 < 1/4:
                        # General comment
                        $ wdel_mood = "A2"
                        wdel "Way better than any of my old schools.{w=[wt4]} The staff here are a bunch of bums. This whole thing about giving all the work to the Student Council is perfect! They may even feel useful as the headmistress's lapdogs, but they are still weak pawns."
                        
                        $ hero_mood = "A2"
                        hero "Don't you think the Student Council does a good job?"
                        
                        $ wdel_mood = "A3"
                        wdel "{lg}GAH HA HA HA...{/lg}{w=[wt2]} Your mom does much better in the brothel!{w=[wt3]} Any place with that many hormonal virgins packed together ain't gonna be professional{w=[wt1]}, no matter what fancy abbreviation they slap on school name, ya hear?{w=[wt4]} Still{w=[wt2]}, the place has character.{w=[wt3]} I'll give it that much."
                    
                    elif a_event_0 < 2/4:
                        # Add tip of a private map to bang a girl
                        $ wdel_mood = "A1"
                        wdel "The rooftop access door is supposed to be locked, but the mechanism is busted.{w=[wt3]} If you push it just right while turning the handle, it pops open.{w=[wt4]} Great hiding spot during lunch if you want peace and quiet.{w=[wt3]} Or if you need to duck {nm}The Living Doll{/nm} when she's hunting for uniform violations.{w=[wt3]} {gg}Heh!{/gg}"
                        
                        $ hero_mood = "O1"
                        hero "Isn't that against school rules?"
                        
                        $ wdel_mood = "O2"
                        wdel "No shit, Sherlock.{w=[wt3]} That's what makes it good.{w=[wt3]} The view's killer too.{w=[wt4]} You can see the whole courtyard, so you know exactly when it's safe to come down.{w=[wt3]} Just don't get caught up there or we'll both be screwed, got it?"
                    
                    elif a_event_0 < 3/4:
                        # Add tip of a private map to bang a girl
                        $ wdel_mood = "A3"
                        wdel "The old storage room behind the sport court is fucking awesome!{w=[wt3]} {lg}GAH HA HA HA...{/lg}{w=[wt3]} There's all kinds of abandoned equipment in there.{w=[wt4]} Found some old volleyball poles that make perfect drum sticks.{w=[wt3]} The acoustics are sick too.{w=[wt4]} Me and {nm}[fnamewuza]{/nm} jam in there sometimes after practice.{w=[wt3]} Nobody ever checks it."
                        
                        $ hero_mood = "A2"
                        hero "You two are in a band?"
                        
                        $ wdel_mood = "A1"
                        wdel "Not officially.{w=[wt3]} Just messing around.{w=[wt4]} But that storage room is perfect for it.{w=[wt3]} There's even this broken old trophy case we use as a makeshift drum.{w=[wt3]} The coach never ventures that far into the junk pile.{w=[wt4]} LET'S ROCK!!!"
                    
                    else:
                        # Add tip of a private map to bang a girl
                        $ wdel_mood = "A1"
                        wdel "The space behind the auditorium curtains is fucking wild, bro.{w=[wt3]} There's this crawlspace that goes beneath the stage.{w=[wt4]} Me and {nm}[fnamewuza]{/nm} found it last week.{w=[wt3]} You can hear everything that happens in the auditorium from down there.{w=[wt3]} {gg}Heh!{/gg}{w=[wt3]} Spooked the crap out of some theater club nerds by making ghost noises."
                        
                        $ hero_mood = "A4"
                        hero "That sounds like something straight out of a horror movie!"
                        
                        $ wdel_mood = "A3"
                        wdel "Right!?{w=[wt3]} {lg}GAH HA HA HA...{/lg}{w=[wt3]} Freaking hilarious!{w=[wt4]} And nobody suspects a thing.{w=[wt3]} Now they're all convinced the place is haunted.{w=[wt4]} You should've seen their faces when we made the stage lights flicker!{w=[wt3]} Fucking priceless!{w=[wt3]} Their theater meeting ended real quick after that!"


                "Beach":
                    $ hero_mood = "A2"
                    hero "Ever been to the beach around here?"

                    $ a_event_0 = renpy.random.random()

                    if a_event_0 < 1/2:
                        # Add tip of map for dating
                        $ wdel_mood = "A3"
                        wdel "Hell yeah! The city beach is fucking amazing at night, bro!{w=[wt3]} We sneak out there sometimes after dark.{w=[wt4]} Build a bonfire, blast some tunes, just chill.{w=[wt3]} No boring assholes, no rules, just the sound of waves and good company.{w=[wt3]} {gg}Heh!{/gg}"
                        
                        $ wdel_mood = "A1"
                        wdel "Besides, there's this sick cave at the north end that's perfect for dares and shit.{w=[wt3]} {lg}GAH HA HA HA...{/lg}{w=[wt3]} We once convinced some freshman it was haunted.{w=[wt4]} Kid almost pissed himself when we made ghost noises from behind the rocks!{w=[wt3]} You should totally come with us sometime.{w=[wt3]} If you've got the balls for it."
                        
                        $ hero_mood = "A2"
                        hero "Maybe I will. Isn't it dangerous though?"
                        
                        $ wdel_mood = "A2"
                        wdel "That's half the fun, asshole!{w=[wt4]} Just don't expect me to save your ass if you get scared.{w=[wt3]} Though the cave's actually pretty awesome for exploring.{w=[wt4]} Goes back pretty far.{w=[wt3]} We've never reached the end.{w=[wt3]} Might do it someday when we bring proper lights instead of just phone flashlights."
                    
                    else:
                        # Add tip of map for dating and gift item
                        $ wdel_mood = "A3"
                        wdel "Beach is rad.{w=[wt3]} Used to go a lot when I was younger.{w=[wt4]} My old man would take me and {nm}[fnamewuza]{/nm} there on weekends.{w=[wt3]} We'd try to surf while he'd scope out desperate single moms.{w=[wt3]} {gg}Heh!{/gg}{w=[wt3]} Typical Dad."
                        
                        $ hero_mood = "A2"
                        hero "Oh{w=[wt2]}, it seems like there’s no right or wrong age to enjoy life, right?{w=[wt3]} So you surf, huh?{w=[wt2]} That's pretty cool!"
                        
                        $ wdel_mood = "O1"
                        wdel "Was never that good at it.{w=[wt3]} Last time we went, me and {nm}[fnamewuza]{/nm} crashed into each other and both boards snapped in half.{w=[wt4]} Fucking disaster.{w=[wt3]} And to top it all off, dad had vanished with some bitch he met.{w=[wt3]} Left us stranded for hours until he finally showed up after dark to drive us home.{w=[wt3]} Jackass never even apologized."
                        
                        $ hero_mood = "O1"
                        hero "That sounds rough.{w=[wt3]} You ever think about trying again?{w=[wt3]} S{w=[wt1]}-surfing, I mean."
                        
                        $ wdel_mood = "A1"
                        wdel "Sure!{w=[wt3]} Wouldn't mind giving it another shot.{w=[wt4]} {nm}[fnamewuza]{/nm} keeps bugging me about it too.{w=[wt3]} Says we should 'reclaim the experience' or some motivational bullshit.{w=[wt3]} {lg}GAH HA HA HA...{/lg}{w=[wt3]} Girl watches too many sports movies.{w=[wt4]} But yeah, could be fun.{w=[wt3]} If we had boards, that is."

                "Shopping":
                    $ hero_mood = "A2"
                    hero "Got any favorite shops around town?"

                    $ a_event_0 = renpy.random.random()

                    if a_event_0 < 1/2:
                        # Add tip of map for dating and gift item
                        $ wdel_mood = "A3"
                        wdel "There's this fucking awesome music store at the mall.{w=[wt3]} On the second floor.{w=[wt4]} It's like heaven, bro!{w=[wt3]} Wall-to-wall instruments.{w=[wt3]} My dad bought my drum kit there when I was thirteen.{w=[wt3]} Said it was either that or therapy.{w=[wt3]} {lg}GAH HA HA HA...{/lg}"
                        
                        $ hero_mood = "A2"
                        hero "You must spend a lot of time there, huh?"
                        
                        $ wdel_mood = "O1"
                        wdel "Just to browse mostly.{w=[wt3]} That shit's expensive.{w=[wt4]} Usually just pick up drumsticks since I'm always breaking them.{w=[wt3]} Or {nm}[fnamewuza]{/nm} breaks them when I try teaching her.{w=[wt3]} Girl's got the coordination of a drunk elephant, I swear.{w=[wt3]} {gg}Heh!{/gg}{w=[wt3]} Still love her though."
                        
                        $ hero_mood = "A2"
                        hero "What kind of drum kit do you have?"
                        
                        $ wdel_mood = "A1"
                        wdel "Nothing fancy, but it gets the job done.{w=[wt4]} Had to soundproof my room after the neighbors called the cops twice.{w=[wt3]} Worth it though.{w=[wt3]} There's nothing like beating the shit out of drums after a bad day, ya hear?{w=[wt3]} Better than punching actual people.{w=[wt3]} Usually."
                    
                    else:
                        # Add tip of map for dating and gift item
                        $ wdel_mood = "A2"
                        wdel "There's this store at the mall that sells vintage clothes.{w=[wt3]} I walk by sometimes just to check out the window displays.{w=[wt4]} They've got all this badass stuff.{w=[wt3]} Band shirts, leather jackets, combat boots.{w=[wt3]} Real punk and metal gear, not that mass-produced poser shit."
                        
                        $ hero_mood = "A2"
                        hero "You ever buy anything there?"
                        
                        $ wdel_mood = "O1"
                        wdel "Nah.{w=[wt3]} Way too expensive for my budget.{w=[wt4]} You seen the price tags on those leather pants?{w=[wt3]} Fucking highway robbery.{w=[wt3]} Could feed myself for a month on what they charge for one jacket.{w=[wt3]} But someday, man.{w=[wt3]} Someday I'm gonna walk in there and buy that leather jacket they've had on display forever."
                        
                        $ hero_mood = "A2"
                        hero "Maybe for a special occasion?"
                        
                        $ wdel_mood = "A3"
                        wdel "Yeah, like if I ever actually start a real band that gets a gig.{w=[wt3]} That'd be the perfect excuse.{w=[wt4]} Need to look the part, right?{w=[wt3]} {lg}GAH HA HA HA...{/lg}{w=[wt3]} Though with my luck, by the time that happens, the damn thing will be sold.{w=[wt3]} Always some rich kid buying shit just for the look, not cause they appreciate what it stands for."

                "Return":
                    jump wdel_interact_chat

        "Talk about someone":
            menu:
                "{image=icon_hprv} {nm}[fnamehprv]{/nm}" if not "Talk_Char_HPRV" in wdel_know:
                    $ wdel_know.append("Talk_Char_HPRV")
                    $ hero_mood = "A1"
                    hero "So what's the deal with {nm}[fnamehprv]{/nm}?"

                    $ a_event_0 = renpy.random.random()

                    if a_event_0 < 1/2:
                        $ wdel_mood = "A1" 
                        wdel "Oh, this wimp...! He listens to trash. That rap stuff, you know? That must be what makes his face look so punchable. Maybe after a few beatings he'll get better and start listening to real music!"

                        $ hero_mood = "A2"
                        hero "I don't think it's going to change anyone's taste in music."

                    elif a_event_0 < 4/8:  # Variation 4: potential ally
                        $ wdel_mood = "A2"
                        wdel "This dude is actually pretty good at spotting when teachers are coming.{w=[wt4]} Probably developed that sixth sense from all his creeping around.{w=[wt3]} Makes him decent lookout material, if you can stand being near him."
                        
                        $ hero_mood = "A2"
                        hero "I hadn't thought about that."
                        
                        $ wdel_mood = "A1"
                        wdel "Yeah, used him once when {nm}[fnamewuza]{/nm} and I were skipping class to get food.{w=[wt3]} Told him to text us if the teacher headed our way.{w=[wt4]} He came through!{w=[wt3]} 'Course, I had to threaten to pound him if he didn't, but still... not completely useless, ya hear?"

                    else:
                        $ wdel_mood = "A1"
                        wdel "Heh...!{w=[wt2]} Gotta respect that dude, ya hear?{w=[wt3]} Most guys would cry or run to their mommies when they feel my fists.{w=[wt3]} But he doesn't only takes all with a smile on his face, but also keeps coming back for more!{w=[wt3]} That's the kinda grit I can respect, bro."
                        
                        $ hero_mood = "A2"
                        hero "Maybe the smile in his face is that he sees or feels something else while you're beating him, don't you think?"
                        
                        $ wdel_mood = "A3"
                        wdel "Yeah{w=[wt2]}, Probably the adrenaline rush or something.{w=[wt4]} Some people are just into that thrill of getting their ass kicked and surviving, ya know?{w=[wt3]} Like those extreme sports nuts, but without any actual skills."
                        
                        $ wdel_mood = "A1" 
                        wdel "Maybe he's trying to toughen up!{w=[wt3]} That's how real men are, always wanting to prove they can handle shit.{w=[wt4]} He probably thinks if he can stand up to me, he'll earn some street cred or something.{w=[wt3]} Heh{w=[wt2]}, it's not like he's wrong, of course!"
                        
                        $ hero_mood = "A1"
                        hero "R{w=[wt1]}-right{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} that must be it."

                # WUZA
                "{image=icon_wuza} {nm}[fnamewuza]{/nm}" if not "Talk_Char_WUZA" in wdel_know:
                    $ wdel_know.append("Talk_Char_WUZA")

                    if not "WDEL_BG_WUZA_1" in hero_know:
                        $ hero_know.append("WDEL_BG_WUZA_1")
                        $ msg.msg(renpy.translate_string("You know {nm}[fnamewdel]{/nm} a little more"))
                        $ add_stat("wdel", "inti", 1)

                        $ hero_mood = "A2"
                        hero "Hey, you and {nm}[fnamewuza]{/nm} seem to know each other pretty well."
                        
                        $ wdel_mood = "A3"
                        wdel "That giant goofball?{w=[wt3]} Yeah, we go way back{w=[wt2]}, ya hear?{w=[wt4]} Grew up in the same crappy neighborhood.{w=[wt3]} Been causin' trouble together since we were tiny brats.{w=[wt3]} So{w=[wt2]}, yeah!{w=[wt3]} I've been putting up with that hysterical voice screaming in my ear all this time!"
                        
                        $ hero_mood = "A2"
                        hero "You two seem really close. I doubt you'd even mind anything she does these days."
                        
                        $ hero_mood = "A1"
                        $ wdel_mood = "A1"
                        wdel "{gg}Heh!{/gg}{w=[wt2]} You're right.{w=[wt3]} {nm}[fnamewuza]{/nm}'s been through some rough stuff.{w=[wt3]} Still, just kept that crazy energy going. Even when she's bein' extra loud or breakin' stuff.{w=[wt3]} Girl's earned the right to make some noise.{w=[wt3]} Anyone gives her crap about it has to answer to me!"
                        
                    else:
                        $ hero_mood = "A2"
                        hero "What do you think of {nm}[fnamewuza]{/nm}?"

                        $ a_event_0 = renpy.random.random()

                        if a_event_0 < 0.3 and wdel_inti >= char_inti_cap/2 and wuza_love >= char_inti_cap/2:
                           $ wdel_mood = "A1"
                           wdel "She's got more energy than sense, I swear!{w=[wt3]} We've been tight since we were kids.{w=[wt4]} She's the only one who can keep up with me, ya hear?{w=[wt3]} Though sometimes I wish she'd turn the volume down a notch."

                           $ hero_mood = "A2"
                           hero "She is pretty loud, isn't she?"

                           $ wdel_mood = "A3"
                           wdel "LOUD?{w=[wt3]} Dude, that's putting it mildly!{w=[wt4]} When we were ten, she cheered so hard at my first drum performance that she got us both kicked out!{w=[wt3]} I was pissed at first, but then we spent the afternoon throwing rocks at abandoned cars instead.{w=[wt4]} Best day ever!"

                           $ hero_mood = "A2"
                           hero "Sounds like you two have a lot of history."

                           $ wdel_mood = "A2"
                           wdel "More than I can count, bro.{w=[wt3]} Don't tell her I said this, but{w=[wt2]}... she's the only one who stuck around when everyone else thought I was just trouble.{w=[wt4]} Girl's loyal to a fault."

                        elif a_event_0 < 0.6 and wdel_inti >= char_inti_cap/2 and wuza_love >= char_inti_cap/2:
                           $ wdel_mood = "A1"
                           wdel "Hmph! I tried to teach this wild animal how to play the drums, and the miserable  ended up breaking my drumsticks. Then she looks at me like an idiot and says, 'Oops, my bad!' My bad, my ass! You're gonna sell your body to buy me a new one!"

                           $ hero_mood = "A2"
                           hero "She seems to break things a lot, doesn't she?"

                           $ wdel_mood = "A3"
                           wdel "You have NO idea, dude!{w=[wt3]} That girl's like a walking natural disaster!{w=[wt4]} But I gotta admit{w=[wt2]}, it's freakin' hilarious watching her try to be careful.{w=[wt3]} Her face gets all scrunched up with concentration{w=[wt2]}, and then {aw}BOOM!{/aw}{w=[wt3]} Something else bites the dust!"

                           $ hero_mood = "A4"
                           hero "Haha, I can imagine that!"

                           $ wdel_mood = "A1"
                           wdel "Yeah{w=[wt2]}, can't stay mad at her for long.{w=[wt3]} Just don't tell her I said that{w=[wt2]}, ya hear?{w=[wt3]} I still want those new drumsticks!"

                        elif a_event_0 < 0.7:
                           $ wdel_mood = "A1"
                           wdel "{gg}Heh!{/gg} She's the only woman who can handle a fight with me!"

                           $ hero_mood = "O1"
                           hero "You two actually fight each other?"

                           $ wdel_mood = "A3"
                           wdel "Fuck yeah we do!{w=[wt3]} It's how we show friendship{w=[wt2]}, ya hear?{w=[wt4]} Most people think I'm the tough one{w=[wt2]}, but {nm}[fnamewuza]{/nm}?{w=[wt3]} She's got raw power that's straight-up scary.{w=[wt3]} I'm just quicker on my feet and know how to talk my way outta trouble.{w=[wt3]} She just barrels through it!"

                           $ hero_mood = "A2"
                           hero "Sounds like you respect her a lot."

                           $ wdel_mood = "O1"
                           wdel "Tch!{w=[wt3]} Don't go gettin' all sappy on me, you wimp!"

                        elif a_event_0 < 0.8:
                           $ wdel_mood = "A3"
                           wdel "Oh man{w=[wt2]}, me and {nm}[fnamewuza]{/nm} go WAY back!{w=[wt3]} We've gotten into so much shit together{w=[wt2]}, it's crazy!{w=[wt4]} This one time{w=[wt2]}, we were like twelve{w=[wt2]}, and we decided to sneak into this abandoned factory near our neighborhood."

                           $ hero_mood = "A2"
                           hero "That sounds dangerous. What happened?"

                           $ wdel_mood = "A3"
                           wdel "Oh, it was AWESOME!{w=[wt3]} We found this huge empty space that echoed like crazy.{w=[wt4]} I started banging on some old metal pipes{w=[wt2]}, and {nm}[fnamewuza]{/nm} just went WILD{w=[wt2]}, jumping and climbing everything!{w=[wt4]} Then she accidentally knocked over this rusty shelf and{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} BOOM!{w=[wt3]} Whole place started coming down around us!"

                           $ hero_mood = "O1"
                           hero "Holy crap! Were you guys okay?"

                           $ wdel_mood = "A4"
                           wdel "{lg}Hell yeah!{/lg}{w=[wt3]} We ran outta there like our asses were on fire!{w=[wt4]} My old man grounded me for a month when I got home covered in dirt and rust.{w=[wt3]} But it was totally worth it!{w=[wt4]} Still gives me a rush thinking about it.{w=[wt3]} That girl's always down for adventure{w=[wt2]}, ya hear?"

                        elif a_event_0 < 0.9:
                           $ wdel_mood = "O1"
                           wdel "This girl would be a good rock vocalist with the vocal power she has! It's a shame she prefers to listen to trash!"

                           $ hero_mood = "A2"
                           hero "Oh yeah? What kind of music does she like?"

                           $ wdel_mood = "O2"
                           wdel "Ugh{w=[wt2]}, all that poppy workout garbage with no soul!{w=[wt3]} Just beats to get pumped up to.{w=[wt4]} I've been tryin' to educate her on real music for YEARS{w=[wt2]}, ya hear?{w=[wt3]} Played her some classic rock, metal, punk{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} stuff with actual meaning!"

                           $ hero_mood = "A2"
                           hero "Oh, electronic music, right?"

                           $ wdel_mood = "O2"
                           wdel "Yeah, that garbage!{w=[wt3]} All 'untz untz untz' and no substance!{w=[wt4]} I swear, every time we hang out, it's a battle for the playlist.{w=[wt3]} But I gotta admit{w=[wt2]}, when she belts out lyrics, even to her crappy songs{w=[wt2]}...{w=[wt3]} damn, the girl's got pipes!{w=[wt4]} Could be fronting a hardcore band if she wasn't so obsessed with sports and protein shakes."

                           $ hero_mood = "A2"
                           hero "Maybe you could convince her to try singing something different?"

                           $ wdel_mood = "A1"
                           wdel "Been tryin' for years, bro.{w=[wt3]} One day I'll wear her down.{w=[wt4]} We'd make a killer band together{w=[wt2]}, me on drums, her belting it out.{w=[wt3]} Just gotta fix her taste in music first!"

                        else:
                           $ wdel_mood = "A1"
                           wdel "She's my partner in crime{w=[wt2]}, bro!{w=[wt3]} She's always up for anything wild.{w=[wt3]} That's why we click so well.{w=[wt3]} Most people can't keep up with us."

                           wdel "We go way back, ya know?{w=[wt3]} Same neighborhood, same old school.{w=[wt3]} She's like this human tornado that just powers through everything.{w=[wt3]} Breaks stuff without even trying, but her heart's solid gold."

                           $ hero_mood = "A1"
                           hero "Sounds like you two have a lot of fun together."

                           $ wdel_mood = "A4"
                           wdel "Hell yeah we do!{w=[wt3]} You should've seen us at the arcade last weekend.{w=[wt3]} She got so pumped playing that boxing game she actually punched through the machine!{w=[wt4]} The owner was pissed, but it was epic!{w=[wt3]} Had to drag her outta there before she challenged him to an actual fight, got it?"

                           $ hero_mood = "A2"
                           hero "She seems really... energetic."

                           $ wdel_mood = "A1"
                           wdel "That's putting it mildly!{w=[wt3]} One time, she got so pumped during gym that she accidentally broke the volleyball net.{w=[wt3]} Just RIPPED it down celebrating a point!{w=[wt4]} The coach wasn't even mad, just impressed."

                "Return":
                    jump wdel_interact_chat

        "Return":
            jump wdel_interact

    $ add_stat("wdel", "inti", 0.2)
    $ gametimemin += 20
    jump wdel_interact_check

# ----------------------------------------------------------------------------------------------------
# Character Initiative
# ----------------------------------------------------------------------------------------------------
label initiative_wdel:
    $ wdel_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------------------------------------------------------------------------------------------------
    # Ask if HERO ever dated
    # ----------------------------------------------------------------------------------------------------
    if renpy.random.random() < (wdel_inti*0.02) and not any(get_id.startswith("HERO_Dated") for get_id in wdel_know):

        $ wdel_mood = "A1"
        wdel "Hey{w=[wt2]}, bro.{w=[wt3]} Have you ever hooked up with a chick?"

        $ hero_fx = 1
        $ hero_mood = "A2"
        menu:
            wdel "Hey{w=[wt2]}, bro.{w=[wt3]} Have you ever hooked up with a chick?{fast}"
            
            "Deny":
                $ wdel_know.append("HERO_Dated_N")
                $ msg.msg(renpy.translate_string("{nm}[fnamewdel]{/nm} knows you a little more"))
                $ add_stat("wdel", "inti", 0.5)

                hero "N{w=[wt1]}-no{w=[wt2]}, not really..."

                $ wdel_mood = "A4"
                wdel "{lg}GAH HA HA HA!{/lg}{w=[wt3]} No fuckin' way!{w=[wt3]} What a loser!"

                $ hero_mood = "O2"
                hero "{aw}H{w=[wt1]}-hey...!{/aw}"
                
                $ wdel_mood = "A1"
                wdel "Just kidding, bro!{w=[wt3]} Y'know{w=[wt2]}, it's not like it's a big deal, right?{w=[wt3]} All that relationship bullshit just slows you down.{w=[wt3]} Most people are too fuckin' boring anyway. Besides{w=[wt2]}, look at the chumps around here who think they're players.{w=[wt3]} Half of 'em couldn't find a girl's sweet spot with a fuckin' GPS.{w=[wt3]} At least you're a honest loser!"

            "Confirm":
                $ wdel_know.append("HERO_Dated_Y")
                $ msg.msg(renpy.translate_string("{nm}[fnamewdel]{/nm} knows you a little more"))
                $ add_stat("wdel", "inti", 0.5)

                hero "Y{w=[wt1]}-yeah{w=[wt2]}, I've dated before."

                $ wdel_mood = "A3"
                wdel "No shit?{w=[wt3]} You actually convinced someone to put up with your ass?{w=[wt1]} {lg}GAH HA HA HA!{/lg}"

                $ hero_mood = "O2"
                hero "{aw}H{w=[wt1]}-hey...!{/aw}"
                
                $ wdel_mood = "A1"
                wdel "All that relationship crap is for suckers anyway.{w=[wt3]} Gets in the way of actually living, ya hear?{w=[wt3]} Just drama and bullshit.{w=[wt3]} Better to keep it simple.{w=[wt3]} No strings{w=[wt2]}, no expectations{w=[wt2]}, nobody getting all clingy and weird.{w=[wt3]} But hey{w=[wt2]}, you actually dated someone.{w=[wt3]} So maybe you're not as soft as you look."

            "Don't choose":
                jump initiative_wdel_return

    # ----------------------------------------------------------------------------------------------------
    # Ask HERO's girl preference
    # ----------------------------------------------------------------------------------------------------
    elif renpy.random.random() < (wdel_inti*0.02) and sum(1 for get_id in wdel_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wdel_know if get_id.startswith("HERO_N_Girl")) < 4:
        $ wdel_mood = "A4"
        wdel "Hey, straight up{w=[wt2]}, what kinda chick gets your engine runnin'?{nw}"

        menu:
            wdel "Hey, straight up, what kinda chick gets your engine runnin'?{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in wdel_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in wdel_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in wdel_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in wdel_know if "Personality_" in get_id)

                # Appearance Likes(Y)/Dislikes(N)
                $ a_event_1 = wdel_know
                $ a_event_3 = "initiative_wdel_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_2

                # Store the answer if one was given
                if _return:
                    $ wdel_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg(renpy.translate_string("{nm}[fnamewdel]{/nm} knows you a little more"))
                $ add_stat("wdel", "inti", 0.5)

                if _return in ["Personality_4", "Breast_2", "Breast_3", "HairSize_2", "HairSize_3", "Personality_1"]: # Match - aggressive, medium breasts, short hair, energetic
                    $ add_stat("wdel", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ wdel_mood = "A4"
                    wdel "{lg}GAH HA HA HA!{/lg}{w=[wt3]} Look at you, not as much of a pussy as I thought!{w=[wt3]} Got some actual taste!"

                elif _return in ["Personality_6", "Personality_8", "Breast_0", "Breast_1", "HairSize_5", "HairSize_6"]: # Opposite match - shy/timid, chaste, flat/tiny breasts, long hair
                    $ add_stat("wdel", "bonus", -10)
                    $ wdel_mood = "O1"
                    wdel "Tch!{w=[wt3]} Seriously?{w=[wt3]} That's what you're into?{w=[wt3]} Man, no accounting for taste, ya hear?"

                else: # Others
                    $ wdel_mood = "A1"
                    wdel "Not bad, I guess.{w=[wt3]} Kinda basic, but whatever floats your boat, right?"

            "Don't choose":
                jump initiative_wdel_return

    # ----------------------------------------------------------------------------------------------------
    # No question was chosen
    # ----------------------------------------------------------------------------------------------------
    else:
        $ wdel_mood = "A2"
        $ a_event_0 = renpy.random.random()
        
        if a_event_0 < 1/4:
            wdel "Actually{w=[wt2]}, nevermind.{w=[wt3]} Just had a stupid question.{w=[wt2]} Forget about it."
        elif a_event_0 < 2/4:
            wdel "Yo{w=[wt2]}, wanna hear somethin' crazy?{w=[wt3]} Ah, forget it.{w=[wt3]} You probably wouldn't get it anyway."
        elif a_event_0 < 3/4:
            wdel "Was gonna ask something but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Fuck it.{w=[wt3]} Let's talk about something else."
        else:
            wdel "You ever just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Nah, forget it.{w=[wt3]} Not important right now."

        jump wdel_interact

    # ----------------------------------------------------------------------------------------------------
    # Question ended
    # ----------------------------------------------------------------------------------------------------
    $ gametimemin += 20
    $ add_stat("wdel", "inti", 0.20)
    jump wdel_interact_check

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wdel_return:

    call hero_n_answer from _call_hero_n_answer_2

    $ wdel_mood = "O1"
    $ a_event_0 = renpy.random.random()
    
    if a_event_0 < 1/5:
        wdel "Tch!{w=[wt2]} Asshole!"
        
    elif a_event_0 < 2/5:
        wdel "Oh{w=[wt2]}, so fuck you!"
        
    elif a_event_0 < 3/5:
        wdel "C'mon!{w=[wt2]} Just spit it out already!"
        
    elif a_event_0 < 4/5:
        wdel "Hmph!{w=[wt2]} Whatever, asshole!"
        
    else:
        wdel "{aw}Ehhh...?{/aw}{w=[wt3]} What a asshole you are, dude!"
    
    
    jump wdel_interact
