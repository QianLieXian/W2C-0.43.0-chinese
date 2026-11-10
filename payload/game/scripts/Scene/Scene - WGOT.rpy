image wgot_1_2_wgot_vid 1 = Movie(play="images/Scene/WGOT - 1Meeting/wgot_1_2_wgot_vid 1.webm", loop=True)
image wgot_1_2_wgot_vid 2 = Movie(play="images/Scene/WGOT - 1Meeting/wgot_1_2_wgot_vid 2.webm", loop=True)
image qqwejqwe = Movie()

label wgot_quest0:

    stop BGM fadeout 3

    scene bg_0 with Dissolve(1) # HERO walking in school hallway.

    $ a_event_1  = _preferences.get_volume("bgm")
    #$ _preferences.set_volume
    $ renpy.music.set_volume(volume=a_event_1/8, delay=0, channel="BGM")
    play BGM "audio/W2C - Melancholy (Piano).mp3"

    # show screen wgot_piano_practice # gets short random piano sounds

    # HERO notices a melancholic music coming from the music room
    scene wgot_1_1_bg
    show wgot_1_1_hero 1
    with Dissolve(2)

    show wgot_1_1_hero 2 with dissolve
    mind "(Hmm?{w=[wt3]} Someone is playing piano?)"

    #scene bg_0 with dissolve

    $ renpy.music.set_volume(volume=1, delay=0, channel='BGM')

    #scene wgot_1_2_bg
    #show wgot_1_2_mg 1
    scene wgot_1_2_wgot_vid 1
    show wgot_1_2_fx_darkness:
        blend "multiply"
    with Dissolve(1)

    pause(0.5)
    
    show wgot_1_2_mg 2
    show wgot_1_2_hero 1
    show wgot_1_2_fx 1:
        blend "add"
    #hide wgot_1_2_wgot
    #show wgot_1_2_wgot 1
    with dissolve


    pause(0.5)

    mind "(Ohh{w=[wt2]}, that girl{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"

    #hide screen wgot_piano_practice # Closer view of the girl, WGOT, playing piano

    mind "(Ohh, that girl...{fast}{w=[wt2]} She's from my class!)"

    scene wgot_1_2_wgot_vid 1
    show wgot_1_2_fx_darkness:
        blend "multiply"
    show wgot_1_2_hero 2
    show wgot_1_2_hero_face 1o0
    with dissolve

    show wgot_1_2_hero_face 1o1
    pause(0.5)
    show wgot_1_2_hero_face 1o0
    pause(0.5)
    show wgot_1_2_hero_face 1o2

    pause

    scene wgot_1_2_wgot_vid 2
    show wgot_1_2_fx_darkness:
        blend "multiply"
    show wgot_1_2_hero 2
    show wgot_1_2_hero_face 1o2

    pause

    # WGOT notices HERO
    scene wgot_1_2_bg
    show wgot_1_2_mg 1
    show wgot_1_2_hero 2
    show wgot_1_2_hero_face 1o2
    show wgot_1_2_wgot 2
    with dissolve

    wgot "Huh...!?{nw}"

    stop BGM
    stop SE1
    play SE1 "Piano0.mp3"

    $ X_spd = 1

    show wgot_1_2_fx 2 at Opacity1
    show wgot_1_2_wgot 3
    show wgot_1_2_hero_face 1s0

    wgot "Huh...!?{fast}"

    hide wgot_1_2_fx
    show wgot_1_2_hero 3
    show wgot_1_2_hero_face 2o0
    with dissolve

    show wgot_1_2_hero_face 2o1
    hero "Ohh{w=[wt2]}, well{w=[wt2]}, t{w=[wt1]}-that was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{nw}"

    menu:
        hero "Ohh, well, t-that was...{fast}"

        "Beautiful":

            play BGM "audio/W2C - Mystic.mp3"

            hero "Ohh, well, t-that was...{fast} a beautiful music."
            
            $ add_stat("wgot", "love", 2)
            $ add_stat("hero", "cha_soc", 2)

            show wgot_1_2_hero_face 2o0 with None

            show wgot_1_2_wgot 4
            show wgot_1_2_wgot_mouth o0
            with dissolve # WGOT gets embarrassed

            pause(1.5)
            
            show wgot_1_2_wgot_mouth o1
            show wgot_1_2_hero_face 2o0
            wgot "It seems that beauty exists even in the darkest corners of existence.{w=[wt3]} Like how a corpse flower blooms magnificently despite smelling of decay."
            
        "Sad":

            play BGM "audio/W2C - Mystic.mp3"

            hero "Ohh, well, t-that was...{fast} a sad melody, right?"

            $ add_stat("wgot", "bonus", 20)

            show wgot_1_2_hero_face 2o0 with None

            show wgot_1_2_wgot 4
            show wgot_1_2_wgot_mouth o0
            with dissolve # WGOT gets embarrassed

            pause(1.5)
            
            show wgot_1_2_wgot_mouth o1
            show wgot_1_2_hero_face 2o0
            wgot "Yes.{w=[wt2]} Just how life is.{w=[wt3]} The piano speaks what my voice cannot.{w=[wt3]} The melody merely echoes the eternal melancholy that surrounds us all."

    show wgot_1_2_wgot_mouth o0
    show wgot_1_2_hero_face 2o1
    hero "{aw}Ehhh...?{/aw}{w=[wt4]} B{w=[wt1]}-by the way{w=[wt2]}, it was amazing!"

    show wgot_1_2_wgot_mouth o1
    show wgot_1_2_hero_face 2o0
    wgot "Thank you.{w=[wt3]} That was my funeral rehearsal."

    show wgot_1_2_wgot_mouth o0
    show wgot_1_2_hero_face 2o1
    hero "{pa}EHHHH!?!?{/pa}"

    show wgot_1_2_wgot_mouth o1
    show wgot_1_2_hero_face 2o0
    wgot "You're {nm}[fnamehero]{/nm} aren't you?{w=[wt3]} I must assure you I've studied the school rule book and found no prohibition against expressing one's impending doom through music.{w=[wt3]} But if you're here to report my trespassing anyway{w=[wt2]}, please note that my punishment should be swift and preferably fatal."

    show wgot_1_2_wgot_mouth o0
    show wgot_1_2_hero_face 2o1
    hero "N{w=[wt1]}-no!{w=[wt3]} W{w=[wt1]}-wait{w=[wt2]}, {aw}what!?{/aw}{w=[wt3]} I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} S{w=[wt1]}-sorry for entering like this.{w=[wt3]} I just wanted to hear it better!"

    show wgot_1_2_wgot_mouth o1
    show wgot_1_2_hero_face 2o0
    wgot "Ah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} A fellow wandering soul drawn to the music.{w=[wt3]} How delightfully tragic."

    if perk_int_mem >= 1:

        $ msg.msg(renpy.translate_string("You know {nm}[fnamewgot]{/nm} a little more"))
        $ add_stat("wgot", "inti", 0.5)
        $ add_stat("wgot", "love", 0.5)
        $ add_stat("hero", "cha_soc", 1.0)

        show wgot_1_2_wgot_mouth o0
        show wgot_1_2_hero_face 2o1
        hero "So{w=[wt2]}, you're {nm}[fnamewgot]{/nm}, right?"

        show wgot_1_2_wgot_mouth o1
        show wgot_1_2_hero_face 2o0
        wgot "Yes{w=[wt2]}, that's me.{w=[wt3]} I apologize for being in your class."

    else:

        show wgot_1_2_wgot_mouth o0
        show wgot_1_2_hero_face 2o1
        hero "Y{w=[wt1]}-you're in class 1B, right?"

        show wgot_1_2_wgot_mouth o1
        show wgot_1_2_hero_face 2o0
        wgot "Yes{w=[wt2]}, I'm {nm}[fnamewgot]{/nm}.{w=[wt3]} I apologize for being in your class."

    # View: Camera pans around the dark room. All curtains are drawn, only thin strips of light peek through

    show wgot_1_2_wgot_mouth o0
    show wgot_1_2_hero_face 2o1
    hero "Nice to meet you, {nm}[fnamewgot]{/nm}."

    show wgot_1_2_hero_face 2o0 with None

    hide wgot_1_2_hero
    hide wgot_1_2_hero_face
    with dissolve

    scene wgot_1_3_bg
    show wgot_1_3_wgot 1
    show wgot_1_3_wgot_face o0
    with Dissolve(1)

    hero "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{nw}"

    $ X_spd = 1
    show wgot_1_3_hero 1 at Opacity2
    hero "Well...{fast}{w=[wt4]} I was walking down the hallway when I heard you playing.{w=[wt4]} It's pretty dark in here{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Do you always practice with the curtains closed?"

    # View: WGOT's silhouette against the thin strips of light
    show wgot_1_3_wgot_face o1
    wgot "I found comfort in darkness and solitude.{w=[wt3]} The sun's harsh judgment scorches my flesh{w=[wt2]}, much like society's gaze burns the soul.{w=[wt3]} In the end{w=[wt2]}, it turns into an eternal cycle where I hide even more from the light and from people.{w=[wt3]} Here{w=[wt2]}, in the shadows{w=[wt2]}, I can be myself without inflicting my presence upon others."

    show wgot_1_3_wgot_face o0 with None
    show wgot_1_3_hero 2 with dissolve
    hero "I see{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Sorry for asking.{w=[wt2]} You must have been through a lot."

    show wgot_1_3_wgot_face o1
    wgot "Don't worry.{w=[wt3]} The darkness and I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Understand each other."

    show wgot_1_3_wgot_face o0 with None

    scene bg_0 with Dissolve(1)

    # View: HERO is putting a chair on the side of WGOT's stool to sit close to her.
    scene wgot_1_4_bg
    show wgot_1_4_hero 1 at RC
    show wgot_1_4_hero_face a0 at RC
    show wgot_1_4_hero 1 at CC_slow
    show wgot_1_4_hero_face a0 at CC_slow
    show wgot_1_4_wgot 1
    show wgot_1_4_wgot_m o0
    show wgot_1_4_wgot_e d
    with Dissolve(2)

    show wgot_1_4_wgot_e s
    show wgot_1_4_hero_face a1
    hero "So, {nm}[fnamewgot]{/nm}{w=[wt2]}, I don't think we've had a proper conversation yet."

    show wgot_1_4_wgot_e d
    show wgot_1_4_hero_face a2
    show wgot_1_4_hero 2
    with dissolve

    show wgot_1_4_wgot_m o1
    wgot "I don't recommend you get too close to me."

    show wgot_1_4_wgot_m o0
    show wgot_1_4_hero_face s1
    hero "S{w=[wt1]}-sorry{w=[wt2]}, I didn't mean to be intrusive."

    show wgot_1_4_wgot_m o1
    show wgot_1_4_hero_face s0
    wgot "You did nothing wrong.{w=[wt3]} You seem like a good person.{w=[wt3]} I just don't want your life to become another chapter in my book of accidental tragedies."

    show wgot_1_4_wgot_m o0
    show wgot_1_4_hero_face s1
    hero "W{w=[wt1]}-what do you mean?"

    show wgot_1_4_wgot_m o1
    show wgot_1_4_hero_face s0
    wgot "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} My goldfish committed suicide by jumping from their bowl.{w=[wt3]} My birthday cakes mysteriously develop mold overnight.{w=[wt3]} My cactus decided death was preferable to my care.{w=[wt3]} My childhood pets met tragic ends.{w=[wt3]} The last person who sat this close developed an inexplicable rash in the shape of a skull."

    show wgot_1_4_wgot_m o0
    show wgot_1_4_hero_face s1
    hero "{aw}Ehhh...?{/aw}{w=[wt3]} W{w=[wt1]}-wait{w=[wt2]}, are you saying you give bad omens or something?"

    show wgot_1_4_hero_face s0 with None

    $ X_spd = 3

    scene wgot_1_8_bg
    show wgot_1_8_fg1
    with Dissolve(2)

    show wgot_1_8_fg1 at Opacity1
    show wgot_1_8_fg2 at Opacity2
    wgot "Have you ever noticed how energy flows between living things?{w=[wt3]} Like ripples in a dark pond{w=[wt2]}, spreading outward{w=[wt1]}...{w=[wt2]} affecting everything they touch."

    wgot "Like the ripples{w=[wt2]}, some things vibrate at positive frequencies{w=[wt1]}, sharing life{w=[wt2]}, while others{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Well{w=[wt3]}, let's just say my particular frequency tends to disturb the natural harmony.{w=[wt3]} Nothing good happens to anyone who comes close to a curse."

    hero "C{w=[wt1]}-curse...?"

    wgot "Yes."

    $ zoomT1 = 0
    $ zoomX1 = 0.85
    $ zoomY1 = 0.95
    $ zoomS1 = 1

    $ zoomT2 = 20
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1
    $ zoomS2 = 2

    scene wgot_1_7_bg at ZoomSTXY with dissolve # HERO looking WGOT's cleavage

    hero "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I don't know what kind of curse you're talking about{w=[wt2]}, but I think I'm already seeing some good luck right now."

    wgot "Really?{w=[wt2]} What are you seeing?"

    scene wgot_1_4_bg at Shake2
    show wgot_1_4_hero 2 at Shake2
    show wgot_1_4_hero_fx at Shake2
    show wgot_1_4_hero_face s3 at Shake2
    show wgot_1_4_wgot 1 at Shake2
    show wgot_1_4_wgot_e s at Shake2
    show wgot_1_4_wgot_m o0 at Shake2

    hero "{aw}Eh!?{/aw}{w=[wt2]} W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Good things happens all the time, you know?{w=[wt3]} Maybe good and bad luck are just a matter of perspective!{w=[wt2]} What if something seen as a bad omen is actually a good thing if used well?"

    show wgot_1_4_wgot_m o1
    show wgot_1_4_hero_face s2
    wgot "Damn{w=[wt2]}, so you weren't predicting my death after all."

    show wgot_1_4_wgot_m o0
    show wgot_1_4_hero_face s1
    hero "{aw}Ehhh!?{/aw}{w=[wt3]} O{w=[wt1]}-of course not!!!"

    show wgot_1_4_hero_face o0 with None
    show wgot_1_4_wgot_e d with dissolve

    show wgot_1_4_wgot_m o1
    wgot "I'm sorry.{w=[wt3]} I appreciate your kind words{w=[wt2]}, but I can't see any good in being around me.{w=[wt3]} I still believe that getting close to me will bring you downfall in some way."

    show wgot_1_4_wgot_m o0 with None

    menu:
        "Flirt":
            show wgot_1_4_hero_face a3
            hero "But I don't!{w=[wt2]} To me it's quite the opposite.{w=[wt2]} I feel lucky for have seen you here."

            show wgot_1_4_wgot_m o1
            show wgot_1_4_hero_face a4
            wgot "You just don't know me."

            show wgot_1_4_wgot_m o0
            show wgot_1_4_hero_face o1
            hero "So give me a chance to get to know you.{w=[wt3]} If I'm wrong{w=[wt1]}, then you're worth any risk!{w=[wt3]}{nw}"

            show wgot_1_4_hero_face o2
            hero "So give me a chance to get to know you.{w=[wt3]} If I'm wrong{w=[wt1]}, then you're worth any risk!{w=[wt3]}{fast} {mind}(What man wouldn't die for a cute goth girl?){/mind}"

            $ add_stat("wgot", "lust", 1)
            $ add_stat("wgot", "love", 1)

            show wgot_1_4_wgot_m o1
            wgot "How bold{w=[wt2]}... Most flee from the darkness{w=[wt3]}, yet you embrace it with questionable intentions.{w=[wt3]} Why do they say women are the mysterious ones?{w=[wt2]} Men need to be studied in depth."

            show wgot_1_4_wgot_m o0
            show wgot_1_4_hero_face s1
            hero "T{w=[wt1]}-that's not it!{w=[wt2]} I mean{w=[wt3]}, I'm kinda lucky already.{w=[wt3]} So we won't have a problem about me{w=[wt1]}, I guess."
            
        "Comfort her":
            show wgot_1_4_hero_face a3
            hero "If that's the case{w=[wt2]}, it won't be a problem to me."

            show wgot_1_4_wgot_m o1
            show wgot_1_4_hero_face a4
            wgot "What do you mean?"

            show wgot_1_4_wgot_m o0
            show wgot_1_4_hero_face a3
            hero "Actually{w=[wt2]}, I feel like I have really good luck.{w=[wt3]} Maybe I could balance things out or even cure your unluck?"
            
            $ add_stat("wgot", "love", 2)
            
            show wgot_1_4_wgot_m o1
            show wgot_1_4_hero_face a4
            wgot "Balance the darkness with light?{w=[wt2]} How{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} intriguing.{w=[wt3]} Though I should warn you{w=[wt2]}, the last optimist who tried that now works as a professional mime.{w=[wt4]} The trauma rendered them speechless."

            show wgot_1_4_wgot_m o0
            show wgot_1_4_hero_face a3
            hero "Regardless{w=[wt2]}, I don't think you deserve to feel alone all the time.{w=[wt4]} So know you can count on me from now on, okay?"

    stop BGM fadeout 3

    show wgot_1_4_wgot_m o1
    show wgot_1_4_hero_face a4
    wgot "I see.{w=[wt3]} So you really trust your luck that much?{w=[wt3]} Do you really think it would be worth approaching me? "

    show wgot_1_4_wgot_m o0
    show wgot_1_4_hero_face a5
    hero "{aw}Sure!{/aw}"

    show wgot_1_4_hero_face a2 with None

    play BGM "audio/W2C - Tranquility.mp3"

    $ X_spd = 3
    $ X_pos = -450

    scene wgot_1_6_bg # Outside, courtyard view. WNEI is trying to catch a bug.
    show wgot_1_6_mg l at OR
    show wgot_1_6_wnei l at OR
    show wgot_1_6_wkuu l at OR
    show wgot_1_6_mg l at X_X
    show wgot_1_6_fx:
        blend "add"
    with Dissolve(1)

    show wgot_1_6_wnei l at X_X
    hero "You know{w=[wt2]}{nw}"

    show wgot_1_6_wkuu l at X_X
    hero "You know{fast}, I found myself in a desperate situation a few days ago.{w=[wt3]}{nw}"

    $ X_pos = 2400
    show wgot_1_6_mg at X_X
    hero "You know, I found myself in a desperate situation a few days ago.{fast} But then I decided to accept the help that was offered to me{nw}"

    show wgot_1_6_wnei r at X_X
    hero "You know, I found myself in a desperate situation a few days ago. But then I decided to accept the help that was offered to me{fast}{w=[wt2]}, and I ended up realizing that I was not alone.{nw}"

    show wgot_1_6_wkuu r at X_X
    hero "You know, I found myself in a desperate situation a few days ago. But then I decided to accept the help that was offered to me, and I ended up realizing that I was not alone.{fast}{w=[wt4]} Well{w=[wt2]}, I can say I feel much better now."

    $ X_spd = 2

    scene wgot_1_9_bg # The bugs are mating behind the wilted flower
    show wgot_1_9_mg1 at CC
    show wgot_1_9_mg2 1 at OR
    show wgot_1_9_mg2 1 at CC_X
    show wgot_1_9_fg
    with Dissolve(2)

    show wgot_1_9_mg2 2 at CC

    hero "I believe that bad days happen to everyone{w=[wt2]}, but they might not last forever.{w=[wt2]}{nw}"

    $ X_spd = 0.15

    $ Z_zoom = 1
    $ X_pos = 2
    $ Y_pos = 2
    $ alpha1 = 1

    $ Z_zoom2 = 1
    $ X_pos2 = -2
    $ Y_pos2 = -2
    $ alpha2 = 1

    show wgot_1_9_mg1 at Move_Repeat
    show wgot_1_9_mg2 2 at Move_Repeat

    $ X_spd = 1

    $ Z_zoom = 0.01
    $ X_pos = 0
    $ Y_pos = 500
    $ alpha1 = 1

    $ Z_zoom2 = 1
    $ X_pos2 = 0
    $ Y_pos2 = 0
    $ alpha2 = 0

    show wgot_1_9_fx at CC
    show wgot_1_9_fx at Move_Repeat2

    hero "I believe that bad days happen to everyone, but they might not last forever.{fast}"

    scene wgot_1_4_bg
    show wgot_1_4_hero 2
    show wgot_1_4_hero_face a2
    show wgot_1_4_wgot 1
    show wgot_1_4_wgot_e d
    show wgot_1_4_wgot_m o0
    with Dissolve(2)

    show wgot_1_4_hero_face a5
    hero "I just wanna say that{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I don't know what you've been through, but know that you can count on me if you need."

    show wgot_1_4_hero_face a2

    play SE1 "BellSchool.mp3"

    pause(2)

    show wgot_1_4_wgot_m o1
    wgot "Ah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Time's tyrannical march continues.{w=[wt3]}{nw}"

    show wgot_1_4_wgot_e s
    wgot "Ah... Time's tyrannical march continues.{fast}{w=[wt3]} {nm}[fnamehero]{/nm}{w=[wt2]}, thank you for your kindness.{w=[wt3]} Your bravery in the face of supernatural warning is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} intriguing.{w=[wt4]} Perhaps fate has plans for us after all.{w=[wt3]} Until darkness brings us together again{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} If we're both still breathing by then."

    show wgot_1_4_wgot_m o0
    stop BGM fadeout 3

#---------------------------------------------------------------------------
    scene bg_0
    with Dissolve(2)

    $ add_stat("wgot", "inti", 3)

    $ wgot_quest_1 = 1

    call gametime_schoolnext from _call_gametime_schoolnext_8
    $ gametimemin += _return
    call gametime from _call_gametime_104

    pause

    play BGM "audio/W2C - Tranquility.mp3"
    
    call check_playermap from _call_check_playermap_39
    jump show_ui
#---------------------------------------------------------------------------
