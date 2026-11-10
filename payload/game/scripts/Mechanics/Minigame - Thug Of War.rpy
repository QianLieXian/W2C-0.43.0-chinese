#---------------------------------------------------------------------------
screen get_texticulo(texticulo):
#---------------------------------------------------------------------------
    text texticulo xalign 0.5 yalign 0.5

    modal True
    key "mousedown_1" action Return()

#---------------------------------------------------------------------------
screen minigame_thugofwar_1():
#---------------------------------------------------------------------------
    timer 0.15 repeat True action [
        If(var_bao>0,
            true=([Stop("SE2"), Play("SE2", "ButtonCLICK.ogg"), SetVariable("var_bao", var_bao - (var_npc * 3))]),
            false=(Return("Lose")),
            ),
        If(var_bao>=var_bam, Return("Win")),
    ]

    bar value VariableValue("var_bao", 50) xmaximum 1000 xalign 0.5 yalign 0.9

    modal True
    key "mousedown_1" action [Stop("SE1"), Play("SE1", "ButtonCLICK.ogg"), SetVariable("var_bao", var_bao + (var_pla * 5))]

#---------------------------------------------------------------------------
screen minigame_thugofwar_2():
#---------------------------------------------------------------------------
    timer 1 repeat True action [
        If(var_tio < var_tim,
            true=(SetVariable("var_tio", var_tio+1)),
            false=(Return("TimeUp")),
            )
    ]
    timer 0.15 repeat True action [
        If(var_bao>0,
            true=([Stop("SE2"), Play("SE2", "ButtonCLICK.ogg"), SetVariable("var_bao", var_bao - (var_npc * 3))]),
            false=(Return("Lose")),
            ),
        If(var_bao>=var_bam, Return("Win")),
    ]

    vbox:
        spacing 10
        xalign 0.5
        yalign 0.9
        bar value VariableValue("var_bao", 100) xmaximum 1000
        bar value VariableValue("var_tio", var_tim) xmaximum 1000

    modal True
    key "mousedown_1" action [Stop("SE1"), Play("SE1", "ButtonCLICK.ogg"), SetVariable("var_bao", var_bao + (var_pla * 5))]

#---------------------------------------------------------------------------
screen minigame_thugofwar(var_pla=1, var_npc=1, var_bao=50, var_bam=100, var_tio=0, var_tim=None, var_txt=None, var_mod="classic", var_sco=0, var_sca=0.1):
#---------------------------------------------------------------------------
    # Initialize screen variables
    default bar_current = var_bao
    default timer_current = var_tio
    default game_started = False
    default score = var_sco
    default npc_power = var_npc * 1.0
    default input_disabled = False
    default reset_step = 0.0

    # Auto-set timer for continuous mode
    default effective_tim = (150 if (var_mod == "continuous" and var_tim is None) else var_tim)

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
                label renpy.translate_string("{size=+80}{b}Thug of War{/b}{/size}") xalign 0.5
                vbox:
                    xalign 0.5
                    xysize (960, 400)
                    if var_txt == None:
                        if var_mod == "continuous":
                            text renpy.translate_string("{size=+10}Rapidly tap the screen to fill the bar as many times as you can! Each time the bar fills, the resistance gets stronger. Survive until time runs out!{/size}") xalign 0.5
                        elif effective_tim == None:
                            text renpy.translate_string("{size=+10}Rapidly tap the screen to fill the bar forward before the resistance force pushes you back.{/size}") xalign 0.5
                        else:
                            text renpy.translate_string("{size=+10}Rapidly tap the screen to fill the bar forward before the resistance force pushes you back. If the bottom bar fills before you fill the top bar, time runs out.{/size}") xalign 0.5
                    else:
                        text renpy.translate_string("{size=+10}[var_txt]{/size}") xalign 0.5
                text renpy.translate_string("[C_Dat]{size=+40}{b}Click to start!{/b}[C_Off]") xalign 0.5

        key "mousedown_1" action SetScreenVariable("game_started", True)

    # --------------------------------------------------
    # Game Started
    # --------------------------------------------------
    else:
        # --------------------------------------------------
        # Timer (if enabled). Paused during the bar-reset animation so
        # the player isn't charged time for moments they can't act.
        # --------------------------------------------------
        if effective_tim != None and not input_disabled:
            timer 0.1 repeat True action [
                If(timer_current < effective_tim,
                    true=(SetScreenVariable("timer_current", timer_current+1)),
                    false=(Return(score) if var_mod == "continuous" else Return("TimeUp")),
                )
            ]

        # --------------------------------------------------
        # Challenge Force / Reset Animation
        # --------------------------------------------------
        if input_disabled:
            # Continuous mode: gradually reduce bar back to var_bao
            timer 0.15 repeat True action [
                If(bar_current > var_bao,
                    true=(SetScreenVariable("bar_current", max(var_bao, bar_current - reset_step))),
                    false=([SetScreenVariable("bar_current", var_bao), SetScreenVariable("input_disabled", False)]),
                ),
            ]
        else:
            timer 0.15 repeat True action [
                If(bar_current > 0,
                    true=([Stop("SE2"), Play("SE2", "ButtonCLICK.ogg"), SetScreenVariable("bar_current", bar_current - (npc_power * 3))]),
                    false=(NullAction() if var_mod == "continuous" else Return("Lose")),
                ),
                If(bar_current >= var_bam,
                    ([  Play("SE2", "JingleRight.ogg"),
                        SetScreenVariable("score", score + 1),
                        SetScreenVariable("npc_power", npc_power * (1.0 + var_sca)),
                        SetScreenVariable("reset_step", (var_bam - var_bao) / max(1.0, var_tio / 0.15)),
                        SetScreenVariable("input_disabled", True),
                    ]) if var_mod == "continuous" else Return("Win")
                ),
            ]

            key "mousedown_1" action [Stop("SE1"), Play("SE1", "ButtonCLICK.ogg"), SetScreenVariable("bar_current", bar_current + (var_pla * 5))]

    # --------------------------------------------------
    # UI Display
    # --------------------------------------------------
    vbox:
        spacing 10
        xalign 0.5
        yalign 0.9
        bar value bar_current range var_bam xmaximum 1000
        if effective_tim != None:
            bar value timer_current range effective_tim xmaximum 1000
        if var_mod == "continuous":
            text renpy.translate_string("{size=+20}{b}Score: [score]{/b}{/size}") xalign 0.5

    modal True
