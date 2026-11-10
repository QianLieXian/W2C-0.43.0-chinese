image wdel_1_5_fg:
    "wdel_1_5_fg 1"
    0.15
    "wdel_1_5_fg 2"
    0.15
    "wdel_1_5_fg 3"
    0.15
    "wdel_1_5_fg 4"
    0.15
    repeat

label wdel_quest0:

    #stop BGM fadeout 3

    $ hero_map = "School - Classroom (1B)"

    scene bg_0 with Dissolve(1) # HERO walking in school hallway.

    #play BGM "audio/W2C - Melancholy (Piano).mp3"

    scene wdel_1_1_bg
    with Dissolve(2)

    mind "(That's the short-haired girl who sits near me!{w=[wt2]} What's she doing?)"

    scene wdel_1_2_bg
    show wdel_1_2_hero 1
    show wdel_1_2_mg
    show wdel_1_2_wdel 0
    show wdel_1_2_fg:
        blend "add"
    with fade

    hide wdel_1_2_fg
    show wdel_1_2_wdel 1
    show wdel_1_2_wdel_head 1
    show wdel_1_2_wdel_face 1o0
    show wdel_1_2_wdel_hand 1
    show wdel_1_2_fg:
        blend "add"
    with dissolve

    show wdel_1_2_wdel_face 1o1
    wdel "What're you staring at, wimp?{w=[wt2]} Want me to clean your face too?"

    show wdel_1_2_wdel_face 1o0
    show wdel_1_2_hero_face 1
    hero "Oh{w=[wt2]}, s{w=[wt1]}-sorry!{w=[wt2]} Are you in detention?"

    show wdel_1_2_wdel_face 1o1
    hide wdel_1_2_hero_face 1
    wdel "Detention?{w=[wt2]} Me?{w=[wt2]}{nw}"

    show wdel_1_2_wdel_face 1a1
    wdel "Detention?{w=[wt2]} Me?{w=[wt2]}{fast} {bt}Nahh...!{/bt}{w=[wt3]} I'm just cleaning the window to see if I can see your mom getting banged from here!"

    show wdel_1_2_wdel_face 1a0
    hero ".{w=[wt1]}.{w=[wt1]}.{w=[wt2]}"

    show wdel_1_2_hero_face 1
    hero ".{w=[wt1]}.{w=[wt1]}.{w=[wt2]}{fast} Maybe I should report that offense to the Student Council{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Yeah{w=[wt1]}, good idea.{w=[wt3]} See ya."

    show wdel_1_2_wdel 2
    hide wdel_1_2_wdel_head
    hide wdel_1_2_wdel_face
    hide wdel_1_2_wdel_hand
    hide wdel_1_2_hero_face 1
    show wdel_1_2_hero at CC
    show wdel_1_2_hero at RC_slow
    wdel "H{w=[wt1]}-hey!{w=[wt2]}{nw}"

    show wdel_1_2_hero at CC_heavy
    wdel "H{w=[wt1]}-hey!{fast} Wait up, bro!{w=[wt2]} I'm just messing with ya!{w=[wt2]} Come back!{w=[wt3]}{nw}"

    hide wdel_1_2_fg
    show wdel_1_2_wdel 3
    show wdel_1_2_wdel_face 4a1
    show wdel_1_2_fg:
        blend "add"
    wdel "H{w=[wt1]}-hey!{fast} Wait up, bro!{w=[wt2]} I'm just messing with ya!{w=[wt2]} Come back!{w=[wt3]}{fast} Look{w=[wt1]}, I'm even cleaning this desk so you can sit here and keep me company{w=[wt1]}, see?"

    show wdel_1_2_hero_face 1
    hero "Fine{w=[wt2]}, not like I have anything better to do anyway.{nw}"

    play SE1 "Boing1.mp3"

    show wdel_1_2_wdel 3 at Scare
    show wdel_1_2_wdel_face 4a0  at Scare
    hide wdel_1_2_hero_face
    hero "Fine{w=[wt2]}, not like I have anything better to do anyway.{fast}"

    scene wdel_1_2_bg
    show wdel_1_2_mg
    show wdel_1_2_wdel 1
    show wdel_1_2_wdel_head 2
    show wdel_1_2_wdel_face 2o0
    show wdel_1_2_wdel_hand 1
    show wdel_1_2_hero 2
    show wdel_1_2_hero_face a0
    show wdel_1_2_fg:
        blend "add"
    with pixellate

    show wdel_1_2_hero_face a1
    hero "So{w=[wt1]}, what'd you do to get in trouble?"

    show wdel_1_2_hero_face a0
    show wdel_1_2_wdel_face 2o1
    wdel "Huh{w=[wt2]}, nothing special.{w=[wt3]} Just got caught punching someone."

    show wdel_1_2_hero_fx 1
    show wdel_1_2_hero at Scare
    show wdel_1_2_hero_face s1 at Scare
    show wdel_1_2_wdel_face 2o0
    hero "{aw}Ehhh!?{/aw}{w=[wt3]} You got in a fight with another girl?"

    hide wdel_1_2_hero_fx
    show wdel_1_2_hero_face s0
    show wdel_1_2_wdel_face 2o2
    wdel "Huh?{w=[wt2]} Hell no, dumbass!{w=[wt3]} If I hit girls, I would've already decked that nano-robot from the other class!{w=[wt4]} Damn Student Council lapdog!{w=[wt2]} She needs to mind her own business.{w=[wt4]} She's lucky that a dude should never punch a little girl like her!"

    show wdel_1_2_wdel_face 2o0 with None
    menu:
        wdel "Huh? Hell no, dumbass! If I hit girls, I would've already decked that nano-robot from the other class! Damn Student Council lapdog! She needs to mind her own business. She's lucky that a dude should never punch a little girl like her!{fast}"

        "Ask if she's a guy":
            $ a_event_0 = 1
            show wdel_1_2_hero_face a1
            hero "W{w=[wt1]}-wait{w=[wt2]}, are you a guy...?"

        "Say she looks like a girl":
            $ a_event_0 = 2
            show wdel_1_2_hero_face a1
            hero "Well{w=[wt2]}, Y{w=[wt1]}-you look like a girl to me..."

    show wdel_1_2_hero_face a0
    wdel "{w=[wt2]}.{w=[wt2]} .{w=[wt2]} .{w=[wt4]}{nw}"

    if a_event_0 == 1:
        $ add_stat("wdel", "love", 2)
    elif a_event_0 == 2:
        $ add_stat("wdel", "lust", 2)

    show wdel_1_2_wdel_hand 2
    show wdel_1_2_wdel_face 3o1
    wdel ". . .{fast} Oh{w=[wt2]}, wait{w=[wt2]}, you're right{w=[wt2]}, forgot this detail.{w=[wt3]} I'm a girl too."

    show wdel_1_2_wdel_face 3o0
    show wdel_1_2_hero_fx 1
    show wdel_1_2_hero at Scare
    show wdel_1_2_hero_face s1 at Scare
    hero "{pa}How does someone forget that!?{/pa}"

    hide wdel_1_2_hero_fx
    show wdel_1_2_hero_face a1

    if perk_int_mem >= 1:

        hero "Your name is {nm}[fnamewdel]{/nm}, right?"

        $ msg.msg(renpy.translate_string("You know {nm}[fnamewdel]{/nm} a little more"))
        $ add_stat("wdel", "inti", 0.5)
        $ add_stat("wdel", "love", 0.5)
        $ add_stat("hero", "cha_soc", 1.0)

        show wdel_1_2_hero_face a0 with None

        show wdel_1_2_wdel_hand 1
        show wdel_1_2_wdel_face 2a0
        with dissolve

        show wdel_1_2_wdel_face 2a1
        wdel "{gg}Heh!{/gg}, the right one!"

    else:
        hero "S{w=[wt1]}-sorry{w=[wt1]}, what's your name again?"

        show wdel_1_2_hero_face a0 with None

        show wdel_1_2_wdel_hand 1
        show wdel_1_2_wdel_face 2a0
        with dissolve

        show wdel_1_2_wdel_face 2a1
        wdel "It's {nm}[fnamewdel]{/nm}, bro!"
    
    show wdel_1_2_hero_face a0
    show wdel_1_2_wdel_face 2a0
    mind "(Well{w=[wt1]}, it's definitely a feminine name.)"

    show wdel_1_2_hero_face a0
    show wdel_1_2_wdel_face 2a1
    wdel "And yours?"
    
    show wdel_1_2_hero_face a1
    show wdel_1_2_wdel_face 2a0
    hero "I'm {nm}[fnamehero]{/nm}.{w=[wt2]} Nice to meet you!"

    scene wdel_1_3_bg
    show wdel_1_3_wdel 0
    with Fade(0.5,0,2)

    pause

    show wdel_1_3_wdel 1
    show wdel_1_3_wdel_face 1a0
    with Dissolve(1)

    show wdel_1_3_wdel_face 1a1
    wdel "Anyway, dude.{w=[wt2]} That nosy nano-robot probably couldn't handle the ass-kicking she deserves, y'know?{w=[wt2]} She'd snap like a twig."

    show wdel_1_3_wdel_face 1a0
    pause
    
    hero "{mind}(Wow{w=[wt2]}, she's not feminine at all{w=[wt1]}, but actually does look pretty feminine in the important parts){/mind}{w=[wt3]} S{w=[wt1]}-so{w=[wt2]}, well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} W{w=[wt1]}-who did you fight with?{w=[wt2]} What does this have to do with the president of the other classroom?"

    show wdel_1_3_wdel_face 1a1
    wdel "Well{w=[wt2]}, it wasn't really a fight, see?{w=[wt2]} That guy from our class who sits in the middle, y'know?{w=[wt3]} His face just looked so punchable that my fist moved on its own!{w=[wt3]} But we didn't fight.{w=[wt2]} Actually{w=[wt2]}, after I knocked him down and started stepping on him{w=[wt1]}, I got the impression he was enjoying it!"
    
    show wdel_1_3_wdel_face 1a0
    hero "{aw}Did you do what!?{/aw}{w=[wt3]} Oh{w=[wt2]}, wait{w=[wt2]}, that must've been {nm}[fnamehprv]{/nm}.{w=[wt3]} Maybe it's okay in this case.{w=[wt2]} {mind}(Depending on his angle of view from the floor{w=[wt1]}, he probably didn't mind being stepped on by a woman at all.){/mind}"
    
    show wdel_1_3_wdel_face 1o1
    wdel "That's when that ribbon-wearing robot from the Student Council showed up saying {i}'Infraction!{w=[wt1]} Beep beep!{w=[wt1]} Infraction!{w=[wt1]} Beep beep!'{/i}{w=[wt3]} And then put me in detention."

    show wdel_1_3_wdel_face 1o0
    hero "Oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Now I see."

    show wdel_1_3_wdel_face 1o1
    wdel "But you know what?{w=[wt3]}{nw}"

    show wdel_1_3_wdel_face 1a1
    wdel "But you know what?{w=[wt3]}{fast} I'm not letting it slide!"
    
    show wdel_1_3_wdel 2
    show wdel_1_3_wdel_face 2a0
    show wdel_1_3_wdel_fg 1
    with dissolve

    hero "Wait{w=[wt2]}, what are you doing with that paperclip?{w=[wt3]} You're not planning anything illegal, are you?"
    
    show wdel_1_3_wdel_face 2a1
    wdel "Shut up, dumbass!{w=[wt3]} I bet the teachers keep the whiteboard markers in this drawer{w=[wt1]}, wanna see?"
    
    show wdel_1_3_wdel_face 2a0 with None

    show wdel_1_3_wdel 3
    hide wdel_1_3_wdel_face
    hide wdel_1_3_wdel_fg
    with dissolve

    hero "N{w=[wt1]}-no I d-{w=[wt1]}...{w=[wt2]} I mean{w=[wt1]}, yes{w=[wt1]}, please show me everything."
    
    wdel "Awesome!{w=[wt2]} Make sure no one's coming!{w=[wt3]} It's not a big deal for you, huh?"
    
    hero "B{w=[wt1]}-big?{w=[wt2]} Doesn't look big at all.{w=[wt3]} I mean{w=[wt2]}, It actually looks quite small{w=[wt2]}, but it makes it easier to see everything else.{w=[wt3]} It's a good view."
    
    wdel "What are you saying, you weirdo!?{w=[wt3]} If it's not a problem for you{w=[wt2]}, then just shut up and look at it properly!"
    
    hero "S{w=[wt1]}-sure.{w=[wt2]} Nothing will escape my vision at this exact moment."

    pause
    
    show wdel_1_3_wdel 2
    show wdel_1_3_wdel_face 2a0
    show wdel_1_3_wdel_fg 2
    with dissolve

    pause
    
    show wdel_1_3_wdel_face 2a1
    wdel "{gg}Heh!{/gg}{w=[wt2]} See what I mean?"
    
    show wdel_1_3_wdel_face 2a0
    hero "I saw absolutely everything."
    
    scene wdel_1_4_bg
    show wdel_1_4_hero_body
    show wdel_1_4_hero_face s0
    with fade

    show wdel_1_4_wdel 1 with dissolve

    wdel "{lg}GAH HA HA HA...{/lg}{w=[wt3]} You look like such an idiot right now!{w=[wt2]} Don't tell me you expected me not to make it?"
    
    show wdel_1_4_hero_face s1
    hero "N{w=[wt1]}-no{w=[wt1]}, I..."

    show wdel_1_4_hero_face s0 with None
    show wdel_1_4_wdel 2 with dissolve
    wdel "Shut up, you wimp!{w=[wt2]} Now you'll see my artistic talent!"

    hero ".{w=[wt2]}.{w=[wt2]}.{w=[wt3]}{nw}"

    show wdel_1_4_hero_face s2
    hero ".{w=[wt2]}.{w=[wt2]}.{w=[wt3]}{fast} {aw}Whaaaat!?{/aw}{w=[wt3]} Wait{w=[wt1]}, you're going to draw on the window you just cleaned with a whiteboard marker!?"
    
    show wdel_1_4_hero_face s0
    wdel "{lg}GAH HA HA HA...{/lg}{w=[wt3]} Of course, dumbass!{w=[wt3]} Want a marker?{w=[wt3]} If you're too chicken{w=[wt1]}, just sit back and watch a master at work!"

    menu:
        "Join her":
            show wdel_1_4_hero_face o1
            hero "Alright!{w=[wt2]} Pass me a marker then!"
            
            $ add_stat("wdel", "love", 2)
            $ add_stat("hero", "cha_soc", 2)
            
            show wdel_1_4_hero_face o0
            wdel "That's what I'm talkin' about!{w=[wt3]} Just let me finish this masterpiece first{w=[wt1]}..."

        "Try to convince her to stop":
            show wdel_1_4_hero_face o3
            hero "Wait{w=[wt1]}, don't do it!{w=[wt3]} You're already in detention.{w=[wt2]} You'll get in even more trouble!"

            $ add_stat("wdel", "bonus", 20)
            
            show wdel_1_4_hero_face o2
            wdel "Relax{w=[wt1]}, I'll put everything back where it belongs.{w=[wt3]} If you keep your mouth shut{w=[wt1]}, no one will ever prove it was me!"

    show wdel_1_4_hero_face o3
    hero "B{w=[wt1]}-but..."

    show wdel_1_4_hero_face o2
    wdel "{aw}Almost done!{/aw}{w=[wt2]} Just a little line here and..."

    stop BGM fadeout 2
    scene bg_1 with Dissolve(2)

    play BGM "audio/W2C - MainTheme (PUNK).mp3"

    scene wdel_1_5_bg
    show wdel_1_5_fg
    with Dissolve(2)

    wdel "{pa}Check out this work of art!!!{/pa}"

    hero "Wait{w=[wt2]}, did you really draw that?{w=[wt3]} How old are you?"

    wdel "And you better keep your mouth shut!{w=[wt3]} Wonder what Little Miss Robot will think of it? {lg}GAH HA HA HA...{/lg}"

    stop BGM
    play SE1 "CartoonStratch.ogg"
    scene wdel_1_2_bg
    show wdel_1_2_hprv 1 at RC
    show wdel_1_2_hprv_face o0 at RC
    show wdel_1_2_wkuu at CC
    show wdel_1_2_wkuu_face o0 at CC
    show wdel_1_2_mg
    show wdel_1_2_hero 3
    show wdel_1_2_wdel 4
    show wdel_1_2_fg:
        blend "add"
    with vpunch

    play BGM "audio/W2C - Awkward.mp3"

    show wdel_1_2_wkuu_face o1
    wkuu "Regarding what I think{w=[wt2]}, it seems extremely irregular{w=[wt3]}. The visual pollution caused by the asymmetry is more obscene than the symbolism of the drawing itself{w=[wt1]}, since the artistic quality is not enough to represent it.{w=[wt2]} Please dedicate yourself more to biology and art classes."

    wkuu "Regarding the penalty of your detention{w=[wt2]}, it should increase due to new violations that include:{w=[wt4]} School property invasion{w=[wt2]}; vandalism of school property{w=[wt2]}; physical offense to student{w=[wt2]}; and disobedience of Student Council penalty.{w=[wt3]}{nw}"

    show wdel_1_2_hprv at CC_heavy
    show wdel_1_2_hprv_face o0 at CC_heavy
    wkuu "Regarding the penalty of your detention{w=[wt2]}, it should increase due to new violations that include:{w=[wt4]} School property invasion{w=[wt2]}; vandalism of school property{w=[wt2]}; physical offense to student{w=[wt2]}; and disobedience of Student Council penalty.{w=[wt3]}{fast} The previous punishment was only lenient because hitting the student {nm}[fnamehprv]{/nm} was presumed to be an act of justice."

    show wdel_1_2_wkuu_face o0 with None
    show wdel_1_2_hprv at CC_fast
    show wdel_1_2_hprv_face o1 at CC_fast

    hprv "Hey!!"

    show wdel_1_2_hprv_face o0
    show wdel_1_2_wkuu_face o1
    wkuu "{nm}[fnamehprv]{/nm}{w=[wt2]}, your detention period for making masochism expressions when being attacked by a classmate is over.{nw}"

    show wdel_1_2_hprv_face o2
    wkuu "{nm}[fnamehprv]{/nm}{w=[wt2]}, your detention period for making masochism expressions when being attacked by a classmate is over.{fast}{w=[wt2]} Please behave yourself.{w=[wt4]} Miss{w=[wt2]}, please report to the Student Council room immediately."

    show wdel_1_2_wkuu at RC_slow
    show wdel_1_2_wkuu_face o0 at RC_slow

    pause(1)

    show wdel_1_2_wdel 5 with dissolve
    hide wdel_1_2_wkuu
    hide wdel_1_2_wkuu_face

    wdel "Well{w=[wt1]}, bro.{w=[wt2]} Nice meeting you.{w=[wt3]} If I don't get expelled{w=[wt1]}, see ya!!"
    
    hero "S{w=[wt1]}-sure{w=[wt2]}, see ya."

    show wdel_1_2_wdel 6 with dissolve
    wdel "Oh{w=[wt2]}, Hey, dude!!{w=[wt3]}{nw}"

    scene wdel_1_2_bg
    show wdel_1_2_hprv_wdel_body
    show wdel_1_2_hprv_wdel_hand 1
    show wdel_1_2_mg
    show wdel_1_2_hero 3
    show wdel_1_2_fg:
        blend "add"

    wdel "Oh{w=[wt2]}, Hey, dude!!{w=[wt3]}{fast} We're cool, aren't we?{w=[wt3]} Ya didn't get mad at me 'cos of a few little punches and kicks, did you?"
    hprv "N{w=[wt1]}-no!{w=[wt2]} W{w=[wt1]}-we're cool."

    show wdel_1_2_hprv_wdel_hand 2 with Dissolve(1)

    $ zoomT1 = 0
    $ zoomX1 = 0
    $ zoomY1 = 0.4
    $ zoomS1 = 1
    $ alpha1 = 0

    $ zoomT2 = 1
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1
    $ zoomS2 = zoomS1
    $ alpha2 = 1

    scene wdel_1_2_bg
    show wdel_1_2_wdel 7
    show wdel_1_2_hprv 3
    show wdel_1_2_mg
    show wdel_1_2_hero 3
    show wdel_1_2_hero_fx 2 at ZoomSTXYA
    show wdel_1_2_fg:
        blend "add"

    play SE1 "Hit1.ogg"

    wdel "{aw}I know, bro!{w=[wt1]}{/aw}{nw}"

    play SE1 "Hit2.ogg"

    show wdel_1_2_hprv 4
    show wdel_1_2_wdel 8 at CC
    show wdel_1_2_wdel at RR_heavy
    wdel "{aw}I know, bro!{/aw}{fast}{w=[wt2]} See ya too!"

    $ zoomT1 = 0
    $ zoomX1 = 0
    $ zoomY1 = 0
    $ zoomS1 = 1
    $ alpha1 = 0

    $ zoomT2 = 3
    $ zoomX2 = zoomX1
    $ zoomY2 = 100
    $ zoomS2 = zoomS1
    $ alpha2 = 1

    show wdel_1_2_hero_fx 2 at ZoomSTXY_3

    hide wdel_1_2_wdel with dissolve

    pause

#---------------------------------------------------------------------------
    scene bg_0
    with Dissolve(2)

    $ add_stat("wdel", "inti", 3)

    $ wdel_quest_1 = 1

    call gametime_schoolnext from _call_gametime_schoolnext_5
    $ gametimemin += _return
    call gametime from _call_gametime_100

    pause

    play BGM "audio/W2C - Tranquility.mp3"
    
    call check_playermap from _call_check_playermap_35
    jump show_ui
#---------------------------------------------------------------------------
