image wnei_kiss:
    function SFX_Kiss
    0.15
    function SFX_GigA
    0.15
    function SFX_Kiss
    0.3
    function SFX_Kiss
    0.3
    function SFX_Kiss
    0.3
    function SFX_Kiss
    0.3
    repeat

#---------------------------------------------------------------------------
label wnei_quest_0_1: # Watching TV
#---------------------------------------------------------------------------

    scene wnei_watchtv_2_bg
    if Check_CharSameMap("wsis", "hero"):
        show wnei_watchtv_2_wsis
    show wnei_watchtv_2_wnei
    show wnei_watchtv_2_hero
    with Fade(0.5, 0.5, 2)

    $ gametimemin += 60
    $ add_stat("wnei", "inti", 0.6)
    if Check_CharSameMap("wsis", "hero"):
        $ add_stat("wsis", "inti", 0.6)
    call gametime from _call_gametime_109

    pause
    
    jump show_ui

#---------------------------------------------------------------------------
label wnei_quest_0_0: # Watching TV
#---------------------------------------------------------------------------

    $ hero_mood = "O1"
    hero "Ehh?{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} Cartoon?{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} won't it be boring?"
    wnei "Of course not!{w=[wt2]} It's {bt=a5-s2}{b}SUPER DUPER COOL!!!{/b}{/bt}{w=[wt3]} Ya'll see!"

    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night
    scene bg_0
    with dissolve
    stop BGM fadeout 10

    mind "(Oh,{w=[wt1]} cool!{w=[wt2]} {nm}[hero_about_wsis!c]{/nm} joined us!{w=[wt3]} Maybe I don't have to suffer alone.{w=[wt4]} Wait{w=[wt2]}, what?{w=[wt3]} Did she also like it!?{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} here we go then...)"

    play BGM "audio/W2C - Awkward.mp3"

    scene wnei_watchtv_1_bg at ZoomL2R
    show wnei_watchtv_1_wsis 1 at ZoomL2R
    show wnei_watchtv_1_hero_wnei 1 at ZoomL2R
    show wnei_watchtv_1_fg at ZoomL2R
    with dissolve

    mind "(Wow!{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} that scene was awesome!!!{w=[wt3]} I never thought I'd enjoy something {nm}[fnamewnei]{/nm} recommended this much,{w=[wt1]} but still{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I don't know if I can say she was right{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} since she is the one who seems {bt}BORED THE MOST!{/bt})"
    wnei "Hey, {nm}[fnamehero]{/nm}!{w=[wt2]} Lemme see if ya have cool games on yar phone!"

    scene wnei_watchtv_1_bg
    show wnei_watchtv_1_wsis 2
    show wnei_watchtv_1_hero_wnei 2
    show wnei_watchtv_1_fg
    with dissolve
    pause (1)

    wnei "Is it here?"
    hero "{aw}W{w=[wt1]}-wait!{/aw}"
    wnei "It's not{w=[wt1]}-.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} {bt=a2-s2-p20}{b}Ehh!?{/b}{/bt}{w=[wt2]} Is dat yar {gradient2=4-#FFAFAF-#FFFFAF-10-#FFFFAF-#AFFFFF-10-#AFFFFF-#AFAFFF-10-#AFAFFF-#FFAFAF-10}{b}lollipop{/b}{/gradient2}!?{w=[wt3]} Did it grows dat much!?"
    $ msg.msg(renpy.translate_string("{nm}[fnamewsis]{/nm}'s  lust {color=#32FF32}+")+str(1 * lustadd_wsis)[:4])
    $ add_stat("wsis", "lust", 1)
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."
    wnei "C'mon!{w=[wt1]} Lemme see it!"
    $ msg.msg(renpy.translate_string("{nm}[fnamewsis]{/nm}'s  lust {color=#32FF32}+")+str(1 * lustadd_wsis)[:4])
    $ add_stat("wsis", "lust", 1)
    hero "{pa}EHHH!?!?{/pa}"
    wnei "Hurry!{w=[wt1]} Gimme yar phone!!!"
    hero "{aw}O{w=[wt1]}-oh!{w=[wt2]} The p{w=[wt1]}-phone!{w=[wt2]} s{w=[wt1]}-s{w=[wt1]}-sure!{w=[wt3]} I{w=[wt1]}-it's here on the other p{w=[wt1]}-pocket!{/aw}"
    wnei "{bt}Yaaay!!!{/bt}"

    $ add_stat("wnei", "love", 2)
    $ add_stat("hero", "cha_soc", 2)

    show wnei_watchtv_1_wsis 3
    show wnei_watchtv_1_hero_wnei 3
    with dissolve

    mind "({w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} For a moment{w=[wt1]}, I thought something else was gonna happen{w=[wt2]}, and I'm not sure if I was ready for that.)"
    
    scene bg_0
    with Dissolve(1)

    mind "({pa}WAIT!{w=[wt2]} SHE HAS ACCESS TO MY PHONE!!!{/pa})"
    hero "{pa}{b}GIMME BACK!!!{/b}{/pa}"
    wnei "{bt=a5}Ahh . . .{/bt}"
    mind "(Better check if she changed something!)"

    $ cellbg.insert(1, "SHOT_WatchingTV_HERO")
    $ cellbg.insert(1, "SHOT_WatchingTV_WSIS")
    $ msg.msg(renpy.translate_string("New photos added to phone Gallery"))
    scene bg_home livingroom
    with Dissolve(1)

    $ Set_CharMap("hero", "home", "living_room")
    $ Set_CharMap("wnei", "home", "living_room")
    $ Set_CharMap("wsis", "home", "living_room")
    $ StartAct("wnei", ("watching TV", 60), True)
    $ StartAct("wsis", ("watching TV", 60), True)
    $ wnei_quest_1 = 1
    $ gametimemin += 60
    $ add_stat("wnei", "inti", 0.6)
    $ add_stat("wsis", "inti", 0.6)
    call gametime from _call_gametime_110
    
    jump show_ui

#---------------------------------------------------------------------------
label scenestep_0_0: # WNEI visit
#---------------------------------------------------------------------------

    $ wmom_mood = "A1"
    $ wnei_mood = "A3"
    $ hero_mood = "A1"

    call hide_ui from _call_hide_ui_183
    scene bg_home livingroom
    show HERO at RC
    show WMOM at OL
    show WNEI at OL
    with fade

    show WMOM at LC_slow
    show WNEI at LL_slow
    wmom "Honey{w=[wt1]}, look who came to see you!"
    show WNEI at CC_average
    pause(0.5)

    $ a_event_1 = round((20 + ((3 + (perk_phy_str * 2)) * (3 + (perk_phy_str * 2)))) * (1 + (stat_phy * 0.01)), 2)
    $ a_event_2 = round((21*wnei_size*wnei_size), 2)

    scene bg_2 yellow
    show bg_fx1
    show action_wnei_hug1_body

    if a_event_1 < a_event_2:
        show action_wnei_hug1_face 1
    else:
        show action_wnei_hug1_face 2

    if wnei_wear == "school":
        show action_wnei_hug1_outfitwnei school
    else:
        show action_wnei_hug1_outfitwnei common1
    if hero_wear == "school":
        show action_wnei_hug1_outfithero school
    else:
        show action_wnei_hug1_outfithero common1

    if a_event_1 < a_event_2:
        show action_wnei_hug1_body at Shaking
        show action_wnei_hug1_face at Shaking
        show action_wnei_hug1_outfitwnei at Shaking
        show action_wnei_hug1_outfithero at Shaking

    with Fade(0.5, 0, 1.5, color="#FFF")

    wnei "{bt}{size=+30}{color=#64C8FF}[fnamehero]{/color}!!!{/size}{/bt}"

    if a_event_1 < a_event_2:
        play SE1 "Slip.ogg"
        show action_wnei_hug1_body at Fall1
        show action_wnei_hug1_face at Fall1
        show action_wnei_hug1_outfitwnei at Fall1
        show action_wnei_hug1_outfithero at Fall1
        wnei "{pa}WOOOOAAH!!!{/pa}{w=0.2}{nw}"
        play SE1 "Hit2.mp3"
        hide bg_fx1 with dissolve
        $ msg.msg(renpy.translate_string("Oops! The little {nm}[fnamewnei]{/nm} seems to be too heavy for you"))
    else:
        $ add_stat("wnei", "love", 0.5)
        $ add_stat("wnei", "inti", 0.5)

    pause

    $ StartAct("wnei", (("staying", "living_room"), 60), True)
    $ StartAct("wmom", [("cleaning", 60), ("cooking", 180)], True)
    $ map_lock_bedroom_wsis = False
    $ hero_quest_1 = 1
    jump show_ui

#---------------------------------------------------------------------------
label wnei_quest_2_2: # Meet WMAM
#---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_184

    stop BGM fadeout 3
    scene bg_0 with dissolve
    
    play SE1 "WindowKnock.mp3"
    pause(0.2)
    play SE1 "WindowKnock.mp3"
    pause(0.2)
    play SE1 "WindowKnock.mp3"
    pause(0.2)
    play SE1 "WindowKnock.mp3"
    pause(0.2)
    play SE1 "WindowKnock.mp3"
    pause(0.5)
    
    mind "(Hmm?)"

    play BGM "audio/W2C - Tranquility.mp3"
    
    scene wnei_meetwmam_1_bg 1
    show wnei_meetwmam_1_wnei_body 1
    show wnei_meetwmam_1_wnei_face o0
    show wnei_meetwmam_1_mg
    show wnei_meetwmam_1_fg
    show wnei_meetwmam_1_hero_body
    show fx_light:
        blend "add"
    with dissolve

    show wnei_meetwmam_1_hero_body at Shake2

    mind "({aw}Ehhh!?!?{/aw})"

    $ zoomS1 = 1
    $ zoomT1 = 0
    $ zoomX1 = 0.7
    $ zoomY1 = 0.4
    $ zoomS2 = 2
    $ zoomT2 = 1
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1
    $ alpha1 = 1
    $ alpha2 = 0

    scene wnei_meetwmam_1_bg 1 at ZoomSTXY
    show wnei_meetwmam_1_wnei_body 1 at ZoomSTXY
    show wnei_meetwmam_1_wnei_face o0 at ZoomSTXY
    show wnei_meetwmam_1_mg at ZoomSTXY
    show wnei_meetwmam_1_fg at ZoomSTXYA
    show wnei_meetwmam_1_hero_body at ZoomSTXYA
    show wnei_meetwmam_1_hero_fx at ZoomSTXYA
    show fx_light:
        blend "add"

    pause(1.5)

    $ zoomS1 = 1
    $ zoomT1 = 0
    $ zoomX1 = 0.7
    $ zoomY1 = 0.4
    $ zoomS2 = 2
    $ zoomT2 = 0 # Instant
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1
    $ alpha1 = 1
    $ alpha2 = 0

    scene wnei_meetwmam_1_bg 1 at ZoomSTXY
    show wnei_meetwmam_1_wnei_body 1 at ZoomSTXY
    show wnei_meetwmam_1_wnei_face o0 at ZoomSTXY
    show wnei_meetwmam_1_mg at ZoomSTXY
    show wnei_meetwmam_1_fg at ZoomSTXYA
    show wnei_meetwmam_1_hero_body at ZoomSTXYA
    show wnei_meetwmam_1_hero_fx at ZoomSTXYA
    show fx_light:
        blend "add"

    show wnei_meetwmam_1_wnei_face o1
    wnei "Well{w=[wt2]}, ain't you an early bird today!{w=[wt2]} Whatcha up to?"
    
    show wnei_meetwmam_1_wnei_body 2
    show wnei_meetwmam_1_wnei_face o2
    with dissolve

    hero "{aw}Whoa!!{/aw}{w=[wt2]} C{w=[wt1]}-could you maybe{w=[wt1]}, um{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} p{w=[wt1]}-put on some{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} N{w=[wt1]}-nevermind."

    show wnei_meetwmam_1_wnei_face o3
    wnei "Put on some what?{w=[wt3]}{nw}"

    show wnei_meetwmam_1_wnei_face o4
    wnei "Put on some what?{w=[wt3]}{fast} {bt}Waaaah...{/bt}{w=[wt4]}{nw}"
    
    show wnei_meetwmam_1_wnei_face o3
    wnei "Put on some what?{w=[wt3]} {bt}Waaaah...{/bt}{w=[wt4]}{fast} Too early for riddles!"

    show wnei_meetwmam_1_wnei_face o2
    hero "S{w=[wt1]}-sure.{w=[wt3]} I'm just doing my morning routine."

    show wnei_meetwmam_1_wnei_face o5
    wnei "{aw}Ohhh!!{/aw}{w=[wt2]} Hold yer horses{w=[wt2]}, I'll join ya in a jiffy!"

    show wnei_meetwmam_1_wnei_face o6
    hero "S{w=[wt1]}-sure..."
    
    play SE1 "DoorOpen1.ogg"

    pause(1)

    $ zoomS1 = 2
    $ zoomT1 = 0
    $ zoomX1 = 0.7
    $ zoomY1 = 0.4
    $ zoomS2 = 1
    $ zoomT2 = 5
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1
    $ alpha1 = 0
    $ alpha2 = 1

    scene wnei_meetwmam_1_bg 2 at ZoomSTXY
    show wnei_meetwmam_1_wmam 1 at ZoomSTXY
    show wnei_meetwmam_1_wnei_body 2 at ZoomSTXY
    show wnei_meetwmam_1_wnei_face o7 at ZoomSTXY
    show wnei_meetwmam_1_mg at ZoomSTXY
    show wnei_meetwmam_1_fg at ZoomSTXYA
    show wnei_meetwmam_1_hero_body at ZoomSTXYA
    show wnei_meetwmam_1_hero_fx at ZoomSTXYA
    show fx_light:
        blend "add"

    play SE1 "DoorOpen2.ogg"

    pause(2)
    
    wmam "{bt}Waaaa...{/bt}{w=[wt3]} Sweetie pie{w=[wt2]}, have ya seen yer papa?{w=[wt3]} The bed's cold without my teddy bear..."

    scene wnei_meetwmam_2_bg
    show wnei_meetwmam_2_wmam_body
    show wnei_meetwmam_2_wmam_face t0
    show wnei_meetwmam_2_wnei_body
    show wnei_meetwmam_2_wnei_face a0
    show wnei_meetwmam_2_fg
    show fx_light:
        blend "add"
    with dissolve

    pause

    mind "({pa}WHAT BREASTS!!!{/pa}{w=[wt3]} Now I realize why it took me a while to recognize {nm}[fnamewnei]{/nm} when I met her again here at the window that day.{w=[wt3]} She became a copy of her mother!)"

    show wnei_meetwmam_2_wnei_face a1
    wnei "Mama{w=[wt2]}, ya know Papa goes shoppin' every Saturday mornin'!"

    show wnei_meetwmam_2_wmam_face t3
    show wnei_meetwmam_2_wnei_face a0
    wmam "Oh my{w=[wt2]}, yer right!{w=[wt1]} {gg}Tee-hee...{/gg}"

    show wnei_meetwmam_2_wmam_face t2

    pause(0.5)

    show wnei_meetwmam_2_wmam_face o0 with dissolve

    pause(1)

    show wnei_meetwmam_2_wmam_face o1
    wmam "Oh dear!{w=[wt2]} Sweetie, ya shouldn't leave yar boobas out in front of a man!"

    show wnei_meetwmam_2_wmam_face o2
    show wnei_meetwmam_2_wnei_face a0
    mind "(You're not being the best example for her about this, you know!?)"

    show wnei_meetwmam_2_wnei_face a3
    wnei "{lg}Shi Shi Shi...{/lg}{w=[wt3]} Oh, mama{w=[wt2]}, that ain't no man!{w=[wt2]} It's just {nm}[fnamehero]{/nm}!"

    show wnei_meetwmam_2_wnei_face a2
    show wnei_meetwmam_2_wmam_face o0
    mind "(Could you stop saying that to your parents?{w=[wt3]} I'm starting to develop a complex here.)"

    show wnei_meetwmam_2_wmam_face t3
    wmam "Oh{w=[wt1]}, if it ain't our lil' {nm}[fnamehero]{/nm}!{w=[wt2]} {gg}Tee-hee...{/gg}"

    show wnei_meetwmam_2_wmam_face t2
    hero "{mind}(That hurts, Miss){/mind}.{w=[wt3]} Good morning, {nm}Mrs. [lnamewnei]{/nm}!{w=[wt2]} Glad to see you're feeling better!"

    show wnei_meetwmam_2_wmam_face t3
    wmam "Oh my{w=[wt2]}, glad see you back here, dear!{w=[wt2]} Why don't ya cum to have a breakfast with us, hm?{w=[wt3]} I'm gonna make a special lunch for you!{nw}"

    menu:
        wmam "Oh my{w=[wt2]}, glad see you back here, dear!{w=[wt2]} Why don't ya cum to have a breakfast with us, hm?{w=[wt3]} I'm gonna make a special lunch for you!{fast}"

        "Accept":
            $ a_event_0 = 1
            show wnei_meetwmam_2_wmam_face t2
            hero "Sure!{w=[wt2]} I'd love!"

            show wnei_meetwmam_2_wmam_face t3
            show wnei_meetwmam_2_wnei_face a0
            wmam "Awesome!{w=[wt2]} We'll be waiting for you, dear!{w=[wt3]} Come on, lil sweetheart.{w=[wt2]} Get dressed and help Mama to prepare our meal!"

        "Refuse":
            $ a_event_0 = 2
            show wnei_meetwmam_2_wmam_face t2
            hero "O{w=[wt1]}-oh...{w=[wt2]} Thank you for the invitation, {nm}Mrs. [lnamewnei]{/nm}.{w=[wt2]} But I'm afraid I can't today."

            show wnei_meetwmam_2_wmam_face t3
            show wnei_meetwmam_2_wnei_face a0

            if (wnei_inti >= 10 and hpap_love >= 10 and wmam_love >= 10): # All requirements for next stage

                if wnei_quest_6 <= 1: # Neighbor's Reunion content never started

                    if wnei_quest_6 < 1: # Neighbor's Reunion 1st time invitation
                        $ msg.msg(renpy.translate_string("⭐ Intimacy cap increased"))
                        $ msg.msg(renpy.translate_string("⭐ {b}Content unlocked:{/b} [C_Dat]Neighbor's Reunion[C_Off]"))
                        $ wnei_inti_cap = char_inti_req_date

                    $ wnei_quest_6 = 1
                    wmam "Ohhh{w=[wt2]}, that's a shame, dear...{w=[wt4]} But consider joining us in our lunch tomorrow!{w=[wt3]} We'll make a delicious barbecue banquet and would love to have you and your family with us!"

                else: # Neighbor's Reunion content already completed before

                    wmam "Ohhh{w=[wt2]}, that's a shame, dear...{w=[wt4]} But consider joining us in our lunch tomorrow!{w=[wt3]} We'll make another delicious barbecue banquet and would love to have you and your family with us!"

                hero "It'd be a pleasure, miss.{w=[wt3]} Thank you for your invitation!"

            else: # No requirements for next stage
                wmam "Ohhh{w=[wt2]}, that's a shame, dear...{w=[wt4]} Know you're welcum here whenever you want!"

            show wnei_meetwmam_2_wmam_face t2
            show wnei_meetwmam_2_wnei_face a1
            wnei "So{w=[wt1]}, mama.{w=[wt2]} I'm gonna {nm}[fnamehero]{/nm}'s house now."

            show wnei_meetwmam_2_wmam_face t3
            show wnei_meetwmam_2_wnei_face a0
            wmam "Okay, Sweetie pie{w=[wt2]}, Behave yourself!"
            $ StartAct("wnei", (("bathing", "home"), 0), True)
            $ StartAct("wnei", (("changing", "home"), 0), True)
            $ StartAct("wnei", (("moving", "home"), 20), True)
            $ wnei_wear = "home"

    $ zoomS1 = 3
    $ zoomT1 = 0
    $ zoomX1 = 0.5
    $ zoomY1 = 0.1
    $ zoomS2 = 2
    $ zoomT2 = 3
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1
    $ alpha1 = 0
    $ alpha2 = 1

    scene wnei_meetwmam_3_bg at ZoomSTXY
    show wnei_meetwmam_3_hero_body at ZoomSTXY
    show wnei_meetwmam_3_hero_face a0 at ZoomSTXY
    with dissolve

    wnei "See ya soon, {nm}[fnamehero]{/nm}!"

    show wnei_meetwmam_3_hero_face a1
    hero "S{w=[wt1]}-see ya!"

    $ zoomS1 = 2
    $ zoomT1 = 0
    $ zoomX1 = 0.5
    $ zoomY1 = 0.1
    $ zoomS2 = 1
    $ zoomT2 = 8
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1
    $ alpha1 = 0
    $ alpha2 = 1

    scene wnei_meetwmam_3_bg at ZoomSTXY
    show wnei_meetwmam_3_hero_body at ZoomSTXY
    show wnei_meetwmam_3_hero_face a0 at ZoomSTXY
    show wnei_meetwmam_3_fx at ZoomSTXYA

    stop BGM fadeout 5

    mind "(It's nice to know that they feel comfortable with me.{w=[wt4]} Yeah.{w=[wt4]} It's nice, isn't it?)"

    pause

    mind "(My dick is hard and my honor is destroyed.{w=[wt4]} I can't go out like this.)"

    $ wnei_quest_3 = 1
    $ add_stat("wnei", "inti", 1)
    $ gametimemin += 20
    call gametime from _call_gametime_111

    if a_event_0 == 1:
        jump wnei_breakfast_start

    if a_event_0 == 2:
        scene bg_0 with Dissolve(3)
        play BGM "audio/W2C - GoodVibes.mp3"

        jump show_ui

# ---------------------------------------------------------------------------
label wnei_breakfast_start: # Family Breakfast with WMAM
# ---------------------------------------------------------------------------
    scene bg_0 with Dissolve(3)

    play BGM "audio/W2C - GoodVibes.mp3"
    $ Set_CharMap("hero", "neighbor", "living_room")

    scene wnei_meetwmam_4_bg
    show wnei_meetwmam_4_mg
    show wnei_meetwmam_4_wmam_face a0
    show wnei_meetwmam_4_wnei_face a0
    show fx_light:
        blend "add"
    with Dissolve(2)
    
    show wnei_meetwmam_4_wnei_face a1
    wnei "Here he is, mama!"
    
    # WMAM bustles around kitchen in transparent nightwear, completely natural
    
    show wnei_meetwmam_4_wnei_face a0
    show wnei_meetwmam_4_wmam_face a1
    wmam "Isn't my little cutie so precious?{w=[wt2]} Opening the door to our dear guest!"
    
    show wnei_meetwmam_4_wnei_face a1
    show wnei_meetwmam_4_wmam_face a0
    wnei "Of course!{w=[wt2]} That's what a super duper polite woman would do, mama!"
    
    show wnei_meetwmam_4_wnei_face a0
    show wnei_meetwmam_4_wmam_face a1
    wmam "{gg}Tee-hee...{/gg}{w=[wt3]} It's perfect timing, [C_Nam][fnamehero][C_Off]!{w=[wt2]} I was just finishing up breakfast preparations!{w=[wt3]} Come, come!{w=[wt2]} Sit at the table, sweetheart!{w=[wt2]} You're our special guest!"
    
    show wnei_meetwmam_4_wmam_face a0 with None
    
    scene wnei_meetwmam_5_bg
    show wnei_meetwmam_5_hero_body 1
    show wnei_meetwmam_5_hero_eye d
    show wnei_meetwmam_5_hero_face a0
    show wnei_meetwmam_5_wnei_body 2
    show wnei_meetwmam_5_wnei_face 2a0
    show wnei_meetwmam_5_wmam_body 1
    show wnei_meetwmam_5_wmam_face 1a0
    show wnei_meetwmam_5_mg_food 1
    show fx_light:
        blend "add"
    with Fade(1,0,1)
    
    show wnei_meetwmam_5_wmam_face 1a1
    show wnei_meetwmam_5_hero_eye l
    wmam "Here we go, dears!"
    
    scene wnei_meetwmam_5_bg
    show wnei_meetwmam_5_wnei_body 2
    show wnei_meetwmam_5_wnei_face 2a0
    show wnei_meetwmam_5_wmam_body 2
    show wnei_meetwmam_5_wmam_face 2a0
    show wnei_meetwmam_5_wmam_eye 2d
    show wnei_meetwmam_5_hero_body 2
    show wnei_meetwmam_5_hero_face a0
    show wnei_meetwmam_5_hero_eye l
    show wnei_meetwmam_5_mg_food 2
    show fx_light:
        blend "add"
    with dissolve

    show wnei_meetwmam_5_wnei_face 2a1
    show wnei_meetwmam_5_hero_eye r
    wnei "{bt}Mama always prepares enough food for a super duper big army!{/bt}"

    show wnei_meetwmam_5_wnei_body 1a
    show wnei_meetwmam_5_wnei_face 1a0
    with dissolve

    show wnei_meetwmam_5_wmam_face 2a1
    show wnei_meetwmam_5_hero_eye l
    wmam "Growing boys and girls need proper nutrition!"
    
    show wnei_meetwmam_5_wmam_face 2a0
    show wnei_meetwmam_5_hero_face a1
    show wnei_meetwmam_5_hero_eye d
    hero "Thank you [C_Nam][fnamewmam][C_Off].{w=[wt2]} It looks great!"
    
    show wnei_meetwmam_5_hero_eye l
    show wnei_meetwmam_5_hero_face a0
    show wnei_meetwmam_5_wmam_face 2a1
    wmam "{gg}Tee-hee...{/gg}{w=[wt3]} I'm so glad you're back, [C_Nam][fnamehero][C_Off].{w=[wt2]} It seems that my little darling is even happier these days{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'm sure you're the reason for this."
    
    show wnei_meetwmam_5_hero_face a1
    show wnei_meetwmam_5_wmam_face 2a0
    hero "I'm happy to be back too.{w=[wt2]} It feels like home here."
    
    show wnei_meetwmam_5_hero_face a0
    show wnei_meetwmam_5_wmam_face 2a1
    wmam "Oh!{w=[wt2]} {nm}[fnamewmom]{/nm} invited us to your return party{w=[wt2]}, but I'm so sorry we couldn't make it!{w=[wt3]} I had caught a terrible cold."
    
    show wnei_meetwmam_5_hero_face a1
    show wnei_meetwmam_5_wmam_face 2a0
    hero "It's completely okay.{w=[wt2]} I'm glad you're fine now!"

    show wnei_meetwmam_5_wmam_eye 2r
    show wnei_meetwmam_5_wnei_face 1a1
    show wnei_meetwmam_5_hero_face a0
    show wnei_meetwmam_5_hero_eye r
    wnei "Of course she's fine now!{w=[wt3]} I took care of her all day!"

    show wnei_meetwmam_5_wnei_face 1a0
    show wnei_meetwmam_5_hero_face o0
    mind "(Now I get why she took so long to get well.)"
    
    show wnei_meetwmam_5_wmam_eye 2d
    show wnei_meetwmam_5_wmam_face 2a1
    show wnei_meetwmam_5_hero_eye l
    wmam "{gg}Tee-hee...{/gg}{w=[wt3]} My lil angel is always so kind to her mama!{w=[wt3]} She set aside spending the day with [C_Nam][fnamewsis][C_Off] in your house to be taking care of me.{w=[wt4]} What can I want more in this life having a treasure like this?"

    show wnei_meetwmam_5_wmam_face 2a0
    show wnei_meetwmam_5_wmam_eye 2r
    show wnei_meetwmam_5_wnei_face 1a1
    show wnei_meetwmam_5_hero_eye r
    wnei "Mama got caught in the rain in the backyard while she was taking the clothes off the clothesline.{w=[wt3]} The problem got even worse 'cos in her rush, she forgot to put her own clothes on."
    
    show wnei_meetwmam_5_hero_face s0
    show wnei_meetwmam_5_wnei_face 1a0
    mind "(Ehhh...!?)"

    show wnei_meetwmam_5_wmam_face 2a1
    show wnei_meetwmam_5_wmam_eye 2d
    show wnei_meetwmam_5_hero_eye l
    wmam "{gg}Tee-hee...{/gg}{w=[wt3]} I sometimes forget to wear something around the house.{w=[wt2]} Luckily{w=[wt2]}, so far{w=[wt2]}, this has never happened while I have a visitor.{w=[wt3]} Well{w=[wt2]}, our neighborhood isn't much for visitors, is it?{w=[wt3]} You guys are our only close neighbors.{w=[wt3]} So{w=[wt2]}, I guess it's okay."

    $ X_spd = 0.5

    show wnei_meetwmam_5_wmam_face 2a0
    show wnei_meetwmam_5_hero_eye f
    with None

    show wnei_meetwmam_5_hero_face s2
    show wnei_meetwmam_5_hero_body 3
    with dissolve

    mind "(Wait{w=[wt2]}, am I really allowed to have this information?{w=[wt2]} These two are completely oblivious)"
    
    show wnei_meetwmam_5_wmam_face 2a3
    wmam "Oh{w=[wt2]}, you must have been through a lot, dear.{w=[wt3]} My condolences about your father.{w=[wt3]} Know that we'll be here for whatever you need!"
    
    show wnei_meetwmam_5_wmam_face 2a2 with None

    show wnei_meetwmam_5_hero_face a2
    show wnei_meetwmam_5_hero_body 2
    show wnei_meetwmam_5_hero_eye l
    with dissolve

    show wnei_meetwmam_5_hero_face a3
    hero "Thank you{w=[wt2]}, that means a lot to me."
    
    show wnei_meetwmam_5_wmam_face 2a1
    show wnei_meetwmam_5_hero_face a2
    wmam "You know{w=[wt2]}, seeing you back here reminds me of those days when you were just little creatures."
    
    show wnei_meetwmam_5_wmam_face 2a0
    show wnei_meetwmam_5_wnei_face 1a1
    show wnei_meetwmam_5_hero_eye r
    show wnei_meetwmam_5_hero_face a0
    wnei "But now we're super duper big!"

    show wnei_meetwmam_5_wmam_body at Opacity1
    show wnei_meetwmam_5_wmam_face at Opacity1
    show wnei_meetwmam_5_wmam_eye at Opacity1
    show wnei_meetwmam_5_wnei_face 1a0
    mind "(No{w=[wt2]}, besides the tits, you're still a little creature.)"
    
    show wnei_meetwmam_5_wnei_face 1a1
    show wnei_meetwmam_5_hero_face o0
    wnei "Hey, mama!{w=[wt2]} Where are you go{w=[wt1]}-{nw}"
    
    show wnei_meetwmam_5_wmam_body 3 at Opacity2
    show wnei_meetwmam_5_wmam_face 3a0 at Opacity2
    show wnei_meetwmam_5_wmam_eye 3d at Opacity2
    show wnei_meetwmam_5_hero_eye l
    show wnei_meetwmam_5_hero_face s0
    show wnei_meetwmam_5_mg_book at Opacity2
    show wnei_meetwmam_5_wnei_face 1o1

    wnei "Hey, mama!{w=[wt2]} Where are you go{w=[wt1]}-{fast}...!{w=[wt4]} {aw}Oh, shit...{w=[wt3]} Here we go again...{/aw}"

    show wnei_meetwmam_5_wmam_face 3a1
    show wnei_meetwmam_5_wnei_face 1s0
    show wnei_meetwmam_5_hero_eye d
    wmam "Look!{w=[wt2]} I still have a lot of pictures of my lil baby!"

    show wnei_meetwmam_5_wmam_face 3a0
    mind "(Miss{w=[wt2]}, I'm feeling something soft on my shoulders...)"

# ---------------------------------------------------------------------------
# [MINIGAME SECTION - Multiple scenarios with different responses]
# ---------------------------------------------------------------------------
    $ a_check_0 = 0 # Mark Direction
    $ a_check_1 = 500 # Mark Position
    $ a_check_2 = 1000 # Red Bar Size
    $ a_check_3 = int(a_check_2 / (50 / ((1 + (perk_cha_soc*1)) * (1 + (stat_cha_soc*0.01))))) # Green Bar Size
    $ a_check_4 = int(a_check_3 * 3) # Yellow Bar Size
    $ a_check_5 = int(a_check_3 * 6) # Orange Bar Size
    $ a_check_6 = 0 # Counter
    $ wnei_photoalbum_queue = ['wnei_breakfast_photoalbum_1', 'wnei_breakfast_photoalbum_2', 'wnei_breakfast_photoalbum_3'] # Random Scenario

    label wnei_breakfast_photoalbum_0:
        $ a_check_6 += 1
        if a_check_6 <= 3:
            $ a_check_1 = renpy.random.randint(int(a_check_2/2), int(a_check_2))
            $ renpy.call(label=renpy.random.choice(wnei_photoalbum_queue))
        else:
            jump wnei_breakfast_end

    # ---------------------------------------------------------------------------
    label wnei_breakfast_photoalbum_1:
    # ---------------------------------------------------------------------------
    # Minigame Answer - Crayon Masterpieces
    # ---------------------------------------------------------------------------

        show wnei_meetwmam_5_wmam_face 3a1
        wmam "Here's one that brings back memories!{w=[wt3]} I came home from grocery shopping and found crayon drawings everywhere{w=[wt2]}, on the house walls{w=[wt2]}, the table{w=[wt2]}, even her bedroom door! {gg}Tee-hee...{/gg}"

        show wnei_meetwmam_5_hero_face o0
        wmam "But the sweetest part was when I found this beautiful drawing of our whole family in the refrigerator door{w=[wt2]}, me{w=[wt2]}, her papa{w=[wt2]}, and herself{w=[wt2]}, all holding hands with big smiles.{w=[wt2]} She even added little hearts floating around us!"
        wmam "I just couldn't stay mad at her.{w=[wt3]} How could I scold such a loving heart?{w=[wt3]} So instead{w=[wt2]}, I asked her papa to buy lots and lots of drawing paper!{w=[wt3]} I still feel a little guilty about scrubbing away all that cute artwork though."

        show wnei_meetwmam_5_wmam_face 3a0 with None
        
    # ---------------------------------------------------------------------------
    # Minigame Result - Crayon Masterpieces
    # ---------------------------------------------------------------------------
        $ a_check_0 = 0
        $ wnei_photoalbum_queue.remove('wnei_breakfast_photoalbum_1')
        call screen minigame_precision(var_mod="classic", var_bao=a_check_1, var_bam=a_check_2, var_grn=a_check_3, var_yel=a_check_4, var_org=a_check_5)
        $ renpy.pause(0.5, hard=True)

        if _return == 3: # HERO answers perfectly

            show wnei_meetwmam_5_hero_face a1
            hero "You made the absolute best decision possible!{w=[wt3]} Instead of crushing her creative spirit{w=[wt2]}, you showed [C_Nam][fnamewnei][C_Off] that self-expression is wonderful{w=[wt2]}, and helped her find the right canvas.{w=[wt3]} And look how much she loves drawing now!"
            hero "It's so like [C_Nam][fnamewnei][C_Off] to create art that brings joy.{w=[wt3]} Drawing your family on the refrigerator wasn't really a mischief{w=[wt2]}, it was her way of saying {i}I love you so much{w=[wt2]}, I want to see your faces every day!{/i}"

            $ add_stat("wnei", "love", 3)
            $ add_stat("wmam", "love", 3)
            show wnei_meetwmam_5_hero_face a0
            show wnei_meetwmam_5_wnei_face 1s2
            show wnei_meetwmam_5_wmam_face 3a3

            wmam "Oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I never thought of it that way!{w=[wt2]} She really was sharing her love, wasn't she?{w=[wt3]} You understand her heart so deeply{w=[wt2]}, dear!{w=[wt3]} Thank you for making me see all this.{w=[wt3]} Now I don't feel guilty at all{w=[wt2]}, I feel proud that I helped nurture such a loving, creative soul!"
            
        elif _return == 2: # HERO answers not completely bad

            show wnei_meetwmam_5_hero_face a1
            hero "Well{w=[wt2]}, I think you handled that well.{w=[wt2]} Supporting her creativity while teaching her boundaries was not a bad thing.{w=[wt3]} I mean{w=[wt2]}, she still loves drawing, right?{w=[wt3]} It means it may have worked well."

            $ add_stat("wnei", "love", 1)
            $ add_stat("wmam", "love", 1)
            show wnei_meetwmam_5_hero_face a0
            show wnei_meetwmam_5_wnei_face 1s2
            show wnei_meetwmam_5_wmam_face 3a1

            wmam "{gg}Shi Hi Hi...{/gg}{w=[wt3]} Thank you, dear!{w=[wt2]} It's so nice to hear that I made the right choice.{w=[wt3]} She really is such a creative little artist!"
            
        elif _return == 1: # HERO answer bad

            show wnei_meetwmam_5_hero_face a3
            hero "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} at least it was{w=[wt2]}, huh{w=[wt2]}, artistic and{w=[wt2]}, colorful, right?{w=[wt3]} It's good for a memory."
            
            show wnei_meetwmam_5_hero_face a2
            show wnei_meetwmam_5_wnei_face 1s0
            show wnei_meetwmam_5_wmam_face 3a3

            wmam "{gg}Shi Hi Hi...{/gg}{w=[wt3]} That's one way to look at it!{w=[wt2]} It certainly brightened up the kitchen for a while!{w=[wt2]} She does love her bright colors!"
            
        elif _return == 0: # HERO ending up make things worse

            show wnei_meetwmam_5_hero_face a3
            hero "Ohhh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} That really sounds a lot of cleaning, right...?{w=[wt3]} It's too bad all that artwork had to be erased."
            
            $ add_stat("wnei", "love", -1)
            $ add_stat("wmam", "love", -1)
            show wnei_meetwmam_5_hero_face a2
            show wnei_meetwmam_5_wnei_face 1s1
            show wnei_meetwmam_5_wmam_face 3a3

            wmam "Oh{w=[wt2]}, yes{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I remember her crying while I scrubbed away that beautiful family drawing on the refrigerator{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} She kept asking me why I was washing away her {i}love picture{/i}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} and I didn't know what to tell her.{w=[wt3]} The only way I found to preserve some of it was by this photo."

        jump wnei_breakfast_photoalbum_0

    # ---------------------------------------------------------------------------
    label wnei_breakfast_photoalbum_2:
    # ---------------------------------------------------------------------------
    # Minigame Answer - Mud Pie Cooking
    # ---------------------------------------------------------------------------
    
        show wnei_meetwmam_5_wmam_face 3a1
        wmam "Look!{w=[wt2]} Here's a special one that [C_Nam][fnamewmom][C_Off] took!"

        show wnei_meetwmam_5_hero_face a1
        show wnei_meetwmam_5_wmam_face 3a0
        hero "Oh!{w=[wt2]} These are me, [C_Nam][fnamewnei][C_Off], and [C_Nam][hero_about_wsis][C_Off]."

        show wnei_meetwmam_5_hero_face a0
        show wnei_meetwmam_5_wmam_face 3a1
        wmam "This was in [C_Nam]Miss. [fnamewgma][C_Off]'s backyard when you three were little!{w=[wt3]} Look at my precious baby here{w=[wt2]}, she's making what she called {i}Super Duper Gourmet Mud Cuisine{/i} for everyone!{w=[wt3]} She had this whole setup with leaves as plates{w=[wt2]}, rocks as fancy decorations{w=[wt2]}, and different types of mud mixed with grass and flowers!"
        wmam "{gg}Tee-hee...{/gg}{w=[wt3]} [C_Nam][fnamewmom][C_Off] said she couldn't stop giggling while taking this photo!{w=[wt3]} She was so serious about it too!{w=[wt2]} Taking orders from everyone like a real chef{w=[wt2]}, asking what 'flavors' they wanted{w=[wt2]}, and even trying to make the presentation look beautiful!"
        
        show wnei_meetwmam_5_wmam_face 3a0 with None

    # ---------------------------------------------------------------------------
    # Minigame Result - Mud Pie Cooking
    # ---------------------------------------------------------------------------
        $ a_check_0 = 0
        $ wnei_photoalbum_queue.remove('wnei_breakfast_photoalbum_2')
        call screen minigame_precision(var_mod="classic", var_bao=a_check_1, var_bam=a_check_2, var_grn=a_check_3, var_yel=a_check_4, var_org=a_check_5)
        $ renpy.pause(0.5, hard=True)

        if _return == 3: # HERO answers perfectly

            show wnei_meetwmam_5_hero_face a1
            hero "Oh wow{w=[wt2]}, I remember that day perfectly!{w=[wt3]} [C_Nam][fnamewnei][C_Off] made a special dish for everyone.{w=[wt3]} She gave [C_Nam][hero_about_wsis][C_Off] a {i}grumpy special{/i} because [C_Nam][hero_about_wsis][C_Off] was being moody that day{w=[wt2]}, and it was this elaborate mud cake with pretty flower petals on top!"
            hero "And when [C_Nam][hero_about_wgma][C_Off] started scolding her about messing up the garden{w=[wt2]}, [C_Nam][fnamewnei][C_Off] just handed her this beautiful {i}apology pie{/i} with the shiniest rocks arranged like jewelry!{w=[wt3]} [C_Nam][hero_about_wgma][C_Off] got so speechless she forgot what she was mad about!"
            hero "She made dishes for [C_Nam][hero_about_wcou][C_Off] and [C_Nam][hero_about_wmom][C_Off] too{w=[wt2]}, each one 'customized' for their personalities."
            hero "But here's the funny part{w=[wt2]}, I was the only one who actually took a bite{w=[wt2]}, well{w=[wt2]}, she had put a lot of effort into it, you know?{w=[wt3]} I spent the entire night in the bathroom{w=[wt2]}, and [C_Nam][fnamewnei][C_Off] felt so bad she made me a {i}get-well card{/i} with crayon drawings of medicine bottles."

            $ add_stat("wnei", "love", 3)
            $ add_stat("wmam", "love", 3)
            show wnei_meetwmam_5_hero_face a0
            show wnei_meetwmam_5_wnei_face 1s2
            show wnei_meetwmam_5_wmam_face 3a3
            
            wmam "Oh my stars!{w=[wt2]} You remember all those details, dear!{w=[wt3]} And you actually ate it!{w=[wt2]} {gg}Shi Hi Hi...{/gg}{w=[wt3]} No wonder you two are such good friends.{w=[wt3]} I love that you always been so kind to each other!"
            
        elif _return == 2: # HERO answers good

            show wnei_meetwmam_5_hero_face a1
            hero "I remember that!{w=[wt2]} [C_Nam][fnamewnei][C_Off] was so excited about being a chef that day.{w=[wt3]} She really wanted to make everyone happy with her cooking{w=[wt2]}, even though it was just mud and leaves.{w=[wt3]} It was really sweet how much effort she put into it!"
            
            $ add_stat("wnei", "love", 1)
            $ add_stat("wmam", "love", 1)
            show wnei_meetwmam_5_hero_face a0
            show wnei_meetwmam_5_wnei_face 1s2
            show wnei_meetwmam_5_wmam_face 3a3

            wmam "Yes!{w=[wt2]} She's always had such a generous heart{w=[wt2]}, wanting to take care of everyone!{w=[wt3]} Even as a little girl{w=[wt2]}, she was always thinking about making others happy!"
            
        elif _return == 1: # HERO answer neutral

            show wnei_meetwmam_5_hero_face a3
            hero "Yeah{w=[wt2]}, that was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} quite a creative day.{w=[wt3]} Kids and their imagination{w=[wt2]}, right?{w=[wt3]} Very{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} artistic."
            
            show wnei_meetwmam_5_hero_face a2
            show wnei_meetwmam_5_wnei_face 1s0
            show wnei_meetwmam_5_wmam_face 3a3

            wmam "{gg}Shi Hi Hi...{/gg}{w=[wt3]} That's one way to put it!{w=[wt2]} She certainly has always been creative with whatever materials she could find!"
            
        elif _return == 0: # HERO ending up making things awkward

            show wnei_meetwmam_5_hero_face a3
            hero "Oh{w=[wt2]}, yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I remember that day{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I got really sick after eating the mud.{w=[wt3]} Passed all night on the bathroom."
            
            $ add_stat("wnei", "love", -1)
            $ add_stat("wmam", "love", -1)
            show wnei_meetwmam_5_hero_face a2
            show wnei_meetwmam_5_wnei_face 1s1
            show wnei_meetwmam_5_wmam_face 3a3

            wmam "Oh dear{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} yes{w=[wt2]}, I remember [C_Nam][fnamewmom][C_Off] calling me that night{w=[wt2]}, so worried about you!{w=[wt3]} Poor [C_Nam][fnamewnei][C_Off] cried for hours thinking she had poisoned her best friend{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} She kept asking if you were going to die{w=[wt2]}, and we had to convince her that people don't die from eating a little dirt."
            
        jump wnei_breakfast_photoalbum_0

# ---------------------------------------------------------------------------
    label wnei_breakfast_photoalbum_3:
    # ---------------------------------------------------------------------------
    # Minigame Answer - Sock Puppet Shows
    # ---------------------------------------------------------------------------
    
        show wnei_meetwmam_5_wmam_face 3a1
        wmam "Look!{w=[wt2]} Here's on of my favorites!{w=[wt3]} Sometimes [C_Nam][fnamewnei][C_Off] would set up her {i}Super Duper Sock Theater{/i} in the living room!{w=[wt3]} She'd gather every sock she could find{w=[wt2]}, draw little faces on them with markers{w=[wt2]}, and create these incredibly dramatic stories!{w=[wt3]} {gg}Tee-hee...{/gg}"

        show wnei_meetwmam_5_hero_face o0
        wmam "She had different voices for each character{w=[wt2]}, there was [C_Nam]Sir Stripey, The Brave Knight[C_Off]{w=[wt2]}, [C_Nam]Princess Polka-Dot, The Wise Ruler[C_Off]{w=[wt2]}, and [C_Nam]Captain Argyle, The Silly Sidekick[C_Off]!"
        wmam "But here's the sweetest part{w=[wt2]}, she would make us all sit on the couch like we were at a real theater{w=[wt2]}, and she'd perform these amazing adventures where the sock heroes always saved the day!{w=[wt3]} She was so serious about it too{w=[wt2]}, taking bows at the end and asking for applause!"
        wmam "When I tried to go back to my chores, she always insisted that I stay until the end{w=[wt2]}, but sometimes the shows would go on for almost an entire hour because she'd get so excited about the story!"
        
        show wnei_meetwmam_5_wmam_face 3a0 with None

    # ---------------------------------------------------------------------------
    # Minigame Result - Sock Puppet Shows
    # ---------------------------------------------------------------------------
        $ a_check_0 = 0
        $ wnei_photoalbum_queue.remove('wnei_breakfast_photoalbum_3')
        call screen minigame_precision(var_mod="classic", var_bao=a_check_1, var_bam=a_check_2, var_grn=a_check_3, var_yel=a_check_4, var_org=a_check_5)
        $ renpy.pause(0.5, hard=True)

        if _return == 3: # HERO answers perfectly

            show wnei_meetwmam_5_hero_face a1
            hero "I was always amazed by [C_Nam][fnamewnei][C_Off]'s creativity and improvisation!{w=[wt3]} When we played with our toys{w=[wt2]}, she'd create completely new adventures on the spot.{w=[wt4]} But what really impressed me was how she made every story feel special for whoever was watching.{w=[wt3]} It was like she could sense what each person needed to hear{w=[wt2]}, and then weave it into the story!"

            $ add_stat("wnei", "love", 3)
            $ add_stat("wmam", "love", 3)
            show wnei_meetwmam_5_hero_face a0
            show wnei_meetwmam_5_wnei_face 1s2
            show wnei_meetwmam_5_wmam_face 3a3
            
            wmam "Now that you mention it{w=[wt2]}, it was like that time her father was worried about work{w=[wt2]}, and suddenly her story became about [C_Nam]Captain Argyle[C_Off] learning that {i}even brave heroes need help from friends sometimes{/i}."

            show wnei_meetwmam_5_hero_face a1
            show wnei_meetwmam_5_wmam_face 3a2
            hero "It really is like her!{w=[wt2]} Probably looking at you and [C_Nam][fnamehpap][C_Off] and creating healing stories for each of you{w=[wt2]}, using silly sock puppets to make everyone feel better.{w=[wt3]} She has this gift of turning simple play into something that touches people's hearts."

            show wnei_meetwmam_5_hero_face a0
            show wnei_meetwmam_5_wmam_face 3a3
            wmam "Oh my goodness!{w=[wt2]} I always wondered why I felt so much better after her shows{w=[wt2]}, even on my worst days!{w=[wt3]} She really was taking care of all of us, wasn't she?{w=[wt3]} My little angel has such a gift for understanding people's hearts{w=[wt1]}, and I never even realized it!{w=[wt3]} {gg}Shi Hi Hi...{/gg}{w=[wt3]} She's going to touch so many lives with that beautiful soul of hers!"
            
        elif _return == 2: # HERO answers good

            show wnei_meetwmam_5_hero_face a1
            hero "That's really impressive!{w=[wt2]} [C_Nam][fnamewnei][C_Off] has always been amazing at creating characters and stories.{w=[wt3]} I remember she could make up entire adventures just with whatever toys we had.{w=[wt3]} She's naturally gifted with creativity!"
            
            $ add_stat("wnei", "love", 1)
            $ add_stat("wmam", "love", 1)
            show wnei_meetwmam_5_hero_face a0
            show wnei_meetwmam_5_wnei_face 1s2
            show wnei_meetwmam_5_wmam_face 3a3

            wmam "I totally agree, dear!{w=[wt2]} She's always been such a natural performer!{w=[wt3]} Even now{w=[wt2]}, when she tells us about her day{w=[wt2]}, she makes it sound like the most exciting adventure!{w=[wt3]} She has such a wonderful imagination!"
            
        elif _return == 1: # HERO answer weak

            show wnei_meetwmam_5_hero_face a3
            hero "Oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} That sounds{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} entertaining, right?"
            
            show wnei_meetwmam_5_hero_face a2
            show wnei_meetwmam_5_wnei_face 1s0
            show wnei_meetwmam_5_wmam_face 3a3

            wmam "{gg}Shi Hi Hi...{/gg}{w=[wt3]} What matters to me is that my little entertainer was very happy on her shows!"
            
        elif _return == 0: # HERO makes things worse

            show wnei_meetwmam_5_hero_face a3
            hero "An entire hour{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} That must have been{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} difficult to endure{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Especially when you had chores to do."

            $ add_stat("wnei", "love", -1)
            $ add_stat("wmam", "love", -1)
            show wnei_meetwmam_5_hero_face a2
            show wnei_meetwmam_5_wnei_face 1s1
            show wnei_meetwmam_5_wmam_face 3a3

            wmam "Well{w=[wt2]}, yes{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I remember one day I was so focused on watching her show that I completely forgot about dinner cooking on the stove.{w=[wt3]} The food burned so badly it ruined my favorite pan{w=[wt2]}, and the whole house smelled like smoke for days{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} My husband was not very happy about that."
            
        jump wnei_breakfast_photoalbum_0
    
# ---------------------------------------------------------------------------
# End of minigame section, results determine WMAM's final reaction
# ---------------------------------------------------------------------------
label wnei_breakfast_end:

    # WNEI gets cookie pieces on cheek
    show wnei_meetwmam_5_hero_face a0
    show wnei_meetwmam_5_hero_eye d
    show wnei_meetwmam_5_wmam_body 2
    show wnei_meetwmam_5_wmam_face 2a0
    show wnei_meetwmam_5_wnei_body 1b
    show wnei_meetwmam_5_wnei_fx
    hide wnei_meetwmam_5_wmam_eye
    show wnei_meetwmam_5_wmam_eye 2d
    hide fx_light
    show fx_light:
        blend "add"
    with dissolve

    show wnei_meetwmam_5_hero_eye l
    show wnei_meetwmam_5_wmam_face 2a1
    if wmam_love < 9:
        wmam "Shi{w=[wt1]}-hi{w=[wt1]}-hi{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} That's why she'll always be my little baby!{w=[wt2]} Right, dear?"

        show wnei_meetwmam_5_hero_eye r
        show wnei_meetwmam_5_wmam_eye 2d
        show wnei_meetwmam_5_wmam_face 2a0
        show wnei_meetwmam_5_wnei_face 1a1
        wnei "I'm already a big woman, mama!"
    else:
        wmam "Shi hi hi{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} And look how she is now{w=[wt2]}, such a beautiful grown woman{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}!"

        show wnei_meetwmam_5_hero_eye r
        show wnei_meetwmam_5_wmam_eye 2d
        show wnei_meetwmam_5_wmam_face 2a0
        show wnei_meetwmam_5_wnei_face 1a1
        wnei "Yeah, and a super duper cool woman, mama!"
    
    show wnei_meetwmam_5_wnei_face 1a0 with None

    # WMAM wipes WNEI's cheek clean
    show wnei_meetwmam_5_hero_face o0
    show wnei_meetwmam_5_wmam_body 4
    show wnei_meetwmam_5_wmam_face 4a0
    show wnei_meetwmam_5_wmam_eye 4
    with dissolve

    show wnei_meetwmam_5_wmam_face 4a1
    wmam "Of course you are, darling!"

    show wnei_meetwmam_5_wmam_face 4a0 with None
    hide wnei_meetwmam_5_wnei_fx with dissolve

    mind "([C_Nam]Miss[C_Off]{w=[wt2]}, you are the one most to blame for your daughter not maturing mentally.)"
    
    show wnei_meetwmam_5_wnei_face 1a1
    wnei "Mama, I'm full!{w=[wt2]} I'm gonna go to [C_Nam][fnamehero][C_Off]'s home now!"
    
    show wnei_meetwmam_5_wmam_face 4a1
    show wnei_meetwmam_5_wnei_face 1a0
    wmam "But sweetie{w=[wt2]}, you just ate one cookie!{w=[wt2]} Just drink your coffee and I'll let you go, okay?"

    play SE1("Equip1.mp3")
    show wnei_meetwmam_5_wmam_body 2
    show wnei_meetwmam_5_wmam_face 2a0
    show wnei_meetwmam_5_wmam_eye 2r
    with dissolve

    pause(0.5)
    play SE1("Hit4.mp3")

    show wnei_meetwmam_5_wmam_face 2o0
    show wnei_meetwmam_5_wmam_eye 2l
    show wnei_meetwmam_5_hero_eye l
    with None

    stop BGM fadeout 3

    pause

    show wnei_meetwmam_5_wmam_face 2a3
    wmam "Oops!{w=[wt2]} I dropped a spoon."

    show wnei_meetwmam_5_wmam_face 2a2 with None

    scene bg_0
    with Dissolve(1)
    
    play BGM "audio/W2C - Lust.mp3"
    
    $ Z_alp = 0.5
    
    # WMAM starts packing leftovers, but drops a cutlery. When she stay down searching it to gather it, HERO can see her ass
    scene wnei_meetwmam_6_bg
    show wnei_meetwmam_6_wmam_body
    if wmam_love < 9:
        show wnei_meetwmam_6_wmam_wear
    show wnei_meetwmam_6_fg at Opacity
    show fx_light:
        blend "add"
    with Dissolve(2)

    pause

    $ Z_alp = 1
    show wnei_meetwmam_6_fg at Opacity with dissolve
    
    mind "(I'm glad I came to have breakfast with them today.{w=[wt3]} That's a great moment to appropriate.{w=[wt2]} I love my neighborhood.{w=[wt3]} The only problem now is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} How am I supposed to get up now with this hard on again?)"
    
    if wmam_love >= 10:

        # WMAM is without panties
        wnei "Oh, Mama{w=[wt2]}, you forgot it again!{w=[wt3]} I bet [C_Nam][fnamehero][C_Off] also noticed it but don't wanna tell you."
        wmam "Hmm...?{w=[wt3]} What, my lil sweetheart?"

        # Gladly, WNEI didn't notice what HERO noticed
        scene wnei_meetwmam_5_bg
        show wnei_meetwmam_5_wnei_body 2
        show wnei_meetwmam_5_wnei_face 2a0
        show wnei_meetwmam_5_hero_body 3
        show wnei_meetwmam_5_hero_face s2
        show wnei_meetwmam_5_hero_eye b
        show wnei_meetwmam_5_mg_food 2
        show wnei_meetwmam_5_mg_book
        show fx_light:
            blend "add"
        with Dissolve(2)

        hide wnei_meetwmam_5_hero_body
        hide wnei_meetwmam_5_hero_face
        hide wnei_meetwmam_5_hero_eye
        show wnei_meetwmam_5_wmam_body 2
        show wnei_meetwmam_5_wmam_face 2a2
        show wnei_meetwmam_5_wmam_eye 2r
        show wnei_meetwmam_5_hero_body 3
        show wnei_meetwmam_5_hero_face s2
        show wnei_meetwmam_5_hero_eye b
        hide fx_light
        show fx_light:
            blend "add"
        with dissolve

        show wnei_meetwmam_5_wnei_face 2a1
        wnei "Suggar."

        show wnei_meetwmam_5_wnei_face 2a0
        show wnei_meetwmam_5_wmam_face 2a3
        wmam "Oh, my!{w=[wt2]} I'm so sorry, my lil angel!{w=[wt2]} I can't believe{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Poor [C_Nam][fnamehero][C_Off]{w=[wt2]}, drunk all the coffee without even complaining!{w=[wt3]} You could have let me know, dear!"

        show wnei_meetwmam_5_wmam_face 2a2
        hero "D{w=[wt1]}-don't worry, [C_Nam][fnamewmam][C_Off]!{w=[wt2]} It was very good the way it was.{w=[wt2]} Thank you!{w=[wt3]} [C_Mnd](In fact{w=[wt2]}, I couldn't even concentrate on the taste amidst so many emotions.{w=[wt2]} Was it really sugar-free?{w=[wt3]} I'll never know.{w=[wt3]} Gladly, this scare ended up lowering my erection.)[C_Off]"

        show wnei_meetwmam_5_wmam_face 2a0
        show wnei_meetwmam_5_wnei_face 2a1
        wnei "[C_Nam][fnamehero][C_Off]!{w=[wt2]} Let's go!"

        show wnei_meetwmam_5_wnei_face 2a0
        hero "Sure!"
    else:
        scene wnei_meetwmam_5_bg
        show wnei_meetwmam_5_wnei_body 2
        show wnei_meetwmam_5_wnei_face 2a0
        show wnei_meetwmam_5_hero_body 3
        show wnei_meetwmam_5_hero_face s2
        show wnei_meetwmam_5_hero_eye b
        show wnei_meetwmam_5_mg_food 2
        show wnei_meetwmam_5_mg_book
        show fx_light:
            blend "add"
        with Dissolve(2)

        hide wnei_meetwmam_5_hero_body
        hide wnei_meetwmam_5_hero_face
        hide wnei_meetwmam_5_hero_eye
        show wnei_meetwmam_5_wmam_body 2
        show wnei_meetwmam_5_wmam_face 2a0
        show wnei_meetwmam_5_wmam_eye 2r
        show wnei_meetwmam_5_hero_body 3
        show wnei_meetwmam_5_hero_face s2
        show wnei_meetwmam_5_hero_eye b
        hide fx_light
        show fx_light:
            blend "add"
        with dissolve

        show wnei_meetwmam_5_wnei_face 2a1
        wnei "Done, mama!{w=[wt2]} [C_Nam][fnamehero][C_Off]!{w=[wt2]} Let's go!"

        show wnei_meetwmam_5_wnei_face 2a0
        hero "W{w=[wt1]}-well{w=[wt2]}, just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} just a moment, please.{w=[wt2]} I'll take a little more food{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} [C_Mnd](Need to wait for this to calm down before I get up.)[C_Off]"

    scene bg_0
    with Dissolve(2)

    $ a_event_0 = 0

    # WMAM packs breakfast leftovers
    while a_event_0 < 10: # Add random food items to fridge
        if renpy.random.random() < 0.25:
            $ a_event_0 += 1
            $ AddItem_Inventory("Eat_Farm_Egg", renpy.random.randint(1, 5), inventory_id=inventory_fridge)
            $ msg.msg(renpy.translate_string("[C_Itm]Egg[C_Off] is added in the fridge"))
        elif renpy.random.random() < 0.5:
            $ a_event_0 += 1
            $ AddItem_Inventory("Eat_Veg_Apple", renpy.random.randint(1, 3), inventory_id=inventory_fridge)
            $ msg.msg(renpy.translate_string("[C_Itm]Apple[C_Off] is added in the fridge"))
        elif renpy.random.random() < 0.75:
            $ a_event_0 += 1
            $ AddItem_Inventory("Eat_Snack_SandwichVegan", renpy.random.randint(1, 2), inventory_id=inventory_fridge)
            $ msg.msg(renpy.translate_string("[C_Itm]Vegan Sandwish[C_Off] is added in the fridge"))
        else:
            $ a_event_0 += 1
            $ AddItem_Inventory("Eat_Snack_ChickenCroquettes", renpy.random.randint(1, 2), inventory_id=inventory_fridge)
            $ msg.msg(renpy.translate_string("[C_Itm]Chicken Croquettes[C_Off] is added in the fridge"))

    if (wnei_inti >= 10 and hpap_love >= 10 and wmam_love >= 10): # All requirements for next stage

        if wnei_quest_6 <= 1: # Neighbor's Reunion content never started

            if wnei_quest_6 < 1: # Neighbor's Reunion 1st time invitation
                $ msg.msg(renpy.translate_string("⭐ Intimacy cap increased"))
                $ msg.msg(renpy.translate_string("⭐ {b}Content unlocked:{/b} [C_Dat]Neighbor's Reunion[C_Off]"))
                $ wnei_inti_cap = char_inti_req_date

            $ wnei_quest_6 = 1
            wmam "Take this for later, dears!{w=[wt3]} [C_Nam][fnamehero][C_Off]{w=[wt2]}, consider joining us in our lunch tomorrow!{w=[wt3]} We'll make a delicious barbecue banquet and would love to have you and your family with us!"

        else: # Neighbor's Reunion content already completed before

            wmam "Take this for later, dears!{w=[wt3]} [C_Nam][fnamehero][C_Off]{w=[wt2]}, we'll gonna have another delicious barbecue banquet tomorrow and would love to have you and your family with us!"

        hero "It'd be a pleasure, miss!{w=[wt3]} Thank you for the invitation and for this wonderful breakfast!"

    else: # No requirements for next stage
        wmam "Take this for later, dears!{w=[wt3]} [C_Nam][fnamehero][C_Off]{w=[wt2]}, you're welcome here anytime, dear!{w=[wt2]} You two can play together whenever you want!"
        hero "Thank you for the wonderful breakfast{w=[wt2]}, [C_Nam][fnamewmam][C_Off]."

    wnei "Bye bye, mama!{w=[wt2]} We're gonna have super duper fun!"
    wmam "Have fun, my little angels!"
    
    $ Set_CharMap("hero", "home", "living_room")
    $ add_stat("wnei", "inti", 1)
    $ add_stat("wmam", "love", 1)
    
    call gametime_wait(8,0) from _call_gametime_wait_24
    jump show_ui

#---------------------------------------------------------------------------
label wnei_quest_2b: # WNEI's Front House
#---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_185
    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night

    scene bg_0
    with Dissolve(3)

    wnei "So{w=[wt1]}, gimme a goodbye kiss so I can allow yar departure!"

    scene wnei_fronthouse_3_bg
    show wnei_fronthouse_3_body 3
    hide wnei_fronthouse_3_face            
    if gametimeweek == "Saturday" or gametimeweek == "Sunday":
        show wnei_fronthouse_3_outfit 3party
    else:
        show wnei_fronthouse_3_outfit 3school
    with dissolve

    menu:
        "Playful kisses on check":
            show wnei_fronthouse_3_body 4a
            hide wnei_fronthouse_3_face
            
            if gametimeweek == "Saturday" or gametimeweek == "Sunday":
                show wnei_fronthouse_3_outfit 4aparty
            else:
                show wnei_fronthouse_3_outfit 4aschool
            with Dissolve(0.25)

            show wnei_kiss
            pause
            hide wnei_kiss
            with dissolve

            $ add_stat("wnei", "love", 1)
            $ add_stat("hero", "cha_sex", 1)

        "Romantic kiss on mouth":
            $ a_event_0 = 1
            show wnei_fronthouse_3_body 4b
            show wnei_fronthouse_3_face 4a0
            
            if gametimeweek == "Saturday" or gametimeweek == "Sunday":
                show wnei_fronthouse_3_outfit 4bparty
            else:
                show wnei_fronthouse_3_outfit 4bschool
            with Dissolve(0.25)

            show wnei_fronthouse_3_face 4o0

            pause(0.5)

            show wnei_fronthouse_3_body 5
            show wnei_fronthouse_3_face 5o0
            
            if gametimeweek == "Saturday" or gametimeweek == "Sunday":
                show wnei_fronthouse_3_outfit 5party
            else:
                show wnei_fronthouse_3_outfit 5school

            wnei "{aw}Bleeeerg...!{/aw}{w=[wt2]}{nw}"

            show wnei_fronthouse_3_face 5o1
            $ add_stat("wnei", "lust", 1)
            $ add_stat("hero", "cha_sex", 0.1)

            wnei "{aw}Bleeeerg...!{/aw}{fast} What are ya doin'!?{w=[wt3]} Why do it have to be on my mouth?{w=[wt4]} Are you a harasser or what!?"

            show wnei_fronthouse_3_face 5o2

            hero "I j{w=[wt1]}-just..."

            show wnei_fronthouse_3_face 5o1

            wnei "{bt}Indecent!{/bt}"

    show wnei_fronthouse_3_body 1
    show wnei_fronthouse_3_face 1a0
    if gametimeweek == "Saturday" or gametimeweek == "Sunday":
        show wnei_fronthouse_3_outfit 1party
    else:
        show wnei_fronthouse_3_outfit 1school
    with Dissolve(1)

    show wnei_fronthouse_3_face 1a1
    wnei "So{w=[wt1]}, see ya!!"

    if hpap_love < wnei_inti_cap or (hpap_love >= wnei_inti_cap and wnei_quest_6 < 1):

        scene bg_0 with dissolve

        play SE1 "DoorOpen1.ogg"

        scene wnei_fronthouse_5_bg
        show wnei_fronthouse_5_hero_wnei_body 1
        if wnei_wear == "school":
            show wnei_fronthouse_5_hero_wnei_outfit 1school
        else:
            show wnei_fronthouse_5_hero_wnei_outfit 1party
        show wnei_fronthouse_5_hpap_body
        show wnei_fronthouse_5_hpap_arm 1
        if wnei_wear == "school":
            show wnei_fronthouse_5_hpap_outfit school
        else:
            show wnei_fronthouse_5_hpap_outfit party
        show wnei_fronthouse_5_fg
        with Dissolve(2)

        if hpap_love < 10:
            hpap "Hmph...!{w=[wt2]} Papa's lil baby{w=[wt2]}, What did I told ya 'bout being that clingy with a boy?{w=[wt4]} You can only date when you have completed a post-doctorate degree{w=[wt1]}, have a high-level job{w=[wt1]}, and are at least 59 years old."

            wnei "What are ya saying, papa?{w=[wt2]} I'm just saying goodbye to [C_Nam][fnamehero][C_Off]!"

        hpap "Oh{w=[wt2]}, [C_Nam][fnamehero][C_Off]!{w=[wt3]} Thanks for escortin' my lil angel home."

        hero "Hi, [C_Nam]Mr. [lnamewnei][C_Off]!{w=[wt2]} That's nothing.{w=[wt3]} Good to see you!"

        $ hero_ani_mouA = 0
        $ wnei_ani_mouA = 0
        $ wnei_ani_eye = 0
        $ a_event_1 = 0 # clicks

        if wnei_wear == "school":
            $ a_event_2 = 0 # Outfit 1
            $ a_event_3 = 1 # Outfit 2

        else:
            $ a_event_2 = 1 # Outfit 1
            $ a_event_3 = 0 # Outfit 2

        $ a_event_4 = 0 # HandShake
        $ a_event_5 = 0 # HandPressure

        scene wnei_fronthouse_7_bg
        show wnei_fronthouse_7_fg breathe
        show wnei_fronthouse_7_fx0 1:
            blend "add"
        with fade

        if (wnei_inti >= 10 and hpap_love >= 10 and wmam_love >= 10): # All requirements for next stage

            if wnei_quest_6 <= 1: # Neighbor's Reunion content never started

                if wnei_quest_6 < 1: # Neighbor's Reunion 1st time invitation
                    $ msg.msg(renpy.translate_string("⭐ Intimacy cap increased"))
                    $ msg.msg(renpy.translate_string("⭐ {b}Content unlocked:{/b} [C_Dat]Neighbor's Reunion[C_Off]"))
                    $ wnei_inti_cap = char_inti_req_date

                $ wnei_quest_6 = 1
                hpap "Why don't you come have lunch with us any weekend? It'd be a nice to have you and yer family here!"

            else: # Neighbor's Reunion content already completed before

                hpap "This sunday we'll have barbecue again, boy. You and yer family are more than welcome here with us!"

            hero "Thank you for the invitation, [C_Nam]Mr. [lnamewnei][C_Off]! It'd be a pleasure!"
            hpap "Show up whenever you want, kid."

        else: # No requirements for next stage
            hpap "See ya, boy."

        show screen wnei_quest_2_handshake_05

        $ a_event_1 = ((perk_phy_str + 1) * (1 + stat_phy/100))

        menu:

            "Just do a gentleman handshake":
                $ config.window = "hide"
                window hide
                hide screen wnei_quest_2_handshake_08
                show screen wnei_quest_2_handshake_20
                hide wnei_fronthouse_7_fx1 with dissolve

                $ wnei_ani_eye = 0.5
                $ hero_ani_mouA = 1
                hero "It was a pleasure to see you again, [C_Nam]Mr. [lnamewnei][C_Off]. Have a good night."

                $ add_stat("hpap", "love", 2)
                $ add_stat("wnei", "love", 1)
                $ add_stat("hero", "cha_soc", 1)

                $ wnei_ani_eye = 0
                $ hero_ani_mouA = 0
                hpap "Good night, {nm}[fnamehero]{/nm}."

            "Try to impress him{p}[C_Dat](Minigame: Thug Of War; Your Level: [a_event_1]; Opponent Level: 3)[C_Off]":

                "{nw}"

                call screen wnei_quest_2_handshake_guide

                scene bg_2 sparking
                show wnei_fronthouse_7_fg breathe
                show wnei_fronthouse_7_fx0 2:
                    blend "add"
                with fade

                hide screen wnei_quest_2_handshake_08
                show screen wnei_quest_2_handshake_20
                hide wnei_fronthouse_7_fx1 with dissolve
                $ wnei_ani_eye = 0.5
                $ a_event_5 = 50
                call screen minigame_thugofwar(var_pla=a_event_1, var_npc=3)
                #call screen wnei_quest_2_handshake_sparking

                $ renpy.pause(1, hard=True)

                $ wnei_ani_eye = 0
                if _return == "Win":
                    $ msg.msg(renpy.translate_string("You managed to impress {nm}Mr. [lnamewnei]{/nm}."))
                    $ add_stat("hpap", "love", 5)
                    $ add_stat("wnei", "love", 1)
                    $ add_stat("hero", "cha_soc", 1)
                    hpap "Well then, have a good night, {nm}[fnamehero]{/nm}."

                    $ hero_ani_mouA = 1
                    $ wnei_ani_eye = 1
                    hero "Good night, both of you!"
                else:
                    $ msg.msg(renpy.translate_string("Oops... It seems you're not strong enough."))
                    $ add_stat("hpap", "love", -1)
                    $ add_stat("wnei", "love", 1)
                    $ add_stat("hero", "cha_soc", 1)
                    hpap "One last thing, {nm}[fnamehero]{/nm}...{w=[wt3]} {b}NO HUGGING AFTER DARK!{/b}"

                    $ hero_ani_mouA = 1
                    $ wnei_ani_eye = 1
                    hero "{aw}S{w=[wt1]}-sure.{w=[wt3]} H{w=[wt1]}-have a good night.{/aw}"

        hide screen wnei_quest_2_handshake_05
        hide screen wnei_quest_2_handshake_08
        hide screen wnei_quest_2_handshake_20
        hide screen wnei_quest_2_handshake_sparking
        hide screen wnei_quest_2_handshake_guide

    scene bg_0 with Dissolve(1)
    play SE1 "DoorOpen1.ogg"
    pause(1)
    play SE1 "DoorLock.mp3"
    pause(1)

    $ add_stat("wnei", "inti", 1)
    $gametimemin += 60
    call gametime from _call_gametime_112
    call goto_home_facade from _call_goto_home_facade_3

    jump show_ui

#---------------------------------------------------------------------------
label wnei_quest_2a: # WNEI's Front House
#---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_186
    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night

    scene bg_0
    with Dissolve(3)

    scene wnei_fronthouse_1_bg
    show wnei_fronthouse_1_body 1
    if gametimeweek == "Saturday" or gametimeweek == "Sunday":
        show wnei_fronthouse_1_fg 1party
    else:
        show wnei_fronthouse_1_fg 1school
    with Dissolve(2)

    wnei "Bye {nm}[fnamehero]{/nm}!{w=[wt2]} See ya later!"
    hero "Bye!"

    scene wnei_fronthouse_2_bg
    show wnei_fronthouse_2_body 1
    if gametimeweek == "Saturday" or gametimeweek == "Sunday":
        show wnei_fronthouse_2_outfit 1party
    else:
        show wnei_fronthouse_2_outfit 1school
    with Fade(2,0,2)

    pause(1)

    show wnei_fronthouse_2_body 2
    
    if gametimeweek == "Saturday" or gametimeweek == "Sunday":
        show wnei_fronthouse_2_outfit 2party
    else:
        show wnei_fronthouse_2_outfit 2school
    show wnei_fronthouse_2_face 1
    with dissolve

    pause(0.5)

    show wnei_fronthouse_2_face 2
    with dissolve

    pause(1)

    scene wnei_fronthouse_1_bg
    show wnei_fronthouse_1_body 2
    
    if gametimeweek == "Saturday" or gametimeweek == "Sunday":
        show wnei_fronthouse_1_fg 2party
    else:
        show wnei_fronthouse_1_fg 2school
    with Fade(2,0,2)

    wnei "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}"
    hero "Hmm...?"
    wnei "Can you come here?"
    hero "S{w=[wt1]}-sure."

    stop BGM fadeout 4
    scene bg_0
    with Dissolve(2)
    scene bg_1
    with Dissolve(2)

    play BGM "audio/W2C - Romance.mp3"

    scene wnei_fronthouse_3_bg
    show wnei_fronthouse_3_body 1
    show wnei_fronthouse_3_face 1a0    
    if gametimeweek == "Saturday" or gametimeweek == "Sunday":
        show wnei_fronthouse_3_outfit 1party
    else:
        show wnei_fronthouse_3_outfit 1school
    with Dissolve(4)

    show wnei_fronthouse_3_face 1a1
    wnei "Let's make an appropriate goodbye this time."

    show wnei_fronthouse_3_face 1a0
    hero "W{w=[wt1]}-what do you mean?"

    show wnei_fronthouse_3_face 1a1
    wnei "Once{w=[wt2]}, we were playing{w=[wt2]}, talking{w=[wt2]}, and having a lotta fun.{w=[wt3]} Like a super duper cool day!{w=[wt4]} From one day to another{w=[wt1]}, ya simply disappeared.{w=[wt3]} And since that day we have never spoken again.{w=[wt4]} I never knew if I did something bad or not so ya didn't say goodbye.{w=[wt4]} So{w=[wt1]}, if ya disappear again{w=[wt1]}, I want at least the memory that ya said goodbye to me."

    show wnei_fronthouse_3_face 1a0
    hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} You didn't anything wrong."

    show wnei_fronthouse_3_face 1a1
    wnei "Is that so?"

    show wnei_fronthouse_3_face 1a0
    hero "Yes.{w=[wt4]} My father just broke with {nm}[hero_about_wmom]{/nm} and took me with him to the countryside.{w=[wt4]} It was just a surprise to me too.{w=[wt2]} I didn't even have time to understand what was going on."

    show wnei_fronthouse_3_body 2
    show wnei_fronthouse_3_face 2a0
    
    if gametimeweek == "Saturday" or gametimeweek == "Sunday":
        show wnei_fronthouse_3_outfit 2party
    else:
        show wnei_fronthouse_3_outfit 2school
    with Dissolve(1)

    show wnei_fronthouse_3_face 2a1
    wnei "You know..."

    show wnei_fronthouse_3_face 2a0
    hero "Hm?"

    show wnei_fronthouse_3_face 2a1
    wnei "Adults always want to control everything and decide what is better for children{w=[wt2]}, but never take into account what children think.{w=[wt3]} They just think of work and monotonous things!{w=[wt3]} I was always afraid of becoming that way{w=[wt2]}, So I decided I wouldn't change{w=[wt2]}, and that I'd become a super duper cool adult!"

    show wnei_fronthouse_3_face 2a0

    menu:
        wnei "Adults always want to control everything and decide what is better for children, but never take into account what children think. They just think of work and monotonous things! I was always afraid of becoming that way, So I decided I wouldn't change, and that I'd become a super duper cool adult!{fast}"
        "Say that this thought can be dangerous":
            $ add_stat("hero", "bonus_cha", 5)
            show wnei_fronthouse_3_face 2a2
            hero "You don't have to give up your essence{w=[wt1]}, but sometimes it's better to change a little.{w=[wt3]} Otherwise{w=[wt1]}, it may be difficult to deal with the difficulties of life."
            
            show wnei_fronthouse_3_face 2a3
            wnei "{bt}Ehhhh...?{/bt}{w=[wt4]} No cool!{w=[wt2]} Ya became a super duper boring man!"
        "Say that she became super cool":
            $ add_stat("wnei", "love", 1)
            show wnei_fronthouse_3_face 2a2
            hero "You are a super duper cool woman now!{w=[wt3]} You may be proud of yourself{w=[wt1]}, aren't you?"

            show wnei_fronthouse_3_face 2a1
            wnei "{lg}Tchi Hi Hi Hi...{/lg}{w=[wt2]} I am super duper proud of my super duper cool me!!!"

    wnei "So{w=[wt1]}, gimme a goodbye kiss so I can allow yar departure!"

    show wnei_fronthouse_3_body 3
    hide wnei_fronthouse_3_face            
    if gametimeweek == "Saturday" or gametimeweek == "Sunday":
        show wnei_fronthouse_3_outfit 3party
    else:
        show wnei_fronthouse_3_outfit 3school
    with dissolve

    mind "({aw}Ehhh...!?{/aw})"

    menu:
        mind "({aw}Ehhh...!?{/aw}){fast}"
        "Playful kisses on check":
            show wnei_fronthouse_3_body 4a
            hide wnei_fronthouse_3_face
            
            if gametimeweek == "Saturday" or gametimeweek == "Sunday":
                show wnei_fronthouse_3_outfit 4aparty
            else:
                show wnei_fronthouse_3_outfit 4aschool
            with Dissolve(0.25)

            show wnei_kiss
            pause
            hide wnei_kiss
            with dissolve

            $ add_stat("wnei", "love", 1)
            $ add_stat("hero", "cha_sex", 1)

        "Romantic kiss on mouth":
            $ a_event_0 = 1
            show wnei_fronthouse_3_body 4b
            show wnei_fronthouse_3_face 4a0
            
            if gametimeweek == "Saturday" or gametimeweek == "Sunday":
                show wnei_fronthouse_3_outfit 4bparty
            else:
                show wnei_fronthouse_3_outfit 4bschool
            with Dissolve(0.25)

            show wnei_fronthouse_3_face 4o0

            pause(0.5)

            show wnei_fronthouse_3_body 5
            show wnei_fronthouse_3_face 5o0
            
            if gametimeweek == "Saturday" or gametimeweek == "Sunday":
                show wnei_fronthouse_3_outfit 5party
            else:
                show wnei_fronthouse_3_outfit 5school

            wnei "{aw}Bleeeerg...!{/aw}{w=[wt2]}{nw}"

            show wnei_fronthouse_3_face 5o1
            $ add_stat("wnei", "lust", 1)
            $ add_stat("hero", "cha_sex", 0.1)

            wnei "{aw}Bleeeerg...!{/aw}{fast} What are ya doin'!?{w=[wt3]} Why do it have to be on my mouth?{w=[wt4]} Are you a harasser or what!?"

            show wnei_fronthouse_3_face 5o2

            hero "I t{w=[wt1]}-thought..."

            show wnei_fronthouse_3_face 5o1

            wnei "{bt}Indecent!{/bt}"

    show wnei_fronthouse_3_body 1
    show wnei_fronthouse_3_face 1a0
    if gametimeweek == "Saturday" or gametimeweek == "Sunday":
        show wnei_fronthouse_3_outfit 1party
    else:
        show wnei_fronthouse_3_outfit 1school
    with Dissolve(1)

    show wnei_fronthouse_3_face 1a1
    wnei "So{w=[wt1]}, we are goodbyed now.{w=[wt2]} You have learned how you do it this time, right?"

    show wnei_fronthouse_3_face 1a0
    hero "Y{w=[wt1]}-yes."

    show wnei_fronthouse_3_face 1a1
    wnei "You won't make that mistake anymore, right?"

    show wnei_fronthouse_3_face 1a0
    hero "Right."

    show wnei_fronthouse_3_face 1a1
    wnei "Good.{w=[wt3]} Then we're done here.{w=[wt3]} See ya!"

    if wnei_quest_2 == 0:
        stop BGM fadeout 3
        scene bg_0 with Dissolve(3)
        play SE1 "DoorOpen2.ogg"
        pause(1)
        play BGM "audio/W2C - Tension.mp3"
        scene wnei_fronthouse_4_bg with Dissolve(3)
        pause(1)

        mind "(Wait{w=[wt3]}, what's this menacing aura...?)"
        hpap "{aw}{b}AHEM!{/b}{/aw}{w=[wt2]} What do you think you're doing embraced like that at this hour in front of my house?"

        stop BGM fadeout 1
        scene wnei_fronthouse_5_bg
        show wnei_fronthouse_5_hero_wnei_body 1
        if wnei_wear == "school":
            show wnei_fronthouse_5_hero_wnei_outfit 1school
        else:
            show wnei_fronthouse_5_hero_wnei_outfit 1party
        show wnei_fronthouse_5_hpap_body
        show wnei_fronthouse_5_hpap_arm 1
        if wnei_wear == "school":
            show wnei_fronthouse_5_hpap_outfit school
        else:
            show wnei_fronthouse_5_hpap_outfit party
        show wnei_fronthouse_5_fg
        with dissolve
        pause(1)

        mind "(...Hmm?{w=[wt2]} A... dwarf?{nw}"

        play BGM "audio/W2C - Awkward.mp3"

        mind "(...Hmm? A... dwarf?{fast}{w=[wt3]} Since when did this neighborhood have a fantasy realm gateway?)"
        hpap "Get inside, young lady!{w=[wt3]} Yer old man's gonna have a proper talk with the man there!"
        mind "(Ehhh!?{w=[wt2]} That's her father!?{w=[wt2]} In my memories, he was like a tower!{w=[wt3]} Is this what they mean by 'childhood memories are deceiving'!?)"

        show wnei_fronthouse_5_hero_wnei_body 2
        if wnei_wear == "school":
            show wnei_fronthouse_5_hero_wnei_outfit 2school
        else:
            show wnei_fronthouse_5_hero_wnei_outfit 2party
        with dissolve

        wnei "Papa, what're ya fussin' about?{w=[wt2]} This ain't a man.{w=[wt2]} This is just {nm}[fnamehero]{/nm}."
        mind "(I wish you hadn't tried to defend me)."

        show wnei_fronthouse_5_hpap_arm 2
        hpap "Oh my!{w=[wt2]} If it ain't lil' {nm}[fnamehero]{/nm}!{w=[wt3]} Why didn't ya say so earlier?{w=[wt1]} {gg}Tee-hee...{/gg}"
        mind "(I'll step on you, you little bastard!){w=[wt4]}{nw}"
        hero "{mind}(I'll step on you, you little bastard!){/mind}{fast}. {aw}N{w=[wt1]}-no worries at all, {nm}Mr. [lnamewnei]{/nm}!{/aw}{w=[wt1]} Glad to see you again. {gg}Heh heh...{/gg}"

        $ zoomS1 = 3
        $ zoomT1 = 0
        $ zoomX1 = 0.3
        $ zoomY1 = 0
        $ zoomS2 = 2.25
        $ zoomT2 = 13
        $ zoomX2 = zoomX1
        $ zoomY2 = zoomY1+0.1

        scene wnei_fronthouse_6_bg at ZoomSTXY
        show wnei_fronthouse_6_body at ZoomSTXY
        show wnei_fronthouse_6_hpapface o1 at ZoomSTXY
        show wnei_fronthouse_6_wneiface o0 at ZoomSTXY
        if wnei_wear == "school":
            show wnei_fronthouse_6_outfit school at ZoomSTXY
        else:
            show wnei_fronthouse_6_outfit party at ZoomSTXY
        with fade
        hpap "Ya must forgive this old man's behavior, {nm}[fnamehero]{/nm}.{w=[wt3]} Your father and I were thick as thieves back in the day.{w=[wt3]} But ya see{w=[wt2]}, my precious {nm}[fnamewnei]{/nm} is as pure as fresh mountain spring water.{w=[wt3]} This cruel world would corrupt her faster than my morning coffee!{w=[wt3]} A father's gotta do what a father's gotta do to protect his child!"

        $ zoomS1 = 2.5
        $ zoomT1 = 0
        $ zoomX1 = 0.3
        $ zoomY1 = 0.1
        $ zoomS2 = 1
        $ zoomT2 = 1
        $ zoomX2 = zoomX1
        $ zoomY2 = zoomY1

        scene wnei_fronthouse_6_bg at ZoomSTXY
        show wnei_fronthouse_6_body at ZoomSTXY
        show wnei_fronthouse_6_hpapface o1 at ZoomSTXY
        show wnei_fronthouse_6_wneiface o0 at ZoomSTXY
        if wnei_wear == "school":
            show wnei_fronthouse_6_outfit school at ZoomSTXY
        else:
            show wnei_fronthouse_6_outfit party at ZoomSTXY

        mind "({pa}WHO DO YOU THINK LOOKS LIKE THE CHILD HERE!?{/pa})"

        show wnei_fronthouse_6_wneiface o1

        wnei "Papa{w=[wt2]}, yer gettin' mighty heavy there.{w=[wt2]} If ya don't lay off them beers{w=[wt2]}, I'm gonna have to start hidin'em!"

        show wnei_fronthouse_6_wneiface o0
        show wnei_fronthouse_6_hpapface o0
        hpap "Now{w=[wt1]}, now{w=[wt1]}, sweetie pie!{w=[wt2]} Papa needs his daily{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Err{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {bt}Nutrients{/bt}!"

        $ hero_ani_mouA = 0
        $ wnei_ani_mouA = 0
        $ wnei_ani_eye = 0
        $ a_event_1 = 0 # clicks
        if wnei_wear == "school":
            $ a_event_2 = 0 # Outfit 1
            $ a_event_3 = 1 # Outfit 2
        else:
            $ a_event_2 = 1 # Outfit 1
            $ a_event_3 = 0 # Outfit 2
        $ a_event_4 = 0 # HandShake
        $ a_event_5 = 0 # HandPressure

        scene wnei_fronthouse_7_bg
        show wnei_fronthouse_7_fg breathe
        show wnei_fronthouse_7_fx0 1:
            blend "add"
        with fade

        hpap "Well then, {nm}[fnamehero]{/nm}.{w=[wt3]} Thanks for escortin' my lil angel home.{w=[wt3]} It's good to have ya back in town.{w=[wt3]} My sincere apologies for missin' your return celebration.{w=[wt3]} Missus wasn't feelin' her best these days, ya see.{w=[wt3]} Had to stay by her side."

        $ wnei_ani_eye = 1
        $ hero_ani_mouA = 1
        hero "Thank you, {nm}Mr. [lnamewnei]{/nm}.{w=[wt2]} Please give my best to {nm}Mrs. [lnamewnei]{/nm}.{w=[wt2]} I hope she feels better soon."

        $ wnei_ani_eye = 0
        $ hero_ani_mouA = 0
        hpap "She will!{w=[wt3]} Drop by for dinner sometime.{w=[wt2]} She makes a mean stew!"

        show screen wnei_quest_2_handshake_05
        stop BGM fadeout 3
        $ wnei_ani_eye = 1
        $ hero_ani_mouA = 1
        hero "Sure!"

        $ hero_ani_mouA = 0
        hide screen wnei_quest_2_handshake_05
        show screen wnei_quest_2_handshake_08

        play SE1 "Perception.mp3"
        show wnei_fronthouse_7_fx1
        show wnei_fronthouse_7_fx2
        with Dissolve(1)
        pause(0.5)
        hide wnei_fronthouse_7_fx2 with dissolve

        mind "(...Wait!{w=[wt3]} I'm in trouble!!!{nw}"
        play BGM "audio/W2C - Adrenaline.mp3"
        mind "(...Wait!{w=[wt3]} I'm in trouble!!!{fast}{w=[wt4]} The handshake moment is when the father examines another man's hand{w=[wt1]}, where a firm handshake means the man is hardworking{w=[wt1]}, then worthy of his daughter.{w=[wt3]} Else{w=[wt2]}, the suitor is seen as a bum!{w=[wt3]} Am I strong enough for that?{w=[wt3]} I still can play it safe and just do a gentleman handshake.{w=[wt4]} What do I do now!?){nw}"

        menu:
            mind "(...Wait!{w=[wt3]} I'm in trouble!!!{w=[wt4]} The handshake moment is when the father examines another man's hand{w=[wt1]}, where a firm handshake means the man is hardworking{w=[wt1]}, then worthy of his daughter.{w=[wt3]} Else{w=[wt2]}, the suitor is seen as a bum!{w=[wt3]} Am I strong enough for that?{w=[wt3]} I still can play it safe and just do a gentleman handshake.{w=[wt4]} What do I do now!?){fast}"

            "Just do a gentleman handshake":
                $ config.window = "hide"
                window hide
                hide screen wnei_quest_2_handshake_08
                show screen wnei_quest_2_handshake_20
                hide wnei_fronthouse_7_fx1 with dissolve

                $ wnei_ani_eye = 0.5
                $ hero_ani_mouA = 1
                hero "It was a pleasure to see you again, {nm}Mr. [lnamewnei]{/nm}. Have a good night."

                $ add_stat("wnei", "love", 1)
                $ add_stat("hero", "cha_soc", 1)

                $ wnei_ani_eye = 0
                $ hero_ani_mouA = 0
                hpap "Good night, {nm}[fnamehero]{/nm}."

            "Try to impress him{p}[C_Dat](Minigame: Thug Of War; Your Level: 1; Opponent Level: 1)[C_Off]":

                "{nw}"

                call screen wnei_quest_2_handshake_guide

                scene bg_2 sparking
                show wnei_fronthouse_7_fg breathe
                show wnei_fronthouse_7_fx0 2:
                    blend "add"
                with fade

                hide screen wnei_quest_2_handshake_08
                show screen wnei_quest_2_handshake_20
                hide wnei_fronthouse_7_fx1 with dissolve
                $ wnei_ani_eye = 0.5
                $ a_event_5 = 50
                call screen wnei_quest_2_handshake_sparking
                label wnei_quest_2_handshake_sparkingzero:
                    $ renpy.pause(0.5, hard=True)
                    scene wnei_fronthouse_7_bg
                    show wnei_fronthouse_7_fg breathe
                    show wnei_fronthouse_7_fx0 1:
                        blend "add"
                    with Dissolve(1)

                $ wnei_ani_eye = 0
                if a_event_5 >= 50:
                    $ msg.msg(renpy.translate_string("You managed to impress {nm}Mr. [lnamewnei]{/nm}."))
                    $ add_stat("hpap", "love", 5)
                    $ add_stat("wnei", "love", 1)
                    $ add_stat("hero", "cha_soc", 1)
                    hpap "Well then, have a good night, {nm}[fnamehero]{/nm}."

                    $ hero_ani_mouA = 1
                    $ wnei_ani_eye = 1
                    hero "Good night, both of you!"
                else:
                    $ msg.msg(renpy.translate_string("Oops... It seems you're not strong enough."))
                    $ add_stat("hpap", "love", -1)
                    $ add_stat("wnei", "love", 1)
                    $ add_stat("hero", "cha_soc", 1)
                    hpap "One last thing, {nm}[fnamehero]{/nm}...{w=[wt3]} {b}NO HUGGING AFTER DARK!{/b}"

                    $ hero_ani_mouA = 1
                    $ wnei_ani_eye = 1
                    hero "{aw}S{w=[wt1]}-sure.{w=[wt3]} H{w=[wt1]}-have a good night.{/aw}"


        $ wnei_ani_eye = 1
        $ wnei_ani_mouA = 1
        $ hero_ani_mouA = 0
        wnei "G'night, {nm}[fnamehero]{/nm}!{w=[wt2]} See ya!"

        hide screen wnei_quest_2_handshake_05
        hide screen wnei_quest_2_handshake_08
        hide screen wnei_quest_2_handshake_20
        hide screen wnei_quest_2_handshake_sparking
        hide screen wnei_quest_2_handshake_guide

    $ wnei_ani_mouA = 0
    stop BGM fadeout 3
    scene bg_0
    with Dissolve(3)

    play BGM "audio/W2C - Memories.mp3"
    if a_event_0 == 1:
        mind "(I can't believe I kiss her.{w=[wt3]} I really kissed her!{w=[wt4]} But{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} She just turned her face quickly.{w=[wt4]} Has she...{w=[wt4]} Rejected me?{w=[wt4]} If she had rejected me{w=[wt1]}, she wouldn't have hugged me back, right?{w=[wt3]} I don't know if I'm happy or sad.{w=[wt2]} Maybe both.{w=[wt3]} At least{w=[wt1]}, I can still feel her lips.{w=[wt3]} I wish I could feel it for a little long.)"
    else:
        mind "(She's so lovely.{w=[wt3]} I hope we can spend more time like this together in the future.)"


    $ wnei_quest_2 = 1
    $ add_stat("wnei", "inti", 1)
    $ gametimemin += 60
    call gametime from _call_gametime_113
    call goto_home_facade from _call_goto_home_facade_4

    jump show_ui

#---------------------------------------------------------------------------
screen wnei_quest_2_handshake_05():
#---------------------------------------------------------------------------
    timer 0.01 repeat True action [
        If(a_event_4<=0.5, SetVariable("a_event_4", a_event_4+0.01))
    ]

#---------------------------------------------------------------------------
screen wnei_quest_2_handshake_08():
#---------------------------------------------------------------------------
    timer 0.01 repeat True action [
        If(a_event_4<=0.8, SetVariable("a_event_4", a_event_4+0.01))
    ]

#---------------------------------------------------------------------------
screen wnei_quest_2_handshake_20():
#---------------------------------------------------------------------------
    timer 0.01 repeat True action [
        If(a_event_4<=2, SetVariable("a_event_4", a_event_4+0.03))
    ]

#---------------------------------------------------------------------------
screen wnei_quest_2_handshake_sparking():
#---------------------------------------------------------------------------
    timer 1 repeat True action [
        If(a_event_6<5,
            true=(SetVariable("a_event_6", a_event_6+1)),
            false=(Jump("wnei_quest_2_handshake_sparkingzero")),
            )
    ]
    timer 0.15 repeat True action [
        If(a_event_5>0, [Stop("SE2"), Play("SE2", "ButtonCLICK.ogg"), SetVariable("a_event_5", a_event_5-10)])
    ]

    bar value VariableValue("a_event_5", 100) xmaximum 1000 xalign 0.5 yalign 0.9

    modal True
    key "mousedown_1" action [Stop("SE1"), Play("SE1", "ButtonCLICK.ogg"), SetVariable("a_event_5", a_event_5 + (5 + ((5 * perk_phy_str)*(1+(times_phy/100)))))]

    #vbox:
        #xalign 0.5
        #yalign 0.4
        #text str(round(a_event_5,2)) size 100
        #text "[a_event_6]" size 100

#---------------------------------------------------------------------------
screen wnei_quest_2_handshake_guide():
#---------------------------------------------------------------------------
    add "UI/BG0.webp"
    hbox:
        frame:
            xsize 540
            ysize 1080
            xpadding 50
            ypadding 50
            xalign 0.0
            yalign 0.0
            vbox:
                text renpy.translate_string("{pr}Minigames")
                textbutton _("{image=starchan} {color=#FF325B}Tug Of War{/color}")
                textbutton _("{pr}START!"):
                    action Return()
        frame:
            xsize 1400
            ysize 1080
            xoffset -20
            xpadding 50
            ypadding 50
            vbox:
                spacing 25
                label renpy.translate_string("Tug Of War")

                side ("c l"):
                    area (-10,0,1380,1280)
                    viewport id "ScrollGuide":
                        xoffset 25
                        draggable True mousewheel True
                        vbox:
                            spacing 15
                            text renpy.translate_string("In this contest of strength, click on the screen as many times as you can to force the bar to your side. The greater your [C_Dat]strength[C_Off] talent, the more points you apply with each click.")
                            image "guide_minigametugofwar"

                    vbar value YScrollValue("ScrollGuide")
