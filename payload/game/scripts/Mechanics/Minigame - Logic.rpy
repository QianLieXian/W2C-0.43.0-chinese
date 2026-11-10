# ----------------------------------------------------------------------------------------------------
init python:
# ----------------------------------------------------------------------------------------------------
    _LOGIC_COLOR_PALETTE = [
        ("Red",     "#FF0000"),
        ("Yellow",  "#FFFF00"),
        ("Green",   "#00FF00"),
        ("Cyan",    "#00FFFF"),
        ("Blue",    "#0000FF"),
        ("Magenta", "#FF00FF"),
        ("Orange",  "#FFA500"),
    ]

    _LOGIC_SPELL_WORDS = [
        "cat", "dog", "bird", "fish", "tree", "book", "moon", "star",
        "fire", "rain", "lake", "bread", "cloud", "river", "stone",
    ]

    _LOGIC_SHAPES = [
        ("●", "Circle"),
        ("■", "Square"),
        ("▲", "Triangle"),
        ("◆", "Diamond"),
        ("★", "Star"),
        ("♥", "Heart"),
        ("✚", "Cross"),
    ]

    _LOGIC_EMOJIS = [
        ("\U0001F431", "Cat"),
        ("\U0001F436", "Dog"),
        ("\U0001F98A", "Fox"),
        ("\U0001F43B", "Bear"),
        ("\U0001F43C", "Panda"),
        ("\U0001F438", "Frog"),
        ("\U0001F435", "Monkey"),
        ("\U0001F430", "Rabbit"),
    ]

    _LOGIC_OPPOSITES = [
        ("hot",   "cold"),
        ("big",   "small"),
        ("fast",  "slow"),
        ("happy", "sad"),
        ("day",   "night"),
        ("up",    "down"),
        ("light", "dark"),
        ("hard",  "soft"),
        ("empty", "full"),
    ]

    _LOGIC_BADGES = "①②③④⑤⑥⑦⑧⑨⑩"  # ①..⑩

    def _logic_badge(idx):
        if idx is None:
            return ""
        if 0 <= idx < len(_LOGIC_BADGES):
            return _LOGIC_BADGES[idx]
        return str(idx + 1)

    def _logic_random_hex():
        return renpy.random.choice(_LOGIC_COLOR_PALETTE)[1]

    def _logic_random_hex_excluding(exclude_hex):
        candidates = [h for _, h in _LOGIC_COLOR_PALETTE if h != exclude_hex]
        if not candidates:
            return exclude_hex
        return renpy.random.choice(candidates)

    def _logic_make_pair_math():
        a = renpy.random.randint(0, 10)
        b = renpy.random.randint(0, 10)
        op = renpy.random.choice(["+", "-"])
        if op == "-" and a < b:
            a, b = b, a
        result = (a + b) if op == "+" else (a - b)
        return {
            "question": "{} {} {}".format(a, op, b),
            "answer":   str(result),
            "display":  str(result),
        }

    def _logic_make_pair_color():
        name, hexv = renpy.random.choice(_LOGIC_COLOR_PALETTE)
        trick_hex = _logic_random_hex_excluding(hexv)
        return {
            "question": hexv,
            "answer":   name,
            "display":  "{{color={}}}{}{{/color}}".format(trick_hex, renpy.translate_string(name)),
        }

    def _logic_make_pair_spell():
        word = renpy.translate_string(renpy.random.choice(_LOGIC_SPELL_WORDS))
        letters = list(word)
        for _ in range(20):
            renpy.random.shuffle(letters)
            if "".join(letters) != word:
                break
        scrambled_parts = []
        for ch in letters:
            scrambled_parts.append("{{color={}}}{}{{/color}}".format(_logic_random_hex(), ch))
        return {
            "question": "".join(scrambled_parts),
            "answer":   word,
            "display":  word,
        }

    def _logic_make_pair_shape():
        glyph, name = renpy.random.choice(_LOGIC_SHAPES)
        glyph_hex = _logic_random_hex()
        display_hex = _logic_random_hex_excluding(glyph_hex)
        return {
            "question": "{{color={}}}{}{{/color}}".format(glyph_hex, glyph),
            "answer":   name,
            "display":  "{{color={}}}{}{{/color}}".format(display_hex, renpy.translate_string(name)),
        }

    def _logic_make_pair_emoji():
        emoji, name = renpy.random.choice(_LOGIC_EMOJIS)
        display_hex = _logic_random_hex()
        return {
            "question": emoji,
            "answer":   name,
            "display":  "{{color={}}}{}{{/color}}".format(display_hex, renpy.translate_string(name)),
        }

    def _logic_make_pair_opposite():
        a, b = renpy.random.choice(_LOGIC_OPPOSITES)
        if renpy.random.random() < 0.5:
            q_word, a_word = a, b
        else:
            q_word, a_word = b, a
        display_hex = _logic_random_hex()
        return {
            "question": renpy.translate_string(q_word),
            "answer":   a_word,
            "display":  "{{color={}}}{}{{/color}}".format(display_hex, renpy.translate_string(a_word)),
        }

    _LOGIC_GENERATORS = {
        "math":     _logic_make_pair_math,
        "color":    _logic_make_pair_color,
        "spell":    _logic_make_pair_spell,
        "shape":    _logic_make_pair_shape,
        "emoji":    _logic_make_pair_emoji,
        "opposite": _logic_make_pair_opposite,
    }

    def _logic_new_round(theme, var_num):
        gen = _LOGIC_GENERATORS.get(theme, _logic_make_pair_math)
        pairs = []
        seen_answers = set()
        attempts = 0
        max_attempts = max(50, var_num * 50)
        while len(pairs) < var_num and attempts < max_attempts:
            pair = gen()
            if pair["answer"] not in seen_answers:
                seen_answers.add(pair["answer"])
                pairs.append(pair)
            attempts += 1
        # Pool exhausted (shouldn't happen with curated pools sized > var_num,
        # but guarantee var_num pairs even if duplicates slip through).
        while len(pairs) < var_num:
            pairs.append(gen())
        return pairs

    def _logic_make_answer_order(var_num):
        order = list(range(var_num))
        renpy.random.shuffle(order)
        return order

    def _logic_score(connections, round_data, answer_order):
        s = 0
        for q_i, slot_i in connections.items():
            if round_data[q_i]["answer"] == round_data[answer_order[slot_i]]["answer"]:
                s += 1
        return s

    def _logic_score_delta(connections, round_data, answer_order, total):
        # Round payout: +0.25 per correct, -1 per wrong.
        correct = _logic_score(connections, round_data, answer_order)
        wrong = total - correct
        return 0.25 * correct - wrong

    def _logic_break_q(connections, q_i):
        if q_i in connections:
            del connections[q_i]

    def _logic_break_slot(connections, slot_i):
        for k in list(connections.keys()):
            if connections[k] == slot_i:
                del connections[k]

    def _logic_connect(connections, q_i, slot_i):
        if q_i in connections:
            del connections[q_i]
        for k in list(connections.keys()):
            if connections[k] == slot_i:
                del connections[k]
        connections[q_i] = slot_i

    def _logic_slot_owner(connections, slot_i):
        for k, v in connections.items():
            if v == slot_i:
                return k
        return None

    def _logic_reset_dict(d):
        d.clear()

    def _logic_resolve_theme(var_the):
        # Lists pick uniformly per call; "any" expands to every supported theme.
        # Recurse so a list containing "any" (or nested lists) still resolves.
        if isinstance(var_the, list):
            if not var_the:
                return "math"
            return _logic_resolve_theme(renpy.random.choice(var_the))
        if var_the == "any":
            return renpy.random.choice(list(_LOGIC_GENERATORS.keys()))
        return var_the

# ----------------------------------------------------------------------------------------------------
style logic_frame:
# ----------------------------------------------------------------------------------------------------
    background "#3232327D"
    hover_background "#00000064"
    xsize 400
    ysize 150
    xalign 0.5
    yalign 0.5

# ----------------------------------------------------------------------------------------------------
style logic_frame_selected:
# ----------------------------------------------------------------------------------------------------
    background "#FFCB64C8"
    hover_background "#FFCB64C8"
    xsize 400
    ysize 150
    xalign 0.5
    yalign 0.5

# ----------------------------------------------------------------------------------------------------
screen minigame_logic(var_the="math", var_num=4, var_tio=0, var_tim=None, var_txt=None, var_mod="classic", var_sco=0, var_sca=0.5):
# ----------------------------------------------------------------------------------------------------
    default game_started = False
    default selected_q = None
    default connections = dict()
    default score = var_sco * 1
    default timer_current = var_tio
    default scale_acc = 0.0
    default effective_num = var_num
    default current_theme = _logic_resolve_theme(var_the)
    default round_data = _logic_new_round(current_theme, var_num)
    default answer_order = _logic_make_answer_order(var_num)
    default effective_tim = (15 if (var_mod == "continuous" and var_tim is None) else var_tim)

    $ frame_h = min(150, max(60, int(600 / max(1, effective_num))))
    $ frame_w = 400

    # --------------------------------------------------
    # Preparation Screen
    # --------------------------------------------------
    if not game_started:
        frame:
            background "#000000C8"
            xysize (1920, 1080)
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                label renpy.translate_string("{size=+80}{b}Logic{/b}{/size}") xalign 0.5
                vbox:
                    xalign 0.5
                    xysize (960, 400)
                    if var_txt == None:
                        if isinstance(var_the, list) or var_the == "any":
                            text renpy.translate_string("{size=+10}Connect each question to its match — the puzzle type changes every round!{/size}") xalign 0.5
                        elif var_the == "math":
                            text renpy.translate_string("{size=+10}Connect each sum to its result.{/size}") xalign 0.5
                        elif var_the == "color":
                            text renpy.translate_string("{size=+10}Connect each colour to its name — don't let the text colour fool you!{/size}") xalign 0.5
                        elif var_the == "spell":
                            text renpy.translate_string("{size=+10}Unscramble each word and connect it to its match.{/size}") xalign 0.5
                        elif var_the == "shape":
                            text renpy.translate_string("{size=+10}Connect each shape to its name.{/size}") xalign 0.5
                        elif var_the == "emoji":
                            text renpy.translate_string("{size=+10}Connect each emoji to its name.{/size}") xalign 0.5
                        elif var_the == "opposite":
                            text renpy.translate_string("{size=+10}Connect each word to its opposite.{/size}") xalign 0.5
                        else:
                            text renpy.translate_string("{size=+10}Connect each question to its matching answer.{/size}") xalign 0.5
                        if var_mod == "continuous":
                            text renpy.translate_string("{size=+5}Solve as many rounds as you can before time runs out — each round adds more pairs.{/size}") xalign 0.5
                    else:
                        text renpy.translate_string("{size=+10}[var_txt]{/size}") xalign 0.5
                text renpy.translate_string("[C_Dat]{size=+40}{b}Click to start!{/b}[C_Off]") xalign 0.5

        key "mousedown_1" action SetScreenVariable("game_started", True)

    # --------------------------------------------------
    # Game Started
    # --------------------------------------------------
    else:
        # Timer — auto-set to 15s in continuous mode if caller didn't pass one.
        if effective_tim != None:
            timer 1 repeat True action [
                If(timer_current < effective_tim,
                    true=(SetScreenVariable("timer_current", timer_current + 1)),
                    false=(Return(score)),
                )
            ]

        # Top header: title, timer bar, connection counter, live score (continuous)
        $ connection_count = len(connections)
        vbox:
            xalign 0.5
            yalign 0.0
            yoffset 20
            spacing 10
            text renpy.translate_string("{size=+30}{b}Logic{/b}{/size}") xalign 0.5
            if effective_tim != None:
                bar value timer_current range effective_tim xmaximum 800 xalign 0.5
            text renpy.translate_string("{size=+5}Connected: [connection_count] / [effective_num]{/size}") xalign 0.5
            if var_mod == "continuous":
                text renpy.translate_string("{size=+15}{b}Score: [score]{/b}{/size}") xalign 0.5

        # Centre: question + answer columns
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 200

            # Question column
            vbox:
                spacing 20
                for q_i in range(effective_num):
                    $ q_data = round_data[q_i]
                    $ is_selected_q = (selected_q == q_i)
                    $ is_connected_q = (q_i in connections)
                    # 2-px coloured border via a wrapping frame whose
                    # background IS the border colour; the inner button sits
                    # inside the 2px padding. Keeps the indicator visible
                    # even when the inner background is a vivid colour.
                    $ q_outline_color = "#FFFF00" if is_selected_q else ("#FFF" if is_connected_q else "#000")
                    frame:
                        xysize (frame_w, frame_h)
                        background q_outline_color
                        padding (2, 2)
                        button:
                            xysize (frame_w - 4, frame_h - 4)
                            if current_theme == "color":
                                background q_data["question"]
                                hover_background q_data["question"]
                            else:
                                background "#3232327D"
                                hover_background "#00000064"
                            action If(is_selected_q,
                                true=SetScreenVariable("selected_q", None),
                                false=[
                                    Function(_logic_break_q, connections, q_i),
                                    SetScreenVariable("selected_q", q_i),
                                ]
                            )
                            if current_theme == "math" or current_theme == "spell" or current_theme == "opposite":
                                text q_data["question"] size 50 xalign 0.5 yalign 0.5
                            elif current_theme == "shape" or current_theme == "emoji":
                                text q_data["question"] size 100 xalign 0.5 yalign 0.5
                            # "color": frame background carries the question; no text needed.
                            if is_connected_q:
                                $ q_badge = _logic_badge(connections[q_i])
                                text renpy.translate_string("[q_badge]") size 40 xalign 0.95 yalign 0.05 color "#FFFF64" outlines [(2, "#000", 0, 0)]

            # Answer column (shuffled order)
            vbox:
                spacing 20
                for slot_i in range(effective_num):
                    $ pair_idx = answer_order[slot_i]
                    $ a_data = round_data[pair_idx]
                    $ slot_owner = _logic_slot_owner(connections, slot_i)
                    $ is_connected_slot = (slot_owner is not None)
                    $ a_outline_color = "#FFF" if is_connected_slot else "#000"
                    frame:
                        xysize (frame_w, frame_h)
                        background a_outline_color
                        padding (2, 2)
                        button:
                            xysize (frame_w - 4, frame_h - 4)
                            background "#3232327D"
                            hover_background "#00000064"
                            action If(selected_q != None,
                                true=[
                                    Function(_logic_connect, connections, selected_q, slot_i),
                                    SetScreenVariable("selected_q", None),
                                ],
                                false=Function(_logic_break_slot, connections, slot_i),
                            )
                            text a_data["display"] size 50 xalign 0.5 yalign 0.5
                            if is_connected_slot:
                                $ a_badge = _logic_badge(slot_owner)
                                text renpy.translate_string("[a_badge]") size 40 xalign 0.05 yalign 0.05 color "#FFFF64" outlines [(2, "#000", 0, 0)]

        # Pre-compute the next round's scale/frame count and theme for continuous mode.
        $ next_scale_acc = scale_acc + var_sca
        $ next_effective_num = var_num + int(next_scale_acc)
        $ next_theme = _logic_resolve_theme(var_the)

        # Bottom: Check button (enabled only when every question has a connection)
        if var_mod == "continuous":
            textbutton renpy.translate_string("{size=+10}{b}Check{/b}{/size}"):
                xalign 0.5
                yalign 1.0
                yoffset -30
                xsize 300
                ysize 80
                background "#3232327D"
                hover_background "#00000064"
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
                sensitive (len(connections) == effective_num)
                action [
                    Play("SE2", "JingleRight.ogg"),
                    # +0.25 per correct answer, -1 per wrong. Difficulty
                    # (effective_num) still scales via var_sca.
                    SetScreenVariable("score", score + _logic_score_delta(connections, round_data, answer_order, effective_num)),
                    SetScreenVariable("scale_acc", next_scale_acc),
                    SetScreenVariable("effective_num", next_effective_num),
                    SetScreenVariable("current_theme", next_theme),
                    SetScreenVariable("round_data", _logic_new_round(next_theme, next_effective_num)),
                    SetScreenVariable("answer_order", _logic_make_answer_order(next_effective_num)),
                    Function(_logic_reset_dict, connections),
                    SetScreenVariable("selected_q", None),
                ]
        else:
            textbutton renpy.translate_string("{size=+10}{b}Check{/b}{/size}"):
                xalign 0.5
                yalign 1.0
                yoffset -30
                xsize 300
                ysize 80
                background "#3232327D"
                hover_background "#00000064"
                text_color "#FFFFFF"
                text_xalign 0.5
                text_yalign 0.5
                sensitive (len(connections) == effective_num)
                action Return(_logic_score_delta(connections, round_data, answer_order, effective_num))

    modal True
