# ----------------------------------------------------------------------------------------------------
init python:

    def Cheat_Infinite(var="money", state=None):
        # "Infinite" money/perks pay out a big finite CHEAT_<VAR>, never math.inf: the date HUD bar draws money over date_money, and inf/inf is NaN, which crashes the renderer.
        # Turning it on banks the current value; turning it off hands that value straight back, so the cheat leaves nothing behind. gamecheck tops the var back up while it is on.
        flag = "cheat_" + var
        new_state = (not getattr(store, flag)) if state is None else bool(state)
        if new_state == getattr(store, flag):
            return
        if new_state:
            setattr(store, flag + "_bak", getattr(store, var))
            setattr(store, var, getattr(store, "CHEAT_" + var.upper()))
        else:
            setattr(store, var, getattr(store, flag + "_bak"))
        setattr(store, flag, new_state)

    # The cheat bar for HERO's attributes. A sub-stat bar writes the sub-stat and re-averages its parent; a main bar shifts its three sub-stats by the same delta (clamped 0-100) and re-averages, so stat_cha/int/phy stay the computed averages add_stat() maintains and are never written directly.
    class HeroStatValue(BarValue, FieldEquality):
        equality_fields = ("stat",)

        def __init__(self, stat):
            self.stat = stat

        def get_adjustment(self):
            return ui.adjustment(range=100, value=stat_value("hero", self.stat), changed=self.changed)

        def changed(self, value):
            main = self.stat.split("_")[0]
            subs = [sub for tree_main, _name, _icon, tree_subs in HERO_STAT_TREE if tree_main == main for sub, _sub_name in tree_subs]
            if self.stat == main:
                delta = value - stat_value("hero", main)
                for sub in subs:
                    setattr(store, "stat_" + sub, round(max(0, min(100, stat_value("hero", sub) + delta)), 2))
            else:
                setattr(store, "stat_" + self.stat, round(max(0, min(100, value)), 2))
            setattr(store, "stat_" + main, round(sum(stat_value("hero", sub) for sub in subs) / 3.0, 2))
            check_stat()
            renpy.restart_interaction()

# HERO's attribute tree for the character panel: (main stat, label, icon, its three sub-stats), in the order the bars are drawn.
define HERO_STAT_TREE = [
    ("int", "Intelligence", "ICON_StatInt", [("int_per", "Perception"), ("int_mem", "Knowledge"), ("int_log", "Logic")]),
    ("cha", "Charisma", "ICON_StatCha", [("cha_sex", "Sensuality"), ("cha_per", "Performance"), ("cha_soc", "Social")]),
    ("phy", "Physics", "ICON_StatPhy", [("phy_str", "Strength"), ("phy_agi", "Agility"), ("phy_res", "Endurance")]),
    ]

# ----------------------------------------------------------------------------------------------------
label inputcheat:
    $ preferences.codetype = renpy.input(renpy.translate_string("Input a code. Don't know how to use codes? then type [C_Dat]guide[C_Off]"), length=12)

    # KCC Code Generator
    python:
        # Define the kcc_cha string
        kcc_cha = 'abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ0123456789'

        # Get the current year, month, and day
        kcc_yea = datetime.datetime.now().year
        kcc_mon = datetime.datetime.now().month
        kcc_day = datetime.datetime.now().day

        # Calculate the positions based on the formula
        pos1 = (kcc_yea * kcc_mon * kcc_day) % len(kcc_cha)
        pos2 = (kcc_yea + kcc_mon * kcc_day) % len(kcc_cha)
        pos3 = (kcc_yea * kcc_mon + kcc_day) % len(kcc_cha)
        pos4 = (kcc_yea + kcc_mon + kcc_day) % len(kcc_cha)
        pos5 = (kcc_mon * kcc_day) % len(kcc_cha)

        # Generate kcc_code based on the calculated positions
        kcc_code = (
            kcc_cha[pos1] +
            kcc_cha[pos2] +
            kcc_cha[pos3] +
            kcc_cha[pos4] +
            kcc_cha[pos5]
        )

    if preferences.codetype == "guide" or preferences.codetype == "Guide" or preferences.codetype == "GUIDE":
        jump UI_Menu_Guide_Code

    if preferences.codetype == "bug" or preferences.codetype == "Bug" or preferences.codetype == "BUG":
        $ raise Exception("test")

    if preferences.codetype == preferences.codecheat:
        if preferences.cheatmode == False:
            play SE1 "BeepRight.ogg"
            $ preferences.cheatmode = True
            $ preferences.codecheatuse = preferences.codecheat
            $ msg.msg(renpy.translate_string("Cheat Enabled"))
        else:
            play SE1 "BeepWrong.ogg"
            $ msg.msg(renpy.translate_string("This code is already activated"))

    elif preferences.codetype == "gettheme":
        menu:
            "Common":
                $ preferences.gametimeevent = None
            "Halloween":
                $ preferences.gametimeevent = "Halloween"
            "Christmas":
                $ preferences.gametimeevent = "XMAS"

    elif preferences.codetype == kcc_code:
        if not "KCC1" in cellbg:
            play SE1 "BeepRight.ogg"
            $ cellbg.insert(1, "KCC6")
            $ cellbg.insert(1, "KCC5")
            $ cellbg.insert(1, "KCC4")
            $ cellbg.insert(1, "KCC3")
            $ cellbg.insert(1, "KCC2")
            $ cellbg.insert(1, "KCC1")
            $ msg.msg(renpy.translate_string("New photos added to phone Gallery"))
        else:
            play SE1 "BeepWrong.ogg"
            $ msg.msg(renpy.translate_string("This code is already activated"))

    elif preferences.codetype == "changeimg":
        if ("KCC1" in cellbg or "KCC1AI" in cellbg):
            play SE1 "BeepRight.ogg"
            if "KCC1" in cellbg:
                $ cellbg[cellbg.index("KCC1")] = "KCC1AI"
                $ cellbg[cellbg.index("KCC2")] = "KCC2AI"
                $ cellbg[cellbg.index("KCC3")] = "KCC3AI"
                $ cellbg[cellbg.index("KCC4")] = "KCC4AI"
                $ cellbg[cellbg.index("KCC5")] = "KCC5AI"
                $ cellbg[cellbg.index("KCC6")] = "KCC6AI"
                $ msg.msg(renpy.translate_string("Arts changed to AI generated images"))
            elif "KCC1AI" in cellbg:
                $ cellbg[cellbg.index("KCC1AI")] = "KCC1"
                $ cellbg[cellbg.index("KCC2AI")] = "KCC2"
                $ cellbg[cellbg.index("KCC3AI")] = "KCC3"
                $ cellbg[cellbg.index("KCC4AI")] = "KCC4"
                $ cellbg[cellbg.index("KCC5AI")] = "KCC5"
                $ cellbg[cellbg.index("KCC6AI")] = "KCC6"
                $ msg.msg(renpy.translate_string("AI generated images changed to arts"))
        else:
            play SE1 "BeepWrong.ogg"
            $ msg.msg(renpy.translate_string("You need to activate the KCC code first"))
    else:
        play SE1 "BeepWrong.ogg"
        $ msg.msg(renpy.translate_string("No code was found"))
        $ preferences.codetype = ""

    jump UI_Menu_Options

# ----------------------------------------------------------------------------------------------------
# GUIDE
# ----------------------------------------------------------------------------------------------------
image guide_minigamereaction_w = Movie(play="images/UI/Guide/HRIV_Fight_WIN.webm", loop=True)
image guide_minigamereaction_l = Movie(play="images/UI/Guide/HRIV_Fight_LOSE.webm", loop=True)
image guide_minigamehreceive_w = Movie(play="images/UI/Guide/WCOU_Office_WIN.webm", loop=True)
image guide_minigamehreceive_l = Movie(play="images/UI/Guide/WCOU_Office_LOSE.webm", loop=True)
image guide_minigametugofwar = Movie(play="images/UI/Guide/Minigame_TugOfWar.webm", loop=True)
image guide_minigameact_1 = Movie(play="images/UI/Guide/X_WSUK 1.webm", loop=True)
image guide_minigameact_2 = Movie(play="images/UI/Guide/X_WSUK 2.webm", loop=True)
image guide_minigameact_3 = Movie(play="images/UI/Guide/X_WSUK 3.webm", loop=True)
image guide_minigameact_4 = Movie(play="images/UI/Guide/X_WSUK 4.webm", loop=True)
image guide_minigamestretching_p = Movie(play="images/UI/Guide/WMOM_Yoga_PLAY.webm", loop=True)
image guide_minigamestretching_l = Movie(play="images/UI/Guide/WMOM_Yoga_LOSE.webm", loop=True)
image guide_kcc2w2c = Movie(play="images/UI/Guide/KCC2W2C.webm", loop=True)
image guide_extra = Movie(play="images/UI/Guide/Extra.webm", loop=True)
image guide_cheat = Movie(play="images/UI/Guide/Cheat.webm", loop=True)
# ----------------------------------------------------------------------------------------------------

label UI_Menu_Guide_Code:
    call gamecheck from _call_gamecheck_20
    call hide_ui from _call_hide_ui_140
    $ a_menu_2 = "Code"
    # Called like the Guide button's path, so the quick menu's X (a Jump to show_ui) takes it down too; a shown screen stayed up under the UI.
    call screen UI_Menu_Guide
    jump show_ui

label UI_Menu_Guide:
    call gamecheck from _call_gamecheck_21
    call hide_ui from _call_hide_ui_141
    $ a_menu_2 = "About"
    call screen UI_Menu_Guide
    jump show_ui

screen UI_Menu_Guide():
    hbox:
        #xpos 100
        vbox:
            frame:
                xsize 420
                ysize 980
                xpadding 50
                ypadding 50

                vbox:
                    spacing 25
                    label renpy.translate_string("Guide")

                    side ("c l"):
                        area (-10,0,1380,830)
                        viewport id "ScrollGuide_L":
                            xoffset 25
                            draggable True mousewheel True
                            vbox:
                                text renpy.translate_string("Info")
                                textbutton _("{image=starchan} About") action SetVariable("a_menu_2", "About")
                                textbutton _("{image=starchan} Code") action SetVariable("a_menu_2", "Code")

                                text renpy.translate_string("{p}Work In Progress")
                                textbutton renpy.translate_string("⚠ Interface") action None
                                textbutton renpy.translate_string("⚠ Content") action None
                                textbutton renpy.translate_string("⚠ Minigames") action None

                                if 0 > 1:
                                    textbutton _("{image=starchan} User Interface") action SetVariable("a_menu_2", "UI")
                                    textbutton _("{image=starchan} Content") action SetVariable("a_menu_2", "Content")

                                    text renpy.translate_string("{p}Mechanics")
                                    textbutton _("{image=starchan} Attributes") action SetVariable("a_menu_2", "Attributes")
                                    textbutton _("{image=starchan} Talents") action SetVariable("a_menu_2", "Talents")
                                    textbutton _("{image=starchan} Personality") action SetVariable("a_menu_2", "Personality")
                                    textbutton _("{image=starchan} Stats") action SetVariable("a_menu_2", "Stats")

                                    text renpy.translate_string("{p}Minigames")
                                    textbutton _("{image=starchan} (Re)Action") action SetVariable("a_menu_2", "Minigame_Reaction")
                                    textbutton _("{image=starchan} Stretching") action SetVariable("a_menu_2", "Minigame_Stretching")
                                    if wnei_quest_2 >= 1:
                                        textbutton _("{image=starchan} Tug Of War") action SetVariable("a_menu_2", "Minigame_TugOfWar")
                                    if hero_quest_2 >= 4:
                                        textbutton _("{image=starchan} H Scene (Receive)") action SetVariable("a_menu_2", "Minigame_HReceive")
                                    if hero_xnum > 0:
                                        textbutton _("{image=starchan} H Scene (Act)") action SetVariable("a_menu_2", "Minigame_HAct")
                        vbar value YScrollValue("ScrollGuide_L")
            frame:
                xsize 420
                ysize 100
                textbutton _("Close") action Return() xalign 0.5 yalign 0.5

        frame:
            xsize 1400
            ysize 1080
            xpadding 50
            ypadding 50
            vbox:
                spacing 25
                if a_menu_2 == "About":
                    label renpy.translate_string("About")
                elif a_menu_2 == "UI":
                    label renpy.translate_string("User Interface")
                elif a_menu_2 == "Code":
                    label renpy.translate_string("Code")
                elif a_menu_2 == "Attributes":
                    label renpy.translate_string("Attributes")
                elif a_menu_2 == "Talents":
                    label renpy.translate_string("Talents")
                elif a_menu_2 == "Personality":
                    label renpy.translate_string("Personality")
                elif a_menu_2 == "Stats":
                    label renpy.translate_string("Stats")
                elif a_menu_2 == "Minigame_Reaction":
                    label renpy.translate_string("(Re)Action")
                elif a_menu_2 == "Minigame_Stretching":
                    label renpy.translate_string("Stretching [C_Mnd](PROTOTYPE)[C_Off]")
                elif a_menu_2 == "Minigame_HReceive":
                    label renpy.translate_string("H Scene (Receive)")
                elif a_menu_2 == "Minigame_HAct":
                    label renpy.translate_string("H Scene (Act)")
                elif a_menu_2 == "Minigame_TugOfWar":
                    label renpy.translate_string("Tug Of War")
                else:
                    label renpy.translate_string("Content")

                side ("c l"):
                    area (-10,0,1300,940)
                    viewport id "ScrollGuide_R":
                        xoffset 25
                        draggable True mousewheel True
                        vbox:
                            spacing 20
                            justify True
                            if a_menu_2 == "About":
                                text renpy.translate_string("WelCUM To The City is intended to not be just one more visual novel game with linear story where you just keep clicking and doing repetitive things again and again, but also have some RPG and sandbox features, where you can upgrade your character skills and your decisions affect the world around you.")
                                image "images/UI/Guide/About.webp"
                                text renpy.translate_string("Some mechanics often used in visual novels, such as {b}Wrong Choices{/b} or {b}Scene Gallery{/b} will probably not be implemented in the game. Instead, it will be more like a life simulator, where everything is intended to be part of your progress.")

                            elif a_menu_2 == "Content":
                                text renpy.translate_string("This game is in a very early development stage. Which means that it's far from complete and does not have all the content that is intended to have. Therefore, consider checking the content list to know what is available at the moment.")
                                image "images/UI/Guide/ContentList.webp"

                            elif a_menu_2 == "Code":
                                text renpy.translate_string("WelCUM To The City has some bonus features unlockable from codes. To use that, just get the codes and input it on Player Menu following the examples below.")
                                text renpy.translate_string("{p}")
                                label renpy.translate_string("Free Gallery Images Code")
                                text renpy.translate_string("Open Kawaii Character Creator and find the special code on the bottom of the game, then, just type or paste it in the input section to unlock special gallery photos.")
                                image "guide_kcc2w2c"
                                textbutton renpy.translate_string("{b}Open:{/b} Kawaii Character Creator") action OpenURL("https://quiquersson.itch.io/kcc")
                                text renpy.translate_string("{p}")
                                label renpy.translate_string("Cheat Code")
                                text renpy.translate_string("Cheat codes are available on the montly update posts for {b}big tiers{/b} on [C_Dat]SubscribeStar[C_Off] and [C_Dat]Patreon[C_Off].")
                                image "images/UI/Guide/SuportTier.webp" xalign 0.5
                                textbutton renpy.translate_string("{b}Open:{/b} SubscribeStar") action OpenURL("https://subscribestar.adult/quiquersson")
                                textbutton renpy.translate_string("{b}Open:{/b} Patreon") action OpenURL("https://www.patreon.com/quiquersson")
                                text renpy.translate_string("{p}Once you get the code, just need input it in the {image=icon_code} {b}Code Session{/b} to enable it like the example below.")
                                image "guide_cheat" xalign 0.5

                            elif a_menu_2 == "UI":
                                text renpy.translate_string("When you aren't in any scene, you may be free to choose what to do from the interface buttons.")
                                image "images/UI/Guide/UI.webp"
                                text renpy.translate_string("If any message appears indicating that the particular activity is not available when you click in a button, you are probably in the middle of an important event, and you need to finish it first.")
                                text renpy.translate_string("[C_But]{b}Data & Time:{/b}[C_Off] Information about what day and time you are. Click on the icon to pass to the next hour.")
                                text renpy.translate_string("[C_But]{b}Character Data:{/b}[C_Off] The amount of energy; attribute points; and money you current have. You have energy to perform 4 workouts every day; and up to 2 workouts of some specific attribute, which may be: Intelligence; Physical; and Charisma. Your energy recovers completely when you sleep. [C_Mnd](PROTOTYPE: It may work different in future versions)[C_Off]")
                                text renpy.translate_string("[C_But]{b}Available Characters:{/b}[C_Off] Characters available to interact in the current map.")
                                text renpy.translate_string("[C_But]{b}Available Activities:{/b}[C_Off] Activities available to interact in the current map.")
                                text renpy.translate_string("[C_But]{b}Map Navigation:{/b}[C_Off] Navigate between maps.")
                                text renpy.translate_string("[C_But]{b}Main Menu:{/b}[C_Off] Customize settings and check general game info.")
                                text renpy.translate_string("[C_But]{b}Character Menu:{/b}[C_Off] Check information about characters and their available contents.")
                                text renpy.translate_string("[C_But]{b}Item Menu:{/b}[C_Off] Check and use items [C_Mnd](PROTOTYPE: It's just visual for now)[C_Off].")
                                text renpy.translate_string("[C_But]{b}Player Menu:{/b}[C_Off] Check and customize more personal data from your game.")
                                text renpy.translate_string("[C_But]{b}Guide Menu:{/b}[C_Off] Check information about the game. {bt}You are here{/bt}.")

                            elif a_menu_2 == "Attributes":
                                vbox:
                                    xminimum 1280
                                    xalign 0.5
                                    spacing 10
                                    hbox:
                                        xalign 0.5
                                        spacing 25
                                        image "images/UI/ICON_StatCha.webp"
                                        text renpy.translate_string("CHA") size 60
                                        image "images/UI/ICON_StatCha.webp"
                                    hbox:
                                        xalign 0.5
                                        text renpy.translate_string("Charisma") size 40
                                    text ""
                                    text renpy.translate_string("* Unlocks certain dialogues with characters")
                                    text renpy.translate_string("* Increases intimacy point gain for most characters")
                                    text renpy.translate_string("* Increases love point gain for most characters")
                                    text renpy.translate_string("* Increases lust point gain for most characters")
                                    text renpy.translate_string("{p}")
                                vbox:
                                    xminimum 1280
                                    xalign 0.5
                                    spacing 10
                                    hbox:
                                        xalign 0.5
                                        spacing 25
                                        image "images/UI/ICON_StatInt.webp"
                                        text renpy.translate_string("INT") size 60
                                        image "images/UI/ICON_StatInt.webp"
                                    hbox:
                                        xalign 0.5
                                        text renpy.translate_string("Intelligence")
                                    text ""
                                    text renpy.translate_string("* Unlocks certain dialogues with some intelligent characters")
                                    text renpy.translate_string("* Increases performance in mental minigames")
                                    text renpy.translate_string("* Increases intimacy point gain for some intelligent characters")
                                    text renpy.translate_string("* Increases love point gain for some intelligent characters")
                                    text renpy.translate_string("{p}")
                                vbox:
                                    xminimum 1280
                                    xalign 0.5
                                    spacing 10
                                    hbox:
                                        xalign 0.5
                                        spacing 25
                                        image "images/UI/ICON_StatPhy.webp"
                                        text renpy.translate_string("PHY") size 60
                                        image "images/UI/ICON_StatPhy.webp"
                                    hbox:
                                        xalign 0.5
                                        text renpy.translate_string("Physics")
                                    text ""
                                    text renpy.translate_string("* Increases performance in minigame {b}(Re)Action{/b}")
                                    text renpy.translate_string("* Increases performance in minigame {b}Stretching{/b}")
                                    text renpy.translate_string("* Increases performance in minigame {b}H Scene (Receive){/b}")
                                    text renpy.translate_string("{p}")

                            elif a_menu_2 == "Talents":
                                vbox:
                                    spacing 50

                                    text renpy.translate_string("Level up and gain perk points to spend on talents. You can level up during day changes by gaining experience points from increasing your attributes or girls' love, lust, and intimacy, or by making girls cum. [C_Mnd](Some perks are currently unavailable so you cannot spend it in not implemented content)[C_Off].")

                                    label renpy.translate_string("Basic Talents")

                                    vbox:
                                        xsize 1200
                                        xoffset 25

                                        label renpy.translate_string("[C_But]Strength[C_Off]")
                                        text renpy.translate_string("Improves your performance when carrying girls and heavier items; increases your damage in fights [C_Mnd](when available)[C_Off]. [C_Dat]You can carry ") + str(round((20 + ((3 + (perk_phy_str * 2)) * (3 + (perk_phy_str * 2)))) * (1 + (stat_phy * 0.01)), 2)) + "kg[C_Off]."
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Agility[C_Off] [C_Mnd](Unavailable)[C_Off]")
                                        text renpy.translate_string("Improves your speed performance. Spend less time when use fast travel. Time passes slower in agility minigames.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Endurance[C_Off] [C_Mnd](Unavailable)[C_Off]")
                                        text renpy.translate_string("Increases your stamina and ability to perform physical activities for longer periods, and increase your resistance in fights.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Perception[C_Off]")
                                        text renpy.translate_string("Enhances your ability to notice hidden scenes and see through characters' words and actions. Reduce chances of you to be caught by surprise in some scenes [C_Mnd](when available)[C_Off]. [C_Dat]You have a ") + str(round(((perk_int_per/3)*100), 2)) + "% chance of noticing hidden things[C_Off]."
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Knowledge[C_Off]")
                                        text renpy.translate_string("Allows you to have knowledge of general things around you, enhances your ability to remember information and details, and slightly improves your performance in some skills.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Logic[C_Off] [C_Mnd](Unavailable)[C_Off]")
                                        text renpy.translate_string("Improves your logical reasoning skills, making it easier to solve complex problems and puzzles, and make better decisions. Time passes slower in thinking minigames.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Sensuality[C_Off]")
                                        text renpy.translate_string("Increases your attractiveness and the amount of lust generated in the characters.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Performance[C_Off]")
                                        text renpy.translate_string("Improves your performance in using skills and increases the amount of money received when working.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Social[C_Off] [C_Mnd](Unavailable)[C_Off]")
                                        text renpy.translate_string("Increases your performance in character interactions.")
                                        text renpy.translate_string("{p}")

                                    label renpy.translate_string("Advanced Talents")

                                    vbox:
                                        xsize 1200
                                        xoffset 25

                                        label renpy.translate_string("[C_But]Sensuality[C_Off]")
                                        text renpy.translate_string("Improve your performance in H scenes. Characters get even hornier by erotic physical contacts with you, and also get horny by common physical contacts with you.")
                                        text renpy.translate_string("{p}")
                                        
                                        label renpy.translate_string("[C_But]Ninjutsu[C_Off] [C_Mnd](Unavailable)[C_Off]")
                                        text renpy.translate_string("Increases the chances that you won't be noticed when you're in hiding. Reduces the chance of you being caught off guard in some scenes. Time passes slowly in agility minigames.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Psychology[C_Off] [C_Mnd](Unavailable)[C_Off]")
                                        text renpy.translate_string("Improves your performance in character interactions, and allows you to see through their words and actions. Unlocks additional information about characters.")
                                        text renpy.translate_string("{p}")

                                    label renpy.translate_string("Skills")

                                    vbox:
                                        xsize 1200
                                        xoffset 25

                                        label renpy.translate_string("[C_But]Dance[C_Off]")
                                        text renpy.translate_string("Allows you to dance in a rhythm minigame.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Guitar[C_Off] [C_Mnd](Unavailable)[C_Off]")
                                        text renpy.translate_string("Allows you to play guitar in a rhythm minigame.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Swimming[C_Off]")
                                        text renpy.translate_string("Allows you to swim in scenes and minigames [C_Mnd](when available)[C_Off].")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Massage[C_Off] [C_Mnd](Unavailable)[C_Off]")
                                        text renpy.translate_string("Allows you to massage characters.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Cooking[C_Off] [C_Mnd](Unavailable)[C_Off]")
                                        text renpy.translate_string("Allows you to cook or create consumable itens.")
                                        text renpy.translate_string("{p}")

                                        label renpy.translate_string("[C_But]Tutoring[C_Off]")
                                        text renpy.translate_string("Allows you to teach a skill you know.")
                                        text renpy.translate_string("{p}")

                            elif a_menu_2 == "Personality":
                                label renpy.translate_string("[C_But]Your main personality is:[C_Off] [C_Per]{b}[personality[0]]{/b}[C_Off]")
                                text renpy.translate_string("{p}{b}Common{/b}")
                                text renpy.translate_string("[C_Mnd](balanced rate)[C_Off]")
                                text renpy.translate_string("Neither there nor here... the middle path is ideal")
                                text renpy.translate_string("{p}{b}Hentai{/b}")
                                text renpy.translate_string("[C_Mnd]([C_Pos]increases lust rate[C_Off], but [C_Neg]decreases love rate[C_Off])[C_Off]")
                                text renpy.translate_string("You perfected in made decisions in your life thinking with your bottom head, now you can easily influence people to get horny. however, you also get easily horny, and now people don't believe that much in your kind actions since they tend to think you're doing that just to take advantage later.")
                                text renpy.translate_string("{p}{b}Kind{/b}")
                                text renpy.translate_string("[C_Mnd]([C_Pos]increases love rate[C_Off], but [C_Neg]decreases lust rate[C_Off])[C_Off]")
                                text renpy.translate_string("You have shown yourself to be a very good-hearted person, and that delights everyone. People often trust you so much that they tend to believe that you don't do anything wrong on purpose. It also implies that your actions look so cute that it's harder for you to make people horny.")
                                text renpy.translate_string("{p}{b}Reserved{/b}")
                                text renpy.translate_string("[C_Mnd]([C_Pos]increases skill and money rate[C_Off], but [C_Neg]decreases affection rate[C_Off])[C_Off]")
                                text renpy.translate_string("You've become accustomed to acting with a certain level of formality, without being swayed by emotions, and this has shown people that you know how to separate things very well and that they shouldn't cross the line with you. Now everyone tends to respect you a lot and avoid disappointing you as much as possible. Your performance in studies and work tends to be above average.")
                                text renpy.translate_string("{p}{b}Intimate{/b}")
                                text renpy.translate_string("[C_Mnd]([C_Pos]increases affection rate[C_Off], but [C_Neg]decreases skill and money rate[C_Off])[C_Off]")
                                text renpy.translate_string("You've shown yourself to be a very welcoming person and people tend to be extremely comfortable around you, and open up more when talking, talking more easily about subjects they wouldn't talk about with just anyone. However, because you are quite emotional, you tend to have difficulty with logical reasoning and imposing yourself on others.")

                            elif a_menu_2 == "Stats":
                                text renpy.translate_string("Each character reacts to you differently depending on their personality and yours. At the moment, {b}love{/b} and {b}lust{/b} do not yet have their full functionality within the game, so the most important status is {b}intimacy{/b}, as it unlocks more content. {b}Love{/b} and {b}lust{/b} only serve to increase characters {b}intimacy{/b} rate.")

                                text renpy.translate_string("{p}[C_But]{b}Intimacy:{/b}[C_Off] Determines how intimate this character considers you to be. Unlocks new scenes with characters. This stat increase very slowly, but don't decrease.")

                                text renpy.translate_string("{p}[C_But]{b}Love:{/b}[C_Off] Determines how much the character likes you, which can vary between -100% (hate) and 100% (love). This stat increases slowly and only decreases on special occasions. [C_Mnd]({b}PLANS:{/b} It should increase the chance that characters will seek you out on their own, start conversations with you, give you gifts, and be more likely to approve of your actions.)[C_Off]")

                                text renpy.translate_string("{p}[C_But]{b}Lust:{/b}[C_Off] Determines how aroused the character is. Increases quickly but is very unstable, resetting when characters cum [C_Mnd](Occurs when lust reaches approximately 80% to 100%)[C_Off], or decreasing significantly [C_Mnd](about 12,5% to 30%)[C_Off] between one day and the next. [C_Mnd]({b}PLANS:{/b} Some girls masturbate when they are really horny and it should be possible to see some of these scenes if you are in the right place.)[C_Off]")

                                text renpy.translate_string("{p}[C_But]{b}Pain:{/b}[C_Off] Determines how sore the character is feeling. Some characters must have better resistance than others depending on their physical size, height, and flexibility. Decreasing significantly [C_Mnd](about 6,25% to 25%)[C_Off] between one day and the next. [C_Mnd](Only available for {image=icon_wmom} until now. {b}PLANS:{/b} medicines and massages may reduce pain; characters with more sexual experience; wider anus or vagina; or greater flexibility, should withstand deeper penetration during H scenes, while the opposite, you would need to act more cautiously if you don't want to hurt them.)[C_Off]")

                                text renpy.translate_string("{p}[C_But]{b}Flexibility:{/b}[C_Off] Determines how flexible the character's leg joints are, decreasing very slowly [C_Mnd](1%)[C_Off] between one day and the next. [C_Mnd](Only available for {image=icon_wmom} in the {b}Stretching{/b} minigame until now.)[C_Off]")

                                text renpy.translate_string("{p}[C_But]{b}Extra Points:{/b}[C_Off]")
                                image "guide_extra"
                                text renpy.translate_string("Influences the characters' {b}intimacy{/b}, {b}love{/b}, and {b}lust{/b} point count. These extra points can generally be acquired in moments when a certain character is not present, but is mentioned in a positive or negative way. Positive extras increase the gain and decrease the loss of {b}intimacy{/b}, {b}love{/b}, and {b}lust{/b}, while positive extras have the opposite effect. The amount of extra points acquired tends to be very small, on the other hand, there is no limit to how many you can have, but their absolute value reduces by 0.2% every day [C_Mnd](Example: 1% would take 5 days to reset if no new extra points are adquired, while -10% would take 50 days)[C_Off].")

                            elif a_menu_2 == "Minigame_Reaction":
                                text renpy.translate_string("Click correctly on the arrows that appear on the screen as quickly as possible so that your action or reaction to a certain event performs better.")
                                image "guide_minigamereaction_w"
                                text renpy.translate_string("Clicking the wrong arrow or not clicking within the right time will make you miss the current turn and move on to the next one.")
                                image "guide_minigamereaction_l"
                                text renpy.translate_string("Increase your {image=images/UI/ICON_StatPhy.webp} to see time pass more slowly and have the opportunity to act or react better")

                            elif a_menu_2 == "Minigame_Stretching":
                                text renpy.translate_string("[C_Neg]{b}WARNING:{/b} This system is just a prototype and the current {b}flexibility{/b} stat must be reset in future updates so you can enjoy a better experience (Know more on the bottom info).[C_Off]{p}")
                                text renpy.translate_string("Click and hold the screen to stretch the girl leg, and release it to release the stretching. Control your holding and releasing time to increase her flexibility by 100% before the time ends, without leaving the pain bar reach 100%.")
                                image "guide_minigamestretching_p"
                                text renpy.translate_string("The more you open her legs, the faster you tend to increase her flexibility, but also, the more you tend to hurt her if she doesn't have the necessary flexibility to withstand the pain. Therefore, for the best performance, control how much you stretch her legs according to her current flexibility, being careful not to strain her legs more than she can handle.")
                                image "guide_minigamestretching_l"
                                text renpy.translate_string("Increase your {image=images/UI/ICON_StatPhy.webp} to ease your strength control and don't force girls legs too much.")
                                text renpy.translate_string("{p}[C_Mnd]({b}PLANS:{/b} {image=icon_wmom}'s flexibility should unlock new yoga scenes and increase way more slowly so that you can enjoy a better progression of your relationship with her; The arrow button may be changed to something else.)[C_Off]")

                            elif a_menu_2 == "Minigame_HReceive":
                                text renpy.translate_string("Your mind is very full of lewd thoughts. To get rid of them, click as soon as possible in the {b}Thinking Balloons{/b} to control your urges. The faster you burst the balloons, the less your lust will increase and you can resist H scenes for longer.")
                                image "guide_minigamehreceive_w"
                                text renpy.translate_string("Or just let it go if you prefer.")
                                image "guide_minigamehreceive_l"
                                text renpy.translate_string("More experienced girls tend to resist more at H-Scenes. Increase your {image=images/UI/ICON_StatPhy.webp} to ease your lust control at H-Scenes and make girls cum more times.")

                            elif a_menu_2 == "Minigame_TugOfWar":
                                text renpy.translate_string("In this contest of strength, click on the screen as many times as you can to force the bar to your side. The greater your [C_Dat]strength[C_Off] talent, the more points you apply with each click.")
                                image "guide_minigametugofwar"

                            elif a_menu_2 == "Minigame_HAct":
                                text renpy.translate_string("Sex content is completely player-controllable, with performance dependent on skills and attributes such as [C_Dat]Sensuality[C_Off].{p}Click the penetration button to enable control.")
                                image "guide_minigameact_1"
                                text renpy.translate_string("Move the cursor/finger in the red area below to control penis movement after is control is enabled. The speed at which you move this is very important to define the characters' reactions of pleasure, pain, and breath.{p}The upper part of the control area can cause pain to the girl if you make too many sudden movements, and if the pain indicator reaches its maximum, the scene ends.{p}Note the speed at which the girl feels the most pleasure and use this to your advantage.")
                                image "guide_minigameact_2"
                                text renpy.translate_string("The closer a character's lust meter gets to maximum, the more likely they are to cum. If you cum, the scene ends. The higher the [C_Dat]Sensuality[C_Off] skill level, the less likely you are to automatically cum, and the higher is girl's pleasure.{p}For the highest possible score, make the girl cum at least 3 times, and cum at the same time as her.{p}To cum at the same time as the girl, you need to click the ejaculation button when the girl has at least 90% lust, or has more lust than you.")
                                image "guide_minigameact_3"
                                text renpy.translate_string("Want to just watch the scene while leaving your right hand free? No problem! Just use the automatic mode and hide the interface. The automatic mode is enabled after the first sexual intercourse. This mode calculates the average speed of your movements from your last sexual intercourse and tries to simulate your speed.")
                                image "guide_minigameact_4"
                                text renpy.translate_string("This content is still in the process of being improved and the energy indicator is not very useful. A mechanic for a better penis control, different positions; reactions; and scenarios should be implemented in the future.")

                            else:
                                text renpy.translate_string("[C_Mnd]Oops... Missing info.[C_Off]")
                    vbar value YScrollValue("ScrollGuide_R")

# ----------------------------------------------------------------------------------------------------
# PHONE
# ----------------------------------------------------------------------------------------------------
# --------------------------------------------------
# CITY Name
# --------------------------------------------------
label rename_rnamecity:
    if fnameselect:
        $ rnamecity = renpy.input(renpy.translate_string("What's your city Name?{p}{color=#FFAF32}(Leave it blank to generate a random name)[C_Off]"), length=12)
        if rnamecity == "":
            call rnamegen from _call_rnamegen
            $ rnamecity = a_check_0
    else:
        call rnamegen from _call_rnamegen_1
        $ rnamecity = a_check_0
        pause(0.5)
    $ persistent.rnamecity = rnamecity
    jump UI_Menu_Options_Settings

# ----------------------------------------------------------------------------------------------------
label UI_Menu_Options:
    call gamecheck from _call_gamecheck_22
    $ a_menu_1 = 0
    $ a_menu_2 = 0
    $ a_menu_3 = 0
    call hide_ui from _call_hide_ui_154
    call screen UI_Menu_Options
    jump show_ui

label UI_Menu_Options_Gallery:
    call gamecheck from _call_gamecheck_23
    $ a_menu_1 = 0
    $ a_menu_2 = 0
    $ a_menu_3 = 0
    call hide_ui from _call_hide_ui_155
    call screen UI_Menu_Options_Gallery

label UI_Menu_Options_Gallery_IMG:
    # Save the clicked photo index before gamecheck resets it
    $ _temp_photo_index = a_menu_3
    call gamecheck from _call_gamecheck_24
    # Restore the clicked photo index
    $ a_menu_3 = _temp_photo_index
    $ a_menu_1 = 0
    $ a_menu_2 = 0
    $ photo_view = 0    # every photo opens whole; the view button cycles from there
    call hide_ui from _call_hide_ui_156
    call screen UI_Menu_Options_Gallery_IMG

label Set_Wallpaper:
    call hide_ui from _call_hide_ui_157
    $ cellwx = 50
    $ cellwy = 50
    $ cellwz = 0
    call screen Set_Wallpaper
    $ cellbg[0] = cellbg[a_menu_3]
    $ a_menu_1 = 0
    $ a_menu_2 = 0
    $ a_menu_3 = 0
    $ msg.msg(renpy.translate_string("Wallpaper Updated"))
    jump UI_Menu_Options

screen Set_Wallpaper():
    hbox:
        #xpos 100        
        frame:
            background None
            xpadding 0
            ypadding 0
            xsize 620
            ysize 1080
            add AlphaMask(
                Fixed(
                    Transform(Cell_Img(cellbg[a_menu_3]),
                        zoom = Cell_WZoom(cellbg[a_menu_3], cellwz),
                        xalign = (cellwx/100),
                        yalign = (cellwy/100)),
                        xysize=(620, 1080)  # Size of the masked area
                ),
                "images/UI/CellphoneBG/Menu_Mask_2.webp"
            )
            add "images/UI/CellphoneBG/Menu_FG.webp"
            vbox:
                xalign 0.5
                yalign 0.125
                spacing 25
                vbox:
                    xalign 0.5
                    text renpy.translate_string("Day [gametimeday], [gametimeclock]") size 60
                vbox:
                    xalign 0.5
                    text renpy.translate_string("[fnamehero] [lnamehero]") size 30
        vbox:
            xsize 1200
            yalign 0.5
            xalign 0.5
            spacing 50
            label renpy.translate_string("Adjust View") xalign 0.5
            bar value VariableValue("cellwx", 100) xmaximum 1000 xalign 0.5
            bar value VariableValue("cellwy", 100) xmaximum 1000 xalign 0.5
            bar value VariableValue("cellwz", 100) xmaximum 1000 xalign 0.5
            textbutton renpy.translate_string("Confirm") action Return() xalign 0.5

label UI_Menu_Options_Music:
    call gamecheck from _call_gamecheck_25
    $ a_menu_1 = 0
    $ a_menu_2 = 0
    $ a_menu_3 = 0
    call hide_ui from _call_hide_ui_158
    call screen UI_Menu_Options_Music(music_room)
    #call screen music_room(music_room)
    jump show_ui

label UI_Menu_Options_Contacts:
    call gamecheck from _call_gamecheck_26
    $ a_menu_1 = "none"
    $ a_menu_2 = "Any"
    $ a_menu_3 = 0
    $ a_menu_4 = 0
    $ a_menu_8 = 0
    call hide_ui from _call_hide_ui_159
    call screen UI_Menu_Options_Contacts
    jump show_ui

label UI_Menu_Options_KCC:
    call gamecheck from _call_gamecheck_27
    $ a_menu_1 = 0
    $ a_menu_2 = 0
    $ a_menu_3 = 0
    call hide_ui from _call_hide_ui_160
    call screen UI_Menu_Options_KCC
    jump show_ui

label UI_Menu_Options_Skill:
    call gamecheck from _call_gamecheck_28
    $ a_menu_1 = 0
    $ a_menu_2 = 0
    $ a_menu_3 = 0
    call hide_ui from _call_hide_ui_161
    call screen UI_Menu_Options_Skill
    jump show_ui

label UI_Menu_Options_Settings:
    call gamecheck from _call_gamecheck_29
    $ a_menu_1 = "rename"
    $ a_menu_2 = 0
    $ a_menu_3 = 0
    call hide_ui from _call_hide_ui_162
    call screen UI_Menu_Options_Settings
    jump show_ui

label UI_Menu_Options_Square:
    call gamecheck from _call_gamecheck_30
    jump UI_Menu_Options

label UI_Menu_Options_Triangle:
    call gamecheck from _call_gamecheck_31
    if renpy.get_screen("UI_Menu_Options"):
        jump show_ui
    else:
        jump UI_Menu_Options

screen UI_Menu_Options():
    frame:
        background None
        xpadding 0
        ypadding 0
        xsize 620
        ysize 1080
        #xpos 100
        add AlphaMask(
            Fixed(
                Transform(Cell_Img(cellbg[0]),
                    zoom = Cell_WZoom(cellbg[0], cellwz),
                    xalign = (cellwx/100),
                    yalign = (cellwy/100)),
                    xysize=(620, 1080)  # Size of the masked area
            ),
            "images/UI/CellphoneBG/Menu_Mask_2.webp"
        )
        add "images/UI/CellphoneBG/Menu_FG.webp"
        vbox:
            xalign 0.5
            yalign 0.125
            spacing 25
            vbox:
                xalign 0.5
                text renpy.translate_string("Day [gametimeday], [gametimeclock]") size 60
            vbox:
                xalign 0.5
                text renpy.translate_string("[fnamehero] [lnamehero]") size 30
        vpgrid:
            spacing 25
            cols 3
            xalign 0.5
            yalign 0.5
            imagebutton:
                idle "images/UI/SUBMENU_Option_Gallery.webp"
                hover "images/UI/SUBMENU_Option_Gallery.webp"
                action Jump("UI_Menu_Options_Gallery")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Music.webp"
                hover "images/UI/SUBMENU_Option_Music.webp"
                action Jump("UI_Menu_Options_Music")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Contacts.webp"
                hover "images/UI/SUBMENU_Option_Contacts.webp"
                action Jump("UI_Menu_Options_Contacts")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Study.webp"
                hover "images/UI/SUBMENU_Option_Study.webp"
                action Jump("UI_Menu_Options_Skill")
            imagebutton:
                idle "images/UI/SUBMENU_Option_Code.webp"
                hover "images/UI/SUBMENU_Option_Code.webp"
                action Jump("inputcheat")
            imagebutton:
                idle "images/UI/SUBMENU_Option_KCC.webp"
                hover "images/UI/SUBMENU_Option_KCC.webp"
                action Jump("UI_Menu_Options_KCC")
        hbox:
            xalign 0.5
            yalign 0.9
            spacing 50
            imagebutton:
                idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                action Jump("show_ui")
            imagebutton:
                idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                action Jump("show_ui")
            imagebutton:
                idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                action Jump("show_ui")

screen UI_Menu_Options_Contacts():
    add AlphaMask(Cell_Img(cellbg[0]),"images/UI/CellphoneBG/00_MScreen.webp")
    add "images/UI/CellphoneBG/00.webp"
    add "images/UI/button_Option 1 OFF.webp"
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        text renpy.translate_string("Not available yet")
    imagebutton:
        xalign 0.41
        yalign 0.915
        idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
        hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
        action Jump("UI_Menu_Options_Triangle")
    imagebutton:
        xalign 0.5
        yalign 0.915
        idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
        hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
        action Jump("show_ui")

screen UI_Menu_Options_Gallery_IMG():
    on "show" action Function(renpy.hide_screen, "UI_Menu_Options")

    # A player photo sits on black — a vertical one cannot fill a 16:9 screen, and the game behind it must not show through the gap. `photo_view` picks between the three ways of looking at a vertical photo.
    if Cell_Photo(cellbg[a_menu_3]):
        add Solid("#000000")
        if Cell_Tall(cellbg[a_menu_3]) and photo_view == 2:
            # Blown up to the screen's width, so the rest of it is reached by dragging up and down.
            viewport:
                xsize config.screen_width
                ysize config.screen_height
                draggable True
                mousewheel True
                yinitial 0.5
                add Cell_View(cellbg[a_menu_3], 2)
        else:
            add Cell_View(cellbg[a_menu_3], photo_view if Cell_Tall(cellbg[a_menu_3]) else 0)
    else:
        add Cell_Full(cellbg[a_menu_3])
    if a_menu_1 == "p.sdraws":
        frame:
            
            xalign 0.5
            yalign 0.5
            xpadding 50
            ypadding 50
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                text renpy.translate_string("This art was made by [C_Dat]yuro pri[C_Off]") size 60
                textbutton renpy.translate_string("{size=60}Visit artist's Instagram{/size}") xalign 0.5:
                    action [OpenURL("https://www.instagram.com/p.sdraws/"), SetVariable("a_menu_1","")]
                textbutton renpy.translate_string("{size=60}Return{/size}") xalign 0.5:
                    action SetVariable("a_menu_1","")

    elif a_menu_1 == "silvestre_siri":
        frame:
            
            xalign 0.5
            yalign 0.5
            xpadding 50
            ypadding 50
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                text renpy.translate_string("This art was made by [C_Dat]siri[C_Off]") size 60
                textbutton renpy.translate_string("{size=60}Visit artist's Instagram{/size}") xalign 0.5:
                    action [OpenURL("https://www.instagram.com/silvestre_siri/"), SetVariable("a_menu_1","")]
                textbutton renpy.translate_string("{size=60}Return{/size}") xalign 0.5:
                    action SetVariable("a_menu_1","")

    elif a_menu_1 == "TikkiWii":
        frame:
            
            xalign 0.5
            yalign 0.5
            xpadding 50
            ypadding 50
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                text renpy.translate_string("This art was made by [C_Dat]TikkiWii[C_Off]") size 60
                textbutton renpy.translate_string("{size=60}Visit artist's Instagram{/size}") xalign 0.5:
                    action [OpenURL("https://www.instagram.com/tikkiwiii/"), SetVariable("a_menu_1","")]
                textbutton renpy.translate_string("{size=60}Return{/size}") xalign 0.5:
                    action SetVariable("a_menu_1","")

    elif a_menu_1 == "Aquaryart":
        frame:
            
            xalign 0.5
            yalign 0.5
            xpadding 50
            ypadding 50
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                text renpy.translate_string("This art was made by [C_Dat]Aquaryart[C_Off]") size 60
                textbutton renpy.translate_string("{size=60}Visit artist's Carrd{/size}") xalign 0.5:
                    action [OpenURL("https://aquaryartoficial.carrd.co/"), SetVariable("a_menu_1","")]
                textbutton renpy.translate_string("{size=60}Return{/size}") xalign 0.5:
                    action SetVariable("a_menu_1","")

    elif a_menu_1 == "pedrodesenhador":
        frame:
            
            xalign 0.5
            yalign 0.5
            xpadding 50
            ypadding 50
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                text renpy.translate_string("This art was made by [C_Dat]Pedro Desenhador[C_Off]") size 60
                textbutton renpy.translate_string("{size=60}Visit artist's Carrd{/size}") xalign 0.5:
                    action [OpenURL("https://pedrodesenhador.carrd.co/"), SetVariable("a_menu_1","")]
                textbutton renpy.translate_string("{size=60}Return{/size}") xalign 0.5:
                    action SetVariable("a_menu_1","")

    elif a_menu_1 == "goBlinzzy":
        frame:
            
            xalign 0.5
            yalign 0.5
            xpadding 50
            ypadding 50
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                text renpy.translate_string("This art was made by [C_Dat]Blinzzy[C_Off]") size 60
                textbutton renpy.translate_string("{size=60}Visit artist's Twitter{/size}") xalign 0.5:
                    action [OpenURL("https://twitter.com/goBlinzzy/media"), SetVariable("a_menu_1","")]
                textbutton renpy.translate_string("{size=60}Return{/size}") xalign 0.5:
                    action SetVariable("a_menu_1","")

    else:
        if a_menu_4 == 0:
            vbox:
                xalign 0.0
                yalign 0.0
                imagebutton:
                    idle "images/UI/Arrow_L IDLE.webp"
                    hover "images/UI/Arrow_L HOVER.webp"
                    action If (a_menu_3 == 1, true=SetVariable("a_menu_3", len(cellbg)-1), false=SetVariable("a_menu_3", a_menu_3-1))
            vbox:
                xalign 1.0
                yalign 0.0
                imagebutton:
                    idle "images/UI/Arrow_R IDLE.webp"
                    hover "images/UI/Arrow_R HOVER.webp"
                    action If (a_menu_3 == len(cellbg)-1, true=SetVariable("a_menu_3", 1), false=SetVariable("a_menu_3", a_menu_3+1))
            
            frame:
                background None
                xalign 0.5
                yalign 1.1
                xpadding 1000
                ypadding 100
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 300
                    imagebutton at Zoom_2:
                        idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                        hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                        action Jump("UI_Menu_Options_Triangle")
                    imagebutton at Zoom_2:
                        idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                        hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                        action Jump("show_ui")
                    imagebutton at Zoom_2:
                        idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                        hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                        action Jump("UI_Menu_Options_Gallery")

        hbox:
            xalign 0.5
            yalign 0.025
            spacing 250
            if a_menu_4 == 0:
                # White outline, the same treatment the quick_menu buttons get, so these read against any photo behind them instead of vanishing into a dark one.
                imagebutton:
                    idle At("images/UI/SUBMENU_GalleryHide.webp", outline_transform(5, "#FFF", 5.0))
                    hover At("images/UI/SUBMENU_GalleryShow.webp", outline_transform(5, "#FFF", 5.0))
                    action [SetVariable("a_menu_4", 1), Hide("quick_menu")]
                # A vertical player photo can be looked at whole, turned sideways, or blown up and dragged.
                # Both files are 150x150, so this button carries no zoom either and matches the one above.
                if Cell_Tall(cellbg[a_menu_3]):
                    imagebutton:
                        idle At("images/UI/SUBMENU_Option_Autoplay_Circle.webp", outline_transform(5, "#FFF", 5.0))
                        hover At("images/UI/SUBMENU_Option_Autoplay_Circle.webp", outline_transform(5, "#FFF", 5.0))
                        action SetVariable("photo_view", (photo_view + 1) % 3)
                if cellbg[a_menu_3] == "KCC1":
                    imagebutton at Zoom_2:
                        idle "images/UI/SUBMENU_GalleryArt.webp"
                        hover "images/UI/SUBMENU_GalleryArt.webp"
                        action (SetVariable("a_menu_1","p.sdraws"))
                if cellbg[a_menu_3] == "KCC2":
                    imagebutton at Zoom_2:
                        idle "images/UI/SUBMENU_GalleryArt.webp"
                        hover "images/UI/SUBMENU_GalleryArt.webp"
                        action (SetVariable("a_menu_1","pedrodesenhador"))
                if cellbg[a_menu_3] == "KCC3":
                    imagebutton at Zoom_2:
                        idle "images/UI/SUBMENU_GalleryArt.webp"
                        hover "images/UI/SUBMENU_GalleryArt.webp"
                        action (SetVariable("a_menu_1","silvestre_siri"))
                if cellbg[a_menu_3] == "KCC4":
                    imagebutton at Zoom_2:
                        idle "images/UI/SUBMENU_GalleryArt.webp"
                        hover "images/UI/SUBMENU_GalleryArt.webp"
                        action (SetVariable("a_menu_1","TikkiWii"))
                if cellbg[a_menu_3] == "KCC5":
                    imagebutton at Zoom_2:
                        idle "images/UI/SUBMENU_GalleryArt.webp"
                        hover "images/UI/SUBMENU_GalleryArt.webp"
                        action (SetVariable("a_menu_1","Aquaryart"))
                if cellbg[a_menu_3] == "KCC6":
                    imagebutton at Zoom_2:
                        idle "images/UI/SUBMENU_GalleryArt.webp"
                        hover "images/UI/SUBMENU_GalleryArt.webp"
                        action (SetVariable("a_menu_1","goBlinzzy"))
                imagebutton at Zoom_2:
                    idle "images/UI/SUBMENU_GalleryWallpaper.webp"
                    hover "images/UI/SUBMENU_GalleryWallpaper.webp"
                    action Jump("Set_Wallpaper")
            elif a_menu_4 == 1:
                imagebutton at Zoom_2:
                    idle "images/UI/CellphoneBG/00_WScreen.webp"
                    hover "images/UI/CellphoneBG/00_WScreen.webp"
                    action (SetVariable("a_menu_4",0))

screen UI_Menu_Options_Gallery():
    hbox:
        #xpos 100
        frame:
            background None
            xpadding 0
            ypadding 0
            xsize 620
            ysize 1080
            add AlphaMask(
                Fixed(
                    Transform(Cell_Img(cellbg[a_menu_3]),
                        zoom = Cell_WZoom(cellbg[a_menu_3], cellwz),
                        xalign = (cellwx/100),
                        yalign = (cellwy/100)),
                        xysize=(620, 1080)  # Size of the masked area
                ),
                "images/UI/CellphoneBG/Menu_Mask_2.webp"
            )
            add "images/UI/CellphoneBG/Menu_FG.webp"
            hbox:
                xalign 0.5
                yalign 0.2
                spacing 25
                imagebutton:
                    idle "images/UI/Arrow_4 IDLE.webp"
                    hover "images/UI/Arrow_4 HOVER.webp"
                    action If (a_menu_2 == 0, true=(SetVariable("a_menu_2", math.ceil((0.25 * len(cellbg)) - 1.25))), false=(SetVariable("a_menu_2", a_menu_2-1)))
                text renpy.translate_string("Gallery") size 60
                imagebutton:
                    idle "images/UI/Arrow_6 IDLE.webp"
                    hover "images/UI/Arrow_6 HOVER.webp"
                    action If (a_menu_2 == math.ceil((0.25 * len(cellbg)) - 1.25), true=(SetVariable("a_menu_2", 0)), false=(SetVariable("a_menu_2", a_menu_2+1)))
            vbox:
                yalign 0.0
                xalign 0.5
                spacing 10
                # Four photos a page, built from the list itself. It used to be three pages of hand-written slots, which capped the gallery at 12 — the player's own photobooth shots outgrow that.
                for gal_row in range(2):
                    hbox:
                        spacing 10
                        ypos 320
                        for gal_col in range(2):
                            $ gal_i = 1 + a_menu_2 * 4 + gal_row * 2 + gal_col
                            if 1 <= gal_i < len(cellbg):
                                imagebutton at Zoom_025:
                                    idle Cell_Thumb(cellbg[gal_i])
                                    hover Cell_Thumb(cellbg[gal_i])
                                    action [SetVariable("a_menu_3", gal_i), SetVariable("a_menu_2", -1), Jump("UI_Menu_Options_Gallery_IMG")]

            hbox:
                xalign 0.5
                yalign 0.9
                spacing 50
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                    action Jump("UI_Menu_Options_Triangle")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                    action Jump("show_ui")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                    action Jump("show_ui")

screen UI_Menu_Options_Message():
    add AlphaMask(Cell_Img(cellbg[0]),"images/UI/CellphoneBG/00_MScreen.webp")
    add "images/UI/CellphoneBG/00.webp"
    add "images/UI/button_Option 1 OFF.webp"
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        text renpy.translate_string("Not available yet")

    imagebutton:
        xalign 0.41
        yalign 0.915
        idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
        hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
        action Jump("UI_Menu_Options_Triangle")
    imagebutton:
        xalign 0.5
        yalign 0.915
        idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
        hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
        action Jump("show_ui")

screen UI_Menu_Options_Settings():
    hbox:
        #xpos 100
        frame:
            background None
            xpadding 0
            ypadding 0
            xsize 620
            ysize 1080
            add AlphaMask(
                Fixed(
                    Transform(Cell_Img(cellbg[a_menu_3]),
                        zoom = Cell_WZoom(cellbg[a_menu_3], cellwz),
                        xalign = (cellwx/100),
                        yalign = (cellwy/100)),
                        xysize=(620, 1080)  # Size of the masked area
                ),
                "images/UI/CellphoneBG/Menu_Mask_2.webp"
            )
            add "images/UI/CellphoneBG/Menu_FG.webp"
            vbox:
                yalign 0.5
                xalign 0.5
                hbox:
                    xalign 0.5
                    label renpy.translate_string("Edit Data")
                hbox:
                    xalign 0.5
                    textbutton renpy.translate_string("Character Names") action SetVariable("a_menu_1", "rename")
                hbox:
                    xalign 0.5
                    textbutton renpy.translate_string("Stats & Attributes") action SetVariable("a_menu_1", "Cheat")
            
            hbox:
                xalign 0.5
                yalign 0.9
                spacing 50
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                    action Jump("UI_Menu_Options_Triangle")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                    action Jump("show_ui")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                    action Jump("show_ui")
        frame:
            xalign 0.0
            xsize 600
            ysize 1080
            xpadding 50
            ypadding 50
            vbox:
                spacing 20
                if a_menu_1 == "Cheat":
                    label renpy.translate_string("Stats & Attributes")
                    text renpy.translate_string("Stats and attributes can only be editable by enabling cheat. Cheat codes are available on the montly update posts for [C_Dat]{b}big tiers{/b}[C_Off] on [C_Dat]{b}SubscribeStar{/b}[C_Off] and [C_Dat]{b}Patreon{/b}[C_Off].")
                    textbutton renpy.translate_string("How to use codes") action Jump("UI_Menu_Guide_Code")
                    if not preferences.cheatmode:
                        text renpy.translate_string("[C_Neg]Cheat is disabled[C_Off].")
                    else:
                        text renpy.translate_string("[C_Pos]Cheat is enabled[C_Off]. Drag the bars to edit data values.")
                elif a_menu_1 == "rename":
                    label renpy.translate_string("Character Names")
                    text renpy.translate_string("Click on character names to change it. Then write or just leave it blank to generate a random name.")
                    text renpy.translate_string("{p}{b}Generation Method:{/b}")
                    textbutton renpy.translate_string("All names") action SetVariable("fnamelang", "All")
                    textbutton renpy.translate_string("Brazilian names") action SetVariable("fnamelang", "Brazilian")
                    textbutton renpy.translate_string("Fantasy names") action SetVariable("fnamelang", "Fantasy")
                    text renpy.translate_string("{p}Would you like to see a generation method with names from your country/language or from themes that you find interesting? Then consider suggesting a list of names on our Discord!")
        frame:
            xalign 1.0
            xsize 600
            ysize 1080
            xpadding 50
            ypadding 50
            side ("c l"):
                yoffset 10
                area (-15,0,640,1080)
                viewport id "ScrollEditData":
                    xoffset 25
                    draggable True mousewheel True
                    vbox:
                        spacing 25
                        if a_menu_1 == "rename":
                            label renpy.translate_string("Available Maps")
                            hbox:
                                spacing 10
                                vbox:
                                    yalign 0.5
                                    image "icon_city"
                                vbox:
                                    textbutton renpy.translate_string("[rnamecity]") action Function(renpy.call, "rename_rnamecity")

                            text ""
                            label renpy.translate_string("Available Characters")
                            hbox:
                                spacing 10
                                vbox:
                                    yalign 0.5
                                    image "icon_hero"
                                vbox:
                                    textbutton renpy.translate_string("[fnamehero]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "hero", 1)
                                    textbutton renpy.translate_string("[lnamehero]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "hero", 2)
                            hbox:
                                spacing 10
                                vbox:
                                    yalign 0.5
                                    image "icon_wsis"
                                vbox:
                                    textbutton renpy.translate_string("[fnamewsis]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "wsis", 1)
                                    textbutton renpy.translate_string("[lnamestep]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "wsis", 2)
                            hbox:
                                spacing 10
                                vbox:
                                    yalign 0.5
                                    image "icon_wmom"
                                vbox:
                                    textbutton renpy.translate_string("[fnamewmom]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "wmom", 1)
                                    textbutton renpy.translate_string("[lnamestep]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "wmom", 2)
                            hbox:
                                spacing 10
                                vbox:
                                    yalign 0.5
                                    image "icon_wcou"
                                vbox:
                                    textbutton renpy.translate_string("[fnamewcou]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "wcou", 1)
                                    textbutton renpy.translate_string("[lnamerela]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "wcou", 2)
                            hbox:
                                spacing 10
                                vbox:
                                    yalign 0.5
                                    image "icon_wgma"
                                vbox:
                                    textbutton renpy.translate_string("[fnamewgma]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "wgma", 1)
                                    textbutton renpy.translate_string("[lnamerela]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "wgma", 2)
                            hbox:
                                spacing 10
                                vbox:
                                    yalign 0.5
                                    image "icon_wnei"
                                vbox:
                                    textbutton renpy.translate_string("[fnamewnei]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "wnei", 1)
                                    textbutton renpy.translate_string("[lnamewnei]") action Function(renpy.invoke_in_new_context, ChaNameWrite, "wnei", 2)
                            if hero_quest_2 >= 1:
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wpre"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewpre]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wpre", 1)
                                        textbutton renpy.translate_string("[lnamewpre]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wpre", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wric"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewric]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wric", 1)
                                        textbutton renpy.translate_string("[lnamewric]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wric", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wgal"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewgal]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wgal", 1)
                                        textbutton renpy.translate_string("[lnamewgal]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wgal", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wota"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewota]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wota", 1)
                                        textbutton renpy.translate_string("[lnamewota]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wota", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wdis"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewdis]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wdis", 1)
                                        textbutton renpy.translate_string("[lnamewdis]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wdis", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_hriv"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamehriv]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "hriv", 1)
                                        textbutton renpy.translate_string("[lnamehriv]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "hriv", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_hprv"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamehprv]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "hprv", 1)
                                        textbutton renpy.translate_string("[lnamehprv]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "hprv", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wsuk"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewsuk]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wsuk", 1)
                                        textbutton renpy.translate_string("[lnamewsuk]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wsuk", 2)

                                text ""
                                label renpy.translate_string("Unavailable Characters")
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wdel"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewdel]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wdel", 1)
                                        textbutton renpy.translate_string("[lnamewdel]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wdel", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wuza"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewuza]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wuza", 1)
                                        textbutton renpy.translate_string("[lnamewuza]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wuza", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wlaz"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewlaz]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wlaz", 1)
                                        textbutton renpy.translate_string("[lnamewlaz]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wlaz", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wgot"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewgot]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wgot", 1)
                                        textbutton renpy.translate_string("[lnamewgot]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wgot", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_hine"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamehine]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "hine", 1)
                                        textbutton renpy.translate_string("[lnamehine]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "hine", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wdan"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewdan]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wdan", 1)
                                        textbutton renpy.translate_string("[lnamewdan]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wdan", 2)
                                hbox:
                                    spacing 10
                                    vbox:
                                        yalign 0.5
                                        image "icon_wrin"
                                    vbox:
                                        textbutton renpy.translate_string("[fnamewrin]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wrin", 1)
                                        textbutton renpy.translate_string("[lnamewrin]"):
                                                action Function(renpy.invoke_in_new_context, ChaNameWrite, "wrin", 2)

                        if a_menu_1 == "Cheat":
                            if not preferences.cheatmode:
                                vbox:
                                    spacing 50
                                    vbox:
                                        text renpy.translate_string("{image=icon_hero} [C_Nam][fnamehero][C_Off]")
                                        text renpy.translate_string("{image=images/UI/ICON_StatInt.webp}: ") + str(stat_int)[:4] + "%"
                                        text renpy.translate_string("{image=images/UI/ICON_StatCha.webp}: ") + str(stat_cha)[:4] + "%"
                                        text renpy.translate_string("{image=images/UI/ICON_StatPhy.webp}: ") + str(stat_phy)[:4] + "%"
                                    vbox:
                                        text renpy.translate_string("{image=icon_wmom} [C_Nam][fnamewmom][C_Off]")
                                        text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wmom_inti)[:4] + "%"
                                        text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wmom_love)[:4] + "%"
                                        text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wmom_lust)[:4] + "%"
                                    vbox:
                                        text renpy.translate_string("{image=icon_wsis} [C_Nam][fnamewsis][C_Off]")
                                        text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wsis_inti)[:4] + "%"
                                        text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wsis_love)[:4] + "%"
                                        text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wsis_lust)[:4] + "%"
                                    vbox:
                                        text renpy.translate_string("{image=icon_wnei} [C_Nam][fnamewnei][C_Off]")
                                        text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wnei_inti)[:4] + "%"
                                        text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wnei_love)[:4] + "%"
                                        text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wnei_lust)[:4] + "%"
                                    if wpre_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_wpre} [C_Nam][fnamewpre][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wpre_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wpre_love)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wpre_lust)[:4] + "%"
                                    if wric_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_wric} [C_Nam][fnamewric][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wric_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wric_love)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wric_lust)[:4] + "%"
                                    if wgal_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_wgal} [C_Nam][fnamewgal][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wgal_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wgal_love)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wgal_lust)[:4] + "%"
                                    if wota_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_wota} [C_Nam][fnamewota][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wota_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wota_love)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wota_lust)[:4] + "%"
                                    if wdis_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_wdis} [C_Nam][fnamewdis][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wdis_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wdis_love)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wdis_lust)[:4] + "%"
                                    if wgot_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_wgot} [C_Nam][fnamewgot][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wgot_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wgot_love)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wgot_lust)[:4] + "%"
                                    if wdel_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_wdel} [C_Nam][fnamewdel][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wdel_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wdel_love)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wdel_lust)[:4] + "%"
                                    if wuza_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_wuza} [C_Nam][fnamewuza][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wuza_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wuza_love)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wuza_lust)[:4] + "%"
                                    if wlaz_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_wlaz} [C_Nam][fnamewlaz][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(wlaz_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(wlaz_love)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}: ") + str(wlaz_lust)[:4] + "%"
                                    if hriv_quest[0] >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_hriv} [C_Nam][fnamehriv][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(hriv_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(hriv_love)[:4] + "%"
                                    if hprv_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_hprv} [C_Nam][fnamehprv][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(hprv_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(hprv_love)[:4] + "%"
                                    if hine_quest_1 >= 1:
                                        vbox:
                                            text renpy.translate_string("{image=icon_hine} [C_Nam][fnamehine][C_Off]")
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}: ") + str(hine_inti)[:4] + "%"
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}: ") + str(hine_love)[:4] + "%"

                            else:
                                vbox:
                                    label renpy.translate_string("{image=icon_hero} [C_Nam][fnamehero][C_Off]")
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatInt.webp}")
                                        bar value VariableValue("stat_int", 100) xmaximum 300
                                        text str(stat_int) + "%"
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatCha.webp}")
                                        bar value VariableValue("stat_cha", 100) xmaximum 300
                                        text str(stat_cha) + "%"
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatPhy.webp}")
                                        bar value VariableValue("stat_phy", 100) xmaximum 300
                                        text str(stat_phy) + "%"
                                    textbutton ("Money: [C_Pos]Infinite (ON)[C_Off]" if cheat_money else "Money: "+str(round(money, 2))) action Function(Cheat_Infinite, "money")
                                    textbutton ("Perks: [C_Pos]Infinite (ON)[C_Off]" if cheat_perk else "Perks: [perk]") action Function(Cheat_Infinite, "perk")
                                    text ""

                                vbox:
                                    label renpy.translate_string("{image=icon_wmom} [C_Nam][fnamewmom][C_Off]")
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                        bar value VariableValue("wmom_inti", wmom_inti_cap) xmaximum 300
                                        text str(wmom_inti) + "%"
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                        bar value VariableValue("wmom_love", 100) xmaximum 300
                                        text str(wmom_love) + "%"
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                        bar value VariableValue("wmom_lust", 100) xmaximum 300
                                        text str(wmom_lust) + "%"
                                    text ""

                                vbox:
                                    label renpy.translate_string("{image=icon_wsis} [C_Nam][fnamewsis][C_Off]")
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                        bar value VariableValue("wsis_inti", wsis_inti_cap) xmaximum 300
                                        text str(wsis_inti) + "%"
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                        bar value VariableValue("wsis_love", 100) xmaximum 300
                                        text str(wsis_love) + "%"
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                        bar value VariableValue("wsis_lust", 100) xmaximum 300
                                        text str(wsis_lust) + "%"
                                    text ""

                                vbox:
                                    label renpy.translate_string("{image=icon_wnei} [C_Nam][fnamewnei][C_Off]")
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                        bar value VariableValue("wnei_inti", wnei_inti_cap) xmaximum 300
                                        text str(wnei_inti) + "%"
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                        bar value VariableValue("wnei_love", 100) xmaximum 300
                                        text str(wnei_love) + "%"
                                    hbox:
                                        spacing 10
                                        text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                        bar value VariableValue("wnei_lust", 100) xmaximum 300
                                        text str(wnei_lust) + "%"
                                    text ""

                                if wpre_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_wpre} [C_Nam][fnamewpre][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("wpre_inti", char_inti_cap) xmaximum 300
                                            text str(wpre_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("wpre_love", 100) xmaximum 300
                                            text str(wpre_love) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                            bar value VariableValue("wpre_lust", 100) xmaximum 300
                                            text str(wpre_lust) + "%"
                                        text ""

                                if wric_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_wric} [C_Nam][fnamewric][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("wric_inti", char_inti_cap) xmaximum 300
                                            text str(wric_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("wric_love", 100) xmaximum 300
                                            text str(wric_love) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                            bar value VariableValue("wric_lust", 100) xmaximum 300
                                            text str(wric_lust) + "%"
                                        text ""

                                if wgal_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_wgal} [C_Nam][fnamewgal][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("wgal_inti", char_inti_cap) xmaximum 300
                                            text str(wgal_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("wgal_love", 100) xmaximum 300
                                            text str(wgal_love) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                            bar value VariableValue("wgal_lust", 100) xmaximum 300
                                            text str(wgal_lust) + "%"
                                        text ""

                                if wota_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_wota} [C_Nam][fnamewota][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("wota_inti", char_inti_cap) xmaximum 300
                                            text str(wota_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("wota_love", 100) xmaximum 300
                                            text str(wota_love) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                            bar value VariableValue("wota_lust", 100) xmaximum 300
                                            text str(wota_lust) + "%"
                                        text ""

                                if wdis_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_wdis} [C_Nam][fnamewdis][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("wdis_inti", char_inti_cap) xmaximum 300
                                            text str(wdis_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("wdis_love", 100) xmaximum 300
                                            text str(wdis_love) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                            bar value VariableValue("wdis_lust", 100) xmaximum 300
                                            text str(wdis_lust) + "%"
                                        text ""

                                if wgot_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_wgot} [C_Nam][fnamewgot][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("wgot_inti", char_inti_cap) xmaximum 300
                                            text str(wgot_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("wgot_love", 100) xmaximum 300
                                            text str(wgot_love) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                            bar value VariableValue("wgot_lust", 100) xmaximum 300
                                            text str(wgot_lust) + "%"
                                        text ""

                                if wdel_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_wdel} [C_Nam][fnamewdel][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("wdel_inti", char_inti_cap) xmaximum 300
                                            text str(wdel_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("wdel_love", 100) xmaximum 300
                                            text str(wdel_love) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                            bar value VariableValue("wdel_lust", 100) xmaximum 300
                                            text str(wdel_lust) + "%"
                                        text ""

                                if wuza_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_wuza} [C_Nam][fnamewuza][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("wuza_inti", char_inti_cap) xmaximum 300
                                            text str(wuza_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("wuza_love", 100) xmaximum 300
                                            text str(wuza_love) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                            bar value VariableValue("wuza_lust", 100) xmaximum 300
                                            text str(wuza_lust) + "%"
                                        text ""

                                if wlaz_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_wlaz} [C_Nam][fnamewlaz][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("wlaz_inti", char_inti_cap) xmaximum 300
                                            text str(wlaz_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("wlaz_love", 100) xmaximum 300
                                            text str(wlaz_love) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLust.webp}")
                                            bar value VariableValue("wlaz_lust", 100) xmaximum 300
                                            text str(wlaz_lust) + "%"
                                        text ""

                                if hriv_quest[0] >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_hriv} [C_Nam][fnamehriv][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("hriv_inti", char_inti_cap) xmaximum 300
                                            text str(hriv_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("hriv_love", 100) xmaximum 300
                                            text str(hriv_love) + "%"
                                        text ""

                                if hprv_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_hprv} [C_Nam][fnamehprv][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("hprv_inti", char_inti_cap) xmaximum 300
                                            text str(hprv_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("hprv_love", 100) xmaximum 300
                                            text str(hprv_love) + "%"
                                        text ""

                                if hine_quest_1 >= 1:
                                    vbox:
                                        label renpy.translate_string("{image=icon_hine} [C_Nam][fnamehine][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("hine_inti", char_inti_cap) xmaximum 300
                                            text str(hine_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("hine_love", 100) xmaximum 300
                                            text str(hine_love) + "%"
                                        text ""
                                    vbox:
                                        label renpy.translate_string("{image=icon_wsuk} [C_Nam][fnamewsuk][C_Off]")
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatInti.webp}")
                                            bar value VariableValue("wsuk_inti", char_inti_cap) xmaximum 300
                                            text str(wsuk_inti) + "%"
                                        hbox:
                                            spacing 10
                                            text renpy.translate_string("{image=images/UI/ICON_StatLove.webp}")
                                            bar value VariableValue("wsuk_love", 100) xmaximum 300
                                            text str(wsuk_love) + "%"
                                        text ""
                vbar value YScrollValue("ScrollEditData")
            null height 20 #just a height set.

screen UI_Menu_Options_Music(mr):
    default current_track = mr.get_current_song()
    hbox:
        #xpos 100
        frame:
            #style_prefix "music_room"
            background None
            xpadding 0
            ypadding 0
            xsize 620
            ysize 1080
            add AlphaMask(
                Fixed(
                    Transform(Cell_Img(cellbg[a_menu_3]),
                        zoom = Cell_WZoom(cellbg[a_menu_3], cellwz),
                        xalign = (cellwx/100),
                        yalign = (cellwy/100)),
                        xysize=(620, 1080)  # Size of the masked area
                ),
                "images/UI/CellphoneBG/Menu_Mask_2.webp"
            )
            add "images/UI/CellphoneBG/Menu_MG_2B.webp"
            add "images/UI/CellphoneBG/Menu_MG_1.webp"
            frame:
                style_prefix 'track_list'
                background None #"#00000032"
                xsize 540
                ysize 620
                xalign 0.5
                yalign 0.6
                viewport:
                    mousewheel True scrollbars "vertical" draggable True
                    has vbox
                    label renpy.translate_string("Soundtrack") style "music_room_title"
                    ## get_tracklist takes one argument, all_tracks. If all_tracks is
                    ## True, it shows all tracks, including locked ones (which will be
                    ## shown grayed out). If all_tracks is False, it only shows unlocked
                    ## tracks.
                    for num, song in enumerate(mr.get_tracklist(all_tracks=True)):
                        button:
                            action mr.Play(song.path)
                            has hbox
                            fixed:
                                if song is current_track:
                                    ## If the song is currently playing, add a bit of
                                    ## flair with some audio bars.
                                    add Transform('audio_bars', ysize=30, xalign=0.5,
                                        yzoom=-1.0, yalign=0.55)
                                else:
                                    ## The track number. +1 is because enumerate starts
                                    ## at 0 instead of 1.
                                    text str(num+1) align (0.5, 0.55)
                            vbox:
                                spacing 4
                                ## Track info
                                label song.name
                                text song.artist
            add "images/UI/CellphoneBG/Menu_FG.webp"
            hbox:
                xalign 0.5
                yalign 0.9
                spacing 50
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                    action Jump("UI_Menu_Options_Triangle")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                    action Jump("show_ui")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                    action Jump("show_ui")
        frame:
            xsize 600
            ysize 1080
            xpadding 25
            ypadding 25
            xalign 0.0
            yalign 0.0
            vbox:
                spacing 25
                yalign 0.1
                xalign 0.5
                if current_track:
                    add current_track.art xalign 0.5 xsize 500 fit "contain"
                    label current_track.name xalign 0.5
                    text renpy.translate_string("[C_Mnd]")+current_track.artist+"[C_Off]" xalign 0.5
                else:
                    ## To maintain sizing, the default art is shown at alpha 0.0.
                    ## You can also just include it without the alpha 0.0 to display
                    ## it regardless of whether a track is playing or not.
                    add mr.default_art xalign 0.5 alpha 0.0 ysize 440 fit "contain"
                    text "" # This represents the space taken up by the song title
                    text _("No song playing")

                hbox:
                    spacing 10
                    xalign 0.5
                    ## This fixed (and the duration one below it) ensure that the
                    ## pos and duration text don't change size as the text updates
                    ## (which could move the hbox around since it's center-aligned).
                    add mr.get_pos(style="music_room_pos") xalign 0.0
                    ## This makes a special music bar which shows the current position
                    ## of the song, and also allows you to click the bar to skip around.
                    ## It takes the same style properties as a regular bar, and in this
                    ## case even gets the style "music_room_bar" because of the style
                    ## prefix.
                    ## It needs to be passed the music room - in our case, that's
                    ## `room mr` because the music room is passed in as "mr".
                    music_bar room mr xsize 300 xalign 0.5
                    ## Again, this fixed helps keep the hbox from changing size.
                    add mr.get_duration(style="music_room_duration") xalign 1.0

                ## This contains the music controls. You can remove whichever ones
                ## you don't need.
                hbox:
                    xalign 0.5
                    spacing 25
                    ################## Shuffle button ##################
                    frame:
                        background None
                        xpadding 0
                        ypadding 0
                        xsize 75
                        ysize 75
                        imagebutton:
                            idle "shuffle_button"
                            at colorize_button(MUSIC_ROOM_INSENSITIVE_COLOR, MUSIC_ROOM_IDLE_COLOR)
                            action mr.ToggleShuffle()
                        ################## Previous, play/pause, next buttons ##################
                    frame:
                        background None
                        xpadding 0
                        ypadding 0
                        xsize 75
                        ysize 75
                        imagebutton:
                            idle "prev_button"
                            at colorize_button()
                            action mr.Previous()
                    frame:
                        background None
                        xpadding 0
                        ypadding 0
                        xsize 75
                        ysize 75
                        imagebutton:
                            at colorize_button()
                            idle "pause_button" hover "pause_button"
                            selected_idle "play_button" selected_hover "play_button"
                            action mr.PlayAction()
                    frame:
                        background None
                        xpadding 0
                        ypadding 0
                        xsize 75
                        ysize 75
                        imagebutton:
                            idle "next_button"
                            at colorize_button()
                            action mr.Next()
                    frame:
                        background None
                        xpadding 0
                        ypadding 0
                        xsize 75
                        ysize 75
                        imagebutton:
                            xalign 0.5
                            yalign 0.5
                            at colorize_button(idle=MUSIC_ROOM_INSENSITIVE_COLOR,
                                hover=MUSIC_ROOM_IDLE_COLOR)
                            idle "repeat_all_button"
                            action mr.CycleLoop()
                        if mr.single_track:
                            text renpy.translate_string("{size=60}{b}1{/b}{/size}") at colorize_button() xalign 0.5 yalign 0.5
                viewport:
                    xsize 540
                    ysize 350
                    yalign 1.0
                    yoffset 10
                    mousewheel True scrollbars "vertical" draggable True
                    if current_track:
                        text current_track.description justify True
        frame:
            xsize 600
            ysize 1080
            xpadding 10
            ypadding 25
            xalign 0.5
            yalign 0.0
            viewport:
                mousewheel True scrollbars "vertical" draggable True xalign 0.5
                style "music_room_title"
                if current_track:
                    text current_track.lyrics style "prosa" xalign 0.5

screen UI_Menu_Options_KCC():
    hbox:
        #xpos 100
        frame:
            background None
            xpadding 0
            ypadding 0
            xsize 620
            ysize 1080
            add AlphaMask(
                Fixed(
                    Transform(Cell_Img(cellbg[a_menu_3]),
                        zoom = Cell_WZoom(cellbg[a_menu_3], cellwz),
                        xalign = (cellwx/100),
                        yalign = (cellwy/100)),
                        xysize=(620, 1080)  # Size of the masked area
                ),
                "images/UI/CellphoneBG/Menu_Mask_2.webp"
            )
            add "images/UI/CellphoneBG/Menu_FG.webp"
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 10
                vbox:
                    xalign 0.5
                    label renpy.translate_string("Dev Info{p}")
                vbox:
                    xalign 0.5
                    textbutton renpy.translate_string("Projects") action SetVariable("a_menu_1", 0)
                vbox:
                    xalign 0.5
                    textbutton renpy.translate_string("Discord") action SetVariable("a_menu_1", "DISCORD")
                vbox:
                    xalign 0.5
                    textbutton renpy.translate_string("Support") action SetVariable("a_menu_1", "SUPPORT")
                vbox:
                    xalign 0.5
                    textbutton renpy.translate_string("KCC") action SetVariable("a_menu_1", "KCC")
            
            hbox:
                xalign 0.5
                yalign 0.9
                spacing 50
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                    action Jump("UI_Menu_Options_Triangle")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                    action Jump("show_ui")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                    action Jump("show_ui")
        frame:
            xsize 1200
            ysize 1080
            xpadding 50
            ypadding 50
            xalign 0.0
            yalign 0.0
            side ("c l"):
                area (-10,0,1200,1000)
                viewport id "ScrollAuthorData":
                    xoffset 25
                    draggable True mousewheel True
                    vbox:
                        spacing 15
                        if a_menu_1 == 0:
                            label renpy.translate_string("All In One")
                            text renpy.translate_string("You can simply access my Carrd to know everything about my games, projects, and social media.")
                            textbutton renpy.translate_string("Open Carrd") action [OpenURL("https://quiquersson.carrd.co/"), Return()]
                            label renpy.translate_string("{p}Social Media")
                            text renpy.translate_string("You can follow me on your preferred social media.")
                            textbutton renpy.translate_string("Open YouTube") action [OpenURL("https://www.youtube.com/@quiquersson"), Return()]
                            textbutton renpy.translate_string("Open Twitch") action [OpenURL("https://www.twitch.tv/quiquersson"), Return()]
                            textbutton renpy.translate_string("Open X/Twitter") action [OpenURL("https://x.com/quiquersson"), Return()]
                            textbutton renpy.translate_string("Open Instagram") action [OpenURL("https://www.instagram.com/quiquersson/"), Return()]
                            textbutton renpy.translate_string("Open DeviantArt") action [OpenURL("https://www.deviantart.com/quiquersson"), Return()]
                            label renpy.translate_string("{p}Games")
                            text renpy.translate_string("Follow my account on itch.io to stay up to date with updates of WelCUM To The City and Kawaii Character Creator.")
                            textbutton renpy.translate_string("Open Itch") action [OpenURL("https://quiquersson.itch.io"), Return()]
                            label renpy.translate_string("{p}SFW Stuff")
                            text renpy.translate_string("Feel free to follow my SFW accounts and projects if you're interested.")
                            textbutton renpy.translate_string("Open Carrd") action [OpenURL("https://kikeluzi.carrd.co/"), Return()]
                            
                        if a_menu_1 == "KCC":
                            label renpy.translate_string("Kawaii Character Creator")
                            text renpy.translate_string("Create your own character in this sexy Dress-Up game")
                            textbutton renpy.translate_string("Open the game") action [OpenURL("https://quiquersson.itch.io/kcc"), Return()]

                        if a_menu_1 == "DISCORD":
                            label renpy.translate_string("Discord")
                            text renpy.translate_string("Join our Discord and let's do fun community things, like:{p}{image=starchan} Interact with other cool pervert people like us{p}{image=starchan} Give me game feedbacks{p}{image=starchan} Report errors{p}{image=starchan} Give suggestions for future characters or scenes. {p}{image=starchan} Chat with WelCUM To The City characters '-'")
                            image "UI/Guide/Discord.webp"
                            textbutton renpy.translate_string("Join Our Guild") action [OpenURL("https://discord.gg/raU65TZqbE"), Return()]

                        if a_menu_1 == "SUPPORT":
                            label renpy.translate_string("Financial Support")
                            text renpy.translate_string("You can directly support me on Patreon or SubscribeStar, allowing me to dedicate more time to game development. Plus you get early access to my games and also access to some exclusive stuff. I should be posting the same content on both platforms from now on..")
                            textbutton renpy.translate_string("Open Patreon") action [OpenURL("https://www.patreon.com/quiquersson"), Return()]
                            textbutton renpy.translate_string("Open SubscribeStar") action [OpenURL("https://subscribestar.adult/quiquersson"), Return()]
                vbar value YScrollValue("ScrollAuthorData")

screen UI_Menu_Options_Contacts():
    hbox:
        #xpos 100
        frame:
            background None
            xpadding 0
            ypadding 0
            xsize 620
            ysize 1080

            add AlphaMask(
                Fixed(
                    Transform(Cell_Img(cellbg[a_menu_3]),
                        zoom = Cell_WZoom(cellbg[a_menu_3], cellwz),
                        xalign = (cellwx/100),
                        yalign = (cellwy/100)),
                        xysize=(620, 1080)  # Size of the masked area
                ),
                "images/UI/CellphoneBG/Menu_Mask_2.webp"
            )

            add "images/UI/CellphoneBG/Menu_MG_2A.webp"

            if a_menu_1 != "none":
                image "[a_menu_1!u] STYLE":
                    xalign 0.5 yalign 0.0 zoom 0.75 xpos 312 ypos 100
            else:
                image AlphaMask(
                Fixed(
                    Transform("NONE",
                        xalign = 0.5,
                        yalign = 0.0,
                        zoom = 0.47,
                        xpos = 312,
                        ypos = 100),
                        xysize=(620, 1080)
                ),
                "images/UI/CellphoneBG/Menu_Mask_2.webp"
                )

            add "images/UI/CellphoneBG/Menu_MG_1.webp"

            if a_menu_1 != "none":
                vbox:
                    spacing 10 xalign 0.5 yalign 0.15
                    if a_menu_1 in ["wsis", "wmom"]:
                        label str(getattr(store, f"fname{a_menu_1}") + " [lnamestep]") xalign 0.5
                    elif a_menu_1 in ["wcou", "wgma", "waun"]:
                        label str(getattr(store, f"fname{a_menu_1}") + " [lnamerela]") xalign 0.5
                    else:
                        label str(getattr(store, f"fname{a_menu_1}") + " " + getattr(store, f"lname{a_menu_1}")) xalign 0.5
                    hbox:
                        xalign 0.5
                        if len(getattr(store, a_menu_1 + "_achiev_wear")) >= 2:
                            textbutton renpy.translate_string("{size=60}◀{/size}") action [SetVariable("a_menu_8", (a_menu_8 - 1) % max(1, len(getattr(store, a_menu_1 + "_achiev_wear"))))]
                        else:
                            textbutton renpy.translate_string("{size=60}◀{/size}") action None
                        text renpy.translate_string("{size=60} Style {/size}")
                        if len(getattr(store, a_menu_1 + "_achiev_wear")) >= 2:
                            textbutton renpy.translate_string("{size=60}▶{/size}") action [SetVariable("a_menu_8", (a_menu_8 + 1) % max(1, len(getattr(store, a_menu_1 + "_achiev_wear"))))]
                        else:
                            textbutton renpy.translate_string("{size=60}▶{/size}") action None
            else:
                vbox:
                    spacing 10 xalign 0.5 yalign 0.15
                    label renpy.translate_string("Select a Character") xalign 0.5 yalign 0.15
                    textbutton renpy.translate_string("{size=40}Style{/size}") action None xalign 0.5


            add "images/UI/CellphoneBG/Menu_FG.webp"
            
            hbox:
                xalign 0.5
                yalign 0.9
                spacing 50
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                    action Jump("UI_Menu_Options_Triangle")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                    action Jump("show_ui")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                    action Jump("show_ui")

        frame:
            xysize(1200, 1080)
            xpadding 25
            ypadding 25
            hbox:
                spacing 50
                side ("c l"):
                    area (0, 0, 200, 1030)
                    vpgrid id "ScrollOCButton":
                        draggable True mousewheel True
                        xoffset 20
                        spacing 25
                        cols 1
                        if a_menu_2 in ["Any", 0]:
                            if gametimeday >= 2:
                                imagebutton:
                                    idle At("images/UI/OC_NONE.webp", ButtonIdle)
                                    hover At("images/UI/OC_NONE.webp", ButtonHover)
                                    action [SetVariable("a_menu_1", "none"), SetVariable("a_menu_8", 0)]
                            imagebutton:
                                idle At("images/UI/OC_HERO.webp", ButtonIdle)
                                hover At("images/UI/OC_HERO.webp", ButtonHover)
                                action [SetVariable("a_menu_1", "hero"), SetVariable("a_menu_8", 0)]
                        if a_menu_2 in ["Dateable", "Any"]:
                            imagebutton:
                                idle At("images/UI/OC_WMOM.webp", ButtonIdle)
                                hover At("images/UI/OC_WMOM.webp", ButtonHover)
                                action [SetVariable("a_menu_1", "wmom"), SetVariable("a_menu_8", 0)]
                            imagebutton:
                                idle At("images/UI/OC_WSIS.webp", ButtonIdle)
                                hover At("images/UI/OC_WSIS.webp", ButtonHover)
                                action [SetVariable("a_menu_1", "wsis"), SetVariable("a_menu_8", 0)]
                            imagebutton:
                                idle At("images/UI/OC_WNEI.webp", ButtonIdle)
                                hover At("images/UI/OC_WNEI.webp", ButtonHover)
                                action [SetVariable("a_menu_1", "wnei"), SetVariable("a_menu_8", 0)]
                            if wpre_quest_1 >= 1:
                                imagebutton:
                                    idle At("images/UI/OC_WPRE.webp", ButtonIdle)
                                    hover At("images/UI/OC_WPRE.webp", ButtonHover)
                                    action [SetVariable("a_menu_1", "wpre"), SetVariable("a_menu_8", 0)]
                            if wota_quest_1 >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_WOTA.webp", ButtonIdle)
                                        hover At("images/UI/OC_WOTA.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "wota"), SetVariable("a_menu_8", 0)]
                            if wdis_quest_1 >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_WDIS.webp", ButtonIdle)
                                        hover At("images/UI/OC_WDIS.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "wdis"), SetVariable("a_menu_8", 0)]
                            if wgal_quest_1 >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_WGAL.webp", ButtonIdle)
                                        hover At("images/UI/OC_WGAL.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "wgal"), SetVariable("a_menu_8", 0)]
                            if wric_quest_1 >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_WRIC.webp", ButtonIdle)
                                        hover At("images/UI/OC_WRIC.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "wric"), SetVariable("a_menu_8", 0)]
                            if wgot_quest_1 >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_WGOT.webp", ButtonIdle)
                                        hover At("images/UI/OC_WGOT.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "wgot"), SetVariable("a_menu_8", 0)]
                            if wdel_quest_1 >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_WDEL.webp", ButtonIdle)
                                        hover At("images/UI/OC_WDEL.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "wdel"), SetVariable("a_menu_8", 0)]
                            if wuza_quest_1 >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_WUZA.webp", ButtonIdle)
                                        hover At("images/UI/OC_WUZA.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "wuza"), SetVariable("a_menu_8", 0)]
                            if wlaz_quest_1 >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_WLAZ.webp", ButtonIdle)
                                        hover At("images/UI/OC_WLAZ.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "wlaz"), SetVariable("a_menu_8", 0)]

                        if a_menu_2 in ["Friendly", "Any"]:
                            if hprv_quest_1 >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_HPRV.webp", ButtonIdle)
                                        hover At("images/UI/OC_HPRV.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "hprv"), SetVariable("a_menu_8", 0)]
                            if hine_quest_1 >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_HINE.webp", ButtonIdle)
                                        hover At("images/UI/OC_HINE.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "hine"), SetVariable("a_menu_8", 0)]
                            if hriv_quest[0] >= 1:
                                    imagebutton:
                                        idle At("images/UI/OC_HRIV.webp", ButtonIdle)
                                        hover At("images/UI/OC_HRIV.webp", ButtonHover)
                                        action [SetVariable("a_menu_1", "hriv"), SetVariable("a_menu_8", 0)]

                        if a_menu_2 in ["Tutor", "Any"]:
                            if hero_quest_1 >= 6:
                                imagebutton:
                                    idle At("images/UI/OC_WCOU.webp", ButtonIdle)
                                    hover At("images/UI/OC_WCOU.webp", ButtonHover)
                                    action [SetVariable("a_menu_1", "wcou"), SetVariable("a_menu_8", 0)]

                        if a_menu_2 in ["Sex-Doll", "Any"]:
                            if hero_quest_3 >= 3:
                                imagebutton:
                                    idle At("images/UI/OC_WGMA.webp", ButtonIdle)
                                    hover At("images/UI/OC_WGMA.webp", ButtonHover)
                                    action [SetVariable("a_menu_1", "wgma"), SetVariable("a_menu_8", 0)]
                            if hine_quest_1 >= 1:
                                imagebutton:
                                    idle At("images/UI/OC_wsuk.webp", ButtonIdle)
                                    hover At("images/UI/OC_wsuk.webp", ButtonHover)
                                    action [SetVariable("a_menu_1", "wsuk"), SetVariable("a_menu_8", 0)]
                    vbar value YScrollValue("ScrollOCButton")

                vbox:
                    xysize(850, 980)
                    xalign 0.5
                    yalign 0.0
                    spacing 50

                    hbox:
                        spacing 10
                        xalign 0.5
                        yalign 0.0
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_Stat.webp", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_Stat.webp", ButtonHover)
                            action SetVariable("a_menu_4", 0)
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_List.webp", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_List.webp", ButtonHover)
                            action SetVariable("a_menu_4", 1)
                        imagebutton:
                            idle At("images/UI/SUBMENU_Option_Quest.webp", ButtonIdle)
                            hover At("images/UI/SUBMENU_Option_Quest.webp", ButtonHover)
                            action SetVariable("a_menu_4", 2)
                        if persistent.debug == True or perk_int_per >= 1:
                            imagebutton:
                                idle At("images/UI/QUICK_Time.webp", ButtonIdle)
                                hover At("images/UI/QUICK_Time.webp", ButtonHover)
                                action SetVariable("a_menu_4", 3)

                    vbox:
                        xalign 0.5
                        yalign 0.0
                        spacing 25

                        if a_menu_4 == 0 and a_menu_1 not in ["none"]:

                            side ("c r"):
                                area (10, 0, 900, 800)
                                viewport id "ScrollOCData":
                                    draggable True mousewheel True xoffset -10

                                    vbox:
                                        xalign 0.5
                                        yalign 0.0
                                        spacing 10

                                        # Name editing buttons
                                        $ _char_fname = getattr(store, f"fname{a_menu_1}")
                                        if a_menu_1 in ["wmom", "wsis"]:
                                            $ _char_lname = lnamestep
                                        elif a_menu_1 in ["wgma", "wcou", "waun"]:
                                            $ _char_lname = lnamerela
                                        else:
                                            $ _char_lname = getattr(store, f"lname{a_menu_1}")

                                        hbox:
                                            spacing 10
                                            frame:
                                                background "#323232" xsize 420 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                textbutton renpy.translate_string("{size=50}[_char_fname]{/size}"):
                                                    xalign 0.5 yalign 0.5
                                                    action Function(renpy.invoke_in_new_context, ChaNameWrite, a_menu_1, 1)
                                            frame:
                                                background "#323232" xsize 420 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                textbutton renpy.translate_string("{size=50}[_char_lname]{/size}"):
                                                    xalign 0.5 yalign 0.5
                                                    action Function(renpy.invoke_in_new_context, ChaNameWrite, a_menu_1, 2)

                                        # Stat bars — every cheat bar re-runs check_stat() so the database tab's rates follow the drag without leaving the menu.
                                        if a_menu_1 == "hero":
                                            # One main bar per HERO_STAT_TREE entry; its icon folds the three sub-stat bars open (a_menu_10 holds the open one, so opening another closes the first).
                                            for _main, _name, _icon, _subs in HERO_STAT_TREE:
                                                frame:
                                                    background None xsize 850 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                    if preferences.cheatmode:
                                                        bar value HeroStatValue(_main) ymaximum 100 xmaximum 850
                                                    else:
                                                        bar value stat_value("hero", _main) range 100 ymaximum 100 xmaximum 850
                                                    hbox:
                                                        xalign 0.0 yalign 0.5 xpos 10 spacing 10
                                                        imagebutton:
                                                            idle At("images/UI/" + _icon + ".webp", ButtonIdle)
                                                            hover At("images/UI/" + _icon + ".webp", ButtonHover)
                                                            selected_idle At("images/UI/" + _icon + ".webp", ButtonHover)
                                                            yalign 0.5
                                                            action ToggleVariable("a_menu_10", _main, 0)
                                                        text renpy.translate_string("{size=50}") + _name + ": " + str(stat_value("hero", _main))[:4] + "%{/size}" yalign 0.5 outlines [(2, "#191919", 0, 0)]
                                                if a_menu_10 == _main:
                                                    for _sub, _sub_name in _subs:
                                                        frame:
                                                            background None xsize 780 ysize 80 xalign 1.0 yalign 0.5 xpadding 0 ypadding 0
                                                            if preferences.cheatmode:
                                                                bar value HeroStatValue(_sub) ymaximum 80 xmaximum 780
                                                            else:
                                                                bar value stat_value("hero", _sub) range 100 ymaximum 80 xmaximum 780
                                                            text renpy.translate_string("{size=40}• ") + _sub_name + ": " + str(stat_value("hero", _sub))[:4] + "%{/size}" xalign 0.0 yalign 0.5 xpos 10 outlines [(2, "#191919", 0, 0)]
                                        else:
                                            frame:
                                                background None xsize 850 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                if preferences.cheatmode:
                                                    if a_menu_1 in ["wmom"]:
                                                        bar value VariableValue(stat_key(a_menu_1, "inti"), wmom_inti_cap, action=Function(check_stat)) ymaximum 100 xmaximum 850 xalign 0.5 yalign 0.5

                                                    elif a_menu_1 in ["wsis"]:
                                                        bar value VariableValue(stat_key(a_menu_1, "inti"), wsis_inti_cap, action=Function(check_stat)) ymaximum 100 xmaximum 850 xalign 0.5 yalign 0.5

                                                    elif a_menu_1 in ["wnei"]:
                                                        bar value VariableValue(stat_key(a_menu_1, "inti"), wnei_inti_cap, action=Function(check_stat)) ymaximum 100 xmaximum 850 xalign 0.5 yalign 0.5

                                                    else:
                                                        bar value VariableValue(stat_key(a_menu_1, "inti"), char_inti_cap, action=Function(check_stat)) ymaximum 100 xmaximum 850 xalign 0.5 yalign 0.5
                                                else:
                                                    if a_menu_1 in ["wmom"]:
                                                        bar value stat_value(a_menu_1, "inti") range wmom_inti_cap ymaximum 100 xmaximum 850 xalign 0.5 yalign 0.5

                                                    elif a_menu_1 in ["wsis"]:
                                                        bar value stat_value(a_menu_1, "inti") range wsis_inti_cap ymaximum 100 xmaximum 850 xalign 0.5 yalign 0.5

                                                    elif a_menu_1 in ["wnei"]:
                                                        bar value stat_value(a_menu_1, "inti") range wnei_inti_cap ymaximum 100 xmaximum 850 xalign 0.5 yalign 0.5

                                                    else:
                                                        bar value stat_value(a_menu_1, "inti") range char_inti_cap ymaximum 100 xmaximum 850 xalign 0.5 yalign 0.5
                                                text renpy.translate_string("{size=50}{image=images/UI/ICON_StatInti.webp} Intimacy: ")+str(stat_value(a_menu_1, "inti"))[:4]+"%{/size}" xalign 0.0 yalign 0.5 xpos 10 outlines [(2, "#191919", 0, 0)]
                                            frame:
                                                background None xsize 850 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                if preferences.cheatmode:
                                                    bar value VariableValue(stat_key(a_menu_1, "love"), 100, action=Function(check_stat)) ymaximum 100 xmaximum 850
                                                else:
                                                    bar value (stat_value(a_menu_1, "love")+100) range 200 ymaximum 100 xmaximum 850
                                                text renpy.translate_string("{size=50}{image=images/UI/ICON_StatLove.webp} Love: ")+str(stat_value(a_menu_1, "love"))[:4]+"%{/size}" xalign 0.0 yalign 0.5 xpos 10 outlines [(2, "#191919", 0, 0)]
                                            frame:
                                                background None xsize 850 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                if preferences.cheatmode:
                                                    bar value VariableValue(stat_key(a_menu_1, "lust"), 100, action=Function(check_stat)) ymaximum 100 xmaximum 850
                                                else:
                                                    bar value stat_value(a_menu_1, "lust") range 100 ymaximum 100 xmaximum 850
                                                text renpy.translate_string("{size=50}{image=images/UI/ICON_StatLust.webp} Lust: ")+str(stat_value(a_menu_1, "lust"))[:4]+"%{/size}" xalign 0.0 yalign 0.5 xpos 10 outlines [(2, "#191919", 0, 0)]
                                        if a_menu_1 == "wnei":
                                            hbox:
                                                spacing 10
                                                frame:
                                                    background None xsize 420 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                    if preferences.cheatmode:
                                                        bar value VariableValue(stat_key("hpap", "love"), wnei_inti_cap, action=Function(check_stat)) ymaximum 100 xmaximum 420
                                                    else:
                                                        bar value (stat_value("hpap", "love")) range wnei_inti_cap ymaximum 100 xmaximum 420
                                                    text renpy.translate_string("{size=50}👨‍👧 Dad's: ")+str(stat_value("hpap", "love"))[:4]+"%{/size}" xalign 0.0 yalign 0.5 xpos 10 outlines [(2, "#191919", 0, 0)]
                                                frame:
                                                    background None xsize 420 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                    if preferences.cheatmode:
                                                        bar value VariableValue(stat_key("wmam", "love"), wnei_inti_cap, action=Function(check_stat)) ymaximum 100 xmaximum 420
                                                    else:
                                                        bar value (stat_value("wmam", "love")) range wnei_inti_cap ymaximum 100 xmaximum 420
                                                    text renpy.translate_string("{size=50}👩‍👧 Mom's: ")+str(stat_value("wmam", "love"))[:4]+"%{/size}" xalign 0.0 yalign 0.5 xpos 10 outlines [(2, "#191919", 0, 0)]
                                        if a_menu_1 == "hero" or perk_int_per >= 1:
                                            frame:
                                                background None xsize 850 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                if preferences.cheatmode:
                                                    bar value VariableValue(stat_key(a_menu_1, "hyg"), 100, action=Function(check_stat)) ymaximum 100 xmaximum 850
                                                else:
                                                    bar value stat_value(a_menu_1, "hyg") range 100 ymaximum 100 xmaximum 850
                                                text renpy.translate_string("{size=50}{image=images/UI/ICON_StatHyg.webp} Hygiene: ")+str(stat_value(a_menu_1, "hyg"))[:4]+"%{/size}" xalign 0.0 yalign 0.5 xpos 10 outlines [(2, "#191919", 0, 0)]
                                            frame:
                                                background None xsize 850 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                if preferences.cheatmode:
                                                    bar value VariableValue(stat_key(a_menu_1, "eat"), 100, action=Function(check_stat)) ymaximum 100 xmaximum 850
                                                else:
                                                    bar value stat_value(a_menu_1, "eat") range 100 ymaximum 100 xmaximum 850
                                                text renpy.translate_string("{size=50}🍗 Saciety: ")+str(stat_value(a_menu_1, "eat"))[:4]+"%{/size}" xalign 0.0 yalign 0.5 xpos 10 outlines [(2, "#191919", 0, 0)]
                                            hbox:
                                                spacing 10
                                                frame:
                                                    background "#323232" xsize 420 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                    if preferences.cheatmode and a_menu_1 == "hero":
                                                        # Only HERO's panel toggles the cheat — the wallet it pays into is his.
                                                        textbutton ("{size=50}{image=images/UI/ICON_StatMon.webp} Money: [C_Pos]Infinite (ON)[C_Off]{/size}" if cheat_money else "{size=50}{image=images/UI/ICON_StatMon.webp} Money: $"+str(stat_value(a_menu_1, "money"))[:4]+"{/size}"):
                                                            xalign 0.0 yalign 0.5 xpos 10 text_outlines [(2, "#191919", 0, 0)]
                                                            action Function(Cheat_Infinite, "money")
                                                    else:
                                                        text renpy.translate_string("{size=50}{image=images/UI/ICON_StatMon.webp} Money: $")+str(stat_value(a_menu_1, "money"))[:4]+"{/size}" xalign 0.0 yalign 0.5 xpos 10 outlines [(2, "#191919", 0, 0)]
                                                frame:
                                                    background "#323232" xsize 420 ysize 100 xalign 0.5 yalign 0.5 xpadding 0 ypadding 0
                                                    if preferences.cheatmode and a_menu_1 == "hero":
                                                        # Perk points are HERO's alone, so only his panel toggles the cheat.
                                                        textbutton ("{size=50}🗿 Perks: [C_Pos]Infinite (ON)[C_Off]{/size}" if cheat_perk else "{size=50}🗿 Perks: [perk]{/size}"):
                                                            xalign 0.0 yalign 0.5 xpos 10 text_outlines [(2, "#191919", 0, 0)]
                                                            action Function(Cheat_Infinite, "perk")
                                                    else:
                                                        text renpy.translate_string("{size=50}🗿 Perks: [perk]{/size}") xalign 0.0 yalign 0.5 xpos 10 outlines [(2, "#191919", 0, 0)]


                                vbar value YScrollValue("ScrollOCData")

                        elif a_menu_4 == 0 and a_menu_1 == "none":
                            # Name Generation Tools
                            label renpy.translate_string("Name Generation")
                                        
                            $ _batch_chars = ["hero", "wmom", "wsis", "wnei", "wcou", "wgma", "wpre", "wric", "wgal", "wota", "wdis", "wgot", "wdel", "wuza", "wlaz", "hprv", "hine", "hriv", "wsuk", "wdan", "wrin"]
                            textbutton renpy.translate_string("Generate All First Names") action Function(ChaNameGen, char_id=_batch_chars, target=1)
                            textbutton renpy.translate_string("Generate All Last Names") action Function(ChaNameGen, char_id=_batch_chars, target=2)

                            text renpy.translate_string("{p}{b}Generation Method:{/b} [fnamelang]")

                            hbox:
                                spacing 10
                                box_wrap True
                                for _lang in ["All", "English", "Portuguese", "Fantasy", "Spanish", "Chinese", "French", "Italian", "German", "Japanese", "Polish", "Filipino", "Slavic"]:
                                    textbutton _lang:
                                        action SetVariable("fnamelang", _lang)
                                        #text_size 20
                                        padding (5, 5, 5, 5)
                                        if fnamelang == _lang:
                                            background Solid("#FFFFFF25")
                                        else:
                                            background Solid("#FFFFFF10")
                                        hover_background Solid("#FFFFFF35")

                        elif a_menu_4 == 1:
                            frame:
                                side ("c r"):
                                    area (25, 0, 850, 800)
                                    viewport id "Scroll_Database":
                                        draggable True mousewheel True
                                        vbox:
                                            # The page is built from CHAR_DATA (Data - Char.rpy): one data entry per character, plus WCOU's gate, instead of a hand-written text block each.
                                            if a_menu_1 == "wcou" and hero_quest_2 < 4:
                                                text _p("""{size=40}{b}[C_Neg]Finish all content of 2nd Day to unlock info[C_Off]{/b}
                                                            {p}{p}{b}Type:{/b} [C_Mnd]???[C_Off].
                                                            {p}{p}{b}Personality:{/b} [C_Mnd]???[C_Off]
                                                            {p}{p}{b}Height:{/b} [C_Mnd]???[C_Off]
                                                            {p}{p}{b}[C_Pos]Bonus[C_Off] & [C_Neg]Onus[C_Off]:{/b} [C_Mnd]???[C_Off]
                                                                {/size}""")
                                            else:
                                                text Char_InfoText(a_menu_1)
                                    vbar value YScrollValue("Scroll_Database")
                            null height 20 #just a height set.

                        elif a_menu_4 == 2:
                            # Built from CONTENT_DATA (Data - Content.rpy): the list, its ✅/❌ and the bar all read the same entries the Custom new game toggles.
                            $ _content = Content_Shown(a_menu_1)
                            $ _content_done, _content_total = Content_Progress(a_menu_1)
                            vbox:
                                xalign 0.0
                                yalign 0.0
                                spacing 10
                                vbox:
                                    xalign 0.5
                                    label renpy.translate_string("Content Progress")
                                vbox:
                                    xalign 0.5
                                    bar value (_content_done if _content_total else 1) range (_content_total or 1) xmaximum 650
                                text ""
                                frame:
                                    background "gui/game_menu.webp"
                                    side ("c r"):
                                        area (25, 0, 850, 650)
                                        viewport id "ScrollContent":
                                            draggable True mousewheel True

                                            vbox:
                                                xalign 0.0
                                                yalign 0.0
                                                spacing 15
                                                if a_menu_1 == "none":
                                                    text Content_UnlockStatus()
                                                if _content:
                                                    for _entry in _content:
                                                        label Content_Title(_entry)
                                                        for _block in Content_Text(_entry):
                                                            text _block
                                                        text ""
                                                elif a_menu_1 != "none":
                                                    vbox:
                                                        xalign 0.5
                                                        label renpy.translate_string("{p}Unavailable Content") xalign 0.5
                                                        text renpy.translate_string("Oops. No data available for this character in the current game version.") xalign 0.5
                                        vbar value YScrollValue("ScrollContent")

                        elif a_menu_4 == 3 and a_menu_1 not in  ["none", "hero"]:
                            side ("c r"):
                                area (25, 0, 1000, 850)
                                viewport id "Scroll_Schedule":
                                    draggable True mousewheel True
                                    vbox:
                                        spacing 10
                                        text renpy.translate_string("{b}Map:{/b} ") + str(getattr(store, a_menu_1 + "_map"))
                                        text renpy.translate_string("{b}Wear:{/b} ") + str(getattr(store, a_menu_1 + "_wear"))
                                        text renpy.translate_string("{b}Activity:{/b} ") + str(getattr(store, a_menu_1 + "_activity_current")) + ", {b}Since:{/b} " + str(Get_MinuteToClock(getattr(store, a_menu_1 + "_activity_time_start"))) + ", {b}To:{/b} " + str(Get_MinuteToClock(getattr(store, a_menu_1 + "_activity_time_end")))
                                        if persistent.debug == True or perk_int_per >= 2:
                                            text renpy.translate_string("{b}Done List:{/b}\n") + (
                                                "\n".join([
                                                    "{color=#64AFFF}* " + (
                                                        str(item["name"]) if isinstance(item["name"], str)
                                                        else str(item["name"][0]) if isinstance(item["name"], tuple)
                                                        else str(item["name"])
                                                    ) + " (ended: " + str(Get_MinuteToClock(item["end_time"])) + "){/color}"
                                                    if item["source"] is not None
                                                    else "{color=#64FF64}* " + (
                                                        str(item["name"]) if isinstance(item["name"], str)
                                                        else str(item["name"][0]) if isinstance(item["name"], tuple)
                                                        else str(item["name"])
                                                    ) + " (ended: " + str(Get_MinuteToClock(item["end_time"])) + "){/color}"
                                                    for item in getattr(store, a_menu_1 + "_activity_list_done")
                                                ]) if getattr(store, a_menu_1 + "_activity_list_done") else "Empty"
                                            )
                                        if persistent.debug == True or perk_int_per >= 3:
                                            text renpy.translate_string("{b}To Do:{/b}\n") + (
                                                "\n".join([
                                                    "{color=#64AFFF}* " + (
                                                        str(item["name"]) if isinstance(item["name"], str)
                                                        else str(item["name"][0]) if isinstance(item["name"], tuple)
                                                        else str(item["name"])
                                                    ) + " (" + str(item["duration"]) + " min){/color}"
                                                    if item["source"] is not None
                                                    else "{color=#64FF64}* " + (
                                                        str(item["name"]) if isinstance(item["name"], str)
                                                        else str(item["name"][0]) if isinstance(item["name"], tuple)
                                                        else str(item["name"])
                                                    ) + " (" + str(item["duration"]) + " min){/color}"
                                                    for item in getattr(store, a_menu_1 + "_activity_list_queue")
                                                ]) if getattr(store, a_menu_1 + "_activity_list_queue") else "Empty"
                                            )
                                vbar value YScrollValue("Scroll_Schedule")

screen UI_Menu_Options_Skill():
    hbox:
        #xpos 100
        frame:
            background None
            xpadding 0
            ypadding 0
            xsize 620
            ysize 1080
            add AlphaMask(
                Fixed(
                    Transform(Cell_Img(cellbg[a_menu_3]),
                        zoom = Cell_WZoom(cellbg[a_menu_3], cellwz),
                        xalign = (cellwx/100),
                        yalign = (cellwy/100)),
                        xysize=(620, 1080)  # Size of the masked area
                ),
                "images/UI/CellphoneBG/Menu_Mask_2.webp"
            )

            label renpy.translate_string("Select a Skill") xalign 0.5 yalign 0.3
            side ("c l"):
                area (-50, 0, 620, 490)
                xalign 0.5 yalign 0.65 xoffset 50
                vpgrid id "Scroll_Skill":
                    draggable True mousewheel True cols 3 xalign 0.5 yalign 0.5 spacing 20 xoffset -50

                    # ----------------------------------------------------------------------------------------------------
                    # PHYSICS TALENT
                    # ----------------------------------------------------------------------------------------------------
                    frame:                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_phy_str >= 1:
                                idle "images/UI/Talent/TalentBG_PHY ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_PHY OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_phy_str")
                        image "images/UI/Talent/TalentICON STR.webp"
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_phy_agi >= 1:
                                idle "images/UI/Talent/TalentBG_PHY ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_PHY OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_phy_agi")
                        image "images/UI/Talent/TalentICON AGI.webp"
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_phy_res >= 1:
                                idle "images/UI/Talent/TalentBG_PHY ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_PHY OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_phy_res")
                        image "images/UI/Talent/TalentICON RES.webp"
                    # ----------------------------------------------------------------------------------------------------
                    # INTELLIGENCE TALENT
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_int_per >= 1:
                                idle "images/UI/Talent/TalentBG_INT ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_INT OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_int_per")
                        image "images/UI/Talent/TalentICON OBS.webp"
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_int_mem >= 1:
                                idle "images/UI/Talent/TalentBG_INT ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_INT OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_int_mem")
                        image "images/UI/Talent/TalentICON KNW.webp"
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_int_log >= 1:
                                idle "images/UI/Talent/TalentBG_INT ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_INT OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_int_log")
                        image "images/UI/Talent/TalentICON SNS.webp"
                    # ----------------------------------------------------------------------------------------------------
                    # CHARISMA TALENT
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_cha_sex >= 1:
                                idle "images/UI/Talent/TalentBG_CHA ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_CHA OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_cha_sex")
                        image "images/UI/Talent/TalentICON SEX.webp"
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_cha_per >= 1:
                                idle "images/UI/Talent/TalentBG_CHA ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_CHA OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_cha_per")
                        image "images/UI/Talent/TalentICON PRF.webp"
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_cha_soc >= 1:
                                idle "images/UI/Talent/TalentBG_CHA ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_CHA OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_cha_soc")
                        image "images/UI/Talent/TalentICON CRM.webp"
                    # ----------------------------------------------------------------------------------------------------
                    # SKILL
                    # ----------------------------------------------------------------------------------------------------
                    if 0 > 1: # Disable
                        frame:
                            
                            xsize 150
                            ysize 150
                            xpadding 0
                            ypadding 0
                            imagebutton:
                                if perk_skl_dnc >= 1:
                                    idle "images/UI/Talent/TalentBG_SKL ON.webp"
                                else:
                                    idle "images/UI/Talent/TalentBG_SKL OFF.webp"
                                hover "images/UI/Talent/TalentBG ON.webp"
                                action SetVariable("a_menu_2", "perk_skl_dnc")
                            image "images/UI/Talent/TalentICON DNC.webp"
                    # ----------------------------------------------------------------------------------------------------
                    if 0 > 1: # Disable
                        frame:
                            
                            xsize 150
                            ysize 150
                            xpadding 0
                            ypadding 0
                            imagebutton:
                                if perk_skl_gui >= 1:
                                    idle "images/UI/Talent/TalentBG_SKL ON.webp"
                                else:
                                    idle "images/UI/Talent/TalentBG_SKL OFF.webp"
                                hover "images/UI/Talent/TalentBG ON.webp"
                                action SetVariable("a_menu_2", "perk_skl_gui")
                            image "images/UI/Talent/TalentICON GUI.webp"
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_skl_swm >= 1:
                                idle "images/UI/Talent/TalentBG_SKL ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_SKL OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_skl_swm")
                        image "images/UI/Talent/TalentICON SWM.webp"
                    # ----------------------------------------------------------------------------------------------------
                    if 0 > 1: # Disable
                        frame:
                            
                            xsize 150
                            ysize 150
                            xpadding 0
                            ypadding 0
                            imagebutton:
                                if perk_skl_msg >= 1:
                                    idle "images/UI/Talent/TalentBG_SKL ON.webp"
                                else:
                                    idle "images/UI/Talent/TalentBG_SKL OFF.webp"
                                hover "images/UI/Talent/TalentBG ON.webp"
                                action SetVariable("a_menu_2", "perk_skl_msg")
                            image "images/UI/Talent/TalentICON MSG.webp"
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_skl_cok >= 1:
                                idle "images/UI/Talent/TalentBG_SKL ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_SKL OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_skl_cok")
                        image "images/UI/Talent/TalentICON COK.webp"
                    # ----------------------------------------------------------------------------------------------------
                    frame:
                        
                        xsize 150
                        ysize 150
                        xpadding 0
                        ypadding 0
                        imagebutton:
                            if perk_skl_tut >= 1:
                                idle "images/UI/Talent/TalentBG_SKL ON.webp"
                            else:
                                idle "images/UI/Talent/TalentBG_SKL OFF.webp"
                            hover "images/UI/Talent/TalentBG ON.webp"
                            action SetVariable("a_menu_2", "perk_skl_tut")
                        image "images/UI/Talent/TalentICON TUT.webp"
                    # ----------------------------------------------------------------------------------------------------
                vbar value YScrollValue("Scroll_Skill")

            add "images/UI/CellphoneBG/Menu_MG_1.webp"
            add "images/UI/CellphoneBG/Menu_FG.webp"
            hbox:
                xalign 0.5
                yalign 0.9
                spacing 50
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomTriangle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomTriangle HOVER.webp"
                    action Jump("UI_Menu_Options_Triangle")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomCircle IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomCircle HOVER.webp"
                    action Jump("show_ui")
                imagebutton:
                    idle "images/UI/SUBMENU_Option_BottomSquare IDLE.webp"
                    hover "images/UI/SUBMENU_Option_BottomSquare HOVER.webp"
                    action Jump("show_ui")

        frame:
            xsize 1200
            ysize 1080
            xpadding 30
            ypadding 30
            xalign 0.0
            yalign 0.0
            vbox:
                spacing 25
                label renpy.translate_string("Talents") xalign 0.5
                text renpy.translate_string("{b}Level:{/b} [lvl], {b}Experience:{/b} [xp_now], {b}Perks:{/b} [perk]")
                bar value xp_now range xp_max

                if a_menu_2 == "perk_phy_str":
                    if perk_phy_str == 0 and perk >= 1 and stat_phy_str >= 5:
                        label renpy.translate_string("Strength")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_phy_str", 1), SetVariable("perk", perk-1)]
                    elif perk_phy_str == 1 and perk >= 2 and stat_phy_str >= 20:
                        label renpy.translate_string("Strength (LVL 1)")
                        textbutton renpy.translate_string("Spend 2 Points") action [SetVariable("perk_phy_str", 2), SetVariable("perk", perk-2)]
                    elif perk_phy_str == 2 and perk >= 3 and stat_phy_str >= 80:
                        label renpy.translate_string("Strength (LVL 2)")
                        textbutton renpy.translate_string("Spend 3 Points") action [SetVariable("perk_phy_str", 3), SetVariable("perk", perk-3)]
                    elif perk_phy_str == 3:
                        label renpy.translate_string("Strength (LVL 3)")
                        textbutton renpy.translate_string("[C_Pos]Complete[C_Off]") action None
                    else:
                        if perk_phy_str > 0:
                            label renpy.translate_string("Strength (LVL [perk_phy_str])")
                        if perk_phy_str == 0:
                            label renpy.translate_string("Strength")
                            textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None
                        if perk_phy_str == 1:
                            textbutton renpy.translate_string("[C_Mnd]Spend 2 Points[C_Off]") action None
                        if perk_phy_str == 2:
                            textbutton renpy.translate_string("[C_Mnd]Spend 3 Points[C_Off]") action None

                if a_menu_2 == "perk_phy_agi":
                    if 1 < 0:
                        label renpy.translate_string("Agility")
                        textbutton renpy.translate_string("[C_Mnd]Unavailable[C_Off]") action None
                    elif perk_phy_agi == 0 and perk >= 1 and stat_phy_agi >= 5:
                        label renpy.translate_string("Agility")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_phy_agi", 1), SetVariable("perk", perk-1)]
                    elif perk_phy_agi == 1 and perk >= 2 and stat_phy_agi >= 20:
                        label renpy.translate_string("Agility (LVL 1)")
                        textbutton renpy.translate_string("Spend 2 Points") action [SetVariable("perk_phy_agi", 2), SetVariable("perk", perk-2)]
                    elif perk_phy_agi == 2 and perk >= 3 and stat_phy_agi >= 80:
                        label renpy.translate_string("Agility (LVL 2)")
                        textbutton renpy.translate_string("Spend 3 Points") action [SetVariable("perk_phy_agi", 3), SetVariable("perk", perk-3)]
                    elif perk_phy_agi == 3:
                        label renpy.translate_string("Agility (LVL 3)")
                        textbutton renpy.translate_string("[C_Pos]Complete[C_Off]") action None
                    else:
                        if perk_phy_agi > 0:
                            label renpy.translate_string("Agility (LVL [perk_phy_agi])")
                        if perk_phy_agi == 0:
                            label renpy.translate_string("Agility")
                            textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None
                        if perk_phy_agi == 1:
                            textbutton renpy.translate_string("[C_Mnd]Spend 2 Points[C_Off]") action None
                        if perk_phy_agi == 2:
                            textbutton renpy.translate_string("[C_Mnd]Spend 3 Points[C_Off]") action None

                if a_menu_2 == "perk_phy_res":
                    if 1 < 0:
                        label renpy.translate_string("Endurance")
                        textbutton renpy.translate_string("[C_Mnd]Unavailable[C_Off]") action None
                    elif perk_phy_res == 0 and perk >= 1 and stat_phy_res >= 5:
                        label renpy.translate_string("Endurance")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_phy_res", 1), SetVariable("perk", perk-1)]
                    elif perk_phy_res == 1 and perk >= 2 and stat_phy_res >= 20:
                        label renpy.translate_string("Endurance (LVL 1)")
                        textbutton renpy.translate_string("Spend 2 Points") action [SetVariable("perk_phy_res", 2), SetVariable("perk", perk-2)]
                    elif perk_phy_res == 2 and perk >= 3 and stat_phy_res >= 80:
                        label renpy.translate_string("Endurance (LVL 2)")
                        textbutton renpy.translate_string("Spend 3 Points") action [SetVariable("perk_phy_res", 3), SetVariable("perk", perk-3)]
                    elif perk_phy_res == 3:
                        label renpy.translate_string("Endurance (LVL 3)")
                        textbutton renpy.translate_string("[C_Pos]Complete[C_Off]") action None
                    else:
                        if perk_phy_res > 0:
                            label renpy.translate_string("Endurance (LVL [perk_phy_res])")
                        if perk_phy_res == 0:
                            label renpy.translate_string("Endurance")
                            textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None
                        if perk_phy_res == 1:
                            textbutton renpy.translate_string("[C_Mnd]Spend 2 Points[C_Off]") action None
                        if perk_phy_res == 2:
                            textbutton renpy.translate_string("[C_Mnd]Spend 3 Points[C_Off]") action None

                if a_menu_2 == "perk_int_per":
                    if perk_int_per == 0 and perk >= 1 and stat_int_per >= 5:
                        label renpy.translate_string("Perception")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_int_per", 1), SetVariable("perk", perk-1)]
                    elif perk_int_per == 1 and perk >= 2 and stat_int_per >= 20:
                        label renpy.translate_string("Perception (LVL 1)")
                        textbutton renpy.translate_string("Spend 2 Points") action [SetVariable("perk_int_per", 2), SetVariable("perk", perk-2)]
                    elif perk_int_per == 2 and perk >= 3 and stat_int_per >= 80:
                        label renpy.translate_string("Perception (LVL 2)")
                        textbutton renpy.translate_string("Spend 3 Points") action [SetVariable("perk_int_per", 3), SetVariable("perk", perk-3)]
                    elif perk_int_per == 3:
                        label renpy.translate_string("Perception (LVL 3)")
                        textbutton renpy.translate_string("[C_Pos]Complete[C_Off]") action None
                    else:
                        if perk_int_per > 0:
                            label renpy.translate_string("Perception (LVL [perk_int_per])")
                        if perk_int_per == 0:
                            label renpy.translate_string("Perception")
                            textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None
                        if perk_int_per == 1:
                            textbutton renpy.translate_string("[C_Mnd]Spend 2 Points[C_Off]") action None
                        if perk_int_per == 2:
                            textbutton renpy.translate_string("[C_Mnd]Spend 3 Points[C_Off]") action None

                if a_menu_2 == "perk_int_mem":
                    if perk_int_mem == 0 and perk >= 1 and stat_int_mem >= 5:
                        label renpy.translate_string("Knowledge")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_int_mem", 1), SetVariable("perk", perk-1)]
                    elif perk_int_mem == 1 and perk >= 2 and stat_int_mem >= 20:
                        label renpy.translate_string("Knowledge (LVL 1)")
                        textbutton renpy.translate_string("Spend 2 Points") action [SetVariable("perk_int_mem", 2), SetVariable("perk", perk-2)]
                    elif perk_int_mem == 2 and perk >= 3 and stat_int_mem >= 80:
                        label renpy.translate_string("Knowledge (LVL 2)")
                        textbutton renpy.translate_string("Spend 3 Points") action [SetVariable("perk_int_mem", 3), SetVariable("perk", perk-3)]
                    elif perk_int_mem == 3:
                        label renpy.translate_string("Knowledge (LVL 3)")
                        textbutton renpy.translate_string("[C_Pos]Complete[C_Off]") action None
                    else:
                        if perk_int_mem > 0:
                            label renpy.translate_string("Knowledge (LVL [perk_int_mem])")
                        if perk_int_mem == 0:
                            label renpy.translate_string("Knowledge")
                            textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None
                        if perk_int_mem == 1:
                            textbutton renpy.translate_string("[C_Mnd]Spend 2 Points[C_Off]") action None
                        if perk_int_mem == 2:
                            textbutton renpy.translate_string("[C_Mnd]Spend 3 Points[C_Off]") action None

                if a_menu_2 == "perk_int_log":
                    if 1 < 0:
                        label renpy.translate_string("Logic")
                        textbutton renpy.translate_string("[C_Mnd]Unavailable[C_Off]") action None
                    elif perk_int_log == 0 and perk >= 1 and stat_int_log >= 5:
                        label renpy.translate_string("Logic")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_int_log", 1), SetVariable("perk", perk-1)]
                    elif perk_int_log == 1 and perk >= 2 and stat_int_log >= 20:
                        label renpy.translate_string("Logic (LVL 1)")
                        textbutton renpy.translate_string("Spend 2 Points") action [SetVariable("perk_int_log", 2), SetVariable("perk", perk-2)]
                    elif perk_int_log == 2 and perk >= 3 and stat_int_log >= 80:
                        label renpy.translate_string("Logic (LVL 2)")
                        textbutton renpy.translate_string("Spend 3 Points") action [SetVariable("perk_int_log", 3), SetVariable("perk", perk-3)]
                    elif perk_int_log == 3:
                        label renpy.translate_string("Logic (LVL 3)")
                        textbutton renpy.translate_string("[C_Pos]Complete[C_Off]") action None
                    else:
                        if perk_int_log > 0:
                            label renpy.translate_string("Logic (LVL [perk_int_log])")
                        if perk_int_log == 0:
                            label renpy.translate_string("Logic")
                            textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None
                        if perk_int_log == 1:
                            textbutton renpy.translate_string("[C_Mnd]Spend 2 Points[C_Off]") action None
                        if perk_int_log == 2:
                            textbutton renpy.translate_string("[C_Mnd]Spend 3 Points[C_Off]") action None

                if a_menu_2 == "perk_cha_sex":
                    if perk_cha_sex == 0 and perk >= 1 and stat_cha_sex >= 5:
                        label renpy.translate_string("Sensuality")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_cha_sex", 1), SetVariable("perk", perk-1)]
                    elif perk_cha_sex == 1 and perk >= 2 and stat_cha_sex >= 20:
                        label renpy.translate_string("Sensuality (LVL 1)")
                        textbutton renpy.translate_string("Spend 2 Points") action [SetVariable("perk_cha_sex", 2), SetVariable("perk", perk-2)]
                    elif perk_cha_sex == 2 and perk >= 3 and stat_cha_sex >= 80:
                        label renpy.translate_string("Sensuality (LVL 2)")
                        textbutton renpy.translate_string("Spend 3 Points") action [SetVariable("perk_cha_sex", 3), SetVariable("perk", perk-3)]
                    elif perk_cha_sex == 3:
                        label renpy.translate_string("Sensuality (LVL 3)")
                        textbutton renpy.translate_string("[C_Pos]Complete[C_Off]") action None
                    else:
                        if perk_cha_sex > 0:
                            label renpy.translate_string("Sensuality (LVL [perk_cha_sex])")
                        if perk_cha_sex == 0:
                            label renpy.translate_string("Sensuality")
                            textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None
                        if perk_cha_sex == 1:
                            textbutton renpy.translate_string("[C_Mnd]Spend 2 Points[C_Off]") action None
                        if perk_cha_sex == 2:
                            textbutton renpy.translate_string("[C_Mnd]Spend 3 Points[C_Off]") action None

                if a_menu_2 == "perk_cha_per":
                    if perk_cha_per == 0 and perk >= 1 and stat_cha_per >= 5:
                        label renpy.translate_string("Performance")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_cha_per", 1), SetVariable("perk", perk-1)]
                    elif perk_cha_per == 1 and perk >= 2 and stat_cha_per >= 20:
                        label renpy.translate_string("Performance (LVL 1)")
                        textbutton renpy.translate_string("Spend 2 Points") action [SetVariable("perk_cha_per", 2), SetVariable("perk", perk-2)]
                    elif perk_cha_per == 2 and perk >= 3 and stat_cha_per >= 80:
                        label renpy.translate_string("Performance (LVL 2)")
                        textbutton renpy.translate_string("Spend 3 Points") action [SetVariable("perk_cha_per", 3), SetVariable("perk", perk-3)]
                    elif perk_cha_per == 3:
                        label renpy.translate_string("Performance (LVL 3)")
                        textbutton renpy.translate_string("[C_Pos]Complete[C_Off]") action None
                    else:
                        if perk_cha_per > 0:
                            label renpy.translate_string("Performance (LVL [perk_cha_per])")
                        if perk_cha_per == 0:
                            label renpy.translate_string("Performance")
                            textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None
                        if perk_cha_per == 1:
                            textbutton renpy.translate_string("[C_Mnd]Spend 2 Points[C_Off]") action None
                        if perk_cha_per == 2:
                            textbutton renpy.translate_string("[C_Mnd]Spend 3 Points[C_Off]") action None

                if a_menu_2 == "perk_cha_soc":
                    if 1 < 0:
                        label renpy.translate_string("Social")
                        textbutton renpy.translate_string("[C_Mnd]Unavailable[C_Off]") action None
                    elif perk_cha_soc == 0 and perk >= 1 and stat_cha_soc >= 5:
                        label renpy.translate_string("Social")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_cha_soc", 1), SetVariable("perk", perk-1)]
                    elif perk_cha_soc == 1 and perk >= 2 and stat_cha_soc >= 20:
                        label renpy.translate_string("Social (LVL 1)")
                        textbutton renpy.translate_string("Spend 2 Points") action [SetVariable("perk_cha_soc", 2), SetVariable("perk", perk-2)]
                    elif perk_cha_soc == 2 and perk >= 3 and stat_cha_soc >= 80:
                        label renpy.translate_string("Social (LVL 2)")
                        textbutton renpy.translate_string("Spend 3 Points") action [SetVariable("perk_cha_soc", 3), SetVariable("perk", perk-3)]
                    elif perk_cha_soc == 3:
                        label renpy.translate_string("Social (LVL 3)")
                        textbutton renpy.translate_string("[C_Pos]Complete[C_Off]") action None
                    else:
                        if perk_cha_soc > 0:
                            label renpy.translate_string("Social (LVL [perk_cha_soc])")
                        if perk_cha_soc == 0:
                            label renpy.translate_string("Social")
                            textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None
                        if perk_cha_soc == 1:
                            textbutton renpy.translate_string("[C_Mnd]Spend 2 Points[C_Off]") action None
                        if perk_cha_soc == 2:
                            textbutton renpy.translate_string("[C_Mnd]Spend 3 Points[C_Off]") action None

                if a_menu_2 == "perk_skl_dnc":
                    if 1 > 0:
                        label renpy.translate_string("Dance")
                        textbutton renpy.translate_string("[C_Mnd]Unavailable[C_Off]") action None
                    elif perk_skl_dnc == 0 and perk >= 1 and stat_cha >= 10:
                        label renpy.translate_string("Dance")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_skl_dnc", 1), SetVariable("perk", perk-1)]
                    elif perk_skl_dnc >= 1:
                        label renpy.translate_string("Dance (LVL 1)")
                        textbutton renpy.translate_string("[C_Pos]Skill Learned[C_Off]") action None
                    else:
                        label renpy.translate_string("Dance (LVL [perk_skl_dnc])")
                        textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None

                if a_menu_2 == "perk_skl_gui":
                    if 1 > 0:
                        label renpy.translate_string("Guitar")
                        textbutton renpy.translate_string("[C_Mnd]Unavailable[C_Off]") action None
                    elif perk_skl_gui == 0 and perk >= 1 and stat_int >= 10:
                        label renpy.translate_string("Guitar")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_skl_gui", 1), SetVariable("perk", perk-1)]
                    elif perk_skl_gui >= 1:
                        label renpy.translate_string("Guitar (LVL 1)")
                        textbutton renpy.translate_string("[C_Pos]Skill Learned[C_Off]") action None
                    else:
                        label renpy.translate_string("Guitar (LVL [perk_skl_gui])")
                        textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None

                if a_menu_2 == "perk_skl_swm":
                    if perk_skl_swm == 0 and perk >= 1 and stat_phy >= 10:
                        label renpy.translate_string("Swimming")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_skl_swm", 1), SetVariable("perk", perk-1)]
                    elif perk_skl_swm >= 1:
                        label renpy.translate_string("Swimming (LVL 1)")
                        textbutton renpy.translate_string("[C_Pos]Skill Learned[C_Off]") action None
                    else:
                        label renpy.translate_string("Swimming (LVL [perk_skl_swm])")
                        textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None

                if a_menu_2 == "perk_skl_msg":
                    if 1 > 0:
                        label renpy.translate_string("Massaging")
                        textbutton renpy.translate_string("[C_Mnd]Unavailable[C_Off]") action None
                    elif perk_skl_msg == 0 and perk >= 1 and stat_cha >= 10:
                        label renpy.translate_string("Massaging")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_skl_msg", 1), SetVariable("perk", perk-1)]
                    elif perk_skl_msg >= 1:
                        label renpy.translate_string("Massaging (LVL 1)")
                        textbutton renpy.translate_string("[C_Pos]Skill Learned[C_Off]") action None
                    else:
                        label renpy.translate_string("Massaging (LVL [perk_skl_msg])")
                        textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None

                if a_menu_2 == "perk_skl_cok":
                    if 1 < 0:
                        label renpy.translate_string("Cooking")
                        textbutton renpy.translate_string("[C_Mnd]Unavailable[C_Off]") action None
                    elif perk_skl_cok == 0 and perk >= 1 and stat_int >= 10:
                        label renpy.translate_string("Cooking")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_skl_cok", 1), SetVariable("perk", perk-1)]
                    elif perk_skl_cok >= 1:
                        label renpy.translate_string("Cooking (LVL 1)")
                        textbutton renpy.translate_string("[C_Pos]Skill Learned[C_Off]") action None
                    else:
                        label renpy.translate_string("Cooking (LVL [perk_skl_cok])")
                        textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None

                if a_menu_2 == "perk_skl_tut":
                    if perk_skl_tut == 0 and perk >= 1 and stat_cha >= 5 and stat_int >= 5:
                        label renpy.translate_string("Tutoring")
                        textbutton renpy.translate_string("Spend 1 Point") action [SetVariable("perk_skl_tut", 1), SetVariable("perk", perk-1)]
                    elif perk_skl_tut >= 1:
                        label renpy.translate_string("Tutoring (LVL 1)")
                        textbutton renpy.translate_string("[C_Pos]Skill Learned[C_Off]") action None
                    else:
                        label renpy.translate_string("Tutoring (LVL [perk_skl_tut])")
                        textbutton renpy.translate_string("[C_Mnd]Spend 1 Point[C_Off]") action None

                side ("c l"):
                    area (0, 0, 1100, 680)
                    viewport id "ScrollDatabase":
                        xoffset 25
                        draggable True mousewheel True
                        vbox:
                            if a_menu_2 == "perk_phy_str":
                                text renpy.translate_string("Improves your performance when carrying girls and heavier items; increases your damage in fights [C_Mnd](when available)[C_Off]. [C_Dat]You can carry ") + str(round((20 + ((3 + (perk_phy_str * 2)) * (3 + (perk_phy_str * 2)))) * (1 + (stat_phy * 0.01)), 2)) + "kg[C_Off]."
                                if perk_phy_str >= 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 5 STR")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_phy_str >= 5:
                                        text renpy.translate_string("{p}✅ 5 STR")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 STR")

                                if perk_phy_str >= 2:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 2 Perk{p}✅ 20 STR")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}Requires:")
                                    if perk >= 2:
                                        text renpy.translate_string("{p}✅ 2 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 2 Perk")
                                    if stat_phy_str >= 20:
                                        text renpy.translate_string("{p}✅ 20 STR")
                                    else:
                                        text renpy.translate_string("{p}❌ 20 STR")

                                if perk_phy_str == 3:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 3 Perk{p}✅ 80 STR")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}Requires:")
                                    if perk >= 3:
                                        text renpy.translate_string("{p}✅ 3 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 3 Perk")
                                    if stat_phy_str >= 80:
                                        text renpy.translate_string("{p}✅ 80 STR")
                                    else:
                                        text renpy.translate_string("{p}❌ 80 STR")

                            if a_menu_2 == "perk_phy_agi":
                                text renpy.translate_string("Improves your speed performance. Spend less time when use fast travel. Time passes slower in agility minigames.")
                                if perk_phy_agi >= 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 5 AGI")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_phy_agi >= 5:
                                        text renpy.translate_string("{p}✅ 5 AGI")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 AGI")

                                if perk_phy_agi >= 2:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 2 Perk{p}✅ 20 AGI")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}Requires:")
                                    if perk >= 2:
                                        text renpy.translate_string("{p}✅ 2 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 2 Perk")
                                    if stat_phy_agi >= 20:
                                        text renpy.translate_string("{p}✅ 20 AGI")
                                    else:
                                        text renpy.translate_string("{p}❌ 20 AGI")

                                if perk_phy_agi == 3:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 3 Perk{p}✅ 80 AGI")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}Requires:")
                                    if perk >= 3:
                                        text renpy.translate_string("{p}✅ 3 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 3 Perk")
                                    if stat_phy_agi >= 80:
                                        text renpy.translate_string("{p}✅ 80 AGI")
                                    else:
                                        text renpy.translate_string("{p}❌ 80 AGI")

                            if a_menu_2 == "perk_phy_res":
                                text renpy.translate_string("Increases your stamina and ability to perform physical activities for longer periods, and increase your resistance in fights.")
                                if perk_phy_res >= 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 5 RES")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_phy_res >= 5:
                                        text renpy.translate_string("{p}✅ 5 RES")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 RES")

                                if perk_phy_res >= 2:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 2 Perk{p}✅ 20 RES")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}Requires:")
                                    if perk >= 2:
                                        text renpy.translate_string("{p}✅ 2 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 2 Perk")
                                    if stat_phy_res >= 20:
                                        text renpy.translate_string("{p}✅ 20 RES")
                                    else:
                                        text renpy.translate_string("{p}❌ 20 RES")

                                if perk_phy_res == 3:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 3 Perk{p}✅ 80 RES")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}Requires:")
                                    if perk >= 3:
                                        text renpy.translate_string("{p}✅ 3 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 3 Perk")
                                    if stat_phy_res >= 80:
                                        text renpy.translate_string("{p}✅ 80 RES")
                                    else:
                                        text renpy.translate_string("{p}❌ 80 RES")

                            if a_menu_2 == "perk_int_per":
                                text renpy.translate_string("Enhances your ability to notice hidden scenes and see through characters' words and actions. Reduce chances of you to be caught by surprise in some scenes [C_Mnd](when available)[C_Off]. [C_Dat]You have a ") + str(round(((perk_int_per/3)*100), 2)) + "% chance of noticing hidden things[C_Off]."
                                if perk_int_per >= 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 5 PER")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_int_per >= 5:
                                        text renpy.translate_string("{p}✅ 5 PER")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 PER")

                                if perk_int_per >= 2:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 2 Perk{p}✅ 20 PER")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}Requires:")
                                    if perk >= 2:
                                        text renpy.translate_string("{p}✅ 2 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 2 Perk")
                                    if stat_int_per >= 20:
                                        text renpy.translate_string("{p}✅ 20 PER")
                                    else:
                                        text renpy.translate_string("{p}❌ 20 PER")

                                if perk_int_per == 3:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 3 Perk{p}✅ 80 PER")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}Requires:")
                                    if perk >= 3:
                                        text renpy.translate_string("{p}✅ 3 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 3 Perk")
                                    if stat_int_per >= 80:
                                        text renpy.translate_string("{p}✅ 80 PER")
                                    else:
                                        text renpy.translate_string("{p}❌ 80 PER")

                            if a_menu_2 == "perk_int_mem":
                                text renpy.translate_string("Allows you to have knowledge of general things around you, enhances your ability to remember information and details, and slightly improves your performance in some skills.")
                                if perk_int_mem >= 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 5 MEM")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_int_mem >= 5:
                                        text renpy.translate_string("{p}✅ 5 MEM")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 MEM")

                                if perk_int_mem >= 2:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 2 Perk{p}✅ 20 MEM")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}Requires:")
                                    if perk >= 2:
                                        text renpy.translate_string("{p}✅ 2 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 2 Perk")
                                    if stat_int_mem >= 20:
                                        text renpy.translate_string("{p}✅ 20 MEM")
                                    else:
                                        text renpy.translate_string("{p}❌ 20 MEM")

                                if perk_int_mem == 3:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 3 Perk{p}✅ 80 MEM")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}Requires:")
                                    if perk >= 3:
                                        text renpy.translate_string("{p}✅ 3 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 3 Perk")
                                    if stat_int_mem >= 80:
                                        text renpy.translate_string("{p}✅ 80 MEM")
                                    else:
                                        text renpy.translate_string("{p}❌ 80 MEM")

                            if a_menu_2 == "perk_int_log":
                                text renpy.translate_string("Improves your logical reasoning skills, making it easier to solve complex problems and puzzles, and make better decisions. Time passes slower in thinking minigames.")
                                if perk_int_log >= 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 5 LOG")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_int_log >= 5:
                                        text renpy.translate_string("{p}✅ 5 LOG")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 LOG")

                                if perk_int_log >= 2:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 2 Perk{p}✅ 20 LOG")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}Requires:")
                                    if perk >= 2:
                                        text renpy.translate_string("{p}✅ 2 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 2 Perk")
                                    if stat_int_log >= 20:
                                        text renpy.translate_string("{p}✅ 20 LOG")
                                    else:
                                        text renpy.translate_string("{p}❌ 20 LOG")

                                if perk_int_log == 3:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 3 Perk{p}✅ 80 LOG")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}Requires:")
                                    if perk >= 3:
                                        text renpy.translate_string("{p}✅ 3 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 3 Perk")
                                    if stat_int_log >= 80:
                                        text renpy.translate_string("{p}✅ 80 LOG")
                                    else:
                                        text renpy.translate_string("{p}❌ 80 LOG")

                            if a_menu_2 == "perk_cha_sex":
                                text renpy.translate_string("Increases your attractiveness and the amount of lust generated in the characters. Improve your performance in H scenes. Characters get even hornier by erotic physical contacts with you, and also get horny by common physical contacts with you.")
                                if perk_cha_sex >= 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 5 SEX")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_cha_sex >= 5:
                                        text renpy.translate_string("{p}✅ 5 SEX")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 SEX")

                                if perk_cha_sex >= 2:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 2 Perk{p}✅ 20 SEX")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}Requires:")
                                    if perk >= 2:
                                        text renpy.translate_string("{p}✅ 2 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 2 Perk")
                                    if stat_cha_sex >= 20:
                                        text renpy.translate_string("{p}✅ 20 SEX")
                                    else:
                                        text renpy.translate_string("{p}❌ 20 SEX")

                                if perk_cha_sex == 3:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 3 Perk{p}✅ 80 SEX")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}Requires:")
                                    if perk >= 3:
                                        text renpy.translate_string("{p}✅ 3 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 3 Perk")
                                    if stat_cha_sex >= 80:
                                        text renpy.translate_string("{p}✅ 80 SEX")
                                    else:
                                        text renpy.translate_string("{p}❌ 80 SEX")

                            if a_menu_2 == "perk_cha_per":
                                text renpy.translate_string("Improves your performance in using skills and increases the amount of money received when working.")
                                if perk_cha_per >= 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 5 PER")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_cha_per >= 5:
                                        text renpy.translate_string("{p}✅ 5 PER")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 PER")

                                if perk_cha_per >= 2:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 2 Perk{p}✅ 20 PER")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}Requires:")
                                    if perk >= 2:
                                        text renpy.translate_string("{p}✅ 2 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 2 Perk")
                                    if stat_cha_per >= 20:
                                        text renpy.translate_string("{p}✅ 20 PER")
                                    else:
                                        text renpy.translate_string("{p}❌ 20 PER")

                                if perk_cha_per == 3:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 3 Perk{p}✅ 80 PER")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}Requires:")
                                    if perk >= 3:
                                        text renpy.translate_string("{p}✅ 3 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 3 Perk")
                                    if stat_cha_per >= 80:
                                        text renpy.translate_string("{p}✅ 80 PER")
                                    else:
                                        text renpy.translate_string("{p}❌ 80 PER")

                            if a_menu_2 == "perk_cha_soc":
                                text renpy.translate_string("Increases your performance in character interactions.")
                                if perk_cha_soc >= 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 5 SOC")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_cha_soc >= 5:
                                        text renpy.translate_string("{p}✅ 5 SOC")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 SOC")

                                if perk_cha_soc >= 2:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 2 Perk{p}✅ 80 SOC")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 2{/b}{p}Requires:")
                                    if perk >= 2:
                                        text renpy.translate_string("{p}✅ 2 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 2 Perk")
                                    if stat_cha_soc >= 20:
                                        text renpy.translate_string("{p}✅ 20 SOC")
                                    else:
                                        text renpy.translate_string("{p}❌ 20 SOC")

                                if perk_cha_soc == 3:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 3 Perk{p}✅ 80 SOC")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 3{/b}{p}Requires:")
                                    if perk >= 3:
                                        text renpy.translate_string("{p}✅ 3 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 3 Perk")
                                    if stat_cha_soc >= 80:
                                        text renpy.translate_string("{p}✅ 80 SOC")
                                    else:
                                        text renpy.translate_string("{p}❌ 80 SOC")

                            if a_menu_2 == "perk_skl_dnc":
                                text renpy.translate_string("Allows you to dance in a rhythm minigame.")
                                if perk_skl_dnc == 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 10 CHA")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_cha >= 10:
                                        text renpy.translate_string("{p}✅ 10 CHA")
                                    else:
                                        text renpy.translate_string("{p}❌ 10 CHA")

                            if a_menu_2 == "perk_skl_gui":
                                text renpy.translate_string("Allows you to play guitar in a rhythm minigame.")
                                if perk_skl_gui == 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 10 INT")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_int >= 10:
                                        text renpy.translate_string("{p}✅ 10 INT")
                                    else:
                                        text renpy.translate_string("{p}❌ 10 INT")

                            if a_menu_2 == "perk_skl_swm":
                                text renpy.translate_string("Allows you to swim in scenes and minigames [C_Mnd](when available)[C_Off].")
                                if perk_skl_swm == 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 10 PHY")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_phy >= 10:
                                        text renpy.translate_string("{p}✅ 10 PHY")
                                    else:
                                        text renpy.translate_string("{p}❌ 10 PHY")

                            if a_menu_2 == "perk_skl_msg":
                                text renpy.translate_string("Allows you to massage characters.")
                                if perk_skl_msg == 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 10 CHA")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_cha >= 10:
                                        text renpy.translate_string("{p}✅ 10 CHA")
                                    else:
                                        text renpy.translate_string("{p}❌ 10 CHA")

                            if a_menu_2 == "perk_skl_cok":
                                text renpy.translate_string("Increases your performance in cooking, leaving its minigames easier.")
                                if perk_skl_cok == 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 10 INT")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_int >= 10:
                                        text renpy.translate_string("{p}✅ 10 INT")
                                    else:
                                        text renpy.translate_string("{p}❌ 10 INT")

                            if a_menu_2 == "perk_skl_tut":
                                text renpy.translate_string("Allows you to teach a skill you know.")
                                if perk_skl_tut == 1:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}[C_Pos]Adquired[C_Off]:{p}✅ 1 Perk{p}✅ 5 CHA{p}✅ 5 INT")
                                else:
                                    text renpy.translate_string("{p}{b}LVL 1{/b}{p}Requires:")
                                    if perk >= 1:
                                        text renpy.translate_string("{p}✅ 1 Perk")
                                    else:
                                        text renpy.translate_string("{p}❌ 1 Perk")
                                    if stat_cha >= 5:
                                        text renpy.translate_string("{p}✅ 5 CHA")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 CHA")
                                    if stat_int >= 5:
                                        text renpy.translate_string("{p}✅ 5 INT")
                                    else:
                                        text renpy.translate_string("{p}❌ 5 INT")
                    vbar value YScrollValue("ScrollDatabase")
