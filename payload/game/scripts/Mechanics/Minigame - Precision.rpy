init python:
    def _precision_new_pos(arrow_pos, arrow_dir, var_pla, var_bam):
        new_pos = arrow_pos + arrow_dir * var_pla * 20.0
        if new_pos >= var_bam:
            return float(var_bam)
        if new_pos <= 0:
            return 0.0
        return new_pos

    def _precision_new_dir(arrow_pos, arrow_dir, var_pla, var_bam):
        new_pos = arrow_pos + arrow_dir * var_pla * 20.0
        if new_pos >= var_bam:
            return -1
        if new_pos <= 0:
            return 1
        return arrow_dir

    def _precision_zone(arrow_pos, var_bam, var_grn, var_yel, var_org):
        center = var_bam / 2.0
        dist = abs(arrow_pos - center)
        if dist <= var_grn / 2.0:
            return 3
        if dist <= var_yel / 2.0:
            return 2
        if dist <= var_org / 2.0:
            return 1
        return 0

#---------------------------------------------------------------------------
screen minigame_precision(var_pla=1, var_npc=1, var_bao=500, var_bam=1000, var_tio=0, var_tim=None, var_txt=None, var_mod="classic", var_sco=0, var_sca=0.2, var_grn=80, var_yel=200, var_org=400):
#---------------------------------------------------------------------------
    default arrow_pos = var_bao * 1.0
    default arrow_dir = renpy.random.choice([-1, 1])
    default timer_current = var_tio
    default game_started = False
    default score = (var_sco if var_mod == "continuous" else 0)
    default pla_power = var_pla * 1.0

    modal True

    # --------------------------------------------------
    # Preparation Screen
    # --------------------------------------------------
    if not game_started:
        frame:
            background "#000000C8"
            xysize (1920, 1080)
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                label renpy.translate_string("{size=+80}{b}Precision{/b}{/size}") xalign 0.5
                vbox:
                    xalign 0.5
                    xysize (960, 400)
                    if var_txt == None:
                        if var_mod == "continuous":
                            text renpy.translate_string("{size=+10}Click when the arrow lines up with a colored zone. The green center scores the most. Each click makes the arrow faster!{/size}") xalign 0.5
                        else:
                            text renpy.translate_string("{size=+10}Click when the arrow lines up with a colored zone. Aim for the green center for the best result.{/size}") xalign 0.5
                    else:
                        text renpy.translate_string("{size=+10}[var_txt]{/size}") xalign 0.5
                text renpy.translate_string("[C_Dat]{size=+40}{b}Click to start!{/b}[C_Off]") xalign 0.5

        key "mousedown_1" action SetScreenVariable("game_started", True)

    # --------------------------------------------------
    # Game Started
    # --------------------------------------------------
    else:
        # Timer (if enabled)
        if var_tim != None:
            timer 1 repeat True action [
                If(timer_current < var_tim,
                    true=SetScreenVariable("timer_current", timer_current + 1),
                    false=(Return(score) if var_mod == "continuous" else Return(0)),
                )
            ]

        # Arrow movement
        timer 0.01 repeat True action [
            SetScreenVariable("arrow_dir", _precision_new_dir(arrow_pos, arrow_dir, pla_power, var_bam)),
            SetScreenVariable("arrow_pos", _precision_new_pos(arrow_pos, arrow_dir, pla_power, var_bam)),
        ]

        # Click resolution: classic returns 0/1/2/3, continuous adds to score
        if var_mod == "continuous":
            key "mousedown_1" action [
                If(_precision_zone(arrow_pos, var_bam, var_grn, var_yel, var_org) == 3,
                    [Function(msg.msg, "[C_Pos]Perfect Answer[C_Off]"), Play("SE1", "BeepRight.ogg"), SetScreenVariable("score", score + 3), SetScreenVariable("pla_power", pla_power * (1.0 + var_sca))],
                    If(_precision_zone(arrow_pos, var_bam, var_grn, var_yel, var_org) == 2,
                        [Function(msg.msg, "[C_Pos]Good Answer[C_Off]"), Play("SE1", "BeepRight.ogg"), SetScreenVariable("score", score + 2), SetScreenVariable("pla_power", pla_power * (1.0 + var_sca))],
                        If(_precision_zone(arrow_pos, var_bam, var_grn, var_yel, var_org) == 1,
                            [Function(msg.msg, "[C_Neg]Neutral Answer[C_Off]"), Play("SE1", "BeepWrong.ogg"), SetScreenVariable("score", score + 1), SetScreenVariable("pla_power", pla_power * (1.0 + var_sca))],
                            [Function(msg.msg, "[C_Neg]Bad Answer[C_Off]"), Play("SE1", "BeepWrong.ogg"), SetScreenVariable("pla_power", pla_power * (1.0 + var_sca))]
                        )
                    )
                )
            ]
        else:
            key "mousedown_1" action [
                If(_precision_zone(arrow_pos, var_bam, var_grn, var_yel, var_org) == 3,
                    [Function(msg.msg, "[C_Pos]Perfect Answer[C_Off]"), Play("SE1", "BeepRight.ogg"), Return(3)],
                    If(_precision_zone(arrow_pos, var_bam, var_grn, var_yel, var_org) == 2,
                        [Function(msg.msg, "[C_Pos]Good Answer[C_Off]"), Play("SE1", "BeepRight.ogg"), Return(2)],
                        If(_precision_zone(arrow_pos, var_bam, var_grn, var_yel, var_org) == 1,
                            [Function(msg.msg, "[C_Neg]Neutral Answer[C_Off]"), Play("SE1", "BeepWrong.ogg"), Return(1)],
                            [Function(msg.msg, "[C_Neg]Bad Answer[C_Off]"), Play("SE1", "BeepWrong.ogg"), Return(0)]
                        )
                    )
                )
            ]

    # --------------------------------------------------
    # UI Display
    # --------------------------------------------------
    fixed:
        xsize 1920
        ysize 1080

        # Red bar (full width)
        frame:
            background "#FF0000"
            xsize var_bam
            ysize 50
            xalign 0.5
            yalign 0.5

        # Orange zone
        frame:
            background "#FFA900"
            xsize var_org
            ysize 50
            xalign 0.5
            yalign 0.5

        # Yellow zone
        frame:
            background "#FFFF00"
            xsize var_yel
            ysize 50
            xalign 0.5
            yalign 0.5

        # Green zone
        frame:
            background "#00FF00"
            xsize var_grn
            ysize 50
            xalign 0.5
            yalign 0.5

        # Moving arrow
        $ bar_left = (1920 - var_bam) // 2
        add "images/UI/Arrow_2 IDLE.webp":
            xpos int(bar_left + arrow_pos)
            yalign 0.45
            anchor (0.5, 0.5)

        # Timer bar (if enabled)
        if var_tim != None:
            bar:
                value timer_current
                range var_tim
                xmaximum 1000
                xalign 0.5
                yalign 0.6

        # Score display (continuous)
        if var_mod == "continuous":
            text renpy.translate_string("{size=+20}{b}Score: [score]{/b}{/size}") xalign 0.5 yalign 0.65
