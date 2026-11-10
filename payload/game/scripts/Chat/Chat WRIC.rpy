# ----------------------------------------------------------------------------------------------------
# Load sprite
# ----------------------------------------------------------------------------------------------------
label wric_show:

    if wric_love < 0:
        $ wric_mood = "O1"
    elif wric_love < 30:
        $ wric_mood = "A1"
    elif wric_love < 60:
        $ wric_mood = "A1"

    $ hero_mood = "A1"
    call npc_lust from _call_npc_lust_11

    show WRIC at RC
    show HERO at LC
    with dissolve

    return

# ----------------------------------------------------------------------------------------------------
# Load activity
# ----------------------------------------------------------------------------------------------------
label wric_show_activity:
    $ msg.msg("[C_Nam][fnamewric][C_Off] is " + str(Get_ActivityName("wric")))

    if Get_ActivityName("wric") in ["at class"]:
        jump show_ui

    else:
        return

# ----------------------------------------------------------------------------------------------------
# End chat
# ----------------------------------------------------------------------------------------------------
label wric_interact_end:
    if "interacting_hero" in wric_know:
        $ wric_know.remove("interacting_hero")
        $ msg.msg("Finish talking")
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Start chat
# ----------------------------------------------------------------------------------------------------
label wric_interact_start:
    call hide_ui from _call_hide_ui_78
    call wric_show_activity from _call_wric_show_activity
    $ wric_inti = min(char_inti_cap, wric_inti)
    call hide_ui from _call_hide_ui_79
    call wric_show from _call_wric_show

# ----------------------------------------------------------------------------------------------------
# Check Conditions
# ----------------------------------------------------------------------------------------------------
label wric_map_check:
    # ----------------------------------------------------------------------------------------------------
    # Is in same map
    # ----------------------------------------------------------------------------------------------------
    if hero_map == wric_map:
        pass

# ----------------------------------------------------------------------------------------------------
# Check Interaction
# ----------------------------------------------------------------------------------------------------
label wric_interact_check:
    # Save current outfit before any updates
    $ wric_wear_keep = wric_wear

    call gametime from _call_gametime_37
    call hide_ui from _call_hide_ui_80

    # Check if outfit changed during time update - if so, keep the previous one, so the character does not change outfit in front of the player
    if wric_wear != wric_wear_keep:
        $ wric_wear = wric_wear_keep

    call wric_show from _call_wric_show_1
    $ a_event_0 = 0
    $ a_event_1 = 0

    # ----------
    # Is Unavailable
    # ----------
    if gametimehour >= 18:
        if wric_love <= 0:
            $ wric_mood = "O1"
            wric "Finally{w=[wt2]}, a reason to leave.{w=[wt3]} Try not to miss me too much{w=[wt2]}, though I'm sure you will."

        elif wric_love < 10:
            $ wric_mood = "O1"
            wric "Ugh{w=[wt2]}, how dreadful.{w=[wt3]} I suppose I must attend to other matters now.{w=[wt3]} Do try to contain your disappointment at my departure."

        elif wric_love < 50:
            $ wric_mood = "O1"
            wric "Hmph!{w=[wt3]} As much as this conversation isn't entirely terrible{w=[wt2]}, I really must be going.{w=[wt3]} Such is the burden of my social obligations."

        elif wric_love < 80:
            $ wric_mood = "O1"
            wric "W{w=[wt1]}-wait{w=[wt2]}, is it that time already?{w=[wt3]} How annoying{w=[wt2]}, I was actually enjoying our chat.{w=[wt4]} I'll talk to you next time{w=[wt2]}, okay?{w=[wt3]} Good bye!"

        else:
            $ a_event_0 = renpy.random.random()
            $ wric_mood = "O1"
            if a_event_0 < 1/3:
                wric "No{w=[wt2]}, no{w=[wt2]}, no!{w=[wt3]} This is so unfair!{w=[wt3]} Why must I leave just now...?{w=[wt4]} Hmph!{w=[wt2]} You better come find me later{w=[wt2]}, {nm}[fnamehero]{/nm}!"
            elif a_event_0 < 2/3:
                wric "I can't believe I have to go now.{w=[wt3]} This is simply tragic!{w=[wt3]} You will come see me again soon{w=[wt2]}, won't you{w=[wt2]}, {nm}[fnamehero]{/nm}?{w=[wt3]} Promise me!"
            else:
                wric "Hmph!{w=[wt3]} If only you'd come earlier{w=[wt2]}, we could have spent more time together.{w=[wt3]} This is entirely your fault{w=[wt2]}, you know?{w=[wt3]} You'll have to make it up to me next time!"

        $ hero_fx = 0
        jump wric_interact_end

    # ----------------------------------------------------------------------------------------------------
    elif Check_TimeStr("school_class") and Get_MapName("wric", "at class"): # Class Time
    # ----------------------------------------------------------------------------------------------------
        if Check_CharSameMap("hero", "wric"):
            $ wric_mood = "O1"
            wric "Ugh{w=[wt2]}, how dreadful.{w=[wt3]} Class is starting.{nw}"

            show WRIC at RC
            show WRIC at OR_slow
            wric "Ugh{w=[wt2]}, how dreadful.{w=[wt3]} Class is starting.{fast}{w=[wt2]} {bt}Shoo...!{/bt}"

            jump wric_interact_end

        else:
            $ wric_mood = "A1"
            wric "It's time for class.{w=[wt3]} Hurry.{w=[wt2]} You'll walk me there."

            if Get_MapName("wric", "at class") == Get_MapName(None, "school", "class_1b"):
                menu:
                    "Go together":
                        $ hero_mood = "A2"
                        hero "Sure{w=[wt2]}, let's go."
                        
                        $ wric_mood = "A2"
                        $ wric_fx = 1
                        wric "Just don't take advantage of my kindness and keep a good distance."
                        
                        scene bg_0
                        with dissolve

                        $ hero_map = wric_map
                        call gametime from _call_gametime_38
                        call check_playermap from _call_check_playermap_20
                        call hide_ui from _call_hide_ui_81
                        show WRIC at RC
                        show HERO at LC
                        with dissolve
                        
                        $ wric_mood = "A1"
                        wric "There.{w=[wt2]} You may leave now.{w=[wt3]} I must prepare myself for the tedium ahead."

                        jump wric_interact_end
                        
                    "Let her go":
                        pass
            
            $ hero_mood = "A1"
            hero "I have something to do first."

            $ wric_mood = "O3"
            $ wric_fx = 1
            wric "W{w=[wt1]}-what!?{w=[wt3]} You're refusing to accompany me?{w=[wt3]} How{w=[wt2]}, how dreadful!{nw}"
            
            $ wric_mood = "O2"
            wric "W{w=[wt1]}-what!?{w=[wt3]} You're refusing to accompany me?{w=[wt3]} How{w=[wt2]}, how dreadful!{fast}{w=[wt4]} Hmph...!{w=[wt3]} I suppose I can't expect proper manners from{w=[wt2]}, from commoners!{w=[wt3]} How utterly disappointing!"
            
            show WRIC at RC
            show WRIC at OR_average
            pause(1.5)

        jump wric_interact_end

    # ----------------------------------------------------------------------------------------------------
    # WRIC is at School - Courtyard
    # ----------------------------------------------------------------------------------------------------
    elif Check_CharInMap("hero", "school", "courtyard") and Get_ActivityName("wric") in ["eating"]:
        "{nm}[fnamewric]{/nm} is spending time at a courtyard table{nw}"
        menu:
            "{nm}[fnamewric]{/nm} is spending time at a courtyard table{fast}"
            "Join her":
                call circletable("wric") from _call_circletable_9

                while Get_ActivityName("wric") in ["eating"]:
                    $ a_event_1 = gametimehour
                    $ a_event_2 = gametimemin + 10
                    call gametime_wait(a_event_1, a_event_2) from _call_gametime_wait_12
                call gametime from _call_gametime_39

                jump wric_interact_start

            "Return":
                jump wric_interact_end

    # ----------
    # Comment After An Interaction
    # ----------
    elif "interacting_hero" in wric_know:
        $ a_event_0 = renpy.random.random()

        # ----------
        # Bring Up A Topic
        # ----------
        if renpy.random.random() < (0.2 + (wric_love * 0.003)):
            jump initiative_wric

        # ----------
        # Common
        # ----------
        elif wric_love < 10:
            if a_event_0 < 1/9:
                wric "I suppose you require more of my precious time?"
            elif a_event_0 < 2/9:
                wric "Do make it quick.{w=[wt3]} My time is far too valuable to waste."
            elif a_event_0 < 3/9:
                wric "Hmph!{w=[wt3]} What else do you want?"
            elif a_event_0 < 4/9:
                $ wric_mood = "O1"
                wric "I suppose you still want to chat a little more.{w=[wt3]} Not that I care{w=[wt2]}, but do try not to waste too much of my time."
            elif a_event_0 < 5/9:
                $ wric_mood = "O1"
                wric "So{w=[wt2]}, what else could you possibly want?{w=[wt3]} Though I suppose I can spare another moment{w=[wt2]}, if you insist."
            elif a_event_0 < 6/9:
                $ wric_mood = "O1"
                wric "Hmph.{w=[wt3]} Fine{w=[wt2]}, I can give you a little bit more of my time{w=[wt2]}, but know I have important matters to attend to."
            elif a_event_0 < 7/9:
                $ wric_mood = "O1"
                wric "Well{w=[wt2]}, I guess you can stay{w=[wt2]}, since you enjoy my presence so much."
            elif a_event_0 < 8/9:
                wric "Well{w=[wt2]}, I suppose I can spare a few more moments."
            else:
                wric "Hmph.{w=[wt3]} I do hope this is worth my time."

        elif wric_love < 50:
            if a_event_0 < 1/6:
                $ wric_mood = "A1"
                wric "Well{w=[wt2]}, I suppose your company isn't entirely terrible."
            elif a_event_0 < 2/6:
                $ wric_mood = "A1"
                wric "I suppose I could give you a little more of my time{w=[wt2]}, since you seem so eager."
            elif a_event_0 < 3/6:
                $ wric_mood = "A1"
                wric "You know{w=[wt2]}, you're not as bothersome as most people of school."
            elif a_event_0 < 4/6:
                $ wric_mood = "A1"
                wric "Well{w=[wt2]}, I suppose your company isn't completely dreadful."
            elif a_event_0 < 5/6:
                wric "Yes{w=[wt2]}, what else would you like to discuss?"
            else:
                wric "At least you know how to maintain a decent conversation."

        elif wric_love < 80:
            if a_event_0 < 1/5:
                $ wric_mood = "A1"
                wric "So{w=[wt2]}, what would you like to talk about now?"
            elif a_event_0 < 2/5:
                $ wric_mood = "A1"
                wric "So{w=[wt2]}, what more would you want me to tell you?"
            elif a_event_0 < 3/5:
                $ wric_mood = "A1"
                wric "You know{w=[wt2]}, you're quite good at listening.{w=[wt3]} Most people don't appreciate my stories properly."
            elif a_event_0 < 4/5:
                wric "Your company is{w=[wt2]}, surprisingly{w=[wt2]}, quite pleasant."
            else:
                $ wric_mood = "A1"
                wric "You know{w=[wt2]}, I'm glad you're someone who understands the value of proper conversation!"

        else:
            if a_event_0 < 1/4:
                $ wric_mood = "A1"
                wric "Don't you dare think of leaving yet{w=[wt2]}, {nm}[fnamehero]{/nm}!{w=[wt3]} I have so much more to share with you!"
            elif a_event_0 < 2/4:
                $ wric_mood = "A1"
                wric "You'll stay longer{w=[wt2]}, won't you?{w=[wt3]} It's so rare to find someone who truly appreciates my company."
            elif a_event_0 < 3/4:
                $ wric_mood = "A1"
                wric "You know{w=[wt2]}, most people would give anything for more time with me{w=[wt2]}, so you better appreciate this moment!"
            else:
                $ wric_mood = "A1"
                wric "How cruel would you be to leave me all alone now{w=[wt2]}, {nm}[fnamehero]{/nm}?{w=[wt3]} Stay a bit longer!"

    # ----------
    # Welcum Message
    # ----------
    else:
        $ a_event_0 = renpy.random.random()

        if wric_love <= 0 and 0 > 1: # Unavailable due to lack of interaction options at the moment
            if a_event_0 < 1/3:
                $ wric_mood = "O1"
                wric "Ugh{w=[wt2]}, I don't have time for people like you.{w=[wt3]} Go bother someone else."
            elif a_event_0 < 2/3:
                $ wric_mood = "O1"
                wric "Hmm?{w=[wt2]} I don't wanna talk to someone like you."
            else:
                $ wric_mood = "O1"
                wric "Don't even think about approaching me.{w=[wt3]} I have standards, you know."

            mind "(Wow{w=[wt2]}, she didn't even give me a chance to speak.{w=[wt3]} Maybe the only way to improve my relationship with her for now would be if we had to do some school activity together.)"
            jump wric_interact_end

        elif wric_love < 10:
            if a_event_0 < 1/12:
                $ wric_mood = "O1"
                wric "Oh{w=[wt2]}, it's you again.{w=[wt3]} I suppose you want something?"
            elif a_event_0 < 2/12:
                $ wric_mood = "O1"
                wric "Hmph!{w=[wt3]} Well{w=[wt2]}, since you're already here{w=[wt2]}, what is it?"
            elif a_event_0 < 3/12:
                $ wric_mood = "O1"
                wric "I suppose I can spare a moment{w=[wt2]}, though I can't imagine why you keep bothering me."
            elif a_event_0 < 4/12:
                $ wric_mood = "O1"
                wric "You again?{w=[wt3]} Well{w=[wt2]}, I guess I can tolerate your presence for a bit."
            elif a_event_0 < 5/12:
                wric "Ugh{w=[wt2]}, what do you want?"
            elif a_event_0 < 6/12:
                wric "Oh{w=[wt2]}, it's you again.{w=[wt3]} How... quaint."
            elif a_event_0 < 7/12:
                wric "Hmph!{w=[wt3]} Must you always interrupt my peace?"
            elif a_event_0 < 8/12:
                wric "I do hope you have a good reason for approaching me."
            elif a_event_0 < 9/12:
                wric "Tsk tsk{w=[wt2]}, another commoner seeking my attention."
            elif a_event_0 < 10/12:
                wric "Yes?{w=[wt3]} What is it?"
            elif a_event_0 < 11/12:
                wric "Yes?{w=[wt3]} I suppose you want something?"
            else:
                wric "Hmph!{w=[wt3]} I suppose I can spare a moment for you."

        elif wric_love < 50:
            if a_event_0 < 1/4:
                $ wric_mood = "A1"
                wric "Oh{w=[wt2]}, {nm}[fnamehero]{/nm}.{w=[wt3]} Your timing isn't completely terrible."
            elif a_event_0 < 2/4:
                $ wric_mood = "A1"
                wric "Well{w=[wt2]}, look who's here.{w=[wt3]} I was getting rather bored anyway."
            elif a_event_0 < 3/4:
                $ wric_mood = "A1"
                wric "I suppose I could use some company{w=[wt2]}, even if it's just yours."
            elif a_event_0 < 3/4:
                $ wric_mood = "A1"
                wric "{nm}[fnamehero]{/nm}!{w=[wt3]} I was hoping someone would come by!"
            else:
                $ wric_mood = "A1"
                wric "{nm}[fnamehero]{/nm}!{w=[wt3]} You'll do nicely for some conversation."

        elif wric_love < 80:
            if a_event_0 < 1/8:
                $ wric_mood = "A1"
                wric "{nm}[fnamehero]{/nm}!{w=[wt3]} I was hoping you would come by!"
            elif a_event_0 < 2/8:
                $ wric_mood = "A1"
                wric "Perfect timing!{w=[wt3]} I have so many things to tell you about!"
            elif a_event_0 < 3/8:
                $ wric_mood = "A1"
                wric "Finally{w=[wt2]}, someone worth talking to!{w=[wt3]} Come here{w=[wt2]}, {nm}[fnamehero]{/nm}!"
            elif a_event_0 < 4/8:
                wric "{nm}[fnamehero]{/nm}!{w=[wt3]} Do join me!"
            elif a_event_0 < 5/8:
                wric "{nm}[fnamehero]{/nm}!{w=[wt3]} Simply good to see you!"
            elif a_event_0 < 6/8:
                wric "{nm}[fnamehero]{/nm}! you've arrived at the perfect moment!"
            elif a_event_0 < 7/8:
                wric "Finally{w=[wt2]}, someone worth talking to."

        else:
            if a_event_0 < 1/7:
                $ wric_mood = "A1"
                wric "{nm}[fnamehero]{/nm}!{w=[wt3]} Where have you been!?{w=[wt3]} You shouldn't keep a lady waiting!"
            elif a_event_0 < 2/7:
                $ wric_mood = "A1"
                wric "Finally{w=[wt2]}, you're here!{w=[wt3]} Do you know how lonely it's been without you?"
            elif a_event_0 < 3/7:
                $ wric_mood = "A1"
                wric "Took you long enough to come to talk to me{w=[wt2]}, {nm}[fnamehero]{/nm}!{w=[wt3]} You better make up for your absence!"
            elif a_event_0 < 4/7:
                $ wric_mood = "O1"
                wric "There you are!{w=[wt3]} I was beginning to think you were avoiding me{w=[wt2]}, which would be absolutely unforgivable!!!"
            elif a_event_0 < 5/7:
                $ wric_mood = "A1"
                wric "Oh{w=[wt2]}, {nm}[fnamehero]{/nm}!{w=[wt3]} I was just thinking about calling for you!"
            elif a_event_0 < 6/7:
                wric "I{w=[wt1]}-I was just thinking about you."
            else:
                $ wric_mood = "A1"
                wric "H{w=[wt1]}-hi, {nm}[fnamehero]{/nm}!"

# ----------------------------------------------------------------------------------------------------
# Interact Options
# ----------------------------------------------------------------------------------------------------
label wric_interact:
    call hide_ui from _call_hide_ui_82
    if "interacting_hero" not in wric_know:
        $ wric_know.append("interacting_hero")

    menu:
        "Chat" if not is_specialevent:
            jump wric_interact_chat
        "Touch" if not is_specialevent:
            jump wric_interact_touch
        "Hang out":
            jump wric_interact_hangout
        "Give item" if not is_specialevent:
            jump wric_interact_gift
        "Return":
            jump wric_interact_end

# ----------------------------------------------------------------------------------------------------
# Interact Gift
# ----------------------------------------------------------------------------------------------------
label wric_interact_gift:
    $ a_item_8 = "wric"
    $ a_item_9 = 0
    $ a_item_6 = "wric_interact"
    call UI_give_Item from _call_UI_give_Item_12

label wric_interact_gift_receive(reaction):
    $ gametimemin += 5
    jump wric_interact

# ----------------------------------------------------------------------------------------------------
# Interact Touch
# ----------------------------------------------------------------------------------------------------
label wric_interact_touch:
    menu:
        "Hug":
            label wric_interact_touch_hug:
                pass

            $ wric_know.append("Hug")
            $ a_event_0 = sum(1 for buceta in wric_know if buceta =="Hug")
            $ wric_fx = 1

            $ a_event_1 = renpy.random.random()
            if a_event_1 <= 0.33:
                scene bg_2 pink
            elif a_event_1 <= 0.66:
                scene bg_2 yellow
            else:
                scene bg_2 flowers

            show action_wric_hug 1a
            with dissolve

            show action_wric_hug 1b

            $ add_stat("wric", "love", 2/a_event_0)
            $ add_stat("hero", "cha_sex", 2/a_event_0)

            $ a_event_0 = renpy.random.random()
            if a_event_0 <= 0.25:
                wric "W{w=[wt1]}-what do you think you're doing?"
            elif a_event_0 <= 0.50:
                wric "S{w=[wt1]}-stop!{w=[wt3]} How utterly presumptuous!"
            elif a_event_0 <= 0.75:
                wric "Such impropriety!"
            else:
                wric "This is highly irregular!{w=[wt2]} My personal space costs more than your entire wardrobe, you know."

            show action_wric_hug 1a with None

        "Return":
            jump wric_interact

    call gamecheck from _call_gamecheck_16
    call hide_ui from _call_hide_ui_83
    call wric_show from _call_wric_show_2
    $ gametimemin += 10
    $ add_stat("wric", "inti", 0.1)
    jump wric_interact_check

# ----------------------------------------------------------------------------------------------------
# Hang Out Options
# ----------------------------------------------------------------------------------------------------
label wric_interact_hangout:
    menu:
        "Return":
            jump wric_interact

    $ gametimemin += 30
    jump wric_interact_check

# ----------
# Dialogue Options
# ----------
label wric_interact_chat:
    menu:
        "Ask how she is" if not "Talk_How" in wric_know:
            $ hero_mood = "A1"
            hero "How are you doing today?"

            if wric_love < 10:
                $ wric_mood = "O1"
                wric "Tsk{w=[wt2]}, how presumptuous of you to inquire about my personal state.{w=[wt3]} Though I suppose I'll humor you{w=[wt2]}, I'm managing quite well without your concern."

            elif wric_love < 50:
                $ wric_mood = "A1"
                wric "Well{w=[wt2]}, since you asked{w=[wt2]}, I suppose I'm doing fine.{w=[wt3]} You know{w=[wt2]}, you're not completely terrible at conversation."
                hero "That's good to hear."
                wric "Of course it is.{w=[wt3]} Though I doubt you truly understand how much work it takes to maintain my standards."

            elif wric_love < 80:
                $ wric_mood = "A1"
                wric "Much better now that you're here to listen to me!{w=[wt3]} You know{w=[wt2]}, it's so hard to find good company these days."
                hero "I'm glad to hear that."
                wric "Of course you are.{w=[wt3]} You know{w=[wt2]}, you're one of the few people who understand me."

            else:
                $ wric_mood = "A1"
                wric "I'm wonderful now that you're here!"
                hero "I'm happy to see you too."
                wric "You better be!{w=[wt3]} You know how dreadfully boring it is without you around?{w=[wt3]} So{w=[wt2]}, don't you dare think of leaving too soon{w=[wt2]}, I have so much to tell you!"

            $ wric_know.append("Talk")
            $ wric_know.append("Talk_How")
            $ add_stat("wric", "love", 0.5)
            $ add_stat("hero", "cha_soc", 0.5)

        "Ask about her prestige at school" if not "Talk_School" in wric_know:
            $ wric_know.append("Talk_School")

            if perk_int_per >= 1 and not "WRIC_BG_PRESIDENT_GGGDAUGHTER" in hero_know:
                $ msg.msg("[C_Pos]Success check for [C_Dat]Perception[C_Off] skill[C_Off]")
                play SE1 "JingleRight.mp3"
                hero "You know{w=[wt2]}, there's something I noticed a while ago.{w=[wt3]} You have the same last name as the president honored on the monument in the school front yard.{w=[wt3]} Is there some degree of kinship between you?"

                $ add_stat("wric", "love", perk_int_per)
                $ add_stat("hero", "cha_soc", perk_int_per)

                $ wric_mood = "A1"
                wric "{bt}Well... Well...{/bt}{w=[wt3]} You really do surprise me sometimes, you know?{w=[wt2]} I have to say I admire how observant you are.{w=[wt4]} Exactly.{w=[wt2]} That man was my great-great-grandfather{w=[wt2]}, the greatest president this country has ever had! He was honored for his education bills!"

                $ hero_know.append("WRIC_BG_PRESIDENT_GGGDAUGHTER")
                $ msg.msg("You know {nm}[fnamewric]{/nm} a little more")
                $ add_stat("wric", "inti", perk_int_per)

                if not "WRIC_BG_SCHOOL_1" in hero_know:
                    hero "Wow{w=[wt2]}, this is really impressive!{w=[wt3]} And to think that I'm talking to the great-great-granddaughter of a president!{w=[wt4]} You must have a great prestige in our school, don't you?"
                    jump wric_interact_chat_WRIC_BG_SCHOOL_1
                else:
                    hero "Wow{w=[wt2]}, this is really impressive!{w=[wt3]} And to think that I'm talking to the great-great-granddaughter of a president!{w=[wt4]} Now I understand why do your family has so much prestige in our school!"
                    jump wric_interact_chat_WRIC_BG_SCHOOL_2

            if not "WRIC_BG_SCHOOL_1" in hero_know:
                $ hero_mood = "A1"
                hero "You seem to have quite the prestige at school, right?"

                label wric_interact_chat_WRIC_BG_SCHOOL_1:
                    if not "WRIC_BG_SCHOOL_1" in hero_know:
                        $ hero_know.append("WRIC_BG_SCHOOL_1")
                        $ msg.msg("You know {nm}[fnamewric]{/nm} a little more")
                        $ add_stat("wric", "inti", 1)

                        $ wric_mood = "A1"
                        wric "Naturally I do!{w=[wt3]} After all{w=[wt2]}, my family has been deeply involved with this institution for generations.{w=[wt4]} Daddy finances this school in addition to my tuition, you know.{w=[wt3]} Many of the school's most important decisions are made with our family's input."
                        
                        $ wric_mood = "A1"
                        wric "For instance{w=[wt2]}, you should be aware that class 1B was planned for new students like you{w=[wt2]}, and 1A for re-enrolled students.{w=[wt3]} I asked Daddy to enroll me in class 1B with the new students{w=[wt2]}, rather than the those utterly annoying people I already know{w=[wt2]}, he arranged everything immediately!"

                        hero "{bt}Ohhhh...!{/bt}{w=[wt2]} So that's why you're in my classroom?"

                        wric "Exactly!{w=[wt3]} He even ensured my dear bestie would sit close to me as I asked!{w=[wt4]} Though I must admit{w=[wt2]}, seeing that some already known weirdos ended up in the same class as me when 1A reached capacity{w=[wt2]}, and that some new weirdos appeared{w=[wt2]}, I almost regretted it!"

                        mind "(I hope she's not talking about me)"
                        
                        $ wric_mood = "O1"
                        wric "After all{w=[wt2]}, in classroom 1A there are still some people who at least know how to act appropriately and treat me well."

            else:
                $ hero_mood = "A1"
                hero "About what you told me before, Your family has a lot of influence here at school, doesn't it?"

                label wric_interact_chat_WRIC_BG_SCHOOL_2:
                    $ wric_mood = "A1"
                    wric "Ah yes{w=[wt2]}, I don't blame you for being so interested in my family influence.{w=[wt3]} I suppose my life seems quite fascinating.{w=[wt4]} As I mentioned{w=[wt2]}, Daddy's influence ensures things run smoothly for those who matter."

                    wric "When I asked Daddy to enroll me in class 1B with the new students{w=[wt2]}, rather than the those utterly annoying people I already know{w=[wt2]}, he arranged everything immediately.{w=[wt4]} He even ensured my dear bestie would sit close to me as I asked!"

                    wric "Though I must say{w=[wt2]}, even with all our influence{w=[wt2]}, it's quite vexing how some rather undesirable elements still managed to end up in our class."

                    mind "(I hope she's not talking about me)"

        "Talk about someone":
            menu:
                "{image=icon_wgal} {nm}[fnamewgal]{/nm}" if not "Talk_Char_WGAL" in wric_know:
                    $ wric_know.append("Talk_Char_WGAL")

                    $ hero_mood = "A2"
                    hero "You and {nm}[fnamewgal]{/nm} seem quite close."

                    $ wric_mood = "A1"
                    wric "Of course we are!{w=[wt3]} She's the only one who truly understands me.{w=[wt3]} {nm}[fnamewgal]{/nm} is my dearest friend here!{w=[wt4]} She's perfect!{w=[wt3]} She's sweet{w=[wt2]}; nice{w=[wt2]}; beautiful{w=[wt2]}; everything!{w=[wt4]} With {nm}[fnamewgal]{/nm}{w=[wt1]}, we share all secrets and dreams!{w=[wt2]} We are besties!"

                    hero "Cool!{w=[wt3]} It's good to know you have such a great friendship!"
                    
                    $ wric_mood = "A1"
                    wric "Of course you would find it good.{w=[wt3]} Not everyone is worthy of meeting someone like that.{w=[wt3]} Obviously I am!{w=[wt3]} Unlike most people in the school.{w=[wt3]} {aw}Ugh!{/aw}{w=[wt2]} It seems like they don't know how to put themselves in their shoes!{w=[wt4]} But I hope someone like you can one day have a friend at her level."

                    hero "S{w=[wt1]}-sure.{w=[wt3]} Thank you{w=[wt2]}, I guess."

                "{image=icon_wdis} {nm}[fnamewdis]{/nm}" if "WRIC_BG_SCHOOL_1" in hero_know and not "Talk_Char_WDIS" in hero_know:
                    $ wric_know.append("Talk_Char_WDIS")
                    $ hero_mood = "A2"
                    hero "{nm}[fnamewdis]{/nm} is a re-enrolled student just like you, isn't she?{w=[wt3]} Don't you two get along?"

                    $ wric_mood = "O1"
                    wric "Ugh{w=[wt2]}, that girl{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Why did you ask about such human disaster?{w=[wt3]} If she's so shameless as to show her panties to everyone{w=[wt2]}, she should at least lose weight!"
                    wric "You know what?{w=[wt2]} Someone like her should just look in the mirror and simply stop appearing in front of people!{w=[wt3]} Disgusting!{w=[wt3]} Really{w=[wt2]}, I wonder if any man would really be enchanted by a person so devoid of manners and beauty."

                "{image=icon_wota} {nm}[fnamewota]{/nm}" if "WRIC_BG_SCHOOL_1" in hero_know and not "Talk_Char_WOTA" in hero_know:
                    $ wric_know.append("Talk_Char_WOTA")
                    $ hero_mood = "A2"
                    hero "{nm}[fnamewota]{/nm} is a re-enrolled student just like you, isn't she?{w=[wt3]} Don't you two get along?"

                    $ wric_mood = "O1"
                    wric "That weirdo?{w=[wt3]} I just want to stay away from that kind{w=[wt2]}, what if it's contagious?{w=[wt3]} Honestly{w=[wt2]}, I think these kind of people should just grow up and stop acting like children."
                    wric "And on top of that{w=[wt2]}, she has no shame!{w=[wt3]} She keeps reading these{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} these{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} lewd stories in public!{w=[wt4]} Seriously{w=[wt2]}, this girl is completely disgusting!"

                "{image=icon_wsis} {nm}[fnamewsis]{/nm}" if not "Talk_Char_WSIS" in wric_know:
                    $ wric_know.append("Talk_Char_WSIS")

                    if not "WRIC_BG_WSIS_1" in hero_know:
                        $ hero_know.append("WRIC_BG_WSIS_1")
                        $ msg.msg("You know {nm}[fnamewric]{/nm} a little more")
                        $ add_stat("wric", "inti", 1)

                        $ hero_mood = "A2"
                        hero "I've noticed you and {nm}[fnamewsis]{/nm} don't seem to get along very well."

                        $ wric_mood = "O1"
                        wric "There's NO WAY I can get along with someone like her!{w=[wt3]} SHE IS THE WORST!{w=[wt4]} B{w=[wt1]}-but she's the one who has a problem with me.{w=[wt3]} I've done nothing to deserve such hostility!"

                        $ hero_mood = "A2"
                        hero "Well{w=[wt2]}, d{w=[wt1]}-do you mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} More than her normal?"
                        wric "Hunf!{w=[wt2]} You don't know anything!{w=[wt3]} But really{w=[wt2]}, I'd rather not discuss her.{w=[wt3]} It's quite unpleasant just thinking about this kind of person!"

                    elif not "WRIC_BG_WSIS_2" in hero_know:
                        if not (wric_inti >= min(20, char_inti_cap)) or not (wric_love >= 25):
                            $ wric_mood = "O1"
                            wric "Didn't I already tell you I don't wish to discuss that person?{w=[wt3]} Please respect my wishes on this matter."
                            if not (wric_inti >= min(20, char_inti_cap)):
                                mind "(She doesn't seem to feel close enough to me to have this kind of conversation.)"
                            elif not (wric_love >= 25):
                                mind "(She doesn't seem to like me enough to have this kind of conversation.)"

                        else:
                            $ hero_know.append("WRIC_BG_WSIS_2")
                            $ msg.msg("You know {nm}[fnamewric]{/nm} a little more")
                            $ add_stat("wric", "inti", 1)

                            $ hero_mood = "O1"
                            hero "I'm sorry to bring this up again, but I really want to understand what happened between you two."

                            $ wric_mood = "O1"
                            wric "You're quite persistent{w=[wt2]}, aren't you?{w=[wt3]} *sigh*{w=[wt3]} Fine.{w=[wt3]} If you must know{w=[wt2]}, I actually tried to be her friend once."
                            wric "But do you know what she did?{w=[wt3]} She threatened me!{w=[wt3]} Actually threatened me with physical violence!{w=[wt3]} Can you imagine?"
                            wric "And that's not even the worst part.{w=[wt3]} She's completely untrustworthy.{w=[wt3]} Just ask {nm}[fnamewgal]{/nm} about how she betrayed her trust{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}"
                            hero "{bt}Ehhh...?{/bt} What do you mean by that?"
                            $ wric_mood = "O1"
                            wric "Hmph! Of course you don't know! If you knew you wouldn't be defending her! She just... Huh... I{w=[wt1]}-I've said too much!{w=[wt3]} I shouldn't be telling you this, it was a secret! What a busybody you are, huh!? You better not go around saying anything, do you understand!?"
                            hero "But you ended up not telling me anything!"
                            wric "And that was already too much!"
                            hero "{bt}Ehhh...?{/bt}"

                    elif not "WRIC_BG_WSIS_3" in hero_know:
                        $ hero_know.append("WRIC_BG_WSIS_3")
                        $ msg.msg("You know {nm}[fnamewric]{/nm} a little more")
                        $ add_stat("wric", "inti", 1)

                        $ wric_mood = "O1"
                        wric "Again with this topic?{w=[wt3]} Really{w=[wt2]}, you're becoming quite bothersome about this."

                        $ hero_mood = "A2"
                        hero "I just think maybe there's been some misunderstanding.{w=[wt3]} Maybe you two could be friends if-{nw}"

                        $ wric_mood = "O1"
                        wric "Friends!?{w=[wt3]} With someone who threatened to hit me?{w=[wt3]} With someone who stole {nm}[fnamewgal]{/nm}'s boyfriend?{w=[wt3]} Absolutely not!"
                        wric "Do you know how much that hurt my best friend?{w=[wt3]} {nm}[fnamewsis]{/nm} pretended to be {nm}[fnamewgal]{/nm}'s friend and then went behind her back to steal the boy she liked!"
                        $ wric_mood = "O1"
                        wric "I've said far too much.{w=[wt3]} Please{w=[wt2]}, just{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} leave it alone."

                "Return":
                    jump wric_interact_chat

        "Return":
            jump wric_interact

    $ add_stat("wric", "inti", 0.2)
    $ gametimemin += 20
    jump wric_interact_check

# ----------
# Character Initiative
# ----------
label initiative_wric:
    $ wric_know.append("Talk")
    $ a_event_0 = renpy.random.random()

    # ----------------------------------------------------------------------------------------------------
    # Space for new ideas
    # ----------------------------------------------------------------------------------------------------
    if 0 > 1:
        pass

    # ----------
    # Ask if HERO ever dated
    # ----------
    elif renpy.random.random() < (wric_inti*0.02) and not any(get_id.startswith("HERO_Dated") for get_id in wric_know):

        $ wric_mood = "A1"
        wric "You know{w=[wt2]}, it can be quite tiresome sometimes.{w=[wt3]} Daddy constantly arranges these{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} social gatherings with other prestigious families.{w=[wt3]} Their sons are always so eager to court me{w=[wt2]}, though most of them are desperately lacking in refinement{w=[wt2]}, even with their noble upbringing."

        $ wric_mood = "A1"
        wric "Though I suppose you wouldn't know anything about proper courtship{w=[wt2]}, would you?{w=[wt3]} I doubt you've ever even been in the presence of anyone worth dating."

        $ hero_fx = 1
        $ hero_mood = "O1"

        menu:
            wric "Though I suppose you wouldn't know anything about proper courtship, would you? I doubt you've ever even been in the presence of anyone worth dating.{fast}"

            "Deny":
                $ wric_know.append("HERO_Dated_N")
                $ msg.msg("{nm}[fnamewric]{/nm} knows you a little more")
                $ add_stat("wric", "inti", 0.5)
                hero "N{w=[wt1]}-no{w=[wt2]}, I've never dated anyone."

                $ wric_mood = "A1"
                wric "Well{w=[wt2]}, naturally.{w=[wt3]} Though I suppose there's a certain charm in your honesty about it.{w=[wt3]} Not everyone can be born into the proper social circles, after all."

            "Confirm":
                $ wric_know.append("HERO_Dated_Y")
                $ msg.msg("{nm}[fnamewric]{/nm} knows you a little more")
                $ add_stat("wric", "inti", 0.5)
                hero "W{w=[wt1]}-well{w=[wt2]}, I have dated someone before..."

                $ wric_mood = "O1"
                wric "Oh?{w=[wt3]} How{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} unexpected.{w=[wt3]} Though I'm sure it was nothing like the sophisticated courtships I've experienced.{w=[wt3]} Probably some quaint little romance."

    # ----------
    # Ask HERO's girl preference
    # ----------
    elif renpy.random.random() < (wric_inti*0.02) and sum(1 for get_id in wric_know if get_id.startswith("HERO_Y_Girl")) + sum(1 for get_id in wric_know if get_id.startswith("HERO_N_Girl")) < 4:

        $ a_event_0 = renpy.random.random()

        if a_event_0 < 1/4:
            $ wric_mood = "A1"
            wric "You know{w=[wt2]}, at the last charity gala{w=[wt2]}, so many young men were practically falling over themselves trying to get my attention.{w=[wt3]} Though I can hardly blame them{w=[wt2]}, given my perfect breeding and refined manners."
            wric "I suppose someone like you would have much{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} simpler tastes?{w=[wt3]} Probably the sort who's impressed by any girl who merely glances your way."

        elif a_event_0 < 2/4:
            wric "*sigh*{w=[wt3]} Daddy keeps suggesting I consider some of his business partners' sons{w=[wt2]}, but really{w=[wt2]}, their standards are so disappointing.{w=[wt3]} Just the other day, one of them was absolutely smitten with a girl who didn't even know the proper way to hold a tea cup!"
            wric "Though I suppose that's the sort of thing you'd find perfectly acceptable{w=[wt2]}, isn't it?{w=[wt3]} I can't imagine you have very discerning taste in ladies."

        elif a_event_0 < 3/4:
            wric "It can be quite exhausting{w=[wt2]}, you know{w=[wt2]}, having to maintain such high standards.{w=[wt3]} All these suitors trying to court me{w=[wt2]}, yet so few understand what a lady of my caliber truly desires."
            wric "But then{w=[wt2]}, someone like you probably wouldn't even know what qualities to look for in a proper lady{w=[wt2]}, would you?{w=[wt3]} I bet you're the type to be impressed by just about anyone."

        else:
            wric "Honestly{w=[wt2]}, it's rather amusing how often my friends come to me for advice about potential suitors.{w=[wt3]} I suppose they recognize my superior judgment when it comes to selecting appropriate matches."
            wric "Though I doubt you've given much thought to what makes a lady worthy of pursuit{w=[wt2]}, have you?{w=[wt3]} Your standards are probably far too{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} modest."

        menu:
            "Deny":
                hero "O{w=[wt1]}-of course I have my standards!"

                $ wric_mood = "A1"
                wric "Well{w=[wt2]}, naturally.{w=[wt3]} Though I suppose there's a certain charm in your honesty about it.{w=[wt3]} Not everyone can be born into the proper social circles, after all."

            "Confirm":
                hero "Y{w=[wt1]}-you're right.{w=[wt3]} I don't really have much standards."

                $ wric_mood = "A1"
                wric "Of course I'm right.{w=[wt3]} Just by looking at you I can tell from afar."
                $ gametimemin += 20
                $ add_stat("wric", "inti", 0.20)
                jump wric_interact_check

        wric "Hmph!{w=[wt3]} So, what would your so refined standards be?{nw}"

        menu:
            wric "Hmph! So, what would your so refined standards be?{fast}"

            "Answer":
                $ hero_mood = "A1"
                hero "Well, let me think{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

                # Count already answered categories
                $ a_breast_count = sum(1 for get_id in wric_know if "Breast_" in get_id)
                $ a_hair_count = sum(1 for get_id in wric_know if "HairSize_" in get_id)
                $ a_eye_count = sum(1 for get_id in wric_know if "EyeShape_" in get_id)
                $ a_personality_count = sum(1 for get_id in wric_know if "Personality_" in get_id)

                # Appearance Likes(Y)/Dislikes(N)
                $ a_event_1 = wric_know
                $ a_event_3 = "initiative_wric_return"
                call hero_y_girl(Get_Breast=max(0, 1-a_breast_count), Get_HairSize=max(0, 1-a_hair_count), Get_EyeShape=max(0, 1-a_eye_count), Get_Personality=max(0, 3-a_personality_count)) from _call_hero_y_girl_11

                # Store the answer if one was given
                if _return:
                    $ wric_know.append("HERO_Y_Girl_" + _return)

                $ msg.msg("{nm}[fnamewric]{/nm} knows you a little more")
                $ add_stat("wric", "inti", 0.5)

                if _return in ["Personality_9", "Personality_11", "Breast_2", "Breast_3", "HairSize_5", "HairSize_6"]: # Match - intelligent, visually diligent, medium/big breasts, long hair (elegant)
                    $ add_stat("wric", "bonus", 10)
                    $ add_stat("hero", "cha_soc", 0.5)
                    $ wric_mood = "A1"
                    wric "Y{w=[wt1]}-you have surprisingly refined taste.{w=[wt3]} Though I wonder if someone of your standing could ever attract such a lady!"

                elif _return in ["Personality_12", "Personality_10", "Breast_0", "Breast_1", "HairSize_0", "HairSize_1", "HairSize_2"]: # Opposite match - sloppy, stupid, flat/tiny breasts, bald/short hair
                    $ add_stat("wric", "bonus", -10)
                    $ wric_mood = "O1"
                    wric "Hmp!{w=[wt2]} Of course boys always look at that kind of girl, right?{w=[wt3]} What could I expect?"

                else: # Others
                    $ wric_mood = "A1"
                    wric "I suppose that's not entirely terrible taste."

            "Don't choose":
                jump initiative_wric_return

    # ----------
    # No question was chosen
    # ----------
    else:
        $ wric_mood = "A1"
        wric "Oh{w=[wt2]}, never mind.{w=[wt3]} I suppose this subject is too sophisticated to discuss with someone like you."
        jump wric_interact

    # ----------
    # Question ended
    # ----------
    $ gametimemin += 20
    $ add_stat("wric", "inti", 0.20)
    jump wric_interact_check

# ----------------------------------------------------------------------------------------------------
# Player didn't answer
# ----------------------------------------------------------------------------------------------------
label initiative_wric_return:
    hero "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Well{w=[wt2]}, I don't really know how to answer that right now."
    wric "Tsk{w=[wt2]}, how disappointing.{w=[wt3]} I suppose I shouldn't have expected a proper response."
    jump wric_interact