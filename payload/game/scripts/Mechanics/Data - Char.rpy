# --------------------------------------------------
# CHARACTER DATABASE
# --------------------------------------------------
# Feeds the database page of the Guide menu (System - Info.rpy). It is CHAR_DATA and not Char_Data because every save up to 0.33.1 still carries the old mutable Char_Data dict and would restore it straight over a define on load — the same trap that made 0.40.2 crash with KeyError: 'facade' (see Data - Map.rpy).

# What each Type promises the player.
define CHAR_TYPE = {
    "Main Character" : "This character is controllable by player.",
    "Dateable" : "This character should be available for H and romantic content [C_Unv](Working in progress)[C_Off].",
    "Tutor"    : "This character can help you and guide your progress.",
    "Sex-Doll" : "This character is available for easy H content.",
    "Friendly" : "This character may be available for non conventional content.",
    }

# Read as (stat, label, standard base gain), so a rate can be shown as a percentage off the standard gain; a character whose own base differs (WSUK) gets an "Own pace" row for the difference. Numbers are colored by sign alone — green above the standard, red below — even for rage, where slower is the good news.
define CHAR_BOOST = [
    ("inti", "Intimacy", 1.0),
    ("love", "Love", 2.5),
    ("lust", "Lust", 5.0),
    ("rage", "Rage", 7.5),
    ]

# HERO counts his training rates instead of affinity, and every one of them falls as the attribute climbs (GameCheck.rpy), so his numbers go red once a stat is well trained.
define CHAR_BOOST_HERO = [
    ("cha", "Charisma", 0.2),
    ("int", "Intelligence", 1.0),
    ("phy", "Physics", 1.0),
    ("cha_soc", "Social", 0.2),
    ("cha_sex", "Sensuality", 0.5),
    ("cha_per", "Performance", 1.0),
    ("int_log", "Logic", 1.0),
    ("int_per", "Perception", 1.0),
    ("int_mem", "Knowledge", 1.0),
    ("phy_str", "Strength", 1.0),
    ("phy_agi", "Agility", 1.0),
    ("phy_res", "Endurance", 1.0),
    ("lust", "Lust", 1.0),
    ]

# Order the Bonus/Onus/Info groups are printed in.
define CHAR_GROUP = ["Chat", "Touch", "Gift", "Sex", "Event"]

# --------------------------------------------------
define CHAR_DATA = { # Bonus = green, Onus = red, Info = neutral. Notes are free lines that no percentage can say for the character.
# --------------------------------------------------

    "hero" : {
        "Type" : "Main Character",
        "Personality" : "Any",
        "Trait" : "Defined by player choices and playability",
        "Notes" : [
            "Training gets harder the further an attribute goes, so a [C_Pos]green[C_Off] rate is one that still climbs fast, and a [C_Neg]red[C_Off] one is already well trained. Bonus points, [C_Dat]hygiene[C_Off] and [C_Dat]energy[C_Off] push every rate up, and repeating the same workout on the same day pushes it down.",
            "Lust is the one you want [C_Pos]slow[C_Off]: a [C_Pos]green[C_Off] rate there means it fills faster and it gets harder to keep your head. [C_Per]Sensuality[C_Off] perks slow it down.",
            ],
        },

    "wsis" : {
        "Type" : "Dateable",
        "Personality" : "Tsundere/Stubborn",
        "Trait" : "Tries to hide her true feeling",
        "Notes" : [
            "Intimacy and lust rates [C_Pos]can grow very fast at high love[C_Off], [C_Neg]but love grows extremely slowly in early game, so intimacy and lust also does[C_Off]. If you are younger than her, she tends to avoid aggressive actions against you, but the rate of love and lust slightly decreases.",
            ],
        "Onus" : {
            "Chat" : [
                "Easily gets tired of chatting, and doesn't bring up topics if love is low",
                "Exceeding the barriers of intimacy can make her angry, and she should avoid talking to you for a while",
                ],
            "Touch" : [
                "You better not get too close if you don't have enough intimacy",
                ],
            },
        "Info" : {
            "Chat" : ["Acceptance regens after 1h"],
            "Touch" : ["Hug acceptance regens after 6h"],
            },
        },

    "wmom" : {
        "Type" : "Dateable",
        "Personality" : "Mothery",
        "Bonus" : {
            "Chat" : [
                "Unlimited",
                ],
            "Touch" : [
                "Never refused",
                "Increased effect",
                ],
            },
        "Onus" : {
            "Touch" : [
                "Costs more time",
                ],
            },
        },

    "wcou" : {
        "Type" : "Tutor",
        "Personality" : "Teasedere",
        "Trait" : "Loves to tease and flirt",
        "Notes" : [
            "[C_Pos]Obey her without contesting her orders to get her affection[C_Off], [C_Neg]else, it may grows very slowly (or even decrease)[C_Off].",
            "[C_Pos]INT and PHY increases affection rate as much as CHA does[C_Off].",
            ],
        "Bonus" : {
            "Chat" : [
                "Get tips and bonus points with other characters by mentioning them in dialogue",
                "Time passes slowly during the conversation",
                ],
            },
        "Onus" : {
            "Chat" : [
                "You do not gain intimacy points for spending time",
                ],
            },
        },

    "wgma" : {
        "Type" : "Sex-Doll",
        "Personality" : "Gaga/Senile",
        "Trait" : "Doesn't even know what she says",
        "Notes" : [
            "[C_Mnd]None[C_Off].",
            ],
        },

    "wnei" : {
        "Type" : "Dateable",
        "Personality" : "Genkikko/Bakadere",
        "Trait" : "Too stupid to be hated",
        "Bonus" : {
            "Chat" : [
                "Easily bring up topics",
                ],
            },
        "Onus" : {
            "Chat" : [
                "Easily gets tired of chatting",
                ],
            },
        "Info" : {
            "Chat" : ["Acceptance regens after 1h"],
            "Touch" : ["Hug acceptance regens after 2h"],
            },
        },

    "wpre" : {
        "Type" : "Dateable",
        "Personality" : "Oujodere",
        "Trait" : "A proper lady",
        "Notes" : [
            "[C_Pos]INT increases affection rate as much as CHA does[C_Off].",
            ],
        "Info" : {
            "Touch" : ["Hug acceptance regens after 3h"],
            },
        },

    "wgal" : {
        "Type" : "Dateable",
        "Personality" : "Kanedere",
        "Trait" : "Only cares about status",
        "Notes" : [
            "[C_Pos]Charm has increased effect[C_Off].",
            ],
        "Bonus" : {
            "Chat" : [
                "Unlimited",
                ],
            "Gift" : [
                "Received gifts have bonus effects",
                ],
            },
        "Onus" : {
            "Touch" : [
                "Decreased effect for physical contact gain",
                ],
            },
        "Info" : {
            "Touch" : ["Hug acceptance regens after 3h"],
            },
        },

    "wric" : {
        "Type" : "Dateable",
        "Personality" : "Himedere",
        "Trait" : "Wants to have constant attention as the princess she is",
        "Bonus" : {
            "Chat" : [
                "Unlimited",
                ],
            "Touch" : [
                "Never refused",
                ],
            },
        },

    "wota" : {
        "Type" : "Dateable",
        "Personality" : "Chūnibyō",
        "Trait" : "Has fantastic delusions of grandeur",
        "Bonus" : {
            "Chat" : [
                "Occasionally increases her own lust by saying random lewd things, or just by thinking too much. The higher the love and intimacy, the higher the chance of her bringging out lewd stuff",
                ],
            },
        "Info" : {
            "Touch" : ["Hug acceptance regens after 3h"],
            },
        },

    "wdis" : {
        "Type" : "Dateable",
        "Personality" : "Dojikko",
        "Trait" : "Disastrous girl. A complete failure",
        "Notes" : [
            "[C_Pos]Intimacy and lust rates grow faster at higher love[C_Off].",
            ],
        "Bonus" : {
            "Chat" : [
                "Unlimited",
                ],
            "Touch" : [
                "Never refused",
                ],
            },
        },

    "wgot" : {
        "Type" : "Dateable",
        "Personality" : "Utsudere",
        "Trait" : "A gloomy depressive girl",
        "Bonus" : {
            "Chat" : [
                "Unlimited",
                ],
            "Touch" : [
                "Never refused",
                ],
            },
        },

    "wdel" : {
        "Type" : "Dateable",
        "Personality" : "Tomboy",
        "Trait" : "Sometimes forget she's a girl",
        "Bonus" : {
            "Chat" : [
                "Unlimited",
                ],
            },
        "Onus" : {
            "Touch" : [
                "Don't accept a second hug",
                ],
            },
        "Info" : {
            "Touch" : ["Hug acceptance regens after a day"],
            },
        },

    "wuza" : {
        "Type" : "Dateable",
        "Personality" : "Uzadere",
        "Trait" : "A very loud girl that doesn't know what's personal space",
        "Notes" : [
            "[C_Unv](Working in progress)[C_Off].",
            ],
        },

    "wlaz" : {
        "Type" : "Dateable",
        "Personality" : "Darudere",
        "Trait" : "Too lazy",
        "Notes" : [
            "[C_Unv](Working in progress)[C_Off].",
            ],
        },

    "wsuk" : {
        "Type" : "Sex-Doll",
        "Personality" : "Sukebe",
        "Trait" : "A nymphomaniac",
        "Bonus" : {
            "Sex" : [
                "Enjoy it best at an average speed",
                ],
            "Event" : [
                "Has [C_Dat][wsuk_chance]% chance[C_Off] of appearing everyday and invite you to have sex. The higher your [C_Dat]Sensualization[C_Off] skill and her love, the greater the chances of her appearing",
                ],
            },
        "Onus" : {
            "Sex" : [
                "Feels little pleasure when feeling pain",
                ],
            "Event" : [
                "Reject may decrease her love",
                ],
            },
        "Info" : {
            "Event" : ["[C_Mnd](PROTOTYPE: for now you can just have sex by calling her on the map)[C_Off]"],
            },
        },

    "hprv" : {
        "Type" : "Friendly",
        "Personality" : "Erodere",
        "Trait" : "Pervert dude",
        "Bonus" : {
            "Chat" : [
                "Unlimited",
                ],
            },
        "Onus" : {
            "Touch" : [
                "Don't accept a second hug",
                ],
            },
        "Info" : {
            "Touch" : ["Hug acceptance regens after a day"],
            },
        },

    "hine" : {
        "Type" : "Friendly",
        "Personality" : "Hinedere",
        "Notes" : [
            "Inverse affection rate [C_Mnd](the lower is your CHA, the higher is the affection gain)[C_Off].",
            "Hard to start, easy to maintain [C_Mnd](the higher is the love, the higher is the affection gain)[C_Off].",
            ],
        },

    "hriv" : {
        "Type" : "Friendly",
        "Personality" : "Chad",
        "Notes" : [
            "CHA is much more important than usual.",
            "Hard to start, easy to maintain [C_Mnd](the higher is the love, the higher is the affection gain)[C_Off].",
            "[C_Neg]High Ego. The more you defeat him in games or the more girls are in love with you, the more he may envy you.[C_Off] [C_Mnd](Take girls' virginity before he does and let him know to get increased envy effect, when available)[C_Off].",
            ],
        },
    }

init python:

    # The boost: hyperlink protocol behind the 🔹 of each Boost row (blue marks the clickable ones, orange the plain lines): click unfolds that stat's factors, click again folds them, another 🔸 swaps to that stat.
    def Boost_Toggle(stat_id):
        store.a_menu_11 = 0 if store.a_menu_11 == stat_id else stat_id
        renpy.restart_interaction()

    config.hyperlink_handlers["boost"] = Boost_Toggle

    def Char_InfoText(char_id):
        """Builds the whole database page for char_id out of CHAR_DATA, so the text is written once here instead of once per character on the screen."""

        data = CHAR_DATA.get(char_id, None)
        if data is None:
            return "{size=40}{p}{b}" + __("No Data") + "{/b}{/size}"

        size = getattr(store, char_id + "_size", 0)
        fat = getattr(store, char_id + "_fat", 0)

        # Every header line is optional, so HERO can skip straight to his counters without a Type or a Personality.
        head = []
        if data.get("Type", None):
            head.append("{b}" + __("Type") + ":{/b} [C_Per]" + __(data["Type"]) + "[C_Off]. " + __(CHAR_TYPE.get(data["Type"], "")))
        if data.get("Personality", None):
            head.append("{b}" + __("Personality") + ":{/b} [C_Per]" + __(data["Personality"]) + "[C_Off]" + (". " + __(data["Trait"]) if data.get("Trait", None) else ""))
        if size:
            head.append("{b}" + __("Height") + ":{/b} " + str(size) + "m")
        if size and fat:
            head.append("{b}" + __("Weight") + ":{/b} " + str(round(fat * size * size, 2)) + "kg")
        head.append("{b}" + __("[C_Pos]Bonus[C_Off] & [C_Neg]Onus[C_Off]") + ":{/b}")
        txt = "{size=40}" + "{p}{p}".join(head)

        for note in data.get("Notes", []):
            txt += "{p}🔶 " + __(note)

        # A multiplier as a signed percentage off 1.0: green above, red below, grey when it does nothing yet.
        def percent(factor):
            value = (factor - 1) * 100
            color = "[C_Mnd]" if abs(value) < 0.005 else ("[C_Pos]" if value > 0 else "[C_Neg]")
            return color + ("+" if value >= 0.005 else "") + ("%.2f" % value) + "%[C_Off]"

        # Boost reads the live rates back off the standard gain (affinity for the girls, training speed for HERO). The 🔹 of each row is a boost: hyperlink that unfolds the factors behind it exactly as check_stat() multiplies them (a_menu_11 holds the open one), so the player can see which lever moves the number.
        boost = Stat_Modifiers.get(char_id, {}).get("add", {})
        fades = Stat_Fades.get(char_id, {})
        parts = Stat_Factors.get(char_id, {})
        rows = []
        for stat_id, stat_name, base in (CHAR_BOOST_HERO if char_id == "hero" else CHAR_BOOST):
            if stat_id not in boost:
                continue
            own_base, factors = parts.get(stat_id, (base, []))
            rows.append("{p}{space=60}{a=boost:" + stat_id + "}🔹{/a} [C_Dat]" + __(stat_name) + "[C_Off] (" + percent(boost[stat_id] * fades.get(stat_id, 1.0) / base) + ")")
            if a_menu_11 != stat_id:
                continue
            lines = ([("Own pace", own_base / base)] if own_base != base else []) + list(factors) + ([("Growth slowdown", fades[stat_id])] if stat_id in fades else [])
            for label, factor in lines:
                rows.append("{p}{space=120}{size=32}• " + __(label) + " " + percent(factor) + "{/size}")
        if rows:
            txt += "{p}{p}🔶 " + __("Boost") + ":" + "".join(rows)

        for group in CHAR_GROUP:
            rows = []
            for entry in data.get("Bonus", {}).get(group, []):
                rows.append("{p}{space=60}🔸 [C_Pos]" + __(entry) + "[C_Off]")
            for entry in data.get("Onus", {}).get(group, []):
                rows.append("{p}{space=60}🔸 [C_Neg]" + __(entry) + "[C_Off]")
            for entry in data.get("Info", {}).get(group, []):
                rows.append("{p}{space=60}🔸 " + __(entry))
            if rows:
                txt += "{p}{p}🔶 " + __(group) + ":" + "".join(rows)

        # WSUK's appearance chance rides on her love and HERO's Sensualization, so it is the one number filled in as the page is built.
        return txt.replace("[wsuk_chance]", str(max(0, round((2 + (perk_cha_sex * perk_cha_sex * 2)) + (wsuk_love * wsuk_love / 125))))) + "{/size}"

# --------------------------------------------------
define Char_Schedule = { # CHARACTER SCHEDULE
# --------------------------------------------------
    # Char ID
        # Schedule with routines in weeks
        # Routine, with: (start, duration, action)
        # Action, with: (affinity, duration, action, condition)

    # --------------------------------------------------
    "wmom": {
    # --------------------------------------------------
        "schedule" : { # weeks
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "routine_2" : ["Sunday"],
        },
        "routine_1": [
            ("05:00", "00:10", "bathing"),
            ("05:20", "00:40", "cooking"),
            ("06:30", "00:10", ("changing", "casual")),
            ("06:30", "00:15", "eating"),
            ("07:00", "00:40", ("moving", "work")),
            ("08:00", "00:00", "working"),
            ("17:00", "00:30", ("moving", "home")),
            ("17:00", "01:00", "cooking"),
            ("17:00", "00:15", "eating"),
            ("17:00", "00:30", "cleaning"),
            ("17:00", "00:10", "bathing"),
            ("21:00", "00:10", ("changing", "sleep")),
            ("21:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("06:00", "00:10", ("changing", "home")),
            ("06:00", "00:10", "bathing"),
            ("06:00", "01:00", "cleaning"),
            ("06:00", "00:20", "laundring"),
            ("10:00", "00:40", "cooking"),
            ("10:00", "00:15", "eating"),
            ("15:50", "00:10", ("changing", "sport")),
            ("15:50", "01:00", ("exercising")),
            ("15:50", "00:10", "bathing"),
            ("15:50", "00:10", ("changing", "home")),
            ("17:30", "01:00", "cooking"),
            ("18:30", "00:15", "eating"),
            ("19:00", "00:30", "cleaning"),
            ("21:00", "00:10", "bathing"),
            ("21:00", "00:10", ("changing", "sleep")),
            ("21:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.30, "00:30", "cleaning", None),
            (0.20, "00:30", "watching tv", None),
            (0.15, "00:30", "reading", None),
        ],
    },

    # --------------------------------------------------
    "wsis": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday"],
            "routine_2" : ["Friday"],
            "routine_3" : ["Saturday"],
            "routine_4" : ["Sunday"],
        },
        "routine_1": [
            ("05:00", "00:10", "bathing"),
            ("05:00", "00:10", ("changing", "school")),
            ("05:00", "00:15", "eating"),
            ("07:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            ("12:00", "00:15", "eating"),
            ("12:15", "00:45", ("staying", "frontyard")), # Waits for HERO at the frontyard until 12:59
            ("13:00", "00:20", ("moving", "home")),
            ("13:00", "00:10", "bathing"),
            ("13:00", "00:10", ("changing", "home")),
            ("17:30", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "00:10", ("changing", "sleep")),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("05:00", "00:10", "bathing"),
            ("05:00", "00:10", ("changing", "school")),
            ("05:00", "00:15", "eating"),
            ("07:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            ("12:00", "00:15", "eating"),
            ("12:15", "00:45", ("staying", "frontyard")), # Waits for HERO at the frontyard until 12:59
            ("13:00", "00:20", ("moving", "home")),
            ("13:00", "00:10", "bathing"),
            ("13:00", "00:10", ("changing", "home")),
            ("17:30", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("23:00", "00:10", ("changing", "sleep")),
            ("23:00", "08:00", "sleeping"),
        ],
        "routine_3": [
            ("07:00", "00:10", ("changing", "home")),
            ("07:00", "00:15", "eating"),
            ("17:30", "00:10", "bathing"),
            ("20:00", "03:00", "at sleepover"),
            ("23:00", "00:10", ("changing", "sleep")),
            ("23:00", "08:00", "sleeping"),
        ],
        "routine_4": [
            ("07:00", "00:10", ("changing", "home")),
            ("07:00", "00:15", "eating"),
            ("07:00", "00:20", "laundring"),
            ("17:30", "00:10", "bathing"),
            ("22:00", "00:10", ("changing", "sleep")),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.35, "00:40", "gaming", None),
            (0.20, "00:20", "drawing", None),
            (0.20, "00:20", "watching tv", None),
            (0.15, "00:20", "eating", None),
            (0.15, "00:20", "cleaning", None),
            (0.10, "00:20", "studying", None),
        ],
    },

    # --------------------------------------------------
    "wnei": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday"],
            "routine_3" : ["Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("07:00", "00:10", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:20", ("moving", "neighbor")),
            ("17:00", "00:10", "bathing"),
            ("22:00", "00:10", ("changing", "under")),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("07:00", "00:10", ("changing", "home")),
            ("07:00", "00:15", "eating"),
            ("07:00", "00:05", ("moving", "home")),
            ("17:30", "00:10", "bathing"),
            ("20:00", "03:00", "at sleepover"),
            ("23:00", "00:10", ("changing", "sleep")),
            ("23:00", "08:00", "sleeping"),
        ],
        "routine_3": [
            ("07:00", "00:10", ("changing", "home")),
            ("07:00", "00:15", "eating"),
            ("07:00", "00:05", ("moving", "home")),
            ("17:00", "00:10", "bathing"),
            ("17:00", "00:05", ("moving", "neighbor")),
            ("22:00", "00:10", ("changing", "under")),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:20", "drawing", None),
            (0.30, "00:40", "playing", None),
            (0.30, "00:40", "gaming", None),
            (0.25, "00:20", "watching tv", None),
        ],
    },

    # --------------------------------------------------
    "wmam": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        },
        "routine_1": [
            ("07:00", "00:10", "bathing"),
            ("07:30", "00:10", ("changing", "home")),
            ("08:00", "00:15", "eating"),
            ("18:00", "00:15", "eating"),
            ("21:00", "00:10", "bathing"),
            ("22:00", "09:00", "sleeping"),
        ],
        "pastime": [
            (0.35, "00:40", "reading", None),
            (0.25, "00:30", "watching tv", None),
            (0.20, "00:30", "cooking", None),
            (0.20, "00:30", "gardening", None),
        ],
    },

    # --------------------------------------------------
    "hpap": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        },
        "routine_1": [
            ("07:00", "00:10", "bathing"),
            ("07:30", "00:10", ("changing", "home")),
            ("08:00", "00:15", "eating"),
            ("18:00", "00:15", "eating"),
            ("21:00", "00:10", "bathing"),
            ("22:00", "09:00", "sleeping"),
        ],
        "pastime": [
            (0.35, "00:40", "reading", None),
            (0.25, "00:30", "watching tv", None),
            (0.20, "00:30", "cooking", None),
            (0.20, "00:30", "gardening", None),
        ],
    },

    # --------------------------------------------------
    "wgma": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        },
        "routine_1": [
            ("07:00", "00:10", "bathing"),
            ("07:30", "00:10", ("changing", "home")),
            ("08:00", "00:15", "eating"),
            ("18:00", "00:15", "eating"),
            ("21:00", "00:10", "bathing"),
            ("22:00", "09:00", "sleeping"),
        ],
        "pastime": [
            (0.35, "00:40", "reading", None),
            (0.25, "00:30", "watching tv", None),
            (0.20, "00:30", "cooking", None),
            (0.20, "00:30", "gardening", None),
        ],
    },

    # --------------------------------------------------
    "wcou": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "work")),
            ("06:00", "00:15", "eating"),
            ("07:00", "00:20", ("moving", "office")), # Going to work
            ("08:00", "10:00", "working"),
            ("18:00", "00:15", "eating"),
            #("20:00", "00:20", ("moving", "care_center")), # Taking WGMA
            ("20:00", "00:20", ("moving", "grandma")), # Going home
            ("21:00", "00:10", "bathing"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [ # At home (Grandma's)
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "work")),
            ("06:00", "00:15", "eating"),
            ("18:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.50, "00:30", "reading", None),
            (0.50, "00:30", "exercising", None),
        ],
    },

    # --------------------------------------------------
    "wpre": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Wednesday", "Friday"],
            "routine_2" : ["Tuesday", "Thursday"],
            "routine_3" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            ("12:00", "00:30", "at club"),
            ("12:30", "00:30", ("moving", "work")),
            ("12:30", "00:10", ("changing", "casual")),
            ("14:00", "06:00", "working"),
            ("20:00", "00:40", ("moving", "unknown")),
            ("20:00", "00:10", "bathing"),
            ("20:00", "00:10", ("changing", "school")),
            ("20:00", "07:30", "sleeping"),
        ],
        "routine_2": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:50", ("moving", "unknown")),
            ("20:00", "00:10", "bathing"),
            ("20:00", "00:10", ("changing", "school")),
            ("20:00", "07:30", "sleeping"),
        ],
        "routine_3": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("07:00", "00:30", ("moving", "work")),
            ("07:00", "00:10", ("changing", "casual")),
            ("08:00", "10:00", "working"),
            ("18:00", "00:40", ("moving", "unknown")),
            ("20:00", "00:10", "bathing"),
            ("20:00", "00:10", ("changing", "school")),
            ("20:00", "07:30", "sleeping"),
        ],
        "pastime": [
            (0.30, "01:00", "studying", None),
            (0.30, "00:40", "cleaning", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "hine": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            ("12:00", "00:30", ("moving", "unknown")),
            ("18:00", "00:10", "bathing"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:10", "bathing"),
            ("09:00", "00:15", "eating"),
            ("18:00", "00:10", "bathing"),
            ("23:00", "09:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "hprv": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },
    
    # --------------------------------------------------
    "wric": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wgal": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wdis": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wota": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wdel": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wuza": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wgot": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wlaz": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "hriv": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "hbul": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "hfem": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wdan": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wkuu": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wemo": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wnem": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wahu": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wtec": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wido": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wrin": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wsuk": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "at class"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "at class"),
            #("12:00", "05:00", "at club"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:15", "eating"),
            ("12:00", "00:15", "eating"),
            ("17:00", "00:10", "bathing"),
            ("18:00", "00:15", "eating"),
            ("22:00", "08:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },

    # --------------------------------------------------
    "wtpe": {
    # --------------------------------------------------
        "schedule" : {
            "routine_1" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "routine_2" : ["Saturday", "Sunday"],
        },
        "routine_1": [
            ("06:00", "00:10", "bathing"),
            ("06:00", "00:10", ("changing", "school")),
            ("06:00", "00:15", "eating"),
            ("06:00", "00:20", ("moving", "school")),
            ("07:30", "02:00", "teaching"),
            #("09:30", "00:30", "at break"),
            ("10:00", "02:00", "teaching"),
            ("12:00", "05:00", "working"),
            ("17:00", "00:30", ("moving", "unknown")),
            ("18:00", "00:10", "bathing"),
            ("22:00", "08:00", "sleeping"),
        ],
        "routine_2": [
            ("08:00", "00:10", "bathing"),
            ("08:30", "00:10", ("changing", "school")),
            ("09:00", "00:15", "eating"),
            ("18:00", "00:10", "bathing"),
            ("23:00", "09:00", "sleeping"),
        ],
        "pastime": [
            (0.20, "00:30", "playing", None),
            (0.20, "00:30", "eating", None),
            (0.20, "00:30", "reading", None),
            (0.20, "00:30", "studying", None),
            (0.20, "00:30", "writing", None),
        ],
    },
}