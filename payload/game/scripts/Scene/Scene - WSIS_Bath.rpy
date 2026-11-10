# --------------------------------------------------
# Animation Video
# --------------------------------------------------
image wsis_bath4_mov_1 = Movie(play="/images/Scene/WSIS - Bath/wsis_bath4_mov_1.webm", loop=True, start_image="wsis_bath4_mov_1a", image="wsis_bath4_mov_1a")
image bath_clean_massage_1 =  Movie(play="/images/Scene/WSIS - Bath/bath_clean_massage_1.webm", loop=True, start_image="bath_clean_massage_1a", image="bath_clean_massage_1a")
image bath_clean_massage_2 =  Movie(play="/images/Scene/WSIS - Bath/bath_clean_massage_2.webm", loop=True, start_image="bath_clean_massage_2a", image="bath_clean_massage_2a")

# --------------------------------------------------
screen wsis_bath_control():
# --------------------------------------------------
    on "show"    action SetVariable("ch_mouse_ctl", True)
    on "replace" action SetVariable("ch_mouse_ctl", True)
    on "hide"    action SetVariable("ch_mouse_ctl", False)

    timer 0.05 repeat True action NullAction()

    $ _f = MOCHA_FORTH.peek()
    $ _d = MOCHA_DOWN.peek()

    textbutton renpy.translate_string("Done") align (0.5, 1.0) action [
        SetVariable("ch_move_forth", MOCHA_FORTH.peek()),
        SetVariable("ch_move_down", MOCHA_DOWN.peek()),
        Hide("wsis_bath_control"), Return()]
        
# ---------------------------------------------------------------------------
label wsis_bath_1: # Bathroom Scene
# ---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_197

    scene bg_0
    with Dissolve(2)

    play BGM "audio/W2C - Awkward.mp3"

    scene wsis_bath2_bg
    show wsis_bath2_hero_body 1
    show wsis_bath2_hero_wear 1_dressy
    show wsis_bath2_wsis_body 1
    show wsis_bath2_wsis_face 1o0
    show wsis_bath2_wsis_wear 1_dressy
    show fx_light
    with Dissolve(3)

    if wsis_quest_10 == 0:
        show wsis_bath2_wsis_face 1o1
        wsis "I can't believe{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Why didn't you say anything, you pervert!?"

        show wsis_bath2_wsis_face 1o0
        hero "{aw}What should I do!?{/aw}"

        show wsis_bath2_wsis_face 1o1
        wsis "Pervert!{w=[wt1]} I'll just do it cause if you get sick, [C_Nam]Mom[C_Off] will be a pain in the neck...!"

        show wsis_bath2_wsis_face 1o0
        hero "Well{w=[wt2]}, actually{w=[wt2]}, I kinda never get sick, I guess.{w=[wt3]} I{w=[wt1]}-I'll just wait you out, okay?{w=[wt3]} Don't take too long!"

        show wsis_bath2_wsis_face 1o1
        wsis "You'll stay here!"

        show wsis_bath2_wsis_face 1o0
        hero "{aw}Ehhh...!?{/aw}"

        show wsis_bath2_wsis_face 1o1
        wsis "D{w=[wt1]}-don't go getting any crazy ideas!{w=[wt2]} I just don't want to lose my computer and internet access because my mom thinks I kicked you out and convinced you to deny it, got it?{w=[wt3]} T{w=[wt1]}-that's all!"

        show wsis_bath2_wsis_face 1o0
        hero "{aw}S{w=[wt1]}-sure...!{/aw}"

        show wsis_bath2_wsis_face 1o1
        wsis "S{w=[wt1]}-so{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} H{w=[wt1]}-hurry up and l{w=[wt1]}-let's finish it soon!"

        show wsis_bath2_wsis_face 1o0
        hero "{aw}O{w=[wt1]}-okay.{/aw}"

        scene wsis_bath2_bg
        show wsis_bath2_wsis_wear 2_dressy
        #show wsis_bath2_hero_wear 2_dressy
        show wsis_bath2_wsis_body 2
        show wsis_bath2_wsis_eye 2f
        show wsis_bath2_wsis_face 2s0
        show wsis_bath2_hero_body 2
        show wsis_bath2_hero_eye 2f
        show wsis_bath2_hero_face 2s0
        show fx_light
        with fade

        show wsis_bath2_wsis_face 2s1
        show wsis_bath2_hero_face 2s0
        wsis "{aw}Don't dare to say one word!!!{/aw}"

        show wsis_bath2_wsis_face 2s0
        show wsis_bath2_hero_face 2s1
        hero "{aw}I'm not even saying anything!{w=[wt2]} What do you want me to do!?{/aw}" id wsis_bath_1_388cd234_1

        show wsis_bath2_wsis_face 2s1
        show wsis_bath2_hero_face 2s0
        wsis "{aw}J{w=[wt1]}-just d{w=[wt1]}-don't stare at me{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} t{w=[wt1]}-to much!{/aw}"

        show wsis_bath2_wsis_face 2s0
        show wsis_bath2_hero_face 2s1
        hero "Fine then.{w=[wt2]} Just short peeks here and there.{w=[wt3]} Got it."

        show wsis_bath2_wsis_face 2s1
        show wsis_bath2_hero_face 2s0
        wsis "{aw}Ehh!?{/aw}{w=[wt4]}{nw}"

        show wsis_bath2_wsis_face 2s0
        show wsis_bath2_hero_eye 2d
        wsis "{aw}Ehh!?{/aw}{fast}{w=[wt4]}{nw}"

        show wsis_bath2_wsis_face 2s1
        wsis "{aw}Ehh!?{/aw}{fast} Y{w=[wt1]}-you're{nw}"

        show wsis_bath2_hero_eye 2f
        wsis "{aw}Ehh!?{/aw} Y-you're{fast} staring at my body!{w=[wt4]}{nw}"

        show wsis_bath2_hero_face 2s0
        show wsis_bath2_wsis_face 2s0
        show wsis_bath2_wsis_eye 2d
        wsis "{aw}Ehh!?{/aw} Y-you're staring at my body!{fast}"

        pause(0.5)

        show wsis_bath2_hero_face 2s1
        show wsis_bath2_wsis_eye 2f
        hero "What are you{nw}"

        show wsis_bath2_wsis_eye 2f
        hero "What are you{fast} complaining!?{w=[wt3]} You're doing the same!"

        show wsis_bath2_wsis_face 2s1
        show wsis_bath2_hero_face 2s0
        wsis "I'm not!"

        show wsis_bath2_wsis_face 2s0
        show wsis_bath2_hero_face 2s1
        hero "You are!"

        show wsis_bath2_wsis_face 2s1
        show wsis_bath2_hero_face 2s0
        wsis "I'm just doing because you did before!"

        show wsis_bath2_wsis_face 2s0
        show wsis_bath2_hero_face 2s1
        hero "So that means you did!{nw}"

        show wsis_bath2_hero_eye 2d
        hero "So that means you did!{fast}{w=[wt4]} What means you lost your right to not allow me to look!"

        show wsis_bath2_wsis_face 2s1
        show wsis_bath2_wsis_eye 2d
        show wsis_bath2_hero_face 2s0
        wsis "Stop!"

        show wsis_bath2_wsis_face 2s0
        with None

        play SE1 "Boing1.mp3"
        show wsis_bath2_hero_body 3 with dissolve

        pause

        show wsis_bath2_wsis_face 2s1
        wsis "{aw}What's that, you pervert!?{w=[wt3]} Did you just get a hard on!?{/aw}"

        show wsis_bath2_hero_face 2s1
        show wsis_bath2_wsis_face 2s0
        hero "{aw}It's not my fault!{/aw}" id wsis_bath_1_934d5c85_1

        show wsis_bath2_hero_face 2s0
        show wsis_bath2_wsis_face 2s1
        wsis "{aw}You won't aim me with this bazooka!{w=[wt2]} Turn around and get in into the shower!{/aw}"


        show wsis_bath2_hero_face 2s1
        show wsis_bath2_wsis_face 2s0
        hero "O{w=[wt1]}-okay..."

        show wsis_bath2_hero_face 2s0
        show wsis_bath2_wsis_face 2s0
        with None

        # ---------------------------------------------------------------------------
        scene wsis_bath3_bg
        show fx_light
        with Dissolve(1) # WSIS applies soap on HERO
        # ---------------------------------------------------------------------------

        show wsis_bath3_hero_body 1
        show wsis_bath3_hero_face 1o0
        hide fx_light
        show fx_light
        with dissolve
        
        show wsis_bath3_wsis_body 1
        show wsis_bath3_wsis_face 1o0
        hide fx_light
        show fx_light
        with dissolve

        # Turn shower on

        show wsis_bath3_wsis_face 1o1
        wsis "Hurry up!{w=[wt2]} Turn on the shower!{w=[wt3]} I'll help you to wash your back!"

        stop BGM fadeout 5

        show wsis_bath3_wsis_face 1o0
        show wsis_bath3_hero_face 1o1
        hero "{aw}Ehhh...!?{/aw}"

        show wsis_bath3_wsis_face 1o1
        show wsis_bath3_hero_face 1o0
        wsis "“Ehhh” what!?{w=[wt2]} Of course it's to help you to finish it soon!{w=[wt3]} J{w=[wt1]}-just that...!"

        show wsis_bath3_wsis_face 1o0


        menu:
            "Dynamic animation":
                #$ MoChaQuality("affine")

                play BGM "audio/W2C - SexyVibes.mp3"

                # wsis's arms are deliberately left alone: massage_1/2 keyframe them, and in idle they rest at the value the rig authors. Pinning them to 0.0 here is what made them thin.
                $ ch_stretch_arm_f = 0.0
                $ ch_stretch_arm_b = 0.0
                $ ch_move_forth    = 0.0
                $ ch_move_down     = 0.0

                scene wsis_bath3_bg
                #show bath_clean massage_1 at SXY2(1, 0, -200)
                show expression mocha("bath_clean", "massage_1", move_forth=0, move_down=0) as bath_clean at SXY2(1, 0, -200)
                show action_bathing_fg at SXY2(1, -400, 0)
                show fx_light
                with Dissolve(1)

                pause

            "Simple animation (for weaker devices)":
                scene bath_clean_massage_1
                show action_bathing_fg at SXY2(1, -400, 0)
                show fx_light
                with Dissolve(1)
                pause

        wsis "So{w=[wt2]}, it's okay like this?"

        hero "Y{w=[wt1]}-yes..."

        pause

        wsis "N{w=[wt1]}-now it's my time.{w=[wt3]} Y{w=[wt1]}-you apply soap on my back."

        hero "O{w=[wt1]}-okay..."

        menu:
            "Dynamic animation":

                scene wsis_bath3_bg
                show expression mocha("bath_clean", "massage_2", move_forth=MoChaMouse("x", invert=True, smooth=0.15), move_down=MoChaMouse("y", smooth=0.15)) as bath_clean at SXY2(1, 0, -200)
                show action_bathing_fg at SXY2(1, -400, 0)
                show fx_light                

                $ ch_mouse_ctl = False

                call screen minigame_coverage(
                    var_cps = 25.0,
                    var_ttl = "Cleaning",
                    var_txt = "Move the cursor to clean " +str(C_Nam) + str(fnamewsis) + str(C_Off) + " until she's completelly clean.",
                    var_tim = None,
                    var_names = ["Breasts", "Shoulders", "Belly", "Back", "Groin", "Butt"],
                    var_pos = (0.025, 0.025),
                    var_var = "ch_mouse_ctl",
                    )

                stop BGM fadeout 10

                #$ a_event_0 = _return
                #$ ch_mouse_ctl = False
                #$ ch_move_forth    = 1.0
                #$ ch_move_down     = 0.0

                show bath_clean massage_2 with Dissolve(2)

            "Simple animation (for weaker devices)":
                scene bath_clean_massage_2
                show action_bathing_fg at SXY2(1, -400, 0)
                show fx_light
                with Dissolve(1)
                pause

        scene bg_0 with Dissolve(2)

        pause

        wsis "[C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} I can't hold anymore..."

        pause(0.25)

        play BGM "audio/W2C - Intensity.mp3"

        pause(0.25)

        scene wsis_bath4_mov_1 at SXY2(1.02, 2, 0) with Dissolve(5)

        pause

        scene bg_0 with Dissolve(3)

        play SE2 renpy.random.choice(["Moan/A lvl7 (1).mp3"])

        pause(3)

        play SE2 renpy.random.choice(["Moan/A lvl7 (2).mp3"])

        pause(3)

        play SE2 renpy.random.choice(["Moan/A lvl7 (3).mp3"])

        pause(3)

        $ wsis_lust = 0
        $ msg.msg(renpy.translate_string("{nm}[fnamewsis]{/nm} came, and her lust reset."))
        $ xp_now += 25
        $ msg.msg(renpy.translate_string("XP [C_Pos]+ 25[C_Off]."))
        $ wsis_quest_10 = 1

        pause(2)

        jump wsis_bath_1_end

        # ---------------------------------------------------------------------------
        scene wsis_bath_1_bg 4
        # ---------------------------------------------------------------------------

        wsis "Wait... [C_Nam][wsis_to_hero][C_Off]... That's wrong... We can't..."

        hero "I can't control anymore..."

        wsis "No...! Stop...!"

        hero "Sorry, I've lost my mind..."

        wsis "I'm not ready..."

        hero "Don't worry. I won't do anything you don't want. And... If you want it. Just... Keep the time you need."

        wsis "Thank you, [C_Nam][wsis_to_hero][C_Off]."

        # ---------------------------------------------------------------------------
        scene wsis_bath_1_bg 4 # Preview
        # ---------------------------------------------------------------------------

        wsis "Can you... use your hands?"

        hero "S-sure...!"

        # ---------------------------------------------------------------------------
        scene wsis_bath_1_bg 4 # Animation 1
        # ---------------------------------------------------------------------------

        pause

        wsis "Now let me help you with that."

        # ---------------------------------------------------------------------------
        scene wsis_bath_1_bg 4 # Animation 2
        # ---------------------------------------------------------------------------

        pause

# ---------------------------------------------------------------------------
label wsis_bath_1_end: # Bathroom Scene End
# ---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_198

    $ wsis_wear = None
    $ hero_wear = None

    $ wsis_fx = 1
    $ hero_fx = 1
    $ wsis_mood = "O2"
    $ hero_mood = "A1"

    scene bg_home_bathroom
    show HERO at PoseX_X(850, 0.0)
    show WSIS at PoseX_X(1050, 0.0)
    with Dissolve(2)

    wsis "We'll {b}never{/b} tell [C_Nam]Mom[C_Off] about today, understood?"

    hero "Understood!"

    wsis "{aw}Not one word!!!{/aw}"

    hero "Not one word!"

    if perk_cha_sex >= 1:
       $ add_stat("wsis", "lust", 2)

    $ add_stat("wsis", "inti", 2)
    $ add_stat("wsis", "love", 2)
    $ add_stat("hero", "cha_sex", 2)

    $ a_event_0 = renpy.random.random()
    if a_event_0 <= 0.33:
        scene bg_2 pink
    elif a_event_0 <= 0.66:
        scene bg_2 yellow
    else:
        scene bg_2 flowers

    scene bg_1
    show action_wsis_kiss_body
    show action_wsis_kiss_hero_face u0
    show action_wsis_kiss_wsis_face u0
    show action_wsis_kiss_wsis_fg
    with Fade(1, 0, 2, color="#FFF")

    pause

    if wsis_love >= 60:
        wsis "I love you, [C_Nam][wsis_to_hero][C_Off]"

    pause

# ---------------------------------------------------------------------------
    if gametimehour < 20:
        $ StartAct("wsis", (("changing", "home"), 0), True)
    else:
        $ StartAct("wsis", (("changing", "sleep"), 0), True)

    jump show_ui
# ---------------------------------------------------------------------------
