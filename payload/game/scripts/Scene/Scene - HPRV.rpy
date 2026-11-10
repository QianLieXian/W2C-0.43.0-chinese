#---------------------------------------------------------------------------
label hprv_quest0: # Courtyard
#---------------------------------------------------------------------------
    stop BGM fadeout 1
    call hide_ui from _call_hide_ui_177
    scene bg_0
    with Dissolve(1)

    play BGM "audio/W2C - Tranquility.mp3"

    scene hprv_meeting_1_bg
    show hprv_meeting_1_hprv 1
    with Dissolve(3)

    $ zoomT1 = 0
    $ zoomX1 = -2600
    $ zoomY1 = -500
    $ zoomS1 = 3
    $ zoomT2 = 5
    $ zoomX2 = 0
    $ zoomY2 = 0
    $ zoomS2 = 1
    show hprv_meeting_1_hero at ZoomSTXY_3

    pause(0.5)

    show hprv_meeting_1_hprv 2
    show hprv_meeting_1_hprv_face a0

    pause(0.5)

    show hprv_meeting_1_hprv_face a1

    hprv "Oh{w=[wt2]}, {nm}[fnamehero]{/nm}!{w=[wt2]} I'm glad you came!{w=[wt2]} Come here bro{w=[wt2]}, I need your help!"

    show hprv_meeting_1_hprv_face a0
    hero "O{w=[wt1]}-oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} S{w=[wt1]}-sure."

    # HERO and HPRV sit together
    scene hprv_meeting_2_bg
    show hprv_meeting_2_hero 1
    show hprv_meeting_2_hero_arm 1
    show hprv_meeting_2_hero_mouth o0
    show hprv_meeting_2_hero_eye r
    show hprv_meeting_2_hprv 1
    show hprv_meeting_2_hprv_mouth a0
    show hprv_meeting_2_hprv_eye l
    with Fade(0.5,0.5,2)

    show hprv_meeting_2_hero_mouth a1
    hero "Well{w=[wt2]}, {nm}[fnamehprv]{/nm}, right?{w=[wt2]} What are you doing?"

    show hprv_meeting_2_hero_mouth a0
    show hprv_meeting_2_hprv_mouth a1
    hprv "{gg}Hehehe...{/gg}{w=[wt2]} I've discovered the perfect location for observing the beauty of feminine fashion{w=[wt1]}, if you know what I mean.{w=[wt2]}{nw}"

    show hprv_meeting_2_hero_mouth o0
    show hprv_meeting_2_hprv_mouth a1
    hprv "{gg}Hehehe...{/gg} I've discovered the perfect location for observing the beauty of feminine fashion, if you know what I mean.{fast}{w=[wt2]} I can share my knowledge with you if you want.{w=[wt2]} Just help me with the preparations and I'll show you the ropes!"

    show hprv_meeting_2_hero_eye l
    show hprv_meeting_2_hero_mouth t2
    show hprv_meeting_2_hprv_mouth a0
    hero "Oh{w=[wt1]}, what a shame{w=[wt2]}, I just remember I need to{w=[wt1]}-{nw}"

    show hprv_meeting_2_hero_mouth t0
    show hprv_meeting_2_hprv_mouth a1
    hprv "Great!{w=[wt2]} Then, check this out.{w=[wt2]} I used my physics knowledge to set up a mirror to reflect the perfect view of the balcony from here!{w=[wt3]} Now we can see everything without anyone noticing.{w=[wt3]} Pretty clever, right?"

    show hprv_meeting_2_hero_mouth t1
    show hprv_meeting_2_hprv_mouth a0
    hero "I'm not sure about this..."

    show hprv_meeting_2_hero_eye r
    show hprv_meeting_2_hero_mouth t0
    show hprv_meeting_2_hprv_mouth a1
    hprv "Oh{w=[wt2]}, one more thing!{w=[wt2]} Lend me your phone.{w=[wt3]} You know{w=[wt2]}, I don't have one anymore, remember?{w=[wt3]} With the phone, we see the zoom view of the mirror image with a fixed camera.{w=[wt3]} Besides{w=[wt2]}, If anyone looks here{w=[wt1]}, they'll just see two dudes checking out memes or something.{w=[wt4]} Yes.{w=[wt2]} I know.{w=[wt2]} It's a foolproof plan!"

    show hprv_meeting_2_hero_mouth o1
    show hprv_meeting_2_hprv_mouth a0
    show hprv_meeting_2_hero_arm 2
    hero "Well{w=[wt2]}, are you sure it's just for that?{w=[wt2]} I mean{w=[wt2]}, I don't know..."

    show hprv_meeting_2_hero_arm 1
    show hprv_meeting_2_hero_mouth o0
    show hprv_meeting_2_hprv 2
    show hprv_meeting_2_hprv_mouth a3
    hide hprv_meeting_2_hprv_eye
    hprv "Of course!{w=[wt2]}{nw}"

    # Takes HERO phone

    hprv "Of course!{fast}{w=[wt3]} In addition{w=[wt2]}, we can also take good shots!"

    show hprv_meeting_2_hero_mouth s3
    show hprv_meeting_2_hprv_mouth a2
    hero "W{w=[wt1]}-wait!{w=[wt3]} So you were really planning that!"

    show hprv_meeting_2_hero_mouth s2
    show hprv_meeting_2_hero_eye c
    show hprv_meeting_2_hprv_mouth a3
    hprv "Alright{w=[wt2]}, let's just adjust it here and there{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} And{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
    hprv "Alright, let's just adjust it here and there... And...{fast} Done!{w=[wt2]} It's ready!{w=[wt4]} Oh{w=[wt2]}, just in time!{w=[wt2]} Look!"

    stop BGM fadeout 3

    $ a_event_0 = []

    # WPRE appears in the balcony, holding the railing while looking at the courtyard view, wearing a white panthose.
    scene hprv_meeting_3_bg
    show hprv_meeting_3_wpre
    show hprv_meeting_3_fg
    show hprv_meeting_3_fx
    with fade

    menu:
        "{nm}[fnamewpre]{/nm} appears on the balcony."
        "Watch":
            play BGM "audio/W2C - SexyVibes.mp3"
            hide hprv_meeting_3_fx with dissolve
            $ a_event_0.append("WPRE")
            $ add_stat("hprv", "love", 2)
            $ add_stat("hero", "cha_soc", 2)

            hprv "{bt}Holy scholarship!{/bt}{w=[wt2]} Our class prez is rocking the {i}''innocent librarian''{/i} look!{w=[wt3]} Those white pantyhose are like the blank pages of knowledge just waiting to be filled!"
            hero "That's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} an interesting way to put it."
            hprv "Trust me{w=[wt2]}, I'm a connoisseur of fine literature!{w=[wt2]} ...And finer legs!{w=[wt3]} Look at how those long{w=[wt1]}, slender limbs disappear into that misty white veil.{w=[wt2]} The difference between bare legs and a transparent material like this{w=[wt1]}, is that the material serves only to further highlight what would be covered!"
            hero "I'm pretty sure that's not what {nm}[fnamewpre]{/nm} had in mind when she got dressed this morning."
            hprv "Ah{w=[wt1]}, but that's the beauty of it!{w=[wt3]} The modest exterior hiding depths of mystery.{w=[wt3]} Just as expected of our diligent class president!{w=[wt3]} I bet she color-codes her study notes just like she color-coordinates her undergarments.{w=[wt3]} Precision in all things, my friend!"

            scene hprv_meeting_2_bg
            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hero_eye c
            show hprv_meeting_2_hprv 1
            show hprv_meeting_2_hprv_mouth a0
            show hprv_meeting_2_hprv_eye c
            with Fade(0.25, 0, 0.25)

            show hprv_meeting_2_hero_mouth o1
            hero "G{w=[wt1]}-got it."

            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hprv_mouth a1

        "Cover the view":
            play BGM "audio/W2C - Awkward.mp3"
            scene hprv_meeting_2_bg at Shake
            show hprv_meeting_2_hprv 1 at Shake
            show hprv_meeting_2_hprv_mouth s0 at Shake
            show hprv_meeting_2_hprv_eye 0 at Shake
            show hprv_meeting_2_hero 2 at Shake
            show hprv_meeting_2_hero_mouth s0 at Shake
            with dissolve

            $ add_stat("wpre", "bonus", 10)

            show hprv_meeting_2_hero_mouth s1
            hero "W{w=[wt1]}-wait!{w=[wt2]} We can't do that to her!"

            show hprv_meeting_2_hero_mouth s0
            show hprv_meeting_2_hprv_mouth s1
            hprv "{aw}Ehhh...!?{/aw}{w=[wt3]} But it's a masterpiece of modesty!{w=[wt2]} A canvas of purity!"

            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hero_eye r
            show hprv_meeting_2_hprv_mouth s0
            show hprv_meeting_2_hprv_eye l
            with dissolve

            show hprv_meeting_2_hero_mouth s3
            hero "I think that's not right!{w=[wt3]} She seems to be a very decent girl."

            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hprv_mouth s1
            hprv "{bt}Ehhhh...?{/bt}{w=[wt4]}{nw}"

            show hprv_meeting_2_hprv_mouth a1
            hprv "{bt}Ehhhh...?{/bt}{fast} Ah{w=[wt2]}, I see how it is!{w=[wt3]} You're into the {i}''smart girl''{/i} type, eh?{w=[wt3]} No worries{w=[wt2]}, your secret's safe with me, bro!{w=[wt3]} But let me tell you{w=[wt2]}, her soul is practically begging{w=[wt2]}, {i}''Someone please light the fire that exists within me!!!''{/i}"

            show hprv_meeting_2_hero_mouth o1
            show hprv_meeting_2_hprv_mouth a0
            hero "I'm pretty sure her soul would completely put out that fire if it found the way you intend to light it!"

            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hprv_eye r
            pause(0.5)

            scene hprv_meeting_2_bg
            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hero_eye r
            show hprv_meeting_2_hprv 2
            show hprv_meeting_2_hprv_mouth a2

            pause(0.2)

            scene hprv_meeting_2_bg at Shake
            show hprv_meeting_2_hero 1 at Shake
            show hprv_meeting_2_hero_arm 1 at Shake
            show hprv_meeting_2_hero_mouth o0 at Shake
            show hprv_meeting_2_hero_eye r at Shake
            show hprv_meeting_2_hprv 2 at Shake
            show hprv_meeting_2_hprv_mouth a2 at Shake

            pause(0.2)

            show hprv_meeting_2_hprv_mouth a3

    hprv "By the way{w=[wt2]}, {bt}look who's coming now!{/bt}"

    # WDIS appears in the balcony, on her back, wearing white panties with red polka dots that are entering in her butt. She's talking to WOTA, who appears on her front, doing a weird chunnybious pose, wearing panties with white and blue stripes.
    scene hprv_meeting_3_bg
    show hprv_meeting_3_wota
    show hprv_meeting_3_wdis
    show hprv_meeting_3_fg
    show hprv_meeting_3_fx
    with fade

    menu:
        "{nm}[fnamewdis]{/nm} and {nm}[fnamewota]{/nm} appear on the balcony."
        "Watch":
            if not "WPRE" in a_event_0:
                play BGM "audio/W2C - SexyVibes.mp3"
            hide hprv_meeting_3_fx with dissolve
            $ a_event_0.append("WDIS")
            $ add_stat("hprv", "love", 2)
            $ add_stat("hero", "cha_soc", 2)

            hprv "{bt}Wooow!{w=[wt2]} Great galaxies of glorious undergarments!{/bt}{w=[wt2]} It's like a clash of alternate universes down there!"
            hero "What are you talking about?"
            hprv "Open your third eye, my uninitiated friend!{w=[wt2]} We're witnessing the convergence of cosmic fashion!{w=[wt3]} First{w=[wt2]}, feast your eyes on {nm}[fnamewdis]{/nm}'s magnificent rear!{w=[wt2]} Those white panties with red polka dots are like a map of her scattered thoughts!"
            hero "What?"
            hprv "Look!{w=[wt2]} They're not just dots, my friend.{w=[wt2]} They're the chaotic particles of her adorable{w=[wt1]}, bumbling charm{w=[wt1]}, bouncing around in a quantum state of perpetual embarrassment!{w=[wt3]} See how they're slowly being devoured by the black hole of her buttocks?"
            hero "Uh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} That's certainly an{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Interesting interpretation."
            hprv "But wait{w=[wt2]}, there's more!{w=[wt3]} Shift your gaze to our cryptic {nm}[fnamewota]{/nm}!{w=[wt2]} Behold her mystical pose!{w=[wt2]} It's as if she's channeling the very essence of her realm!{w=[wt3]} The white stripes represent the purity of her soul{w=[wt1]}, while the blue is clearly the color of the mana that fuels her magical powers!"
            hero "I see..."
            hprv "It's like watching two parallel universes collide in a spectacular display of cotton and elastic!"
            hero "Well{w=[wt2]}, you really put a lot of thought into this, huh?"
            hprv "My dear {nm}[fnamehero]{/nm}{w=[wt2]}, this isn't mere thought.{w=[wt2]} This is the culmination of years of dedicated research and observation!{w=[wt2]} We're not just looking at undergarments.{w=[wt2]} We are unraveling the most intimate aspects of girls from the fabric analysis of their garments!"

            scene hprv_meeting_2_bg
            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hero_eye c
            show hprv_meeting_2_hprv 1
            show hprv_meeting_2_hprv_mouth a0
            show hprv_meeting_2_hprv_eye c
            with Fade(0.25, 0, 0.25)

            show hprv_meeting_2_hero_mouth o1

            hero "G{w=[wt1]}-got it."

            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hprv_mouth a1

        "Cover the view":
            if "WPRE" in a_event_0:
                play BGM "audio/W2C - Awkward.mp3"
            scene hprv_meeting_2_bg at Shake
            show hprv_meeting_2_hprv 1 at Shake
            show hprv_meeting_2_hprv_mouth s0 at Shake
            show hprv_meeting_2_hprv_eye 0 at Shake
            show hprv_meeting_2_hero 2 at Shake
            show hprv_meeting_2_hero_mouth s0 at Shake
            with dissolve

            $ add_stat("wdis", "bonus", 5)
            $ add_stat("wota", "bonus", 5)

            show hprv_meeting_2_hero_mouth s1
            show hprv_meeting_2_hprv_mouth s0
            hero "Wait!{w=[wt2]} That's not cool."

            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hero_eye r
            show hprv_meeting_2_hprv_mouth s0
            show hprv_meeting_2_hprv_eye 0
            with dissolve

            show hprv_meeting_2_hprv_mouth s1
            hprv "{aw}Ehhh...!?{/aw}{w=[wt2]} C'mon man{w=[wt2]}, the chubby ones also have their charm!"

            show hprv_meeting_2_hero_mouth s3
            show hprv_meeting_2_hprv_eye l
            show hprv_meeting_2_hprv_mouth s0
            hero "{aw}That's not what I meant!{/aw}{w=[wt3]} We just can't invade their privacy like that."

            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hprv_mouth s1
            hprv "{bt}Ehhhh...?{/bt}{w=[wt4]}{nw}"

            show hprv_meeting_2_hprv_mouth a1
            hprv "{bt}Ehhhh...?{/bt}{fast} Oho!{w=[wt2]} I see you're a guardian of the multiversal barriers!{w=[wt3]} Fear not{w=[wt2]}, your secret heroism is safe with me{w=[wt1]}, dimensional protector!"

            show hprv_meeting_2_hprv_mouth o1
            hprv "But consider this{w=[wt2]}: {nm}[fnamewdis]{/nm}'s polka dots are like her countless disastrous attempts to get things done{w=[wt2]}; and {nm}[fnamewota]{/nm}'s stripes are the very bars that separate our mundane world from her mystical universe!{w=[wt3]} By averting our gaze{w=[wt1]}, {b}aren't we closing the portal to untold adventures!?{/b}"

            show hprv_meeting_2_hprv_mouth o2
            hprv "{pa}Not observing such events is like giving up science!{/pa}"

            show hprv_meeting_2_hero_mouth a1
            show hprv_meeting_2_hprv_mouth o0
            hero "For now{w=[wt2]}, let's just stick to the theoretical part of science.{w=[wt2]} Maybe your field research seems a little inappropriate."

            show hprv_meeting_2_hero_mouth a0
            show hprv_meeting_2_hprv_eye r
            pause(0.5)

            scene hprv_meeting_2_bg
            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hero_eye r
            show hprv_meeting_2_hprv 2
            show hprv_meeting_2_hprv_mouth a2

            pause(0.2)

            scene hprv_meeting_2_bg at Shake
            show hprv_meeting_2_hero 1 at Shake
            show hprv_meeting_2_hero_arm 1 at Shake
            show hprv_meeting_2_hero_mouth o0 at Shake
            show hprv_meeting_2_hero_eye r at Shake
            show hprv_meeting_2_hprv 2 at Shake
            show hprv_meeting_2_hprv_mouth a2 at Shake

            pause(0.2)

            show hprv_meeting_2_hprv_mouth a3

    hprv "{bt}Wait!{/bt}{w=[wt2]} Speaking of multiverse{w=[wt2]}, a big event just happened right now!!!{w=[wt3]} Those two beauties decided to leave to feel the presence of something even greater!!!"

    # WGAL appears in the balcony, on her back, wearing high-waisted lace panties, talking with WRIC, who appears on her front, wearing a white pantyhose that covers pink princess-like panties.
    scene hprv_meeting_3_bg
    show hprv_meeting_3_wric
    show hprv_meeting_3_wgal
    show hprv_meeting_3_fg
    show hprv_meeting_3_fx
    with fade

    menu:
        "{nm}[fnamewgal]{/nm} and {nm}[fnamewric]{/nm} appear on the balcony."
        "Watch":
            if not "WDIS" in a_event_0:
                play BGM "audio/W2C - SexyVibes.mp3"
            hide hprv_meeting_3_fx with dissolve
            $ a_event_0.append("WGAL")
            $ add_stat("hprv", "love", 2)
            $ add_stat("hero", "cha_soc", 2)

            hprv "{aw}Gah!{/aw}{w=[wt2]} Damn {nm}[fnamewota]{/nm}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} So the panty-less rumor was just another of her elaborate pranks!{w=[wt3]} I should've known better than to trust that little blind bitch!"
            hero "Wait{w=[wt2]}, what were you expecting to see?"
            hprv "{aw}(sigh...){/aw}{w=[wt3]} You're absolutely right!{w=[wt3]} I don't have time to feel bad.{w=[wt3]} There's a great show of lace and spandex being performed just in front of us!!!"
            hero "Well{w=[wt2]}, that's a good way to say it."
            hprv "Of course!{w=[wt2]} Open your eyes to the grand tapestry before us!{w=[wt3]} First{w=[wt2]}, feast your eyes upon the magnificent {nm}[fnamewgal]{/nm}'s bottom!{w=[wt3]} That's not mere underwear{w=[wt2]}, it's a manifesto!"
            hprv "And those curves!{w=[wt2]} The lace hugs them like a desperate lover{w=[wt2]}, afraid to let go!{w=[wt3]} It screams{w=[wt2]}, {i}''Watch, losers!{w=[wt2]} You can have the honor of admiring my beautiful curves through this thin fabric!''{/i}"
            hero "Well{w=[wt2]}, as I recall{w=[wt2]}, the last time you tried to have this honor{w=[wt2]}, she didn't seem to be that happy about it."
            hprv "Now{w=[wt2]}, look at how that platinum blonde hair cascades down {nm}[fnamewric]{/nm}'s delicate back{w=[wt2]}, almost touching those pantyhose.{w=[wt3]} It's like watching a waterfall of moonlight spilling over a snow-capped mountain!{w=[wt3]} Ah{w=[wt2]}, what a sight to behold!"
            hprv "Those princess panties peeking through that gossamer veil of pantyhose{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} It's like a metaphor for her entire existence!{w=[wt3]} {i}''I'm royalty''{/i}{w=[wt1]}, they say{w=[wt2]}, {i}''but I'm not afraid to let the common peasant like you get a tantalizing glimpse of my majesty!''{/i}"
            hero "I'm pretty sure she'd be horrified to know anyone's getting a glimpse of anything."

            if "WPRE" in a_event_0:
                $ add_stat("hprv", "love", 2)
                $ add_stat("hero", "cha_soc", 2)
                hprv "For better reading purposes{w=[wt2]}, it is worth making a brief comparison between this pantyhose and the one noted earlier.{w=[wt3]} Although both are white{w=[wt2]}, the appearances are completely different!{w=[wt2]} This underscores the shapes through its strong glow{w=[wt1]}, exuding royalty!"
                hero "That's a good point."

            scene hprv_meeting_2_bg
            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hero_eye c
            show hprv_meeting_2_hprv 1
            show hprv_meeting_2_hprv_mouth a0
            show hprv_meeting_2_hprv_eye c
            with Fade(0.25, 0, 0.25)

            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hprv_mouth o1
            hprv "Oh{w=[wt1]}, no!{w=[wt2]} They're already leaving{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} But why did they seem so upset?{w=[wt4]}{nw}"

            show hprv_meeting_2_hprv_mouth a1
            hprv "Oh, no! They're already leaving... But why did they seem so upset?{fast} W{w=[wt1]}-wait!{w=[wt2]} That's it!{w=[wt2]} They just went out so that the supreme beauty could shine!!!"
            show hprv_meeting_2_hprv_mouth a0

        "Cover the view":
            if "WDIS" in a_event_0:
                play BGM "audio/W2C - Awkward.mp3"
            scene hprv_meeting_2_bg at Shake
            show hprv_meeting_2_hprv 1 at Shake
            show hprv_meeting_2_hprv_mouth s0 at Shake
            show hprv_meeting_2_hprv_eye 0 at Shake
            show hprv_meeting_2_hero 2 at Shake
            show hprv_meeting_2_hero_mouth s0 at Shake
            with dissolve

            $ add_stat("wgal", "bonus", 5)
            $ add_stat("wric", "bonus", 5)

            show hprv_meeting_2_hero_mouth s1
            hero "Wait{w=[wt1]}, no!"

            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hero_eye r
            show hprv_meeting_2_hprv_mouth s0
            show hprv_meeting_2_hprv_eye 0
            with dissolve

            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hprv_mouth s1
            hprv "{aw}Ehhh...!?{/aw}{w=[wt3]} You dare interrupt this grand tale of royality{w=[wt2]}, written in the language of undies!?"

            show hprv_meeting_2_hero_mouth s3
            show hprv_meeting_2_hprv_eye l
            show hprv_meeting_2_hprv_mouth o0
            hero "I don't think it's right to do that to them."

            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hprv_mouth a1
            hprv "Oh{w=[wt2]}, sweet summer child{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Who knew you'd be the knight in shining armor for the queen bee?{w=[wt3]} So this means {nm}[fnamehriv]{/nm} might have competition in the chivalry department!{w=[wt2]} Interesting..."

            show hprv_meeting_2_hprv_mouth a0
            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hprv_eye r
            pause(0.5)

            show hprv_meeting_2_hprv_mouth o1
            hprv "Oh{w=[wt1]}, no!{w=[wt2]} They're already leaving{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} But why did they seem so upset?{w=[wt4]}{nw}"

            scene hprv_meeting_2_bg
            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth o0
            show hprv_meeting_2_hero_eye r
            show hprv_meeting_2_hprv 2
            show hprv_meeting_2_hprv_mouth a2

            pause(0.2)

            scene hprv_meeting_2_bg at Shake
            show hprv_meeting_2_hero 1 at Shake
            show hprv_meeting_2_hero_arm 1 at Shake
            show hprv_meeting_2_hero_mouth o0 at Shake
            show hprv_meeting_2_hero_eye r at Shake
            show hprv_meeting_2_hprv 2 at Shake
            show hprv_meeting_2_hprv_mouth a2 at Shake

            pause(0.2)

            show hprv_meeting_2_hprv_mouth a3
            hprv "Oh, no! They're already leaving... But why did they seem so upset?{fast} W{w=[wt1]}-wait!{w=[wt2]} That's it!{w=[wt2]} They just went out so that the supreme beauty could shine!!!"
            show hprv_meeting_2_hprv_mouth a2

    show hprv_meeting_2_hero_mouth o1
    show hprv_meeting_2_hero_eye c
    hero "Hm?{w=[wt2]} What{w=[wt1]}-{nw}"

    # WSIS appears in the balcony, holding a soda can while looking at the courtyard view, wearing a black pantyhose.
    scene hprv_meeting_3_bg
    show hprv_meeting_3_wsis
    show hprv_meeting_3_fg
    show hprv_meeting_3_fx
    with fade

    menu:
        "{nm}[fnamewsis]{/nm} appears on the balcony."
        "Watch":
            if not "WGAL" in a_event_0:
                play BGM "audio/W2C - SexyVibes.mp3"
            hide hprv_meeting_3_fx with dissolve
            $ a_event_0.append("WSIS")
            $ add_stat("hprv", "love", 2)
            $ add_stat("hero", "cha_soc", 2)

            hprv "Man{w=[wt2]}, {nm}[fnamewsis]{/nm} is the pinnacle of perfection!{w=[wt3]} Look at those curves man{w=[wt2]}, they're like the silhouette of a midnight goddess!{w=[wt3]} That black pantyhose?{w=[wt2]} It's like staring into the abyss{w=[wt2]}, and let me tell you{w=[wt2]}, the abyss stares back!{w=[wt3]} And it's breathtaking!"
            hprv "Oh man{w=[wt2]}, this girl is so wonderful{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I wonder how it would feel to be that soda can{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Pressed against those luscious lips{w=[wt2]}, feeling the warmth of her breath..."

            scene hprv_meeting_2_bg
            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hero_eye c
            show hprv_meeting_2_hprv 1
            show hprv_meeting_2_hprv_mouth a0
            show hprv_meeting_2_hprv_eye c
            with Fade(0.25, 0, 0.25)

        "Cover the view":
            if "WGAL" in a_event_0:
                play BGM "audio/W2C - Awkward.mp3"
            scene hprv_meeting_2_bg at Shake
            show hprv_meeting_2_hprv 1 at Shake
            show hprv_meeting_2_hprv_mouth s0 at Shake
            show hprv_meeting_2_hprv_eye 0 at Shake
            show hprv_meeting_2_hero 2 at Shake
            show hprv_meeting_2_hero_mouth s0 at Shake
            with dissolve

            $ add_stat("wsis", "bonus", 10)

            show hprv_meeting_2_hero_mouth s1
            hero "Stop!{w=[wt2]} That's {nm}[fnamewsis]{/nm}!{w=[wt3]} From what I remember{w=[wt1]}, you told her you wouldn't do something like that to her!"

            show hprv_meeting_2_hero 1
            show hprv_meeting_2_hero_arm 1
            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hero_eye r
            show hprv_meeting_2_hprv_mouth s0
            show hprv_meeting_2_hprv_eye 0
            with dissolve

            show hprv_meeting_2_hprv_mouth s1
            hprv "C'mon man!{w=[wt2]} The siren song of the dark pantyhose calls to me!{w=[wt3]} Didn't she say she couldn't care less?{w=[wt2]} That's practically an invitation!"

            show hprv_meeting_2_hprv_eye l
            show hprv_meeting_2_hprv_mouth o0
            show hprv_meeting_2_hero_mouth s3
            hero "No{w=[wt2]}, it's absolutely not."

            show hprv_meeting_2_hprv_mouth o1
            show hprv_meeting_2_hero_mouth s2
            hprv "But think about it!{w=[wt2]} The contrast between her pale skin and that inky black fabric{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} It's like watching a solar eclipse!{w=[wt3]} A once-in-a-lifetime spectacle of celestial beauty!{w=[wt3]} You're depriving me of a divine masterpiece!!!"

            show hprv_meeting_2_hero_eye l

    show hprv_meeting_2_hprv_eye l
    show hprv_meeting_2_hprv_mouth o0
    hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

    show hprv_meeting_2_hprv_mouth a4
    hprv "{aw}W{w=[wt1]}-well{/aw}{w=[wt2]}, I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm sorry, dude!{w=[wt3]} Now I remember you're kinda close, right?{w=[wt3]} She's the most beautiful girl in the school{w=[wt1]}, so{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I just couldn't control my urges.{w=[wt3]} Well{w=[wt2]}, I don't know if she's your girlfriend or something like{w=[wt2]}, but{w=[wt2]}, sorry man."

    show hprv_meeting_2_hprv_mouth o0
    show hprv_meeting_2_hero_mouth s2
    show hprv_meeting_2_hero_eye l with dissolve

    menu:
        "Say that you have no relationship with {nm}[fnamewsis]{/nm}":

            $ add_stat("wsis", "bonus", -10)
            $ hprv_know.append("WSIS_IS_Acquaintance")

            show hprv_meeting_2_hero_mouth s3
            hero "I have nothing to do with her."
            
            $ add_stat("hprv", "love", 2)
            $ add_stat("hero", "cha_soc", 2)

            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hprv_mouth a1
            hprv "R{w=[wt1]}-really!?{w=[wt3]} Does that mean she's free for me?{w=[wt3]} Oh, guy!{w=[wt2]} I'm so luck!"

            show hprv_meeting_2_hero_mouth t1
            show hprv_meeting_2_hprv_mouth a0
            hero "Well{w=[wt1]}, I guess I could say she wouldn't waste her life like that."

            show hprv_meeting_2_hero_mouth t0
            show hprv_meeting_2_hprv_mouth a1
            hprv "Hope is the last that dies, bro!{w=[wt2]} I still have time to win her heart!"

        "Say that {nm}[fnamewsis]{/nm} is your step-sister":

            $ add_stat("wsis", "bonus", 5)
            $ hprv_know.append("WSIS_IS_Stepsister")

            show hprv_meeting_2_hero_mouth s3
            hero "She's my step-sister."

            $ add_stat("hprv", "love", -1)
            $ add_stat("hero", "cha_soc", -1)

            show hprv_meeting_2_hero_mouth s2
            hprv "{w=[wt2]}.{w=[wt2]} .{w=[wt2]} .{w=[wt4]}{nw}"

            show hprv_meeting_2_hprv_mouth o2
            hprv ". . .{fast} {pa}EHHHH!?!?!?{/pa}"

            show hprv_meeting_2_hprv_mouth a4
            hprv "{bt}Wait! Wait! Wait!{/bt}{w=[wt3]} Are you saying you're the stepbrother of that goddess!?{w=[wt3]} Do you guys live together!?{w=[wt2]} Has she already shouted {bt}{i}''stepbro{w=[wt1]}, help!''{/i}{/bt} while she was stuck in the washing machine!?"

            show hprv_meeting_2_hero_mouth s3
            show hprv_meeting_2_hero_eye r
            show hprv_meeting_2_hprv_mouth o0
            hero "{aw}Ehhh!?!?!?{/aw}"

            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hprv_mouth o1
            hprv "Oh, man!{w=[wt2]} I'm so jealous of you!{w=[wt3]} You're probably the luckiest guy in the world!"

        "Say that {nm}[fnamewsis]{/nm} is your sister":

            $ add_stat("wsis", "bonus", 10)
            $ hprv_know.append("WSIS_IS_Sister")

            show hprv_meeting_2_hero_mouth s3
            hero "She's my sister."

            $ add_stat("hprv", "love", -2)
            $ add_stat("hero", "cha_soc", -2)

            show hprv_meeting_2_hero_mouth s2
            hprv "{w=[wt2]}.{w=[wt2]} .{w=[wt2]} .{w=[wt4]}{nw}"

            show hprv_meeting_2_hprv_mouth o2
            hprv ". . .{fast} {pa}EHHHH!?!?!?{/pa}"

            show hprv_meeting_2_hprv_mouth o1
            hprv "{bt}Wait! Wait! Wait!{/bt}{w=[wt3]} Are you saying you're the brother of that goddess!?{w=[wt3]} Do you guys live together!?{w=[wt3]} Have you ever seen her naked!?"

            show hprv_meeting_2_hero_mouth s3
            show hprv_meeting_2_hero_eye r
            show hprv_meeting_2_hprv_mouth o0
            hero "{aw}Ehhh!?!?!?{/aw}"

            show hprv_meeting_2_hero_mouth s2
            show hprv_meeting_2_hprv_mouth a4
            hprv "Oh, man!{w=[wt2]} I'm so jealous of you!{w=[wt3]} You're probably the luckiest guy in the world!{w=[wt2]} Why don't you introduce me to your sister?{w=[wt2]} We can be brothers-in-law!{w=[wt3]} Have you ever thought that would be cool?"

            show hprv_meeting_2_hero_eye l
            show hprv_meeting_2_hero_mouth t1
            show hprv_meeting_2_hprv_mouth o0
            hero "I wouldn't let my sister waste her life like that."

            show hprv_meeting_2_hero_mouth t0

        "Stay silent":
            pass

    show hprv_meeting_2_hprv_mouth a1
    show hprv_meeting_2_hprv_eye l
    hprv "By the way{w=[wt2]}, break's almost over, bro.{w=[wt3]} We should head back.{w=[wt3]} Thank you for joining me in my beauty research.{w=[wt3]} We should do that again!"

    show hprv_meeting_2_hprv_mouth a0
    show hprv_meeting_2_hero_mouth o0
    show hprv_meeting_2_hero_eye r with dissolve

    show hprv_meeting_2_hero_mouth o1
    hero "Well{w=[wt2]}, I don't know..."

    show hprv_meeting_2_hprv_mouth a1
    show hprv_meeting_2_hero_mouth o0
    hprv "Think about it{w=[wt2]}, we are in a vast kitchen where we can contemplate different forms of beauty every day.{w=[wt3]} Giving up this is throwing away the grace we were given!{w=[wt3]} Therefore{w=[wt2]}, we must taste each food feeling every detail of its flavor!"
    hprv "So{w=[wt2]}, that's it!{w=[wt2]} I'm going ahead.{w=[wt3]} See you, bro!"
    show hprv_meeting_2_hprv_mouth a0

    scene bg_0 with dissolve

    hero "Wait!"

    scene bg_1
    show hprv_meeting_4_bg # HERO and HPRV are facing each other.
    show hprv_meeting_4_hprv
    show hprv_meeting_4_hprv_face o0
    show hprv_meeting_4_hero
    with Dissolve(1)

    hprv "Hmmm?"
    hero "I'm just curious{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} About{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} T{w=[wt1]}-the kitchen you told."

    show hprv_meeting_4_hprv_face a1
    hprv "It seems that you are finally beginning to understand my feelings!{w=[wt3]} Shoot, brother!{w=[wt3]} I'll just answer whatever you wanna know!"
    stop BGM fadeout 3

    show hprv_meeting_4_hprv_face o0
    hero "What if you see different ingredients on the dish?"

    show hprv_meeting_4_hprv_face a2
    hprv "{aw}Ehh?{/aw}"

    show hprv_meeting_4_hprv_face a0
    hero "You know{w=[wt2]}, what if you realize that that soft{w=[wt1]}, juicy orange you were dying to eat{w=[wt2]}, was actually a very huge{w=[wt1]}, hard banana?{w=[wt3]} Would you throw it away?"

    show hprv_meeting_4_hprv_face o0 with dissolve
    show hprv_meeting_4_hprv_fx with Dissolve(2)

    $ Z_alp = 0.75
    scene bg_0
    with Dissolve(2)

    play BGM "audio/W2C - MainTheme (EPIC).mp3" fadein 5

    show hprv_meeting_5_hprv
    show hprv_meeting_5_hprv_face o0
    show hprv_meeting_5_fx1
    show hprv_meeting_5_fx2 at Opacity:
        blend "multiply"
    with Dissolve(4)

    pause(1)

    show hprv_meeting_5_hprv_face a0

    pause(1)

    scene bg_1
    $ X_spd = 15
    $ Z_alp = 0.25
    show hprv_meeting_5_bg at Parallax
    show hprv_meeting_5_hprv
    show hprv_meeting_5_hprv_face a0
    hide hprv_meeting_5_fx1
    show hprv_meeting_5_fx2 at Opacity:
        blend "multiply"
    show hprv_meeting_5_fg 1
    show hprv_meeting_5_fx:
        blend "add"
    with Dissolve(5)

    $ WindowOpacity = 0

    show hprv_meeting_5_hprv_face a1
    show hprv_meeting_5_fx2 at Opacity
    hprv "{size=+20}{b}Nah{w=[wt2]}, I'd taste.{/b}{/size}"

    $ WindowOpacity = 1

    show hprv_meeting_5_hprv_face a0

    if preferences.wahu == False:
        scene bg_1 with Dissolve(2)

    else:

        pause # Dramatic pause for humor purposes

        hprv "So.{w=[wt2]} That's it{w=[wt2]}, bro.{w=[wt3]} See ya!"

        scene hprv_meeting_5_bg with dissolve # HPRV and WAHU bump into each other 

        scene hprv_meeting_6_bg with dissolve # HPRV and WAHU are droopy, his hand is on her breasts

        hero "(How did his hand end up there instead of breaking his fall?)"

        scene hprv_meeting_7_bg with dissolve

        # scene hprv_meeting_bg8 # View of WAHU big volume on panties

        pause

        # scene hprv_meeting_bg9 # WAHU runs away

        wahu "I{w=[wt1]}-I'm so sorry!"

#---------------------------------------------------------------------------
    scene bg_0
    with Dissolve(2)

    $ add_stat("hprv", "inti", 3)

    $ hprv_quest_1 = 1

    call gametime_schoolnext from _call_gametime_schoolnext_4
    $ gametimemin += _return
    call gametime from _call_gametime_98

    pause

    $ msg.msg(renpy.translate_string("[C_Nam][fnamehprv][C_Off] is now unlocked"))

    play BGM "audio/W2C - Tranquility.mp3"
    
    $ Set_CharMap("hero", "school", "courtyard")
    call check_playermap from _call_check_playermap_34
    jump show_ui
#---------------------------------------------------------------------------
