image wgal_classroom4_wgal_cfg:
    "images/Scene/WGAL - Classroom/wgal_classroom4_wgal_cfg 1.webp"
    0.2
    "images/Scene/WGAL - Classroom/wgal_classroom4_wgal_cfg 2.webp"
    0.2
    "images/Scene/WGAL - Classroom/wgal_classroom4_wgal_cfg 3.webp"
    0.2
    "images/Scene/WGAL - Classroom/wgal_classroom4_wgal_cfg 2.webp"
    0.2
    repeat

#---------------------------------------------------------------------------
label wgal_quest0: # Pair Activity
#---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_181
    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night

    stop BGM fadeout 3
    scene bg_0
    with Dissolve(2)

    pause(1)
    play BGM "audio/W2C - GoodVibes.mp3"

    scene wgal_classroom1_bg
    with Dissolve(2)

    $ a_check_1 = "Teacher"

    sup1 "Hello, class.{w=[wt2]} Today we're going to do a group project!{nw}"

    play BGE "Crowd (Small).ogg"

    sup1 "Hello, class. Today we're going to do a group project!{fast}{w=[wt4]} Wow{w=[wt2]}, I see that some of you are already excited to join your friends, right?{w=[wt2]} But I need to say that the idea of this project is for you to interact with different people{w=[wt2]}, so I'll draw who will be paired with whom.{w=[wt3]} I just separated the names here on the list."

    sup1 """
    {b}And the pairs are:{/b}{w=[wt2]}
    {pr}{nm}[fnamewpre]{/nm} and {nm}[fnamehprv]{/nm}{w=[wt2]}; {nm}[fnamewota]{/nm} and {nm}[fnamewlaz]{/nm}{w=[wt2]};
    {pr}{nm}[fnamewric]{/nm} and {nm}[fnamewgot]{/nm}{w=[wt2]}; {nm}[fnamewdis]{/nm} and {nm}[fnamewdel]{/nm}{w=[wt2]};
    {pr}{nm}[fnamewuza]{/nm} and {nm}[fnamehine]{/nm}{w=[wt2]}; and {nm}[fnamehero]{/nm} and {nm}[fnamewgal]{/nm}.
    """

    # She says the pairs

    mind "({aw}Ehhh...?{/aw}{w=[wt2]} {nm}[fnamewgal]{/nm}!?{w=[wt3]} Isn't she that girl?)"

    sup1 "I'll give you a minute to sit closer."

    stop BGE fadeout 3

    scene wgal_classroom2_bg
    show wgal_classroom2_wricbody 1
    show wgal_classroom2_wricface 1
    show wgal_classroom2_wgal 1
    with Fade(1,0,2)

    show wgal_classroom2_wricface 2
    wric "{nm}[fnamewgal]{/nm}..."

    show wgal_classroom2_wricface 1
    wgal "Yeah, what a bitch, right?"

    show wgal_classroom2_wricface 3
    show wgal_classroom2_hero at OL
    show wgal_classroom2_hero at CC_slow
    pause(1)

    hero "Um{w=[wt1]}, uh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{nw}"

    show wgal_classroom2_wgal 2
    show wgal_classroom2_wgalface o0

    hero "Um{w=[wt2]}, uh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{fast}{w=[wt2]} Hi{w=[wt2]}, can I bring my table here or would you prefer to go back there?"

    show wgal_classroom2_wricface 1
    show wgal_classroom2_wgalface o1
    wgal "Ugh{w=[wt2]}, seriously?{w=[wt3]} You're {bt}supposed{/bt} to be the man here.{w=[wt2]} You're not going to make me lift this heavy desk, right?"

    show wgal_classroom2_wricface 3
    show wgal_classroom2_wgalface o0
    hero "Y{w=[wt1]}-you're right.{w=[wt3]} I'm gonna bring my table."


    show wgal_classroom2_hero at OL_slow

    pause(0.2)

    show wgal_classroom2_wricface 1
    show wgal_classroom2_wgalface o1
    wgal "Dumbass..."

    hide wgal_classroom2_wricbody
    hide wgal_classroom2_wricface
    with dissolve

    show wgal_classroom2_wgal 1
    hide wgal_classroom2_wgalface
    with dissolve
    hide wgal_classroom2_hero

    hide wgal_classroom2_wgal
    hide wgal_classroom2_wric
    show wgal_classroom2_wgal_wric
    show wgal_classroom2_wgal_wricface o0
    with Dissolve(1)

    show wgal_classroom2_wgal_wricface o1
    wric "{aw}Ugh{w=[wt1]}, bestie.{w=[wt3]} The teacher paired me with that freak!{/aw}"

    show wgal_classroom2_wgal_wricface o0
    wgal "What about me, bestie?{w=[wt3]} Did you see the dumbass having {bt}AUDACITY{/bt} to ask if I was going to drag my desk to him?{w=[wt4]} I was like{w=[wt3]}, {bt}are you kidding me!?!?{/bt}"

    show wgal_classroom2_wgal_wricface o1
    wric "{aw}Ugh...{w=[wt2]} This class is going to be the worst...!{/aw}"

    show wgal_classroom2_wgot 1
    with dissolve

    show wgal_classroom2_wgal_wricface s0
    wgot "Excuse me."

    show wgal_classroom2_wgot 2
    with dissolve

    show wgal_classroom2_wgal_wricface s1
    wric "Ugh..."

    show wgal_classroom2_wgal_wricface s0 with None

    stop BGM fadeout 3

    scene bg_0
    with Dissolve(2)

    pause(1)

    play BGM "audio/W2C - Tranquility.mp3"

    scene wgal_classroom3_bg
    show wgal_classroom3_herobody
    show wgal_classroom3_herohead d
    show wgal_classroom3_wgalbody
    show wgal_classroom3_wgalhead 1
    show wgal_classroom3_wgalface 1o0
    with Dissolve(2)

    sup1 "Very well.{nw}"

    show wgal_classroom3_herohead u
    show wgal_classroom3_heroface 1

    sup1 "Very well.{fast}{w=[wt2]} I want one of the group members to copy the questions I wrote on the board and work on the answers together.{w=[wt4]} So{w=[wt2]}, that's it, class{w=[wt3]}, In the meantime, I'm going right here to the canteen and get a coffee, okay?{w=[wt2]} I didn't have time to have breakfast today, you know.{w=[wt2]}{nw}"

    $ X_spd = 4
    $ Y_pos = -530
    $ Y_pos2 = 100
    $ X_pos = 1260
    $ X_pos2 = 0
    $ Z_rot = 0
    $ Z_rot2 = 0
    show schoolday_1_2herofx at XYZ_Move2

    show wgal_classroom3_heroface 2
    sup1 "Very well.{w=[wt2]} I want one of the group members to copy the questions I wrote on the board and work on the answers together.{w=[wt4]} So{w=[wt2]}, that's it, class{w=[wt3]}, In the meantime, I'm going right here to the canteen and get a coffee, okay?{w=[wt2]} I didn't have time to have breakfast today, you know.{w=[wt2]}{fast} That's it!{w=[wt2]} Behave!{w=[wt2]} Bye Bye!"

    show wgal_classroom3_wgalface 1o1
    wgal "Ugh{w=[wt2]}, seriously?{w=[wt2]} I bet this bitch is gonna suck some dick while she gives us work to do!{w=[wt3]} Like{w=[wt2]}, do we really need a group for this stupid shit...?"

    hide schoolday_1_2herofx
    with dissolve

    show wgal_classroom3_herohead l
    show wgal_classroom3_heroface 4
    show wgal_classroom3_wgalface 1o2
    hero "W{w=[wt1]}-well{w=[wt1]}, I can copy the questions while you think about the answers.{w=[wt3]} How about that?"

    show wgal_classroom3_heroface 3
    show wgal_classroom3_wgalhead 2
    show wgal_classroom3_wgalface 2o1
    wgal "Hmph!{w=[wt2]} Who do you think you are to boss me around, dumbass?"

    show wgal_classroom3_heroface 4
    show wgal_classroom3_wgalface 2o0
    hero "Huh?{w=[wt2]} No{w=[wt1]}, I just-"

    show wgal_classroom3_heroface 3
    show wgal_classroom3_wgalface 2o1
    wgal "Don't start thinking I'm like your little girlfriend, okay?{w=[wt3]}{nw}"

    show wgal_classroom3_wgalface 2a1
    wgal "Don't start thinking I'm like your little girlfriend, okay?{fast} Although that sly bitch must be just playing coy with you!{w=[wt1]} Pfff{w=[wt1]}-{gg}bwa-ha-ha-ha...{/gg}"

    show wgal_classroom3_heroface 5
    show wgal_classroom3_wgalface 2a0
    pause(0.5)
    
    menu:
        "Say that you have no relationship with {nm}[fnamewsis]{/nm}":

            show wgal_classroom3_heroface 6
            hero "I have nothing to do with her."

            $ wgal_know.append("WSIS_IS_Acquaintance")
            $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} knows you a little more"))
            $ add_stat("wsis", "bonus", 9)
            $ add_stat("wgal", "inti", 0.5)
            $ add_stat("wgal", "love", 3)
            $ add_stat("hero", "cha_soc", 3)

            show wgal_classroom3_heroface 5
            show wgal_classroom3_wgalface 2a1
            wgal "Ahh{w=[wt2]}, gonna tell me you{w=[wt2]}, like{w=[wt2]}, aren't dying to put your baby carrot inside that fat ass, huh?{w=[wt4]} It's {bt}OOOBVIOUS{/bt} you do!{w=[wt4]} I know you guys only care about that.{w=[wt3]} Every guy's exactly the same."

        "Say that {nm}[fnamewsis]{/nm} is your sister":

            show wgal_classroom3_heroface 6
            hero "She's my sister."

            $ wgal_know.append("WSIS_IS_Sister")
            $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} knows you a little more"))
            $ add_stat("wsis", "bonus", 3)
            $ add_stat("wgal", "inti", 0.5)
            $ add_stat("wgal", "love", 1)
            $ add_stat("hero", "cha_soc", 1)

            show wgal_classroom3_heroface 5
            show wgal_classroom3_wgalface 2a1
            wgal "{gg}Bwa-ha-ha-ha...{/gg}{w=[wt4]} Sister?{w=[wt3]} Oh no, no, no, no...{w=[wt2]} Stop the presses! {gg}Bwa-ha-ha-ha...{/gg}{w=[wt4]} No{w=[wt2]}, I better not say anything...{w=[wt3]} But{w=[wt2]}, like{w=[wt2]}, gonna tell me you{w=[wt1]}, like{w=[wt2]}, if you weren't siblings you wouldn't be dying to put your baby carrot inside that fat ass, huh?{w=[wt4]} It's {bt}OOOBVIOUS{/bt} you do!{w=[wt4]} I know you guys only care about that.{w=[wt3]} Every guy's exactly the same."

        "Say that {nm}[fnamewsis]{/nm} is your step-sister":

            show wgal_classroom3_heroface 6
            hero "She's my step-sister."

            $ wgal_know.append("WSIS_IS_Stepsister")
            $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} knows you a little more"))
            $ add_stat("wgal", "inti", 0.5)
            $ add_stat("wgal", "love", 1.5)
            $ add_stat("hero", "cha_soc", 1.5)

            show wgal_classroom3_heroface 5
            show wgal_classroom3_wgalface 2a1
            wgal "{gg}Bwa-ha-ha-ha...{/gg}{w=[wt4]} STEP-SISTER?{w=[wt3]} Oh no, no, no, no...{w=[wt2]} Stop the presses! {gg}Bwa-ha-ha-ha...{/gg}{w=[wt4]} No{w=[wt2]}, I better not say anything...{w=[wt3]} But{w=[wt2]}, like{w=[wt2]}, you're not a real family, right?{w=[wt3]} Gonna tell me you{w=[wt1]}, like{w=[wt2]}, aren't dying to put your baby carrot inside that fat ass, huh?{w=[wt4]} It's {bt}OOOBVIOUS{/bt} you do!{w=[wt4]} I know you guys only care about that.{w=[wt3]} Every guy's exactly the same."

        "Defend {nm}[fnamewsis]{/nm}":

            show wgal_classroom3_heroface 6
            hero "What's your problem with her?{w=[wt2]} She's not at all what you said."

            $ wgal_know.append("WSIS_IS_Girlfriend")
            $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} knows you a little more"))
            $ add_stat("wsis", "bonus", 15)
            $ add_stat("wgal", "inti", 0.5)
            $ add_stat("wgal", "love", -1)
            $ add_stat("hero", "cha_soc", 1)

            show wgal_classroom3_heroface 5
            show wgal_classroom3_wgalface 2a1
            wgal "Hunf{w=[wt2]}, I used to consider that faker a friend{w=[wt2]}, so I have more reasons than you think not to like her!{w=[wt3]} But that's not the point.{w=[wt2]} I'm talking more about you!{w=[wt3]} Gonna tell me you{w=[wt1]}, like{w=[wt2]}, aren't dying to put your baby carrot inside that fat ass, huh?{w=[wt4]} It's {bt}OOOBVIOUS{/bt} you do!{w=[wt4]} I know you guys only care about that.{w=[wt3]} Every guy's exactly the same."

        "Stay silent":
            pause(0.5)

            show wgal_classroom3_wgalface 2o0
            show wgal_classroom3_herohead d
            hide wgal_classroom3_heroface
            with dissolve

            pause(1)

            show wgal_classroom3_wgalface 2a0

            pause(1)

            show wgal_classroom3_wgalface 2a1
            wgal "{gg}Bwa-ha-ha-ha...{/gg}{w=[wt3]} You're so boring, huh?{w=[wt2]} Must be a virgin!{w=[wt3]} Gonna tell me you{w=[wt1]}, like{w=[wt2]}, aren't dying to put your baby carrot inside that fat ass, huh?{w=[wt4]} It's {bt}OOOBVIOUS{/bt} you do!{w=[wt4]} I know you guys only care about that.{w=[wt3]} Every guy's exactly the same."



    show wgal_classroom3_wgalface 2a0
    hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"

    show wgal_classroom3_herohead l
    show wgal_classroom3_heroface 5
    hero "...{fast}{w=[wt2]}{nw}"

    show wgal_classroom3_heroface 6
    hero "...{fast} So{w=[wt2]}, does that mean that {nm}[fnamehriv]{/nm}{w=[wt1]}, whom you seem to think is a cool guy{w=[wt1]}, would be included in that?"

    show wgal_classroom3_heroface 5
    show wgal_classroom3_wgalface 2a1
    wgal "{bt}Hmm...?{/bt}{w=[wt3]} Why are you talking about him?{w=[wt3]} Feeling a little jealous of me, baby?"

    show wgal_classroom3_heroface 6
    show wgal_classroom3_wgalface 2a0
    hero "It's not that.{w=[wt3]} It's just that I remember when he broke {nm}[fnamehprv]{/nm}'s phone{w=[wt1]}, you two seemed close."

    show wgal_classroom3_heroface 5
    show wgal_classroom3_wgalface 2a1
    wgal "{gg}Bwa-ha-ha-ha...{/gg}{w=[wt3]} You're quite dumbass, huh?{w=[wt2]} What if we're close, huh?"

    show wgal_classroom3_heroface 6
    show wgal_classroom3_wgalface 2a0
    hero "That's not the case.{w=[wt2]} You're just avoiding the question."

    stop BGM fadeout 3
    show wgal_classroom3_heroface 5
    show wgal_classroom3_wgalface 2a1
    wgal "Okay{w=[wt1]}, what's the question?"

    show wgal_classroom3_wgalface 2a0
    hero ".{w=[wt2]}.{w=[wt2]}.{w=[wt4]}{nw}"

    show wgal_classroom3_heroface 7
    with Dissolve(1)
    play BGM "audio/W2C - Awkward.mp3"
    pause(1)

    mind "(Oh, God.{w=[wt2]} Is this a girl or a monkey?{w=[wt3]} Does this animal have enough neurons to understand a sentence without distorting its meaning?{w=[wt3]} I wonder if I can lower the level of dialogue to the point where we can speak the same language.{w=[wt4]} But how low would this level of dialogue be?)"

    show wgal_classroom3_heroface 5
    with Dissolve(1)
    pause(1)

    show wgal_classroom3_wgalface 2a0
    show wgal_classroom3_heroface 6
    hero "Look{w=[wt2]}, I know you can be close to whoever you want.{w=[wt3]} That said{w=[wt2]}, considering you said every guy is exactly the same{w=[wt2]}, and the person you're close to is a guy{w=[wt3]}, do you see him as just like all the others{w=[wt1]}, even though you're close to him?"

    stop BGM fadeout 3

    show wgal_classroom3_wgalface 2o0
    show wgal_classroom3_heroface 5
    wgal "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{nw}"

    show wgal_classroom3_wgalface 2o1
    wgal "...{fast} {bt}Okay... Okay...{/bt}{w=[wt2]} But like{w=[wt2]}, I'll answer this with another question."

    show wgal_classroom3_wgalface 2o0
    show wgal_classroom3_heroface 6
    hero "Heh...?{w=[wt2]} You're going to dodge-"

    show wgal_classroom3_wgalface 2o1
    show wgal_classroom3_heroface 5
    wgal "Chill dumbass{w=[wt2]}, I won't dodge the question!{w=[wt3]} But like{w=[wt2]}, you need to answer with a yes or no{w=[wt1]}, got it?"

    show wgal_classroom3_wgalhead 1
    show wgal_classroom3_wgalface 1o0
    show wgal_classroom3_heroface 6
    hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} R{w=[wt1]}-right then.{w=[wt2]} Go ahead."

    scene bg_0
    with Dissolve(1)

    play BGM "audio/W2C - SexyVibes.mp3"

    scene wgal_classroom4_bg
    show wgal_classroom4_wgal_a
    show wgal_classroom4_wgal_b 1
    show wgal_classroom4_wgal_c 0
    show wgal_classroom4_wgal_d 1
    show wgal_classroom4_wgal_e o0
    show wgal_classroom4_wgal_f d
    show wgal_classroom4_herobody 0
    show wgal_classroom4_mg
    show wgal_classroom4_herofg 1
    with Dissolve(2)

    play SE1 "Zipper.mp3"
    show wgal_classroom4_wgal_c 2
    show wgal_classroom4_wgal_f r
    show wgal_classroom4_fg
    with Dissolve(1)

    show wgal_classroom4_herobody 2
    show wgal_classroom4_heroface 2s0
    show wgal_classroom4_herofg 2
    with dissolve

    show wgal_classroom4_wgal_e o1
    wgal "So{w=[wt2]}, tell me{w=[wt3]}, wouldn't you really want a little taste of this body? {bt}Hmmm...?{/bt}"

    show wgal_classroom4_wgal_c 3
    show wgal_classroom4_wgal_e o0
    show wgal_classroom4_wgal_f d
    show wgal_classroom4_wgal_c 3
    with dissolve

    show wgal_classroom4_wgal_e a0
    show wgal_classroom4_wgal_c 4a
    show wgal_classroom4_wgal_cfg
    with dissolve

    show wgal_classroom4_wgal_e a1
    show wgal_classroom4_wgal_f r
    wgal "What if this was your lollipop?{w=[wt4]} Do you think you could do it in my tits?"

    show wgal_classroom4_heroface 2s1
    hero "W{w=[wt1]}-what are you{w=[wt1]}-{nw}"

    show wgal_classroom4_heroface 2s0
    show wgal_classroom4_wgal_b 2
    show wgal_classroom4_wgal_c 4b
    show wgal_classroom4_wgal_cfg
    show wgal_classroom4_wgal_e a0
    show wgal_classroom4_wgal_f d
    with dissolve

    pause (0.5)

    show wgal_classroom4_wgal_e a0
    show wgal_classroom4_wgal_f r
    with dissolve

    pause (0.5)

    show wgal_classroom4_wgal_e a1
    wgal "Wanna see what's down here?"

    show wgal_classroom4_wgal_e a0
    #$personality[0]="Hentai"
    $personality[0]="Kind"

    if stat_cha >= 20:
        show wgal_classroom4_heroface 2s3
        hero "Heh{w=[wt2]}, you wouldn't have the courage!"
        
        $ add_stat("wgal", "lust", 2)
        $ add_stat("hero", "cha_soc", 0.2)

        show wgal_classroom4_heroface 2s2
        show wgal_classroom4_wgal_e a1
        wgal "Are you sure?"

        show wgal_classroom4_heroface 2s3
        show wgal_classroom4_wgal_e a0
        hero "If you had{w=[wt2]}, you'd have done it already, right?"

        show wgal_classroom4_wgal_b 1
        show wgal_classroom4_wgal_c 1
        hide wgal_classroom4_wgal_cfg
        hide wgal_classroom4_fg
        with dissolve
        
        show wgal_classroom4_heroface 2s2
        show wgal_classroom4_wgal_e o1
        wgal "What a pervert!{w=[wt2]} Of course there's nothing for you here!"

        show wgal_classroom4_heroface 2s3
        show wgal_classroom4_wgal_e o0
        hero "See how right I was?"

        $ add_stat("wgal", "love", 2)
        $ add_stat("hero", "cha_soc", 2)

        show wgal_classroom4_heroface 2s2
        show wgal_classroom4_wgal_e a0
        wgal "{gg}Bwa-ha-ha-ha...{/gg}{w=[wt2]} Idiot!{w=[wt4]} At least you seem more talkable than your disgusting pervert friend over there.{w=[wt3]} Perhaps I will think fondly if you behave well in the future."

    elif personality[0] == "Hentai":
        show wgal_classroom4_heroface 2s1
        hero "...Y{w=[wt1]}-yes!"
        
        show wgal_classroom4_wgal_e a1
        show wgal_classroom4_heroface 2s0
        wgal "Why don't you ask for it?"

        show wgal_classroom4_wgal_e a0
        show wgal_classroom4_heroface 2s1
        hero "...C{w=[wt1]}-can you show me?"

        show wgal_classroom4_heroface 2s0
        show wgal_classroom4_wgal_b 1
        show wgal_classroom4_wgal_c 1
        hide wgal_classroom4_wgal_cfg
        hide wgal_classroom4_fg
        with dissolve
        
        show wgal_classroom4_wgal_e o1
        wgal "Not even in your dreams, virgin!"

    elif personality[0] == "Kind":
        show wgal_classroom4_heroface 2s1
        hero "{aw}S{w=[wt1]}-stop!{w=[wt2]} S{w=[wt1]}-someone can see y{w=[wt1]}-you!{/aw}"

        show wgal_classroom4_heroface 2s0
        show wgal_classroom4_wgal_b 1
        show wgal_classroom4_wgal_c 1
        hide wgal_classroom4_wgal_cfg
        hide wgal_classroom4_fg
        with dissolve

        $ add_stat("wgal", "love", 1)
        $ add_stat("hero", "cha_soc", 1)
        
        show wgal_classroom4_wgal_e o1
        wgal "Heh...!{w=[wt2]} You're kinda boring{w=[wt2]}, but at least is not just a stupid pervert like your disgusting friend."

    else:
        hero "..."

        show wgal_classroom4_wgal_b 1
        show wgal_classroom4_wgal_c 1
        hide wgal_classroom4_wgal_cfg
        hide wgal_classroom4_fg
        with dissolve
        
        show wgal_classroom4_wgal_e o1
        wgal "Wow{w=[wt2]}, you're really super boring!{w=[wt3]} You just freeze in front of a girl, don't you?"   

    show wgal_classroom4_wgal_e o0
    pause(0.5)

    show wgal_classroom4_herobody 1
    show wgal_classroom4_heroface 1o0
    show wgal_classroom4_herofg 1
    with dissolve

    pause(1)

    show wgal_classroom4_heroface 1o1
    if stat_cha >= 20:
        hero "{bt}Sure... Sure...{/bt}{w=[wt4]} So{w=[wt2]}, what else?"
    else:
        hero "So{w=[wt2]}, what else?"

    show wgal_classroom4_heroface 1o0
    show wgal_classroom4_wgal_f d
    show wgal_classroom4_wgal_e o1
    wgal "I{w=[wt2]}, like{w=[wt2]}, know I'm pretty hot and{w=[wt2]}, like{w=[wt2]}, it's{w=[wt1]} {bt}OOOBVIOUS{/bt} that every man would die to fuck me!{w=[wt2]} That's all they think, isn't it?{w=[wt4]} What's your answer?"

    show wgal_classroom4_wgal_e o0

    menu:
        wgal "I{w=[wt2]}, like{w=[wt2]}, know I'm pretty hot and{w=[wt2]}, like{w=[wt2]}, it's{w=[wt1]} {bt}OOOBVIOUS{/bt} that every man would die to fuck me!{w=[wt2]} That's all they think, isn't it?{w=[wt4]} What's your answer?{fast}"

        "Agree that she's really hot":
            hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
            show wgal_classroom4_heroface 1o1
            hero "...{fast} Y{w=[wt1]}-yeah.{w=[wt3]} You're right."

            $ add_stat("wgal", "lust", 2)
            $ add_stat("hero", "cha_soc", 0.2)

            show wgal_classroom4_heroface 1o0
            show wgal_classroom4_wgal_e o1
            wgal "I know, right?{w=[wt2]} But back off, 'cos you're not getting anything from me, okay?{w=[wt3]} I'm not into charity{w=[wt2]}, but like{w=[wt2]}, you can keep dreaming, alright?"

        "Say she might have other qualities":
            hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
            show wgal_classroom4_heroface 1o1
            hero "...{fast} I{w=[wt1]}-I don't know you well{w=[wt2]}, but maybe you have more to offer than just your body."

            $ add_stat("wgal", "love", 2)
            $ add_stat("hero", "cha_soc", 2)

            show wgal_classroom4_heroface 1o0
            show wgal_classroom4_wgal_e a0
            wgal "Pfff{w=[wt1]}-{gg}bwa-ha-ha-ha...{/gg}{w=[wt2]} You're trying to pull that on me, huh?{w=[wt3]} Look{w=[wt2]}, you're not getting anything from me, okay?{w=[wt3]} But like{w=[wt2]}, you can keep dreaming, alright?"

    show wgal_classroom4_heroface 1o1
    show wgal_classroom4_wgal_f r
    hero "{bt}Sure... Sure...{/bt}"

    show wgal_classroom4_heroface 1o0

    pause(0.5)

    show wgal_classroom4_wgal_f d

    pause(1)

    hide wgal_classroom4_wgal_a
    hide wgal_classroom4_wgal_b
    hide wgal_classroom4_wgal_c
    hide wgal_classroom4_wgal_d
    hide wgal_classroom4_herobody
    hide wgal_classroom4_heroface
    hide wgal_classroom4_mg
    hide wgal_classroom4_herofg

    show wgal_classroom4_wgalbody
    show wgal_classroom4_wgalface o0
    show wgal_classroom4_herobody 1
    show wgal_classroom4_heroface 1o0
    show wgal_classroom4_mg
    show wgal_classroom4_herofg 1
    with dissolve

    pause(1)

    show wgal_classroom4_wgalface o1
    wgal "But like{w=[wt2]}, answering your question..."

    show wgal_classroom4_wgalface o0
    hero "..."

    $ add_stat("wgal", "bonus", 10)

    show wgal_classroom4_wgalface o1
    wgal "It's obvious that {nm}[fnamehriv]{/nm} is just a man like any other."

    show wgal_classroom4_heroface 1o1
    show wgal_classroom4_wgalface o0
    hero "Got it."

    show wgal_classroom4_heroface 1o0
    stop BGM fadeout 10
    pause(2)

    show wgal_classroom4_heroface 1o1
    hero "Well{w=[wt2]}, changing the subject{w=[wt2]}, have you thought about the answer to any of the questions?"

    show wgal_classroom4_heroface 1o0
    show wgal_classroom4_wgalface o1
    wgal "Hmm...?{w=[wt4]} What questions?"

    show wgal_classroom4_wgalface o0
    "{nw}"
    show wgal_classroom4_heroface 1o2
    with Dissolve(1)

#---------------------------------------------------------------------------
    scene bg_0
    with Dissolve(2)

    "Then you ended up having to do all the work yourself."
    
    $ add_stat("wgal", "inti", 3)

    $ wgal_quest_1 = 1

    call gametime_schoolnext from _call_gametime_schoolnext_7
    $ gametimemin += _return
    call gametime from _call_gametime_103

    pause

    play BGM "audio/W2C - Tranquility.mp3"
    
    call check_playermap from _call_check_playermap_38
    jump show_ui
#---------------------------------------------------------------------------
