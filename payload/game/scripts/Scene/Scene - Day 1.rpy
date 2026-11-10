image BG_Peach = Movie(play="images/BG/bg_3 peach.webm", loop=True)

# --------------------------------------------------
# Transforms
# --------------------------------------------------
transform campaign_panel_dark:
    matrixcolor SaturationMatrix(0.3) * BrightnessMatrix(-0.35)

transform campaign_panel_bright:
    matrixcolor SaturationMatrix(1.2) * BrightnessMatrix(0.0)

transform campaign_btn_idle:
    zoom 1.0
    alpha 0.9

transform campaign_btn_hover:
    zoom 1.05
    alpha 1.0

# ==================================================
# Checkpoint Helpers
# ==================================================
init python:
    # Quest lists come from CONTENT_DATA (Data - Content.rpy), so a new entry there gets its toggle here on its own.
    def cp_toggle_content(entry):
        Content_Set(entry, Content_Value(entry) < entry["goal"])
        renpy.restart_interaction()

    def cp_set_all_quests(val):
        for entry in Content_Checkpoint("hero"):
            Content_Set(entry, val)
        for owner, entries in Content_Checkpoint():
            for entry in entries:
                Content_Set(entry, val)
        renpy.restart_interaction()

    # HERO's quests chain: turning one on completes the earlier ones, turning it off clears it and the later ones.
    def cp_set_scenestep(var_name, val):
        quest_order = [(e["var"], e["goal"]) for e in reversed(Content_Checkpoint("hero"))]
        names = [v for v, _ in quest_order]
        idx = names.index(var_name)
        setattr(store, var_name, val)
        if val > 0:
            for earlier_name, earlier_max in quest_order[:idx]:
                setattr(store, earlier_name, earlier_max)
        else:
            for later_name, _ in quest_order[idx:]:
                setattr(store, later_name, 0)
        renpy.restart_interaction()

    def cp_toggle_inti(char_id):
        key = char_id + "_inti"
        if getattr(store, key) >= 100:
            setattr(store, key, 0)
        else:
            setattr(store, key, 100)
        renpy.restart_interaction()

    def cp_set_all_inti(val):
        for cid in Content_Owners():
            if cid in CHAR_IDS:
                setattr(store, cid + "_inti", val)
        renpy.restart_interaction()

    def cp_all_quests_on():
        if not all(Content_Value(e) >= e["goal"] for e in Content_Checkpoint("hero")):
            return False
        return all(Content_Value(e) >= e["goal"] for owner, entries in Content_Checkpoint() for e in entries)

    def cp_all_inti_max():
        for cid in Content_Owners():
            if cid in CHAR_IDS:
                if getattr(store, cid + "_inti", 0) < 100:
                    return False
        return True

    def cp_apply_boost_and_start():
        if store.cp_stat_boost:
            store.stat_cha_bonus = 400
            store.stat_int_bonus = 400
            store.stat_phy_bonus = 400
        # Land on the day of HERO's first quest left off, read from its "start" in CONTENT_DATA, or on the last quest's day once all are on.
        hero_quests = list(reversed(Content_Checkpoint("hero")))
        store.is_skipable = next((e["start"] for e in hero_quests if Content_Value(e) < e["goal"]), hero_quests[-1]["start"])

# ==================================================
# Checkpoint Screen
# ==================================================
screen campaign_checkpoint():
    modal True
    zorder 200

    python:
        cp_hero_steps = [(e["var"], e["title"], e["goal"]) for e in reversed(Content_Checkpoint("hero"))]
        cp_data = Content_Checkpoint()

    # Default "Skip Character Creation" to match Global Data setting
    on "show" action If(preferences.is_namepersistent, SetVariable("preferences.is_skipcharcreate", True), SetVariable("preferences.is_skipcharcreate", False))

    # Dark backdrop
    button:
        background Solid("#000000CC")
        xysize (1920, 1080)
        action NullAction()

    # Main panel
    frame:
        background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
        xsize 1920
        ysize 1080
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 25

        vbox:
            spacing 20
            xfill True

            # --- Header ---
            text renpy.translate_string("{b}Checkpoint Configuration{/b}"):
                xalign 0.5
                color "#f0d878"
                size 50
                outlines [(2, "#1a1000", 0, 0), (4, "#000000", 0, 0)]

            # --- Bulk actions ---
            hbox:
                xalign 0.5
                spacing 100

                $ skip_cc_icon = "{color=#14C814}☑{/color}" if preferences.is_skipcharcreate else "{color=#C81414}☐{/color}"
                textbutton skip_cc_icon + " Skip Character Creation":
                    text_size 35
                    text_outlines [(1, "#000000", 0, 0)]
                    padding (10, 5, 10, 5)
                    background Solid("#FFFFFF10")
                    hover_background Solid("#FFFFFF25")
                    sensitive preferences.is_namepersistent
                    action ToggleVariable("preferences.is_skipcharcreate")

                $ boost_icon = "{color=#14C814}☑{/color}" if cp_stat_boost else "{color=#C81414}☐{/color}"
                textbutton boost_icon + " Stat Rate x5":
                    text_size 35
                    text_outlines [(1, "#000000", 0, 0)]
                    padding (10, 5, 10, 5)
                    background Solid("#FFFFFF10")
                    hover_background Solid("#FFFFFF25")
                    action ToggleVariable("cp_stat_boost")

                $ quests_on = cp_all_quests_on()
                textbutton ("{color=#14C814}☑{/color}" if quests_on else "{color=#C81414}☐{/color}") + " All Quests":
                    text_size 35
                    text_outlines [(1, "#000000", 0, 0)]
                    padding (10, 5, 10, 5)
                    background Solid("#FFFFFF10")
                    hover_background Solid("#FFFFFF25")
                    action Function(cp_set_all_quests, 0 if quests_on else 1)

                $ inti_max = cp_all_inti_max()
                textbutton ("{color=#FF6496}♥{/color}" if inti_max else "{color=#646464}♡{/color}") + " All Intimacy":
                    text_size 35
                    text_outlines [(1, "#000000", 0, 0)]
                    padding (10, 5, 10, 5)
                    background Solid("#FFFFFF10")
                    hover_background Solid("#FFFFFF25")
                    action Function(cp_set_all_inti, 0 if inti_max else 100)

            # --- Separator ---
            add Solid("#FFFFFF32") xsize 1820 ysize 5 xalign 0.5

            # --- Character list (scrollable) ---
            viewport:
                xfill True
                ysize 760
                mousewheel True
                draggable True
                scrollbars "vertical"

                vbox:
                    spacing 25
                    xfill True

                    # ===========================
                    # HERO - Story Checkpoints
                    # ===========================
                    hbox:
                        spacing 25
                        ysize 70
                        xfill True

                        hbox:
                            xsize 520
                            xalign 0.0
                            spacing 25

                            # Hero icon
                            fixed:
                                xsize 150
                                ysize 150
                                add "images/UI/OC_HERO.webp":
                                    #zoom 0.35
                                    yalign 0.5
                                    xalign 0.5

                            # Hero label
                            text renpy.translate_string("{b}HERO{/b}"):
                                yalign 0.5
                                color "#f0d878"
                                size 40
                                min_width 60
                                outlines [(1, "#000000", 0, 0)]

                        # Story checkpoint buttons
                        vbox:
                            xsize 1400
                            spacing 20
                            xalign 0.0
                            yalign 0.5

                            for step_var, step_label, step_max in cp_hero_steps:
                                $ is_active = (getattr(store, step_var) >= step_max)

                                textbutton ("{color=#14C814}☑{/color} " + step_label if is_active else "{color=#C81414}☐{/color} " + step_label):
                                    xalign 0.0
                                    yalign 0.5
                                    text_size 35
                                    text_outlines [(1, "#000000", 0, 0)]
                                    padding (10, 5, 10, 5)
                                    background Solid("#FFFFFF10")
                                    hover_background Solid("#FFFFFF25")
                                    action Function(cp_set_scenestep, step_var, 0 if is_active else step_max)

                        # Spacer
                        null width 10

                    add Solid("#FFFFFF32") xsize 1820 ysize 1 xalign 0.5

                    # ===========================
                    # NPC Characters
                    # ===========================
                    for char_id, char_quests in cp_data:
                        hbox:
                            spacing 25
                            ysize 70
                            xfill True

                            hbox:
                                xsize 520
                                xalign 0.0
                                spacing 25

                                # Character icon
                                fixed:
                                    xsize 150
                                    ysize 150
                                    add ("images/UI/OC_" + char_id.upper() + ".webp" if renpy.loadable("images/UI/OC_" + char_id.upper() + ".webp") else "images/UI/OC_NONE.webp"):
                                        #zoom 0.5
                                        yalign 0.5
                                        xalign 0.5

                                vbox:
                                    # Character ID label
                                    text renpy.translate_string("{b}") + char_id.upper() + "{/b}":
                                        xalign 0.5
                                        color "#c8aa6e"
                                        size 40
                                        min_width 60
                                        outlines [(1, "#000000", 0, 0)]

                                    # Intimacy toggle
                                    if char_id in CHAR_IDS:
                                        $ inti_val = getattr(store, char_id + "_inti", 0)

                                        textbutton ("{color=#FF6496}♥ " + str(int(inti_val)) + "{/color}" if inti_val >= 100 else "{color=#646464}♡ " + str(int(inti_val)) + "{/color}"):
                                            yalign 0.5
                                            xalign 0.5
                                            text_size 35
                                            text_outlines [(1, "#000000", 0, 0)]
                                            padding (10, 5, 10, 5)
                                            background Solid("#FFFFFF10")
                                            hover_background Solid("#FFFFFF25")
                                            action Function(cp_toggle_inti, char_id)

                            # Quest toggles
                            vbox:
                                xsize 1400
                                spacing 20
                                xalign 0.0
                                yalign 0.5

                                for quest in char_quests:
                                    $ q_on = Content_Value(quest) >= quest["goal"]

                                    textbutton ("{color=#14C814}☑{/color} " + quest["title"] if q_on else "{color=#C81414}☐{/color} " + quest["title"]):
                                        xalign 0.0
                                        yalign 0.5
                                        text_size 35
                                        text_outlines [(1, "#000000", 0, 0)]
                                        padding (10, 5, 10, 5)
                                        background Solid("#FFFFFF10")
                                        hover_background Solid("#FFFFFF25")
                                        action Function(cp_toggle_content, quest)

                            # Spacer
                            null width 10

                        add Solid("#FFFFFF32") xsize 1820 ysize 1 xalign 0.5

            # --- Bottom buttons ---
            hbox:
                xalign 0.5
                spacing 40

                textbutton renpy.translate_string("Return"):
                    xminimum 200
                    text_xalign 0.5
                    text_color "#c8aa6e"
                    text_hover_color "#ffffff"
                    text_size 26
                    text_bold True
                    text_outlines [(2, "#000000", 0, 0)]
                    background Frame("gui/button/choice_idle_background.png", 20, 10)
                    hover_background Frame("gui/button/choice_hover_background.png", 20, 10)
                    padding (30, 10, 30, 10)
                    action Hide("campaign_checkpoint")

                textbutton renpy.translate_string("Start"):
                    xminimum 200
                    text_xalign 0.5
                    text_color "#f0d878"
                    text_hover_color "#ffffff"
                    text_size 26
                    text_bold True
                    text_outlines [(2, "#000000", 0, 0)]
                    background Frame("gui/button/choice_idle_background.png", 20, 10)
                    hover_background Frame("gui/button/choice_hover_background.png", 20, 10)
                    padding (30, 10, 30, 10)
                    action [Function(cp_apply_boost_and_start), Hide("campaign_checkpoint"), Return()]

# --------------------------------------------------
# Screen
# --------------------------------------------------
screen campaign_select():
    # Track which panel is selected (None = all collapsed)
    default _selected_panel = None

    # Panel definitions: (id, title, subtitle, buttons_list)
    # buttons_list = [(label, action), ...]
    python:
        panels = [
            {
                "id": "day1",
                "title": "Memories",
                "subtitle": "Start from 1st day",
                "image": "images/UI/Guide/Intro_1.webp",
                "buttons": [
                    ("Start", [
                        Function(cp_set_all_quests, 0),
                        SetVariable("is_skipable", False), Return(),
                        ]),
                    ("Skip Intro", [SetVariable("is_skipable", "Day1"), Return()]),
                ]
            },
            {
                "id": "day2",
                "title": "City Life",
                "subtitle": "Start from 2nd day",
                "image": "images/UI/Guide/Intro_2.webp",
                "buttons": [
                    ("Start", [
                        Function(cp_set_all_quests, 0),
                        SetVariable("stat_cha_bonus", stat_cha_bonus + 50),
                        SetVariable("stat_phy_bonus", stat_phy_bonus + 50),
                        SetVariable("stat_int_bonus", stat_int_bonus + 50),
                        SetVariable("is_skipable", "Day2"),
                        SetVariable("xp_now", xp_now + 15),
                        Return()
                    ]),
                ]
            },
            {
                "id": "day3",
                "title": "A New Journey",
                "subtitle": "Start from 3rd day",
                "image": "images/UI/Guide/Intro_3.webp",
                "buttons": [
                    ("Start", [
                        Function(cp_set_all_quests, 0),
                        SetVariable("stat_cha_bonus", stat_cha_bonus + 100),
                        SetVariable("stat_phy_bonus", stat_phy_bonus + 100),
                        SetVariable("stat_int_bonus", stat_int_bonus + 100),
                        SetVariable("is_skipable", "Day3"),
                        SetVariable("xp_now", xp_now + 45),
                        Return()
                    ]),
                ]
            },
            {
                "id": "custom",
                "title": "Custom",
                "subtitle": "Your Rules",
                "image": "images/UI/Guide/Intro_4.webp",
                "buttons": [
                    ("Configure", [Function(cp_set_all_quests, 1), Function(cp_set_all_inti, 100), Show("campaign_checkpoint")]),
                ]
            },
        ]

        total_panels = len(panels)
        if _selected_panel is not None:
            expanded_w = 760
            collapsed_w = int((1920 - expanded_w) / (total_panels - 1))
        else:
            expanded_w = 0
            collapsed_w = int(1920 / total_panels)

    # Full black background
    add Solid("#0a0a0f")

    hbox:
        xsize 1920
        ysize 1080
        spacing 0

        for panel in panels:
            $ is_selected = (_selected_panel == panel["id"])
            $ pw = expanded_w if is_selected else collapsed_w

            button:
                xsize pw
                ysize 1080
                padding (0, 0, 0, 0)
                background None
                hover_background None
                action SetScreenVariable("_selected_panel", panel["id"] if not is_selected else None)

                fixed:
                    xsize pw
                    ysize 1080

                    # --- Background Image (cropped to center) ---
                    # We crop from the center of a 1920x1080 image
                    # xoffset centers the crop window on the image
                    viewport:
                        xsize pw
                        ysize 1080
                        xinitial 0.5
                        child_size (1920, 1080)
                        mousewheel False
                        draggable False

                        add panel["image"]:
                            at (campaign_panel_bright if is_selected else campaign_panel_dark)

                    # --- Dark gradient overlay on collapsed panels ---
                    if not is_selected:
                        # Vertical edge darkening
                        add Solid("#00000066"):
                            xsize pw
                            ysize 1080

                    # --- Vertical border lines ---
                    # Left border
                    add Solid("#c8aa6e"):
                        xsize 2
                        ysize 1080
                        xpos 0
                    # Right border
                    add Solid("#c8aa6e"):
                        xsize 2
                        ysize 1080
                        xalign 1.0

                    # --- COLLAPSED: Show vertical title ---
                    if not is_selected:
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 10

                            # Title (displayed letter-by-letter vertically)
                            text renpy.translate_string(panel["title"]):
                                xalign 0.5
                                text_align 0.5
                                color "#c8aa6e"
                                outlines [(2, "#1a1000", 0, 0), (4, "#000000", 0, 0)]
                                size 42
                                bold True
                                font (gui.interface_text_font if preferences.language == "zh" else "DejaVuSans.ttf")

                    # --- EXPANDED: Show full content ---
                    else:
                        # Top section: title area
                        vbox:
                            xalign 0.5
                            yalign 0.0
                            yoffset 40
                            spacing 5

                            text renpy.translate_string(panel["subtitle"]):
                                xalign 0.5
                                text_align 0.5
                                color "#c8aa6e"
                                outlines [(2, "#1a1000", 0, 0), (4, "#000000", 0, 0)]
                                size 24
                                italic True
                                font (gui.interface_text_font if preferences.language == "zh" else "DejaVuSans.ttf")

                            text renpy.translate_string(panel["title"]):
                                xalign 0.5
                                text_align 0.5
                                color "#f0d878"
                                outlines [(2, "#1a1000", 0, 0), (6, "#000000", 0, 0)]
                                size 56
                                bold True
                                font (gui.interface_text_font if preferences.language == "zh" else "DejaVuSans.ttf")

                        # Bottom section: action buttons
                        vbox:
                            xalign 0.5
                            yalign 1.0
                            yoffset -80
                            spacing 16

                            for btn in panel["buttons"]:
                                # btn[0] = label text, btn[1] = action list
                                textbutton renpy.translate_string(btn[0]):
                                    xalign 0.5
                                    xminimum 280
                                    yminimum 54
                                    text_xalign 0.5
                                    text_color "#f0d878"
                                    text_hover_color "#ffffff"
                                    text_size 28
                                    text_bold True
                                    text_font (gui.interface_text_font if preferences.language == "zh" else "DejaVuSans.ttf")
                                    text_outlines [(2, "#1a1000", 0, 0), (3, "#000000", 0, 0)]
                                    background Frame("gui/button/choice_idle_background.png", 20, 10)
                                    hover_background Frame("gui/button/choice_hover_background.png", 20, 10)
                                    padding (30, 10, 30, 10)
                                    at transform:
                                        on idle:
                                            ease 0.15 zoom 1.0 alpha 0.9
                                        on hover:
                                            ease 0.15 zoom 1.05 alpha 1.0
                                    action btn[1]

                        # Bonus info for Day 2 and Day 3
                        if panel["id"] == "day2":
                            text renpy.translate_string("{size=20}{color=#c8aa6e}[C_Pos]+50%[C_Off] stat bonus{/color}{/size}"):
                                xalign 0.5
                                yalign 1.0
                                yoffset -40
                                text_align 0.5
                                outlines [(2, "#000000", 0, 0)]

                        elif panel["id"] == "day3":
                            text renpy.translate_string("{size=20}{color=#c8aa6e}[C_Pos]+100%[C_Off] stat bonus{/color}{/size}"):
                                xalign 0.5
                                yalign 1.0
                                yoffset -40
                                text_align 0.5
                                outlines [(2, "#000000", 0, 0)]


# --------------------------------------------------
# How to call it (replaces your old menu)
# --------------------------------------------------
# label your_label:
#     call screen campaign_select
#     # After the screen returns, is_skipable is already set
#     # Continue with your existing logic...

label start:
    stop BGM fadeout 3

    # ----------------------------------------------------------------------------------------------------
    if is_test == True: # TESTE
    # ----------------------------------------------------------------------------------------------------
        scene bg_1
        $ X_pos = 200
        show WMOM at X
        $ X_pos = 700
        show WGMA at X
        $ X_pos = 1200
        show WCOU at X
        $ X_pos = 1700
        show WSIS at X

        pause

    # ----------------------------------------------------------------------------------------------------
    $ a_check_0 = 0
    $ a_check_1 = 0
    $ a_check_2 = 0
    $ a_check_3 = "charcreator1"
    $ a_check_4 = 0
    $ a_check_5 = 0
    $ a_check_6 = 0
    $ a_check_7 = 3
    $ a_check_8 = 0
    $ a_check_9 = 0
    $ minigamestep = 50

    $ fnameselect = True
    $ lnameselect = True

    call gamecheck_textcps from _call_gamecheck_textcps_2

    if is_test == True:    
        $ Set_CharMap("hero", "home", "bedroom_hero")
        call gametime from _call_gametime_87
        jump show_ui

    else:
        $ wsis_to_hero = "{color=#F00}?????{/color}"

        if preferences.is_namepersistent == True:

            # Load persistent relationship data into game variables
            python:
                if hasattr(persistent, "wsis_to_hero") and persistent.wsis_to_hero:
                    wsis_to_hero = persistent.wsis_to_hero
                else:
                    wsis_to_hero = "{color=#F00}?????{/color}"
                if hasattr(persistent, "hero_to_wsis") and persistent.hero_to_wsis:
                    hero_to_wsis = persistent.hero_to_wsis
                if hasattr(persistent, "hero_to_wmom") and persistent.hero_to_wmom:
                    hero_to_wmom = persistent.hero_to_wmom
                if hasattr(persistent, "hero_to_wgma") and persistent.hero_to_wgma:
                    hero_to_wgma = persistent.hero_to_wgma
                if hasattr(persistent, "hero_to_wcou") and persistent.hero_to_wcou:
                    hero_to_wcou = persistent.hero_to_wcou
                if hasattr(persistent, "hero_about_wmom") and persistent.hero_about_wmom:
                    hero_about_wmom = persistent.hero_about_wmom
                if hasattr(persistent, "hero_about_wsis") and persistent.hero_about_wsis:
                    hero_about_wsis = persistent.hero_about_wsis
                if hasattr(persistent, "hero_about_wgma") and persistent.hero_about_wgma:
                    hero_about_wgma = persistent.hero_about_wgma
                if hasattr(persistent, "hero_about_wcou") and persistent.hero_about_wcou:
                    hero_about_wcou = persistent.hero_about_wcou

                # Load persistent character names; missing/empty -> "?????" so the
                # creator screen prompts only for the slots that aren't stored yet.
                _placeholder = "{color=#F00}?????{/color}"
                for _name_key in (
                    "fnamehero", "lnamehero",
                    "fnamewmom", "fnamewsis", "fnamewcou", "fnamewgma",
                    "fnamewnei", "lnamewnei",
                    "lnamestep", "lnamerela",
                ):
                    _stored = getattr(persistent, _name_key, None)
                    if _stored:
                        setattr(store, _name_key, _stored)
                    else:
                        setattr(store, _name_key, _placeholder)

                if not getattr(store, "fnamewpre", None):
                    fnamewpre = "Attendant"

                # Load persistent region names
                for _reg_key in ("rnamectry", "rnamecity", "rnamevil1", "rnamevil2", "rnamebeac"):
                    _stored = getattr(persistent, _reg_key, None)
                    if _stored:
                        setattr(store, _reg_key, _stored)
                    else:
                        setattr(store, _reg_key, _placeholder)

            if persistent.statstart:
                if len(persistent.statstart) == 9 and sum(persistent.statstart) == 15:
                    # New 9-sub-stat format
                    $ stat_phy_str = persistent.statstart[0]
                    $ stat_phy_agi = persistent.statstart[1]
                    $ stat_phy_res = persistent.statstart[2]
                    $ stat_int_per = persistent.statstart[3]
                    $ stat_int_mem = persistent.statstart[4]
                    $ stat_int_log = persistent.statstart[5]
                    $ stat_cha_sex = persistent.statstart[6]
                    $ stat_cha_per = persistent.statstart[7]
                    $ stat_cha_soc = persistent.statstart[8]
                    $ a_check_7 = 0
                elif len(persistent.statstart) == 3 and persistent.statstart[0] + persistent.statstart[1] + persistent.statstart[2] == 15:
                    # Legacy 3-base-stat format — route to default sub-stats
                    $ stat_phy_str = persistent.statstart[0]
                    $ stat_int_log = persistent.statstart[1]
                    $ stat_cha_soc = persistent.statstart[2]
                    $ a_check_7 = 0

                if hero_to_wgma == __("Miss. ") + fnamewgma:
                    $ a_check_8 = 1
                if hero_to_wgma == __("Miss. ") + lnamerela:
                    $ a_check_8 = 2
                if hero_to_wgma == "Stepgrandma":
                    $ a_check_8 = 3
                if hero_to_wgma == "Grandma":
                    $ a_check_8 = 4

                if hero_about_wcou == fnamewcou:
                    $ a_check_9 = 1
                if hero_about_wcou == "my stepcousin":
                    $ a_check_9 = 2
                if hero_about_wcou == "my cousin":
                    $ a_check_9 = 3
                if hero_about_wcou == "cousin":
                    $ a_check_9 = 4

        else:
                $ fnamehero = "{color=#F00}?????{/color}"
                $ lnamehero = "{color=#F00}?????{/color}"
                $ fnamewmom = "{color=#F00}?????{/color}"
                $ fnamewsis = "{color=#F00}?????{/color}"
                $ lnamestep = "{color=#F00}?????{/color}"
                $ fnamewcou = "{color=#F00}?????{/color}"
                $ fnamewgma = "{color=#F00}?????{/color}"
                $ lnamerela = "{color=#F00}?????{/color}"
                $ fnamewnei = "{color=#F00}?????{/color}"
                $ lnamewnei = "{color=#F00}?????{/color}"
                $ fnamewpre = "Attendant"
                $ rnamecity = "{color=#F00}?????{/color}"
                $ rnamevil1 = "{color=#F00}?????{/color}"

# ----------------------------------------------------------------------------------------------------
# START SCREEN
# ----------------------------------------------------------------------------------------------------
    call check_itemname from _call_check_itemname_1
    $ _skipping = False
    $ quick_menu = False
    $ config.window = "hide"
    window hide
    hide screen splashscreen
    hide screen splashscreen2
    #$ Update_NameData()

    call gamecheck from _call_gamecheck_33
    call hide_ui from _call_hide_ui_165

    scene bg_0

    call screen campaign_select # with Dissolve(2)

    # Checks
    if wsis_quest_1 >= 1:
        $ wsis_inti_cap = char_inti_req_date

    if wnei_quest_6 >= 1:
        $ wnei_inti_cap = char_inti_req_date
        
    play BGM "audio/W2C - Memories.mp3"


    # Skip character creation when Global Data is on and all data is already set
    if preferences.is_namepersistent:
        if hero_to_wmom == "Stepmama-san" or hero_to_wsis == "Stepsis-chan" or hero_to_wcou == "Step-cousin" or hero_to_wgma == "Step-grandma" or lnamestep == "{color=#F00}?????{/color}" or lnamerela == "{color=#F00}?????{/color}" or fnamewsis == "{color=#F00}?????{/color}" or fnamewmom == "{color=#F00}?????{/color}" or  fnamewcou == "{color=#F00}?????{/color}" or fnamewgma == "{color=#F00}?????{/color}" or fnamewnei == "{color=#F00}?????{/color}" or lnamewnei == "{color=#F00}?????{/color}" or fnamehero == "{color=#F00}?????{/color}" or lnamehero == "{color=#F00}?????{/color}":
            pass

        else:
            jump start_mid_1

    call screen charactercreator1a with Dissolve(6)

    label start_mid_1:
        pass

    $ fnamewmam = "Mrs. "+lnamewnei
    $ fnamehpap = "Mr. "+lnamewnei

    # Aggregate base stats from sub-stat picks made during character creation.
    $ stat_phy = round((stat_phy_str + stat_phy_agi + stat_phy_res) / 3.0, 2)
    $ stat_int = round((stat_int_per + stat_int_mem + stat_int_log) / 3.0, 2)
    $ stat_cha = round((stat_cha_sex + stat_cha_per + stat_cha_soc) / 3.0, 2)

    $ persistent.statstart = [
        stat_phy_str, stat_phy_agi, stat_phy_res,
        stat_int_per, stat_int_mem, stat_int_log,
        stat_cha_sex, stat_cha_per, stat_cha_soc,
    ]

    # Persist the names entered in character creation so a future "Global Data" playthrough can reuse them without re-prompting.
    python:
        for _name_key in (
            "fnamehero", "lnamehero",
            "fnamewmom", "fnamewsis", "fnamewcou", "fnamewgma",
            "fnamewnei", "lnamewnei",
            "lnamestep", "lnamerela",
        ):
            _val = getattr(store, _name_key, "")
            if _val and _val != "{color=#F00}?????{/color}":
                setattr(persistent, _name_key, _val)

    $ personality[4] = minigamestep
    $ personality[3] = 100 - personality[4]
    if a_check_8 == 1:
        $ hero_to_wmom = __("Miss. ") + fnamewmom
        $ hero_about_wmom = __("Miss. ") + fnamewmom
        $ hero_to_wgma = __("Miss. ") + fnamewgma
        $ hero_about_wgma = __("Miss. ") + fnamewgma
        $ persistent.hero_to_wmom = __("Miss. ") + fnamewmom
        $ persistent.hero_about_wmom = __("Miss. ") + fnamewmom
        $ persistent.hero_to_wgma = __("Miss. ") + fnamewgma
        $ persistent.hero_about_wgma = __("Miss. ") + fnamewgma
    elif a_check_8 == 2:
        $ hero_to_wmom = __("Miss. ") + lnamestep
        $ hero_about_wmom = __("Miss. ") + lnamestep
        $ hero_to_wgma = __("Miss. ") + lnamerela
        $ hero_about_wgma = __("Miss. ") + lnamerela
        $ persistent.hero_to_wmom = __("Miss. ") + lnamestep
        $ persistent.hero_about_wmom = __("Miss. ") + lnamestep
        $ persistent.hero_to_wgma = __("Miss. ") + lnamerela
        $ persistent.hero_about_wgma = __("Miss. ") + lnamerela
    elif a_check_8 == 3:
        $ hero_to_wmom = "Stepmom"
        $ hero_about_wmom = "my stepmother"
        $ hero_to_wgma = "Stepgrandma"
        $ hero_about_wgma = "my stepgrandmother"
        $ persistent.hero_to_wmom = "Stepmom"
        $ persistent.hero_about_wmom = "my stepmother"
        $ persistent.hero_to_wgma = "Stepgrandma"
        $ persistent.hero_about_wgma = "my stepgrandmother"
    elif a_check_8 == 4:
        $ hero_to_wmom = "Mom"
        $ hero_about_wmom = "my mother"
        $ hero_to_wgma = "Grandma"
        $ hero_about_wgma = "my grandmother"
        $ persistent.hero_to_wmom = "Mom"
        $ persistent.hero_about_wmom = "my mother"
        $ persistent.hero_to_wgma = "Grandma"
        $ persistent.hero_about_wgma = "my grandmother"

    if a_check_9 == 1:
        $ hero_to_wsis = fnamewsis
        $ hero_about_wsis = fnamewsis
        $ hero_to_wcou = fnamewcou
        $ hero_about_wcou = fnamewcou
        $ persistent.hero_to_wsis = fnamewsis
        $ persistent.hero_about_wsis = fnamewsis
        $ persistent.hero_to_wcou = fnamewcou
        $ persistent.hero_about_wcou = fnamewcou
    elif a_check_9 == 2:
        $ hero_to_wsis = "Stepsis"
        $ hero_about_wsis = "my stepsister"
        $ hero_to_wcou = "Stepcousin"
        $ hero_about_wcou = "my stepcousin"
        $ persistent.hero_to_wsis = "Stepsis"
        $ persistent.hero_about_wsis = "my stepsister"
        $ persistent.hero_to_wcou = "Stepcousin"
        $ persistent.hero_about_wcou = "my stepcousin"
    elif a_check_9 == 3:
        $ hero_to_wsis = "Sis"
        $ hero_about_wsis = "my sister"
        $ hero_to_wcou = "Cousin"
        $ hero_about_wcou = "my cousin"
        $ persistent.hero_to_wsis = "Sis"
        $ persistent.hero_about_wsis = "my sister"
        $ persistent.hero_to_wcou = "Cousin"
        $ persistent.hero_about_wcou = "my cousin"

    elif a_check_9 == 4:
        if wsis_to_hero == "Lil bro":
            $ hero_to_wsis = "Big sis"
            $ hero_about_wsis = "my big sister"
            $ persistent.hero_to_wsis = "Big sis"
            $ persistent.hero_about_wsis = "my big sister"
        else:
            $ hero_to_wsis = "Lil sis"
            $ hero_about_wsis = "my little sister"
            $ persistent.hero_to_wsis = "Lil sis"
            $ persistent.hero_about_wsis = "my little sister"
        $ hero_to_wcou = "Cousin"
        $ hero_about_wcou = "cousin"
        $ persistent.hero_to_wcou = "Cousin"
        $ persistent.hero_about_wcou = "cousin"

    if is_skipable != False:
        $ _skipping = True
        $ quick_menu = True
        stop BGE fadeout 3
        play BGM "audio/W2C - Tranquility.mp3" fadein 3
        jump start_end

    play BGE "train.mp3" fadein 10
    scene scen_prologue 1 at Shaking
    with Dissolve(1)

    $ a_check_0 = 0
    $ a_check_1 = 0
    $ a_check_2 = 0
    $ a_check_3 = 0
    $ a_check_4 = 0
    $ a_check_5 = 0
    $ a_check_6 = 0
    $ a_check_7 = 3
    $ a_check_8 = 0
    $ a_check_9 = 0
    $ minigamestep = 0

    $ quick_menu = True
    $ _skipping = True

    mind "(I can feel anxiety coursing through me.{w=[wt3]} It's a strange feeling, knowing that my father is gone.{w=[wt4]} Well{w=[wt2]}, now he must be happy with my mother again...{w=[wt2]} But now I'm alone.{w=[wt3]} And my situation has become very difficult in the countryside without his support.)"

    mind "({nm}[rnamevil1]{/nm} is not a place with many opportunities{w=[wt2]}, I'm returning to {nm}[rnamecity]{/nm}{w=[wt1]}, where I was born and raised...{w=[wt3]} I don't have anything important to bring with me, apart from a little money and some clothes{w=[wt3]}. There's not much else I need.)"

    hide screen UI_stats
    with Dissolve(1)

    mind "(And the best thing to do was to accept my stepmother's invitation to live with her.{w=[wt3]} Even though she and my dad have split up in the past,{w=[wt1]} I believe the wisest thing is to forget about it and move on.)"

    mind "(Anyway{w=[wt3]}, I can't help but feel a little nervous about living there now,{w=[wt3]} especially 'cos of my stepsister.{w=[wt3]} She was quite stubborn and irritable when we were kids, and we used to fight a lot...{w=[wt3]} But, well{w=[wt3]}, maybe things have changed since then!)"

    mind "(As this train rattles along, I can't help but wonder what the future holds for me...)"

    stop BGE fadeout 4
    scene bg_street
    with Fade(2,1,3)

    mind "(The city seems much bigger than I remembered,{w=[wt1]} but still{w=[wt1]}, I can recognize the house where I used to live.{w=[wt3]} Though it has changed a bit, it still gives me a nostalgic feeling.)"

    scene scen_prologue mom1
    with fade

    mind "(I'm still a little nervous{w=[wt2]}, but well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Here goes nothing!)"

    window hide
    pause 0.5
    play SE1 "DoorBell.ogg"
    pause 3.0
    window show

    mind "(I can hear footsteps!{w=[wt2]} It might be {nm}[hero_about_wmom]{/nm}.)"

    stop BGM fadeout 7

    window hide
    pause 1.0
    play SE1 "DoorOpen1.ogg"
    pause 0.5
    play SE1 "DoorOpen2.ogg"
    pause 1.0
    scene scen_prologue mom2
    pause 1.5


    window show

    hero "Hi, {nm}[hero_to_wmom]{/nm}!.{w=[wt1]} I-.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"

    scene scen_prologue mom3
    with dissolve

    play BGM "audio/W2C - Tranquility.mp3"

    wmom "{vspace=15}{bt}DARLING!!!{/bt}"

    mind "(Oh my...{w=[wt3]} What a warm hug!{w=[wt3]} It's making my heart beat faster!{w=[wt3]} I need to remind myself that she's {nm}[hero_about_wmom]{/nm} before something gets hard down here!)"

    wmom "{bt}YOUR MAMA MISSED YOU SO MUUUCH!{/bt}{w=[wt3]} You can't imagine how happy I am to have you back!!!{w=[wt4]} I promise that I won't let you go ever again, okay!?"

    hero "{pa}MMM!!!{/pa}{w=[wt4]}{nw}"

    window hide
    pause 0.5
    scene scen_prologue mom4
    with Dissolve (1.5)
    play SE1 "FailurePiano.ogg"
    show prologue_mom soul
    with Dissolve (1.5)
    pause 1.0

    mind "(Am I still alive?)"
    
    $ Define_NPCState()

    scene bg_home facade
    show WMOM
    with fade

    wmom "{bt}{b}Ara ara...{/b}{/bt}{w=[wt3]} How careless I am!{w=[wt3]} Forgive me, honey...{w=[wt2]} I just couldn't hold myself as I saw my little sweetheart after so long...{w=[wt3]} Now he's {bt}such a handsome grown man{/bt}!{w=[wt3]} {lg}Tche He He...{/lg}{w=[wt4]} Welcome home, honey!"

    hero "Thank you, {nm}[hero_to_wmom]{/nm}!{w=[wt3]} I'm happy to see you again too!{w} {mind}(In fact, I wouldn't mind if she does that again.){/mind}"

    scene bg_home hallway
    show WMOM
    with fade

    mind "(Home sweet home{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} The house really has changed a lot since the last time I was here.{w=[wt3]} It looks much more modern and stylish,{w=[wt2]} but still cozy.)"

    wmom "Feeling nostalgic, honey?{w=[wt3]} It's where you used to live!{w=[wt3]} I've refurnished the house a bit,{w=[wt1]} so you may be noticing some differences, right?{w=[wt4]} Oh!{w=[wt2]} Also{w=[wt2]}, your sis has moved into the bedroom that used to be yours!{w=[wt3]} I hope you don't mind."

    mind "(Oh no!{w=[wt3]} When I went to live in the countryside, I missed my big and comfortable room so much!{w=[wt3]} Now that I'm back, it's been taken from me!{w=[wt3]} Well{w=[wt3]}, at least,{w=[wt1]} the other room must be easier to clean{w=[wt3]}, {bt}I guess...{/bt})"

    scene bg_home bedroom hero
    with fade

    show WMOM
    wmom "I hope you like your room, sweetie.{w=[wt3]} It's been redecorated just for you!"

    hero "Of course!{w=[wt3]} Thank you, {nm}[hero_to_wmom]{/nm}!{w=[wt4]} {mind}(I'm surprised by how pleasant and inviting it looks{w=[wt1]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Why did the neighbor decide to make a second floor in a house that's already so close to ours?{w=[wt3]} Doesn't he know the words {b}ventilation{/b} and {b}privacy{/b}!?){/mind}"

    wmom "Why not see if your sis is awake, sweetie?{w=[wt2]} I know you're tired from your journey{w=[wt1]}, but I'm sure she'll be so happy to see you again!"

    wmom "You still remember her, don't you?"


    hero "Of course I remember {nm}[hero_about_wsis]{/nm}!{w=[wt3]} I'll go see her right now!{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} {mind}(I hope she doesn't hate me now...){/mind}"

    scene bg_home hallway
    with fade

    hide WMOM
    mind "(As I walk down the hallway{w=[wt1]}, I can't help but feel a bit nervous about seeing {nm}[hero_about_wsis]{/nm} again.{w=[wt3]} I wonder if she's still as irritable as she used to be{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I hope we can get along this time...)"

    scene scen_prologue sis4
    with dissolve

    play SE1 "DoorKnock.ogg"
    pause 0.2
    play SE1 "DoorKnock.ogg"
    pause 0.2
    play SE1 "DoorKnock.ogg"
    pause 1.0

    wsis "What do you want at this hour, mom?!"
    window hide

    stop BGM fadeout 3

    play SE1 "DoorOpen1.ogg"
    pause 0.5
    play SE1 "DoorOpen2.ogg"
    pause 0.5

    scene scen_prologue sis1
    with dissolve
    pause 0.5

    scene scen_prologue sis2
    show prologue_wsis shy
    with dissolve

    pause

    play BGM "audio/W2C - Awkward.mp3"

    pause 1.0

    wsis "..."

    scene scen_prologue sis3

    mind "(!!!)"

    $ a_event_0 = str(__(hero_to_wsis)[:1])
    menu:
        "Apologize and turn back":

            $ personality[1] -= 15
            $ personality[2] += 15
            scene scen_prologue sis2
            show prologue_wsis shy
            with dissolve
            hero "{aw}I{w=[wt1]}-I'm S{w=[wt1]}-sorry, [a_event_0]{w=[wt1]}-{nm}[hero_to_wsis]{/nm}!{w=[wt2]} I{w=[wt1]}-I'll talk to you later!{/aw}"

        "Compliment her body":

            $ personality[1] += 15 
            $ personality[2] -= 15    
            scene scen_prologue sis2
            show prologue_wsis shy
            with dissolve       
            hero "{aw}N{w=[wt1]}-nice tits, [a_event_0]{w=[wt1]}-{nm}[hero_to_wsis]{/nm}!{/aw}"

    stop BGM
    play SE1 "DoorBam.ogg"
    pause 0.2
    scene scen_prologue sis4
    show prologue_wsis shy
    pause 1

    mind "(Okay...{w=[wt3]} I better go back to my room for now)"
    play BGM "audio/W2C - Tranquility.mp3" fadein 3.0

    scene scen_prologue nei1
    with fade

    mind "(Oh lord{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Which architect agreed to add another floor to the neighbor's house like that?{w=[wt3]} how do I report them all to the authorities?{w=[wt3]} How can these people not be sentenced to prison already!?!?{w=[wt3]} The wall has completely stolen the breath and glow of this side of my room!)"

    scene scen_prologue nei2
    with dissolve

    show prologue_2hero alert
    pause 0.5
    hide prologue_2hero alert
    pause 0.5

    show prologue_shy
    with Dissolve (1.0)
    pause 0.5

    mind "(Well{w=[wt1]}, on second thought{w=[wt2]}, it's not like I'm a plant or something to need light and wind that much anyway, right?{w=[wt4]} Even a wall this close isn't all {bt}thaaat{/bt} bad!{w=[wt4]} In fact{w=[wt1]}, I'm starting to find the neighborhood quite lovely, I'd say!)"
    mind "(Wait!{w=[wt3]} This girl is {nm}[fnamewnei]{/nm}!)"

    stop BGM fadeout 2

    scene scen_prologue nei3
    show prologue_shy
    with dissolve
    pause 0.5
    show prologue_2wsis alert
    pause 0.25
    show prologue_2hero alert
    pause 0.25
    hide prologue_2wsis
    pause 0.25
    hide prologue_2hero
    pause 0.25

    play BGM "audio/W2C - Fun.mp3"

    mind "(Oops...)"

    wnei "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

    hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

    scene scen_prologue nei4
    with dissolve

    wnei "{nm}[fnamehero]{/nm}!?{w=[wt2]} Is that ya!?{w=[wt3]} {pa}{size=+15}OH MY GAAAH!!!{/size}{/pa}{w=[wt4]} {nm}[fnamewsis]{/nm} told me ya'd be cumin' this afternoon,{w=[wt1]} {bt}but ya're already here!!!{/bt}"

    hero "{aw}I{w=[wt1]}-I t{w=[wt1]}-took a train b{w=[wt1]}-before dawn and...{/aw}{w=[wt4]}{nw}"

    hero "{aw}I-I t-took a train b-before dawn and...{/aw}{fast}{pr}{aw}Hey, [C_Nam][fnamewnei][C_Off]... y{w=[wt1]}-you know t{w=[wt1]}-that you're...{/aw}{w=[wt4]}{nw}"

    hero "{aw}I-I t-took a train b-before dawn and...{/aw}{pr}{aw}Hey, [C_Nam][fnamewnei][C_Off]... y-you know t-that you're...{/aw}{fast}{pr}{aw}E{w=[wt1]}-e{w=[wt1]}-exposed right in front of a man, right?{/aw}"

    wnei "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

    hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

    wnei "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.I don't get ya, {nm}[fnamehero]{/nm}!{w=[wt3]} You're speaking such funny things!{pr}{lg}SHI HI HI HI HI...{/lg}"

    mind "(Oh...{w=[wt3]} I can't believe...{w=[wt3]} Her boobs are really the only thing that grew up!{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{pr}{pa}SHE'S STILL AN IDIOT!!!{/pa})"

    wnei "Hey, {nm}[fnamehero]{/nm}!"

    scene scen_prologue nei5

    wnei "Hey, {nm}[fnamehero]{/nm}! {fast} since we're so close now, gimme a hug!!!"

    hero "{pa}Ehhh!?!?{/pa}"

    menu:
        "Tell her it can be dangerous":
            $ personality[1] -= 30
            $ personality[2] += 30

            hero "{aw}Wait, {nm}[fnamewnei]{/nm}!{w=[wt1]} It can be dangerous!{w=[wt3]} I don't want you to fall down and die here!{/aw}"

            wnei ".{w=[wt1]}.{w=[wt1]}.{w=[wt1]}Oh, gah...{w=[wt4]} I think you're right!{w=[wt3]} So...{w=[wt3]}{nw}"

            scene scen_prologue nei4
            
            wnei "...Oh, gah... I think you're right! So...{fast} I'ma put something on and go there with ya, okie?{w=[wt3]} wait for me!!!"

        "Just hug her":
            $ personality[1] += 30
            $ personality[2] -= 30

            wnei "C'mon!!"

            hero "{aw}O{w=[wt1]}-ok{w=[wt1]}.{w=[wt1]}.{w=[wt2]}.{/aw}"

            scene scen_prologue nei6

            hero "{aw}O-ok...{/aw}{fast} {mind}(I might even die here,{w=[wt3]} but on the other hand I'm sure life wouldn't be worth living knowing that I let this moment pass.{w=[wt3]} So, I think it's right then){/mind}"

            wnei "{lg}Shi hi hi...  {/lg}{w=[wt3]} it's fun but this hug isn't very comfortable."

            hero "{aw}Y{w=[wt1]}-yes{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/aw}{w=[wt3]} {mind}(It's certainly not the best position to hug,{w=[wt1]} but it's still with a topless girl...{w=[wt3]} I can't complain, right?){/mind}"

            scene scen_prologue nei4
            with fade

            wnei "So...{w=[wt3]} I'ma put something on and go there with ya, okie?{w=[wt3]} wait for me!!!"

    scene scen_prologue nei7
    with dissolve

    mind "(Oh lord!{w=[wt3]} Who was the architect who agreed to build another floor of the neighbor's house?{w=[wt3]} {b}how do I thank this hero?{w=[wt3]} How can I give him a kiss?{/b}{w=[wt3]} At least I can thank my neighbor for the daughter he has and for how their brains work{w=[wt3]}, or maybe...{w=[wt3]} the way they don't work, in this case...)"

    mind "(Wow!{w=[wt3]} Just within the hour that I arrived, my return was already worth it...{w=[wt3]} There's so many things on my mind right now...{w=[wt3]} but mainly, I can't forget...)"

    scene scen_prologue nei8
    with Dissolve (2.0)

    pause 1.0

    menu:
         mind "(Just within the hour that I arrived, my return was already worth it... There's so many things on my mind right now... but mainly, I can't forget...){fast}"

         "{nm}[hero_about_wmom]{/nm} breasts":
            $ personality[1] += 5
            $ personality[2] -= 5
            $ wmom_bonus += 1.5
            $ msg.msg(renpy.translate_string("+ 1.5% bonus for next interations with {nm}[fnamewmom]{/nm}"))

            mind "(Wow! Just within the hour that I arrived, my return was already worth it... There's so many things on my mind right now... but mainly, I can't forget{fast} {nm}[hero_about_wmom]{/nm}'s huge tits{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} and wow...{w=[wt3]} I think I should do something to calm this awakened monster here before someone arrives!)"

         "{nm}[hero_about_wsis]{/nm} breasts":
            $ personality[1] += 5
            $ personality[2] -= 5
            $ wsis_bonus += 1.5
            $ msg.msg(renpy.translate_string("+ 1.5% bonus for next interations with {nm}[fnamewsis]{/nm}"))
            mind "(Wow! Just within the hour that I arrived, my return was already worth it... There's so many things on my mind right now... but mainly, I can't forget{fast} {nm}[hero_about_wsis]{/nm}'s cute titties{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} and wow...{w=[wt3]} I think I should do something to calm this awakened monster here before someone arrives!)"

         "{nm}[fnamewnei]{/nm} breasts":
            $ personality[1] += 5
            $ personality[2] -= 5
            $ wnei_bonus += 1.5
            $ msg.msg(renpy.translate_string("+ 1.5% bonus for next interations with {nm}[fnamewnei]{/nm}"))
            mind "(Wow! Just within the hour that I arrived, my return was already worth it... There's so many things on my mind right now... but mainly, I can't forget{fast} {nm}[fnamewnei]{/nm}'s gorgeous boobies{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} and wow...{w=[wt3]} I think I should do something to calm this awakened monster here before someone arrives!)"

         "All the hot girls":
            $ personality[1] += 5
            $ personality[2] -= 5
            $ wsis_bonus += 0.5
            $ wsis_bonus += 0.5
            $ wsis_bonus += 0.5
            $ msg.msg(renpy.translate_string("+ 0.5% bonus for next interations with the girls"))
            mind "(Wow! Just within the hour that I arrived, my return was already worth it... There's so many things on my mind right now... but mainly, I can't forget{fast} all these hotties!{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} and wow...{w=[wt3]} I think I should do something to calm this awakened monster here before someone arrives!)"

         "To be back with loved ones":
            $ personality[1] -= 5
            $ personality[2] += 5
            $ wsis_bonus += 0.5
            $ wsis_bonus += 0.5
            $ wsis_bonus += 0.5
            $ msg.msg(renpy.translate_string("+ 0.5% bonus for next interations with the girls"))
            mind "(Wow! Just within the hour that I arrived, my return was already worth it... There's so many things on my mind right now... but mainly, I can't forget{fast} that I'm back to people I love!{w=[wt3]} I missed then so much...{w=[wt2]} but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I think I should do something to calm this awakened monster here before someone arrives!)"

    stop BGM

    wnei "Ah!{w=[wt3]} {nm}[fnamehero]{/nm}!{w=[wt3]} I almost forgot!!!"

    scene bg_0
    with Dissolve(1.5)
    play BGM "audio/W2C - MainTheme (EPIC).mp3"
    pause(0.5)

    $ pygame.event.set_allowed(None)
    $ pygame.event.set_allowed(pygame.USEREVENT)

    $ zoomS1 = 5
    $ zoomT1 = 0
    $ zoomX1 = 0.5
    $ zoomY1 = 0.75
    $ zoomS2 = 1
    $ zoomT2 = 6
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1


    scene scen_prologue_nei9_bg at ZoomSTXY
    show scen_prologue_nei9_hero 1 at ZoomSTXY
    show scen_prologue_nei9_wnei at ZoomSTXY
    with Dissolve (2)

    show scen_prologue_nei9_hero 2
    with Dissolve (2)

    pause(2)

    $ _skipping = True
    $ pygame.event.set_blocked(None)

    wnei "{vspace=30}{bt}{b}{size=60}WELCUM TO THE CITY!!!{/size}{/b}{/bt}"
    pause(0.5)

label start_end:

    $ StartAct("wnei", [(("moving", "home"), 0), (("staying", "living_room"), 10)], True)
    $ StartAct("wsis", (("staying", "bedroom_wsis"), 10), True)
    $ StartAct("wmom", (("staying", "living_room"), 10), True)
    $ map_lock_bedroom_wsis = True

    scene bg_home bedroom hero
    with Fade (3.0, 0.0, 3.0, color="#FFF")

    if personality[4] > 70:
        $ cellbg.insert(1, "PER_Intimate")
        $ cellbg[0] = "PER_Intimate"

    if personality[3] > 70:
        $ cellbg.insert(1, "PER_Reserved")
        $ cellbg[0] = "PER_Reserved"

    if personality[2] > 70:
        $ cellbg.insert(1, "PER_Kind")
        $ cellbg[0] = "PER_Kind"

    if personality[1] > 70:
        $ cellbg.insert(1, "PER_Hentai")
        $ cellbg[0] = "PER_Hentai"

    if personality[1] <= 70 and personality[2] <= 70 and personality[3] <= 70 and personality[4] <= 70:
        $ cellbg.insert(1, "PER_Common")
        $ cellbg[0] = "PER_Common"

    call personality from _call_personality
    $ check_stat()

    if is_skipable == "Day3":
        stop BGE fadeout 3
        $ a_check_3 = 0
        $ ChaNameGen(char_id="hstt", target=1)
        $ ChaNameGen(char_id="wric", target=2)
        $ hero_quest_1 = 6
        $ hero_quest_2 = 1
        jump schoolday_1_1_skip

    else:
        $ _skipping = True
        $ quick_menu = True
        stop BGE fadeout 3
        $ Set_CharMap("hero", "home", "bedroom_hero")
        if is_skipable == "Day2":
            $ hero_quest_1 = 6
            jump passday
        else:
            $ hero_quest_1 = 0
            jump show_ui

#---------------------------------------------------------------------------
label scenestep_0_1: #Lunch Start
#---------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_166
    scene bg_0
    with Dissolve(1)
    stop BGM

    play BGM "audio/W2C - Tranquility.mp3"
    pause(1)

    $ wmom_mood = "A1"
    $ wnei_mood = "A3"
    $ hero_mood = "A1"

    scene bg_home diningroom
    show HERO at LL
    show WNEI at LC
    show WMOM at RC
    show WSIS at OR
    with Dissolve(3)

    wmom "It's lunchtime, lovelies!{w=[wt1]} {nm}[fnamewnei]{/nm}, you're welcome to join us, honey!"
    wnei "Thank you, miss!{w=[wt2]} I didn't tell my family I was gonna have lunch here so mama must be waitin' for me.{w=[wt2]} Imma cum back!"
    show WSIS at RR_slow
    wmom "It's okay, honey.{w=[wt2]} You can come here whenever you want!{w=[wt3]} {nm}[fnamewsis]{/nm}, my love,{w=[wt2]} could you open the door for her while I set the table?"
    wsis "C'mon!{nw}"        
    show WSIS at OL_slow
    show WNEI at OL_slow
    wsis "C'mon!{fast}"
    show WMOM at CC_slow
    wmom "What a lovely girl, don't you think?{w=[wt3]} You should invite her to have dinner with us tonight, honey!{w=[wt3]} I'm gonna buy some goodies to celebrate your return!"
    hide WNEI
    $ wnei_is_flw = False
    hero "Oh{w=[wt1]}, that's great!{w=[wt2]} Thank you {nm}[hero_to_wmom]{/nm}{w=[wt2]}, I will do anything to help!"
    wmom "Oh dear{w=[wt1]}, you don’t need to bother yourself!{w=[wt3]} Actually{w=[wt2]}, why don’t you take your sis to the grocery this afternoon?{w=[wt3]} I’ll give you some cash to splurge on whatever you two want!"
    mind "(Nice!{w=[wt2]} I think it's a good opportunity for us to get along!{w=[wt3]} Maybe she won't be so mad with me if I buy something she likes at the grocery store."
    show WSIS at RC_heavy
    hero "Leave it to me, {nm}[hero_to_wmom]{/nm}!"

    wsis "I'm hungry!"
    wmom "Leave a little room in your belly for dinner tonight, honey!"
    wsis "Oh!{w=[wt2]} Sure!"

    scene bg_0
    with Dissolve(1)
    pause(1)
    mind "(W{w=[wt1]}-wait, What was that!?{w=[wt3]} No way she can be that fit eating like that!{w=[wt3]} Does she have a black hole in her belly by any chance!?)"

    $ gametimehour = 13
    $ gametimemin = 30
    $ hero_quest_1 = 2
    call gametime from _call_gametime_88

    $ wnei_eat = 100
    $ wsis_eat = 100
    $ wmom_eat = 100
    $ StartAct("wnei", [(("moving", "neighbor"), 0), ("eating", 0)], True)
    $ StartAct("wsis", ("eating", 0), True)
    $ StartAct("wmom", ("eating", 0), True)
    $ StartAct("wsis", (("staying", "bedroom_wsis"), 60), True)

    jump show_ui

#---------------------------------------------------------------------------
label scenestep_0_2: # Grocery Store
#---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    # Chat with WSIS
    #---------------------------------------------------------------------------
    $ add_stat("wsis", "inti", 1)
    hero "Let's get some goodies for tonight at the grocery!"
    wsis "Hmph{w=[wt2]}, what can you do without me?{w=[wt4]} {bt}Fine... Fine...{/bt}{w=[wt2]} I'll just change my clothes."

    $ add_stat("wsis", "love", 1)
    $ add_stat("hero", "cha_soc", 1)

    $ hero_mood = "A1"
    hero "You're fine,{w=[wt1]} come on!"
    wsis "Shut up, moron!{w=[wt1]} I won't go out dressed like this."
    if Check_CharInMap("wsis", "home", "bedroom_wsis"):
        window hide
        $ hero_mood = "O1"
        $ wsis_mood = "O2"
        show HERO at MoveOUT_L
        show WSIS at LC
        with ease
        wsis "{bt=a2-s2-p20}Shoo!{w=[wt1]} Shoo!{w=[wt1]} Hurry!!!{/bt}"
        $ Set_CharMap("hero", "home", "hallway")
        play SE1 "DoorBam.ogg"

        show WSIS at LC
        $ wsis_mood = "O1"
        $ wsis_fx = "1"
        with Dissolve(1)
        pause(1)

    else:
        show WSIS at MoveOUT_L
        pause 1

    scene bg_0
    with Dissolve(1)
    $ Set_CharMap("wsis", "home", "bedroom_wsis")
    $ hero_quest_1 = 3
    $ Define_NPCState()
    $ hero_mood = "A1"
    $ wsis_mood = "O1"
    $ wsis_fx = "0"
    hide WSIS

    # 0 ---------------------------------------------------------------------------

    $ wsis_wear = "casual"
    
    scene sccash1 bg
    show sccash1_wmom1bg
    show sccash1_wmom1fg 1
    show sccash1_herobg at OR
    with Fade(0.5,1,2)

    show sccash1_herobg at CC_slow

    show sccash1_wmom1fg 2
    show sccash1_herofg 1
    with Dissolve(1)

    hero "So, {nm}[hero_to_wmom]{/nm},{w=[wt2]} I asked {nm}[hero_about_wsis]{/nm} to the Grocery Store with me.{w=[wt4]} She's getting ready to go."

    show sccash1_wmom1fg 3
    wmom "{bt}Ara Ara...{/bt}{w=[wt2]} Very cute, darling!{w=[wt2]} I'm so glad you two are getting along again."

    show sccash1_wmom1fg 2
    show sccash1_herofg 2
    with Dissolve(1)
    hero "Not really yet, {nm}[hero_to_wmom]{/nm},{w=[wt3]} but I hope we can get along!"

    show sccash1_wmom1fg 4
    hide sccash1_herofg

    wmom "Oh, darling{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Know that she can be a little stubborn at times{w=[wt1]}, but she really loves you a lot!{w=[wt4]} If you knew how long this girl cried when you left{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} I felt so bad for her, dear.{w=[wt2]} Even more{w=[wt1]}, knowing it was all my fault."

    show sccash1_wmom1fg 3
    wmom "So please, take care of your sis, OK darling?{w=[wt2]} She's my little precious gem!{w=[wt4]} I know she can be very difficult to deal with at first{w=[wt2]}, and maybe too hesitant to trust someone and improve the relationship well.{w=[wt3]} Which's why she doesn't have many friends.{w=[wt3]} But I assure you that if you have a little patience with her{w=[wt1]}, you will see what a treasure she is!"

    show sccash1_wmom1fg 2
    hero "O{w=[wt1]}-okay!{w=[wt2]} I'll keep it in mind!"
    show sccash1_wmom1fg 3
    wmom "Thank you for being so understanding.{w=[wt2]} Love you, honey!{w=[wt4]} By the way{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Let me give you the money to spend in the grocery store.{w=[wt2]} Could you get it here from my pocket?{w=[wt1]} My hands are soapy now..."
    $ hero_mood = "O1"
    $ hero_fx = "2"
    stop BGM fadeout 3
    show sccash1_herofg 3
    show sccash1_wmom1fg 1
    hero "{aw}{b}E{w=[wt1]}-eh...!?{/b}{w=[wt3]} S{w=[wt1]}-s{w=[wt1]}-sure!{/aw}"

    play BGM "audio/W2C - Awkward.mp3"

    scene sccash2 bg
    show sccash2_wmom1bg
    show sccash2_wmom1fg 0
    show sccash2_heromg
    with Dissolve(1)

    pause (1)

    hero "{aw}W{w=[wt1]}-wait!{w=[wt2]} Does your s{w=[wt1]}-shorts really have pockets?{/aw}"
    wmom "I'm sure it has, darling!{w=[wt2]} Maybe you haven't seen it because they're pretty thin."
    hero "{mind}(Oh{w=[wt2]}, That's right!{w=[wt3]} The pockets on these shorts are so thin that I almost couldn't see them!{w=[wt3]} Damn{w=[wt1]}, they feel so tight that if I put my hand there I should feel all of her skin!!){/mind}{w=[wt4]} {aw}I{w=[wt1]}-I found it now!{w=[wt3]} Which one is the money in?{/aw}"
    wmom "{bt}Hmmm...{/bt}{w=[wt4]} I don't remember, honey!{w=[wt2]} {lg}Tche He He...{/lg}{w=[wt3]} Sorry{w=[wt1]}, but I think you'll have to find out."
    hero "{aw}R{w=[wt1]}-right!{/aw}"

    hide sccash2_wmom1fg
    hide sccash2_heromg
    show sccash2_herobg
    show sccash2_wmom1fg l
    show sccash2_heromg
    with Dissolve(1)

    mind "(Okay{w=[wt2]}, it's not like I'm taking advantage of {nm}[hero_about_wmom]{/nm}, right?{w=[wt3]} I'm just putting my hand in her pocket to find the money she asked for!{w=[wt3]} Yes!{w=[wt2]} it's just that!{w=[wt4]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} it's not in this one.)"

    hide sccash2_herobg
    show sccash2_wmom1fg 0
    with Dissolve(1)

    hero "{aw}{nm}[hero_to_wmom]{/nm}{w=[wt2]}, I think it's not here.{/aw}"
    wmom "Then it must be in the other one, darling."

    hero "{aw}O{w=[wt1]}-okay{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/aw}"

    hide sccash2_herobg
    hide sccash2_heromg
    hide sccash2_wmom1fg
    show sccash2_herofg
    show sccash2_wmom1fg r
    show sccash2_heromg
    with Dissolve(1)

    mind "(Well{w=[wt2]}, isn't it supposed to be in one of the pockets?)"
    wmom "Still nothing, honey?{w=[wt4]} Let me help!{w=[wt2]} Here{w=[wt2]}, take a proper look."

    window hide
    hide sccash2_heromg
    hide sccash2_wmom1bg
    hide sccash2_wmom1fg
    show sccash2_wmom2bg
    show sccash2_wmom2fg 0
    show sccash2_heromg
    with Dissolve(1)
    pause(1)

    hero "{aw}R{w=[wt1]}-right!{/aw}"

    window hide
    pause(0.5)
    hide sccash2_heromg
    hide sccash2_wmom2bg
    hide sccash2_wmom2fg 0
    show sccash2_hero2
    show sccash2_wmom2bg
    show sccash2_wmom2fg 1
    show sccash2_heromg
    with Dissolve(1)
    pause(1)

    hero "{mind}({w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Now I don't know if I want to find that money or if I prefer to keep looking.{w=[wt4]} Oh God{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} it's definitely not in the pockets!){/mind}{w=[wt4]} {aw}I{w=[wt1]}-I think it's n{w=[wt1]}-not here, {nm}[hero_to_wmom]{/nm}...{/aw}"

    scene sccash1 bg
    show sccash3_wmombg 1
    show sccash3_wmomfg 1
    show sccash3_herobg 1
    with Fade(1,1,0.5)
    
    wmom "{pa}Ehhh!?{/pa}{w=[wt4]} So I did lose my money!?{w=[wt4]} I swore I kept it in my p{w=[wt1]}{nw}"
    show sccash3_wmomfg 2
    wmom "{pa}Ehhh!?{/pa} So I did lose my money!? I swore I kept it in my p{fast}{w=[wt1]}-{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{nw}"
    show sccash3_wmomfg 3
    wmom "{pa}Ehhh!?{/pa} So I did lose my money!? I swore I kept it in my p{w=[wt1]}-{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{fast} ah!{w=[wt2]} I remembered!{w=[wt2]} Since these pockets are too small{w=[wt1]}, I kept it in my blouse!{w=[wt1]} {lg}Tche He He...{/lg}"
    hero "{pa}EHHH!?!?{/pa}"

    show sccash3_wmombg 2
    hide sccash3_wmomfg
    show sccash3_herobg 2
    show sccash3_wsis at OR
    with dissolve

    show sccash3_herofg
    with dissolve

    $ wsis_fx = "1"
    $ wsis_mood = "O2"

    pause(1)
    show sccash3_wsis at CC
    with ease

    wsis "{pa}{nm}MOM{/nm}!!!{/pa}{w=[wt2]} {aw}What are you doing in front of [C_Nam][fnamehero][C_Off]!?!?{/aw}"

    scene bg_home diningroom
    show WMOM at LC
    show HERO at LL
    show WSIS at RC
    call gametime from _call_gametime_89
    $ wmom_itemL = "1"
    $ wsis_wear = "casual"
    with Fade(1,1,2)

    wmom "Your cash, honey!{w=[wt2]} Buy whatever you want!"
    $ wsis_fx = "2"
    show WMOM at CC_slow
    show WSIS at RR_fast
    with ease
    $ wmom_itemL = "0"
    $ wmom_itemR = "1"
    wsis "{aw}Ugh!{w=[wt2]} {nm}Mom{/nm}!!!{w=[wt2]} I won't touch this thing!!!{/aw}"
    $ wmom_mood = "O1"
    wmom "Hmm?{w=[wt2]} I don't get you, darling{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{nw}"
    show WMOM at LC_slow
    $ wmom_mood = "A1"
    $ wmom_itemL = "1"
    $ wmom_itemR = "0"
    wmom "Hmm? I don't get you, darling...{fast} Well{w=[wt1]}, don't worry{w=[wt2]}, cos {nm}[fnamehero]{/nm} will take care of everything!{w=[wt3]}{nw}"
    $ wmom_itemL = "0"
    $ hero_body = "2"
    $ hero_itemR = "1"
    wmom "Hmm? I don't get you, darling... Well, don't worry, cos {nm}[fnamehero]{/nm} will take care of everything!{fast} I'm sure he's a very responsible man now.{w=[wt1]} Right honey?"

    $ money += 100
    $ msg.msg(renpy.translate_string("$100 was added to the cash"))
    $ hero_body = "1"
    $ hero_itemR = "0"
    $ hero_fx = "1"
    $ hero_mood = "A2"
    hero "{aw}S{w=[wt1]}-sure!{w=[wt2]}{/aw}{nw}"
    mind "{aw}S-sure!{/aw}{fast} (I guess).{w=[wt2]}{nw}"
    hero "{aw}S-sure!{/aw} {mind}(I guess){/mind}.{fast} {aw}Leave it to me!{w=[wt2]}{/aw}{nw}"
    mind "{aw}S-sure!{/aw} (I guess). {aw}Leave it to me!{fast}{/aw} (I guess)."
    $ wsis_mood = "O3"
    show WSIS at MoveOUT_R
    wsis "{sc=1}Ugh!{/sc}{w=[wt2]} {aw}Hurry up you pervert!{/aw}"
    $ hero_mood = "O1"
    hero "{aw}{b}Ehhh!?{/b}{/aw}{w=[wt4]}{nw}"
    $ hero_mood = "A1"
    mind "{aw}{b}Ehhh!?{/b}{/aw}{fast} (Well{w=[wt2]}, at least I think it could have been even worse if she had arrived moments earlier, right?){w=[wt4]}{nw}"
    show HERO at MoveOUT_R
    hero "{aw}{b}Ehhh!?{/b}{/aw} {mind}(Well{w=[wt1]}, at least I think it could have been even worse if she had arrived moments earlier, right?){/mind}{fast} {aw}B{w=[wt1]}-bye, {nm}[hero_to_wmom]{/nm}!{/aw}"
    show WMOM at RR_slow
    wmom "Be careful, my loves!"
    stop BGM fadeout 5

    # 1 ---------------------------------------------------------------------------

    $ a_check_2 = fnamewpre
    $ a_check_3 = lnamewpre
    $ fnamewpre = "Attendant"
    $ lnamewpre = ""

    scene bg_0 with Dissolve(3)

    #jump grocerystore_backup

    wsis "Here.{w=[wt2]} There it is."

    play BGM "audio/W2C - Tranquility.mp3"

    scene sd1_grocerystore_1_bg
    show sd1_grocerystore_1_wpre 1
    show sd1_grocerystore_1_wsis 1
    show sd1_grocerystore_1_hero 1
    show sd1_grocerystore_1_hero_face 1
    with Dissolve(1)

    show sd1_grocerystore_1_wpre 2
    show sd1_grocerystore_1_wpre_face a0
    show sd1_grocerystore_1_wpre_eye s
    show sd1_grocerystore_1_wpre_fg
    with dissolve

    show sd1_grocerystore_1_wpre_face a1
    wpre "Oh{w=[wt2]}, Welcome to our humble{nw}"

    show sd1_grocerystore_1_wpre_eye f
    wpre "Oh{w=[wt2]}, welcome to our humble{fast} establishment!"

    show sd1_grocerystore_1_wpre_face a0

    stop BGM fadeout 3
    show sd1_grocerystore_1_hero_face 2 with dissolve

    mind "(Wait{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Am I seeing things...?)"
    #pause

    scene bg_1 with Dissolve(1)

    play SE1 "Wow1.mp3"

    scene BG_Peach
    show sd1_grocerystore_2_wpre
    with Dissolve(2)
    play BGM "audio/W2C - Lust.mp3"

    pause

    hero "{size=-10}Whoooa!{w=[wt3]} Look at that camel toe!{w=[wt3]} It's so big!!!{/size}"

    stop BGM
    play SE1 "CartoonStratch.ogg"

    show sd1_grocerystore_1_bg
    show sd1_grocerystore_1_wpre 2
    show sd1_grocerystore_1_wpre_face o0
    show sd1_grocerystore_1_wpre_eye s
    show sd1_grocerystore_1_wpre_fg
    show sd1_grocerystore_1_wsis 2
    show sd1_grocerystore_1_wsis_face o0
    show sd1_grocerystore_1_wsis_eye l
    show sd1_grocerystore_1_wsis_fg
    show sd1_grocerystore_1_hero 2
    show sd1_grocerystore_1_hero_face s0
    with dissolve

    play BGM "audio/W2C - Awkward.mp3"
    pause(0.5)

    show sd1_grocerystore_1_wsis_face o1
    wsis "What are you mumbling about now, you moron?{w=[wt2]} Of course this camel toe is big.{w=[wt2]} This is how you attract people's attention to the store."

    show sd1_grocerystore_1_hero_face s1
    show sd1_grocerystore_1_wsis_face o0
    hero "{aw}Ehhh!?{/aw}{w=[wt2]} N{w=[wt1]}-no{w=[wt2]}, w{w=[wt1]}-wait!{w=[wt2]} {nw}"

    show sd1_grocerystore_1_hero_face s0
    hero "{aw}Ehhh!?{/aw}{w=[wt2]} N{w=[wt1]}-no{w=[wt2]}, w{w=[wt1]}-wait!{w=[wt2]} {fast}{mind}(Damn!{w=[wt2]} Did I say it out loud!?{w=[wt3]} And to make matters worse{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} {nm}[hero_about_wsis!u]{/nm} DID REALLY HINTED IN THE FACE OF THE GIRL THAT SHE IS A KIND OF SLUT THAT JUST LEFT IT ON PURPOSE FOR EVERYONE TO SEE!?){/mind}"

    show sd1_grocerystore_1_wsis_eye r
    show sd1_grocerystore_1_wpre_face a1
    wpre "Oh{w=[wt2]}, that!{w=[wt2]}{nw}"

    show sd1_grocerystore_1_wpre_eye f
    wpre "Oh{w=[wt2]}, that!{w=[wt2]}{fast}{gg}Tee-hee...{/gg}{w=[wt2]} Yes, sir!{w=[wt2]} This camel toe is quite eye-catching, isn't it?{w=[wt3]} I really like knowing that everyone can see it clearly from the street!"

    show sd1_grocerystore_1_wsis_eye l
    show sd1_grocerystore_1_wpre_face a0
    show sd1_grocerystore_1_hero_face s1
    hero "{pa}EHHH!?!?!?{/pa}"

    show sd1_grocerystore_1_hero_face s0
    wsis "Hmph{w=[wt2]}, {nw}"

    show sd1_grocerystore_1_wsis_face o1
    wsis "Hmph{w=[wt2]}, {fast}why are you acting so impressed as if she's saying something from another world?"

    show sd1_grocerystore_1_wsis_face o0
    show sd1_grocerystore_1_hero_face s1
    hero "W{w=[wt1]}-wait!{w=[wt2]} S{w=[wt1]}-so you also agree it's okay to j{w=[wt1]}-just show it like this?"

    show sd1_grocerystore_1_hero_face s0
    wsis "Huh!?!?"

    scene sd1_grocerystore_3_bg
    show sd1_grocerystore_3_wpre
    show sd1_grocerystore_3_wpre_face a0
    show sd1_grocerystore_3_wpre_eye f
    show sd1_grocerystore_3_wpre_fg
    show sd1_grocerystore_3_wsis
    show sd1_grocerystore_3_wsis_face o0
    show sd1_grocerystore_3_wsis_eye l
    show sd1_grocerystore_3_wsis_fg
    show sd1_grocerystore_3_hero
    show sd1_grocerystore_3_hero_face s
    with dissolve

    show sd1_grocerystore_3_wpre_face a1
    wpre "As you noticed, sir{w=[wt2]}, our mascot is quite the attention-grabber!{w=[wt3]} So you don't need to worry about that.{w=[wt3]} Like our well-traveled camel{w=[wt2]}, we bring goods from all corners of the world to our little store.{w=[wt3]} This is what our logo represents."

    show sd1_grocerystore_3_wpre_face a0
    show sd1_grocerystore_3_hero_face t0 with Dissolve(1)
    show sd1_grocerystore_3_hero_face t1
    hero "O{w=[wt1]}-oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I s{w=[wt1]}-see."

    show sd1_grocerystore_3_hero_face t0
    show sd1_grocerystore_3_wpre_eye s
    show sd1_grocerystore_3_wsis_eye r
    show sd1_grocerystore_3_wsis_face a1
    wsis "I'm sorry about him, miss.{w=[wt3]} He is not from here.{w=[wt3]} Stores probably just have plain signs with the owner's name or something like that where he came from.{w=[wt3]} I should've told him how things are in the city, I guess."

    show sd1_grocerystore_3_wsis_face a0
    show sd1_grocerystore_3_wpre_face a1
    wpre "Oh my!{w=[wt2]} What a wonderful coincidence!{w=[wt2]} I'm actually from the countryside too!{w=[wt3]} I only moved here recently.{w=[wt3]} You're absolutely right about the simpler stores back home!{w=[wt1]} {gg}Tee-hee...{/gg}{w=[wt4]}{nw}"

    show sd1_grocerystore_3_wpre_eye f
    wpre "Oh my!{w=[wt2]} What a wonderful coincidence!{w=[wt2]} I'm actually from the countryside too!{w=[wt3]} I only moved here recently.{w=[wt3]} You're absolutely right about the simpler stores back home!{w=[wt1]} {gg}Tee-hee...{/gg}{w=[wt4]}{fast} Oh, God! It's so nice to meet someone who also came from the countryside!!"

    if perk_int_mem >= 1:
        $ hero_know.append("WPRE_Work_GroceryStore")
        $ hero_know.append("WPRE_BG_Countryside")

    show sd1_grocerystore_3_wpre_eye s
    show sd1_grocerystore_3_wsis_face a1
    show sd1_grocerystore_3_wpre_face a0
    wsis "Come to think of it{w=[wt2]}, I really don't recall seeing you here before.{w=[wt3]} Well...{w=[wt3]} Welcome, I guess."

    show sd1_grocerystore_3_wsis_face a0
    show sd1_grocerystore_3_wpre_face a1
    wpre "Own{w=[wt2]}, thank you so much for your kindness, miss!{w=[wt3]} Oh{w=[wt2]}, my apologies!{w=[wt2]} I'm taking up your shopping time.{w=[wt3]} Please feel free to look around.{w=[wt2]} If I may be of assistance{w=[wt1]}, I'll be with you shortly!"

    show sd1_grocerystore_3_wsis_face a1
    show sd1_grocerystore_3_wpre_face a0
    wsis "Sure.{w=[wt2]} Thanks.{w=[wt3]}{nw}"

    show sd1_grocerystore_3_wsis_face o1
    show sd1_grocerystore_3_wsis_eye l
    wsis "Sure. Thanks.{fast} You{w=[wt2]}, c'mon!"

    show sd1_grocerystore_3_wsis_face o0
    show sd1_grocerystore_3_wpre_eye f
    show sd1_grocerystore_3_hero_face t1
    hero "Hey{w=[wt2]}, how come I didn't get a welcome from you when I moved here?"

    show sd1_grocerystore_3_wpre_eye s
    show sd1_grocerystore_3_wsis_face o1
    show sd1_grocerystore_3_hero_face t0
    wsis "Cos you're not!{w=[wt2]} Now c'mon!{w=[wt2]} Hurry up!!!"

    show sd1_grocerystore_3_wpre_face o0
    show sd1_grocerystore_3_wsis at CC
    show sd1_grocerystore_3_wsis_face o0 at CC
    show sd1_grocerystore_3_wsis_eye l at CC
    show sd1_grocerystore_3_wsis_fg at CC
    with None

    show sd1_grocerystore_3_wsis at RC_slow
    show sd1_grocerystore_3_wsis_face at RC_slow
    show sd1_grocerystore_3_wsis_eye at RC_slow
    show sd1_grocerystore_3_wsis_fg at RC_slow
    with None

    hide sd1_grocerystore_3_wsis
    hide sd1_grocerystore_3_wsis_face
    hide sd1_grocerystore_3_wsis_eye
    hide sd1_grocerystore_3_wsis_fg
    with Dissolve(1)

    show sd1_grocerystore_3_wpre_eye f
    show sd1_grocerystore_3_hero_face t1
    hero "{aw}Ehhh...!?{/aw}{w=[wt4]} W{w=[wt1]}-wait!"

    show sd1_grocerystore_3_hero at CC
    show sd1_grocerystore_3_hero_face t0 at CC
    with None

    show sd1_grocerystore_3_hero at RC_slow
    show sd1_grocerystore_3_hero_face at RC_slow
    with None

    show sd1_grocerystore_3_wpre_eye s
    hide sd1_grocerystore_3_hero
    hide sd1_grocerystore_3_hero_face
    with dissolve


    stop BGM fadeout 2
    scene sd1_grocerystore_4_bg
    show sd1_grocerystore_4_wsis 1
    with Fade(2,0,1)

    play BGM "audio/W2C - Tranquility.mp3"
    pause

    mind "(Whooa{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} This store really does seem to sell everything!{w=[wt3]} They even have food in the display case by the checkout.{w=[wt2]} Hmmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} it looks really tasty!{w=[wt4]} {nm}[hero_about_wsis]{/nm} is such a big eater{w=[wt2]}, so she'll end up wanting to buy everything.)"
    mind "(Oh!{w=[wt3]} They've got plushies on sale!{w=[wt2]} 80%% off just for today!{w=[wt3]} If I can keep enough money from this shopping trip{w=[wt2]}, I might be able to get a very cute gift for [C_Dat]$100[C_Off].{w=[wt3]} Damn{w=[wt2]}, It wasn't easy saving up that much...{w=[wt3]} At regular price{w=[wt2]}, I'd have to work more than twice as long to afford one.)" # mechanics tip for the player
    
    show sd1_grocerystore_4_wsis 2
    show sd1_grocerystore_4_wsis_face o1
    with dissolve
    wsis "Are you going to stand there gawking all day or actually help?"

    show sd1_grocerystore_4_wsis_face o0
    "{nw}"

    scene sd1_grocerystore_5_bg
    show sd1_grocerystore_5_wsis_body
    show sd1_grocerystore_5_wsis_head 1
    with Fade(1,0,2)

    wsis "Let's start with drinks.{w=[wt3]} What should we get?"
    hero "Well{w=[wt2]}, there's soda{w=[wt2]}, juice{w=[wt2]}, wine{w=[wt2]}, beer..."

    show sd1_grocerystore_5_wsis_head 2
    show sd1_grocerystore_5_wsis_face o0
    with dissolve

    show sd1_grocerystore_5_wsis_face o1
    wsis "No!{w=[wt2]} No alcohol!{w=[wt2]} We have school tomorrow.{w=[wt3]} B{w=[wt1]}-besides{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {w=[wt1]}Hmph{w=[wt2]}, I don't want {nm}Mom{/nm} getting drunk."

    show sd1_grocerystore_5_wsis_face o0
    hero "Well{w=[wt2]}, what about-{nw}"
    
    show sd1_grocerystore_5_wsis_face o1
    wsis "And don't even think about juice.{w=[wt2]} It's too expensive!{w=[wt3]} Let's just pick a soda already."    

    hide sd1_grocerystore_5_wsis_face
    hide sd1_grocerystore_5_wsis_body
    hide sd1_grocerystore_5_wsis_head
    show sd1_grocerystore_5_wsis
    with dissolve

    pause

    wsis "Hmmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} There's no soda here."

    pause

    mind "(Don't worry {nm}[hero_to_wsis]{/nm}.{w=[wt3]} Just keep looking there and I'll keep looking here.)"
    
    hide sd1_grocerystore_5_wsis
    show sd1_grocerystore_5_wsis_body
    show sd1_grocerystore_5_wsis_head 1
    with dissolve

    show sd1_grocerystore_5_wsis_head 2
    show sd1_grocerystore_5_wsis_face o0
    with dissolve

    wsis "Hmp!"
    mind "(Oops!)"

    play SE1 "Boing1.mp3"
    scene sd1_grocerystore_6_bg
    show sd1_grocerystore_6_fg
    with hpunch

    wsis "{aw}Ugh!{/aw}{w=[wt2]} You're useless!{w=[wt4]} If you're not helping{w=[wt2]}, at least don't just stand there daydreaming on the way!{w=[wt3]} {bt}Shoo! Shoo!{/bt}"

    scene sd1_grocerystore_7_bg
    show sd1_grocerystore_7_wsis_body
    show sd1_grocerystore_7_wsis_fg 1
    with Fade(1,0,1)

    pause

    show sd1_grocerystore_7_wsis_fg 2
    show sd1_grocerystore_7_wsis_face o0
    with dissolve

    show sd1_grocerystore_7_wsis_fg 3 with dissolve
    show sd1_grocerystore_7_wsis_face o1
    wsis "See?{w=[wt3]} The sodas are right here{w=[wt1]}, you useless..."

    show sd1_grocerystore_7_wsis_face o0
    show sd1_grocerystore_7_wsis_fg 2 with dissolve
    hero "Oh y{w=[wt1]}-yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I can see them clearly now..."

    show sd1_grocerystore_7_wsis_face o1
    wsis "I think grape is the best option!{w=[wt3]} What do you think?{w=[wt3]}{nw}"

    hide sd1_grocerystore_7_wsis_face
    show sd1_grocerystore_7_wsis_fg 1

    wsis "I think grape is the best option!{w=[wt3]} What do you think?{fast}{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Though {nm}mommy{/nm} really prefers guarana{w=[wt2]}, and {nm}[fnamewnei]{/nm} always goes for orange{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Hmm..."

    show sd1_grocerystore_7_wsis_face o0
    show sd1_grocerystore_7_wsis_fg 2 with dissolve

    show sd1_grocerystore_7_wsis_face o1
    wsis "What do you think?{w=[wt3]} {aw}Ugh!{/aw}{w=[wt2]} You're not even looking at anything!"

    show sd1_grocerystore_7_wsis_face o0
    hero "I'm just looking at everything!"

    show sd1_grocerystore_7_wsis_face o1
    wsis "Shut up!{w=[wt3]} Every time I look at you you're just looking at me daydreaming, you moron!"

    show sd1_grocerystore_7_wsis_face o0
    menu:
        "Apologize":
            hero "S{w=[wt1]}-sorry{w=[wt2]}, y{w=[wt1]}-you're right, {nm}[hero_to_wsis]{/nm}."

            $ add_stat("wsis", "love", 1)

            show sd1_grocerystore_7_wsis_face o1
            wsis "Hmph{w=[wt2]}, You're so useless!{w=[wt3]} C'mon!{w=[wt3]} Just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Ugh!{w=[wt3]} Pick something already!"

        "Compliment":
            hero "Well{w=[wt2]}, y{w=[wt1]}-you can't blame me, you know?{w=[wt3]} You're so beautiful that i{w=[wt1]}-it's really hard not to get lost looking at you, {nm}[hero_to_wsis]{/nm}."

            $ add_stat("wsis", "lust", 1)
            show sd1_grocerystore_7_wsis_fx with dissolve

            show sd1_grocerystore_7_wsis_face o1
            wsis "Stop saying nonsense, you moron!{w=[wt3]} C'mon!{w=[wt3]} Just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Ugh!{w=[wt3]} Pick something already!"

    scene sd1_grocerystore_8_bg
    show sd1_grocerystore_8_wsis_bg
    show sd1_grocerystore_8_wsis_mouth o0
    show sd1_grocerystore_8_wsis_fg
    with fade

    pause
    
    show sd1_grocerystore_8_wsis_mouth o1
    wsis "Stop staring and make a choice!{w=[wt3]} I'm not doing all the work while you slack off!"

    scene sd1_grocerystore_9_bg
    show sd1_grocerystore_9_wpre 1
    show sd1_grocerystore_9_wpre_face a0
    show sd1_grocerystore_9_wsis 2
    show sd1_grocerystore_9_wsis_head 1
    show sd1_grocerystore_9_hero_body
    show sd1_grocerystore_9_hero_head 1
    with Fade(0.5,0,1)
    
    jump grocerystore_end

    $ hero_know.append("WSIS_Y_Flavor_Grape")
    $ hero_know.append("WNEI_Y_Flavor_Guarana")
    $ hero_know.append("WMOM_Y_Flavor_Orange")
    $ item_sale = ["Drink_JuiceGrape", "Drink_JuiceGuarana", "Drink_JuiceOrange", "Drink_SodaGrape", "Drink_SodaGuarana", "Drink_SodaOrange", "Drink_SodaCola",]
    $ item_cart = []

    $ _skipping = False

    label grocerystore_option0:
        show sd1_grocerystore_8_wsis_mouth o0
        $ a_item_5 = "grocerystore_option1"
        call UI_buy_Item from _call_UI_buy_Item

    label grocerystore_option1:
        hide screen UI_buy_Item

    $ _skipping = True

    show sd1_grocerystore_8_wsis_mouth o1

    if item_cart == []:
        wsis "No!{w=[wt2]} I won't do anything else for you.{w=[wt3]} Just choose one by yourself!"
        jump grocerystore_option0
    elif len(item_cart) > 6:
        wsis "Do you have shit in your head or what?{w=[wt3]} There's no room in the fridge for all that!"
        jump grocerystore_option0
    elif len(item_cart) > 3:
        wsis "Ugh!{w=[wt2]} You took too many!{w=[wt2]} Take just one and leave others back!"
        jump grocerystore_option0
    elif len(item_cart) > 1:
        wsis "Hey!{w=[wt2]} Who said you could get more than one?{w=[wt3]} We're on a budget here!{w=[wt4]} Hmph!{w=[wt2]} Whatever{w=[wt2]}, we'll sort it out later..."
    elif "Drink_JuiceGrape" in item_cart or "Drink_JuiceGuarana" in item_cart or "Drink_JuiceOrange" in item_cart:
        wsis "I just told you juice was too expensive!{w=[wt3]} Are you even listening?{w=[wt4]} Hmph!{w=[wt2]} We'll figure something out..."
    elif "Drink_SodaGrape" in item_cart:
        wsis "Hmph{w=[wt2]}, at least you have decent taste{w=[wt2]}, for once."
    else:
        wsis "Finally!{w=[wt3]} Let's just move on."

    scene sd1_grocerystore_9_bg
    show sd1_grocerystore_9_wpre 1
    show sd1_grocerystore_9_wpre_face a0
    show sd1_grocerystore_9_wsis 1
    show sd1_grocerystore_9_hero_body
    show sd1_grocerystore_9_hero_head 1
    with Fade(0.5,0,1)

    show sd1_grocerystore_9_hero_head 2
    wsis "Wow!{w=[wt3]} Everything in the display case looks amazing!"

    show sd1_grocerystore_9_hero_head 1
    show sd1_grocerystore_9_wpre_face a1
    wpre "Please take your time!{w=[wt2]} I'll be happy to get anything you'd like to try."

    show sd1_grocerystore_9_hero_head 2
    show sd1_grocerystore_9_wpre_face a0
    wsis "That shrimp pie looks incredible!{w=[wt3]} No{w=[wt2]}, wait{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {nm}[fnamewnei]{/nm} has that seafood allergy{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Darn it{w=[wt2]}, maybe the Chicken Croquettes?{w=[wt2]} Everyone could eat those{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Oh{w=[wt2]}, but {nm}mom{/nm} isn't supposed to have fried foods."
    wsis "I guess we could get these vegan sandwiches she likes{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Ugh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I don't know{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Maybe pizza is safer since everyone can have some.{w=[wt3]} Ugh!{w=[wt3]} Let me check the desserts first."
    wsis "{bt}Sweet heavens!{/bt}{w=[wt2]} Ice cream!!!{w=[wt3]} This is-{w=[wt1]} No{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {nm}Mom{/nm}'s migraines{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} The Fruit Pie would be perfect for her{w=[wt2]} but {nm}[fnamewnei]{/nm} would rather starve than touch fruit pie.{w=[wt3]} A box of candies maybe?{w=[wt3]} But that feels so{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} meh!{w=[wt3]} Chocolate cake might be our best bet here."

    show sd1_grocerystore_9_wsis 2
    show sd1_grocerystore_9_wsis_head 1
    wsis "{aw}Ugh!{/aw}{w=[wt2]} This is impossible!{w=[wt4]} You know what?{w=[wt2]} You decide!"
    hero "{aw}Ehhh!?{/aw}"
    wsis "Hurry up!"

    $ hero_know.append("WSIS_Y_Flavor_Grape")
    $ hero_know.append("WNEI_Y_Flavor_Guarana")
    $ hero_know.append("WMOM_Y_Flavor_Orange")

    label grocerystore_option2:
        $ _skipping = False
        $ item_sale = ["Drink_JuiceGrape", "Drink_JuiceGuarana", "Drink_JuiceOrange", "Drink_SodaGrape", "Drink_SodaGuarana", "Drink_SodaOrange", "Drink_SodaCola", "Eat_Dess_Icecream", "Eat_Sweet_CandyBox", "Eat_Lunch_PieFruit", "Eat_Dess_CakeChocolate", "Eat_Lunch_Pizza", "Eat_Lunch_PieShrimp", "Eat_Snack_ChickenCroquettes", "Eat_Snack_SandwichVegan",]

        python:
            for buceta in item_cart:
                if buceta in item_sale:
                    item_sale.remove(buceta)

        $ a_item_5 = "grocerystore_option3"
        call UI_buy_Item from _call_UI_buy_Item_1

    label grocerystore_option3:
        hide screen UI_buy_Item

    $ _skipping = True

    if (CountItem_Inventory("Drink_JuiceGrape", item_cart) == 0 and
        CountItem_Inventory("Drink_JuiceGuarana", item_cart) == 0 and
        CountItem_Inventory("Drink_JuiceOrange", item_cart) == 0 and
        CountItem_Inventory("Drink_SodaGrape", item_cart) == 0 and
        CountItem_Inventory("Drink_SodaGuarana", item_cart) == 0 and
        CountItem_Inventory("Drink_SodaOrange", item_cart) == 0 and
        CountItem_Inventory("Drink_SodaCola", item_cart) == 0):
        wsis "Seriously?{w=[wt2]} Are you idiot or what!?!?{w=[wt3]} You even removed the drink!{w=[wt4]} Get back there and fix this!"
        jump grocerystore_option2

    elif (
        CountItem_Inventory("Eat_Dess_Icecream", item_cart) == 0 and
        CountItem_Inventory("Eat_Sweet_CandyBox", item_cart) == 0 and
        CountItem_Inventory("Eat_Lunch_PieFruit", item_cart) == 0 and
        CountItem_Inventory("Eat_Dess_CakeChocolate", item_cart) == 0 and
        CountItem_Inventory("Eat_Lunch_Pizza", item_cart) == 0 and
        CountItem_Inventory("Eat_Lunch_PieShrimp", item_cart) == 0 and
        CountItem_Inventory("Eat_Snack_ChickenCroquettes", item_cart) == 0 and
        CountItem_Inventory("Eat_Snack_SandwichVegan", item_cart) == 0
        ):
        wsis "We need both lunch and dessert!{w=[wt3]} Is that really so hard to understand?"
        jump grocerystore_option2

    elif (
        CountItem_Inventory("Eat_Dess_Icecream", item_cart) == 0 and
        CountItem_Inventory("Eat_Sweet_CandyBox", item_cart) == 0 and
        CountItem_Inventory("Eat_Lunch_PieFruit", item_cart) == 0 and
        CountItem_Inventory("Eat_Dess_CakeChocolate", item_cart) == 0
        ):
        wsis "{aw}Ehhh!?{/aw}{w=[wt2]} What about the dessert?{w=[wt3]} Do I have to explain everything?"
        jump grocerystore_option2

    elif (
        CountItem_Inventory("Eat_Lunch_Pizza", item_cart) == 0 and
        CountItem_Inventory("Eat_Lunch_PieShrimp", item_cart) == 0 and
        CountItem_Inventory("Eat_Snack_ChickenCroquettes", item_cart) == 0 and
        CountItem_Inventory("Eat_Snack_SandwichVegan", item_cart) == 0
        ):
        wsis "{aw}Are you kidding me!?{/aw}{w=[wt3]} We can't just have dessert for lunch!{w=[wt3]} Pick something proper!"
        jump grocerystore_option2

    elif money > 100 and money <= 200: # To prevent bug with infinite money
        wsis "We still have money{w=[wt2]}, go take another soda!"
        jump grocerystore_option2

    elif money < 100:
        wsis "Wait{w=[wt2]}, this is too much!{w=[wt3]} We can't afford all this!"
        hero "Don't worry about it.{w=[wt3]} I'll just cover the difference."
        wsis "Y{w=[wt1]}-you don't have to do that, idiot..."

        show sd1_grocerystore_9_hero_head 1
        hero "It's fine.{w=[wt3]} Here you go{w=[wt2]}, miss."

    else:
        show sd1_grocerystore_9_hero_head 1
        hero "Here you go, miss."

    label grocerystore_end:
        pass

    show sd1_grocerystore_9_wpre_face a1
    wpre "Thank you so much!{w=[wt3]} Let me package everything nicely for you."

    show sd1_grocerystore_9_wpre_face a0
    show sd1_grocerystore_9_wsis_head 2 with dissolve

    wsis "Oh!{w=[wt2]} You have Galmons!"

    show sd1_grocerystore_9_wpre_face a1
    wpre "Pardon?"

    show sd1_grocerystore_9_wpre_face a0
    show sd1_grocerystore_9_wsis_head 1 with dissolve
    wsis "T{w=[wt1]}-those plushies up there{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} on the top shelf..."

    show sd1_grocerystore_9_wpre 2
    hide sd1_grocerystore_9_wpre_face
    show sd1_grocerystore_9_wsis_head 2
    show sd1_grocerystore_9_hero_head 2
    with dissolve

    show sd1_grocerystore_9_wpre 2
    hide sd1_grocerystore_9_wpre_face
    wpre "Ohh{w=[wt2]}{nw}"

    show sd1_grocerystore_9_wpre 1
    show sd1_grocerystore_9_wpre_face a1
    wpre "Ohh{fast}, yes!{w=[wt3]} These plushies are so cute!{w=[wt3]} They're actually on sale today for $100.{w=[wt2]}{nw}"

    show sd1_grocerystore_9_wsis_head 1
    show sd1_grocerystore_9_hero_head 1
    wpre "Ohh, yes! These plushies are so cute! They're actually on sale today for $100.{fast}{w=[wt2]} Would you like one, miss?"

    show sd1_grocerystore_9_wpre_face a0
    wsis "N{w=[wt1]}-no{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I was just looking..."

    if money >= 100:
        menu:
            "Propose to buy":
                show sd1_grocerystore_9_hero_head 2
                hero "Hey{w=[wt2]}, don't worry about it!{w=[wt3]} Pick whichever one you want.{w=[wt2]} My treat!"
                wsis "N{w=[wt1]}-no{w=[wt2]}, really..."

                menu:
                    "Finish shopping":
                        jump grocerystore_option5

                    "Choose the sheep":
                        hero "OK{w=[wt2]}, since you won't choose{w=[wt2]}, then I'll just pick the sheep."

                    "Choose the chick":
                        hero "OK{w=[wt2]}, since you won't choose{w=[wt2]}, then I'll just pick the chick."

                    "Choose the monkey":
                        hero "OK{w=[wt2]}, since you won't choose{w=[wt2]}, then I'll just pick the monkey."

                jump grocerystore_option4

            "Finish shopping":
                jump grocerystore_option5
    else:
        $ msg.msg(renpy.translate_string("You don't have enough money"))
        jump grocerystore_option5

    label grocerystore_option4:
        wsis "Wait!{w=[wt4]} T{w=[wt1]}-the bunny..."

        show sd1_grocerystore_9_hero_head 1
        hero "The bunny it is then!{w=[wt3]} We'll take that one please!"

        show sd1_grocerystore_9_wpre_face a1
        wpre "Of course!{w=[wt3]} J{w=[wt1]}-just give me a moment..."

        show sd1_grocerystore_9_wpre_face a0 with None
    
    scene sd1_grocerystore_10_bg
    show sd1_grocerystore_10_wpre
    show sd1_grocerystore_10_wpre_face a0
    show sd1_grocerystore_10_hero_body
    show sd1_grocerystore_10_hero_head 1
    show sd1_grocerystore_10_wsis_body
    show sd1_grocerystore_10_wsis_head 1
    with Fade(1,0,2)

    show sd1_grocerystore_10_wpre_face a1
    wpre "I{w=[wt1]}-I apologize{w=[wt2]}, I'm just a bit nervous with ladders.{w=[wt3]} I'll do my best to retrieve it quickly!"

    show sd1_grocerystore_10_wpre_face a0
    wsis "N{w=[wt1]}-no, please{w=[wt2]}, d{w=[wt1]}-don't need to apologize!{w=[wt3]}{nw}"
    show sd1_grocerystore_10_wsis_head 2

    wsis "N-no, please, d-don't need to apologize!{fast}{w=[wt2]} Hey{nw}, "

    show sd1_grocerystore_10_hero_body at Shake2
    show sd1_grocerystore_10_hero_head 2 at Shake2

    wsis "N-no, please, d-don't need to apologize!{fast}{w=[wt2]} Hey{fast}, you're the man here, aren't you?{w=[wt2]} Go help her with that ladder!"
    hero "Oh{w=[wt2]}, r{w=[wt1]}-right!"

    show sd1_grocerystore_10_hero_body at Shake2
    show sd1_grocerystore_10_hero_head at Shake2
    wsis "{aw}Hurry up!!!{/aw}"
    
    scene sd1_grocerystore_11_bg
    show sd1_grocerystore_11_hero_body
    show sd1_grocerystore_11_hero_head 1
    show sd1_grocerystore_11_hero_mouth a0
    show sd1_grocerystore_11_wpre 1
    show sd1_grocerystore_11_wsis
    with fade

    wpre "T{w=[wt1]}-this is so kind of you both{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm terribly sorry for the trouble.{w=[wt3]} How embarrassing..."

    show sd1_grocerystore_11_hero_mouth a1
    hero "Y{w=[wt1]}-you don't need to!{w=[wt3]} It's okay."
    
    show sd1_grocerystore_11_wpre 2
    show sd1_grocerystore_11_hero_head 2
    hide sd1_grocerystore_11_hero_mouth
    with dissolve

    stop BGM fadeout 3

    wpre "I'll just be a moment!"

    play BGM "audio/W2C - Lust.mp3"
    scene sd1_grocerystore_12_bg
    show sd1_grocerystore_12_wpre 1
    with Fade(0.5,0,1)

    pause

    mind "(What a great moment to be alive{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} ''It's okay?''.{w=[wt3]} What an understatement!{w=[wt3]} What did I have in mind to say something as shallow as that?{w=[wt2]} This is a privilege!{w=[wt2]} An honor!{w=[wt2]} I'm very grateful to be helping you, miss!{w=[wt3]} What a wonderfully moment.{w=[wt3]} I absolutely love camel t{w=[wt1]}- Store!)"
    
    show sd1_grocerystore_12_wpre 2
    with dissolve

    pause

    wpre "{gg}Tee-hee...{/gg}"
    mind "(You did it, Miss!{w=[wt3]} I'm proud of you.{w=[wt3]} I can even see the tail!{w=[wt3]} It's no a super big tail, I'd say{w=[wt2]}, but it's so round{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} so prominent{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'd love to squeeze it so bad!{w=[wt4]} Oh if I could put my both hands on this tail, miss...)"

    $ money -= 100
    $ msg.msg(renpy.translate_string("You spent [C_Neg]100 money[C_Off]"))
    $ add_stat("wsis", "love", 10)
    $ add_stat("hero", "cha_soc", 10)
    $ wsis_item.append("Coll_Plushy_BunnyPink")
    $ msg.msg(renpy.translate_string("[C_Dat]Cute Bunny Monster Girl[C_Off] added in {nm}[fnamewsis]{/nm} inventory"))

    stop BGM fadeout 3
    scene sd1_grocerystore_9_bg
    show sd1_grocerystore_9_wpre 1
    show sd1_grocerystore_9_wpre_face a0
    show sd1_grocerystore_9_wsis 2
    show sd1_grocerystore_9_wsis_head 1
    show sd1_grocerystore_9_hero_body
    show sd1_grocerystore_9_hero_head 1
    with Fade(1,0,2)
    play BGM "audio/W2C - Tranquility.mp3"

    label grocerystore_option5:
        hero "That should be everything{w=[wt2]}, thank you."

        show sd1_grocerystore_9_wpre_face a1
        wpre "Thank you both for shopping with us today!{w=[wt2]} Have a wonderful afternoon!"

        show sd1_grocerystore_9_wpre_face a0 with None

        $ wsis_know.append("HangOut_Groceries")
        call gametime_wait(16, 0) from _call_gametime_wait_18

    $ fnamewpre = a_check_2
    $ lnamewpre = a_check_3
    $ a_event_2 = 0
    $ a_event_3 = 0
    $ hero_body = "2"
    $ hero_itemR = "2"
    $ hero_itemL = "2"
    $ is_resetmood = True

    call gametime from _call_gametime_90

    $ wsis_wear = "casual"

    scene bg_home livingroom
    show WMOM at LC
    show WSIS at OR
    show HERO at OR
    show WSIS at RR_heavy
    show HERO at RC_heavy
    with Fade(1,0,3)

    #---------------------------------------------------------------------------

    wsis "We're back!"
    wmom "{bt}Ohhh...{w=[wt1]} Look at my big boy!{/bt}{w=[wt2]} Carrying all the bags for his dear sister!{w=[wt3]} Welcome back, lovelies!{w=[wt3]} Just leave these bags on the table, honey.{w=[wt1]}{nw}"

    show HERO at CC_slow
    wmom "{bt}Ohhh... Look at my big boy!{/bt} Carrying all the bags for his dear sister! Welcome back, lovelies! Just leave these bags on the table, honey.{fast}{w=[wt1]} I'll take a look later.{w=[wt2]} Need to do my Sunday workout first.{nw}"

    $ hero_body = "1"
    $ hero_itemR = "0"
    $ hero_itemL = "0"
    show HERO at RC_slow

    wmom "{bt}Ohhh... Look at my big boy!{/bt} Carrying all the bags for his dear sister! Welcome back, lovelies! Just leave these bags on the table, honey. I'll take a look later. Need to do my Sunday workout first.{fast}{w=[wt2]} I'll be in my room.{nw}"

    show WMOM at OL_slow
    wmom "{bt}Ohhh... Look at my big boy!{/bt} Carrying all the bags for his dear sister! Welcome back, lovelies! Just leave these bags on the table, honey. I'll take a look later. Need to do my Sunday workout first. I'll be in my room.{fast}"

    $ hero_fx = 1
    mind "(Is it me, or did it sound like an invitation?)"
    wsis "Hmm{w=[wt1]}, where's the TV remote...?"

    scene bg_0
    with Dissolve(1)
    $ is_specialevent = False
    call goto_home_livingroom from _call_goto_home_livingroom_3
    jump show_ui

#---------------------------------------------------------------------------
label scenestep_0_3: # Pre-Celebration
#---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_167

    scene bg_0
    with Dissolve(2)

    $ wmom_wear = "sport"
    $ wsis_wear = "home"

    play BGM "audio/W2C - Tranquility.mp3" fadein 3

    if Check_CharInMap("hero", "home", "bedroom_wmom"):
        scene bg_home bedroom wmom
        show WMOM at LL
        show HERO at LC
        show WSIS at OR
        $ wsis_mood = "O1"
        $ wsis_fx = 0
        $ hero_fx = 0
        with Dissolve(3)

        show WSIS at RR_slow

        wsis "{aw}Ehh!?{/aw}{w=[wt3]} What is he doing here?"
        wmom "We are practicing yoga together, sweetie!"
        if personality[0] == "Hentai":
            wsis "Why do you let this pervert do yoga with you!?"
            wmom "Please{w=[wt1]}, stop saying such things to your brother, darling!"

        wsis "Hunf...!{w=[wt2]} So{w=[wt1]}, I wanna ask if you have any battery.{w=[wt2]} The TV remote's one is over."
        wmom "I don't think so, darling.{w=[wt2]} But we'll deal with this later.{w=[wt2]} Hurry and go take a shower!{w=[wt2]} Today is a special day.{w=[wt2]} We have to prepare ourselves to our celebration."
        if gametimemin <= 9:
            $ a_event_0 = "0"+str(gametimemin)
        else:
            $ a_event_0 = str(gametimemin)
        wsis "Ugh, mom...!{w=[wt1]} It's still [gametimehour]:[a_event_0]!{w=[wt3]} {nm}[fnamehero]{/nm} can go first."
        $ wmom_mood = "O1"
        wmom "Ehh...?{w=[wt2]} Why don't you take a shower together?{w=[wt2]}{nw}"
        $ wmom_mood = "A1"
        wmom "Ehh...? Why don't you take a shower together?{fast} You're siblings!"
        $ wsis_fx = "2"
        $ wsis_mood = "O3"
        $ hero_fx = "2"
        $ hero_mood = "O1"
        wsis "{sc=1}Oh,{/sc}{w=[wt2]} {sc=2}{size=+15}God!{/size}{/sc}{w=[wt2]} {sc=7}{size=+30}{nm}MOM{/nm}!!!!!{/size}{/sc}"
        show WSIS at OR_average
        $ wmom_mood = "O1"
        wsis "{aw}Hunf!{w=[wt2]} I'm going!!!{/aw}"
        wmom "{bt}Ara Ara...{/bt}{w=[wt2]} I can't understand this girl{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
        $ wmom_mood = "A1"
        wmom "{bt}Ara Ara...{/bt} I can't understand this girl...{fast} Hurry up, honey!{w=[wt2]} you need to get ready!"

    else:
        scene bg_home livingroom
        show WMOM at OL
        show HERO at RC
        show WSIS at RR
        $ wsis_fx = 0
        $ hero_fx = 0
        with Dissolve(3)

        show WMOM at LL_slow

        wmom "Oh, sweethearts{w=[wt1]}, You're still here!{w=[wt2]} Hurry and go take a shower!{w=[wt2]} Today is a special day.{w=[wt2]} We have to prepare ourselves to our celebration."
        if gametimemin <= 9:
            $ a_event_0 = "0"+str(gametimemin)
        else:
            $ a_event_0 = str(gametimemin)
        wsis "Ugh, mom...!{w=[wt1]} It's still [gametimehour]:[a_event_0]!{w=[wt3]} {nm}[fnamehero]{/nm} can go first."
        $ wmom_mood = "O1"
        wmom "Ehh...?{w=[wt2]} Why don't you take a shower together?{w=[wt2]}{nw}"
        $ wmom_mood = "A1"
        wmom "Ehh...? Why don't you take a shower together?{fast} You're siblings!"
        $ wsis_fx = "2"
        $ wsis_mood = "O3"
        $ hero_fx = "2"
        $ hero_mood = "O1"
        wsis "{sc=1}Oh,{/sc}{w=[wt2]} {sc=2}{size=+15}God!{/size}{/sc}{w=[wt2]} {sc=7}{size=+30}{nm}MOM{/nm}!!!!!{/size}{/sc}"
        show WSIS at OL_average
        $ wmom_mood = "O1"
        wsis "{aw}Hunf!{w=[wt2]} I'm going!!!{/aw}"
        wmom "{bt}Ara Ara...{/bt}{w=[wt2]} I can't understand this girl{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
        $ wmom_mood = "A1"
        wmom "{bt}Ara Ara...{/bt} I can't understand this girl...{fast} Hurry up, honey!{w=[wt2]} you need to get ready!"

    scene bg_0
    with Dissolve(1)

    call gametime_wait(18, 0) from _call_gametime_wait_19

    pause(1)

    $ hero_fx = 0
    $ hero_mood = "a1"
    call gametime from _call_gametime_91
    call goto_home_livingroom from _call_goto_home_livingroom_4

    $ Set_CharMap("hero", "home", "bedroom_hero")
    $ StartAct("wmom", (("changing", "casual"), 0), True)
    $ StartAct("wsis", (("changing", "casual"), 0), True)
    $ StartAct("wnei", (("changing", "casual"), 0), True)
    $ StartAct("wnei", (("moving", "home"), 0), True)
    $ StartAct("wmom", (("staying", "living_room"), 3*60), True)
    $ StartAct("wsis", (("staying", "living_room"), 3*60), True)
    $ StartAct("wnei", (("staying", "living_room"), 3*60), True)
    $ is_specialevent = True

    jump show_ui

#---------------------------------------------------------------------------
label scenestep_0_5: #Dinner End
#---------------------------------------------------------------------------
    $ hero_mood = "a1"
    $ wnei_mood = "a1"
    $ wsis_mood = "o1"
    $ wmom_mood = "a1"

    call hide_ui from _call_hide_ui_168

    #call goto_home_livingroom
    # `scene`, not `show`: `bg_home livingroom` is tag `bg_home` + attribute `livingroom`, so a `show` MERGES it into whatever that tag already carries (HERO is sent to bedroom_hero at 2572, leaving `bg_home bedroom hero` on screen) and resolves to an image that does not exist — which is why the raw single-tag `bg_home_livingroom` appeared to work. `scene` clears the layer first, like line 2432 and GameCheck.rpy:470.
    scene bg_home livingroom
    show HERO at LC
    show WMOM at RR
    show WSIS at OL
    show WNEI at CC
    with Fade(1,1,3)

    wnei "I think it's late.{w=[wt2]} I need to go home.{w=[wt2]} Good bye, {nm}[fnamehero]{/nm}!{w=[wt1]} Thanks for the party, Miss. {nm}[fnamewmom]{/nm}!"
    wmom "You're welcome, Honey.{w=[wt2]} It's a pleasure to have you here!"
    wnei "Where's {nm}[fnamewsis]{/nm}? "
    $ wmom_mood = "o1"
    wmom "She got very down, Dear...{w=[wt2]} I think she ate too much and is not feeling very well..."
    $ wnei_mood = "o1"
    $ hero_mood = "o1"
    wnei "Oh no!{w=[wt2]} Will she be okay?{w=[wt3]} Classes will start tomorrow!"
    wmom "I hope so, Dear...{w=[wt2]} I also hope I'm fine tomorrow to work...{nw}"
    show WSIS at LL_heavy
    wmom "I hope so, Dear... I also hope I'm fine tomorrow to work...{fast}{w=[wt3]} This ache in my back is killing me!"
    wsis "H{w=[wt1]}-hey{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Let me accompany you to your house."

    $ Set_CharMap("hero", "home", "living_room")
    $ StartAct("wnei", (("moving", "neighbor"), 0), True)
    $ StartAct("wmom", (("changing", "sleep"), 0), True)
    $ StartAct("wsis", (("changing", "sleep"), 0), True)
    $ StartAct("wnei", (("changing", "under"), 0), True)
    $ StartAct("wmom", ("sleeping", 8*60), True)
    $ StartAct("wsis", ("sleeping", 8*60), True)
    $ StartAct("wnei", ("sleeping", 8*60), True)

    menu:
        "Accompany {nm}[fnamewnei]{/nm} to her house":
            $ a_event_0 = "wnei"
            $ hero_mood = "a1"
            hero "Don't worry about {nm}[fnamewnei]{/nm}!{w=[wt1]} I'll accompany her."
            $ wnei_mood = "a3"
            $ wmom_mood = "a1"
            wnei "Yaaay!"
            wmom "Very gallant, Darling!{w=[wt2]} Make sure you take the key behind the door!"
            hero "Okay!"
            show WNEI at LL_slow
            wnei "Bye, {nm}[fnamewsis]{/nm}!{w=[wt2]} See ya tomorrow if ya survive!{w=[wt1]}{nw}"
            play SE1 "kiss.ogg"
            wnei "Bye, {nm}[fnamewsis]{/nm}! See ya tomorrow if ya survive! (kiss){fast}{w=[wt2]}{nw}"
            show WNEI at OL_slow
            show HERO at OL_slow
            wnei "Bye, {nm}[fnamewsis]{/nm}! See ya tomorrow if ya survive! (kiss){fast}"

            jump wnei_quest_2a

        "Take care of {nm}[fnamewsis]{/nm}":
            $ a_event_0 = "wsis"
            hero "Hey{w=[wt1]}, I think you better go rest."
            $ wmom_mood = "a2"
            wmom "{nm}[fnamehero]{/nm} is right, sweetheart!{w=[wt2]} Go rest and I'll accompany {nm}[fnamewnei]{/nm}{w=[wt1]}, okay?"
            wnei "Yes{w=[wt1]}, what if ya die on the way to my house?"
            wsis "H{w=[wt1]}-hey{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} Isn't it too much?"
            $ hero_mood = "a1"
            hero "I'll help you to get upstairs."
            $ wsis_fx = 1
            $ wsis_mood = "o2"
            $ wnei_mood = "a1"
            $ wmom_mood = "a1"
            wsis "I{w=[wt1]}-I d{w=[wt1]}-dont{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} need{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} y{w=[wt1]}-{nw}"
            hero "Hey{w=[wt1]}, don't die before finishing your sentence!{w=[wt2]} Come on!"
            wsis "S{w=[wt1]}-shut up!"
            show WNEI at LL_slow
            wnei "Bye, {nm}[fnamewsis]{/nm}!{w=[wt2]} See ya tomorrow if ya survive!{nw}"
            play SE1 "kiss.ogg"
            wnei "Bye, {nm}[fnamewsis]{/nm}! See ya tomorrow if ya survive!{fast}{w=[wt2]}{nw}"
            wnei "Bye, {nm}[fnamewsis]{/nm}! See ya tomorrow if ya survive! (kiss){fast}{w=[wt2]}{nw}"
            show WNEI at OL_slow
            show WMOM at OL_slow
            wnei "Bye, {nm}[fnamewsis]{/nm}! See ya tomorrow if ya survive! (kiss){fast}"

            jump wsis_quest_1_0

        "Give {nm}[fnamewmom]{/nm} a massage":
            $ a_event_0 = "wmom"
            $ hero_mood = "a2"
            hero "Let me help you with your back, {nm}[hero_to_wmom]{/nm}.{w=[wt2]} Maybe you'll wake up better tomorrow."
            $ wmom_mood = "a2"
            $ wnei_mood = "a1"
            wmom "Oh{w=[wt1]}, Darling...{w=[wt2]} I'd appreciate it a lot!{w=[wt3]} Let me just finish tidying things up here{w=[wt1]}, and let's go to my room, okay?"
            $ hero_mood = "a1"
            hero "Don't worry about it{w=[wt2]}, I think you already did too much today and need to rest a little.{w=[wt3]} Just wait for me there and let me take care of things here."
            wmom "You're so sweet, Darling{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Thank you for this!{w=[wt2]} I'll wait you in my room then.{w=[wt3]} Good bye, [fnamewnei]!{w=[wt2]} come back whenever you want!"
            $ wnei_mood = "a3"
            wnei "Good bye Miss {nm}[fnamewmom]{/nm}!{w=[wt2]} Good bye {nm}[fnamehero]{/nm}!{w=[wt2]} See ya tomorrow!{nw}"
            show WNEI at OL_slow
            show WSIS at OL_slow
            wnei "Good bye Miss {nm}[fnamewmom]{/nm}! Good bye {nm}[fnamehero]{/nm}! See ya tomorrow!{fast}"
            hero "Bye! See ya!"

            scene bg_0 with Dissolve(1)
            stop BGM fadeout 3
            pause

            mind "(Okay. Everything is done. It's time to give {nm}[hero_to_wmom]{/nm} a massage)"
            jump wmom_massage

    $ hero_quest_1 = 6

    $ Set_CharMap("hero", "home", "bedroom_hero")
    scene bg_home bedroom hero
    with Fade(3,1,3)

    if a_event_0 == "wmom":
        $ add_stat("wmom", "love", 2)
        $ add_stat("hero", "cha_soc", 2)
    if a_event_0 == "wsis":
        $ add_stat("wsis", "love", 2)
        $ add_stat("hero", "cha_soc", 2)
    if a_event_0 == "wnei":
        $ add_stat("wnei", "love", 2)
        $ add_stat("hero", "cha_soc", 2)

    mind "(Wooow...{w=[wt2]} Today was an intense day{w=[wt2]}{nw}"

    if a_event_0 == "wmom":
        $ add_stat("wmom", "inti", 1)
    if a_event_0 == "wsis":
        $ add_stat("wsis", "inti", 1)
    if a_event_0 == "wnei":
        $ add_stat("wnei", "inti", 1)

    mind "(Wooow... Today was an intense day{fast}, and probably tomorrow it should be even more!{w=[wt4]} In the morning I'm going to visit my new school.{w=[wt3]} At night I have an appointment with {nm}[hero_about_wcou]{/nm}.{w=[wt3]}.{w=[wt1]}.{w=[wt3]} I wonder what the future holds for me.{w=[wt3]} By the way{w=[wt2]}, I need to sleep soon{w=[wt1]}, or perhaps do a last night training)"
    
    jump show_ui

#---------------------------------------------------------------------------
label scenestep_0_4_call: #Videocall Start
#---------------------------------------------------------------------------

    stop BGM fadeout 3
    
    scene bg_0
    with Dissolve(1)
    pause 1

    scene scen_1_home_bg
    show scen_1_home_wmomandwsis_body
    show scen_1_home_wsisa_face o0
    show scen_1_home_wsisa_fg 2
    show scen_1_home_wmoma_face a0
    show scen_1_home_wmoma_eye d
    show scen_1_home_wmom_fg
    show scen_1_home_wsisa_eye d
    show scen_1_home_hero_body a
    show scen_1_home_heroa_face a0
    show scen_1_home_heroa_eye d
    show scen_1_home_wnei_body a1
    with Dissolve(3)
    play BGM "audio/W2C - Tranquility.mp3" fadein 3

    show scen_1_home_wmoma_face a1
    show scen_1_home_wmoma_eye l
    show scen_1_home_heroa_eye u
    wmom "Are you looking forward to talking to your grandma, Darling?{w=[wt2]} I'm sure she'll love this surprise!"

    show scen_1_home_wmoma_face a0
    hero "S{w=[wt1]}-sure.{w=[wt3]} {mind}(Well...{w=[wt2]} maybe not much{w=[wt2]}, but it can't be that bad, right?{w=[wt3]} She's not my biological grandmother{w=[wt1]}, but it would still be good to see {nm}[hero_to_wgma]{/nm} again.){/mind}"

    show scen_1_home_wmoma_face a1
    show scen_1_home_wmoma_eye r
    wmom "Sweetheart{w=[wt1]}, I want {nm}Mom{/nm} to see {nm}[fnamehero]{/nm}.{w=[wt2]} Could you show me again how this works please?"

    show scen_1_home_wsisa_face o1
    show scen_1_home_wmoma_face a0
    show scen_1_home_wmoma_eye d
    show scen_1_home_wsisa_fg 1
    wsis "Hmmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} First we need to start a video call with Cousin, so she can take us to Grandma."

    show scen_1_home_wmoma_face a1
    show scen_1_home_wsisa_face o0
    wmom "Oh{w=[wt1]}, it's true!{w=[wt1]} That's how we did it last time, wasn't it, Dear?"
    show scen_1_home_wmoma_face a0
    mind "(C{w=[wt1]}-cousin...?{w=[wt2]} Would it be {nm}[fnamewcou]{/nm}?{w=[wt3]} That's gonna be amazing!{w=[wt2]} I wonder how {nm}[hero_about_wcou]{/nm} is now.{w=[wt3]} You know{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} The first crush is something very difficult to forget...)"
    hero "Hey, {nm}[fnamewnei]{/nm}!{w=[wt2]} This way I won't be able to see anything!"

    show scen_1_home_wnei_body a2
    wnei "But I wanna see too{w=[wt1]}{nw}"
    show scen_1_home_wnei_body a1
    wnei "But I wanna see too{fast}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{nw}"
    show scen_1_home_wnei_body a2
    wnei "But I wanna see too...{fast} Got an idea!"

    pause(0.25)
    hide scen_1_home_hero_body
    hide scen_1_home_wnei_body
    show scen_1_home_wneiandhero_body
    show scen_1_home_wneib_face a0
    show scen_1_home_herob_face s1
    show scen_1_home_herob_eye l
    show scen_1_home_wmoma_eye l
    show scen_1_home_wsisa_face o2
    show scen_1_home_wsisa_eye l
    with dissolve
    pause(0.25)

    hero "{pa}E{w=[wt1]}-eehh!?{/pa}"

    show scen_1_home_herob_eye u
    show scen_1_home_herob_face s0
    show scen_1_home_wmoma_eye r
    show scen_1_home_wsisa_fg 2
    show scen_1_home_wsisa_face o3
    wsis "{aw}Hey, [C_Nam][fnamewnei][C_Off]!{w=[wt2]} {b}What are you doing!?{/b}{/aw}"
    show scen_1_home_wmoma_face a1
    show scen_1_home_wsisa_face o2
    wmom "Go easy on her, dear!{w=[wt2]} She also missed {nm}[fnamehero]{/nm} a lot and I'm sure he doesn't mind!"
    show scen_1_home_wmoma_face a0
    show scen_1_home_wsisa_face o1
    wsis "Hunf!{w=[wt1]}{nw}"
    show scen_1_home_wsisa_eye d
    show scen_1_home_wsisa_fg 1
    wsis "Hunf!{fast}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} H{w=[wt1]}-here.{w=[wt2]} Done!"
    show scen_1_home_herob_eye d
    show scen_1_home_wmoma_eye d
    show scen_1_home_wsisa_face o2
    show scen_1_home_wsisa_fg 2
    play SE1 "PhoneVibration.ogg"
    pause 2
    play SE1 "PhoneVibration.ogg"
    pause 2
    play SE1 "BeepRight.ogg"

    $ X_pos = 500
    scene scen_1_home_bg at X_average
    show scen_1_home_wmomandwsis_body at X_average
    show scen_1_home_wmoma_face a0 at X_average
    show scen_1_home_wmoma_eye d at X_average
    show scen_1_home_wmom_fg at X_average
    show scen_1_home_wsisa_face o0 at X_average
    show scen_1_home_wsisa_eye d at X_average
    show scen_1_home_wsisa_fg 2 at X_average
    show scen_1_home_wneiandhero_body at X_average
    show scen_1_home_wneib_face a0 at X_average
    show scen_1_home_herob_face s0 at X_average
    show scen_1_home_herob_eye d at X_average
    pause 0.01

    $ picaR_N = -540
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a0"
    show screen TwoPicas
    with wipeleft

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a1"

    wcou "Auntie!{w=[wt2]} Cousin!{w=[wt2]} {bt}What a surprise!{/bt}{w=[wt3]} Hi {nm}[fnamewnei]{/nm} my dear!{w=[wt2]} Oh!{w=[wt2]} Is that handsome man who I think he is?{w=[wt3]} {bt}Wow, auntie!{/bt}{w=[wt2]} Are you trying to give me a heart attack or something!?"

    show scen_1_home_wmoma_face a1
    show scen_1_home_herob_face a0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a0"

    wmom "{lg}Tche He He...{/lg}{w=[wt2]} It's him, darling!{w=[wt2]} He came back today and will live with us again!{w=[wt1]} Isn't it amazing?"

    show scen_1_home_wmoma_face a0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a1"

    wcou "Oh my God, Auntie!{w=[wt2]} That's nice to hear...{w=[wt2]}{nw}"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a3"

    wcou "Oh my God, Auntie! That's nice to hear...{fast}{w=[wt2]} I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {nm}[fnamehero]{/nm},  my condolences for Uncle.{w=[wt2]}{nw}"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a3"
    show scen_1_home_herob_face o0

    wcou "Oh my God, Auntie! That's nice to hear... I mean... {nm}[fnamehero]{/nm}, my condolences for Uncle.{fast} I hope you're fine now, dear."

    show scen_1_home_herob_face a1
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a2"

    hero "Thank you, {nm}[fnamewcou]{/nm}.{w=[wt2]} It's nice to talk to you again!"

    show scen_1_home_herob_face a0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a1"

    wcou "Tell me about it, babe!{w=[wt2]} I missed you so much!!!{w=[wt3]} When will you visit me so I can take a good look at you, hmm?"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a0"

    show scen_1_home_herob_face s1
    hero "{aw}W{w=[wt1]}-well...{w=[wt2]} I{w=[wt1]}-I...{/aw}"

    show scen_1_home_herob_face s0
    show scen_1_home_wmoma_face a1
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a0"

    wmom "{bt}Ara Ara...{/bt}{w=[wt2]} I'm sure he's dying to see you too, honey!{w=[wt2]} hope you have some free time for my big boy when he is not at school."

    show scen_1_home_wmoma_face a0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a3"

    wcou "Tell me about it, auntie!{w=[wt2]} Some days I don't even have time to go home to sleep."

    show scen_1_home_herob_face o0
    show scen_1_home_herob_eye u
    show scen_1_home_wmoma_face a1
    show scen_1_home_wmoma_eye l
    show scen_1_home_wsisa_face a0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a0"

    wmom "That's right, honey!{w=[wt1]} {nm}[fnamewcou]{/nm} is such a talented girl!{w=[wt3]} She graduated as doctor...{w=[wt2]} biologist...{w=[wt2]} neuroscientist...{w=[wt2]} psychologist...{w=[wt2]} lawyer...{w=[wt3]}{nw}"
    show scen_1_home_wmoma_eye d
    wmom "That's right, honey! {nm}[fnamewcou]{/nm} is such a talented girl! She graduated as doctor... biologist... neuroscientist... psychologist... lawyer...{fast} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Am I forgetting something, honey?"

    show scen_1_home_wmoma_face a0
    show scen_1_home_herob_eye d
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a1"

    wcou "Oh, Auntie!{w=[wt2]} If you talk like that, {nm}[fnamehero]{/nm} will think I'm some kind of genius!{w=[wt3]} I just used my {bt}methods...{/bt} {lg}He He...{/lg}"

    show scen_1_home_wsisa_face a1
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a0"

    wsis "If you are not at least a genius{w=[wt1]}, I must be at most a monkey!"
    show scen_1_home_wsisa_face a0
    show scen_1_home_wsisa_eye l
    show scen_1_home_wmoma_face o1
    show scen_1_home_wmoma_eye r
    wmom "{bt}Nooo...!{/bt}{w=[wt1]} Don't say that, my sweetheart!!!{w=[wt2]} I'm sure I'm the only dumb one in the family."
    show scen_1_home_wsisa_eye d
    show scen_1_home_wmoma_face a1
    show scen_1_home_wmoma_eye d
    wmom "{nm}[fnamewcou]{/nm}, my dear{w=[wt1]}, I also feel bad for not having time to visit you and {nm}Mom{/nm}.{w=[wt2]} You make me ashamed of myself working so much and still having time to take care of her!{w=[wt3]} By the way{w=[wt2]}, can you take us to her, darling?{w=[wt2]} I wanna show {nm}[fnamehero]{/nm}!{w=[wt2]} {lg}Tche He He He...{/lg}"

    show scen_1_home_wmoma_face a0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a3"

    wcou "I don't know if it's a good idea, auntie...{w=[wt2]}{nw}"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a1"

    wcou "I don't know if it's a good idea, auntie...{fast} I wonder if her heart will withstand this surprise... {gg}Hee-hee-hee...{/gg}{w=[wt3]} Just kidding!{w=[wt1]} She'll love it!{w=[wt2]} Let me just put on a bra and I'll take you downstairs, okie?{w=[wt2]} I'll be embarrassed if the {nm}[fnamehero]{/nm} sees more than he should."

    show scen_1_home_herob_face s0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma a0"

    mind "({fast}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"
    mind "(...){fast}"
    stop BGM fadeout 10
    $ picaR_N = -500
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma b1"
    show screen TwoPicas
    with vpunch
    pause 0.4
    $ picaR_N = 0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma b1"
    show screen TwoPicas
    with hpunch
    pause 0.2
    $ picaR_N = -200
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma b2"
    show scen_1_home_herob_face s1
    show screen TwoPicas
    with hpunch
    wcou "Just a minute, okay?"
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma b3"
    show screen TwoPicas
    with Dissolve(1)
    play BGM "audio/W2C - Fun.mp3" fadein 3

    hide screen TwoPicas

    $ zoomT1 = 0
    $ zoomS1 = 1
    $ zoomX1 = 0.5
    $ zoomY1 = 0.5
    $ zoomT2 = 4
    $ zoomS2 = 4
    $ zoomX2 = 0.4
    $ zoomY2 = 0.25
    scene scen_1_home_bg at ZoomSTXY
    show scen_1_home_wmomandwsis_body at ZoomSTXY
    show scen_1_home_wmoma_face a0 at ZoomSTXY
    show scen_1_home_wmoma_eye d at ZoomSTXY
    show scen_1_home_wmom_fg at ZoomSTXY
    show scen_1_home_wsisa_face o0 at ZoomSTXY
    show scen_1_home_wsisa_eye d at ZoomSTXY
    show scen_1_home_wsisa_fg 2 at ZoomSTXY
    show scen_1_home_wneiandhero_body at ZoomSTXY
    show scen_1_home_wneib_face a0 at ZoomSTXY
    show scen_1_home_herob_face s1 at ZoomSTXY
    show scen_1_home_herob_eye d at ZoomSTXY

    with wiperight
    mind "(Wooow!!!{w=[wt2]} She has nipple piercings!!!)"

    play SE1 "SWFMoan245.ogg"

    $ zoomT1 = 0
    $ zoomS1 = 4
    $ zoomX1 = 0.4
    $ zoomY1 = 0.25
    $ zoomT2 = 0.25
    $ zoomS2 = 3
    $ zoomX2 = 0.25
    $ zoomY2 = 0.1

    scene scen_1_home_bg at ZoomSTXY
    hide scen_1_home_wneiandhero_body
    hide scen_1_home_wneib_face a0
    hide scen_1_home_herob_face s1
    show scen_1_home_wmomandwsis_body at ZoomSTXY
    show scen_1_home_wmoma_face a0 at ZoomSTXY
    show scen_1_home_wmoma_eye d at ZoomSTXY
    show scen_1_home_wmom_fg at ZoomSTXY
    show scen_1_home_wsisa_face o0 at ZoomSTXY
    show scen_1_home_wsisa_eye d at ZoomSTXY
    show scen_1_home_wsisa_fg 2 at ZoomSTXY
    show scen_1_home_wneiandhero a2 at ZoomSTXY

    pause 0.5

    $ zoomT1 = 0
    $ zoomS1 = 3
    $ zoomX1 = 0.25
    $ zoomY1 = 0.1
    $ zoomT2 = 1
    $ zoomS2 = 3
    $ zoomX2 = 0.2
    $ zoomY2 = 0.8

    scene scen_1_home_bg at ZoomSTXY
    show scen_1_home_wmomandwsis_body at ZoomSTXY
    show scen_1_home_wmoma_face a0 at ZoomSTXY
    show scen_1_home_wmoma_eye d at ZoomSTXY
    show scen_1_home_wmom_fg at ZoomSTXY
    show scen_1_home_wsisa_face o0 at ZoomSTXY
    show scen_1_home_wsisa_eye l at ZoomSTXY
    show scen_1_home_wsisa_fg 2 at ZoomSTXY
    show scen_1_home_wneiandhero a2 at ZoomSTXY

    wnei ".{w=[wt1]}.{w=[wt1]}.{w=[wt1]}What's{w=[wt1]}-{nw}"

    $ zoomT1 = 0
    $ zoomS1 = 3
    $ zoomX1 = 0.2
    $ zoomY1 = 1.0
    $ zoomT2 = 0.3
    $ zoomS2 = 1
    $ zoomX2 = 0.5
    $ zoomY2 = 0.5

    scene scen_1_home_bg at ZoomSTXY
    show scen_1_home_wmomandwsis_body at ZoomSTXY
    show scen_1_home_wmoma_face a0 at ZoomSTXY
    show scen_1_home_wmoma_eye d at ZoomSTXY
    show scen_1_home_wmom_fg at ZoomSTXY
    show scen_1_home_wsisa_face o2 at ZoomSTXY
    show scen_1_home_wsisa_eye l at ZoomSTXY
    show scen_1_home_wsisa_fg 2 at ZoomSTXY
    show scen_1_home_wneiandhero a3 at ZoomSTXY
    show scen_1_home_heroa3_eye l at ZoomSTXY

    hero "{aw}Shhh...!{/aw}"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma b4"
    show screen TwoPicas

    scene scen_1_home_bg at LC_slow
    show scen_1_home_wmomandwsis_body at LC_slow
    show scen_1_home_wmoma_face a0 at LC_slow
    show scen_1_home_wmoma_eye d at LC_slow
    show scen_1_home_wmom_fg at LC_slow
    show scen_1_home_wsisa_face o2 at LC_slow
    show scen_1_home_wsisa_eye d at LC_slow
    show scen_1_home_wsisa_fg 2 at LC_slow
    show scen_1_home_wneiandhero a3 at LC_slow
    show scen_1_home_heroa3_eye r at LC_slow
    with wipeleft
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma b5"

    wcou "{bt}{b}Tadaaah...!{/b}{/bt}{w=[wt2]} Am I good enough for the party, my lovelies?"

    show scen_1_home_wmoma_face a1
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma b4"

    wmom "{bt}Ara Ara...{/bt}{w=[wt2]} Of course, dear!{w=[wt1]} You're gorgeous!!"

    show scen_1_home_wmoma_face a0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma b5"

    wcou "Then I'll take you downstairs to Granny!{w=[wt3]} Hold the line just a minute, okay?"

    hide screen TwoPicas

    scene scen_1_home_bg at CC_slow
    show scen_1_home_wmomandwsis_body at CC_slow
    show scen_1_home_wmoma_face a0 at CC_slow
    show scen_1_home_wmoma_eye d at CC_slow
    show scen_1_home_wmom_fg at CC_slow
    show scen_1_home_wsisa_face o2 at CC_slow
    show scen_1_home_wsisa_eye d at CC_slow
    show scen_1_home_wsisa_fg 2 at CC_slow
    show scen_1_home_wneiandhero a3 at CC_slow
    show scen_1_home_heroa3_eye r at CC_slow
    with wiperight

    show scen_1_home_wmoma_face a1
    wmom "We'll wait you, dear!"

    hide scen_1_home_heroa3_eye
    show scen_1_home_wneiandhero a4 at LL
    show scen_1_home_wneiandhero a4 at OR_slow
    show scen_1_home_wmoma_face a0
    show scen_1_home_wmoma_eye l
    show scen_1_home_wsisa_eye l
    hero "{aw}In the meantime I'll go{/aw}{nw}"
    show scen_1_home_wmoma_eye r
    hero "{aw}In the meantime I'll go{fast} right{/aw}{nw}"
    show scen_1_home_wsisa_eye r
    hero "{aw}In the meantime I'll go right{fast} there real quick with [C_Nam][fnamewnei][C_Off]!{/aw}"

    show scen_1_home_wsisa_face o3
    show scen_1_home_wsisa_eye d
    wsis "What's up with these two?!"

    show scen_1_home_wmoma_face a1
    show scen_1_home_wsisa_face o2
    show scen_1_home_wsisa_eye l
    wmom "I don't know, Sweetheart.{w=[wt2]} Why don't you go there and ask them?"

    show scen_1_home_wmoma_face a0
    show scen_1_home_wsisa_face o3
    show scen_1_home_wsisa_eye r
    wsis "{aw}A{w=[wt1]}-as i{w=[wt1]}-if I care!{/aw}{nw}"
    show scen_1_home_wsisa_face o2
    stop BGM fadeout 6
    wsis "{aw}A-as i-if I care!{/aw}{fast}"

    $ wnei_wear = "casual"
    $ wnei_mood = "o1"
    $ hero_mood = "o1"
    $ hero_fx = "2"
    scene bg_home diningroom
    show HERO at OR
    show WNEI at OR
    with Dissolve(1)

    play BGM "audio/W2C - Awkward.mp3" fadein 3

    show HERO at RC_slow
    show WNEI at RC_slow
    pause 1.25

    show WNEI at CC_slow

    hero "{aw}H{w=[wt1]}-hey, I'm sorry I{w=[wt1]}-I...{/aw}"
    wnei "I felt something poking me.{w=[wt1]} What's that?"
    hero "{aw}T{w=[wt1]}-t{w=[wt1]}-that's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{/aw}{nw}"

    menu:
        hero "{aw}T-t-that's...{/aw}{fast}"

        '"My lollipop"':
            hero "{aw}T-t-that's...{fast} my l{w=[wt1]}-''lollipop!''{w=[wt4]} Don't tell anyone, please!{/aw}"
            $ wnei_mood = "a1"
            wnei "Ohhh...{w=[wt2]} So that was it!{w=[wt3]} Your lollipop makes me feel{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} {aw}k{w=[wt1]}-kinda weird...?{/aw}{w=[wt4]} Why did it got super big?{w=[wt2]} is that a super power?"
            $ add_stat("wnei", "lust", 1)
            $ add_stat("hero", "cha_soc", 0.1)
            $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm}'s  lust {color=#32FF32}+")+str(1 * lustadd_wnei)[:4])
            $ X_pos = 1100
            show WNEI at X_average
            pause 0.5
            show HERO at RR_average
            $ hero_mood = "o1"
            hero "{aw}H{w=[wt1]}-hey!{/aw}{nw}"
            $ wnei_mood = "o1"
            hero "{aw}H-hey!{fast} D{w=[wt1]}-don't touch it!{/aw}"
            wnei "{bt}But...{/bt}"

        '"My phone"':
            $ hero_mood = "a2"
            hero "{aw}T-t-that's...{fast} just my phone!{/aw} {gg}He-he...{/gg}"
            wnei "Is dat true?{w=[wt2]} B{w=[wt1]}-but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} I feel like it was moving!"
            hero "{aw}O{w=[wt1]}-oh{w=[wt2]}, m{w=[wt1]}-maybe it's the vibra call? {/aw} {gg}He-he...{/gg}"
            $ wnei_mood = "a1"
            wnei "Ohhh...{w=[wt2]} So that was it!{w=[wt3]} I felt{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"

            $ X_pos = 1100
            show WNEI at X_average

            wnei "Ohhh... So that was it! I felt...{fast}{w=0.25} {aw}k{w=[wt1]}-kinda weird...?{/aw}{w=[wt1]}{nw}"

            show HERO at RR_average

            $ hero_mood = "o1"

            wnei "Ohhh... So that was it! I felt...{aw}k-kinda weird...?{/aw}{fast}{w=[wt1]}{nw}"
            hero "{aw}H{w=[wt1]}-hey!{/aw}{nw}"
            $ wnei_mood = "o1"
            hero "{aw}H-hey!{fast} D{w=[wt1]}-don't touch it!{/aw}"
            $ wnei_mood = "o2"
            wnei "It's...{w=[wt1]} yar lollipop!{w=[wt3]} {bt=a2-s1-p25}{b}You lied to me!{/b}{/bt}"
            hero "{aw}I{w=[wt1]}-it's cos I think you're too pure to think about this kind of things, okay?{/aw}"
            $ add_stat("wnei", "love", 1)
            $ add_stat("hero", "cha_soc", 1)
            $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm}'s  love {color=#32FF32}+")+str(1 * loveadd_wnei)[:4])
            $ wnei_mood = "o1"
            wnei "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}{bt}Okay...{/bt}"

    $ hero_fx = "1"
    hero "Come on!{w=[wt2]} Let's take a drink!"
    $ wnei_mood = "a2"
    wnei "Oh{w=[wt1]}, so that's why you brought me here!{w=[wt3]} But I have another question..."
    hero "{aw}W{w=[wt1]}-what is it?{/aw}"
    wnei "Why {nm}[fnamewsis]{/nm} said she's a monkey?{w=[wt3]} I didn't get'er!"
    hero "Eh...?"
    wnei "Hm?"
    mind "(So it's just that...{w=[wt2]} What a relief!{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} Somehow my dick calmed down after all that talk...){w=[wt4]}{nw}"
    $ hero_fx = "0"
    $ hero_mood = "a1"
    hero "{mind}(So it's just that... What a relief! Well... Somehow my dick calmed down after all that talk...){/mind}{fast} Hey{w=[wt1]}, let's go back!{w=[wt2]} {nm}[hero_about_wcou!c]{/nm} must have gotten to {nm}[hero_about_wgma]{/nm} by now"

    show HERO at OR_slow
    show WNEI at OR_slow

    hero "{nw}"

    scene scen_1_home_bg
    show scen_1_home_wmomandwsis_body
    show scen_1_home_wmoma_face a0
    show scen_1_home_wmoma_eye d
    show scen_1_home_wmom_fg
    show scen_1_home_wsisa_face o0
    show scen_1_home_wsisa_eye d
    show scen_1_home_wsisa_fg 2
    show scen_1_home_hero_body c at OL
    show scen_1_home_wnei_body c at OR
    with Fade(1,0,3)

    show scen_1_home_hero_body c at CC_slow
    show scen_1_home_wnei_body c at CC_slow

    show scen_1_home_wsisa_face o2
    show scen_1_home_wsisa_eye r
    pause 0.2
    show scen_1_home_wsisa_eye l
    pause 0.3
    show scen_1_home_wsisa_eye r
    pause 0.1

    wnei "We're here!"

    hide scen_1_home_wnei_body
    hide scen_1_home_wsisa_face
    hide scen_1_home_wsisa_eye
    hide scen_1_home_wsisa_fg
    hide scen_1_home_wmomandwsis_body
    hide scen_1_home_wmoma_face a0
    hide scen_1_home_wmoma_eye d
    hide scen_1_home_wmom_fg
    show scen_1_home_wmom_body b
    show scen_1_home_wmomb_face a0
    show scen_1_home_wmomb_eye r
    show scen_1_home_wmom_fg
    show scen_1_home_wneiandwsis c1
    with dissolve

    wsis "Hey, {nm}[fnamewnei]{/nm}!{w=[wt1]} Don't tell me you don't sit down cos you're waiting {nm}[fnamehero]{/nm} to sit!?{w=[wt2]}{pr}{bt=a2-s1-p25}No way!{w=[wt3]} {b}You're mine now!{/b}{/bt}"

    hide scen_1_home_wmom_body
    hide scen_1_home_wmomb_face
    hide scen_1_home_wmomb_eye
    hide scen_1_home_wmom_fg
    hide scen_1_home_hero_body
    hide scen_1_home_wneiandwsis
    show scen_1_home_wneiandwsis c2
    show scen_1_home_wneic_eye l
    show scen_1_home_wneic_face o0
    show scen_1_home_wsisc_eye r
    show scen_1_home_wsisc_face o0
    show scen_1_home_wmom_body b
    show scen_1_home_wmomb_face a0
    show scen_1_home_wmomb_eye r
    show scen_1_home_wmom_fg
    show scen_1_home_hero_body a
    show scen_1_home_heroa_face o0
    show scen_1_home_heroa_eye u
    with Dissolve(1)

    show scen_1_home_wneic_face o1

    wnei "{bt=a3-s1-p15}Nooo!{/bt}{w=[wt1]} I wanna sit on {nm}[fnamehero]{/nm}'s lap, not yours!"

    show scen_1_home_wsisc_face o1
    show scen_1_home_wneic_face o0
    show scen_1_home_wmomb_face o0

    wsis "Not fair!{w=[wt2]} I feel offended now!"

    hide scen_1_home_wneic_eye l
    hide scen_1_home_wneic_face o0
    hide scen_1_home_wsisc_eye r
    hide scen_1_home_wsisc_face o0
    show scen_1_home_wneiandwsis c3

    wnei "{bt=a2-s1-p25}{sc=1}Ahhh!{w=[wt1]} Stop!{w=[wt2]} it hurts!{/sc}{/bt}"

    show scen_1_home_wmomb_face o1

    wmom "Darling,{w=[wt1]} please be careful!{nw}"

    hide scen_1_home_wmom_body
    hide scen_1_home_wmomb_face
    hide scen_1_home_wmomb_eye
    hide scen_1_home_wmom_fg
    hide scen_1_home_hero_body
    hide scen_1_home_heroa_face
    hide scen_1_home_heroa_eye
    show scen_1_home_wneiandwsis c2
    show scen_1_home_wneic_eye l
    show scen_1_home_wneic_face o0
    show scen_1_home_wsisc_eye l
    show scen_1_home_wsisc_face o0
    show scen_1_home_wmom_body b
    show scen_1_home_wmomb_face o1
    show scen_1_home_wmomb_eye r
    show scen_1_home_wmom_fg
    show scen_1_home_hero_body a
    show scen_1_home_heroa_face o0
    show scen_1_home_heroa_eye u

    wmom "Darling, please be careful!{fast}{w=[wt3]} You know that {nm}[fnamewnei]{/nm} nipples are super sensitive!"

    show scen_1_home_heroa_eye d
    show scen_1_home_wmomb_face o0
    mind "(Oh, God...{w=[wt3]} I'm learning so many things today...)"
    show scen_1_home_wsisc_eye r
    show scen_1_home_wsisc_face o1
    wsis "Okay{w=[wt1]}, I'll take care of my baby."

    $ picaR_N = -540
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0go0"
    show screen TwoPicas

    $ X_pos = 400
    scene scen_1_home_bg at X_average

    scene scen_1_home_bg at X_average
    show scen_1_home_wneiandwsis c2 at X_average
    show scen_1_home_wneic_eye d at X_average
    show scen_1_home_wneic_face o0 at X_average
    show scen_1_home_wsisc_eye d at X_average
    show scen_1_home_wsisc_face o0 at X_average
    show scen_1_home_wmom_body b at X_average
    show scen_1_home_wmomb_face a0 at X_average
    show scen_1_home_wmomb_eye d at X_average
    show scen_1_home_wmom_fg at X_average
    show scen_1_home_hero_body a at X_average
    show scen_1_home_heroa_face o0 at X_average
    show scen_1_home_heroa_eye d at X_average
    with wipeleft

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca1go0"
    wcou "Hey, Granny!{w=[wt1]}     me to see you today!"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0go0"

    wgma "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"
    window hide
    pause

    show scen_1_home_wmomb_face o0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0go1"

    wgma "Is it a video?{w=[wt2]} Who is this bitch?"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca1go0"

    wcou "Oh no, Granny!{w=[wt2]} Don't tell me you don't recognize your own daughter?{w=[wt3]} It's {nm}Aunt [fnamewmom]{/nm}!"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0go1"

    wgma "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nm}[fnamewmom]{/nm} is not fat like that..."

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0go0"
    show scen_1_home_wmomb_face o1

    wmom "{nm}Mom{/nm}!{w=[wt2]} Why are you so mean!?"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0ga1"
    show scen_1_home_wmomb_face o0

    wgma "Ohhh{w=[wt1]}, {nm}[fnamewmom]{/nm}, it's you!{w=[wt1]} {lg}Tcho Ho Ho Ho...{/lg}{w=[wt4]} Are you talking to me from inside the telephone?{w=[wt4]} It's been so long since you came to visit me that I didn't even recognize you anymore, my dear!{w=[wt2]} I guess you've been eating too much, huh...?"
    wgma "By the way, who are these people, Dear?{w=[wt2]} Are you into young people now?{w=[wt2]} Huh?{w=[wt4]} Oh!{w=[wt2]} Wait!{w=[wt2]} I just realized!{w=[wt4]} You are breastfeeding them, right my Dear?{w=[wt4]} You haven't changed at all... {lg}Tcho Ho Ho Ho...{/lg}"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0ga0"

    mind "(Oh{w=[wt1]}, I didn't expect such an awkward conversation!)"
    show scen_1_home_wmomb_face a1
    show scen_1_home_wmomb_eye r
    wmom "Here's your granddaughter {nm}[fnamewsis]{/nm} and her friend {nm}[fnamewnei]{/nm}!"
    show scen_1_home_wmomb_eye d
    show scen_1_home_wmomb_face a0
    show scen_1_home_wneic_face a0
    show scen_1_home_wsisc_face o1
    wsis "Hi, {nm}Grandma{/nm}!"
    show scen_1_home_wneic_face a1
    show scen_1_home_wsisc_face o0
    wnei "Hey {nm}Miss Grandma{/nm}!"

    show scen_1_home_wneic_face a0
    show scen_1_home_wsisc_face o0
    show scen_1_home_heroa_face a0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0ga1"
    wgma "Ohhh!{w=[wt2]} {lg}Tcho Ho Ho Ho...{/lg}{w=[wt3]} So it's them!!{w=[wt4]} They became such beautiful girls that I didn't recognize them!{w=[wt3]} Grandma love you, babies!{w=[wt3]} I remember you since you were little snotnoses brats!{w=[wt3]} I still have a great memory, you know?"

    show scen_1_home_wsisc_face o1
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0ga0"
    wsis "But we talked via video call a few months ago, Gramma!"

    show scen_1_home_wsisc_face o0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0ga1"
    wgma 'Hmm...?{w=[wt3]} Did we?{w=[wt4]} What is "video call"?'

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0ga0"
    show scen_1_home_wmomb_face a1
    show scen_1_home_wmomb_eye l

    wmom "And here's {nm}[fnamehero]{/nm}, {nm}Mom{/nm}!"
    show scen_1_home_wmomb_eye d
    show scen_1_home_wmomb_face a0
    show scen_1_home_heroa_face a1

    hero "H{w=[wt1]}-hi, {nm}[hero_to_wgma]{/nm}!"

    show scen_1_home_heroa_face a0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0go0"
    wgma "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0go1"
    wgma "...{fast}{aw}OHHH!{/aw}{w=[wt3]} Is that [C_Nam][fnamehero][C_Off]!?{w=[wt3]} {pa}Oh God!!!{/pa}{w=[wt3]} {bt}He became so handsome!!!{/bt}{w=[wt4]}{nw}"
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0ga1"
    wgma "...{aw}OHHH!{/aw}{w=[wt3]} Is that [C_Nam][fnamehero][C_Off]!?{w=[wt3]} {pa}Oh God!!!{/pa}{w=[wt3]} {bt}He became so handsome!!!{/bt}{fast}{vspace=1}I remember him when he was just a wee boy!{w=[wt2]} I miss you and your dad so much, Dear!{w=[wt3]} Those were good times{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} It makes me think that the best decision {nm}[fnamewmom]{/nm} did in her life was to spread her legs to your dad and join our family!"

    show scen_1_home_heroa_face o0
    show scen_1_home_wmomb_face o1
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma co0ga0"
    wmom "{pa}{nm}MOM{/nm}!!!{/pa}"
    show scen_1_home_wmomb_face o0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0ga0"
    mind "(Wait{w=[wt2]}, is it some kind of karma for {nm}[hero_about_wsis]{/nm}?{w=[wt3]} Or maybe this is all just a family tradition of shaming the next generation?)"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0ga1"
    wgma "Back then, everything was joy...{w=[wt3]} You kids used to play naked in the garden! {lg}Tcho Ho Ho Ho...{/lg}{w=[wt3]} {nm}[fnamehero]{/nm} just had a cute little pee-pee. Now it should be enough to put a woman in the clouds, isn't it?{w=[wt3]} {lg}Tcho Ho Ho Ho...{/lg}"

    show scen_1_home_wmomb_eye r
    show scen_1_home_wmomb_face o2
    show scen_1_home_wsisc_eye r
    show scen_1_home_wsisc_face o0
    show scen_1_home_wneic_face a1
    show scen_1_home_heroa_eye u
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma co0ga0"

    wnei "{bt}{b}IT'S SUPER DUPER BIG NOW, MISS!{/b}{/bt}"

    show scen_1_home_wmomb_eye r
    show scen_1_home_wmomb_face o1
    show scen_1_home_wsisc_eye r
    show scen_1_home_wsisc_face o2
    show scen_1_home_wneic_face a0
    show scen_1_home_heroa_face o1

    $ a_check_1 = str(fnamehero)+", "+str(fnamewmom)+", and "+str(fnamewsis)
    sup1 "{vspace=30}{pa}{size=60}EHHH!?!?!?{/size}{/pa}"

    show scen_1_home_wmomb_eye d
    show scen_1_home_wmomb_face o0
    show scen_1_home_wsisc_eye d
    show scen_1_home_wsisc_face o0
    show scen_1_home_wneic_face a0
    show scen_1_home_heroa_eye d
    show scen_1_home_heroa_face o0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0ga1"

    wgma "You know your stuff, little girl!{w=[wt2]} You'll go far! {lg}Tcho Ho Ho Ho...{/lg}{w=[wt4]} {nm}[fnamehero]{/nm}, dear{w=[wt2]}, if you're not only into young girls, come visit your old Grandma, and give her a little care, huh?{w=[wt3]} I wanna take a closer look at you to see how much you've grown!"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma co0ga0"
    show scen_1_home_wmomb_face o1

    wmom "{aw}W{w=[wt1]}-what are you saying, [C_Nam]Mom[C_Off]!?{w=[wt3]} [C_Nam][fnamehero][C_Off] is my son!{w=[wt3]} {b}Stop that!!!{/b}{/aw}"
    show scen_1_home_wmomb_face o0

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma co0go1"

    wgma "What!?{w=[wt2]} You never come to see me just once and now you don't even leave my grandchildren either?"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma co0go0"
    show scen_1_home_wmomb_face o1

    wmom "{aw}I{w=[wt1]}-it's not that, Mom{w=[wt2]}, it's just{w=[wt1]}-{/aw}{nw}"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma cogo"
    show screen TwoPicas
    with vpunch
    wmom "I-it's not that, {nm}Mom{/nm}, it's just-{fast}...{nw}"
    $ picaR_N = -720
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma co0"
    pause 0.1
    $ picaR_N = 0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma cogo"
    pause 0.1
    $ picaR_N = 0
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma co0"
    pause 0.1
    $ picaR_N = -540
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma cogo"
    show screen TwoPicas
    with vpunch

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma co1"
    show scen_1_home_wmomb_face o0

    wcou "W{w=[wt1]}-well{w=[wt2]}, I think it's enough for now, babes!{w=[wt3]} It's time for Granny to take her medicine, okie?"

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma co0"
    show scen_1_home_wmomb_face o1
    wmom "You're right, darling.{w=[wt3]} I think it's better to hang up now."

    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma co1"
    show scen_1_home_wmomb_face o0

    wcou "I'm sorry for that, Auntie.{w=[wt3]} We know that Granny is getting old and already running out of filters... {gg}He-he...{/gg}{w=[wt3]}{nw}"
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca1"
    wcou "I'm sorry for that, Auntie. You know that Granny is getting old and already running out of filters... {gg}He-he...{/gg}{fast} But don't worry{w=[wt1]}, she'll forget it soon!"
    wcou "By the way{w=[wt1]}, I remembered I have a perfect day on my schedule to see {nm}[fnamehero]{/nm}{w=[wt1]}, and I'm scheduling it right now on my phone.{w=[wt4]} {nm}[fnamewsis]{/nm}, babe{w=[wt1]}, could you send {nm}[fnamehero]{/nm} my contact and the office address?"

    show scen_1_home_wmomb_face a0
    show scen_1_home_wmomb_eye r
    show scen_1_home_wsisc_face o1
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca0"

    wsis "{aw}S{w=[wt1]}-sure...{/aw}"

    show scen_1_home_wsisc_face o0
    show scen_1_home_wmomb_eye d
    $ picaR = "Scene Day 1 - NightCelebration/scen_1_home_wgma ca1"

    wcou "Thank you, babe!{w=[wt2]} Come to my office tomorrow night, {nm}[fnamehero]{/nm}!{w=[wt3]} You've been away too long and I need to know how you're doing.{w=[wt3]} You'll get a free check-up.{w=[wt2]} No delays.{w=[wt2]} I'll be waiting for you!{w=[wt4]} Have a {bt}Good Nite{/bt}, babes.{w=[wt1]} Love you all so much!{w=[wt1]}{nw}"
    play SE1 "kiss.ogg"
    wcou "Thank you, babe! Come to my office tomorrow night, {nm}[fnamehero]{/nm}! You've been away too long and I need to know how you're doing. You'll get a free check-up. No delays. I'll be waiting for you! Have a {bt}Good Nite{/bt}, my lovelies. Love you all so much! (kiss){fast}"

    hide screen TwoPicas
    scene scen_1_home_bg at CC
    show scen_1_home_wneiandwsis c2 at CC
    show scen_1_home_wneic_eye d at CC
    show scen_1_home_wneic_face a0 at CC
    show scen_1_home_wsisc_eye d at CC
    show scen_1_home_wsisc_face o0 at CC
    show scen_1_home_wmom_body b at CC
    show scen_1_home_wmomb_face a0 at CC
    show scen_1_home_wmomb_eye d at CC
    show scen_1_home_wmom_fg at CC
    show scen_1_home_hero_body a at CC
    show scen_1_home_heroa_face o0 at CC
    show scen_1_home_heroa_eye d at CC
    with wiperight

    show scen_1_home_wmomb_face a1
    show scen_1_home_wmomb_eye l
    show scen_1_home_wsisc_eye l
    show scen_1_home_wneic_eye l
    show scen_1_home_heroa_eye u
    wmom "{bt}Ara Ara...{/bt}{w=[wt2]} That's so nice, honey!{w=[wt2]} Your cousin is very talented in whatever she does{w=[wt2]}, and now she gets to look after your health.{w=[wt3]} I’m glad she’s a part of our family.{w=[wt2]} Rest assured{w=[wt1]}, you’re now in excellent hands, honey!"

    stop BGM fadeout 5
    show scen_1_home_wmomb_face o2
    show scen_1_home_wmomb_eye r
    show scen_1_home_wneic_face a1
    show scen_1_home_wsisc_eye r
    wnei "Will she measure his lollipop?"
    show scen_1_home_wneic_face a0
    window hide
    $ hero_quest_1 += 2

    pause 1
    scene bg_0
    with Dissolve(3)
    play BGM "audio/W2C - Tranquility.mp3"
    pause 1
    jump show_ui
