# ----------------------------------------------------------------------------------------------------
# CHECK REAL TIME SECONDS
# ----------------------------------------------------------------------------------------------------
label gametimesec:
    $ gametimesec = tempo.time()
    $ renpy.pause(1, hard=True)
    $ gametimesec = 1 * (tempo.time() - gametimesec)
    return

# ----------------------------------------------------------------------------------------------------
# PLAY: 1 ARROW
# ----------------------------------------------------------------------------------------------------
screen minigametimer1():
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 2), false=[Hide('minigametimer1'), Return(False)])
    bar value time range timerrange xalign 0.5 yalign 0.1 xmaximum 980 at alpha_dissolve

    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        if setarrow == 2:
            key "K_DOWN"    action [Hide('minigametimer1'), Return(True)]
            key "K_LEFT"    action [Hide('minigametimer1'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer1'), Return(False)]
            key "K_UP"      action [Hide('minigametimer1'), Return(False)]
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_2 IDLE.webp" at ClickNone
        elif setarrow == 4:
            key "K_DOWN"    action [Hide('minigametimer1'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer1'), Return(True)]
            key "K_RIGHT"   action [Hide('minigametimer1'), Return(False)]
            key "K_UP"      action [Hide('minigametimer1'), Return(False)]
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_4 IDLE.webp" at ClickNone
        elif setarrow == 6:
            key "K_DOWN"    action [Hide('minigametimer1'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer1'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer1'), Return(True)]
            key "K_UP"      action [Hide('minigametimer1'), Return(False)]
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_6 IDLE.webp" at ClickNone
        elif setarrow == 8:
            key "K_DOWN"    action [Hide('minigametimer1'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer1'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer1'), Return(False)]
            key "K_UP"      action [Hide('minigametimer1'), Return(True)]
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_8 IDLE.webp" at ClickNone

    if renpy.variant("mobile") and not (renpy.variant("pc") or renpy.variant("web")):
        if setarrow <= 4:
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_4 IDLE.webp" at ClickNone
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [Hide('minigametimer1'), Return(True)]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [Hide('minigametimer1'), Return(False)]
        elif setarrow >= 6:
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_6 IDLE.webp" at ClickNone
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [Hide('minigametimer1'), Return(False)]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [Hide('minigametimer1'), Return(True)]

init python:
    def _sequence_new_arrows(n):
        return [renpy.random.choice([2, 4, 6, 8]) for _ in range(max(1, n))]

# ----------------------------------------------------------------------------------------------------
# PLAY: DYNAMIC ARROWS
# ----------------------------------------------------------------------------------------------------
screen minigame_sequence(time_pass=1, var_tim=15, count_arrow=4, var_txt=None, var_mod="classic", var_sco=0, var_sca=0.0):
    # Initialize variables on screen entry
    default time = var_tim
    default timerrange = var_tim
    default score = (var_sco if var_mod == "continuous" else 0)
    default setarrow = _sequence_new_arrows(count_arrow + (var_sco if var_mod == "continuous" else 0))
    default minigamestep = 0
    default game_started = False

    # --------------------------------------------------
    # Preparation Screen
    # --------------------------------------------------
    if not game_started:
        frame:
            background "#000000C8"
            xysize (1920,1080)
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                label renpy.translate_string("{size=+80}{b}Sequence{/b}{/size}") xalign 0.5
                vbox:
                    xalign 0.5
                    xysize (960, 400)
                    if var_txt == None:
                        if var_mod == "continuous":
                            if renpy.variant("mobile") and not (renpy.variant("pc") or renpy.variant("web")):
                                text renpy.translate_string("{size=+10}Tap the arrow buttons (⬅➡) in the correct sequence to score. Each new stage adds one more arrow. Keep going before time runs out!{/size}") xalign 0.5
                            else:
                                text renpy.translate_string("{size=+10}Press the arrow keys (⬅➡⬆⬇) in the correct sequence to score. Each new stage adds one more arrow. Keep going before time runs out!{/size}") xalign 0.5
                        else:
                            if renpy.variant("mobile") and not (renpy.variant("pc") or renpy.variant("web")):
                                text renpy.translate_string("Click the arrow keys (⬅➡) on the side of your screen correctly according to the arrows in the respective order that appear on the screen.") xalign 0.5
                            else:
                                text renpy.translate_string("Click the arrow keys (⬅➡⬆⬇) on your keyboard correctly according to the arrows in the respective order that appear on the screen.") xalign 0.5
                    else:
                        text renpy.translate_string("{size=+10}[var_txt]{/size}") xalign 0.5
                text renpy.translate_string("[C_Dat]{size=+40}{b}Click to start!{/b}[C_Off]") xalign 0.5

        key "mousedown_1" action SetScreenVariable("game_started", True)

    # --------------------------------------------------
    # Game Started
    # --------------------------------------------------
    else:
        timer 0.1 repeat True action If(time > 0,
            true=SetScreenVariable('time', time - time_pass),
            false=(Return(score) if var_mod == "continuous" else Return("Lose"))
        )
        bar value time range timerrange xalign 0.5 yalign 0.1 xmaximum 980 at alpha_dissolve

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            hbox:
                xalign 0.5
                yalign 0.15
                spacing 0.25
                for i in range(len(setarrow)):
                    if i < minigamestep:
                        image "images/UI/Arrow_" + str(setarrow[i]) + " IDLE.webp" at ClickCorrect
                    else:
                        image "images/UI/Arrow_" + str(setarrow[i]) + " IDLE.webp" at ClickNone

            # Dynamic key handling for each step
            for step in range(len(setarrow)):
                if minigamestep == step:
                    $ correct_advance = [SetScreenVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
                    $ correct_final = ([
                        SetScreenVariable("score", score + 0.5),
                        SetScreenVariable("minigamestep", 0),
                        SetScreenVariable("setarrow", _sequence_new_arrows(count_arrow + round(score*2) + 1)),
                        Play("SE1", "BeepRight.ogg"),
                    ] if var_mod == "continuous" else Return("Win"))
                    $ wrong_action = ([SetScreenVariable("minigamestep", 0), Play("SE1", "BeepWrong.ogg")] if var_mod == "continuous" else Return("Lose"))

                    if setarrow[step] == 2:
                        key "K_DOWN" action If(step < len(setarrow) - 1, correct_advance, correct_final)
                        key "K_LEFT" action wrong_action
                        key "K_RIGHT" action wrong_action
                        key "K_UP" action wrong_action
                    elif setarrow[step] == 4:
                        key "K_DOWN" action wrong_action
                        key "K_LEFT" action If(step < len(setarrow) - 1, correct_advance, correct_final)
                        key "K_RIGHT" action wrong_action
                        key "K_UP" action wrong_action
                    elif setarrow[step] == 6:
                        key "K_DOWN" action wrong_action
                        key "K_LEFT" action wrong_action
                        key "K_RIGHT" action If(step < len(setarrow) - 1, correct_advance, correct_final)
                        key "K_UP" action wrong_action
                    elif setarrow[step] == 8:
                        key "K_DOWN" action wrong_action
                        key "K_LEFT" action wrong_action
                        key "K_RIGHT" action wrong_action
                        key "K_UP" action If(step < len(setarrow) - 1, correct_advance, correct_final)

        if renpy.variant("mobile") and not (renpy.variant("pc") or renpy.variant("web")):
            # Simplify arrows for mobile (only left/right)
            python:
                for i in range(len(setarrow)):
                    if setarrow[i] <= 4:
                        setarrow[i] = 4
                    elif setarrow[i] >= 6:
                        setarrow[i] = 6

            hbox:
                xalign 0.5
                yalign 0.15
                spacing 0.25
                for i in range(len(setarrow)):
                    if i < minigamestep:
                        image "images/UI/Arrow_" + str(setarrow[i]) + " IDLE.webp" at ClickCorrect
                    else:
                        image "images/UI/Arrow_" + str(setarrow[i]) + " IDLE.webp" at ClickNone

            # Dynamic button handling for each step
            for step in range(len(setarrow)):
                if minigamestep == step:
                    $ correct_advance = [SetScreenVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
                    $ correct_final = ([
                        SetScreenVariable("score", score + 0.5),
                        SetScreenVariable("minigamestep", 0),
                        SetScreenVariable("setarrow", _sequence_new_arrows(count_arrow + round(score*2) + 1)),
                        Play("SE1", "BeepRight.ogg"),
                    ] if var_mod == "continuous" else Return("Win"))
                    $ wrong_action = ([SetScreenVariable("minigamestep", 0), Play("SE1", "BeepWrong.ogg")] if var_mod == "continuous" else Return("Lose"))

                    if setarrow[step] <= 4:
                        imagebutton:
                            xalign 0.0
                            yalign 0.6
                            idle "images/UI/Arrow_L IDLE.webp"
                            hover "images/UI/Arrow_L HOVER.webp"
                            action If(step < len(setarrow) - 1, correct_advance, correct_final)
                        imagebutton:
                            xalign 1.0
                            yalign 0.5
                            idle "images/UI/Arrow_R IDLE.webp"
                            hover "images/UI/Arrow_R HOVER.webp"
                            action wrong_action
                    elif setarrow[step] >= 6:
                        imagebutton:
                            xalign 0.0
                            yalign 0.6
                            idle "images/UI/Arrow_L IDLE.webp"
                            hover "images/UI/Arrow_L HOVER.webp"
                            action wrong_action
                        imagebutton:
                            xalign 1.0
                            yalign 0.5
                            idle "images/UI/Arrow_R IDLE.webp"
                            hover "images/UI/Arrow_R HOVER.webp"
                            action If(step < len(setarrow) - 1, correct_advance, correct_final)

        # Score display (continuous)
        if var_mod == "continuous":
            text renpy.translate_string("{size=+20}{b}Score: [score]{/b}{/size}") xalign 0.5 yalign 0.25

    modal True

# ----------------------------------------------------------------------------------------------------
# PLAY: 4 ARROWS
# ----------------------------------------------------------------------------------------------------
screen minigametimer4(time_pass):
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - time_pass), false=[Hide('minigametimer4'), Return(False)])
    bar value time range timerrange xalign 0.5 yalign 0.1 xmaximum 980 at alpha_dissolve

    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        hbox:
            xalign 0.5
            yalign 0.15
            spacing 0.25
            image "images/UI/Arrow_" + str(setarrow[0]) + " IDLE.webp" at ClickNone
            image "images/UI/Arrow_" + str(setarrow[1]) + " IDLE.webp" at ClickNone
            image "images/UI/Arrow_" + str(setarrow[2]) + " IDLE.webp" at ClickNone
            image "images/UI/Arrow_" + str(setarrow[3]) + " IDLE.webp" at ClickNone

        #STEP 1
        if setarrow[0] == 2 and minigamestep == 0:
            key "K_DOWN"    action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[0] == 4 and minigamestep == 0:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[0] == 6 and minigamestep == 0:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[0] == 8 and minigamestep == 0:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]

        #STEP 2
        if setarrow[1] == 2 and minigamestep == 1:
            key "K_DOWN"    action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[1] == 4 and minigamestep == 1:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[1] == 6 and minigamestep == 1:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[1] == 8 and minigamestep == 1:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]

        #STEP 3
        if setarrow[2] == 2 and minigamestep == 2:
            key "K_DOWN"    action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[2] == 4 and minigamestep == 2:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[2] == 6 and minigamestep == 2:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[2] == 8 and minigamestep == 2:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]

        #STEP 4
        if setarrow[3] == 2 and minigamestep == 3:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(True)]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[3] == 4 and minigamestep == 3:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(True)]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[3] == 6 and minigamestep == 3:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(True)]
            key "K_UP"      action [Hide('minigametimer4'), Return(False)]
        elif setarrow[3] == 8 and minigamestep == 3:
            key "K_DOWN"    action [Hide('minigametimer4'), Return(False)]
            key "K_LEFT"    action [Hide('minigametimer4'), Return(False)]
            key "K_RIGHT"   action [Hide('minigametimer4'), Return(False)]
            key "K_UP"      action [Hide('minigametimer4'), Return(True)]

    if renpy.variant("mobile") and not (renpy.variant("pc") or renpy.variant("web")):
        if setarrow[0] <= 4:
            $setarrow[0] = 4
        elif setarrow[0] >= 6:
            $setarrow[0] = 6

        if setarrow[1] <= 4:
            $setarrow[1] = 4
        elif setarrow[1] >= 6:
            $setarrow[1] = 6

        if setarrow[2] <= 4:
            $setarrow[2] = 4
        elif setarrow[2] >= 6:
            $setarrow[2] = 6

        if setarrow[3] <= 4:
            $setarrow[3] = 4
        elif setarrow[3] >= 6:
            $setarrow[3] = 6

        hbox:
            xalign 0.5
            yalign 0.15
            spacing 0.25
            image "images/UI/Arrow_" + str(setarrow[0]) + " IDLE.webp" at ClickNone
            image "images/UI/Arrow_" + str(setarrow[1]) + " IDLE.webp" at ClickNone
            image "images/UI/Arrow_" + str(setarrow[2]) + " IDLE.webp" at ClickNone
            image "images/UI/Arrow_" + str(setarrow[3]) + " IDLE.webp" at ClickNone

        if setarrow[0] <= 4 and minigamestep == 0:
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [Hide('minigametimer4'), Return(False)]
        elif setarrow[0] >= 6 and minigamestep == 0:
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [Hide('minigametimer4'), Return(False)]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
        if setarrow[1] <= 4 and minigamestep == 1:
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [Hide('minigametimer4'), Return(False)]
        elif setarrow[1] >= 6 and minigamestep == 1:
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [Hide('minigametimer4'), Return(False)]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
        if setarrow[2] <= 4 and minigamestep == 2:
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [Hide('minigametimer4'), Return(False)]
        elif setarrow[2] >= 6 and minigamestep == 2:
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [Hide('minigametimer4'), Return(False)]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [SetVariable("minigamestep", minigamestep+1), Play("SE1", "BeepRight.ogg")]

        if setarrow[3] <= 4 and minigamestep == 3:
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [Hide('minigametimer4'), Return(True)]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [Hide('minigametimer4'), Return(False)]
        elif setarrow[3] >= 6 and minigamestep == 3:
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [Hide('minigametimer4'), Return(False)]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [Hide('minigametimer4'), Return(True)]

# ----------------------------------------------------------------------------------------------------
# PLAY: CLICK CRAZY
# ----------------------------------------------------------------------------------------------------
screen minigametimercrazy():
    timer 1 repeat True action If(time > 0, true=[SetVariable('time', time - minigame_cpu), SetVariable('setarrow', renpy.random.choice([2,4,6,8]))], false=[Hide('minigametimercrazy'), Return(False)])
    bar value time range timerrange xalign 0.5 yalign 0.1 xmaximum 980 at alpha_dissolve

    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        if setarrow == 2:
            key "K_DOWN"    action If(time < timerrange, true=[SetVariable('time', time + 20), Play("SE1", "BeepRight.ogg")], false=[Hide('minigametimercrazy'), Return(True)])
            key "K_LEFT"    action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            key "K_RIGHT"   action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            key "K_UP"      action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_2 IDLE.webp" at ClickNone
        elif setarrow == 4:
            key "K_DOWN"    action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            key "K_LEFT"    action If(time < timerrange, true=[SetVariable('time', time + 20), Play("SE1", "BeepRight.ogg")], false=[Hide('minigametimercrazy'), Return(True)])
            key "K_RIGHT"   action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            key "K_UP"      action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_4 IDLE.webp" at ClickNone
        elif setarrow == 6:
            key "K_DOWN"    action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            key "K_LEFT"    action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            key "K_RIGHT"   action If(time < timerrange, true=[SetVariable('time', time + 20), Play("SE1", "BeepRight.ogg")], false=[Hide('minigametimercrazy'), Return(True)])
            key "K_UP"      action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_6 IDLE.webp" at ClickNone
        elif setarrow == 8:
            key "K_DOWN"    action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            key "K_LEFT"    action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            key "K_RIGHT"   action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            key "K_UP"      action If(time < timerrange, true=[SetVariable('time', time + 20), Play("SE1", "BeepRight.ogg")], false=[Hide('minigametimercrazy'), Return(True)])
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_8 IDLE.webp" at ClickNone

    if renpy.variant("mobile") and not (renpy.variant("pc") or renpy.variant("web")):
        if setarrow <= 4:
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_4 IDLE.webp" at ClickNone
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action If(time < timerrange, true=[SetVariable('time', time + 20), Play("SE1", "BeepRight.ogg")], false=[Hide('minigametimercrazy'), Return(True)])
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
        elif setarrow >= 6:
            hbox:
                xalign 0.5
                yalign 0.15
                image "images/UI/Arrow_6 IDLE.webp" at ClickNone
            imagebutton:
                xalign 0.0
                yalign 0.6
                idle "images/UI/Arrow_L IDLE.webp"
                hover "images/UI/Arrow_L HOVER.webp"
                action [SetVariable('time', time - 20), Play("SE1", "BeepWrong.ogg")]
            imagebutton:
                xalign 1.0
                yalign 0.5
                idle "images/UI/Arrow_R IDLE.webp"
                hover "images/UI/Arrow_R HOVER.webp"
                action If(time < timerrange, true=[SetVariable('time', time + 20), Play("SE1", "BeepRight.ogg")], false=[Hide('minigametimercrazy'), Return(True)])

# ----------------------------------------------------------------------------------------------------
# PLAY: CLICK HOLD
# ----------------------------------------------------------------------------------------------------
screen minigameplay_hold():
    # ACTION VAR
    timer 0.01 repeat True action [
        SetVariable("bar_action", max(0, min(bar_actionmax, bar_action + a_event_0))),
        If(minigame_cpu >= 100, true = [Hide('minigameplay_hold'), SetVariable("minigamestep", "defeat"), Jump(minigame_defeat)]),
        If(minigame_p1 >= 100, true = Jump(minigame_victory)),
        ]

    vbox:
        xalign 0.02
        yalign 0.5
        spacing 10
        vbar value bar_action range bar_actionmax ymaximum 1000 xmaximum 75 at alpha_dissolve

    if a_event_0 == 0:
        text renpy.translate_string("HOLD CLICK") at ClickNone size 100 xalign 0.5 yalign 0.5

    modal True
    key "mousedown_1" action SetVariable("a_event_0", a_event_1)
    key "mouseup_1" action SetVariable("a_event_0", -a_event_2)

# ----------------------------------------------------------------------------------------------------
# SHOW: YOGA STATS
# ----------------------------------------------------------------------------------------------------
screen minigameshow_yoga():

    # TIME VAR
    timer 1 repeat True action If(bar_time > 0, true=SetVariable('bar_time', bar_time - 1), false=[Hide('minigameplay_hold'), SetVariable("minigamestep", "defeat"), Jump(minigame_timeup)])

    # ACTION VAR
    timer 0.1 repeat True action [
        If(a_event_0 == a_event_1 and a_event_0 > 0, true = SetVariable("minigame_p1", min(100, minigame_p1 + ((bar_action*0.006)+(bar_action*0.006))/(1+(minigame_p1*0.01))))),
        If(a_event_0 == a_event_1 and a_event_0 > 0 and bar_action > (20+(minigame_p1*0.8)), true = SetVariable("minigame_cpu", min(100, minigame_cpu + ((bar_action*bar_action*0.05)/(0.1+(minigame_p1*5)))))),
        If(a_event_0 == -a_event_2 and a_event_0 < 0, true = SetVariable("minigame_cpu", max(0, minigame_cpu - 0.1))),

        If(bar_action > (20+(minigame_p1*0.8)),

            true = If(not renpy.music.is_playing(channel="SE2"),
            
                true = [
                    If(minigame_cpu <= 10,
                        true = [
                            SetVariable("minigamestep1", 1),
                            If(preferences.vibration == True, Function(renpy.vibrate, 0.25)),
                            Play("SE2", renpy.random.choice(["Moan/D lvl2 (1).ogg", "Moan/D lvl2 (2).ogg", "Moan/D lvl2 (3).ogg", "Moan/D lvl2 (4).ogg", "Moan/D lvl2 (5).ogg", "Moan/D lvl2 (6).ogg", "Moan/D lvl2 (7).ogg", "Moan/D lvl2 (8).ogg", "Moan/D lvl2 (9).ogg", "Moan/D lvl2 (10).ogg", "Moan/D lvl2 (11).ogg", "Moan/D lvl2 (12).ogg", "Moan/D lvl2 (13).ogg", "Moan/D lvl2 (14).ogg", "Moan/D lvl2 (15).ogg", "Moan/D lvl2 (16).ogg"])),
                            ]),

                    If(minigame_cpu <= 25 and minigame_cpu > 10,
                        true = [
                            SetVariable("minigamestep1", 1),
                            If(preferences.vibration == True, Function(renpy.vibrate, 0.5)),
                            Play("SE2", renpy.random.choice(["Moan/D lvl3 (1).ogg", "Moan/D lvl3 (2).ogg", "Moan/D lvl3 (3).ogg"])),
                            ]),
                    
                    If(minigame_cpu <= 75 and minigame_cpu > 25,
                        true = [
                            SetVariable("minigamestep1", 1),
                            If(preferences.vibration == True, Function(renpy.vibrate, 0.75)),
                            Play("SE2", renpy.random.choice(["Moan/D lvl4 (1).ogg", "Moan/D lvl4 (2).ogg", "Moan/D lvl4 (3).ogg", "Moan/D lvl4 (4).ogg", "Moan/D lvl4 (5).ogg", "Moan/D lvl4 (6).ogg", "Moan/D lvl4 (7).ogg", "Moan/D lvl4 (8).ogg", "Moan/D lvl4 (9).ogg", "Moan/D lvl4 (10).ogg"])),
                            ]),
                    
                    If(minigame_cpu <= 90 and minigame_cpu > 75,
                        true = [
                            SetVariable("minigamestep1", 2),
                            If(preferences.vibration == True, Function(renpy.vibrate, 1)),
                            Play("SE2", renpy.random.choice(["Moan/D lvl4 (1).ogg", "Moan/D lvl4 (2).ogg", "Moan/D lvl4 (3).ogg", "Moan/D lvl4 (4).ogg", "Moan/D lvl4 (5).ogg", "Moan/D lvl4 (6).ogg", "Moan/D lvl4 (7).ogg", "Moan/D lvl4 (8).ogg", "Moan/D lvl4 (9).ogg", "Moan/D lvl4 (10).ogg", "Moan/D lvl5 (1).ogg", "Moan/D lvl5 (2).ogg", "Moan/D lvl5 (3).ogg", "Moan/D lvl5 (4).ogg", "Moan/D lvl5 (5).ogg"])),
                            ]),
                    
                    If(minigame_cpu >= 90,
                        true = [
                            SetVariable("minigamestep1", 2),
                            If(preferences.vibration == True, Function(renpy.vibrate, 1.5)),
                            Play("SE2", renpy.random.choice(["Moan/D lvl5 (1).ogg", "Moan/D lvl5 (2).ogg", "Moan/D lvl5 (3).ogg", "Moan/D lvl5 (4).ogg", "Moan/D lvl5 (5).ogg"])),
                            ]),

                    ]),

            false = [
                SetVariable("minigamestep1", 0),
            ]),
        ]

    vbox:
        xalign 0.98
        yalign 0.5
        spacing 50
        vbox:
            spacing 10
            vbox:
                xalign 0.5
                text renpy.translate_string("{color=#FFFFFF}{b}Time:{/b} [bar_time]s{/color}") outlines [(2, "#323232", 0, 0)]
            vbox:
                vbar:
                    xysize(150,150)
                    value AnimatedValue(bar_time, bar_timemax, delay=1)
                    right_bar "gui/CustomBar/TimeMin.webp" at Zoom_15
                    left_bar "gui/CustomBar/TimeMax.webp"
        vbox:
            spacing 10
            vbox:
                xalign 0.5
                text renpy.translate_string("{color=#FFFFFF}{b}Pain:{/b} ")+str(int(minigame_cpu)).zfill(2)+"%{/color}" outlines [(2, "#323232", 0, 0)]
            vbox:
                xalign 0.5
                vbar:
                    xysize(150,150)
                    value AnimatedValue(minigame_cpu, 100, delay=0.5)
                    range 100
                    left_bar "gui/CustomBar/PainMin.webp" at Zoom_15
                    right_bar "gui/CustomBar/PainMax.webp"
        vbox:
            spacing 10
            vbox:
                xalign 0.5
                text renpy.translate_string("{color=#FFFFFF}{b}Flexibility:{/b} ")+str(int(minigame_p1))+"%{/color}" outlines [(2, "#323232", 0, 0)]
            vbox:
                xalign 0.5
                vbar:
                    xysize(150,150)
                    value AnimatedValue(minigame_p1, 100, delay=0.5)
                    range 100
                    left_bar "gui/CustomBar/FlexMin.webp" at Zoom_15
                    right_bar "gui/CustomBar/FlexMax.webp"
