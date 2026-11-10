label hide_ui:

    hide screen bg_map_hero
    hide screen bg_map_wnei
    hide screen bg_map_store
    hide screen bg_map_office
    hide screen bg_map_school

    hide screen SkipScene

    hide screen UI_chat
    hide screen UI_action
    hide screen UI_stats
    hide screen UI_items
    hide screen UI_show_DataPer
    hide screen UI_show_DataInt
    hide screen UI_show_DataPhy
    hide screen UI_show_DataCha

    hide screen UI_Inventory_Fridge
    hide screen UI_buy_Item
    hide screen UI_give_Item
    hide screen UI_show_Item
    hide screen UI_Menu_Options
    hide screen UI_Menu_Options_Settings
    hide screen UI_Menu_Options_Gallery_IMG
    hide screen UI_Menu_Options_Gallery
    hide screen UI_Menu_Options_Music
    hide screen UI_Menu_Options_KCC
    
    hide screen NavButton
    hide screen nav_map

    hide screen nav_office_facade
    hide screen nav_office_room

    hide screen nav_home_facade
    hide screen nav_home_livingroom
    hide screen nav_home_hallway
    hide screen nav_home_bedroom_hero
    hide screen nav_home_bedroom_wsis
    hide screen nav_home_bedroom_wmom
    hide screen nav_home_bathroom

    hide screen nav_school_facade
    hide screen nav_school_frontyard
    hide screen nav_school_hallway1
    hide screen nav_school_library
    hide screen nav_school_courtyard

    hide screen nav_school_club_council

    hide screen nav_school_locker_m
    hide screen nav_school_locker_f
    hide screen nav_school_pool
    hide screen nav_school_sportcourt
    
    hide screen nav_school_hallway2
    hide screen nav_school_classroom
    hide screen nav_school_classroom_1a
    hide screen nav_school_classroom_1b
    hide screen nav_school_classroom_3a

    hide screen nav_shopping_facade
    hide screen nav_shopping_hall
    hide screen nav_shopping_cinema_entrance
    hide screen nav_shopping_store_clothing
    hide screen nav_shopping_store_arcade
    hide screen nav_shopping_court_food
    return

label hide_windows:
    if renpy.get_screen("say"):
        $ config.window = "hide"
    else:
        $ config.window = "show"
    return

label show_ui:
    call gamecheck from _call_gamecheck_32
    call item_check from _call_item_check

    if len(item_cart) > 0:
        python:
            for buceta in item_cart:
                inventory.append(buceta)
    $ item_cart = []

    window hide
    hide screen UI_Menu_Options
    show screen quick_menu
    show screen UI_chat
    show screen UI_action

    if date_active == False:
        show screen UI_stats
        show screen UI_items
        hide screen Date_UI

    else:
        hide screen UI_stats
        hide screen UI_items
        show screen Date_UI
    
    $ config.allow_skipping = True

    $ ui.interact()

    jump show_ui

# ----------------------------------------------------------------------------------------------------
# SCREENS
# ----------------------------------------------------------------------------------------------------
screen fx_morning():
    image "images/BG/fx_morning.webp" blend "add"

screen fx_afternoon():
    image "images/BG/fx_afternoon.webp":
        blend "add"

screen fx_night():
    image "images/BG/fx_night.webp":
        blend "multiply"
    image "images/BG/fx_light.webp":
        blend "add"

# Define the reusable button screen
screen NavButton(Nav_IMG="", Nav_LABEL="", Nav_TXT1=None, Nav_TXT2=None, Nav_TXT3=None):
    frame:
        background "#000"
        xsize 260
        ysize 150
        button:
            xalign 0.5
            yalign 0.5

            # Visual
            if Nav_LABEL == "action_map" or Nav_LABEL == "date_end":
                add "images/UI/Navigation/nav_map.webp" at Zoom_X(0.85) xalign 0.5 yalign 0.5
            else:
                add "images/BG/bg_sky1.webp" at Zoom_X(0.1285) xalign 0.5 yalign 0.5
                add "images/BG/"+Nav_IMG+".webp" at Zoom_X(0.1285) xalign 0.5 yalign 0.5
            at transform:
                on idle:
                    ButtonIdle2
                on hover:
                    ButtonHover2

            # Action
            if Nav_LABEL == "action_map":
                action Function(renpy.call, "goto_map")

            elif Nav_LABEL == "date_end":
                action Function(renpy.call, "date_end")

            else:
                if isinstance(Nav_LABEL, tuple):
                    if Nav_LABEL[0] == "msg":
                        action Function(msg.msg, Nav_LABEL[1])
                else:
                    action Function(renpy.call, Nav_LABEL)
                if preferences.text_mapbutton == True:
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        if Nav_TXT1 != None:
                            text renpy.translate_string("{b}")+Nav_TXT1+"{/b}" xalign 0.5 yalign 0.5 size 40 color "#323232" outlines [(3, "#FFF", 0, 0)]
                        if Nav_TXT2 != None:
                            text renpy.translate_string("{b}")+Nav_TXT2+"{/b}" xalign 0.5 yalign 0.5 size 40 color "#323232" outlines [(3, "#FFF", 0, 0)]
                        if Nav_TXT3 != None:
                            text renpy.translate_string("{b}")+Nav_TXT3+"{/b}" xalign 0.5 yalign 0.5 size 40 color "#323232" outlines [(3, "#FFF", 0, 0)]

# ----------------------------------------------------------------------------------------------------
# MAP
# ----------------------------------------------------------------------------------------------------
screen nav_map():
    hbox:
        spacing 10
        xalign 0.5
        yalign 0.95
        #xpos 25
        use NavButton("bg_home_facade", "goto_home_facade", "Home")
        if gametimehour <= 18:
            use NavButton("bg_grocerystore_facade", "action_map_store", "Convenience")
        if gametimehour <= 17:
            use NavButton("bg_school_facade", "goto_school_facade", "School")
        if (gametimehour >= 18 and gametimehour < 20) and (hero_quest_2 < 4 or hero_quest_3 >= 2) and (gametimeweek != "Sunday" and gametimeweek != "Saturday"):
            use NavButton("bg_office_facade", "goto_office_facade", "Office")

# ----------------------------------------------------------------------------------------------------
# HOME
# ----------------------------------------------------------------------------------------------------
screen nav_home_facade():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("nav_map", "action_map")
        use NavButton("bg_home_livingroom", "goto_home_livingroom", "Living", "Room")

screen nav_home_livingroom():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        if hero_quest_2 >= 2:
            use NavButton("bg_home_facade", "goto_home_facade", "Entrance")
        use NavButton("bg_home_hallway", "goto_home_hallway", "Hallway")

screen nav_home_hallway():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_home_livingroom", "goto_home_livingroom", "Living", "Room")
        use NavButton("bg_home_bedroom_hero", "goto_home_bedroom_hero", "My", "Bedroom")
        use NavButton("bg_home_bedroom_wsis", "goto_home_bedroom_wsis", "[C_Nam][hero_about_wsis][C_Off]'s", "Bedroom")
        use NavButton("bg_home_bedroom_wmom", "goto_home_bedroom_wmom", "[C_Nam][hero_about_wmom][C_Off]'s", "Bedroom")
        use NavButton("bg_home_bathroom", "goto_home_bathroom", "Bathroom")

screen nav_home_bedroom_hero():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_home_hallway", "goto_home_hallway", "Hallway")

screen nav_home_bedroom_wsis():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_home_hallway", "goto_home_hallway", "Hallway")

screen nav_home_bedroom_wmom():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_home_hallway", "goto_home_hallway", "Hallway")

screen nav_home_bathroom():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_home_hallway", "goto_home_hallway", "Hallway")

# ----------------------------------------------------------------------------------------------------
# OFFICE
# ----------------------------------------------------------------------------------------------------
screen nav_office_facade():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("nav_map", "action_map")
        if (gametimehour < 20 and gametimehour >= 18):
            use NavButton("bg_office_room", "goto_office_room", "Doctor's", "Office")

screen nav_office_room():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_office_facade", "goto_office_facade", "Entrance")

# ----------------------------------------------------------------------------------------------------
# SCHOOL
# ----------------------------------------------------------------------------------------------------
screen nav_school_facade():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        if (gametimeday == 2 and gametimehour >= 12) or gametimeday >= 3:
            use NavButton("nav_map", "action_map")
        use NavButton("bg_school_frontyard", "goto_school_frontyard", "Frontyard")

screen nav_school_frontyard():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_facade", "goto_school_facade", "{size=35}Entrance{/size}")
        use NavButton("bg_school_hallway1", "goto_school_hallway1", "{size=35}Downstairs{/size}", "{size=35}Hallway{/size}")

screen nav_school_courtyard():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_hallway1", "goto_school_hallway1", "{size=35}Downstairs{/size}", "{size=35}Hallway{/size}")
        if hero_quest_2 >= 2:
            use NavButton("bg_school_locker_m", "goto_school_locker_m", "{size=35}Male{/size}", "{size=35}Locker Room{/size}")
        if (hero_locker_f_access or club_stco_quest_1 == 1) and not hero_locker_f_ban:
            use NavButton("bg_school_locker_f", "goto_school_locker_f", "{size=35}Female{/size}", "{size=35}Locker Room{/size}")

screen nav_school_locker_m():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_courtyard", "goto_school_courtyard", "Courtyard")
        use NavButton("bg_school_pool", "goto_school_pool", "{size=35}Swimming{/size}", "{size=35}Area{/size}")
        use NavButton("bg_school_sportcourt", "goto_school_sportcourt", "{size=35}Sport{/size}", "{size=35}Court{/size}")

screen nav_school_locker_f():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_courtyard", "goto_school_courtyard", "Courtyard")
        use NavButton("bg_school_pool", "goto_school_pool", "{size=35}Swimming{/size}", "{size=35}Area{/size}")
        use NavButton("bg_school_sportcourt", "goto_school_sportcourt", "{size=35}Sport{/size}", "{size=35}Court{/size}")

screen nav_school_hallway1():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_frontyard", "goto_school_frontyard", "Frontyard")
        use NavButton("bg_school_courtyard", "goto_school_courtyard", "Courtyard")
        use NavButton("bg_school_library", "goto_school_library", "Library")
        use NavButton("bg_school_hallway2", "goto_school_hallway2", "{size=35}Upstairs{/size}", "{size=35}Hallway{/size}")

screen nav_school_hallway2():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_hallway1", "goto_school_hallway1", "{size=35}Downstairs{/size}", "{size=35}Hallway{/size}")
        if not Check_TimeStr("school_class"):
            use NavButton("bg_school_classroom_1a", "goto_school_classroom_1a", "Class 1A")
        else:
            use NavButton("bg_school_classroom_1a", ("msg", "Class 1A is at class"), "Class 1A")
        use NavButton("bg_school_classroom_1b", "goto_school_classroom_1b", "Class 1B")
        #use NavButton("bg_school_classroom_3a", "goto_school_classroom_3a", "Class 3A")
        if hine_quest_1 >= 1:
            use NavButton("bg_school_club_council", "goto_school_club_council", "Club", "{size=30}Student Council{/size}")

screen nav_school_classroom_1a():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_hallway2", "goto_school_hallway2", "{size=35}Upstairs{/size}", "{size=35}Hallway{/size}")

screen nav_school_classroom_1b():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_hallway2", "goto_school_hallway2", "{size=35}Upstairs{/size}", "{size=35}Hallway{/size}")

screen nav_school_classroom_3a():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_hallway2", "goto_school_hallway2", "{size=35}Upstairs{/size}", "{size=35}Hallway{/size}")

screen nav_school_library():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_hallway1", "goto_school_hallway1", "{size=35}Downstairs{/size}", "{size=35}Hallway{/size}")

screen nav_school_sportcourt():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_locker_m", "goto_school_locker_m", "{size=35}Male{/size}", "{size=35}Locker Room{/size}")
        if (hero_locker_f_access or club_stco_quest_1 == 1) and not hero_locker_f_ban:
            use NavButton("bg_school_locker_f", "goto_school_locker_f", "{size=35}Female{/size}", "{size=35}Locker Room{/size}")

screen nav_school_pool():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_locker_m", "goto_school_locker_m", "{size=35}Male{/size}", "{size=35}Locker Room{/size}")
        if (hero_locker_f_access or club_stco_quest_1 == 1) and not hero_locker_f_ban:
            use NavButton("bg_school_locker_f", "goto_school_locker_f", "{size=35}Female{/size}", "{size=35}Locker Room{/size}")

screen nav_school_club_council():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_school_hallway2", "goto_school_hallway2", "{size=35}Upstairs{/size}", "{size=35}Hallway{/size}")

# ----------------------------------------------------------------------------------------------------
# SHOPPING MALL
# ----------------------------------------------------------------------------------------------------
screen nav_shopping_facade():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        if date_active == True:
            use NavButton("nav_map", "date_end")
        else:
            use NavButton("nav_map", "action_map")
        use NavButton("bg_shopping_hall", "goto_shopping_hall", "Main Hall")

screen nav_shopping_hall():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_shopping_facade", "goto_shopping_facade", "Entrance")
        use NavButton("bg_shopping_cinema_entrance", "goto_shopping_cinema_entrance", "Cinema")
        use NavButton("bg_shopping_store_clothing", "goto_shopping_store_clothing", "Clothing Store")
        use NavButton("bg_shopping_store_arcade", "goto_shopping_store_arcade", "Arcade Store")
        use NavButton("bg_shopping_court_food", "goto_shopping_court_food", "Food Court")

screen nav_shopping_cinema_entrance():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_shopping_hall", "goto_shopping_hall", "Main Hall")

screen nav_shopping_store_clothing():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_shopping_hall", "goto_shopping_hall", "Main Hall")

screen nav_shopping_store_arcade():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_shopping_hall", "goto_shopping_hall", "Main Hall")

screen nav_shopping_court_food():
    hbox:
        spacing 20
        xalign 0.0
        yalign 1.0
        xpos 15
        yoffset -20
        use NavButton("bg_shopping_hall", "goto_shopping_hall", "Main Hall")

# ----------------------------------------------------------------------------------------------------
# CHAT
# ----------------------------------------------------------------------------------------------------
screen UI_chat():
    hbox:
        spacing 20
        xalign 0.0
        yalign 0.0
        xpos 20
        ypos 200
        frame:
            background None # "#00000032"
            side ("c l"):
                area (-10, 0, 1040, 330)
                vpgrid id "Scroll_UI_chat":
                    xoffset 20
                    draggable True
                    mousewheel True
                    spacing 20
                    cols 6
                    if hero_quest_2 != 1:
                        if Check_CharSameMap("hero", "wsis"):
                            imagebutton:
                                idle At("images/UI/OC_WSIS.webp", ButtonIdle)
                                hover At("images/UI/OC_WSIS.webp", ButtonHover)
                                action Function(renpy.call, "wsis_interact_start")
                        if Check_CharSameMap("hero", "wmom"):
                            imagebutton:
                                idle At("images/UI/OC_WMOM.webp", ButtonIdle)
                                hover At("images/UI/OC_WMOM.webp", ButtonHover)
                                action Function(renpy.call, "wmom_interact_start")
                        if Check_CharSameMap("hero", "wcou"):
                            imagebutton:
                                idle At("images/UI/OC_WCOU.webp", ButtonIdle)
                                hover At("images/UI/OC_WCOU.webp", ButtonHover)
                                action Function(renpy.call, "wcou_interact_start")
                        if Check_CharSameMap("hero", "wgma"):
                            imagebutton:
                                idle At("images/UI/OC_WGMA.webp", ButtonIdle)
                                hover At("images/UI/OC_WGMA.webp", ButtonHover)
                                action Function(renpy.call, "wgma_interact_start")
                                
                        if Check_CharSameMap("hero", "wnei") or (Get_ActivityName("wnei") in ["changing", "sleeping"] and Check_CharInMap("hero","home","bedroom_hero") and Check_CharInMap("wnei","neighbor","bedroom_wnei")):
                            imagebutton:
                                idle At("images/UI/OC_WNEI.webp", ButtonIdle)
                                hover At("images/UI/OC_WNEI.webp", ButtonHover)
                                action Function(renpy.call, "wnei_interact_start")
                        if Check_CharSameMap("hero", "wpre") and wpre_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_WPRE.webp", ButtonIdle)
                                hover At("images/UI/OC_WPRE.webp", ButtonHover)
                                action Function(renpy.call, "wpre_interact_start")
                        if Check_CharSameMap("hero", "wota") and wota_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_WOTA.webp", ButtonIdle)
                                hover At("images/UI/OC_WOTA.webp", ButtonHover)
                                action Function(renpy.call, "wota_interact_start")
                        if Check_CharSameMap("hero", "wdis") and wdis_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_WDIS.webp", ButtonIdle)
                                hover At("images/UI/OC_WDIS.webp", ButtonHover)
                                action Function(renpy.call, "wdis_interact_start")
                        if Check_CharSameMap("hero", "wgal") and wgal_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_WGAL.webp", ButtonIdle)
                                hover At("images/UI/OC_WGAL.webp", ButtonHover)
                                action Function(renpy.call, "wgal_interact_start")
                        if Check_CharSameMap("hero", "wric") and wric_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_WRIC.webp", ButtonIdle)
                                hover At("images/UI/OC_WRIC.webp", ButtonHover)
                                action Function(renpy.call, "wric_interact_start")
                        if Check_CharSameMap("hero", "wgot") and wgot_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_WGOT.webp", ButtonIdle)
                                hover At("images/UI/OC_WGOT.webp", ButtonHover)
                                action Function(renpy.call, "wgot_interact_start")
                        if Check_CharSameMap("hero", "wdel") and wdel_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_WDEL.webp", ButtonIdle)
                                hover At("images/UI/OC_WDEL.webp", ButtonHover)
                                action Function(renpy.call, "wdel_interact_start")
                        if Check_CharSameMap("hero", "wlaz") and wlaz_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_WLAZ.webp", ButtonIdle)
                                hover At("images/UI/OC_WLAZ.webp", ButtonHover)
                                action Function(renpy.call, "wlaz_interact_start")
                        if Check_CharSameMap("hero", "wuza") and wuza_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_WUZA.webp", ButtonIdle)
                                hover At("images/UI/OC_WUZA.webp", ButtonHover)
                                action Function(renpy.call, "wuza_interact_start")
                        if Check_CharSameMap("hero", "hriv") and hriv_quest[0] >= 1:
                            imagebutton:
                                idle At("images/UI/OC_HRIV.webp", ButtonIdle)
                                hover At("images/UI/OC_HRIV.webp", ButtonHover)
                                action Function(renpy.call, "hriv_interact_start")
                        if Check_CharSameMap("hero", "hprv") and hprv_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_HPRV.webp", ButtonIdle)
                                hover At("images/UI/OC_HPRV.webp", ButtonHover)
                                action Function(renpy.call, "hprv_interact_start")
                        if Check_CharSameMap("hero", "hine") and hine_quest_1 >= 1:
                            imagebutton:
                                idle At("images/UI/OC_HINE.webp", ButtonIdle)
                                hover At("images/UI/OC_HINE.webp", ButtonHover)
                                action Function(renpy.call, "hine_interact_start")
                vbar value YScrollValue("Scroll_UI_chat")

label gametimepassbutton:
    call hide_ui from _call_hide_ui_164
    menu:
        "Set custom time" if 0 > 1:
            call screen UI_Menu_TimeSet
            call gametime from _call_gametime_84

        "Pass X hours":
            $ a_menu_0 = int(renpy.input(renpy.translate_string("Set the amount of hours to skip"), length=2, allow="0123456789"))
            $ a_menu_1 = int(min(23, a_menu_0 + gametimehour))
            if isinstance(a_menu_1, int):
                call gametime_wait(target_hour=a_menu_1, target_min=0) from _call_gametime_wait_16
            else:
                $ msg.msg(renpy.translate_string("You should input an integer"))

        "Skip To Day Of Week":

            $ a_menu_0 = None

            menu:
                "Monday" if gametimeweek != "Monday":
                    $ a_menu_0 = "Monday"
                    $ a_menu_3 = "Sunday"

                "Tuesday" if gametimeweek != "Tuesday":
                    $ a_menu_0 = "Tuesday"
                    $ a_menu_3 = "Monday"

                "Wednesday" if gametimeweek != "Wednesday":
                    $ a_menu_0 = "Wednesday"
                    $ a_menu_3 = "Tuesday"

                "Thursday" if gametimeweek != "Thursday":
                    $ a_menu_0 = "Thursday"
                    $ a_menu_3 = "Wednesday"

                "Friday" if gametimeweek != "Friday":
                    $ a_menu_0 = "Friday"
                    $ a_menu_3 = "Thursday"

                "Saturday" if gametimeweek != "Saturday":
                    $ a_menu_0 = "Saturday"
                    $ a_menu_3 = "Friday"

                "Sunday" if gametimeweek != "Sunday":
                    $ a_menu_0 = "Sunday"
                    $ a_menu_3 = "Saturday"

                "Cancel":
                    pass

            if a_menu_0 is not None:
                $ a_menu_1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                $ a_menu_2 = (a_menu_1.index(a_menu_0) - a_menu_1.index(gametimeweek) - 1) % 7
                $ gametimeday += a_menu_2
                $ gametimeweek = a_menu_3
                call gametime_wait(target_hour=23, target_min=0) from _call_gametime_wait_17

        "Pass 1 hour":
            $ gametimemin = 60
            call gametime from _call_gametime_85

        "Pass +10 min":
            $ gametimemin += 10
            call gametime from _call_gametime_86

        "Return":
            pass

    jump show_ui

screen UI_Menu_TimeSet():
    zorder 200
    modal True
    
    # Store initial time when screen opens
    default initial_hour = gametimehour
    default initial_min = gametimemin
    
    frame:
        xpos 20
        xsize 1820
        ysize 1080
        
        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5
            
            label renpy.translate_string("Set Game Time") xalign 0.5
            
            # Calculate added time
            python:
                total_initial = initial_hour * 60 + initial_min
                total_current = gametimehour * 60 + gametimemin
                total_added = total_current - total_initial
                addhour = total_added // 60
                addmin = total_added % 60
                
                # Calculate maximum allowed values (cap at 23:00)
                max_hour = 23
                max_min = 0 if gametimehour >= 23 else 59
            
            # Hour adjustment
            vbox:
                spacing 10
                
                text renpy.translate_string("Hours: +[addhour]") size 24
                
                bar:
                    value VariableValue("gametimehour", max_hour, offset=initial_hour)
                    xsize 1000
                    ysize 50
            
            # Minute adjustment
            vbox:
                spacing 10
                
                text renpy.translate_string("Minutes: +[addmin]") size 24
                
                # Limit minutes based on current hour
                if gametimehour >= 23:
                    # If at or past 23:00, set to 23:00 exactly
                    bar:
                        value VariableValue("gametimemin", 0)
                        xsize 1000
                        ysize 50
                elif gametimehour == initial_hour:
                    # If hour hasn't changed, start from initial minute
                    bar:
                        value VariableValue("gametimemin", 59, offset=initial_min)
                        xsize 1000
                        ysize 50
                else:
                    # Normal range
                    bar:
                        value VariableValue("gametimemin", 59)
                        xsize 1000
                        ysize 50
            
            # Display current and maximum time
            text renpy.translate_string("Current Time: [gametimehour:02d]:[gametimemin:02d]") size 28 xalign 0.5
            text renpy.translate_string("Maximum: 23:00") size 20 xalign 0.5
            
            # Close button
            textbutton renpy.translate_string("Close") action Return() xalign 0.5

# ----------------------------------------------------------------------------------------------------
# ACTION
# ----------------------------------------------------------------------------------------------------
screen UI_action():
    hbox:
        spacing 20
        xalign 0.0
        yalign 0.0
        xpos 20
        ypos 545
        frame:
            background None # "#00000032"
            side ("c l"):
                area (-10, 0, 1040, 330)
                vpgrid id "Scroll_UI_action":
                    xoffset 20
                    draggable True
                    mousewheel True
                    spacing 20
                    cols 6
                    if not is_specialevent and gametimehour < 20 and not Check_CharInMap("hero", "home", "bathroom"):
                        imagebutton:
                            idle At("images/UI/QUICK_Time.webp", ButtonIdle)
                            hover At("images/UI/QUICK_Time.webp", ButtonHover)
                            action Jump("gametimepassbutton")

                    # TEST ONLY — Rig Builder (System - RigBuilder.rpy). Visible only when is_test.
                    if is_test and Check_CharInMap("hero", "home", "bedroom_hero"):
                        imagebutton:
                            idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                            action Function(renpy.call, "rig_builder")

                    # TEST ONLY — Dance chart recorder (Minigame - RhythmBPM.rpy). Visible only when is_test.
                    if is_test and Check_CharInMap("hero", "home", "living_room"):
                        imagebutton:
                            idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                            action Function(renpy.call, "dance_recorder")

                    # ----------------------------------------------------------------------------------------------------
                    # QUEST
                    # ----------------------------------------------------------------------------------------------------
                    if 0 > 1: # Easy to copy/paste followings
                        pass

                    # Early Morning
                    elif (gametimehour <= 7) and Check_CharInMap("hero", "home", "bedroom_hero") and Check_CharInMap("wnei", "neighbor", "bedroom_wnei") and (wnei_quest_2 >= 1) and (gametimeweek == "Saturday"):
                        imagebutton:
                            idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                            action Function(renpy.call, "action_quest")

                    elif gametimeweek in ["Sunday"] and gametimehour in [10, 11, 12] and Check_CharInMap("hero", "home", "facade") and wnei_quest_6 >= 1:
                        imagebutton:
                            idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                            action Function(renpy.call, "wnei_quest_6_0", get_guest=wnei_quest_7)
                                
                    # Before Class
                    elif Check_TimeStr("school_breaks_1") and hero_quest_2 != 1:
                        if Check_CharInMap("hero", "school", "hallway_2") and wric_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                        elif Check_CharInMap("hero", "school", "hallway_2") and wdel_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                        elif Check_CharInMap("hero", "school", "hallway_1") and wgot_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                    # After Class
                    elif Check_TimeStr("school_breaks_2"):
                        if Check_CharInMap("hero", "school", "hallway_1") and hprv_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                        elif Check_CharInMap("hero", "school", "class_1b") and wdis_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                    # During Class
                    elif Check_TimeStr("school_class"):
                        if Check_CharInMap("hero", "school", "swimming_pool") and wota_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                        elif Check_CharInMap("hero", "school", "sports_court") and (stat_phy >= 20) and (wtpe_quest != 1):
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                        elif Check_CharInMap("hero", "school", "sports_court") and wuza_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                        elif Check_CharInMap("hero", "school", "locker_m") and wlaz_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                        elif Check_CharInMap("hero", "school", "class_1b") and wpre_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                        elif Check_CharInMap("hero", "school", "class_1b") and wgal_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                        elif Check_CharInMap("hero", "school", "class_1b") and hine_quest_1 == 0:
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                    # After School Time
                    elif (gametimehour == 18):
                        if Check_CharInMap("hero", "school", "hallway_2") and hine_quest_1 > 0:
                            imagebutton:
                                idle At("images/UI/X_Dick.webp", ButtonIdle)
                                hover At("images/UI/X_Dick.webp", ButtonHover)
                                action Function(renpy.jump, "wsuk_quest_0_1")
                        
                    # Late Night
                    elif (gametimehour >= 19 and gametimehour < 21):
                        if Check_CharInMap("hero", "home", "living_room"):
                            imagebutton:
                                idle At("images/UI/ACTION_Quest.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Quest.webp", ButtonHover)
                                action Function(renpy.call, "action_quest")

                    # ----------------------------------------------------------------------------------------------------
                    # COMMON
                    # ----------------------------------------------------------------------------------------------------
                    # 2.1: cleaning is available anytime at home (was gated behind: and "Neighbors_Reunion" in wmom_know)
                    if is_specialevent == False and Check_CharInMap("hero", "home"):
                        imagebutton:
                            idle At("images/UI/ACTION_Clean.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Clean.webp", ButtonHover)
                            action Function(renpy.call, "action_clean_home")
                    # Sleep: any home map at sleep time; passday() fast-travels HERO to bedroom_hero first.
                    if is_specialevent == False and Check_CharInMap("hero", "home") and gametimehour >= 20:
                        imagebutton:
                            idle At("images/UI/ACTION_Sleep.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Sleep.webp", ButtonHover)
                            action Function(renpy.call, "goto_sleep")
                    if is_specialevent == False and Check_CharInMap("hero", "home", "bedroom_hero"):
                        #frame:
                            #background None
                            #xysize(150,150)
                            #text str(wnei_act[0])[4] xalign 0.5 yalign 0.6 size 40 color "#00FF00" outlines [(4, "#009600", 0, 0)]
                        if gametimehour < 23:
                            #if 0 > 1: # Disable
                            imagebutton:
                                idle At("images/UI/ACTION_LvlCha.webp", ButtonIdle)
                                hover At("images/UI/ACTION_LvlCha.webp", ButtonHover)
                                action Function(renpy.call, "action_train_home")
                            #imagebutton:
                                #idle At("images/UI/ACTION_LvlInt.webp", ButtonIdle)
                                #hover At("images/UI/ACTION_LvlInt.webp", ButtonHover)
                                #action Function(renpy.call, "action_trainINT")
                            #imagebutton:
                                #idle At("images/UI/ACTION_LvlPhy.webp", ButtonIdle)
                                #hover At("images/UI/ACTION_LvlPhy.webp", ButtonHover)
                                #action Function(renpy.call, "action_trainPHY")
                            #imagebutton:
                                #idle At("images/UI/ButtomBase_Circle IDLE.webp", ButtonIdle)
                                #hover At("images/UI/ButtomBase_Circle IDLE.webp", ButtonHover)
                                #action Function(renpy.call, "minigame_ludo")
                            #imagebutton:
                                #idle At("images/UI/ACTION_LvlCha.webp", ButtonIdle)
                                #hover At("images/UI/ACTION_LvlCha.webp", ButtonHover)
                                #action Jump("memory_game")
                            #imagebutton:
                                #idle At("images/UI/ButtomBase_Circle IDLE.webp", ButtonIdle)
                                #hover At("images/UI/ButtomBase_Circle IDLE.webp", ButtonHover)
                                #action Jump("buceta123")
                    if is_specialevent == False and Check_CharInMap("hero", "home", "living_room"):
                        imagebutton:
                            idle At("images/UI/ACTION_Fridge.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Fridge.webp", ButtonHover)
                            action Call("UI_Menu_Inventory_Transfer", toptype=["food", "drink", "ingredient"], bottype="any")
                    if is_specialevent == False and Check_CharInMap("hero", "home", "living_room") and stat_eat <= 80 and ((gametimehour == 6 and gametimemin >= 30) or (gametimehour >= 18 and gametimehour <= 19)):
                        imagebutton:
                            idle At("images/UI/ACTION_Eat.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Eat.webp", ButtonHover)
                            action Call("action_eat", 1)
                    if is_specialevent == False and Check_CharInMap("hero", "home", "living_room") and (Check_IfActivity(char_id="wsis", act_name="watching tv") and Check_CharSameMap("hero", "wsis")) or (Check_IfActivity(char_id="wmom", act_name="watching tv") and Check_CharSameMap("hero", "wmom")) or (Check_IfActivity(char_id="wnei", act_name="watching tv") and Check_CharSameMap("hero", "wnei")):
                        imagebutton:
                            idle At("images/UI/ACTION_WatchTV.webp", ButtonIdle)
                            hover At("images/UI/ACTION_WatchTV.webp", ButtonHover)
                            action Call("action_watchtv")
                    if is_specialevent == False and Check_CharInMap("hero", "home", "bathroom") or Check_CharInMap("hero", "school", "locker_m"):
                        imagebutton:
                            idle At("images/UI/ACTION_Bathe.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Bathe.webp", ButtonHover)
                            action Function(renpy.call, "action_bathe")
                        if Check_CharInMap("hero", "home", "bathroom"):
                            imagebutton:
                                idle At("images/UI/ACTION_Lock.webp", ButtonIdle)
                                hover At("images/UI/ACTION_Lock.webp", ButtonHover)
                                action Function(renpy.call, "action_lock")
                    # Shower quest: open female-locker stall doors while searching for the broken shower.
                    if is_specialevent == False and Check_CharInMap("hero", "school", "locker_f") and club_stco_quest_1 == 1:
                        imagebutton:
                            idle At("images/UI/ACTION_Door.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Door.webp", ButtonHover)
                            action Function(renpy.call, "action_locker_stalls")

                    #if (hero_map == "Home - Facade" or hero_map == "School - Facade" or hero_map == "Office Building - Facade") and hero_quest_2 >= 2 and not (hero_map == "Office Building - Facade" and hero_quest_2 == 3):
                        #imagebutton:
                            #idle At("images/UI/ACTION_Map.webp", ButtonIdle)
                            #hover At("images/UI/ACTION_Map.webp", ButtonHover)
                            #action Function(renpy.call, "action_map")
                    # Class: any school map with a scheduled class; action_study fast-travels HERO to its real room.
                    if Check_TimeStr("school_class") and Check_CharInMap("hero", "school") and Get_MapName("hero", map_main="at class") != "Unknown":
                        imagebutton:
                            idle At("images/UI/ACTION_Study.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Study.webp", ButtonHover)
                            action Function(renpy.call, "action_study")
                    if (gametimehour >= 12 and gametimehour <= 14) and Check_CharInMap("hero", "school", "club_coun"):
                        imagebutton:
                            idle At("images/UI/ACTION_Club.webp", ButtonIdle)
                            hover At("images/UI/ACTION_Club.webp", ButtonHover)
                            action Function(renpy.call, "club_studentcouncil")
                vbar value YScrollValue("Scroll_UI_action")

screen UI_stats():
    default hover_substat = None  # None | "int" | "phy" | "cha"

    frame:
        background None
        xsize 1920
        ypos 25
        xpadding 10
        ypadding 10

        hbox:
            xalign 0.0
            xpos 20
            spacing 80
            yalign 0.0

            vbox:
                spacing 10
                text renpy.translate_string("{b}[gametimeweek] [gametimeday], [gametimeclock]{/b}") size 40 color "#FFF" outlines [(2, "#323232", 0, 0)] xalign 0.0
                text renpy.translate_string("{b}[C_Map]")+str(hero_map)+"[C_Off]" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)] xalign 0.0

            vbox:
                spacing 4

                hbox:
                    spacing 40
                    yalign 0.0

                    hbox:
                        spacing 10
                        image "images/UI/ICON_StatHyg.webp"
                        text renpy.translate_string("{b}")+str(int(stat_hyg)).zfill(3)+"{/b}{p}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]

                    hbox:
                        spacing 10
                        image "images/UI/ICON_StatEne.webp"
                        text renpy.translate_string("{b}")+str(int(stat_ene)).zfill(3)+"{/b}{p}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]

                    # icon + number, with sub-stat tooltip below on hover
                    # INT pack
                    button:
                        xpadding 0
                        ypadding 0
                        background None
                        hover_background None
                        hover_sound None
                        activate_sound None
                        action NullAction()
                        hovered SetScreenVariable("hover_substat", "int")
                        unhovered If(hover_substat == "int", true=SetScreenVariable("hover_substat", None), false=NullAction())
                        hbox:
                            spacing 10
                            image "images/UI/ICON_StatInt.webp"
                            text renpy.translate_string("{b}")+str(int(stat_int)).zfill(3)+"{/b}{p}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]

                    # PHY pack
                    button:
                        xpadding 0
                        ypadding 0
                        background None
                        hover_background None
                        hover_sound None
                        activate_sound None
                        action NullAction()
                        hovered SetScreenVariable("hover_substat", "phy")
                        unhovered If(hover_substat == "phy", true=SetScreenVariable("hover_substat", None), false=NullAction())
                        hbox:
                            spacing 10
                            image "images/UI/ICON_StatPhy.webp"
                            text renpy.translate_string("{b}")+str(int(stat_phy)).zfill(3)+"{/b}{p}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]
                    # CHA pack
                    button:
                        xpadding 0
                        ypadding 0
                        background None
                        hover_background None
                        hover_sound None
                        activate_sound None
                        action NullAction()
                        hovered SetScreenVariable("hover_substat", "cha")
                        unhovered If(hover_substat == "cha", true=SetScreenVariable("hover_substat", None), false=NullAction())
                        hbox:
                            spacing 10
                            image "images/UI/ICON_StatCha.webp"
                            text renpy.translate_string("{b}")+str(int(stat_cha)).zfill(3)+"{/b}{p}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]

                    hbox:
                        spacing 10
                        image "images/UI/ICON_StatMon.webp"
                        if money < 1000:
                            text renpy.translate_string("{b}")+str("$" + str(round(money,2)).zfill(3)).ljust(9)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]
                        elif money < 1000000:
                            text renpy.translate_string("{b}")+str("$" + str(int(money/1000)).zfill(3) + "K").ljust(9)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]
                        elif money < 1000000000:
                            text renpy.translate_string("{b}")+str("$" + str(int(money/1000000)).zfill(3) + "M").ljust(9)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]
                        else:
                            text renpy.translate_string("{b}LOTS{/b}") size 40 color "#FFF" outlines [(3, "#323232", 0, 0)]

                if hover_substat == "int":
                    hbox:
                        xalign 0.5 spacing 40
                        hbox:
                            spacing 10
                            add "images/UI/Talent/TalentICON OBS.webp" size (60, 60)
                            text renpy.translate_string("{b}")+str(int(stat_int_per)).zfill(2)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]
                        hbox:
                            spacing 10
                            add "images/UI/Talent/TalentICON KNW.webp" size (60, 60)
                            text renpy.translate_string("{b}")+str(int(stat_int_mem)).zfill(2)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]
                        hbox:
                            spacing 10
                            add "images/UI/Talent/TalentICON SNS.webp" size (60, 60)
                            text renpy.translate_string("{b}")+str(int(stat_int_log)).zfill(2)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]

                if hover_substat == "phy":
                    hbox:
                        xalign 0.5 spacing 40
                        hbox:
                            spacing 10
                            add "images/UI/Talent/TalentICON STR.webp" size (60, 60)
                            text renpy.translate_string("{b}")+str(int(stat_phy_str)).zfill(2)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]
                        hbox:
                            spacing 10
                            add "images/UI/Talent/TalentICON AGI.webp" size (60, 60)
                            text renpy.translate_string("{b}")+str(int(stat_phy_agi)).zfill(2)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]
                        hbox:
                            spacing 10
                            add "images/UI/Talent/TalentICON RES.webp" size (60, 60)
                            text renpy.translate_string("{b}")+str(int(stat_phy_res)).zfill(2)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]

                if hover_substat == "cha":
                    hbox:
                        xalign 0.5 spacing 40
                        hbox:
                            spacing 10
                            add "images/UI/Talent/TalentICON SEX.webp" size (60, 60)
                            text renpy.translate_string("{b}")+str(int(stat_cha_sex)).zfill(2)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]
                        hbox:
                            spacing 10
                            add "images/UI/Talent/TalentICON PRF.webp" size (60, 60)
                            text renpy.translate_string("{b}")+str(int(stat_cha_per)).zfill(2)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]
                        hbox:
                            spacing 10
                            add "images/UI/Talent/TalentICON CRM.webp" size (60, 60)
                            text renpy.translate_string("{b}")+str(int(stat_cha_soc)).zfill(2)+"{/b}" size 40 color "#FFF" outlines [(2, "#323232", 0, 0)]

screen UI_stats_LOCKED():

    $ show_cha = str(int(stat_cha)).zfill(2)
    $ show_int = str(int(stat_int)).zfill(2)
    $ show_phy = str(int(stat_phy)).zfill(2)
    $ show_money = str("$" + str(money) + ".00").ljust(9)

    frame:
        background Frame("images/UI/BG1.webp")

    hbox:
        yalign 0.01
        xalign 0.02
        spacing 25
        imagebutton:
            idle "images/UI/QUICK_Time.webp"
            hover "images/UI/QUICK_Time.webp"
        text renpy.translate_string("[gametimeweek] [gametimeday], [gametimeclock]")
    hbox:
        yalign 0.01
        xalign 0.5
        spacing 30
        image "images/UI/ICON_StatInt.webp"
        text renpy.translate_string("[show_int] ")
        image "images/UI/ICON_StatPhy.webp"
        text renpy.translate_string("[show_phy] ")
        image "images/UI/ICON_StatCha.webp"
        text renpy.translate_string("[show_cha] ")
        image "images/UI/ICON_StatMon.webp"
        text renpy.translate_string("[show_money]")

screen UI_items():
    vbox:
        yalign 0.5
        xalign 1.0
        spacing 100
        xoffset -110
        # yoffset -25
        # cols 6
        imagebutton:
            idle "images/UI/MENU_Option IDLE.webp"
            hover "images/UI/MENU_Option HOVER.webp"
            action Function(renpy.jump, "UI_Menu_Options")
        imagebutton:
            idle "images/UI/MENU_Items IDLE.webp"
            hover "images/UI/MENU_Items HOVER.webp"
            action Function(renpy.jump, "UI_Menu_Inventory")
        imagebutton:
            idle "images/UI/MENU_Guide IDLE.webp"
            hover "images/UI/MENU_Guide HOVER.webp"
            action Function(renpy.jump, "UI_Menu_Guide")

screen TwoPicas():
    hbox:
        xalign 1.0
        frame:
            area (0,0,970,1100)
            viewport id "right_side":
                draggable False
                scrollbars None
                hbox:
                    image "images/Scene/[picaR].webp" xoffset picaR_N


# --------------------------------------------------
screen quick_menu(): # The Quick Menu is displayed in-game to provide easy access to the out-of-game menus.
# --------------------------------------------------

    zorder 999 # Ensure this appears on top of other screens.
    
    if not Is_ScreenShowing(("UI_Menu_Options_Gallery_IMG", "LoadingCheckpoint", "minigame_find", "minigame_memory", "minigame_logic", "minigame_sequence", "minigame_balance", "minigame_thugofwar")):

        $ tooltip = GetTooltip()
        #$ TT_Body = GetTooltip()

        frame:
            xysize(900, 120)
            xalign 0.5
            yalign 0.15
            if tooltip:
                background "#00000064"
                text renpy.translate_string("[tooltip]") size 40 xalign 0.5 yalign 0.5
            else:
                background None


        frame:
            xysize(100, 1080)
            xalign 1.0
            if not Is_ScreenShowing(("UI_give_Item", "UI_show_Item", "UI_show_Database", "UI_Menu", "UI_Menu_Options_Gallery", "UI_Menu_Options_Settings", "UI_Menu_Options_Music", "UI_Menu_Options_KCC", "UI_Menu_Options_Contacts", "UI_Menu_Options_Skill")):
                background None
            vbox:
                xalign 0.5
                yalign 1.0
                spacing 60
                if quick_menu:
                    imagebutton at Zoom_04:
                        idle At(At("images/UI/SUBMENU_Option_Quit.webp", ButtonIdle), outline_transform(5, "#FFF", 5.0))
                        hover At(At("images/UI/SUBMENU_Option_Quit.webp", ButtonHover), outline_transform(5, "#FFF", 5.0))
                        tooltip renpy.translate_string("{b}Quit:{/b} Leaves the screen or the game")
                        if Is_ScreenShowing(("UI_show_Item", "UI_show_Database", "UI_Menu")):
                            action Jump("show_ui") xalign 0.5
                        else:
                            action Quit(confirm=not main_menu) xalign 0.5
                    frame:
                        background None
                        xsize 60 ysize 60 xalign 0.5 yalign 0.5
                        imagebutton at Zoom_04:
                            idle At(At("images/UI/SUBMENU_Option_Settings.webp", ButtonIdle_Rotate), outline_transform(5, "#FFF", 5.0))
                            hover At(At("images/UI/SUBMENU_Option_Settings.webp", ButtonHover_Rotate), outline_transform(5, "#FFF", 5.0))
                            action ShowMenu("preferences") xalign 0.5 yalign 0.5
                            tooltip renpy.translate_string("{b}Settings:{/b} Enters on game Main Menu")
                            #TT_Body "Enters on game Main Menu"
                    imagebutton at Zoom_04:
                        idle At(At("images/UI/SUBMENU_Option_Rollback.webp", ButtonIdle), outline_transform(5, "#FFF", 5.0))
                        hover At(At("images/UI/SUBMENU_Option_Rollback.webp", ButtonHover), outline_transform(5, "#FFF", 5.0))
                        action Rollback()
                        tooltip renpy.translate_string("{b}Rollback:{/b} Turn back to previous actions")
                        xalign 0.5
                    if config.skipping == "slow" or config.skipping == "fast":
                        imagebutton at Zoom_04:
                            idle At(At("images/UI/SUBMENU_Option_Skip.webp", ButtonIdle), outline_transform(14, "#FFF", 5.0))
                            hover At(At("images/UI/SUBMENU_Option_Skip.webp", ButtonHover), outline_transform(14, "#FFF", 5.0))
                            action Skip() alternate Skip(fast=True, confirm=True)
                            tooltip renpy.translate_string("{b}Skip:{/b} Quickly pass through dialogues")
                            xalign 0.5
                    else:
                        imagebutton at Zoom_04:
                            idle At(At("images/UI/SUBMENU_Option_Skip.webp", ButtonIdle), outline_transform(5, "#FFF", 5.0))
                            hover At(At("images/UI/SUBMENU_Option_Skip.webp", ButtonHover), outline_transform(5, "#FFF", 5.0))
                            action Skip() alternate Skip(fast=True, confirm=True)
                            tooltip renpy.translate_string("{b}Skip:{/b} Quickly pass through dialogues")
                            xalign 0.5
                    frame:
                        background None
                        xsize 60 ysize 60 xalign 0.5 yalign 0.5
                        button:
                            if _preferences.afm_enable:
                                add At("images/UI/SUBMENU_Option_Autoplay_Circle.webp", Zoom_04, ButtonHover_Rotate, outline_transform(2, "#FFF", 5.0)) xalign 0.5 yalign 0.5
                            else:
                                add At("images/UI/SUBMENU_Option_Autoplay_Circle.webp", outline_transform(5, "#FFF", 5.0)) at Zoom_04 xalign 0.5 yalign 0.5
                            add At("images/UI/SUBMENU_Option_Autoplay_Play.webp", outline_transform(5, "#FFF", 5.0)) at Zoom_04 xalign 0.5 yalign 0.5
                            at transform:
                                on idle:
                                    ButtonIdle
                                on hover:
                                    ButtonHover
                            action Preference("auto-forward", "toggle")
                            tooltip renpy.translate_string("{b}Auto Play:{/b} Automatically passes to next dialogue without needing to click")
                    imagebutton at Zoom_04:
                        idle At(At("images/UI/SUBMENU_Option_Save.webp", ButtonIdle), outline_transform(5, "#FFF", 5.0))
                        hover At(At("images/UI/SUBMENU_Option_Save.webp", ButtonHover), outline_transform(5, "#FFF", 5.0))
                        action QuickSave()
                        tooltip renpy.translate_string("{b}Quick Save:{/b} Saves in a Quick Slot ('Q' section in saves)")
                        xalign 0.5
                    imagebutton at Zoom_04:
                        idle At(At("images/UI/SUBMENU_Option_Load.webp", ButtonIdle), outline_transform(5, "#FFF", 5.0))
                        hover At(At("images/UI/SUBMENU_Option_Load.webp", ButtonHover), outline_transform(5, "#FFF", 5.0))
                        action HideInterface()
                        tooltip renpy.translate_string("{b}Quick Load:{/b} Loads last save in Quick Slot ('Q' section in saves)")
                        xalign 0.5
                    imagebutton at Zoom_04:
                        idle At(At("images/UI/SUBMENU_GalleryShow.webp", ButtonIdle), outline_transform(5, "#FFF", 5.0))
                        hover At(At("images/UI/SUBMENU_GalleryHide.webp", ButtonHover), outline_transform(5, "#FFF", 5.0))
                        action HideInterface()
                        tooltip renpy.translate_string("{b}Hide:{/b} Hides interface")
                        xalign 0.5
                imagebutton at Zoom_04:
                    idle At(At("images/UI/SUBMENU_Option_Menu.webp", ButtonIdle), outline_transform(5, "#FFF", 5.0))
                    hover At(At("images/UI/SUBMENU_Option_Menu.webp", ButtonHover), outline_transform(5, "#FFF", 5.0))
                    action ToggleVariable("quick_menu") xalign 0.5
                    tooltip renpy.translate_string("{b}Quick Menu:{/b} Hides or expand quick menu buttons")

# This code ensures that the quick_menu screen is displayed in-game, whenever the player has not explicitly hidden the interface.
init python:

    config.overlay_screens.append("quick_menu")

    def Is_ScreenShowing(screen_id=None):
        # Check all screens that match your prefixes
        all_screens = renpy.display.screen.screens
        for screen_name in all_screens.keys():
            if screen_id == None:
                if screen_name[0].startswith(("UI_", "nav_", "bg_map_", "SkipScene")):
                    if renpy.get_screen(screen_name[0]):
                        return True
            else:
                if screen_name[0].startswith(screen_id):
                    if renpy.get_screen(screen_name):
                        return True
        return False

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines [ (1, "#646464", 0, 0) ]
