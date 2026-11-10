init python:
    def _hold_bar_tick(bar_current, is_holding, pla_power, var_bam):
        if is_holding:
            return min(float(var_bam), bar_current + pla_power * 3.0)
        else:
            return max(0.0, bar_current - pla_power * 3.0)

    def _hold_classic_score(bar_current, mark_pos, zero_dist, score):
        distance = abs(bar_current - mark_pos)
        ratio = min(distance / max(1.0, zero_dist), 2.0)
        delta = (1.0 - ratio) * 0.015
        return max(0.0, min(1.0, score + delta))

    def _hold_timed_score(bar_current, mark_pos, zero_dist):
        distance = abs(bar_current - mark_pos)
        ratio = min(distance / max(1.0, zero_dist), 1.0)
        return max(0.0, (1.0 - ratio) ** 2)

    def _hold_range_time(bar_current, mark_pos, var_rng, hold_time):
        if abs(bar_current - mark_pos) <= var_rng:
            return hold_time + 0.15
        return max(0.0, hold_time - 0.30)

    def _hold_new_mark(mrk):
        if isinstance(mrk, tuple):
            return renpy.random.randint(mrk[0], mrk[1])
        return mrk

    def _hold_mark_pos(mark_pos, mark_vel, mark_speed, var_bam, var_rng):
        lo = float(var_rng)
        hi = float(var_bam) - var_rng
        return max(lo, min(hi, mark_pos + mark_vel * mark_speed))

    def _hold_mark_vel(mark_pos, mark_vel, mark_speed, var_bam, var_rng):
        new_pos = mark_pos + mark_vel * mark_speed
        if new_pos <= var_rng:
            return 1
        if new_pos >= var_bam - var_rng:
            return -1
        return mark_vel

    def _hold_maybe_flip_vel(bar_current, mark_pos, var_rng, mark_vel):
        if abs(bar_current - mark_pos) <= var_rng and renpy.random.random() < 0.5:
            return -mark_vel
        return mark_vel

#---------------------------------------------------------------------------
screen minigame_balance(var_pla=1, var_npc=1, var_bao=50, var_bam=100, var_axi=50, var_tio=0, var_tim=None, var_txt=None, var_mod="classic", var_sco=0, var_sca=0.2, var_rng=15, var_hol=3.0, var_zer=None):
#---------------------------------------------------------------------------
    # Initialize screen variables
    default bar_current = var_bao * 1.0
    default timer_current = var_tio
    default game_started = False
    default is_holding = False
    default pla_power = var_pla * 1.0
    default hold_time = 0.0
    default score = (var_sco if var_mod == "continuous" else 0.5)
    default mark_pos = _hold_new_mark(var_axi) * 1.0
    default mark_vel = renpy.random.choice([-1, 1])
    default mark_speed = var_npc * 1.5
    default zero_dist = (var_zer if var_zer is not None else var_bam * 0.25)

    # Auto-set timer for continuous mode
    default effective_tim = (15.1 if (var_mod == "continuous" and var_tim is None) else var_tim)

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
                label renpy.translate_string("{size=+80}{b}Balance{/b}{/size}") xalign 0.5
                vbox:
                    xalign 0.5
                    xysize (960, 400)
                    if var_txt == None:
                        if var_mod == "continuous":
                            text renpy.translate_string("{size=+10}Hold the screen to keep the bar at the mark. Keep it steady to score points! The control gets harder each time you score.{/size}") xalign 0.5
                        elif effective_tim == None:
                            text renpy.translate_string("{size=+10}Hold the screen to move the bar toward the mark. Keep it close to win, but drift too far and you lose!{/size}") xalign 0.5
                        else:
                            text renpy.translate_string("{size=+10}Hold the screen to move the bar toward the mark. Keep it as close as possible when time runs out!{/size}") xalign 0.5
                    else:
                        text renpy.translate_string("{size=+10}[var_txt]{/size}") xalign 0.5
                text renpy.translate_string("[C_Dat]{size=+40}{b}Click to start!{/b}[C_Off]") xalign 0.5

        key "mousedown_1" action SetScreenVariable("game_started", True)

    # --------------------------------------------------
    # Game Started
    # --------------------------------------------------
    else:
        # --------------------------------------------------
        # Timer (if enabled)
        # --------------------------------------------------
        if effective_tim != None:
            timer 1 repeat True action [
                If(timer_current < effective_tim,
                    true=(SetScreenVariable("timer_current", timer_current + 1)),
                    false=(Return(score) if var_mod == "continuous" else Return(_hold_timed_score(bar_current, mark_pos, zero_dist))),
                )
            ]

        # --------------------------------------------------
        # Random direction flip (each second player is inside the mark)
        # --------------------------------------------------
        timer 1 repeat True action SetScreenVariable("mark_vel", _hold_maybe_flip_vel(bar_current, mark_pos, var_rng, mark_vel))

        # --------------------------------------------------
        # Bar Movement + Scoring
        # --------------------------------------------------
        timer 0.1 repeat True action [
            # Move bar based on hold state
            SetScreenVariable("bar_current", _hold_bar_tick(bar_current, is_holding, pla_power, var_bam)),

            # Move mark (bouncing at edges, respecting mark half-width)
            SetScreenVariable("mark_vel", _hold_mark_vel(mark_pos, mark_vel, mark_speed, var_bam, var_rng)),
            SetScreenVariable("mark_pos", _hold_mark_pos(mark_pos, mark_vel, mark_speed, var_bam, var_rng)),

            # Classic untimed: update score, check win/lose
            If(var_mod == "classic" and effective_tim == None, true=[
                SetScreenVariable("score", _hold_classic_score(bar_current, mark_pos, zero_dist, score)),
                If(score <= 0.0, Return(0)),
                If(score >= 1.0, Return(1)),
            ]),

            # Continuous: track time in range, score when held enough
            If(var_mod == "continuous", true=[
                SetScreenVariable("hold_time", _hold_range_time(bar_current, mark_pos, var_rng, hold_time)),
                If(hold_time >= var_hol, [
                    Play("SE2", "JingleRight.ogg"),
                    SetScreenVariable("score", score + 1),
                    SetScreenVariable("mark_speed", mark_speed * (1.0 + var_sca)),
                    SetScreenVariable("pla_power", pla_power * (1.0 + var_sca)),
                    SetScreenVariable("hold_time", 0.0),
                ]),
            ]),
        ]

        # Hold input
        key "mousedown_1" action SetScreenVariable("is_holding", True)
        key "mouseup_1" action SetScreenVariable("is_holding", False)

    # --------------------------------------------------
    # UI Display
    # --------------------------------------------------
    vbox:
        spacing 10
        xalign 0.5
        yalign 0.9

        # Player bar with mark overlay
        fixed:
            xsize 1000
            ysize 36
            xalign 0.5
            bar value bar_current range var_bam xmaximum 1000 yalign 0.5
            # Range zone (continuous mode)
            if var_mod == "continuous":
                frame:
                    background "#FFFFFF30"
                    xsize int(1000.0 * var_rng * 2.0 / var_bam)
                    ysize 36
                    anchor (0.5, 0.5)
                    xpos int(1000.0 * mark_pos / var_bam)
                    yalign 0.5
            # Mark line
            frame:
                background "#000000"
                xsize 5
                ysize 35
                anchor (0.5, 0.5)
                xpos int(1000.0 * mark_pos / var_bam)
                yalign 0.5

        # Score bar (classic untimed)
        if var_mod == "classic" and effective_tim == None:
            bar value score range 1.0 xmaximum 1000

        # Hold time progress (continuous)
        if var_mod == "continuous":
            bar value hold_time range var_hol xmaximum 1000

        # Timer bar
        if effective_tim != None:
            bar value timer_current range effective_tim xmaximum 1000

        # Score display (continuous)
        if var_mod == "continuous":
            text renpy.translate_string("{size=+20}{b}Score: [score]{/b}{/size}") xalign 0.5

    modal True
