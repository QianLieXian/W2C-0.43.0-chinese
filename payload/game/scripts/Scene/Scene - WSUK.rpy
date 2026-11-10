image wsuk_xxx_a2a0 = Movie(play="images/Scene/WSUK - 1Meeting/WSUK_A2A0.webm", loop=True, start_image="wsuk_xxx_a", image="wsuk_xxx_a")
image wsuk_xxx_a2a1 = Movie(play="images/Scene/WSUK - 1Meeting/WSUK_A2A1.webm", loop=True, start_image="wsuk_xxx_a", image="wsuk_xxx_a")
image wsuk_xxx_a2a2 = Movie(play="images/Scene/WSUK - 1Meeting/WSUK_A2A2.webm", loop=True, start_image="wsuk_xxx_a", image="wsuk_xxx_a")
image wsuk_xxx_a2b = Movie(play="images/Scene/WSUK - 1Meeting/WSUK_A2B.webm", loop=False, start_image="wsuk_xxx_a", image="wsuk_xxx_b")
image wsuk_xxx_b2c = Movie(play="images/Scene/WSUK - 1Meeting/WSUK_B2C.webm", loop=False, start_image="wsuk_xxx_b", image="wsuk_xxx_c")
image wsuk_xxx_b2b:
    choice:
        Movie(play="images/Scene/WSUK - 1Meeting/WSUK_B2B1.webm", loop=False, start_image="wsuk_xxx_b", image="wsuk_xxx_b")
        2.7
    choice:
        Movie(play="images/Scene/WSUK - 1Meeting/WSUK_B2B2.webm", loop=False, start_image="wsuk_xxx_b", image="wsuk_xxx_b")
        2.7
    choice:
        Movie(play="images/Scene/WSUK - 1Meeting/WSUK_B2B3.webm", loop=False, start_image="wsuk_xxx_b", image="wsuk_xxx_b")
        2.7
    choice:
        Movie(play="images/Scene/WSUK - 1Meeting/WSUK_B2B4.webm", loop=False, start_image="wsuk_xxx_b", image="wsuk_xxx_b")
        2.7
    repeat

# ---------------------------------------------------------------------------
screen xxx_locker_1leg_wsuk_ani():
# ---------------------------------------------------------------------------
    timer 0.01 repeat True action [

        # Character Data
        SetVariable("loveadd_wsuk", ((4.0 * ((1.00 + (perk_cha_sex * 0.2)) * (1 + (stat_cha * 0.0025)))) * (1 + (0.01 * wsuk_bonus))) / (1 + (int(Club_IsMember("hero", "stco")) * 0.3))),
        SetVariable("lustadd_wsuk", ((2.0 * ((1.00 + (perk_cha_sex * 0.2)) * (1 + (stat_cha * 0.0025)))) * (1 + (0.01 * wsuk_bonus))) / (1 + (int(Club_IsMember("hero", "stco")) * 0.3)) / (1 + (wsuk_lust * wsuk_lust * 0.0001))),
        SetVariable("intiadd_wsuk", ((2.0 * ((1.00 + (perk_cha_sex * 0.2)) * (1 + (stat_cha * 0.0025)))) * (1 + (0.01 * wsuk_bonus))) / (1 + (int(Club_IsMember("hero", "stco")) * 0.3)) * (0.8 + (wsuk_love * 0.01)) * (0.9 + (wsuk_lust * 0.005)) / (1 + (wsuk_inti * 0.02))),

        # Reaction Energy
        SetVariable("hero_enrg", hero_enrg - 0.02 - ((0.1 * abs(wsuk_ani_xxx_speed*wsuk_ani_xxx_speed)) / (0.25 + (perk_phy_res * 0.25)))),
        SetVariable("wsuk_enrg", wsuk_enrg - 0.01 - (0.05 * abs(wsuk_ani_xxx_speed*wsuk_ani_xxx_speed) + (wsuk_pain*wsuk_pain / 1000000))),

        # Mouth Expression
        If(renpy.get_screen("xxx_locker_1leg_wsuk_warning"),
            true=(
                If(wsuk_ani_mouth <= 3, SetVariable("a_event_6", 1)),
                If(wsuk_ani_mouth >= 4, SetVariable("a_event_6", 2)),
                If(a_event_6 == 0, SetVariable("wsuk_ani_mouth", 3)),
                If(a_event_6 == 1, SetVariable("wsuk_ani_mouth", wsuk_ani_mouth+0.2)),
                If(a_event_6 == 2, SetVariable("wsuk_ani_mouth", wsuk_ani_mouth-0.2)),
                ),
            false=(
                If(wsuk_ani_mouth <= 2,
                    true=(If(wsuk_ani_mouth > 1, SetVariable("wsuk_ani_mouth", wsuk_ani_mouth-0.005))),
                    false=(If(wsuk_ani_mouth <= 4,
                        true=(If(wsuk_ani_mouth > 3, SetVariable("wsuk_ani_mouth", wsuk_ani_mouth-0.04))),
            ))))),

        # Auto Mode
        If(a_event_7 == 1,
            true=([

                # Get Data
                #SetVariable("a_event_0", wsuk_ani_xxx_frame),
                SetVariable("wsuk_ani_xxx_speed", a_event_8 + hero_xspd/3),

                # Penetration IN
                If(wsuk_ani_xxx_frame == 0,
                    If(wsuk_ani_xxx < 2+(wsuk_ani_xxx_speed),
                        true=([SetVariable("wsuk_ani_xxx", wsuk_ani_xxx + wsuk_ani_xxx_speed), If(wsuk_ani_xxx_grip>0, SetVariable("wsuk_ani_xxx_grip", wsuk_ani_xxx_grip-wsuk_ani_xxx_speed))]),
                        false=([SetVariable("wsuk_ani_xxx_frame", 1), Jump("wsuk_quest_0_2_randomizer")]),
                    )),

                # Penetration OUT
                If(wsuk_ani_xxx_frame == 1,
                    If(wsuk_ani_xxx > 1,
                        true=([SetVariable("wsuk_ani_xxx", wsuk_ani_xxx - wsuk_ani_xxx_speed), If(wsuk_ani_xxx_grip<1, SetVariable("wsuk_ani_xxx_grip", wsuk_ani_xxx_grip+wsuk_ani_xxx_speed))]),
                        false=([SetVariable("wsuk_ani_xxx_frame", 0), Jump("wsuk_quest_0_2_randomizer")]),
                    )),

                # Impact
                If(wsuk_ani_xxx > 2,
                    If(wsuk_ani_xxx_speed > 0.1, SetVariable("wsuk_ani_xxx_implow_on", 1)),
                    If(wsuk_ani_xxx_speed > 0.5, SetVariable("wsuk_ani_xxx_imphig_on", 2)),
                    ),

                # Reaction Lust
                SetVariable("hero_lust", hero_lust + ((1 * abs(wsuk_ani_xxx_speed)) / (1 + perk_cha_sex))),

                If(abs(wsuk_ani_xxx_speed) != 0, true=([
                    If(wsuk_ani_xxx <= 2.1,
                        true=(SetVariable("wsuk_lust", wsuk_lust + (lustadd_wsuk * (0.02 / (0.01 + abs((wsuk_ani_xxx_speed*wsuk_ani_xxx_speed*wsuk_ani_xxx_speed*1000)-1))) * (0.5 + (perk_cha_sex * perk_cha_sex * 0.25)) / (0.9 + (a_event_1 * a_event_1 * 0.1))) )),
                        false=([
                            SetVariable("wsuk_lust", wsuk_lust - ((lustrem_wsuk / (0.5 + (perk_cha_sex * perk_cha_sex * 0.5)) * (0.0001 * (wsuk_ani_xxx * wsuk_ani_xxx * wsuk_ani_xxx))) / (0.9 + (a_event_1 * a_event_1 * 0.1)) ) ),
                            SetVariable("wsuk_pain", wsuk_pain + ( ( abs(wsuk_ani_xxx_speed) * wsuk_ani_xxx * wsuk_ani_xxx * wsuk_ani_xxx) / (0.9 + (a_event_1 * a_event_1 * 0.1)) ) ),
                        ])),
                    ])),

                # Reaction Impact
                If(wsuk_ani_xxx_implow_on == 1,
                    true=(If(wsuk_ani_xxx_implow < 1,
                        true=([SetVariable("wsuk_ani_xxx_implow", wsuk_ani_xxx_implow + (0.04)), Jump("wsuk_quest_1_1_Moan2")]),
                        false=([SetVariable("wsuk_ani_xxx_implow_on", 0), SetVariable("wsuk_ani_xxx_implow", 0)])
                        )),
                    ),

                If(wsuk_ani_xxx_imphig_on == 2,
                    true=(If(wsuk_ani_xxx_imphig < 1,
                        true=([SetVariable("wsuk_ani_xxx_imphig", wsuk_ani_xxx_imphig + (0.03)), Jump("wsuk_quest_1_1_Moan3")]),
                        false=([SetVariable("wsuk_ani_xxx_imphig_on", 0), SetVariable("wsuk_ani_xxx_imphig", 0)])
                        )),
                    ),

                If(wsuk_ani_xxx > 2,
                    true=(If(wsuk_ani_xxx_speed > 0, SetVariable("wsuk_pain", wsuk_pain + (5 * abs(wsuk_ani_xxx_speed * wsuk_ani_xxx_speed))))),
                    false=(SetVariable("wsuk_pain", max(0, wsuk_pain - (0.01 / 1 + (abs(wsuk_ani_xxx_speed * wsuk_ani_xxx_speed)))))),        
                    ),

                If(wsuk_ani_xxx > 3,
                    If(wsuk_ani_xxx_speed > 0, SetVariable("wsuk_pain", wsuk_pain + (15 * abs(wsuk_ani_xxx_speed * wsuk_ani_xxx_speed)))),
                    ),

                # Warning
                If(wsuk_pain >= a_event_5, Jump("wsuk_quest_1_1_warn")),

                # Finish
                If(wsuk_pain >= 100, Jump("wsuk_quest_1_1_end")),

                If(random.random() > (1.05 + (perk_cha_sex * 0.02) - (hero_lust * hero_lust / 100000)), Jump("wsuk_quest_1_1_end")),

                If(random.random() > (1.07 - (wsuk_lust * wsuk_lust / 100000)), Jump("wsuk_quest_1_1_cum")),

            ])),

        If(a_event_7 == -1,
            If(wsuk_ani_xxx > -1,
                true=([SetVariable("wsuk_ani_xxx", min(1, wsuk_ani_xxx-0.05)), SetVariable("wsuk_ani_eyeX", 0.5)]),
                false=([SetVariable("wsuk_ani_xxx", -1), SetVariable("a_event_7", 0)]),
            )),

        # Turn Control ON
        If(wsuk_ani_xxx_on == True, 
            true=([
                # Insert Animation
                If(wsuk_ani_xxx < 1, [SetVariable("wsuk_ani_xxx", min(1, wsuk_ani_xxx+0.05)), SetVariable("wsuk_ani_eyeX", 0.5)]),

                # Mouse Position
                If(renpy.get_mouse_pos()[1]/1080 >= 0.5, true=(
                    If(renpy.get_mouse_pos()[0]/1920 >= 0.7, true=([

                        # Speed
                        If(wsuk_ani_xxx_speed > 0, [

                            SetVariable("wsuk_ani_xxx_media", ((wsuk_ani_xxx_media + wsuk_ani_xxx_speed) / 1.1)),
                            
                            # Grip
                            If( (((6 - (renpy.get_mouse_pos()[1]/(1080/5))) - wsuk_ani_xxx_frame) < 0), If(wsuk_ani_xxx_grip<1, SetVariable("wsuk_ani_xxx_grip", wsuk_ani_xxx_grip+wsuk_ani_xxx_speed))),
                            If( (((6 - (renpy.get_mouse_pos()[1]/(1080/5))) - wsuk_ani_xxx_frame) > 0), If(wsuk_ani_xxx_grip>0, SetVariable("wsuk_ani_xxx_grip", wsuk_ani_xxx_grip-wsuk_ani_xxx_speed))),

                            ]),

                        SetVariable("wsuk_ani_xxx_speed", abs((6 - (renpy.get_mouse_pos()[1]/(1080/5))) - wsuk_ani_xxx_frame)),
                        SetVariable("wsuk_ani_xxx_frame", 6 - (renpy.get_mouse_pos()[1]/(1080/5))),

                        # Control
                        If(wsuk_ani_xxx_on == True, true=([
                            If(wsuk_ani_xxx >= 1, SetVariable("wsuk_ani_xxx", max(1, min(3, (5 - (renpy.get_mouse_pos()[1]/(1080/4))))))),
                            If(wsuk_ani_xxx > 2,
                                If(wsuk_ani_xxx_speed > 0.1, SetVariable("wsuk_ani_xxx_implow_on", 1)),
                                If(wsuk_ani_xxx_speed > 0.5, SetVariable("wsuk_ani_xxx_imphig_on", 2)),

                            )])),

                        # Reaction Lust
                        SetVariable("hero_lust", hero_lust + ((1 * abs(wsuk_ani_xxx_speed)) / (1 + perk_cha_sex))),

                        If(abs(wsuk_ani_xxx_speed) != 0, true=([
                            If(wsuk_ani_xxx <= 2.1,
                                true=(SetVariable("wsuk_lust", wsuk_lust + (lustadd_wsuk * (0.02 / (0.01 + abs((wsuk_ani_xxx_speed*wsuk_ani_xxx_speed*wsuk_ani_xxx_speed*1000)-1))) * (0.5 + (perk_cha_sex * perk_cha_sex * 0.25)) / (0.9 + (a_event_1 * a_event_1 * 0.1))) )),
                                false=([
                                    SetVariable("wsuk_lust", wsuk_lust - ((lustrem_wsuk / (0.5 + (perk_cha_sex * perk_cha_sex * 0.5)) * (0.0001 * (wsuk_ani_xxx * wsuk_ani_xxx * wsuk_ani_xxx))) / (0.9 + (a_event_1 * a_event_1 * 0.1)) ) ),
                                    SetVariable("wsuk_pain", wsuk_pain + ( ( abs(wsuk_ani_xxx_speed) * wsuk_ani_xxx * wsuk_ani_xxx * wsuk_ani_xxx) / (0.9 + (a_event_1 * a_event_1 * 0.1)) ) ),
                                ])),
                            ])),

                        # Reaction Impact
                        If(wsuk_ani_xxx_implow_on == 1,
                            true=(If(wsuk_ani_xxx_implow < 1,
                                true=([SetVariable("wsuk_ani_xxx_implow", wsuk_ani_xxx_implow + (0.04)), Jump("wsuk_quest_1_1_Moan2")]),
                                false=([SetVariable("wsuk_ani_xxx_implow_on", 0), SetVariable("wsuk_ani_xxx_implow", 0)])
                                )),
                            ),

                        If(wsuk_ani_xxx_imphig_on == 2,
                            true=(If(wsuk_ani_xxx_imphig < 1,
                                true=([SetVariable("wsuk_ani_xxx_imphig", wsuk_ani_xxx_imphig + (0.03)), Jump("wsuk_quest_1_1_Moan3")]),
                                false=([SetVariable("wsuk_ani_xxx_imphig_on", 0), SetVariable("wsuk_ani_xxx_imphig", 0)])
                                )),
                            ),

                        If(wsuk_ani_xxx > 2,
                            true=(If(wsuk_ani_xxx_speed > 0, SetVariable("wsuk_pain", wsuk_pain + (5 * abs(wsuk_ani_xxx_speed * wsuk_ani_xxx_speed))))),
                            false=(SetVariable("wsuk_pain", max(0, wsuk_pain - (0.01 / 1 + (abs(wsuk_ani_xxx_speed * wsuk_ani_xxx_speed)))))),        
                            ),

                        If(wsuk_ani_xxx > 3,
                            If(wsuk_ani_xxx_speed > 0, SetVariable("wsuk_pain", wsuk_pain + (15 * abs(wsuk_ani_xxx_speed * wsuk_ani_xxx_speed)))),
                            ),

                        # Warning
                        If(wsuk_pain >= a_event_5, Jump("wsuk_quest_1_1_warn")),

                        # Finish
                        If(wsuk_pain >= 100, Jump("wsuk_quest_1_1_end")),

                        If(random.random() > (1.05 + (perk_cha_sex * 0.02) - (hero_lust * hero_lust / 100000)), Jump("wsuk_quest_1_1_end")),

                        If(random.random() > (1.07 - (wsuk_lust * wsuk_lust / 100000)), Jump("wsuk_quest_1_1_cum")),

                        ])),
                    )),
                ]),

            false=(
                If(wsuk_ani_xxx > 0, true=(
                    If(a_event_7 == 0, SetVariable("wsuk_ani_xxx", max(0, wsuk_ani_xxx-0.05)))
                    ))),
            ),

        # Breathe
        If(hero_ani_breathing_turn == 0,
            true=(If(hero_ani_breathing <= 1/(1+(0.04*hero_enrg)), true=(SetVariable("hero_ani_breathing", hero_ani_breathing + (0.05/(1+(0.00001*hero_enrg*hero_enrg*hero_enrg))))), false=(SetVariable("hero_ani_breathing_turn", 1)))),
            false=(If(hero_ani_breathing >= 0, true=(SetVariable("hero_ani_breathing", hero_ani_breathing - (0.05/(1+(0.001*hero_enrg*hero_enrg))))), false=(SetVariable("hero_ani_breathing_turn", 0)))),
            ),
        If(wsuk_ani_breathing_turn == 0,
            true=(If(wsuk_ani_breathing <= 1, true=(SetVariable("wsuk_ani_breathing", wsuk_ani_breathing + (0.01*wsuk_ani_breathing_speed))), false=(SetVariable("wsuk_ani_breathing_turn", 1)))),
            false=(If(wsuk_ani_breathing >= 0, true=(SetVariable("wsuk_ani_breathing", wsuk_ani_breathing - (0.01*wsuk_ani_breathing_speed))), false=(SetVariable("wsuk_ani_breathing_turn", 0)))),
            ),

    ]

# ---------------------------------------------------------------------------
screen xxx_locker_1leg_wsuk_warning():
# ---------------------------------------------------------------------------
    timer 0.1 repeat True action [
        SetVariable("a_event_4", a_event_4 + 1),
        If(a_event_4>25, Hide("xxx_locker_1leg_wsuk_warning")),
        ]

    frame:
        background None
        xalign 0.4
        yalign 0.9
        vbox:
            text renpy.translate_string("{b}{nm}[fnamewsuk] [lnamewsuk]{/nm}{/b}") size 40 color "#FFF" outlines [(2, "#323232", 0, 0)] xalign 0.0
            text renpy.translate_string("{b}Hold on! This way it's hurting!{/b}") size 60 color "#FFF" outlines [(2, "#323232", 0, 0)] xalign 0.5

# ---------------------------------------------------------------------------
screen xxx_locker_1leg_wsuk_ui():
# ---------------------------------------------------------------------------
    if a_event_9 == -1:
        frame:
            xysize(1920,1080)
            xpadding 25
            ypadding 25
            background None                
            imagebutton:
                xalign 1.0
                yalign 0.0
                idle At("images/UI/QUICK_Hide.webp", ButtonIdle)
                hover At("images/UI/QUICK_Hide.webp", ButtonHover)
                action SetVariable("a_event_9", 0)
    else:
        frame:
            xpadding 25
            ypadding 25
            background "images/UI/MinigameAction/UI Hentai.webp"

            #vbox:
                #xalign 0.5
                #yalign 0.1
                #text "Speed = "+str(round(wsuk_ani_xxx_speed,2)) size 100 color "#FFF" outlines [(2, "#323232", 0, 0)]
                #text "Media = "+str(round(wsuk_ani_xxx_media,2)) size 60 color "#FFF" outlines [(2, "#323232", 0, 0)]
                #text "a_event_5 = "+str(round(a_event_5,2)) size 60 color "#FFF" outlines [(2, "#323232", 0, 0)]
                #text "Pain = "+str(round(wsuk_pain,2)) size 60 color "#FFF" outlines [(2, "#323232", 0, 0)]

            hbox:
                xalign 0.0
                spacing 25
                vbox:
                    spacing 10
                    #bar value VariableValue("wsuk_ani_xxx_speed", 10) xmaximum 500
                    #bar value VariableValue("hero_ani_breathing_speed", 10) xmaximum 500
                    #bar value VariableValue("wsuk_ani_breathing_speed", 10) xmaximum 500
                    image "images/UI/OC_WSUK.webp"
                    vbar:
                        xysize(150,150)
                        value AnimatedValue(wsuk_lust, 100, delay=1)
                        left_bar "gui/CustomBar/LustMin.webp"
                        right_bar "gui/CustomBar/LustMax.webp"
                    vbar:
                        xysize(150,150)
                        value AnimatedValue(wsuk_enrg, 100, delay=1)
                        left_bar "gui/CustomBar/EnrgMin.webp"
                        right_bar "gui/CustomBar/EnrgMax.webp"
                    vbar:
                        xysize(150,150)
                        value AnimatedValue(wsuk_pain, 100, delay=1)
                        left_bar "gui/CustomBar/PainMin.webp"
                        right_bar "gui/CustomBar/PainMax.webp"
                vbox:
                    spacing 10
                    #bar value VariableValue("wsuk_ani_xxx_speed", 10) xmaximum 500
                    #bar value VariableValue("hero_ani_breathing_speed", 10) xmaximum 500
                    #bar value VariableValue("wsuk_ani_breathing_speed", 10) xmaximum 500
                    image "images/UI/OC_HERO.webp"
                    vbar:
                        xysize(150,150)
                        value AnimatedValue(hero_lust, 100, delay=1)
                        left_bar "gui/CustomBar/LustMin.webp"
                        right_bar "gui/CustomBar/LustMax.webp"
                    vbar:
                        xysize(150,150)
                        value AnimatedValue(hero_enrg, 100, delay=1)
                        left_bar "gui/CustomBar/EnrgMin.webp"
                        right_bar "gui/CustomBar/EnrgMax.webp"

            vpgrid:
                xalign 1.0
                spacing 25
                cols 3
                imagebutton:
                    idle At("images/UI/QUICK_Hide.webp", ButtonIdle)
                    hover At("images/UI/QUICK_Hide.webp", ButtonHover)
                    action SetVariable("a_event_9", -1)
                if a_event_7 == 0:
                    imagebutton:
                        idle At("images/UI/X_1Leg.webp", ButtonIdle)
                        hover At("images/UI/X_1Leg.webp", ButtonHover)
                        action ToggleVariable("wsuk_ani_xxx_on", True)
                else:
                    imagebutton:
                        idle At("images/UI/X_1Leg.webp", ButtonOff)
                        hover At("images/UI/X_1Leg.webp", ButtonOff)
                        action None

                if hero_xspd > 0 and wsuk_ani_xxx_on != True:
                    imagebutton:
                        idle At("images/UI/X_Auto.webp", ButtonIdle)
                        hover At("images/UI/X_Auto.webp", ButtonHover)
                        action ToggleVariable("a_event_7", 1, -1)
                else:
                    imagebutton:
                        idle At("images/UI/X_Auto.webp", ButtonOff)
                        hover At("images/UI/X_Auto.webp", ButtonOff)
                        action None

                if hero_lust > 80:
                    imagebutton:
                        idle At("images/UI/X_Cum.webp", ButtonIdle)
                        hover At("images/UI/X_Cum.webp", ButtonHover)
                        action [SetVariable("a_event_3", 1), Jump("wsuk_quest_1_1_end")]
                else:
                    imagebutton:
                        idle At("images/UI/X_Cum.webp", ButtonOff)
                        hover At("images/UI/X_Cum.webp", ButtonOff)
                        action None


        #frame:
            #background None
            #xalign 1.0
            #yalign 1.0
            #xysize (576 , 540)
            #drag:
                #drag_name "DragDick"
                #xalign 0.5
                #yalign 0.2
                #draggable True
                #droppable False
                #dragged drag_placed
                #drag_raise True
                #image "images/UI/MinigameAction/DRAG_Dick.webp"

# ---------------------------------------------------------------------------
label wsuk_quest_0_2_prototype:
# ---------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_203

    menu:
        "Prototype Menu{fast}"

        "Have sex at the locker":
            jump wsuk_quest_1_2

        "Return":
            jump show_ui

# ---------------------------------------------------------------------------
label wsuk_quest_0_1:
# ---------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_204

    scene bg_school classroom_3a
    show HERO at LC
    show WSUK at RC
    with fade

    if wsuk_quest_1 == 0:
        $ wsuk_quest_1 = 1

        wsuk "{bt}Well, well...{/bt}{w=[wt2]} if it isn't my favorite stud dropping by at closing time.{w=[wt3]} Come to rethink that invitation to join the club, babe?{w=[wt2]} Or maybe you're here for something a little more{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} personal? ~❤"

        hero "I was just{w=[wt2]}, uh{w=[wt2]}, passing by.{w=[wt3]} Wanted to see more about the club activities."

        wsuk "{gg}Tee-hee...{/gg}{w=[wt2]} Activities, huh?{w=[wt3]} The school's emptying out right now.{w=[wt2]} Everyone's heading home{w=[wt2]}, even those nosy Student Council types.{w=[wt3]} We could lock the door and have the whole room to ourselves.{w=[wt2]} I could show you some private dance moves.{w=[wt3]} Ones that require a very attentive partner."

        hero "{aw}P{w=[wt1]}-private moves?{/aw}"

        wsuk "{bt}Mmm-hmm...{/bt}{w=[wt2]} Remember how I said body language is uninhibited here?{w=[wt3]} Let me demonstrate.{w=[wt2]} Unless you're still hung up on that 'misunderstanding' with your ex and her friend.{w=[wt2]} Don't worry, babe.{w=[wt3]} I don't mind sharing secrets.{w=[wt3]} Or anything else, for that matter."

        wsuk "Or are you gonna chicken out like with your jerk friend around?{w=[wt3]} Come on, babe!{w=[wt2]} Imagine the fun we could have.{w=[wt2]} Me{w=[wt2]}, you{w=[wt2]}, these mirrors reflecting every angle...{w=[wt3]} Sounds steamy, doesn't it?"

    else:
        wsuk "{bt}Well, well...{/bt}{w=[wt2]} if it isn't my favorite stud dropping by at closing time.{w=[wt3]} Wanna have fun? ~❤"

    menu:
        "Accept":
            hero "Alright... let's do this."

            wsuk "{bt}That's what I like to hear!{/bt}{w=[wt2]} Follow me, hottie.{w=[wt3]} Time to make some art... the performing kind. ~❤"

            jump wsuk_quest_1_2

        "Refuse":
            hero "I... I can't right now."

            wsuk "{aw}Aww, really?{/aw}{w=[wt2]} You're breaking my heart here.{w=[wt3]} Fine, but don't keep a girl waiting too long next time."

            jump show_ui

# ---------------------------------------------------------------------------
label wsuk_quest_1_2:
# ---------------------------------------------------------------------------

    stop BGM fadeout 5
    scene bg_0
    with Dissolve(2)

    menu:
        "Sex content is currently under development and should be reworked on next update. For now, you can decide what prototype you prefer.{fast}"

        "Play Sex Minigame [C_Mnd](PROTOTYPE)[C_Off]":
            pass

        "Run Sex Animation [C_Mnd](BETA)[C_Off]":
            $ hero_xnum += 1
            play BGM "audio/W2C - Lust.mp3"

            scene wsuk_xxx_a2a0
            with Dissolve(3)

            pause

            scene wsuk_xxx_a2a2
            wsuk "{bt}Mmm...{/bt}{w=[wt2]} Come on, babe...{w=[wt3]} Can't you see how ready I am? ~❤.{w=[wt3]} Don't keep a girl waiting when she's this...{w=[wt2]} {aw}wet{/aw}{w=[wt2]}, and willing.{w=[wt3]} Hurry up and slide that big thing inside me already, hmm? ~❤!{nw}"

            scene wsuk_xxx_a2a0
            wsuk "{bt}Mmm...{/bt}{w=[wt2]} Come on, babe...{w=[wt3]} Can't you see how ready I am? ~❤.{w=[wt3]} Don't keep a girl waiting when she's this...{w=[wt2]} {aw}wet{/aw}{w=[wt2]}, and willing.{w=[wt3]} Hurry up and slide that big thing inside me already, hmm? ~❤!{fast}"

            scene wsuk_xxx_a2a1
            hero "S{w=[wt1]}-sure{w=[wt2]}, here I come!{nw}"

            scene wsuk_xxx_a2a0
            hero "S{w=[wt1]}-sure{w=[wt2]}, here I come!{fast}"

            scene wsuk_xxx_a2b

            $ renpy.pause(2.7, hard=True)

            scene wsuk_xxx_b2b

            $ a_event_0 = "b"

            while a_event_0 != "c":
                pause
                menu:
                    "Keep":
                        pass
                    "Cum":
                        $ a_event_0 = "c"

            scene wsuk_xxx_b2c

            $ renpy.pause(2.7, hard=True)

            scene wsuk_xxx_c

            $ a_event_0 = "c"
            $ hero_xnum += 1
            $ msg.msg(renpy.translate_string("You came."))
            $ xp_now += 25
            $ msg.msg(renpy.translate_string("XP [C_Pos]+ 25[C_Off]."))

            pause(0.5)

            scene bg_0
            with Dissolve(3)

            $ gametimemin = 1140 - ((gametimehour * 60) + gametimemin)
            pause
            jump show_ui

    if hero_xnum == 0:
        scene bg_0 with Dissolve(1)
        play SE1 "JingleRight.ogg"
        $ msg.msg(renpy.translate_string("[C_Dat]H Scene (Action)[C_Off] unlocked"))
        call screen WSUK_show_Guide with dissolve

    screen WSUK_show_Guide():
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
                    textbutton _("{image=starchan} {color=#FF325B}H Scene (Action){/color}")
                    textbutton _("{pr}START!"):
                        action Function(renpy.jump, "wsuk_show_guide")
            frame:
                xsize 1400
                ysize 1080
                xoffset -20
                xpadding 50
                ypadding 50
                vbox:
                    spacing 25
                    label renpy.translate_string("H Scene (Action)")

                    side ("c l"):
                        area (-10,0,1380,1280)
                        viewport id "ScrollGuide": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                            xoffset 25
                            draggable True mousewheel True
                            vbox:
                                spacing 15
                                text renpy.translate_string("Sex content is completely player-controllable, with performance dependent on skills and attributes such as [C_Dat]Sensuality[C_Off].{pr}Click the penetration button to enable control.")
                                image "guide_minigameact_1"
                                text renpy.translate_string("Move the cursor/finger in the red area below to control penis movement after is control is enabled. The speed at which you move this is very important to define the characters' reactions of pleasure, pain, and breath.{pr}The upper part of the control area can cause pain to the girl if you make too many sudden movements, and if the pain indicator reaches its maximum, the scene ends.{pr}Note the speed at which the girl feels the most pleasure and use this to your advantage.")
                                image "guide_minigameact_2"
                                text renpy.translate_string("The closer a character's lust meter gets to maximum, the more likely they are to cum. If you cum, the scene ends. The higher the [C_Dat]Sensuality[C_Off] skill level, the less likely you are to automatically cum, and the higher is girl's pleasure.{pr}For the highest possible score, make the girl cum at least 3 times, and cum at the same time as her.{pr}To cum at the same time as the girl, you need to click the ejaculation button when the girl has at least 90% lust, or has more lust than you.")
                                image "guide_minigameact_3"
                                text renpy.translate_string("Want to just watch the scene while leaving your right hand free? No problem! Just use the automatic mode and hide the interface. The automatic mode is enabled after the first sexual intercourse. This mode calculates the average speed of your movements from your last sexual intercourse and tries to simulate your speed.")
                                image "guide_minigameact_4"
                                text renpy.translate_string("This content is still in the process of being improved and the energy indicator is not very useful. A mechanic for a better penis control, different positions; reactions; and scenarios should be implemented in the future.")
                        vbar value YScrollValue("ScrollGuide") #TAKES YOUR VIEWPORT ID AS THE ARG
                null height 20 #just a height set.
    
    label wsuk_show_guide:
        pass

    $ config.allow_skipping = False
    $ config.rollback_enabled = False

    $ wsuk_quest_2 = 1 # Trigger Enable
    $ a_event_1 = 0 # wsuk cum times
    $ a_event_3 = 0 # hero controled cum
    $ a_event_4 = 0 # pain warning time
    $ a_event_5 = 20 # pain warning
    $ a_event_6 = 0 # talking mouth
    $ a_event_7 = 0 # auto (0 = OFF, 1 = ON)
    $ hero_lust = 10
    $ wsuk_lust += 20

    $ wsuk_ani_mouth = 1
    $ wsuk_ani_eyeX = 0.0
    $ wsuk_ani_eyeY = 0.2
    $ wsuk_ani_xxx = -1
    $ wsuk_ani_xxx_on = False
    $ wsuk_ani_xxx_grip = 0
    $ wsuk_ani_xxx_speed = 0
    $ wsuk_ani_xxx_media = 0
    $ wsuk_ani_xxx_frame = 0
    $ wsuk_ani_xxx_implow = 0
    $ wsuk_ani_xxx_imphig = 0
    $ wsuk_ani_xxx_implow_on = 0
    $ wsuk_ani_xxx_imphig_on = 0
    $ hero_ani_breathing = 0
    $ wsuk_ani_breathing = 0.9
    $ hero_ani_breathing_speed = 1
    $ wsuk_ani_breathing_speed = 1
    $ hero_ani_breathing_turn = 0
    $ wsuk_ani_breathing_turn = 0

    play BGM "audio/W2C - Lust.mp3"

    show screen xxx_locker_1leg_wsuk_ani
    scene xxx_locker_1leg_bg 1
    show xxx_locker_1leg_wsuk breathe_hero
    show xxx_locker_1leg_fx:
        blend "add"
    with Dissolve(4)

    call screen xxx_locker_1leg_wsuk_ui with dissolve

    $ renpy.pause(hard=True)
    jump wsuk_quest_1_1_end

# ---------------------------------------------------------------------------
label wsuk_quest_0_2_randomizer:
# ---------------------------------------------------------------------------
    $ a_event_8 = random.random()/10
    jump wsuk_quest_1_1_recall

# ---------------------------------------------------------------------------
label wsuk_quest_1_1_Moan1:
# ---------------------------------------------------------------------------
    if not renpy.music.is_playing(channel="SE2"):
        play SE2 renpy.random.choice(["Moan/C lvl1 (1).ogg","Moan/C lvl1 (2).ogg","Moan/C lvl1 (3).ogg","Moan/C lvl1 (4).ogg"])
        $ wsuk_ani_eyeX = 0.0
        $ wsuk_ani_eyeY = 0.2
        $ wsuk_ani_mouth = 3.2
    jump wsuk_quest_1_1_recall

# ---------------------------------------------------------------------------
label wsuk_quest_1_1_Moan2:
# ---------------------------------------------------------------------------
    if not renpy.music.is_playing(channel="SE2"):
        play SE2 renpy.random.choice(["Moan/C lvl2 (1).ogg","Moan/C lvl2 (2).ogg","Moan/C lvl2 (3).ogg","Moan/C lvl2 (4).ogg","Moan/C lvl2 (5).ogg","Moan/C lvl2 (6).ogg","Moan/C lvl2 (7).ogg","Moan/C lvl2 (8).ogg","Moan/C lvl2 (9).ogg","Moan/C lvl2 (10).ogg"])
        $ wsuk_ani_eyeX = 0.0
        $ wsuk_ani_eyeY = 0.1
        $ wsuk_ani_mouth = 3.6
    jump wsuk_quest_1_1_recall

# ---------------------------------------------------------------------------
label wsuk_quest_1_1_Moan3:
# ---------------------------------------------------------------------------
    if not renpy.music.is_playing(channel="SE2"):
        play SE2 renpy.random.choice(["Moan/C lvl3 (1).ogg","Moan/C lvl3 (2).ogg","Moan/C lvl4 (1).ogg","Moan/C lvl4 (2).ogg","Moan/C lvl4 (3).ogg","Moan/C lvl4 (4).ogg"])
        $ wsuk_ani_eyeX = 0.3
        $ wsuk_ani_eyeY = 0.0
        $ wsuk_ani_mouth = 4
    jump wsuk_quest_1_1_recall

# ---------------------------------------------------------------------------
label wsuk_quest_1_1_cum:
# ---------------------------------------------------------------------------
    play SE2 renpy.random.choice(["Moan/A lvl7 (1).mp3","Moan/A lvl7 (2).mp3","Moan/A lvl7 (3).mp3"])
    $ msg.msg(renpy.translate_string("{nm}[fnamewsuk]{/nm} came, and her lust reset."))
    $ wsuk_ani_mouth = 2
    $ wsuk_lust = 0
    $ wsuk_ani_eyeX = 0.5
    $ wsuk_ani_eyeY = 1.0
    $ a_event_1 += 1
    jump wsuk_quest_1_1_recall

# ---------------------------------------------------------------------------
label wsuk_quest_1_1_recall:
# ---------------------------------------------------------------------------
    $ config.allow_skipping = False
    $ config.rollback_enabled = False

    show screen xxx_locker_1leg_wsuk_ani
    scene xxx_locker_1leg_bg 1
    show xxx_locker_1leg_wsuk breathe_hero
    show xxx_locker_1leg_fx:
        blend "add"
    call screen xxx_locker_1leg_wsuk_ui

    $ renpy.pause(hard=True)
    jump wsuk_quest_1_1_end

# ---------------------------------------------------------------------------
label wsuk_quest_1_1_warn:
# ---------------------------------------------------------------------------
    play SE2 renpy.random.choice(["Moan/C lvl4 (1).ogg","Moan/C lvl4 (2).ogg","Moan/C lvl4 (3).ogg","Moan/C lvl4 (4).ogg"])
    $ a_event_4 = 0
    $ a_event_5 = wsuk_pain * 1.5
    show screen xxx_locker_1leg_wsuk_warning
    jump wsuk_quest_1_1_recall

# ---------------------------------------------------------------------------
label wsuk_quest_1_1_end:
# ---------------------------------------------------------------------------

    play SE1 "JingleRight.ogg"

    hide screen xxx_locker_1leg_wsuk_ani
    hide screen xxx_locker_1leg_wsuk_ui

    $ a_event_4 = 3 * (1 + (a_event_1 * a_event_1 * 0.5))
    $ hero_x_wsuk += 1 # Add Sex Count with WSUK
    $ hero_fx = 1
    $ hero_xnum += 1

    if wsuk_ani_xxx_media > 0 and a_event_7 == 0:
        $ hero_xspd = (wsuk_ani_xxx_media/3)

    scene bg_1 with Dissolve(1)

    if wsuk_pain >= 100:
        $ msg.msg(renpy.translate_string("You was too aggressive."))
        scene xxx_wsuk_end1_bg
        show xxx_wsuk_end1_mg
        show xxx_wsuk_end1_wsuk_mouth 0
        with Dissolve(3)

        $ add_stat("wsuk", "love", -5)
        $ add_stat("hero", "cha_sex", -5)

        hide xxx_wsuk_end1_wsuk_mouth
        wsuk "{pa}Stop!{w=[wt2]} It hurts so much!!!{/pa}"

        show xxx_wsuk_end1_wsuk_mouth 0

        $ a_event_5 = -100 # Score

    elif a_event_1 >= 3:
        if (wsuk_lust >= 70 or wsuk_lust > hero_lust):
            play SE2 renpy.random.choice(["Moan/A lvl7 (1).mp3","Moan/A lvl7 (2).mp3","Moan/A lvl7 (3).mp3"])
            $ a_event_1 += 1
            $ msg.msg(renpy.translate_string("You came together."))

        else:
            $ msg.msg(renpy.translate_string("You came."))

        scene xxx_wsuk_end4_bg
        show xxx_wsuk_end4_mg
        show xxx_wsuk_end4_cum
        show xxx_wsuk_end4_wsuk_mouth 0
        with Dissolve(3)

        $ hero_lust = 0
        $ wsuk_lust = 0

        $ add_stat("wsuk", "inti", a_event_4)
        $ add_stat("wsuk", "love", a_event_4)
        $ add_stat("hero", "cha_sex", 8.0)

        $ a_event_3 = 25 * a_event_1
        $ xp_now += a_event_3
        $ msg.msg(renpy.translate_string("XP [C_Pos]+ [a_event_3][C_Off]."))

        show xxx_wsuk_end4_wsuk_mouth 1
        wsuk "{aw}❤ P{w=[wt1]}-please{w=[wt2]}, stop! ❤{w=[wt3]} I c{w=[wt1]}-can't t{w=[wt1]}-take it anymore! ❤{/aw}"

        show xxx_wsuk_end4_wsuk_mouth 0

        $ a_event_5 = min(100, 25 + a_event_3) # Score

    if a_event_1 >= 1 or wsuk_lust >= 70 or wsuk_lust > hero_lust:
        if (wsuk_lust >= 70 or wsuk_lust > hero_lust):
            play SE2 renpy.random.choice(["Moan/A lvl7 (1).mp3","Moan/A lvl7 (2).mp3","Moan/A lvl7 (3).mp3"])
            $ a_event_1 += 1
            $ msg.msg(renpy.translate_string("You came together."))

        else:
            $ msg.msg(renpy.translate_string("You came."))

        scene xxx_wsuk_end3_bg
        show xxx_wsuk_end3_mg
        show xxx_wsuk_end3_cum
        show xxx_wsuk_end3_wsuk_mouth 0
        with Dissolve(3)

        $ hero_lust = 0
        $ wsuk_lust = 0

        $ add_stat("wsuk", "inti", a_event_4)
        $ add_stat("wsuk", "love", a_event_4)
        $ add_stat("hero", "cha_sex", 8.0)

        $ a_event_3 = 25 * a_event_1
        $ xp_now += a_event_3
        $ msg.msg(renpy.translate_string("XP [C_Pos]+ [a_event_3][C_Off]."))

        hide xxx_wsuk_end3_wsuk_mouth
        if a_event_1 > 1:
            wsuk "{bt}Wooow...{w=[wt2]} That was AWESOME!{/bt}"

        else:
            wsuk "{bt}Hmmm...{/bt}{w=[wt3]} You're so good at this!"

    else:
        $ msg.msg(renpy.translate_string("Oops. You came too early."))
        scene xxx_wsuk_end2_bg
        show xxx_wsuk_end2_mg
        show xxx_wsuk_end2_cum
        show xxx_wsuk_end2_wsuk_mouth 0
        with Dissolve(3)

        if a_event_2 == 0:
            $ add_stat("wsuk", "inti", 1.5)
            $ add_stat("hero", "cha_sex", 1.5)

            hide xxx_wsuk_end2_wsuk_mouth
            wsuk "{aw}Ehhh...?{w=[wt2]} Already?{/aw}{w=[wt2]} But don't worry.{w=[wt2]} We can practice a little more if you want! ❤"
            show xxx_wsuk_end2_wsuk_mouth 0

            $ a_event_5 = 0 # Score

        else:
            $ add_stat("wsuk", "love", -1)
            $ add_stat("wsuk", "inti", 0.5)
            $ add_stat("hero", "cha_sex", -1)

            hide xxx_wsuk_end2_wsuk_mouth
            wsuk "{aw}What?{w=[wt2]} Already?{/aw}"
            show xxx_wsuk_end2_wsuk_mouth 0

            $ a_event_5 = -50 # Score

    pause

    stop BGM fadeout 3
    scene bg_0 with Dissolve(3)
    play BGM "audio/W2C - Satisfaction.mp3"

    $ renpy.block_rollback()
    $ config.allow_skipping = True
    $ config.rollback_enabled = True

    $ xp_now = round(xp_now,2)
    $ wsuk_wear = "school"
    $ hero_wear = "school"
    $ hero_map = "School - Upstairs Hallway"

    $ gametimemin += 60
    call gametime from _call_gametime_128
    call check_playermap from _call_check_playermap_46
    call hide_ui from _call_hide_ui_205
    show HERO at LC
    show WSUK at RC

    if a_event_5 < -50:
        $ wsuk_mood = "O4"
        $ hero_mood = "O1"
        wsuk "Oh, fuck!{w=[wt2]} I never thought you were such an insensitive person!{w=[wt3]}{nw}"

        show WSUK at OL_slow
        wsuk "Oh, fuck!{w=[wt2]} I never thought you were such an insensitive person!{w=[wt3]}{fast} Never again{w=[wt1]}, you fucking jerk!"

    elif a_event_5 < 0:
        $ wsuk_mood = "O1"
        $ hero_mood = "O1"
        wsuk "Damn{w=[wt2]}, you really sucks, man.{w=[wt2]} Couldn't you hold it a little more?"
        hero "I'm sorry."
        wsuk "Hunf{w=[wt2]}, whatever.{w=[wt3]}{nw}"

        show WSUK at OL_slow
        wsuk "Hunf{w=[wt2]}, whatever.{w=[wt3]}{fast} See ya."

    elif a_event_5 == 0:
        $ wsuk_mood = "O2"
        $ hero_mood = "O1"
        wsuk "Damn{w=[wt2]}, I haven't even cum."
        hero "I'm sorry."

        $ wsuk_mood = "A2"
        wsuk "It's okay.{w=[wt2]} You just need to practice a little more.{w=[wt3]} We can try again another day.{w=[wt3]}{nw}"

        show WSUK at OL_slow
        wsuk "It's okay.{w=[wt2]} You just need to practice a little more.{w=[wt3]} We can try again another day.{w=[wt3]}{fast} See ya!"

    elif a_event_5 < 50:
        $ wsuk_mood = "A1"
        $ hero_mood = "A1"
        wsuk "So, babe!{w=[wt2]} Did you have a good time?"

        $ hero_mood = "A2"
        hero "Y{w=[wt1]}-yes! I{w=[wt1]}-I loved!"

        $ wsuk_mood = "A2"
        wsuk "{gg}Tee-hee...{/gg}{w=[wt2]} I know, right?{w=[wt3]}{nw}"

        show WSUK at OL_slow
        wsuk "{gg}Tee-hee...{/gg}{w=[wt2]} I know, right?{w=[wt3]}{fast} See ya!"

    elif a_event_5 < 100:
        $ wsuk_mood = "A4"
        $ hero_mood = "A1"
        wsuk "{bt}Wooow{w=[wt2]}, that was awesome, babe!{/bt}"

        $ hero_mood = "A2"
        hero "I loved it too!"

        $ wsuk_mood = "A2"
        wsuk "{gg}Tee-hee...{/gg}{w=[wt2]} I know, right?{w=[wt3]} Hope we can fuck more times.{w=[wt3]}{nw}"

        show WSUK at OL_slow
        wsuk "{gg}Tee-hee...{/gg}{w=[wt2]} I know, right?{w=[wt3]} Hope we can fuck more times.{w=[wt3]}{fast} See ya!"

    elif a_event_5 >= 100:
        $ wsuk_mood = "A4"
        $ hero_mood = "A1"
        wsuk "{bt}Oh, fuck!{w=[wt2]} You're a MONSTER ❤!{/bt}{w=[wt3]} I hope I can walk home{w=[wt2]}, I can barelly feel my legs!"

        $ hero_mood = "A2"
        hero "{gg}He-he...{/gg}{w=[wt2]} I loved it too."

        $ wsuk_mood = "A2"
        wsuk "Hope you can flood this pussy with cum more times.{w=[wt3]}{nw}"

        show WSUK at OL_slow
        wsuk "Hope you can flood this pussy with cum more times.{w=[wt3]}{fast} Bye bye, my stud ❤!"

    jump show_ui
