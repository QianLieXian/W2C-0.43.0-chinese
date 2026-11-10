image Entrada = Movie(play="gui/MainMenu/MainMenu(INTRO).webm", image="bg_1", loop=False)
image passday = Movie(play="/images/Action/General/passday_vid.webm", start_image="passday_1", image="passday_2", loop=False)

# ----------------------------------------------------------------------------------------------------
label gameover:
# ----------------------------------------------------------------------------------------------------
    show screen GameOver
    with Dissolve(3)
    $ a_event_0 = ""
    $ _skipping = False
    $ renpy.pause(hard=True)

screen GameOver():
    add "UI/BG0.webp"
    frame:
        xsize 1920
        ysize 1080
        xpadding 150
        ypadding 150
        xalign 0.0
        vbox:
            yalign 0.5
            xalign 0.5
            spacing 25 
            vbox:
                xalign 0.5
                text renpy.translate_string("{bt=a2-s1-p10}{size=70}{color=#FFCB64}That's all for this version. Thank you for playing![C_Off]{/bt}")
            vbox:
                xalign 0.5
                text renpy.translate_string("{color=#6496FF}About game updates,[C_Off] I can say that {bt}{b}someday around{/b}{/bt} the end of each month:{p}* the current public version may be removed;{p}* the current early access version may come out publicly;{p}* the new updated version may come out as the new early access.{p}{p}Did you realize that there are students without data on the student list? That's because there are 'slots' in the classroom, but the characters haven't been created yet. So... Do you have cool ideas for characters you'd like to see in the game someday? Now there's a place for you to give suggestions for future characters on our {a=https://discord.gg/raU65TZqbE}Discord{/a}! Also, feel free to interact; give me feedbacks; report errors; tell which waifu is your favorite one; and of course, chat with other cool pervert people like us!!! UwU") size 40
            vbox:
                xalign 0.5
                textbutton _("{size=50}Return to Main Menu") action MainMenu(confirm=False)
            vbox:
                xalign 0.5
                textbutton _("{size=50}Quit the game") action Quit(confirm=False)
            vbox:
                xalign 0.5
                text renpy.translate_string("{explode=3}{color=#FF325B}{b}{size=50}Explode{/b}[C_Off]{/explode}")

# ----------------------------------------------------------------------------------------------------
label testscreen: # testscreen splashscreen
# ----------------------------------------------------------------------------------------------------
    screen testscreen():
        vbox:
            xalign 1
            yalign 0.05
            spacing 10
            #textbutton _("CHA: [stat_cha]") action SetVariable("stat_cha", 20)
            #textbutton _("Test Scene") action Function(renpy.jump,"wgal_quest_0")
            textbutton _("Wear Nothing") action [SetVariable("a_event_0", None),Function(renpy.call,"testscreen_GET")]
            textbutton _("Wear Common") action [SetVariable("a_event_0","common1"), SetVariable("wpre_style", "common"), Function(renpy.call,"testscreen_GET")]
            textbutton _("Wear School Common Uniform") action [SetVariable("a_event_0","school"), SetVariable("wpre_style", "gracious"), Function(renpy.call,"testscreen_GET")]
            textbutton _("Wear School Gym Uniform") action [SetVariable("a_event_0","school_sport"), SetVariable("wpre_style", "gracious"), Function(renpy.call,"testscreen_GET")]
            textbutton _("Wear School Swimsuit Uniform") action [SetVariable("a_event_0","school_swim"), SetVariable("wpre_style", "gracious"), Function(renpy.call,"testscreen_GET")]
            textbutton _("Change") action [If(a_event_1==1, true=(Function(renpy.call,"testscreen2"))), If(a_event_1==2, true=(Function(renpy.call,"testscreen3"))), If(a_event_1==3, true=(Function(renpy.call,"testscreen4"))), If(a_event_1==4, true=(Function(renpy.call,"testscreen5"))), If(a_event_1==5, true=(Function(renpy.call,"testscreen1")))]
            #textbutton _("{size=50}RESET BAR") action [SetVariable("wmom_pain",0), SetVariable("wmom_flex",0)]
            #textbutton _("{size=50}BACK") action Function(renpy.jump,"splashscreen")
            textbutton _("{size=50}QUIT") action Quit(confirm=False)
    $ a_event_1 = 1
    $ a_event_2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis."

    label testscreen0:
        hide screen minigametimerfast

        scene bg_1

        if a_event_1 == 0:
            show mainmenu_bg at parallax_sky
            show Live2D_MainMenu breathe
            show mainmenu_fg at parallax_leaves

        if a_event_1 == 1:
            $ X_pos = 1600
            show WRIC at X
            $ X_pos = 1250
            show WOTA at X
            $ X_pos = 900
            show WSIS at X
            $ X_pos = 550
            show WDAN at X
            $ X_pos = 200
            show WNEI at X

        elif a_event_1 == 2:

            $ X_pos = 1625
            show WLAZ at X
            $ X_pos = 1175
            show WGAL at X
            $ X_pos = 725
            show WPRE at X
            $ X_pos = 275
            show WDIS at X

        elif a_event_1 == 3:
            $ X_pos = 1600
            show WUZA at X
            $ X_pos = 950
            show WGOT at X
            $ X_pos = 300
            show WDEL at X

            #$ X_pos = 1600
            #show WMOM at X
            #$ X_pos = 1150
            #show WGMA at X
            #$ X_pos = 700
            #show WCOU at X
            #$ X_pos = 250
            #show WSIS at X

        elif a_event_1 == 4:
            $ X_pos = 1625
            show HRIV at X
            $ X_pos = 1175
            show HPRV at X
            $ X_pos = 725
            show HERO at X
            $ X_pos = 275
            show HINE at X

            #$ X_pos = 200
            #show 2DHA g_idle at X
            #$ X_pos = 500
            #show 2DHI m01 at CC
            #$ X_pos = 800
            #show 2DMA mtn_01 at X
            #$ X_pos = 1100
            #show 2DMK m01 at X
            #$ X_pos = 1400
            #show 2DNA mtn_01 at X
            #$ X_pos = 1400
            #show 2DRI idle at X

        elif a_event_1 == 5:
            show WRIN at LC
            show WSUK at RC

        show screen testscreen
        pause

        jump testscreen0

    label testscreen1:
        $ a_event_1 = 1
        jump testscreen0

    label testscreen2:
        $ a_event_1 = 2
        jump testscreen0

    label testscreen3:
        $ a_event_1 = 3
        jump testscreen0

    label testscreen4:
        $ a_event_1 = 4
        jump testscreen0

    label testscreen5:
        $ a_event_1 = 5
        jump testscreen0

    label testscreen_GET:
        $ wpre_wear = a_event_0
        $ wgal_wear = a_event_0
        $ wdis_wear = a_event_0
        $ wota_wear = a_event_0
        $ wnei_wear = a_event_0

        $ wric_wear = a_event_0
        $ wlaz_wear = a_event_0
        $ wdel_wear = a_event_0
        $ wgot_wear = a_event_0
        $ wuza_wear = a_event_0
        $ wkuu_wear = a_event_0

        $ wsis_wear = a_event_0
        $ hriv_wear = a_event_0
        $ hero_wear = a_event_0
        $ hprv_wear = a_event_0
        $ hine_wear = a_event_0

        $ wrin_wear = a_event_0
        $ wsuk_wear = a_event_0

        if a_event_0 == None:
            $ wcou_wear = None
            $ wmom_wear = None
            $ wgma_wear = None

        elif a_event_0 == "school_sport":
            $ wcou_wear = "doctor"
            $ wmom_wear = "sport1"
            $ wgma_wear = "common1"

        else:
            $ wcou_wear = "party"
            $ wmom_wear = "common1"
            $ wgma_wear = "common1"

        jump testscreen0

# ----------------------------------------------------------------------------------------------------
label splashscreen: # splashscreen testscreen
# ----------------------------------------------------------------------------------------------------
    #if 1 > 0:
     #$ raise Exception("test")


    if preferences.text_cps != 0:
        if renpy.variant("pc") or renpy.variant("web"):
            $ preferences.text_cps = 40
            $ wt1 = 0.25
            $ wt2 = 0.50
            $ wt3 = 0.75
            $ wt4 = 1.00
        else:
            $ preferences.text_cps = 30
            $ wt1 = 0.1
            $ wt2 = 0.2
            $ wt3 = 0.4
            $ wt4 = 0.8

    $ a_menu_1 = 0
    $ a_menu_2 = 0
    $ a_menu_3 = 0
    $ a_menu_4 = 0
    
    $ hero_wear = "home"
    $ preferences.gr = False # gore is removed from the game
    $ preferences.ui_menu = False # Start Main Menu with hidden UI

    if persistent.resetdata == 2024:
        $ preferences.parallax = True
        $ preferences.happy2025 = True
        $ preferences.intro = True
        $ preferences.warning = True
        $ persistent.resetdata = "2025_JAN"

    $ preferences.codecheat = "m1sfK"
        #W2Cgodmode to cheat, #KCC2W2C to add wallpaper
        # test = godmodeON
        # 0.14 = Yv202
        # 0.15 = Ui751
        # 0.16 = v4xAd
        # 0.17 = rum3Z
        # 0.18 = zU3R4
        # 0.19 = J4seL
        # 0.20 = fL4Gi
        # 0.21 = H2k25
        # 0.22 = 1F4ji
        # 0.23 = Ve4Do
        # 0.24 = 0Giar
        # 0.25 = Zu8iU
        # 0.26 = 1Finb
        # 0.27 = xeLU0
        # 0.28 = MUbA2
        # 0.29 = Br3Me
        # 0.30 = CunN1
        # 0.31 = Cauv0
        # 0.32 = kr1zA
        # 0.33 = hoCU5
        # 0.34 = G3vuX
        # 0.35 = ken1M
        # 0.36 = Taj0T
        # 0.37 = CaWi7
        # 0.38 = xe81T
        # 0.39 = ZU93p
        # 0.40 = gEn67
        # 0.41 = VG3Gq
        # 0.42 = ALeT1
        # 0.43 = m1sfK

    if preferences.codecheatuse != preferences.codecheat:
        $ preferences.cheatmode = False

    if renpy.variant("mobile") and not (renpy.variant("pc") or renpy.variant("web")):
        $ persistent.os = 1 # Android
        #if persistent.welcum == False:
            #$ preferences.parallax = False
    else:
        $ persistent.os = 0 # PC

    if is_test == False:
        $ persistent.welcum = True
        $ quick_menu = False
        scene splashscreen
        show screen splashscreen
        $ _skipping = False
        $ renpy.pause(hard=True)
        screen splashscreen():

            image "images/UI/UIBG/splashscreen.webp"
            image "gui/BG80.webp"
            vbox:
                yalign 0.1
                xalign 0.5
                text renpy.translate_string("{b}[C_Red]Warning[C_Off]{/b}") size 100 xalign 0.5
                text renpy.translate_string("All characters in this game are of legal age,") size 60 xalign 0.5
                text renpy.translate_string("and you must be as well to play this game.") size 60 xalign 0.5
                text renpy.translate_string("{b}[C_Red]Do you confirm you are of legal age?[C_Off]{/b}") size 60 xalign 0.5

            hbox:
                yalign 0.85
                xalign 0.5
                spacing 50

                frame:
                    background None
                    xsize 460
                    ysize 460
                    imagebutton:
                        idle "images/UI/splashscreen_n_IDLE.webp"
                        hover "images/UI/splashscreen_n_HOVER.webp"
                        action Quit()
                    vbox:
                        yalign 0.5
                        xalign 0.5
                        spacing -15
                        text renpy.translate_string("[C_Gre]{b}NO{/b}[C_Off]") size 140 xalign 0.5
                        text renpy.translate_string("[C_Gre]I am[C_Off]") size 60 xalign 0.5
                        text renpy.translate_string("[C_Gre]underage[C_Off]") size 60 xalign 0.5

                frame:
                    background None
                    xsize 460
                    ysize 460
                    imagebutton:
                        idle "images/UI/splashscreen_y_IDLE.webp"
                        hover "images/UI/splashscreen_y_HOVER.webp"
                        action Function(renpy.jump, "splashscreen2")
                        #action MainMenu(confirm=False)
                    vbox:
                        yalign 0.5
                        xalign 0.5
                        spacing -15
                        text renpy.translate_string("[C_Red]{b}YES{/b}[C_Off]") size 140 xalign 0.5
                        text renpy.translate_string("[C_Red]I am of[C_Off]") size 60 xalign 0.5
                        text renpy.translate_string("[C_Red]legal age[C_Off]") size 60 xalign 0.5
    else:
        return

# ----------------------------------------------------------------------------------------------------
label splashscreen2:
# ----------------------------------------------------------------------------------------------------
    if preferences.warning:
        play SE1 "JingleRight.ogg"
        hide screen splashscreen with Dissolve(1)
        pause(0.5)
        scene splashscreen2 with dissolve
        pause
        scene bg_0 with dissolve

    if preferences.intro:
        show screen OpeningEnd
        jump splashscreen3
    else:
        return

# ----------------------------------------------------------------------------------------------------
label splashscreen3:
# ----------------------------------------------------------------------------------------------------
    hide screen splashscreen
    hide screen splashscreen2
    $ a_event_0 = 0

    play SE1 "Dreamy SFX.mp3"

    scene bg_1
    with Dissolve(1)

    #scene bg_1
    #scene image "gui/MainMenu/MainMenu(INTRO).webp"
    #define MainMenuINTRO = Movie(play="gui/MainMenu/MainMenu(INTRO).webm")
    
    call hide_ui from _call_hide_ui_102
    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night

    show Entrada with Dissolve(1)

    play BGM "audio/W2C - Welcum To The City!.mp3"
    #play BGM "<from 160>audio/W2C - Welcum To The City!.mp3"
    queue BGM "audio/W2C - MainTheme (EPIC).mp3"

    while a_event_0 < 10:
        if renpy.music.get_pos(channel="BGM") != None:
            $ a_event_0 = 10
            show screen OpeningLyrics
            show screen OpeningMusicTimer1
            with dissolve
            pause
        else:
            $ a_event_0 += 1
            pause(0.25)

    play BGE "Crowd_Female.mp3" fadein 3
    hide screen pseudo_main_menu
    hide screen OpeningLyrics
    return

# ----------------------------------------------------------------------------------------------------
label splashscreen4:
# ----------------------------------------------------------------------------------------------------
    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night
    hide screen splashscreen
    hide screen splashscreen2
    hide screen OpeningLyrics
    hide screen OpeningMusicTimer1
    show screen OpeningMusicTimer2
    show screen pseudo_main_menu
    show screen OpeningLyrics
    with Dissolve(4)
    pause

    label splashscreen4_end:
        pass

    $ _skipping = True
    $ quick_menu = True
    play BGE "Crowd_Female.mp3" fadein 3
    hide screen pseudo_main_menu
    hide screen OpeningMusicTimer1
    hide screen OpeningMusicTimer2
    hide screen OpeningLyrics
    hide screen OpeningEnd
    return

# ----------------------------------------------------------------------------------------------------
# TEST
# ----------------------------------------------------------------------------------------------------
screen gametimesec_run():
    timer 0.01 repeat True action [SetVariable("gametimemin", gametimemin+1), Function(renpy.call, "gametime")]
    key "mousedown_1" action Hide("gametimesec_run")

# ----------------------------------------------------------------------------------------------------
screen OpeningEnd():
# ----------------------------------------------------------------------------------------------------
    modal False
    key "mousedown_1" action Jump("splashscreen4_end")
    key "mouseup_1" action Jump("splashscreen4_end")

# ----------------------------------------------------------------------------------------------------
screen OpeningMusicTimer1():
# ----------------------------------------------------------------------------------------------------
    timer 0.5 repeat True action If(
        renpy.music.get_pos(channel="BGM") is not None and renpy.music.get_pos(channel="BGM") >= 17, 
        true=Jump("splashscreen4")
    )
    #timer 0.5 repeat True action Jump("splashscreen4")

# ----------------------------------------------------------------------------------------------------
screen OpeningMusicTimer2():
# ----------------------------------------------------------------------------------------------------
    timer 1 repeat True action If(
        renpy.music.get_pos(channel="BGM") is not None and renpy.music.get_pos(channel="BGM") >= 178, 
        true=Jump("splashscreen4_end")
    )

# ----------------------------------------------------------------------------------------------------
screen OpeningLyrics():
# ----------------------------------------------------------------------------------------------------
    timer 0.1 repeat True action Show("OpeningLyrics")
    $ music_pos = renpy.music.get_pos(channel="BGM")  # Get position ONCE
    if music_pos is not None:  # Changed from "not == None"
        if not ((music_pos >= 6.5 and music_pos < 21) or (music_pos >= 124 and music_pos < 136)):
            frame:
                background "gui/nvl75.webp"
                xmaximum 1000
                ymaximum 5
                yalign 0.85
                xalign 0.0
        vbox:
            ypos 960
            xalign 0.5
            # --------------------------------------------------
            # INTRO
            # --------------------------------------------------
            if renpy.music.get_pos(channel="BGM") >= 0.5 and renpy.music.get_pos(channel="BGM") < 1.5:
                text renpy.translate_string("I'm glad you're back here!"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True

            elif renpy.music.get_pos(channel="BGM") >= 1.5 and renpy.music.get_pos(channel="BGM") < 3.5:
                text renpy.translate_string("{mind}{s}Cum{/s}{/mind} Come*, come, and come to me."):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True

            elif renpy.music.get_pos(channel="BGM") >= 3.5 and renpy.music.get_pos(channel="BGM") < 5.3:
                text renpy.translate_string("So come on, hold my hands and let's..."):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True

            elif renpy.music.get_pos(channel="BGM") >= 5.3 and renpy.music.get_pos(channel="BGM") < 6.5:
                text renpy.translate_string("{b}...HAVE FUN!{/b}"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True


            # --------------------------------------------------
            # VERSE
            # --------------------------------------------------
            elif renpy.music.get_pos(channel="BGM") >= 22 and renpy.music.get_pos(channel="BGM") < 24:
                text renpy.translate_string("Hey friend, you've grown up a lot"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 24 and renpy.music.get_pos(channel="BGM") < 27.5:
                text renpy.translate_string("My front door looks too narrow now"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 27.5 and renpy.music.get_pos(channel="BGM") < 30:
                text renpy.translate_string("If you visit me, please enter gently"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 30 and renpy.music.get_pos(channel="BGM") < 34:
                text renpy.translate_string("Because I certainly want you inside! {mind}(want you inside!){/mind}"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 34 and renpy.music.get_pos(channel="BGM") < 36.5:
                text renpy.translate_string("I really missed you so much"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 36.5 and renpy.music.get_pos(channel="BGM") < 39:
                text renpy.translate_string("We have to make up for lost time"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 39 and renpy.music.get_pos(channel="BGM") < 42.5:
                text renpy.translate_string("I want you to fill me with your love"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 42.5 and renpy.music.get_pos(channel="BGM") < 46:
                text renpy.translate_string("Even if it's warm and sticky! {mind}(warm and stick!){/mind}"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True

            # --------------------------------------------------
            # PRE-CHORUS
            # --------------------------------------------------
            if renpy.music.get_pos(channel="BGM") >= 46 and renpy.music.get_pos(channel="BGM") < 47:
                text renpy.translate_string("I'm glad you're back here!"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 47 and renpy.music.get_pos(channel="BGM") < 49:
                text renpy.translate_string("{mind}{s}Cum{/s}{/mind} Come*, come, and come to me."):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 49 and renpy.music.get_pos(channel="BGM") < 51:
                text renpy.translate_string("So come on, hold my hands and let's..."):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 51 and renpy.music.get_pos(channel="BGM") < 52:
                text renpy.translate_string("{b}...HAVE FUN!{/b}"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True

            # --------------------------------------------------
            # CHORUS
            # --------------------------------------------------
            elif renpy.music.get_pos(channel="BGM") >= 52 and renpy.music.get_pos(channel="BGM") < 53.5:
                text renpy.translate_string("Hugging, kissing, talking!"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
            elif renpy.music.get_pos(channel="BGM") >= 53.5 and renpy.music.get_pos(channel="BGM") < 55.5:
                text renpy.translate_string("Games, beach, shopping!"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
            elif renpy.music.get_pos(channel="BGM") >= 55.5 and renpy.music.get_pos(channel="BGM") < 58.5:
                text renpy.translate_string("Our school year, lots to do here"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
            elif renpy.music.get_pos(channel="BGM") >= 58.5 and renpy.music.get_pos(channel="BGM") < 61:
                text renpy.translate_string("Leave the shame aside, I will be your guide"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
            elif renpy.music.get_pos(channel="BGM") >= 61 and renpy.music.get_pos(channel="BGM") < 65:
                text renpy.translate_string("Here our life is pretty"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
            elif renpy.music.get_pos(channel="BGM") >= 65 and renpy.music.get_pos(channel="BGM") < 67:
                text renpy.translate_string("WELCUM TO THE CITY"):
                    color "#FFFFC8" outlines [(2, "#C8C814", 0, 0)] size 100 bold True yoffset -20

            # --------------------------------------------------
            # VERSE
            # --------------------------------------------------
            elif renpy.music.get_pos(channel="BGM") >= 78.5 and renpy.music.get_pos(channel="BGM") < 81:
                text renpy.translate_string("I know you missed me too"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 81 and renpy.music.get_pos(channel="BGM") < 84:
                text renpy.translate_string("I noticed that you hug me more now"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 84 and renpy.music.get_pos(channel="BGM") < 86:
                text renpy.translate_string("But be careful because I'm sensitive"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 86 and renpy.music.get_pos(channel="BGM") < 90.5:
                text renpy.translate_string("So please stop poking me! {mind}(poking me!){/mind}"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True

            elif renpy.music.get_pos(channel="BGM") >= 90 and renpy.music.get_pos(channel="BGM") < 93:
                text renpy.translate_string("I love running with you so much"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 93 and renpy.music.get_pos(channel="BGM") < 95.5:
                text renpy.translate_string("That sometimes we get so sweaty"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 95.5 and renpy.music.get_pos(channel="BGM") < 98:
                text renpy.translate_string("So I can say I have more fun"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 98 and renpy.music.get_pos(channel="BGM") < 102:
                text renpy.translate_string("When you make me all wet!  {mind}(when make me all wet!){/mind}"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True

            # --------------------------------------------------
            # PRE-CHORUS
            # --------------------------------------------------
            if renpy.music.get_pos(channel="BGM") >= 102 and renpy.music.get_pos(channel="BGM") < 103.5:
                text renpy.translate_string("I'm glad you're back here!"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 103.5 and renpy.music.get_pos(channel="BGM") < 105:
                text renpy.translate_string("{mind}{s}Cum{/s}{/mind} Come*, come, and come to me."):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 105 and renpy.music.get_pos(channel="BGM") < 107.5:
                text renpy.translate_string("So come on, hold my hands and let's..."):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 107.5 and renpy.music.get_pos(channel="BGM") < 108.5:
                text renpy.translate_string("{b}...HAVE FUN!{/b}"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True

            # --------------------------------------------------
            # CHORUS
            # --------------------------------------------------
            elif renpy.music.get_pos(channel="BGM") >= 108.5 and renpy.music.get_pos(channel="BGM") < 109.5:
                text renpy.translate_string("{b}Hugging, kissing, talking!"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
            elif renpy.music.get_pos(channel="BGM") >= 109.5 and renpy.music.get_pos(channel="BGM") < 111.5:
                text renpy.translate_string("Games, beach, shopping!"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
            elif renpy.music.get_pos(channel="BGM") >= 111.5 and renpy.music.get_pos(channel="BGM") < 114.5:
                text renpy.translate_string("{b}Our school year, lots to do here{/b}"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
            elif renpy.music.get_pos(channel="BGM") >= 114.5 and renpy.music.get_pos(channel="BGM") < 117.5:
                text renpy.translate_string("{b}Leave the shame aside, I will be your guide{/b}"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
            elif renpy.music.get_pos(channel="BGM") >= 117.5 and renpy.music.get_pos(channel="BGM") < 121:
                text renpy.translate_string("{b}Here our life is pretty{/b}"):
                    color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
            elif renpy.music.get_pos(channel="BGM") >= 121 and renpy.music.get_pos(channel="BGM") < 124:
                text renpy.translate_string("{b}WELCUM TO THE CITY{/b}"):
                    color "#FFFFC8" outlines [(2, "#C8C814", 0, 0)] size 100 bold True yoffset -20

            # --------------------------------------------------
            # BRIDGE
            # --------------------------------------------------
            elif renpy.music.get_pos(channel="BGM") >= 133 and renpy.music.get_pos(channel="BGM") < 136:
                text renpy.translate_string("{mind}(Here our life is pretty...){/mind}"):
                    color "#FFFFC8" outlines [(2, "#C8C814", 0, 0)] size 100 bold True yoffset -20

            elif renpy.music.get_pos(channel="BGM") >= 137 and renpy.music.get_pos(channel="BGM") < 138.5:
                vbox:
                    yoffset -45
                    text renpy.translate_string("{b}Hugging, kissing, talking!{/b}"):
                        color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
                    text renpy.translate_string("{mind}(Yeeeah...){/mind}"):
                        xalign 0.5 color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 138.5 and renpy.music.get_pos(channel="BGM") < 140.5:
                vbox:
                    yoffset -45
                    text renpy.translate_string("{b}Games, beach, shopping!{/b}"):
                        color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
                    text renpy.translate_string("{mind}(Yeeeah...){/mind}"):
                        xalign 0.5 color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 140.5 and renpy.music.get_pos(channel="BGM") < 143.5:
                vbox:
                    yoffset -45
                    text renpy.translate_string("{b}Our school year, lots to do here{/b}"):
                        color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
                    text renpy.translate_string("{mind}(Yeeeah...){/mind}"):
                        xalign 0.5 color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 143.5 and renpy.music.get_pos(channel="BGM") < 146.5:
                text renpy.translate_string("{b}Leave the shame aside, I will be your guide{/b}"):
                    color "#FFFFC8" outlines [(2, "#C8C814", 0, 0)] size 100 bold True yoffset -20
            elif renpy.music.get_pos(channel="BGM") >= 146.5 and renpy.music.get_pos(channel="BGM") < 149.5:
                text renpy.translate_string("{b}Here our life is pretty{/b}"):
                    color "#FFFFC8" outlines [(2, "#C8C814", 0, 0)] size 100 bold True yoffset -20

            # --------------------------------------------------
            # OUTRO
            # --------------------------------------------------
            elif renpy.music.get_pos(channel="BGM") >= 149.5 and renpy.music.get_pos(channel="BGM") < 151:
                vbox:
                    yoffset -45
                    text renpy.translate_string("{b}Hugging, kissing, talking!{/b}"):
                        color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
                    text renpy.translate_string("{mind}(Yeeeah...){/mind}"):
                        xalign 0.5 color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 151 and renpy.music.get_pos(channel="BGM") < 152.5:
                vbox:
                    yoffset -45
                    text renpy.translate_string("{b}Games, beach, shopping!{/b}"):
                        color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
                    text renpy.translate_string("{mind}(Yeeeah...){/mind}"):
                        xalign 0.5 color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 152.5 and renpy.music.get_pos(channel="BGM") < 155.5:
                vbox:
                    yoffset -45
                    text renpy.translate_string("{b}Our school year, lots to do here{/b}"):
                        color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True yoffset -10
                    text renpy.translate_string("{mind}(Yeeeah...){/mind}"):
                        xalign 0.5 color "#FFE1FF" outlines [(2, "#FF19FF", 0, 0)] size 60 bold True
            elif renpy.music.get_pos(channel="BGM") >= 155.5 and renpy.music.get_pos(channel="BGM") < 158.5:
                text renpy.translate_string("{b}Leave the shame aside, I will be your guide{/b}"):
                    color "#FFFFC8" outlines [(2, "#C8C814", 0, 0)] size 100 bold True yoffset -20
            elif renpy.music.get_pos(channel="BGM") >= 158.5 and renpy.music.get_pos(channel="BGM") < 162:
                text renpy.translate_string("{b}Here our life is pretty{/b}"):
                    color "#FFFFC8" outlines [(2, "#C8C814", 0, 0)] size 100 bold True yoffset -20
            elif renpy.music.get_pos(channel="BGM") >= 162 and renpy.music.get_pos(channel="BGM") < 165:
                text renpy.translate_string("{b}WELCUM TO THE CITY{/b}"):
                    color "#FFFFC8" outlines [(2, "#C8C814", 0, 0)] size 100 bold True yoffset -20

            elif renpy.music.get_pos(channel="BGM") >= 174 and renpy.music.get_pos(channel="BGM") < 177:
                text renpy.translate_string("{b}WELCUM TO THE CITY{/b}"):
                    color "#FFFFC8" outlines [(2, "#C8C814", 0, 0)] size 100 bold True yoffset -20

            else:
                text ""  size 50

# ----------------------------------------------------------------------------------------------------
screen GetXP():
# ----------------------------------------------------------------------------------------------------
    vbox:
        hbox:
            spacing 25
            label renpy.translate_string("Level: [lvl]")
            label renpy.translate_string("Experience: ")+str(round(xp_now,2))+"/"+str(round(xp_max,2))
            label renpy.translate_string("Perks: [perk]")
        bar value AnimatedValue(min(xp_max, a_event_1), xp_max, delay=0.5) xalign 0.5 yalign 0.5

# ----------------------------------------------------------------------------------------------------
label goto_sleep:
# ----------------------------------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_103

    # Fast-travel: walk HERO to the bedroom (with a transition) via its goto_ label before sleeping.
    if not Check_CharInMap("hero", "home", "bedroom_hero"):
        call goto_home_bedroom_hero from _call_goto_home_bedroom_hero
        scene bg_home bedroom hero
        with dissolve
        pause(0.3)

    else:
        call passday from _call_passday

    jump show_ui

# ----------------------------------------------------------------------------------------------------
label passday:
# ----------------------------------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_104

    stop BGM fadeout 3

    scene passday_1
    with Fade(2, 0, 1)

    $ Set_CharMap("hero", "home", "bedroom_hero")

    # --------------------------------------------------
    # Check Sleeping Scenes
    if "Watch_Horror_end" in wsis_know:
        $ wsis_know.remove("Watch_Horror_end")
        
    elif "Watch_Horror" in wsis_know:
        call wsis_sleep_together_1 from _call_wsis_sleep_together_1

    pause(1)

    play BGM "audio/W2C - Subtitle.mp3"

    if (hero_quest_3 < 1 and hero_quest_2 == 4) and (hprv_quest_1+hine_quest_1+wpre_quest_1+wdis_quest_1+wota_quest_1+wgal_quest_1+wric_quest_1+wgot_quest_1+wdel_quest_1+wuza_quest_1+wlaz_quest_1 >= 3) and any(getattr(store, char_id + "_inti", 0) >= 10 for char_id in ["hprv", "hine", "wpre", "wdis", "wota", "wgal", "wric", "wgot", "wdel", "wuza", "wlaz"]) and (gametimeweek != "Friday" and gametimeweek != "Saturday"):
        $ hero_quest_3 = 1
    
    # --------------------------------------------------
    #$ ResetActivityList()
    call gametime_wait from _call_gametime_wait_15
    #$ ResetActivityList()
    # Reset activities

    # GET XP
    # --------------------------------------------------
    if xp_now > xp_get:
        play SE1 "Dreamy SFX.mp3"
    $ a_event_0 = lvl
    $ a_event_1 = xp_now
    show screen GetXP with dissolve
    $ xp_now += max(0, round(((
            ((stat_cha + stat_int + stat_phy)) + 
            ((wmom_inti + wsis_inti + wcou_inti + wnei_inti + wpre_inti + wgal_inti + wdis_inti + wota_inti)*10) + 
            ((wmom_love + wsis_love + wcou_love + wnei_love + wpre_love + wgal_love + wdis_love + wota_love)/1) + 
            ((wmom_lust + wsis_lust + wcou_lust + wnei_lust + wpre_lust + wgal_lust + wdis_lust + wota_lust)/5)
            ) - xp_get), 2) )

    label GetXP:
        if a_event_0 < lvl:
            $ a_event_1 = 0

        show screen GetXP
        show screen GetXP
        $ a_event_1 = xp_now

        if xp_now >= xp_max:
            play SE1 "JingleRight.ogg"
            pause(0.5)
            $ lvl += 1
            $ perk += 1
            $ xp_now -= xp_max
            $ xp_max = (10 + (10 * lvl))
            jump GetXP

        else:
            pause(0.5)

        pause(0.5)
        hide screen GetXP with Dissolve(2)

        $ xp_get = (
            ((stat_cha + stat_int + stat_phy)) + 
            ((wmom_inti + wsis_inti + wcou_inti + wnei_inti + wpre_inti + wgal_inti + wdis_inti + wota_inti)*10) + 
            ((wmom_love + wsis_love + wcou_love + wnei_love + wpre_love + wgal_love + wdis_love + wota_love)/1) + 
            ((wmom_lust + wsis_lust + wcou_lust + wnei_lust + wpre_lust + wgal_lust + wdis_lust + wota_lust)/5)
            )
        $ xp_now = round(xp_now, 2)

    # --------------------------------------------------
    # RESETING DAILY QUEST
    # --------------------------------------------------
    if wtpe_quest == 1:
        $ wtpe_quest = 2

    # "Step-Bro, Help!" laundry stuck scene is replayable once per new day
    $ wsis_stuck_done = False

    # A bad changing-room verdict bars HERO from the female locker — until the next morning.
    $ hero_locker_f_ban = False

    # Shower-repair quest resets each day: clear progress, the broken stall, opened doors, and locker access.
    if club_stco_quest_1 == 3:
        $ club_stco_quest_1 = 0
        $ locker_shower_stall = 0
        $ locker_opened_girls = []
        $ hero_locker_f_access = False

    # --------------------------------------------------
    # RESETING LUST & PAIN
    # --------------------------------------------------
    # KEEP
    $ wgma_lust = 0
    $ wmom_flex = max(0,(wmom_flex-1))
    $ wnei_lust = max(0,(wnei_lust*0.8)-10)
    $ wpre_lust = max(0,(wpre_lust*0.8)-10)

    $ wmom_pain = 0 #max(0,(wmom_pain*0.8)-5)
    $ wsuk_pain = 0 #max(0,(wsuk_pain*0.8)-5)

    # RESET
    if wmom_lust >= 90:
        $ wmom_lust = 0
    else:
        $ wmom_lust = max(0,(wmom_lust*0.8)-10)

    if wsis_lust >= 90:
        $ wsis_lust = 0
    else:
        $ wsis_lust = max(0,(wsis_lust*0.8)-10)

    if wcou_lust >= 80:
        $ wcou_lust = 0
    else:
        $ wcou_lust = max(0,(wcou_lust*0.8)-10)

    if wgal_lust >= 80:
        $ wgal_lust = 0
    else:
        $ wgal_lust = max(0,(wgal_lust*0.8)-10)

    if wota_lust >= 50:
        $ wota_lust = 0
    else:
        $ wota_lust = max(0,(wota_lust*0.8)-10)

    if wdis_lust >= 70:
        $ wdis_lust = 0
    else:
        $ wdis_lust = max(0,(wdis_lust*0.8)-10)

    if wsuk_lust >= 50:
        $ wsuk_lust = 0
    else:
        $ wsuk_lust = max(0,(wsuk_lust*0.8)-10)

    $ msg.msg(renpy.translate_string("Girls lust has decreased"))

    # --------------------------------------------------
    # RESETING BONUS/ONUS
    # --------------------------------------------------
    if stat_cha_bonus > 0:
        $ stat_cha_bonus = max(0, stat_cha_bonus-0.2)
    elif stat_cha_bonus < 0:
        $ stat_cha_bonus = min(0, stat_cha_bonus+0.2)

    if stat_int_bonus > 0:
        $ stat_int_bonus = max(0, stat_int_bonus-0.2)
    elif stat_int_bonus < 0:
        $ stat_int_bonus = min(0, stat_int_bonus+0.2)

    if stat_phy_bonus > 0:
        $ stat_phy_bonus = max(0, stat_phy_bonus-0.2)
    elif stat_phy_bonus < 0:
        $ stat_phy_bonus = min(0, stat_phy_bonus+0.2)

    if wsis_bonus > 0:
        $ wsis_bonus = max(0, wsis_bonus-0.2)
    elif wsis_bonus < 0:
        $ wsis_bonus = min(0, wsis_bonus+0.2)

    if wmom_bonus > 0:
        $ wmom_bonus = max(0, wmom_bonus-0.2)
    elif wmom_bonus < 0:
        $ wmom_bonus = min(0, wmom_bonus+0.2)

    if wcou_bonus > 0:
        $ wcou_bonus = max(0, wcou_bonus-0.2)
    elif wcou_bonus < 0:
        $ wcou_bonus = min(0, wcou_bonus+0.2)

    if wnei_bonus > 0:
        $ wnei_bonus = max(0, wnei_bonus-0.2)
    elif wnei_bonus < 0:
        $ wnei_bonus = min(0, wnei_bonus+0.2)

    if wpre_bonus > 0:
        $ wpre_bonus = max(0, wpre_bonus-0.2)
    elif wpre_bonus < 0:
        $ wpre_bonus = min(0, wpre_bonus+0.2)

    if wgal_bonus > 0:
        $ wgal_bonus = max(0, wgal_bonus-0.2)
    elif wgal_bonus < 0:
        $ wgal_bonus = min(0, wgal_bonus+0.2)

    if wota_bonus > 0:
        $ wota_bonus = max(0, wota_bonus-0.2)
    elif wota_bonus < 0:
        $ wota_bonus = min(0, wota_bonus+0.2)

    if wdis_bonus > 0:
        $ wdis_bonus = max(0, wdis_bonus-0.2)
    elif wdis_bonus < 0:
        $ wdis_bonus = min(0, wdis_bonus+0.2)

    if hriv_bonus > 0:
        $ hriv_bonus = max(0, hriv_bonus-0.2)
    elif hriv_bonus < 0:
        $ hriv_bonus = min(0, hriv_bonus+0.2)

    if hprv_bonus > 0:
        $ hprv_bonus = max(0, hprv_bonus-0.2)
    elif hprv_bonus < 0:
        $ hprv_bonus = min(0, hprv_bonus+0.2)

    if hine_bonus > 0:
        $ hine_bonus = max(0, hine_bonus-0.2)
    elif hine_bonus < 0:
        $ hine_bonus = min(0, hine_bonus+0.2)

    if wsuk_bonus > 0:
        $ wsuk_bonus = max(0, wsuk_bonus-0.2)
    elif wsuk_bonus < 0:
        $ wsuk_bonus = min(0, wsuk_bonus+0.2)

    $ msg.msg(renpy.translate_string("Bonus/Onus stats has decreased"))

    # --------------------------------------------------
    # CHECK CHARACTERS STATE
    # --------------------------------------------------
    if "DayOff" in group_tutor:
        $ group_tutor.remove("DayOff")

    if "WSIS_is_sick" in wsis_know:
        $ msg.msg(renpy.translate_string("{nm}[fnamewsis]{/nm} is now rested"))

    # --------------------------------------------------
    # Check Waking Up Scenes I (To fix and move to bottom)
    # --------------------------------------------------
    if "Watch_Horror" in wsis_know:
        call wsis_sleep_together_2 from _call_wsis_sleep_together_2

    # --------------------------------------------------
    # UPDATE DATA
    # --------------------------------------------------
    $ a_event_1 = 0
    $ a_event_2 = 0

    python:
        # Full Reset Daily Interaction
        # --------------------
        # WCOU
        for buceta in wcou_know[:]:
            if buceta == "Hug":
                wcou_know.remove(buceta)
            elif buceta == "Talk":
                wcou_know.remove(buceta)
            elif buceta == "Spermogram":
                wcou_know.remove(buceta)
            elif buceta.startswith("About_INTI"):
                wcou_know.remove(buceta)

        # WNEI
        for buceta in wnei_know[:]:
            if buceta == "Hug":
                wnei_know.remove(buceta)
            elif buceta == "Hug_Enough":
                wnei_know.remove(buceta)
            elif buceta == "Hug_Hour":
                wnei_know.remove(buceta)
            elif buceta == "Talk":
                wnei_know.remove(buceta)
            elif buceta == "PatHead":
                wnei_know.remove(buceta)
            elif buceta == "PatHead_Hour":
                wnei_know.remove(buceta)
            elif buceta == "HangOut_WatchTV":
                wnei_know.remove(buceta)
            elif buceta == "Needs_Pee_N":
                wnei_know.remove(buceta)
            elif buceta == "Needs_Pee_Y":
                wnei_know.remove(buceta)

        # WSIS
        for buceta in wsis_know[:]:
            if buceta == "Hug":
                wsis_know.remove(buceta)
            elif buceta == "Hug_Enough":
                wsis_know.remove(buceta)
            elif buceta == "Hug_Regen":
                wsis_know.remove(buceta)
            elif buceta == "Talk":
                wsis_know.remove(buceta)
            elif buceta == "Talk_How":
                wsis_know.remove(buceta)
            elif buceta == "Talk_How_Regen":
                wsis_know.remove(buceta)
            elif buceta == "PatHead":
                wsis_know.remove(buceta)
            elif buceta == "HangOut_WatchTV":
                wsis_know.remove(buceta)
            elif buceta == "HangOut_Groceries":
                wsis_know.remove(buceta)
            elif buceta == "Watch_Horror":
                wsis_know.remove(buceta)
            elif buceta == "Date_Shopping":
                wsis_know.remove(buceta)

        # WMOM
        for buceta in wmom_know[:]:
            if buceta == "Hug":
                wmom_know.remove(buceta)
            elif buceta == "Talk":
                wmom_know.remove(buceta)
            elif buceta == "Talk_How":
                wmom_know.remove(buceta)
            elif buceta == "Talk_How_Regen":
                wmom_know.remove(buceta)
            elif buceta == "HERO_2_Fridge":
                wmom_know.remove(buceta)
            elif buceta == "HangOut_WatchTV":
                wmom_know.remove(buceta)
            elif buceta == "is_shopping":
                wmom_know.remove(buceta)
            elif buceta == "is_cooking":
                wmom_know.remove(buceta)

        # WDEL
        for buceta in wdel_know[:]:
            if buceta == "Hug":
                wdel_know.remove(buceta)

        # HPRV
        for buceta in hprv_know[:]:
            if buceta == "Hug":
                hprv_know.remove(buceta)

        # Get Items
        # --------------------
        for buceta, xereca in item_data.items():
            # Grocery Store Shopping Items
            if (xereca["valu"] > 0) and item_sale.count(buceta) < 10:
                if renpy.random.random() > 0.75:
                    for xoxota in range(renpy.random.randint(1, 6)):  # Try up to 6 times
                        item_sale.append(buceta)  # Add item to sale

            # Buffs
            if buceta.startswith("Coll_Plushy"):

                # WMOM
                a_event_1 = 0
                if CountItem_Inventory(buceta, wmom_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wmom_item_love:
                            a_event_1 += 0.25
                    wmom_love += min(1, a_event_1)

                # WSIS
                a_event_1 = 0
                if CountItem_Inventory(buceta, wsis_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wsis_item_love:
                            a_event_1 += 0.25
                    wsis_love += min(1, a_event_1)
                
                # WNEI
                a_event_1 = 0
                if CountItem_Inventory(buceta, wnei_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wnei_item_love:
                            a_event_1 += 0.25
                    wnei_love += min(1, a_event_1)
                
                # WPRE
                a_event_1 = 0
                if CountItem_Inventory(buceta, wpre_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wpre_item_love:
                            a_event_1 += 0.25
                    wpre_love += min(1, a_event_1)
                
                # WOTA
                a_event_1 = 0
                if CountItem_Inventory(buceta, wota_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wota_item_love:
                            a_event_1 += 0.25
                    wota_love += min(1, a_event_1)
                
                # WDIS
                a_event_1 = 0
                if CountItem_Inventory(buceta, wdis_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wdis_item_love:
                            a_event_1 += 0.25
                    wdis_love += min(1, a_event_1)
                
                # WGAL
                a_event_1 = 0
                if CountItem_Inventory(buceta, wgal_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wgal_item_love:
                            a_event_1 += 0.25
                    wgal_love += min(1, a_event_1)
                
                # WRIC
                a_event_1 = 0
                if CountItem_Inventory(buceta, wric_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wric_item_love:
                            a_event_1 += 0.25
                    wric_love += min(1, a_event_1)
                
                # WGOT
                a_event_1 = 0
                if CountItem_Inventory(buceta, wgot_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wgot_item_love:
                            a_event_1 += 0.25
                    wgot_love += min(1, a_event_1)
                
                # WDEL
                a_event_1 = 0
                if CountItem_Inventory(buceta, wdel_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wdel_item_love:
                            a_event_1 += 0.25
                    wdel_love += min(1, a_event_1)
                
                # WUZA
                a_event_1 = 0
                if CountItem_Inventory(buceta, wuza_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wuza_item_love:
                            a_event_1 += 0.25
                    wuza_love += min(1, a_event_1)
                
                # WLAZ
                a_event_1 = 0
                if CountItem_Inventory(buceta, wlaz_item) >= 1:
                    a_event_2 += 1
                    for xoxota in xereca["tags"]:
                        if xoxota in wlaz_item_love:
                            a_event_1 += 0.25
                    wlaz_love += min(1, a_event_1)

        if a_event_2 == 1:
            msg.msg(renpy.translate_string("Someone must have remembered you last night"))
        elif a_event_2 > 1:
            msg.msg(renpy.translate_string("[a_event_2] people must have remembered you last night"))

    # --------------------------------------------------
    # Update Interaction To Day
    # WNEI
    if "PatHead_Hour" in wnei_know:
        $ wnei_know.remove("PatHead_Hour")
        $ wnei_know.append("PatHead_Day")
    if "Hug_Hour" in wnei_know:
        $ wnei_know.remove("Hug_Hour")
        $ wnei_know.append("Hug_Day")

    # WSUK
    if wsuk_love < 0:
        $ wsuk_love += 5
    if wsuk_quest_2 == 2:
        $ wsuk_quest_2 = 1

    # --------------------------------------------------
    # Reset Unique Daily Interaction
    # WNEI
    if "Hug_Enough" in wnei_know:
        $ wnei_know.remove("Hug_Enough")

    # WSIS
    if "Upset" in wsis_know:
        $ wsis_know.remove("Upset")
    if "Compliment" in wsis_know:
        $ wsis_know.remove("Compliment")

    # WMOM
    if "Greeting" in wmom_know:
        $ wmom_know.remove("Greeting")

    # --------------------------------------------------
    # 2.3: Resident-noticing (generalized) — any housemate notices HERO cleaned
    # --------------------------------------------------
    python:
        for _res in ["wmom", "wsis"]:
            _know = getattr(store, _res + "_know")
            if "HERO_Clean_Home" in _know:
                _know.remove("HERO_Clean_Home")

        if task_hero_clean_home > 0:
            for _res in ["wmom", "wsis"]:
                if Check_CharInMap(_res, "home"):
                    _know = getattr(store, _res + "_know")
                    _know.append("HERO_Clean_Home")
                    _char_name = getattr(store, "fname" + _res, _res)
                    msg.msg(C_Nam + _char_name + C_Off + renpy.translate_string(" noticed you left the house cleaner"))
                    add_stat(_res, "love", task_hero_clean_home / 20)
            task_hero_clean_home = 0

    $ Get_CleanDecay()

    # --------------------------------------------------
    # Check Waking Up Scenes II
    # --------------------------------------------------
    scene passday

    pause
    
    if "Sleepover_Together" in wsis_know:
        call wsis_sleepover_wakeup from _call_wsis_sleepover_wakeup

    scene bg_1 with Dissolve(1)

    stop BGM fadeout 3

    # --------------------------------------------------
    # RESET PLAYER STATS
    # --------------------------------------------------

    $ hero_needs = [False,False,False,False] #Bathe, Breakfast, Lunch, Dinner
    $ stat_ene = 100
    $ times_cha = 0
    $ times_int = 0
    $ times_phy = 0
    $ msg.msg(renpy.translate_string("You feel rested"))

    stop BGM fadeout 3
    if Check_CharInMap("hero", "home", "bedroom_wsis"):
        scene bg_home bedroom wsis
    else:
        scene bg_home bedroom hero
    with Dissolve(2)

    # --------------------------------------------------
    # NEW DAY
    # --------------------------------------------------
    play BGM "audio/W2C - GoodVibes.mp3"

    # WSIS was sick the day before
    if "WSIS_is_sick" in wsis_know:
        mind "(Maybe it is better to check if {nm}[hero_about_wsis]{/nm} is well before doing anything else.)"

    jump show_ui

    
# ----------------------------------------------------------------------------------------------------
label test_x1:
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_142
    menu:
        "WSIS - UI":
            call test_x1_ui from _call_test_x1_ui

        "WSIS - Animation":
            call test_x1_ai from _call_test_x1_ai

        "WMOM - Animation":
            scene bg_0
            show action_masturbate_bg wmom_bedroom wmom_1
            show fx_light
            pause
            show action_masturbate_bg wmom_bedroom wmom_2
            pause

        "WGAL - Animation":
            scene action_masturbate_bg school_locker_f wgal_1
            pause

        "WOTA - Animation":
            scene action_masturbate_bg school_locker_f wota_1
            pause

    jump show_ui

# ----------------------------------------------------------------------------------------------------
# Animation
# ----------------------------------------------------------------------------------------------------
image xxx_bedroomhero wsis_missionary_loop1:
    choice:
        Movie(play="/images/Action/XXX/xxx_bedroomhero wsis_missionary_1.webm", start_image="xxx_bedroomhero wsis_missionary_a", image="xxx_bedroomhero wsis_missionary_a", loop=False)
    choice:
        Movie(play="/images/Action/XXX/xxx_bedroomhero wsis_missionary_2.webm", start_image="xxx_bedroomhero wsis_missionary_a", image="xxx_bedroomhero wsis_missionary_a", loop=False)
    choice:
        Movie(play="/images/Action/XXX/xxx_bedroomhero wsis_missionary_3.webm", start_image="xxx_bedroomhero wsis_missionary_a", image="xxx_bedroomhero wsis_missionary_a", loop=False)
    choice:
        Movie(play="/images/Action/XXX/xxx_bedroomhero wsis_missionary_4.webm", start_image="xxx_bedroomhero wsis_missionary_a", image="xxx_bedroomhero wsis_missionary_a", loop=False)
    choice:
        Movie(play="/images/Action/XXX/xxx_bedroomhero wsis_missionary_5.webm", start_image="xxx_bedroomhero wsis_missionary_a", image="xxx_bedroomhero wsis_missionary_a", loop=False)
    3.25
    repeat

image xxx_bedroomhero wsis_missionary_end = Movie(play="/images/Action/XXX/xxx_bedroomhero wsis_missionary_6.webm", start_image="xxx_bedroomhero wsis_missionary_a", image="xxx_bedroomhero wsis_missionary_b", loop=False)

image xxx_bedroomhero wsis_missionary_loop2 = Movie(play="/images/Action/XXX/xxx_bedroomhero wsis_missionary_7.webm", start_image="xxx_bedroomhero wsis_missionary_b", image="xxx_bedroomhero wsis_missionary_b", loop=True)

image action_masturbate_bg wmom_bedroom wmom_1:
    choice:
        Movie(play="/images/Action/Masturbating/action_masturbate_bg wmom_bedroom wmom_1.webm", start_image="action_masturbate_bg wmom_bedroom wmom_c", image="action_masturbate_bg wmom_bedroom wmom_c", loop=False)
    choice:
        Movie(play="/images/Action/Masturbating/action_masturbate_bg wmom_bedroom wmom_2.webm", start_image="action_masturbate_bg wmom_bedroom wmom_c", image="action_masturbate_bg wmom_bedroom wmom_c", loop=False)
    choice:
        Movie(play="/images/Action/Masturbating/action_masturbate_bg wmom_bedroom wmom_3.webm", start_image="action_masturbate_bg wmom_bedroom wmom_c", image="action_masturbate_bg wmom_bedroom wmom_c", loop=False)
    choice:
        Movie(play="/images/Action/Masturbating/action_masturbate_bg wmom_bedroom wmom_4.webm", start_image="action_masturbate_bg wmom_bedroom wmom_c", image="action_masturbate_bg wmom_bedroom wmom_c", loop=False)
    3.25
    repeat

image action_masturbate_bg wmom_bedroom wmom_2 = Movie(play="/images/Action/Masturbating/action_masturbate_bg wmom_bedroom wmom_5.webm", start_image="action_masturbate_bg wmom_bedroom wmom_a", image="action_masturbate_bg wmom_bedroom wmom_b", loop=False)

image action_masturbate_bg school_locker_f wgal_1:
    choice:
        Movie(play="/images/Action/Masturbating/action_masturbate_bg school_locker_f wgal_1.webm", start_image="action_masturbate_bg school_locker_f wgal_a", image="action_masturbate_bg school_locker_f wgal_a", loop=False)
    choice:
        Movie(play="/images/Action/Masturbating/action_masturbate_bg school_locker_f wgal_2.webm", start_image="action_masturbate_bg school_locker_f wgal_a", image="action_masturbate_bg school_locker_f wgal_a", loop=False)
    choice:
        Movie(play="/images/Action/Masturbating/action_masturbate_bg school_locker_f wgal_3.webm", start_image="action_masturbate_bg school_locker_f wgal_a", image="action_masturbate_bg school_locker_f wgal_a", loop=False)
    choice:
        Movie(play="/images/Action/Masturbating/action_masturbate_bg school_locker_f wgal_4.webm", start_image="action_masturbate_bg school_locker_f wgal_a", image="action_masturbate_bg school_locker_f wgal_a", loop=False)
    choice:
        Movie(play="/images/Action/Masturbating/action_masturbate_bg school_locker_f wgal_5.webm", start_image="action_masturbate_bg school_locker_f wgal_a", image="action_masturbate_bg school_locker_f wgal_a", loop=False)
    3.25
    repeat

image action_masturbate_bg school_locker_f wota_1 = Movie(play="/images/Action/Masturbating/action_masturbate_bg school_locker_f wota_1.webm", start_image="action_masturbate_bg school_locker_f wota_a", image="action_masturbate_bg school_locker_f wota_a", loop=True)

# ----------------------------------------------------------------------------------------------------
label test_x1_ai:
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_143

    scene bg_0
    show xxx_bedroomhero wsis_missionary_loop1
    show fx_light

    pause

    show xxx_bedroomhero wsis_missionary_end

    pause(6)

    show xxx_bedroomhero wsis_missionary_loop2

    pause

    return

# ----------------------------------------------------------------------------------------------------
init python:
    class X1Face(object):
        """WSIS's face in test_x1_ui: moans while her lust rises, glances around, and peaks at 100.
        tick() runs 10x a second from the screen's timer; mouth/eyex/eyey are MoCha2D drivers read every frame."""
        LOW = 30                # below = low lust, below AVERAGE = average, above = high
        AVERAGE = 60
        MOUTH_HOLD = 0.25       # seconds the mouth stays open after a moan
        MOUTH_FADE = 2.0        # seconds it takes to close again
        MOAN_GAP = (0.1, 2.0)   # random pause between one moan ending and the next starting
        WANDER = (0.5, 10.0)    # random seconds between two glances
        GLANCE = (0.0, 1.0)     # range each eye morph is picked from on a glance
        PEAK_HOLD = 3.0         # seconds the peak look stays before moans/glances resume
        CUM_FADE = 1.0          # seconds cum takes to go from 1 to 0 at the peak
        EYE_GLIDE = 0.5         # seconds the eyes take to glide to a new spot (eased in and out)

        def reset(self):
            now = mocha_now()
            self.ex = self.ex0 = 1.5; self.ey = self.ey0 = 1.5; self.et = -99.0
            self.peak = 0.0; self.t0 = -99.0
            self.cum_t = None
            self.next_moan = now
            self.busy_until = now
            self.next_glance = now + renpy.random.uniform(*self.WANDER)

        def tick(self, rate):
            now = mocha_now()
            before = store.wsis_lust
            store.wsis_lust = min(100, before + 0.2 * rate)

            if store.wsis_lust >= 100:
                store.wsis_lust = 0
                self.look(1.5, 2.0, now)
                if self.cum_t is None:
                    self.cum_t = now
                self.busy_until = self.next_moan = now + self.PEAK_HOLD
                self.next_glance = now + self.PEAK_HOLD + renpy.random.uniform(*self.WANDER)
                return

            if store.wsis_lust > before and now >= self.next_moan:
                self.moan(now)

            if now >= self.next_glance and now >= self.busy_until:
                self.look(renpy.random.uniform(*self.GLANCE), renpy.random.uniform(*self.GLANCE), now)
                self.next_glance = now + renpy.random.uniform(*self.WANDER)

        def moan(self, now):
            if store.wsis_lust < self.LOW:
                self.peak, up, sfx = 0.25, 0.0, SFX_Moan_C_LVL1
            elif store.wsis_lust < self.AVERAGE:
                self.peak, up, sfx = 0.5, 0.4, SFX_Moan_C_LVL2
            else:
                self.peak, up, sfx = 1.0, 0.8, SFX_Moan_C_LVL3
            self.look(1.5, 1.0 if renpy.random.random() < up else 2.0, now)
            sfx(None, 0, 0)
            self.t0 = now
            self.busy_until = now + self.MOUTH_HOLD + self.MOUTH_FADE
            self.next_moan = self.busy_until + renpy.random.uniform(*self.MOAN_GAP)

        def look(self, x, y, now):
            # glide from wherever the eyes are right now, so a new look mid-glide never jumps
            self.ex0 = self.eyex(); self.ey0 = self.eyey()
            self.ex = x; self.ey = y; self.et = now

        def _glide(self):
            u = min(1.0, max(0.0, (mocha_now() - self.et) / self.EYE_GLIDE))
            return u * u * (3.0 - 2.0 * u)

        # MoCha2D drivers
        def mouth(self):
            t = mocha_now() - self.t0
            if t < self.MOUTH_HOLD:
                return self.peak
            return self.peak * max(0.0, 1.0 - (t - self.MOUTH_HOLD) / self.MOUTH_FADE)

        def eyex(self):
            return self.ex0 + (self.ex - self.ex0) * self._glide()

        def eyey(self):
            return self.ey0 + (self.ey - self.ey0) * self._glide()

        def ypos(self):
            # the View bar (a_menu_1, 0..100), read every frame so dragging it moves her at once
            return store.a_menu_1 / 100.0

        def cum(self):
            if self.cum_t is None:
                return 1.0
            return max(0.0, 1.0 - (mocha_now() - self.cum_t) / self.CUM_FADE)

    class X1Drive(object):
        """A driver that reads x1_face by NAME, so a loaded save or a rollback never leaves the sprite on a stale copy."""
        def __init__(self, name):
            self.name = name
        def __call__(self):
            return getattr(store.x1_face, self.name)()

define x1_face = X1Face()

# ----------------------------------------------------------------------------------------------------
screen test_x1_ui(xspeed=0):
# ----------------------------------------------------------------------------------------------------
    timer 0.1 repeat True action Function(x1_face.tick, xspeed)

    frame:
        background None xsize 1920 ysize 1080 xpadding 50 ypadding 50

        vbox:
            spacing 50

            vbox:
                spacing 25
                label renpy.translate_string("Data") text_size 60
                hbox:
                    spacing 25
                    text renpy.translate_string("{b}Lust:{/b}") size 60
                    bar value StaticValue(wsis_lust, 100) xmaximum 300
                hbox:
                    spacing 25
                    text renpy.translate_string("{b}View:{/b}") size 60
                    bar value VariableValue("a_menu_1", 100) xmaximum 300

            vbox:
                spacing 25
                label renpy.translate_string("Auto Play") text_size 60
                # Return (variation, speed): the label re-shows the sprite and calls the screen again
                textbutton renpy.translate_string("Stop") text_size 60 action Return((0, 0))
                textbutton renpy.translate_string("Slow") text_size 60 action Return((1, 1))
                textbutton renpy.translate_string("Fast") text_size 60 action Return((1, 3))

            vbox:
                spacing 25
                label renpy.translate_string("Manual Control") text_size 60
                textbutton renpy.translate_string("Dick") text_size 60 action Return((2, 0))

            textbutton renpy.translate_string("End") text_size 60 action Return("end")

# ----------------------------------------------------------------------------------------------------
label test_x1_ui(xvariation=0, xspeed=0):
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_144
    $ a_menu_1 = 50
    $ x1_face.reset()

    while True:
        if xvariation==0:
            show expression mocha("x_wsis_missionary", "idle", ypos=X1Drive("ypos"), cum=X1Drive("cum"), mouth_o=X1Drive("mouth"), eyex=X1Drive("eyex"), eyey=X1Drive("eyey")) as x_wsis_missionary
            show fx_light

        elif xvariation==1:
            show expression mocha("x_wsis_missionary", "x1", ypos=X1Drive("ypos"), cum=X1Drive("cum"), mouth_o=X1Drive("mouth"), eyex=X1Drive("eyex"), eyey=X1Drive("eyey")) as x_wsis_missionary
            show fx_light

        elif xvariation==2:
            show expression mocha("x_wsis_missionary", "idle", ypos=X1Drive("ypos"), cum=X1Drive("cum"), mouth_o=X1Drive("mouth"), eyex=X1Drive("eyex"), eyey=X1Drive("eyey"), penisx=MoChaMouse("x", smooth=0.01, lo=1.0, hi=2.0), penisy=MoChaMouse("y", invert=True, smooth=0.5, lo=1.4, hi=2.0)) as x_wsis_missionary
            show fx_light
            with dissolve

        show fx_light
        call screen test_x1_ui(xspeed)
        if _return == "end":
            jump show_ui
        if isinstance(_return, tuple):
            $ xvariation, xspeed = _return

# ----------------------------------------------------------------------------------------------------
label action_train_home:
# ----------------------------------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_105

    play BGM "audio/W2C - Bravery.mp3"

    label action_train_home_intro:

        call gamecheck from _call_gamecheck_19

        menu (screen="menu_img"):

            #"Test X":
                #jump test_x1

            "Train Physics" ("training_phy_intro_hero"):
                jump action_train_home_phy

            "Train Intellect" ("training_int_study_hero"):
                jump action_train_home_int

            "Do [C_Nam][fnamewsis][C_Off]'s homework" ("training_int_study_hero") if "Neighbors_Reunion" in wsis_know and Check_TaskCompletion("homework_wsis") < 100:
                jump action_train_home_wsis_task

            "Return":
                jump action_train_home_end

    label action_train_home_wsis_task:

        if is_specialevent:
            mind "(I need to do other things now)"
            jump action_train_home_intro

        elif stat_ene < 10:
            mind "(I'm too tired for this.)"
            jump action_train_home_intro

        elif times_int >= 2:
            mind "(I already trained intellect twice today. I should rest.)"
            jump action_train_home_intro

        menu (screen="menu_img"):

            "💬 Language Arts{p}[C_Dat]([task_homework_wsis_la]%% done)[C_Off]" ("training_int_study_hero"):

                if task_homework_wsis_la >= 100:
                    $ msg.msg(renpy.translate_string("This homework is already complete"))
                    jump action_train_home_wsis_task

                else:

                    if renpy.random.random() < 0.75:
                        call screen minigame_memory(var_pla=perk_int_mem, var_cpu=1, var_mod="classic")
                        $ add_stat("hero", "int_mem", _return)

                    else:
                        call screen minigame_logic(var_the="any", var_num=2, var_mod="continuous", var_tim=int(30 * (1 + (perk_int_log*0.5))))
                        $ add_stat("hero", "int_log", _return)

                    $ add_stat("hero", "cha_per", _return)
                    $ task_homework_wsis_la += min(100, _return*20) # Homework of Language Arts

                    # Apply homework effects (same as intellect training)
                    $ times_int += 1
                    $ add_stat("hero", "ene", -5)
                    $ gametimemin += 30
                    call gametime from _call_gametime_49

            "🌡️ Natural Sciences{p}[C_Dat]([task_homework_wsis_sc]%% done)[C_Off]" ("training_int_study_hero"):

                if task_homework_wsis_sc >= 100:
                    $ msg.msg(renpy.translate_string("This homework is already complete"))
                    jump action_train_home_wsis_task

                else:

                    if renpy.random.random() < 0.33:
                        $ a_event_0 = renpy.random.choice(["Beach_015", "Park_015", "School_015"])
                        call screen minigame_find(var_map=a_event_0, var_mod="continuous", var_cnt=10, var_tim=30, var_sca=int(5/(1+(perk_int_per*0.5))))
                        $ add_stat("hero", "int_per", _return)

                    elif renpy.random.random() < 0.66:
                        call screen minigame_memory(var_pla=perk_int_mem, var_cpu=1, var_mod="classic")
                        $ add_stat("hero", "int_mem", _return)

                    else:
                        call screen minigame_logic(var_the="any", var_num=2, var_mod="continuous", var_tim=int(30 * (1 + (perk_int_log*0.5))))
                        $ add_stat("hero", "int_log", _return)

                    $ task_homework_wsis_sc += min(100, _return*20) # Homework of Natural Sciences

                    # Apply homework effects (same as intellect training)
                    $ times_int += 1
                    $ add_stat("hero", "ene", -5)
                    $ gametimemin += 30
                    call gametime from _call_gametime_50

            "♾️ Mathematics & Logic{p}[C_Dat]([task_homework_wsis_ns]%% done)[C_Off]" ("training_int_study_hero"):

                if task_homework_wsis_ns >= 100:
                    $ msg.msg(renpy.translate_string("This homework is already complete"))
                    jump action_train_home_wsis_task

                else:

                    call screen minigame_logic(var_the="any", var_num=2, var_mod="continuous", var_tim=int(30 * (1 + (perk_int_log*0.5))))
                    $ add_stat("hero", "int_log", _return)

                    $ task_homework_wsis_ns += min(100, _return*20) # Homework of Mathematics & Logic

                    # Apply homework effects (same as intellect training)
                    $ times_int += 1
                    $ add_stat("hero", "ene", -5)
                    $ gametimemin += 30
                    call gametime from _call_gametime_51

            "🥂 Humanities & Socials{p}[C_Dat]([task_homework_wsis_hu]%% done)[C_Off]" ("training_int_study_hero"):

                if task_homework_wsis_hu >= 100:
                    $ msg.msg(renpy.translate_string("This homework is already complete"))
                    jump action_train_home_wsis_task

                else:

                    if renpy.random.random() < 0.75:
                        $ a_event_0 = renpy.random.choice(["Beach_015", "Park_015", "School_015"])
                        call screen minigame_find(var_map=a_event_0, var_mod="continuous", var_cnt=10, var_tim=30, var_sca=int(5/(1+(perk_int_per*0.5))))
                        $ add_stat("hero", "int_per", _return)

                    else:
                        call screen minigame_memory(var_pla=perk_int_mem, var_cpu=1, var_mod="classic")
                        $ add_stat("hero", "int_mem", _return)

                    $ task_homework_wsis_hu += min(100, _return*20) # Homework of Humanities & Socials

                    # Apply homework effects (same as intellect training)
                    $ times_int += 1
                    $ add_stat("hero", "ene", -5)
                    $ gametimemin += 30
                    call gametime from _call_gametime_52

            "Return":
                jump action_train_home_intro

        jump action_train_home_wsis_task

    label action_train_home_int:

        if is_specialevent:
            mind "(I need to do other things now)"
            jump action_train_home_intro

        elif stat_ene < 10:
            mind "(I'm too tired for this.)"
            jump action_train_home_intro

        elif times_int >= 2:
            mind "(I already trained intellect twice today. I should rest.)"
            jump action_train_home_intro

        menu (screen="menu_img"):

            "👁 PER" ("training_int_study_hero"):
                $ a_event_0 = renpy.random.choice(["Beach_015", "Park_015", "School_015"])
                call screen minigame_find(var_map=a_event_0, var_mod="continuous", var_cnt=10, var_tim=30, var_sca=int(5/(1+(perk_int_per*0.5))))
                $ add_stat("hero", "int_per", _return*2)

            "🧠 MEM" ("training_int_study_hero"):
                call screen minigame_memory(var_pla=perk_int_mem, var_cpu=1, var_mod="classic")
                $ add_stat("hero", "int_mem", _return*2)

            "🧩 LOG" ("training_int_study_hero"):
                #$ a_event_0 = renpy.random.choice(["math", "color", "spell", "shape", "emoji", "opposite"])
                call screen minigame_logic(var_the="any", var_num=2, var_mod="continuous", var_tim=int(30 * (1 + (perk_int_log*0.5))))
                $ add_stat("hero", "int_log", _return*2)

            "Return":
                jump action_train_home_intro

        # Apply training effects
        $ times_int += 1
        $ add_stat("hero", "ene", -5)
        $ gametimemin += 30
        call gametime from _call_gametime_53

        jump action_train_home_int

    label action_train_home_phy:

        if is_specialevent:
            mind "(I need to do other things now)"
            jump action_train_home_intro

        elif stat_ene < 10:
            mind "(I'm too tired for this.)"
            jump action_train_home_intro

        elif times_phy >= 2:
            mind "(I already trained physics twice today. I should rest.)"
            jump action_train_home_intro

        menu (screen="menu_img"):

            "👟 Agility" ("training_phy_jumprope_hero"):
                scene training_phy_jumprope_hero
                call screen minigame_sequence(time_pass=(1 / (1 + (stat_phy_agi * 0.01))), count_arrow=1, var_txt=None, var_mod="continuous", var_sco=0, var_sca=0.2, var_tim=int(250 * (1 + (perk_phy_agi * 0.5))))
                $ add_stat("hero", "phy_agi", _return*2)

            "🛡 Resistance" ("training_phy_plank_hero"):
                scene training_phy_plank_hero
                call screen minigame_balance(var_mod="continuous", var_rng=int(15 * (1 + (perk_phy_res * 0.5))), var_axi=(25, 75), var_hol=(3 / (1 + (stat_phy_res * 0.01))))
                $ add_stat("hero", "phy_res", _return*2)

            "💪 Strength" ("training_phy_pushup_hero"):
                scene training_phy_pushup_hero
                call screen minigame_thugofwar(var_pla=int((3 + (stat_phy_str * 0.01)) * (1 + (perk_phy_str * 0.5))), var_npc=3, var_bao=0, var_bam=100, var_tio=1, var_tim=100, var_txt=None, var_mod="continuous", var_sco=0, var_sca=0.2)
                $ add_stat("hero", "phy_str", _return*2)

            "Return":
                jump action_train_home_intro

        # Apply training effects
        $ times_phy += 1
        $ add_stat("hero", "ene", -5)
        $ add_stat("hero", "hyg", -(10 + (stat_hyg * 0.3)))
        $ gametimemin += 30
        call gametime from _call_gametime_54

        jump action_train_home_phy

    label action_train_home_end:

        play BGM "audio/W2C - Tranquility.mp3"
        jump show_ui

# ----------------------------------------------------------------------------------------------------
label action_trainCHA:
# ----------------------------------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_106

    # --- menu_img test (2 choices + text-only) ---
    menu (screen="menu_img"):
        "Train Physics" ("training_phy_intro_hero"):
            $ a_check_0 = "PHY"

        "Train Intellect" ("training_int_study_hero"):
            $ a_check_0 = "INT"

        "Return":
            jump show_ui

    if a_check_0 == "PHY":
        # --- menu_img test (3 choices) ---
        menu (screen="menu_img"):
            "👟 Agility" ("training_phy_jumprope_hero"):
                scene training_phy_jumprope_hero
                call screen minigame_sequence(time_pass=(1 / (1 + (stat_phy_agi * 0.01))), count_arrow=1, var_txt=None, var_mod="continuous", var_sco=0, var_sca=0.2, var_tim=int(250 * (1 + (perk_phy_agi * 0.5))))
                $ add_stat("hero", "phy_agi", _return*2)

            "🛡 Resistance" ("training_phy_plank_hero"):
                scene training_phy_plank_hero
                call screen minigame_balance(var_mod="continuous", var_rng=int(15 * (1 + (perk_phy_res * 0.5))), var_axi=(25, 75), var_hol=(3 / (1 + (stat_phy_res * 0.01))))
                $ add_stat("hero", "phy_res", _return*2)

            "💪 Strength" ("training_phy_pushup_hero"):
                scene training_phy_pushup_hero
                call screen minigame_thugofwar(var_pla=int((3 + (stat_phy_str * 0.01)) * (1 + (perk_phy_str * 0.5))), var_npc=3, var_bao=0, var_bam=100, var_tio=1, var_tim=100, var_txt=None, var_mod="continuous", var_sco=0, var_sca=0.2)
                $ add_stat("hero", "phy_str", _return*2)

            "Return":
                jump show_ui

    if is_specialevent:
        mind "(I need to do other things now)"

    elif stat_ene >= 10 and times_cha < 2:
        $ times_cha += 1

        scene bg_0
        with Dissolve(1)

        $ add_stat("hero", "bonus_cha", (5 / (0.5+(times_cha*0.5))))
        $ add_stat("hero", "ene", -5)

        scene training_cha_bg
        show training_cha_hero1
        show training_cha_mg
        show training_cha_hero2
        with dissolve
        pause

        $ gametimemin += 30
        call gametime from _call_gametime_55

    else:
        mind "(I'm too tired for this.)"

    jump show_ui

# ----------------------------------------------------------------------------------------------------
label action_trainINT:
# ----------------------------------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_107
    $ check_stat()

    if is_specialevent:
        mind "(I need to do other things now)"

    elif stat_ene >= 10 and times_int < 2:
        $ times_int += 1

        scene bg_0
        with Dissolve(1)

        scene training_int_bg
        show training_int_hero
        with dissolve

        menu:

            "👁 PER":
                $ a_event_0 = renpy.random.choice(["Beach_015", "Park_015", "School_015"])
                call screen minigame_find(var_map=a_event_0, var_mod="continuous", var_cnt=10, var_tim=30, var_sca=int(5/(1+(perk_int_per*0.5))))
                $ add_stat("hero", "int_per", _return*2)

            "🧠 MEM":
                call screen minigame_memory(var_pla=perk_int_mem, var_cpu=1, var_mod="classic")
                $ add_stat("hero", "int_mem", _return*2)

            "🧩 LOG":
                #$ a_event_0 = renpy.random.choice(["math", "color", "spell", "shape", "emoji", "opposite"])
                call screen minigame_logic(var_the="any", var_num=2, var_mod="continuous", var_tim=int(30 * (1 + (perk_int_log*0.5))))
                $ add_stat("hero", "int_log", _return*2)

        $ add_stat("hero", "ene", -5)

        pause

        $ gametimemin += 30
        call gametime from _call_gametime_56

    else:
        mind "(I'm too tired for this.)"

    jump show_ui

# ----------------------------------------------------------------------------------------------------
label action_trainPHY:
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_108
    $ check_stat()
    
    if is_specialevent:
        mind "(I need to do other things now)"

    elif stat_ene >= 10 and times_phy < 2:
        $ times_phy += 1

        stop BGM fadeout 1

        scene bg_0
        with Dissolve(1)

        play BGM "audio/W2C - Bravery.mp3"

        scene training_phy_bg
        show training_phy_hero
        with dissolve

        menu:
        
            "👟 AGI":
                call screen minigame_sequence(time_pass=(1 / (1 + (stat_phy_agi * 0.01))), count_arrow=1, var_txt=None, var_mod="continuous", var_sco=0, var_sca=0.2, var_tim=int(250 * (1 + (perk_phy_agi * 0.5))))
                $ add_stat("hero", "phy_agi", _return*2)

            "💪 STR":
                call screen minigame_thugofwar(var_pla=int((3 + (stat_phy_str * 0.01)) * (1 + (perk_phy_str * 0.5))), var_npc=3, var_bao=0, var_bam=100, var_tio=1, var_tim=100, var_txt=None, var_mod="continuous", var_sco=0, var_sca=0.2)
                $ add_stat("hero", "phy_str", _return*2)

            "🛡 RES":
                call screen minigame_balance(var_mod="continuous", var_rng=int(15 * (1 + (perk_phy_res * 0.5))), var_axi=(25, 75), var_hol=(3 / (1 + (stat_phy_res * 0.01))))
                $ add_stat("hero", "phy_res", _return*2)

        #$ add_stat("hero", "phy", _return/5)
        $ add_stat("hero", "ene", -5)
        $ add_stat("hero", "hyg", -(10 + (stat_hyg * 0.3)))

        pause

        $ gametimemin += 30
        call gametime from _call_gametime_57

    else:
        mind "(I'm too tired for this.)"

    jump show_ui

# ----------------------------------------------------------------------------------------------------
label action_quest:
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_109
    menu:
        # Meeting Scene
        "[C_Dat]🌟[C_Off] Clubs Start" if (hine_quest_1 == 0) and Check_CharInMap("hero", "school", "class_1b") and Check_TimeStr("school_class_2"):
            jump hine_quest0
        "[C_Dat]🌟[C_Off] Physical XXXducation I" if (wtpe_quest != 1) and (stat_phy >= 20) and Check_CharInMap("hero", "school", "sports_court") and Check_TimeStr("school_class"):
            jump wtpe_quest_0_1
        "[C_Dat]🌟[C_Off] Help the P.E. teacher with an errand" if (not hero_locker_f_access) and (hero_locker_favor_day != gametimeday) and Check_CharInMap("hero", "school", "sports_court") and Check_TimeStr("school_class"):
            jump wtpe_locker_favor
        "{image=icon_wpre} Talk to {nm}[fnamewpre]{/nm} before the class" if (wpre_quest_1 == 0) and Check_CharInMap("hero", "school", "class_1b") and Check_TimeStr("school_class"):
            jump wpre_quest0
        "{image=icon_wgal} Do an activity in pairs" if (wgal_quest_1 == 0) and Check_CharInMap("hero", "school", "class_1b") and Check_TimeStr("school_class"):
            jump wgal_quest0
        "{image=icon_wota} Talk to {nm}[fnamewota]{/nm} before the class" if (wota_quest_1 == 0) and Check_CharInMap("hero", "school", "swimming_pool") and Check_TimeStr("school_class"):
            jump wota_quest0
        "{image=icon_wlaz} Go to PE class" if (wlaz_quest_1 == 0) and Check_CharInMap("hero", "school", "locker_m") and Check_TimeStr("school_class"):
            jump wlaz_quest0
        "{image=icon_wuza} Go to PE class" if (wuza_quest_1 == 0) and Check_CharInMap("hero", "school", "sports_court") and Check_TimeStr("school_class"):
            jump wuza_quest0
        "{image=icon_wric} Go to the canteen" if (wric_quest_1 == 0) and Check_CharInMap("hero", "school", "hallway_2") and Check_TimeStr("school_breaks_1"):
            jump wric_quest0
        "{image=icon_wgot} Go to the music room" if (wgot_quest_1 == 0) and Check_CharInMap("hero", "school", "hallway_1") and Check_TimeStr("school_breaks_1"):
            jump wgot_quest0
        "{image=icon_wdel} Go to classroom" if (wdel_quest_1 == 0) and Check_CharInMap("hero", "school", "hallway_2") and Check_TimeStr("school_breaks_1"):
            jump wdel_quest0
        "{image=icon_wdis} Go to the hallway" if (wdis_quest_1 == 0) and Check_CharInMap("hero", "school", "class_1b") and Check_TimeStr("school_breaks_2"):
            jump wdis_quest0
        "{image=icon_hprv} Go to the courtyard" if (hprv_quest_1 == 0) and Check_CharInMap("hero", "school", "hallway_1") and Check_TimeStr("school_breaks_2"):
            jump hprv_quest0

        #"{image=icon_wsuk} Swim" if Check_CharInMap("hero", "school", "swimming_pool") and (wsuk_quest_1 == 0 and hero_quest_3 >= 3) and (gametimehour == 18):
            #jump wsuk_quest_0_1

        # Low Intimacy
        "{image=icon_wnei} Look At The Window" if (wnei_quest_2 >= 1) and (gametimehour <= 7) and Check_CharInMap("hero", "home", "bedroom_hero") and Check_CharInMap("wnei", "neighbor", "bedroom_wnei") and (gametimeweek == "Saturday"):
            jump wnei_quest_2_2
        "{image=icon_wsis} Check [C_Nam][fnamewsis][C_Off]" if Check_CharInMap("hero", "home", "living_room") and (gametimehour >= 19 and gametimehour < 21):
            jump wsis_quest_1_kitchen

        # Return
        "Return":
            return

# ----------------------------------------------------------------------------------------------------
label action_watchtv(buceta=None):
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_110

    $ a_event_0 = []
    $ a_event_2 = buceta
    $ a_event_3 = 0
    $ a_event_4 = "common"
    $ a_event_5 = [] # Add NPCs that appeared

    if not buceta == "wnei" and (Check_IfActivity(char_id="wnei", act_name="watching tv") and Check_CharSameMap("hero", "wnei")):
        $ a_event_0.append("wnei")
    if not buceta == "wsis" and (Check_IfActivity(char_id="wsis", act_name="watching tv") and Check_CharSameMap("hero", "wsis")):
        $ a_event_0.append("wsis")
    if not buceta == "wmom" and (Check_IfActivity(char_id="wmom", act_name="watching tv") and Check_CharSameMap("hero", "wmom")):
        $ a_event_0.append("wmom")

    if buceta != None:
        $ a_event_3 += 1

    $ a_event_3 += sum(1 for xereca in a_event_0)

    scene sitting_bg home_livingroom

    # ----------------------------------------------------------------------------------------------------
    if a_event_3 >= 2: # 2 NPCs
    # ----------------------------------------------------------------------------------------------------
        # Right
        if buceta != None:
            if buceta == "wnei":
                $ a_event_5.append("wnei")
                $ add_stat("wnei", "inti", 0.6)
                if wnei_inti < 20:
                    show sitting_wnei_body 1 at RR
                    show sitting_wnei_wear 1home at RR
                else:
                    $ a_event_4 = renpy.random.choice(["embrace_1", "embrace_2"])
                    if a_event_4 == "embrace_1":
                        show sitting_embrace_1_wnei_body_bg 1 at CC
                        show sitting_embrace_1_wnei_wear_bg 1_home at CC

            elif buceta == "wmom":
                $ a_event_5.append("wmom")
                $ add_stat("wmom", "inti", 0.6)
                if wmom_inti < 20:
                    show sitting_wmom_body 1 at RR
                    if wmom_wear == "sleep":
                        show sitting_wmom_boob 0 at RR
                        show sitting_wmom_wear 1sleep at RR
                        show sitting_wmom_hair 0 at RR
                    else:
                        show sitting_wmom_boob 1 at RR
                        show sitting_wmom_wear 1home at RR
                        show sitting_wmom_hair 1 at RR
                else:
                    $ a_event_4 = "embrace_1"
                    show sitting_embrace_1_wmom_body_bg 1 at CC
                    show sitting_embrace_1_wmom_wear_bg 1_home at CC

            elif buceta == "wsis":
                $ a_event_5.append("wsis")
                $ add_stat("wsis", "inti", 0.6)
                if wmom_inti < 20:
                    show sitting_wsis_body 1 at RR
                    if wsis_wear == "sleep":
                        show sitting_wsis_wear 1sleep at RR
                    else:
                        show sitting_wsis_wear 1home at RR
                else:
                    $ a_event_4 = "embrace_2"

        else:
            $ a_event_1 = renpy.random.choice(a_event_0)
            if a_event_1 == "wnei":
                $ a_event_5.append("wnei")
                $ add_stat("wnei", "inti", 0.6)
                if wnei_inti < 20:
                    $ a_event_0.remove("wnei")
                    show sitting_wnei_body 1 at RR
                    show sitting_wnei_wear 1home at RR
                else:
                    $ a_event_4 = renpy.random.choice(["embrace_1", "embrace_2"])
                    if a_event_4 == "embrace_1":
                        show sitting_embrace_1_wnei_body_bg 1 at CC
                        show sitting_embrace_1_wnei_wear_bg 1_home at CC
            elif a_event_1 == "wmom":
                $ a_event_5.append("wmom")
                $ add_stat("wmom", "inti", 0.6)
                $ a_event_0.remove("wmom")
                if wmom_inti < 20:
                    show sitting_wmom_body 1 at RR
                    if wmom_wear == "sleep":
                        show sitting_wmom_boob 0 at RR
                        show sitting_wmom_wear 1sleep at RR
                        show sitting_wmom_hair 0 at RR
                    else:
                        show sitting_wmom_boob 1 at RR
                        show sitting_wmom_wear 1home at RR
                        show sitting_wmom_hair 1 at RR
                else:
                    $ a_event_4 = "embrace_1"
                    show sitting_embrace_1_wmom_body_bg 1 at CC
                    show sitting_embrace_1_wmom_wear_bg 1_home at CC
            elif a_event_1 == "wsis":
                $ a_event_5.append("wsis")
                $ add_stat("wsis", "inti", 0.6)
                $ a_event_0.remove("wsis")
                if wsis_love < 20 and wsis_quest_2 < 1:
                    show sitting_wsis_body 1 at RR
                    if wsis_wear == "sleep":
                        show sitting_wsis_wear 1sleep at RR
                    else:
                        show sitting_wsis_wear 1home at RR
                else:
                    $ a_event_4 = "embrace_2"

        if a_event_4 == "common":
            # HERO
            show sitting_hero_body 1 at CC
            show sitting_hero_face 1a0 at CC
            show sitting_hero_wear 1home at CC

        elif a_event_4 == "embrace_1":
            # HERO
            show sitting_embrace_1_hero_body 1 at CC
            show sitting_embrace_1_hero_wear 1_home at CC
            show sitting_embrace_1_hero_face 1_s0 at CC
            if buceta == "wnei" or a_event_1 == "wnei":
                $ add_stat("wnei", "love", 1)
                $ add_stat("wnei", "lust", 0.5)
                show sitting_embrace_1_wnei_body_fg 1 at CC
                show sitting_embrace_1_wnei_face 1_a0 at CC
            elif buceta == "wmom" or a_event_1 == "wmom":
                $ add_stat("wmom", "love", 1)
                $ add_stat("wmom", "lust", 0.5)
                show sitting_embrace_1_wmom_body_fg 1 at CC
                show sitting_embrace_1_wmom_wear_fg 1_home at CC
                show sitting_embrace_1_wmom_face 1_a0 at CC

        elif a_event_4 == "embrace_2":
            # HERO
            show sitting_embrace_2_hero_bg_body 1 at CC
            show sitting_embrace_2_hero_bg_wear 1_home at CC
            show sitting_embrace_2_hero_face o0 at CC
            if buceta == "wnei" or a_event_1 == "wnei":
                $ add_stat("wnei", "love", 1)
                $ add_stat("wnei", "lust", 0.5)
                show sitting_embrace_2_wnei_bg_body 1 at CC
                show sitting_embrace_2_wnei_bg_wear 1_home at CC
                show sitting_embrace_2_wnei_face a0 at CC
            if buceta == "wsis" or a_event_1 == "wsis":
                $ add_stat("wsis", "love", 1)
                $ add_stat("wsis", "lust", 0.5)
                show sitting_embrace_2_wsis_body 1 at CC
                if wsis_wear == "sleep":
                    show sitting_embrace_2_wsis_wear 1_sleep at CC
                else:
                    show sitting_embrace_2_wsis_wear 1_home at CC
                show sitting_embrace_2_wsis_face o0 at CC
            # HERO
            show sitting_embrace_2_hero_fg_body 1 at CC
            show sitting_embrace_2_hero_fg_wear 1_home at CC
            if buceta == "wnei" or a_event_1 == "wnei":
                show sitting_embrace_2_wnei_fg_body 1 at CC

        elif a_event_4 == "lap1":
            $ add_stat("wnei", "love", 1)
            $ add_stat("wnei", "lust", 0.5)
            # HERO
            show sitting_lap_herownei_body 1 at CC
            show sitting_lap_herownei_hero_wear 1_home at CC
            show sitting_lap_herownei_hero_face s0 at CC
            show sitting_lap_herownei_wnei_wear 1_home at CC
            show sitting_lap_herownei_wnei_face 1_a0 at CC

        # Left
        $ a_event_1 = renpy.random.choice(a_event_0)
        if a_event_1 == "wnei":
            $ a_event_5.append("wnei")
            $ add_stat("wnei", "inti", 0.6)
            $ a_event_0.remove("wnei")
            show sitting_wnei_body 1 at LL
            show sitting_wnei_wear 1home at LL
        elif a_event_1 == "wmom":
            $ a_event_5.append("wmom")
            $ add_stat("wmom", "inti", 0.6)
            $ a_event_0.remove("wmom")
            show sitting_wmom_body 1 at LL
            if wmom_wear == "sleep":
                show sitting_wmom_boob 0 at LL
                show sitting_wmom_wear 1sleep at LL
                show sitting_wmom_hair 0 at LL
            else:
                show sitting_wmom_boob 1 at LL
                show sitting_wmom_wear 1home at LL
                show sitting_wmom_hair 1 at LL
        elif a_event_1 == "wsis":
            $ a_event_5.append("wsis")
            $ add_stat("wsis", "inti", 0.6)
            $ a_event_0.remove("wsis")
            show sitting_wsis_body 1 at LL
            if wsis_wear == "sleep":
                show sitting_wsis_wear 1sleep at LL
            else:
                show sitting_wsis_wear 1home at LL

    # ----------------------------------------------------------------------------------------------------
    else: # 1 NPC
    # ----------------------------------------------------------------------------------------------------
        # Right
        if buceta != None:
            if buceta == "wnei":
                $ a_event_5.append("wnei")
                $ add_stat("wnei", "inti", 0.6)
                if wnei_inti < 20:
                    show sitting_wnei_body 1 at RC
                    show sitting_wnei_wear 1home at RC
                else:
                    $ a_event_4 = renpy.random.choice(["lap1", "embrace_2"])

            elif buceta == "wmom":
                $ a_event_5.append("wmom")
                $ add_stat("wmom", "inti", 0.6)
                if wmom_inti < 20:
                    show sitting_wmom_body 1 at RC
                    if wmom_wear == "sleep":
                        show sitting_wmom_boob 0 at RC
                        show sitting_wmom_wear 1sleep at RC
                        show sitting_wmom_hair 0 at RC
                    else:
                        show sitting_wmom_boob 1 at RC
                        show sitting_wmom_wear 1home at RC
                        show sitting_wmom_hair 1 at RC
                else:
                    $ a_event_4 = "embrace_1"
                    show sitting_embrace_1_wmom_body_bg 1 at CC
                    show sitting_embrace_1_wmom_wear_bg 1_home at CC

            elif buceta == "wsis":
                $ a_event_5.append("wsis")
                $ add_stat("wsis", "inti", 0.6)
                if wmom_inti < 20:
                    show sitting_wsis_body 1 at RC
                    if wsis_wear == "sleep":
                        show sitting_wsis_wear 1sleep at RC
                    else:
                        show sitting_wsis_wear 1home at RC
                else:
                    $ a_event_4 = "embrace_2"

        else:
            $ a_event_1 = renpy.random.choice(a_event_0)
            if a_event_1 == "wnei":
                $ a_event_5.append("wnei")
                $ add_stat("wnei", "inti", 0.6)
                $ a_event_0.remove("wnei")
                if wnei_inti < 20:
                    show sitting_wnei_body 1 at RC
                    show sitting_wnei_wear 1home at RC
                else:
                    $ a_event_4 = renpy.random.choice(["lap1", "embrace_2"])
            elif a_event_1 == "wmom":
                $ a_event_5.append("wmom")
                $ add_stat("wmom", "inti", 0.6)
                $ a_event_0.remove("wmom")
                if wmom_inti < 20:
                    show sitting_wmom_body 1 at RC
                    if wmom_wear == "sleep":
                        show sitting_wmom_boob 0 at RC
                        show sitting_wmom_wear 1sleep at RC
                        show sitting_wmom_hair 0 at RC
                    else:
                        show sitting_wmom_boob 1 at RC
                        show sitting_wmom_wear 1home at RC
                        show sitting_wmom_hair 1 at RC
                else:
                    $ a_event_4 = "embrace_1"
                    show sitting_embrace_1_wmom_body_bg 1 at CC
                    show sitting_embrace_1_wmom_wear_bg 1_home at CC
            elif a_event_1 == "wsis":
                $ a_event_5.append("wsis")
                $ add_stat("wsis", "inti", 0.6)
                $ a_event_0.remove("wsis")
                if wsis_love < 20 and wsis_quest_2 < 1:
                    show sitting_wsis_body 1 at RC
                    if wsis_wear == "sleep":
                        show sitting_wsis_wear 1sleep at RC
                    else:
                        show sitting_wsis_wear 1home at RC
                else:
                    $ a_event_4 = "embrace_2"

        if a_event_4 == "common":
            # HERO
            show sitting_hero_body 1 at CC
            show sitting_hero_face 1a0 at CC
            show sitting_hero_wear 1home at CC

        elif a_event_4 == "embrace_1":
            # HERO
            show sitting_embrace_1_hero_body 1 at CC
            show sitting_embrace_1_hero_wear 1_home at CC
            show sitting_embrace_1_hero_face 1_s0 at CC
            if buceta == "wnei" or a_event_1 == "wnei":
                $ add_stat("wnei", "love", 1)
                $ add_stat("wnei", "lust", 0.5)
                show sitting_embrace_1_wnei_body_fg 1 at CC
                show sitting_embrace_1_wnei_face 1_a0 at CC
            elif buceta == "wmom" or a_event_1 == "wmom":
                $ add_stat("wmom", "love", 1)
                $ add_stat("wmom", "lust", 0.5)
                show sitting_embrace_1_wmom_body_fg 1 at CC
                show sitting_embrace_1_wmom_wear_fg 1_home at CC
                show sitting_embrace_1_wmom_face 1_a0 at CC

        elif a_event_4 == "embrace_2":
            # HERO
            show sitting_embrace_2_hero_bg_body 1 at CC
            show sitting_embrace_2_hero_bg_wear 1_home at CC
            show sitting_embrace_2_hero_face o0 at CC
            if buceta == "wnei" or a_event_1 == "wnei":
                $ add_stat("wnei", "love", 1)
                $ add_stat("wnei", "lust", 0.5)
                show sitting_embrace_2_wnei_bg_body 1 at CC
                show sitting_embrace_2_wnei_bg_wear 1_home at CC
                show sitting_embrace_2_wnei_face a0 at CC
            if buceta == "wsis" or a_event_1 == "wsis":
                $ add_stat("wsis", "love", 1)
                $ add_stat("wsis", "lust", 0.5)
                show sitting_embrace_2_wsis_body 1 at CC
                if wsis_wear == "sleep":
                    show sitting_embrace_2_wsis_wear 1_sleep at CC
                else:
                    show sitting_embrace_2_wsis_wear 1_home at CC
                show sitting_embrace_2_wsis_face o0 at CC
            # HERO
            show sitting_embrace_2_hero_fg_body 1 at CC
            show sitting_embrace_2_hero_fg_wear 1_home at CC
            if buceta == "wnei" or a_event_1 == "wnei":
                show sitting_embrace_2_wnei_fg_body 1 at CC

        elif a_event_4 == "lap1":
            $ add_stat("wnei", "love", 1)
            $ add_stat("wnei", "lust", 0.5)
            # HERO
            show sitting_lap_herownei_body 1 at CC
            show sitting_lap_herownei_hero_wear 1_home at CC
            show sitting_lap_herownei_hero_face s0 at CC
            show sitting_lap_herownei_wnei_wear 1_home at CC
            show sitting_lap_herownei_wnei_face 1_a0 at CC

    if gametimehour < 18 and gametimehour > 5:
        show fx_light:
            blend "add"
    elif gametimehour == 18:
        show fx_afternoon:
            blend "add"
    else:
        show fx_light:
            blend "add"
        show fx_night:
            blend "multiply"

    pause

    if gametimehour >= 22:
        call action_watchtv_carryprincess from _call_action_watchtv_carryprincess

    if a_event_1 == "wnei" or a_event_1 == "wsis" or a_event_1 == "wmom":
        pass

    else:
        $ gametimemin += 10
        call gametime from _call_gametime_58
        jump show_ui

    while Get_ActivityName(a_event_1) in ["watching tv"]:
        $ gametimemin += 10
        if a_event_4 == "lap1":
            $ hero_lust += 10
            if hero_lust >= 20:
                call action_watchtv_paudurecencia from _call_action_watchtv_paudurecencia
        call gametime from _call_gametime_59

    jump show_ui

# ----------------------------------------------------------------------------------------------------
label action_watchtv_carryprincess:
# ----------------------------------------------------------------------------------------------------
    scene bg_0 with Dissolve(1)

    if len(a_event_5) > 1:
        "It seems that girls fell asleep."
    else:
        "It seems that someone fell asleep."

    $ a_event_1 = round((20 + ((3 + (perk_phy_str * 2)) * (3 + (perk_phy_str * 2)))) * (1 + (stat_phy * 0.01)), 2)
    $ a_event_2 = round((19*wsis_size*wsis_size), 2)
    $ a_event_3 = round((21*wnei_size*wnei_size), 2)
    $ a_event_4 = round((30*wmom_size*wmom_size), 2)

    while a_event_4 != None:

        menu:
            "Carry [C_Nam][fnamewsis][C_Off] to her room" if "wsis" in a_event_5:
                if a_event_1 > a_event_2:
                    if renpy.music.get_playing(channel='BGM') != "audio/W2C - Romance.mp3":
                        play BGM "audio/W2C - Romance.mp3"
                    scene bg_2 sparkling
                    show carry_1_hero_body_bg 1
                    show carry_1_hero_wear_bg 1_home
                    show carry_1_wsis_body 1
                    show carry_1_wsis_wear 1_under
                    show carry_1_wsis_wear 1_sleep
                    show carry_1_hero_body_fg 1
                    show fx_light:
                        blend "add"
                    with dissolve

                    pause

                    scene bg_0
                    with Dissolve(1)

                    $ a_event_5.remove("wsis")
                    $ add_stat("wsis", "inti", 0.5)
                    $ add_stat("wmom", "love", 0.5)
                    $ add_stat("hero", "phy", 0.5)
                    $ msg.msg(renpy.translate_string("You carried her to her room."))
                else:
                    $ msg.msg(renpy.translate_string("Oops! [C_Nam][fnamewsis][C_Off] seems to be too heavy for you."))

            "Carry [C_Nam][fnamewnei][C_Off] to [C_Nam][fnamewsis][C_Off] room" if "wnei" in a_event_5:
                if a_event_1 > a_event_3:
                    if renpy.music.get_playing(channel='BGM') != "audio/W2C - Romance.mp3":
                        play BGM "audio/W2C - Romance.mp3"
                    scene bg_2 sparkling
                    show carry_1_hero_body_bg 1
                    show carry_1_hero_wear_bg 1_home
                    show carry_1_wnei_body 1
                    show carry_1_wnei_wear 1_under
                    show carry_1_wnei_wear 1_home
                    show carry_1_hero_body_fg 1
                    show fx_light:
                        blend "add"
                    with dissolve

                    pause

                    scene bg_0
                    with Dissolve(1)

                    $ a_event_5.remove("wnei")
                    $ add_stat("wnei", "inti", 0.5)
                    $ add_stat("wmom", "love", 0.5)
                    $ add_stat("hero", "phy", 0.5)
                    $ msg.msg(renpy.translate_string("You carried her to [C_Nam][fnamewsis][C_Off] room."))
                else:
                    $ msg.msg(renpy.translate_string("Oops! The little {nm}[fnamewnei]{/nm} seems to be too heavy for you"))

            "Carry [C_Nam][fnamewmom][C_Off] to her room" if "wmom" in a_event_5:
                if a_event_1 > a_event_4:
                    if renpy.music.get_playing(channel='BGM') != "audio/W2C - Romance.mp3":
                        play BGM "audio/W2C - Romance.mp3"
                    scene bg_2 sparkling
                    show carry_1_hero_body_bg 1
                    show carry_1_hero_wear_bg 1_home
                    show carry_1_wmom_body 1
                    show carry_1_wmom_wear 1_sleep
                    show carry_1_hero_body_fg 1
                    show fx_light:
                        blend "add"
                    with dissolve

                    pause

                    scene bg_0
                    with Dissolve(1)

                    $ a_event_5.remove("wmom")
                    $ add_stat("wmom", "inti", 0.5)
                    $ add_stat("wmom", "love", 0.5)
                    $ add_stat("hero", "phy", 0.5)
                    $ msg.msg(renpy.translate_string("You carried her to her room."))
                else:
                    $ msg.msg(renpy.translate_string("Oops! Mrs. {nm}[fnamewmom]{/nm} seems to be too heavy for you"))

            "Go to your room":
                $ a_event_4 = None

    call passday from _call_passday_1

    return

# ----------------------------------------------------------------------------------------------------
label action_watchtv_paudurecencia:
# ----------------------------------------------------------------------------------------------------

    play SE1 "Record Scratch.mp3"

    $ msg.msg(renpy.translate_string("{aw}{size=60}Oops... You're getting hard!{/size}{/aw}"))

    stop BGM fadeout 2
    pause

    play SE1 "Grow.mp3"
    play SE2 renpy.random.choice(["Moan/B lvl3 (4).ogg", "Moan/B lvl3 (5).ogg", "Moan/B lvl3 (6).ogg", "Moan/B lvl3 (8).ogg", "Moan/B lvl3 (9).ogg"])

    show sitting_lap_herownei_body 2 at CC
    show sitting_lap_herownei_hero_wear 2_home at CC
    show sitting_lap_herownei_hero_face s1 at CC
    show sitting_lap_herownei_wnei_wear 2_home at CC
    show sitting_lap_herownei_wnei_face 2_o1 at CC
    with dissolve

    show sitting_lap_herownei_wnei_face 2_o0 with None

    pause

    show sitting_lap_herownei_wnei_face 2_o1
    wnei "{gg}Ugh!{/gg} It's your lollipop!{nw}"

    play BGM "audio/W2C - Adrenalust.mp3"

    wnei "{gg}Ugh!{/gg} It's your lollipop!{fast}"

    show sitting_lap_herownei_wnei_face 2_o0 with None

    play SE1 "Slip.ogg"
    show sitting_lap_herownei_body 3
    show sitting_lap_herownei_hero_wear 3_home
    show sitting_lap_herownei_wnei_wear 3_home
    with dissolve

    pause

    show sitting_lap_herownei_wnei_face 2_o1
    wnei "How do you make it become super duper giant?"

    show sitting_lap_herownei_wnei_face 2_o0
    hero "{aw}I need to go to the bathroom!!!{/aw}"

    $ hero_lust = 0
    $ a_event_4 = 0

    return


# ----------------------------------------------------------------------------------------------------
label action_study:
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_111
    $ check_stat()

    # Fast-travel: walk HERO to the scheduled class's real room (with a transition) via its goto_ label.
    python:
        _class_map = Get_MapName("hero", map_main="at class")
    if _class_map != "Unknown" and hero_map != _class_map:
        if _class_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["swimming_pool"]["name"]:
            call goto_school_pool from _call_goto_school_pool_2
            scene bg_school pool
        elif _class_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["sports_court"]["name"]:
            call goto_school_sportcourt from _call_goto_school_sportcourt_1
            scene bg_school sportcourt
        else:
            call goto_school_classroom_1b from _call_goto_school_classroom_1b
            scene bg_school classroom_1b
        with dissolve
        pause(0.3)
        return

    # ----------------------------------------------------------------------------------------------------
    # Check quests availability
    # ----------------------------------------------------------------------------------------------------
    if Check_TimeStr("school_class"):
        menu:
            "Focus on class" if 0 > 1: # Disable
                scene bg_0
                with dissolve
                pause(0.5)
                jump action_study_start

            "Focus on socialization":
                scene bg_0
                with dissolve
                pause(0.5)

                # Class
                if hero_map == "School - Classroom (1B)":

                    if Check_TimeStr("school_class_1"):
                        $ a_event_1 = (gametimehour * 60) + gametimemin

                    elif Check_TimeStr("school_class_2"):
                        $ a_event_1 = (gametimehour * 60) + gametimemin

                    $ a_event_2 = a_event_1/600
                    call action_study_class_socialization from _call_action_study_class_socialization

                    call gametime_schoolnext(a_event_2) from _call_gametime_schoolnext
                    $ gametimemin += _return
                    call gametime from _call_gametime_60
                    jump action_study_end

                # Jogging
                if hero_map == "School - Sports Court":

                    if not (wpre_quest_1 >= 1 or wdis_quest_1 >= 1 or wota_quest_1 >= 1 or wgal_quest_1 >= 1 or wric_quest_1 >= 1 or wgot_quest_1 >= 1 or wdel_quest_1 >= 1 or wuza_quest_1 >= 1 or wlaz_quest_1 >= 1 or hprv_quest_1 >= 1 or hine_quest_1 >= 1):
                        $ msg.msg(renpy.translate_string("You felt like you weren't familiar with anyone in your class yet, so you decided to jog alone"))
                        jump action_study_start

                    else:
                        call gametime_schoolnext(a_event_2) from _call_gametime_schoolnext_1
                        $ a_event_1 = _return

                    $ a_event_3 = 0.25
                    while a_event_1 > 0:
                        if gametimemin == 0 or gametimemin == 30:
                            $ a_event_2 = 30
                            $ gametimemin += a_event_2

                        else:
                            $ a_event_2 = 30 - gametimemin
                            $ gametimemin += a_event_2

                        $ a_event_1 -= 30

                        call gametime from _call_gametime_61

                        $ a_event_2 = a_event_2/60
                        if renpy.random.random() < (a_event_3 + (0.75 * ((stat_cha/200)*(0.5 + (perk_cha_sex * 0.5))))):
                            $ a_event_3 = max(0, a_event_3-0.1)
                            call action_jog_sportcourt from _call_action_jog_sportcourt
                        else:
                            $ a_event_3 += 0.25
                            $ msg.msg(renpy.translate_string("You couldn't socialize with anyone, so you started jogging alone"))
                            call action_jog_sportcourt from _call_action_jog_sportcourt_1
                            pause

                # Swimming
                if hero_map == "School - Swimming Pool":

                    if not (wpre_quest_1 >= 1 or wdis_quest_1 >= 1 or wota_quest_1 >= 1 or wgal_quest_1 >= 1 or wric_quest_1 >= 1 or wgot_quest_1 >= 1 or wdel_quest_1 >= 1 or wuza_quest_1 >= 1 or wlaz_quest_1 >= 1 or hprv_quest_1 >= 1 or hine_quest_1 >= 1):
                        $ msg.msg(renpy.translate_string("You felt like you weren't familiar with anyone in your class yet, so you decided to swim a lap"))
                        jump action_study_start

                    else:
                        call gametime_schoolnext(a_event_2) from _call_gametime_schoolnext_2
                        $ a_event_1 = _return

                    $ a_event_3 = 0.25
                    while a_event_1 > 0:
                        if gametimemin == 0 or gametimemin == 30:
                            $ a_event_2 = 30
                            $ gametimemin += a_event_2

                        else:
                            $ a_event_2 = 30 - gametimemin
                            $ gametimemin += a_event_2

                        $ a_event_1 -= 30

                        call gametime from _call_gametime_62

                        $ a_event_2 = a_event_2/60
                        if renpy.random.random() < (a_event_3 + (0.75 * ((stat_cha/200)*(0.5 + (perk_cha_sex * 0.5))))):
                            $ a_event_3 = max(0, a_event_3-0.1)
                            call action_study_swimming_socialization from _call_action_study_swimming_socialization
                        else:
                            $ a_event_3 += 0.25
                            $ msg.msg(renpy.translate_string("You couldn't socialize with anyone, so you started swimming"))
                            call action_study_swimming_study from _call_action_study_swimming_study

            "Return":
                return

    elif gametimehour < 7:
        $ msg.msg(renpy.translate_string("Next class starts at 7:00"))

    elif (gametimehour >= 9 and (gametimehour == 10 and gametimemin < 30)):
        $ msg.msg(renpy.translate_string("Next class starts at 10:30"))

    else:
        $ msg.msg(renpy.translate_string("There are no more classes today"))

    jump show_ui

    # ----------------------------------------------------------------------------------------------------
    label action_study_start: # Class
    # ----------------------------------------------------------------------------------------------------
        if gametimehour >= 7 and gametimehour <= 9:

            $ a_event_0 = ((10*2) - (2 * (gametimehour + (gametimemin/60))))

            if hero_map == "School - Classroom (1B)":
                $ add_stat("hero", "int_log", a_event_0 * 0.5, stat_mod=False)
                scene studying_classroom with fade

            elif hero_map == "School - Sports Court" or hero_map == "School - Swimming Pool":
                $ add_stat("hero", "phy_agi", a_event_0 * 0.5, stat_mod=False)
                if hero_map == "School - Swimming Pool":
                    scene studying_swimming_bg
                    if renpy.random.random() < 0.5:
                        show studying_swimming_hero backstroke
                    else:
                        show studying_swimming_hero crawl
                    with dissolve
                else:
                    scene bg_0

            pause

            $ a_event_0 = (gametimehour * 60) + gametimemin
            $ gametimemin += 600 - a_event_0 # Advance to 10:00

        elif (gametimehour == 10 and gametimemin >= 30) or (gametimehour >= 11 and gametimehour <= 12):

            $a_event_0 = ((13*2) - (2 * (gametimehour + (gametimemin/60))))

            if hero_map == "School - Classroom (1B)":
                $ add_stat("hero", "int_log", a_event_0 * 0.5, stat_mod=False)
                scene studying_classroom with fade

            elif hero_map == "School - Sports Court" or hero_map == "School - Swimming Pool":
                $ add_stat("hero", "phy_agi", a_event_0 * 0.5, stat_mod=False)
                if hero_map == "School - Swimming Pool":
                    scene studying_swimming_bg
                    if renpy.random.random() < 0.5:
                        show studying_swimming_hero backstroke
                    else:
                        show studying_swimming_hero crawl
                    with dissolve
                else:
                    scene bg_0
            pause

            $ a_event_0 = (gametimehour * 60) + gametimemin
            $ gametimemin += 780 - a_event_0 # Advance to 13:00

        jump action_study_end

    # ----------------------------------------------------------------------------------------------------
    label action_study_end: # After Class
    # ----------------------------------------------------------------------------------------------------
        call gametime from _call_gametime_63
        # ----------------------------------------------------------------------------------------------------
        if ((gametimehour == 10 and gametimemin == 0) or (gametimehour == 13 and gametimemin == 0)) and (hero_map == "School - Swimming Pool"):
            $ stat_hyg = 100
            $ hero_needs[0] = True
            $ msg.msg(renpy.translate_string("You are clean."))

    jump show_ui

    # ----------------------------------------------------------------------------------------------------
    label action_study_swimming_study: # Swimming Situations
    # ----------------------------------------------------------------------------------------------------
        $ a_event_0 = ["hero","hero","hero","hero","hero"]

        if wpre_quest_1 >= 1:
            $ a_event_0.append("wpre")
        if wdis_quest_1 >= 1:
            $ a_event_0.append("wdis")
        if wota_quest_1 >= 1:
            $ a_event_0.append("wota")
        if wgal_quest_1 >= 1:
            $ a_event_0.append("wgal")
        if wric_quest_1 >= 1:
            $ a_event_0.append("wric")
        if wuza_quest_1 >= 1:
            $ a_event_0.append("wuza")
        if hine_quest_1 >= 1:
            $ a_event_0.append("hine")
        if wgot_quest_1 >= 1:
            $ a_event_0.append("wgot")

        $ a_event_0 = renpy.random.choice(a_event_0)

        if a_event_0 == "wdis":
            $ msg.msg(renpy.translate_string("Oops, you accidentally touched something!"))
            scene studying_swimming_2_bg
            show studying_swimming_2_wdis
            show studying_swimming_2_hero
            with dissolve
            $ add_stat("wdis", "lust", 3)

        elif a_event_0 == "wota":
            $ msg.msg(renpy.translate_string("Oops, you accidentally touched something!"))
            scene studying_swimming_2_bg
            show studying_swimming_2_wota
            show studying_swimming_2_hero
            with dissolve
            $ add_stat("wota", "lust", 3)

        elif a_event_0 == "wpre":
            $ msg.msg(renpy.translate_string("Oops, you accidentally touched something!"))
            scene studying_swimming_2_bg
            show studying_swimming_2_wpre
            show studying_swimming_2_hero
            with dissolve
            $ add_stat("wpre", "lust", 3)

        elif a_event_0 == "wgal":
            $ msg.msg(renpy.translate_string("Oops, you accidentally touched something!"))
            scene studying_swimming_2_bg
            show studying_swimming_2_wgal
            show studying_swimming_2_hero
            with dissolve
            $ add_stat("wgal", "lust", 3)

        else:
            scene studying_swimming_bg
            if renpy.random.random() < 0.5:
                show studying_swimming_hero backstroke
            else:
                show studying_swimming_hero crawl
            with dissolve
            $ add_stat("hero", "phy", a_event_2 * 0.5, stat_mod=False)

        pause
        return

    # ----------------------------------------------------------------------------------------------------
    label action_study_class_socialization: # Socialization
    # ----------------------------------------------------------------------------------------------------
        $ a_event_0 = []

        if wpre_quest_1 >= 1:
            $ a_event_0.append("wpre")
        if wdis_quest_1 >= 1:
            $ a_event_0.append("wdis")
        if wota_quest_1 >= 1:
            $ a_event_0.append("wota")
        if wgal_quest_1 >= 1:
            $ a_event_0.append("wgal")
        if wric_quest_1 >= 1:
            $ a_event_0.append("wric")
        if wuza_quest_1 >= 1:
            $ a_event_0.append("wuza")
        if hine_quest_1 >= 1:
            $ a_event_0.append("hine")
        if wgot_quest_1 >= 1:
            $ a_event_0.append("wgot")

        if a_event_0:
            $ a_event_0 = renpy.random.choice(a_event_0)
            scene socializing_class_bg classroom
        else:
            $ a_event_0 = None

        if a_event_0 == "wpre":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewpre]{/nm}"))
            $ add_stat("wpre", "inti", a_event_2)
            $ add_stat("wpre", "love", a_event_2)
            show socializing_class_hero learning
            show socializing_class_wpre

        elif a_event_0 == "wdis":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewdis]{/nm}"))
            $ add_stat("wdis", "inti", a_event_2)
            $ add_stat("wdis", "love", a_event_2)
            show socializing_class_wdis
            show socializing_class_hero teaching

        elif a_event_0 == "wota":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewota]{/nm}"))
            $ add_stat("wota", "inti", a_event_2)
            $ add_stat("wota", "love", a_event_2)
            show socializing_class_hero learning
            show socializing_class_wota

        elif a_event_0 == "wgal":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewgal]{/nm}"))
            $ add_stat("wgal", "inti", a_event_2)
            $ add_stat("wgal", "love", a_event_2)
            show socializing_class_hero base
            show socializing_class_hero_face a1
            show socializing_class_wgal

        elif a_event_0 == "wric":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewric]{/nm}"))
            $ add_stat("wric", "inti", a_event_2)
            $ add_stat("wric", "love", a_event_2)
            show socializing_class_hero base
            show socializing_class_hero_face a0
            show socializing_class_wric

        elif a_event_0 == "wgot":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewgot]{/nm}"))
            $ add_stat("wgot", "inti", a_event_2)
            $ add_stat("wgot", "love", a_event_2)

            $ X_pos = 500
            show socializing_class_hero base
            show socializing_class_hero_face a1
            show circletable_wgot at X

        elif a_event_0 == "wuza":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewuza]{/nm}"))
            $ add_stat("wuza", "inti", a_event_2)
            $ add_stat("wuza", "love", a_event_2)
            show socializing_class_wuza
            show socializing_class_hero teaching

        elif a_event_0 == "hine":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamehine]{/nm}"))
            $ add_stat("hine", "inti", a_event_2)
            $ add_stat("hine", "love", a_event_2)
            show socializing_class_hero learning
            show socializing_class_hine

        else:
            $ msg.msg(renpy.translate_string("You felt like you weren't familiar with anyone in your class yet, so you decided to study alone"))
            jump action_study_start

        $ add_stat("hero", "int", a_event_2)

        if a_event_0:
            show socializing_class_fg classroom
            with dissolve

        pause
        return

    # ----------------------------------------------------------------------------------------------------
    label action_study_swimming_socialization: # Socialization
    # ----------------------------------------------------------------------------------------------------
        $ a_event_0 = []
        if wpre_quest_1 >= 1:
            $ a_event_0.append("wpre")
        if wdis_quest_1 >= 1:
            $ a_event_0.append("wdis")
        if wota_quest_1 >= 1:
            $ a_event_0.append("wota")
        if wgal_quest_1 >= 1:
            $ a_event_0.append("wgal")
        if wric_quest_1 >= 1:
            $ a_event_0.append("wric")
        if wgot_quest_1 >= 1:
            $ a_event_0.append("wgot")
        if wuza_quest_1 >= 1:
            $ a_event_0.append("wuza")
        if wdel_quest_1 >= 1:
            $ a_event_0.append("wdel")
        if wlaz_quest_1 >= 1:
            $ a_event_0.append("wlaz")
        if hprv_quest_1 >= 1:
            $ a_event_0.append("hprv")
        if hine_quest_1 >= 1:
            $ a_event_0.append("hine")

        $ a_event_0 = renpy.random.choice(a_event_0)

        scene socializing_pool_bg 1
        if a_event_0 == "wpre":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewpre]{/nm}"))
            $ add_stat("wpre", "inti", a_event_2)
            $ add_stat("wpre", "love", a_event_2)
            show socializing_pool_hero talking
            show socializing_pool_wpre
            with dissolve
        elif a_event_0 == "wdis":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewdis]{/nm}"))
            $ add_stat("wdis", "inti", a_event_2)
            $ add_stat("wdis", "love", a_event_2)
            show socializing_pool_hero embarrassed
            show socializing_pool_wdis
            with dissolve
        elif a_event_0 == "wota":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewota]{/nm}"))
            $ add_stat("wota", "inti", a_event_2)
            $ add_stat("wota", "love", a_event_2)
            show socializing_pool_hero listening
            show socializing_pool_wota
            with dissolve
        elif a_event_0 == "wgal":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewgal]{/nm}"))
            $ add_stat("wgal", "inti", a_event_2)
            $ add_stat("wgal", "love", a_event_2)
            if (wgal_love >= 20) or (wgal_inti >= 5):
                show socializing_pool_hero listening
                show socializing_pool_wgal 1
                with dissolve
            else:
                show socializing_pool_hero awkward
                show socializing_pool_wgal 0
                with dissolve
        elif a_event_0 == "wric":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewric]{/nm}"))
            $ add_stat("wric", "inti", a_event_2)
            $ add_stat("wric", "love", a_event_2)
            if (wric_love >= 20) or (wric_inti >= 5):
                show socializing_pool_hero listening
                show socializing_pool_wric 1
                with dissolve
            else:
                show socializing_pool_hero awkward
                show socializing_pool_wric 0
                with dissolve
        elif a_event_0 == "wgot":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewgot]{/nm}"))
            $ add_stat("wgot", "inti", a_event_2)
            $ add_stat("wgot", "love", a_event_2)
            show socializing_pool_hero listening
            show socializing_pool_wgot
            with dissolve
        elif a_event_0 == "wlaz":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewlaz]{/nm}"))
            $ add_stat("wlaz", "inti", a_event_2)
            $ add_stat("wlaz", "love", a_event_2)
            show socializing_pool_wlaz
            show socializing_pool_hero talking
            with dissolve
        elif a_event_0 == "wdel":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewdel]{/nm}"))
            $ add_stat("wdel", "inti", a_event_2)
            $ add_stat("wdel", "love", a_event_2)
            show socializing_pool_hero awkward
            show socializing_pool_wdel
            with dissolve
        elif a_event_0 == "wuza":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamewuza]{/nm}"))
            $ add_stat("wuza", "inti", a_event_2)
            $ add_stat("wuza", "love", a_event_2)
            show socializing_pool_wuza
            show socializing_pool_hero listening
            with dissolve
        elif a_event_0 == "hprv":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamehprv]{/nm}"))
            $ add_stat("hprv", "inti", a_event_2)
            $ add_stat("hprv", "love", a_event_2)
            show socializing_pool_hero listening
            show socializing_pool_hprv
            with dissolve
        elif a_event_0 == "hine":
            $ msg.msg(renpy.translate_string("You chat with {nm}[fnamehine]{/nm}"))
            $ add_stat("hine", "inti", a_event_2)
            $ add_stat("hine", "love", a_event_2)
            show socializing_pool_hero talking
            show socializing_pool_hine
            with dissolve
        else:
            scene studying_swimming_bg
            if renpy.random.random() < 0.5:
                show studying_swimming_hero backstroke
            else:
                show studying_swimming_hero crawl
            with dissolve
            $ add_stat("hero", "phy", a_event_2 * 0.5, stat_mod=False)

        $ add_stat("hero", "cha_soc", a_event_2)

        pause
        return

    # ----------------------------------------------------------------------------------------------------
    label action_jog_sportcourt: # Jogging Scene
    # ----------------------------------------------------------------------------------------------------
        $ a_event_0 = []
        if wpre_quest_1 >= 1:
            $ a_event_0.append("wpre")
        if wdis_quest_1 >= 1:
            $ a_event_0.append("wdis")
        if wota_quest_1 >= 1:
            $ a_event_0.append("wota")
        if wgal_quest_1 >= 1:
            $ a_event_0.append("wgal")
        if wric_quest_1 >= 1:
            $ a_event_0.append("wric")
        if wgot_quest_1 >= 1:
            $ a_event_0.append("wgot")
        if wuza_quest_1 >= 1:
            $ a_event_0.append("wuza")
        if wdel_quest_1 >= 1:
            $ a_event_0.append("wdel")
        if wlaz_quest_1 >= 1:
            $ a_event_0.append("wlaz")
        if hprv_quest_1 >= 1:
            $ a_event_0.append("hprv")
        if hine_quest_1 >= 1:
            $ a_event_0.append("hine")

        python:
            # HERO socializes with a random handful of the already-unlocked joggers.
            # Roll 1-3: `result` is BOTH how many characters share the jog AND the divisor, so the total attention (a_event_2) is split evenly among them (1 partner -> full gain each; 3 partners -> a third each).
            if a_event_0:
                result = renpy.random.randint(1, 3)
                result = min(result, len(a_event_0))
                jog_partners = renpy.random.sample(a_event_0, result)
                names = []
                for char in jog_partners:
                    add_stat(char, "inti", a_event_2 / result)
                    add_stat(char, "love", a_event_2 / result)
                    names.append("{nm}" + (getattr(store, "fname" + char, None) or char) + "{/nm}")
                msg.msg(renpy.translate_string("You jog with ") + renpy.translate_string(str(", ".join(names))))

        # BG
        scene bg_sky1
        show action_jog_bg sportcourt at SXY(1, 0.5, 0.5)

        # 12 jogger slots, ordered back-to-front (ascending scale) so they layer correctly.
        # WLAZ (slot 4) and HERO (slot 12) are pinned; the other 10 characters are shuffled into the remaining slots so the crowd lands in random spots each time this runs.
        python:
            _jog_slots = [
                (0.06, 0.25, 0.3, None),    # 1
                (0.1, 0.1, 0.3, None),      # 2
                (0.14, 0.3, 0.3, None),     # 3
                (0.17, 0.5, 0.13, "wlaz"),  # 4: fixed WLAZ
                (0.18, -0.05, 0.3, None),   # 5
                (0.26, 0.9, 0.3, None),     # 6
                (0.30, 0.5, 0.3, None),     # 7
                (0.34, -0.02, 0.3, None),     # 8
                (0.38, 1.2, 0.3, None),     # 9
                (0.42, 0.85, 0.3, None),    # 10
                (0.5, (renpy.random.randint(0, 4) * 0.1), 0.7, None),        # 11
                (0.6, (renpy.random.randint(6, 10) * 0.1), 1, "hero"),      # 12: fixed HERO
            ]
            _jog_chars = ["wdel", "hine", "wdis", "wric", "wpre", "wgot", "hprv", "wgal", "wota", "wuza"]
            renpy.random.shuffle(_jog_chars)
            _ci = 0
            for _s, _x, _y, _fixed in _jog_slots:
                if _fixed:
                    _char = _fixed
                else:
                    _char = _jog_chars[_ci]
                    _ci += 1
                renpy.show("action_jog_" + _char + "_1_body", at_list=[SXY(_s, _x, _y)])
                renpy.show("action_jog_" + _char + "_1_wear sport", at_list=[SXY(_s, _x, _y)])
        show fx_light

        pause
        return


    # ----------------------------------------------------------------------------------------------------
    label action_study_jogging_socialization: # Socialization
    # ----------------------------------------------------------------------------------------------------
        $ a_event_0 = []
        if wpre_quest_1 >= 1:
            $ a_event_0.append("wpre")
        if wdis_quest_1 >= 1:
            $ a_event_0.append("wdis")
        if wota_quest_1 >= 1:
            $ a_event_0.append("wota")
        if wgal_quest_1 >= 1:
            $ a_event_0.append("wgal")
        if wric_quest_1 >= 1:
            $ a_event_0.append("wric")
        if wgot_quest_1 >= 1:
            $ a_event_0.append("wgot")
        if wuza_quest_1 >= 1:
            $ a_event_0.append("wuza")
        if wdel_quest_1 >= 1:
            $ a_event_0.append("wdel")
        if wlaz_quest_1 >= 1:
            $ a_event_0.append("wlaz")
        if hprv_quest_1 >= 1:
            $ a_event_0.append("hprv")
        if hine_quest_1 >= 1:
            $ a_event_0.append("hine")

        $ a_event_0 = renpy.random.choice(a_event_0)

        scene socializing_jogging_bg sportcourt
        show socializing_jogging_hero_body 1
        show socializing_jogging_hero_face 1a0
        show socializing_jogging_hero_wear 1_school_sport
        if a_event_0 == "wpre":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamewpre]{/nm}"))
            $ add_stat("wpre", "inti", a_event_2)
            $ add_stat("wpre", "love", a_event_2)
            show socializing_jogging_wpre_body 1
            show socializing_jogging_wpre_wear 1_school_sport
            with dissolve
        elif a_event_0 == "wdis":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamewdis]{/nm}"))
            $ add_stat("wdis", "inti", a_event_2)
            $ add_stat("wdis", "love", a_event_2)
            show socializing_jogging_wdis_body 1
            show socializing_jogging_wdis_wear 1_school_sport
            with dissolve
        elif a_event_0 == "wota":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamewota]{/nm}"))
            $ add_stat("wota", "inti", a_event_2)
            $ add_stat("wota", "love", a_event_2)
            show socializing_jogging_wota_body 1
            show socializing_jogging_wota_wear 1_school_sport
            with dissolve
        elif a_event_0 == "wgal":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamewgal]{/nm}"))
            $ add_stat("wgal", "inti", a_event_2)
            $ add_stat("wgal", "love", a_event_2)
            show socializing_jogging_wgal_body 1
            show socializing_jogging_wgal_wear 1_school_sport
            with dissolve
        elif a_event_0 == "wric":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamewric]{/nm}"))
            $ add_stat("wric", "inti", a_event_2)
            $ add_stat("wric", "love", a_event_2)
            show socializing_jogging_wric_body 1
            show socializing_jogging_wric_wear 1_school_sport
            with dissolve
        elif a_event_0 == "wgot":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamewgot]{/nm}"))
            $ add_stat("wgot", "inti", a_event_2)
            $ add_stat("wgot", "love", a_event_2)
            show socializing_jogging_wgot_body 1
            show socializing_jogging_wgot_wear 1_school_sport
            with dissolve
        elif a_event_0 == "wuza":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamewuza]{/nm}"))
            $ add_stat("wuza", "inti", a_event_2)
            $ add_stat("wuza", "love", a_event_2)
            show socializing_jogging_wuza_body 1
            show socializing_jogging_wuza_wear 1_school_sport
            with dissolve
        elif a_event_0 == "wdel":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamewdel]{/nm}"))
            $ add_stat("wdel", "inti", a_event_2)
            $ add_stat("wdel", "love", a_event_2)
            show socializing_jogging_wdel_body 1
            show socializing_jogging_wdel_wear 1_school_sport
            with dissolve
        elif a_event_0 == "wlaz":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamewlaz]{/nm}"))
            $ add_stat("wlaz", "inti", a_event_2)
            $ add_stat("wlaz", "love", a_event_2)
            show socializing_jogging_wlaz_body 1
            show socializing_jogging_wlaz_wear 1_school_sport
            with dissolve
        elif a_event_0 == "hprv":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamehprv]{/nm}"))
            $ add_stat("hprv", "inti", a_event_2)
            $ add_stat("hprv", "love", a_event_2)
            show socializing_jogging_hprv_body 1
            show socializing_jogging_hprv_wear 1_school_sport
            with dissolve
        elif a_event_0 == "hine":
            $ msg.msg(renpy.translate_string("You jog with {nm}[fnamehine]{/nm}"))
            $ add_stat("hine", "inti", a_event_2)
            $ add_stat("hine", "love", a_event_2)
            show socializing_jogging_hine_body 1
            show socializing_jogging_hine_wear 1_school_sport
            with dissolve
        else:
            $ add_stat("hero", "phy", a_event_2 * 0.5, stat_mod=False)

        $ add_stat("hero", "cha_soc", a_event_2)

        pause
        return

# ----------------------------------------------------------------------------------------------------
screen bg_map_hero():
# ----------------------------------------------------------------------------------------------------
    image "images/BG/bg_map_hero.webp" at Zoom_05

# ----------------------------------------------------------------------------------------------------
screen bg_map_wnei():
# ----------------------------------------------------------------------------------------------------
    image "images/BG/bg_map_wnei.webp" at Zoom_05

# ----------------------------------------------------------------------------------------------------
screen bg_map_office():
# ----------------------------------------------------------------------------------------------------
    image "images/BG/bg_map_office.webp" at Zoom_05

# ----------------------------------------------------------------------------------------------------
screen bg_map_school():
# ----------------------------------------------------------------------------------------------------
    image "images/BG/bg_map_school.webp" at Zoom_05

# ----------------------------------------------------------------------------------------------------
screen bg_map_store():
# ----------------------------------------------------------------------------------------------------
    image "images/BG/bg_map_store.webp" at Zoom_05

# ----------------------------------------------------------------------------------------------------
screen action_map():
# ----------------------------------------------------------------------------------------------------
    frame:
        background Color("#000000BF")
        xysize(500,1080)
        button:
            xysize(500,1080)
            hovered [
                SetVariable("a_event_1", 0.5),
                SetVariable("a_event_2", 0.5),
                #SetVariable("a_event_3", 0),
                #SetVariable("a_event_4", 0),
                Jump("action_map_open")
            ]
            action None
        vbox:
            xpos 25
            ypos 25
            label renpy.translate_string("{size=40}{b}[rnamecity]{/b}{/size}")

            text renpy.translate_string("{pr}")

            # HOME
            if hero_map != "Home - Facade":
                textbutton renpy.translate_string("Home") hovered [
                    Show("bg_map_hero"),
                    Hide("bg_map_wnei"),
                    Hide("bg_map_school"),
                    Hide("bg_map_office"),
                    Hide("bg_map_store"),
                    SetVariable("a_event_1", 0.5),
                    SetVariable("a_event_2", 0.5),
                    SetVariable("a_event_3", 0),
                    SetVariable("a_event_4", 0),
                    Jump("action_map_open"),
                ] action Jump("action_map_hero")
            else:
                textbutton renpy.translate_string("Home") hovered [
                    Show("bg_map_hero"),
                    Hide("bg_map_wnei"),
                    Hide("bg_map_school"),
                    Hide("bg_map_office"),
                    Hide("bg_map_store"),
                    SetVariable("a_event_1", 0.5),
                    SetVariable("a_event_2", 0.5),
                    SetVariable("a_event_3", 0),
                    SetVariable("a_event_4", 0),
                    Jump("action_map_open"),
                ] action None

            # SCHOOL
            if gametimehour <= 17 and not hero_map == "School - Facade" and (gametimeweek != "Sunday" and gametimeweek != "Saturday"):
                textbutton renpy.translate_string("School") hovered [
                    Show("bg_map_school"),
                    Hide("bg_map_hero"),
                    Hide("bg_map_wnei"),
                    Hide("bg_map_office"),
                    Hide("bg_map_store"),
                    SetVariable("a_event_1", 0.5),
                    SetVariable("a_event_2", 0.5),
                    SetVariable("a_event_3", 0),
                    SetVariable("a_event_4", 0),
                    Jump("action_map_open")
                ] action Jump("action_map_school")
            else:
                textbutton renpy.translate_string("School") hovered [
                    Show("bg_map_school"),
                    Hide("bg_map_hero"),
                    Hide("bg_map_wnei"),
                    Hide("bg_map_office"),
                    Hide("bg_map_store"),
                    SetVariable("a_event_1", 0.5),
                    SetVariable("a_event_2", 0.5),
                    SetVariable("a_event_3", 0),
                    SetVariable("a_event_4", 0),
                    Jump("action_map_open")
                ] action None

            # OFFICE
            if (hero_quest_2 < 4 or hero_quest_3 >= 2):
                if gametimehour >= 18 and not hero_map == "Office Building - Facade" and (gametimeweek != "Sunday" and gametimeweek != "Saturday"):
                    textbutton renpy.translate_string("{nm}[fnamewcou]{/nm}'s Office") hovered [
                        Show("bg_map_office"),
                        Hide("bg_map_hero"),
                        Hide("bg_map_wnei"),
                        Hide("bg_map_school"),
                        Hide("bg_map_store"),
                        SetVariable("a_event_1", 0.5),
                        SetVariable("a_event_2", 0.5),
                        SetVariable("a_event_3", 0),
                        SetVariable("a_event_4", 0),
                        Jump("action_map_open")
                    ] action Jump("action_map_office")
                else:
                    textbutton renpy.translate_string("{nm}[fnamewcou]{/nm}'s Office") hovered [
                        Show("bg_map_office"),
                        Hide("bg_map_hero"),
                        Hide("bg_map_wnei"),
                        Hide("bg_map_school"),
                        Hide("bg_map_store"),
                        SetVariable("a_event_1", 0.5),
                        SetVariable("a_event_2", 0.5),
                        SetVariable("a_event_3", 0),
                        SetVariable("a_event_4", 0),
                        Jump("action_map_open")
                    ] action None

            # SHOPPING MALL
            if gametimehour <= 18:
                textbutton renpy.translate_string("Camel Store") hovered [
                    Show("bg_map_store"),
                    Hide("bg_map_hero"),
                    Hide("bg_map_wnei"),
                    Hide("bg_map_school"),
                    Hide("bg_map_office"),
                    SetVariable("a_event_1", 0.5),
                    SetVariable("a_event_2", 0.5),
                    SetVariable("a_event_3", 0),
                    SetVariable("a_event_4", 0),
                    Jump("action_map_open")
                ] action Jump("action_map_store")
            else:
                textbutton renpy.translate_string("Camel Store") hovered [
                    Show("bg_map_store"),
                    Hide("bg_map_hero"),
                    Hide("bg_map_wnei"),
                    Hide("bg_map_school"),
                    Hide("bg_map_office"),
                    SetVariable("a_event_1", 0.5),
                    SetVariable("a_event_2", 0.5),
                    SetVariable("a_event_3", 0),
                    SetVariable("a_event_4", 0),
                    Jump("action_map_open")
                ] action None

            text renpy.translate_string("{pr}")

            textbutton renpy.translate_string("Return") hovered [
                Hide("bg_map_hero"),
                Hide("bg_map_wnei"),
                Hide("bg_map_store"),
                Hide("bg_map_school"),
                Hide("bg_map_office"),
                SetVariable("a_event_1", 0.5),
                SetVariable("a_event_2", 0.5),
                SetVariable("a_event_3", 0),
                SetVariable("a_event_4", 0),
                Jump("action_map_open")
            ] action [
                Jump("show_ui")
            ]

# ----------------------------------------------------------------------------------------------------
label action_map:
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_112

    $ a_event_1 = 0.5
    $ a_event_2 = 0
    $ a_event_3 = 0
    $ a_event_4 = 0

    if preferences.citymap == False:
        menu:
            "Home" if not hero_map == "Home - Facade":
                label action_map_hero:
                    $ hero_wear = Wear_Available("hero", "home")
                    call goto_home_facade from _call_goto_home_facade
            "School" if gametimehour <= 17 and not hero_map == "School - Facade":
                label action_map_school:
                    $ hero_wear = "school"
                    call goto_school_facade from _call_goto_school_facade
            "{nm}[fnamewcou]{/nm}'s Office" if gametimehour >= 18 and not hero_map == "Office Building - Facade" and (hero_quest_2 < 4 or hero_quest_3 >= 2) and (gametimeweek != "Sunday" and gametimeweek != "Saturday"):
                label action_map_office:
                    # Home clothes in the wash: he goes to the office in the uniform rather than in a towel.
                    $ hero_wear = Wear_Available("hero", "home")
                    if hero_wear == "towel":
                        $ hero_wear = "school"
                    call goto_office_facade from _call_goto_office_facade
            "Camel Store" if gametimehour <= 18:
                label action_map_store:
                    scene bg_grocerystore
                    #$ a_item_5 = "show_ui"
                    call screen UI_Menu_Inventory_Shop()
            "Return":
                pass

    else:

        label action_map_open:
            $ zoomS2 = a_event_1
            $ zoomT2 = a_event_2
            $ zoomX2 = a_event_3
            $ zoomY2 = a_event_4

            $ zoomS1 = zoomS2
            $ zoomT1 = 0
            $ zoomX1 = zoomX2
            $ zoomY1 = zoomY2
            show bg_map at ZoomSTXY
            call screen action_map
            $ ui.interact()

        label action_map_close:
            jump show_ui

    jump show_ui

# ----------------------------------------------------------------------------------------------------
label test_vendormachine:
# ----------------------------------------------------------------------------------------------------
    $ a_event_0 = renpy.random.choice([1,2,3,4,5,6])

    if a_event_0 == 1:
        $ item_id.remove("Drink_JuiceGrape")
        $ item_id.insert(0,"Drink_JuiceGrape")
        $ inventory.append("Drink_JuiceGrape")
    elif a_event_0 == 2:
        $ item_id.remove("Drink_JuiceGuarana")
        $ item_id.insert(0,"Drink_JuiceGuarana")
        $ inventory.append("Drink_JuiceGuarana")
    elif a_event_0 == 3:
        $ item_id.remove("Drink_JuiceOrange")
        $ item_id.insert(0,"Drink_JuiceOrange")
        $ inventory.append("Drink_JuiceOrange")
    elif a_event_0 == 4:
        $ item_id.remove("Drink_SodaGrape")
        $ item_id.insert(0,"Drink_SodaGrape")
        $ inventory.append("Drink_SodaGrape")
    elif a_event_0 == 5:
        $ item_id.remove("Drink_SodaGuarana")
        $ item_id.insert(0,"Drink_SodaGuarana")
        $ inventory.append("Drink_SodaGuarana")
    else:
        $ item_id.remove("Drink_SodaOrange")
        $ item_id.insert(0,"Drink_SodaOrange")
        $ inventory.append("Drink_SodaOrange")

    jump UI_show_Item

# ----------------------------------------------------------------------------------------------------
label action_lock:
# ----------------------------------------------------------------------------------------------------
    play SE1 "DoorLock.mp3"
    if hero_lock == False:
        $ hero_lock = True
        $ msg.msg(renpy.translate_string("The door is locked."))
    elif hero_lock == True:
        $ hero_lock = False
        $ msg.msg(renpy.translate_string("The door is unlocked."))
    return

# ----------------------------------------------------------------------------------------------------
label action_bathe_oops_1:
# ----------------------------------------------------------------------------------------------------
    stop BGM fadeout 1

    scene showering_2_bg
    show showering_2_door 1
    show showering_2_mg 0
    if wnei_map == hero_map and wsis_map == hero_map:
        show showering_2_wnei
        show showering_2_wnei_face o0
    if wnei_map == hero_map and wsis_map != hero_map:
        show showering_2_wnei_body 1
        if gametimehour < 8 or gametimehour >= 21:
            show showering_2_wnei_outfit underwear 1
            show showering_2_wnei_mouth o0
            show showering_2_wnei_eyes 0
        else:
            show showering_2_wnei_outfit common 1
            show showering_2_wnei_mouth a0
            show showering_2_wnei_eyes 1
    if wsis_map == hero_map:
        show showering_2_wsis
        show showering_2_wsis_face s0
    if wsis_map == hero_map and wnei_map == hero_map:
        show showering_2_wnei_fingers
    show showering_2_fg
    show showering_2_hero
    with Dissolve(1)

    play SE1 "Wow1.mp3"

    # WSIS entered
    # ----------------------------------------------------------------------------------------------------
    if wsis_map == hero_map and wnei_map != hero_map:
        show showering_2_wsis
        show showering_2_wsis_face s1
        show showering_2_wsis_fx
        show showering_2_hero_fx

        pause(0.5)

        if (renpy.music.get_playing(channel="BGM") != "audio/W2C - Awkward.mp3"): 
            play BGM "audio/W2C - Awkward.mp3"

        pause

        hide showering_2_wsis_fx
        hide showering_2_hero_fx
        wsis "{aw}S{w=[wt1]}-sorry!!!{/aw}{w=[wt1]}{nw}"

        show showering_2_door 0
        hide showering_2_wsis
        hide showering_2_wsis_face
        hide showering_2_wnei_fingers
        play SE1 "DoorBam.ogg"

    # WSIS & WNEI entered
    # ----------------------------------------------------------------------------------------------------
    if wsis_map == hero_map and wnei_map == hero_map:
        show showering_2_wsis
        show showering_2_wsis_face s1
        show showering_2_wsis_fx
        show showering_2_wnei_face a0
        show showering_2_hero_fx

        pause(0.5)

        if (renpy.music.get_playing(channel="BGM") != "audio/W2C - Awkward.mp3"): 
            play BGM "audio/W2C - Awkward.mp3"

        pause

        hide showering_2_wsis_fx
        hide showering_2_hero_fx
        show showering_2_wnei_face a1
        wnei "Ohh{w=[wt2]}, {nm}[fnamehero]{/nm}{w=[wt2]}, Ya're already here!{w=[wt3]} We're joinin' ya-{w=[wt1]}{nw}"

        show showering_2_door 0
        hide showering_2_wnei
        hide showering_2_wnei_face
        hide showering_2_wsis
        hide showering_2_wsis_face
        hide showering_2_wnei_fingers
        play SE1 "DoorBam.ogg"

    # WNEI entered
    # ----------------------------------------------------------------------------------------------------
    if wsis_map != hero_map and wnei_map == hero_map:
        show showering_2_hero_fx

        pause(0.5)

        if (renpy.music.get_playing(channel="BGM") != "audio/W2C - Awkward.mp3"): 
            play BGM "audio/W2C - Awkward.mp3"

        pause

        hide showering_2_hero_fx
        if gametimehour < 8 or gametimehour >= 21:
            show showering_2_wnei_outfit underwear 1
            show showering_2_wnei_mouth o1
            show showering_2_wnei_eyes 0
            wnei "Hmm{w=[wt2]}, {nm}[fnamehero]{/nm}{w=[wt2]}, is that ya?{w=[wt3]} {bt}Waaa...{/bt}"

            show showering_2_door 0
            show showering_2_mg 1
            show showering_2_wnei_body 2
            show showering_2_wnei_outfit underwear 2
            show showering_2_wnei_face a2
            hide showering_2_wnei_mouth
            hide showering_2_wnei_eyes
            with Dissolve(1)

        else:
            show showering_2_wnei_outfit common 1
            show showering_2_wnei_mouth a1
            show showering_2_wnei_eyes 1
            wnei "Ohh{w=[wt2]}, {nm}[fnamehero]{/nm}{w=[wt2]}, Ya're here!{w=[wt3]} I'm glad you leave the door opened."

            show showering_2_door 0
            show showering_2_mg 1
            show showering_2_wnei_body 2
            show showering_2_wnei_outfit common 2
            show showering_2_wnei_face a2
            hide showering_2_wnei_mouth
            hide showering_2_wnei_eyes
            with Dissolve(1)

        pause

        show showering_2_wnei_face a3

        play SE1 "Phew1.mp3"
        pause(1.5)

        show showering_2_wnei_face a2

        pause

        hide showering_2_wnei_face
        show showering_2_door 1
        show showering_2_mg 0
        show showering_2_wnei_body 1

        if gametimehour < 8 or gametimehour >= 21:
            show showering_2_wnei_outfit underwear 1
            show showering_2_wnei_mouth o0
            show showering_2_wnei_eyes 0
            with Dissolve(1)

            show showering_2_wnei_mouth o1
            wnei "{bt}Good Night...{/bt}"

        else:
            show showering_2_wnei_outfit common 1
            show showering_2_wnei_mouth a0
            show showering_2_wnei_eyes 1
            with Dissolve(1)

            show showering_2_wnei_mouth a1
            wnei "You're my hero!{w=[wt2]} Good bath for ya!{w=[wt3]} Don't forget to wash everything properly!"

        show showering_2_door 0
        hide showering_2_wnei_body
        hide showering_2_wnei_outfit
        hide showering_2_wnei_mouth
        hide showering_2_wnei_eyes
        with dissolve
    
    $ msg.msg(renpy.translate_string("You couldn't take a peaceful bath this time."))

    pause

    jump action_bathe_end

#image action_bathing_fg = Movie(play="/images/Action/Bathing/action_bathing_fg.webm", loop=True)

image action_bathing_fg:
     "action_bathing_fg_1"
     0.1
     "action_bathing_fg_2"
     0.1
     "action_bathing_fg_3"
     0.1
     "action_bathing_fg_4"
     0.1
     "action_bathing_fg_5"
     0.1
     repeat

# ----------------------------------------------------------------------------------------------------
label action_bathe_oops_2:
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_113
    # Door is locked
    # ----------------------------------------------------------------------------------------------------
    if (map_lock_bathroom == True):
        mind "(It's occupied)"
        return

    # WSIS & WNEI entered
    # ----------------------------------------------------------------------------------------------------
    elif wsis_map == "Home - Bathroom" and wnei_map == "Home - Bathroom":
        scene showering_3_bg
        show showering_3_wsis_body
        show showering_3_wsis_face o0
        show showering_3_wnei_body
        show showering_3_wnei_face a0
        show showering_3_fx
        show showering_3_fg
        with Dissolve(1)
        play SE1 "Wow1.mp3"
        pause(1)

        if (renpy.music.get_playing(channel="BGM") != "audio/W2C - Awkward.mp3"): 
            play BGM "audio/W2C - Awkward.mp3"

        show showering_3_wsis_face s0
        show showering_3_wnei_face a1
        wnei "Ohh{w=[wt2]}, {nm}[fnamehero]{/nm}{w=[wt2]}, are ya cummin' to join us?{nw}"

        show showering_3_wnei_face a0
        menu:
            wnei "Ohh{w=[wt2]}, {nm}[fnamehero]{/nm}{w=[wt2]}, are ya cummin' to join us?{fast}"
            "Accept":
                scene showering_4_bg
                show showering_4_mg 0
                show showering_4_hero 1 at CC
                show showering_4_hero_face a0 at CC
                show showering_4_fg
                with dissolve

                show showering_4_hero 1 at RR_slow
                show showering_4_hero_face a1 at RR_slow
                hero "Sure!{w=[wt2]} I'm comin-{w=[wt1]}{nw}"

                $ add_stat("wsis", "lust", 1)
                $ add_stat("wsis", "love", -1)

                play SE1 "Hit1.ogg"
                $ X_spd = 0.1
                hide showering_4_hero_face
                show showering_4_hero 2 at CC_X

            "Refuse":
                scene showering_4_bg
                show showering_4_mg 1
                show showering_4_hero 3
                show showering_4_fg
                with dissolve

                play SE1 "DoorBam.ogg"
                hero "I{w=[wt1]}-I'm s{w=[wt1]}-sorry!"

    # WSIS entered
    # ----------------------------------------------------------------------------------------------------
    elif wsis_map == "Home - Bathroom":
        #scene showering_3_bg
        #show showering_3_wsis
        #show showering_3_fx
        #show showering_3_fg

        scene action_bathing_bg home_bathroom
        show action_bathing_wsis 1
        show action_bathing_fg
        show fx_light
        with Dissolve(1)
        
        play SE1 "Wow1.mp3"
        pause(1)

        if (renpy.music.get_playing(channel="BGM") != "audio/W2C - Awkward.mp3"): 
            play BGM "audio/W2C - Awkward.mp3"

        menu:
            "Compliment her body":
                scene showering_4_bg
                show showering_4_mg 0
                show showering_4_hero 1
                show showering_4_hero_face a0
                show showering_4_fg
                with dissolve

                show showering_4_hero 1
                show showering_4_hero_face a1

                $ a_event_0 = str(__(hero_to_wsis)[:4])
                hero "Wooow!{w=[wt2]} Nice ass, [a_event_0]-{nw}"

                $ add_stat("wsis", "lust", 1)
                $ add_stat("wsis", "love", -1)

                play SE1 "Hit1.ogg"
                hide showering_4_hero_face
                show showering_4_hero 2

            "Apologize and turn back":
                scene showering_4_bg
                show showering_4_mg 1
                show showering_4_hero 3
                show showering_4_fg
                with dissolve

                play SE1 "DoorBam.ogg"
                hero "I{w=[wt1]}-I'm s{w=[wt1]}-sorry!"

    pause

    $ map_lock_bathroom = True

    scene bg_0
    with Dissolve(2)

    jump show_ui

# ----------------------------------------------------------------------------------------------------
label action_locker_stalls: # Shower quest — open female-locker stall doors (club_stco_quest_1 == 1)
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_114

    # Assign the broken shower to a random stall (1-12) once, then keep it for the rest of the quest.
    if locker_shower_stall == 0:
        $ locker_shower_stall = renpy.random.randint(1, 12)

    python:
        _lf = Get_MapName(map_main="school", map_sub="locker_f")

        # Free any already-opened door whose girl has since finished her bath (openable again).
        _still = []
        for _g in locker_opened_girls:
            _ga = getattr(store, _g + "_activity_current", None)
            _gn = _ga[0] if isinstance(_ga, tuple) else _ga
            if getattr(store, _g + "_map", "") == _lf and _gn == "bathing":
                _still.append(_g)
        locker_opened_girls[:] = _still

        # Girls currently bathing in the female locker that haven't been opened yet.
        # Only girls with a bathing sprite ("action_bathing_<id> 1") can appear — no art, no stall option.
        _bathers = []
        for _g in NPC_IDS:
            if not _g.startswith("w"):
                continue
            if not renpy.has_image("action_bathing_" + _g + " 1", exact=True):
                continue
            if getattr(store, _g + "_map", "") != _lf:
                continue
            _ga = getattr(store, _g + "_activity_current", None)
            _gn = _ga[0] if isinstance(_ga, tuple) else _ga
            if _gn == "bathing" and _g not in locker_opened_girls:
                _bathers.append(_g)

        # Openable doors = the broken-shower stall + one per bather. Stall numbers are cosmetic for now (re-rolled each visit), distinct from each other and from the shower's fixed stall.
        _pool = [n for n in range(1, 13) if n != locker_shower_stall]
        renpy.random.shuffle(_pool)
        _doors = [(locker_shower_stall, "shower", None)]
        for _i, _g in enumerate(_bathers):
            _doors.append((_pool[_i], "girl", _g))
        _doors.sort(key=lambda d: d[0])

        # NOTE: in renpy.display_menu a value of None renders as an unselectable caption, so give Return a real value — it falls through both branches below to the final jump show_ui.
        _items = [("Open stall #" + str(_num), (_kind, _who)) for _num, _kind, _who in _doors]
        _items.append(("Return", ("return", None)))

    scene bg_school locker_f
    with Dissolve(1)

    $ _pick = renpy.display_menu(_items)

    if _pick is None:
        jump show_ui

    # ----- Wrong door: a girl is showering -----
    if _pick[0] == "girl":
        $ _g = _pick[1]
        $ _gname = getattr(store, "fname" + _g, _g)

        # A girl with a stall animation ("action_masturbate_bg school_locker_f <id>_1": WGAL, WOTA) is caught in it first
        $ _pre = "action_masturbate_bg school_locker_f " + _g + "_1"
        if renpy.has_image(_pre, exact=True):
            $ renpy.scene()
            $ renpy.show(_pre)
            with Dissolve(1)
            pause

        scene action_bathing_bg school_f_locker
        $ _img = "action_bathing_" + _g + " 1"
        if renpy.has_image(_img, exact=True):
            $ renpy.show(_img)
        show action_bathing_fg
        show fx_light
        with Dissolve(1)

        play SE1 "Wow1.mp3"

        pause(1)

        $ msg.msg(renpy.translate_string("You open the stall — [C_Nam]") + _gname + renpy.translate_string("[C_Off] is showering!"))

        # No reaction art yet: she's embarrassed, HERO apologizes, stats shift (love down, lust + inti up).
        $ add_stat(_g, "love", -2)
        $ add_stat(_g, "lust", 2)
        $ add_stat(_g, "inti", 1)
        $ hero_lust = min(100, hero_lust + 3)

        hero "S-Sorry!{w=[wt2]} Wrong door!"

        play SE1 "DoorBam.ogg"

        # Her door stays shut until she finishes her bath.
        $ locker_opened_girls.append(_g)

        scene bg_school locker_f
        with Dissolve(1)
        jump action_locker_stalls

    # ----- Right door: the broken shower -----
    elif _pick[0] == "shower":
        scene action_bathing_bg school_f_locker
        show fx_light

        mind "(There it is!){nw}"

        menu:

            mind "(There it is!){fast}"

            "Repair":
                $ msg.msg(renpy.translate_string("Broken shower found"))
                mind "(There it is!{w=[wt2]} Let me shut the valve and tighten this up{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.)"
                $ msg.msg(renpy.translate_string("Quest Complete"))
                mind "(There it is!{w=[wt2]} Let me shut the valve and tighten this up{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{fast} Done!{w=[wt2]} Time to report it back to the [C_Dat]Student Council[C_Off]!)"
                $ club_stco_quest_1 = 2
                $ hero_locker_f_access = False  # objective done — locker access ends

            "Return":
                return

    jump show_ui

# ----------------------------------------------------------------------------------------------------
label action_bathe:
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_115

    if stat_hyg >= 90:
        $ msg.msg(renpy.translate_string("You are already clean."))

    elif hero_map == "Home - Bathroom" and gametimehour in [8, 9, 10, 11] and gametimeday == 2:
        mind "(I don't have time for that...)"
        return

    elif gametimehour < 8 and gametimeday == 2:
        scene bg_0
        with Dissolve(1)
        pause(1)

        menu:
            "Take a quick bath":
                pass

            "Return":
                jump show_ui

    else:
        scene bg_0
        with Dissolve(1)
        pause(1)

        $ a_event_1 = round(5 + (10/(1+(stat_hyg*0.09))))
        $ a_event_2 = round(15 + (15/(1+(stat_hyg*0.14))))
        $ a_event_3 = round((5/(1+(stat_hyg*0.04)))/(1+(stat_int*0.04)), 2)
        $ a_event_4 = round((15/(1+(stat_hyg*0.05))), 2)
        $ a_event_5 = round((10/(1+(stat_hyg*0.09))), 2)

        menu:
            "Take a quick bath{pr}{color=#FFAF32}({image=images/UI/ICON_Time.webp}+[a_event_1]min)" if not is_specialevent:
                while a_event_1 > 10:
                    $ gametimemin += 10
                    $ a_event_1 -= 10
                    call gametime from _call_gametime_64
                    if (hero_lock == False) and (wsis_map == hero_map or wnei_map == hero_map):
                        jump action_bathe_oops_1
                $ gametimemin += a_event_1
                call gametime from _call_gametime_65

                if (hero_lock == False) and (wsis_map == hero_map or wnei_map == hero_map):
                    jump action_bathe_oops_1

            "Take a contemplative bath{pr}{color=#FFAF32}({image=images/UI/ICON_Time.webp}+[a_event_2]min, {image=images/UI/ICON_StatInt.webp}+[a_event_3])" if not is_specialevent:
                while a_event_2 > 10:
                    $ gametimemin += 10
                    $ a_event_2 -= 10
                    call gametime from _call_gametime_66
                    if (hero_lock == False) and (wsis_map == hero_map or wnei_map == hero_map):
                        jump action_bathe_oops_1
                $ gametimemin += a_event_2
                call gametime from _call_gametime_67

                if (hero_lock == False) and (wsis_map == hero_map or wnei_map == hero_map):
                    jump action_bathe_oops_1

                else:
                    $ add_stat("hero", "int", a_event_3, stat_mod=False)
                    scene showering_1_bg
                    show showering_1_hero contemplative
                    show showering_1_fg
                    with Dissolve(1)
                    pause

            "Take a relaxing bath{pr}{color=#FFAF32}({image=images/UI/ICON_Time.webp}+[a_event_2]min, {image=images/UI/ICON_StatCha.webp}+[a_event_4])" if not is_specialevent:
                while a_event_2 > 10:
                    $ gametimemin += 10
                    $ a_event_2 -= 10
                    call gametime from _call_gametime_68
                    if (hero_lock == False) and (wsis_map == hero_map or wnei_map == hero_map):
                        jump action_bathe_oops_1
                $ gametimemin += a_event_2
                call gametime from _call_gametime_69

                if (hero_lock == False) and (wsis_map == hero_map or wnei_map == hero_map):
                    jump action_bathe_oops_1

                else:
                    $ stat_cha_bonus += a_event_4
                    $ msg.msg(renpy.translate_string("[C_Pos]")+renpy.translate_string(str(str(a_event_4)))+renpy.translate_string("% bonus[C_Off] for CHA gaining"))
                    scene showering_1_bg
                    show showering_1_hero relaxing
                    show showering_1_fg
                    with Dissolve(1)
                    pause

            "Return":
                jump show_ui

# ----------------------------------------------------------------------------------------------------
label action_bathe_end:
# ----------------------------------------------------------------------------------------------------
    if wsis_map != "Home - Bathroom" and wnei_map == "Home - Bathroom":
        $ wnei_know.append("Needs_Pee_Y")
        if "Needs_Pee_N" in wnei_know:
            $ wnei_know.remove("Needs_Pee_N")
        $ wnei_map = wsis_map

    call gametime from _call_gametime_70
    $ stat_hyg = 100
    $ hero_needs[0] = True
    $ msg.msg(renpy.translate_string("You are clean."))

    if wsis_map == hero_map:
        scene bg_0 with dissolve
        wsis "Oh, finally!{w=[wt2]} Why do you have to take so long!?{w=[wt2]} {bt}Shoo! Shoo!{/bt}"

        $ hero_map = "Home - Hallway"
        play SE1 "DoorBam.ogg"

    jump show_ui

# ----------------------------------------------------------------------------------------------------
label action_eat(buceta=2):
# ----------------------------------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_116

    if Check_CharInMap("wmom", "home") and Get_ActivityName("wmom") != "eating":
        $ StartAct("wmom", ("eating", 10), True)
    if Check_CharInMap("wsis", "home") and Get_ActivityName("wsis") != "eating":
        $ StartAct("wsis", ("eating", 10), True)
    if Check_CharInMap("wnei", "home") and Get_ActivityName("wnei") != "eating":
        $ StartAct("wnei", ("eating", 10), True)

    if buceta == 1:
        if Check_CharInMap("hero", "home"):

            scene sitting_bg home_diningroom 1
            show sitting_mg home_diningroom

            if Check_CharInMap("wsis", "home") and Get_ActivityName("wsis") == "eating":
                show sitting_wsis_body 2 at LC
                if wsis_wear == "sleep":
                    show sitting_wsis_wear 2sleep at LC
                elif wsis_wear == "school":
                    show sitting_wsis_wear 2school_in at LC
                else:
                    show sitting_wsis_wear 2home at LC

            if Check_CharInMap("wmom", "home") and Get_ActivityName("wmom") == "eating":
                show sitting_wmom_body 2 at RC
                if wmom_wear == "sleep":
                    show sitting_wmom_wear 2sleep at RC
                elif wmom_wear == "casual":
                    show sitting_wmom_wear 2casual at RC
                else:
                    show sitting_wmom_wear 2home at RC
            show sitting_fg home_diningroom
            show fx_light:
                blend "add"
            with fade

            pause

            scene sitting_bg home_diningroom 2
            show sitting_mg home_diningroom
            if Check_CharInMap("wnei", "home") and Get_ActivityName("wnei") == "eating":
                show sitting_wnei_body 2 at LC
                if wnei_wear == "casual":
                    show sitting_wnei_wear 2sleep at LC
                elif wnei_wear == "school":
                    show sitting_wnei_wear 2school_in at LC
                else:
                    show sitting_wnei_wear 2home at LC

            # HERO
            show sitting_hero_body 2 at RC
            show sitting_hero_wear 2home at RC

            show sitting_fg home_diningroom
            show fx_light:
                blend "add"
            $ buceta = 3
            with fade

            pause

    if wsis_map == hero_map:
        $ add_stat("wsis", "inti", 1)
        $ wsis_eat = 100
    if wmom_map == hero_map:
        $ add_stat("wmom", "inti", 1)
        $ wmom_eat = 100
    if wnei_map == hero_map:
        $ add_stat("wnei", "inti", 1)
        $ wnei_eat = 100

    #hero "[inventory_home_table]{fast}"
    $ inventory_home_table.clear()
    $ stat_phy_bonus += 5
    $ msg.msg(renpy.translate_string("[C_Pos]5% bonus[C_Off] for PHY gaining"))
    $ stat_int_bonus += 5
    $ msg.msg(renpy.translate_string("[C_Pos]5% bonus[C_Off] for INT gaining"))
    #$ hero_needs[1] = True
    $ stat_eat = 100
    $ msg.msg(renpy.translate_string("You are satiated."))
    #hero "[inventory_home_table]{fast}"
    pause(1)

    $ gametimemin += 10

    jump show_ui


# ----------------------------------------------------------------------------------------------------
screen SkipScene():
# ----------------------------------------------------------------------------------------------------
    timer 0.1 repeat True action If(PercentData==100, true=[Jump(minigamestep), SetVariable("PercentAdd", 0), SetVariable("PercentData", 0)], false=(SetVariable("PercentData", max(0, min(100, PercentData + PercentAdd)))))

    key ["keydown_K_LCTRL", "keydown_K_RCTRL"] action SetVariable("PercentAdd", 10)
    key ["keyup_K_LCTRL", "keyup_K_RCTRL"] action [SetVariable("PercentAdd", 0), SetVariable("PercentData", 0)]

    if PercentAdd != 0:
        frame:
            background None
            xsize 150
            ysize 150
            align(1.0, 0.0)

            circular_bar:
                style "skipcirclebar"
                start_thumb "colorize:b3_base2_thumb|#f93c3e"
                hover_start_thumb "colorize:b3_base2_thumb|#FF8335"
                hide_start_thumb True
                value PercentData range 100
                align(0.5, 0.5)

            text renpy.translate_string("[PercentData]%") align(0.5, 0.5)

# ----------------------------------------------------------------------------------------------------
label action_walk(a="hero", b="wsis", c=15):
# ----------------------------------------------------------------------------------------------------
    if a == "hero":
        $ stat_hyg = round(max(0, stat_hyg - DIRT_MOVE), 2)   # 2.2c: crossing the streets is grimy
    scene bg_0
    if gametimehour < 15:
        show action_walk_bg_1 sky_morning
    elif gametimehour < 18:
        show action_walk_bg_1 sky_afternoon
    else:
        show action_walk_bg_1 sky_night
    show action_walk_bg street
    # Outfit layers go through Sit_Wear, so a walk layer for a new outfit (`action_walk_<char>_wear 1dressy` and friends, for a date) is picked up the day it is drawn and falls back to the old one until then.
    if a == "hero":
        show action_walk_hero_body 1
        if hero_wear == "school":
            show action_walk_hero_wear 1school
        else:
            show expression Sit_Wear("action_walk_hero_wear 1", "hero", "") as walk_hero_wear
    if b == "wsis":
        $ add_stat("wsis", "inti", (c/100))
        if wsis_inti >= 20 and wsis_love >= 20:
            show action_walk_wsis_body 2
            if hero_wear == "school":
                show action_walk_wsis_wear 2school
            else:
                show expression Sit_Wear("action_walk_wsis_wear 2", "wsis", "", "casual") as walk_wsis_wear
        else:
            show action_walk_wsis_body 1
            if hero_wear == "school":
                show action_walk_wsis_wear 1school
            else:
                show expression Sit_Wear("action_walk_wsis_wear 1", "wsis", "", "casual") as walk_wsis_wear
    with Fade(1, 0, 2)

    pause

    return

# ----------------------------------------------------------------------------------------------------
# Circletable Panorama View
# ----------------------------------------------------------------------------------------------------
init python:
# ----------------------------------------------------------------------------------------------------
    import pygame_sdl2 as pygame

    def Circle_Venue(venue): # Panorama scenery id, falling back to the courtyard until its art exists
    # --------------------------------------------------
        # The whole panorama is one naming family (`circletable_bg/mg/fg/fx <venue> ...`), so a new place is a set of files and nothing else. Until they are drawn the scene still runs, dressed as the courtyard.
        return venue if renpy.has_image("circletable_bg " + venue + " panorama2", exact=True) else "courtyard"

    # --------------------------------------------------
    def get_circletable_chars(char_id):
        test_char = ["wsis", "wnei", "wpre", "wdis", "wota", "wgal", "wric", "wlaz", "wdel", "wuza", "wgot", "hprv"]

        if char_id is None:
            chars = renpy.random.sample(test_char, 3)
            chars.insert(0, "hero")
        elif isinstance(char_id, list):
            chars = list(char_id)
        else:
            pool = [c for c in test_char if c != char_id]
            chars = renpy.random.sample(pool, 2)
            chars.insert(0, "hero")
            chars.append(char_id)

        return chars

    # --------------------------------------------------
    class CircleState: # Transient pan position (0-1 of one loop) the auto pan reports each frame; a class attribute, so it never reaches a save
        auto = 0.0

    def Circle_Track(trans, st, at): # ATL function riding along the auto pan, so the code knows where the 15s loop is
        CircleState.auto = (st % 15.0) / 15.0
        return 0

    def Circle_Pos(scope): # Current pan position of the screen, whatever the mode
        return CircleState.auto if scope["mode"] == "auto" else scope["manual_pos"]

    def Circle_Spot(chars, seen): # Pops the seat's line the first time its character reaches the middle of the screen
        _pos = Circle_Pos(renpy.current_screen().scope)
        _seat = int((_pos * 7680 + 960) // 1920) % 4
        if _seat >= len(chars) or chars[_seat] in seen:
            return
        _char = chars[_seat]
        seen.append(_char)
        if _char in CIRCLE_LINES:
            msg.msg(CIRCLE_LINES[_char])
        if _char != "hero":
            add_stat(_char, "inti", CIRCLE_INTI)
        renpy.restart_interaction()

    def Circle_ToggleMode(): # View button: manual mode starts where the auto pan was, so the picture doesn't jump
        _scope = renpy.current_screen().scope
        if _scope["mode"] == "auto":
            _scope["manual_pos"] = CircleState.auto
            _scope["mode"] = "manual"
        else:
            _scope["mode"] = "auto"
        _scope["touched"] = True
        renpy.restart_interaction()

    class CircleDrag(renpy.Displayable): # Invisible full-screen layer: dragging anywhere pans the table and switches to manual mode
        def __init__(self, **kwargs):
            super(CircleDrag, self).__init__(**kwargs)
            self.start = None # (mouse x, pan position) at press
            self.moving = False

        def render(self, width, height, st, at):
            return renpy.Render(width, height)

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and renpy.display.focus.get_grab() is None:
                self.start = (x, Circle_Pos(renpy.current_screen().scope))
                self.moving = False
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.start = None
            elif ev.type == pygame.MOUSEMOTION and self.start is not None:
                if not ev.buttons[0]:
                    self.start = None
                    return None
                _dx = x - self.start[0]
                if not self.moving and abs(_dx) < 8: # Dead zone, so a click on a button never turns into a drag
                    return None
                self.moving = True
                _scope = renpy.current_screen().scope
                _scope["mode"] = "manual"
                _scope["manual_pos"] = (self.start[1] - _dx / 7680.0) % 1.0
                _scope["touched"] = True
                renpy.restart_interaction()
                raise renpy.IgnoreEvent()
            return None

# Line popped when each character's seat reaches the middle of the screen (from the old round-by-round table scene).
define CIRCLE_LINES = {
    "hero": "And here you are!",
    "hprv": "Here is {nm}[fnamehprv]{/nm}, talking about completely a healthy and non-vulgar thing.",
    "wsis": "Here is {nm}[fnamewsis]{/nm}, but it's not like she likes your presence or anything, baka!",
    "wnei": "Here is {nm}[fnamewnei]{/nm}, drawing something super duper cool!",
    "wdis": "Here is {nm}[fnamewdis]{/nm}, trying to eat snacks without dropping any.",
    "wota": "Here is {nm}[fnamewota]{/nm}, catching up on her reading.",
    "wpre": "Here is {nm}[fnamewpre]{/nm}. Isn't she a sweetheart?",
    "wgal": "Here is {nm}[fnamewgal]{/nm}, who couldn't care less about your presence.",
    "wric": "Here is {nm}[fnamewric]{/nm}, sipping her delicious milkshake. You better not spill it this time!",
    "wgot": "Here is {nm}[fnamewgot]{/nm}, showing her elegance.",
    "wdel": "Here is {nm}[fnamewdel]{/nm}, behaving quite well, so far.",
    "wuza": "Here is {nm}[fnamewuza]{/nm}, recharging her energy!",
    "wlaz": "Here is {nm}[fnamewlaz]{/nm}, playing video game. You can't even say she noticed you're here.",
}
define CIRCLE_INTI = 1 # Intimacy each tablemate gives the first time she is seen

transform circletable_pan(offset):
    subpixel True
    anchor (0.0, 0.0)
    pos (offset, 0)
    linear 15 xpos (offset - 7680)
    repeat

transform circletable_static(xpos):
    subpixel True
    anchor (0.0, 0.0)
    pos (xpos, 0)

transform circletable_fx_crop_pan:
    crop (0, 0, 1920, 1080)
    linear 15 crop (5760, 0, 1920, 1080)
    repeat

transform circletable_track:
    function Circle_Track

transform circletable_blink:
    alpha 1.0
    linear 0.6 alpha 0.15
    linear 0.6 alpha 1.0
    repeat

screen circletable_view(chars, venue="courtyard"):
    default mode = "auto"
    default manual_pos = 0.0
    default touched = False
    default seen = []
    default v = Circle_Venue(venue)
    default drag = CircleDrag() # One instance for the whole screen: `add CircleDrag()` rebuilt it on every update and dropped the drag after one step

    if mode == "auto":
        add Null() at circletable_track

        # Background (tiled for seamless loop)
        add ("circletable_bg " + v + " panorama2") at circletable_pan(0)
        add ("circletable_bg " + v + " panorama2") at circletable_pan(7680)

        # Midground chairs (duplicated for wrap)
        for i in range(len(chars)):
            add ("circletable_mg " + v) at circletable_pan(i * 1920)
            add ("circletable_mg " + v) at circletable_pan(i * 1920 + 7680)

        # Characters (duplicated for wrap)
        for i, char in enumerate(chars):
            add ("circletable_" + char) at circletable_pan(i * 1920)
            add ("circletable_" + char) at circletable_pan(i * 1920 + 7680)

        # Static foreground + effect (cropped and synced)
        add Flatten(
            AlphaMask(
                Fixed(
                    ("circletable_fg " + v),
                    At(Transform(("circletable_fx " + v + " panorama"), blend="add"), circletable_fx_crop_pan),
                    fit_first=True
                ),
                ("circletable_fg " + v)
            )
        )

        # Panorama foreground + effect (masked and flattened)
        add Flatten(
            AlphaMask(
                Fixed(
                    ("circletable_fg " + v + " panorama"),
                    Transform(("circletable_fx " + v + " panorama"), blend="add"),
                    fit_first=True
                ),
                ("circletable_fg " + v + " panorama")
            )
        ) at circletable_pan(0)

        add Flatten(
            AlphaMask(
                Fixed(
                    ("circletable_fg " + v + " panorama"),
                    Transform(("circletable_fx " + v + " panorama"), blend="add"),
                    fit_first=True
                ),
                ("circletable_fg " + v + " panorama")
            )
        ) at circletable_pan(7680)

    else:
        # Manual mode - static positioning
        $ pan_x = int(-manual_pos * 7680)
        $ crop_x = int(manual_pos * 5760)

        # Background
        add ("circletable_bg " + v + " panorama2") at circletable_static(pan_x)
        add ("circletable_bg " + v + " panorama2") at circletable_static(pan_x + 7680)

        # Midground chairs
        for i in range(len(chars)):
            add ("circletable_mg " + v) at circletable_static(i * 1920 + pan_x)
            add ("circletable_mg " + v) at circletable_static(i * 1920 + pan_x + 7680)

        # Characters
        for i, char in enumerate(chars):
            add ("circletable_" + char) at circletable_static(i * 1920 + pan_x)
            add ("circletable_" + char) at circletable_static(i * 1920 + pan_x + 7680)

        # Static foreground + effect (cropped to visible area)
        add Flatten(
            AlphaMask(
                Fixed(
                    ("circletable_fg " + v),
                    Transform(("circletable_fx " + v + " panorama"), blend="add", crop=(crop_x, 0, 1920, 1080)),
                    fit_first=True
                ),
                ("circletable_fg " + v)
            )
        )

        # Panorama foreground + effect (masked and flattened)
        add Flatten(
            AlphaMask(
                Fixed(
                    ("circletable_fg " + v + " panorama"),
                    Transform(("circletable_fx " + v + " panorama"), blend="add"),
                    fit_first=True
                ),
                ("circletable_fg " + v + " panorama")
            )
        ) at circletable_static(pan_x)

        add Flatten(
            AlphaMask(
                Fixed(
                    ("circletable_fg " + v + " panorama"),
                    Transform(("circletable_fx " + v + " panorama"), blend="add"),
                    fit_first=True
                ),
                ("circletable_fg " + v + " panorama")
            )
        ) at circletable_static(pan_x + 7680)

    # Drag anywhere (below the bar and buttons, so they still get their clicks first)
    add drag

    timer 0.1 repeat True action Function(Circle_Spot, chars, seen)

    if not touched:
        text renpy.translate_string("< Drag The Screen >"):
            align (0.5, 0.5)
            size 60
            outlines [(4, "#000000", 0, 0)]
            at circletable_blink

    # Bar (manual mode) + buttons, on one row: the bar fills from the left margin up to the View button
    side "c r":
        xpos 50
        xsize 1720
        yalign 0.95
        spacing 50

        if mode == "manual":
            bar:
                value ScreenVariableValue("manual_pos", 1.0)
                ysize 30
                yalign 0.5
        else:
            null

        hbox:
            spacing 50
            yalign 0.5

            textbutton renpy.translate_string("View"):
                text_outlines [(3, "#000000", 0, 0)]
                action Function(Circle_ToggleMode)

            textbutton renpy.translate_string("Continue"):
                text_outlines [(3, "#000000", 0, 0)]
                action Return()

label circletable(char_id=None, venue="courtyard"):
    $ chars = get_circletable_chars(char_id)

    call screen circletable_view(chars, venue)

    return

# ----------------------------------------------------------------------------------------------------
label action_clean_home:
# ----------------------------------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_117

label action_chore_loop:
    # 2.7: Build all chore screen data
    python:
        # Room info
        _room_name = Get_MapName("hero", False)
        _room_clean = 0
        _is_facade = Check_CharInMap("hero", "home", "facade")
        if _is_facade:
            _room_clean = task_clean_home_facade
        elif Check_CharInMap("hero", "home", "living_room"):
            _room_clean = task_clean_home_living_room
        elif Check_CharInMap("hero", "home", "hallway"):
            _room_clean = task_clean_home_hallway
        elif Check_CharInMap("hero", "home", "bathroom"):
            _room_clean = task_clean_home_bathroom
        elif Check_CharInMap("hero", "home", "bedroom_hero"):
            _room_clean = task_clean_home_bedroom_hero
        elif Check_CharInMap("hero", "home", "bedroom_wsis"):
            _room_name = fnamewsis + "'s bedroom"
            _room_clean = task_clean_home_bedroom_wsis
        elif Check_CharInMap("hero", "home", "bedroom_wmom"):
            _room_name = fnamewmom + "'s bedroom"
            _room_clean = task_clean_home_bedroom_wmom

        _house_clean = Check_TaskCompletion("clean_home")
        _clothes_clean = Check_TaskCompletion("wash_home")

        # Can clean this area?
        _can_clean = (not _is_facade and _room_clean < 100)
        # Can throw trash?
        _can_trash = (_is_facade and _house_clean >= 85 and task_clean_home_facade < 100)
        _trash_blocked = (_is_facade and _house_clean < 85)

        # Laundry outfit data
        _laundry_chars = []
        _any_basket = False
        _any_washer = False
        _any_line = False
        _any_dry = False
        _cnt_basket = 0
        _collect_rooms = {"hero": "bedroom_hero", "wsis": "bedroom_wsis", "wmom": "bedroom_wmom"}
        for _cid, _cname in [("hero", fnamehero), ("wsis", fnamewsis), ("wmom", fnamewmom)]:
            _current_wear = getattr(store, _cid + "_wear", "")
            _in_bedroom = Check_CharInMap("hero", "home", _collect_rooms.get(_cid, ""))
            _char_outfits = []
            for _o in Outfits_For(_cid):
                _loc = getattr(store, "task_loc_" + _cid + "_" + _o, "wardrobe")
                _wash = getattr(store, "task_wash_" + _cid + "_" + _o, 100)
                _is_worn = (_o == _current_wear)
                # HERO may toss the outfit he is wearing too (the girls do the same on wash day): he wraps himself in a towel like they do.
                _can_collect = (_loc == "wardrobe" and _in_bedroom and (not _is_worn or _cid == "hero"))
                _char_outfits.append((_o, OUTFIT_NAMES.get(_o, _o), int(_wash), _loc, _is_worn, _can_collect))
                if _loc == "basket":
                    _any_basket = True
                    _cnt_basket += 1
                elif _loc == "washer": _any_washer = True
                elif _loc == "line": _any_line = True
                elif _loc == "dry": _any_dry = True
            _laundry_chars.append((_cid, _cname, _char_outfits))

        _wash_left = max(0, task_laundry_end - Get_MinuteTotal()) if task_laundry_end > 0 else 0
        _dry_left = max(0, task_dry_end - Get_MinuteTotal()) if task_dry_end > 0 else 0

    call screen UI_Chore(_room_name, int(_room_clean), int(_house_clean), int(_clothes_clean), _is_facade, _can_clean, _can_trash, _trash_blocked, _laundry_chars, _any_basket, _any_washer, _any_line, _any_dry, _cnt_basket, _wash_left, _dry_left)

    $ _result = _return

    # --- Close ---
    if _result[0] == "close":
        jump show_ui

    # --- Clean this area ---
    if _result[0] == "clean":
        $ _clean_time = 30 / ((1 + (perk_cha_per * 1)) + (1 + (stat_cha_per * 0.01)))
        python:
            _did_clean = False
            if Check_CharInMap("hero", "home", "living_room") and task_clean_home_living_room < 100:
                task_clean_home_living_room = 100
                _did_clean = True
            elif Check_CharInMap("hero", "home", "hallway") and task_clean_home_hallway < 100:
                task_clean_home_hallway = 100
                _did_clean = True
            elif Check_CharInMap("hero", "home", "bathroom") and task_clean_home_bathroom < 100:
                task_clean_home_bathroom = 100
                _did_clean = True
            elif Check_CharInMap("hero", "home", "bedroom_hero") and task_clean_home_bedroom_hero < 100:
                task_clean_home_bedroom_hero = 100
                _did_clean = True
            elif Check_CharInMap("hero", "home", "bedroom_wsis") and task_clean_home_bedroom_wsis < 100:
                task_clean_home_bedroom_wsis = 100
                _did_clean = True
            elif Check_CharInMap("hero", "home", "bedroom_wmom") and task_clean_home_bedroom_wmom < 100:
                task_clean_home_bedroom_wmom = 100
                _did_clean = True
        if _did_clean:
            $ gametimemin += _clean_time
            $ stat_hyg = round(max(0, stat_hyg - DIRT_CLEAN), 2)
            $ task_hero_clean_home += 10
            call gametime from _call_gametime_71
        else:
            $ msg.msg(renpy.translate_string("This area is already clean"))
        jump action_chore_loop

    # --- Throw the trash ---
    if _result[0] == "trash":
        if task_clean_home_facade >= 100:
            $ msg.msg(renpy.translate_string("The house is already clean!"))
        elif _house_clean >= 85:
            $ task_clean_home_facade = 100
            $ msg.msg(renpy.translate_string("The house is clean!"))
            $ task_hero_clean_home += 10
        else:
            $ msg.msg(renpy.translate_string("Clean all dirty areas in the house first"))
        jump action_chore_loop

    # --- Collect one outfit to basket ---
    if _result[0] == "collect":
        $ _cid = _result[1]
        $ _oid = _result[2]
        $ setattr(store, "task_loc_" + _cid + "_" + _oid, "basket")
        if _cid == "hero" and _oid == hero_wear:
            $ hero_wear = Wear_Available("hero", "home")
            $ msg.msg(renpy.translate_string("You toss what you were wearing in the basket and wrap yourself in a towel."))
        $ _collect_time = max(1, int(5.0 / (1.0 + (getattr(store, _cid + "_diligence", 50) * 0.04))))
        $ gametimemin += _collect_time
        $ stat_hyg = round(max(0, stat_hyg - DIRT_CLEAN), 2)
        $ task_hero_clean_home += 5
        call gametime from _call_gametime_72

        # 2.4: WSIS laundry scene — caught red-handed if she's in the room while you take ANY of her clothes; otherwise the quiet underwear flavor (gated on intimacy).
        if _cid == "wsis" and Check_CharSameMap("hero", "wsis"):
            jump action_clean_wsis_caught
        elif _cid == "wsis" and _oid == "under" and intimacy_tier("wsis") >= 1:
            $ msg.msg(renpy.translate_string("While collecting [C_Nam][fnamewsis][C_Off]'s clothes, you come across her underwear..."))
            $ hero_lust = min(100, hero_lust + 5)
            $ add_stat("wsis", "inti", 2)

        jump action_chore_loop

    # --- Load washer ---
    if _result[0] == "wash":
        python:
            for _cid in ["hero", "wsis", "wmom"]:
                for _o in Outfits_For(_cid):
                    _lv = "task_loc_" + _cid + "_" + _o
                    if getattr(store, _lv, "wardrobe") == "basket":
                        setattr(store, _lv, "washer")
            task_laundry_end = Get_MinuteTotal() + LAUNDRY_WASH_DUR
        $ gametimemin += 2
        $ task_hero_clean_home += 10
        call gametime from _call_gametime_73
        $ msg.msg(renpy.translate_string("You loaded the washing machine. It will be done in about ") + renpy.translate_string(str(str(LAUNDRY_WASH_DUR))) + renpy.translate_string(" minutes"))
        jump action_chore_loop

    # --- Hang clothes ---
    if _result[0] == "hang":
        python:
            for _cid in ["hero", "wsis", "wmom"]:
                for _o in Outfits_For(_cid):
                    _lv = "task_loc_" + _cid + "_" + _o
                    if getattr(store, _lv, "wardrobe") == "washer":
                        setattr(store, _lv, "line")
            if task_dry_end == 0:
                task_dry_end = Get_MinuteTotal() + LAUNDRY_DRY_DUR
        $ gametimemin += LAUNDRY_HANG_DUR
        $ task_hero_clean_home += 10
        call gametime from _call_gametime_74
        $ msg.msg(renpy.translate_string("You hung the clothes on the clothesline. They'll dry in about ") + renpy.translate_string(str(str(LAUNDRY_DRY_DUR))) + renpy.translate_string(" minutes"))
        jump action_chore_loop

    # --- Collect dry clothes ---
    if _result[0] == "collect_dry":
        python:
            for _cid in ["hero", "wsis", "wmom"]:
                for _o in Outfits_For(_cid):
                    _lv = "task_loc_" + _cid + "_" + _o
                    if getattr(store, _lv, "wardrobe") == "dry":
                        setattr(store, _lv, "wardrobe")
                        setattr(store, "task_wash_" + _cid + "_" + _o, 100)
        $ gametimemin += LAUNDRY_COLLECT_DUR
        $ task_hero_clean_home += 10
        call gametime from _call_gametime_75
        $ msg.msg(renpy.translate_string("You collected the clean, dry clothes and put them away"))
        jump action_chore_loop

    # Fallback
    jump action_chore_loop

# ----------------------------------------------------------------------------------------------------
label action_clean_wsis_caught:
# ----------------------------------------------------------------------------------------------------
    # 2.4: WSIS catches HERO red-handed taking her laundry from her bedroom.
    call hide_ui from _call_hide_ui_118

    # Map WSIS' current outfit to the available collection sprites (home / sleep / under).
    if wsis_wear == "home":
        $ _caught_wear = "home"
    elif wsis_wear == "sleep":
        $ _caught_wear = "sleep"
    else:
        $ _caught_wear = "under"

    stop BGM fadeout 1

    # HERO caught grabbing her panties.
    scene action_laundry_collect_bg home_bedroom_wsis
    show action_laundry_collect_hero_body
    show action_laundry_collect_hero_wear home
    show action_laundry_collect_hero_item wsis_panties

    show action_laundry_collect_wsis_body at OR
    show action_laundry_collect_wsis_hair at OR
    if _caught_wear == "home":
        show action_laundry_collect_wsis_wear home at OR
    elif _caught_wear == "sleep":
        show action_laundry_collect_wsis_wear sleep at OR
    else:
        show action_laundry_collect_wsis_wear under at OR
    show fx_light
    with dissolve

    $ msg.msg(renpy.translate_string("While collecting [C_Nam][fnamewsis][C_Off]'s clothes, you come across her underwear..."))
    hero "{mind}(These must be [C_Nam][hero_about_wsis][C_Off]'s... I should just toss them in the basket.){/mind}"

    show action_laundry_collect_wsis_body at CC_fast
    show action_laundry_collect_wsis_hair at CC_fast
    if _caught_wear == "home":
        show action_laundry_collect_wsis_wear home at CC_fast
    elif _caught_wear == "sleep":
        show action_laundry_collect_wsis_wear sleep at CC_fast
    else:
        show action_laundry_collect_wsis_wear under at CC_fast

    pause(0.25)
    play SE1 "Slip.ogg"
    pause(0.25)

    wsis "{aw}WHAT do you think you're doing with my PANTIES, you creep!?{/aw}"
    hero "W{w=[wt1]}-wait, it's not what it looks like!"

    # The hit event — she tries to punch him.
    call wsis_hit(_caught_wear if _caught_wear in ("home", "under") else "under") from _call_wsis_hit_1

    if _return == "Win":
        $ add_stat("wsis", "inti", 1)
        hero "Calm down, calm down! I'm just doing the laundry, I swear!"
        wsis "...{w=[wt2]} The laundry?"
        hero "Yeah. Someone's gotta wash all this. Including yours."
        wsis "{mind}Tsk...{/mind} Fine.{w=[wt2]} Do whatever you want with the chores, just{w=[wt1]} {b}DON'T{/b} touch my clothes with those perverted hands again!"
        $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] grabs her clothes back and storms off."))

    else:
        # HERO faints; time passes based on his physical resistance.
        $ a_event_0 = round(20 / ((0.5 + (perk_phy_res * 0.5)) * (1 + (stat_phy_res * 0.01))), 2)
        $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] knocks you out cold. You're out for a while..."))
        scene bg_0 with Dissolve(1)
        $ gametimemin += a_event_0
        call gametime from _call_gametime_76
        $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] took her clothes back while you were out cold."))

    # WSIS' clothes leave the basket and return to her wardrobe.
    python:
        for _o in Outfits_For("wsis"):
            if getattr(store, "task_loc_wsis_" + _o, "wardrobe") == "basket":
                setattr(store, "task_loc_wsis_" + _o, "wardrobe")

    play BGM "audio/W2C - Tranquility.mp3"
    $ map_lock_bedroom_wsis = True
    call goto_home_hallway from _call_goto_home_hallway
    jump show_ui

# ----------------------------------------------------------------------------------------------------
# 2.7: Chore Menu screen — unified cleaning + laundry management
# ----------------------------------------------------------------------------------------------------
screen UI_Chore(room_name, room_clean, house_clean, clothes_clean, is_facade, can_clean, can_trash, trash_blocked, chars, any_basket, any_washer, any_line, any_dry, cnt_basket, wash_left, dry_left):
    hbox:
        #xpos 100
        vbox:
            frame:
                xsize 640
                ysize 930
                xpadding 50
                ypadding 50

                vbox:
                    spacing 25
                    label renpy.translate_string("Chores")

                    side ("c l"):
                        area (-10, 0, 580, 780)
                        viewport id "ScrollChore_L":
                            xoffset 25
                            draggable True mousewheel True
                            vbox:
                                spacing 15
                                # --- Room & house info ---
                                text renpy.translate_string("{b}House cleanliness:{/b} ") + str(house_clean) + "%"
                                text renpy.translate_string("{b}Clothes cleanliness:{/b} ") + str(clothes_clean) + "%"
                                text renpy.translate_string("{b}[room_name]:{/b} ") + str(room_clean) + "%"

                                null height 10

                                # --- Pipeline status ---
                                if cnt_basket > 0:
                                    text renpy.translate_string("{b}Basket:{/b} ") + str(cnt_basket) + " outfit(s)"
                                if any_washer:
                                    if wash_left > 0:
                                        text renpy.translate_string("{b}Washer:{/b} [wash_left] min left")
                                    else:
                                        text renpy.translate_string("{b}Washer:{/b} done")
                                if any_line:
                                    if dry_left > 0:
                                        text renpy.translate_string("{b}Line:{/b} drying, [dry_left] min left")
                                if any_dry:
                                    text renpy.translate_string("{b}Line:{/b} dry")

                                null height 20

                                # --- Action buttons ---
                                if is_facade:
                                    textbutton renpy.translate_string("Throw the trash away") action Return(("trash",)):
                                        sensitive can_trash
                                    if trash_blocked:
                                        text renpy.translate_string("Clean all rooms first") size 20
                                else:
                                    textbutton renpy.translate_string("Clean this area") action Return(("clean",)):
                                        sensitive can_clean

                                null height 10

                                # --- Laundry global actions ---
                                textbutton renpy.translate_string("Load washer") action Return(("wash",)):
                                    sensitive (any_basket and not any_washer and wash_left == 0)
                                textbutton renpy.translate_string("Hang clothes") action Return(("hang",)):
                                    sensitive (any_washer and wash_left == 0)
                                textbutton renpy.translate_string("Collect dry clothes") action Return(("collect_dry",)):
                                    sensitive (any_dry and dry_left == 0)

                        vbar value YScrollValue("ScrollChore_L")
            frame:
                xsize 640
                ysize 150
                textbutton _("Close") action Return(("close",)) xalign 0.5 yalign 0.5

        frame:
            xsize 1180
            ysize 1080
            xpadding 50
            ypadding 50
            vbox:
                spacing 25
                label renpy.translate_string("Laundry")

                side ("c l"):
                    area (-10, 0, 1080, 940)
                    viewport id "ScrollChore_R":
                        xoffset 25
                        draggable True mousewheel True
                        vbox:
                            spacing 20
                            for _cid, _cname, _outfits in chars:
                                vbox:
                                    spacing 8
                                    text renpy.translate_string("{b}") + _cname + "{/b}"
                                    # Column headers
                                    hbox:
                                        spacing 15
                                        text renpy.translate_string("{u}Outfit{/u}") min_width 250
                                        text renpy.translate_string("{u}Clean{/u}") min_width 100
                                        text renpy.translate_string("{u}Status{/u}") min_width 220
                                        text renpy.translate_string("{u}Action{/u}")
                                    # Outfit rows
                                    for _oid, _oname, _wash, _loc, _worn, _can_collect in _outfits:
                                        hbox:
                                            spacing 15
                                            yalign 0.5
                                            text _oname min_width 250
                                            if _loc == "wardrobe":
                                                if _wash >= 80:
                                                    text renpy.translate_string("{color=#44cc44}") + str(_wash) + "%{/color}" min_width 100
                                                elif _wash >= WASH_DIRTY_BELOW:
                                                    text renpy.translate_string("{color=#cccc44}") + str(_wash) + "%{/color}" min_width 100
                                                else:
                                                    text renpy.translate_string("{color=#cc4444}") + str(_wash) + "%{/color}" min_width 100
                                            else:
                                                text str(_wash) + "%" min_width 100
                                            # Location status
                                            if _worn:
                                                text renpy.translate_string("{color=#8888ff}Wearing{/color}") min_width 220
                                            elif _loc == "wardrobe":
                                                text renpy.translate_string("Wardrobe") min_width 220
                                            elif _loc == "basket":
                                                text renpy.translate_string("{color=#cc8800}In basket{/color}") min_width 220
                                            elif _loc == "washer":
                                                text renpy.translate_string("{color=#0088cc}In washer{/color}") min_width 220
                                            elif _loc == "line":
                                                text renpy.translate_string("{color=#88aa00}On clothesline{/color}") min_width 220
                                            elif _loc == "dry":
                                                text renpy.translate_string("{color=#44cc44}Dry{/color}") min_width 220
                                            else:
                                                text _loc min_width 220
                                            # Action button
                                            if _can_collect:
                                                textbutton renpy.translate_string("Collect") action Return(("collect", _cid, _oid))
                                            else:
                                                text ""
                                    null height 10
                    vbar value YScrollValue("ScrollChore_R")
