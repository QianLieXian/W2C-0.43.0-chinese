# A single add_stat() call may never move a stat by more than this many points at once, no matter how large the raw value or its Stat_Modifiers multiplier (e.g. the boosted lust base gain). Caps every stat — inti/love/lust/club rep/anything — to ±STAT_STEP_CAP per call.
define STAT_STEP_CAP = 25

init python:

    def calculate_substat():
        triples = [
            ("stat_int", "stat_int_log", "stat_int_mem", "stat_int_per"),
            ("stat_phy", "stat_phy_str", "stat_phy_agi", "stat_phy_res"),
            ("stat_cha", "stat_cha_soc", "stat_cha_per", "stat_cha_sex"),
        ]
        for stat_key, primary, sub_b, sub_c in triples:
            stat_value = getattr(store, stat_key)
            subs = {
                primary: getattr(store, primary),
                sub_b:   getattr(store, sub_b),
                sub_c:   getattr(store, sub_c),
            }
            extra = stat_value * 3 - sum(subs.values())
            if extra > 0:
                subs[primary] += extra
            for _ in range(50):
                over_key = next((k for k, v in subs.items() if v > 100), None)
                if over_key is None:
                    break
                overflow = subs[over_key] - 100
                subs[over_key] = 100
                others = [k for k in subs if k != over_key]
                for o in others:
                    subs[o] += overflow / 2.0
            for k, v in subs.items():
                setattr(store, k, round(v, 2))

# ----------------------------------------------------------------------------------------------------
# General Check
# ----------------------------------------------------------------------------------------------------
label gamecheck:

    $ config.menu_include_disabled = False
    # $ config.main_menu_music = "audio/W2C - MainTheme.mp3"

    #$ afterload_0_36 = True # Debug For v0.36
    $ afterload_0_37 = True # Debug For v0.37

    $ is_resetmood = True
    call hide_ui from _call_hide_ui_121
    call gametime from _call_gametime_78
    call check_playermap from _call_check_playermap_32
    $ check_stat()
    $ calculate_substat()

    python: # Auto-recap date intimacy ceilings to `char_inti_req_date` (a `define`)
        for buceta in ("wsis_inti_cap", "wnei_inti_cap", "wmom_inti_cap"):
            # A ceiling EARNED on a date is a reward and is never taken back, whatever the define says.
            if getattr(store, buceta) >= char_inti_req_date:
                continue
            if getattr(store, buceta) in (40, 50) and getattr(store, buceta) != char_inti_req_date:
                setattr(store, buceta, char_inti_req_date)

    # The infinite money/perk cheats top themselves back up here, and a save that still holds the old math.inf value is repaired to the same finite number.
    $ money = CHEAT_MONEY if (cheat_money or not math.isfinite(money)) else round(money, 2)
    $ perk = CHEAT_PERK if (cheat_perk or not math.isfinite(perk)) else perk
    #$ scenestep[2] = 0
    $ a_event_0 = 0
    $ a_event_1 = 0
    $ a_event_2 = 0
    $ a_event_3 = 0
    $ a_event_4 = 0
    $ a_event_5 = 0
    $ a_event_6 = 0
    $ a_event_7 = 0
    $ a_event_8 = 0
    $ a_event_9 = 0
    $ a_check_0 = 0
    $ a_check_1 = 0
    $ a_check_2 = 0
    $ a_check_3 = 0
    $ a_check_4 = 0
    $ a_check_5 = 0
    $ a_check_6 = 0
    $ a_check_7 = 0
    $ a_check_8 = 0
    $ a_check_9 = 0
    $ a_item_0 = 0
    $ a_item_1 = 0
    $ a_item_2 = 0
    $ a_item_3 = 0
    $ a_item_4 = 0
    $ a_item_5 = 0
    $ a_item_6 = 0
    $ a_item_7 = 0
    $ a_item_8 = 0
    $ a_item_9 = 0
    $ a_menu_0 = 0
    $ a_menu_1 = 0
    $ a_menu_2 = 0
    $ a_menu_3 = 0
    $ a_menu_4 = 0
    $ a_menu_5 = 0
    $ a_menu_6 = 0
    $ a_menu_7 = 0
    $ a_menu_8 = 0
    $ a_menu_9 = 0
    $ a_menu_10 = 0
    $ a_menu_11 = 0
    $ a_ani_0 = 0
    $ a_ani_1 = 0
    $ a_ani_2 = 0
    $ a_ani_3 = 0
    $ a_ani_4 = 0
    $ a_ani_5 = 0
    $ a_ani_6 = 0
    $ a_ani_7 = 0
    $ a_ani_8 = 0
    $ a_ani_9 = 0
    $ minigamestep = 0
    $ minigamemax = 0

    call gamecheck_textcps from _call_gamecheck_textcps

    show screen UI_chat
    return

# ----------------------------------------------------------------------------------------------------
# Fix android loading incompatibility
# ----------------------------------------------------------------------------------------------------
#if persistent.last_version is None or persistent.last_version != config.version:
    #python:
        #persistent.last_version = config.version
        #for savegame in renpy.list_saved_games(fast=True):
            #renpy.unlink_save(savegame)

# ----------------------------------------------------------------------------------------------------
label autocomplete1:
# ----------------------------------------------------------------------------------------------------
    if gametimeweek == "Friday":
        $ gametimehour += 24
        call gametime from _call_gametime_79

    if gametimeweek == "Saturday":
        $ gametimehour += 24
        call gametime from _call_gametime_80

    #$ hero_quest_3 = 1

    jump passday

# ----------------------------------------------------------------------------------------------------
# Checkpoint Screen
# ----------------------------------------------------------------------------------------------------
image LoadCorrupt:
    choice:
        Movie(play="gui/LoadCorrupt_1.webm", loop=True, start_image="gui/LoadCorrupt.webp", image="gui/LoadCorrupt.webp")
    choice:
        Movie(play="gui/LoadCorrupt_2.webm", loop=True, start_image="gui/LoadCorrupt.webp", image="gui/LoadCorrupt.webp")
    choice:
        Movie(play="gui/LoadCorrupt_3.webm", loop=True, start_image="gui/LoadCorrupt.webp", image="gui/LoadCorrupt.webp")
    choice:
        Movie(play="gui/LoadCorrupt_4.webm", loop=True, start_image="gui/LoadCorrupt.webp", image="gui/LoadCorrupt.webp")
    choice:
        Movie(play="gui/LoadCorrupt_5.webm", loop=True, start_image="gui/LoadCorrupt.webp", image="gui/LoadCorrupt.webp")
    choice:
        Movie(play="gui/LoadCorrupt_6.webm", loop=True, start_image="gui/LoadCorrupt.webp", image="gui/LoadCorrupt.webp")
    choice:
        Movie(play="gui/LoadCorrupt_7.webm", loop=True, start_image="gui/LoadCorrupt.webp", image="gui/LoadCorrupt.webp")
    3
    repeat


screen LoadingCheckpoint():
    on "show" action Hide("quick_menu")

    frame:
        background "LoadCorrupt" xysize(1920,1080)

        frame:
            background "#00000064"
            xsize 700
            ysize 980
            xpadding 25
            ypadding 25
            xalign 0.0
            yalign 0.5
            xpos 25

            vbox:
                spacing 50 xalign 0.5 yalign 0.5 xsize 600

                label renpy.translate_string("{size=60}Attention, hero!{/size}") xalign 0.5

                text renpy.translate_string("This place is no longer safe! In the moment, the multiverses are corrupted, causing various conflicts and incompatibilities between saves, therefore you must get isekaied through [C_Dat]New Game[C_Off]. But don't worry, you now have the option to choose your progress through [C_Dat]Custom[C_Off] option!") justify True size 45 xalign 0.5

                #text "It seems that this save is from a older version of the game, that may contain incompatibilities. It's suggested to continue playing from a safer checkpoint on [C_Dat]New Game[C_Off]." justify True

                textbutton renpy.translate_string("Return") action MainMenu(confirm=False) xalign 0.5

                #textbutton "Just Load" action Return() xalign 0.5

# ----------------------------------------------------------------------------------------------------
# After Load
# ----------------------------------------------------------------------------------------------------
label after_load:

    if not hasattr(store, 'afterload_0_37'):
        $ msg.clear()
        play BGM "audio/W2C - Tension.mp3"
        call screen LoadingCheckpoint

    # --------------------------------------------------
    # The live map/school data is MAP_DATA/SCHOOL_DATA (Data - Map.rpy) — `define`s under names no save has ever held, so nothing here restores or repairs them. What is left below is one-way salvage: a pre-0.40.2 save still carries the OLD `Map_Data`/`School_Data` it wrote back when they were `default`s, and the two branches that held mutable state (home room locks, club rep/money) are lifted out of it into the flat vars that own them now. Renaming is what fixed 0.40.2's `KeyError: 'facade'`: repairing the old names in place worked until the player rolled back past this label, which handed the stale dict straight back.
    # --------------------------------------------------
    python:
        _stale_map = getattr(store, "Map_Data", None) or {}
        _stale_school = getattr(store, "School_Data", None) or {}

        # Legacy room locks: pull them out of the stale saved dict (MAP_DATA has none; flat map_lock_* vars are the live state).
        for _room in ["bathroom", "bedroom_hero", "bedroom_wsis", "bedroom_wmom"]:
            _lock = _stale_map.get("home", {}).get("map", {}).get(_room, {}).get("lock", None)
            if _lock is not None:
                setattr(store, "map_lock_" + _room, _lock)

        # Club state now lives in flat vars (Data - Club.rpy + script.rpy). Migrate any legacy School_Data["club"] rep/money from a pre-replan save into those flats. Idempotent because the stale dict is dropped below, so a re-save has nothing left to read.
        _old_clubs = _stale_school.get("club", {})

        # The stale copies are dead weight in every future save once drained, and leaving them invites code reaching for the old name. Char_Data has nothing to drain — the database it holds in a <=0.33.1 save is the dead stat dict, and the live one is CHAR_DATA (Data - Char.rpy) — it is dropped for the same reason.
        for _dead in ("Map_Data", "School_Data", "Char_Data"):
            if hasattr(store, _dead):
                delattr(store, _dead)

        _club_id_map = {"coun": "stco", "perf": "perf", "musi": "musi", "life": "life", "spor": "spor", "arts": "arts"}
        for _old_id, _club in _old_clubs.items():
            _new_id = _club_id_map.get(_old_id)
            if _new_id is None:
                continue
            for _char, _rep in _club.get("rep", {}).items():
                setattr(store, "club_" + _new_id + "_" + _char + "_rep", _rep)
            if "money" in _club:
                setattr(store, "club_" + _new_id + "_money", _club["money"])

        # Old single flat SC rep folds into HERO's SC rep, then stops existing.
        if hasattr(store, "club_stco_rep"):
            store.club_stco_hero_rep = store.club_stco_hero_rep + store.club_stco_rep
            del store.club_stco_rep

        # Renamed item ids (ITEM_ID_RENAMES, Item - System.rpy): ids are saved, so a rename leaves the OLD id sitting in old saves and the unguarded item_data[<id>] lookups then raise KeyError on the shop/inventory screens. Rewrite every saved container in place; adding a future rename is one line in that table, nothing here changes.
        if ITEM_ID_RENAMES:
            _id_lists = [store.inventory, store.inventory_fridge, store.inventory_home_table,
                         store.item_cart, store.item_sale]
            for _cid in CHAR_IDS:
                _inv = getattr(store, _cid + "_item", None)
                if isinstance(_inv, list):
                    _id_lists.append(_inv)
            for _id_list in _id_lists:
                for _i, _old_id in enumerate(_id_list):
                    _new_id = ITEM_ID_RENAMES.get(_old_id)
                    if _new_id is not None:
                        _id_list[_i] = _new_id

# --------------------------------------------------
# TEMPORARY ANTIBUG (Need to Force Recompile)
# --------------------------------------------------

    # --------------------------------------------------
    # Anti-bug for outdated files
    # --------------------------------------------------
    #$ renpy.block_rollback()

    # --------------------------------------------------
    # Short notification timer
    # --------------------------------------------------
    #$ persistent.notice1 = 0.01  # FadeIn
    #$ persistent.notice2 = 0.1  # Duration
    #$ persistent.notice3 = 0.01  # FadeOut

    # --------------------------------------------------
    # Update Character Per Second
    # --------------------------------------------------
    call gamecheck_textcps from _call_gamecheck_textcps_1
    $ check_stat()

    # --------------------------------------------------
    # Fix Missing Gallery Image
    # --------------------------------------------------
    if "SHOT_WatchingTV" in cellbg and "SHOT_WatchingTV_HERO" not in cellbg:
        $ msg.msg(renpy.translate_string("[C_Pos]Updated data for phone gallery image[C_Off]"))
        $ cellbg.remove("SHOT_WatchingTV")
        $ cellbg.insert(1, "SHOT_WatchingTV_HERO")
        $ cellbg.insert(1, "SHOT_WatchingTV_WSIS")

    # --------------------------------------------------
    # Replace Gift Name
    # --------------------------------------------------
    python:
        # Check if old item exists in wsis_item inventory        
        if [item for item in wsis_item if hasattr(item, 'item_id') and item.item_id == "Plushy_GalmonBunny"]:
            for buceta in xereca:
                wsis_item.remove(buceta)
            
            # Add new item using proper function
            AddItem_Inventory("Coll_Plushy_BunnyPink", 1, None, wsis_item)
            msg.msg(renpy.translate_string("[C_Pos]Updated data for [C_Off][C_Nam][fnamewsis][C_Off][C_Pos]'s inventory[C_Off]"))

    # --------------------------------------------------
    # Student Council database fixed
    # --------------------------------------------------
    if hasattr(store, 'council_blacklist'):
        $ msg.msg(renpy.translate_string("[C_Pos]Updated data for Student Council database[C_Off]"))
        $ club_stco_blacklist = [council_blacklist]
        if "hriv" in club_stco_blacklist:
            $ add_stat("hero", "club_stco", 5)

    # --------------------------------------------------
    # WSIS mechanics
    # --------------------------------------------------
    if wsis_to_hero == [0, "Lil bro", "younger brother"] :
        $ wsis_to_hero = "Lil Bro"
    else:
        $ wsis_to_hero = "Big Bro"
    # --------------------------------------------------
    # Remove hriv_prey
    # --------------------------------------------------
    if hasattr(store, 'hriv_prey'):
        if hriv_prey[3] != 40:
            $ msg.msg(renpy.translate_string("[C_Pos]Updated data for affection between characters[C_Off]"))
            $ wdis_hriv = hriv_prey[3]
            $ hriv_prey[3] = 0
    # --------------------------------------------------
    if perk_skl_dnc == 1:
        $ perk_skl_dnc = 0
        $ perk += 1
        $ msg.msg(renpy.translate_string("[C_Dat]Dance skill[C_Off] was removed and 1 perk was added back"))

    # --------------------------------------------------
    # Convert old string-based items to new Item objects
    # --------------------------------------------------
    call check_itemname from _call_check_itemname

    # --------------------------------------------------
    # Add default items if missing
    # --------------------------------------------------
    if (not any(buceta.item_id == "Unique_Key_Home" for buceta in inventory)):
        $ AddItem_Inventory("Unique_Key_Home", 1, None, inventory)
    
    if (not any(buceta.item_id == "Tool_Cook_Pan" for buceta in inventory_fridge)):
        $ AddItem_Inventory("Tool_Cook_Pan", 1, None, inventory_fridge)
    
    if (not any(buceta.item_id == "Tool_Cook_PanFry" for buceta in inventory_fridge)):
        $ AddItem_Inventory("Tool_Cook_PanFry", 1, None, inventory_fridge)
    
    if (not any(buceta.item_id == "Ingredient_Cook_Oil" for buceta in inventory_fridge)):
        $ AddItem_Inventory("Ingredient_Cook_Oil", 1, None, inventory_fridge)
    
    if (not any(buceta.item_id == "Ingredient_Cook_Salt" for buceta in inventory_fridge)):
        $ AddItem_Inventory("Ingredient_Cook_Salt", 1, None, inventory_fridge)
    
    if (not any(buceta.item_id == "Ingredient_Cook_Butter" for buceta in inventory_fridge)):
        $ AddItem_Inventory("Ingredient_Cook_Butter", 1, None, inventory_fridge)
    
    if (not any(buceta.item_id == "Tool_Cook_Knife" for buceta in inventory_fridge)):
        $ AddItem_Inventory("Tool_Cook_Knife", 1, None, inventory_fridge)

    # --------------------------------------------------
    # Short notification timer
    # --------------------------------------------------
    $ msg.msg(renpy.translate_string("[C_Pos]Game loaded successfully[C_Off]"))
    pause
    $ msg.clear()
    # --------------------------------------------------
    # Short notification timer
    # --------------------------------------------------

    $ persistent.notice1 = 0.5  # FadeIn
    $ persistent.notice2 = 5.5  # Duration
    $ persistent.notice3 = 0.5  # FadeOut

    # --------------------------------------------------
    # Reset Generic Vars
    # --------------------------------------------------
    $ a_check_0 = 0
    $ a_check_1 = 0
    $ a_check_2 = 0
    $ a_check_3 = 0
    $ a_check_4 = 0
    $ a_check_5 = 0
    $ a_check_6 = 0
    $ a_check_7 = 0
    $ a_check_8 = 0
    $ a_check_9 = 0

    # --------------------------------------------------
    return

# --------------------------------------------------
label check_itemname:
# --------------------------------------------------
    python:
        # List of all inventory variable names
        a_check_0 = [
            'inventory', 'inventory_fridge', 'item_cart',
            'wmom_item', 'wsis_item', 'wnei_item', 'wpre_item',
            'wota_item', 'wdis_item', 'wgal_item', 'wric_item',
            'wgot_item', 'wdel_item', 'wuza_item', 'wlaz_item'
        ]
        
        # Migrate each inventory
        for xereca in a_check_0:
            # Get the actual variable by name
            a_check_1 = getattr(store, xereca)
            
            # Prepare migrated list
            a_check_2 = []
            for buceta in a_check_1:
                if hasattr(buceta, 'item_id'):
                    # It's already an Item object - check if ID needs updating
                    if buceta.item_id in item_id_migrations:
                        buceta.item_id = item_id_migrations[buceta.item_id]
                        buceta.data = item_data[buceta.item_id]
                    
                    # Fix dummy items: if item now exists in item_data, update it
                    if buceta.item_id in item_data:
                        if buceta.data.get("name") == "Unknown Item":
                            buceta.data = item_data[buceta.item_id]
                    
                    a_check_2.append(buceta)
                elif isinstance(buceta, str):
                    # Convert old ID to new ID if needed
                    if buceta in item_id_migrations:
                        buceta = item_id_migrations[buceta]
                    
                    # Convert string to Item object
                    if buceta in item_data:
                        a_check_2.append(Item(buceta, quality=None))
            
            # Actually update the store variable
            setattr(store, xereca, a_check_2)
    return

# ----------------------------------------------------------------------------------------------------
# Check Text Character Per Second
# ----------------------------------------------------------------------------------------------------
label gamecheck_textcps:
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
    else:
        $ preferences.text_cps = 0
    return

# ----------------------------------------------------------------------------------------------------
# Check Player Current Map
# ----------------------------------------------------------------------------------------------------
label check_playermap:
    if hero_map == None:
        $ Get_MapName("hero")

    if hero_map == MAP_DATA["city"]["name"]:
        call goto_map from _call_goto_map
        scene bg_map at Zoom_X(0.5)
        show screen nav_map

    # At home HERO wears whatever the laundry left him: the home outfit when it is clean and in the wardrobe, his underwear or a towel while it is in the wash (the same Wear_Available ladder the girls follow), and he changes back the moment it returns.
    if Check_CharInMap("hero", "home") and hero_wear != Wear_Available("hero", "home"):
        scene bg_0
        with dissolve
        if hero_wear != None and Wear_Available("hero", "home") == "home":
            $ msg.msg(renpy.translate_string("You dressed your home outfit."))
        elif hero_wear != None and task_loc_hero_home != "wardrobe":
            $ msg.msg(renpy.translate_string("Your home clothes are in the wash, so you make do with what is left."))
        elif hero_wear != None:
            $ msg.msg(renpy.translate_string("Your home clothes are too filthy to wear, so you make do with what is left."))
        $ hero_wear = Wear_Available("hero", "home")

    # Once a day each housemate who shares the room reacts to HERO in his underwear or a towel: someone close enjoys the view (intimacy, a little lust), anyone else glares (WSIS rage, WMOM love).
    if Check_CharInMap("hero", "home") and hero_wear in ("under", "towel"):
        python:
            for _res in ["wmom", "wsis"]:
                if Check_CharSameMap("hero", _res) and getattr(store, _res + "_under_day") != gametimeday:
                    setattr(store, _res + "_under_day", gametimeday)
                    _res_name = C_Nam + getattr(store, "fname" + _res) + C_Off
                    _res_look = "in your underwear" if hero_wear == "under" else "in nothing but a towel"
                    if intimacy_tier(_res) >= 2:
                        msg.msg(_res_name + renpy.translate_string(" eyes you up ") + _res_look + renpy.translate_string(" and doesn't look away"))
                        add_stat(_res, "inti", 2)
                        add_stat(_res, "lust", 2)
                    elif _res == "wsis":
                        msg.msg(_res_name + renpy.translate_string(" glares at you wandering around ") + _res_look)
                        add_stat(_res, "rage", 3)
                    else:
                        msg.msg(_res_name + renpy.translate_string(" scolds you for wandering around ") + _res_look)
                        add_stat(_res, "love", -1)

    if hero_map == MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["facade"]["name"]:
        call goto_home_facade from _call_goto_home_facade_1
        scene bg_home facade
        show screen nav_home_facade

    elif hero_map == MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["living_room"]["name"]:
        call goto_home_livingroom from _call_goto_home_livingroom_2
        scene bg_home livingroom
        show screen nav_home_livingroom

    elif hero_map == MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["hallway"]["name"]:
        call goto_home_hallway from _call_goto_home_hallway_1
        scene bg_home hallway
        show screen nav_home_hallway

    elif hero_map == MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bedroom_hero"]["name"]:
        call goto_home_bedroom_hero from _call_goto_home_bedroom_hero_1
        scene bg_home bedroom hero
        show screen nav_home_bedroom_hero

    elif hero_map == MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bedroom_wsis"]["name"]:
        call goto_home_bedroom_wsis from _call_goto_home_bedroom_wsis
        scene bg_home bedroom wsis
        show screen nav_home_bedroom_wsis
        #with fade

    elif hero_map == MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bedroom_wmom"]["name"]:
        call goto_home_bedroom_wmom from _call_goto_home_bedroom_wmom
        scene bg_home bedroom wmom
        show screen nav_home_bedroom_wmom

    elif hero_map == MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bathroom"]["name"]:
        call goto_home_bathroom from _call_goto_home_bathroom
        scene bg_home bathroom
        show screen nav_home_bathroom

    elif hero_map == MAP_DATA["office"]["name"] + " - " + MAP_DATA["office"]["map"]["facade"]["name"]:
        call goto_office_facade from _call_goto_office_facade_1
        scene bg_office facade
        show screen nav_office_facade

    elif hero_map == MAP_DATA["office"]["name"] + " - " + MAP_DATA["office"]["map"]["office_wcou"]["name"]:
        call goto_office_room from _call_goto_office_room
        scene bg_office_room
        show screen nav_office_room

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["facade"]["name"]:
        call goto_school_facade from _call_goto_school_facade_1
        scene bg_school facade
        show screen nav_school_facade

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["courtyard"]["name"]:
        call goto_school_courtyard from _call_goto_school_courtyard
        if not hero_wear == "school":
            scene bg_0
            with dissolve
            $ hero_wear = "school"
            $ msg.msg(renpy.translate_string("You dressed your school uniform."))
            #$ msg.msg("You're at" + str(Get_MapName("hero")))
            pause(1)
        scene bg_school courtyard
        show screen nav_school_courtyard

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["frontyard"]["name"]:
        call goto_school_frontyard from _call_goto_school_frontyard
        scene bg_school frontyard
        show screen nav_school_frontyard

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["locker_m"]["name"]:
        call goto_school_locker_m from _call_goto_school_locker_m
        scene bg_school locker_m
        show screen nav_school_locker_m

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["locker_f"]["name"]:
        call goto_school_locker_f from _call_goto_school_locker_f
        scene bg_school locker_f
        show screen nav_school_locker_f

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["hallway_1"]["name"]:
        call goto_school_hallway1 from _call_goto_school_hallway1
        scene bg_school hallway1
        show screen nav_school_hallway1

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["hallway_2"]["name"]:
        call goto_school_hallway2 from _call_goto_school_hallway2
        scene bg_school hallway2
        show screen nav_school_hallway2

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["class_1a"]["name"]:
        call goto_school_classroom_1a from _call_goto_school_classroom_1a
        scene bg_school classroom_1a
        show screen nav_school_classroom_1a

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["class_1b"]["name"]:
        call goto_school_classroom_1b from _call_goto_school_classroom_1b_1
        scene bg_school classroom_1b
        show screen nav_school_classroom_1b

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["class_3a"]["name"]:
        call goto_school_classroom_3a from _call_goto_school_classroom_3a
        scene bg_school classroom_3a
        show screen nav_school_classroom_3a

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["library"]["name"]:
        call goto_school_library from _call_goto_school_library
        scene bg_school library
        show screen nav_school_library

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["swimming_pool"]["name"]:
        call goto_school_pool from _call_goto_school_pool_3
        if not hero_wear == "school_swim":
            scene bg_0
            with dissolve
            $ hero_wear = "school_swim"
            $ msg.msg(renpy.translate_string("You dressed your swimsuit uniform."))
            pause(1)
        scene bg_school pool
        show screen nav_school_pool

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["sports_court"]["name"]:
        call goto_school_sportcourt from _call_goto_school_sportcourt_2
        if not hero_wear == "school_sport":
            scene bg_0
            with dissolve
            $ hero_wear = "school_sport"
            $ msg.msg(renpy.translate_string("You dressed your gym uniform."))
            pause(1)
        scene bg_school sportcourt
        show screen nav_school_sportcourt

    elif hero_map == MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["club_coun"]["name"]:
        call goto_school_club_council from _call_goto_school_club_council
        scene bg_school club_council
        show screen nav_school_club_council

    elif (Check_CharInMap("hero", "shopping", "facade")):
        call goto_shopping_facade from _call_goto_shopping_facade
        scene bg_shopping_facade
        show screen nav_shopping_facade

    elif (Check_CharInMap("hero", "shopping", "hall")):
        call goto_shopping_hall from _call_goto_shopping_hall
        scene bg_shopping_hall
        show screen nav_shopping_hall

    elif (Check_CharInMap("hero", "shopping", "store_clothing")):
        call goto_shopping_store_clothing from _call_goto_shopping_store_clothing
        scene bg_shopping_store_clothing
        show screen nav_shopping_store_clothing

    elif (Check_CharInMap("hero", "shopping", "store_arcade")):
        call goto_shopping_store_arcade from _call_goto_shopping_store_arcade
        scene bg_shopping_store_arcade
        show screen nav_shopping_store_arcade

    elif (Check_CharInMap("hero", "shopping", "court_food")):
        call goto_shopping_court_food from _call_goto_shopping_court_food
        scene bg_shopping_court_food
        show screen nav_shopping_court_food

    elif (Check_CharInMap("hero", "shopping", "cinema_entrance")):
        call goto_shopping_cinema_entrance from _call_goto_shopping_cinema_entrance
        scene bg_shopping_cinema_entrance
        show screen nav_shopping_cinema_entrance

    # ----------------------------------------------------------------------------------------------------
    # Check if there's an available scene on the current map
    # ----------------------------------------------------------------------------------------------------
    call check_availablescene from _call_check_availablescene

    # --------------------------------------------------
    # Default notification timer
    # --------------------------------------------------
    $ persistent.notice1 = 0.5  # FadeIn
    $ persistent.notice2 = 5.5  # Duration
    $ persistent.notice3 = 0.5  # FadeOut

    return

# ----------------------------------------------------------------------------------------------------
# Check Personality
# ----------------------------------------------------------------------------------------------------
label personality:

    if personality[1] < 70 and personality[2] < 70 and personality[3] < 70 and personality[4] < 70:
        $ personality[0] = "Common"

    elif personality[1] > personality[2] and personality[1] > personality[3] and personality[1] > personality[4]:
        $ personality[0] = "Hentai"

    elif personality[2] > personality[1] and personality[2] > personality[3] and personality[2] > personality[4]:
        $ personality[0] = "Kind"

    elif personality[3] > personality[1] and personality[3] > personality[2] and personality[3] > personality[4]:
        $ personality[0] = "Reserved"

    elif personality[4] > personality[1] and personality[4] > personality[2] and personality[4] > personality[3]:
        $ personality[0] = "Intimate"

    if renpy.get_screen("charactercreator1a"):
        if minigamestep < 30:
            $ personality[0] = "Reserved"
        elif minigamestep > 70:
            $ personality[0] = "Intimate"
        else:
            $ personality[0] = "Common"

        call screen charactercreator1a
        return
    else:
        return

# ----------------------------------------------------------------------------------------------------
# Add CHA
# ----------------------------------------------------------------------------------------------------
label stat_addCHA:
    $ check_stat()

    if statget_cha > 0:
        $ add_stat("hero", "cha_soc", 0.2 + ((statget_cha * statadd_cha)/10), stat_mod=False)
    elif statget_cha < 0:
        $ add_stat("hero", "cha_soc", -(0.2 + ((statget_cha * statadd_cha)/10)), stat_mod=False)

    return

init python:

    # Hero sub-stats (0-100 floats, 2 decimal places). Base stats stat_cha/stat_int/stat_phy are computed averages of these and are maintained by add_stat — never write them directly.
    HERO_SUB_STATS = {
        "cha_sex", "cha_per", "cha_soc",
        "phy_str", "phy_agi", "phy_res",
        "int_per", "int_mem", "int_log",
        "skl_dnc", "skl_gui", "skl_swm", "skl_msg", "skl_cok", "skl_tut",
    }

    # Date score axes and the affinity each one is really made of: spice is lust, romance and fun are love.
    DATE_AXIS_STAT = {"date_rom": "love", "date_fun": "love", "date_spi": "lust"}

    # The bonus call that goes with each axis: "date_fun_bonus" banks percent onto the axis "date_fun".
    DATE_AXIS_BONUS = {axis + "_bonus": axis for axis in DATE_AXIS_STAT}

    # The late-game fade, held OUT of Stat_Modifiers so a gain can be paid with it (base stats, which get
    # harder as the relationship matures) or without it (date score, which must not flatten with them).
    # Same two curves for everyone, so only WHO fades on WHICH stat is data: "sq" fades on the stat's own
    # square, "li" on a gentler line. The `rem` side keeps its fades inline — nothing reads those but a loss.
    STAT_FADE = {
        ("love", "sq") : ("wsis", "wmom", "wnei", "wdan", "wpre", "wric", "wgal", "wota", "wdis", "wgot", "wdel", "wuza", "wlaz"),
        ("lust", "sq") : ("wcou", "wsuk"),
        ("inti", "li") : ("wsis", "wmom", "wnei", "wdan", "wpre", "wric", "wgal", "wota", "wdis", "wgot", "wdel", "wuza", "wlaz", "wsuk", "hprv", "hine", "hriv"),
    }

    def add_stat(char_id=None, stat_id=None, stat_value=None, stat_mod=True):
        """
        Add or remove stat value for a character using flat store variables.

        Args:
            char_id: Character identifier (e.g., "hero", "wmom", "wsis")
            stat_id: Stat identifier (e.g., "inti", "love", "cha_soc", "int_log", "bonus_cha", "club_stco")
            stat_value: Amount to add (positive) or remove (negative)
            stat_mod: Apply stat modifiers from check_stat() (True) or use raw value (False)
        """
        # Validate inputs
        if char_id is None or stat_id is None or stat_value is None:
            return

        # Legacy redirect: hero "cha"/"phy"/"int" gains land on the default sub-stat.
        # Existing call sites like add_stat("hero", "cha_soc", N) keep working without edits.
        if char_id == "hero" and stat_id in ("cha", "phy", "int"):
            stat_id = {"cha": "cha_soc", "phy": "phy_str", "int": "int_log"}[stat_id]

        # A "date_<axis>_bonus" call banks percent on that axis for the rest of the date instead of paying
        # points: every later gain on that axis is worth that much more (or less, when negative). It is the
        # date's own state, so off the date it does nothing, and it floors at -100% so a gain never inverts.
        if stat_id in DATE_AXIS_BONUS:
            if not (date_active and char_id == date_char):
                return

            bonus_was = getattr(store, stat_id)
            setattr(store, stat_id, round(max(-100.0, bonus_was + stat_value), 2))
            bonus_moved = getattr(store, stat_id) - bonus_was

            if bonus_moved:
                bonus_name = date_score_ui[DATE_AXIS_BONUS[stat_id][5:]][0].lower()
                bonus_char = getattr(store, f"fname{char_id}", None) or char_id
                if bonus_moved > 0:
                    msg.msg(renpy.translate_string("[C_Nam]") + bonus_char + renpy.translate_string("[C_Off] [C_Per]") + bonus_name + renpy.translate_string(" bonus[C_Off]: [C_Pos]+") + renpy.translate_string(str(str(round(bonus_moved, 2)))) + renpy.translate_string("%[C_Off]"))
                else:
                    msg.msg(renpy.translate_string("[C_Nam]") + bonus_char + renpy.translate_string("[C_Off] [C_Per]") + bonus_name + renpy.translate_string(" bonus[C_Off]: [C_Neg]") + renpy.translate_string(str(str(round(bonus_moved, 2)))) + renpy.translate_string("%[C_Off]"))
            return

        # Date axes earn on the date's OWN scale: a flat base per raw point, multiplied by how far that
        # affinity has already come. date_scale is what ONE point of love/lust is worth, so at 100 the beat
        # pays (1 + 100 * date_scale) times its base — no Stat_Modifiers, no fade, nothing that throttles the
        # affinity itself. An axis call feeds only the meter (the date settles the affinity at its end); a
        # plain love/lust gain pays its stat AND spills onto the axes it belongs to, love halved because its
        # result is split over the two it feeds.
        if date_active and char_id == date_char and (stat_id in DATE_AXIS_STAT or stat_id in ("love", "lust")):
            axis_src = DATE_AXIS_STAT.get(stat_id, stat_id)

            if stat_id in DATE_AXIS_STAT:
                axis_list, axis_split = (stat_id,), 1.0
            elif stat_id == "lust":
                axis_list, axis_split = ("date_spi",), 1.0
            else:
                axis_list, axis_split = ("date_rom", "date_fun"), 2.0

            axis_aff = get_cvar(char_id, "stat", axis_src, default=0)
            axis_gain = (stat_value * date_base * (1.0 + (axis_aff * date_scale))) / axis_split

            # `axis_moved` is what the meter ACTUALLY took after the 0-100 clamp, which is what gets reported: a full bar has to say nothing, not announce the gain it threw away.
            axis_moved = 0.0
            for axis in axis_list:
                # The axis bonus scales what the axis EARNS, so it is read per axis (love feeds two of them) and only ever applied to a gain — a "+25% fun" bonus must not deepen a fun loss.
                axis_bonus = getattr(store, axis + "_bonus", 0)
                axis_pay = axis_gain * (1.0 + (axis_bonus / 100.0)) if axis_gain > 0 else axis_gain

                axis_was = getattr(store, axis)
                setattr(store, axis, round(max(0.0, min(100.0, axis_was + axis_pay)), 2))
                if abs(getattr(store, axis) - axis_was) > abs(axis_moved):
                    axis_moved = getattr(store, axis) - axis_was

            if stat_id in DATE_AXIS_STAT:
                # An axis call is the meter's own gain: it never touches the affinity, so it reports itself and stops here.
                if axis_moved:
                    axis_name = date_score_ui[stat_id[5:]][0].lower()
                    axis_char = getattr(store, f"fname{char_id}", None) or char_id
                    if axis_moved > 0:
                        msg.msg(renpy.translate_string("[C_Nam]") + axis_char + renpy.translate_string("[C_Off] [C_Per]") + axis_name + renpy.translate_string("[C_Off]: [C_Pos]+") + renpy.translate_string(str(str(round(axis_moved, 2)))) + renpy.translate_string("%[C_Off]"))
                    else:
                        msg.msg(renpy.translate_string("[C_Nam]") + axis_char + renpy.translate_string("[C_Off] [C_Per]") + axis_name + renpy.translate_string("[C_Off]: [C_Neg]") + renpy.translate_string(str(str(round(axis_moved, 2)))) + renpy.translate_string("%[C_Off]"))
                return

        # No date running (or not with her): an axis call simply pays the affinity it is made of.
        if stat_id in DATE_AXIS_STAT:
            stat_id = DATE_AXIS_STAT[stat_id]

        # Check if this is a club reputation stat
        if stat_id.startswith("club_"):
            club_id = stat_id.replace("club_", "")  # Extract club id (e.g., "stco" from "club_stco")

            # Check if club exists
            if club_id not in Club_Data:
                return

            # Reputation is a flat var (club_<club>_<char>_rep); Get_ClubRep defaults missing to 0.
            current_value = Get_ClubRep(club_id, char_id)

            # Calculate final value (clubs might have their own modifiers keyed by the club_<id> stat)
            if stat_mod and stat_id in Stat_Modifiers:
                if stat_value > 0:
                    modifier = Stat_Modifiers.get(stat_id, {}).get("add", {}).get("rep", 1.0)
                    final_value = round(stat_value * modifier, 2)
                elif stat_value < 0:
                    modifier = Stat_Modifiers.get(stat_id, {}).get("rem", {}).get("rep", 1.0)
                    final_value = round(stat_value * modifier, 2)
                else:
                    final_value = 0
            else:
                final_value = stat_value

            # Per-call step cap (same as the regular stat path): cap rep change at ±STAT_STEP_CAP.
            final_value = max(-STAT_STEP_CAP, min(STAT_STEP_CAP, final_value))

            # Set the new value (setattr on a store var is save/rollback-safe once written)
            setattr(store, "club_" + club_id + "_" + char_id + "_rep", current_value + final_value)

            # Display message
            if final_value != 0:
                char_name = getattr(store, f"fname{char_id}", None) or char_id

                if char_id == "hero":
                    char_name = "Your"

                club_name = Club_Data[club_id]["name"]
                stat_display = f"[C_Per]reputation[C_Off] with [C_Dat]{club_name}[C_Off]"

                if final_value > 0:
                    msg.msg(renpy.translate_string("[C_Nam]") + char_name + renpy.translate_string("[C_Off] ") + stat_display + renpy.translate_string(": [C_Pos]+") + renpy.translate_string(str(str(final_value))) + renpy.translate_string("[C_Off]"))
                else:
                    msg.msg(renpy.translate_string("[C_Nam]") + char_name + renpy.translate_string("[C_Off] ") + stat_display + renpy.translate_string(": [C_Neg]") + renpy.translate_string(str(str(final_value))) + renpy.translate_string("[C_Off]"))

            return

        # Check if character exists
        if char_id not in CHAR_IDS:
            return

        # Perks are now plain integers (0-3) set only by the Skill UI's SetVariable actions — they are no longer mutable via add_stat. Sub-stat ids (e.g. "cha_sex", "phy_str", "int_per", "skl_dnc") fall through to the regular sub-stat write path below.

        # Check if this is a bonus stat
        is_bonus = False
        actual_stat = stat_id
        if stat_id in ["bonus_cha", "bonus_int", "bonus_phy"]:
            is_bonus = True
            actual_stat = stat_id.replace("bonus_", "")  # Extract the actual stat name (cha, int, phy)
            store_key = _cvar_key(char_id, "bonus", actual_stat)
        else:
            store_key = _cvar_key(char_id, "stat", stat_id)

        if not hasattr(store, store_key):
            return

        current_value = getattr(store, store_key)

        # Calculate final value
        if stat_mod:
            # Apply modifiers from Stat_Modifiers dictionary
            if stat_value > 0:
                # The fade multiplies in HERE, not in the table, so the date score can read the modifier without it.
                modifier = Stat_Modifiers.get(char_id, {}).get("add", {}).get(stat_id, 1.0) * Stat_Fades.get(char_id, {}).get(stat_id, 1.0)
                final_value = round(stat_value * modifier, 2)
            elif stat_value < 0:
                modifier = Stat_Modifiers.get(char_id, {}).get("rem", {}).get(stat_id, 1.0)
                final_value = round(stat_value * modifier, 2)
            else:
                final_value = 0
        else:
            # Use raw value without modifiers
            final_value = stat_value

        # Per-call step cap: never let one add_stat move a stat by more than ±STAT_STEP_CAP, so a large base value or modifier (e.g. the boosted lust gain) can't spike it at once.
        final_value = max(-STAT_STEP_CAP, min(STAT_STEP_CAP, final_value))

        # Set the new value (clamp hero sub-stats to 0..100, 2 decimals)
        new_value = current_value + final_value
        if char_id == "hero" and stat_id in HERO_SUB_STATS:
            new_value = round(max(0, min(100, new_value)), 2)
        setattr(store, store_key, new_value)

        # Aggregate base stats from sub-stats (hero only).
        # stat_cha / stat_phy / stat_int are computed averages, never written directly.
        if char_id == "hero" and stat_id in HERO_SUB_STATS:
            if stat_id.startswith("cha_"):
                store.stat_cha = round((store.stat_cha_sex + store.stat_cha_per + store.stat_cha_soc) / 3.0, 2)
            elif stat_id.startswith("phy_"):
                store.stat_phy = round((store.stat_phy_str + store.stat_phy_agi + store.stat_phy_res) / 3.0, 2)
            elif stat_id.startswith("int_"):
                store.stat_int = round((store.stat_int_per + store.stat_int_mem + store.stat_int_log) / 3.0, 2)

        # Display message
        if final_value != 0:
            char_name = getattr(store, f"fname{char_id}", None) or char_id

            if char_id == "hero":
                char_name = "Your"

            # Translate stat_id to display name
            stat_display = stat_id
            if stat_id == "inti":
                stat_display = "intimacy"
            elif stat_id == "cha_sex":
                stat_display = "sensuality"
            elif stat_id == "cha_per":
                stat_display = "performance"
            elif stat_id == "cha_soc":
                stat_display = "charisma"
            elif stat_id == "phy_str":
                stat_display = "strength"
            elif stat_id == "phy_agi":
                stat_display = "agility"
            elif stat_id == "phy_res":
                stat_display = "resistance"
            elif stat_id == "int_per":
                stat_display = "perception"
            elif stat_id == "int_mem":
                stat_display = "memory"
            elif stat_id == "int_log":
                stat_display = "intelligence"
            elif stat_id == "ene":
                stat_display = "energy"
            elif stat_id == "hyg":
                stat_display = "hygiene"
            elif stat_id == "bonus":
                stat_display = "bonus[C_Off][C_Whi] for next interactions"

            if stat_id.startswith("bonus"):
                if stat_id == "bonus_cha":
                    stat_display = "bonus[C_Off][C_Whi] for next charisma gaining"
                elif stat_id == "bonus_int":
                    stat_display = "bonus[C_Off][C_Whi] for next intelligence gaining"
                elif stat_id == "bonus_phy":
                    stat_display = "bonus[C_Off][C_Whi] for next physics gaining"
                else:
                    stat_display = "bonus[C_Off][C_Whi] for next interactions"
                if final_value > 0:
                    msg.msg(renpy.translate_string("[C_Nam]") + char_name + renpy.translate_string("[C_Off] [C_Per]") + stat_display + renpy.translate_string("[C_Off]: [C_Pos]+") + renpy.translate_string(str(str(final_value))) + renpy.translate_string("%[C_Off]"))
                else:
                    msg.msg(renpy.translate_string("[C_Nam]") + char_name + renpy.translate_string("[C_Off] [C_Per]") + stat_display + renpy.translate_string("[C_Off]: [C_Neg]") + renpy.translate_string(str(str(final_value))) + renpy.translate_string("%[C_Off]"))
            else:
                if final_value > 0:
                    msg.msg(renpy.translate_string("[C_Nam]") + char_name + renpy.translate_string("[C_Off] [C_Per]") + stat_display + renpy.translate_string("[C_Off]: [C_Pos]+") + renpy.translate_string(str(str(final_value))) + renpy.translate_string("[C_Off]"))
                else:
                    msg.msg(renpy.translate_string("[C_Nam]") + char_name + renpy.translate_string("[C_Off] [C_Per]") + stat_display + renpy.translate_string("[C_Off]: [C_Neg]") + renpy.translate_string(str(str(final_value))) + renpy.translate_string("[C_Off]"))
        
        return

    def Stat_Product(char_id, stat_id, base, factors):
        """Records the (label, multiplier) factors behind one gain rate for the database page and returns base times their product, so the rate the game applies and the breakdown the player reads can never disagree."""
        Stat_Factors.setdefault(char_id, {})[stat_id] = (base, factors)
        for _label, factor in factors:
            base *= factor
        return base

    def check_stat():
        """
        Calculate stat modifiers for all characters based on current stats, personality, and skills.
        Stores modifiers in global Stat_Modifiers dictionary and clamps stat values.
        """
        
        # Initialize global modifiers dictionary
        global Stat_Modifiers
        Stat_Modifiers = {}

        # ...and the fade that rides alongside it (see STAT_FADE above)
        global Stat_Fades
        Stat_Fades = {}

        # ...and the labeled factors behind every add rate, refilled by Stat_Product() as the rates below are built
        global Stat_Factors
        Stat_Factors = {}

        for (fade_stat, fade_curve), fade_chars in STAT_FADE.items():
            for fade_char in fade_chars:
                fade_val = get_cvar(fade_char, "stat", fade_stat, default=0)
                Stat_Fades.setdefault(fade_char, {})[fade_stat] = 1.0 / (1 + ((fade_val * fade_val * 0.0004) if fade_curve == "sq" else (fade_val * 0.02)))
        
        # ====================================================================================================
        # HERO - Base stat modifiers
        # ====================================================================================================
        # Every "add" rate is base * Stat_Product(labeled factors), so the database page can list each factor the way the game really multiplies it.
        hero_hyg = ("Hygiene", 0.8 + ((stat_hyg * stat_hyg) / 50000))
        hero_ene = ("Energy", 0.5 + (0.005 * stat_ene))
        hero_int_rep = ("Repeated today", 1 / (1 + (1 * times_int)))
        hero_phy_rep = ("Repeated today", 1 / (1 + (1 * times_phy)))
        hero_cha_pts = ("Bonus points", 1 + (0.01 * stat_cha_bonus))
        hero_int_pts = ("Bonus points", 1 + (0.01 * stat_int_bonus))
        hero_phy_pts = ("Bonus points", 1 + (0.01 * stat_phy_bonus))

        Stat_Modifiers["hero"] = {
            "add": {
                "cha": Stat_Product("hero", "cha", 0.2, [("Current level", 1 / (1 + (0.04 * stat_cha))), hero_cha_pts, hero_hyg]),
                "int": Stat_Product("hero", "int", 1.0, [("Current level", 1 / (1 + (0.04 * stat_int))), hero_int_pts, hero_int_rep, hero_ene]),
                "phy": Stat_Product("hero", "phy", 1.0, [("Current level", 1 / (1 + (0.04 * stat_phy))), hero_phy_pts, hero_phy_rep, hero_ene]),
                "cha_soc": Stat_Product("hero", "cha_soc", 0.2, [("Current level", 1 / (1 + (0.02 * stat_cha_soc))), hero_cha_pts, hero_hyg]),
                "cha_sex": Stat_Product("hero", "cha_sex", 0.5, [("Current level", 1 / (1 + (0.02 * stat_cha_sex))), hero_cha_pts, hero_hyg]),
                "cha_per": Stat_Product("hero", "cha_per", 1.0, [("Current level", 1 / (1 + (0.02 * stat_cha_per))), hero_cha_pts, hero_hyg]),
                "int_log": Stat_Product("hero", "int_log", 1.0, [("Current level", 1 / (1 + (0.02 * stat_int_log))), hero_int_pts, hero_int_rep, hero_ene]),
                "int_per": Stat_Product("hero", "int_per", 1.0, [("Current level", 1 / (1 + (0.02 * stat_int_per))), hero_int_pts, hero_int_rep, hero_ene]),
                "int_mem": Stat_Product("hero", "int_mem", 1.0, [("Current level", 1 / (1 + (0.02 * stat_int_mem))), hero_int_pts, hero_int_rep, hero_ene]),
                "phy_str": Stat_Product("hero", "phy_str", 1.0, [("Current level", 1 / (1 + (0.02 * stat_phy_str))), hero_phy_pts, hero_phy_rep, hero_ene]),
                "phy_agi": Stat_Product("hero", "phy_agi", 1.0, [("Current level", 1 / (1 + (0.02 * stat_phy_agi))), hero_phy_pts, hero_phy_rep, hero_ene]),
                "phy_res": Stat_Product("hero", "phy_res", 1.0, [("Current level", 1 / (1 + (0.02 * stat_phy_res))), hero_phy_pts, hero_phy_rep, hero_ene]),
                "lust": Stat_Product("hero", "lust", 1.0, [("Sensuality perks", 1 / (1 + (perk_cha_sex * 0.2)))]),
            },
            "rem": {
                "cha": 0.5 * (1 + (0.04 * stat_cha)) / (0.8 + ((stat_hyg * stat_hyg)/50000)),
                "int": 1.0 * (1 + (0.04 * stat_int)),
                "phy": 1.0 * (1 + (0.04 * stat_phy)),
                "lust": 1.0,
            }
        }

        # Helper values for character calculations
        hero_cha_soc = (1 + (perk_cha_soc * 0.1))
        hero_cha_sex = (1 + (perk_cha_sex * 0.2))
        hero_combined_stats = stat_cha + stat_int + stat_phy
        # SC membership dampens HERO's affinity gains with outsiders (0 or 1); single source of truth is club_stco_mem (was the old club_stco_quest_0 join flag); math below is unchanged.
        hero_stco = int(Club_IsMember("hero", "stco"))

        # The factors most girls share, labeled once: HERO's perks, the Student Council penalty on outsiders (and its bonus for its own members).
        f_soc = ("Social perks", hero_cha_soc)
        f_sex = ("Sensuality perks", hero_cha_sex)
        f_stco = ("Student Council", 1 / (1 + (hero_stco * 0.2)))
        f_stco_in = ("Student Council", 1 + (hero_stco * 0.2))

        # ====================================================================================================
        # WSIS - Step-sister
        # ====================================================================================================
        f_wsis_pts = ("Bonus points", 1 + (0.01 * wsis_bonus))
        f_wsis_bro = ("Younger than her", 0.9 if wsis_to_hero == "Lil Bro" else 1.0)

        Stat_Modifiers["wsis"] = {
            "add": {
                "love": Stat_Product("wsis", "love", 2.5, [f_soc, f_wsis_pts, ("Kind side", 0.75 + (0.004 * personality[2])), f_stco, f_wsis_bro, ("Memories I", 0.75 + (wsis_quest_1 * 0.25)), ("Forgiveness", 0.25 + (wsis_quest_2 * 0.75)), ("Memories II", 0.5 + (wsis_quest_3 * 0.5))]),
                "lust": Stat_Product("wsis", "lust", 5.0, [f_sex, f_wsis_pts, ("Hentai side", 0.75 + (0.001 * personality[1])), f_stco, f_wsis_bro, ("Current love", 0.8 + (wsis_love * 0.004))]),
                "inti": Stat_Product("wsis", "inti", 1.0, [f_soc, f_wsis_pts, ("Intimate side", 0.75 + (0.001 * personality[4])), f_stco, f_wsis_bro, ("Current love", 0.8 + (wsis_love * 0.004)), ("Current lust", 0.95 + (wsis_lust * 0.001))]),
                "rage": Stat_Product("wsis", "rage", 7.5, [("Social perks", 1 / hero_cha_soc), ("Bonus points", 1 / max(0.01, (1 + (0.01 * wsis_bonus)))), ("Hentai side", 0.75 + (0.004 * personality[1])), ("Current intimacy", 1 / (0.5 + (wsis_inti * 0.01)))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wsis_bonus)))) * (0.75 + (0.004 * personality[1])),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wsis_bonus)))) * (0.75 + (0.001 * personality[2])) / (0.8 + (wsis_love * 0.004)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wsis_bonus)))) * (0.75 + (0.001 * personality[3])) / (0.8 + (wsis_love * 0.004)) / (0.95 + (wsis_lust * 0.001)) / (1 + (wsis_inti * 0.02)),
                "rage": ((7.5 * hero_cha_soc) * max(0.01, (1 + (0.01 * wsis_bonus)))) / (0.75 + (0.004 * personality[1])) * (0.5 + (wsis_inti * 0.01)),
            }
        }

        # ====================================================================================================
        # WMOM - Step-mother
        # ====================================================================================================
        f_wmom_pts = ("Bonus points", 1 + (0.01 * wmom_bonus))

        Stat_Modifiers["wmom"] = {
            "add": {
                "love": Stat_Product("wmom", "love", 2.5, [f_soc, f_wmom_pts, ("Kind side", 0.75 + (0.002 * personality[2])), ("Intimate side", 0.975 + (personality[4] * 0.0005))]),
                "lust": Stat_Product("wmom", "lust", 5.0, [f_sex, f_wmom_pts, ("Hentai side", 0.75 + (0.002 * personality[1])), ("Intimate side", 0.975 + (personality[4] * 0.0005))]),
                "inti": Stat_Product("wmom", "inti", 1.0, [f_soc, f_wmom_pts, ("Intimate side", (0.75 + (0.002 * personality[4])) * (0.975 + (personality[4] * 0.0005))), ("Current love", 0.8 + (wmom_love * 0.01)), ("Current lust", 0.9 + (wmom_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wmom_bonus)))) * (0.75 + (0.002 * personality[1])) * (0.975 + (personality[3] * 0.0005)),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wmom_bonus)))) * (0.75 + (0.002 * personality[2])) * (0.975 + (personality[3] * 0.0005)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wmom_bonus)))) * (0.75 + (0.002 * personality[3])) * (0.975 + (personality[3] * 0.0005)) / max(0.01, (0.8 + (wmom_love * 0.01))) / (0.9 + (wmom_lust * 0.005)) / (1 + (wmom_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WCOU - Cousin
        # ====================================================================================================
        f_wcou_pts = ("Bonus points", 1 + (0.01 * wcou_bonus))
        f_wcou_stats = ("Your attributes", 0.90 + (hero_combined_stats * 0.002))

        Stat_Modifiers["wcou"] = {
            "add": {
                "love": Stat_Product("wcou", "love", 2.5, [f_wcou_stats, f_wcou_pts, ("Hentai side", 0.75 + (0.002 * personality[1]))]),
                "lust": Stat_Product("wcou", "lust", 5.0, [f_wcou_stats, f_wcou_pts, ("Hentai side", 0.75 + (0.002 * personality[1]))]),
                "inti": Stat_Product("wcou", "inti", 1.0, [f_wcou_stats, f_wcou_pts, ("Intimate side", 0.75 + (0.002 * personality[4]))]),
            },
            "rem": {
                "love": ((2.5 / (0.90 + (hero_combined_stats * 0.002))) / max(0.01, (1 + (0.01 * wcou_bonus)))) * (0.75 + (0.002 * personality[2])),
                "lust": ((5.0 / (0.90 + (hero_combined_stats * 0.002))) / max(0.01, (1 + (0.01 * wcou_bonus)))) * (0.75 + (0.002 * personality[2])),
                "inti": ((1.0 / (0.90 + (hero_combined_stats * 0.002))) / max(0.01, (1 + (0.01 * wcou_bonus)))) * (0.75 + (0.002 * personality[3])),
            }
        }

        # ====================================================================================================
        # WNEI - Neighbor (1A)
        # ====================================================================================================
        f_wnei_pts = ("Bonus points", 1 + (0.01 * wnei_bonus))

        Stat_Modifiers["wnei"] = {
            "add": {
                "love": Stat_Product("wnei", "love", 2.5, [f_soc, f_wnei_pts, ("Kind side", 0.75 + (0.002 * personality[2])), f_stco]),
                "lust": Stat_Product("wnei", "lust", 5.0, [f_sex, f_wnei_pts, ("Hentai side", 0.75 + (0.002 * personality[1])), f_stco]),
                "inti": Stat_Product("wnei", "inti", 1.0, [f_soc, f_wnei_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco, ("Current love", 0.8 + (wnei_love * 0.01)), ("Current lust", 0.9 + (wnei_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wnei_bonus)))) * (0.75 + (0.002 * personality[1])),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wnei_bonus)))) * (0.75 + (0.002 * personality[2])),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wnei_bonus)))) * (0.75 + (0.002 * personality[3])) / max(0.01, (0.8 + (wnei_love * 0.01))) / (0.9 + (wnei_lust * 0.005)) / (1 + (wnei_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WDAN - Dancer (1A)
        # ====================================================================================================
        f_wdan_pts = ("Bonus points", 1 + (0.01 * wdan_bonus))

        Stat_Modifiers["wdan"] = {
            "add": {
                "love": Stat_Product("wdan", "love", 2.5, [f_soc, f_wdan_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "lust": Stat_Product("wdan", "lust", 5.0, [f_sex, f_wdan_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "inti": Stat_Product("wdan", "inti", 1.0, [f_soc, f_wdan_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), ("Hentai side", 0.975 + (personality[1] * 0.0005)), f_stco, ("Current love", 0.8 + (wdan_love * 0.01)), ("Current lust", 0.9 + (wdan_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wdan_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wdan_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wdan_bonus)))) * (0.75 + (0.002 * personality[3])) / (0.975 + (personality[1] * 0.0005)) / max(0.01, (0.8 + (wdan_love * 0.01))) / (0.9 + (wdan_lust * 0.005)) / (1 + (wdan_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WPRE - President (1B)
        # ====================================================================================================
        f_wpre_pts = ("Bonus points", 1 + (0.01 * wpre_bonus))
        f_wpre_int = ("Your intelligence", 0.8 + (stat_int * 0.002))
        f_wpre_res = ("Reserved side", 0.975 + (personality[3] * 0.0005))

        Stat_Modifiers["wpre"] = {
            "add": {
                "love": Stat_Product("wpre", "love", 2.5, [f_soc, f_wpre_pts, ("Kind side", (0.75 + (0.002 * personality[2])) * (0.975 + (personality[2] * 0.0005))), f_stco_in, f_wpre_int, f_wpre_res]),
                "lust": Stat_Product("wpre", "lust", 5.0, [f_sex, f_wpre_pts, ("Hentai side", 0.75 + (0.002 * personality[1])), f_stco_in, f_wpre_int, f_wpre_res, ("Kind side", 0.975 + (personality[2] * 0.0005))]),
                "inti": Stat_Product("wpre", "inti", 1.0, [f_soc, f_wpre_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco_in, f_wpre_int, f_wpre_res, ("Kind side", 0.975 + (personality[2] * 0.0005)), ("Current love", 0.8 + (wpre_love * 0.01)), ("Current lust", 0.9 + (wpre_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wpre_bonus)))) * (0.75 + (0.002 * personality[1])) / (0.8 + (stat_int * 0.002)) / (0.975 + (personality[3] * 0.0005)) / (0.975 + (personality[2] * 0.0005)),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wpre_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.8 + (stat_int * 0.002)) / (0.975 + (personality[3] * 0.0005)) / (0.975 + (personality[2] * 0.0005)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wpre_bonus)))) * (0.75 + (0.002 * personality[3])) / (0.8 + (stat_int * 0.002)) / (0.975 + (personality[3] * 0.0005)) / (0.975 + (personality[2] * 0.0005)) / max(0.01, (0.8 + (wpre_love * 0.01))) / (0.9 + (wpre_lust * 0.005)) / (1 + (wpre_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WRIC - Rich Girl (1B)
        # ====================================================================================================
        f_wric_pts = ("Bonus points", 1 + (0.01 * wric_bonus))

        Stat_Modifiers["wric"] = {
            "add": {
                "love": Stat_Product("wric", "love", 2.5, [f_soc, f_wric_pts, ("Kind side", 0.75 + (0.002 * personality[2])), f_stco_in, ("Hentai side", 0.975 + (personality[1] * 0.0005))]),
                "lust": Stat_Product("wric", "lust", 5.0, [f_sex, f_wric_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco_in]),
                "inti": Stat_Product("wric", "inti", 1.0, [f_soc, f_wric_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco_in, ("Hentai side", 0.975 + (personality[1] * 0.0005)), ("Current love", 0.8 + (wric_love * 0.01)), ("Current lust", 0.9 + (wric_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wric_bonus)))) * (0.75 + (0.002 * personality[1])) / (0.975 + (personality[1] * 0.0005)),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wric_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wric_bonus)))) * (0.75 + (0.002 * personality[3])) / (0.975 + (personality[1] * 0.0005)) / max(0.01, (0.8 + (wric_love * 0.01))) / (0.9 + (wric_lust * 0.005)) / (1 + (wric_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WGAL - Gal (1B)
        # ====================================================================================================

        hero_cha_soc_gal = (0.50 + (perk_cha_soc * 0.5)) + (0.50 + (perk_cha_soc * 0.5))
        f_wgal_soc = ("Social perks", hero_cha_soc_gal)
        f_wgal_pts = ("Bonus points", 1 + (0.01 * wgal_bonus))

        Stat_Modifiers["wgal"] = {
            "add": {
                "love": Stat_Product("wgal", "love", 2.5, [f_wgal_soc, f_wgal_pts, ("Kind side", 0.75 + (0.002 * personality[2])), f_stco, ("Hentai side", 1 / (0.975 + (personality[1] * 0.0005)))]),
                "lust": Stat_Product("wgal", "lust", 5.0, [f_wgal_soc, f_wgal_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) / (0.975 + (personality[1] * 0.0005))), f_stco]),
                "inti": Stat_Product("wgal", "inti", 1.0, [f_wgal_soc, f_wgal_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco, ("Hentai side", 1 / (0.975 + (personality[1] * 0.0005))), ("Current love", 0.8 + (wgal_love * 0.01)), ("Current lust", 0.9 + (wgal_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc_gal) / max(0.01, (1 + (0.01 * wgal_bonus)))) * (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005)),
                "lust": ((5.0 / hero_cha_soc_gal) / max(0.01, (1 + (0.01 * wgal_bonus)))) * (0.75 + (0.002 * personality[2])) * (0.975 + (personality[1] * 0.0005)),
                "inti": ((1.0 / hero_cha_soc_gal) / max(0.01, (1 + (0.01 * wgal_bonus)))) * (0.75 + (0.002 * personality[3])) * (0.975 + (personality[1] * 0.0005)) / max(0.01, (0.8 + (wgal_love * 0.01))) / (0.9 + (wgal_lust * 0.005)) / (1 + (wgal_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WOTA - Otaku (1B)
        # ====================================================================================================
        f_wota_pts = ("Bonus points", 1 + (0.01 * wota_bonus))

        Stat_Modifiers["wota"] = {
            "add": {
                "love": Stat_Product("wota", "love", 2.5, [f_soc, f_wota_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "lust": Stat_Product("wota", "lust", 5.0, [f_sex, f_wota_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "inti": Stat_Product("wota", "inti", 1.0, [f_soc, f_wota_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco, ("Hentai side", 0.975 + (personality[1] * 0.0005)), ("Current love", 0.8 + (wota_love * 0.01)), ("Current lust", 0.9 + (wota_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wota_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wota_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wota_bonus)))) * (0.75 + (0.002 * personality[3])) / (0.975 + (personality[1] * 0.0005)) / max(0.01, (0.8 + (wota_love * 0.01))) / (0.9 + (wota_lust * 0.005)) / (1 + (wota_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WDIS - Disciplinary (1B)
        # ====================================================================================================
        f_wdis_pts = ("Bonus points", 1 + (0.01 * wdis_bonus))

        Stat_Modifiers["wdis"] = {
            "add": {
                "love": Stat_Product("wdis", "love", 2.5, [f_soc, f_wdis_pts, ("Kind side", 0.75 + (0.002 * personality[2])), f_stco, ("Current love", 1 + (wdis_love * 0.0025))]),
                "lust": Stat_Product("wdis", "lust", 5.0, [f_sex, f_wdis_pts, ("Hentai side", 0.75 + (0.002 * personality[1])), f_stco, ("Current love", 1 + (wdis_love * 0.0025))]),
                "inti": Stat_Product("wdis", "inti", 1.0, [f_soc, f_wdis_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco, ("Current love", 1 + (wdis_love * 0.0050)), ("Current lust", 0.9 + (wdis_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wdis_bonus)))) * (0.75 + (0.002 * personality[1])) / (1 + (wdis_love * 0.0025)),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wdis_bonus)))) * (0.75 + (0.002 * personality[2])) / (1 + (wdis_love * 0.0025)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wdis_bonus)))) * (0.75 + (0.002 * personality[3])) / (1 + (wdis_love * 0.0050)) / (0.9 + (wdis_lust * 0.005)) / (1 + (wdis_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WGOT - Goth (1B)
        # ====================================================================================================
        f_wgot_pts = ("Bonus points", 1 + (0.01 * wgot_bonus))

        Stat_Modifiers["wgot"] = {
            "add": {
                "love": Stat_Product("wgot", "love", 2.5, [f_soc, f_wgot_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "lust": Stat_Product("wgot", "lust", 5.0, [f_sex, f_wgot_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "inti": Stat_Product("wgot", "inti", 1.0, [f_soc, f_wgot_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco, ("Hentai side", 0.975 + (personality[1] * 0.0005)), ("Current love", 0.8 + (wgot_love * 0.01)), ("Current lust", 0.9 + (wgot_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wgot_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wgot_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wgot_bonus)))) * (0.75 + (0.002 * personality[3])) / (0.975 + (personality[1] * 0.0005)) / max(0.01, (0.8 + (wgot_love * 0.01))) / (0.9 + (wgot_lust * 0.005)) / (1 + (wgot_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WDEL - Delinquent (1B)
        # ====================================================================================================
        f_wdel_pts = ("Bonus points", 1 + (0.01 * wdel_bonus))

        Stat_Modifiers["wdel"] = {
            "add": {
                "love": Stat_Product("wdel", "love", 2.5, [f_soc, f_wdel_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "lust": Stat_Product("wdel", "lust", 5.0, [f_sex, f_wdel_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "inti": Stat_Product("wdel", "inti", 1.0, [f_soc, f_wdel_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco, ("Hentai side", 0.975 + (personality[1] * 0.0005)), ("Current love", 0.8 + (wdel_love * 0.01)), ("Current lust", 0.9 + (wdel_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wdel_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wdel_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wdel_bonus)))) * (0.75 + (0.002 * personality[3])) / (0.975 + (personality[1] * 0.0005)) / max(0.01, (0.8 + (wdel_love * 0.01))) / (0.9 + (wdel_lust * 0.005)) / (1 + (wdel_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WUZA - Uzaki (1B)
        # ====================================================================================================
        f_wuza_pts = ("Bonus points", 1 + (0.01 * wuza_bonus))

        Stat_Modifiers["wuza"] = {
            "add": {
                "love": Stat_Product("wuza", "love", 2.5, [f_soc, f_wuza_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "lust": Stat_Product("wuza", "lust", 5.0, [f_sex, f_wuza_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "inti": Stat_Product("wuza", "inti", 1.0, [f_soc, f_wuza_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco, ("Hentai side", 0.975 + (personality[1] * 0.0005)), ("Current love", 0.8 + (wuza_love * 0.01)), ("Current lust", 0.9 + (wuza_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wuza_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wuza_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wuza_bonus)))) * (0.75 + (0.002 * personality[3])) / (0.975 + (personality[1] * 0.0005)) / max(0.01, (0.8 + (wuza_love * 0.01))) / (0.9 + (wuza_lust * 0.005)) / (1 + (wuza_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WLAZ - Lazy (1B)
        # ====================================================================================================
        f_wlaz_pts = ("Bonus points", 1 + (0.01 * wlaz_bonus))

        Stat_Modifiers["wlaz"] = {
            "add": {
                "love": Stat_Product("wlaz", "love", 2.5, [f_soc, f_wlaz_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "lust": Stat_Product("wlaz", "lust", 5.0, [f_sex, f_wlaz_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "inti": Stat_Product("wlaz", "inti", 1.0, [f_soc, f_wlaz_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco, ("Hentai side", 0.975 + (personality[1] * 0.0005)), ("Current love", 0.8 + (wlaz_love * 0.01)), ("Current lust", 0.9 + (wlaz_lust * 0.005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * wlaz_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "lust": ((5.0 / hero_cha_sex) / max(0.01, (1 + (0.01 * wlaz_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wlaz_bonus)))) * (0.75 + (0.002 * personality[3])) / (0.975 + (personality[1] * 0.0005)) / max(0.01, (0.8 + (wlaz_love * 0.01))) / (0.9 + (wlaz_lust * 0.005)) / (1 + (wlaz_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # WSUK - Succubus (3A)
        # ====================================================================================================
        f_wsuk_pts = ("Bonus points", 1 + (0.01 * wsuk_bonus))
        f_wsuk_stco = ("Student Council", 1 / (1 + (hero_stco * 0.3)))

        Stat_Modifiers["wsuk"] = {
            "add": {
                "love": Stat_Product("wsuk", "love", 4.0, [f_soc, f_wsuk_pts, f_wsuk_stco]),
                "lust": Stat_Product("wsuk", "lust", 5.0, [f_soc, f_wsuk_pts, f_wsuk_stco]),
                "inti": Stat_Product("wsuk", "inti", 2.0, [f_soc, f_wsuk_pts, f_wsuk_stco, ("Current love", 0.8 + (wsuk_love * 0.01)), ("Current lust", 0.9 + (wsuk_lust * 0.005))]),
            },
            "rem": {
                "love": ((4.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wsuk_bonus)))),
                "lust": ((5.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wsuk_bonus)))),
                "inti": ((2.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * wsuk_bonus)))) / max(0.01, (0.8 + (wsuk_love * 0.01))) / (0.9 + (wsuk_lust * 0.005)) / (1 + (wsuk_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # HPRV - Pervert (Boy)
        # ====================================================================================================
        f_hprv_pts = ("Bonus points", 1 + (0.01 * hprv_bonus))

        Stat_Modifiers["hprv"] = {
            "add": {
                "love": Stat_Product("hprv", "love", 2.5, [f_soc, f_hprv_pts, ("Hentai side", (0.75 + (0.002 * personality[1])) * (0.975 + (personality[1] * 0.0005))), f_stco]),
                "lust": Stat_Product("hprv", "lust", 5.0, []),
                "inti": Stat_Product("hprv", "inti", 1.0, [f_soc, f_hprv_pts, ("Intimate side", 0.75 + (0.002 * personality[4])), f_stco, ("Hentai side", 0.975 + (personality[1] * 0.0005))]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * hprv_bonus)))) * (0.75 + (0.002 * personality[2])) / (0.975 + (personality[1] * 0.0005)),
                "lust": 5.0,
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * hprv_bonus)))) * (0.75 + (0.002 * personality[3])) / (0.975 + (personality[1] * 0.0005)) / (1 + (hprv_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # HINE - Inept (Boy)
        # ====================================================================================================
        f_hine_pts = ("Bonus points", 1 + (0.01 * hine_bonus))

        Stat_Modifiers["hine"] = {
            "add": {
                "love": Stat_Product("hine", "love", 2.5, [("Social perks", 1 / hero_cha_soc), f_hine_pts, ("Reserved side", 0.9 + (0.002 * personality[3])), f_stco, ("Current love", 0.75 + (hine_love * 0.005))]),
                "lust": Stat_Product("hine", "lust", 1.0, []),
                "inti": Stat_Product("hine", "inti", 1.0, [("Social perks", 1 / hero_cha_soc), f_hine_pts, ("Reserved side", 0.9 + (0.002 * personality[3])), f_stco, ("Current love", 0.75 + (hine_love * 0.005))]),
            },
            "rem": {
                "love": ((2.5 * hero_cha_soc) / max(0.01, (1 + (0.01 * hine_bonus)))) / (0.9 + (0.002 * personality[3])) * (0.75 + (hine_love * 0.005)),
                "lust": 1.0,
                "inti": ((1.0 * hero_cha_soc) / max(0.01, (1 + (0.01 * hine_bonus)))) / (0.9 + (0.002 * personality[3])) * (0.75 + (hine_love * 0.005)) / (1 + (hine_inti * 0.02)),
            }
        }

        # ====================================================================================================
        # HRIV - Rival (Boy)
        # ====================================================================================================
        f_hriv_pts = ("Bonus points", 1 + (0.01 * hriv_bonus))

        Stat_Modifiers["hriv"] = {
            "add": {
                "love": Stat_Product("hriv", "love", 2.5, [f_soc, f_hriv_pts, ("Current love", 0.75 + (hriv_love * 0.005)), f_stco]),
                "lust": Stat_Product("hriv", "lust", 2.5, []),
                "inti": Stat_Product("hriv", "inti", 1.0, [f_soc, f_hriv_pts, ("Current love", 0.75 + (hriv_love * 0.005)), f_stco]),
            },
            "rem": {
                "love": ((2.5 / hero_cha_soc) / max(0.01, (1 + (0.01 * hriv_bonus)))) * (0.75 + (hriv_love * 0.005)),
                "lust": 2.5,
                "inti": ((1.0 / hero_cha_soc) / max(0.01, (1 + (0.01 * hriv_bonus)))) * (0.75 + (hriv_love * 0.005)) / (1 + (hriv_inti * 0.02)),
            }
        }
        
        # ====================================================================================================
        # CLUBS & GROUPS
        # ====================================================================================================
        Stat_Modifiers["club_stco"] = {
            "add": {
                "rep": (1 + hero_stco) * (0.75 + (0.005 * personality[3])),
            },
            "rem": {
                "rep": (1 + hero_stco) / (0.75 + (0.005 * personality[3])),
            }
        }
        
        # ====================================================================================================
        # CLAMP & ROUND STATS
        # ====================================================================================================
        # Hero stats
        store.stat_cha = min(100, round(abs(store.stat_cha), 2))
        store.stat_int = min(100, round(store.stat_int, 2))
        store.stat_phy = min(100, round(store.stat_phy, 2))
        store.stat_ene = min(100, round(store.stat_ene, 2))
        store.stat_hyg = min(100, round(store.stat_hyg, 2))
        store.stat_eat = min(100, round(store.stat_eat, 2))
        
        # Character stats with their specific max intimacy values
        char_inti_limits = {
            "wmom": wmom_inti_cap,
            "wsis": wsis_inti_cap,
            "wnei": wnei_inti_cap,

            "wcou": char_inti_cap,
            "wgma": char_inti_cap,
            "wdan": char_inti_cap,
            "wpre": char_inti_cap,
            "wric": char_inti_cap,
            "wgal": char_inti_cap,
            "wota": char_inti_cap,
            "wdis": char_inti_cap,
            "wgot": char_inti_cap,
            "wdel": char_inti_cap,
            "wuza": char_inti_cap,
            "wlaz": char_inti_cap,
            "wsuk": char_inti_cap,
            "hprv": char_inti_cap,
            "hine": char_inti_cap,
            "hriv": char_inti_cap,
        }
        
        # Clamp all character stats
        for char_id, inti_limit in char_inti_limits.items():
            if char_id in CHAR_IDS:
                lust_key = char_id + "_lust"
                if hasattr(store, lust_key):
                    setattr(store, lust_key, max(0, min(100, round(getattr(store, lust_key), 2))))
                love_key = char_id + "_love"
                if hasattr(store, love_key):
                    setattr(store, love_key, max(-100, min(100, round(getattr(store, love_key), 2))))
                inti_key = char_id + "_inti"
                if hasattr(store, inti_key):
                    setattr(store, inti_key, max(0, min(inti_limit, round(getattr(store, inti_key), 2))))
        
        return

# ----------------------------------------------------------------------------------------------------
label gametime_wait(target_hour=6, target_min=0): # Wait until target time. Resets activity at 00:00
# ----------------------------------------------------------------------------------------------------
    $ gametimemin = (gametimemin // 10) * 10
    # Callers pass `min + 10`, which can be 60+ (or hour 24) and never matches the clock, so carry it over.
    $ target_hour = (target_hour + target_min // 60) % 24
    $ target_min = target_min % 60
    while not (gametimehour == target_hour and gametimemin == target_min):
        $ gametimemin += 10
        call gametime from _call_gametime_81
        if gametimehour == 0 and gametimemin == 0:
            $ ResetActivityList()
    return

# --------------------------------------------------
label gametime_schoolnext(min_bonus=0): # Auto-calculate time to skip to next school period
# --------------------------------------------------
    python:
        skip_time = 0
        
        if Check_TimeStr("school_intro"): # Currently 07:00-07:29 → Skip to 07:30 (class_1 starts)
            skip_time = Get_Time("school_class_1")
        
        elif Check_TimeStr("school_class_1"): # Currently 07:30-09:29 → Skip to 09:30 (break starts)
            skip_time = Get_Time("school_break")
        
        elif Check_TimeStr("school_break"): # Currently 09:30-09:59 → Skip to 10:00 (class_2 starts)
            skip_time = Get_Time("school_class_2")
        
        elif Check_TimeStr("school_class_2"): # Currently 10:00-11:59 → Skip to 12:00 (end period starts)
            skip_time = Get_Time("school_end")
        
        elif Check_TimeStr("school_end"): # Currently 12:00-12:29 → Skip to 12:30 (school ends)
            current_time = Get_MinuteCurrent()
            skip_time = (750 - current_time) if current_time < 750 else 0
        
        else: # Not in any school period → Skip to next intro (07:00 tomorrow)
            skip_time = Get_Time("school_intro")
        
        skip_time += min_bonus # Add bonus time (for being late, etc)
    
    return skip_time

# ----------------------------------------------------------------------------------------------------
label gametime: # Check Game Time
# ----------------------------------------------------------------------------------------------------
    
    $ gametimehour = int(gametimehour)
    $ gametimemin = int(gametimemin)

    while gametimemin >= 60:
        # 1.2 fix (Plan - Efficiency.md): each loop pass is one hour, so decay a flat 60 min — the old `gametimemin*0.04` re-counted the remaining minutes every pass, over-decaying long time jumps quadratically.
        $ stat_hyg = max(0, stat_hyg-(60*0.04))
        python:
            for char_id in NPC_IDS:
                hyg_key = char_id + "_hyg"
                if hasattr(store, hyg_key):
                    setattr(store, hyg_key, round(max(0, getattr(store, hyg_key)-(60*0.04)), 2))
                eat_key = char_id + "_eat"
                if hasattr(store, eat_key):
                    setattr(store, eat_key, round(max(0, getattr(store, eat_key)-5), 2))
                # 2.2c: exertion dirt on top of time decay — sweat in P.E./Aquatics, grime from travel.
                # gametimehour*60 = top of the hour being processed this iteration.
                if hasattr(store, hyg_key):
                    dirt = 0
                    if Get_NPCSubject(char_id, gametimehour * 60) in ("P.E", "Aquatics"):
                        dirt = DIRT_PE
                    elif Get_ActivityName(char_id) == "moving":
                        dirt = DIRT_MOVE
                    if dirt:
                        setattr(store, hyg_key, round(max(0, getattr(store, hyg_key) - dirt), 2))
        $ gametimemin = gametimemin - 60
        $ gametimehour += 1
        call npc_action from _call_npc_action

    while gametimehour >= 24:
        $ gametimehour = gametimehour - 24
        $ gametimeday += 1
        $ gametimeweek = gametimeweeks[(gametimeweeks.index(gametimeweek) + 1) % 7]
    
    $ gametimeclock = str(int(gametimehour)).zfill(2) + ":" + str(int(gametimemin)).zfill(2)

    # 1.1 (Plan - Efficiency.md): the per-minute im.* tint chain lived here — bg images now tint via Get_TintBG_M/Get_TintSky_M (Spriteset.rpy), same formulas computed on demand.

    # 2.7: Laundry completion runs BEFORE Define_NPCState so a freshly-finished load can be acted on THIS tick — otherwise the NPC's "hanging clothes"/"collecting clothes" check still sees the washer/dryer running and skips, so nobody ever walks to the living room for it (BetterTXT fix 2).
    # Wash completion — washer finishes; outfits stay at loc="washer" until hung.
    if task_laundry_end > 0 and Get_MinuteTotal() >= task_laundry_end:
        $ task_laundry_end = 0

    # Dry completion — clothesline timer expires; move outfits from "line" to "dry".
    if task_dry_end > 0 and Get_MinuteTotal() >= task_dry_end:
        $ task_dry_end = 0
        python:
            for _cid in ["hero", "wsis", "wmom"]:
                for _o in Outfits_For(_cid):
                    _lv = "task_loc_" + _cid + "_" + _o
                    if getattr(store, _lv, "wardrobe") == "line":
                        setattr(store, _lv, "dry")

    $ Define_NPCState()
    $ Inject_SelfCare()        # 2.2a: free NPCs at home bathe/eat off-schedule when a need runs low
    $ Inject_ClassLocker()     # 2.2g: force locker change before & shower after a P.E./Aquatics block
    # 2.2f tension-relief now runs per activity-transition inside Get_NPCAct (Phase 6), not per-tick here.

    $ Define_MapState()

    return

# ----------------------------------------------------------------------------------------------------
# Change Map ID
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Map
# ----------------------------------------------------------------------------------------------------
label goto_map:
    $ hero_map = MAP_DATA["city"]["name"]
    return
# ----------------------------------------------------------------------------------------------------
# 2.5: Generic room-entry exposure — deterministic hook for private activities
# ----------------------------------------------------------------------------------------------------
label room_entry_exposure(char_id, activity):
    $ _char_name = getattr(store, "fname" + char_id, char_id)
    $ _tier = intimacy_tier(char_id)
    # Set replay guard FIRST — prevents infinite re-trigger if the scene jumps away
    $ setattr(store, char_id + "_exposure_seen", getattr(store, char_id + "_activity_time_start", 0))

    if activity == "bathing":
        if _tier >= 2:
            call hide_ui from _call_hide_ui_122
            $ msg.msg(renpy.translate_string("You accidentally walk in on [C_Nam]") + _char_name + renpy.translate_string("[C_Off] taking a bath!"))
            $ msg.msg(renpy.translate_string("[C_Nam]") + _char_name + renpy.translate_string("[C_Off] is startled but quickly covers herself."))
            $ add_stat(char_id, "inti", 1)
            $ hero_lust = min(100, hero_lust + 3)
            jump show_ui
        elif _tier >= 1:
            $ msg.msg(renpy.translate_string("You hear water running inside. [C_Nam]") + _char_name + renpy.translate_string("[C_Off] is taking a bath."))

    elif activity == "changing":
        if _tier >= 2:
            call hide_ui from _call_hide_ui_123
            $ msg.msg(renpy.translate_string("You walk in on [C_Nam]") + _char_name + renpy.translate_string("[C_Off] changing clothes!"))
            $ msg.msg(renpy.translate_string("[C_Nam]") + _char_name + renpy.translate_string("[C_Off] freezes for a moment before shooing you out."))
            $ add_stat(char_id, "inti", 1)
            $ hero_lust = min(100, hero_lust + 3)
            jump show_ui
        elif _tier >= 1:
            $ msg.msg(renpy.translate_string("You hear rustling inside. [C_Nam]") + _char_name + renpy.translate_string("[C_Off] is getting changed."))

    return

# ----------------------------------------------------------------------------------------------------
# Home
# ----------------------------------------------------------------------------------------------------
label goto_home_facade:
    $ hero_map = MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["facade"]["name"]
    return
# --------------------------------------------------
label goto_home_livingroom:
    $ hero_map = MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["living_room"]["name"]
    return
# --------------------------------------------------
label goto_home_kitchen:
    $ hero_map = MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["kitchen"]["name"]
    return
# --------------------------------------------------
label goto_home_hallway:
    $ hero_map = MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["hallway"]["name"]
    return
# --------------------------------------------------
label goto_home_bedroom_hero:
    $ hero_map = MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bedroom_hero"]["name"]
    return
# --------------------------------------------------
label goto_home_bedroom_wmom:
    $ hero_map = MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bedroom_wmom"]["name"]

    # 2.5: Room-entry exposure — WMOM changing in her bedroom
    if wmom_activity_current == "changing" or (isinstance(wmom_activity_current, tuple) and wmom_activity_current[0] == "changing"):
        if wmom_exposure_seen != wmom_activity_time_start and intimacy_tier("wmom") >= 1:
            call room_entry_exposure("wmom", "changing") from _call_room_entry_exposure

    return
# --------------------------------------------------
label goto_home_bedroom_wsis:

    if wsis_activity_current == "at sleepover":
        jump wsis_sleepover

    elif map_lock_bedroom_wsis == True:
        $ msg.msg(renpy.translate_string("It's locked"))
        return

    $ hero_map = MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bedroom_wsis"]["name"]

    # 2.5: Room-entry exposure — WSIS changing (replay guard on existing scene)
    if wsis_activity_current == "changing" or (isinstance(wsis_activity_current, tuple) and wsis_activity_current[0] == "changing"):
        if wsis_exposure_seen != wsis_activity_time_start and intimacy_tier("wsis") >= 1:
            call hide_ui from _call_hide_ui_124
            jump wsis_show_activity_changing

    return
# --------------------------------------------------
label goto_home_bathroom:
    if hero_map == "Home - Hallway":
        if (wsis_map == MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bathroom"]["name"]) or (wnei_map == MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bathroom"]["name"]):
            call action_bathe_oops_2 from _call_action_bathe_oops_2
        elif wnei_is_flw:
            call hide_ui from _call_hide_ui_125
            mind "(Oops{w=[wt1]}, {nm}[fnamewnei]{/nm} is following me)"
            jump show_ui
        else:
            $ hero_map = MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bathroom"]["name"]

            # 2.5: Room-entry exposure — WMOM bathing
            if wmom_activity_current == "bathing" or (isinstance(wmom_activity_current, tuple) and wmom_activity_current[0] == "bathing"):
                if wmom_exposure_seen != wmom_activity_time_start and intimacy_tier("wmom") >= 1:
                    call room_entry_exposure("wmom", "bathing") from _call_room_entry_exposure_1
    return
    
# ----------------------------------------------------------------------------------------------------
# Office
# ----------------------------------------------------------------------------------------------------
label goto_office_facade:
    $ hero_map = MAP_DATA["office"]["name"] + " - " + MAP_DATA["office"]["map"]["facade"]["name"]
    return

label goto_office_room:
    $ hero_map = MAP_DATA["office"]["name"] + " - " + MAP_DATA["office"]["map"]["office_wcou"]["name"]
    return

# ----------------------------------------------------------------------------------------------------
# School
# ----------------------------------------------------------------------------------------------------
label goto_school_facade:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["facade"]["name"]
    return
# --------------------------------------------------
label goto_school_courtyard:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["courtyard"]["name"]
    return
# --------------------------------------------------
label goto_school_frontyard:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["frontyard"]["name"]
    return
# --------------------------------------------------
label goto_school_hallway1:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["hallway_1"]["name"]
    return
# --------------------------------------------------
label goto_school_hallway2:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["hallway_2"]["name"]
    return
# --------------------------------------------------
label goto_school_library:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["library"]["name"]
    return
# --------------------------------------------------
label goto_school_locker_m:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["locker_m"]["name"]
    return
# --------------------------------------------------
label goto_school_locker_f:
    # Remember the room HERO came in from, so a bad changing-room verdict can throw him back out to it. check_playermap re-calls this label every gamecheck while he stands here, so only a genuine arrival (hero_map is still the OLD room) may overwrite it.
    if hero_map != MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["locker_f"]["name"]:
        $ hero_map_prev = hero_map
        $ hero_locker_oops_visit = False    # a fresh arrival re-arms the group scene (one per visit)

        # Did he walk in with a real reason? This MUST be captured on arrival, because the errand below consumes `hero_locker_f_access` before `action_change_oops` ever runs — reading the flag inside the scene scored an honest answer as a lie.
        $ hero_locker_f_excuse = hero_locker_f_access or club_stco_quest_1 == 1

    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["locker_f"]["name"]

    # Idea 4: room-entry exposure — find the first girl mid-change/bath in the female locker. Reuses the generic room_entry_exposure (which JUMPS to show_ui on tier 2+, so must-run work goes before it).
    python:
        _exposed_g, _exposed_a = None, None
        _lf = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["locker_f"]["name"]
        for _g in NPC_IDS:
            if not _g.startswith("w"):
                continue
            if getattr(store, _g + "_map", "") != _lf:
                continue
            _ga = getattr(store, _g + "_activity_current", None)
            _gn = _ga[0] if isinstance(_ga, tuple) else _ga
            if _gn in ("changing", "bathing") and getattr(store, _g + "_exposure_seen", None) != getattr(store, _g + "_activity_time_start", 0) and intimacy_tier(_g) >= 1:
                _exposed_g, _exposed_a = _g, _gn
                break

    # Idea 4 v1: the only reason HERO can reach this room is WTPE's "grab my item" errand — complete it on entry (BEFORE the exposure's possible jump). Future access hooks would branch on their own flag.
    if hero_locker_f_access and club_stco_quest_1 == 0:
        $ hero_locker_f_access = False
        $ msg.msg(renpy.translate_string("You quickly grab the equipment bag the teacher left on the bench."))

    # Group confrontation takes priority: if anyone is mid-CHANGE the crowd scene runs instead of the single-girl toast (it carries its own replay guard for the whole cast). Scene + interaction live in `action_change_oops` (System - Changing.rpy); a lone bather still falls through to the old path.
    # `hero_locker_oops_visit` caps it at ONE group scene per visit. Without it this label re-runs on every gamecheck while HERO stands here, so each girl who starts changing next would chain another scene.
    if not hero_locker_oops_visit and Change_OopsCast():
        call action_change_oops from _call_action_change_oops

    # During the shower quest (any active state) stalls are driven by the Door button, so the auto-exposure only runs on the normal (non-quest, e.g. WTPE errand) locker access.
    if _exposed_g is not None and club_stco_quest_1 == 0:
        call room_entry_exposure(_exposed_g, _exposed_a) from _call_room_entry_exposure_2

    return
# --------------------------------------------------
label goto_school_sportcourt:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["sports_court"]["name"]
    return
# --------------------------------------------------
label goto_school_pool:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["swimming_pool"]["name"]
    return
# --------------------------------------------------
label goto_school_classroom_1a:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["class_1a"]["name"]
    return
# --------------------------------------------------
label goto_school_classroom_1b:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["class_1b"]["name"]
    return
# --------------------------------------------------
label goto_school_classroom_3a:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["class_3a"]["name"]
    return
# --------------------------------------------------
label goto_school_club_council:
    $ hero_map = MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["club_coun"]["name"]
    return

# ----------------------------------------------------------------------------------------------------
# Shopping Mall
# ----------------------------------------------------------------------------------------------------
label goto_shopping_facade:
    $ Set_CharMap("hero", "shopping", "facade")
    return
# --------------------------------------------------
label goto_shopping_hall:
    $ Set_CharMap("hero", "shopping", "hall")
    return
# --------------------------------------------------
label goto_shopping_cinema_entrance:
    $ Set_CharMap("hero", "shopping", "cinema_entrance")
    return
# --------------------------------------------------
label goto_shopping_store_clothing:
    $ Set_CharMap("hero", "shopping", "store_clothing")
    return
# --------------------------------------------------
label goto_shopping_store_arcade:
    $ Set_CharMap("hero", "shopping", "store_arcade")
    return
# --------------------------------------------------
label goto_shopping_court_food:
    $ Set_CharMap("hero", "shopping", "court_food")
    return

# ----------------------------------------------------------------------------------------------------
# Check available Scenes
# ----------------------------------------------------------------------------------------------------
label check_availablescene:
    # -----------------------------------------------------------------------------------------------
    # Outfit Unlock
    # -----------------------------------------------------------------------------------------------
    if hero_quest_1 >= 3:
        if "casual" not in wsis_achiev_wear:
            $ wsis_achiev_wear.append("casual")

        if "casual" not in hero_achiev_wear:
            $ hero_achiev_wear.append("casual")

    if hero_quest_1 >= 4:
        if "casual" not in wmom_achiev_wear:
            $ wmom_achiev_wear.append("casual")

        if "casual" not in wnei_achiev_wear:
            $ wnei_achiev_wear.append("casual")

    if hero_quest_1 >= 6:
        if "sleep" not in wsis_achiev_wear:
            $ wsis_achiev_wear.append("sleep")
        if "under" not in wsis_achiev_wear:
            $ wsis_achiev_wear.append("under")

        if "sleep" not in wmom_achiev_wear:
            $ wmom_achiev_wear.append("sleep")
        if "under" not in wmom_achiev_wear:
            $ wmom_achiev_wear.append("under")

        if "under" not in wnei_achiev_wear:
            $ wnei_achiev_wear.append("under")

    if gametimeday >= 2:
        if "school" not in hero_achiev_wear:
            $ hero_achiev_wear.append("school")
        if "school_sport" not in hero_achiev_wear:
            $ hero_achiev_wear.append("school_sport")
        if "school_swim" not in hero_achiev_wear:
            $ hero_achiev_wear.append("school_swim")

        if "school" not in wsis_achiev_wear:
            $ wsis_achiev_wear.append("school")
        if "school_sport" not in wsis_achiev_wear:
            $ wsis_achiev_wear.append("school_sport")
        if "school_swim" not in wsis_achiev_wear:
            $ wsis_achiev_wear.append("school_swim")

        if "school" not in wnei_achiev_wear:
            $ wnei_achiev_wear.append("school")
        if "school_sport" not in wnei_achiev_wear:
            $ wnei_achiev_wear.append("school_sport")
        if "school_swim" not in wnei_achiev_wear:
            $ wnei_achiev_wear.append("school_swim")

    if hero_quest_2 >= 4:
        if "work" not in wcou_achiev_wear:
            $ wcou_achiev_wear.append("work")
        if "under" not in wcou_achiev_wear:
            $ wcou_achiev_wear.append("under")

    # -----------------------------------------------------------------------------------------------
    # Special Event
    # -----------------------------------------------------------------------------------------------
    if gametimehour == 23:
        call hide_ui from _call_hide_ui_126
        scene bg_0
        with dissolve
        "You got very sleepy and went to bed.{fast}"
        call passday from _call_passday_2

    if hero_quest_1 == 0:
        $ is_specialevent = True

    elif (hero_quest_1 == 1 or hero_quest_1 == 2) and (gametimehour >= 12 and gametimehour <= 13):
        if Check_CharInMap("wnei", "home"):
            $ StartAct("wnei", (("moving", "neighbor"), 10), True)
        if Get_ActivityName("wsis") not in ["staying"] and hero_quest_1 == 1:
            $ StartAct("wsis", (("staying", "living_room"), 60), True)
        if Get_ActivityName("wmom") not in ["staying"] and hero_quest_1 == 1:
            $ StartAct("wmom", (("staying", "living_room"), 60), True)
        $ is_specialevent = True

    else:
        $ is_specialevent = False

    if gametimeday == 1 and gametimehour >= 20 and not ("WSIS" in scenestep or "WMOM" in scenestep or "WNEI" in scenestep):
        $ is_specialevent = False

    elif gametimeday == 1 and gametimehour >= 18 and gametimehour <= 19:
        $ is_specialevent = True
        if 0 > 1: # disable
            $ hero_fx = 0
            $ hero_mood = "a1"
            $ wmom_wear = "party1"
            $ wsis_wear = "party2"
            $ wnei_wear = "party1"
            $ wmom_map = "Home - Living Room"
            $ wsis_map = "Home - Living Room"
            $ wnei_map = "Home - Living Room"

    elif hero_quest_1 == 3 and gametimehour >= 17:
        $ hero_quest_1 = 4
        jump scenestep_0_3

    if gametimeday == 2 and ((gametimehour >= 6 and gametimehour <= 7) or (gametimehour >= 12 and gametimehour <= 13)) and hero_quest_2 <= 2:
        if gametimehour == 6:
            if Get_ActivityName("wsis") not in ["staying"]:
                $ StartAct("wsis", (("changing", "school"), 0), True)
                $ StartAct("wsis", (("staying", "living_room"), 60), True)
        $ is_specialevent = True

        if hero_quest_2 <= 2 and (gametimehour >= 12 and gametimehour <= 13):
            jump schoolday_wsis_leaving

    elif gametimeday == 2 and gametimehour >= 18 and hero_quest_2 < 4:
        $ is_specialevent = True

    # ----------------------------------------------------------------------------------------------------
    # Scenes triggered in "Home - Living Room"
    # ----------------------------------------------------------------------------------------------------
    if Check_CharInMap(char_id="hero", map_main="home", map_sub="living_room"):
        if hero_quest_1 == 0:
            jump scenestep_0_0

        elif hero_quest_1 == 1 and gametimehour >= 12 and gametimehour <= 13:
            jump scenestep_0_1

        elif "WSIS" in scenestep and "WMOM" in scenestep and "WNEI" in scenestep:
            $ scenestep.remove("WSIS")
            $ scenestep.remove("WMOM")
            $ scenestep.remove("WNEI")
            $ is_specialevent = False
            $ gametimemin += 180
            jump scenestep_0_5

    # ----------------------------------------------------------------------------------------------------
    # Scenes triggered in "Office Building - Doctor's Office"
    # ----------------------------------------------------------------------------------------------------
    if gametimeday == 2 and gametimehour >= 18 and (Get_ActivityName("wcou") not in ["staying"]) and hero_quest_2 < 4:
        $ StartAct("wcou", (("staying", "office_wcou"), 60), True)
        call hide_ui from _call_hide_ui_127
        mind "(Oh, look at the time! I need to hurry and meet with {nm}[hero_about_wcou]{/nm}."
        $ scenestep[1] = "Tua Mãe"
        jump show_ui

    if hero_map == "Office Building - Doctor's Office":
        if hero_quest_2 <= 3:
            jump wcou_office1

    # ----------------------------------------------------------------------------------------------------
    # Scenes triggered when HERO wakes up
    # ----------------------------------------------------------------------------------------------------
    screen phone_call():
        timer 3 repeat True action If(renpy.variant("mobile"), true=(If(preferences.vibration == True, Function(renpy.vibrate, 1))), false=(Play("SE1", "PhoneVibration.ogg", loop=False)))

    if hero_quest_3 == 1 and (gametimeweek != "Sunday" and gametimeweek != "Saturday"):

        show screen phone_call
        call hide_ui from _call_hide_ui_128
        show HERO at CC with dissolve

        "You're receiving a phone call."

        hide screen phone_call
        pause(0.5)

        wcou "{bt}❤ Good morning, love of my life! ❤{/bt}"
        hero "H{w=[wt1]}-hi, {nm}[hero_to_wcou]{/nm}.{w=[wt2]} Good morning!"
        wcou "So babe.{w=[wt2]} Let me ask you a question.{w=[wt3]} How often do you get sick?"

        $ hero_mood = "A2"
        hero "Well{w=[wt2]}, I think it's kinda rare...{w=[wt3]} In fact{w=[wt1]}, I don't really remember the last time I got sick."
        wcou "Ohhh!{w=[wt2]} So that's how it was, right?{w=[wt2]} Well{w=[wt1]}, I have some news for you babe!{w=[wt3]} Your exam results are ready{w=[wt1]}, but I need to deliver them to you in person.{w=[wt3]} Come to my office at night okay?"

        $ hero_mood = "O1"
        hero "{aw}Ehhh...?{/aw}{w=[wt4]} O{w=[wt1]}-okay.{w=[wt3]} But{w=[wt2]}, now you've got me a little apprehensive.{w=[wt4]} W{w=[wt1]}-what's{w=[wt1]}-{w=[wt1]}{nw}"
        wcou "Oh{w=[wt1]}, I have to go now babe.{w=[wt2]} I'll explain everything to you at night in my office!{w=[wt2]}{pr}{bt}Bye bye! ❤{/bt}"
        hero "W{w=[wt1]}-wait!"
        mind "(She turned off.{w=[wt3]} Shit!{w=[wt1]} What did she mean by that question!?)"

        $ hero_quest_3 = 2

        jump show_ui

    # ----------------------------------------------------------------------------------------------------
    # Scenes triggered in "School
    # ----------------------------------------------------------------------------------------------------
    # Frontyard
    # --------------------------------------------------
    elif gametimeday == 2 and hero_map == "School - Frontyard" and hero_quest_2 < 1:
        jump schoolday_1_1

    # Hallway2
    # --------------------------------------------------
    elif hero_quest_2 == 1 and wpre_is_flw and not "hallway2" in scenestep and hero_map == "School - Upstairs Hallway":
        jump schoolday_1_1_hallway

    # Courtyard
    # --------------------------------------------------
    elif hero_quest_2 == 1 and wpre_is_flw and not "courtyard" in scenestep and hero_map == "School - Courtyard":
        jump schoolday_1_1_courtyard

    # Library
    # --------------------------------------------------
    elif hero_quest_2 == 1 and wpre_is_flw and not "library" in scenestep and hero_map == "School - Library":
        jump schoolday_1_1_library

    # Classroom
    # --------------------------------------------------
    elif hero_quest_2 == 1 and hero_map == "School - Classroom (1B)":
        jump schoolday_1_1_classroom

    # ----------------------------------------------------------------------------------------------------
    # No Scene found
    # ----------------------------------------------------------------------------------------------------
    return

# ----------------------------------------------------------------------------------------------------
# NPC Lust Effect
# ----------------------------------------------------------------------------------------------------
label npc_lust:

    # WMOM
    if wmom_lust >= min(100,(char_inti_cap*2.5)+25):
        $ wmom_fx = 2
        if "WMOM_is_horny_1" in wmom_know:
            $ wmom_know.remove("WMOM_is_horny_1")
        if not "WMOM_is_horny_2" in wmom_know:
            $ wmom_know.append("WMOM_is_horny_2")
            $ msg.msg(renpy.translate_string("{nm}[fnamewmom]{/nm} is very horny."))
    elif wmom_lust >= min(75,(char_inti_cap*2)+20):
        $ wmom_fx = 1
        if "WMOM_is_horny_2" in wmom_know:
            $ wmom_know.remove("WMOM_is_horny_2")
        if not "WMOM_is_horny_1" in wmom_know:
            $ wmom_know.append("WMOM_is_horny_1")
            $ msg.msg(renpy.translate_string("{nm}[fnamewmom]{/nm} is getting horny."))
    else:
        $ wmom_fx = 0
        if "WMOM_is_horny_1" in wmom_know:
            $ wmom_know.remove("WMOM_is_horny_1")
        if "WMOM_is_horny_2" in wmom_know:
            $ wmom_know.remove("WMOM_is_horny_2")

    # WSIS
    if wsis_lust >= min(100,(char_inti_cap*2.5)+25):
        $ wsis_fx = 2
        if "WSIS_is_horny_1" in wsis_know:
            $ wsis_know.remove("WSIS_is_horny_1")
        if not "WSIS_is_horny_2" in wsis_know:
            $ wsis_know.append("WSIS_is_horny_2")
            $ msg.msg(renpy.translate_string("{nm}[fnamewsis]{/nm} is very horny."))
    elif wsis_lust >= min(75,(char_inti_cap*2)+20):
        $ wsis_fx = 1
        if "WSIS_is_horny_2" in wsis_know:
            $ wsis_know.remove("WSIS_is_horny_2")
        if not "WSIS_is_horny_1" in wsis_know:
            $ wsis_know.append("WSIS_is_horny_1")
            $ msg.msg(renpy.translate_string("{nm}[fnamewsis]{/nm} is getting horny."))
    else:
        $ wsis_fx = 0
        if "WSIS_is_horny_1" in wsis_know:
            $ wsis_know.remove("WSIS_is_horny_1")
        if "WSIS_is_horny_2" in wsis_know:
            $ wsis_know.remove("WSIS_is_horny_2")

    # WNEI
    if wnei_lust >= min(100,(char_inti_cap*2.5)+25):
        $ wnei_fx = 2
        if "WNEI_is_horny_1" in wnei_know:
            $ wnei_know.remove("WNEI_is_horny_1")
        if not "WNEI_is_horny_2" in wnei_know:
            $ wnei_know.append("WNEI_is_horny_2")
            $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} is very horny."))
    elif wnei_lust >= min(75,(char_inti_cap*2)+20):
        $ wnei_fx = 1
        if "WNEI_is_horny_2" in wnei_know:
            $ wnei_know.remove("WNEI_is_horny_2")
        if not "WNEI_is_horny_1" in wnei_know:
            $ wnei_know.append("WNEI_is_horny_1")
            $ msg.msg(renpy.translate_string("{nm}[fnamewnei]{/nm} is getting horny."))
    else:
        $ wnei_fx = 0
        if "WNEI_is_horny_1" in wnei_know:
            $ wnei_know.remove("WNEI_is_horny_1")
        if "WNEI_is_horny_2" in wnei_know:
            $ wnei_know.remove("WNEI_is_horny_2")

    # WPRE
    if wpre_lust >= min(100,(char_inti_cap*2.5)+25):
        $ wpre_fx = 2
        if "WPRE_is_horny_1" in wpre_know:
            $ wpre_know.remove("WPRE_is_horny_1")
        if not "WPRE_is_horny_2" in wpre_know:
            $ wpre_know.append("WPRE_is_horny_2")
            $ msg.msg(renpy.translate_string("{nm}[fnamewpre]{/nm} is very horny."))
    elif wpre_lust >= min(75,(char_inti_cap*2)+20):
        $ wpre_fx = 1
        if "WPRE_is_horny_2" in wpre_know:
            $ wpre_know.remove("WPRE_is_horny_2")
        if not "WPRE_is_horny_1" in wpre_know:
            $ wpre_know.append("WPRE_is_horny_1")
            $ msg.msg(renpy.translate_string("{nm}[fnamewpre]{/nm} is getting horny."))
    else:
        $ wpre_fx = 0
        if "WPRE_is_horny_1" in wpre_know:
            $ wpre_know.remove("WPRE_is_horny_1")
        if "WPRE_is_horny_2" in wpre_know:
            $ wpre_know.remove("WPRE_is_horny_2")

    # WOTA
    if wota_lust >= min(100,(char_inti_cap*2.5)+25):
        $ wota_fx = 2
        if "WOTA_is_horny_1" in wota_know:
            $ wota_know.remove("WOTA_is_horny_1")
        if not "WOTA_is_horny_2" in wota_know:
            $ wota_know.append("WOTA_is_horny_2")
            $ msg.msg(renpy.translate_string("{nm}[fnamewota]{/nm} is very horny."))
    elif wota_lust >= min(75,(char_inti_cap*2)+20):
        $ wota_fx = 1
        if "WOTA_is_horny_2" in wota_know:
            $ wota_know.remove("WOTA_is_horny_2")
        if not "WOTA_is_horny_1" in wota_know:
            $ wota_know.append("WOTA_is_horny_1")
            $ msg.msg(renpy.translate_string("{nm}[fnamewota]{/nm} is getting horny."))
    else:
        $ wota_fx = 0
        if "WOTA_is_horny_1" in wota_know:
            $ wota_know.remove("WOTA_is_horny_1")
        if "WOTA_is_horny_2" in wota_know:
            $ wota_know.remove("WOTA_is_horny_2")

    # WDIS
    if wdis_lust >= min(100,(char_inti_cap*2.5)+25):
        $ wdis_fx = 2
        if "WDIS_is_horny_1" in wdis_know:
            $ wdis_know.remove("WDIS_is_horny_1")
        if not "WDIS_is_horny_2" in wdis_know:
            $ wdis_know.append("WDIS_is_horny_2")
            $ msg.msg(renpy.translate_string("{nm}[fnamewdis]{/nm} is very horny."))
    elif wdis_lust >= min(75,(char_inti_cap*2)+20):
        $ wdis_fx = 1
        if "WDIS_is_horny_2" in wdis_know:
            $ wdis_know.remove("WDIS_is_horny_2")
        if not "WDIS_is_horny_1" in wdis_know:
            $ wdis_know.append("WDIS_is_horny_1")
            $ msg.msg(renpy.translate_string("{nm}[fnamewdis]{/nm} is getting horny."))
    else:
        $ wdis_fx = 0
        if "WDIS_is_horny_1" in wdis_know:
            $ wdis_know.remove("WDIS_is_horny_1")
        if "WDIS_is_horny_2" in wdis_know:
            $ wdis_know.remove("WDIS_is_horny_2")

    # WGAL
    if wgal_lust >= min(100,(char_inti_cap*2.5)+25):
        $ wgal_fx = 2
        if "WGAL_is_horny_1" in wgal_know:
            $ wgal_know.remove("WGAL_is_horny_1")
        if not "WGAL_is_horny_2" in wgal_know:
            $ wgal_know.append("WGAL_is_horny_2")
            $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} is very horny."))
    elif wgal_lust >= min(75,(char_inti_cap*2)+20):
        $ wgal_fx = 1
        if "WGAL_is_horny_2" in wgal_know:
            $ wgal_know.remove("WGAL_is_horny_2")
        if not "WGAL_is_horny_1" in wgal_know:
            $ wgal_know.append("WGAL_is_horny_1")
            $ msg.msg(renpy.translate_string("{nm}[fnamewgal]{/nm} is getting horny."))
    else:
        $ wgal_fx = 0
        if "WGAL_is_horny_1" in wgal_know:
            $ wgal_know.remove("WGAL_is_horny_1")
        if "WGAL_is_horny_2" in wgal_know:
            $ wgal_know.remove("WGAL_is_horny_2")

    # HPRV
    if hprv_lust >= min(100,(char_inti_cap*2.5)+25):
        $ hprv_fx = 2
        if "HPRV_is_horny_1" in hprv_know:
            $ hprv_know.remove("HPRV_is_horny_1")
        if not "HPRV_is_horny_2" in hprv_know:
            $ hprv_know.append("HPRV_is_horny_2")
            $ msg.msg(renpy.translate_string("{nm}[fnamehprv]{/nm} is very horny."))
    elif hprv_lust >= min(75,(char_inti_cap*2)+20):
        $ hprv_fx = 1
        if "HPRV_is_horny_2" in hprv_know:
            $ hprv_know.remove("HPRV_is_horny_2")
        if not "HPRV_is_horny_1" in hprv_know:
            $ hprv_know.append("HPRV_is_horny_1")
            $ msg.msg(renpy.translate_string("{nm}[fnamehprv]{/nm} is getting horny."))
    else:
        $ hprv_fx = 0
        if "HPRV_is_horny_1" in hprv_know:
            $ hprv_know.remove("HPRV_is_horny_1")
        if "HPRV_is_horny_2" in hprv_know:
            $ hprv_know.remove("HPRV_is_horny_2")

    return

# ----------------------------------------------------------------------------------------------------
# NPC Action
# ----------------------------------------------------------------------------------------------------
label npc_action:
    # -----------------------------------------------------------------------------------------------
    # Update Memory
    # -----------------------------------------------------------------------------------------------
    # WCOU
    if "Hug" in wcou_know:
        $ wcou_know.remove("Hug") # Start Hug Regen Cooldown

    # WNEI
    if "Talk" in wnei_know:
        $ wnei_know.remove("Talk") # Regen 1 Talk
    if "Hug_Hour" in wnei_know and "Hug_Enough" in wnei_know:
        $ wnei_know.remove("Hug_Enough") # Regen Hug Affection
    if "Hug" in wnei_know and not "Hug_Hour" in wnei_know:
        $ wnei_know.append("Hug_Hour") # Start Hug Regen Cooldown
    if "PatHead" in wnei_know and not "PatHead_Hour" in wnei_know:
        $ wnei_know.append("PatHead_Hour") # Start Head Pat Regen Cooldown
    if "Needs_Pee_Y" in wnei_know and gametimehour == 21:
        $ wnei_know.remove("Needs_Pee_Y")

    # WSIS
    if "Talk" in wsis_know:
        $ wsis_know.remove("Talk") # Regen 1 Talk
    if "Hug_Enough" in wsis_know:
        $ wsis_know.append("Hug_Regen") # Regen 1/6 Hug
    if sum(1 for buceta in wsis_know if buceta == "Hug_Regen") >= 6:
        $ wsis_know.remove("Hug_Enough") # Regen 1 Hug
        $ wsis_know.remove("Hug_Regen") # Regen 1 Hug
    if "Talk_How" in wsis_know:
        $ wsis_know.append("Talk_How_Regen") # Regen 1/6 Talk_How
    if sum(1 for buceta in wsis_know if buceta == "Talk_How_Regen") >= 8:
        $ wsis_know.remove("Talk_How") # Regen 1 Talk_How
        while "Talk_How_Regen" in wsis_know:
            $ wsis_know.remove("Talk_How_Regen") # Regen 1 Talk_How
    if "WSIS_Quest_1_1" in wsis_know and gametimehour >= 12:
        $ wsis_know.remove("WSIS_Quest_1_1")
    if "WakeUp" in wsis_know and gametimehour >= 9:
        $ wsis_know.remove("WakeUp")

    # WGAL
    if "Hug_Enough" in wgal_know:
        $ wgal_know.append("Hug_Regen") # Regen 1/6 Hug
    if sum(1 for buceta in wgal_know if buceta == "Hug_Regen") >= 3:
        $ wgal_know.remove("Hug_Enough") # Regen 1 Hug
        $ wgal_know.remove("Hug_Regen") # Regen 1 Hug
    if "Hug" in wgal_know:
        $ wgal_know.remove("Hug") # Start Hug Regen Cooldown
    if "Talk_How" in wgal_know:
        $ wgal_know.append("Talk_How_Regen") # Regen 1/6 Talk_How
    if sum(1 for buceta in wgal_know if buceta == "Talk_How_Regen") >= 8:
        $ wgal_know.remove("Talk_How") # Regen 1 Talk_How
        while "Talk_How_Regen" in wgal_know:
            $ wgal_know.remove("Talk_How_Regen") # Regen 1 Talk_How

    # WPRE
    if "Hug_Enough" in wpre_know:
        $ wpre_know.append("Hug_Regen") # Regen 1/6 Hug
    if sum(1 for buceta in wpre_know if buceta == "Hug_Regen") >= 3:
        $ wpre_know.remove("Hug_Enough") # Regen 1 Hug
        $ wpre_know.remove("Hug_Regen") # Regen 1 Hug
    if "Hug" in wpre_know:
        $ wpre_know.remove("Hug") # Start Hug Regen Cooldown
    if "Talk_How" in wpre_know:
        $ wpre_know.append("Talk_How_Regen") # Regen 1/6 Talk_How
    if sum(1 for buceta in wpre_know if buceta == "Talk_How_Regen") >= 8:
        $ wpre_know.remove("Talk_How") # Regen 1 Talk_How
        while "Talk_How_Regen" in wpre_know:
            $ wpre_know.remove("Talk_How_Regen") # Regen 1 Talk_How

    # WOTA
    if "Hug_Enough" in wota_know:
        $ wota_know.append("Hug_Regen") # Regen 1/6 Hug
    if sum(1 for buceta in wota_know if buceta == "Hug_Regen") >= 3:
        $ wota_know.remove("Hug_Enough") # Regen 1 Hug
        $ wota_know.remove("Hug_Regen") # Regen 1 Hug
    if "Hug" in wota_know:
        $ wota_know.remove("Hug") # Start Hug Regen Cooldown
    if "Talk_How" in wota_know:
        $ wota_know.append("Talk_How_Regen") # Regen 1/6 Talk_How
    if sum(1 for buceta in wota_know if buceta == "Talk_How_Regen") >= 8:
        $ wota_know.remove("Talk_How") # Regen 1 Talk_How
        while "Talk_How_Regen" in wota_know:
            $ wota_know.remove("Talk_How_Regen") # Regen 1 Talk_How

    # WDIS
    if "Talk_How" in wdis_know:
        $ wdis_know.append("Talk_How_Regen") # Regen 1/6 Talk_How
    if sum(1 for buceta in wdis_know if buceta == "Talk_How_Regen") >= 8:
        $ wdis_know.remove("Talk_How") # Regen 1 Talk_How
        while "Talk_How_Regen" in wdis_know:
            $ wdis_know.remove("Talk_How_Regen") # Regen 1 Talk_How

    # HPRV 
    if "Talk_How" in hprv_know:
        $ hprv_know.append("Talk_How_Regen") # Regen 1/6 Talk_How
    if sum(1 for buceta in hprv_know if buceta == "Talk_How_Regen") >= 8:
        $ hprv_know.remove("Talk_How") # Regen 1 Talk_How
        while "Talk_How_Regen" in hprv_know:
            $ hprv_know.remove("Talk_How_Regen") # Regen 1 Talk_How

    # -----------------------------------------------------------------------------------------------
    # Randomize Action ID
    # -----------------------------------------------------------------------------------------------
    if renpy.random.random() >= 0.0:
        $ hriv_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ hprv_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ hine_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ wmom_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ wsis_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ wnei_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ wcou_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ wgma_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ wpre_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ wgal_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ wdis_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ wota_act[0] = renpy.random.random()

    if renpy.random.random() >= 0.0:
        $ wric_act[0] = renpy.random.random()

    return
