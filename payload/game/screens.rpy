# --------------------------------------------------
# Initialization
# --------------------------------------------------
init offset = -1

# --------------------------------------------------
# Styles
# --------------------------------------------------
style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button_oc:
    background "#F0F"
    hover_background "#0F0"
    foreground "#F0F"
    hover_foreground "#0F0"
    properties gui.button_properties("image_button")
    hover_sound "ButtonHOVER.ogg"
    activate_sound "ButtonCLICK.ogg"

style button:
    properties gui.button_properties("button")
    hover_sound "ButtonHOVER.ogg"
    activate_sound "ButtonCLICK.ogg"

style image_button:
    properties gui.button_properties("image_button")
    hover_sound "ButtonHOVER.ogg"
    activate_sound "ButtonCLICK.ogg"

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
    xalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"

style frame:
    padding gui.frame_borders.padding
    background ConditionSwitch(
        "preferences.windowtheme == 'City'", Frame("gui/frame_dark.png", gui.frame_borders, tile=gui.frame_tile),
        "True", Frame("gui/frame_light.png", gui.frame_borders, tile=gui.frame_tile)
    )
# --------------------------------------------------
# In-game screens
# --------------------------------------------------
    # Say screen

    # The say screen is used to display dialogue to the player. It takes two parameters, who and what, which are the name of the speaking character and the text to be displayed, respectively. (The who parameter can be None if no name is given.)

    # This screen must create a text displayable with id "what", as Ren'Py uses this to manage text display. It can also create displayables with id "who" and id "window" to apply style properties.

    # https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    # style_prefix "say"

    on "show" action SetVariable("wmomto_hero", renpy.random.choice([__("dear"), __("my dear"), __("darling"), __("honey"), __("sweetheart"), __("my sweetheart"), __("my love")]))

    window:
        background Transform(If(preferences.windowtheme == "City", style.window.background, style.window_2.background), alpha = WindowOpacity)
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        side ("c l"):
            area (gui.dialogue_xpos-38, gui.dialogue_ypos, gui.dialogue_width+20, int(gui.textbox_height * 0.725)) #124 #75
            viewport id "Scroll_TextBox":
                xoffset 10
                draggable True mousewheel True
                text what id "what"
            vbar value YScrollValue("Scroll_TextBox")

    # If there's a side image, display it above the text. Do not display on the
    # phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


# Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox_1.png", xalign=0.5, yalign=1.0)

style window_2:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox_2.webp", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False
    justify True

style my_style:
    bold True


# Input screen

    # This screen is used to display renpy.input. The prompt parameter is used to pass a text prompt in.

    # This screen must create an input displayable with id "input" to accept the various input parameters.

    # https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

init python:
    import pygame

# Choice screen
    # This screen is used to display the in-game choices presented by the menu statement. The one parameter, items, is a list of objects, each with caption and action fields.
    # https://www.renpy.org/doc/html/screen_special.html#choice

# Pass "menu (yoffset=100):" to shift the whole choice block down by 100 pixels.
screen choice(items, yoffset=0):
    style_prefix "choice"

    $ _choice_cols = 1 if len(items) <= 5 else (2 if len(items) <= 11 else 3)
    $ _choice_yoff = yoffset

    vbox:
        yanchor 0.5
        xalign 0.50
        yalign 0.33
        yoffset _choice_yoff
        spacing 10
        for row_start in range(0, len(items), _choice_cols):
            hbox:
                xalign 0.5
                spacing 10
                for i in items[row_start:row_start + _choice_cols]:
                    textbutton i.caption action i.action

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "ButtonHOVER.ogg"
    activate_sound "ButtonCLICK.ogg"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    hover_sound "ButtonHOVER.ogg"
    activate_sound "ButtonCLICK.ogg"

# --------------------------------------------------
# Image Choice Menu
# --------------------------------------------------
# Usage:
#   menu (screen="menu_img"):
#       "Option A" ("image_name_a"):
#           $ var = "A"
#       "Option B" ("image_name_b"):
#           $ var = "B"
#       "Text only option":
#           $ var = "C"
# Image names are passed as menu item args and resolved by Ren'Py.
# Buttons without an image arg appear at the bottom as text-only choices.

screen menu_img(items):
    zorder 500
    python:
        _img_items = []
        _txt_items = []
        for _it in items:
            _it_args = getattr(_it, 'args', None)
            if _it_args:
                _img_items.append((_it.caption, _it_args[0], _it.action))
            else:
                _txt_items.append(_it)
        _menu_img_count = len(_img_items)
        _menu_img_spacing = 0
        _menu_img_h = (1080 - 100 - _menu_img_spacing) if _txt_items else 1080
        _menu_img_pw = (1820 - _menu_img_spacing * max(_menu_img_count - 1, 0)) // max(_menu_img_count, 1)
        _txt_count = len(_txt_items)
        _txt_spacing = 4
        _txt_pw = (1820 - _txt_spacing * max(_txt_count - 1, 0)) // max(_txt_count, 1)

    hbox:
        vbox:
            pos (0, 0)
            xsize 1820
            spacing _menu_img_spacing

            if _img_items:
                hbox:
                    spacing _menu_img_spacing
                    for _mi_text, _mi_img, _mi_action in _img_items:
                        frame:
                            xsize _menu_img_pw
                            ysize _menu_img_h
                            padding (0, 0, 0, 0)

                            button:
                                xfill True
                                yfill True
                                action _mi_action
                                hover_sound "ButtonHOVER.ogg"
                                activate_sound "ButtonCLICK.ogg"
                                idle_foreground Solid("#00000044")
                                hover_foreground Solid("#00000000")

                                viewport:
                                    xinitial 0.5
                                    child_size (1920, 1080)
                                    mousewheel False
                                    add _mi_img

                                text _mi_text:
                                    xalign 0.5
                                    yalign 0.5
                                    color "#ffffff"
                                    bold True
                                    size 36
                                    text_align 0.5
                                    outlines [(2, "#000000", 0, 0)]

            if _txt_items:
                hbox:
                    spacing _txt_spacing
                    for _ti in _txt_items:
                        frame:
                            xsize _txt_pw
                            ysize 100
                            textbutton _ti.caption:
                                xalign 0.5
                                yalign 0.5
                                action _ti.action
                                hover_sound "ButtonHOVER.ogg"
                                activate_sound "ButtonCLICK.ogg"
                                style "choice_button"
                                text_style "choice_button_text"
        frame:
            xsize 100
            ysize 1080

# --------------------------------------------------
# Main and Game Menu Screens
# --------------------------------------------------

# Navigation screen ##############################
#
# This screen is included in the main and game menus, and provides navigation
# to other menus, and to start the game.

screen navigation():

    vbox:
        ypos 20
        if preferences.language == "zh":
            fixed:
                xysize (360, 145)
                text "欢欲都市":
                    xalign 0.5
                    ypos 10
                    size 78
                    color "#FF325B"
                    outlines [(3, "#FFFFFF", 0, 0), (7, "#241526", 0, 0)]
                text "简体中文版":
                    xalign 0.5
                    ypos 108
                    size 28
                    color "#FFFFFF"
                    outlines [(2, "#241526", 0, 0)]
        else:
            image "gui/LOGO.webp"
        text str("v" + config.version) xalign 1.0 xoffset -15

    vbox:
        #style_prefix "navigation"
        #spacing gui.navigation_spacing
        #xpos gui.navigation_xpos
        yalign 0.0
        xalign 1.0
        ypos 260
        xpos 350
        spacing 5

        if main_menu:
            textbutton _("New Game") action Start() xalign 1.0
            textbutton _("Load Game") action ShowMenu("load") xalign 1.0
            textbutton _("Settings") action ShowMenu("preferences") xalign 1.0
            textbutton _("Language") action ShowMenu("language") xalign 1.0

        else:
            textbutton _("History") action ShowMenu("history") xalign 1.0
            textbutton _("Save") action ShowMenu("save") xalign 1.0
            textbutton _("Load Game") action ShowMenu("load") xalign 1.0
            textbutton _("Settings") action ShowMenu("preferences") xalign 1.0
            textbutton _("Language") action ShowMenu("language") xalign 1.0

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True) xalign 1.0

        elif not main_menu:
            textbutton _("Main Menu") action MainMenu() xalign 1.0

        textbutton _("About") action ShowMenu("about") xalign 1.0

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            # Help isn't necessary or relevant to mobile devices.
            vbox:
                xalign 1.0
                textbutton _("Help") action ShowMenu("help")

        if main_menu and 0 > 1:
            vbox:
                xalign 1.0
                imagebutton:
                    idle "gui/SubscribeStar IDLE.webp"
                    hover "gui/SubscribeStar HOVER.webp"
                    action OpenURL("https://subscribestar.adult/quiquersson")

            vbox:
                xalign 1.0
                imagebutton:
                    idle "gui/Patreon IDLE.webp"
                    hover "gui/Patreon HOVER.webp"
                    action OpenURL("https://www.patreon.com/quiquersson")

            vbox:
                xalign 1.0
                imagebutton:
                    idle "gui/Discord IDLE.webp"
                    hover "gui/Discord HOVER.webp"
                    action OpenURL("https://discord.gg/raU65TZqbE")

            vbox:
                xalign 1.0
                imagebutton:
                    idle "gui/Carrd IDLE.webp"
                    hover "gui/Carrd HOVER.webp"
                    action OpenURL("https://quiquersson.carrd.co/")
        vbox:
            xalign 1.0
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


# Main Menu screen ##############################
#
# Used to display the main menu when Ren'Py starts.
#
# https://www.renpy.org/doc/html/screen_special.html#main-menu

init python:
    import pygame
    import math


    class TrackCursor(renpy.Displayable):
        def __init__(self, child, paramod, **kwargs):
            super(TrackCursor, self).__init__()
            self.child = renpy.displayable(child)
            self.x = 0
            self.y = 0
            self.actual_x = 0
            self.actual_y = 0
            self.paramod = paramod
            self.last_st = 0

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            minimum_speed = 0.1
            maximum_speed = 3
            speed = 1 + minimum_speed
            mouse_distance_x = min(maximum_speed, max(minimum_speed, (self.x - self.actual_x)))
            mouse_distance_y = (self.y - self.actual_y)
            if self.x is not None:
                st_change = st - self.last_st
                self.last_st = st
                self.actual_x = math.floor(self.actual_x + ((self.x - self.actual_x) * speed * (st_change )) * self.paramod)
                self.actual_y = math.floor(self.actual_y + ((self.y - self.actual_y) * speed * (st_change)) * self.paramod)
                if mouse_distance_y <= minimum_speed:
                    mouse_distance_y = minimum_speed
                elif mouse_distance_y >= maximum_speed:
                    mouse_distance_y = maximum_speed
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.actual_x, self.actual_y))
            renpy.redraw(self, 0)
            return rv

        def event(self, ev, x, y, st):
            hover = ev.type == pygame.MOUSEMOTION
            click = ev.type == pygame.MOUSEBUTTONDOWN
            mousefocus = pygame.mouse.get_focused()
            if hover:
                if (x != self.x) or (y != self.y) or click:
                    self.x = -x /self.paramod
                    self.y = -y /self.paramod

transform parallax_leaves:
    xpos 0 ypos -1188
    linear 15 xpos -2200 ypos 0
    repeat

transform parallax_2025:
    xalign 0.5 yalign 0.5 zoom 0.01 alpha 1
    ease 10 zoom 1
    ease 5 alpha 0

transform parallax_sky:
    xpos 0
    linear 300 xpos -2200
    repeat

screen pseudo_main_menu():
    if preferences.parallax == True:
        timer 0.1 repeat True action [
            SetVariable("a_ani_1", a_ani_1 + (a_ani_2*a_ani_4)),

            If(a_ani_1 >= 5, SetVariable("a_ani_1", 1)),
            If(a_ani_1 < 1, SetVariable("a_ani_1", 5)),

            If(a_ani_3 == 0, SetVariable("a_ani_2", a_ani_2 + 0.0025)),
            If(a_ani_3 == 1, SetVariable("a_ani_2", a_ani_2 - 0.0025)),

            If(a_ani_2 >= 0.1, SetVariable("a_ani_2", 0), SetVariable("a_ani_3", 1)),
            If(a_ani_2 <= -0.1, SetVariable("a_ani_2", 0), SetVariable("a_ani_3", 0)),
        ]

        timer 1 repeat True action [
            SetVariable("a_ani_4", renpy.random.choice([-1, 1]))
        ]

    else:
        timer 0.1 repeat False action [SetVariable("a_ani_1", 0), SetVariable("a_ani_2", 0), SetVariable("a_ani_3", 0), SetVariable("a_ani_4", 0)]

    image "mainmenu_bg" at parallax_sky
    image "Live2D_MainMenu breathe"
    image "mainmenu_fg" at parallax_leaves
    image "mainmenu_fx":
        blend "add"

transform xmas1:
    alpha 0
    ease 3 alpha 1
    ease 3 alpha 0
    pause 12
    repeat

transform xmas2:
    alpha 0
    pause 3
    ease 3 alpha 1
    ease 3 alpha 0
    pause 9
    repeat

transform xmas3:
    alpha 0
    pause 6
    ease 3 alpha 1
    ease 3 alpha 0
    pause 6
    repeat

transform xmas4:
    alpha 0
    pause 9
    ease 3 alpha 1
    ease 3 alpha 0
    pause 3
    repeat

transform xmas5:
    alpha 0
    pause 12
    ease 3 alpha 1
    ease 3 alpha 0
    repeat

transform xmas6:
    alpha 1
    ease 3 alpha 0
    pause 12
    ease 3 alpha 1
    repeat

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    key "mousedown_1" action [Play("SE1", "BeepRight.ogg"), ToggleVariable("preferences.ui_menu")]
    key "mousedown_4" action [SetVariable("a_ani_9", min(100, a_ani_9 + 5))]
    key "mousedown_5" action [SetVariable("a_ani_9", max(0, a_ani_9 - 5))]

    if preferences.parallax == True:
        timer 0.1 repeat True action [
            SetVariable("a_ani_1", a_ani_1 + (a_ani_2 * a_ani_4)),

            If(a_ani_1 >= 5, SetVariable("a_ani_1", 1)),
            If(a_ani_1 < 1, SetVariable("a_ani_1", 5)),

            If(a_ani_3 == 0, SetVariable("a_ani_2", a_ani_2 + 0.0025)),
            If(a_ani_3 == 1, SetVariable("a_ani_2", a_ani_2 - 0.0025)),

            If(a_ani_2 >= 0.1, SetVariable("a_ani_2", 0), SetVariable("a_ani_3", 1)),
            If(a_ani_2 <= -0.1, SetVariable("a_ani_2", 0), SetVariable("a_ani_3", 0)),
        ]

        timer 1 repeat True action [
            SetVariable("a_ani_4", renpy.random.choice([-1, 1]))
        ]

    else:
        timer 0.1 repeat False action [SetVariable("a_ani_1", 0), SetVariable("a_ani_2", 0), SetVariable("a_ani_3", 0), SetVariable("a_ani_4", 0)]

    if preferences.gametimeevent == "Halloween": # Enable/Disable
        if not (renpy.music.get_playing(channel="BGM") == "audio/W2C - MainTheme (HALLOWEEN).mp3" or renpy.music.get_playing(channel="BGM") == "audio/W2C - MainTheme (EPIC).mp3" or renpy.music.get_playing(channel="BGM") == "<from 0>audio/W2C - Welcum To The City!.mp3"):
            on "show" action Play("BGM", "audio/W2C - MainTheme (HALLOWEEN).mp3", loop=True)
            on "hide" action Stop("BGM", fadeout=2)
        image "gui/MainMenu_Halloween 01.webp"
        image "gui/MainMenu_Halloween 02.webp" at HalloweenFX1
        image "gui/MainMenu_Halloween 03.webp" at HalloweenFX2

    elif preferences.gametimeevent == "XMAS": # Enable/Disable
        if not (renpy.music.get_playing(channel="BGM") == "audio/W2C - MainTheme (XMAS).mp3" or renpy.music.get_playing(channel="BGM") == "audio/W2C - MainTheme (EPIC).mp3" or renpy.music.get_playing(channel="BGM") == "<from 0>audio/W2C - Welcum To The City!.mp3"):
            on "show" action Play("BGM", "audio/W2C - MainTheme (XMAS).mp3", loop=True)
            on "hide" action Stop("BGM", fadeout=2)
        image "gui/MainMenu_XMAS.webp"
        image "gui/MainMenu_XMAS_FX 1.webp" at xmas1:
            blend "add"
        image "gui/MainMenu_XMAS_FX 2.webp" at xmas2:
            blend "add"
        image "gui/MainMenu_XMAS_FX 3.webp" at xmas3:
            blend "add"
        image "gui/MainMenu_XMAS_FX 4.webp" at xmas4:
            blend "add"
        image "gui/MainMenu_XMAS_FX 5.webp" at xmas5:
            blend "add"
        image "gui/MainMenu_XMAS_FX 6.webp" at xmas6:
            blend "add"

    else:
        if not (renpy.music.get_playing(channel="BGM") == "audio/W2C - MainTheme.mp3" or renpy.music.get_playing(channel="BGM") == "audio/W2C - MainTheme (EPIC).mp3" or renpy.music.get_playing(channel="BGM") == "<from 0>audio/W2C - Welcum To The City!.mp3"):

            on "show" action Play("BGM", "audio/W2C - MainTheme.mp3", loop=True)
            on "hide" action Stop("BGM", fadeout=2)

        #image "gui/MainMenu/mainmenu_bg.webp" at parallax_sky
        #image "gui/MainMenu.webp"

        image "mainmenu_bg" at parallax_sky
        image "Live2D_MainMenu breathe"
        #image "mainmenu_test"
        image "mainmenu_fg" at parallax_leaves
        image "mainmenu_fx":
            blend "add"

    if preferences.ui_menu == True:
        hbox:
            xalign 1.0
            yalign 0.0
            frame:
                background None
                xpadding 25
                ypadding 25
                if preferences.gametimeevent == None:
                    imagebutton:
                        idle At("images/UI/SUBMENU_Option_Quest.webp", ButtonIdle)
                        hover At("images/UI/SUBMENU_Option_Quest.webp", ButtonHover)
                        action [SetVariable("preferences.gametimeevent", "Halloween"), Play("BGM", "audio/W2C - MainTheme (HALLOWEEN).mp3", loop=True)]
                elif preferences.gametimeevent == "Halloween":
                    imagebutton:
                        idle At("images/UI/SUBMENU_Option_Quest.webp", ButtonIdle)
                        hover At("images/UI/SUBMENU_Option_Quest.webp", ButtonHover)
                        action [SetVariable("preferences.gametimeevent", "XMAS"), Play("BGM", "audio/W2C - MainTheme (XMAS).mp3", loop=True)]
                else:
                    imagebutton:
                        idle At("images/UI/SUBMENU_Option_Quest.webp", ButtonIdle)
                        hover At("images/UI/SUBMENU_Option_Quest.webp", ButtonHover)
                        action [SetVariable("preferences.gametimeevent", None), Play("BGM", "audio/W2C - MainTheme.mp3", loop=True)]
        frame:
            background None
            xysize(1920,1080)
            xpadding 25
            ypadding 25
            hbox:
                xalign 1.0
                yalign 1.0
                spacing 25
                vbox:
                    yalign 0.5
                    xsize 600
                    if preferences.gametimeevent == None:
                        text "{color=#000}👇Drag here👇 or scroll to zoom{/color}" size 40 xalign 0.5
                        bar value VariableValue("a_ani_9", 100) xmaximum 600 ymaximum 50 xalign 0.5
                imagebutton:
                    idle At("images/UI/SM_Carrd.webp", ButtonIdle)
                    hover At("images/UI/SM_Carrd.webp", ButtonHover)
                    action OpenURL("https://quiquersson.carrd.co/")
                imagebutton:
                    idle At("images/UI/SM_Twitch.webp", ButtonIdle)
                    hover At("images/UI/SM_Twitch.webp", ButtonHover)
                    action OpenURL("https://www.twitch.tv/quiquersson")
                imagebutton:
                    idle At("images/UI/SM_Discord.webp", ButtonIdle)
                    hover At("images/UI/SM_Discord.webp", ButtonHover)
                    action OpenURL("https://discord.gg/raU65TZqbE")
                imagebutton:
                    idle At("images/UI/SM_SubscribeStar.webp", ButtonIdle)
                    hover At("images/UI/SM_SubscribeStar.webp", ButtonHover)
                    action OpenURL("https://subscribestar.adult/quiquersson")
                imagebutton:
                    idle At("images/UI/SM_Patreon.webp", ButtonIdle)
                    hover At("images/UI/SM_Patreon.webp", ButtonHover)
                    action OpenURL("https://www.patreon.com/quiquersson")

        # This empty frame darkens the main menu.
        frame:
            style "main_menu_frame"

        # The use statement includes another screen inside this one. The actual
        # contents of the main menu are in the navigation screen.
        use navigation

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.webp"
    #background None

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


# Game Menu screen ##############################
#
# This lays out the basic common structure of a game menu screen. It's called
# with the screen title, and displays the background, title, and navigation.
#
# The scroll parameter can be None, or one of "viewport" or "vpgrid". When
# this screen is intended to be used with one or more children, which are
# transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            # Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        xoffset -30

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.webp"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xalign 0.5
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


# About screen ################################
#
# This screen gives credit and copyright information about the game and Ren'Py.
#
# There's nothing special about this screen, and hence it also serves as an
# example of how to make a custom screen.


screen about():

    tag menu

    # This use statement includes the game_menu screen inside this one. The
    # vbox child is then included inside the viewport inside the game_menu
    # screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        python:
            log_id = []
            log_txt = []
            for a, b in gui.devlog.items():
                log_id.append(a)
                log_txt.append(b)

        default logvv = 0

        vbox:

            # gui.about is usually set in options.rpy.
            if gui.about:

                hbox:
                    spacing 25
                    xsize 1350
                    xalign 0.5
                    label "Devlog:"

                    viewport id "devlog_bar":
                        xsize 1150
                        ysize 60
                        xalign 0.5
                        scrollbars "horizontal"
                        mousewheel "horizontal"
                        draggable True

                        hbox:
                            spacing 25
                            xalign 0.5
                            for logii, logvr in enumerate(log_id):
                                textbutton "[logvr]":
                                    action SetScreenVariable("logvv", logii)
                                    selected (logvv == logii)

                text "Check {a=https://quiquersson.itch.io/w2c/devlog}itch.io{/a} for more detailed devlog info."
                text log_txt[logvv] justify True xsize 1350
                text "[gui.about!t]\n" justify True xsize 1350

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


# Load and Save screens ############################
#
# These screens are responsible for letting the player save the game and load
# it again. Since they share nearly everything in common, both are implemented
# in terms of a third screen, file_slots.
#
# https://www.renpy.org/doc/html/screen_special.html#save https://
# www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            # This ensures the input will get the enter event before any of the
            # buttons do.
            order_reverse True

            # The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            # The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            # Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                # range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 5
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


# Preferences screen #############################
#
# The preferences screen allows the player to configure the game to better suit
# themselves.
#
# https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Settings"), scroll="viewport"):

        vbox:
            box_wrap True

            hbox:
                spacing 100

                vbox:
                    label _("Display")
                    vbox:
                        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                            hbox:
                                spacing 25
                                style_prefix "radio"
                                textbutton _("Window") action Preference("display", "window")
                                textbutton _("Fullscreen") action Preference("display", "fullscreen")

                    vbox:
                        style_prefix "check"
                        #textbutton _("Visual City Map") action ToggleField(preferences, "citymap")
                        #textbutton _("Wind Simulation") action ToggleField(preferences, "parallax")
                        textbutton _("Main Screen Wind Simulation") action ToggleField(preferences, "parallax")
                        textbutton _("Intro Music") action ToggleField(preferences, "intro")
                        textbutton _("Intro Splash Arts") action ToggleField(preferences, "warning")

                    label _("{pr}{pr}Optional Content & Features")
                    vbox:
                        style_prefix "check"
                        if renpy.variant("mobile"):
                            textbutton _("Phone Vibration") action ToggleField(preferences, "vibration")
                        #textbutton _("Blood") action ToggleField(preferences, "gr")
                        textbutton _("Elder") action ToggleField(preferences, "elder")
                        textbutton _("Femdom") action ToggleField(preferences, "femdom")
                        textbutton _("Voyeur") action ToggleField(preferences, "voyeur")
                        #textbutton _("Gay/Yaoi/BL") action ToggleField(preferences, "yaoi")
                        #textbutton _("Futanari") action ToggleField(preferences, "wahu")
                
                vbox:
                    label _("Theme")
                    hbox:
                        spacing 25
                        style_prefix "radio"
                        textbutton _("City Theme") action SetVariable("preferences.windowtheme", "City")
                        textbutton _("Notebook Theme") action SetVariable("preferences.windowtheme", "Notebook")
                    frame:
                        xpadding 25 ypadding 25 xsize 700 ysize 500
                        vbox:
                            text """ 💛 {b}Welcum To The City{/b} 💛

{i}[C_Dat]Lorem ipsum dolor sit amet[C_Off], consectetur adipiscing elit. In lobortis ullamcorper diam. [C_Nam]Pellentesque[C_Off] habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nunc et leo sed sem porttitor aliquam. Sed justo turpis, finibus quis viverra nec, condimentum sed est.{/i}""" justify True

            # Only switches that measurably change frame rate/battery — no placebo toggles.
            label _("{pr}{pr}Performance")
            hbox:
                vbox:
                    style_prefix "check"
                    textbutton _("Minigame Dancers") action ToggleField(preferences, "dancers")
                    textbutton _("Animated Menu Scene") action ToggleField(preferences, "animatedmenu")

            label _("{pr}{pr}Text & Dialogue")
            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                hbox:
                    vbox:
                        style_prefix "check"
                        textbutton _("Global Data") action ToggleVariable("preferences.is_namepersistent")
                        textbutton _("Button Map Name") action ToggleVariable("preferences.text_mapbutton")
                    vbox:
                        style_prefix "radio"
                        textbutton _("Immersive") action SetVariable("preferences.text_cps", 40)
                        textbutton _("Practical") action SetVariable("preferences.text_cps", 0)
                        textbutton _("{bt}Animated Text{/bt}") action [SetVariable("preferences.enable_TXT_Tag", True), SetVariable("preferences.fx", 1)]
                        textbutton _("Simple Text") action [SetVariable("preferences.enable_TXT_Tag", False), SetVariable("preferences.fx", 0)]
                    vbox:
                        style_prefix "check"
                        textbutton _("Skip Unseen Text") action Preference("skip", "toggle")
                        textbutton _("Skip After Choices") action Preference("after choices", "toggle")
                        textbutton _("Skip Transitions") action InvertSelected(Preference("transitions", "toggle"))
            else:
                vbox:
                    spacing 100
                    vbox:
                        style_prefix "check"
                        textbutton _("Permanent Data") action ToggleVariable("preferences.is_namepersistent")
                    vbox:
                        style_prefix "radio"
                        textbutton _("Immersive") action SetVariable("preferences.text_cps", 30)
                        textbutton _("Practical") action SetVariable("preferences.text_cps", 0)
                        textbutton _("{bt}Animated Text{/bt}") action [SetVariable("preferences.enable_TXT_Tag", True), SetVariable("preferences.fx", 1)]
                        textbutton _("Simple Text") action [SetVariable("preferences.enable_TXT_Tag", False), SetVariable("preferences.fx", 0)]
                    vbox:
                        style_prefix "check"
                        textbutton _("Skip Unseen Text") action Preference("skip", "toggle")
                        textbutton _("Skip After Choices") action Preference("after choices", "toggle")
                        textbutton _("Skip Transitions") action InvertSelected(Preference("transitions", "toggle"))

                # Additional vboxes of type "radio_pref" or "check_pref" can be
                # added here, to add additional creator-defined preferences.

            label "{pr}{pr}Audio Volume"
            hbox:
                vbox:
                    style_prefix "slider"

                    if config.has_music:
                        text _("Background Music")
                        hbox:
                            bar value Preference("mixer bgm volume")

                    if config.has_music:
                        text _("Background Environment")
                        hbox:
                            bar value Preference("mixer bge volume")

                    if config.has_sound:
                        hbox:
                            text _("Sound Effect")
                            textbutton _("(TEST)") action Play("SE1", renpy.random.choice(["Peidinho.ogg","Slip.ogg","Squeak2.ogg","Boing1.mp3"]))
                        hbox:
                            bar value Preference("mixer se1 volume")

                    if config.has_sound:
                        hbox:
                            text _("Sound Voice")
                            textbutton _("(TEST)") action Play("SE2", renpy.random.choice(["Giggle A1.mp3","WNEI_grunt.ogg","Giggle B1.mp3","Giggle C1.mp3","Moan1.mp3","SWFMoan248.ogg"]))
                        hbox:
                            bar value Preference("mixer se2 volume")

                    if config.has_voice and preferences.wt == 1:
                        hbox:
                            text _("Dialog Beeps")
                            textbutton _("(TEST)") action Play("SE3", renpy.random.choice(["audio/Voice/HERO1.ogg","audio/Voice/HERO2.ogg","audio/Voice/HERO3.ogg","audio/Voice/HERO4.ogg","audio/Voice/HERO5.ogg","audio/Voice/HERO6.ogg","audio/Voice/HERO7.ogg"]), loop=False)
                        hbox:
                            bar value Preference("mixer se3 volume")

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 450

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground Text("❌", size=25, yalign=0.5)
    selected_foreground Text("✅", size=25, yalign=0.5)
    left_padding 50

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground Text("❌", size=25, yalign=0.5)
    selected_foreground Text("✅", size=25, yalign=0.5)
    left_padding 50

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 1000

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


# Translation screen ###############################

init python:

    def tl_done_line(language):
        """The "* Done: X%" line under a language button, tinted red (nothing) to green (all of it).

        The count comes from the Translator tool's index (game/tools/Translator), which already walks
        every translate block and old/new pair in the game — so this number moves on its own as lines
        are translated, with nothing here to keep in sync. Returns "" if the tool is not installed.
        """
        try:
            done, total = tltool.lang_stats(language)
        except Exception:
            return ""

        if not total:
            return ""

        pct = int(round(100.0 * done / total))

        # Ramp through yellow, not straight from red to green: the direct line dims to a muddy olive
        # around the halfway mark, which is exactly where the number is worth reading. Green climbs over
        # the first half, red falls over the second, so 0/50/100 land on red / yellow / green at full
        # brightness and every step in between stays legible.
        r = 255 if pct <= 50 else int(round(255 * (100 - pct) / 50.0))
        g = 255 if pct >= 50 else int(round(255 * pct / 50.0))

        return "* Done: {color=#%02x%02x64}%d%%{/color}" % (r, g, pct)


screen language():
    
    tag menu

    use game_menu(_("Language"), scroll="viewport"):

        vbox:
            spacing 100
            xsize 1200
            xalign 0.5

            # Translator tool. This one button is the whole hook — see game/tools/Translator/ReadMe.md.
            vbox:
                spacing 50

                vbox:
                    xsize 1200
                    label "{pr}Translator" xalign 0.5
                    text "{color=#FFFF00}⚠{/color} Rewrite any line of the game in your own language, with the scene it belongs to on screen. Your work is written straight into the translation files. Also opens with {b}SHIFT+T{/b} anywhere in the game."

                vbox:
                    textbutton _("{image=starchan} Open Translator") action TranslatorTool()

            vbox:
                spacing 50
                
                vbox:
                    xsize 1200
                    label "Default" xalign 0.5
                    text "{color=#FFFF00}⚠{/color} If you want to help with any translation or proofreading, just contact me on Discord, Twitter, or email."

                vbox:
                    textbutton _("{image=starchan} English") action [SetVariable("persistent.lang", None), Language(None)]
                    text "* Writting: {b}quiquersson{/b}"
                    text "* Proofreading: {b}BlurCat{/b}; {b}Granite{/b}; {b}Oxymoron{/b}"
                    text tl_done_line(None)

            vbox:
                spacing 50
                
                vbox:
                    xsize 1200
                    label "{pr}Translation" xalign 0.5
                    text "{color=#FFFF00}⚠{/color} Consider go back to the ''English'' language if you witness an error. Remember that you can always change the language to fit your needs."

                vbox:
                    textbutton _("{image=starchan} Português (Brasil)") action [SetVariable("persistent.lang", "pt"), Language("pt")]
                    text "* Translator: {b}quiquersson{/b}, {b}Kola{/b}, {b}Edditor{/b}"
                    text tl_done_line("pt")

                vbox:
                    textbutton _("{image=starchan} Español") action [SetVariable("persistent.lang", "es"), Language("es")]
                    text "* Translator: {b}fenixrage{/b}, {b}Puniasterus{/b}, {b}Viskaax{/b}"
                    text tl_done_line("es")

                vbox:
                    textbutton _("{image=starchan} Italiano") action [SetVariable("persistent.lang", "it"), Language("it")]
                    text "* Translator: {b}mensch{/b}, {b}CristianBuzz{/b}"
                    text tl_done_line("it")

                vbox:
                    textbutton _("{image=starchan} Русский") action [SetVariable("persistent.lang", "ru"), Language("ru")]
                    text "* Translator: {b}BigFloppa{/b}"
                    text tl_done_line("ru")

                vbox:
                    textbutton _("{image=starchan} 中文") action [SetVariable("persistent.lang", "zh"), Language("zh")]
                    if persistent.lang == "zh":
                        text "* Translator: {b}小白{/b} & {b}太上月华静夜天尊{/b} (考虑检查他的 {a=https://space.bilibili.com/38852434}Bilibili 频道{/a})"
                    else:
                        text "* Translator: {b}小白{/b} & {b}太上月华静夜天尊{/b} (Consider checking his {a=https://space.bilibili.com/38852434}Bilibili channel{/a})"
                    text tl_done_line("zh")

                vbox:
                    textbutton _("{image=starchan} Türkçe") action [SetVariable("persistent.lang", "tr"), Language("tr")]
                    text "* Translator: {b}zlpfilee{/b}"
                    text tl_done_line("tr")

                vbox:
                    textbutton _("{image=starchan} Française") action [SetVariable("persistent.lang", "fr"), Language("fr")]
                    text '* Translator: {b}Jin{/b}, {b}Christophe "KurryTofu" Dehay{/b}'
                    text tl_done_line("fr")

                vbox:
                    textbutton _("{image=starchan} 한국어") action [SetVariable("persistent.lang", "ko"), Language("ko")]
                    text "* Translator: {b}kimbaechoo{/b}"
                    text tl_done_line("ko")


# History screen ###############################


# History screen ###############################
#
# This is a screen that displays the dialogue history to the player. While
# there isn't anything special about this screen, it does have to access the
# dialogue history stored in _history_list.
#
# https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    # Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                # This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        # Take the color of the who text from the Character, if
                        # set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


# This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


# Help screen #################################
#
# A screen that gives information about key and mouse bindings. It uses other
# screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
# help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

# --------------------------------------------------
# Additional screens
# --------------------------------------------------


# Confirm screen ###############################
#
# The confirm screen is called when Ren'Py wants to ask the player a yes or no
# question.
#
# https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    # Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.webp"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=gui.frame_tile)
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


# Skip indicator screen ############################
#
# The skip_indicator screen is displayed to indicate that skipping is in
# progress.
#
# https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


# This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha .5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    # We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    # glyph in it.
    font "DejaVuSans.ttf"


# Notify screen ################################
#
# The notify screen is used to show the player a message. (For example, when
# the game is quicksaved or a screenshot has been taken.)
#
# https://www.renpy.org/doc/html/screen_special.html#notify-screen

#----------------------------------------------------------------------------------------------------
# NOTIFY
#----------------------------------------------------------------------------------------------------
# Ways to push a notification into the stack

# 1- inside a python block
# msg.msg("Say something.")

# 2- inside script
# $ msg.msg("Say something.")

# 3- from screen action
# action Function(msg.msg, "say something")

init python:
    class msgz:
        def __init__(self, limit = 20):
            self.t = limit
            self.list = []
            self.n = 0
            for i in range(self.t):
                self.list.append([])

        def msg(self, m):
            self.list[self.n] = m
            if self.n < self.t-1:
                self.n += 1
            else:
                self.n = 0

        def rem(self, i):
            self.list[i] = []
        
        def clear(self):
            self.list = []
            self.n = 0
            for i in range(self.t):
                self.list.append([])

default msg = msgz(30)

init python:
    config.overlay_screens.append('notif')

transform notice:
    alpha 0 xpos 125 ypos 100
    ease persistent.notice1 alpha 1 ypos 0
    pause persistent.notice2
    ease persistent.notice3 alpha 0

screen notif:
    zorder 2000

    vbox:
        yalign 0.0
        yoffset 50
        for i in enumerate(msg.list):
            if i[1]:
                frame:
                    background "#00000032"
                    at notice
                    text i[1] size 50 outlines [(3, "#646464", 0, 0)]
                timer 8 action Function(msg.rem, i[0])
    

#----------------------------------------------------------------------------------------------------


# NVL screen #################################
#
# This screen is used for NVL-mode dialogue and menus.
#
# https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        # Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        # Displays the menu, if given. The menu may be displayed incorrectly if
        # config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


# This controls the maximum number of NVL-mode entries that can be displayed at
# once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.webp"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

# --------------------------------------------------
# Mobile Variants
# --------------------------------------------------

style pref_vbox:
    variant "medium"
    xsize 675

style window:
    variant "small"
    background "gui/phone/textbox_1.webp"

style window_2:
    variant "small"
    background "gui/phone/textbox_2.webp"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.webp"

style check_button:
    variant "small"
    foreground Text("❌", size=28, yalign=0.5)
    selected_foreground Text("✅", size=28, yalign=0.5)
    left_padding 50

style nvl_window:
    variant "small"
    background "gui/phone/nvl.webp"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.webp"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.webp"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.webp"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

