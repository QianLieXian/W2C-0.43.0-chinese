# ---------------------------------------------------------------------------
# Coverage minigame — fill a 2x3 grid of regions by steering two 0..1 drivers.
# Generic: the caller supplies the art, the drivers and the labels. Useful for
# any "work the whole surface" task (scrubbing, painting, sanding, polishing).
# ---------------------------------------------------------------------------

define COVER_KEYS = ["top_left", "top_right", "mid_left", "mid_right", "bottom_left", "bottom_right"]
define COVER_NAMES = ["Top L", "Top R", "Mid L", "Mid R", "Low L", "Low R"]

# Per-region fill 0..100, kept on the store so callers can read it after Return()
default minigame_cover = [0.0] * 6

init python:

    def cover_weights(hx, vy):
        # hx: 0.0 = right .. 1.0 = left | vy: 0.0 = top .. 1.0 = bottom
        # Columns split linearly, rows split as three triangular bands centred
        # on 0.0 / 0.5 / 1.0, so the six weights always sum to exactly 1.0.
        hx = max(0.0, min(1.0, hx))
        vy = max(0.0, min(1.0, vy))
        w_left = hx
        w_right = 1.0 - hx
        w_top = max(0.0, 1.0 - vy * 2.0)
        w_mid = 1.0 - abs(vy - 0.5) * 2.0
        w_low = max(0.0, vy * 2.0 - 1.0)
        return [w_top * w_left, w_top * w_right,
                w_mid * w_left, w_mid * w_right,
                w_low * w_left, w_low * w_right]

    def cover_read(src, fallback=0.0):
        # A driver is a store variable name, a plain number, or None (mouse).
        if src is None:
            return None
        if isinstance(src, str):
            return float(getattr(renpy.store, src, fallback))
        return float(src)

    def cover_mouse_drivers():
        # Right edge -> hx 0.0, left edge -> hx 1.0 | top -> vy 0.0, bottom -> vy 1.0
        mx, my = renpy.get_mouse_pos()
        w, h = config.screen_width, config.screen_height
        hx = 1.0 - (float(mx) / max(1, w))
        vy = float(my) / max(1, h)
        return (hx, vy)

    def cover_tick(cps, hx_src, vy_src, dt):
        hx = cover_read(hx_src)
        vy = cover_read(vy_src)
        if hx is None or vy is None:
            m_hx, m_vy = cover_mouse_drivers()
            hx = m_hx if hx is None else hx
            vy = m_vy if vy is None else vy

        weights = cover_weights(hx, vy)
        gain = cps * dt
        # Rebind rather than mutate so the screen sees the change and redraws
        renpy.store.minigame_cover = [
            min(100.0, p + w * gain) for p, w in zip(minigame_cover, weights)
        ]

    def cover_labels(names):
        # Accepts a list (short lists fall back per slot), a dict keyed by
        # COVER_KEYS, or None for the built-in defaults.
        if not names:
            return list(COVER_NAMES)
        if isinstance(names, dict):
            return [str(names.get(k, d)) for k, d in zip(COVER_KEYS, COVER_NAMES)]
        given = [str(n) for n in list(names)[:6]]
        return given + list(COVER_NAMES[len(given):])

    def cover_done(goal):
        return all(p >= goal for p in minigame_cover)

    def cover_average():
        return sum(minigame_cover) / 6.0

# ---------------------------------------------------------------------------
screen coverage_bars(var_names=None, xsize_bar=360, ysize_bar=34, spacing_bar=6):
# ---------------------------------------------------------------------------
    # Thick bars with the label drawn over the fill, so text costs no width.
    $ labels = cover_labels(var_names)

    vbox:
        spacing spacing_bar
        for i, name in enumerate(labels):
            fixed:
                xysize (xsize_bar, ysize_bar)
                bar:
                    value StaticValue(minigame_cover[i], 100)
                    xysize (xsize_bar, ysize_bar)
                    align (0.5, 0.5)
                text renpy.translate_string("[name] ") + str(int(minigame_cover[i])) + "%":
                    align (0.5, 0.5)
                    size 20
                    outlines [(2, "#000000", 0, 0)]

# ---------------------------------------------------------------------------
screen minigame_coverage(var_cps=25.0, var_hx=None, var_vy=None, var_goal=100, var_tim=None, var_var=None, var_ttl="Clean", var_txt=None, var_names=None, var_bars=True, var_pos=(0.0, 0.0)):
# ---------------------------------------------------------------------------
    # var_cps  : max % gained per second by a single region (balance knob)
    # var_hx   : store variable name / number for the 0..1 horizontal driver, None = mouse
    # var_vy   : store variable name / number for the 0..1 vertical driver, None = mouse
    # var_names: 6-item list or dict keyed by COVER_KEYS, None = COVER_NAMES
    # var_goal : % every region must reach before the game returns
    # var_tim  : optional time limit in seconds, None = untimed
    default game_started = False
    default timer_current = 0

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
                label renpy.translate_string("{size=+80}{b}[var_ttl]{/b}{/size}") xalign 0.5
                vbox:
                    xalign 0.5
                    xysize (960, 400)
                    if var_txt == None:
                        text renpy.translate_string("{size=+10}Move the cursor over every area until each bar is full.{/size}") xalign 0.5
                    else:
                        text renpy.translate_string("{size=+10}[var_txt]{/size}") xalign 0.5
                text renpy.translate_string("[C_Dat]{size=+40}{b}Click to start!{/b}[C_Off]") xalign 0.5

        key "mousedown_1" action [
            SetVariable("minigame_cover", [0.0] * 6),
            If(var_var != None, SetVariable(var_var, True)),
            SetScreenVariable("game_started", True),
            ]

    # --------------------------------------------------
    # Game Started
    # --------------------------------------------------
    else:

        timer 0.05 repeat True action Function(cover_tick, var_cps, var_hx, var_vy, 0.05)

        if cover_done(var_goal):
            timer 0.01 action Return(cover_average())

        if var_tim != None:
            timer 1 repeat True action [
                If(timer_current < var_tim,
                    true=SetScreenVariable("timer_current", timer_current + 1),
                    false=Return(cover_average()))]

            bar:
                value timer_current
                range var_tim
                xmaximum 1000
                xalign 0.5
                yalign 0.05

        if var_bars:
            fixed:
                fit_first True
                align var_pos
                use coverage_bars(var_names)

        #textbutton "Done" align (0.5, 1.0) action Return(cover_average())

# ---------------------------------------------------------------------------
label coverage_preview: # Balance/test harness — mouse-driven, no scene needed
# ---------------------------------------------------------------------------

    call screen minigame_coverage(var_cps=25.0, var_ttl="Clean", var_txt="Move the cursor to clean " +str(C_Nam) + str(fnamewsis) + str(C_Off), var_tim=None)

    $ a_event_0 = _return

    "Average coverage: [a_event_0]"

    return
