image wota_swimming2_bloodfx:
    "images/Scene/WOTA - SwimmingPool/wota_swimming2_bloodfx 1.webp"
    0.1
    "images/Scene/WOTA - SwimmingPool/wota_swimming2_bloodfx 2.webp"
    0.1
    "images/Scene/WOTA - SwimmingPool/wota_swimming2_bloodfx 3.webp"
    0.1
    "images/Scene/WOTA - SwimmingPool/wota_swimming2_bloodfx 4.webp"
    0.1
    repeat

#---------------------------------------------------------------------------
label wota_quest0: # Swimming Area
#---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_188
    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night

    scene bg_0
    with Dissolve(1)

    scene wota_swimming1_bg
    show wota_swimming1_wricbody 1
    show wota_swimming1_wricface 0
    show wota_swimming1_wgalbody 1
    show wota_swimming1_wgalface 0
    show wota_swimming1_wotabody
    show wota_swimming1_wotaface o0
    show wota_swimming1_herobody
    show wota_swimming1_heroface a0
    show wota_swimming1_heroeye m
    with Dissolve(3)
    pause

    show wota_swimming1_heroface a1
    show wota_swimming1_wotaface o0
    hero "Hey, {nm}[fnamewota]{/nm}{w=[wt1]}, is that you?"

    show wota_swimming1_heroface a0
    show wota_swimming1_wotaface o1
    wota "How do you dare not recognize me?"

    show wota_swimming1_heroface a1
    show wota_swimming1_wotaface o0
    hero "It's kinda hard recognize everyone here with these caps{w=[wt2]}, even more when I barely see your eyes.{w=[wt3]} Well{w=[wt2]}, actually{w=[wt2]}, I think this would be more a point that made me think it was you.{w=[wt2]} It's hard to see your eyes when you're wearing your common glasses anyway."

    show wota_swimming1_heroface a0
    show wota_swimming1_wotaface o1
    wota "My eyes cannot be seen by ordinary mortals.{w=[wt2]} This is why we wear glasses with thick lenses{w=[wt2]}, even in swimming glasses.{w=[wt3]} These lenses suppress my powers{w=[wt2]}, what allow you humans to remain alive{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} M{w=[wt1]}-maybe they also serve for some degree of myopia{w=[wt2]}, but this is irrelevant!{nw}"

    show wota_swimming1_heroface a0
    show wota_swimming1_wotaface o0
    menu:
        wota "My eyes cannot be seen by ordinary mortals. This is why we wear glasses with thick lenses, even in swimming glasses. These lenses suppress my powers, what allow you humans to remain alive... M-maybe they also serve for some degree of myopia, but this is irrelevant!{fast}"
        "Thank her for her protection":
            $ add_stat("wota", "love", 1)
            $ add_stat("hero", "cha_soc", 1)
            show wota_swimming1_heroface a1
            show wota_swimming1_wotaface o0
            hero "Got it!{w=[wt2]} Thank you protect us, {nm}Mrs. Extraordinary Being{/nm}!"
            show wota_swimming1_heroface a0
            show wota_swimming1_wotaface a1
            wota "You don't need to.{w=[wt2]} It's just my job."
        "Tell you find her cute with glasses":
            $ add_stat("wota", "lust", 1)
            $ add_stat("hero", "cha_soc", 0.1)
            show wota_swimming1_heroface a1
            show wota_swimming1_wotaface o0
            hero "Got it!{w=[wt2]} I think you look cute with your glasses!"
            show wota_swimming1_wotafx
            with dissolve
            show wota_swimming1_heroface a0
            show wota_swimming1_wotaface o1
            wota "Hunf!{w=[wt2]} I knew that!{w=[wt2]} You really are a hunter of good girls!{w=[wt3]} For your information{w=[wt1]}, keep in mind that I'm a very bad girl and won't let you keep hitting on {nm}[fnamewnei]{/nm}!{w=[wt4]} S{w=[wt1]}-she's a baby that must be protected!"
            show wota_swimming1_heroface s1
            show wota_swimming1_wotaface o0
            hero "{pa}Ehhh!?{/pa}{w=[wt2]} W{w=[wt1]}-what?"
            show wota_swimming1_heroface s0
            hide wota_swimming1_wotafx
            with dissolve
            show wota_swimming1_wotaface o1
            wota "Glad you understood."

    show wota_swimming1_heroeye l
    show wota_swimming1_wotaface o0
    $ a_check_1 = "Teacher"
    sup1 "Remember:{w=[wt3]} 1 lap of Butterfly{w=[wt2]}; 1 lap of Backstroke{w=[wt2]}; 1 lap of Breathstroke{w=[wt2]}; and 1 lap of Crawl Stroke!{w=[wt4]} On your marks{w=[wt3]}; get set{w=[wt3]}; Go!"

    show wota_swimming1_heroeye m
    show wota_swimming1_heroface a0
    show wota_swimming1_wotaface o1
    with dissolve
    wota "Anyway{w=[wt1]}, I hope this stupid waste of time of class will end soon.{w=[wt3]} This is already draining my vital energy."

    show wota_swimming1_heroface a1
    show wota_swimming1_wotaface o0
    hero "Come on{w=[wt1]}, it's not that bad.{w=[wt3]} I bet you will learn how to swim in no time!"

    show wota_swimming1_wotafx
    show wota_swimming1_heroface a0
    with dissolve
    show wota_swimming1_wotaface o1
    wota "I{w=[wt1]}-I know how to swim, okay!?{w=[wt2]} I'm j{w=[wt1]}-just using this equipment to suppress my powers.{w=[wt2]} Just that!{w=[wt3]} Hunf{w=[wt2]}, people are so intrusive{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Anyway{w=[wt2]}, changing the subject{w=[wt2]}, what happened after you went after {nm}[fnamewsis]{/nm}?"

    show wota_swimming1_heroface a1
    show wota_swimming1_wotaface o0
    hide wota_swimming1_wotafx
    with dissolve
    hero "H{w=[wt1]}-huh...?{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} You girls were right.{w=[wt2]} She was about to fight with {nm}[fnamehriv]{/nm}.{w=[wt2]} somehow I managed to make them stop."

    show wota_swimming1_heroface a0
    show wota_swimming1_wotaface a1
    wota "Heh.{w=[wt2]} I knew it, right?{w=[wt2]} You really are the hero of prophecy!"

    show wota_swimming1_heroface a1
    show wota_swimming1_wotaface a0
    hero "What prophecy?"

    show wota_swimming1_heroface a0
    show wota_swimming1_wotaface a1
    wota "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} T{w=[wt1]}-that's not important now!{w=[wt2]} What is important is that you're the main character of a great story!"

    show wota_swimming1_heroface a1
    show wota_swimming1_wotaface a0
    hero "{lg}Ha Ha Ha...{/lg} Me?{w=[wt2]} The main character of a story?{w=[wt2]} You have quite an imagination!{w=[wt4]} So{w=[wt2]}, what kind of story would it be?"

    show wota_swimming1_heroface a0
    show wota_swimming1_wotaface a1
    wota "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} I{w=[wt1]}-It's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} It's about saving the world from the forces of the evil!"

    show wota_swimming1_wotaface a0

    menu:
        "Tell her that you like this story":
            $ add_stat("wota", "love", 2)
            $ add_stat("hero", "cha_soc", 2)
            show wota_swimming1_heroface a1
            show wota_swimming1_wotaface a0
            hero "I'm glad I'm the hero of this story.{w=[wt2]} You can count on me to save the world!"            
            show wota_swimming1_heroface a0

        "Ask her if you'd have a princess in this story":        
            show wota_swimming1_heroface a1
            show wota_swimming1_wotaface a0
            hero "So{w=[wt1]}, since I'm a hero{w=[wt2]}, does this prophecy say something about me getting a princess{w=[wt1]}, maiden{w=[wt1]}, or something?"
            show wota_swimming1_heroface a0
            show wota_swimming1_wotaface a1
            wota "Of course, Hero-san!{w=[wt2]} You will marry {nm}[fnamehriv]{/nm}{w=[wt1]}{nw}"
            show wota_swimming1_heroface s0
            wota "Of course, Hero-san! You will marry {nm}[fnamehriv]{/nm}{fast}, and both will have a lifetime of love and pleasure!{w=[wt2]}{nw}"
            $ add_stat("wota", "lust", 2)
            $ add_stat("hero", "cha_soc", 0.2)
            wota "Of course, Hero-san! You will marry {nm}[fnamehriv]{/nm}{fast}, and both will have a lifetime of love and pleasure!{fast} {pr}{lg}He-He...{w=[wt2]} He-He...{w=[wt2]} He-He...{/lg}{w=[wt2]} M{w=[wt1]}-maybe you'll get pregnant and{w=[wt1]}-"
        
            show wota_swimming1_heroface s1
            show wota_swimming1_wotaface a0
            hero "{aw}I don't wanna be the hero of this story!{/aw}"

            show wota_swimming1_heroface s0

    show wota_swimming1_wotaface a1
    wota "{gg}Tee-hee-hee...{/gg}{w=[wt2]} I could even think about stopping scripting fanfics and starting to master an RPG if I had enough guinea pigs{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I mean{w=[wt2]}, f{w=[wt1]}-friends!"

    show wota_swimming1_wotaface o0
    show wota_swimming1_heroeye l
    with dissolve

    $ a_check_1 = "Teacher"
    sup1 "Well done!{w=[wt2]} Now rest while it's the turn of our colleagues.{w=[wt3]} Come here when I call your name on the list.{w=[wt4]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} {nm}[fnamewgal]{/nm}?"

    show wota_swimming1_wricbody 2
    show wota_swimming1_wgalbody 2
    hide wota_swimming1_wricface
    hide wota_swimming1_wgalface
    show wota_swimming1_heroeye r
    with dissolve
    wgal "{bt}Wooorld{/bt}{w=[wt2]}, looks like my time to shine has come!"

    hide wota_swimming1_wotafx
    with dissolve
    show wota_swimming1_heroface a0
    show wota_swimming1_wotaface o1
    show wota_swimming1_heroeye m
    wota "May the roof fall to her head{w=[wt2]}, amen."

    show wota_swimming1_heroface s1
    show wota_swimming1_wotaface o0
    hero "{aw}W{w=[wt1]}-what kind of prayer are you doing!?{/aw}"

    show wota_swimming1_heroface s0
    show wota_swimming1_wotaface o1
    wota "Nothing personal.{w=[wt2]} But if an accident happens here{w=[wt1]}, the class will have to be interrupted and I don't have to go through it!"

    stop BGM fadeout 2

    show wota_swimming1_wotaface o0
    show wota_swimming1_heroeye l
    sup1 "{nm}[fnamewota]{/nm}?"

    show wota_swimming1_heroface s0
    show wota_swimming1_wotaface o1
    show wota_swimming1_heroeye m
    wota "Damn it."

    show wota_swimming1_wotaface o0
    pause(0.1)

    scene wota_swimming2_bg
    show wota_swimming2_wric 1
    show wota_swimming2_hero 1
    show wota_swimming2_wota 1
    show wota_swimming2_wgal 1
    with Dissolve(1.5)

    pause

    $ X_pos = 1200

    show wota_swimming2_wgal 2 at X
    with Dissolve(0.25)

    play SE1 "Boing1.mp3"

    $ X_spd = 0.1
    $ X_pos = 1000

    show wota_swimming2_wgal 2 at X_X

    pause(0.1)

    $ X_spd = 1.5
    $ X_pos = -700

    show wota_swimming2_wgal 2 at X_X
    show wota_swimming2_wota 2 at RC
    show wota_swimming2_wota 2 at CC_slow

    pause(0.5)


    show wota_swimming2_hero 2
    show wota_swimming2_wric 2

    pause(0.5)

    show wota_swimming2_hero 3
    show wota_swimming2_wota 3

    play SE1 "Squeak1.ogg"

    $ check_stat()
    $ add_stat("wota", "lust", 2)

    #hide wota_swimming2_wgal
    hide wota_swimming2_wota
    hide wota_swimming2_hero
    show wota_swimming2_herowota 1
    show wota_swimming2_heroface o1
    show wota_swimming2_floater 1
    with dissolve

    play SE1 "SWFMoan239.ogg"

    play BGM "audio/W2C - Fun.mp3"

    show wota_swimming2_herowotafx 1
    show wota_swimming2_heroface s0
    with Dissolve(1)

    show wota_swimming2_heroface s1
    hero "S{w=[wt1]}-sorry{w=[wt2]}, I{w=[wt1]}-{nw}"

    pause(0.25)

    play SE1 "Slip.ogg"    

    hide wota_swimming2_heroface
    hide wota_swimming2_herowotafx
    show wota_swimming2_herowota 2
    show wota_swimming2_floater 2
    with Dissolve(0.2)

    $ add_stat("wota", "lust", 2)

    play SE1 "Squeak2.ogg"

    show wota_swimming2_herowota 3
    show wota_swimming2_floater 3
    pause(0.15)

    show wota_swimming2_herowota 4a
    show wota_swimming2_floater 4
    show wota_swimming2_herofx 1

    pause(1)

    show wota_swimming2_herofx 2
    with dissolve

    pause

    play SE1 "Dreamy SFX.mp3"

    scene bg_1
    show wota_swimming2_bg eggplant
    show wota_swimming2_herowota 4b
    show wota_swimming2_wotafx 1
    with Dissolve(2)

    pause(1)

    $ add_stat("wota", "lust", 2)

    play SE1 "Squeak2.ogg"
    show wota_swimming2_herowota 4c
    pause(0.2)
    show wota_swimming2_herowota 4b
    pause(1)

    $ add_stat("wota", "lust", 2)

    play SE1 "Squeak2.ogg"
    show wota_swimming2_herowota 4c
    pause(0.2)
    show wota_swimming2_herowota 4b

    pause(1)

    show wota_swimming2_wotafx 2
    with Dissolve(1)

    pause(1)

    play BGE "Water Squirt.ogg" fadein 1

    hide wota_swimming2_wric
    hide wota_swimming2_herowota
    show wota_swimming2_bloodfx
    show wota_swimming2_herowota 5

    pause(1)

    stop BGE fadeout 6

    scene bg_1
    with Dissolve(3)

    if wota_lust >= 80:
        pause(1)
        play SE1 "JingleRight.ogg"
        $ msg.msg(renpy.translate_string("{nm}[fnamewota]{/nm} came, and her lust reset."))
        $ xp_now += 25
        $ msg.msg(renpy.translate_string("XP [C_Pos]+ 25[C_Off]."))
        $ add_stat("wota", "inti", 3)

    pause(1)

    $ zoomS1 = 1
    $ zoomT1 = 0
    $ zoomX1 = 0.230
    $ zoomY1 = 0.4
    $ zoomS2 = 1.5
    $ zoomT2 = 60
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1

    scene wota_swimming2_bg at ZoomSTXY
    show wota_swimming2_herowota 6 at ZoomSTXY
    if preferences.gr:
        show wota_swimming2_fxblood at ZoomSTXY
    if wota_lust >= 80:
        show wota_swimming2_fxwet at ZoomSTXY
    show wota_swimming2_girls at ZoomSTXY
    hide wota_swimming2_bloodfx at ZoomSTXY
    with Dissolve(5)

    pause(1)

    wpre "{aw}Teacher{w=[wt2]}, {nm}[fnamewota]{/nm} got injured and passed out!!!{/aw}"

    $ a_check_1 = "Teacher"
    sup1 "{pa}What!?{/pa}"

    wgot "I saw everything, teacher.{w=[wt2]} In an attempted murder{w=[wt1]}, {nm}[fnamewgal]{/nm} pushed her{w=[wt1]}, who hit her nose on {nm}[fnamehero]{/nm}'s glasses breaking every bone of her head{w=[wt2]}, and died."

    wdis "{aw}{size=-5}I{w=[wt1]}-I'm sure she just t{w=[wt1]}-throught something p{w=[wt1]}-pervert.{/size}{/aw}"

    sup1 "{nm}[fnamewgal]{/nm}{w=[wt1]}, we need to have a serious conversation, young lady.{w=[wt2]} Don't go thinking my class is a mess!"

    wgal "W{w=[wt1]}-wait!{w=[wt2]} I swear didn't push hard!"

    sup1 "I don't want any excuses!{w=[wt3]} Now.{w=[wt2]} Come with me!"

    $ zoomS1 = 1.5
    $ zoomT1 = 0
    $ zoomX1 = 0.230
    $ zoomY1 = 0.4
    $ zoomS2 = 3
    $ zoomT2 = 2
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1

    scene wota_swimming2_bg at ZoomSTXY
    show wota_swimming2_herowota 6 at ZoomSTXY
    if preferences.gr:
        show wota_swimming2_fxblood at ZoomSTXY
    if wota_lust >= 80:
        show wota_swimming2_fxwet at ZoomSTXY
    show wota_swimming2_girls at ZoomSTXY
    hide wota_swimming2_bloodfx at ZoomSTXY

    pause(0.5)

    mind "(What just happened?)"

#---------------------------------------------------------------------------
    scene bg_0
    with Dissolve(2)

    $ add_stat("wota", "inti", 3)

    if wota_lust >= 80:
        $ wota_lust = 0

    $ wota_quest_1 = 1

    call gametime_schoolnext from _call_gametime_schoolnext_10
    $ gametimemin += _return
    call gametime from _call_gametime_114

    pause

    play BGM "audio/W2C - Tranquility.mp3"
    
    call check_playermap from _call_check_playermap_43
    jump show_ui
#---------------------------------------------------------------------------
