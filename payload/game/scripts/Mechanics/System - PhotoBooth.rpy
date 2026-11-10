# Photobooth — the player composes a photo and keeps it in the phone gallery.
#
# The whole thing is NAME-DRIVEN: every option the player can switch is discovered from the image names in `images/Photo/`, so adding a background, an overlay, a new face or a whole new pose set is dropping files in, never a code edit. `PHOTOBOOTH_LAYERS` is the only ordering statement.
#
# A saved photo is DATA, not pixels: `photo_shots` stores the choices and the gallery recomposes the shot from them. That keeps it save-safe (no files written, nothing to lose on a reload) and means an old photo picks up redrawn art for free. `cellbg` holds a "PHOTO_<id>" token, so shots never overwrite each other.

# ----------------------------------------------------------------------------------------------------
# DATA
# ----------------------------------------------------------------------------------------------------
# Layer stack for a pose set, back to front. Each entry: (part, kind, default)
#   part    - the image name after `photobooth_<set>_`, e.g. "hero_face" -> `photobooth_heroandwsis_1_hero_face 1`
#   kind    - "fixed"  : one image, no attribute (`photobooth_<set>_body`)
#             "wear"   : attribute is the character's outfit, so the photo shows what they are wearing
#             "pick"   : attribute the PLAYER switches (an option row appears for it)
#             "auto"   : attribute picked once and kept (variants that exist but are not player-facing)
#   default - fallback attribute when nothing else resolves
define PHOTOBOOTH_LAYERS = [
    ("outline",        "wear",  "dressy"),
    ("wsis_hair_bg",   "auto",  "1"),
    ("body",           "fixed", None),
    ("hero_wear",      "wear",  "dressy"),
    ("wsis_wear",      "wear",  "dressy"),
    ("hero_hair",      "auto",  "1"),
    ("wsis_hair_fg",   "auto",  "1"),
    ("hero_face",      "pick",  "1"),
    ("wsis_face",      "auto",  "1"),
    ("wsis_hair_wear", "wear",  "dressy"),
]

# Which character owns each "wear" layer, so the layer can follow that character's outfit.
define PHOTOBOOTH_WEAR_OWNER = {"outline": "hero", "hero_wear": "hero", "wsis_wear": "wsis", "wsis_hair_wear": "wsis"}

define PHOTOBOOTH_SQUARE = 1920          # the pose art is a square; the frame is a crop out of it
define PHOTOBOOTH_W = 1920               # long side of a finished photo
define PHOTOBOOTH_H = 1080               # short side of a finished photo
define PHOTOBOOTH_PAN = 0.2              # horizontal photos: where the 1080-tall window sits on the square (0 = heads, 1 = feet)
define PHOTOBOOTH_PANX = 0.5             # horizontal photos: where the window sits across the square (0 = left, 1 = right)
define PHOTOBOOTH_ZOOM = 2.0             # horizontal photos: how close the characters are, and the default
define PHOTOBOOTH_ZOOM_MIN = 1.0         # 1x is the whole width of the square art in frame
define PHOTOBOOTH_ZOOM_MAX = 2.0         # the far end of the zoom bar

# The phone's wallpaper window (the mask in the gallery/home screens), used to work out how far a photo may be scaled DOWN there: the drawn art's floor of 0.9 never lets a vertical photo fit.
define CELL_WALL_W = 620
define CELL_WALL_H = 1080
define CELL_WALL_FLOOR = 0.9

# Booth controls. Every row is the same total width, split arrow / label / arrow, and the pan bar and the Shot+Cancel pair match it — that shared width is what makes the column read as one block.
define PHOTOBOOTH_UI_W = 700             # total width of a control row
define PHOTOBOOTH_UI_ARROW = 120         # fixed width of each arrow cell; the label takes what is left
define PHOTOBOOTH_UI_SIZE = 60           # label size, set for mobile legibility
define PHOTOBOOTH_UI_SIZE_S = 40         # caption size, for the slider labels
define PHOTOBOOTH_UI_OUTLINE = [(4, "#000000", 0, 0)]   # black outline, so a label stays readable on any photo

# Player-facing names for the option rows. A part with no entry falls back to its own name.
define PHOTOBOOTH_LABELS = {"bg": "Background", "fg": "Overlay", "hero_face": "Expression"}

# ----------------------------------------------------------------------------------------------------
# OPTIONS — read off the image names, never a hard-coded list
# ----------------------------------------------------------------------------------------------------
default photo_cfg = {}      # the booth session in progress — a plain default so a save taken inside the booth reloads cleanly
default photo_last = 0      # id of the most recent shot, for a scene that wants to talk about it
default photo_view = 0      # gallery view mode for a vertical photo: 0 whole · 1 turned sideways · 2 blown up and draggable

init python:

    _photo_cache = {}       # composed photos, keyed by their choices, so the gallery does not rebuild a stack every frame

    # --------------------------------------------------
    def Photo_Attrs(prefix): # Every attribute drawn for an image tag, e.g. "photobooth_bg" -> ["color_blue", ...]
    # --------------------------------------------------
        out = []
        for name in renpy.list_images():
            parts = name.split(" ", 1)
            if parts[0] == prefix and len(parts) == 2 and parts[1] not in out:
                out.append(parts[1])
        out.sort()
        return out

    # --------------------------------------------------
    def Photo_Options(pose_set): # The switchable option rows for a pose set: [(part, [attrs...]), ...]
    # --------------------------------------------------
        # A "pick" layer only earns a row when the art gives it something to switch between.
        rows = []
        for part, kind, fallback in PHOTOBOOTH_LAYERS:
            if kind != "pick":
                continue
            attrs = Photo_Attrs("photobooth_" + pose_set + "_" + part)
            if len(attrs) > 1:
                rows.append((part, attrs))
        return rows

    # --------------------------------------------------
    def Photo_Layer(pose_set, part, kind, fallback, cfg): # One layer's image name, or None when it has no art
    # --------------------------------------------------
        base = "photobooth_" + pose_set + "_" + part

        if kind == "fixed":
            return base if renpy.has_image(base, exact=True) else None

        attrs = Photo_Attrs(base)
        if not attrs:
            return None

        if kind == "pick":
            want = cfg.get("picks", {}).get(part, fallback)
        elif kind == "wear":
            # The layer follows what that character was WEARING WHEN THE PHOTO WAS TAKEN — stamped into the config by Photo_NewConfig — so an old shot never re-dresses itself out of today's wardrobe.
            char = PHOTOBOOTH_WEAR_OWNER.get(part, "hero")
            want = cfg.get("wears", {}).get(char) or getattr(store, char + "_wear", None) or fallback
        else:
            want = fallback

        for a in (want, fallback):
            if a in attrs:
                return base + " " + a
        return base + " " + attrs[0]

    # --------------------------------------------------
    def Photo_Frame(cfg): # (width, height) of the finished photo — the square aspect is deliberately not offered
    # --------------------------------------------------
        if cfg.get("aspect", "v") == "h":
            return (PHOTOBOOTH_W, PHOTOBOOTH_H)
        return (PHOTOBOOTH_H, PHOTOBOOTH_W)

    # --------------------------------------------------
    def Photo_Key(cfg): # Everything that changes what a photo looks like, as a hashable key
    # --------------------------------------------------
        picks = tuple(sorted(cfg.get("picks", {}).items()))
        wears = tuple(sorted(cfg.get("wears", {}).items()))
        frame = tuple(round(cfg.get(k, d), 3) for k, d in (("pan", PHOTOBOOTH_PAN), ("panx", PHOTOBOOTH_PANX), ("zoom", PHOTOBOOTH_ZOOM)))
        return (cfg.get("set"), cfg.get("bg"), cfg.get("fg"), cfg.get("aspect"), frame, picks, wears)

    # --------------------------------------------------
    def Photo_Compose(cfg): # The photo itself, as a displayable — used by the booth AND by the gallery
    # --------------------------------------------------
        # bg and fg are drawn vertical, so a horizontal photo turns them a quarter turn. The pose art is square and gets cropped to the frame, centred, which is what makes one drawing serve both aspects.
        key = Photo_Key(cfg)
        if key in _photo_cache:
            return _photo_cache[key]

        pose_set = cfg.get("set", "heroandwsis_1")
        w, h = Photo_Frame(cfg)
        horizontal = (w > h)

        def dressing(name): # a bg/fg plate, turned to match the frame
            if not name:
                return None
            d = renpy.displayable(name)
            if horizontal:
                d = Transform(d, rotate=90)
            return Transform(d, xalign=0.5, yalign=0.5)

        layers = []
        for part, kind, fallback in PHOTOBOOTH_LAYERS:
            name = Photo_Layer(pose_set, part, kind, fallback, cfg)
            if name:
                layers.append(renpy.displayable(name))

        # The window cut out of the square. A horizontal photo is framed by the player: `zoom` decides how close the characters are and `panx`/`pan` slide the window over them — all of which moves the CHARACTERS only, since the backdrop and overlay are their own plates filling the frame. A vertical photo takes the centre of the square at 1x, unchanged.
        square = PHOTOBOOTH_SQUARE
        stack = Fixed(*layers, xysize=(square, square)) if layers else Null(square, square)

        if horizontal:
            z = min(PHOTOBOOTH_ZOOM_MAX, max(PHOTOBOOTH_ZOOM_MIN, cfg.get("zoom", PHOTOBOOTH_ZOOM)))
            side = int(square * z)
            # The zoom is its own Transform: within one Transform a crop is applied BEFORE the zoom, which would cut the window out of the unscaled art and then blow the window up instead.
            if z != 1.0:
                stack = Transform(stack, zoom=z)
            cx = int((side - w) * min(1.0, max(0.0, cfg.get("panx", PHOTOBOOTH_PANX))))
            cy = int((side - h) * min(1.0, max(0.0, cfg.get("pan", PHOTOBOOTH_PAN))))
        else:
            cx, cy = (square - w) // 2, (square - h) // 2

        stack = Transform(stack, crop=(cx, cy, w, h))

        out = []
        bg = dressing("photobooth_bg " + cfg["bg"]) if cfg.get("bg") else None
        fg = dressing("photobooth_fg " + cfg["fg"]) if cfg.get("fg") else None
        if bg:
            out.append(bg)
        out.append(Transform(stack, xalign=0.5, yalign=0.5))
        if fg:
            out.append(fg)

        photo = Fixed(*out, xysize=(w, h))
        # Dragging the pan bar mints a new key per step, so the cache is bounded rather than unbounded.
        if len(_photo_cache) > 200:
            _photo_cache.clear()
        _photo_cache[key] = photo
        return photo

    # --------------------------------------------------
    def Photo_NewConfig(pose_set="heroandwsis_1"): # A fresh booth session — random backdrop, no overlay
    # --------------------------------------------------
        bgs = Photo_Attrs("photobooth_bg")
        cfg = {
            "set"    : pose_set,
            "bg"     : random.choice(bgs) if bgs else None,
            "fg"     : None,
            "aspect" : "v",
            "pan"    : PHOTOBOOTH_PAN,
            "panx"   : PHOTOBOOTH_PANX,
            "zoom"   : PHOTOBOOTH_ZOOM,
            "picks"  : {},
            # What everyone is wearing right now, frozen — the photo keeps the outfit of the day it was taken.
            "wears"  : dict((c, getattr(store, c + "_wear", None)) for c in set(PHOTOBOOTH_WEAR_OWNER.values())),
        }
        for part, attrs in Photo_Options(pose_set):
            cfg["picks"][part] = attrs[0]
        return cfg

    # --------------------------------------------------
    def Photo_Cycle(cfg, part, step): # Step one option row, wrapping around
    # --------------------------------------------------
        # `bg` and `fg` are rows too; fg carries a None entry, since "no overlay" is a real choice.
        if part == "bg":
            attrs = Photo_Attrs("photobooth_bg")
        elif part == "fg":
            attrs = [None] + Photo_Attrs("photobooth_fg")
        else:
            attrs = dict(Photo_Options(cfg.get("set", "heroandwsis_1"))).get(part, [])

        if not attrs:
            return

        cur = cfg.get(part) if part in ("bg", "fg") else cfg.get("picks", {}).get(part)
        i = attrs.index(cur) if cur in attrs else 0
        new = attrs[(i + step) % len(attrs)]

        if part in ("bg", "fg"):
            cfg[part] = new
        else:
            cfg.setdefault("picks", {})[part] = new
        return

    # --------------------------------------------------
    def Photo_Flip(cfg): # Vertical <-> horizontal
    # --------------------------------------------------
        cfg["aspect"] = "h" if cfg.get("aspect", "v") == "v" else "v"
        return

    # --------------------------------------------------
    def Photo_FitZoom(w, h): # The largest zoom that still shows a whole w x h photo on screen
    # --------------------------------------------------
        return min(config.screen_width * 1.0 / w, config.screen_height * 1.0 / h)

    # --------------------------------------------------
    def Photo_Preview(cfg): # The booth's preview: the photo as big as the screen will take it
    # --------------------------------------------------
        w, h = Photo_Frame(cfg)
        return Transform(Photo_Compose(cfg), zoom=Photo_FitZoom(w, h), xalign=0.5, yalign=0.5)

    # --------------------------------------------------
    def Photo_Save(cfg): # Keep the shot: a new gallery entry that never replaces an older one
    # --------------------------------------------------
        shot = dict(cfg)
        shot["picks"] = dict(cfg.get("picks", {}))
        shot["wears"] = dict(cfg.get("wears", {}))
        # The id counts every photo ever taken, so deleting or reordering can never collide with an old token.
        shot["id"] = max([s.get("id", 0) for s in photo_shots] + [0]) + 1
        # The moment it records, for a caption or a memory check later.
        shot["day"] = gametimeday
        shot["time"] = gametimeclock
        shot["chars"] = ["hero", "wsis"]

        photo_shots.append(shot)
        cellbg.insert(1, "PHOTO_" + str(shot["id"]))
        msg.msg(renpy.translate_string("New photo added to phone Gallery"))
        return shot["id"]

    # --------------------------------------------------
    def Photo_ShowShot(shot_id, flash=True): # Put a saved photo on screen for the scene to talk over
    # --------------------------------------------------
        # On BLACK, always: a vertical photo cannot cover a 16:9 screen, and an empty layer renders as Ren'Py's transparency checkerboard. Any scene showing a player photo should come through here.
        renpy.scene()
        renpy.show("photo_shot_bg", what=Solid("#000000"))
        renpy.show("photo_shot", what=Cell_Full("PHOTO_" + str(shot_id)), at_list=([store.PhotoShot] if flash else []))
        return

    # --------------------------------------------------
    def Photo_Shot(shot_id): # A saved shot's config, or None
    # --------------------------------------------------
        for s in photo_shots:
            if s.get("id") == shot_id:
                return s
        return None

    # ------------------------------------------------------------------ gallery plumbing
    # Every gallery site used to build `"images/UI/CellphoneBG/<name>.webp"` by hand. It goes through these two helpers instead, so a "PHOTO_<id>" token resolves to a composed displayable and everything else behaves exactly as before.

    # --------------------------------------------------
    def Cell_Img(name): # A gallery entry as a displayable
    # --------------------------------------------------
        name = str(name)
        if name.startswith("PHOTO_"):
            shot = Photo_Shot(int(name[6:]))
            if shot:
                return Photo_Compose(shot)
            return Null(PHOTOBOOTH_W, PHOTOBOOTH_H)
        return "images/UI/CellphoneBG/" + name + ".webp"

    # --------------------------------------------------
    def Cell_Full(name): # A gallery entry filling the screen, letterboxed if it is a vertical photo
    # --------------------------------------------------
        shot = Cell_Photo(name)
        if shot:
            w, h = Photo_Frame(shot)
            return Transform(Photo_Compose(shot), zoom=Photo_FitZoom(w, h), xalign=0.5, yalign=0.5)
        return Cell_Img(name)

    # --------------------------------------------------
    def Cell_Photo(name): # The saved shot behind a gallery entry, or None when it is a drawn image
    # --------------------------------------------------
        name = str(name)
        return Photo_Shot(int(name[6:])) if name.startswith("PHOTO_") else None

    # --------------------------------------------------
    def Cell_Tall(name): # Is this gallery entry a VERTICAL player photo? (the one that needs view modes)
    # --------------------------------------------------
        shot = Cell_Photo(name)
        if not shot:
            return False
        w, h = Photo_Frame(shot)
        return h > w

    # --------------------------------------------------
    def Cell_View(name, mode=0): # A vertical photo, shown one of three ways in the gallery viewer
    # --------------------------------------------------
        # 0 = whole photo on a black screen · 1 = turned a quarter turn, so it fills the screen (handy on a phone held sideways) · 2 = blown up to the screen's width, for dragging up and down through it.
        shot = Cell_Photo(name)
        if not shot:
            return Cell_Full(name)

        d = Photo_Compose(shot)
        w, h = Photo_Frame(shot)

        sw, sh = config.screen_width, config.screen_height

        if mode == 1:
            # Turned sideways it must COVER the screen, so the zoom is worked out from the rotated dimensions (a quarter turn swaps them) and the result is centred in a screen-sized frame — rotation pads its own bounding box, so it cannot be left to place itself.
            return Fixed(Transform(d, rotate=90, zoom=max(sw * 1.0 / h, sh * 1.0 / w), xalign=0.5, yalign=0.5), xysize=(sw, sh))
        if mode == 2:
            return Transform(d, zoom=sw * 1.0 / w, xalign=0.5)
        return Transform(d, zoom=Photo_FitZoom(w, h), xalign=0.5, yalign=0.5)

    # --------------------------------------------------
    def Cell_WZoom(name, wz): # Wallpaper zoom for the phone screens, floor included
    # --------------------------------------------------
        # The drawn art is 1920x1080 and 0.9 is its hand-tuned floor. A VERTICAL photo is only 1080 wide and would never fit the 620-wide window at that floor, so its floor is the zoom that shows all of it.
        floor = CELL_WALL_FLOOR
        shot = Cell_Photo(name)
        if shot:
            w, h = Photo_Frame(shot)
            if h > w:
                floor = min(CELL_WALL_W * 1.0 / w, CELL_WALL_H * 1.0 / h)
        return floor + wz / 25.0

    # --------------------------------------------------
    def Cell_Thumb(name): # A gallery entry as a square thumbnail
    # --------------------------------------------------
        # The drawn photos are 1920x1080 and their thumbnail window was hand-picked; a composed photo is cropped from its own centre instead, so a vertical shot thumbnails correctly too.
        name = str(name)
        if name.startswith("PHOTO_"):
            shot = Photo_Shot(int(name[6:]))
            if not shot:
                return Null(1000, 1000)
            w, h = Photo_Frame(shot)
            side = min(w, h)
            return Transform(Photo_Compose(shot), crop=((w - side) // 2, (h - side) // 2, side, side), zoom=1000.0 / side)
        return im.Crop("images/UI/CellphoneBG/" + name + ".webp", (420, 0, 1000, 1000))

# ----------------------------------------------------------------------------------------------------
# BOOTH SCREEN
# ----------------------------------------------------------------------------------------------------
screen photobooth(cfg):

    modal True
    zorder 100

    # Solid black, not a scrim: while he is framing the shot the room behind must not show through, so the only thing on screen is what the photo will actually contain.
    add Solid("#000000")

    # The photo as it will be kept, as large as the screen will take it.
    add Photo_Preview(cfg)

    # Every control in one column: orientation first (with the pan bar under it while the photo is horizontal), then a row per switchable option built from the art, then Shot and Cancel.
    vbox:
        xalign 0.02
        yalign 0.5
        spacing 20

        use photobooth_row("Rotate", [Function(Photo_Flip, cfg), Function(renpy.restart_interaction)], [Function(Photo_Flip, cfg), Function(renpy.restart_interaction)])

        # A horizontal photo is framed by hand: how close, and where the window sits on the square art.
        if cfg.get("aspect", "v") == "h":
            use photobooth_bar("Zoom", DictValue(cfg, "zoom", min=PHOTOBOOTH_ZOOM_MIN, max=PHOTOBOOTH_ZOOM_MAX))
            use photobooth_bar("Sideways", DictValue(cfg, "panx", range=1.0))
            use photobooth_bar("Up / down", DictValue(cfg, "pan", range=1.0))

        for row_part in ["bg", "fg"] + [p for p, a in Photo_Options(cfg.get("set", "heroandwsis_1"))]:
            use photobooth_row(PHOTOBOOTH_LABELS.get(row_part, row_part.replace("_", " ").capitalize()), [Function(Photo_Cycle, cfg, row_part, -1), Function(renpy.restart_interaction)], [Function(Photo_Cycle, cfg, row_part, 1), Function(renpy.restart_interaction)])

        hbox:
            xsize PHOTOBOOTH_UI_W
            use photobooth_button("Shot", Return("shot"))
            use photobooth_button("Cancel", Return("leave"))

# One control row: arrow, label, arrow, at fixed widths adding up to PHOTOBOOTH_UI_W. Every booth control is built from this or its sibling below, so the whole column lines up.
screen photobooth_row(row_label, left_action, right_action):

    hbox:
        xsize PHOTOBOOTH_UI_W

        fixed:
            xysize (PHOTOBOOTH_UI_ARROW, 90)
            imagebutton at Zoom_15:
                xalign 0.5
                yalign 0.5
                idle "images/UI/Arrow_4 IDLE.webp"
                hover "images/UI/Arrow_4 HOVER.webp"
                action left_action

        fixed:
            xysize (460, 90)
            text renpy.translate_string("[row_label]"):
                size PHOTOBOOTH_UI_SIZE
                outlines PHOTOBOOTH_UI_OUTLINE
                xsize PHOTOBOOTH_UI_W - PHOTOBOOTH_UI_ARROW * 2
                text_align 0.5
                xalign 0.5
                yalign 0.5

        fixed:
            xysize (PHOTOBOOTH_UI_ARROW, 90)
            imagebutton at Zoom_15:
                xalign 0.5
                yalign 0.5
                idle "images/UI/Arrow_6 IDLE.webp"
                hover "images/UI/Arrow_6 HOVER.webp"
                action right_action

# A labelled slider, the same width as a control row so the column stays square.
screen photobooth_bar(bar_label, bar_value):

    vbox:
        xsize PHOTOBOOTH_UI_W
        spacing 5

        text renpy.translate_string("[bar_label]"):
            size PHOTOBOOTH_UI_SIZE_S
            outlines PHOTOBOOTH_UI_OUTLINE
            xsize PHOTOBOOTH_UI_W
            text_align 0.5

        bar:
            value bar_value
            xsize PHOTOBOOTH_UI_W

# Half-width button, so Shot and Cancel together span exactly one control row.
screen photobooth_button(btn_label, btn_action):

    textbutton renpy.translate_string("[btn_label]"):
        xsize PHOTOBOOTH_UI_W // 2
        action btn_action
        text_size PHOTOBOOTH_UI_SIZE
        text_outlines PHOTOBOOTH_UI_OUTLINE
        text_align 0.5
        text_xalign 0.5

# ----------------------------------------------------------------------------------------------------
# ENTRY — `call photobooth_run` from any scene; returns the SAVED SHOT, or None if he walked away
# ----------------------------------------------------------------------------------------------------
# The shot is the whole config the player composed — `id`, `bg`, `fg`, `aspect`, `picks` (the option rows, e.g. `picks["hero_face"]`), `wears`, `day`, `time`, `chars` — so a scene can score what he chose, not only that he chose something. `shot["id"]` is the gallery token every older caller wanted.
label photobooth_run(pose_set="heroandwsis_1"):

    $ photo_cfg = Photo_NewConfig(pose_set)
    call screen photobooth(photo_cfg)

    if _return == "shot":
        play SE1 "PhotoShot1.mp3"
        $ photo_last = Photo_Save(photo_cfg)
        return Photo_Shot(photo_last)

    return None
