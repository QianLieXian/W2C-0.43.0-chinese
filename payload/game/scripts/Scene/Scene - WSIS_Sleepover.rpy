image wsis_sleepover_2_window_3_a = Movie(play="images/Scene/WSIS - Sleepover/wsis_sleepover_2_window_3A.webm", loop=True, start_image="wsis_sleepover_2_window_3a", image="wsis_sleepover_2_window_3a")

image wsis_sleepover_2_window_3_b = Movie(play="images/Scene/WSIS - Sleepover/wsis_sleepover_2_window_3B.webm", loop=True, start_image="wsis_sleepover_2_window_3b", image="wsis_sleepover_2_window_3b")

init python:

    class DynamicSpeedAnimation(renpy.Displayable):
        # Frame-by-frame animation whose FPS is sampled every render from
        # speed_fn. A slider bound to the variable used by speed_fn changes
        # the visible speed live, without restarting the animation.
        # sfx_at maps frame index -> callback(trans, st, at), fired once on
        # the transition into that frame (matches how `function SFX_xxx`
        # was positioned between pauses in the original ATL).

        def __init__(self, frames, speed_fn, sfx_at=None, **kwargs):
            super(DynamicSpeedAnimation, self).__init__(**kwargs)
            self.frames = [renpy.displayable(f) for f in frames]
            self.speed_fn = speed_fn
            self.sfx_at = sfx_at or {}
            self.virtual_pos = 0.0
            self.last_st = 0.0
            self.last_idx = -1

        def render(self, width, height, st, at):
            if st < self.last_st:
                self.virtual_pos = 0.0
                self.last_idx = -1
            dt = max(0.0, st - self.last_st)
            self.last_st = st
            n = len(self.frames)
            fps = max(0.001, float(self.speed_fn()))
            self.virtual_pos = (self.virtual_pos + dt * fps) % n
            idx = int(self.virtual_pos) % n
            if idx != self.last_idx:
                self.last_idx = idx
                cb = self.sfx_at.get(idx)
                if cb is not None:
                    cb(self, st, at)
            cr = renpy.render(self.frames[idx], width, height, st, at)
            rv = renpy.Render(cr.width, cr.height)
            rv.blit(cr, (0, 0))
            frac = self.virtual_pos - int(self.virtual_pos)
            renpy.redraw(self, max(0.001, (1.0 - frac) / fps))
            return rv

        def visit(self):
            return list(self.frames)

# ---------------------------------------------------------------------------
label wsis_sleepover: # Girl's Sleepover Night
# ---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_201

    scene wsis_sleepover_1_bg
    show wsis_sleepover_1_fg 0
    show fx_light
    with fade

    play SE1 "DoorKnock.ogg"
    pause 0.2
    play SE1 "DoorKnock.ogg"
    pause 0.2
    play SE1 "DoorKnock.ogg"
    pause 1.0
    play SE1 "DoorOpen1.ogg"
    pause 0.5
    play SE1 "DoorOpen2.ogg"

    scene wsis_sleepover_1_bg
    show wsis_sleepover_1_wnei_body 1
    show wsis_sleepover_1_wnei_face a0
    show wsis_sleepover_1_wnei_outfit1 common
    show wsis_sleepover_1_mg
    show wsis_sleepover_1_fg 1
    show fx_light
    with dissolve

    pause

    show wsis_sleepover_1_wnei_face a1

    if wnei_inti < 40:
        wnei "Hey there!{w=[wt2]} We're in a girls-only sleepover.{w=[wt3]} {bt}Bye Bye...{/bt}"

        $ msg.msg(renpy.translate_string("You don't have enough intimacy with [C_Nam][fnamewnei][C_Off] to join [C_Dat]Girl's Sleepover[C_Off] event"))

        play SE1 "DoorOpen2.ogg"
        show wsis_sleepover_1_fg 0 with Dissolve(1)

        play SE1 "DoorLock.mp3"

        pause

        # Relocate HERO out, or check_playermap replays this whole intro every tick if he was already standing in the room when the sleepover started.
        call goto_home_hallway from _call_goto_home_hallway_3
        jump show_ui

    else:
        wnei "Hey, [C_Nam][fnamehero][C_Off]!{w=[wt3]} Let's play!"

        if wsis_inti < 40:
            scene wsis_sleepover_1_bg
            show wsis_sleepover_1_wsis_wnei_body
            show wsis_sleepover_1_wsis_face o0
            show wsis_sleepover_1_wnei_outfit2 common
            show wsis_sleepover_1_wsis_outfit2 common
            show wsis_sleepover_1_mg
            show wsis_sleepover_1_fg 1
            show fx_light
            with dissolve

            show wsis_sleepover_1_wsis_face o1
            wsis "That's a girls sleepover.{w=[wt3]} Get out!"

            $ msg.msg(renpy.translate_string("You don't have enough intimacy with [C_Nam][fnamewsis][C_Off] to join [C_Dat]Girl's Sleepover[C_Off] event"))

            play SE1 "DoorBam.ogg"

            show wsis_sleepover_1_fg 0

            pause

            # Same fix as the WNEI rejection above.
            call goto_home_hallway from _call_goto_home_hallway_4
            jump show_ui

        else:
            jump wsis_sleepover_loop

# ---------------------------------------------------------------------------
label wsis_sleepover_loop:
# ---------------------------------------------------------------------------

    if gametimehour >= 22:
        jump wsis_sleepover_sleep

    scene bg_0 with Dissolve(1)
    scene bg_home bedroom wsis with dissolve

    menu:

        "⭐ Chat with [C_Nam][fnamewnei][C_Off]" if (wsis_quest_6 < 1):
            call wsis_sleepover_chat_1 from _call_wsis_sleepover_chat_1

        "⭐ Open Window" if (wsis_quest_6 == 1) and ("Sleepover" not in wsis_know):
            call wsis_sleepover_window from _call_wsis_sleepover_window

        "Play Ludo" if 0 > 1:
            call screen minigame_ludo(var_paw=1)

        "Dance" if 0 > 1:
            call screen dance_screen()

        "Dress Up" if 0 > 1:
            call wsis_sleepover_dressup from _call_wsis_sleepover_dressup

        "Leave":
            call gametime_wait(22, 00) from _call_gametime_wait_30
            jump wsis_sleepover_loop

    $ gametimemin += 60
    call gametime from _call_gametime_122

    jump wsis_sleepover_loop

# ---------------------------------------------------------------------------
label wsis_sleepover_dressup:
# ---------------------------------------------------------------------------
    hero ""

    $ gametimemin += 60
    call gametime from _call_gametime_123

    jump wsis_sleepover_loop

# ---------------------------------------------------------------------------
label wsis_sleepover_chat_1:
# ---------------------------------------------------------------------------

    $ wsis_quest_6 = 1

    show HERO at LC
    show WNEI at RC
    show WSIS at OR
    show WSIS at RR_slow
    with dissolve

    hero "Hey{w=[wt2]}, [C_Nam][fnamewnei][C_Off].{w=[wt3]} How did you even get your parents to let you come over?{w=[wt3]} I always thought they were pretty strict about that kind of thing."

    wnei "Oh{w=[wt2]}, they ARE!{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} they were {bt}Super Duper Overprotective{/bt}!"

    hero "So what changed their minds?"

    wnei "I asked them SO many times if I could come here to play with [C_Nam][fnamewsis][C_Off]!{w=[wt3]} Like{w=[wt2]}, every single week.{w=[wt3]} And they always said the exact same thing:{w=[wt3]} '{i}A girl should not sleep outside of her own house.{/i}'"

    wsis "That's pretty old-fashioned."

    wnei "Yeah!{w=[wt2]} Very boring!{w=[wt3]} But then they just told me that they changed their mind and that I should come here on weekends."

    hero "{aw}Ehh...!?{/aw} Just like that?"

    wnei "Weird, right?{w=[wt3]} I don't know... It happened after a night I woke up{w=[wt2]}, and I heard this really weird sound coming from their room. Like{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {bt}clapping?{/bt}{w=[wt3]} Really fast clapping."

    hero "..."

    wsis "..."

    wnei "So I knocked on their door and asked what they were doing!{w=[wt3]} I said{w=[wt2]}, '{i}Why are you two applauding so late at night?{/i}'"

    hero "..."

    wsis "..."

    wnei "And they went SO red!{w=[wt3]} I had never seen their faces like that before.{w=[wt1]} {lg}Shi hi hi...{/lg}{w=[wt3]} The next morning{w=[wt2]}, they said they had 'thought it over'{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} and that I was allowed to sleep over at [C_Nam][fnamewsis][C_Off]'s every weekend!{w=[wt3]} Because she's a {bt}good and trustworthy friend!{/bt}"

    show WSIS at CC_slow

    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}O{w=[wt1]}-of course!"

    wnei "{bt}Isn't that great?!{/bt}{w=[wt3]} Turned out to be so easy in the end!"

    hero "Well{w=[wt2]}, don't you think they're-{nw}"

    show HERO at Hurt_L
    show WSIS at Hit_L
    play SE1 "Hit1.ogg"

    wsis "{size=-10}Shut up...!{/size}"

    $ gametimemin += 30
    call gametime from _call_gametime_124

    jump wsis_sleepover_loop

# ---------------------------------------------------------------------------
label wsis_sleepover_window:
# ---------------------------------------------------------------------------

    $ wsis_quest_6 = 2
    $ wsis_know.append("Sleepover")

    scene wsis_sleepover_2_window_1_bg
    show wsis_sleepover_2_window_1_mg 1
    show wsis_sleepover_2_window_1_hero 1
    show fx_light
    with fade

    hero "Hey{w=[wt2]}, those curtains have been closed all night."

    scene wsis_sleepover_2_window_1_bg
    show wsis_sleepover_2_window_1_mg 1
    show wsis_sleepover_2_window_1_hero 1
    show wsis_sleepover_2_window_1_wsis 1
    show fx_light
    with dissolve

    wsis "D{w=[wt1]}-don't touch that!!!"

    scene wsis_sleepover_2_window_2_bg
    show wsis_sleepover_2_window_2_wnei
    show wsis_sleepover_2_window_2_char
    show wsis_sleepover_2_window_2_wsis o0
    show wsis_sleepover_2_window_2_hero a0
    show wsis_sleepover_2_window_2_fg
    show fx_light
    with dissolve

    show wsis_sleepover_2_window_2_hero a1
    hero "Come on{w=[wt2]}, Let some light into your cave!"

    stop BGM fadeout 5

    show wsis_sleepover_2_window_2_wsis o1
    show wsis_sleepover_2_window_2_hero a0
    wsis "Hey!{w=[wt2]} I said don't{nw}"

    show wsis_sleepover_2_window_2_wsis o2
    show wsis_sleepover_2_window_2_hero a2
    wsis "Hey!{w=[wt2]} I said don't{fast}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

    show wsis_sleepover_2_window_2_wsis s0
    show wsis_sleepover_2_window_2_hero s0
    with dissolve

    pause

    menu:
        "Turn on voyeur content? [C_Red](You see other characters having sex)[C_Off]{fast}"

        "No":
            $ preferences.voyeur = False

        "Yes":
            $ preferences.voyeur = True

    play BGM "audio/W2C - SexyVibes.mp3"

    if preferences.voyeur == True:
        scene wsis_sleepover_2_window_3_b

        if 0 > 1:
            if perk_int_per < 2:
                $ msg.msg(renpy.translate_string("[C_Neg]Fail check for [C_Dat]Perception[C_Off] skill[C_Off]"))
                scene wsis_sleepover_2_window_3_a
                show wsis_sleepover_2_window_3_fg

            else:
                $ msg.msg(renpy.translate_string("[C_Pos]Success check for [C_Dat]Perception[C_Off] skill[C_Off]"))
                scene wsis_sleepover_2_window_3_b

    pause

    if preferences.voyeur == False:
        show wsis_sleepover_2_window_2_wsis s0
        show wsis_sleepover_2_window_2_hero s1
    hero "{size=-10}Is that{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} [C_Nam]Mr. [lnamewnei][C_Off] and [C_Nam]Mrs. [lnamewnei][C_Off]...?{/size}"

    if preferences.voyeur == False:
        show wsis_sleepover_2_window_2_wsis s1
        show wsis_sleepover_2_window_2_hero s0
    wsis "{size=-10}Who else do you think could be!?{w=[wt3]} Now hurry up and close it!!{/size}"

    if preferences.voyeur == False:
        show wsis_sleepover_2_window_2_wsis s0
        show wsis_sleepover_2_window_2_hero s1
    hero "{size=-10}They're{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} right in the middle of-{/size}"

    if preferences.voyeur == False:
        hide wsis_sleepover_2_window_2_wnei with dissolve
        show wsis_sleepover_2_window_2_wsis s1
        show wsis_sleepover_2_window_2_hero s0
    wsis "{size=-10}Shut up and close the curtain!{w=[wt3]} Right now!!!{/size}"

    stop BGM
    play SE1 "Record Scratch.mp3"

    scene wsis_sleepover_2_window_1_bg
    show wsis_sleepover_2_window_1_mg 0
    show wsis_sleepover_2_window_1_wnei
    show wsis_sleepover_2_window_1_wnei_face o0
    show wsis_sleepover_2_window_1_hero 2
    show wsis_sleepover_2_window_1_wsis 2
    show fx_light
    with hpunch

    show wsis_sleepover_2_window_1_wnei_face o1
    wnei "{bt}Heyyy!{/bt}{w=[wt3]} What are you two whispering about over there?"

    play BGM "audio/W2C - Awkward.mp3"

    show wsis_sleepover_2_window_1_wnei_face o0
    hero "N{w=[wt1]}-nothing!{w=[wt2]} We were just{w=[wt2]}, uh..."

    wsis "D{w=[wt1]}-discussing what we were going to do now.{w=[wt2]} A{w=[wt1]}-are you ready for the revelation?"

    show wsis_sleepover_2_window_1_wnei_face a1
    wnei "{bt}Ooooh!{w=[wt3]} Sure! Tell me now!{/bt}"

    show wsis_sleepover_2_window_1_wnei_face a0
    wsis "[C_Nam][fnamehero][C_Off] will tell you!{w=[wt4]} {size=-10}And won't say a word about that!!!{/size}"

    show wsis_sleepover_2_window_1_wnei_face a1
    wnei "{bt}Hurry up! Hurry up!{/bt} You two are grumbling too much!!! What we'll do next, [C_Nam][fnamehero][C_Off]?"

    show wsis_sleepover_2_window_1_wnei_face a0
    hero "{aw}Well...{/aw}"

    $ gametimemin += 30
    call gametime from _call_gametime_125

    jump wsis_sleepover_loop

# ---------------------------------------------------------------------------
label wsis_sleepover_sleep:
# ---------------------------------------------------------------------------

    scene wsis_sleepover_3_sleep_1_bg
    show wsis_sleepover_3_sleep_1_wsis
    show wsis_sleepover_3_sleep_1_wsis_face o0
    show wsis_sleepover_3_sleep_1_wsis_eyes u
    show wsis_sleepover_3_sleep_1_hero
    show wsis_sleepover_3_sleep_1_hero_face o0
    show fx_light
    with fade

    show wsis_sleepover_3_sleep_1_wsis_eyes f
    show wsis_sleepover_3_sleep_1_hero_face o1
    with dissolve

    pause(0.5)

    scene wsis_sleepover_3_sleep_1_bg
    show wsis_sleepover_3_sleep_1_wsis
    show wsis_sleepover_3_sleep_1_wsis_face o0
    show wsis_sleepover_3_sleep_1_wsis_eyes u
    show wsis_sleepover_3_sleep_1_wnei 1
    show wsis_sleepover_3_sleep_1_hero
    show wsis_sleepover_3_sleep_1_hero_face o0
    show fx_light
    with Dissolve(1)

    pause(0.5)

    play SE1 "Bounce2.mp3"

    show wsis_sleepover_3_sleep_1_wnei 2
    show wsis_sleepover_3_sleep_1_wsis_face s0
    show wsis_sleepover_3_sleep_1_wsis_eyes u
    show wsis_sleepover_3_sleep_1_hero_face s0
    with dissolve

    pause(0.5)

    play SE1 "Boing1.mp3"

    scene wsis_sleepover_3_sleep_1_bg
    show wsis_sleepover_3_sleep_1_wsis
    show wsis_sleepover_3_sleep_1_wsis_face s0
    show wsis_sleepover_3_sleep_1_wsis_eyes d
    show wsis_sleepover_3_sleep_1_wnei 3
    show wsis_sleepover_3_sleep_1_wnei_face a0
    show wsis_sleepover_3_sleep_1_hero
    show wsis_sleepover_3_sleep_1_hero_face s0
    show fx_light
    with dissolve

    pause(0.5)

    show wsis_sleepover_3_sleep_1_wnei_face a1
    wnei "That's enough for me.{w=[wt3]} Gonna sleep."

    # WNEI removes her blouse, getting topless

    show wsis_sleepover_3_sleep_1_wnei_face a0
    show wsis_sleepover_3_sleep_1_wsis_face s1
    if wsis_quest_5 >= 2: # Content already done

        wsis "{aw}Ugh!{/aw}{w=[wt2]} here you go again{w=[wt2]}, exposing in front of [C_Nam][fnamehero][C_Off]!"

        show wsis_sleepover_3_sleep_1_wsis_face s0
        show wsis_sleepover_3_sleep_1_wnei_face a1
        wnei "Don't worry!{w=[wt2]} He'll lend me his sweatshirt.{w=[wt2]} Right, [C_Nam][fnamehero][C_Off]?"

    else:

        wsis "What are you doing!?{w=[wt2]} You're exposing in front of a boy!!!"

        show wsis_sleepover_3_sleep_1_wsis_face s0
        show wsis_sleepover_3_sleep_1_wnei_face a1
        wnei "Hmm?{w=[wt2]} What do you mean?{w=[wt2]} He's just [C_Nam][fnamehero][C_Off]."

        show wsis_sleepover_3_sleep_1_wsis_eyes u
        show wsis_sleepover_3_sleep_1_wnei_face a0
        mind "(I don't know how to feel when you say that{w=[wt2]}, but for now I'll just stay quiet.)"

        show wsis_sleepover_3_sleep_1_wsis_face s1
        wsis "Stop looking, you pervert!"

        show wsis_sleepover_3_sleep_1_wsis_eyes d
        show wsis_sleepover_3_sleep_1_wsis_face s0
        show wsis_sleepover_3_sleep_1_wnei_face a1
        wnei "But he'll sleep with us, right?"

        show wsis_sleepover_3_sleep_1_wsis_face s1
        show wsis_sleepover_3_sleep_1_wnei_face a0
        wsis "{aw}What!?{/aw}"

        show wsis_sleepover_3_sleep_1_wsis_face s0
        show wsis_sleepover_3_sleep_1_wnei_face a1
        wnei "C'mon!{w=[wt2]} We used to do that a lot!"

        show wsis_sleepover_3_sleep_1_wsis_eyes u
        show wsis_sleepover_3_sleep_1_wsis_face s1
        show wsis_sleepover_3_sleep_1_wnei_face a0
        wsis "{aw}It's different now!{/aw}"

        show wsis_sleepover_3_sleep_1_wsis_face s0
        show wsis_sleepover_3_sleep_1_wnei_face a1
        wnei "Don't tell me you guys stopped sleeping together...!"

        show wsis_sleepover_3_sleep_1_wnei_face a0 with None

        if wsis_quest_5 >= 1: # HERO already slept with WSIS

            show wsis_sleepover_3_sleep_1_wsis_eyes d
            show wsis_sleepover_3_sleep_1_wsis_face s1
            wsis "It d{w=[wt1]}-doesn't matter!{w=[wt3]} I won't let you sleep topless with him in my room!"

            show wsis_sleepover_3_sleep_1_wsis_face s0
            show wsis_sleepover_3_sleep_1_wnei_face a1
            wnei "{bt}Ehhh...?{/bt}{w=[wt3]} But my blouse is too tight to sleep{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Hey{w=[wt2]}, [C_Nam][fnamehero][C_Off].{w=[wt2]} Lend me your sweatshirt!"

            show wsis_sleepover_3_sleep_1_wsis_eyes u
            show wsis_sleepover_3_sleep_1_wnei_face a0
            with None

            hide wsis_sleepover_3_sleep_1_wnei
            hide wsis_sleepover_3_sleep_1_wnei_face
            with dissolve

            show wsis_sleepover_3_sleep_1_wsis_face s1
            wsis "{aw}Hmph...!{/aw}{w=[wt3]} You two are impossible!{w=[wt3]} Look away.{w=[wt3]} I need to change!"

            show wsis_sleepover_3_sleep_1_wsis_face s0 with None

            hide wsis_sleepover_3_sleep_1_wsis
            hide wsis_sleepover_3_sleep_1_wsis_face
            hide wsis_sleepover_3_sleep_1_wsis_eyes
            with dissolve

            pause

            hero ".{w=[wt1]} .{w=[wt1]} .{w=[wt4]} Ehhh...!?{w=[wt3]} [C_Mnd](Wait{w=[wt2]}, how did it end like this!?{w=[wt3]} Will I really sleep here with two girls?)[C_Off]"

            menu:
                "Join Them":
                    $ wsis_quest_5 = 2
                    hero "S{w=[wt1]}-sure..."

                    # HERO lends his sweatshirt to WNEI

                    $ zoomT1 = 0
                    $ zoomX1 = 0.5
                    $ zoomY1 = 0.99
                    $ zoomS1 = 1

                    $ zoomT2 = 5
                    $ zoomX2 = 0.5
                    $ zoomY2 = 0.01
                    $ zoomS2 = 1

                    scene bg_1
                    with Dissolve(1)

                    play BGM "audio/W2C - Adrenalust.mp3"

                    scene bg_2 sparkling
                    show wsis_sleepover_3_sleep_2_wnei at ZoomSTXY
                    show wsis_sleepover_3_sleep_2_wnei_face a0 at ZoomSTXY
                    with Dissolve(1)

                    pause

                    show wsis_sleepover_3_sleep_2_wnei_face a1
                    wnei "Look!{w=[wt2]} It's a dress!"

                    show wsis_sleepover_3_sleep_2_wnei_face a0 with None

                    hide wsis_sleepover_3_sleep_2_wnei
                    hide wsis_sleepover_3_sleep_2_wnei_face
                    show wsis_sleepover_3_sleep_2_wsis at ZoomSTXY
                    show wsis_sleepover_3_sleep_2_wsis_face o0 at ZoomSTXY
                    with Dissolve(1)

                    pause

                    show wsis_sleepover_3_sleep_2_wsis_face o1

                    wsis "{aw}I told you to look away!!!{/aw}"

                    show wsis_sleepover_3_sleep_2_wsis_face o0 with None

                    scene wsis_sleepover_3_sleep_3_bg
                    show wsis_sleepover_3_sleep_3_hero
                    show wsis_sleepover_3_sleep_3_wnei
                    show wsis_sleepover_3_sleep_3_wsis
                    show fx_light
                    with fade

                    pause

                    mind "(Am I really understanding it well?)"

                    scene wsis_sleepover_3_sleep_4_bg
                    show wsis_sleepover_3_sleep_4_char
                    show fx_light
                    with Fade(1, 0, 3)

                    pause

                    mind "(Ehh...? How did it end like this?)"

                    if not "Sleepover_Together" in wsis_know:
                        $ wsis_know.append("Sleepover_Together")

                    call passday from _call_passday_3

                "Leave":
                    hero "Well{w=[wt2]}, I b{w=[wt1]}-better go to my room.{w=[wt3]} Good night, girls!"

                    wnei "{bt}Awww...{/bt}{w=[wt3]} Good night..."

                    wsis "G{w=[wt1]}-good..."

        else:

            show wsis_sleepover_3_sleep_1_wsis_face s1
            show wsis_sleepover_3_sleep_1_wnei_face a0
            wsis "Of course we do!{w=[wt3]} Now go out{w=[wt2]}, that I wanna change!{w=[wt2]} Have a good night.{w=[wt2]} {bt}Shoo...! Shoo...!{/bt}"

            show wsis_sleepover_3_sleep_1_wsis_face s0
            show wsis_sleepover_3_sleep_1_wnei_face a1
            wnei "Good night, [C_Nam][fnamehero][C_Off]!"

            show wsis_sleepover_3_sleep_1_wnei_face a0
            hero "G{w=[wt1]}-good n-{nw}"

            play SE1 "DoorBam.ogg"

            hero "G-good n-{fast}{w}ight..."

        jump show_ui

# ---------------------------------------------------------------------------
label wsis_sleepover_wakeup:
# ---------------------------------------------------------------------------

    stop BGM fadeout 2

    scene bg_1 with Dissolve(2)

    play BGM "audio/W2C - Memories.mp3"

    scene wsis_sleepover_4_wakeup_1_bg
    show wsis_sleepover_4_wakeup_1_char_body
    show wsis_sleepover_4_wakeup_1_wsis_head 1
    show fx_light
    with Dissolve(5)

    pause

    show wsis_sleepover_4_wakeup_1_wsis_head 2
    with dissolve

    pause(0.5)

    show wsis_sleepover_4_wakeup_1_wsis_head 3
    with Dissolve(1)

    pause(1)

    show wsis_sleepover_4_wakeup_1_wsis_head 4
    with dissolve

    show wsis_sleepover_4_wakeup_1_wsis_head 5
    
    pause(1)

    play SE1 "Record Scratch.mp3"
    stop BGM

    show wsis_sleepover_4_wakeup_1_wsis_head 6
    with dissolve

    pause

    scene wsis_sleepover_4_wakeup_2_bg
    show wsis_sleepover_4_wakeup_2_char 1
    show fx_light
    with dissolve

    pause

    play BGM "audio/W2C - Adrenalust.mp3"

    show wsis_sleepover_4_wakeup_2_char 2_cc with Dissolve(1)

    show wsis_sleepover_4_wakeup_2_char 2_wsis
    wsis "What are you doing!?{w=[wt2]} Stop that!"

    show wsis_sleepover_4_wakeup_2_char 2_wnei
    wnei "{aw}Ugh{/aw}{w=[wt1]}, [C_Nam][fnamewsis][C_Off]!{w=[wt2]} How can you be so stubborn at this early morning!?{w=[wt3]} I saw the super duper giga-lollipop-tower first!{w=[wt3]} You should wait your time to play!"

    show wsis_sleepover_4_wakeup_2_char 2_wsis
    wsis "That's not the case!{w=[wt2]} That's not a toy for you to be playing with!{w=[wt3]} Drop it right now!"

    show wsis_sleepover_4_wakeup_2_char 2_wnei
    wnei "No!{w=[wt2]} I'm [C_Nam][fnamewnei]zilla[C_Off]{w=[wt2]}, {aw}the kaiju of the giga-lollipop-tower!{/aw}{w=[wt2]} {bt}Not Ya!{/bt} You should release it!!!"

    show wsis_sleepover_4_wakeup_2_char 2_wsis
    wsis "Is that how you want!?{w=[wt2]} {aw}So I'll make you let it go by force!!!{/aw}"

    $ a_ani_0 = 5

    show wsis_sleepover_4_wakeup_2_char 2

    pause

    mind "(Wait{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} If you continue this{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w} Oh{w=[wt2]}, too late.{w=[wt3]} I can't hold anymore...!)"

    call screen wsis_sleepover_4_wakeup_2_fapada()

    play SE1 "Water Splash 1.mp3"

    scene wsis_sleepover_4_wakeup_2_bg
    show wsis_sleepover_4_wakeup_2_char 2
    show wsis_sleepover_4_wakeup_2_cum
    show fx_light
    with None

    pause(1)

    scene bg_1 with Dissolve(3)

    scene wsis_sleepover_4_wakeup_3_bg
    show fx_light
    with Dissolve(2)

    pause

    mind "(Hmmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}?{w=[wt3]} What's happening{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}?{w=[wt3]} What's that, girls?{w=[wt3]} Why are you soaked with this viscous liquid?{w} {bt}Ahhh...{w=[wt4]} I feel so relaxed...{/bt})"

    $ StartAct("wnei", (("moving", "home"), 0), True)
    $ StartAct("wsis", ("sleeping", 0), True)
    $ StartAct("wnei", ("sleeping", 0), True)
    $ StartAct("wsis", (("staying", "bedroom_wsis"), 10), True)
    $ StartAct("wnei", (("staying", "bedroom_wsis"), 10), True)
    $ wsis_know.remove("Sleepover_Together")
    $ Set_CharMap("hero", "home", "bedroom_wsis")

    scene bg_1 with Dissolve(2)

    return

# ---------------------------------------------------------------------------
screen wsis_sleepover_4_wakeup_2_fapada():
# ---------------------------------------------------------------------------

    vbox:
        xalign 0.5
        yalign 0.9
        spacing 25
        textbutton renpy.translate_string("Finish") action Return() xalign 0.5
        bar:
            value VariableValue("a_ani_0", 10)
            xalign 0.5
            yalign 0.5
            xmaximum 980
            at alpha_dissolve

# ---------------------------------------------------------------------------
image wsis_sleepover_4_wakeup_2_char 1:
# ---------------------------------------------------------------------------
    function SFX_Bounce1
    "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 1_1.webp"
    0.1
    "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 1_2.webp"
    0.1
    "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 1_3.webp"
    0.1
    "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 1_4.webp"
    0.1
    "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 1_5.webp"
    0.1
    "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 1_6.webp"
    0.1
    "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 1_7.webp"
    0.1
    "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 1_8.webp"
    0.1
    repeat

# ---------------------------------------------------------------------------
image wsis_sleepover_4_wakeup_2_char 2 = DynamicSpeedAnimation(
# ---------------------------------------------------------------------------
    [
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 2_cc.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 2_cl.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 2_ll.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 2_lc.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 2_cc.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 2_cr.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 2_rr.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_char 2_rc.webp",
    ],
    speed_fn=lambda: 5 + (a_ani_0 * 2),
    sfx_at={1: SFX_fap2, 5: SFX_fap1},
)

# ---------------------------------------------------------------------------
image wsis_sleepover_4_wakeup_2_cum = DynamicSpeedAnimation(
# ---------------------------------------------------------------------------
    [
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_cum 1.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_cum 2.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_cum 3.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_cum 4.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_cum 5.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_cum 6.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_cum 7.webp",
        "images/Scene/WSIS - Sleepover/wsis_sleepover_4_wakeup_2_cum 8.webp",
    ],
    speed_fn=lambda: 5 + (a_ani_0 * 2),
)
