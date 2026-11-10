init python:

    # --------------------------------------------------
    def Sit_Wear(base, char_id, sep="_", fallback="home"): # Sitting-pose outfit layer, falling back to art that exists
    # --------------------------------------------------
        # The sitting set only has a few outfits drawn per pose, so a character wearing something with no sitting layer yet (dressy, on a date) borrows the fallback one instead of vanishing. Drop `<base><sep><wear>.webp` in and it is picked up with no code change. `sep` exists because the older single-pose art names its outfits `1home` while the newer layered poses use `1_home`; `fallback` exists because a set's "default" outfit is not always home (the walk draws WSIS in `casual`).
        wear = getattr(store, char_id + "_wear", None) or fallback
        for w in (wear, fallback):
            if renpy.has_image(base + sep + w, exact=True):
                return base + sep + w
        return base + sep + fallback

    # --------------------------------------------------
    def Movie_Beat(love=0, lust=0, rom=0, fun=0, spi=0): # What one moment of the movie is worth
    # --------------------------------------------------
        # Affinity is earned WHEREVER they are watching — the sofa at home or a seat at the cinema. The axes only mean anything on a date, so they are paid only when one is running and no branch here has to know which venue it is in.
        if love:
            add_stat("wsis", "love", love)
        if lust:
            add_stat("wsis", "lust", lust)
        if date_active:
            for axis, points in (("date_rom", rom), ("date_fun", fun), ("date_spi", spi)):
                if points:
                    add_stat("wsis", axis, points)
        return

    # --------------------------------------------------
    def Sit_Layer(base, char_id, sep="_"): # An OPTIONAL outfit layer: the exact one, or nothing at all
    # --------------------------------------------------
        # Unlike Sit_Wear this never falls back to `home`. Some layers exist for one outfit only — the popcorn arm has a sleeve drawn for `dressy` and for nothing else — so the honest answer for the others is "there is no such layer", and the caller simply does not show one.
        wear = getattr(store, char_id + "_wear", None)
        name = base + sep + str(wear)
        return name if wear and renpy.has_image(name, exact=True) else None

    # --------------------------------------------------
    def Sit_Room(room): # Sitting background, falling back to the living room until the art exists
    # --------------------------------------------------
        name = "sitting_bg " + room
        return name if renpy.has_image(name, exact=True) else "sitting_bg home_livingroom"

# ---------------------------------------------------------------------------
label sit_popcorn_arm(n=1): # WSIS's popcorn arm, with the sleeve her outfit wears over it
# ---------------------------------------------------------------------------
# The arm is drawn bare and the sleeve is a separate layer that only some outfits have (`dressy` today), so switching arm poses or outfits goes through here rather than through two show statements that can drift.
# The sleeve sits on its own high zorder, above the foreground, so it covers the whole arm whatever else is on screen; only `fx_light` is raised above it, so the shot stays lit. When the outfit has no sleeve the layer is cleared instead of left behind.
# ---------------------------------------------------------------------------

    show expression "sitting_popcorn_1_wsis_arm " + str(n) as wsis_sit_arm

    $ _sleeve = Sit_Layer("sitting_popcorn_1_wsis_arm_wear " + str(n), "wsis")

    if _sleeve:
        show expression _sleeve as wsis_sit_armwear zorder 20
    else:
        hide wsis_sit_armwear

    return

# ---------------------------------------------------------------------------
label wsis_movie_sprites(room="home_livingroom", popcorn=None): # organize sprites
# ---------------------------------------------------------------------------
# `room` lets another scene borrow this exact composition with a different backdrop — the cinema date
# passes "shopping_cinema", which falls back to the living room until that background is drawn.
# `popcorn` overrides the snack check for callers with their own popcorn (the cinema buys it at the counter
# rather than carrying it from the home table); None keeps the original inventory lookup.
# ---------------------------------------------------------------------------

    scene expression Sit_Room(room)

    if popcorn if popcorn is not None else CountItem_Inventory(item_id="Eat_Snack_Popcorn", inventory_id=inventory_home_table):
        show sitting_popcorn_1_hero_body 1
        show expression Sit_Wear("sitting_popcorn_1_hero_wear 1", "hero") as hero_sit_wear
        show sitting_hero_face 1a0
        show sitting_popcorn_1_wsis_body 1
        show expression Sit_Wear("sitting_popcorn_1_wsis_wear 1", "wsis") as wsis_sit_wear
        call sit_popcorn_arm(1) from _call_sit_popcorn_arm
        show sitting_popcorn_1_wsis_face 1o0
        show sitting_popcorn_1_wsis_fg

    elif wsis_love >= 50:
        show sitting_embrace_2_hero_bg_body 1
        show expression Sit_Wear("sitting_embrace_2_hero_bg_wear 1", "hero") as hero_sit_wear_bg
        show sitting_embrace_2_hero_face o0
        show sitting_embrace_2_wsis_body 1
        show sitting_embrace_2_wsis_face o0
        show expression Sit_Wear("sitting_embrace_2_wsis_wear 1", "wsis") as wsis_sit_wear
        show sitting_embrace_2_hero_fg_body 1

    else:
        show sitting_hero_body 1 at LC
        show sitting_hero_face 1a0 at LC
        show expression Sit_Wear("sitting_hero_wear 1", "hero", "") as hero_sit_wear at LC
        show sitting_wsis_body 1 at RC
        show expression Sit_Wear("sitting_wsis_wear 1", "wsis", "") as wsis_sit_wear at RC

    # Above the arm sleeve's zorder, so the lighting still covers every layer of the shot.
    show fx_light zorder 30

    with Fade(1, 0, 2)

    return

# ---------------------------------------------------------------------------
label wsis_movie_1: # player chooses a theme
# ---------------------------------------------------------------------------
    # ---------------------------------------------------------------------------
    # Phase 1:  Choosing
    # ---------------------------------------------------------------------------
    $ a_event_3 = "hero" # Chooser

    menu:
        "Let her decide" if 0 > 1:
            $ a_event_3 = "wsis"
            $ a_event_0 = renpy.random.random()

            hero "You can decide, [C_Nam][hero_to_wsis][C_Off]!"

            if a_event_0 < 0.25 and wsis_quest_9 == 0:
                $ a_event_1 = "horror"
                wsis "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I've never actually seen a horror movie before{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} How about we watch one?"
                hero "{bt}Sure!{/bt}{w=[wt3]} Let's do it!"

            elif a_event_0 < 0.4:
                $ a_event_1 = "action"
                wsis "Action!"
                hero "Nice choice!"

            else:
                $ a_event_1 = "romance"
                wsis "R{w=[wt1]}-romance"
                hero "Okay!"

        "Action" if 0 > 1:
            $ a_event_1 = "action"
            hero "Let's watch an action movie!"

        "Romance" if 0 > 1:
            $ a_event_1 = "romance"
            hero "Let's watch a romance!"

        "Horror":
            $ a_event_1 = "horror"
            hero "Let's watch something scary!"

            if "Watch_Horror" in wsis_know and wsis_quest_9 >= 2:
                wsis "{aw}No{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/aw}{w=[wt2]} Absolutely not.{w=[wt3]} Pick something else."
                jump wsis_movie_1

            elif wsis_quest_9 >= 1:
                wsis "{aw}Ehh...?{/aw}{w=[wt3]} W{w=[wt1]}-Why do you want to watch this kind of thing again?"
                hero "Because it's fun!{w=[wt3]} Come on{w=[wt1]}, don't worry.{w=[wt3]} If you can't sleep after{w=[wt1]}, you can always come sleep with me."
                wsis "{aw}So THAT'S your plan, you pervert!?{/aw}"
                hero "It's just a movie!{w=[wt3]} You'll be fine{w=[wt1]}, I promise!"
                wsis "F{w=[wt1]}-fine..."

            else:
                wsis "Are you sure about that?"
                hero "Yes!{w=[wt3]} Don't tell me you're scared?"
                wsis "{aw}Of course not{w=[wt1]}, idiot!{/aw}{w=[wt3]} I was just worried about {b}you{/b}."
                hero "{bt}Sure... Sure...{/bt}{w=[wt3]} So it's decided!"
                wsis "Hmph!{w=[wt2]} But don't complain if you can't sleep after!"

        "Return":
            jump wsis_interact_hangout

    # ---------------------------------------------------------------------------
    # Phase 2:  Movie Intro
    # ---------------------------------------------------------------------------
    if CountItem_Inventory(item_id="Eat_Veg_Corn", inventory_id=inventory_fridge):
        wsis "There's [C_Itm]Corn[C_Off] in the fridge.{w=[wt3]} Let's make [C_Itm]Popcorn[C_Off]!"
        $ RemItem_Inventory("Eat_Veg_Corn", inventory_id=inventory_fridge)
        $ AddItem_Inventory("Eat_Snack_Popcorn", item_count=1, item_quality=5, inventory_id=inventory_home_table)

    call wsis_movie_sprites from _call_wsis_movie_sprites_1

    if a_event_1 == "action":
        call wsis_movie_action_1 from _call_wsis_movie_action_1
    elif a_event_1 == "romance":
        call wsis_movie_romance_1 from _call_wsis_movie_romance_1
    elif a_event_1 == "horror":
        call wsis_movie_horror_1 from _call_wsis_movie_horror_1_1

    # ---------------------------------------------------------------------------
    # Phase 3:  Loop
    # ---------------------------------------------------------------------------
    call wsis_movie_loop from _call_wsis_movie_loop_1

    $ gametimehour = 23
    $ gametimemin = 0
    call gametime from _call_gametime_121
    jump show_ui

# ---------------------------------------------------------------------------
label wsis_movie_loop(popcorn=None): # Watching the movie — the loop itself, venue-independent
# ---------------------------------------------------------------------------
# Split out of `wsis_movie_1` so the cinema date can run the identical movie without the living room around it. The caller owns the theme (`a_event_1`), the sprites, and the clock — this label only watches.
# `popcorn` overrides the home-table inventory check for callers that bought their own (the cinema does).
# ---------------------------------------------------------------------------

    $ a_event_2 = 120 # Movie duration in minutes

    $ a_event_4 = 50 # wsis Focus
    $ a_event_5 = 50 # wsis Sadness/Happiness
    $ a_event_6 = 0  # wsis Fear
    $ a_event_7 = 50 # wsis Sleepiness/Adrenaline

    $ a_event_8 = 100 # Popcorn percent
    $ a_event_9 = False # Is Chatting

    while a_event_2 > 0:

        $ a_event_4 = min(100, max(0, a_event_4))
        $ a_event_5 = min(100, max(0, a_event_5))
        $ a_event_6 = min(100, max(0, a_event_6))
        $ a_event_7 = min(100, max(0, a_event_7))
        $ a_event_8 = min(100, max(0, a_event_8))

        menu:
            # Each round is a small choice: sharing the bucket and talking to her are worth more than staring at the screen. On a date the same picks feed the axes; at home only the affinity does.
            "Eat popcorn" if (popcorn if popcorn is not None else CountItem_Inventory(item_id="Eat_Snack_Popcorn", inventory_id=inventory_home_table)):
                $ a_event_8 -= int(5 + renpy.random.random() * 20)
                $ msg.msg(renpy.translate_string("You ate some popcorn"))
                $ Movie_Beat(love=0.2, fun=1)

            "Focus on movie":
                $ msg.msg(renpy.translate_string("You're watching the movie"))
                $ Movie_Beat(love=0.1)

            "Chat":
                $ a_event_9 = True
                $ Movie_Beat(love=0.3, rom=1, fun=1)

            "Check [C_Nam][fnamewsis][C_Off]":
                if a_event_6 >= 75:
                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] looks really scared"))
                elif a_event_6 >= 30:
                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] looks tense"))
                elif a_event_5 < 20:
                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] looks sad"))
                elif a_event_5 >= 80:
                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] looks happy"))
                elif a_event_7 < 20:
                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] looks sleepy"))
                elif a_event_7 >= 80:
                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] looks excited"))
                elif a_event_4 >= 75:
                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] is fully focused"))
                else:
                    $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] seems relaxed"))

                $ Movie_Beat(love=0.2)

        $ a_event_0 = renpy.random.random()

        if a_event_1 == "action":
            call wsis_movie_action_2 from _call_wsis_movie_action_2
        elif a_event_1 == "romance":
            call wsis_movie_romance_2 from _call_wsis_movie_romance_2
        elif a_event_1 == "horror":
            call wsis_movie_horror_2 from _call_wsis_movie_horror_2

        if renpy.random.random() * 100 >= a_event_4:
            $ a_event_8 -= int(5 + renpy.random.random() * 20)
            $ msg.msg(renpy.translate_string("[C_Nam][fnamewsis][C_Off] grabbed some popcorn"))

        $ a_event_2 -= 20

    return

# ---------------------------------------------------------------------------
label wsis_movie_action_1: # Movie Action Intro
# ---------------------------------------------------------------------------
    $ wsis_quest_7 = 1

    $ a_event_0 = renpy.random.random()

    if a_event_0 < 1/4:
        if a_event_3 == "wsis":
            wsis "Okay{w=[wt1]}, Let's give it a shot."
            hero "Deal."
        else:
            wsis "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Could've been worse{w=[wt1]}, I guess."
            hero "High praise coming from you."
            wsis "Just don't expect me to get all excited over explosions."
            hero "We'll see about that."

    elif a_event_0 < 2/4:
        if a_event_3 == "wsis":
            wsis "What about this one?"
            hero "Seems fine.{w=[wt3]} Let's see it!"
        else:
            wsis "Just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} don't pick something mindlessly stupid."
            hero "Trust me!"
            wsis "I don't."

    elif a_event_0 < 3/4:
        wsis "Is it at least a good one{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} or are we watching something with a zero budget CGI finale?"
        if a_event_3 == "wsis":
            hero "You picked it, [C_Nam][hero_to_wsis][C_Off]!"
            wsis "{aw}That doesn't answer my question!!!{/aw}"
        else:
            hero "I think we'll like it."
            wsis "I'll be the judge of that."

    else:
        wsis " You know I've seen more action movies than you{w=[wt1]}, right?"
        if a_event_3 == "wsis":
            hero "Then why did it take you so long to pick one?"
            wsis "{aw}Because I was being {b}considerate{/b}{w=[wt1]}, you ungrateful!!!{/aw}"
        else:
            hero "Then feel free to rate my choice when it's over."
            wsis "Oh{w=[wt1]}, I will."

    return


# ---------------------------------------------------------------------------
label wsis_movie_romance_1: # Movie Romance Intro
# ---------------------------------------------------------------------------
    $ wsis_quest_8 = 1

    $ a_event_0 = renpy.random.random()

    if a_event_0 < 1/4:
        if a_event_3 == "wsis":
            wsis "This one looks cute!"
            hero "Great{w=[wt1]}, Let's watch!"
        else:
            hero "What about this one?"
            wsis "Looks cute..."
            hero "Great{w=[wt1]}, Let's watch!"

    elif a_event_0 < 2/4:
        if a_event_3 == "wsis":
            wsis "Don't make it weird."
            hero "Wasn't planning to."
            wsis "Good."
        else:
            wsis "If this has a bad ending{w=[wt1]}, I'm blaming you."
            hero "Noted."

    elif a_event_0 < 3/4:
        if a_event_3 == "wsis":
            wsis "It{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} it has good reviews{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} that's all."
            hero "That's all"
            wsis "{aw}That's{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {b}all{/b}!{/aw}{w=[wt3]} Now shut up."
        else:
            hero "This one is good rated.{w=[wt2]} Let's if it's really that good."
            wsis "Fine."

    else:
        wsis "If they break up over a stupid misunderstanding that one conversation would fix{w=[wt1]}, I'm turning it off."
        if a_event_3 == "wsis":
            hero "You picked a romance movie and that's your condition"
            wsis "Those are my terms{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} take it or leave it."
        else:
            hero "That's like half of all romance movies."
            wsis "Exactly{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} so choose wisely."

    return


# ---------------------------------------------------------------------------
label wsis_movie_horror_1(at_home=True): # Movie Horror Intro
# ---------------------------------------------------------------------------
# `at_home` swaps the two beats that only work in the living room (the watch history, the lights) for cinema versions — everything else plays the same wherever they are watching.
# ---------------------------------------------------------------------------
    $ wsis_quest_9 = 1

    if "Watch_Horror" not in wsis_know:
        $ wsis_know.append("Watch_Horror")

    $ a_event_0 = renpy.random.random()

    if a_event_0 < 1/5:
        wsis "I'm not scared!"
        hero "It hasn't even started yet."
        wsis "I know!{w=[wt2]} I just want that on record before it starts."
        hero "{bt}Sure... Sure...{/bt}"

    elif a_event_0 < 2/5:
        if at_home:
            wsis "If I can't sleep after this{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'm deleting it from the watch history."
        else:
            wsis "If I can't sleep after this{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} you're the one walking me to my room."
        hero "And if you sleep fine?"
        wsis "Then{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} we never speak of this again."
        hero "Deal."

    elif a_event_0 < 3/5:
        wsis "How scary are we talking?"
        hero "It says here:{w=[wt2]} {i}'based on true events'{/i}."
        wsis "W{w=[wt1]}-whatever!{w=[wt3]} I won't get scared."

    elif a_event_0 < 4/5:
        if a_event_3 == "wsis":
            wsis "I can't believe I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} suggested this."
            hero "We don't have to watch it"
            wsis "{aw}No{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/aw}{w=[wt3]} I said it{w=[wt1]}, we're watching it{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I don't back down."
            hero "Brave."
            wsis "Shut up."
        else:
            wsis "You better not laugh if I react to anything."
            hero "No promises."
            wsis "Hmph!"

    elif not at_home:
        wsis "Back row.{w=[wt3]} And you're sitting on the aisle side."
        hero "Why the aisle side?"
        wsis "So there's something between me and{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} whatever comes down it."
        hero "So I'm the shield."
        wsis "You're the {b}volunteer{/b}.{w=[wt3]} There's a difference and I'm not explaining it."

    else:
        wsis "The lights stay on."
        hero "It's a horror movie"
        wsis "The{w=[wt2]}-lights{w=[wt2]}-stay{w=[wt2]}-on!"
        if a_event_3 == "wsis":
            hero "You suggested this movie"
            wsis "And I'm watching it{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} with{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} the{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} lights{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} on{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} is that a problem?"
            hero "Not at all."
        else:
            hero "Fine{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} lights on."
            wsis "Thank you."
            hero "You're welcome."
            wsis "Don't make it a thing."
            hero "Already forgotten."

    return

# ---------------------------------------------------------------------------
label wsis_movie_action_2: # Movie Action Loop
# ---------------------------------------------------------------------------
    $ a_event_4 += 5 + (renpy.random.random() * 20)
    $ a_event_0 = renpy.random.random()

    if a_event_0 >= 0.75: # Epic scene
        $ add_stat("wsis", "lust", 2 * renpy.random.random())
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(fun=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "{bt}YES!!!{/bt}{w=[wt3]} That's what I'm talking about!!!"
                hero "{lg}Ha ha ha...{/lg}{w=[wt3]} Look at your face right now!"
                wsis "{aw}W{w=[wt1]}-What!?{/aw}{w=[wt3]} It was a cool scene{w=[wt1]}, that's all!{w=[wt3]} Stop laughing!"

            elif a_event_0 >= 3/5:
                hero "{bt}OHHH!!!{/bt}{w=[wt3]} Did you see that!?"
                wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I saw it!{w=[wt3]} Play it back{w=[wt1]}, play it back{w=[wt1]}, play it back!"
                hero "We can't rewind a movie, [C_Nam][hero_to_wsis][C_Off]"
                wsis "Then don't distract me and let me watch!"

            elif a_event_0 >= 2/5:
                if a_event_3 == "hero":
                    wsis "{bt}Hmph{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/bt}{w=[wt3]} Don't get smug just because you picked a good scene."
                    hero "You{w=[wt1]}'re{w=[wt1]} W{w=[wt1]}E{w=[wt1]}L{w=[wt1]}C{w=[wt1]}O{w=[wt1]}M{w=[wt1]}E"
                    wsis "{aw}I{w=[wt1]}-I didn't thank you{w=[wt1]}, idiot!!!{/aw}"
                else:
                    wsis "{bt}See?{/bt}{w=[wt3]} I told you I know good movies!"
                    hero "{bt}Okay... Okay...{/bt}{w=[wt4]} You have good taste, [C_Nam][hero_to_wsis][C_Off]."
                    wsis "{bt}Obviously{/bt}{w=[wt3]} Remember that."

            elif a_event_0 >= 1/5:
                hero "Now {b}that{/b} was a clean finish."
                wsis "The choreography was decent{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I'll give it that."
                hero "Decent!?{w=[wt3]} That was {b}insane{/b}!"
                wsis "It was{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} well planned{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Okay{w=[wt1]}, fine{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} it was cool."

            else:
                wsis "That can't be physically possible."
                hero "It's a movie, [C_Nam][hero_to_wsis][C_Off]"
                wsis "I know it's a movie{w=[wt1]}, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} if you're going to ignore physics{w=[wt1]}, at least be {b}consistent{/b} about it!"
                hero "{lg}Ha ha ha...{/lg}{w=[wt3]} You're the only person who critiques the laws of physics during an action movie."
                wsis "{aw}It's called {b}having standards{/b}!{/aw}"

    elif a_event_0 >= 0.45: # Action scene
        $ add_stat("wsis", "lust", 0.5 * renpy.random.random())
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(fun=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "Okay but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} why didn't the villain just dodge that?{w=[wt3]} He literally had time."
                hero "Because he's the villain{w=[wt1]}, he has to lose eventually."
                wsis "That's lazy writing!{w=[wt3]} A villain with actual brain cells would've survived that!{w=[wt2]} He wouldn't even need an incredible person!"
                hero "I bet you'd never dodge that!"
                wsis "Shut up!{w=[wt2]} You're the weak here!"

            elif a_event_0 >= 3/5:
                hero "He's been waiting for this rematch the whole movie"
                wsis "And he still almost lost{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} makes it better honestly."
                hero "Right?{w=[wt3]} The suspense was real."
                wsis "{bt}Mmh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/bt}{w=[wt3]} I didn't hate it."

            elif a_event_0 >= 2/5:
                wsis "His fighting style changed after the training arc{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Did you catch that?"
                hero "Honestly{w=[wt1]}, no"
                wsis "{aw}Were you even watching{w=[wt1]}, moron!?{/aw}"

            elif a_event_0 >= 1/5:
                hero "Go{w=[wt1]}, go{w=[wt1]}, go{w=[wt1]}, go!"
                wsis "MOVE{w=[wt1]}, idiot{w=[wt1]}, MOVE{w=[wt1]}-{w=[wt1]}-!"
                pause(1)
                wsis "We did not just cheer at the same time."
                hero "Definitely did not."

            else:
                wsis "He's outmatched"
                hero "He'll pull something.{w=[wt3]} He's the hero!"
                wsis "If he pulls an asspull power-up out of nowhere I'm turning this off."
                hero "How many movies have ended exactly like that though?"
                wsis "{bt}Too many...!{/bt}{w=[wt3]} That's my point."

    elif a_event_0 >= 0.25: # Funny scene
        $ a_event_5 += 25 * renpy.random.random()
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(love=0.3, fun=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "{lg}Hee hee hee hee...{/lg}{w=[wt4]} Okay{w=[wt1]}, I wasn't expecting that."
                hero "His face{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} the face he made"
                wsis "I know{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {gg}Tchi-hi-hi{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/gg}{w=[wt3]} Stop{w=[wt1]}, I can't breathe"

            elif a_event_0 >= 3/5:
                wsis "{gg}Tchi-hi{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/gg}{w=[wt3]} That was dumb."
                hero "Super dumb{w=[wt1]}.{w=[wt3]} and yet here I am{w=[wt1]}, crying."
                wsis "{gg}Tchi-hi-hi{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/gg}{w=[wt3]} Me too{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} shut up."

            elif a_event_0 >= 2/5:
                wsis "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} didn't expect them to put a comedy bit in the middle of all that."
                hero "Tonal whiplash{w=[wt1]}.{w=[wt2]} but it worked somehow."
                wsis "Somehow{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} yeah."

            elif a_event_0 >= 1/5:
                hero "Did he just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {bt}TRIP{/bt}?{w=[wt3]} In the middle of the final battle??"
                wsis "{lg}Fu hu hu hu...{/lg}{w=[wt3]} The big villain tripped on his {b}own cape{/b}!!!"
                hero "WRITE THAT DOWN{w=[wt1]}, WRITE THAT DOWN{w=[wt1]}-{w=[wt1]}-"
                wsis "{lg}Fu hu hu hu hu...{/lg}{w=[wt3]} I can't{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Stop{w=[wt1]}, stop"

            else:
                wsis "Is the sidekick always like this?"
                hero "Pretty much{w=[wt1]}.{w=[wt2]} but that's why you end up loving him."
                wsis "Debatable{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} he has his moments."

    elif a_event_0 >= 0.15: # Sad scene
        $ a_event_5 -= 25 * renpy.random.random()
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(love=0.5, rom=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "Don't say anything."
                hero "I wasn't going to."
                wsis "Good."

            elif a_event_0 >= 3/5:
                hero "Oh no..."
                wsis "Shut up and watch."

            elif a_event_0 >= 2/5:
                hero "They didn't have to do him like that"
                wsis "He was the best character in the whole thing{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} He didn't deserve it."
                hero "That's how you know a movie is good."
                wsis "{bt}Hmph{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/bt}{w=[wt3]} Cheap trick."

            elif a_event_0 >= 1/5:
                wsis "Don't{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} don't you dare make a comment right now."
                hero "I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} wasn't going to."
                wsis "Good"

            else:
                wsis "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} that escalated fast"
                hero "It's always the ones you don't expect"
                wsis "Yeah"

    else: # Bad scene (plot hole, boring, etc.)
        $ add_stat("wsis", "rage", 0.5 * renpy.random.random())
        $ a_event_4 -= renpy.random.random() * 50
        $ a_event_7 -= renpy.random.random() * 0.0001 * gametimehour * gametimehour * gametimehour * gametimehour

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "Wait{w=[wt1]}, wait{w=[wt1]}, wait{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} How did they manage to do it!?{w=[wt1]} They were completely defeated just seconds ago!"
                hero "It's the power of friendship!"
                wsis "{aw}Shut Up!!!{/aw}"

            elif a_event_0 >= 3/5:
                wsis "This is the third time they used the same shot."
                hero "Are you sure?"
                wsis "{b}Positive{/b}{w=[wt3]} Same movement{w=[wt2]}, same angle{w=[wt2]}, same scenery{w=[wt2]}, same everything{w=[wt3]} They're being lazy!"
                hero "You{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} actually notice that stuff?"
                wsis "I watch a lot of movies, okay!?"

            elif a_event_0 >= 2/5:
                wsis "She just stood there!{w=[wt3]} Why!?{w=[wt3]} It doesn't make sense!!!"
                hero "Some people just don't have such brilliant minds."
                wsis "{aw}The screenwriter of this movie surely doesn't have!{/aw}"

            elif a_event_0 >= 1/5:
                wsis "This is getting stupid."
                hero "Give it a chance!"
                wsis "I've given it a lot!{w=[wt3]} How much more chance does it need?"

            else:
                wsis "If his plan was this obvious from the beginning{w=[wt2]}, why did it take them the whole movie to figure it out?"
                hero "Because then there'd be no movie"
                wsis "Exactly!{w=[wt2]} There should be no movie!!!"

    return

# ---------------------------------------------------------------------------
label wsis_movie_romance_2: # Movie Romance Loop
# ---------------------------------------------------------------------------
    $ a_event_4 += 5 + (renpy.random.random() * 20)
    $ a_event_0 = renpy.random.random()

    if a_event_0 >= 0.75: # Erotic/hot scene
        $ add_stat("wsis", "lust", 2 * renpy.random.random())
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(spi=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                if a_event_3 == "hero":
                    wsis "{aw}So THAT'S why you picked this{w=[wt1]}, you pervert!!!{/aw}"
                    hero "I picked it randomly"
                    wsis "{aw}PERVERT!!!{/aw}"
                else:
                    hero "{bt}Ehhh...!?{/bt}{w=[wt3]} So this is the kind of movie you like...?"
                    wsis "{aw}I{w=[wt1]}-It wasn't supposed to have these indecencies!{w=[wt3]} It's not like I knew{w=[wt1]}-{w=[wt1]}-!{/aw}"
                    hero "{bt}Sure... Sure...{/bt}"
                    wsis "{aw}SHUT{w=[wt1]}-{b}UP{/b}-!!!{/aw}"

            elif a_event_0 >= 3/5:
                wsis "Don't{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} say{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} a{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} single{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} word."
                hero "Well-{nw}"
                wsis "{aw}SHUT UP!!!{/aw}"

            elif a_event_0 >= 2/5:
                wsis "This is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} completely unnecessary!"
                hero "It's artistically bold?"
                wsis "{aw}Hmph...!{/aw}{w=[wt2]} Don't {b}look at me{/b} when you say that!!!" id wsis_movie_romance_2_5d765b6c_1

            elif a_event_0 >= 1/5:
                wsis "Why she got naked!?"
                hero "Oh{w=[wt2]}, I thing they will-{w=[wt1]}{nw}"
                wsis "{aw}Ahhhhh...!{/aw} Shut up!!!{w=[wt3]} Stop looking, you pervert!!!"
                if a_event_3 == "hero":
                    hero "I'm just watching the movie!{w=[wt3]} It's not my fault!"
                    wsis "Who do you think chose this shamelessly movie!?"
                else:
                    hero "It's not my fault! You were the one who chose the movie!"
                    wsis "Shut up!!!"

            else:
                wsis "{aw}Ugh...!{/aw} Turn down the sound!"

    elif a_event_0 >= 0.45: # Romantic scene
        $ add_stat("wsis", "lust", 0.5 * renpy.random.random())
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(love=0.5, rom=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "He's been carrying her feelings the whole time."
                hero "You think she knew?"
                wsis "Of course she knew{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} She just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} wasn't ready."
                hero "Sounds{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} familiar somehow."
                wsis "{aw}Watch{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} the{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} movie.{/aw}"

            elif a_event_0 >= 3/5:
                hero "She's going to say it."
                wsis "Don't jinx it."
                hero "She's definitely going to say it."
                wsis "If she doesn't say it because of you{w=[wt1]}, I swear"
                hero "She said it."
                wsis "{bt}Hmph{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} Fine{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/bt}"

            elif a_event_0 >= 2/5:
                wsis "Why do they always confess in the rain"
                hero "More dramatic."
                wsis "More pneumonia{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} is what it is."
                hero "{lg}Ha ha ha...{/lg}{w=[wt3]} You're so unromantic."
                wsis "{aw}I'm {b}practical{/b}!!!{/aw}"

            elif a_event_0 >= 1/5:
                wsis "He waited three years to say that"
                hero "Some things take time"
                wsis ""
                hero ""
                pause(1.0)
                wsis "Don't{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} make it weird."

            else:
                hero "She keeps pushing him away{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} but she clearly cares."
                wsis "She's scared{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} it's different."
                hero "Is it"
                wsis "Watch the movie, [C_Nam][wsis_to_hero][C_Off]."

    elif a_event_0 >= 0.3: # Funny scene
        $ a_event_5 += 25 * renpy.random.random()
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(love=0.3, fun=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                hero "The side character is carrying this whole movie."
                wsis "{gg}Tchi-hi-hi!{/gg} She keeps saying exactly what I'm thinking."
                hero "Give her the lead role, honestly."
                wsis "{gg}Tchi-hi!{/gg} Right?!"

            elif a_event_0 >= 3/5:
                hero "Did you see that!?"
                wsis "{gg}Tchi-hi-hi!{/gg} I can't believe they actually did that!"
                hero "I was NOT expecting that."
                wsis "Me neither! {gg}Tchi-hi!{/gg} This movie just went up a point."

            elif a_event_0 >= 2/5:
                wsis "Why is this so funny!? It's not even that clever!"
                hero "{lg}Ha ha ha!{/lg} It kind of is though."
                wsis "{gg}Tchi-hi-hi!{/gg} Okay. Okay, fine. It is."
                hero "You're smiling."
                wsis "I'm not."
                hero "You are."
                wsis "Watch the movie."

            elif a_event_0 >= 1/5:
                hero "{lg}Ha ha ha!{/lg}"
                wsis "Stop! I'm trying to keep a straight face!"
                hero "{lg}Ha ha ha!{/lg} Why!?"
                wsis "{gg}Tchi-hi-hi!{/gg} Because if I laugh now I'll never stop!"
                hero "{lg}Ha ha ha ha!{/lg}"
                wsis "{lg}Fu hu hu hu!{/lg} Stop laughing, you're making it worse!!!"

            else:
                wsis "I didn't come here to laugh this much."
                hero "Is that a complaint?"
                wsis "No. It's an observation."
                hero "{gg}Tchi-hi!{/gg}"
                wsis "Don't push it."

            if a_event_0 >= 3/5:
                wsis "Why do they always have to make some huge dramatic gesture in front of everyone?"
                hero "It's romantic."
                wsis "It's embarrassing. For everyone involved, including the bystanders."
                hero "If someone did that for you, you'd secretly love it."
                wsis "{aw}I would {b}not{/b}!!!{/aw} I'd walk away and never speak to them again!"
                hero "Sure you would."
                wsis "{aw}I {b}would{/b}!!!{/aw}"

    elif a_event_0 >= 0.15: # Sad scene
        $ a_event_5 -= 25 * renpy.random.random()
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(love=0.5, rom=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "{bt}...{/bt}"
                hero "You okay?"
                wsis "I'm fine. It's just... she worked so hard and he didn't even notice."
                hero "He'll notice."
                wsis "He better."

            elif a_event_0 >= 3/5:
                wsis "I wasn't expecting it to go there."
                hero "Yeah. Me neither."
                wsis "It's good though. When a story actually surprises you."
                hero "Yeah."
                wsis "{bt}...{/bt}"

            elif a_event_0 >= 2/5:
                hero "That one hurt."
                wsis "It did."
                hero "Didn't expect to feel that watching this."
                wsis "That's how you know it's a good movie."
                hero "Since when do you give out compliments?"
                wsis "I'm complimenting the movie, not you."

            elif a_event_0 >= 1/5:
                wsis "I'm not crying. I got something in my eye."
                hero "Both eyes?"
                wsis "{aw}Both eyes, yes, [C_Nam][wsis_to_hero][C_Off], shut up.{/aw}"
                hero "{bt}...{/bt}"
                wsis "Not a word."
                hero "Wasn't going to."

            else:
                wsis "Why does it always hit harder when it's the quiet moments?"
                hero "Because you're not braced for it."
                wsis "{bt}...{/bt} Yeah. That's exactly it."
                hero "{bt}...{/bt}"

    else: # Bad scene
        $ add_stat("wsis", "rage", 0.5 * renpy.random.random())
        $ a_event_4 -= renpy.random.random() * 50
        $ a_event_7 -= renpy.random.random() * 0.0001 * gametimehour * gametimehour * gametimehour * gametimehour

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "She forgave him{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} just like that"
                hero "Love makes people{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} flexible"
                wsis "{aw}He stood her up {b}three times{/b}!!!{/aw}{w=[wt3]} That's not love{w=[wt1]}, that's a pattern!!!"
                hero "Okay{w=[wt1]}, yeah{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} fair point."

            elif a_event_0 >= 3/5:
                wsis "This is everything wrong with romance movies."
                hero "What is?"
                wsis "She changed {b}everything{/b} about herself for him{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} and he's just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} standing there being mediocre."
                hero "When you put it like that"
                wsis "He doesn't deserve her{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I said what I said."

            elif a_event_0 >= 2/5:
                hero "This subplot{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} makes no sense"
                wsis "It doesn't exist to make sense{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} it exists to pad the runtime."
                hero "How can you tell"
                wsis "I watch a lot of bad movies{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} you develop a sense."

            elif a_event_0 >= 1/5:
                wsis "If the rival love interest has more chemistry with her than the main guy{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} that's a writing problem."
                hero "The writers noticed too{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} they just{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} committed to the original plan."
                wsis "Cowardice."

            else:
                wsis "They're going to get back together after a three minute apology{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} aren't they"
                hero "Probably"
                wsis ""
                hero ""
                wsis "At least the popcorn's good."

    return

# ---------------------------------------------------------------------------
label wsis_movie_horror_2: # Movie Horror Loop
# ---------------------------------------------------------------------------
    $ a_event_4 += 5 + (renpy.random.random() * 20)
    $ a_event_0 = renpy.random.random()

    if a_event_0 >= 0.75: # Jump scare / Horror scene
        $ a_event_6 += 30 * renpy.random.random()
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(lust=0.5, spi=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "{pa}AAAHHH!!!{/pa}{nw}"
                pause(0.3)
                hero "C'mon{w=[wt2]}, was it that scary?"
                wsis "{aw}SHUT UP!!!{/aw}{w=[wt2]} I wasn't scared!{w=[wt3]} I was {b}startled{/b}!{w=[wt2]} That's completely different!!!"
                hero "Sure it is."
                wsis "{aw}It{w=[wt2]} {b}IS{/b}!!!{/aw}"

            elif a_event_0 >= 3/5:
                wsis "{nw}"
                pause(0.3)
                hero "You grabbed my arm."
                wsis "{aw}I needed something to hold!{w=[wt2]} Let go!!!{/aw}"
                hero "You're still holding it."
                wsis "{aw}I {b}know{/b}!!!{w=[wt2]} SHUT UP!!!{/aw}"

            elif a_event_0 >= 2/5:
                wsis "{pa}HUH!!!{/pa}{w=[wt4]} I wasn't ready for that!!!"
                hero "Me neither."
                wsis "You better not tell anyone I made that sound."
                hero "What sound?"
                wsis "Good."

            elif a_event_0 >= 1/5:
                wsis "I knew it was coming.{w=[wt3]} I {b}knew{/b}{w=[wt2]} and I still—"
                hero "{gg}hee-hee-hee...{/gg}{w=[wt2]} Everyone does that, [C_Nam][hero_to_wsis][C_Off]."
                wsis "{aw}Don't laugh!!!{/aw}{w=[wt3]} It's a biological response!{w=[wt2]} It's involuntary!"
                hero "Very involuntary."
                wsis "{aw}Say that again and I {b}will{/b} hurt you!!!{/aw}"

            else:
                pause(0.5)
                wsis "{pa}!!!{/pa}"
                hero "{bt}...{/bt}"
                pause(0.8)
                wsis "We don't talk about what just happened."
                hero "Already forgotten."

    elif a_event_0 >= 0.3: # Tense / suspense scene
        $ a_event_6 += 10 * renpy.random.random()
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(love=0.3, rom=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "Don't go.{w=[wt2]} Don't go.{w=[wt2]} {b}Don't{/b}—"
                hero "They went."
                wsis "{aw}WHY WOULD THEY GO!!!{/aw}"
                hero "Horror movie logic."
                wsis "{aw}It's not {b}logic{/b}!!!{w=[wt2]} It's {b}stupidity{/b}!!!{/aw}"

            elif a_event_0 >= 3/5:
                hero "{bt}...{/bt}"
                wsis "{bt}...{/bt}"
                pause(1.0)
                hero "You moved closer."
                wsis "{aw}No I didn't.{/aw}"
                hero "You did."
                wsis "{aw}Shut up.{/aw}"
                pause(0.5)
                hero "You're still close."
                wsis "{aw}I {b}said{/b} shut up!!!{/aw}"

            elif a_event_0 >= 2/5:
                wsis "I hate when it goes quiet like this."
                hero "That's when you know—"
                wsis "{aw}Don't finish that sentence!!!{/aw}"
                hero "{bt}...{/bt}"
                wsis "I mean it."
                hero "I wasn't going to say anything bad."
                wsis "{aw}Yes you were!!!{/aw}"

            elif a_event_0 >= 1/5:
                wsis "Why would they split up!?{w=[wt2]} They {b}always{/b} split up!"
                hero "Horror movie rule number one."
                wsis "If anyone says{w=[wt2]} 'hello? is anyone there?'{w=[wt2]} I'm turning this off."

            else:
                wsis "Something is about to happen.{w=[wt2]} I can feel it."
                hero "Then look away."
                wsis "I can't look away."
                hero "Morbid curiosity."
                wsis "Don't narrate my experience right now."
                hero "Sorry."
                pause(0.5)
                hero "Something is definitely about to—"
                wsis "{aw}I {b}said{/b} stop!!!{/aw}"

    elif a_event_0 >= 0.15: # Sad/emotional scene
        $ a_event_5 -= 25 * renpy.random.random()
        $ a_event_4 += renpy.random.random() * 10
        $ Movie_Beat(love=0.5, rom=1)

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "That was actually really sad."
                hero "Horror hits different when it makes you feel something."
                wsis "{bt}Hmph.{/bt}{w=[wt2]} Don't get sentimental about it."
                hero "You brought it up."
                wsis "Watch the movie."

            elif a_event_0 >= 3/5:
                wsis "I didn't expect to feel bad for it."
                hero "That's the whole point."
                wsis "Make you feel bad for the thing trying to kill everyone?"
                hero "Make you understand why it does."
                wsis "That's worse somehow."
                hero "Yeah."

            elif a_event_0 >= 2/5:
                wsis "That was completely unnecessary."
                hero "Yeah."
                wsis "{bt}...{/bt}"
                pause(0.8)
                wsis "I hate this movie."
                hero "Me too."
                wsis "We're finishing it."
                hero "Obviously."

            elif a_event_0 >= 1/5:
                wsis "Is it weird that the sad parts scare me more than the scary parts?"
                hero "That's what makes it good horror.{w=[wt2]} You're scared because you care."
                wsis "Yeah.{w=[wt2]} That makes sense."

            else:
                wsis "They didn't have to do that."
                hero "No.{w=[wt2]} They didn't."
                wsis "It's cheap."
                hero "It worked though."
                wsis "That's what makes it cheap."

    else: # Bad scene (stupid decisions, plot holes)
        $ add_stat("wsis", "rage", 0.5 * renpy.random.random())
        $ a_event_4 -= renpy.random.random() * 50
        $ a_event_7 -= renpy.random.random() * 0.0001 * gametimehour * gametimehour * gametimehour * gametimehour

        if a_event_9 == True:
            $ a_event_0 = renpy.random.random()

            if a_event_0 >= 4/5:
                wsis "{aw}Why would they go back!?{w=[wt2]} WHY WOULD THEY GO {b}BACK{/b}!!!{/aw}"
                hero "They forgot something."
                wsis "{aw}NOTHING is worth going back for!!!{/aw}"
                hero "To be fair—"
                wsis "{aw}There is no 'to be fair'!!!{/aw}"

            elif a_event_0 >= 3/5:
                wsis "I already know who did it.{w=[wt2]} It's that guy!"
                hero "What?{w=[wt2]} We're barely into it."
                wsis "It's obvious.{w=[wt2]} The clues have been there since the beginning."
                hero "You can't know that already."
                wsis "Watch!"
                hero "..."
                wsis "See?{w=[wt2]} I told you."
                hero "That's actually impressive."
                wsis "I watch a lot of movies."

            elif a_event_0 >= 2/5:
                wsis "They have {b}everything{/b} they need to survive and they're making the worst possible choice."
                hero "Panic."
                wsis "{aw}That's not panic{w=[wt2]}, that's {b}stupidity{/b}!!!{/aw}{w=[wt2]} Panic has limits!"
                hero "{lg}Ha ha ha!{/lg}"
                wsis "I'm glad you find this funny!"

            elif a_event_0 >= 1/5:
                wsis "If the rules of this world were established at the beginning{w=[wt2]}, why are they ignoring them now?"
                hero "Maybe they forgot."
                wsis "Then {b}we{/b} shouldn't have to suffer for their bad memory!"
                hero "{gg}Tchi-hi!{/gg}{w=[wt2]} You're so invested."
                wsis "{aw}I'm {b}frustrated{/b}! There's a difference!!!{/aw}"

            else:
                hero "Okay{w=[wt2]}, I hated all characters and I'm genuinely rooting for whatever is hunting them at this point."
                wsis "At least it has a consistent strategy."

    return

# ---------------------------------------------------------------------------
label wsis_sleep_together_1:
# ---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_145

    scene bg_0

    play SE1 "DoorKnock.ogg"
    pause 0.2
    play SE1 "DoorKnock.ogg"
    pause 0.2
    play SE1 "DoorKnock.ogg"
    pause 2.0

    mind "(Hmm...? What...?)"

    play SE1 "DoorKnock.ogg"
    pause 0.2
    play SE1 "DoorKnock.ogg"
    pause 0.2
    play SE1 "DoorKnock.ogg"
    pause 2.0

    hero "It's open! You can in!"

    play BGM "audio/W2C - SexyVibes.mp3"

    scene wsis_sleeptogether_1_bg
    show wsis_sleeptogether_1_wsis_body
    show wsis_sleeptogether_1_wsis_face o0
    show fx_light
    with Dissolve(1)

    wsis "..."

    hero "Hey, [C_Nam][hero_to_wsis][C_Off]! What's up?"

    if "Watch_Horror" in wsis_know: # Post Movie Horror

        show wsis_sleeptogether_1_wsis_face o1
        wsis "I can't sleep."

        show wsis_sleeptogether_1_wsis_face o0
        hero "Oh... Did you get scared by what you saw in the movie?"

        show wsis_sleeptogether_1_wsis_face o1
        wsis "Y-yes."

        show wsis_sleeptogether_1_wsis_face o0 with None
        pause

    elif wsis_love >= 60 and wsis_lust >= 20:
        show wsis_sleeptogether_1_wsis_face o1
        wsis "I came to keep you company, [C_Nam][wsis_to_hero][C_Off]."

        show wsis_sleeptogether_1_wsis_face o0 with None

    show wsis_sleeptogether_1_wsis_face o1
    wsis "C-can I... Sleep here tonight...?"

    # It'd be a menu for player to choose, but there's still no interesting reason in game for them to choose to not allow her do it for now, so he'll auto-acept.
    show wsis_sleeptogether_1_wsis_face o0
    hero "S-sure! Come in."

    # WSIS sitting on the bed. HERO makes room, looking at her
    scene wsis_sleeptogether_2_bg
    show wsis_sleeptogether_2_char 1
    show wsis_sleeptogether_2_hero_face 1o0
    show wsis_sleeptogether_2_wsis_face 1o0
    show fx_light
    with Fade(1, 0, 2)

    mind "(Wait, is this really happening? Will I sleep with [C_Nam][hero_about_wsis][C_Off]? That's wearing only this little pajama...? What will happen tonight!?)"

    show wsis_sleeptogether_2_wsis_face 1o1
    wsis "What?"

    show wsis_sleeptogether_2_hero_face 1o1
    show wsis_sleeptogether_2_wsis_face 1o0
    hero "N{w=[wt1]}-nothing.{w=[wt2]} W{w=[wt1]}-welcome!{w=[wt2]}{nw}"

    show wsis_sleeptogether_2_hero_face 1o2
    show wsis_sleeptogether_2_wsis_face 1o0
    hero "N{w=[wt1]}-nothing.{w=[wt2]} W{w=[wt1]}-welcome!{w=[wt2]}{fast}{w=[wt2]} {mind}(That top{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} it barely covers anything.{w=[wt2]} And the shorts{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{/mind}{nw}"

    show wsis_sleeptogether_2_hero_face 1s2
    show wsis_sleeptogether_2_wsis_face 1o0
    hero "N{w=[wt1]}-nothing.{w=[wt2]} W{w=[wt1]}-welcome!{w=[wt2]} {mind}(That top{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} it barely covers anything.{w=[wt2]} And the shorts{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{fast}{w=[wt2]} okay, don't look!{w=[wt1]} Don't look!{w=[wt1]} Don't look!!!){/mind}"

    show wsis_sleeptogether_2_hero_face 1s0
    show wsis_sleeptogether_2_wsis_face 1o1
    wsis "{bt}...You're making a weird face.{/bt}"

    show wsis_sleeptogether_2_hero_face 1s1
    show wsis_sleeptogether_2_wsis_face 1o0
    hero "Am not."

    show wsis_sleeptogether_2_hero_face 1s0
    show wsis_sleeptogether_2_wsis_face 1o1
    wsis "You are."

    show wsis_sleeptogether_2_hero_face 1s1
    show wsis_sleeptogether_2_wsis_face 1o0
    hero "I'm just{w=[wt1]}...{w=[wt2]} that's{w=[wt1]}...{w=[wt3]} {aw}aren't you cold in that?{/aw}"

    show wsis_sleeptogether_2_hero_face 1s0
    show wsis_sleeptogether_2_wsis_face 1o1
    wsis "{aw}W{w=[wt1]}-what's it to you!?{/aw}"

    show wsis_sleeptogether_2_hero_face 1s1
    show wsis_sleeptogether_2_wsis_face 1o2
    hero "I'm asking because I only have one blanket."

    show wsis_sleeptogether_2_hero_face 1s0
    show wsis_sleeptogether_2_wsis_face 1o1
    wsis "Then I'll take it."

    show wsis_sleeptogether_2_hero_face 1s1
    show wsis_sleeptogether_2_wsis_face 1o2
    hero "{aw}Wh{w=[wt1]}-that's not what I said!{/aw}"

    # WSIS lays on the bed, facing HERO
    scene wsis_sleeptogether_2_bg
    show wsis_sleeptogether_2_mg
    show wsis_sleeptogether_2_char 2
    show wsis_sleeptogether_2_hero_face 2o0
    show wsis_sleeptogether_2_wsis_face 2o0
    show fx_light
    with Dissolve(1)

    pause

    if wsis_quest_5 == 0:

        show wsis_sleeptogether_2_wsis_face 2o1
        wsis "It's mine."

        show wsis_sleeptogether_2_hero_face 2o1
        show wsis_sleeptogether_2_wsis_face 2o0
        hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Okay."

        show wsis_sleeptogether_2_hero_face 2o0
        show wsis_sleeptogether_2_wsis_face 2o1
        wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Okay{w=[wt2]}, We can share."

        show wsis_sleeptogether_2_hero_face 2o1
        show wsis_sleeptogether_2_wsis_face 2o0
        hero "O{w=[wt1]}-okay."

        show wsis_sleeptogether_2_hero_face 2o0
        show wsis_sleeptogether_2_wsis_face 2o1
        wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} We're saying much 'okay'."

        show wsis_sleeptogether_2_hero_face 2o1
        show wsis_sleeptogether_2_wsis_face 2o0
        hero "Y{w=[wt1]}-yes{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Let's stop saying 'okay'."

        show wsis_sleeptogether_2_hero_face 2o0
        show wsis_sleeptogether_2_wsis_face 2o1
        wsis "Okay."

        show wsis_sleeptogether_2_hero_face 2o1
        show wsis_sleeptogether_2_wsis_face 2o0
        hero "T{w=[wt1]}-the next one who say 'okay' will sleep without the blanket."

        show wsis_sleeptogether_2_hero_face 2o0
        show wsis_sleeptogether_2_wsis_face 2o1
        wsis "So you did.{w=[wt2]} It's mine."

        show wsis_sleeptogether_2_hero_face 2o1
        show wsis_sleeptogether_2_wsis_face 2o0
        hero "That didn't count."

        show wsis_sleeptogether_2_hero_face 2o0
        show wsis_sleeptogether_2_wsis_face 2o1
        wsis "Why?"

        show wsis_sleeptogether_2_hero_face 2o1
        show wsis_sleeptogether_2_wsis_face 2o0
        hero "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Nevermind."

        show wsis_sleeptogether_2_hero_face 2o0
        show wsis_sleeptogether_2_wsis_face 2o1
        wsis "[C_Nam][wsis_to_hero][C_Off]..."

        show wsis_sleeptogether_2_hero_face 2o1
        show wsis_sleeptogether_2_wsis_face 2o0
        hero "Hi."

        show wsis_sleeptogether_2_hero_face 2o0
        show wsis_sleeptogether_2_wsis_face 2o1
        wsis "D{w=[wt1]}-did I wake you up?"

        show wsis_sleeptogether_2_hero_face 2o1
        show wsis_sleeptogether_2_wsis_face 2o0
        hero "W{w=[wt1]}-well{w=[wt2]}, not really{w=[wt2]}, I was just almost sleeping, I guess.{w=[wt4]} Don't worry."

        show wsis_sleeptogether_2_hero_face 2o0
        show wsis_sleeptogether_2_wsis_face 2o1
        wsis "T{w=[wt1]}-that means I woke you up, idiot..."
     
        show wsis_sleeptogether_2_hero_face 2o1
        show wsis_sleeptogether_2_wsis_face 2o0
        hero "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} N{w=[wt1]}-not really{w=[wt2]}, I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} As I said{w=[wt2]}, you don't need to worry."

    show wsis_sleeptogether_2_hero_face 2o0
    show wsis_sleeptogether_2_wsis_face 2o1
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Am I bothering you?"

    show wsis_sleeptogether_2_hero_face 2o1
    show wsis_sleeptogether_2_wsis_face 2o0
    hero "No."

    show wsis_sleeptogether_2_hero_face 2o0
    show wsis_sleeptogether_2_wsis_face 2o1
    wsis "Even if I disturbed your sleep?"

    show wsis_sleeptogether_2_hero_face 2o1
    show wsis_sleeptogether_2_wsis_face 2o0
    hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]}Yes."

    show wsis_sleeptogether_2_hero_face 2o0
    show wsis_sleeptogether_2_wsis_face 2o1
    wsis "'Yes' that I am or 'yes' that I am not?"

    show wsis_sleeptogether_2_hero_face 2o1
    show wsis_sleeptogether_2_wsis_face 2o0
    hero "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Huh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} M{w=[wt1]}-my brain stopped working.{w=[wt4]} I don't know anymore."

    show wsis_sleeptogether_2_hero_face 2o0
    show wsis_sleeptogether_2_wsis_face 2o1
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Okay.{w=[wt2]} Then{w=[wt1]}, let's sleep."

    # WSIS takes HERO's arm, turns to the other side, with her back pressing against his crotch, placing his arm over her chest, in an embraced pose
    scene wsis_sleeptogether_2_bg
    show wsis_sleeptogether_2_char 3
    show wsis_sleeptogether_2_mg
    show fx_light
    with dissolve

    show wsis_sleeptogether_2_char 4 with dissolve

    pause

    scene wsis_sleeptogether_3_bg
    show wsis_sleeptogether_3_char 1
    show wsis_sleeptogether_3_hero_face 1o0
    show wsis_sleeptogether_3_wsis_face 1o0
    show fx_light
    with Fade(1, 0, 2)

    mind "(Wow{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I can feel her whole body{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} That gigantic ass of her is just right here{w=[wt2]}, it's so big{w=[wt2]}, so round{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Her breasts{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I can already feel it{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} They're tiny and cute{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} And her hair smells like shampoo!{w=[wt3]} It's so fragrant{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I'm getting aroused...!)"

    mind "(It's all so tight close{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} What if I just grab these puffy and perky nipples that are right here in my hand?{w=[wt4]} She herself placed my hand on her chest, right?{w=[wt4]} I wouldn't do anything wrong if I just grab them a little bit, right?{w=[wt4]} And this fat ass{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Is already making me feel hard{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} How could it feel...?{w=[wt3]} She's driving me crazy...!)"

    if wsis_quest_5 == 0:

        stop BGM fadeout 3

        # WSIS hiccups
        show wsis_sleeptogether_3_wsis_face 1o1 with dissolve

        play SE1 "Sniff1.mp3"

        show wsis_sleeptogether_3_hero_face 1o1 with dissolve

        pause

        play SE1 "Sniff2.mp3"

        pause(0.5)

        hero "[C_Mnd]({w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} What was that?{w=[wt3]} Is she okay...?)[C_Off]{w=[wt4]}{nw}"

        show wsis_sleeptogether_3_hero_face 1o2
        hero "[C_Mnd]({w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} What was that?{w=[wt3]} Is she okay...?)[C_Off]{w=[wt4]}{fast} A{w=[wt1]}-are you crying...?"

        show wsis_sleeptogether_3_hero_face 1o1 with None

        pause

        # WSIS nods

        play BGM "audio/W2C - Romance.mp3"

        show wsis_sleeptogether_3_wsis_face 1o2
        wsis "[C_Nam][wsis_to_hero][C_Off]..."

        show wsis_sleeptogether_3_wsis_face 1o1
        hero "Hm...?"

        show wsis_sleeptogether_3_hero_face 1o1
        show wsis_sleeptogether_3_wsis_face 1o2
        wsis "I'm sorry."

        show wsis_sleeptogether_3_hero_face 1o2
        show wsis_sleeptogether_3_wsis_face 1o1
        hero "Well{w=[wt2]}, d{w=[wt1]}-don't worry.{w=[wt3]} I'm just a little tired.{w=[wt3]} But{w=[wt2]}, you know{w=[wt2]}, you're always welcomed here, okay?"

        show wsis_sleeptogether_3_hero_face 1o1
        show wsis_sleeptogether_3_wsis_face 1o2
        wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I still feel bad.{w=[wt4]} I wish we had grown up together{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} We were apart for so long{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} And I've been thinking a lot of bad things about you all these years.{w=[wt4]} And then{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} When you're finally back{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I have been a bad person to you all the time you were here.{w=[wt4]} And yet{w=[wt3]}, you were always doing your best for me."

        wsis "I love you, [C_Nam][wsis_to_hero][C_Off]{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} I want us to never be apart again{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Never never again."

        show wsis_sleeptogether_3_wsis_face 1o1 with None
        show wsis_sleeptogether_3_hero_face 1o0 with dissolve

        pause

        show wsis_sleeptogether_3_char 6
        show wsis_sleeptogether_3_hero_face 6o0
        show wsis_sleeptogether_3_wsis_face 6o0
        with Dissolve(2)

        show wsis_sleeptogether_3_hero_face 6o1
        hero "[C_Nam][hero_to_wsis][C_Off]{w=[wt2]}, I'll be here for you, okay?"

        show wsis_sleeptogether_3_hero_face 6o0 with None
        # WSIS nods

        pause

    else:

        menu:

            "Grab butt":
                play SE1 renpy.random.choice(["Moan/A lvl3 (1).ogg", "Moan/A lvl3 (2).ogg", "Moan/A lvl3 (3).ogg", "Moan/A lvl3 (4).ogg", "Moan/A lvl3 (5).ogg", "Moan/A lvl3 (6).ogg", "Moan/A lvl3 (7).ogg", "Moan/A lvl3 (8).ogg", "Moan/X lvl3 (1).ogg", "Moan/X lvl3 (2).ogg"])

                $ add_stat("wsis", "inti", 1)
                $ add_stat("wsis", "lust", 1)
                $ add_stat("wsis", "love", -2)
                $ add_stat("hero", "cha_sex", 1)

                show wsis_sleeptogether_3_char 2
                show wsis_sleeptogether_3_wsis_face 1s0
                with dissolve

                pause

                play SE1 "Hit1.ogg"

                scene wsis_sleeptogether_3_bg
                show wsis_sleeptogether_3_char 4a
                show fx_light
                with hpunch

                scene wsis_sleeptogether_3_bg
                show wsis_sleeptogether_3_char 4
                show wsis_sleeptogether_3_wsis_face 4o0
                show fx_light
                with dissolve

                show wsis_sleeptogether_3_wsis_face 4o1

                wsis "What are you doing, pervert!?"
                
                scene wsis_sleeptogether_3_bg
                show wsis_sleeptogether_3_char 5
                show wsis_sleeptogether_3_wsis_face 5
                show wsis_sleeptogether_3_hero_face 5
                show fx_light
                with dissolve

            "Grab breasts":
                play SE1 renpy.random.choice(["Moan/A lvl3 (1).ogg", "Moan/A lvl3 (2).ogg", "Moan/A lvl3 (3).ogg", "Moan/A lvl3 (4).ogg", "Moan/A lvl3 (5).ogg", "Moan/A lvl3 (6).ogg", "Moan/A lvl3 (7).ogg", "Moan/A lvl3 (8).ogg", "Moan/X lvl3 (1).ogg", "Moan/X lvl3 (2).ogg"])

                $ add_stat("wsis", "inti", 1)
                $ add_stat("wsis", "lust", 1)
                $ add_stat("wsis", "love", -2)
                $ add_stat("hero", "cha_sex", 1)

                show wsis_sleeptogether_3_char 3
                show wsis_sleeptogether_3_wsis_face 1s0
                with dissolve

                pause

                play SE1 "Hit1.ogg"

                scene wsis_sleeptogether_3_bg
                show wsis_sleeptogether_3_char 4a
                show fx_light
                with hpunch

                scene wsis_sleeptogether_3_bg
                show wsis_sleeptogether_3_char 4
                show wsis_sleeptogether_3_wsis_face 4o0
                show fx_light
                with dissolve

                show wsis_sleeptogether_3_wsis_face 4o1

                wsis "What are you doing, pervert!?"

                scene wsis_sleeptogether_3_bg
                show wsis_sleeptogether_3_char 5
                show wsis_sleeptogether_3_wsis_face 5
                show wsis_sleeptogether_3_hero_face 5
                show fx_light
                with dissolve

            "Hug tight":

                $ add_stat("wsis", "inti", 1)
                $ add_stat("wsis", "love", 1)
                $ add_stat("hero", "cha_sex", 1)

                show wsis_sleeptogether_3_char 6
                show wsis_sleeptogether_3_hero_face 6o0
                show wsis_sleeptogether_3_wsis_face 6o0
                with Dissolve(2)
                pause

            "Fuck" if wsis_quest_11 >= 1:
                $ wsis_know.append("Watch_Horror_end")
                
                menu:
                    "WSIS - UI":
                        call test_x1_ui from _call_test_x1_ui_1

                    "WSIS - Animation":
                        call test_x1_ai from _call_test_x1_ai_1

    stop BGM fadeout 3

    scene bg_0 with Dissolve(3)

    return

# ---------------------------------------------------------------------------
label wsis_sleep_together_2:
# ---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_200

    if wsis_quest_5 < 1:
        $ wsis_quest_5 = 1

    play BGM "audio/W2C - GoodVibes.mp3"

    scene wsis_sleeptogether_4_bg
    show wsis_sleeptogether_4_char 1
    show fx_light
    with Dissolve(3)
    
    pause

    play SE2 "Moan - Soft.mp3"

    show wsis_sleeptogether_4_char 2
    with Dissolve(1)
    
    pause

    show wsis_sleeptogether_4_char 3
    with Dissolve(1)
    
    pause

    $ StartAct("wsis", ("sleeping", 0), True)

    return
