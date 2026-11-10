# ---------------------------------------------------------------------------
screen Minigame_Drag_AI:
# ---------------------------------------------------------------------------
    timer 0.1 repeat True action [
    SetVariable("a_menu_5", renpy.random.random()),
    If(wdis_ani_masturbating>0, true=(SetVariable("wdis_ani_masturbating", max(0, wdis_ani_masturbating-0.5))), false=(SetVariable("wdis_ani_write", 1))),
    If(a_menu_3 >= 200, true=(Jump("action_tutoring_command_check")),
        false=(
            If(wdis_ani_write == 1, If(wdis_ani_writing < 2.0, true=(SetVariable("wdis_ani_writing", wdis_ani_writing+0.2)), false=(SetVariable("wdis_ani_write", 2)))),
            If(wdis_ani_write == 2, If(wdis_ani_writing > 1, true=(SetVariable("wdis_ani_writing", wdis_ani_writing-0.2)), false=(SetVariable("wdis_ani_write", 1)))),
            )),
    If(a_menu_5 < 0.2 + ((a_menu_7*0.05)/(0.5+(a_menu_7*a_menu_7*0.5))) + (wdis_learn*0.007),
        true=(
            If(a_menu_4 < a_menu_2,
                true=(SetVariable("a_menu_2", a_menu_2-25)),
                false=(SetVariable("a_menu_2", a_menu_2+25)),
                ),
            SetVariable("a_menu_3", a_menu_3+5),
            ),
        false=(
            If(a_menu_4 < a_menu_2,
                true=(SetVariable("a_menu_2", a_menu_2+25)),
                false=(SetVariable("a_menu_2", a_menu_2-25)),
                ),
            SetVariable("a_menu_3", a_menu_3+5),
            ),
        )
    ]

    frame:
        background "#00000080"
        xalign 0.5
        yalign 0.9
        xsize 1280
        ysize 500
        text renpy.translate_string("{size=40}Ok. Let's see if she learns{/size}") xalign 0.5 yalign 0.0
        if Minigame_Drag_Item == "Red":
            hbox:
                xalign 0.5
                yalign 0.2
                xoffset a_menu_2
                yoffset a_menu_3
                frame:
                    background "#FF0000"
                    xsize 150
                    ysize 150
        elif Minigame_Drag_Item == "Yellow":
            hbox:
                xalign 0.5
                yalign 0.2
                xoffset a_menu_2
                yoffset a_menu_3
                frame:
                    background "#FFFF00"
                    xsize 150
                    ysize 150
        elif Minigame_Drag_Item == "Green":
            hbox:
                xalign 0.5
                yalign 0.2
                xoffset a_menu_2
                yoffset a_menu_3
                frame:
                    background "#00FF00"
                    xsize 150
                    ysize 150
        elif Minigame_Drag_Item == "Cyan":
            hbox:
                xalign 0.5
                yalign 0.2
                xoffset a_menu_2
                yoffset a_menu_3
                frame:
                    background "#00FFFF"
                    xsize 150
                    ysize 150
        elif Minigame_Drag_Item == "Blue":
            hbox:
                xalign 0.5
                yalign 0.2
                xoffset a_menu_2
                yoffset a_menu_3
                frame:
                    background "#0000FF"
                    xsize 150
                    ysize 150
        elif Minigame_Drag_Item == "Magenta":
            hbox:
                xalign 0.5
                yalign 0.2
                xoffset a_menu_2
                yoffset a_menu_3
                frame:
                    background "#FF00FF"
                    xsize 150
                    ysize 150

        hbox:
            yalign 0.9
            frame:
                background "#FF000080"
                xsize 200
                ysize 200
            frame:
                background "#FFFF0080"
                xsize 200
                ysize 200
            frame:
                background "#00FF0080"
                xsize 200
                ysize 200
            frame:
                background "#00FFFF80"
                xsize 200
                ysize 200
            frame:
                background "#0000FF80"
                xsize 200
                ysize 200
            frame:
                background "#FF00FF80"
                xsize 200
                ysize 200

# ---------------------------------------------------------------------------
screen Minigame_Drag:
# ---------------------------------------------------------------------------
    frame:
        background "#00000080"
        xalign 0.5
        yalign 0.9
        xsize 1280
        ysize 500
        text renpy.translate_string("{size=40}Drag this box to the box with the corresponding color{/size}") xalign 0.5 yalign 0.0
        draggroup:
            if Minigame_Drag_Item == "Red":
                drag:
                    drag_name "DragRed"
                    xalign 0.5
                    yalign 0.2
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
                    frame:
                        background "#FF0000"
                        xsize 150
                        ysize 150
                        text renpy.translate_string("{b}ANSWER{/b}") xalign 0.5 yalign 0.5
            elif Minigame_Drag_Item == "Yellow":
                drag:
                    drag_name "DragYellow"
                    xalign 0.5
                    yalign 0.2
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
                    frame:
                        background "#FFFF00"
                        xsize 150
                        ysize 150
                        text renpy.translate_string("{b}ANSWER{/b}") xalign 0.5 yalign 0.5
            elif Minigame_Drag_Item == "Green":
                drag:
                    drag_name "DragGreen"
                    xalign 0.5
                    yalign 0.2
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
                    frame:
                        background "#00FF00"
                        xsize 150
                        ysize 150
                        text renpy.translate_string("{b}ANSWER{/b}") xalign 0.5 yalign 0.5
            elif Minigame_Drag_Item == "Cyan":
                drag:
                    drag_name "DragCyan"
                    xalign 0.5
                    yalign 0.2
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
                    frame:
                        background "#00FFFF"
                        xsize 150
                        ysize 150
                        text renpy.translate_string("{b}ANSWER{/b}") xalign 0.5 yalign 0.5
            elif Minigame_Drag_Item == "Blue":
                drag:
                    drag_name "DragBlue"
                    xalign 0.5
                    yalign 0.2
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
                    frame:
                        background "#0000FF"
                        xsize 150
                        ysize 150
                        text renpy.translate_string("{b}ANSWER{/b}") xalign 0.5 yalign 0.5
            elif Minigame_Drag_Item == "Magenta":
                drag:
                    drag_name "DragMagenta"
                    xalign 0.5
                    yalign 0.2
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
                    frame:
                        background "#FF00FF"
                        xsize 150
                        ysize 150
                        text renpy.translate_string("{b}ANSWER{/b}") xalign 0.5 yalign 0.5

            drag:
                drag_name "DropRed"
                xalign 0.0
                yalign 0.9
                draggable False
                droppable True
                frame:
                    background "#FF000080"
                    xsize 200
                    ysize 200
                    text renpy.translate_string("{b}QUESTION{/b}") xalign 0.5 yalign 0.5
            drag:
                drag_name "DropYellow"
                xalign 0.2
                yalign 0.9
                draggable False
                droppable True
                frame:
                    background "#FFFF0080"
                    xsize 200
                    ysize 200
                    text renpy.translate_string("{b}QUESTION{/b}") xalign 0.5 yalign 0.5
            drag:
                drag_name "DropGreen"
                xalign 0.4
                yalign 0.9
                draggable False
                droppable True
                frame:
                    background "#00FF0080"
                    xsize 200
                    ysize 200
                    text renpy.translate_string("{b}QUESTION{/b}") xalign 0.5 yalign 0.5
            drag:
                drag_name "DropCyan"
                xalign 0.6
                yalign 0.9
                draggable False
                droppable True
                frame:
                    background "#00FFFF80"
                    xsize 200
                    ysize 200
                    text renpy.translate_string("{b}QUESTION{/b}") xalign 0.5 yalign 0.5
            drag:
                drag_name "DropBlue"
                xalign 0.8
                yalign 0.9
                draggable False
                droppable True
                frame:
                    background "#0000FF80"
                    xsize 200
                    ysize 200
                    text renpy.translate_string("{b}QUESTION{/b}") xalign 0.5 yalign 0.5
            drag:
                drag_name "DropMagenta"
                xalign 1.0
                yalign 0.9
                draggable False
                droppable True
                frame:
                    background "#FF00FF80"
                    xsize 200
                    ysize 200
                    text renpy.translate_string("{b}QUESTION{/b}") xalign 0.5 yalign 0.5

#---------------------------------------------------------------------------
screen tutoring_pose_wdis_masturbate():
#---------------------------------------------------------------------------
    timer 0.1 repeat True action [
        SetVariable("wdis_lust", wdis_lust+0.5),
        If(wdis_ani_masturbate==1, true=([
            If(wdis_ani_masturbating>=8, true=(SetVariable("wdis_ani_masturbating", 4+(wdis_lust*wdis_lust*wdis_lust/500000)))),
            If(wdis_ani_masturbating<8, true=(SetVariable("wdis_ani_masturbating", wdis_ani_masturbating+(wdis_lust*wdis_lust*wdis_lust/500000)))),
            If(wdis_lust>=100, true=(SetVariable("wdis_ani_masturbate", 2))),
            ])),
        If(wdis_ani_masturbate==2, true=(SetVariable("wdis_ani_cum", min(1, wdis_ani_cum+0.1)))),
        If(wdis_ani_cum>=1, true=(SetVariable("wdis_ani_masturbating", max(0, wdis_ani_masturbating-0.1)))),
        ]

    vbox:
        xpos 50
        yalign 0.5
        image "images/UI/OC_WDIS.webp"
        vbar:
            xysize(150,150)
            value AnimatedValue(wdis_lust, 100, delay=1)
            left_bar "gui/CustomBar/LustMin.webp"
            right_bar "gui/CustomBar/LustMax.webp"

#---------------------------------------------------------------------------
screen tutoring_pose_wdis():
#---------------------------------------------------------------------------
    timer 0.1 repeat True action [

    If(wdis_ani_breathe==0, true=(
        If(wdis_ani_breathing<0.2+(0.4*(wdis_lust/50)), true=(
            SetVariable("wdis_ani_breathing", wdis_ani_breathing+(0.03+(wdis_lust*wdis_lust/50000)))
            ), false=(
            SetVariable("wdis_ani_breathe", 1)
            ))
        )),

    If(wdis_ani_breathe==1, true=(
        If(wdis_ani_breathing>0, true=(
            SetVariable("wdis_ani_breathing", wdis_ani_breathing-(0.03+(wdis_lust*wdis_lust/50000)))
            ), false=(
            SetVariable("wdis_ani_breathe", 0)
            ))
        )),

    If(wdis_ani_write == 0, true=([
        SetVariable("wdis_ani_writing", max(0, wdis_ani_writing-0.2)),
        If(wdis_lust>=100, true=(SetVariable("wdis_ani_masturbate", 2)), false=(
            If(wdis_lust>=80, true=([SetVariable("wdis_ani_masturbate", 1), Jump("action_tutoring_end")]))
            )),
        If(hero_ani_hand_XMov == 1, true=(
            If (hero_ani_hand_XPos != -0.5+(renpy.get_mouse_pos()[0]/(1920/2)), true=([
                SetVariable("wdis_lust", wdis_lust+(lustadd_wdis * (abs((0.5*(1+(perk_cha_sex*0.5)))-(hero_ani_hand_XPos-(-0.5+(renpy.get_mouse_pos()[0]/(1920/2))))))/(2+(wdis_focus*0.5)))),
                SetVariable("wdis_focus", max(0, wdis_focus-(0.25+(wdis_lust*0.009)+(abs(0.5-(hero_ani_hand_XPos-(-0.5+(renpy.get_mouse_pos()[0]/(1920/2))))))))),
                ]),false=(
            SetVariable("wdis_focus", max(0, wdis_focus-(0.1+(wdis_lust*0.009)))),
        ))))])),

    SetVariable("loveadd_wdis", ((1.5 * ((1.00 + (perk_cha_sex * 0.2)) * (1 + (stat_cha * 0.0025)))) * (1 + (0.01 * wdis_bonus))) * (0.75 + (0.002 * personality[2])) * (1 + (wdis_love * 0.0025))),
    SetVariable("lustadd_wdis", ((2.0 * ((1.00 + (perk_cha_sex * 0.2)) * (1 + (stat_cha * 0.0025)))) * (1 + (0.01 * wdis_bonus))) * (0.75 + (0.002 * personality[1])) * (1 + (wdis_love * 0.0025)) / (1 + (wdis_lust * wdis_lust * 0.0004))),
    SetVariable("intiadd_wdis", ((0.5 * ((1.00 + (perk_cha_sex * 0.2)) * (1 + (stat_cha * 0.0025)))) * (1 + (0.01 * wdis_bonus))) * (0.75 + (0.002 * personality[4])) * (1 + (wdis_love * 0.0050)) * (0.9 + (wdis_lust * 0.005)) / (1 + (wdis_inti * 0.02))),    
    ]

    vbox:
        xpos 50
        yalign 0.5
        image "images/UI/OC_WDIS.webp"
        vbar:
            xysize(150,150)
            value AnimatedValue(wdis_inti, 100, delay=1)
            left_bar "gui/CustomBar/IntiMin.webp"
            right_bar "gui/CustomBar/IntiMax.webp"
        vbar:
            xysize(150,150)
            value AnimatedValue(wdis_love, 100, delay=1)
            left_bar "gui/CustomBar/LoveMin.webp"
            right_bar "gui/CustomBar/LoveMax.webp"
        vbar:
            xysize(150,150)
            value AnimatedValue(wdis_lust, 100, delay=1)
            left_bar "gui/CustomBar/LustMin.webp"
            right_bar "gui/CustomBar/LustMax.webp"
        vbar:
            xysize(150,150)
            value AnimatedValue(wdis_learn, 100, delay=1)
            left_bar "gui/CustomBar/KnowMin.webp"
            right_bar "gui/CustomBar/KnowMax.webp"
        vbar:
            xysize(150,150)
            value AnimatedValue(wdis_focus, 100, delay=1)
            left_bar "gui/CustomBar/FocuMin.webp"
            right_bar "gui/CustomBar/FocuMax.webp"

#---------------------------------------------------------------------------
screen tutoring_pose_hero():
#---------------------------------------------------------------------------
    timer 0.1 repeat True action [
    SetVariable("hero_ani_hand_XPos", -0.5+(renpy.get_mouse_pos()[0]/(1920/2))),
    If(hero_ani_breathe==0, true=(If(hero_ani_breathing<0.1+(0.3), true=(SetVariable("hero_ani_breathing", hero_ani_breathing+(0.01+(0.01)))), false=(SetVariable("hero_ani_breathe", 1))))),
    If(hero_ani_breathe==1, true=(If(hero_ani_breathing>0, true=(SetVariable("hero_ani_breathing", hero_ani_breathing-(0.01+(0.01)))), false=(SetVariable("hero_ani_breathe", 0))))),
    ]

#---------------------------------------------------------------------------
screen tutoring_UI():
#---------------------------------------------------------------------------
    #timer 0.1 repeat True action [ If(gametimesec < 360, true=(SetVariable("gametimesec", gametimesec+0.1)), false=(Jump("action_tutoring_end")), ), ]

    modal True

    text renpy.translate_string("Score: ")+str(round((1+int(Club_IsMember("hero", "stco"))) * (1+(wdis_learn*0.09)) * (1+(a_menu_6/5)) * (0.75+(perk_cha_per/4)), 2)) size 60 xalign 0.5 yalign 0.2 outlines [(2, "#323232", 0, 0)]
    frame:
        background "#00000064"
        xysize(1400,300)
        xpadding 25
        ypadding 25
        xalign 0.5
        yalign 0.8
        text texticulo.value size 40

    vbox:
        xalign 1.0
        yalign 0.5
        xoffset -50
        spacing 25
        frame:
            background None
            xsize 150
            ysize 150
            hbox:
                xalign 0.5
                yalign 0.5
                button:
                    vbar:
                        xysize(150,150)
                        value AnimatedValue(gametimesec, 360, delay=1)
                        left_bar "gui/CustomBar/TimeMin.webp"
                        right_bar "gui/CustomBar/TimeMax.webp"
                    at transform:
                        on idle:
                            ease 0.1 outline_transform(2, "#FFF", 3.0)
                        on hover:
                            ease 0.1 outline_transform(10, "#FFF", 3.0)
                    hovered texticulo.Action("You have "+str(360-gametimesec)+" seconds left")
                    action texticulo.Action("You have "+str(360-gametimesec)+" seconds left")
        frame:
            background None
            xsize 150
            ysize 150
            hbox:
                xalign 0.5
                yalign 0.5
                button:
                    add "images/UI/MinigameAction/ACTION_Minigame Write.webp"
                    at transform:
                        on idle:
                            ease 0.1 outline_transform(2, "#FFF", 3.0)
                        on hover:
                            ease 0.1 outline_transform(10, "#FFF", 3.0)
                    hovered texticulo.Action("""
                        Teach her how to solve a problem.
                        [C_Dat]▫ Time:[C_Off] [C_Neg]- 20 seconds[C_Off]
                        [C_Dat]▫ Right:[C_Off] [C_Pos]+ """+str(round(min(100, ((5+((1+perk_int_mem)*(1+perk_int_mem))) + (0.75 + (renpy.random.random() * 0.25)) * (1+(5*(1+perk_cha_per)))) * (1+(wdis_inti*0.0005)) * (1+(wdis_love*0.0005)) / (1+(wdis_lust*0.01)))))+""" knowledge[C_Off], [C_Pos]+ """+str(round((wdis_learn/(1+(wdis_lust*0.09)))))+""" focus[C_Off]
                        [C_Dat]▫ Wrong:[C_Off] [C_Neg]- """+str(round(max(0, ((5+((1+perk_int_mem)*(1+perk_int_mem))) + (0.75 + (renpy.random.random() * 0.25)) * (1+(5*(1+perk_int_mem)))) * (1+(wdis_inti*0.0005)) * (1+(wdis_love*0.0005)) / (1+(wdis_lust*0.01)))))+""" knowledge[C_Off], [C_Pos]+ """+str(round((wdis_learn/(1+(wdis_lust*0.09)))))+""" focus[C_Off]
                        """)
                    action Jump("action_tutoring_write")

        frame:
            background None
            xsize 150
            ysize 150
            hbox:
                xalign 0.5
                yalign 0.5
                button:
                    add "images/UI/MinigameAction/ACTION_Minigame Command.webp"
                    at transform:
                        on idle:
                            ease 0.1 outline_transform(2, "#FFF", 3.0)
                        on hover:
                            ease 0.1 outline_transform(10, "#FFF", 3.0)
                    hovered texticulo.Action("""
                        Teach her how to solve a problem.
                        [C_Dat]▫ Time:[C_Off] [C_Neg]- 60 seconds[C_Off]
                        [C_Dat]▫ Right:[C_Off] [C_Pos]+ """+str(round(min(100, (35 + (renpy.random.random() * 10)) * (1+(wdis_inti*0.0005)) * (1+(wdis_love*0.0005)) / (1+(wdis_lust*0.01)))))+""" knowledge[C_Off], [C_Pos]+ 1 Right Answer[C_Off]
                        [C_Dat]▫ Wrong:[C_Off] [C_Neg]- """+str(round(max(0, (35 + (renpy.random.random() * 10)) * (1+(wdis_inti*0.0005)) * (1+(wdis_love*0.0005)) / (1+(wdis_lust*0.01)))))+""" knowledge[C_Off], [C_Neg]- 1 Right Answer[C_Off]
                        """)
                    action Jump("action_tutoring_command")

        frame:
            background None
            xsize 150
            ysize 150
            hbox:
                xalign 0.5
                yalign 0.5
                button:
                    add "images/UI/MinigameAction/ACTION_Minigame Positive.webp"
                    at transform:
                        on idle:
                            ease 0.1 outline_transform(2, "#FFF", 3.0)
                        on hover:
                            ease 0.1 outline_transform(10, "#FFF", 3.0)
                    if a_menu_8 > 0:
                                    hovered texticulo.Action("""
                                        Praise her performance.
                                        [C_Dat]▫ Time:[C_Off] [C_Neg]- 10 seconds[C_Off]
                                        [C_Dat]▫ Love:[C_Off] [C_Pos]+ """+str(round(((0.5 + (a_menu_6 * 0.5)) / (1 + a_menu_7)) * loveadd_wdis))+"""[C_Off]
                                        [C_Dat]▫ Lust:[C_Off] [C_Pos]+ """+str(round(((0.5 + (a_menu_6 * 0.5)) / (1 + a_menu_7)) * lustadd_wdis))+"""[C_Off]
                                        """)
                    elif a_menu_7 == 1:
                                    hovered texticulo.Action("""
                                        Praise her performance.
                                        [C_Dat]▫ Time:[C_Off] [C_Neg]- 10 seconds[C_Off]
                                        [C_Dat]▫ Love:[C_Off] [C_Pos]+ """+str(round(abs(((0.5 + (a_menu_6 * 0.5)) / (1 + a_menu_7)) * loveadd_wdis)/2))+"""[C_Off]
                                        [C_Dat]▫ Lust:[C_Off] [C_Pos]+ """+str(round(((0.5 + (a_menu_6 * 0.5)) / (1 + a_menu_7)) * lustadd_wdis))+"""[C_Off]
                                        """)
                    else:
                                    hovered texticulo.Action("""
                                        Praise her performance.
                                        [C_Dat]▫ Time:[C_Off] [C_Neg]- 10 seconds[C_Off]
                                        [C_Dat]▫ Love:[C_Off] [C_Pos]+ """+str(round(((0.5 + (a_menu_6 * 0.5)) / (1 + a_menu_7)) * loveadd_wdis))+"""[C_Off]
                                        [C_Dat]▫ Lust:[C_Off] [C_Pos]+ """+str(round(((0.5 + (a_menu_6 * 0.5)) / (1 + a_menu_7)) * lustadd_wdis))+"""[C_Off]
                                        """)

                    action Jump("action_tutoring_positive")

# ----------------------------------------------------------------------------------------------------
label action_tutoring_end:
# ----------------------------------------------------------------------------------------------------
    hide screen tutoring_UI
    hide screen tutoring_pose_wdis
    $ hero_ani_hand_YMov = 1
    $ hero_ani_hand_XMov = 0
    $ hero_ani_eyeX = 0.2
    $ hero_ani_eyeY = 0.6

    if wdis_ani_masturbate >= 1:

        $ wdis_ani_mouA = 0
        $ hero_ani_mouA = 1
        hero "A{w=[wt1]}-are you okay...?{w=1}{nw}"

        $ wdis_ani_mouA = 1
        $ hero_ani_mouA = 0
        wdis "U-{w=[wt1]}uh...{w=[wt3]} Y{w=[wt1]}-yes.{w=[wt2]} My l{w=[wt1]}-leg is just a little itchy.{w=[wt3]} D{w=[wt1]}-don't worry.{w=1}{nw}"

        $ wdis_ani_mouA = 0
        $ hero_ani_mouA = 1
        hero "O{w=[wt1]}-okay, so...{w=1}{nw}"

        $ hero_ani_hand_YMov = 0
        $ hero_ani_hand_XMov = 1
        $ hero_ani_mouA = 0
        show screen tutoring_pose_wdis_masturbate
        show screen tutoring_pose_hero
        with dissolve

        if perk_int_per >= 3*renpy.random.random():
            $ hero_ani_eyeX = 0.2
            $ hero_ani_eyeY = 0.2
            $ a_menu_1 = perk_int_per
            $ msg.msg(renpy.translate_string("[C_Pos]Success check for [C_Dat]Perception[C_Off] skill[C_Off]"))
            play SE1 "JingleRight.ogg"
            hide action_tutor_study2_mg library with dissolve
        else:
            $ hero_ani_eyeX = 0.5
            $ hero_ani_eyeY = 0.2
            $ a_menu_1 = 0
            $ msg.msg(renpy.translate_string("[C_Neg]Fail check for [C_Dat]Perception[C_Off] skill[C_Off]"))
            play SE1 "JingleWrong.ogg"

        while wdis_ani_cum < 1:
            $ renpy.pause(1, hard=True)

        hide screen tutoring_pose_wdis_masturbate

        play SE1 "JingleRight.ogg"
        $ msg.msg(renpy.translate_string("{nm}[fnamewdis]{/nm} came, and her lust reset."))
        $ wdis_lust = 0
        $ xp_now += 25 * (a_menu_1+1)
        $ msg.msg(renpy.translate_string("XP [C_Pos]+ ")+str(25 * (a_menu_1+1))[:4]+renpy.translate_string("[C_Off]."))
        $ add_stat("wdis", "inti", 2+a_menu_1)

        pause(1)

        $ wdis_ani_mouA = 1
        wdis "U-{w=[wt1]}uh...{w=[wt3]} S{w=[wt1]}-sorry.{w=[wt3]} I n{w=[wt1]}-need to go now!{w=1}{nw}"

        hide ANI_WDIS_Tutor breathe with dissolve

        $ wdis_ani_mouA = 0
        $ hero_ani_mouA = 1
        hero "O{w=[wt1]}-oh...{w=[wt2]} S{w=[wt1]}-sure...{w=1}{nw}"

        $ hero_ani_mouA = 0
        $ msg.msg(renpy.translate_string("Oops... You didn't gain money for this work."))
        $ wdis_lust = 0

    else:
        $ hero_ani_mouA = 1
        hero "Oops{w=[wt2]}, look at the time!{w=[wt3]} I think that's it for today.{w=1}{nw}"

        $ hero_ani_mouA = 0
        $ wdis_ani_mouA = 1

        if wdis_learn < 30:
            wdis "U-{w=[wt1]}uh.{w=[wt3]} T{w=[wt1]}-thank you for trying to teach me.{w=1}{nw}"
        elif wdis_learn < 60:
            wdis "O{w=[wt1]}-okay...{w=[wt3]} Thank you so much for trying to help someone like me...{w=1}{nw}"
        elif wdis_learn < 90:
            wdis "O{w=[wt1]}-okay{w=[wt2]}, t{w=[wt1]}-thank you so much for your help!{w=[wt3]} Even someone like me could understand some things today.{w=1}{nw}"
        else:
            wdis "Y{w=[wt1]}-you know what?{w=[wt3]} I kinda feel a little more intelligent thanks to you.{w=[wt4]} Thank you so much for taking your time to help someone like me...{w=1}{nw}"

        $ wdis_ani_mouA = 0

        $ check_stat()
        $ a_menu_7 = max(0, a_menu_7)
        $ a_menu_1 = max(5, round((1+int(Club_IsMember("hero", "stco"))) * (1+(wdis_learn*0.09)) * (1+(a_menu_6/5)) * (0.75+(perk_cha_per/4)), 2))
        $ money += a_menu_1
        $ msg.msg(renpy.translate_string("money [C_Pos]+$[a_menu_1][C_Off]"))

        $ add_stat("hero", "club_stco", (1 + (a_menu_1/30)))

        $ a_menu_2 = round(((1+((a_menu_6*2)*((1+(a_menu_7*1.5))/(1+(a_menu_7*a_menu_7)))))/2), 2)
        $ add_stat("wdis", "love", a_menu_2)
        $ add_stat("hero", "cha_soc", a_menu_2)

        $ a_menu_3 = round(((2+((a_menu_6)*((1+(a_menu_7*1.5))/(1+(a_menu_7*a_menu_7)))))/2), 2)
        $ add_stat("wdis", "inti", a_menu_3)

    scene bg_0
    with Dissolve(1)

    pause

    $ gametimehour = 18
    $ gametimemin = 0
    call gametime from _call_gametime_82

    jump show_ui

# ----------------------------------------------------------------------------------------------------
label action_tutoring_command:
# ----------------------------------------------------------------------------------------------------
    hide screen tutoring_UI

    $ hero_ani_hand_XMov = 0
    $ hero_ani_hand_YMov = 1
    $ hero_ani_eyeX = 0.2
    $ hero_ani_eyeY = 0.6
    $ hero_ani_mouA = 1
    $ wdis_focus += (75/(1+(wdis_lust*0.09)))

    hero "Now it's your time.{w=0.2} Let's see if you can do it!{w=1}{nw}"

    $ hero_ani_mouA = 0
    $ wdis_ani_mouA = 1
    wdis "Ok.{w=1}{nw}"

    $ wdis_ani_eyeX = 0.6
    $ wdis_ani_eyeY = 0.2
    $ wdis_ani_mouA = 0
    $ Minigame_Drag_Item = renpy.random.choice(["Red", "Yellow", "Green", "Cyan", "Blue", "Magenta"])

    $ a_menu_2 = 0
    $ a_menu_3 = 0

    if Minigame_Drag_Item == "Red":
        $ a_menu_4 = -550
    elif Minigame_Drag_Item == "Yellow":
        $ a_menu_4 = -350
    elif Minigame_Drag_Item == "Green":
        $ a_menu_4 = -150
    elif Minigame_Drag_Item == "Cyan":
        $ a_menu_4 = 50
    elif Minigame_Drag_Item == "Blue":
        $ a_menu_4 = 250
    elif Minigame_Drag_Item == "Magenta":
        $ a_menu_4 = 450

    call screen Minigame_Drag_AI
    label action_tutoring_command_check:
        $ wdis_ani_write = 0
        if abs(a_menu_2 - a_menu_4) <= 200:

            $ a_menu_6 += 1
            $ a_menu_7 = max(0, a_menu_7-1)
            $ gametimesec += 60
            $ wdis_learn += min(100, (0.8 + (renpy.random.random() * 0.2)) * (1+(wdis_inti*0.0005)) * (1+(wdis_love*0.0005)) / (1+(wdis_lust*0.01)))
            $ msg.msg(renpy.translate_string("Right answer"))
            play SE1 "JingleRight.ogg"

        else:

            $ a_menu_6 -= 1
            $ gametimesec += 60
            $ wdis_learn -= max(0, (0.8 + (renpy.random.random() * 0.2)) * (1+(wdis_inti*0.0005)) * (1+(wdis_love*0.0005)) / (1+(wdis_lust*0.01)))
            $ msg.msg(renpy.translate_string("Wrong answer"))
            play SE1 "JingleWrong.ogg"

    jump action_tutoring_check

# ----------------------------------------------------------------------------------------------------
label action_tutoring_positive:
# ----------------------------------------------------------------------------------------------------
    hide screen tutoring_UI

    $ a_menu_7 += 1
    $ hero_ani_eyeX = 0.2
    $ hero_ani_eyeY = 0.6
    $ hero_ani_mouA = 1

    if a_menu_6 < 0:
        hero "Don't worry{w=1}, you're doing fine.{w=1}{nw}"
    elif a_menu_6 == 0:
        hero "You're doing fine.{w=1}{nw}"
    elif a_menu_6 < 2:
        hero "Good job!{w=1} You're doing fine!{w=1}{nw}"
    elif a_menu_6 == 2:
        hero "Yes!{w=1} You're learned very well!{w=1}{nw}"
    elif a_menu_6 > 2:
        hero "Excelent!{w=1} You're amazing!{w=1}{nw}"

    $ a_menu_8 = ((0.5 + (a_menu_6 * 0.5)) / a_menu_7)
    $ a_menu_9 = ((0.5 + (a_menu_6 * 0.5)) / a_menu_7)

    if a_menu_8 > 0:
        $ add_stat("wdis", "love", a_menu_8)
        $ add_stat("hero", "cha_soc", a_menu_8)
    elif a_menu_7 == 1:
        $ add_stat("wdis", "love", abs(a_menu_8)/2)
        $ add_stat("hero", "cha_soc", abs(a_menu_8)/2)
    else:
        $ add_stat("wdis", "love", a_menu_8)
        $ add_stat("hero", "cha_soc", a_menu_8)

    $ hero_ani_mouA = 0
    $ wdis_ani_eyeX = 0.8
    $ wdis_ani_eyeY = 0.6
    $ wdis_ani_mouA = 1

    if a_menu_6 < 0:
        wdis "A{w=1}-are you making fun of me?{w=1}{nw}"
        hero "I just wanna encourage you.{w=1}{nw}"
    elif a_menu_6 == 0:
        wdis "I still didn't anything...{w=1}{nw}"
        hero "I know you'll do it well.{w=1}{nw}"
    elif a_menu_6 > 0:
        wdis "T{w=1}-thank you!{w=1} It's all thanks to you.{w=1}{nw}"

    $ add_stat("wdis", "lust", a_menu_9)

    $ gametimesec += 10
    $ wdis_ani_mouA = 0
    jump action_tutoring_check

# ----------------------------------------------------------------------------------------------------
label action_tutoring_write:
# ----------------------------------------------------------------------------------------------------
    hide screen tutoring_UI

    $ hero_ani_hand_YMov = 0
    $ hero_ani_hand_XMov = 1
    $ hero_ani_eyeX = 0.2
    $ hero_ani_eyeY = 0.6
    $ hero_ani_mouA = 1
    $ wdis_focus += (15/(1+(wdis_lust*0.09)))

    hero "Here.{w=0.2} Pay attention to this!{w=1}{nw}"

    $ hero_ani_eyeX = 0.4
    $ hero_ani_eyeY = 0.2
    $ hero_ani_mouA = 0

    $ Minigame_Drag_Item = renpy.random.choice(["Red", "Yellow", "Green", "Cyan", "Blue", "Magenta"])
    call screen Minigame_Drag

    if draggable == "DragRed":
        if droppable == "DropRed":
            $ Answer = "Right"
        else:
            $ Answer = "Wrong"

    elif draggable == "DragYellow":
        if droppable == "DropYellow":
            $ Answer = "Right"
        else:
            $ Answer = "Wrong"

    elif draggable == "DragGreen":
        if droppable == "DropGreen":
            $ Answer = "Right"
        else:
            $ Answer = "Wrong"

    elif draggable == "DragCyan":
        if droppable == "DropCyan":
            $ Answer = "Right"
        else:
            $ Answer = "Wrong"

    elif draggable == "DragBlue":
        if droppable == "DropBlue":
            $ Answer = "Right"
        else:
            $ Answer = "Wrong"

    elif draggable == "DragMagenta":
        if droppable == "DropMagenta":
            $ Answer = "Right"
        else:
            $ Answer = "Wrong"

    if Answer == "Right":

        $ gametimesec += 20
        $ wdis_learn += min(100, ((5+((1+perk_int_mem)*(1+perk_int_mem))) + (0.75 + (renpy.random.random() * 0.25)) * (1+(5*(1+perk_cha_per)))) * (1+(wdis_inti*0.0005)) * (1+(wdis_love*0.0005)) / (1+(wdis_lust*0.01)))
        $ wdis_focus += (wdis_learn/(1+(wdis_lust*0.09)))

        play SE1 "JingleRight.ogg"
        $ msg.msg(renpy.translate_string("Right"))
        $ hero_ani_eyeX = 0.2
        $ hero_ani_eyeY = 0.6
        pause(0.5)
        $ hero_ani_mouA = 1
        hero "Got it?{w=1}{nw}"


        if wdis_learn < 30:
            wdis "Uh...{w=3} I don't know.{w=1}{nw}"
        elif wdis_learn < 60:
            wdis "M-{w=1}maybe.{nw}"
        elif wdis_learn < 90:
            wdis "I think I understood{w=1}{nw}"
        else:
            wdis "Y-{w=1}yes!{nw}"

    elif Answer == "Wrong":

        $ gametimesec += 20
        $ wdis_learn -= max(0, ((5+((1+perk_int_mem)*(1+perk_int_mem))) + (0.8 + (renpy.random.random() * 0.2)) * (1+(5*(1+perk_int_mem)))) * (1+(wdis_inti*0.0005)) * (1+(wdis_love*0.0005)) / (1+(wdis_lust*0.01)))
        $ wdis_focus += (wdis_learn/(1+(wdis_lust*0.09)))

        play SE1 "JingleWrong.ogg"
        $ msg.msg(renpy.translate_string("Wrong"))
        $ hero_ani_eyeX = 0.2
        $ hero_ani_eyeY = 0.6
        pause(0.5)
        $ hero_ani_mouA = 1
        hero "Well...{w=1}{nw}"

    $ hero_ani_mouA = 0
    jump action_tutoring_check

screen disable_click():
    timer 0.5 repeat True action Hide("disable_click")
    modal True

# ----------------------------------------------------------------------------------------------------
label action_tutoring_start:
# ----------------------------------------------------------------------------------------------------
    $ gametimesec = max(0, ((gametimehour * 60) + gametimemin) - 720)
    $ a_menu_1 = 0
    $ a_menu_2 = 0
    $ a_menu_3 = 0
    $ a_menu_4 = 0
    $ a_menu_6 = 0
    $ a_menu_7 = 0
    $ a_menu_8 = 0

    $ hero_ani_hand_XMov = 0
    $ hero_ani_hand_YMov = 0
    $ hero_ani_hand_XPos = 0.5 + renpy.get_mouse_pos()[0]/(1920/2)
    $ hero_ani_breathe = 0
    $ hero_ani_breathing = 0.5
    $ hero_ani_eyeX = 0.2
    $ hero_ani_eyeY = 0.6
    $ hero_ani_mouA = 0

    $ wdis_learn = 0
    $ wdis_focus = 100/(1+(wdis_lust*0.99))
    $ wdis_ani_mouA = 0
    $ wdis_ani_breathe = 0
    $ wdis_ani_breathing = 0
    $ wdis_ani_masturbate = 0
    $ wdis_ani_masturbating = 0
    $ wdis_ani_write = 0
    $ wdis_ani_writing = 0
    $ wdis_ani_cum = 0
    $ wdis_ani_eyeX = 0.8
    $ wdis_ani_eyeY = 0.4

    scene action_tutor_study2_bg library
    show ANI_WDIS_Tutor breathe
    show ANI_HERO_Tutor breathe
    show action_tutor_study2_fg library
    show action_tutor_study2_fx:
        blend "add"
    show action_tutor_study2_mg library
    show screen tutoring_pose_wdis
    show screen tutoring_pose_hero
    show screen tutoring_UI
    with dissolve

    jump action_tutoring_check

# ----------------------------------------------------------------------------------------------------
label action_tutoring_check:
# ----------------------------------------------------------------------------------------------------
    if gametimesec >= 360:
        jump action_tutoring_end

    #$ ui.interact()
    $ config.allow_skipping = False
    $ config.rollback_enabled = False

    $ check_stat()

    $ hero_ani_hand_XMov = 0
    $ hero_ani_hand_YMov = 1
    $ hero_ani_mouA = 0
    $ hero_ani_eyeX = 0.2
    $ hero_ani_eyeY = 0.6

    $ wdis_ani_mouA = 0
    $ wdis_ani_eyeX = 0.8
    $ wdis_ani_eyeY = 0.4

    scene action_tutor_study2_bg library
    show ANI_WDIS_Tutor breathe
    show ANI_HERO_Tutor breathe
    show action_tutor_study2_fg library
    show action_tutor_study2_fx:
        blend "add"
    show action_tutor_study2_mg library
    show screen tutoring_pose_wdis
    show screen tutoring_pose_hero
    show screen tutoring_UI
    show screen disable_click

    $ renpy.pause(hard=True)
    jump action_tutoring_end
