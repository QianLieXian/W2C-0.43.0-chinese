# ----------------------------------------------------------------------------------------------------
# DATABASE
# ----------------------------------------------------------------------------------------------------
define date_score = ("rom", "fun", "spi")

define date_score_ui = {
    "rom" : ("Romance", "images/UI/ICON_StatLove.webp", "#FF325B"),
    "fun" : ("Fun",     "images/UI/ICON_StatCha.webp",  "#FFAF32"),
    "spi" : ("Spice",   "images/UI/ICON_StatLust.webp", "#FF32FF"),
}

define date_map = {

    "shopping" : {
        "name"     : "Shopping Mall",
        "map_main" : "shopping",
        "map_sub"  : "facade",
        "open"     : (10, 22),
    },

    # "beach" : {
        # "name"     : "Beach",
        # "map_main" : "beach",
        # "map_sub"  : "shore",
        # "open"     : (10, 20),
    # }
}


# Activities offered at each venue. id / name / time (min) / cost ($) / label / once / score {axis: points}.
# `score` is the activity's flat payout, banked by `date_spend`; the beats inside each label pay their own points on top through `add_stat`.
define date_acts = {

    "shopping" : [

        {   "id"    : "cinema",
            "name"  : "Watch a movie",
            "time"  : 120,
            "cost"  : 30,
            "label" : "date_shop_cinema",
            "once"  : True,
            "score" : {"rom": 8, "fun": 6, "spi": 2},
        },

        {   "id"    : "clothing",
            "name"  : "Look around the clothing store",
            "time"  : 60,
            "cost"  : 0,
            "label" : "date_shop_clothing",
            "once"  : True,
            "score" : {"rom": 3, "fun": 5, "spi": 4},
        },

        {   "id"    : "food",
            "name"  : "Eat at the food court",
            "time"  : 60,
            "cost"  : 25,
            "label" : "date_shop_food",
            "once"  : True,
            "score" : {"rom": 6, "fun": 4, "spi": 1},
        },

        {   "id"    : "photo",
            "name"  : "Take a photo at the photo stall",
            "time"  : 60,
            "cost"  : 15,
            "label" : "date_shop_photo",
            "once"  : True,
            "score" : {"rom": 5, "fun": 7, "spi": 2},
        },
    ],
}

# Per-girl activities at a venue, for a date whose hub is her own (WNEI's stores). Same fields as `date_acts`.
define date_acts_char = {

    "wnei" : [

        {   "id"    : "stationery",
            "name"  : "Look around the stationery store",
            "time"  : 60,
            "cost"  : 0,
            "label" : "date_wnei_stationery",
            "once"  : True,
            "score" : {"rom": 2, "fun": 8, "spi": 0},
        },

        {   "id"    : "fashion",
            "name"  : "Look around the fashion store",
            "time"  : 60,
            "cost"  : 0,
            "label" : "date_wnei_fashion",
            "once"  : True,
            "score" : {"rom": 4, "fun": 5, "spi": 4},
        },
    ],
}

# ----------------------------------------------------------------------------------------------------
# TUNABLES
# ----------------------------------------------------------------------------------------------------
define DATE_SWIMSUIT_COST = 100      # the bikini HERO buys her at the clothing store — the beach date's gate

define TRYON_LAYERS = ["body", "wear", "face", "hair", "glasses"]   # fitting-room draw order, back to front
define TRYON_FACE_FALLBACK = ["o0", "s0"]   # a pose only has a couple of faces drawn; an unavailable one falls back through these
define TRYON_ZOOM = 0.5625      # the fitting-room art is 1080x1920 on a 1920x1080 screen, so full height is 1080/1920
define TRYON_XPOS = 960     # where she stands in the frame (centre of the fitting room)

define DATE_PHOTO_PICK = {
    "bg color_red"    : {"rom": 1},
    "bg color_pink"   : {"rom": 0.5, "spi": 0.5},
    "bg color_blue"   : {"rom": 0.5, "fun": 0.5},
    "bg color_green"  : {"rom": 0.25, "fun": 0.75},
    "bg color_yellow" : {"fun": 1},

    "fg heart"        : {"rom": 3},
    "fg lace"         : {"spi": 3},
    "fg music"        : {"fun": 3},
    "fg None"         : {"fun": 1, "rom": 1, "spi": 1},

    "hero_face 1"     : {"rom": 1},
    "hero_face 2"     : {"fun": 1},
}

# ----------------------------------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------------------------------
init python:

    # --------------------------------------------------
    def Date_VenueOpen(map_id): # Is the venue still accepting a date at this hour?
    # --------------------------------------------------
        first, last = date_map[map_id]["open"]
        return first <= gametimehour <= last

    # --------------------------------------------------
    def Date_ActList(map_id=None): # Activities still available at this venue on this date
    # --------------------------------------------------
        out = []
        for act in date_acts.get(map_id or date_venue, []) + date_acts_char.get(date_char, []):
            if act.get("once", False) and act["id"] in date_done:
                continue
            out.append(act)
        return out

    # --------------------------------------------------
    def Date_Act(act_id, map_id=None): # One activity entry, by id
    # --------------------------------------------------
        for act in date_acts.get(map_id or date_venue, []) + date_acts_char.get(date_char, []):
            if act["id"] == act_id:
                return act
        return None

    # --------------------------------------------------
    def Date_CanAfford(act): # Money check, kept apart so the menu can grey the option instead of hiding it
    # --------------------------------------------------
        return money >= act.get("cost", 0)

    # --------------------------------------------------
    def Date_UnlockDressy(char_id): # Dating unlocks the "dressy" style for HERO and his date, once
    # --------------------------------------------------
        # Gated on the sprite existing, so a character with no such art is never dressed up instead of rendering as a body wearing nothing.
        for who in ("hero", char_id):
            wear_list = getattr(store, who + "_achiev_wear", None)
            if wear_list is None or "dressy" in wear_list:
                continue
            if renpy.loadable("images/Sprite/%s/%s body_wear dressy.webp" % (who, who)):
                wear_list.append("dressy")
        return

    # --------------------------------------------------
    def Date_Bg(name, fallback): # A venue background, falling back to one that exists
    # --------------------------------------------------
        # Same shape as Sit_Room/Circle_Venue: ask for the specific art, use what ships until it is drawn.
        return name if renpy.has_image(name, exact=True) else fallback

    # --------------------------------------------------
    def Shop_Img(name): # Clothing-store version of a grocery-store shot, if it has been drawn
    # --------------------------------------------------
        # The clothing store replays the Day-1 grocery blocking, so every shot is asked for under its own name first and only falls back to the grocery original. Dropping `sd1_clothingstore_<n>_*.webp` in swaps that shot over with no code change. NOTE: this naming follows the old Day-1 scheme and is due a rework — see Status.md.
        alt = name.replace("sd1_grocerystore_", "sd1_clothingstore_")
        return alt if renpy.has_image(alt, exact=True) else name

    # --------------------------------------------------
    def Shop_Show(name, tag): # A store layer, plus the dressy repaint that covers it when she is dressed up
    # --------------------------------------------------
        # STOPGAP, deliberately (see Status.md > To Do). The store art is not split into outfit layers: a `<name>_dressy` file is a full repaint of the same shot that simply sits ON TOP of the casual one. Pairing them here means every shot follows the same rule and the overlay can never be left behind when she is not dressed up.
        renpy.show(Shop_Img(name), tag=tag)

        over = Shop_Img(name + "_dressy")
        if wsis_wear == "dressy" and renpy.has_image(over, exact=True):
            renpy.show(over, tag=tag + "_dressy")
        else:
            renpy.hide(tag + "_dressy")
        return

    # --------------------------------------------------
    def TryOn_Show(pose, wear=None, face=None): # Fitting-room shot, composed from whichever layers exist
    # --------------------------------------------------
        # Layers are `action_tryon_<char>_<pose>_<part>` in images/Action/Changing/. Every part is optional: pose 3 has no wear layer drawn yet, so it simply renders without one instead of crashing.
        # The art is 1080x1920 on a 1920x1080 screen, so every layer goes up through one Transform — without it only her legs are on screen.
        base = "action_tryon_wsis_" + str(pose) + "_"
        at = Transform(zoom=TRYON_ZOOM, xalign=0.5, xpos=TRYON_XPOS, yalign=1.0, ypos=1.0)
        for i, part in enumerate(TRYON_LAYERS):
            # A pose only has a couple of faces drawn, so an unavailable one falls back instead of leaving her faceless.
            if part == "face":
                names = [base + part + " " + f for f in ([face] if face else []) + TRYON_FACE_FALLBACK]
            elif part == "wear":
                names = [base + part + " " + wear] if wear else []
            else:
                names = [base + part]
            renpy.hide("tryon_" + part)
            for name in names:
                if renpy.has_image(name, exact=True):
                    renpy.show(name, tag="tryon_" + part, zorder=10 + i, at_list=[at])
                    break
        return

    # --------------------------------------------------
    def TryOn_Hide(): # Clear every fitting-room layer
    # --------------------------------------------------
        for part in TRYON_LAYERS:
            renpy.hide("tryon_" + part)
        return


# ----------------------------------------------------------------------------------------------------
# SCREEN
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
screen Date_UI(): # Score Panel
# ----------------------------------------------------------------------------------------------------

    zorder 90

    vbox:
        #xalign 0.5
        xpos 25
        ypos 25
        spacing 15

        frame:
            background "#00000064"
            xpadding 25
            ypadding 25

            hbox:
                spacing 25

                imagebutton at Zoom_04:
                    idle At("images/UI/SUBMENU_GalleryHide.webp" if date_hud else "images/UI/SUBMENU_GalleryShow.webp", outline_transform(5, "#FFF", 5.0))
                    hover At("images/UI/SUBMENU_GalleryShow.webp" if date_hud else "images/UI/SUBMENU_GalleryHide.webp", outline_transform(5, "#FFF", 5.0))
                    action ToggleVariable("date_hud")
                    yalign 0.5

                if date_hud:
                    # Icon, name and value sit ON the bar, the way the Character Menu draws a stat: the frame holds no box, so the text simply stacks over the bar it belongs to.
                    for axis in date_score:
                        $ axis_name, axis_icon, axis_color = date_score_ui[axis]
                        $ axis_pct = getattr(store, "date_" + axis)
                        $ axis_text = "{image=%s} %s: %s%%" % (axis_icon, axis_name, axis_pct)
                        frame:
                            background None
                            xsize 400
                            ysize 100
                            xpadding 0
                            ypadding 0
                            yalign 0.5
                            bar:
                                value axis_pct
                                range 100
                                xmaximum 400
                                ymaximum 100
                                left_bar Solid(axis_color)
                                right_bar Solid("#FFFFFF32")
                            text axis_text size 40 xalign 0.0 yalign 0.5 xpos 15 outlines [(2, "#191919", 0, 0)]
                    frame:
                        background None
                        xsize 400
                        ysize 100
                        xpadding 0
                        ypadding 0
                        yalign 0.5
                        bar:
                            # Clamped both ways: a 0 range (broke on arrival) or a value above it renders a NaN width and crashes.
                            value min(money, max(date_money, 1))
                            range max(date_money, 1)
                            xmaximum 400
                            ymaximum 100
                            left_bar Solid("#32FF32")
                            right_bar Solid("#FFFFFF32")
                        text renpy.translate_string("Money: $[money]") size 40 xalign 0.0 yalign 0.5 xpos 15 outlines [(2, "#191919", 0, 0)]

# ----------------------------------------------------------------------------------------------------
# SCENE
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
label date_invite(char_id="wsis", map_id="shopping"): # Intro
# ----------------------------------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_138

    if map_id == "shopping":

        hero "Are you free today?{w=[wt2]} Let's go to the [C_Dat]Shopping[C_Off] together."

        if char_id == "wsis":

            if wsis_love >= 40:
                $ wsis_mood = "O1"
                wsis "Out?{w=[wt2]} With you?{w=[wt4]} {aw}Hmph...!{/aw}{w=[wt2]} Fine.{w=[wt2]} It's not like I have plans or anything better to do."

            else:
                $ wsis_mood = "O1"
                wsis "Why would I go out with you in a date?{w=[wt3]} {aw}Hmph...!{/aw}"
                $ msg.msg(renpy.translate_string("Requires 50% love"))
                return

        elif char_id == "wnei":
            $ wnei_mood = "A1"
            wnei "{bt}YAAAY!!!{/bt}{w=[wt3]} Out together?!{w=[wt2]} Let me get my shoes!"

    scene bg_0 with dissolve
    $ hero_wear = "dressy"
    $ Date_UnlockDressy(char_id)
    if char_id == "wsis":
        $ StartAct("wsis", (("changing", "dressy"), 0), True)
        $ StartAct("wsis", (("staying", "living_room"), 0), True)
        $ wsis_wear = "dressy"
    call goto_shopping_facade from _call_goto_shopping_facade_1
    $ gametimemin += 30
    call action_walk(a="hero", b=char_id, c=30) from _call_action_walk_1
    call date_intro(char_id, map_id) from _call_date_intro

    jump show_ui # Fallback

# ----------------------------------------------------------------------------------------------------
label date_intro(char_id="wsis", map_id="shopping"): # Intro
# ----------------------------------------------------------------------------------------------------

    if char_id == None or map_id == None:
        $ date_active = False
        $ date_char = None
        $ date_venue = None
        $ date_done = []
        $ date_rom = 0.0
        $ date_fun = 0.0
        $ date_spi = 0.0
        $ date_rom_bonus = 0.0
        $ date_fun_bonus = 0.0
        $ date_spi_bonus = 0.0
        $ date_hud = True

    else:
        $ date_active = True
        $ date_char = char_id
        $ date_venue = map_id
        $ date_done = []
        $ date_rom = 0.0
        $ date_fun = 0.0
        $ date_spi = 0.0
        $ date_rom_bonus = 0.0
        $ date_fun_bonus = 0.0
        $ date_spi_bonus = 0.0
        $ date_hud = True
        $ group_follow.append(char_id)

    $ date_money = money

    if char_id == "wnei":
        scene bg_shopping_facade
        show WNEI at RC
        show HERO at LC
        with Fade(1, 0, 2)
        call goto_shopping_facade from _call_goto_shopping_facade_3

        $ wnei_mood = "A1"
        wnei "Woooah...!{w=[wt3]} It's so big!{w=[wt2]} Where do we go first, [C_Nam][fnamehero][C_Off]?"

        $ hero_mood = "A1"
        hero "Let's get in!"

        jump date_wnei_hub

    scene bg_shopping_facade
    show WSIS at RC
    show HERO at LC
    with Fade(1, 0, 2)
    call goto_shopping_facade from _call_goto_shopping_facade_2

    $ wsis_mood = "A1"
    wsis "So{w=[wt2]}, we're here.{w=[wt3]} What now, [C_Nam][wsis_to_hero][C_Off]?"

    $ hero_mood = "A1"
    hero "Let's get in!"

    $ date_activity_shop_photo = 0
    $ date_activity_shop_cinema = 0
    $ date_activity_shop_clothing = 0
    $ date_activity_shop_food = 0

    jump date_shop_hub

# ----------------------------------------------------------------------------------------------------
label date_shop_hub:
# ----------------------------------------------------------------------------------------------------

    $ a_event_0 = max([date_rom, date_fun, date_spi])

    if a_event_0 >= 85 and a_event_0 == date_spi:
        $ wsis_fx = 2
        $ wsis_mood = "A1"

    elif a_event_0 >= 85 and a_event_0 == date_rom:
        $ wsis_fx = 1
        $ wsis_mood = "A1"

    elif a_event_0 >= 85 and a_event_0 == date_fun:
        $ wsis_fx = 0
        $ wsis_mood = "A1"

    elif a_event_0 >= 50 and a_event_0 == date_spi:
        $ wsis_fx = 1
        $ wsis_mood = "A1"
        
    elif a_event_0 >= 50 and a_event_0 == date_rom:
        $ wsis_fx = 0
        $ wsis_mood = "A1"

    elif a_event_0 >= 50 and a_event_0 == date_fun:
        $ wsis_fx = 0
        $ wsis_mood = "A1"

    else:
        $ wsis_fx = 0
        $ wsis_mood = "O1"

    scene bg_shopping_hall
    show WSIS at RC
    show HERO at LC
    show screen Date_UI
    with Fade(1,0,2)
    
    label date_shop_hub_menu:
        pass

    menu:

        "Photo Stall ([C_Dat]$20[C_Off])" if date_activity_shop_photo < 1:
            if money >= 20:
                call date_shop_photo from _call_date_shop_photo
            else:
                $ msg.msg(renpy.translate_string("No enough money"))
                jump date_shop_hub_menu

        "Cinema ([C_Dat]$50[C_Off])" if date_activity_shop_cinema < 1:
            if money >= 50:
                call date_shop_cinema from _call_date_shop_cinema
            else:
                $ msg.msg(renpy.translate_string("No enough money"))
                jump date_shop_hub_menu

        "Clothing Store" if date_activity_shop_clothing < 1:
            call date_shop_clothing from _call_date_shop_clothing

        "Food Court":
            call date_shop_food from _call_date_shop_food

        "Finish":
            call date_end(date_char or "wsis", "shopping", False) from _call_date_end

    jump date_shop_hub

# ----------------------------------------------------------------------------------------------------
label date_shop_cinema:
# ----------------------------------------------------------------------------------------------------

    $ gametimemin += 120
    $ Set_CharMap("hero", "shopping", "cinema_entrance")
    $ Set_CharMap(date_char, "shopping", "cinema_entrance")

    scene bg_shopping_cinema_entrance
    show HERO at RC
    show WSIS at RR
    with Fade(1, 0, 2)

    hero "Two tickets{w=[wt2]}, please."

    $ wsis_mood = "O1"
    wsis "You're really paying for mine?{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I mean{w=[wt1]}, obviously you are.{w=[wt2]} You invited me."

    $ a_event_3 = "hero"

    $ wsis_mood = "A1"
    wsis "What's even on?"

    menu:
        "The action one [C_Drk](started forty minutes ago)[C_Off]" if 0 > 1:
            pass

        "The romance one [C_Drk](sold out)[C_Off]" if 0 > 1:
            pass

        "The horror one [C_Dat](starting now)[C_Off]":
            $ a_event_1 = "horror"
            hero "That one.{w=[wt2]} Screen 4{w=[wt2]}, it starts in ten minutes."

    $ money -= 50

    call wsis_movie_horror_1(False) from _call_wsis_movie_horror_1

    $ _pop = False

    menu:
        "Buy popcorn to share [C_Itm]($10)[C_Off]" if money >= 10:
            $ money -= 10
            $ _pop = True
            $ add_stat(date_char, "date_rom", 3)
            $ add_stat(date_char, "date_fun", 3)

            $ wsis_mood = "A1"
            wsis "One bucket?{w=[wt3]} For{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} both of us?"

            hero "Sharing is cheaper."

            $ wsis_mood = "O1"
            $ wsis_fx = 1
            wsis "Tsk.{w=[wt2]} Cheapskate.{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Fine."

        "Just find our seats":
            $ add_stat(date_char, "date_fun", 1)
            wsis "Good{w=[wt2]}, the trailers already started."

    call wsis_movie_sprites("shopping_cinema", _pop) from _call_wsis_movie_sprites

    "The lights go down.{w=[wt3]} The screen fills the room{w=[wt2]}, and for a moment the whole mall stops existing."

    if _pop:
        $ wsis_fx = 1
        wsis "{size=-10}Hey.{w=[wt2]} That was my piece.{/size}"
        hero "{size=-10}It's a shared bucket.{/size}"
        wsis "{size=-10}It's a shared bucket with {b}rules{/b}.{/size}"
        $ add_stat(date_char, "date_rom", 2)
        $ add_stat(date_char, "date_fun", 3)

    else:
        wsis "{size=-10}Everyone else brought snacks.{w=[wt2]} I want you to know I noticed.{/size}"
        $ add_stat(date_char, "date_fun", 1)

    mind "(She hasn't looked at her phone once.{w=[wt3]} At home she'd have paused this twice by now.)"

    $ wsis_mood = "A1"
    wsis "{size=-10}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Okay, that part was actually good.{w=[wt3]} Don't tell anyone I said that.{/size}"

    $ add_stat(date_char, "date_rom", 3)
    $ add_stat(date_char, "date_fun", 2)

    # The movie itself is the home movie's loop, popcorn state handed over from the counter purchase.
    call wsis_movie_loop(_pop) from _call_wsis_movie_loop

    scene bg_shopping_hall
    show HERO at LC
    show WSIS at RC
    with Fade(1, 0, 2)

    $ wsis_mood = "A1"
    wsis "Not bad.{w=[wt2]} The ending was predictable{w=[wt2]}, but not bad."

    if _pop:
        $ wsis_fx = 1
        wsis "And you ate most of the popcorn{w=[wt2]}, so you're buying next time.{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Next time.{w=[wt2]} I said that out loud, didn't I."

    # ----------------------------------------------------------------------------------------------------
    if "Date_Cinema" not in wsis_know:
        $ wsis_know.append("Date_Cinema")

    #call date_spend("cinema")
    $ date_activity_shop_cinema = 1
    $ Set_CharMap("hero", "shopping", "hall")
    $ Set_CharMap(date_char, "shopping", "hall")
    return
    # ----------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------
label date_shop_clothing:
# ----------------------------------------------------------------------------------------------------

    $ gametimemin += 30
    $ Set_CharMap("hero", "shopping", "store_clothing")
    $ Set_CharMap(date_char, "shopping", "store_clothing")

# ----------------------------------------------------------------------------------------------------
label date_shop_clothing_entrance: # 1 - Coming in through the automatic doors
# ----------------------------------------------------------------------------------------------------
    scene expression Shop_Img("sd1_grocerystore_4_bg")
# ----------------------------------------------------------------------------------------------------
    $ Shop_Show("sd1_grocerystore_4_wsis 1", "store_wsis")
    with Fade(1, 0, 2)

    mind "(Whooa{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} This store seems so fancy!{w=[wt3]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} But I didn't know a shop could have this many {i}shelves{/i} of the same thing.{w=[wt3]} Four walls of jackets and not one price tag I can read without squinting.{w=[wt3]} Maybe that's the price of extravagance.)"

    $ Shop_Show("sd1_grocerystore_4_wsis 2", "store_wsis")
    $ Shop_Show("sd1_grocerystore_4_wsis_face o1", "store_face")
    with dissolve
    wsis "Do you know why automatic doors exist?{w=[wt4]} So no idiot leaves them open.{w=[wt2]} And it seems that's not the case here!{w=[wt3]} Are you goinna stand there all day or actually come in?"

    hero "S{w=[wt1]}-sorry!{w=[wt2]} I'm going!{w=[wt3]} [C_Mnd](Ehhh...!?{w=[wt3]} So it wasn't a leprechaun who opened it?)[C_Off]"

    #$ Shop_Show("sd1_grocerystore_4_wsis_face o0", "store_face")

# ----------------------------------------------------------------------------------------------------
label date_shop_clothing_shoes: # 2 - The shoe shelf. She crouches to reach it, he looks down at her.
# ----------------------------------------------------------------------------------------------------
    scene expression Shop_Img("sd1_grocerystore_7_bg")
    $ Shop_Show("sd1_grocerystore_7_wsis_body", "store_wsis")
    $ Shop_Show("sd1_grocerystore_7_wsis_fg 1", "store_fg")
    with Fade(1, 0, 2)

    wsis "Look at these shoes!{w=[wt3]} They look so beautiful!{w=[wt3]} What do you think?"

    hero "[C_Mnd](From up here{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I have no complaints about the bottom shelf ❤)[C_Off].{w=[wt3]} Yeah{w=[wt2]}, it's a beautiful view, right?"

    wsis "My old ones are almost falling apart.{w=[wt2]} What do you think of the shape of this pair here?"

    hero "The shape is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} really good.{w=[wt3]} Round where it should be round{w=[wt2]}, and it curves in at exactly the right place."

    wsis "That's a lot of words."

    hero "You asked for an honest opinion.{w=[wt3]} I cannot even take my eyes out of it."

    $ Shop_Show("sd1_grocerystore_7_wsis_fg 3", "store_fg")
    $ Shop_Show("sd1_grocerystore_7_wsis_face o0", "store_face")
    with dissolve

    $ Shop_Show("sd1_grocerystore_7_wsis_face o1", "store_face")
    wsis "This one's my size, I guess.{w=[wt3]} How does the fit look from there?"

    $ Shop_Show("sd1_grocerystore_7_wsis_fg 2", "store_fg")
    $ Shop_Show("sd1_grocerystore_7_wsis_face o0", "store_face")
    hero "Snug.{w=[wt3]} Very snug.{w=[wt2]} It's holding the whole line without squeezing anything{w=[wt2]}, which is honestly hard to find."

    $ Shop_Show("sd1_grocerystore_7_wsis_face o1", "store_face")
    wsis "{bt}Mmm.{/bt}{w=[wt3]} And the back?{w=[wt2]} The back always slips on me."

    scene expression Shop_Img("sd1_grocerystore_7_bg")
    $ Shop_Show("sd1_grocerystore_7_wsis_body", "store_wsis")
    $ Shop_Show("sd1_grocerystore_7_wsis_fg 1", "store_fg")
    with dissolve

    hero "The back is the best part."

    scene expression Shop_Img("sd1_grocerystore_7_bg")
    $ Shop_Show("sd1_grocerystore_7_wsis_body", "store_wsis")
    $ Shop_Show("sd1_grocerystore_7_wsis_fg 2", "store_fg")
    $ Shop_Show("sd1_grocerystore_7_wsis_face o0", "store_face")
    with dissolve

    $ Shop_Show("sd1_grocerystore_7_wsis_face o1", "store_face")
    wsis "{aw}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} You're not looking at the shoes.{/aw}"

    $ Shop_Show("sd1_grocerystore_7_wsis_face o0", "store_face")
    hero "I'm looking at the shoes."

    with dissolve
    $ Shop_Show("sd1_grocerystore_7_wsis_face o1", "store_face")

    wsis "Say {i}shoes{/i} one more time{w=[wt2]}, and I'm putting mine in your face!"

    hero "Okay.{w=[wt2]} No more shoes.{w=[wt2]} I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} No more{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} uh{w=[wt2]}, t{w=[wt1]}-that word!"

    wsis "{aw}Ugh!{/aw}{w=[wt3]} Just come down here and tell me what you think!"

    $ add_stat(date_char, "date_rom", 2)
    $ add_stat(date_char, "date_fun", 3)
    $ add_stat(date_char, "date_spi", 5)

# ----------------------------------------------------------------------------------------------------
label date_shop_clothing_lowangle: # 3 - She stands, he is the one crouched now. Low angle.
# ----------------------------------------------------------------------------------------------------
    scene expression Shop_Img("sd1_grocerystore_8_bg")
# ----------------------------------------------------------------------------------------------------
    $ Shop_Show("sd1_grocerystore_8_wsis_bg", "store_wsis")
    $ Shop_Show("sd1_grocerystore_8_wsis_mouth o0", "store_mouth")
    $ Shop_Show("sd1_grocerystore_8_wsis_fg", "store_fg")
    with fade

    pause

    $ Shop_Show("sd1_grocerystore_8_wsis_mouth o1", "store_mouth")
    wsis "So...?"

    $ Shop_Show("sd1_grocerystore_8_wsis_mouth o0", "store_mouth")
    hero "I think we have a very beautiful pair here.{w=[wt3]} It's clearly visible just how beautiful and sharp they are.{w=[wt3]} Just look at that shine!{w=[wt3]} It's mouth-watering.{w=[wt3]} I{w=[wt1]}-I mean{w=[wt2]}, you can even picture how cool someone would look wearing them."

    $ Shop_Show("sd1_grocerystore_8_wsis_mouth o1", "store_mouth")
    wsis "You're not even looking at the shoes!{w=[wt3]} {aw}Hmph...!{/aw}{w=[wt3]} Let's look at the clothes!"

    if "Date_Clothing" not in wsis_know:
        $ wsis_know.append("Date_Clothing")

# ----------------------------------------------------------------------------------------------------
label date_shop_clothing_swimsuit: # 5 - The swimsuit talk, and the fitting room (beach-date gate)
# ----------------------------------------------------------------------------------------------------
    scene expression Shop_Img("sd1_grocerystore_5_bg")
# ----------------------------------------------------------------------------------------------------
    $ Shop_Show("sd1_grocerystore_5_wsis_body", "store_wsis")
    $ Shop_Show("sd1_grocerystore_5_wsis_head 1", "store_head")
    with Fade(1, 0, 2)

    $ _tries = 1
    $ _bought = False
    $ Shop_Show("sd1_grocerystore_5_wsis_body", "store_wsis")
    $ Shop_Show("sd1_grocerystore_5_wsis_head 1", "store_head")
    with Fade(1, 0, 2)

    $ wsis_mood = "O2"
    wsis "Can I admit something?{w=[wt3]} I don't actually have no idea how to chose clothes.{w=[wt3]} My clothes are the same from teenager, since they're still good in me.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'll kill you if you laugh!"

    hero "{aw}I{w=[wt1]}-I wont!{/aw}{w=[wt4]} W{w=[wt1]}-well{w=[wt2]}, so start from the other end.{w=[wt2]} What do you actually need something {i}for{/i}?"

    $ Shop_Show("sd1_grocerystore_5_wsis_head 2", "store_head")
    $ Shop_Show("sd1_grocerystore_5_wsis_face o0", "store_face")
    with dissolve

    $ Shop_Show("sd1_grocerystore_5_wsis_face o1", "store_face")
    wsis "Like what?"

    $ Shop_Show("sd1_grocerystore_5_wsis_face o0", "store_face")
    hero "A party.{w=[wt2]} A wedding.{w=[wt2]} Sports day{w=[wt2]}, if you ever ran anywhere on purpose."

    $ Shop_Show("sd1_grocerystore_5_wsis_face o1", "store_face")
    wsis "I run!{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt2]} When something's chasing me."

    $ Shop_Show("sd1_grocerystore_5_wsis_face o0", "store_face")

    if "Talk_NoSwimsuit" in wsis_know:
        hero "You said you didn't have a swimsuit any more.{w=[wt2]} A real one{w=[wt2]}, not the school one."

        $ Shop_Show("sd1_grocerystore_5_wsis_face o1", "store_face")
        wsis "You {b}remembered{/b} that?{w=[wt3]} That was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} that was one sentence, months ago."

    else:
        hero "The beach, then.{w=[wt2]} Summer's coming."

        $ Shop_Show("sd1_grocerystore_5_wsis_face o1", "store_face")
        wsis "Yeah{w=[wt2]}, I don't have one.{w=[wt3]} A swimsuit, I mean.{w=[wt2]} A real one.{w=[wt3]} The school one doesn't count and I'm not wearing {i}that{/i} in public."

        $ wsis_know.append("Talk_NoSwimsuit")

    $ Shop_Show("sd1_grocerystore_5_wsis_face o0", "store_face")
    hero "Then that's what we're here for.{w=[wt2]} Pick one you like{w=[wt2]}, I'll get it."

    $ Shop_Show("sd1_grocerystore_5_wsis_face o1", "store_face")
    wsis "Absolutely not.{w=[wt3]} Do you know what that {i}means{/i}, you buying me a{w=[wt1]}-{w=[wt1]}{w=[wt2]} no."

    $ Shop_Show("sd1_grocerystore_5_wsis_face o0", "store_face")
    hero "It means you can come to the beach without borrowing something that doesn't fit."

    $ Shop_Show("sd1_grocerystore_5_wsis_face o1", "store_face")
    wsis "It means you'd have {b}bought{/b} it.{w=[wt3]} And every single time I wore it I'd be thinking about that."

    $ Shop_Show("sd1_grocerystore_5_wsis_face o0", "store_face")
    hero "Then think about it at the beach instead of at home."

# ----------------------------------------------------------------------------------------------------
label date_shop_clothing_aisle: # 4 - WSIS tries to pass but HERO is blocking the path, so they're too close
# ----------------------------------------------------------------------------------------------------
    scene expression Shop_Img("sd1_grocerystore_6_bg")
# ----------------------------------------------------------------------------------------------------
    $ Shop_Show("sd1_grocerystore_6_fg", "store_fg")
    with vpunch

    wsis "Ugh!{w=[wt2]} Fine!{w=[wt2]} I'll try {b}one{/b}!{w=[wt3]} {aw}Just get out of the way already!!!{/aw}"

    $ add_stat(date_char, "date_rom", 6)
    $ add_stat(date_char, "date_fun", 2)
    $ add_stat(date_char, "date_spi", 4)

# ----------------------------------------------------------------------------------------------------
label date_shop_clothing_fitting: # 5 - The fitting room. `_1_bg` is the open stall, `_0_bg` the closed one.
# ----------------------------------------------------------------------------------------------------
    scene sd1_clothingstore_1_bg
    $ TryOn_Show(1, "dressy", "o0")
    with Fade(1, 0, 2)

    wsis "Wait out here.{w=[wt3]} And I mean {i}out{/i} here{w=[wt2]}, not leaning on the curtain."

    # Curtain closed: she is behind it, so every try-on layer comes off and only her voice is left.
    scene sd1_clothingstore_0_bg
    $ TryOn_Hide()
    with dissolve

    "The curtain rattles shut.{w=[wt3]} Hangers click.{w=[wt3]} A long, suspicious silence."

    $ wsis_mood = "O2"
    wsis "{size=-10}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} This is so much less fabric than I expected.{/size}"

    hero "Is that a bad thing?"

    wsis "{size=-10}It's an {b}observation{/b}.{/size}"

    # The curtain opens again — she comes out embarrassed, and pose 2 is the flustered one.
    scene sd1_clothingstore_1_bg
    $ TryOn_Show(2, "swim", "s0")
    with dissolve

    $ wsis_fx = 2
    wsis "Don't say anything yet.{w=[wt3]} I'm still deciding whether I'm keeping it on."

    hero "So{w=[wt2]}.{w=[wt2]}.{w=[wt2]} how is it?"

    $ _pose = 2
    $ _turned = False
    $ _asked_back = False

    label date_shop_tryon_loop:

        menu:
            "Ask her to stand properly so you can see it" if _pose != 1:
                $ _tries += 1

                hero "I can't see anything with you folded up like that.{w=[wt2]} Stand up."

                # She moves AFTER he asks, not before.
                $ TryOn_Show(1, "swim", "o1")
                with dissolve

                $ _pose = 1
                $ wsis_mood = "O1"
                wsis "Fine!{w=[wt3]} Fine.{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Well?{w=[wt3]} Say something before I lose my nerve."

                hero "It's the first thing all day that looks like it was made for you."

                $ TryOn_Show(1, "swim", "o0")
                $ wsis_fx = 2
                wsis ".{w=[wt1]}.{w=[wt1]}.{w=[wt2]} You're not allowed to just {i}say{/i} things like that with a straight face."

                $ add_stat(date_char, "date_rom", 1)
                $ add_stat(date_char, "date_spi", 5)
                jump date_shop_tryon_loop

            "Ask her to turn around":
                hero "Turn around a second."

                if stat_value(date_char, "inti") < char_inti_req_date + 10:
                    $ wsis_mood = "O1"
                    $ wsis_fx = 2
                    wsis "{aw}Absolutely not!{/aw}{w=[wt3]} You get the front{w=[wt2]}, and you get it because I'm {i}letting{/i} you."

                    hero "It was just a{w=[wt1]}-{w=[wt1]}{nw}"

                    wsis "I know what it was.{w=[wt3]} Ask me again when I like you more.{w=[wt2]} {size=-10}If that ever happens.{/size}"

                    if not _asked_back:
                        $ add_stat(date_char, "date_spi", 5)

                    $ _asked_back = True
                    jump date_shop_tryon_loop

                $ _tries += 1

                $ wsis_mood = "O2"
                wsis "{size=-10}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} You're going to look either way, aren't you.{/size}"

                $ TryOn_Show(3, "swim", "o0")
                with dissolve

                "She turns, slowly, and holds still with her arms crossed in front of her{w=[wt1]}—{w=[wt1]}which does nothing about the back."

                $ wsis_fx = 2
                wsis "{size=-10}Okay.{w=[wt3]} That's enough.{w=[wt2]} That is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} that's enough.{/size}"

                # Same guard: she can be asked again, but the day only pays for it once.
                if not _turned:
                    $ gametimemin += 20
                    $ add_stat(date_char, "date_rom", 1)
                    $ add_stat(date_char, "date_fun", 1)
                    $ add_stat(date_char, "date_spi", 20)
                $ _turned = True

                $ TryOn_Show(_pose, "swim", "o0")
                jump date_shop_tryon_loop

            "Buy it for her [C_Itm]($[DATE_SWIMSUIT_COST])[C_Off]" if money >= DATE_SWIMSUIT_COST:
                $ gametimemin += 20
                $ money -= DATE_SWIMSUIT_COST
                $ _bought = True

                hero "We're taking it."

                $ wsis_mood = "O2"
                $ wsis_fx = 1
                wsis "I didn't say{w=[wt1]}-{w=[wt1]}{w=[wt2]} you didn't even let me look at the {b}tag{/b}."

                hero "I looked at the tag."

                $ wsis_mood = "A2"
                wsis ".{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Thank you.{w=[wt3]} That's it.{w=[wt2]} That's all you're getting.{w=[wt3]} Don't make it weird."

                "She folds it back into the bag herself{w=[wt2]}, very carefully{w=[wt2]}, corners squared."

                $ add_stat(date_char, "date_rom", 25)
                $ add_stat(date_char, "date_fun", 25)
                $ add_stat(date_char, "date_spi", 25)

                python:
                    # Ownership lives in the style-unlock list: it puts the swimsuit in the Character Menu AND, through Outfits_For, into the laundry/chores system.
                    if "swim" not in wsis_achiev_wear:
                        wsis_achiev_wear.append("swim")
                    if "Own_Swimsuit" not in wsis_know:
                        wsis_know.append("Own_Swimsuit")
                    msg.msg(fnamewsis + renpy.translate_string(" got a swimsuit"))

            "Let her put her own clothes back on":
                $ wsis_mood = "A1"
                wsis "Good answer.{w=[wt3]} .{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'm remembering where it was, though.{w=[wt2]} That's all."
                $ add_stat(date_char, "date_rom", 1)
                $ add_stat(date_char, "date_fun", 1)
                $ add_stat(date_char, "date_spi", 1)

    # Curtain shut again while she changes back into her own clothes.
    scene sd1_clothingstore_0_bg
    $ TryOn_Hide()
    with dissolve

    "The curtain rattles shut.{w=[wt3]} A zip{w=[wt2]}, a hanger{w=[wt2]}, and a sigh she probably thought was quiet."

# ----------------------------------------------------------------------------------------------------
    scene expression Shop_Img("sd1_grocerystore_5_bg")
# ----------------------------------------------------------------------------------------------------
    $ Shop_Show("sd1_grocerystore_5_wsis_body", "store_wsis")
    $ Shop_Show("sd1_grocerystore_5_wsis_head 1", "store_head")
    with Fade(1, 0, 2)

    if _bought:
        $ wsis_mood = "A1"
        wsis "Right.{w=[wt3]} Where else are we going{w=[wt2]}, before I think too hard about what just happened."

    else:
        $ wsis_mood = "O1"
        wsis "That was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} not the worst hour of my life.{w=[wt3]} Don't let it go to your head."

    #call date_spend("clothing", _tries * 20)
    $ date_activity_shop_clothing = 1
    $ Set_CharMap("hero", "shopping", "hall")
    $ Set_CharMap(date_char, "shopping", "hall")
    return

# ----------------------------------------------------------------------------------------------------
# ACTIVITY — FOOD COURT (1h)
# ----------------------------------------------------------------------------------------------------
label date_shop_food:

    $ hero_mood = "A1"
    hero "Let's eat something!"

    $ wsis_mood = "A1"
    wsis "Now you're speaking my language.{w=[wt3]} I'm starving!"

    $ Set_CharMap("hero", "shopping", "court_food")
    $ Set_CharMap(date_char, "shopping", "court_food")

    scene bg_shopping_court_food
    show HERO at LL
    show WSIS at LL
    show WSIS at RC_slow
    show HERO at LC_heavy
    with Fade(1, 0, 2)

    $ hero_mood = "A1"
    $ wsis_mood = "A1"

    show HERO at OR_heavy
    hero "{bt}Whoooah...!{/bt}{w=[wt3]} So many things to eat!{w=[wt4]} What will I buy for me...?"

    wsis "Y{w=[wt1]}-you better don't forget me!{w=[wt3]} I'll be paying attention to what you'll buy!{w=[wt4]} Hey{w=[wt2]}, are you listening?"

    show HERO at OL
    show HERO at LC_heavy

    $ a_event_0 = 0 # loop
    $ a_event_1 = 0 # WSIS' food saciety points
    $ a_event_2 = 0 # HERO's food saciety points

    label date_shop_food_menu:
        pass

    while a_event_0 == 0:
        menu: # (yoffset=250)
            "{b}Saciety Points:{/b}{pr}{image=icon_wsis}: [a_event_1]{pr}{image=icon_hero}: [a_event_2]{fast}"

            "Hamburger ([C_Dat]$40[C_Off])" if money >= 40:
                while a_event_0 == 0 and money >= 40:
                    menu:
                        "{b}Saciety Points:{/b}{pr}{image=icon_wsis}: [a_event_1]{pr}{image=icon_hero}: [a_event_2]{fast}"

                        "Buy for {image=icon_wsis}, get points:{pr}[C_Pos]+5 Fun[C_Off], [C_Neg]-2 Spice[C_Off]":
                            $ add_stat(date_char, "date_fun", 5)
                            $ add_stat(date_char, "date_spi", -2)
                            $ gametimemin += 20
                            $ a_event_1 += 5
                            $ money -= 40

                        "Buy for {image=icon_hero}, get bonus:{pr}[C_Pos]+25%% Fun[C_Off], [C_Neg]-10%% Spice[C_Off]":
                            $ add_stat(date_char, "date_fun_bonus", 20)
                            $ add_stat(date_char, "date_spi_bonus", -10)
                            $ gametimemin += 20
                            $ a_event_2 += 5
                            $ money -= 40

                        "Return":
                            $ a_event_0 = 1

                $ a_event_0 = 0

            "Ice Cream ([C_Dat]$30[C_Off])" if money >= 30:
                while a_event_0 == 0 and money >= 30:
                    menu:
                        "{b}Saciety Points:{/b}{pr}{image=icon_wsis}: [a_event_1]{pr}{image=icon_hero}: [a_event_2]{fast}"
                        
                        "Buy for {image=icon_wsis}, get points:{pr}[C_Pos]+3 Romance[C_Off]":
                            $ add_stat(date_char, "date_rom", 3)
                            $ gametimemin += 16
                            $ a_event_1 += 4
                            $ money -= 30

                        "Buy for {image=icon_hero}, get bonus:{pr}[C_Pos]+15%% Romance[C_Off]":
                            $ add_stat(date_char, "date_rom_bonus", 15)
                            $ gametimemin += 16
                            $ a_event_2 += 4
                            $ money -= 30

                        "Return":
                            $ a_event_0 = 1

                $ a_event_0 = 0

            "Chocolate Bar ([C_Dat]$25[C_Off])" if money >= 25:
                while a_event_0 == 0 and money >= 25:
                    menu:
                        "{b}Saciety Points:{/b}{pr}{image=icon_wsis}: [a_event_1]{pr}{image=icon_hero}: [a_event_2]{fast}"
                        
                        "Buy for {image=icon_wsis}, get points:{pr}[C_Pos]+1 Spice[C_Off], [C_Pos]+1 Romance[C_Off]":
                            $ add_stat(date_char, "date_rom", 1)
                            $ add_stat(date_char, "date_spi", 1)
                            $ gametimemin += 12
                            $ a_event_1 += 3
                            $ money -= 25

                        "Buy for {image=icon_hero}, get bonus:{pr}[C_Pos]+5%% Spice[C_Off], [C_Pos]+5%% Romance[C_Off]":
                            $ add_stat(date_char, "date_rom_bonus", 5)
                            $ add_stat(date_char, "date_spi_bonus", 5)
                            $ gametimemin += 12
                            $ a_event_2 += 3
                            $ money -= 25

                        "Return":
                            $ a_event_0 = 1

                $ a_event_0 = 0

            "Water Bottle ([C_Dat]$15[C_Off])" if money >= 15:

                while a_event_0 == 0 and money >= 15:
                    menu:
                        "{b}Saciety Points:{/b}{pr}{image=icon_wsis}: [a_event_1]{pr}{image=icon_hero}: [a_event_2]{fast}"
                        
                        "Buy for {image=icon_wsis}, get points:{pr}[C_Pos]+1 Fun[C_Off]":
                            $ add_stat(date_char, "date_fun", 1)
                            $ gametimemin += 4
                            $ a_event_1 += 1
                            $ money -= 15

                        "Buy for {image=icon_hero}, get bonus:{pr}[C_Pos]+5%% Fun[C_Off]":
                            $ add_stat(date_char, "date_fun_bonus", 5)
                            $ gametimemin += 4
                            $ a_event_2 += 1
                            $ money -= 15

                        "Return":
                            $ a_event_0 = 1

                $ a_event_0 = 0

            "Continue":
                $ a_event_0 = 1

    label date_shop_food_eat:
        pass

    if a_event_1 == 0 and a_event_1 == a_event_2:
        wsis "What? Won't we eat anything?"

        if money > 10:
            hero "I changed my mind.{w=[wt2]} Maybe we can get back here later if we have time{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} And money."

        else:
            hero "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I realize I'm kinda out of money.{w=[wt4]} Nothing to buy here."

        jump date_shop_hub

    scene expression Date_Bg("sitting_bg shopping_foodcourt", "bg_shopping_court_food")
    show sitting_hero_body 2 at LC
    show expression Sit_Wear("sitting_hero_wear 2", "hero", "") as hero_sit_wear at LC
    show sitting_wsis_body 2 at RC
    show expression Sit_Wear("sitting_wsis_wear 2", "wsis", "") as wsis_sit_wear at RC
    show sitting_fg home_diningroom
    show fx_light
    with Fade(1, 0, 2)

    if a_event_1 == 0:
        $ add_stat(date_char, "love", -2)
        wsis "Hey, [C_Nam][wsis_to_hero][C_Off]!{w=[wt3]} Why did you bought that just for yourself?{w=[wt3]} You know don't have money to buy anything{w=[wt2]}, and yet{w=[wt2]}, you buy it just to eat it in front of me, didn't you?{w=[wt2]} Hurry up{w=[wt2]}, give me a little bit!"

    elif a_event_2 > a_event_1:
        $ add_stat(date_char, "love", -1)
        wsis "{aw}Hmph...!{/aw}{w=[wt2]} You bought the best for yourself just to eat it in front of me, didn't you?"

    elif a_event_1 >= 1 and a_event_1 == a_event_2:
        $ add_stat(date_char, "love", 1)
        wsis "Thank you, [C_Nam][wsis_to_hero][C_Off]!"

    elif a_event_1 > a_event_2:
        $ add_stat(date_char, "love", 2)
        wsis "[C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} W{w=[wt1]}-why does it seem like you care more about me than about yourself?"

    if money > 10:
        hero "Maybe we can get back here later if we have time{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} And money."

    else:
        hero "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm kinda out of money now{w=[wt2]}, so we won't be able to come back here today.{w=[wt3]} Let's make the most of it."

    $ date_activity_shop_food = 1
    $ add_stat(date_char, "eat", a_event_1*5)
    $ add_stat(hero, "eat", a_event_2*5)
    $ Set_CharMap("hero", "shopping", "hall")
    $ Set_CharMap(date_char, "shopping", "hall")

    jump date_shop_hub


# ----------------------------------------------------------------------------------------------------
label date_shop_photo: # Photo Stall
# ----------------------------------------------------------------------------------------------------

    $ gametimemin += 30
    $ hero_mood = "A1"

    hero "How about we capture this moment in that photo booth?"

    $ wsis_fx = 1
    if wsis_love >= 50:
        $ wsis_mood = "A1"
        wsis "W{w=[wt1]}-well{w=[wt2]}, if you want it that much.{w=[wt2]} I think I can take a photo with you."
        hero "So, let's go!{w=[wt2]} Hurry up!"

        show HERO at OR_slow

        wsis "{aw}Hmph...!{/aw}{w=[wt2]}{nw}"

        show WSIS at OR_slow

        wsis "{aw}Hmph...!{/aw}{w=[wt2]} Wait for me!{fast}"

    else:
        $ wsis_fx = 1
        wsis "{aw}Hmph...!{/aw}{w=[wt2]} Then what will you do with the photo?"
        hero "Come on!{w=[wt2]} We'll both have the photo!{w=[wt2]} Let's go!"

        show HERO at OR_slow

        wsis "{aw}Hmph...!{/aw}{w=[wt2]} Idiot...{nw}"

        show WSIS at OR_slow

        wsis "{aw}Hmph...!{/aw}{w=[wt2]} Idiot...{fast}"

    scene bg_shopping_photobooth
    show HERO at LL
    show WSIS at LL
    show HERO at LC_slow
    show WSIS at RC_slow
    with slideleft

    $ money -= 20

    $ wsis_mood = "O1"
    wsis "{aw}Ugh...!{/aw}{w=[wt2]} This booth is too narrow!{w=[wt3]} As if it was built for one person and a half."

    $ a_event_1 = 0 # Fun
    $ a_event_2 = 0 # Rom
    $ a_event_3 = 0 # Spi

    menu:
        "Act fun":
            hero "That's perfect!{w=[wt2]} We're a person and a half!"

            $ wsis_mood = "O3"
            wsis "{aw}What!?{/aw}"

            $ hero_mood = "A3"
            hero "{aw}N{w=[wt1]}-nothing...!{/aw}"

            $ wsis_mood = "O1"

            show WSIS with dissolve

            wsis "Say that again{w=[wt2]}, and I'll make you have only one tooth and a half."

            show HERO at Laugh
            $ hero_mood = "A4"
            hero "But for that, you'd need to reach my teeth!"

            $ wsis_mood = "O3"
            wsis "So those was your last words? I hope you've made the most of life so far!!"

            $ hero_mood = "A1"
            hide HERO
            show HERO at LC
            $ a_event_1 = 3
            $ add_stat(date_char, "date_fun", a_event_1)

        "Act romantic":
            hero "That doesn't matter.{w=[wt3]} It will become a good memory of us together."

            $ wsis_fx = 2
            wsis "Y{w=[wt1]}-you're right..."

            $ a_event_2 = 3
            $ add_stat(date_char, "date_rom", a_event_2)

        "Act spicy":
            hero "Looks perfect to me.{w=[wt2]} This way we can stay very close!"

            $ wsis_fx = 2
            wsis "{aw}Ugh...!{/aw}{w=[wt3]} Of course that was your plan, you pervert!"

            hero "Come on{w=[wt2]}, I don't bite.{w=[wt3]} At least{w=[wt2]}, not that hard."

            wsis "{aw}S{w=[wt1]}-stop that...!{/aw}"

            $ a_event_3 = 3
            $ add_stat(date_char, "date_spi", a_event_3)

    hero "Come on{w=[wt2]}, let's take a shot!{w=[wt2]} Look!{w=[wt2]} we can change the background as we want before shotting.{w=[wt3]} There are many options!{w=[wt4]} What do you prefer?"

    wsis "I{w=[wt1]}-I'll leave it for you."

    show HERO at PoseX_X(850, 1.0)
    show WSIS at PoseX_X(1050, 3.0)
    hero "Then let it with me!"

    call photobooth_run("heroandwsis_1") from _call_photobooth_run
    $ a_event_0 = _return

    # `photobooth_run` hands back the whole shot he composed — `id`, `bg`, `fg`, `picks["hero_face"]` — so the choices are read below, once the photo is on screen.

    if not a_event_0:
        $ wsis_mood = "O1"
        wsis "You're going to stand there fiddling with it until the machine gives up?"

        hero "It's harder than it looks."

        wsis "Let's get out then.{w=[wt3]} I won't be waiting you all the day here."

        jump date_shop_photo_end

    $ Photo_ShowShot(a_event_0["id"])

    hero "{bt}Cheeese!{/bt}"

    python:
        _acted = {"fun": a_event_1, "rom": a_event_2, "spi": a_event_3}
        _score = {"fun": 0.0, "rom": 0.0, "spi": 0.0}

        for _key in ("bg " + str(a_event_0["bg"]), "fg " + str(a_event_0["fg"]), "hero_face " + str(a_event_0["picks"].get("hero_face"))):
            for _axis, _pts in DATE_PHOTO_PICK.get(_key, {}).items():
                _score[_axis] += _pts * (1.0 + _acted[_axis] * 0.5)

        a_event_1 += _score["fun"]
        a_event_2 += _score["rom"]
        a_event_3 += _score["spi"]

# ----------------------------------------------------------------------------------------------------
label date_shop_photo_end: # End
# ----------------------------------------------------------------------------------------------------

    #call date_spend("photo")
    $ date_activity_shop_photo = 1
    $ add_stat(date_char, "date_fun", a_event_1)
    $ add_stat(date_char, "date_rom", a_event_2)
    $ add_stat(date_char, "date_spi", a_event_3)
    $ a_event_1 = 0 # Fun
    $ a_event_2 = 0 # Rom
    $ a_event_3 = 0 # Spi

    return

# ----------------------------------------------------------------------------------------------------
# Spend an activity: charge the money, advance the clock, bank the flat score, mark it done.
# Every activity label calls this, so the bookkeeping lives in exactly one place.
# ----------------------------------------------------------------------------------------------------
label date_spend(act_id, extra_time=0):

    python:
        _act = Date_Act(act_id)

        if _act:
            money -= _act.get("cost", 0)
            gametimemin += _act.get("time", 0) + extra_time

            for _axis, _pts in _act.get("score", {}).items():
                add_stat(date_char, "date_" + _axis, _pts)

            if act_id not in date_done:
                date_done.append(act_id)

    call gametime from _call_gametime_83

    return

# ----------------------------------------------------------------------------------------------------
label date_wnei_hub: # WNEI's own hub: the two stores, in the order the plan tells them
# ----------------------------------------------------------------------------------------------------

    $ wnei_mood = "A1"
    scene expression Date_Bg("bg_shopping_hall", "bg_shopping_hall")
    show WNEI at RC
    show HERO at LC
    show screen Date_UI
    with Fade(1, 0, 2)

    label date_wnei_hub_menu:
        pass

    menu:

        "Stationery Store" if "stationery" not in date_done:
            call date_wnei_stationery from _call_date_wnei_stationery

        "Fashion Store" if "fashion" not in date_done and "stationery" in date_done:
            call date_wnei_fashion from _call_date_wnei_fashion

        "Finish":
            call date_end("wnei", "shopping", False) from _call_date_end_wnei

    jump date_wnei_hub

# ----------------------------------------------------------------------------------------------------
label date_wnei_stationery: # Bookstore walk, ending on the label stickers
# ----------------------------------------------------------------------------------------------------

    stop BGM fadeout 3

    scene bg_0 with Dissolve(1)

    "You decided to enter first in a stationery."

    play BGM "W2C - Tranquility.mp3"

    scene wnei_shopping_book_1_bg
    show fx_light
    with Dissolve(2)

    if 0 > 1:

        wnei "{bt}Woooah...!{/bt}{w=[wt2]} It's a castle!{w=[wt3]} A castle made of {nm}paper{/nm}!"
        hero "It's a bookstore, [C_Nam][fnamewnei][C_Off]."
        wnei "Same thing!{w=[wt3]} Look at how tall the shelves are!{w=[wt2]} Nobody could ever read all of that, not even in a hundred years!"
        hero "Some people try."
        wnei "{aw}Hmm...{/aw}{w=[wt3]} They must be super duper patient."

        # Novels

        wnei "So many{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} [C_Nam][fnamehero][C_Off]{w=[wt1]}, what's this one about?"
        hero "'A detective returns to his hometown to solve a murder that nobody wants solved.'"
        wnei "Ooooh...{w=[wt3]} Did the butler do it?"
        hero "...Why the butler?"
        wnei "It's always the butler!{w=[wt3]} Mom watches those shows, and it's {bt}always{/bt} the butler!"
        hero "{gg}Pff...{/gg}{w=[wt2]} Fair point."

        wnei "{aw}Uhhh...{/aw}{w=[wt3]} this book is bad..."
        hero "Do you think so? What's it about?"
        wnei "I don't even know."
        hero "{aw}Ehhh...?{/aw}"
        wnei "What?"
        hero "Why did you say it's bad?"
        wnei "Oh{w=[wt1]}, that?{w=[wt2]} Hmmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Cause it just have letters.{w=[wt3]} Letters, letters, and more letters.{w=[wt3]} How can I suppose to read a book if it has no pictures at {nm}all{/nm}?."
        hero "{aw}That's how reading works!!!{/aw}"
        wnei "I only like to read {bt}images{/bt}!{w=[wt3]} Images don't need to be untangled, they just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} tell you things!"

        menu:
            "Tell her images are a language too":
                $ add_stat("wnei", "date_rom", 3)
                hero "You know, reading images is a real skill.{w=[wt3]} Most people look at a picture and miss half of what it says."
                wnei "{bt}Eh?!{/bt}{w=[wt3]} Really?"
                hero "Really.{w=[wt2]} You just have to look closely, like you do with everything."
                wnei "{gg}Hehe...{/gg}{w=[wt3]} So I'm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} a super duper reader?"
                hero "The best one in this store."

            "Tease her about it":
                $ add_stat("wnei", "date_fun", 3)
                hero "So you're telling me you'd rather read a menu without words?"
                wnei "Yes!{w=[wt3]} With a picture of the food!"
                hero "And if there's no picture?"
                wnei "Then I order the {nm}one that looks the most delicious{/nm} in my head!"
                hero "That's the most dangerous way to eat I've ever heard."

        wnei "Come on{w=[wt1]}, [C_Nam][fnamehero][C_Off]!{w=[wt2]} The letters give me a headache.{w=[wt3]} Let's go find the {bt}good{/bt} books!"

        # Picture books and comics

        wnei "{bt}HERE!!!{/bt}{w=[wt3]} This is the place!{w=[wt2]} This is my place!"

        wnei "Look{w=[wt1]}, look!{w=[wt2]} A bear who's afraid of the dark!{w=[wt3]} And a fish who wants to fly!{w=[wt3]} And{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} oh!{w=[wt2]} A dragon who runs a bakery!"
        hero "A dragon who runs a bakery?"
        wnei "He burns all the bread by accident, but then everyone loves it because it tastes like {nm}campfire{/nm}!"
        hero "...You already read this one."
        wnei "Uh-huh!{w=[wt3]} Twelve times!"

        wnei "See?{w=[wt3]} The pictures tell a story {bt}inside{/bt} the story.{w=[wt3]} The words say he's sad, but look at his tail!"
        hero "It's wagging."
        wnei "He's lying!{w=[wt3]} He's pretending to be sad so the baker lady gives him a cookie!"
        hero "{lg}Ha ha ha!{/lg}{w=[wt3]} You're right.{w=[wt2]} I didn't notice that at all."

        mind "(She really does read this stuff. Not skimming, not pretending. Page after page, she finds things I'd never look for.)"

        wnei "That's why I like images.{w=[wt3]} You can look at them for a long, long time and they keep giving you {nm}new{/nm} stuff."
        wnei "Letters only say it once."

        hero "...Hey, [C_Nam][fnamewnei][C_Off]."
        wnei "Hm?"
        hero "Maybe next time{w=[wt1]}, I'll draw you a story."
        wnei "{bt}EH?!{/bt}{w=[wt3]} You can draw?!"
        hero "Not well.{w=[wt3]} Stick figures, mostly."
        wnei "{gg}Tee-hee...{/gg}{w=[wt3]} Stick figures are {bt}great{/bt}!{w=[wt2]} They're the most honest kind!"
        $ add_stat("wnei", "date_rom", 3)

        # Drawing books

        wnei "Ooooh...{w=[wt3]} It smells like a {nm}rainy day{/nm} in here."
        hero "That's the charcoal."
        wnei "I like it!{w=[wt2]} It smells like... like when you're about to make something."

        wnei "[C_Nam][fnamehero][C_Off]{w=[wt1]}, what if I draw {bt}my own{/bt} book?{w=[wt3]} With only images!"
        hero "What would it be about?"
        wnei "{aw}Hmm...{/aw}{w=[wt3]} A girl who lives in a house full of{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} very confusing people."
        hero "That sounds familiar."
        wnei "And there's a boy who{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} who{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Hmmm.{w=[wt3]} I haven't decided yet."
        hero "Does he get a cookie at the end?"
        wnei "{gg}Hehehe...{/gg}{w=[wt3]} Only if he's good!"

        mind "(I'll remember that one.)"
        $ wnei_know.append("Sketchbook")

        # Stationery

        wnei "Woooah...!{w=[wt2]} It's like a rainbow threw up in here!"
        hero "That's... a vivid way to put it."
        wnei "Look{w=[wt1]}, [C_Nam][fnamehero][C_Off]!{w=[wt2]} That pen has a {bt}unicorn{/bt} on top!{w=[wt3]} And that one smells like {nm}strawberry{/nm}!"
        hero "Please don't lick the pens."
        wnei "{gg}Tee-hee...{/gg}{w=[wt2]} I wasn't gonna.{w=[wt3]} {aw}...Okay, maybe a little sniff.{/aw}"

        hero "That's my name."
        wnei "Uh-huh!{w=[wt3]} I only know how to write four words.{w=[wt2]} Mom, dog, [C_Nam][fnamehero][C_Off] and{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} 'cookie'."
        hero "That's a pretty good four."
        wnei "{bt}Right?!{/bt}"

    scene wnei_shopping_book_1_wnei a1
    show fx_light
    wnei "[C_Nam][fnamehero][C_Off]{w=[wt1]}, [C_Nam][fnamehero][C_Off]!{w=[wt2]} Can ya buy me {bt}label stickers{/bt}?"

    scene wnei_shopping_book_1_hero a1
    show fx_light
    hero "Label stickers?{w=[wt2]} What for?"

    scene wnei_shopping_book_1_wnei a1
    show fx_light
    wnei "I wanna organize my stuff!{w=[wt3]} My room is a {nm}mess{/nm}, and mom says if I put names on things I'll find 'em!"

    scene wnei_shopping_book_1_hero a1
    show fx_light
    hero "That's actually a smart idea."
    
    scene wnei_shopping_book_1_wnei a1
    show fx_light
    wnei "And since I can write {nm}four{/nm} words, I'll put the same four on everything!"

    scene wnei_shopping_book_1_hero a1
    show fx_light
    hero "...That's less smart."
    
    scene wnei_shopping_book_1_wnei a1
    show fx_light
    wnei "{gg}Hehe...{/gg}{w=[wt2]} I'm a super duper smart girl!"

    scene wnei_shopping_book_1_bg
    show fx_light
    menu:
        "Buy the label stickers {pr}[C_Neg](-$10)[C_Off]": #if money >= 10
            #$ money -= 10
            $ add_stat("wnei", "love", 1)
            $ add_stat("wnei", "date_rom", 4)
            #$ wnei_know.append("Stickers")

            scene wnei_shopping_book_1_hero a1
            show fx_light
            hero "Sure.{w=[wt2]} Let's get them."

            scene wnei_shopping_book_1_wnei a1
            show fx_light
            wnei "{bt}YAAAAY!!!{/bt}{w=[wt3]} You're the best, [C_Nam][fnamehero][C_Off]!"

            scene wnei_shopping_book_1_hero a1
            show fx_light
            "She hugs the sticker pack against her chest like a treasure."

            scene wnei_shopping_book_1_wnei a1
            show fx_light
            wnei "I'm gonna label {bt}everything{/bt}!{w=[wt3]} My bed, my shoes, my{w=[wt1]} toothbrush..."

            scene wnei_shopping_book_1_hero a1
            show fx_light
            hero "Maybe not your toothbrush."

            scene wnei_shopping_book_1_wnei a1
            show fx_light
            wnei "{aw}Awww...{/aw}{w=[wt2]} Okay."

            scene wnei_shopping_book_1_bg
            show fx_light

        #"Buy the label stickers {pr}[C_Neg](-$10)[C_Off]" if money < 10:
            #hero "I don't have enough money for that right now."
            #wnei "{aw}Oh...{/aw}{w=[wt3]} It's okay!{w=[wt2]} Maybe next time!"

        #"Not now":
            #hero "Maybe another time."
            #wnei "{aw}Okay...{/aw}{w=[wt3]} But I'm gonna remember where they are!{w=[wt2]} {bt}Sticker wall!{/bt}"

    return

# ----------------------------------------------------------------------------------------------------
label date_wnei_fashion: # Fancy store: shoes, makeup, the swimsuit rack and the stuck hanger
# ----------------------------------------------------------------------------------------------------

    scene bg_0 with Dissolve(1)

    "You enter in a fashion store."

    # Entrance
    scene wnei_shopping_fashion_1_bg
    show wnei_shopping_fashion_1_char_body
    show wnei_shopping_fashion_1_char_wear dressy
    show fx_light
    with Dissolve(2)

    wnei "{aw}Uhhh...{/aw}{w=[wt3]} [C_Nam][fnamehero][C_Off]..."
    hero "What's wrong?"
    wnei "{aw}Shhh!{/aw}{w=[wt2]} Talk quieter.{w=[wt3]} This is a {nm}fancy{/nm} store."
    hero "How can you tell?"
    wnei "The floor is so clean I can see my {bt}face{/bt} on it!{w=[wt3]} And nobody is shouting.{w=[wt3]} In fancy places nobody shouts."
    hero "{gg}Pff...{/gg}{w=[wt2]} You can talk normally, [C_Nam][fnamewnei][C_Off].{w=[wt3]} Nobody will arrest you."
    wnei "{aw}Are you sure?{/aw}{w=[wt3]} Mom says if I break something expensive, we have to live here forever."
    hero "Then don't break anything."
    wnei "{aw}Okay...{/aw}{w=[wt3]} I'm gonna walk super duper carefully.{w=[wt2]} Like a ninja."
    hero "A ninja in a clothing store."
    wnei "A {bt}fashion ninja{/bt}!"

    # Makeup
    scene wnei_shopping_fashion_2_bg
    show fx_light
    with fade

    wnei "Ooooh...{w=[wt3]} [C_Nam][fnamehero][C_Off]{w=[wt1]}, it's a {nm}paint shop{/nm}!{w=[wt2]} For faces!"
    hero "It's makeup."
    wnei "Makeup!{w=[wt3]} Mom does this every morning in the bathroom with the door closed.{w=[wt3]} I only get to see the before and the after!{w=[wt3]} The middle part is a {bt}mystery{/bt}."
    wnei "Look at all the {nm}little sticks{/nm}!{w=[wt2]} Hundreds of thousands of billions of super-duperllions of 'em!{w=[wt3]} All standing in line, like{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} like a pink army!"
    hero "They're lipsticks."
    wnei "Why would somebody need this many?"
    hero "Maybe{w=[wt2]}, different colors.{w=[wt3]} Different days."
    wnei "{aw}Hmm...{/aw}{w=[wt3]} So they have a lipstick for Mondays, and one for Tuesdays..."
    hero "Something like that, I suppose."
    wnei "And one for when you're {nm}sad{/nm}, and one for when you're {nm}super duper happy{/nm}!"
    hero "{gg}Hee-hee...{/gg}{w=[wt2]} That's a good way to think about it."
    wnei "[C_Nam][fnamehero][C_Off]{w=[wt1]}, what are those little pink boxes, with a mirror in the lid?"
    hero "Powder.{w=[wt3]} For the face."
    wnei "{aw}Hm?{/aw}{w=[wt3]} Face{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {nm}flour{/nm}?"
    hero "Kind of.{w=[wt3]} It makes the skin look smooth."
    wnei "But skin is already smooth!{w=[wt3]} Unless you fall off the swing.{w=[wt2]} Then it's scrapey."
    hero "That's... different."
    wnei "And those bottom ones!{w=[wt3]} All the little tubes, from light to dark, like a{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} like a {nm}chocolate{/nm} rainbow!"
    hero "They have skin tones.{w=[wt2]} Maybe it's for matching any skin."
    wnei "Woooah...!{w=[wt3]} So there's one for {bt}everyone{/bt}?"
    hero "Pretty much."
    wnei "{gg}Hehe...{/gg}{w=[wt3]} I like that.{w=[wt2]} Nobody gets left out of the line except aliens or monsters."
    wnei "[C_Nam][fnamehero][C_Off]{w=[wt1]}, do you think I'd look good with one of those?"
    hero "You look good without anything."
    wnei "{bt}Ehhh...!?{/bt}{w=[wt3]} Won't you get me a super cool and fancy one if I chose?"
    hero "Just if you give me your credit card."
    wnei "I'm {bt}not{/bt} touching anything!{w=[wt3]} See?{w=[wt2]} My hands are frozen!"
    hero "I can see that.{w=[wt3]} You look like a scarecrow."
    wnei "A scarecrow {bt}ninja{/bt}!{w=[wt3]} Still fashion, still very careful to do not touch anything that I can't pay!"
    $ add_stat("wnei", "date_rom", 3)

    if 0 > 1:
        # Shoes
        scene wnei_shopping_fashion_2_bg

        wnei "Woooah...!{w=[wt3]} [C_Nam][fnamehero][C_Off]{w=[wt1]}, look at the shoes!{w=[wt2]} Shoes with {nm}flowers{/nm} on 'em!{w=[wt3]} Real ones?!"
        hero "They're fabric.{w=[wt2]} Don't pull on them."
        wnei "Can I try? {w=[wt2]}Just one?{w=[wt3]} Pleeease?"
        hero "Go ahead.{w=[wt2]} I'll hold the other one."
        wnei "{gg}Hehe...{/gg}{w=[wt3]} It's so soft inside!{w=[wt2]} Like walking on a {nm}cloud{/nm}!"
        wnei "Hey{w=[wt1]}, hey!{w=[wt2]} Look at these tall ones!{w=[wt3]} With the thin stick under the heel!"
        hero "Those are high heels.{w=[wt3]} Careful, they're hard to walk with."
        wnei "Pff, how hard can it be?{w=[wt3]} It's just standing on{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Whoa{w=[wt1]}-whoa{w=[wt1]}-{bt}WHOAAA!{/bt}"
        hero "{pa}Got you!{/pa}{w=[wt3]} I've got you!"
        wnei "{aw}H{w=[wt1]}-heeey...{/aw}{w=[wt3]} The floor moved!"
        hero "The floor didn't move.{w=[wt3]} You tilted."
        wnei "{aw}Hmm...{/aw}{w=[wt3]} Girls who wear these must have {bt}super legs{/bt}."
        hero "Or really good balance."
        wnei "Or a [C_Nam][fnamehero][C_Off] to hold on to!"
        hero "...Let's put these back."
        $ add_stat("wnei", "date_rom", 2)

        # Dresses
        scene wnei_shopping_fashion_3_bg

        wnei "Come on{w=[wt1]}, [C_Nam][fnamehero][C_Off]!{w=[wt2]} Dresses!"
        wnei "Look!{w=[wt3]} This one is so poofy!{w=[wt2]} I'm a princess!{w=[wt3]} {bt}Your highness!{/bt}"
        hero "Your highness."
        wnei "And this one has a tail behind it!{w=[wt3]} I'm a {nm}mermaid{/nm}!{w=[wt2]} Splash, splash!"
        hero "Mermaids don't say splash."
        wnei "Mine does!{w=[wt3]} And this one{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} this one is black and serious.{w=[wt3]} Hmm.{w=[wt2]} I'm a spy!"
        hero "A spy who giggles."
        wnei "{gg}Tee-hee...{/gg}{w=[wt3]} The best spy!{w=[wt2]} Nobody suspects the giggling one!"
        $ add_stat("wnei", "date_fun", 3)

    # Swimwear
    scene wnei_shopping_fashion_3_bg
    show wnei_shopping_fashion_3_wnei o0
    show fx_light
    with Fade(1, 0, 2)

    hero "Here we are!"

    show wnei_shopping_fashion_3_wnei o1
    wnei "[C_Nam][fnamehero][C_Off]{w=[wt1]}, this one is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} really small.{w=[wt3]} I think they forgot to finish them!{w=[wt3]} It's just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} a few triangles and some string!"

    show wnei_shopping_fashion_3_wnei o0
    hero "Maybe this one is for just saying there's something on.{w=[wt4]} What about you?{w=[wt2]} Do you have a swimsuit?"

    show wnei_shopping_fashion_3_wnei a1
    wnei "{bt}Hmm...{/bt}{w=[wt3]} Nope!{w=[wt2]} Mom says my old one is too small now.{w=[wt3]} I put it on last summer and it said {aw}rrrrip{/aw}."

    show wnei_shopping_fashion_3_wnei a0
    hero "Then this is the perfect time to get a new one."

    show wnei_shopping_fashion_3_wnei a1
    wnei "{bt}Yeah!{/bt}{w=[wt3]} Help me pick one!{w=[wt2]} I wanna be the best-dressed at the beach!"
    wnei "Okay{w=[wt1]}, okay.{w=[wt2]} Rules!{w=[wt3]} It has to be cute, it can't itch, and it has to look good {bt}wet{/bt}."

    show wnei_shopping_fashion_3_wnei a0
    hero "How do you know what looks good wet?"

    show wnei_shopping_fashion_3_wnei a1
    wnei "I don't!{w=[wt3]} That's why I need a {nm}professional{/nm}."

    show wnei_shopping_fashion_3_wnei a0
    hero "...I'm a professional now?"

    show wnei_shopping_fashion_3_wnei a1
    wnei "Uh-huh!{w=[wt3]} You get to hold the hangers."

    show wnei_shopping_fashion_3_wnei o1
    wnei "Look at this one!{w=[wt3]} It's got shells between the strings!"

    show wnei_shopping_fashion_3_wnei o0
    hero "Not bad.{w=[wt2]} But you'd lose the shell in the first wave."

    show wnei_shopping_fashion_3_wnei o1
    wnei "{aw}Nooo...{/aw}{w=[wt3]} Then I'd have to dive for it!{w=[wt4]} And this one is black with a skull!{w=[wt2]} I'm a {nm}pirate{/nm}!"

    show wnei_shopping_fashion_3_wnei a0
    hero "A pirate who giggles."

    show wnei_shopping_fashion_3_wnei a1
    wnei "{gg}Tee-hee...{/gg}{w=[wt3]} The best pirate!{w=[wt2]} Nobody suspects the giggling one!"

    show wnei_shopping_fashion_3_wnei o1
    wnei "Hmm... this one's too serious.{w=[wt3]} This one is too long.{w=[wt3]} And this one{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} has a weird plastic thing on it{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} {bt}OH!!!{/bt}{w=[wt3]} [C_Nam][fnamehero][C_Off]{w=[wt1]}, [C_Nam][fnamehero][C_Off]{w=[wt1]}, {bt}[C_Nam][fnamehero][C_Off]!{/bt}"

    show wnei_shopping_fashion_3_wnei o1
    wnei "How about this one?{w=[wt3]} It's yellow, with tiny ruffles on the edges!"

    show wnei_shopping_fashion_3_wnei a0
    hero "That's... really cute.{w=[wt3]} It suits you."

    show wnei_shopping_fashion_3_wnei o1
    wnei "{gg}Hehehe...{/gg}{w=[wt2]} I thought so too!{w=[wt3]} It's {nm}yellow{/nm}!{w=[wt2]} Like the sun!"

    show wnei_shopping_fashion_3_wnei a1
    wnei "I wanna try it on!{w=[wt3]} Come on{w=[wt1]}, [C_Nam][fnamehero][C_Off]!{w=[wt2]} Bring the hangers, professional!"

    show wnei_shopping_fashion_3_wnei a0 with None

    # Fitting room
    scene wnei_shopping_fashion_4_bg 1
    show wnei_shopping_fashion_4_hero 1
    show wnei_shopping_fashion_4_hero_face 1o0
    show wnei_shopping_fashion_4_wnei 1
    show fx_light
    with Fade(1, 0, 2)

    show wnei_shopping_fashion_4_wnei 2
    wnei "Wait here, okay?{w=[wt2]} Don't peek!"

    show wnei_shopping_fashion_4_hero_face 1o1
    show wnei_shopping_fashion_4_wnei 1
    hero "I won't.{w=[wt2]} I'll be right here on the sofa."
    
    show wnei_shopping_fashion_4_hero_face 1o0
    show wnei_shopping_fashion_4_wnei 2
    wnei "Okay!{w=[wt3]} Now close your eyes and count to a hundred!"
    
    show wnei_shopping_fashion_4_hero_face 1o1
    show wnei_shopping_fashion_4_wnei 1
    hero "It won't take a hundred."
    
    show wnei_shopping_fashion_4_hero_face 1o0
    show wnei_shopping_fashion_4_wnei 2
    wnei "{bt}Hmmm...{/bt}{w=[wt4]} Okay{w=[wt2]}, then{w=[wt2]}, to a thousand."
    
    show wnei_shopping_fashion_4_hero_face 1o1
    show wnei_shopping_fashion_4_wnei 1
    hero "It got even worst!!!"
    
    show wnei_shopping_fashion_4_hero_face 1o0
    show wnei_shopping_fashion_4_wnei 2
    wnei "Then{w=[wt2]}, count on how much you prefer{w=[wt2]}, from one to infinite."
    
    show wnei_shopping_fashion_4_hero_face 1o1
    show wnei_shopping_fashion_4_wnei 1
    hero "Okay.{w=[wt3]} One.{w=[wt3]} Are you ready?"
    
    show wnei_shopping_fashion_4_hero_face 1o0
    show wnei_shopping_fashion_4_wnei 2
    wnei "I'm almost ready.{w=[wt2]} Count again!"

    show wnei_shopping_fashion_4_wnei 1 with None

    scene wnei_shopping_fashion_4_bg 2
    show wnei_shopping_fashion_4_hero 1
    show wnei_shopping_fashion_4_hero_face 1o0
    show fx_light
    with dissolve

    pause

    show wnei_shopping_fashion_4_hero_face 1o1
    hero "One.{w=[wt3]} Are you ready?"

    show wnei_shopping_fashion_4_hero_face 1o0
    wnei "{pa}Almost!{w=[wt2]} Do again!!!{/pa}"

    show wnei_shopping_fashion_4_hero_face 1o0 with None

    scene wnei_shopping_fashion_4_bg 2
    show wnei_shopping_fashion_4_hero 2
    show fx_light
    with Fade(2, 0, 3)

    mind "(Why is it taking so long...?)"

    wnei "{aw}Uhhh...{/aw}{w=[wt3]} [C_Nam][fnamehero][C_Off]?"

    scene wnei_shopping_fashion_4_bg 2
    show wnei_shopping_fashion_4_hero 1
    show wnei_shopping_fashion_4_hero_face 1o0
    show fx_light
    with dissolve

    show wnei_shopping_fashion_4_hero_face 1o1
    hero "Yeah?"
    
    show wnei_shopping_fashion_4_hero_face 1o0
    wnei "I need yar help.{w=[wt2]} Cum here!"

    show wnei_shopping_fashion_4_hero_face 1o1
    hero "{aw}Huh...?{/aw}{w=[wt2]} I{w=[wt1]}, uh...{w=[wt3]} I can't go in there."

    show wnei_shopping_fashion_4_hero_face 1o0
    wnei "Why not?"

    show wnei_shopping_fashion_4_hero_face 1o1
    hero "Cause people would find it weird."

    show wnei_shopping_fashion_4_hero_face 1o0
    wnei "Who's {nm}people{/nm}?"

    show wnei_shopping_fashion_4_hero_face 1o1
    hero "{aw}Uh...{/aw}{w=[wt3]} The ones who{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} might come{w=[wt1]}, I guess."

    show wnei_shopping_fashion_4_hero_face 1o0
    wnei "Oh...!{w=[wt2]} Are ya afraid of ghosts?{w=[wt2]} But the lights are on!{w=[wt2]} They're also afraid."

    show wnei_shopping_fashion_4_hero_face 1o1
    hero "I'm not talking about ghosts!{w=[wt3]} People might come here and will think I'm doing something wrong!"

    show wnei_shopping_fashion_4_hero_face 1o0
    wnei "{aw}Ehhh...?{/aw}{w=[wt3]} Why living people would think it's wrong for you to help me?{w=[wt3]} Are you sure you're not talking about ghosts?"

    show wnei_shopping_fashion_4_hero_face 1o1
    hero "I think living people do much worse things than ghosts!{w=[wt3]} {aw}Ugh...{/aw}{w=[wt2]} O{w=[wt1]}-okay.{w=[wt2]} I'm coming in."

    show wnei_shopping_fashion_4_hero_face 1o0 with None

    stop BGM fadeout 3

    scene bg_0 with Dissolve(1)

    play BGM "W2C - Lust.mp3"

    # Stall
    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_hero_body 1a
    show wnei_shopping_fashion_5_hero_face 1s0
    show wnei_shopping_fashion_5_wnei_body 1
    show wnei_shopping_fashion_5_wnei_face 1o0
    show wnei_shopping_fashion_5_wear 1
    show fx_light
    with Dissolve(3)

    show wnei_shopping_fashion_5_hero_face 1s1
    hero "{aw}Ehhh!?!?!? W{w=[wt1]}-w{w=[wt1]}-why are you naked?!{/aw}"

    show wnei_shopping_fashion_5_hero_face 1s0
    show wnei_shopping_fashion_5_wnei_face 1o1
    wnei "Huh?{w=[wt2]} I was changing! {bt}Duuuh...!{/bt}"

    show wnei_shopping_fashion_5_hero_face 1s1
    show wnei_shopping_fashion_5_wnei_face 1o0
    hero "So{w=[wt2]}, remember what I was saying about people potentially thinking weird things when two people are in the same stall?{w=[wt4]} Well{w=[wt2]}, they'd be right."

    show wnei_shopping_fashion_5_hero_face 1s0
    show wnei_shopping_fashion_5_wnei_face 1o1
    wnei "Look!{w=[wt2]} Look at this!{w=[wt3]} It won't come out!{w=[wt3]} I've been pulling and pulling and {bt}pulling{/bt}, and the bikini won't leave the hanger!"

    show wnei_shopping_fashion_5_wnei_body at GetShake(0.02, 0.01, math.inf)
    show wnei_shopping_fashion_5_wnei_face 1o2 at GetShake(0.02, 0.01, math.inf)
    show wnei_shopping_fashion_5_wear at GetShake(0.02, 0.01, math.inf)
    pause    

    show wnei_shopping_fashion_5_hero_face 1s1
    hero "Wait{w=[wt1]}, don't{w=[wt1]}-{nw}"

    show wnei_shopping_fashion_5_hero_face 1s0
    show wnei_shopping_fashion_5_wnei_face 1o3
    wnei "{aw}Grrrrr...!{w=[wt2]} Come on, you stupid thing!{/aw}"

    play SE1 "Slip.ogg"

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_hero_body 2 at RR
    show wnei_shopping_fashion_5_hero_face 2s0 at RR
    show wnei_shopping_fashion_5_wnei_body 1
    show wnei_shopping_fashion_5_wnei_face 1o2
    show wnei_shopping_fashion_5_wear 2 at RR
    show fx_light

    show wnei_shopping_fashion_5_hero_body 2 at CC_fast
    show wnei_shopping_fashion_5_hero_face 2s0 at CC_fast
    show wnei_shopping_fashion_5_wear 2 at CC_fast

    pause(0.25)

    show wnei_shopping_fashion_5_hero_body 2 at CC
    show wnei_shopping_fashion_5_hero_face 2s0 at CC
    show wnei_shopping_fashion_5_wear 2 at CC

    show wnei_shopping_fashion_5_wnei_face 1o0
    show wnei_shopping_fashion_5_hero_face 2s1
    hero "{bt}STOP!{/bt}{w=[wt2]} You're gonna tear it!{w=[wt4]} See this little clip?{w=[wt2]} It's got a button on top.{w=[wt2]} Press it, and{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {nw}"

    play SE1 "Switch.mp3"

    hero "{bt}STOP!{/bt}{w=[wt2]} You're gonna tear it!{w=[wt4]} See this little clip?{w=[wt2]} It's got a button on top.{w=[wt2]} Press it, and{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {aw}(click){/aw}{fast}{w=[wt3]} it's free!"

    show wnei_shopping_fashion_5_wnei_body 2
    show wnei_shopping_fashion_5_wnei_face 2o1
    show wnei_shopping_fashion_5_hero_face 2s0
    wnei "{bt}Ohhh...!{/bt}{w=[wt3]} It was a {nm}button{/nm}?!"

    show wnei_shopping_fashion_5_hero_face 2s1
    hero "Yeah.{w=[wt2]} They do this as a security measure.{w=[wt2]} But in a stupidly foolish way!"

    show wnei_shopping_fashion_5_hero_face 2s0 with None

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_hero_body 3
    show wnei_shopping_fashion_5_hero_face 3s0
    show wnei_shopping_fashion_5_wnei_body 3a
    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_wear 3
    show fx_light
    with dissolve

    show wnei_shopping_fashion_5_wnei_face 3a1
    wnei "Super duper smart, [C_Nam][fnamehero][C_Off]!{w=[wt3]} Thank you!"

    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_hero_face 3s1
    hero "{aw}Y{w=[wt1]}-you're welcome...{/aw}"

    show wnei_shopping_fashion_5_wnei_face 3a1
    show wnei_shopping_fashion_5_hero_face 3s0
    wnei "Ya can wait me outside now.{w=[wt3]} Make sure to count up to a very high number this time!"

    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_hero_face 3s1
    hero "{aw}W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I can't get out hard like this!{/aw}"

    show wnei_shopping_fashion_5_wnei_face 3a1
    show wnei_shopping_fashion_5_hero_face 3s0
    wnei "Hmm?{w=[wt1]} What's hard?"

    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_hero_face 3s1
    hero "W{w=[wt1]}-well{w=[wt2]}, I mean{w=[wt2]}, t{w=[wt1]}-that's hard to think to leave you without help, you know?{w=[wt3]} What if you need me again?{w=[wt3]} I better stay here just to be safe."

    show wnei_shopping_fashion_5_wnei_face 3o0
    show wnei_shopping_fashion_5_hero_face 3s0
    wnei "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}"

    show wnei_shopping_fashion_5_wnei_face 3a0
    wnei "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{fast}{w=[wt2]}{nw}"

    show wnei_shopping_fashion_5_wnei_face 3a1
    wnei "Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{fast} Ahh{w=[wt2]}, I see.{w=[wt4]} Then It's okay!{w=[wt3]} But turn around and don't peek!{w=[wt3]} What if you see me naked?"

    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_hero_face 3s1
    hero "Y{w=[wt1]}-you're right.{w=[wt3]} I better turn around then, right?{w=[wt3]} You wouldn't like I'd end up seeing you naked out of a sudden after all."

    show wnei_shopping_fashion_5_wnei_face 3a1
    show wnei_shopping_fashion_5_hero_face 3s0
    wnei "Yeah!{w=[wt2]} But I trust you.{w=[wt3]} Turn around already!"

    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_hero_face 3s3
    hero "O{w=[wt1]}-okay.{w=[wt2]} I turned."

    show wnei_shopping_fashion_5_wnei_face 3a1
    show wnei_shopping_fashion_5_hero_face 3s2
    wnei "Great!{w=[wt2]} Just don't turn too much so you can't see me if I need help."

    show wnei_shopping_fashion_5_wnei_face 3a0 with None

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_hero_body 3
    show wnei_shopping_fashion_5_hero_face 3s2
    show wnei_shopping_fashion_5_wnei_body 4
    show fx_light
    with dissolve

    show wnei_shopping_fashion_5_hero_face 3s3
    hero "S{w=[wt1]}-sure."

    show wnei_shopping_fashion_5_hero_face 3s4
    hero "S{w=[wt1]}-sure.{fast} Wait.{w=[wt2]} What?"

    show wnei_shopping_fashion_5_hero_face 3s0 with None

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_wnei_body 3a
    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_wear 4
    show wnei_shopping_fashion_5_hero_body 3
    show wnei_shopping_fashion_5_hero_face 3s0
    show fx_light
    with dissolve

    show wnei_shopping_fashion_5_hero_face 3s4
    show wnei_shopping_fashion_5_wnei_face 3a0
    hero "How is that supposed to fit through?{w=[wt3]} Your head is way bigger than the opening."

    show wnei_shopping_fashion_5_hero_face 3s0
    show wnei_shopping_fashion_5_wnei_face 3a1
    wnei "That's how the real world works.{w=[wt2]} Only in games do clothes need tiny heads."

    show wnei_shopping_fashion_5_hero_face 3s4
    show wnei_shopping_fashion_5_wnei_face 3a0
    hero "Shouldn't it be the opposite?{w=[wt3]} What if we live in a simulation?{w=[wt3]} What if we're part of a game?"

    show wnei_shopping_fashion_5_hero_face 3s0
    show wnei_shopping_fashion_5_wnei_face 3a1
    wnei "If we were part of a game{w=[wt2]}, I would have managed to get dressed by now.{w=[wt2]} Because in games{w=[wt2]}, clothes always fit perfectly!!{w=[wt3]} And this isn't going over my chest."

    show wnei_shopping_fashion_5_hero_face 3s4
    show wnei_shopping_fashion_5_wnei_face 3a0
    hero "It just went over your head, though."

    show wnei_shopping_fashion_5_hero_face 3s0
    show wnei_shopping_fashion_5_wnei_face 3a1
    wnei "Breasts are different, fool!{w=[wt3]} It seems ya don't understand anything about physics or real life.{w=[wt3]} Cum on!{w=[wt2]} Ya were right!{w=[wt3]} I still need you to help me to get my super big boobas inside this tiny lil yellow thing."

    show wnei_shopping_fashion_5_hero_face 3s4
    show wnei_shopping_fashion_5_wnei_face 3a0
    hero "{aw}Ehhh!????{/aw}{w=[wt4]} S{w=[wt1]}-sure.{w=[wt3]} Let me..."

    show wnei_shopping_fashion_5_hero_face 3s0 with None

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_char_body 1
    show fx_light
    with dissolve

    pause

    play SE1 "Squeak2.ogg"

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_char_body 2
    show fx_light

    pause(0.25)

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_char_body 1
    show fx_light

    pause

    play SE1 "Squeak2.ogg"

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_char_body 2
    show fx_light

    pause(0.25)

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_char_body 1
    show fx_light

    pause

    play SE1 "Squeak2.ogg"

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_char_body 2
    show fx_light

    pause(0.25)

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_wnei_body 3a
    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_wear 5
    show wnei_shopping_fashion_5_hero_body 3 at RR
    show wnei_shopping_fashion_5_hero_face 3s0 at RR
    show wnei_shopping_fashion_5_hero_body 3 at CC_slow
    show wnei_shopping_fashion_5_hero_face 3s0 at CC_slow
    show fx_light
    with dissolve

    pause

    show wnei_shopping_fashion_5_hero_body 3 at CC
    show wnei_shopping_fashion_5_hero_face 3s0 at CC

    show wnei_shopping_fashion_5_hero_face 3s1
    hero "Done"

    show wnei_shopping_fashion_5_hero_face 3s0
    show wnei_shopping_fashion_5_wnei_face 3a1
    wnei "Thank you!{w=[wt3]} Now ya should close your eyes.{w=[wt3]} I'll wear the bottom.{w=[wt3]} Just open it when I say so, okay?"

    show wnei_shopping_fashion_5_hero_face 3s1
    show wnei_shopping_fashion_5_wnei_face 3a0
    hero "Okay..."

    show wnei_shopping_fashion_5_hero_face 3s0 with None

    stop BGM fadeout 6

    scene bg_0 with Dissolve(3)

    pause

    wnei "Okay.{w=[wt3]} You can open already!"

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

    play BGM "audio/W2C - SexyVibes.mp3"

    scene bg_2 sparkling
    show action_tryon_wnei prototype1 at ZoomSTXY
    with Dissolve(3)

    pause

    hero "{bt} SO CUTE!!!{/bt}"

    show action_tryon_wnei prototype2

    wnei "It got too tiny in me{w=[wt2]}, and is entering inside my peach...!"

    show action_tryon_wnei prototype1

    hero "Now that you mentioned{w=[wt2]}, it seems to be a recurring problem, right?"

    show action_tryon_wnei prototype2

    wnei "Ugh{w=[wt2]}, yeah.{w=[wt2]} It always does this.{w=[wt3]} It bothers me.{w=[wt2]} Sometimes it even hurts."

    show action_tryon_wnei prototype1

    hero "That's because you have a very...{w=[wt2]} puffy peach."

    show action_tryon_wnei prototype2

    wnei "{bt}Heh...!{/bt}{w=[wt2]} Eat your hearts out!{w=[wt2]} I have the most super duper puffy peach of the world!"

    show action_tryon_wnei prototype1

    hero "{aw}I{w=[wt1]}-I didn't mean it as a compliment!!!{/aw}{w=[wt3]} It's a problem for you, right?"

    show action_tryon_wnei prototype2

    wnei "Oh!{w=[wt2]} Yeah.{w=[wt2]} Now that you mentioned{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'd like to stop it from happening."

    show action_tryon_wnei prototype1

    hero "What about the stickers we bought?"

    show action_tryon_wnei prototype2

    wnei "The label ones?"

    show action_tryon_wnei prototype1

    hero "If we put a couple over the{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} p{w=[wt1]}-problem area{w=[wt2]}, the fabric shouldn't dig in."

    show action_tryon_wnei prototype2

    wnei "{bt}Woooah!{/bt} That's actually genius!{w=[wt2]} Let's do it!"

    show action_tryon_wnei prototype1

    hero "Okay{w=[wt2]}, let me take one."

    scene wnei_shopping_fashion_6_bg
    show wnei_shopping_fashion_6_wnei_arm 1
    show wnei_shopping_fashion_6_wnei_body
    show wnei_shopping_fashion_6_wnei_hair 2
    show wnei_shopping_fashion_6_wnei_face o0
    show wnei_shopping_fashion_6_wnei_breasts 2
    show wnei_shopping_fashion_6_wnei_wear_top
    show wnei_shopping_fashion_6_wnei_wear_bot 1
    show fx_light
    with Fade(1, 0, 2)

    show wnei_shopping_fashion_6_wnei_face o1
    wnei "Did you find it?"

    show wnei_shopping_fashion_6_wnei_face o0
    hero "Here, we have a lot of labels!"

    scene wnei_shopping_fashion_6_bg
    show wnei_shopping_fashion_6_wnei_body
    show wnei_shopping_fashion_6_wnei_hair 2
    show wnei_shopping_fashion_6_wnei_face o0
    show wnei_shopping_fashion_6_wnei_wear_bot 2
    show wnei_shopping_fashion_6_wnei_arm 2
    show wnei_shopping_fashion_6_wnei_breasts 2
    show wnei_shopping_fashion_6_wnei_wear_top
    show fx_light
    with dissolve

    pause

    show wnei_shopping_fashion_6_wnei_face o1
    wnei "Excuse me, [C_Nam]Mrs. Peach[C_Off].{w=[wt3]} Now we'll put an additional garment on you!{w=[wt2]} You'll get super duper beautiful in{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Hmm{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Which color will we dress [C_Nam]Mrs. Peach[C_Off]?"

    show wnei_shopping_fashion_6_wnei_face o0 with None

    menu:
        "Red":
            show wnei_shopping_fashion_6_wnei_tape red
        "Orange":
            show wnei_shopping_fashion_6_wnei_tape orange
        "Yellow":
            show wnei_shopping_fashion_6_wnei_tape yellow
        "Green":
            show wnei_shopping_fashion_6_wnei_tape green
        "Blue":
            show wnei_shopping_fashion_6_wnei_tape blue
        "Purple":
            show wnei_shopping_fashion_6_wnei_tape purple
        "Magenta":
            show wnei_shopping_fashion_6_wnei_tape magenta

    show wnei_shopping_fashion_6_hero_arm 1
    hide fx_light
    show fx_light
    with dissolve

    hero "What about this color?"

    show wnei_shopping_fashion_6_wnei_face a1
    wnei "{bt}Cool!{w=[wt3]} [C_Nam]Mrs. Peach[C_Off] is now super duper fancy!{/bt}"

    show wnei_shopping_fashion_6_wnei_face a0
    mind "(Touching her there while she's wearing almost nothing...)"

    hide wnei_shopping_fashion_6_hero_arm
    with dissolve

    show wnei_shopping_fashion_6_wnei_face a1
    wnei "Let me see!"

    show wnei_shopping_fashion_6_wnei_face a0 with None

    scene wnei_shopping_fashion_6_bg
    show wnei_shopping_fashion_6_wnei_arm 1
    show wnei_shopping_fashion_6_wnei_body
    show wnei_shopping_fashion_6_wnei_hair 2
    show wnei_shopping_fashion_6_wnei_face o0
    show wnei_shopping_fashion_6_wnei_breasts 2
    show wnei_shopping_fashion_6_wnei_wear_top
    show wnei_shopping_fashion_6_wnei_wear_bot 3
    show fx_light
    with dissolve

    show wnei_shopping_fashion_6_wnei_face a1
    wnei "{bt}Oooh!{/bt}{w=[wt2]} It worked!"

    scene wnei_shopping_fashion_5_bg
    show wnei_shopping_fashion_5_hero_body 1b
    show wnei_shopping_fashion_5_hero_face 1s0
    show wnei_shopping_fashion_5_wnei_body 3b
    show wnei_shopping_fashion_5_wnei_face 3a0
    show fx_light
    with Fade(1, 0, 2)

    show wnei_shopping_fashion_5_wnei_face 3a1
    show wnei_shopping_fashion_5_hero_face 1s0
    wnei "Hero."

    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_hero_face 1s1
    hero "Y{w=[wt1]}-yeah?"

    show wnei_shopping_fashion_5_wnei_face 3a1
    show wnei_shopping_fashion_5_hero_face 1s0
    wnei "Your lollipop got in the super duper bazooka mode again!"

    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_hero_face 1s1
    hero "I know.{w=[wt3]} I can't walk out like this..."

    show wnei_shopping_fashion_5_wnei_face 3a1
    show wnei_shopping_fashion_5_hero_face 1s0
    wnei "How does it go back to normal?{w=[wt4]} Now that I've stopped to think about it{w=[wt2]}, that night you came back{w=[wt2]}, in the kitchen{w=[wt2]}, it just calmed down after we talked."

    show wnei_shopping_fashion_5_wnei_face 3a1
    show wnei_shopping_fashion_5_hero_face 1s0
    wnei "And that morning when we woke up after the sleepover...{w=[wt2]} Me and [C_Nam][fnamewsis][C_Off] helped you release all that super thick-milk blast!"

    wnei "But the super thick-milk blast would make a huge mess in here."

    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_hero_face 1s0

    pause

    play BGE "Crowd_Female.mp3"

    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_hero_face 1s1
    hero "{size=-8}Don't talk so loud.{w=[wt2]} Some people came to this fitting room!{/size}"

    show wnei_shopping_fashion_5_wnei_face 3a1
    show wnei_shopping_fashion_5_hero_face 1s0
    wnei "{size=-8}Then what do we do?{w=[wt2]} Without talking and without making a mess?{/size}"

    show wnei_shopping_fashion_5_wnei_face 3a0
    show wnei_shopping_fashion_5_hero_face 1s0
    with None

    menu:
        "Blowjob":

            show wnei_shopping_fashion_5_wnei_face 3a0
            show wnei_shopping_fashion_5_hero_face 1s1
            hero "{size=-8}You c{w=[wt1]}-could take care of it with your mouth{w=[wt2]}, and swallow so nothing spills.{/size}"

            show wnei_shopping_fashion_5_wnei_face 3a1
            show wnei_shopping_fashion_5_hero_face 1s0
            if 1 > 0:   # adjust threshold as needed

                wnei "{size=-8}Fine!{w=[wt4]} So, I better take all this clothes off so it doesn't mess everything up if it gets out of control.{/size}"

                show wnei_shopping_fashion_5_wnei_face 3a0
                with None

                scene wnei_shopping_fashion_7_bg a
                show fx_light
                with Fade(1, 0, 2)

                #wnei "{size=-8}There.{w=[wt2]} Better?{/size}"

                #hero "{size=-8}Y{w=[wt1]}-yeah...{/size}"

                pause

                scene wnei_shopping_fashion_7_bg b
                show fx_light
                with dissolve

                pause

            else:

                wnei "{size=-8}No.{w=[wt2]} Too messy.{w=[wt3]} We wait.{/size}"

                show wnei_shopping_fashion_5_wnei_face 3a0
                with None

                jump date_shop_fashion_wait

        "Just wait":
            label date_shop_fashion_wait:

                show wnei_shopping_fashion_5_wnei_face 3a0
                show wnei_shopping_fashion_5_hero_face 1s1
                hero "{size=-8}We just wait.{/size}"

                show wnei_shopping_fashion_5_wnei_face 3a1
                show wnei_shopping_fashion_5_hero_face 1s0
                wnei "{size=-8}...Okay.{/size}"

                show wnei_shopping_fashion_5_wnei_face 3a0
                with None

    $ add_stat("wnei", "love", 1)
    $ add_stat("wnei", "date_rom", 4)
    $ add_stat("wnei", "date_spi", 6)

    stop BGE fadeout 3

    scene bg_0 with Dissolve(2)

    hero "Okay.{w=[wt2]} We're done here.{w=[wt2]} Let's buy the bikini and go home."

    wnei "{bt}Yaaay!{/bt}"

    $ msg.msg(renpy.translate_string("Bikini supposedly purchased."))

    "That's a 'beta' version of this content. And its scenes and mechanics should be improved in future updates."

    return

# ----------------------------------------------------------------------------------------------------
label date_end(char_id="wsis", map_id="shopping", confirm=True):
# ----------------------------------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_139

    # The mall closing ends the date outright, so only a player-chosen finish is worth asking about.
    if confirm:

        menu:
            "Finish date?{fast}"

            "Yes":
                pass

            "No":
                return

    play BGM "audio/W2C - Memories.mp3"

    $ gametimemin += 60
    $ get_cvar(char_id, "know").append("Date_Shopping")
    scene bg_shopping_facade
    if char_id == "wnei":
        show WNEI at RC
    else:
        show WSIS at RC
    show HERO at LC
    with Fade(1, 0, 2)

    $ add_stat(char_id, "lust", -5 + (date_spi)/5)
    $ add_stat(char_id, "love", -5 + (date_rom+date_fun)/10)
    $ add_stat(char_id, "inti", (date_rom+date_fun+date_spi)/15)

    $ a_event_0 = max([date_rom, date_fun, date_spi])
    $ a_event_1 = 0 # 0 = None; 1 = Kiss Enabled

    $ date_active = False
    $ date_char = None
    $ date_venue = None
    $ date_done = []
    $ date_hud = True
    $ group_follow = []
    $ gametimemin += 30
                
    hide screen Date_UI

    $ hero_mood = "A1"
    hero "So{w=[wt2]}, let's go home?"

    if map_id == "shopping":

        if char_id == "wnei":

            $ wnei_fx = 1 if a_event_0 >= 40 else 0
            $ wnei_mood = "A1"

            if a_event_0 >= 40:
                wnei "{aw}Awww...{/aw}{w=[wt3]} Already?{w=[wt2]} Today was {bt}super duper{/bt} fun, [C_Nam][fnamehero][C_Off]!"
                hero "Glad you liked it."
                wnei "{gg}Tee-hee...{/gg}{w=[wt2]} Can we come back again?{w=[wt3]} Pleeease?"
                hero "Sure.{w=[wt2]} Next time."
                wnei "{bt}YAAAAY!!!{/bt}"
            else:
                $ wnei_mood = "O1"
                wnei "Hmm...{w=[wt3]} It's over?{w=[wt2]} Okay!{w=[wt2]} I'm hungry anyway."
                hero "Let's go home, then."

            $ date_rom = 0.0
            $ date_fun = 0.0
            $ date_spi = 0.0
            $ date_rom_bonus = 0.0
            $ date_fun_bonus = 0.0
            $ date_spi_bonus = 0.0

            # She walks home with him; a home arrival is all the plan asks for, so no rain scene like WSIS's.
            call action_walk(a="hero", b=char_id, c=30) from _call_action_walk_wnei
            call goto_home_facade from _call_goto_home_facade_wnei
            jump show_ui

        if char_id == "wsis":

            if a_event_0 >= 85 and a_event_0 == date_rom:
                $ add_stat(char_id, "love", 5)
                $ add_stat(char_id, "lust", 5)
                $ add_stat(char_id, "inti", 10)
                $ wsis_mood = "O2"
                $ wsis_fx = 1
                wsis "{bt}Ehhh...?{/bt}{w=[wt3]} A{w=[wt1]}-already?{w=[wt3]} Time went by so fast..."

                hero "Right?{w=[wt3]} But I'm happy you enjoyed, [C_Nam][hero_to_wsis][C_Off]."

                $ wsis_mood = "A1"
                wsis "Today was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} special{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} T{w=[wt1]}-thank you [C_Nam][wsis_to_hero][C_Off].{w=[wt4]} I love you!"

                $ hero_fx = 1
                menu:
                    "Say you love her":
                        hero "I love you too, [C_Nam][hero_to_wsis][C_Off]."
                        $ a_event_1 = 1

                    "Continue":
                        pass

            elif a_event_0 >= 85 and a_event_0 == date_spi:
                $ add_stat(char_id, "lust", 10)
                $ add_stat(char_id, "inti", 10)
                $ wsis_mood = "O2"
                $ wsis_fx = 1
                wsis "Hm?{w=[wt2]} huh{w=[wt2]}, oh{w=[wt2]}, H{w=[wt1]}-home already?{w=[wt3]} Oh{w=[wt2]}, o{w=[wt1]}-okay{w=[wt2]}, let's go."

                $ hero_mood = "A2"
                hero "{bt}Hmm...?{/bt}{w=[wt3]} You seem spaced out, [C_Nam][hero_to_wsis][C_Off].{w=[wt3]} What's in your mind?"

                $ wsis_fx = 2
                $ wsis_mood = "O3"
                wsis "{aw}M{w=[wt1]}-my m{w=[wt1]}-mind?{/aw}{w=[wt3]} T{w=[wt1]}-there's nothing pervert in my mind, you idiot!{w=[wt3]} It's you the pervert here!!!"

                $ hero_mood = "A1"
                hero "Oh{w=[wt2]}, so you're thinking in pervert stuff...?"

                $ wsis_mood = "O2"
                wsis "Eh!?{w=[wt2]} N{w=[wt1]}-no!!!{w=[wt3]} Shut up and let's go home!"

                show WSIS at OR_slow

            elif a_event_0 >= 85 and a_event_0 == date_fun:
                $ add_stat(char_id, "love", 10)
                $ add_stat(char_id, "inti", 10)
                $ wsis_mood = "O2"
                $ wsis_fx = 0
                wsis "{bt}Nooo...{/bt}{w=[wt3]} Five more minutes!"

                $ hero_mood = "A2"
                hero "That's what you say when you're losing."

                $ wsis_mood = "A2"
                wsis "I have {b}never{/b} lost to you.{w=[wt3]} {gg}Pff...{/gg}{w=[wt2]} Okay{w=[wt1]}, once.{w=[wt2]} You were seven and I let you win."

                $ wsis_mood = "A1"
                $ wsis_fx = 1
                wsis "Fine.{w=[wt3]} Home."

            elif a_event_0 >= 40 and a_event_0 == date_rom:
                $ add_stat(char_id, "love", 1)
                $ add_stat(char_id, "lust", 1)
                $ add_stat(char_id, "inti", 2)
                $ wsis_mood = "A2"
                $ wsis_fx = 1
                wsis "A{w=[wt1]}-already...?{w=[wt4]} S{w=[wt1]}-sure.{w=[wt3]} Let's go home."

                hero "That means you must have enjoyed.{w=[wt3]} I'm glad for that, [C_Nam][hero_to_wsis][C_Off]!"

                $ wsis_mood = "O2"
                wsis "Today wasn't bad.{w=[wt3]} That's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} that's all I'm saying{w=[wt1]}, so don't make that face."

                menu:
                    "Tell her you love her":

                        $ hero_mood = "A1"
                        hero "I love you, [C_Nam][hero_to_wsis][C_Off]!"

                        $ wsis_mood = "O1"
                        $ wsis_fx = 2
                        wsis "{aw}Wh...!?{/aw}{w=[wt3]} Y{w=[wt1]}-you can't just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} out {b}here{/b}!?{w=[wt2]} In front of a {b}mall{/b}!?"

                        hero "I can say it again inside{w=[wt1]}, if the mall is the problem.{w=[wt3]} I can love you anywhere!"

                        $ wsis_mood = "O2"
                        wsis "{aw}T{w=[wt1]}-that is {b}not{/b} the problem!{/aw}{w=[wt3]} D{w=[wt1]}-don't go thinking I'll be all happy just because you made a sappy comment to me or something like that, okay?{w=[wt3]} J{w=[wt1]}-just because I went out with you doesn't mean I love you too or anything, you idiot.{w=[wt2]} {aw}Hmph...!{/aw}{w=[wt4]} Why this smile?{w=[wt4]} I{w=[wt1]}-I'm serious...!"

                        $ add_stat(char_id, "love", 4)
                        $ add_stat(char_id, "inti", 3)
                        $ a_event_1 = 1

                    "Continue":
                        show HERO at OR_heavy

                        $ hero_mood = "A1"
                        hero "Yeah.{w=[wt3]} Let's go, [C_Nam][hero_to_wsis][C_Off]."

                        show WSIS at OR_heavy
                        $ wsis_mood = "A2"
                        wsis "Wait for me!"

            elif a_event_0 >= 40 and a_event_0 == date_spi:
                $ add_stat(char_id, "lust", 2)
                $ add_stat(char_id, "inti", 2)
                $ wsis_mood = "O1"
                $ wsis_fx = 1
                wsis "Home.{w=[wt2]} Right.{w=[wt3]} Somewhere cold{w=[wt1]}, preferably."

                $ hero_mood = "A2"
                hero "You've gone red again, [C_Nam][hero_to_wsis][C_Off]."

                $ wsis_mood = "O2"
                $ wsis_fx = 2
                wsis "{aw}It's the air conditioning!{/aw}{w=[wt3]} This place has terrible air conditioning{w=[wt1]}, everyone knows that."

                $ wsis_mood = "A2"
                wsis "{aw}Hmph...!{/aw}{w=[wt2]} Just walk{w=[wt1]}, pervert.{w=[wt3]} And keep your hands where I can see them."

            elif a_event_0 >= 40 and a_event_0 == date_fun:
                $ add_stat(char_id, "love", 2)
                $ add_stat(char_id, "inti", 2)
                $ wsis_mood = "A1"
                $ wsis_fx = 0
                wsis "Sure.{w=[wt3]} That was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} fine.{w=[wt3]} Better than fine{w=[wt1]}, but don't push it."

                $ hero_mood = "A2"
                hero "I'll take better than fine."

                $ wsis_mood = "A2"
                wsis "You'd take anything.{w=[wt3]} {gg}Pff...{/gg}{w=[wt2]} Next time {b}I{/b} pick where we eat, though."

                $ hero_mood = "A1"
                hero "Next time?"

                $ wsis_mood = "O2"
                $ wsis_fx = 1
                wsis "{aw}If{w=[wt1]} there is one!{/aw}{w=[wt3]} Hypothetically.{w=[wt2]} Don't write it down anywhere."

            else:
                $ wsis_mood = "O1"
                $ wsis_fx = 0
                wsis "Please."

                $ hero_mood = "O1"
                hero "That bad?"

                $ wsis_mood = "O2"
                wsis "I walked around a mall for hours{w=[wt1]}, [C_Nam][wsis_to_hero][C_Off].{w=[wt3]} I could have been raiding with people who at least plan their runs.{w=[wt3]} Come on!{w=[wt3]} Hurry up!"

                show WSIS at OR_slow

                $ hero_mood = "O1"
                hero "{bt}Ehhh...?{/bt}"

            $ date_rom = 0.0
            $ date_fun = 0.0
            $ date_spi = 0.0
            $ date_rom_bonus = 0.0
            $ date_fun_bonus = 0.0
            $ date_spi_bonus = 0.0

            if a_event_1 == 1:
                menu:
                    "Kiss her":
                        call date_end_kiss(char_id="wsis", map_id="shopping") from _call_date_end_kiss

                        $ hero_mood = "A1"
                        $ wsis_mood = "O1"
                        $ hero_fx = 1
                        $ wsis_fx = 1

                        scene bg_shopping_facade
                        show WSIS at LC
                        show HERO at CC
                        with Fade(1, 0, 2)

                        wsis "You idiot{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I won't say it again{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} I love you, [C_Nam][wsis_to_hero][C_Off].{w=[wt4]}{nw}"

                        show WSIS at OR_slow

                        wsis "You idiot{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I won't say it again{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} I love you, [C_Nam][wsis_to_hero][C_Off].{w=[wt4]}{fast} {aw}Hurry!{w=[wt3]} L{w=[wt1]}-let's go home!{/aw}"

                        show HERO at OR_heavy with None

                    "Go home":
                        pass

            call date_end_travel(char_id="wsis", map_id="shopping") from _call_date_end_travel

# ----------------------------------------------------------------------------------------------------
label date_end_kiss(char_id="wsis", map_id="shopping"):
# ----------------------------------------------------------------------------------------------------

    if wsis_quest_11 == 0:
        play SE1 "JingleRight2.mp3"
        $ msg.msg(renpy.translate_string("⭐ Intimacy cap removed"))
        $ xp_now += 20
        $ msg.msg(renpy.translate_string("XP [C_Pos]+ 20[C_Off]."))

    $ wsis_quest_11 = 1
    $ wsis_inti_cap = 100

    stop BGM fadeout 3

    scene bg_1 with Dissolve(2)

    play BGM "audio/W2C - Romance.mp3"

    if perk_cha_sex >= 1:
       $ add_stat("wsis", "lust", 5)
    $ add_stat("wsis", "love", 2)
    $ add_stat("hero", "cha_sex", 2)
    $ add_stat("wsis", "inti", 0.1)
    $ gametimemin += 10

    scene bg_1
    show action_wsis_kiss_body
    show action_wsis_kiss_wear dressy
    show action_wsis_kiss_hero_face u0
    show action_wsis_kiss_wsis_face u0
    show action_wsis_kiss_wsis_fg
    with Dissolve(5)

    pause

    return

# ----------------------------------------------------------------------------------------------------
label date_end_travel(char_id="wsis", map_id="shopping"):
# ----------------------------------------------------------------------------------------------------
    if wsis_lust < 60 and wsis_quest_1 >= 1:
        call action_walk(a="hero", b=char_id, c=30) from _call_action_walk_2
        call goto_home_facade from _call_goto_home_facade_2
        $ StartAct("wsis", (("changing", "home"), 0), True)
        $ StartAct("wsis", (("staying", "bedroom_wsis"), 0), True)
        jump show_ui

    else:
        stop BGM fadeout 3

        scene bg_0
        if gametimehour < 15:
            show action_walk_bg_1 sky_morning
        elif gametimehour < 18:
            show action_walk_bg_1 sky_afternoon
        else:
            show action_walk_bg_1 sky_night
        show action_walk_bg street
        show action_walk_hero_body 1
        show action_walk_hero_wear 1dressy
        if wsis_inti >= 20 and wsis_love >= 20:
            show action_walk_wsis_body 2
            show action_walk_wsis_wear 2dressy
        else:
            show action_walk_wsis_body 1
            show action_walk_wsis_wear 1dressy

        pause

        play SE1 "Thunder.ogg"

        show action_walk_bg_1 sky_cloudy with Dissolve(3)

        play BGE "Rain (Low).mp3"

        show fx_rain 10 1 1 # angle, power, speed
            
        pause

        play BGE "Rain (Heavy).mp3"

        scene bg_0
        show action_walk_bg_1 sky_cloudy
        show action_walk_bg street

        show action_jog_wsis_1_hair 1 at SXY2(S=0.9, X=-50, Y=-0)
        show action_jog_wsis_1_body at SXY2(S=0.9, X=-50, Y=-0)
        show action_jog_wsis_1_wear dressy at SXY2(S=0.9, X=-50, Y=-0)
        show action_jog_wsis_1_face o0 at SXY2(S=0.9, X=-50, Y=-0)
        show action_jog_wsis_1_fg at SXY2(S=0.9, X=-50, Y=-0)

        show action_jog_hero_1_body at SXY2(S=1, X=400, Y=-200)
        show action_jog_hero_1_wear dressy at SXY2(S=1, X=400, Y=-200)
        show action_jog_hero_1_face o0 at SXY2(S=1, X=400, Y=-200)

        show fx_rain 20 2 1 # angle, power, speed

        play BGM "audio/W2C - Adrenaline.mp3"
            
        pause

        scene bg_0 with dissolve

        play SE1 "DoorOpen2.ogg"

        pause(1.5)

        scene wsis_bath1_bg
        show wsis_bath1_hero_body 1
        show wsis_bath1_hero_wear 1_dressy
        show wsis_bath1_hero_face 1o0
        show wsis_bath1_wsis_body 1
        show wsis_bath1_wsis_wear 1_dressy
        show wsis_bath1_wsis_face 1o0
        show wsis_bath1_wsis_fg

        with Dissolve(2)

        show wsis_bath1_wmom_body 1 at RC
        show wsis_bath1_wmom_bodywear 1_casual at RC
        with dissolve

        pause(1)

        $ wmom_mood = "O1"

        wmom "{bt}Ehhh...?{/bt}{w=[wt3]} My dears!{w=[wt4]}{nw}"

        show wsis_bath1_wmom_body 2 at RC
        show wsis_bath1_wmom_bodywear 2_casual at RC
        show wsis_bath1_wmom_arm 1 at RC
        show wsis_bath1_wmom_armwear 1_casual at RC

        wmom "{bt}Ehhh...?{/bt} My dears!{fast} Nice, huh?{w=[wt3]} So{w=[wt2]}, you two went walking around without taking an umbrella!"

        show wsis_bath1_wsis_face 1o1
        wsis "The weather was nice when we left, [C_Nam]Mom[C_Off].{w=[wt3]} The rain just came out of nowhere, and instantlly got super heavy!{w=[wt3]} It's not our fault."

        show wsis_bath1_wsis_face 1o0
        wmom "It is!{w=[wt3]} That's just how rain is.{w=[wt2]} How many times have I told you that we always need to carry an umbrella wherever we go?{w=[wt3]} I don't wanna see anyone in this house getting sick because of a rain!"
        
        show wsis_bath1_wsis_face 1o1
        wsis "{bt}Fine...{w=[wt2]} Fine...{/bt}{w=[wt3]} I'm gonna take a quick shower so [C_Nam][wsis_about_hero][C_Off] don't wait too much."
        
        show wsis_bath1_wsis_face 1o0
        wmom "Huh!?{w=[wt2]} No, miss.{w=[wt3]} The little princess {aw}WON'T{/aw} leave her brother waiting all soaked out here, okay?{w=[wt4]} YOU TWO will go {b}TO{w=[wt1]}-GE{w=[wt1]}-THER{/b}!"

        show wsis_bath1_wsis_face 1s1
        show wsis_bath1_hero_face 1s1
        $ a_check_1 = str(fnamehero)+" and "+str(fnamewsis)
        sup1 "{vspace=30}{pa}{size=60}EHHH...!?{/size}{/pa}"

        show wsis_bath1_wsis_face 1s0
        show wsis_bath1_hero_face 1s0
        wmom "If you don't want me to cut off your internet and computer access{w=[wt3]}, to the bathroom{w=[wt3]}{nw}"

        show wsis_bath1_wmom_body 2 at CC_slow
        show wsis_bath1_wmom_bodywear 2_casual at CC_slow
        show wsis_bath1_wmom_arm 2 at CC_slow
        show wsis_bath1_wmom_armwear 2_casual at CC_slow
        wmom "If you don't want me to cut off your internet and computer access, to the bathroom{w=[wt3]}{fast}{pr}{aw}RIGHT{w=[wt2]} NOW!!!{/aw}"

        stop BGM fadeout 10

        show wsis_bath1_hero_body at OR_heavy
        show wsis_bath1_hero_wear at OR_heavy
        show wsis_bath1_hero_face at OR_heavy
        show wsis_bath1_wsis_body at OR_heavy
        show wsis_bath1_wsis_wear at OR_heavy
        show wsis_bath1_wsis_face at OR_heavy
        show wsis_bath1_wsis_fg at OR_heavy

        pause(1)

        hide wsis_bath1_hero_body
        hide wsis_bath1_hero_wear
        hide wsis_bath1_hero_face
        hide wsis_bath1_wsis_body
        hide wsis_bath1_wsis_wear
        hide wsis_bath1_wsis_face
        hide wsis_bath1_wsis_fg
        with Dissolve(1)

        pause(1)

        show wsis_bath1_wmom_body 1
        show wsis_bath1_wmom_bodywear 1_casual
        hide wsis_bath1_wmom_arm
        hide wsis_bath1_wmom_armwear
        with dissolve

        $ wmom_mood = "O1"

        pause(1)

        wmom "{bt}Phew...{/bt}{w=[wt4]} It hurts me so much to have to act this way{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} What do I do with these two...?"

        stop BGE fadeout 5

        $ StartAct("wsis", [(("moving", "home"), 0), (("staying", "bathroom"), 0)], True)
        $ StartAct("wmom", [(("moving", "home"), 0), (("staying", "living_room"), 0)], True)
        $ hero_map = MAP_DATA["home"]["name"] + " - " + MAP_DATA["home"]["map"]["bathroom"]["name"]

        jump wsis_bath_1

    return
