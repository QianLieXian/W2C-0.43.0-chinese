image wtpe_xxx_a2a0:
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2A0_1.webm", loop=True, start_image="wtpe_xxx_a", image="wtpe_xxx_a")
        4
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2A0_2.webm", loop=True, start_image="wtpe_xxx_a", image="wtpe_xxx_a")
        4
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2A0_3.webm", loop=True, start_image="wtpe_xxx_a", image="wtpe_xxx_a")
        4
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2A0_4.webm", loop=True, start_image="wtpe_xxx_a", image="wtpe_xxx_a")
        4
    repeat

image wtpe_xxx_a2a1:
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2A1_1.webm", loop=True, start_image="wtpe_xxx_a", image="wtpe_xxx_a")
        4
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2A1_2.webm", loop=True, start_image="wtpe_xxx_a", image="wtpe_xxx_a")
        4
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2A1_3.webm", loop=True, start_image="wtpe_xxx_a", image="wtpe_xxx_a")
        4
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2A1_4.webm", loop=True, start_image="wtpe_xxx_a", image="wtpe_xxx_a")
        4
    repeat

image wtpe_xxx_b2b:
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_B2B_1.webm", loop=True, start_image="wtpe_xxx_b", image="wtpe_xxx_b")
        2
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_B2B_2.webm", loop=True, start_image="wtpe_xxx_b", image="wtpe_xxx_b")
        2
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_B2B_3.webm", loop=True, start_image="wtpe_xxx_b", image="wtpe_xxx_b")
        2
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_B2B_4.webm", loop=True, start_image="wtpe_xxx_b", image="wtpe_xxx_b")
        2
    repeat

image wtpe_xxx_c2c1:
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_C2C1_1.webm", loop=True, start_image="wtpe_xxx_c", image="wtpe_xxx_c")
        2
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_C2C1_2.webm", loop=True, start_image="wtpe_xxx_c", image="wtpe_xxx_c")
        2
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_C2C1_3.webm", loop=True, start_image="wtpe_xxx_c", image="wtpe_xxx_c")
        2
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_C2C1_4.webm", loop=True, start_image="wtpe_xxx_c", image="wtpe_xxx_c")
        2
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_C2C1_5.webm", loop=True, start_image="wtpe_xxx_c", image="wtpe_xxx_c")
        2
    repeat

image wtpe_xxx_d2d:
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_D2D_1.webm", loop=True, start_image="wtpe_xxx_d", image="wtpe_xxx_d")
        2
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_D2D_2.webm", loop=True, start_image="wtpe_xxx_d", image="wtpe_xxx_d")
        2
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_D2D_3.webm", loop=True, start_image="wtpe_xxx_d", image="wtpe_xxx_d")
        2
    choice:
        Movie(play="images/Scene/WTPE - 1Meeting/WTPE_D2D_4.webm", loop=True, start_image="wtpe_xxx_d", image="wtpe_xxx_d")
        2
    repeat

image wtpe_xxx_a2b = Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2B.webm", loop=False, start_image="wtpe_xxx_a", image="wtpe_xxx_b")

image wtpe_xxx_a2c = Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2C.webm", loop=False, start_image="wtpe_xxx_a", image="wtpe_xxx_c")

image wtpe_xxx_a2d = Movie(play="images/Scene/WTPE - 1Meeting/WTPE_A2D.webm", loop=False, start_image="wtpe_xxx_a", image="wtpe_xxx_d")

image wtpe_xxx_b2a = Movie(play="images/Scene/WTPE - 1Meeting/WTPE_B2A.webm", loop=False, start_image="wtpe_xxx_b", image="wtpe_xxx_a")

image wtpe_xxx_c2c0 = Movie(play="images/Scene/WTPE - 1Meeting/WTPE_C2C0.webm", loop=True, start_image="wtpe_xxx_c", image="wtpe_xxx_c")

image wtpe_xxx_d2a = Movie(play="images/Scene/WTPE - 1Meeting/WTPE_D2A.webm", loop=False, start_image="wtpe_xxx_d", image="wtpe_xxx_a")

image wtpe_xxx_d2c = Movie(play="images/Scene/WTPE - 1Meeting/WTPE_D2C.webm", loop=False, start_image="wtpe_xxx_d", image="wtpe_xxx_c")

# ---------------------------------------------------------------------------
label wtpe_quest_0_1: # Requires PHY >= 40
# ---------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_206

    # FADE IN: The bustling PE class in the school gym. Students are scattered across the floor, stretching and chatting. wtpe, in her signature tight tracksuit top that's loose at the bottom and short enough to tease, blows her whistle sharply.
    scene bg_0
    with Dissolve(2)

    scene wtpe_1_1_bg
    show wtpe_1_1_hero_face o0
    show fx_light:
        blend "add"
    with dissolve

    wtpe "Hey{w=[wt2]}, you{w=[wt2]}, still have energy left?{w=[wt3]} I need some muscle over here.{w=[wt4]} Storage room{w=[wt2]}, now."

    show wtpe_1_1_hero_face o1
    hero "Y{w=[wt1]}-yes, miss."

    show wtpe_1_1_hero_face o0 with None

    # After a minute, the door creaks open. wtpe slips in, locking it with a casual flick. She saunters over, her ponytail bouncing, a sly smirk playing on her lips.

    scene wtpe_1_2_bg
    show wtpe_1_2_hero_body
    show wtpe_1_2_hero_face o0
    show wtpe_1_2_wtpe_body
    show fx_light:
        blend "add"
    with Fade(1, 0, 2)

    wtpe "Alright{w=[wt2]}, we'll need that thing up there for class.{w=[wt3]} You know{w=[wt2]}, the agility ladder{w=[wt2]}, or maybe the resistance bands.{w=[wt3]} It's way up high.{w=[wt2]} Can't reach it myself without a boost.{w=[wt3]} Hop to it.{w=[wt2]} Let me climb on your shoulders."

    show wtpe_1_2_hero_face o1
    hero "{aw}Ehh!?{/aw}{w=[wt2]} S{w=[wt1]}-sure."

    stop BGM fadeout 1

    scene bg_0
    with Dissolve(1)

    # hero bends down. wtpe hikes up effortlessly, her toned legs draping over his shoulders, her weight pressing down just right. She rummages above, her loose sweatshirt riding up slightly. The fabric gaps at the bottom, hinting at bare skin underneath.

    play BGM "audio/W2C - SexyVibes.mp3"

    scene wtpe_1_3_bg
    show wtpe_1_3_wtpe_face o0
    show fx_light:
        blend "add"
    with Dissolve(2)

    show wtpe_1_3_wtpe_face o1
    wtpe "Steady now.{w=[wt2]} Don't drop your teacher.{w=[wt2]} That'd be embarrassing for both of us."

    show wtpe_1_3_wtpe_face o0 with None
    # WTPE braless breasts are fully exposed—perky, swaying slightly with her movements. She keeps searching, acting oblivious, a faint nipple peek adding to the tease.

    scene wtpe_1_4_bg
    #show wtpe_1_4_mg_ladd 1
    show wtpe_1_4_mg_rope 1
    #show wtpe_1_4_mg_band 1
    show wtpe_1_4_char_bg 1
    show wtpe_1_4_char_face 1o0
    show wtpe_1_4_char_mg 1
    show wtpe_1_4_char_fg 1
    show fx_light:
        blend "add"
    with Fade(1,0,2)

    show wtpe_1_4_char_face 1o1
    wtpe "Good.{w=[wt2]} Keep like this.{w=[wt2]} I need to decide what type of exercise will be best for you guys to do today."

    show wtpe_1_4_char_face 1o0
    mind "(Ehhh!?{w=[wt2]} Am I feeling in my head what I think I'm feeling!?)"

    play SE1 "Boing1.mp3"

    hide wtpe_1_4_mg_rope
    show wtpe_1_4_char_bg 2
    show wtpe_1_4_char_face 2o0
    show wtpe_1_4_char_fg 2
    show wtpe_1_4_mg_rope 2
    hide fx_light
    show fx_light:
        blend "add"
    with dissolve

    show wtpe_1_4_char_face 2o1
    wtpe "Hey{w=[wt2]}, look up here."

    play SE1 "Bounce3.mp3"

    show wtpe_1_4_char_mg 2

    wtpe "Hey, look up here.{fast}{w=[wt2]} I'll let you decide what we'll be using for class.{w=[wt3]} What do you think?{w=[wt3]} The rope?{w=[wt2]} The agility ladder?{w=[wt2]} Or the resistance bands?"

    show wtpe_1_4_char_face 2o0 with None

    menu:
        wtpe "Hey, look up here. I'll let you decide what we'll be using for class. What do you think? The rope? The agility ladder? Or the resistance bands?{pr}[C_Mnd](Not implemented yet)[C_Off]{fast}"

        "Rope{pr}(strength test)":
            hero "Uh{w=[wt2]}, t{w=[wt1]}-the rope."

        #"Agility Ladder{pr}(agility test)":
            #hero "Uh, t-the ladder."

        #"Resistance Band{pr}(resistance test)":
            #hero "Uh, t-the band."

    show wtpe_1_4_char_face 2o1
    wtpe "Then it's decided.{w=[wt3]} Come on{w=[wt2]}, get down so I can get out."

    show wtpe_1_4_char_face 2o0 with None

    # She "finds" it finally, sliding down his body slowly, her curves brushing against him deliberately. Landing face-to-face, her eyes drop to his obvious erection straining against his shorts. She raises an eyebrow, smirking.

    scene wtpe_1_5_bg
    show wtpe_1_5_mg rope2a
    show wtpe_1_5_hero_body 1
    show wtpe_1_5_hero_face 1o0
    show wtpe_1_5_wtpe_body 2a
    show fx_light:
        blend "add"
    with fade

    pause

    play SE1 "Bounce3.mp3"

    scene wtpe_1_5_bg
    show wtpe_1_5_hero_body 1
    show wtpe_1_5_hero_face 1o0
    show wtpe_1_5_wtpe_body 2b
    show wtpe_1_5_mg rope2b
    show fx_light:
        blend "add"
    with dissolve

    scene wtpe_1_5_bg
    show wtpe_1_5_wtpe_body 1b
    show wtpe_1_5_wtpe_face 1o0
    show wtpe_1_5_mg rope1
    show wtpe_1_5_hero_body 1
    show wtpe_1_5_hero_face 1o0
    show fx_light:
        blend "add"
    with dissolve
    
    pause

    show wtpe_1_5_wtpe_face 1o1
    wtpe "What are you waiting?{w=[wt2]} Stand up and let's go back!"

    show wtpe_1_5_wtpe_body 1b
    show wtpe_1_5_wtpe_face 1o0
    show wtpe_1_5_mg rope1
    show wtpe_1_5_hero_body 2
    show wtpe_1_5_hero_face 2o0
    show fx_light:
        blend "add"
    with dissolve

    show wtpe_1_5_hero_face 2o1
    hero "Y{w=[wt1]}-yes, miss."

    show wtpe_1_5_hero_face 2o0
    show wtpe_1_5_wtpe_face 1o1
    wtpe "Whoa there, champ!{w=[wt2]} Can't let you march back out like that.{w=[wt2]} The class'll think I did something naughty to make you like this!{w=[wt4]} Hmph!{w=[wt2]} Guess I'll have to fix this little problem.{w=[wt2]} Consider it extra credit."

    show wtpe_1_5_wtpe_face 1o0 with None

    stop BGM fadeout 2

    scene bg_0
    with Dissolve(2)

    play BGM "audio/W2C - Lust.mp3"

    # WTPE is giving HERO a blowjob
    scene wtpe_xxx_a
    show wtpe_xxx_a2a0
    with Dissolve(3)

    pause

    scene wtpe_xxx_a
    show wtpe_xxx_a2a1
    wtpe "Listen{w=[wt2]}, I'll help you with that{w=[wt2]}, but try to don't make much noises and to finish it fast!{w=[wt2]} People can't see us here, or they'll think we're doing something wrong.{w=[wt3]} We need to hurry!{nw}"

    scene wtpe_xxx_a
    show wtpe_xxx_a2a0
    wtpe "Listen{w=[wt2]}, I'll help you with that{w=[wt2]}, but try to don't make much noises and to finish it fast!{w=[wt2]} People can't see us here, or they'll think we're doing something wrong.{w=[wt3]} We need to hurry!{fast}"

    scene wtpe_xxx_a2b

    $ renpy.pause(2, hard=True)

    scene wtpe_xxx_b
    show wtpe_xxx_b2b

    pause

    scene wtpe_xxx_b2a

    $ renpy.pause(4, hard=True)

    #if stat_phy >= 50: # HERO resists
    scene wtpe_xxx_a
    show wtpe_xxx_a2a1
    wtpe "What are you doing?{w=[wt3]} Hurry up!{w=[wt2]} We need to go back!{w=[wt4]} Hmph!{w=[wt2]} Let's try another way.{w=[wt2]} You better hurry up and release it this time.{nw}"

    scene wtpe_xxx_a
    show wtpe_xxx_a2a0
    wtpe "What are you doing?{w=[wt3]} Hurry up!{w=[wt2]} We need to go back!{w=[wt4]} Hmph!{w=[wt2]} Let's try another way.{w=[wt2]} You better hurry up and release it this time.{fast}"

    stop BGM fadeout 3

    # WTPE is giving HERO a titjob

    scene wtpe_xxx_a2d

    $ renpy.pause(3, hard=True)

    play BGM "audio/W2C - Intensity.mp3"

    scene wtpe_xxx_d
    show wtpe_xxx_d2d

    $ a_event_0 = "d"

    while a_event_0 != "c":
        pause
        menu:
            "Keep":
                pass

            "Blowjob" if a_event_0 != "b":
                $ a_event_0 = "b"
                scene wtpe_xxx_d2a

                $ renpy.pause(2, hard=True)

                scene wtpe_xxx_a2b

                $ renpy.pause(2, hard=True)

                scene wtpe_xxx_b
                show wtpe_xxx_b2b

            "Titjob" if a_event_0 != "d":
                $ a_event_0 = "d"
                scene wtpe_xxx_b2a

                $ renpy.pause(2, hard=True)

                scene wtpe_xxx_a2d

                $ renpy.pause(3, hard=True)

                scene wtpe_xxx_d
                show wtpe_xxx_d2d

            "Cum":
                if a_event_0 == "b":
                    scene wtpe_xxx_b2a

                    $ renpy.pause(2, hard=True)

                    scene wtpe_xxx_a2c

                    $ renpy.pause(3, hard=True)

                elif a_event_0 == "d":
                    scene wtpe_xxx_d2c

                    $ renpy.pause(4, hard=True)

                $ a_event_0 = "c"
                $ hero_xnum += 1
                $ msg.msg(renpy.translate_string("You came."))
                $ xp_now += 10
                $ msg.msg(renpy.translate_string("XP [C_Pos]+ 10[C_Off]."))

                scene wtpe_xxx_c2c0

    pause

    scene wtpe_xxx_c2c1
    wtpe "Damn...{w=[wt3]} My hair will get all sticky.{w=[wt4]} Whatever.{w=[wt2]} Let's clean up fast and go!{nw}"
    
    scene wtpe_xxx_c2c0
    wtpe "Damn...{w=[wt3]} My hair will get all sticky.{w=[wt4]} Whatever.{w=[wt2]} Let's clean up fast and go!{fast}"

    stop BGM fadeout 3

    scene bg_0
    with Dissolve(3)

    play BGM "audio/W2C - Satisfaction.mp3"

    scene wtpe_1_5_bg
    show wtpe_1_5_hero_body 3
    show wtpe_1_5_wtpe_body 1a
    show wtpe_1_5_wtpe_face 1o0
    show wtpe_1_5_mg rope1
    show fx_light:
        blend "add"
    with Dissolve(3)

    show wtpe_1_5_wtpe_face 1o1
    wtpe "Good job, kid.{w=[wt2]} Get some rest but don't be late for class."

    show wtpe_1_5_wtpe_face 1o0 with None

#---------------------------------------------------------------------------
    scene bg_0
    with Dissolve(2)

    $ check_stat()
    $ a_event_0 = 5 / (1 + (0.09 * stat_phy))
    $ add_stat("hero", "phy", a_event_0, stat_mod=False)

    $ wtpe_quest_1 = 1

    call gametime_schoolnext from _call_gametime_schoolnext_13
    $ gametimemin += _return
    call gametime from _call_gametime_129

    pause

    play BGM "audio/W2C - Tranquility.mp3"
    
    call check_playermap from _call_check_playermap_47
    jump show_ui
#---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Idea 4 — locker-access hook #4 ("grab my..." favor)
# Reached from the action_quest star menu while HERO is at the sports court during a class period.
# WTPE trusts HERO over the other students, so she sends him to fetch the equipment bag she left in the locker room. Accepting sets hero_locker_f_access, which reveals the Female Locker nav button; entering the locker fires the generic room_entry_exposure (GameCheck.rpy goto_school_locker_f) if a girl is changing/showering there per 2.2g. Text-only for now (locker CG to be added later).
# ---------------------------------------------------------------------------
label wtpe_locker_favor:
    $ hero_locker_favor_day = gametimeday

    scene bg_school sportcourt
    with Dissolve(1)

    wtpe "Oh, perfect timing!{w=[wt2]} You there{w=[wt1]}, yeah{w=[wt1]}, the dependable one."
    wtpe "I left my equipment bag in the locker room{w=[wt1]}, it was closer than the storage room, so I just tossed it in there."
    wtpe "Be a dear and grab it for me?{w=[wt3]} I'd trust you with it over half the students here."

    menu:
        wtpe "Be a dear and grab it for me?{fast}"

        "Agree to fetch the bag":
            $ hero_locker_f_access = True
            hero "Sure{w=[wt1]}, I'll go get it."
            $ msg.msg(renpy.translate_string("The {b}Female Locker Room{/b} is now reachable from the courtyard, pool, and sport court. Go grab the teacher's bag."))

        "Make an excuse":
            hero "Ah{w=[wt1]}, maybe ask someone else this time?"
            wtpe "Hmph.{w=[wt2]} Suit yourself, then."

    jump show_ui
#---------------------------------------------------------------------------
