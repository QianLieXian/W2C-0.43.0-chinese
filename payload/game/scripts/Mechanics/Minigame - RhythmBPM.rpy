# ----------
# RHYTHM (BPM) - BPM-synced rebuild of the Dance minigame
# ----------
# Notes travel right-to-left and land on the hit line exactly on the beat. Every position comes from ONE playhead (see RhythmConductor), so frame rate changes only smoothness — never speed or spacing. Runs alongside the old top-to-bottom `dance_screen` during the A/B test phase; nothing here is shared.


# ----------
# TUNABLES
# ----------
define DANCE_LEAD_IN = 2.0              # minimum silent fly-in before the music starts, seconds
define DANCE_SPEED = 425                # note travel, pixels/second (~3.8s of read time)
# Hit windows, seconds off the beat. Both widen with the Performance perk (`perk_cha_per`, 0-3):
#   window = base * (1 + perk_cha_per * DANCE_PERK_WINDOW)
# At DANCE_PERK_WINDOW = 0.25 a maxed perk is +75%: perfect 0.020 -> 0.035, good 0.090 -> 0.158.
define DANCE_PERFECT = 0.02             # very tight — near the exact beat
define DANCE_GOOD = 0.09                # medium
define DANCE_PERK_WINDOW = 0.25         # how much each perk level widens both windows
define DANCE_TAIL = 1.5                 # grace after the last note before the screen ends
define DANCE_TAP_DEBOUNCE = 0.1         # a same-lane re-press inside this window is a touch ghost tap: ignored
define DANCE_MISS_MERGE = 0.6           # a note dropping this soon after a whiffed tap is the SAME mistake, not a second one
define DANCE_SYNC_RATE = 0.05           # how hard each audio-clock tick pulls the frame clock
define DANCE_SYNC_SNAP = 0.25           # error above this (seconds) snaps instead of nudging

define DANCE_HIT_X = 300                # hit line; notes spawn off the right edge
define DANCE_LANE_Y = 330               # top of the single lane (PC)
define DANCE_LANE_Y_MOBILE = 160        # top of the 4-lane stack (mobile)
define DANCE_ARROW_H = 96               # arrow sprite height (32px sheet at zoom 3)
define DANCE_LANE_PAD = 5               # breathing room above/below the arrow inside its lane
define DANCE_LANE_H = DANCE_ARROW_H + DANCE_LANE_PAD * 2
define DANCE_LANE_GAP = 6               # space between stacked lanes (4-lane mode)
define DANCE_LANES = ["w", "d", "s", "a"]   # the four keys a note can call for

# The phone is held UPRIGHT, so the widescreen is physically rotated: a lane's height here is a column's width under the player's thumb. Hence the fatter touch lanes — 106px is not a thumb.
define DANCE_TOUCH_SCALE = 2            # lane thickness multiplier in 4-lane (touch) mode

# Layout: PC gets ONE lane (keyboard picks the key, so lanes would be redundant), mobile gets FOUR (tap the lane itself — no keypad to cover the screen). "auto" | "one" | "four".
define DANCE_LANE_MODE = "auto"

define DANCE_DANCER_ZOOM = 1.0          # relative to the pre-scaled 540px frames (= half the 1080px art)
define DANCE_DANCER_LIFT = 100          # gap from the bottom edge, pixels
define DANCE_DANCER_X = 0.15            # left dancer's centre; the right one mirrors it
# Player toggle: preferences.dancers (script.rpy, Settings › Performance) removes both dancers.


# ----------
# SONG DATA
# ----------
# Static and never mutated -> `define` (renpy-builder §1), so new songs reach old saves. `bpm`/`start_offset`/`chart` were measured from the audio by `tools/rhythm_chart.py`; re-tune any of them in the in-engine recorder below (is_test).
#
    # Fields
        # 1. title        - menu label
        # 2. file         - audio path, played noloop by the conductor
        # 3. bpm          - beats per minute; converts the beat-authored chart to seconds
        # 4. start_offset - seconds before the first usable downbeat in the file
        # 5. length       - song length in seconds, drives the progress bar
        # 6. anim_step    - dance-frame pacing (`minigamestep`); one 8-frame loop = 2 beats
        # 7. chart        - (beat, lane) note list; lane in w/d/s/a

define Dance_Songs = {
    "sunrise": {
        "title": "Sunrise Serenade",
        "file": "audio/Dance - Sunrise Serenade.mp3",
        "bpm": 100,
        "start_offset": 0.462,
        "length": 104.9,
        "anim_step": 0.15,
        "chart": [
            (1, "d"), (2.5, "w"), (5, "d"), (6.5, "w"), (8, "d"), (9, "s"), (10.5, "d"), (12, "s"),
            (12.5, "d"), (13, "a"), (16, "w"), (16.5, "d"), (17, "s"), (18.5, "w"), (19, "d"), (21, "s"),
            (24.5, "d"), (25, "s"), (26, "d"), (26.5, "w"), (27, "a"), (28.5, "w"), (29, "d"), (33, "w"),
            (34, "a"), (35, "w"), (36, "a"), (36.5, "w"), (37, "d"), (38, "a"), (39, "d"), (40.5, "a"),
            (41.5, "w"), (42, "d"), (42.5, "w"), (49, "a"), (51, "s"), (57, "a"), (58, "s"), (59, "a"),
            (61, "s"), (62, "a"), (63, "d"), (64.5, "a"), (65, "d"), (67, "s"), (68, "a"), (69, "d"),
            (70, "a"), (71, "d"), (72.5, "s"), (73.5, "a"), (75, "d"), (75.5, "a"), (77, "s"), (78, "a"),
            (80, "s"), (81, "a"), (83, "s"), (84, "a"), (85, "s"), (89, "a"), (90.5, "w"), (93, "s"),
            (94.5, "w"), (97, "d"), (98, "s"), (99, "a"), (101, "d"), (102, "s"), (103, "w"), (104, "a"),
            (105, "d"), (107, "s"), (108, "a"), (109, "d"), (110, "a"), (111, "d"), (112, "s"), (112.5, "w"),
            (113, "d"), (115, "w"), (116, "a"), (117, "d"), (118, "a"), (119, "w"), (119.5, "d"), (120, "a"),
            (120.5, "s"), (122.5, "w"), (123, "d"), (131, "w"), (137, "a"), (138.5, "w"), (139, "s"), (140, "a"),
            (140.5, "w"), (141, "s"), (142, "a"), (143, "d"), (144.5, "w"), (147, "s"), (148, "a"), (149, "s"),
            (150, "a"), (151, "d"), (152.5, "w"), (155, "s"), (157, "d"), (158, "a"), (159, "s"), (160, "a"),
            (161, "d"), (163, "s"), (164, "a"), (165, "s"), (169, "a"), (169.5, "s"), (170.5, "d"), (171, "s"),
            (171.5, "d"), (172, "s"),
        ],
    },

    "bubblegum": {
        "title": "Bubblegum Skies",
        "file": "audio/Dance - Bubblegum Skies.mp3",
        "bpm": 128,
        "start_offset": 0.352,
        "length": 116.1,
        "anim_step": 0.117,
        "chart": [
            (0, "s"), (1, "w"), (2.5, "d"), (3.5, "w"), (5, "d"), (6.5, "w"), (10.5, "d"), (11.5, "s"),
            (17, "a"), (17.5, "s"), (18.5, "d"), (20.5, "s"), (21, "a"), (22, "s"), (22.5, "d"), (24, "w"),
            (25, "s"), (26, "w"), (26.5, "d"), (28.5, "s"), (29, "a"), (30.5, "s"), (31.5, "a"), (33, "s"),
            (34.5, "d"), (37, "s"), (38, "d"), (38.5, "s"), (40, "w"), (40.5, "d"), (41, "s"), (42.5, "d"),
            (45, "w"), (45.5, "d"), (49, "s"), (51.5, "w"), (53, "d"), (55.5, "w"), (57, "d"), (58, "w"),
            (60, "s"), (62, "a"), (62.5, "s"), (63, "a"), (65, "d"), (66, "a"), (68, "s"), (69.5, "d"),
            (70, "a"), (71, "s"), (74, "d"), (75, "s"), (76, "a"), (77.5, "w"), (78, "d"), (79, "a"),
            (82, "s"), (84, "a"), (85, "s"), (89, "a"), (89.5, "d"), (90, "w"), (90.5, "s"), (93, "d"),
            (94.5, "a"), (96, "w"), (97, "s"), (97.5, "w"), (98.5, "a"), (101, "s"), (102.5, "a"), (103.5, "s"),
            (105, "a"), (106.5, "s"), (109, "a"), (110, "s"), (110.5, "a"), (112.5, "d"), (113, "s"), (114.5, "w"),
            (116, "d"), (117, "a"), (124, "d"), (125, "w"), (127.5, "d"), (128, "w"), (129, "d"), (130, "s"),
            (130.5, "d"), (131, "s"), (132, "a"), (135, "s"), (136, "a"), (140, "d"), (141.5, "w"), (143, "a"),
            (144, "s"), (145, "a"), (146, "d"), (147, "s"), (148, "w"), (149, "d"), (150, "w"), (150.5, "d"),
            (151, "a"), (153, "w"), (156, "s"), (156.5, "d"), (160, "w"), (161, "s"), (161.5, "w"), (163.5, "d"),
            (166.5, "w"), (172.5, "d"), (177, "a"), (178, "w"), (179, "s"), (180, "a"), (180.5, "w"), (181, "d"),
            (182, "s"), (183, "a"), (184, "d"), (185, "s"), (186, "a"), (188, "s"), (189, "a"), (189.5, "s"),
            (191, "a"), (191.5, "s"), (192.5, "a"), (193, "s"), (196, "w"), (197, "d"), (198.5, "s"), (199.5, "w"),
            (200, "d"), (200.5, "a"), (201, "d"), (202, "s"), (202.5, "a"), (204, "s"), (211.5, "a"), (212, "s"),
            (213, "d"), (214, "s"), (215, "a"), (217, "w"), (219, "s"), (220, "w"), (221, "d"), (222, "w"),
            (223, "a"), (224, "w"), (225, "a"), (227, "s"), (228, "a"), (229, "s"), (230, "d"), (231, "a"),
            (232, "w"), (233, "s"), (237, "a"), (238, "s"), (239, "a"), (240, "d"), (240.5, "s"),
        ],
    },

    # Unused tracks — measure with `tools/rhythm_chart.py` and chart them to enable:
        # "axe":     Dance - Axé.mp3        (155.8s)
        # "forro":   Dance - Forró.mp3      (101.1s)
        # "cumbia":  Dance - Cumbia.mp3     (104.6s)
        # "popfast": Dance - Pop (FAST).mp3 (104.3s)
        # "popavg":  Dance - Pop (AVERAGE).mp3 (114.6s)
        # "popslow": Dance - Pop (SLOW).mp3 (92.2s)
}


init python:

    def Dance_NoteTimes(song):
        """Resolve a beat-authored chart into (music_time, lane) pairs."""
        beat = 60.0 / song["bpm"]
        return [(song["start_offset"] + b * beat, lane) for b, lane in song["chart"]]

    def Dance_MultiLane():
        """Four lanes on touch devices (the lane IS the button), one on PC (the keyboard is)."""
        if DANCE_LANE_MODE == "four":
            return True
        if DANCE_LANE_MODE == "one":
            return False
        return renpy.variant("mobile")

    def Dance_LaneH(multi):
        return DANCE_LANE_H * (DANCE_TOUCH_SCALE if multi else 1)

    def Dance_LaneY(row, multi):
        top = DANCE_LANE_Y_MOBILE if multi else DANCE_LANE_Y
        return top + row * (Dance_LaneH(multi) + DANCE_LANE_GAP)

    def Dance_DancerFrames(char):
        """Every small (540px) frame a dancer can show — the _DANCE_BPM sets below."""
        c = char.lower()
        names = []
        for s in range(1, 5):
            count = 5 if (c == "hero" and s < 4) else 8
            names += ["%s dance_s_0%d_0%d" % (c, s, f) for f in range(1, count + 1)]
        if c == "hero":
            names += ["hero idle_s", "hero miss_s"]
        return names

    def Dance_AssetNames(chars, dancers):
        """Everything the track screen blits: note/receptor sprites, plus dancer frames if shown."""
        names = ["dance_bpm_arrow %s %s" % (l, c) for l in DANCE_LANES for c in ("beige", "red")]
        names.append("dance_bpm_hit")
        if dancers:
            for ch in chars:
                names += Dance_DancerFrames(ch)
        return names

    def Dance_PredictAssets(*chars):
        """Decode every screen asset during the rules screen, not mid-song (the mobile chop)."""
        for name in Dance_AssetNames(chars, preferences.dancers):
            renpy.start_predict(name)

    def Dance_StopPredictAssets(*chars):
        # Always release the full set — the dancers pref may have flipped since the start call.
        for name in Dance_AssetNames(chars, True):
            renpy.stop_predict(name)

    # ----------
    # CONDUCTOR — owns every note, one clock, one redraw per frame
    # ----------
    class RhythmConductor(renpy.Displayable):

        def __init__(self, song_id, **kwargs):
            super(RhythmConductor, self).__init__(**kwargs)

            self.song = Dance_Songs[song_id]
            self.notes = [
                {"time": t, "lane": lane, "state": "pending"}
                for t, lane in Dance_NoteTimes(self.song)
            ]
            self.last_time = max([n["time"] for n in self.notes] or [0.0])
            first = min([n["time"] for n in self.notes] or [0.0])

            # Lead-in must outlast one note's travel, or an early first note pops in mid-screen instead of flying in from the right edge. Self-adjusting, so new charts can't trip it.
            travel = (1920.0 - DANCE_HIT_X) / DANCE_SPEED
            self.lead_in = max(DANCE_LEAD_IN, travel - first + 0.2)

            self.song_time = -self.lead_in      # master playhead; music starts when it hits 0
            self.started = False                # music playing?
            self.finished = False
            self.st0 = None                     # displayable time at the first render
            self.sync = 0.0                     # frame-clock -> audio-clock correction
            self.last_pos = None                # last DISTINCT get_pos value seen

            # Windows resolved once, at the perk level the player has right now.
            widen = 1.0 + perk_cha_per * DANCE_PERK_WINDOW
            self.w_perfect = DANCE_PERFECT * widen
            self.w_good = DANCE_GOOD * widen

            self.score = 0
            self.bonus = 0                      # perfect streak — the nth in a row pays n
            self.misses = 0                     # miss/wrong streak — the nth in a row costs n
            self.tap_at = {}                    # lane -> last press time, for the ghost-tap debounce
            self.whiff_at = None                # last whiffed press; lets its note drop for free
            self.move = "idle"                  # hero's current dance frame set
            self.move_until = 0.0
            self.popup = None                   # (Text, expiry) floating score, built once per hit

            # HUD drawn by render() so the screen needs no fast restart timer (real CPU on phones).
            # Text objects are rebuilt only when their value changes, then reused frame to frame.
            self.hud, self.hud_key = None, None
            self.fps_img, self.fps_key, self.fps_times = None, None, []
            self.bar_bg = Solid("#00000088", xysize=(1500, 20))
            self.bar_fg = Solid("#ffffffcc", xysize=(1500, 20))

            self.multi = Dance_MultiLane()
            self.rows = len(DANCE_LANES) if self.multi else 1
            self.lane_h = Dance_LaneH(self.multi)
            self.flash = {}                     # row -> (colour, expiry); the lane lights on hit/miss

            # Every drawn element gets its OWN displayable instance, cached once.
            # A shared instance renders to a shared Render, and blitting one Render twice into the same parent collapses it onto the first position (every note would stack up).
            self.bed, self.glow, self.receptor = [], [], []
            for _ in range(self.rows):
                self.bed.append(Solid("#00000055", xysize=(1920, self.lane_h)))
                self.glow.append({c: Solid(Dance_FeedbackColor(c) + "55",
                                           xysize=(1920, self.lane_h))
                                  for c in ("gold", "green", "red")})
                self.receptor.append(Transform("dance_bpm_hit"))

            for n in self.notes:
                n["row"] = DANCE_LANES.index(n["lane"]) if self.multi else 0
                n["img"] = Transform("dance_bpm_arrow %s beige" % n["lane"])
                n["img_missed"] = Transform("dance_bpm_arrow %s red" % n["lane"])

        def row_of(self, lane):
            return DANCE_LANES.index(lane) if self.multi else 0

        # ----------
        # CLOCK
        # ----------
        def clock(self, st):
            """The FRAME clock drives motion; the audio clock only trims slow drift.

            Never drive song_time straight off `renpy.music.get_pos()`. On Android it only
            advances a few times a second, so notes freeze between its ticks and then lurch —
            the two-speed stutter. `st` advances every frame on every device; `self.sync` is a
            slowly-corrected offset that keeps that frame clock married to the audio.
            """
            if self.st0 is None:
                self.st0 = st

            raw = (st - self.st0) - self.lead_in

            if not self.started:
                self.song_time = raw
                if raw >= 0:
                    renpy.music.play(self.song["file"], channel="BGM", loop=False)
                    self.started = True
                return

            # Only correct when the audio clock has actually ticked — a repeated value is stale.
            pos = renpy.music.get_pos(channel="BGM")
            if pos is not None and pos != self.last_pos:
                self.last_pos = pos
                err = pos - (raw + self.sync)
                if abs(err) > DANCE_SYNC_SNAP:
                    self.sync += err                    # way out (a stall/seek): snap
                else:
                    self.sync += err * DANCE_SYNC_RATE  # nudge, invisible per frame

            self.song_time = raw + self.sync

            if self.song_time > self.last_time + DANCE_TAIL:
                self.finished = True

        # ----------
        # SCORING
        # ----------
        def judge(self, note, delta):
            """Right = flat 1. Perfect = the length of the current perfect streak (1, 2, 3, …)."""
            self.misses = 0
            if abs(delta) <= self.w_perfect:
                self.bonus += 1
                self.score += self.bonus
                return "gold", self.bonus
            self.bonus = 0
            self.score += 1
            return "green", 1

        def whiff(self):
            """Miss or wrong key = the length of the current miss streak, negative."""
            self.misses += 1
            self.bonus = 0
            self.score -= self.misses
            return "red", -self.misses

        def press(self, lane):
            """Player hit a lane key: claim the nearest pending note inside the good window."""
            if self.finished:
                return

            # Touch screens can report one tap as two — the phantom press lands within a few frames on the same lane and deepened the miss streak. Silently swallow it.
            last = self.tap_at.get(lane)
            if last is not None and abs(self.song_time - last) < DANCE_TAP_DEBOUNCE:
                return
            self.tap_at[lane] = self.song_time

            best, best_delta = None, None
            for n in self.notes:
                if n["state"] != "pending" or n["lane"] != lane:
                    continue
                delta = n["time"] - self.song_time
                if abs(delta) <= self.w_good and (best_delta is None or abs(delta) < abs(best_delta)):
                    best, best_delta = n, delta

            if best is None:
                color, gain = self.whiff()
                self.whiff_at = self.song_time
                self.move = "miss"
            else:
                best["state"] = "hit"
                color, gain = self.judge(best, best_delta)
                self.move = lane

            self.move_until = self.song_time + self.song["anim_step"] * 8
            self.flash[self.row_of(lane)] = (color, self.song_time + 0.25)
            self.set_popup("+{}".format(gain) if gain > 0 else str(gain), color)

        def drop(self, note):
            """A whiffed tap already paid for the note it was aimed at: without the merge, one
            mistake charged the escalating streak twice (tap -1, then the note drops -2), and the
            second red flash read as a phantom extra click. One wrong tap forgives ONE drop."""
            note["state"] = "missed"
            self.flash[note["row"]] = ("red", self.song_time + 0.25)

            if self.whiff_at is not None and self.song_time - self.whiff_at <= DANCE_MISS_MERGE:
                self.whiff_at = None
                return

            self.whiff()
            self.move = "miss"
            self.move_until = self.song_time + self.song["anim_step"] * 4
            self.set_popup(str(-self.misses), "red")

        def set_popup(self, text, color):
            """One Text per hit — rebuilding it every frame re-runs text layout (slow on phones)."""
            self.popup = (Text(text, size=48, color=Dance_FeedbackColor(color),
                               outlines=[(3, "#000", 0, 0)]),
                          self.song_time + 0.7)

        # ----------
        # RENDER — every note drawn from the playhead, once per frame
        # ----------
        def render(self, width, height, st, at):
            self.clock(st)
            t = self.song_time

            rv = renpy.Render(width, height)

            # Lane beds + receptors. One row on PC, four on touch — same code either way.
            for row in range(self.rows):
                y = Dance_LaneY(row, self.multi)

                flash = self.flash.get(row)
                if flash and t > flash[1]:
                    del self.flash[row]
                    flash = None

                skin = self.glow[row][flash[0]] if flash else self.bed[row]
                rv.blit(renpy.render(skin, width, height, st, at), (0, y))

                mark = renpy.render(self.receptor[row], width, height, st, at)
                mw, mh = mark.get_size()
                rv.blit(mark, (DANCE_HIT_X - mw // 2, y + (self.lane_h - mh) // 2))

            # Notes: x is a pure function of the playhead, so the trajectory never drifts.
            for n in self.notes:
                if n["state"] == "hit":
                    continue
                if n["state"] == "pending" and n["time"] < t - self.w_good:
                    self.drop(n)

                x = DANCE_HIT_X + (n["time"] - t) * DANCE_SPEED
                if x < -160 or x > width + 160:
                    continue

                img = renpy.render(n["img_missed"] if n["state"] == "missed" else n["img"],
                                   width, height, st, at)
                iw, ih = img.get_size()
                rv.blit(img, (int(x - iw // 2),
                              Dance_LaneY(n["row"], self.multi) + (self.lane_h - ih) // 2))

            # Floating hit feedback.
            if self.popup:
                if t > self.popup[1]:
                    self.popup = None
                else:
                    fade = max(0.0, (self.popup[1] - t) / 0.7)
                    img = renpy.render(self.popup[0], width, height, st, at)
                    top = Dance_LaneY(0, self.multi)
                    rv.blit(img, (DANCE_HIT_X - 20, int(top - 70 - (1.0 - fade) * 40)))

            self.render_hud(rv, width, height, st, at, t)

            if self.move != "idle" and t > self.move_until:
                self.move = "idle"

            renpy.redraw(self, 0)
            return rv

        def render_hud(self, rv, width, height, st, at, t):
            """Score/combo/progress, once per frame from cached Texts. This used to be screen
            widgets kept fresh by a 0.1s SetVariable timer — ten full screen re-evaluations per
            second, the second-biggest mobile cost after the dancer textures."""
            big = not self.multi

            if (self.score, self.bonus) != self.hud_key:
                self.hud_key = (self.score, self.bonus)
                self.hud = (
                    Text(str(int(self.score)), size=(100 if big else 80),
                         outlines=[(5, "#000", 0, 0)]),
                    Text("COMBO x{}".format(self.bonus), size=(44 if big else 40),
                         color="#ffd34d", outlines=[(3, "#000", 0, 0)]) if self.bonus >= 3 else None,
                )
            img = renpy.render(self.hud[0], width, height, st, at)
            rv.blit(img, ((width - img.get_size()[0]) // 2, 60 if big else 10))
            if self.hud[1]:
                img = renpy.render(self.hud[1], width, height, st, at)
                rv.blit(img, ((width - img.get_size()[0]) // 2, 170 if big else 100))

            if self.started:
                y = 200 if big else 1040
                rv.blit(renpy.render(self.bar_bg, width, height, st, at), ((width - 1500) // 2, y))
                frac = min(1.0, max(0.0, t) / self.song["length"])
                if frac > 0:
                    fill = renpy.render(self.bar_fg, width, height, st, at)
                    rv.blit(fill.subsurface((0, 0, int(1500 * frac), 20)), ((width - 1500) // 2, y))

            # Live frame rate over the last second, test builds only — evidence for phone tuning.
            if is_test:
                self.fps_times = [x for x in self.fps_times if x > st - 1.0] + [st]
                fps = len(self.fps_times)
                if fps != self.fps_key:
                    self.fps_key = fps
                    self.fps_img = Text("%d FPS" % fps, size=32, color="#7dff7d",
                                        outlines=[(2, "#000", 0, 0)])
                rv.blit(renpy.render(self.fps_img, width, height, st, at), (20, 12))

    def Dance_FeedbackColor(name):
        return {"gold": "#ffd34d", "green": "#7dff7d", "red": "#ff6b6b"}.get(name, "#fff")


# ----------
# PREVIEW / RULES SCREEN
# ----------
# Shown before the song starts, in the same shape as Ludo's prep phase.
#
# On touch the whole panel is laid out on a PORTRAIT canvas and rotated a quarter turn, so it only reads once the phone is upright — which is the point: upright is how the track is meant to be played. Rotated, the widescreen's left edge is the phone's bottom, so notes fall from the top and the four lanes land under both thumbs.
transform dance_preview_rot:
    rotate 90
    rotate_pad False
    align (0.5, 0.5)

transform dance_preview_flat:
    align (0.5, 0.5)

screen dance_preview_bpm(song_id):

    default s_title = Dance_Songs[song_id]["title"]
    default s_bpm = Dance_Songs[song_id]["bpm"]
    default upright = Dance_MultiLane()

    add Solid("#000000D8")

    fixed:
        xysize ((1080, 1920) if upright else (1920, 1080))
        at (dance_preview_rot if upright else dance_preview_flat)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25

            label renpy.translate_string("{size=+60}{b}Dance{/b}{/size}") xalign 0.5
            text renpy.translate_string("{size=+10}[s_title] — [s_bpm] BPM{/size}") xalign 0.5

            if upright:
                text renpy.translate_string("{size=+6}{color=#FFD964}{b}Hold your phone upright{/b}{/color}{/size}") xalign 0.5

            viewport:
                xalign 0.5
                xysize ((980, 900) if upright else (900, 320))
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                vbox:
                    xsize (960 if upright else 880)
                    spacing 5

                    if upright:
                        text renpy.translate_string("{size=+2}Arrows fall from the top of the screen. Hit each one the moment it reaches the line at the bottom — in time with the music.{/size}") xalign 0.5
                    else:
                        text renpy.translate_string("{size=+2}Arrows fly in from the right. Hit each one the moment it reaches the line on the left — in time with the music.{/size}") xalign 0.5

                    text renpy.translate_string("\n{color=#64FF64}Controls:{/color}") xalign 0.5
                    if upright:
                        text renpy.translate_string("• Four lanes run down the screen — tap the {b}lane{/b} the arrow is falling in") xalign 0.5
                        text renpy.translate_string("• They sit at the bottom, one under each thumb — hold with {b}both hands{/b}") xalign 0.5
                    else:
                        text renpy.translate_string("• Press the key the arrow shows: {b}W A S D{/b} or the {b}arrow keys{/b}") xalign 0.5

                    text renpy.translate_string("\n{color=#64FF64}Scoring:{/color}") xalign 0.5
                    text renpy.translate_string("• {color=#7DFF7D}Right{/color} (close enough) = {b}+1{/b}") xalign 0.5
                    text renpy.translate_string("• {color=#FFD34D}Perfect{/color} (dead on the beat) = {b}+1 for each perfect in a row{/b} — 1, then 2, then 3…") xalign 0.5
                    text renpy.translate_string("• {color=#FF6B6B}Miss or wrong key{/color} = {b}-1 for each in a row{/b} — the streak cuts both ways") xalign 0.5

                    text renpy.translate_string("\n{color=#64FF64}Performance perk:{/color}") xalign 0.5
                    if perk_cha_per >= 1:
                        text renpy.translate_string("• Your Performance perk (LVL [perk_cha_per]) widens both timing windows") xalign 0.5
                    else:
                        text renpy.translate_string("• The Performance perk widens both timing windows — you have none yet") xalign 0.5

            textbutton renpy.translate_string("{size=+20}Dance!{/size}") xalign 0.5 action Return(True)


# ----------
# GAME SCREEN
# ----------
# The conductor drives all motion; this timer only refreshes text/dancers and ends the song.
screen dance_screen_bpm(mini_dancer_1=None, mini_dancer_2=None, song_id="sunrise"):

    default con = RhythmConductor(song_id)
    default song = Dance_Songs[song_id]
    default npc_move = "a"
    default is_hero_left = (mini_dancer_1 and mini_dancer_1.lower() == "hero")
    default is_hero_right = (mini_dancer_2 and mini_dancer_2.lower() == "hero")

    # Dancers first — pre-scaled 540px frames (_DANCE_BPM sets), low, and BEHIND the track. The Settings toggle removes them entirely: they are the heaviest thing here for a weak device.
    if mini_dancer_1 and preferences.dancers:
        $ move_1 = (con.move if is_hero_left else npc_move) if con.started else "idle"
        add "{}_DANCE_BPM {}".format(mini_dancer_1.upper(), move_1):
            zoom DANCE_DANCER_ZOOM
            anchor (0.5, 1.0)
            pos (DANCE_DANCER_X, 1.0)
            yoffset -DANCE_DANCER_LIFT

    if mini_dancer_2 and preferences.dancers:
        $ move_2 = (con.move if is_hero_right else npc_move) if con.started else "idle"
        add "{}_DANCE_BPM {}".format(mini_dancer_2.upper(), move_2):
            zoom DANCE_DANCER_ZOOM
            anchor (0.5, 1.0)
            pos (1.0 - DANCE_DANCER_X, 1.0)
            yoffset -DANCE_DANCER_LIFT

    add con

    # End check only — the conductor draws its own HUD, so this tick can be slow and cheap.
    # Every tick re-evaluates the whole screen; at 0.1s that alone dented phone frame rate.
    timer 0.5 repeat True action [
        SetVariable("a_event_0", con.score),
        If(con.finished, true=Jump("wnei_interact_hangout_dance_end_bpm"), false=NullAction()),
    ]

    # Dancers idle through the lead-in, then move from the downbeat.
    if con.started and preferences.dancers:
        timer (song["anim_step"] * 8) repeat True action SetScreenVariable(
            "npc_move", renpy.random.choice(["a", "w", "d", "s"]))

    # Keyboard: always live, on both layouts.
    for lane in DANCE_LANES:
        key lane action Function(con.press, lane)
        key ("K_" + {"w": "UP", "s": "DOWN", "d": "RIGHT", "a": "LEFT"}[lane]) action Function(con.press, lane)

    # Touch (4-lane mode): the lane itself is the button — tap anywhere on its row. Silent, since a click sound would fight the track; the lane flash and score popup carry the feedback.
    if con.multi:
        for row, lane in enumerate(DANCE_LANES):
            button:
                xysize (1920, con.lane_h)
                xpos 0
                ypos Dance_LaneY(row, True)
                padding (0, 0)
                background None
                activate_sound None
                hover_sound None
                action Function(con.press, lane)

    # Score/combo/progress moved into the conductor's render_hud — screen widgets needed the fast restart timer to stay fresh; the conductor already redraws every frame for free.


# ----------
# NOTE / RECEPTOR SPRITES
# ----------
# Same sheet as the old minigame, distinct names + smaller zoom to fit the horizontal lanes.
init:
    image dance_bpm_arrow w beige:
        Crop((0, 0, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True
    image dance_bpm_arrow s beige:
        Crop((32, 0, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True
    image dance_bpm_arrow d beige:
        Crop((64, 0, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True
    image dance_bpm_arrow a beige:
        Crop((96, 0, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True

    image dance_bpm_arrow w green:
        Crop((0, 32, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True
    image dance_bpm_arrow s green:
        Crop((32, 32, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True
    image dance_bpm_arrow d green:
        Crop((64, 32, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True
    image dance_bpm_arrow a green:
        Crop((96, 32, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True

    image dance_bpm_arrow w red:
        Crop((0, 64, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True
    image dance_bpm_arrow s red:
        Crop((32, 64, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True
    image dance_bpm_arrow d red:
        Crop((64, 64, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True
    image dance_bpm_arrow a red:
        Crop((96, 64, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True

    image dance_bpm_hit:
        Crop((0, 96, 32, 32), "images/Mechanics/Dance/sprites.webp")
        zoom 3 nearest True

    # Touch backdrop: the animated BG_DanceFloor rotates AND zooms a full-screen image every frame, which is the single most expensive thing on the screen for a phone GPU. Same look, held still.
    image BG_DanceFloor_Flat:
        rotate_pad False
        align (0.5, 0.5)
        zoom 1.15
        "bg_2 pink"

# ----------
# DANCERS (BPM) — pre-scaled frames
# ----------
# Same animations as the old minigame's HERO_DANCE/WNEI_DANCE, but on 540px copies of the 1080px frames (images/Mechanics/Dance/small/). This screen draws the dancers at half size anyway, and full frames decoded mid-song were the single biggest cause of the mobile chop: ~4.7 MB of texture per frame, ~270 MB across the 58 originals vs ~68 MB for the whole set.
init:
    image HERO_DANCE_BPM a:
        "hero dance_s_01_01"
        pause minigamestep
        "hero dance_s_01_02"
        pause minigamestep
        "hero dance_s_01_01"
        pause minigamestep
        "hero dance_s_01_03"
        pause minigamestep
        "hero dance_s_01_04"
        pause minigamestep
        "hero dance_s_01_05"
        pause minigamestep
        "hero dance_s_01_04"
        pause minigamestep
        "hero dance_s_01_03"
        pause minigamestep

    image HERO_DANCE_BPM w:
        "hero dance_s_02_01"
        pause minigamestep
        "hero dance_s_02_02"
        pause minigamestep
        "hero dance_s_02_01"
        pause minigamestep
        "hero dance_s_02_03"
        pause minigamestep
        "hero dance_s_02_04"
        pause minigamestep
        "hero dance_s_02_05"
        pause minigamestep
        "hero dance_s_02_04"
        pause minigamestep
        "hero dance_s_02_03"
        pause minigamestep

    image HERO_DANCE_BPM d:
        "hero dance_s_03_01"
        pause minigamestep
        "hero dance_s_03_02"
        pause minigamestep
        "hero dance_s_03_01"
        pause minigamestep
        "hero dance_s_03_03"
        pause minigamestep
        "hero dance_s_03_04"
        pause minigamestep
        "hero dance_s_03_05"
        pause minigamestep
        "hero dance_s_03_04"
        pause minigamestep
        "hero dance_s_03_03"
        pause minigamestep

    image HERO_DANCE_BPM s:
        "hero dance_s_04_01"
        pause minigamestep
        "hero dance_s_04_02"
        pause minigamestep
        "hero dance_s_04_03"
        pause minigamestep
        "hero dance_s_04_04"
        pause minigamestep
        "hero dance_s_04_05"
        pause minigamestep
        "hero dance_s_04_06"
        pause minigamestep
        "hero dance_s_04_07"
        pause minigamestep
        "hero dance_s_04_08"
        pause minigamestep

    image HERO_DANCE_BPM idle:
        "hero idle_s"

    image HERO_DANCE_BPM miss:
        "hero miss_s"

    image WNEI_DANCE_BPM a:
        "wnei dance_s_01_01"
        pause minigamestep
        "wnei dance_s_01_02"
        pause minigamestep
        "wnei dance_s_01_03"
        pause minigamestep
        "wnei dance_s_01_04"
        pause minigamestep
        "wnei dance_s_01_05"
        pause minigamestep
        "wnei dance_s_01_06"
        pause minigamestep
        "wnei dance_s_01_07"
        pause minigamestep
        "wnei dance_s_01_08"
        pause minigamestep
        repeat

    image WNEI_DANCE_BPM w:
        "wnei dance_s_02_01"
        pause minigamestep
        "wnei dance_s_02_02"
        pause minigamestep
        "wnei dance_s_02_03"
        pause minigamestep
        "wnei dance_s_02_04"
        pause minigamestep
        "wnei dance_s_02_05"
        pause minigamestep
        "wnei dance_s_02_06"
        pause minigamestep
        "wnei dance_s_02_07"
        pause minigamestep
        "wnei dance_s_02_08"
        pause minigamestep
        repeat

    image WNEI_DANCE_BPM d:
        "wnei dance_s_03_01"
        pause minigamestep
        "wnei dance_s_03_02"
        pause minigamestep
        "wnei dance_s_03_03"
        pause minigamestep
        "wnei dance_s_03_04"
        pause minigamestep
        "wnei dance_s_03_05"
        pause minigamestep
        "wnei dance_s_03_06"
        pause minigamestep
        "wnei dance_s_03_07"
        pause minigamestep
        "wnei dance_s_03_08"
        pause minigamestep
        repeat

    image WNEI_DANCE_BPM s:
        "wnei dance_s_04_01"
        pause minigamestep
        "wnei dance_s_04_02"
        pause minigamestep
        "wnei dance_s_04_03"
        pause minigamestep
        "wnei dance_s_04_04"
        pause minigamestep
        "wnei dance_s_04_05"
        pause minigamestep
        "wnei dance_s_04_06"
        pause minigamestep
        "wnei dance_s_04_07"
        pause minigamestep
        "wnei dance_s_04_08"
        pause minigamestep
        repeat

    # WNEI has no idle/miss art (only HERO does); both dancers idle through the lead-in.
    image WNEI_DANCE_BPM idle:
        "wnei dance_s_01_01"

    image WNEI_DANCE_BPM miss:
        "wnei dance_s_01_01"


# ----------
# TOOL: chart recorder (test-only)
# ----------
# Tap a song's rhythm instead of guessing note numbers (renpy-builder §12). Plays the track over a scrolling beat grid, records each key tap, quantises it to the grid, and writes a pasteable `chart=[...]`. Reached from the test-only living-room action button (UI.rpy); never in a build.

define DANCE_REC_SUBDIV = 2             # grid slots per beat; taps snap to the nearest one

init python:
    import os

    class RhythmRecorder(renpy.Displayable):

        def __init__(self, song_id, **kwargs):
            super(RhythmRecorder, self).__init__(**kwargs)
            self.song_id = song_id
            self.song = Dance_Songs[song_id]
            self.bpm = self.song["bpm"]
            self.offset = self.song["start_offset"]
            self.taps = []                      # (music_pos, lane), raw
            self.pos = 0.0
            self.started = False
            self.saved = None

        def beat_len(self):
            return 60.0 / self.bpm

        def nudge(self, delta):
            self.offset = round(self.offset + delta, 3)

        def tap(self, lane):
            if self.started:
                self.taps.append((self.pos, lane))

        def undo(self):
            if self.taps:
                self.taps.pop()

        def chart(self):
            """Quantise taps to the grid; one note per slot wins, earliest tap kept."""
            slot = 1.0 / DANCE_REC_SUBDIV
            seen, out = set(), []
            for pos, lane in sorted(self.taps):
                b = round((pos - self.offset) / self.beat_len() / slot) * slot
                if b < 0 or b in seen:
                    continue
                seen.add(b)
                out.append((round(b, 3), lane))
            return out

        def export(self):
            chart = self.chart()
            path = os.path.join(config.gamedir, "dance_chart_%s.txt" % self.song_id)
            with open(path, "w") as f:
                f.write('"%s": {\n' % self.song_id)
                f.write('    "title": "%s",\n' % self.song["title"])
                f.write('    "file": "%s",\n' % self.song["file"])
                f.write('    "bpm": %g,\n' % self.bpm)
                f.write('    "start_offset": %.3f,\n' % self.offset)
                f.write('    "length": %g,\n' % self.song["length"])
                f.write('    "anim_step": %g,\n' % self.song["anim_step"])
                f.write('    "chart": [\n')
                for i in range(0, len(chart), 8):
                    row = ", ".join('(%g, "%s")' % n for n in chart[i:i + 8])
                    f.write("        %s,\n" % row)
                f.write("    ],\n},\n")
            self.saved = path
            return path

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)

            pos = renpy.music.get_pos(channel="BGM")
            if pos is not None:
                self.pos = pos
                self.started = True

            beat = self.beat_len()
            t = self.pos

            # Single lane bed, same geometry as the game screen so the feel transfers.
            rv.blit(renpy.render(Solid("#00000055", xysize=(width, DANCE_LANE_H)),
                                 width, height, st, at), (0, DANCE_LANE_Y))

            # Scrolling beat grid: bars are bright, off-beats dim — the visual metronome.
            top, tall = DANCE_LANE_Y, DANCE_LANE_H
            first = int((t - self.offset - (DANCE_HIT_X / float(DANCE_SPEED))) / beat) - 1
            for k in range(first, first + int(width / (beat * DANCE_SPEED)) + 3):
                if k < 0:
                    continue
                x = DANCE_HIT_X + (self.offset + k * beat - t) * DANCE_SPEED
                if x < 0 or x > width:
                    continue
                downbeat = (k % 4 == 0)
                line = Solid("#ffffffcc" if downbeat else "#ffffff33",
                             xysize=(4 if downbeat else 2, tall))
                rv.blit(renpy.render(line, width, height, st, at), (int(x), top))

            # Taps already recorded, drawn on their quantised slot.
            slot = beat / DANCE_REC_SUBDIV
            for pos, lane in self.taps:
                q = self.offset + round((pos - self.offset) / slot) * slot
                x = DANCE_HIT_X + (q - t) * DANCE_SPEED
                if x < -80 or x > width + 80:
                    continue
                # Fresh instance per tap — a shared one would collapse every tap onto one spot.
                img = renpy.render(Transform("dance_bpm_arrow %s beige" % lane),
                                   width, height, st, at)
                iw, ih = img.get_size()
                rv.blit(img, (int(x - iw // 2), DANCE_LANE_Y + (DANCE_LANE_H - ih) // 2))

            # Hit line.
            rv.blit(renpy.render(Solid("#ff325b", xysize=(4, tall)), width, height, st, at),
                    (DANCE_HIT_X, top))

            renpy.redraw(self, 0)
            return rv


screen dance_recorder_screen(song_id):

    default rec = RhythmRecorder(song_id)

    add rec

    for lane in DANCE_LANES:
        key lane action Function(rec.tap, lane)
        key "K_" + {"w": "UP", "s": "DOWN", "d": "RIGHT", "a": "LEFT"}[lane] action Function(rec.tap, lane)

    key "K_BACKSPACE" action Function(rec.undo)
    key "K_LEFTBRACKET" action Function(rec.nudge, -0.01)
    key "K_RIGHTBRACKET" action Function(rec.nudge, 0.01)

    timer 0.05 repeat True action NullAction()

    vbox:
        xpos 40
        ypos 40
        spacing 6
        text renpy.translate_string("REC [song_id] — bpm [rec.bpm] · offset [rec.offset] · notes [len(rec.taps)]")
        text renpy.translate_string("w/a/s/d = tap · Backspace = undo · [ ] = nudge offset · Save writes game/dance_chart_[song_id].txt")
        if rec.saved:
            text renpy.translate_string("Saved: [rec.saved]") color "#7dff7d"

    hbox:
        xalign 0.5
        yalign 0.95
        spacing 30
        textbutton renpy.translate_string("Save chart") action Function(rec.export)
        textbutton renpy.translate_string("Done") action [Stop("BGM", fadeout=1), Return(True)]


label dance_recorder:
    $ _skipping = False

    python:
        a_menu_0 = [(Dance_Songs[s]["title"], s) for s in Dance_Songs]
        a_event_5 = renpy.display_menu(a_menu_0)

    stop BGM
    $ renpy.music.play(Dance_Songs[a_event_5]["file"], channel="BGM", loop=False)

    call screen dance_recorder_screen(a_event_5)

    play BGM "audio/W2C - Tranquility.mp3"
    return
