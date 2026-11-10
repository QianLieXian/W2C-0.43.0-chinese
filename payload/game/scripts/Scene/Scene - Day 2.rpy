#---------------------------------------------------------------------------
label schoolday_1_0: # Entering in school
#---------------------------------------------------------------------------
    
    stop BGM fadeout 3
    scene bg_0
    with Dissolve(2)
    pause(1)

    play BGM "audio/W2C - Tranquility.mp3"

    if gametimeday == 2:

        $ hero_wear = "school"
        $ wsis_wear = "school"
        $ wnei_wear = "school"

        $ X_spd = 30
        $ X_pos = 2600
        scene bg_street
        show HERO at X
        $ X_pos = 2120
        show WSIS at X
        show WNEI at OR
        with Dissolve(1)

        show HERO at LC_X
        show WSIS at LL_X

        $ wsis_mood = "A1"
        hero "Don't you use to walk to school with {nm}[fnamewnei]{/nm}?"
        wsis "No{w=[wt1]}, she always oversleeps.{w=[wt2]} When her father goes to work he takes the time to drive her to school.{w=[wt2]} Well{w=[wt1]}, at least it was like that until last year{w=[wt1]}, when we studied in another school block."
        hero "So that's a school divided in different places?"
        wsis "Yes{w=[wt2]}, we left the Elementary School and are now entering High School{w=[wt2]}, whose buildings are separated.{w=[wt3]} Educational institutions usually prefer to separate students with different ages into different places{w=[wt2]}, especially after that law was passed a few years ago."
        hero "Hm?{w=[wt2]} What law?"
        $ wsis_mood = "O3"
        wsis "Oh{w=[wt1]}, God!{w=[wt2]} You don't really understand anything!!!{w}{nw}"
        $ wsis_mood = "O2"
        wsis "Oh{w=[wt1]}, God!{w=[wt2]} You don't really understand anything!!!{fast} It's the{w=[wt1]}-{w=[wt1]}{nw}"
        wnei "{bt}HEEEY!!!{/bt}{w=[wt4]}{nw}"

        show WNEI at CC_slow

        wnei "{bt}HEEEY!!!{/bt}{fast} Wait for me!!!"

        $ hero_mood = "A1"
        hero "Hey, {nm}[fnamewnei]{/nm}!"
        wsis "I thought your father would drive you to school when he goes to work."
        $ wnei_mood = "A4"
        wnei "{lg}Shi Hi Hi Hi...{/lg}{w=[wt2]} I woke up earlier today to walk with ya guys!"
        show WSIS at OL_slow
        $ wsis_mood = "A1"
        $ wsis_fx = 1
        wsis "Then, Hurry up!"
        $ wnei_mood = "O2"
        wnei "{pa}Ehhh!?{/pa}{w=[wt2]}{nw}"
        $ hero_mood = "O1"
        $ X_spd = 1
        show WNEI at OL_X
        wnei "{pa}Ehhh!?{/pa}{fast} Where's my welcum hug!?"
        wsis "Oh, no!{w=[wt1]} Stop throwing yourself on me!{w=[wt2]} Don't you see {nm}[fnamehero]{/nm} is looking at all your panties?{w=[wt2]}{nw}"
        $ hero_fx = 1
        wsis "Oh, no!{w=[wt1]} Stop throwing yourself on me!{w=[wt2]} Don't you see {nm}[fnamehero]{/nm} is looking at all your panties?{fast} Get out!"
        wnei "Only if you hug me!"
        wsis "{bt}Here... Here...{/bt}"
        wnei "{nm}[fnamehero]{/nm} didn't give me a welcum hug yet!"
        $ hero_fx = 2
        with dissolve
        show HERO at OL_slow
        hero "{aw}I{w=[wt1]}-I'm g{w=[wt1]}-going...{/aw}"
        wsis "Get out of my friend, you pervert!"
        hero "{aw}E{w=[wt1]}-ehhh!?{/aw}"

        # Facade
        #---------------------------------------------------------------------------
        call hide_ui from _call_hide_ui_169
        scene bg_0
        with Dissolve(1)
        $ hero_fx = 0
        $ hero_mood = "A1"
        $ wsis_fx = 0
        $ wsis_mood = "A1"
        $ wnei_fx = 0
        $ wnei_mood = "A1"

        scene bg_school facade
        show HERO at OR
        show WSIS at RC
        show WNEI at OR
        show HERO at RR_heavy
        show WSIS at LC_heavy
        show WNEI at RC_heavy
        with Dissolve(2)

        $ hero_mood = "O1"
        hero "{aw}Ehhh!?{/aw}{w=[wt2]} What's with the name of this school?{w=[wt2]} Am I reading it right?"

        $ wsis_mood = "O1"
        wsis "What's the problem with the name?{w=[wt2]} It's an acronym, of course!"

        $ wnei_mood = "O2"
        wnei "Yes!{w=[wt2]} It means Su[C_Nam]P[C_Off]er Duper [C_Nam]A[C_Off]wesome [C_Nam]N[C_Off]oble [C_Nam]T[C_Off]ranscedent [C_Nam]I[C_Off]ncredible [C_Nam]E[C_Off]xtraordinary [C_Nam]S[C_Off]chool!!!{w=[wt3]} This is where we will live from today onwards.{w=[wt4]} Be careful not to get caught entering the wrong dormitory if you don't want to go to school jail.{w=[wt2]} The staff here is super duper strict!"
        wnei "If we want to play at night{w=[wt1]}, you need to go through the secret passage that connects the dormitories, which is unguarded.{w=[wt2]} But you may have to face monsters."

        hero "Oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} G{w=[wt1]}-got it.{w=[wt2]} Thanks for the heads up."

        $ wnei_mood = "A1"
        wnei "Yar welcum."
        wsis "Hmph{w=[wt2]}, it's [C_Nam]P[C_Off]rofessional [C_Nam]A[C_Off]cademy of [C_Nam]N[C_Off]eedful [C_Nam]T[C_Off]alent [C_Nam]I[C_Off]mprovement in [C_Nam]E[C_Off]ducational [C_Nam]S[C_Off]kills!{w=[wt2]} The school focuses on practical job training through student-managed clubs.{w=[wt3]} So the student council itself handles most of the administration than the staff.{w=[wt3]} And no{w=[wt2]}, it doesn't have a dormitory{w=[wt2]}, much less a jail!"

        $ wnei_mood = "A4"
        wnei "{lg}Shi shi shi...{/lg}{w=[wt2]} So this school is super duper boring!{w=[wt4]} They should've gone with my version{w=[wt2]}, It'd be way way way super duper better!{w=[wt4]} Okay.{w=[wt2]} It's decided!{w=[wt2]}{nw}"

        $ wnei_mood = "A1"
        show WNEI at OR_slow
        wnei "{lg}Shi shi shi...{/lg} So this school is super duper boring! They should've gone with my version, It'd be way way way super duper better! Okay. It's decided!{fast} Let's go home and play!"

        $ hero_mood = "O2"
        show HERO at OR_average
        hero "Get back here, your runaway!{nw}"

        $ hero_mood = "A1"
        $ wnei_mood = "O1"
        show WNEI at RR_heavy
        show HERO at RR_heavy
        hero "Get back here, your runaway!{fast}{w=[wt3]} Where is all that spirit of knowing the new school?{w=[wt2]} Come on!{w=[wt3]}{nw}"

        show WNEI at RC_heavy
        hero "Get back here, your runaway!{fast} Where is all that spirit of knowing the new school?{w=[wt2]} Come on!{w=[wt3]}{fast}"

        $ wnei_mood = "A1"
        show WNEI at RC_slow
        wnei "You're right.{w=[wt2]} Let's record this moment!{w=[wt2]} Everyone's gonna be so jealous when they see we go to a school called {nm}P.A.N.T.I.E.S{/nm}!"

        $ X_spd = 2.5
        scene schoolday_0_bg
        show schoolday_0_wsis at CC
        show schoolday_0_wsis at LL_X
        show schoolday_0_heroandwnei
        with fade

        wsis "Stop{nw}"

        play SE1 "PhotoShot1.mp3"
        show image "images/UI/CellphoneBG/SHOT_SchoolSelfieTogether_1.webp" at PhotoShot

        wsis "Stop{fast} doing these embarrassing things!{nw}"

        $ cellbg.insert(1, "SHOT_SchoolSelfieTogether_1")
        $ msg.msg(renpy.translate_string("New photo added to phone Gallery"))

        wsis "Stop doing these embarrassing things!{fast}"

        wnei "{bt}SOOO COOOOL!!!{/bt}{w=[wt4]} Look, {nm}[fnamewsis]{/nm}!"

        wsis "Hmph{w=[wt2]}, you ended up showing me up."

        hero "Sure{w=[wt2]}, That made the photo complete!"

        wnei "{lg}SHI SHI SHI...{/lg}{w=[wt3]} {bt}Send me!{w=[wt2]} Send me!{/bt}"

        hero "Sure!"

        wsis "People are looking at us!"

        wnei "Then come take a photo with us, so we can go in."

        wsis "J{w=[wt1]}-just because you're insisting so much!{w=[wt3]} It's n{w=[wt1]}-not like I wanna take a weird picture with you or something."

        wnei "{bt}HUUUURRY UP!!!{/bt}"

        hero "Say {bt}Cheeese!{/bt}"

        play SE1 "PhotoShot1.mp3"
        scene image "images/UI/CellphoneBG/SHOT_SchoolSelfieTogether_2.webp" at PhotoShot

        $ cellbg.insert(1, "SHOT_SchoolSelfieTogether_2")
        $ msg.msg(renpy.translate_string("New photo added to phone Gallery"))

        wnei "{bt}Cheeese!{/bt}{w=[wt4]} Lemme see!{w=[wt2]} Lemme see!{w=[wt2]} .{w=[wt1]}.{w=[wt1]}.{w=[wt4]}{pr}{pa}SO COOOOL!!!{/pa}"
        wsis "{size=-10}S{w=[wt1]}-stop yelling!{w=[wt2]} People are looking!!{/size}"
        wnei "What do you think, {nm}[fnamewsis]{/nm}?"
        wsis "Huh?{w=[wt2]} {size=-10}Well{/size}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {size=-20}C{w=[wt1]}-cute{/size}."
        wnei "Hmm?{w=[wt2]} What?"
        wsis "N{w=[wt1]}-nothing.{w=[wt3]} Let's go already!!"
        wnei "Hey, {nm}[fnamehero]{/nm}.{w=[wt2]} Why don't you make one of these photos your phone wallpaper?"
        wsis "D{w=[wt1]}-don't leave a picture of me as your phone wallpaper!{w=[wt3]} That would be embarrassing!{w=[wt3]} Hurry up and let's get in!"

        call gametime_wait(7, 20) from _call_gametime_wait_20
        call gametime from _call_gametime_92
        $ Set_CharMap("hero", "school", "facade")

    jump show_ui

#---------------------------------------------------------------------------
label schoolday_1_1: # Frontyard
#---------------------------------------------------------------------------

    call hide_ui from _call_hide_ui_170
    $ hero_quest_2 = 1
    scene schoolday_1_1bg
    show schoolday_1_1hero_and_wnei
    show schoolday_1_1wsis 1o0
    with Dissolve(1)

    wnei "{bt}Look!{w=[wt1]} Look!{/bt}{w=[wt3]} There's a paunchy dude holdin' a giant phone!"

    hide schoolday_1_1hero_and_wnei
    show schoolday_1_1wnei 2 at CC
    show schoolday_1_1wnei2 o0
    show schoolday_1_1hero 2o0 at CC
    show schoolday_1_1wsis 1o1 at CC
    with dissolve

    wsis "This is a statue of an old president{w=[wt1]}, and he's holding a {bt}scripture{/bt}!"

    show schoolday_1_1wnei2 o1
    show schoolday_1_1wsis 1o0
    wnei "Huh?...{w=[wt2]} Is that so?{w=[wt2]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} He remains a paunchy dude holdin' a giant phone for me..."

    show schoolday_1_1wsis 1o1
    show schoolday_1_1wnei2 o0
    wsis "You don't know anything about History!{w=[wt3]}{nw}"

    show schoolday_1_1wsis 1a1
    wsis "You don't know anything about History!{fast} I bet {nm}[fnamehero]{/nm} also doesn't know who he is!"

    show schoolday_1_1wsis 1a0
    show schoolday_1_1hero 2s1
    hero "{aw}E{w=[wt1]}-ehh?...{w=[wt2]} I...{w=[wt2]}{/aw}{nw}"

    show schoolday_1_1hero 2s0
    $ a_check_0 = "male"
    # ----------------------------------------------------------------------------------------------------
    if perk_int_mem >= 1:
    # ----------------------------------------------------------------------------------------------------
        show schoolday_1_1hero 2s1
        hero "{aw}E-ehh?... I...{/aw}{fast} Of course I know!{w=[wt1]} He is{nw}"
        # --------------------------------------------------
        # HSTT First Name
        # --------------------------------------------------
        if fnameselect:
            $ fnamehstt = renpy.input(renpy.translate_string("{aw}E-ehh?... I...{/aw} Of course I know! He is...{pr}What's the first name of the old president?{pr}{color=#FFAF32}(Leave it blank to generate a random name){/color}"), length=12)
            if fnamehstt == "":
                if preferences.is_namepersistent == True and persistent.fnamehstt:
                    $ fnamehstt = persistent.fnamehstt
                else:
                    $ ChaNameWrite("hstt", 1)
        else:
            if preferences.is_namepersistent == True and persistent.fnamehstt:
                $ fnamehstt = persistent.fnamehstt
            else:
                $ ChaNameGen("hstt", 1)

        # --------------------------------------------------
        # WRIC Last Name
        # --------------------------------------------------
        if lnameselect:
            $ lnamewric = renpy.input(renpy.translate_string("{aw}E-ehh?... I...{/aw} Of course I know! He is Mr. {nm}[fnamehstt]{/nm}...{pr}What's the last name of the old president?{pr}{color=#FFAF32}(Leave it blank to generate a random name){/color}"),length=12)
            if lnamewric == "":
                if preferences.is_namepersistent == True and persistent.lnamewric:
                    $ lnamewric = persistent.lnamewric
                else:
                    $ ChaNameWrite("wric", 2)
        else:
            if preferences.is_namepersistent == True and persistent.lnamewric:
                $ lnamewric = persistent.lnamewric
            else:
                $ ChaNameGen("wric", 2)
        $ persistent.lnamewric = lnamewric
        # --------------------------------------------------

        show schoolday_1_1hero 2s1
        hero "{aw}E-ehh?... I...{/aw} Of course I know!{w=[wt1]} He is Mr. {nm}[fnamehstt] [lnamewric]{/nm}.{fast}{w=[wt3]} He was a very important man to our country!"
        
        show schoolday_1_1wsis 1o1
        show schoolday_1_1hero 2s0
        wsis "What!?{w=[wt2]} So do you really know that without having to read what is written here?"
    # ----------------------------------------------------------------------------------------------------
    else:
    # ----------------------------------------------------------------------------------------------------
        show schoolday_1_1hero 2s1
        hero "{aw}E-ehh?... I...{/aw}{fast} I don't know..."
                
        show schoolday_1_1wsis 1a1
        show schoolday_1_1hero 2s0

        wsis "{lg}Fu Hu Hu Hu...{/lg}{w=[wt1]} You're really an idiot, you know?{w=[wt3]} {bt}Okay... Okay...{/bt}{w=[wt2]} I'll tell you his name{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Let me read it here.{nw}"
        if preferences.is_namepersistent == True and persistent.fnamehstt:
            $ fnamehstt = persistent.fnamehstt
        else:
            $ ChaNameGen("hstt", 1)
        wsis "{lg}Fu Hu Hu Hu...{/lg} You're really an idiot, you know? {bt}Okay... Okay...{/bt} I'll tell you his name... Let me read it here.{fast}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"
        if preferences.is_namepersistent == True and persistent.lnamewric:
            $ lnamewric = persistent.lnamewric
        else:
            $ ChaNameGen("wric", 2)
        wsis "{lg}Fu Hu Hu Hu...{/lg} You're really an idiot, you know? {bt}Okay... Okay...{/bt} I'll tell you his name... Let me read it here...{fast} It's {nm}[fnamehstt] [lnamewric]{/nm}!"
    # ----------------------------------------------------------------------------------------------------

    show schoolday_1_1wsis 1a0
    show schoolday_1_1hero 2s1
    hero "{pa}Ehhh!?!?{/pa}{w=[wt3]} So you mean you were reading all the time!?"

    $ X_spd = 3
    show schoolday_1_1wsis 2 at LL_X
    show schoolday_1_1hero 2s0
    wsis "Of course, moron!{w=[wt1]} I hate History!"

    $ X_spd = 2
    $ X_pos = -600
    hide schoolday_1_1wnei2
    show schoolday_1_1wnei 3 at X_X
    wnei "{bt}Not fair!...{/bt}"

    pause(1)

    show schoolday_1_1hero 3
    with Dissolve(1)

    pause(1)

    show screen SchoolMonument
    with Dissolve(1)

    screen SchoolMonument():
        add "UI/UIBG/School Monument.webp"
        frame:
            background None
            xmargin 740
            ymargin 800
            xalign 0.5
            yalign 0.5
            xoffset 80
            yoffset 5
            hbox:
                text _("""{font=monof55.ttf}{color=#C8C8C8}
                    This monument is in memory of President {b}[fnamehstt] [lnamewric]{/b}.
                    The architect of the {b}Super Endowed Student{/b} law.
                    This landmark legislation expanded the duration of Elementary School years, so that the 3 years of High School would be used by adult students, who can make better decisions in their lifes.

                    {/color}{/font}""") size 40
    pause

    hero "{mind}(So it's because of this guy that I'm here instead of college?{w=[wt4]} Good...){/mind}"
    hide screen SchoolMonument

    scene bg_0
    with Dissolve(1)

    wnei "{bt}Look!{w=[wt1]} Look!{/bt}{w=[wt3]} There's a lotta gals lookin' at papers on the wall!"
    wsis "Oh{w=[wt1]}, The student list!{w=[wt2]} We better take a look too and see wich class we will be at."
    wnei "C'mon!"

    $ msg.msg(renpy.translate_string("Set of names generated"))
    mind "(I better take a look too)"

    $ a_check_6 = 0

    label schoolday_1_1_skip:
        pass

    $ _skipping = False
    $ a_check_4 = 1
    $ a_check_5 = "dice"

    if a_check_6 == 1:
        pass

    else:
        # Skip character creator 2 if all names already exist in persistent
        if preferences.is_skipcharcreate and preferences.is_namepersistent:
            python:
                _cc2_chars = [
                    "wric",
                    "wlaz", "wdel", "wgot", "wdis", "hprv", "wuza", "wgal", "wota", "hine", "wpre",
                    "wdan", "hriv", "hbul", "hfem", "wahu", "wemo", "wtec", "wnem", "wido", "wkuu",
                    "wrin", "wsuk", "wfat", "whip", "hfre", "hbla"
                ]
                _cc2_all_set = all(
                    getattr(persistent, "fname" + _cid, None) and getattr(persistent, "lname" + _cid, None)
                    for _cid in _cc2_chars
                )
            if _cc2_all_set:
                python:
                    for _cid in _cc2_chars:
                        setattr(store, "fname" + _cid, getattr(persistent, "fname" + _cid))
                        setattr(store, "lname" + _cid, getattr(persistent, "lname" + _cid))
                jump start_mid_2

        $ ChaNameGen("wric", 1)
        if lnamewric == "":
            $ ChaNameGen("wric", 2)
        $ ChaNameGen([
            "wlaz", "wdel", "wgot", "wdis", "hprv", "wuza", "wgal", "wota", "hine", "wpre", # 1B
            "wdan", "hriv", "hbul", "hfem", "wahu", "wemo", "wtec", "wnem", "wido", "wkuu", # 1A
            "wrin", "wsuk", "wfat", "whip", "hfre", "hbla" # 3A
            ])

        call charactercreator2 from _call_charactercreator2

    hide screen studentlist1
    hide screen studentlist1_button

    label start_mid_2:
        pass

    $ _skipping = True

    if is_skipable == "Day3":
        $ _skipping = True
        $ quick_menu = True
        $ gametimeday = 2
        $ hero_quest_2 = 4
        $ Set_CharMap("hero", "home", "bedroom_hero")
        jump passday

    $ a_check_2 = fnamewpre
    $ a_check_3 = lnamewpre
    $ fnamewpre = "Girl"
    $ lnamewpre = ""

    scene schoolday_1_2bg
    show schoolday_1_2mg1body
    show schoolday_1_2mg1head 1
    show schoolday_1_2wsis_and_wnei 1
    show schoolday_1_2mg2body
    show schoolday_1_2mg2head 1
    show schoolday_1_2wpre 1
    show schoolday_1_2herobody at CC
    show schoolday_1_2heroarm 1
    with Dissolve(2)

    pause(1)

    mind "(So we'll be in different classrooms...)"
    wnei "Found it!{w=[wt2]} This is our classroom!{w=[wt2]} We are on the 1A list!"
    wsis "Hmp!{w=[wt2]} Those two blonde bitches hasn't been kicked from the school yet.{w=[wt3]} At least we won't be in the same classroom this time.{w=[wt3]} Still{w=[wt1]}, would be better if the redhead jerk also accompanies them as well instead of being on my list!"
    wnei "Hey, {nm}[fnamewsis]{/nm}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I can't find {nm}[fnamehero]{/nm}'s name."

    stop BGM fadeout 3
    wsis "Of course not!{w=[wt2]} You're just looking at 1A list.{w=[wt2]} He's on the 1B list."
    wnei "{aw}Ehhh!?!?{/aw}"

    hide schoolday_1_2wsis_and_wnei
    hide schoolday_1_2mg2body
    hide schoolday_1_2mg2head
    hide schoolday_1_2wpre
    hide schoolday_1_2herobody
    hide schoolday_1_2heroarm
    show schoolday_1_2mg1body
    show schoolday_1_2mg1head 1
    show schoolday_1_2wsisbody 1 at CC
    show schoolday_1_2wsisface o0 at CC
    show schoolday_1_2wsiseye l at CC
    show schoolday_1_2wsisfg at CC
    show schoolday_1_2wneibody 1 at CC
    show schoolday_1_2wneiface o0
    show schoolday_1_2mg2body
    show schoolday_1_2mg2head 1
    show schoolday_1_2wpre 1
    show schoolday_1_2herobody at CC
    show schoolday_1_2heroarm 1 at CC
    with Dissolve(1)
    pause(1)

    $ X_spd = 2
    $ X_pos = -75
    $ Y_pos = 10
    $ Z_rot = -5
    show schoolday_1_2herobody at Hit_XY
    show schoolday_1_2heroarm at Hit_XY

    play BGM "audio/W2C - Fun.mp3"
    show schoolday_1_2wneiface o1
    wnei "{pa}You traitor!!!{/pa}{nw}"
    $ Y_spd = 2
    $ Y_pos = 50
    show schoolday_1_2mg1head 2
    show schoolday_1_2mg2head 2
    show schoolday_1_2wpre 2
    show schoolday_1_2herofx at Y_Move
    wnei "{pa}You traitor!!!{/pa}{fast}"
    show schoolday_1_2wneiface o0
    show schoolday_1_2mg1head 3
    show schoolday_1_2mg2head 3
    show schoolday_1_2wpre 3
    show schoolday_1_2wpre_face o0
    hero "It's not as if I were the one to decide that..."

    show schoolday_1_2wneiface o1
    show schoolday_1_2wneifx
    show schoolday_1_2mg1head 2
    show schoolday_1_2mg2head 2
    show schoolday_1_2wpre 2
    hide schoolday_1_2wpre_face
    wnei "{pa}I trusted you!!!{/pa}"

    show schoolday_1_2wneibody 2 at OR_slow
    hide schoolday_1_2wneiface
    hide schoolday_1_2wneifx
    show schoolday_1_2heroarm 2
    show schoolday_1_2mg1head 3
    show schoolday_1_2mg2head 3
    show schoolday_1_2wpre 3
    show schoolday_1_2wpre_face o0
    hero "{aw}S{w=[wt1]}-t{w=[wt1]}-{/aw}{nw}"
    show schoolday_1_2wsiseye r
    hero "{aw}S-t-{fast}top making people draw wrong conclusions!!!{/aw}"

    show schoolday_1_2wsiseye l
    with dissolve
    $ X_spd = 20
    show schoolday_1_2wsisbody 1 at RC_X
    show schoolday_1_2wsiseye l at RC_X
    show schoolday_1_2wsisface o1 at RC_X
    show schoolday_1_2wsisfg at RC_X
    show schoolday_1_2mg1head 2
    show schoolday_1_2mg2head 2
    show schoolday_1_2wpre 2
    hide schoolday_1_2wpre_face

    wsis "Hey, Moron{w=[wt1]}, I'm going after her!{w=[wt2]} We'll talk later!"

    show schoolday_1_2wsisbody 2 at OR_slow
    hide schoolday_1_2wsiseye
    hide schoolday_1_2wsisface
    hide schoolday_1_2wsisfg
    show schoolday_1_2mg1head 3
    show schoolday_1_2mg2head 3

    hero "H{w=[wt1]}-hey..."

    show schoolday_1_2wpre 3
    show schoolday_1_2wpre_face o0
    with Dissolve(1)
    pause (1)

    show schoolday_1_2wpre_face o1

    wpre "... E{w=[wt1]}-excuse me...?"

    show schoolday_1_2wpre_face o0
    hero "H{w=[wt1]}-hi{w=[wt2]}, h{w=[wt1]}-how may I help you?"

    show schoolday_1_2wpre_face a1
    wpre "Would you be {nm}Mr. [fnamehero] [lnamehero]{/nm}?"
    
    if "WPRE_Work_GroceryStore" in hero_know:
        show schoolday_1_2wpre_face a0
        hero "Y{w=[wt1]}-yes...!{w=[wt3]} W{w=[wt1]}-wait{w=[wt2]}, you're the girl from yesterday!"

        $ msg.msg(renpy.translate_string("You know {nm}[fnamewpre]{/nm} a little more"))
        $ add_stat("wpre", "inti", 0.5)
        $ add_stat("wpre", "love", 0.5)
        $ add_stat("hero", "cha_soc", 1.0)

        show schoolday_1_2wpre_face a1
        wpre "Yes!{w=[wt2]} I attended you and the pink haired girl yesterday.{w=[wt2]} I'm glad you remembered me!{nw}"

        show schoolday_1_2wpre_face o1
        wpre "Yes! I attended you and the pink haired girl yesterday. I'm glad you remembered me!{fast} Oh, I know your name for the fact of it have been recently pronounced by y-your...{nw}"

        show schoolday_1_2wpre_fx
        show schoolday_1_2wpre_face s1
        wpre "Yes!{w=[wt2]} I'm glad you remembered me!{w=[wt2]}{fast} Oh, I know your name for the fact of it have been recently pronounced by y-your..{fast}I mean{w=[wt2]}, T{w=[wt1]}-the blonde girl!"

    else:
        $ msg.msg(renpy.translate_string("You know {nm}[fnamewpre]{/nm} a little more"))
        show schoolday_1_2wpre_face a0
        hero "Y{w=[wt1]}-yes...!{w=[wt3]} W{w=[wt1]}-wait{w=[wt2]}, you're no stranger to me{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Have we met before though...?"

        show schoolday_1_2wpre_face a1
        wpre "Yes!{w=[wt3]}{nw}"

        show schoolday_1_2wpre_face o1
        wpre "Yes!{fast} I{w=[wt1]}-I mean n{w=[wt1]}-not exactly!{w=[wt2]}{nw}"

        show schoolday_1_2wpre_fx
        wpre "Yes!... I-I mean n-not exactly!{fast} I{w=[wt1]}-I know your name for the fact of it have been recently pronounced by y{w=[wt1]}-your...{w=[wt2]}{nw}"

        show schoolday_1_2wpre_face s1
        wpre "Yes! I-I mean n-not exactly! I-I know your name for the fact of it have been recently pronounced by y-your...{fast}T{w=[wt1]}-the blonde girl!...{w=[wt3]} And{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} I recall seeing you yesterday with that other girl."
    
    show schoolday_1_2wpre_face s0
    show schoolday_1_2mg1head 4
    show schoolday_1_2mg2head 4
    with dissolve

    $ a_check_1 = "Girls"
    play SE2 "Talking_Female.mp3" fadein 2
    sup1 "({aw}Did you see? This boy cheated on that tiny girl with that friend of hers!{/aw}){fast}{w=[wt4]}{w=[wt4]}{nw}"
    sup1 "({aw}Did you see? This boy cheated on that tiny girl with that friend of hers!{/aw}){pr}({aw}Oh, poor girl!{/aw}){fast}{w=[wt4]}{w=[wt4]}{nw}"
    sup1 "({aw}Did you see? This boy cheated on that tiny girl with that friend of hers!{/aw}){pr}({aw}Oh, poor girl!{/aw}){pr}({aw}Haven't I told you? All men are the same!{/aw}){fast}"

    call gametime from _call_gametime_93
    $ hero_fx = 1
    $ wpre_fx = 1
    $ wpre_mood = "O1"
    scene bg_school frontyard
    show HERO at LC
    show WPRE at RC
    with Fade(1,1,2)

    if "WPRE_Work_GroceryStore" in hero_know:
        stop BGM fadeout 5
        wpre "Apologies for the misunderstanding, {nm}Mr. [fnamehero] [lnamehero]{/nm}!{w=[wt2]} I've not been myself under the excitement of starting a new school year."

    else:
        wpre "Apologies for the misunderstanding!{w=[wt2]} I work at the grocery store and recall attending you with the dyed hair girl.{w=[wt3]} I assure you that I do not stalk anyone!{w=[wt2]} Simply{w=[wt1]}, her unique appearance made her memorable.{w=[wt2]}{nw}"
        $ wpre_mood = "A2"
        wpre "Apologies for the misunderstanding! I work at the grocery store and recall attending you with the dyed hair girl. I assure you that I do not stalk anyone! Simply, her unique appearance made her memorable.{fast}{w=[wt2]} {aw}I'm not saying she's not beautiful!{w=[wt2]} In fact, I must{/aw}{pr}{aw}commend on her beauty! I{w=[wt1]}-I mean...{/aw}"

        stop BGM fadeout 5

        wpre "Oh{w=[wt2]}, please excuse my improper moment, {nm}Mr. [fnamehero] [lnamehero]{/nm}!{w=[wt2]} I've not been myself under the excitement of starting a new school year."

    play BGM "audio/W2C - Tranquility.mp3" fadein 5

    $ hero_mood = "A2"
    hero "Y{w=[wt1]}-you don't need to.{w=[wt2]} I understood what you meant.{w=[wt3]} You know{w=[wt2]}, it's quite a surprise to see you here at school{w=[wt2]}, uh{w=[wt2]}, {nm}miss{/nm}."

    $ wpre_mood = "A2"
    wpre "Please allow me to introduce myself.{w=[wt2]} My name is {nw}"

    $ fnamewpre = a_check_2
    $ lnamewpre = a_check_3
    $ a_check_2 = 0
    $ a_check_3 = 0

    $ wpre_mood = "A1"
    wpre "Please allow me to introduce myself. My name is {fast}{nm}[fnamewpre] [lnamewpre]{/nm}.{w=[wt2]} I will be your classmate for the year.{w=[wt2]} I look forward to establishing a good relationship with you!"

    $ hero_fx = 0
    hero "Of{w=[wt1]}-Of course!{w=[wt2]} Nice to meet you, {nm}[fnamewpre]{/nm}.{w=[wt2]} It's good that I meet someone in the same class this early.{w=[wt2]}{nw}"

    $ hero_fx = 0
    $ hero_mood = "A1"
    hero "Of-Of course! Nice to meet you, {nm}[fnamewpre]{/nm}. It's good that I meet someone in the same class this early.{fast}{w=[wt2]} By the way...{w=[wt3]} You can call me just {nm}[fnamehero]{/nm} if you don't mind!{w=[wt1]} No need to be so formal."

    $ wpre_fx = 0
    $ wpre_mood = "A2"
    wpre "Apologies.{w=[wt2]} Before moving here{w=[wt1]}, I was advised to always treat people with the utmost respect.{w=[wt3]} I must be approaching this matter from the wrong direction..."

    if "WPRE_BG_Countryside" in hero_know:

        hero "You said you're from countryside, right?{w=[wt2]} What's the name of the place?"

        $ msg.msg(renpy.translate_string("You know {nm}[fnamewpre]{/nm} a little more"))
        $ add_stat("wpre", "inti", 0.5)
        $ add_stat("wpre", "love", 0.5)
        $ add_stat("hero", "cha_soc", 1.0)

    else:

        hero "Oh...{w=[wt1]} Are you from a different region?"

    $ wpre_mood = "A1"
    wpre "Yes.{w=[wt2]} I'm from{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"

    # ----------------------------------------------------------------------------------------------------
    if perk_int_mem >= 1:
    # ----------------------------------------------------------------------------------------------------
        # --------------------------------------------------
        # Region: Countryside Name
        # --------------------------------------------------
        $ rnamevil2 = renpy.input(renpy.translate_string("Yes. I'm from...{pr}What's the name of the village where she came from? {pr}{color=#FFAF32}(Leave it blank to generate a random name){/color}"), length=24)
        if rnamevil2 == "":
            call rnamegen from _call_rnamegen_2
            $ rnamevil2 = a_check_0
        # --------------------------------------------------
    else:
        call rnamegen from _call_rnamegen_3
        $ rnamevil2 = a_check_0
    # ----------------------------------------------------------------------------------------------------

    wpre "Yes.{w=[wt2]} I'm from{fast} {nm}[rnamevil2]{/nm}.{w=[wt2]} It's a small village in the countryside.{w=[wt2]} I went to this city a few months ago to study and work.{w=[wt2]}"

    if rnamevil1 == "":
        call rnamegen from _call_rnamegen_4
        $ rnamevil1 = a_check_0

    # ----------------------------------------------------------------------------------------------------
    if perk_int_mem >= 1:
    # ----------------------------------------------------------------------------------------------------
        hero "Really?{w=[wt2]} I have lived my last years in a slightly farther region.{w=[wt3]} I used to live in {nm}[rnamevil1]{/nm} up to two days ago and came back to the city yesterday."
        $ add_stat("wpre", "love", 1)
        $ add_stat("hero", "cha_soc", 1)
    # ----------------------------------------------------------------------------------------------------
    else:
        hero "That's nice!{w=[wt2]} I was born in the city{w=[wt1]}, but I have lived my last years in the countryside.{w=[wt3]} I used to live in {nm}[rnamevil1]{/nm} up to two days ago and came back to the city yesterday."
    # ----------------------------------------------------------------------------------------------------

    wpre "Most intriguing!{w=[wt2]} It must have been tiring{w=[wt1]}, {nm}[rnamevil1]{/nm} is very far away from here."
    hero "Oh{w=[wt1]}, so do you know it?"
    wpre "Not personally{w=[wt2]}, in fact I rarely went out back then.{w=[wt3]} I simply enjoyed reading books{w=[wt1]}, and have learnt quite thoroughly about the surrounding regions.{w=[wt3]} Countryside life wasn't my cup of tea{w=[wt1]}, so I often buried myself in literature, you see!{w=[wt1]} {gg}Tee-hee-hee...{/gg}"
    hero "That's nice!{w=[wt2]} I bet this school must have a good library!"
    wpre "{bt}Y{w=[wt1]}-yes{w=[wt1]}, it does!!!{/bt}{w=[wt2]} I can barely believe that from now on I can spend some time in a real library...{w=[wt2]} Study in this school is{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]}{nw}"
    $ wpre_fx = 1
    wpre "{bt}Y-yes, it does!!!{/bt} I can barely believe that from now on I can spend some time in a real library... Study in this school is...{fast} {aw}l{w=[wt1]}-like a dream coming true!!!{w=[wt4]}{/aw}{nw}"
    $ wpre_mood = "A2"
    wpre "{bt}Y-yes, it does!!!{/bt} I can barely believe that from now on I can spend some time in a real library... Study in this school is... {aw}l-like a dream coming true!!!{/aw}{fast} Oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} I may sound childish right now.{w=[wt4]} A{w=[wt1]}-anyhow..."
    $ wpre_fx = 0
    wpre "I still don't know the school other than what I heard about.{w=[wt3]} Perhaps I should make use of the time before class to familiarize myself with the place.{w=[wt2]} My apologies for taking so much of your time, {nm}[fnamehero]{/nm}.{w=[wt2]} I will rejoin you back in class.{w=[wt2]} Have a nice day."

    menu:
        "Let her go":
            hero "S{w=[wt1]}-sure!...{w=[wt2]} Nice to meet you too, {nm}[fnamewpre]{/nm}!{w=[wt2]} Have a nice day."
            $ wpre_mood = "A2"
            show WPRE at OR_slow
            pause(1)
        "Accompany her":
            hero "I{w=[wt1]}-I can explore the school with you!...{w=[wt2]} I mean{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} if you don't mind!"
            $ wpre_fx = 1
            $ wpre_mood = "A2"
            with Dissolve(1)
            wpre "I'm glad not to be an annoyance to you, {nm}[fnamehero]{/nm}.{w=[wt2]} It would be nice to have a company!{w=[wt1]} S{w=[wt1]}-so{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"
            $ wpre_mood = "A1"
            $ wpre_is_flw = True
            $ msg.msg(renpy.translate_string("{nm}[fnamewpre]{/nm} is now following you"))
            wpre "I'm glad not to be an annoyance to you, {nm}[fnamehero]{/nm}. It would be nice to have a company! S-so...{fast} let's go?"

    $ hero_fx = 0
    $ wpre_fx = 0
    $ hero_mood = "A1"
    $ wpre_mood = "A1"
    jump show_ui

#---------------------------------------------------------------------------
label schoolday_1_1_hallway:
#---------------------------------------------------------------------------
    $ scenestep.insert(1, "hallway2")

    call hide_ui from _call_hide_ui_171
    show HERO at LC
    show WPRE at RC
    $ hero_fx = 1
    $ hero_mood = "O1"
    with fade

    mind "(Wow...{w=[wt1]} Will this place be full of girls wearing small skirts while people downstairs can take a good look from below?...)"
    wpre "Oh{w=[wt1]}, look at this balcony!{w=[wt2]} It's a pleasant surprise to find this vantage point where we can enjoy a view of the courtyard{w=[wt2]}. I can imagine staying here during breaks!{w=[wt2]} It's quite intriguing how the school has designed these different spaces to serve various purposes, don't you think?"
    menu:
        "Agree, cos the upstairs view is perfect!":
            $ hero_mood = "A2"
            hero "A{w=[wt1]}-absolutely!{w=[wt2]} The view is great in every way...{w=[wt2]} Would be even better if it was breezy up here too!"
            $ add_stat("wpre", "love", 1)
            $ add_stat("hero", "cha_soc", 1)
            wpre "I wholeheartedly agree!{w=[wt2]} That was a great assessment considering the importance of ventilation, {nm}[fnamehero]{/nm}.{w=[wt3]} You certainly have an eye for hidden details!"
            hero "I{w=[wt1]}-I just think of some{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} p{w=[wt1]}-priorities...{w=[wt1]} {lg}He He...{/lg}"

        "Disagree, cos the downstairs view is perfect!":
            hero "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} The balcony is nice and all, but{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} I t{w=[wt1]}-think that people downstairs might have a{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} too c{w=[wt1]}-clear view of the b{w=[wt1]}-balcony{w=[wt1]} and maybe it's not so good..."
            $ wpre_mood = "O1"
            wpre "Hm?...{w=[wt2]} My apologies, {nm}[fnamehero]{/nm}!{w=[wt2]} I...{w=[wt2]} I didn't understand your point."
            hero "T{w=[wt1]}-The angle and sparce railing might not provide the best privacy for girls up here, you know...?"
            wpre ".{w=[wt1]}.{w=[wt1]}.{w=[wt3]}{nw}"
            $ wpre_fx = 1
            $ add_stat("wpre", "lust", 1)
            $ add_stat("hero", "cha_soc", 0.1)
            wpre "...{fast} O{w=[wt1]}-oh!...{w=[wt3]} That's a good point!{w=[wt2]} I'll assure to take care about that when I pass near...{w=[wt2]} Also!...{w=[wt2]}{nw}"
            $ wpre_mood = "A1"
            wpre "...{fast} O-oh!... That's a good point! I'll assure to take care about that when I pass near... Also!...{fast} It's good to know a man who is worried about this.{w=[wt3]} T{w=[wt1]}-thank you for open my mind for that, {nm}[fnamehero]{/nm}"
            $ hero_mood = "A2"
            hero "Y{w=[wt1]}-you're welcome...!"
            mind "(I did the right thing, didn't I?{w=[wt3]} It's one girl less to peep from below{w=[wt1]}, but I don't regret it{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} Right?)"

    $ add_stat("wpre", "inti", 1)
    $ hero_fx = 0
    $ wpre_fx = 0
    $ hero_mood = "A1"
    $ wpre_mood = "A1"
    jump show_ui

#---------------------------------------------------------------------------
label schoolday_1_1_courtyard:
#---------------------------------------------------------------------------
    $ scenestep.insert(1, "courtyard")
    
    call hide_ui from _call_hide_ui_172
    show HERO at LC
    show WPRE at RC
    with fade
    
    $ wpre_mood = "A1"
    $ hero_mood = "A1"
    wpre "Oh{w=[wt1]}, this courtyard is absolutely lovely, isn't it?{w=[wt3]} The ambiance here feels so peaceful and relaxed{w=[wt2]}, the wide open area with benches{w=[wt2]}, kiosks{w=[wt2]}, and that charming fountain seems designed for students to find comfort during breaks or leisure moments.{w=[wt4]} What do you think?{w=[wt2]} Isn't it a very welcoming place?{nw}"

    menu:
        wpre "Oh, this courtyard is absolutely lovely, isn't it? The ambiance here feels so peaceful and relaxed, the wide open area with benches, kiosks, and that charming fountain seems designed for students to find comfort during breaks or leisure moments. What do you think? Isn't it a very welcoming place?{fast}"

        "Say it's good hang out spot":
            hero "Definitely!{w=[wt2]} The fountain makes the environment very relaxing.{w=[wt2]} I can imagine spending a lot of time here chatting{w=[wt1]}, or using the kiosk table to play games with friends!"
            $ add_stat("wpre", "love", 1)
            $ add_stat("hero", "cha_soc", 1)
            wpre "Using the kiosk table for games sounds like a fantastic idea!{w=[wt2]} It's interesting how you see the potential for different activities here."

        "Say it's a good make out spot":
            hero "Yes{w=[wt1]}, it's a perfect make-out spot."
            $ add_stat("wpre", "lust", 1)
            $ add_stat("hero", "cha_soc", 0.1)
            $ wpre_mood = "O2"
            $ wpre_fx = 1
            wpre "{aw}Ehhh...!?{/aw}"
            $ hero_mood = "O1"
            $ hero_fx = 1
            hero "{aw}I{w=[wt1]}-I mean...{/aw}{w=[wt3]} The fountain makes everything a little romantic.{w=[wt2]} People might find comfort here in a lot ways, right?"
            $ wpre_mood = "A2"
            wpre "{gg}Tee-hee-hee...{/gg}{w=[wt4]} Well{w=[wt1]}, you certainly have a creative perspective{w=[wt2]}, the ambiance here is undoubtedly pleasant{w=[wt1]}, and the fountain does add a touch of charm.{w=[wt3]} I suppose people can find various ways to appreciate this place{w=[wt2]}, whether for relaxation{w=[wt2]}, romantic moments{w=[wt2]}, or just good company."

    $ hero_mood = "A1"
    $ wpre_mood = "A1"
    $ hero_fx = 0
    $ wpre_fx = 0
    with dissolve
    $ add_stat("wpre", "inti", 1)

    wpre "Look over there!{w=[wt3]} The grids separate the courtyard from the sports areas while the path guides students efficiently{w=[wt2]}, making them pass through the locker room first{w=[wt1]}, ensuring safety and order.{w=[wt4]} It's interesting how the school keeps everything organized and encourages students to use these spaces responsibly."
    wpre "It made me notice something.{w=[wt3]} The school seems to emphasize freedom in activities.{w=[wt2]} The availability of extracurricular activities during the afternoon shift showcases the school's dedication to preparing us for the future job market.{w=[wt2]} Since external work also counts as a valuable extracurricular activity here."

    wpre "It's a holistic approach{w=[wt1]}, recognizing the value of both traditional school activities and real-world experiences, don't you think?"

    $ hero_mood = "A2"
    hero "Wow...!{w=[wt2]} I didn't even know how the academic routine of this school works.{w=[wt3]} So it has mandatory academic activities in the morning and optional extracurricular in the afternoon?"
    $ wpre_mood = "A2"
    $ wpre_fx = 0
    wpre "Forgive my unkindness{w=[wt1]}, I started talking without knowing that you didn't know.{w=[wt3]} B{w=[wt1]}-but I won't judge!!{w=[wt2]} I have in mind that yesterday must have been really busy for you to think about stuff like that."
    hero "Y{w=[wt1]}-yes...{w=[wt2]} It really was... {gg}He-he...{/gg}"
    $ wpre_mood = "A1"
    wpre "Well{w=[wt1]}, It's as you said.{w=[wt2]} The academic activities of this school are in the morning.{w=[wt2]} But just like afternoon activities{w=[wt1]}, they're not compulsory.{w=[wt2]} We students are free to attend or not to attend classes as long as we don't miss on the test days."
    wpre "The afternoon shift is free to be used for the extracurricular activities of clubs{w=[wt1]}, to encourage students to prepare for the labour market.{w=[wt2]} Therefore{w=[wt1]}, external works also count as such activities{w=[wt1]}, as they are precisely real works."
    $ hero_mood = "A3"
    hero "That's cool!{w=[wt2]} So, does that mean I can use my time the way I want it on weekdays?"
    $ hero_mood = "A1"
    $ wpre_fx = 1
    wpre "{gg}Tee-hee-hee...{/gg}{w=[wt2]} Yes{w=[wt1]}, you can!{w=[wt2]} The school considers to assist in the development of students without interfering with their own choices.{w=[wt3]} After all{w=[wt2]}, as we all students are adults{w=[wt2]}, we need to choose the best way to build our lives for ourselves."
    hero "So you can gain extracurricular workload in your work at the convenience store, right?"
    wpre "Precisely, {nm}[fnamehero]{/nm}!{w=[wt3]} In fact{w=[wt2]}, as I'm working in a part-time job{w=[wt2]}, depending on what kind of activities are available{w=[wt1]}, maybe I share my days of the week between work and some school activities{w=[wt3]}, I believe the clubs should be created during this week.{w=[wt2]} It's quite exciting, isn't it?"
    wpre "By the way{w=[wt2]}, Would you be interested in the opening of some kind of club?{nw}"
    menu:
        wpre "By the way{w=[wt2]}, Would you be interested in the opening of some kind of club?{fast}"
        "A club to hang out":
            $ stat_cha_bonus += 9
            $ msg.msg(renpy.translate_string("{color=#32FF32}9% bonus{/color} for CHA gaining"))
            $ hero_mood = "A2"
            hero "Nothing specific.{w=[wt2]} I think it'd be cool for a club that it was possible to talk and have fun with friends."
            wpre "So you're an outgoing person, hm?{w=[wt2]} A club where the focus is on interaction can be a great place to develop the charisma.{w=[wt3]} By the way...{w=[wt1]} where do we go now?"
        "A club to practice sports":
            $ stat_phy_bonus += 9
            $ msg.msg(renpy.translate_string("{color=#32FF32}9% bonus{/color} for PHY gaining"))
            hero "I'd like to use that area behind this school more often{w=[wt2]}, then{w=[wt1]}, maybe there should be a club were students use this."
            wpre "That's nice!{w=[wt2]} Practicing exercises is critical to health.{w=[wt2]} Such a club would be great for physical improvement!{w=[wt3]} By the way...{w=[wt1]} where do we go now?"
        "A club for mind improvement":
            $ stat_int_bonus += 9
            $ msg.msg(renpy.translate_string("{color=#32FF32}9% bonus{/color} for INT gaining"))
            hero "Since the idea is to make people ready for the job market{w=[wt2]}, I think the ideal club needs to have some activity where intellectual skills could be improved."
            wpre "I absolutelly agree!{w=[wt2]} We should take advantage of our time as students as best as possible to improve our knowledge!{w=[wt3]} By the way... where do we go now?"
#        "It's better to work":
#            $ hero_mood = "A2"
#            hero "I don't know{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} If the idea is to really make people ready for the job market{w=[wt1]}, then{w=[wt1]}, I think it'd be better to use this time to find a real work."
#            $ wpre_mood = "A2"
#            wpre "W{w=[wt1]}-well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} You're not wrong...{w=[wt2]} M{w=[wt1]}-maybe it's the right thing to do, isn't it?{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} By the way...{w=[wt1]} where do we go now?"
        "No idea":
            $ stat_cha_bonus += 3
            $ stat_phy_bonus += 3
            $ stat_int_bonus += 3
            $ msg.msg(renpy.translate_string("{color=#32FF32}3% bonus{/color} for each stat gaining"))
            $ hero_mood = "A2"
            hero "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} I have nothing specific in mind.{w=[wt2]} I think I'll wait to see."
            wpre "You're right.{w=[wt2]} Sometimes it's better not to create expectations, isn't it?...{w=[wt3]} By the way...{w=[wt1]} where do we go now?"

    $ add_stat("wpre", "inti", 1)

    $ hero_fx = 0
    $ wpre_fx = 0
    $ hero_mood = "A1"
    $ wpre_mood = "A1"
    jump show_ui

#---------------------------------------------------------------------------
label schoolday_1_1_library:
#---------------------------------------------------------------------------
    $ scenestep.insert(1, "library")
    
    call hide_ui from _call_hide_ui_173
    show HERO at LC
    show WPRE at RC
    $ hero_mood = "A1"
    $ wpre_mood = "A3"
    $ wpre_fx = 1
    with fade

    wpre "{aw}Oh{w=[wt1]}, here we are!{/aw}{w=[wt3]} I can hardly contain my excitement!!{w=[wt2]} Just look at all these shelves{w=[wt2]}, adorned with books of various genres and topics.{w=[wt3]} I have a feeling I'd spend a lot of time in here.{w=[wt2]} {aw}Imagine all the knowledge and stories waiting to be explored!{/aw}"

    show WPRE at OR_average
    wpre "{bt}Oh my God...!{/bt}{w=[wt1]} {aw}Look at these books!!{/aw}"

    $ hero_mood = "A2"
    mind "(Wooow...!{w=[wt2]} As soon as we entered here she became someone else!{w=[wt3]} It's kinda fun to see a so reserved girl having genuinely fun to the point of not being able to maintain her posture.{w=[wt3]} I wonder if she will allow me to see more of this loose side of her.)"
    $ wpre_mood = "O2"
    $ wpre_fx = 1
    show WPRE at RC_slow
    wpre "Oh{w=[wt1]}, {nm}[fnamehero]{/nm}{w=[wt1]}, p{w=[wt1]}-please{w=[wt1]}, forgive my childishness!{w=[wt2]} I j{w=[wt1]}-just ran out and left you alone here.{w=[wt2]}{nw}"

    show HERO at Laugh
    $ hero_mood = "A4"
    wpre "Oh, {nm}[fnamehero]{/nm}, p-please, forgive my childishness! I j-just ran out and left you alone here.{fast}{w=[wt2]} I promise this won't happen anymore!"
    wpre "{aw}{w=[wt2]}.{w=[wt2]}.{w=[wt2]}.{w=[wt2]}M{w=[wt1]}-may I ask what makes you laugh so much...?{/aw}"

    show HERO at LC
    $ hero_mood = "A2"
    hero "Sorry!{w=[wt2]} I just found your change of posture funny.{nw}"

    menu:
        hero "Sorry!{w=[wt2]} I just found your change of posture funny.{fast}"
        "Try to make her more comfortable about it":
            hero "Sorry! I just found your change of posture funny.{fast} You don't need to feel like this.{w=[wt2]} It's good to see someone who likes books so much."
            $ wpre_mood = "A2"
            $ add_stat("wpre", "love", 1)
            $ add_stat("hero", "cha_soc", 1)
            wpre "Thank you for your kind words, {nm}[fnamehero]{/nm}.{w=[wt2]} That means a lot to me!"

        "Tell you like this side of her":
            hero "Sorry! I just found your change of posture funny.{fast} But I kinda like this side of yours.{w=[wt2]} It's cute."
            $ wpre_mood = "A2"
            $ wpre_fx = 2
            $ add_stat("wpre", "lust", 1)
            $ add_stat("hero", "cha_soc", 0.1)
            wpre "C{w=[wt1]}-cute...?{w=[wt4]} Thank you for your kind words... {gg}Tee-hee...{/gg}{w=[wt4]} No one has ever told me something like that."

    $ wpre_fx = 1
    $ add_stat("wpre", "inti", 1)
    wpre "By the way{w=[wt2]}, did something here caught your attention?{nw}"
    $ wpre_mood = "A1"

    menu:
        wpre "By the way, did something here caught your attention?{fast}"
        "Academic reading section":
            $ hero_mood = "A1"
            $ stat_int_bonus += 9
            $ msg.msg(renpy.translate_string("{color=#32FF32}9% bonus{/color} for INT gaining"))
            hero "Yes!{w=[wt2]} There are several academic books here.{w=[wt3]} It must be a very profitable place to study."
            $ add_stat("wpre", "love", 1)
            $ add_stat("hero", "cha_soc", 1)
            wpre "Absolutely{w=[wt2]},  it's wonderful to have such a resourceful library at our disposal!{w=[wt3]} It's indeed a treasure trove of knowledge.{w=[wt3]} I can already imagine spending countless hours here{w=[wt2]}, delving into these books to enhance our understanding of various subjects.{w=[wt3]} It's a space where learning truly comes to life!"

        "Tables for study groups":
            $ hero_mood = "A1"
            $ stat_cha_bonus += 9
            $ msg.msg(renpy.translate_string("{color=#32FF32}9% bonus{/color} for CHA gaining"))
            hero "Yes!{w=[wt2]} This library has plenty of reading tables.{w=[wt2]} It must be very good to study in groups{w=[wt1]}, don't you think?"
            $ add_stat("wpre", "love", 1)
            $ add_stat("hero", "cha_soc", 1)
            wpre "You are absolutely right!{w=[wt2]} It's great to see that the school sought to establish a pleasant and welcoming environment to encourage joint learning for students!"

        "Erotic reading section":
            $ hero_mood = "A2"
            $ stat_phy_bonus += 9
            $ msg.msg(renpy.translate_string("{color=#32FF32}9% bonus{/color} for PHY gaining"))
            hero "Oh{w=[wt1]}, well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} There's something{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} There is a kamasutra manual right there.{w=[wt1]}{nw}"
            $ wpre_mood = "O2"
            $ wpre_fx = 2
            $ add_stat("wpre", "lust", 1)
            $ add_stat("hero", "cha_soc", 0.1)
            hero "Oh, well... there's something... There is a kamasutra manual right there.{fast}{w=[wt3]} Is that a section of erotic books?"
            wpre "{aw}Ehhh...!?{/aw}{w=[wt3]} Y{w=[wt1]}-you're right{w=[wt2]}, there is really such a section of books.{w=[wt3]}"

    hero "By the way{w=[wt1]}, let's get going?"
    wpre "Of course.{w=[wt2]} Lead the way!"
    $ add_stat("wpre", "inti", 1)
    $ hero_fx = 0
    $ wpre_fx = 0
    $ hero_mood = "A1"
    $ wpre_mood = "A1"
    jump show_ui
    
#---------------------------------------------------------------------------
label schoolday_1_1_classroom:
#---------------------------------------------------------------------------
    call hide_ui from _call_hide_ui_174
    if "library" in scenestep and "courtyard" in scenestep and wpre_is_flw:

        $ add_stat("wpre", "inti", 3)
        show HERO at LC
        show WPRE at RC
        with Fade(1,0,3)
        
        wpre "I'm feeling a mix of excitement and nervousness about starting our first day of high school.{w=[wt3]} I hope to make the most out of this experience!{w=[wt2]} It's a big step forward, don't you think?"
        $ hero_fx = 1
        $ hero_mood = "A2"
        hero "S{w=[wt1]}-sure!"
        $ hero_mood = "A1"
        wpre "I want to sincerely thank you for accompanying me around.{w=[wt2]} I must say{w=[wt1]}, exploring the school with you has been quite enjoyable!{w=[wt3]} I'm looking forward to our classes and the journey ahead."

        $ wpre_is_flw = False
        $ msg.msg(renpy.translate_string("{nm}[fnamewpre]{/nm} is no longer following you"))

        scene bg_0
        with Dissolve (2)
        jump schoolday_1_1_end

    elif wpre_is_flw == False:
        menu:
            "Continue exploring the school area":
                call goto_school_hallway2 from _call_goto_school_hallway2_1
                jump show_ui

            "Finish exploring the school area":
                scene bg_0
                with Dissolve (2)
                jump schoolday_1_1_end

    else:        
        show HERO at LC
        show WPRE at RC
        with fade

        $ wpre_mood = "A2"
        
        wpre "Hm?...{w=[wt2]} Why did we come to the classroom?...{w=[wt2]} Are you tired of exploring?{w=[wt2]} I think we still have time to walk a little more..."
        menu:
            "Continue exploring the school area":
                hero "Yes{w=[wt1]}, sure!{nw}"

                $ wpre_mood = "A1"                
                hero "Yes, sure!{fast} I just came to see a little thing.{w=[wt2]} Let's go back?"
                call goto_school_hallway2 from _call_goto_school_hallway2_2
                jump show_ui

            "Finish exploring the school area":
                $ hero_mood = "O1"
                $ wpre_is_flw = False
                $ msg.msg(renpy.translate_string("{nm}[fnamewpre]{/nm} is no longer following you"))
                hero "Oh{w=[wt1]}, is there any area left to explore?...{w=[wt2]} I think it's better to stay here and not to be delayed to the class."
                if not "library" in scenestep[1]:
                    $ a_event_0 += 2
                if not "courtyard" in scenestep[1]:
                    $ a_event_0 += 1
                $ wpre_mood = "O2"
                $ add_stat("wpre", "love", -a_event_0)
                $ add_stat("hero", "cha_soc", -a_event_0)
                wpre "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} S{w=[wt1]}-sure...{w=[wt3]} I apologize for taking your time, {nm}[fnamehero]{/nm}.{w=[wt2]} Have a good day."
                show WPRE at OR_slow
                hero "..."

                scene bg_0
                with Dissolve (2)
                
                jump schoolday_1_1_end

    $ hero_fx = 0
    $ wpre_fx = 0
    $ hero_mood = "A1"
    $ wpre_mood = "A1"
    jump show_ui

#---------------------------------------------------------------------------
label schoolday_1_1_end:
#---------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------
    # Classroom
    #----------------------------------------------------------------------------------------------------
    if "hallway2" in scenestep:
        $ scenestep.remove("hallway2")
    if "courtyard" in scenestep:
        $ scenestep.remove("courtyard")
    if "library" in scenestep:
        $ scenestep.remove("library")

    call hide_ui from _call_hide_ui_175

    #$ _skipping = False
    #$ minigamestep = "schoolday_1_1_skip_1"
    #$ PercentData = 0
    #$ PercentAdd = 0
    #show screen SkipScene

    #pause (1)

    $ a_check_1 = "Teacher"

    sup1 "Good morning.{w=[wt2]} Welcome to the first day of class.{w=[wt3]} Today we will have just a few presentations and decision-makings for the school year during this first class time.{w=[wt3]} After that{w=[wt1]}, we will attend the opening ceremony in the auditorium{w=[wt2]}, But first{w=[wt1]}, we will have to establish a few positions."

    sup1 "Well{w=[wt1]}, the main thing is to decide who'll be the Class President.{w=[wt3]} I know that most of you here in Classroom B are new at the institution{w=[wt2]}, so most of you may not know each other.{w=[wt2]} But we still need to have one as soon as possible{w=[wt2]}, so all of us can forward to the auditorium and let me go have a coffee for breakfast."

    sup1 "Allow me to remind you that the Class President will be responsible for the contact between the class and the teachers.{w=[wt3]} They will be assigned some exclusive reporting tasks for teachers.{w=[wt3]} In addition{w=[wt1]}, they will need to be at the Student Council at least three times a week{w=[wt1]}, being available to attend to other students."

    sup1 "Because of this{w=[wt1]}, the Class President is exempted from monthly tuition fee{w=[wt2]}, and of course{w=[wt1]}, this activity also counts in the curriculum.{w=[wt3]} Devoted students who fulfill their role in P.A.N.T.I.E.S Student Council tend to enter the best universities and get the most renowned jobs."

    mind "(Woow...{w=[wt3]} This is a very important decision!{w=[wt2]} It seems to be something very laborious{w=[wt1]}, but it can be good for those who need to save money.{w=[wt2]} If I ran for Class President{w=[wt1]}, perhaps the tuition waiver would ease {nm}[hero_about_wmom]{/nm}'s burden...)"

    sup1 "So{w=[wt2]}, anyone running for Class President?{w=[wt2]} Hurry up and raise your hand cos I don't have all the time in the world."

    stop BGM fadeout 3

    $ zoomS1 = 5
    $ zoomT1 = 0
    $ zoomX1 = 0.9
    $ zoomY1 = 0.35
    $ zoomS2 = 1
    $ zoomT2 = 7
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1

    show schoolday_1_1classroom at ZoomSTXY
    with Dissolve(3)

    play BGM "audio/W2C - Subtitle.mp3"

    mind "(W{w=[wt1]}-wait!{w=[wt2]} Is that{w=[wt1]}-{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}){nw}"

    mind "(W-wait! Is that-...){fast}"
    wpre "I{w=[wt1]}-I would like to apply, Ma'am!"
    sup1 "Good.{w=[wt2]} What's your name, Miss?"
    wpre "{nm}[fnamewpre] [lnamewpre]{/nm}{w=[wt1]}, Ma'am!"
    sup1 "Nice.{w=[wt2]} Since no one else volunteered, it's decided!{w=[wt3]} {nm}Miss. [fnamewpre] [lnamewpre]{/nm} is our Class President and we'll decide later if a Vice-President is needed.{w=[wt2]} Now{w=[wt1]}, everyone to the auditorium{w=[wt2]}, {pa}Hurry!{/pa}"

    mind "({aw}Ehh!?{/aw}{w=[wt2]} Without presentations or anything?{w=[wt3]} I can see this woman is completely fed up with work on the very first day of school!)"

    stop BGM fadeout 3
    scene bg_0
    with Dissolve(1)

    pause 2

    #----------------------------------------------------------------------------------------------------
    # Auditorium 1
    #----------------------------------------------------------------------------------------------------
    label schoolday_1_1_skip_1:
        $ PercentData = 0
        $ PercentAdd = 0
        $ minigamestep = "schoolday_1_1_skip_2"
    #----------------------------------------------------------------------------------------------------

    play BGM "audio/W2C - Tranquility.mp3"

    mind "(So this is the auditorium...{w=[wt4]} Oh{w=[wt1]}, there is {nm}[fnamewpre]{/nm}!{w=[wt2]} Maybe I have a good topic to talk now.)"
    hero "Yo, {nm}[fnamewpre]{/nm}!{w=[wt2]} Can I sit here?"
    wpre "Of course, {nm}[fnamehero]{/nm}!{w=[wt2]} Please."

    $ zoomS1 = 1
    $ zoomT1 = 0
    $ zoomX1 = 1.0
    $ zoomY1 = 0.4
    $ zoomS2 = 1.75
    $ zoomT2 = 0
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1


    scene schoolday_1_1auditorium_bg 1a at ZoomSTXY
    show schoolday_1_1auditorium_wprebody 1 at ZoomSTXY
    show schoolday_1_1auditorium_wpreface a0 at ZoomSTXY
    show schoolday_1_1auditorium_herobody 1 at ZoomSTXY
    show schoolday_1_1auditorium_heroface a0 at ZoomSTXY
    show schoolday_1_1auditorium_heroeyes r at ZoomSTXY
    with Dissolve(2)

    show schoolday_1_1auditorium_heroface a1
    hero "That was a surprise that you applied for Class President.{w=[wt2]} Won't it get in the way of your work?"

    show schoolday_1_1auditorium_heroface a0
    show schoolday_1_1auditorium_wpreface a1
    wpre "Y{w=[wt1]}-yes.{w=[wt2]} Maybe I rushed a little...{w=[wt3]} I thought about the fact that the extracurricular activity of the Student Council does weigh quite a lot in the curriculum{w=[wt1]}, so...{w=[wt3]} That's something I'd really like to invest in!{w=[wt2]} I just need to adjust my time with my boss."

    show schoolday_1_1auditorium_heroface a1
    show schoolday_1_1auditorium_wpreface a0
    if stat_cha >= 10:
        hero "I'm sure you'll do well!"
        show schoolday_1_1auditorium_heroface a0
        show schoolday_1_1auditorium_wpreface a1
        $ add_stat("wpre", "love", 1)
        $ add_stat("hero", "cha_soc", 1)
        wpre "Thank you, {nm}[fnamehero]{/nm}.{w=[wt2]} I'll do my best!{nw}"
        show schoolday_1_1auditorium_wpreface a0
        wpre "Thank you, {nm}[fnamehero]{/nm}.{w=[wt2]} I'll do my best!{fast}"

    else:
        hero "Got it!"

    show schoolday_1_1auditorium_heroface a0
    show schoolday_1_1auditorium_wpreface a1
    if wpre_love >= 5:
        $ add_stat("wpre", "inti", 1)
        wpre "By the way{w=[wt2]}, I think it'd be cool if you join the Student Council with me, {lg} Hi Hi Hi... {/lg}{w=[wt3]} {aw}N{w=[wt1]}-Not that I'm intruding on your life decisions!{/aw}{w=[wt3]} That was j{w=[wt1]}-just a c{w=[wt1]}-comment!"
    elif wpre_love >= 0:
        wpre "By the way{w=[wt2]}, The teacher said we can still need a Vice-President.{w=[wt2]} So, maybe you could apply as well."
    else:
        wpre "So{w=[wt2]}, are you looking forward the ceremony?"
    stop BGM fadeout 2

    show schoolday_1_1auditorium_heroface a2
    show schoolday_1_1auditorium_wpreface a0
    hero "Well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}. I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}-{nw}"

    #----------------------------------------------------------------------------------------------------
    #$ pygame.event.set_allowed(None)
    #$ pygame.event.set_allowed(pygame.USEREVENT)
    play BGM "audio/W2C - Fun.mp3"

    $ zoomS1 = 1.75
    $ zoomT1 = 0
    $ zoomX1 = 1.0
    $ zoomY1 = 0.4
    $ zoomS2 = 1
    $ zoomT2 = 3
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1

    scene schoolday_1_1auditorium_bg 1a at ZoomSTXY
    hide schoolday_1_1auditorium_herobody 1 at ZoomSTXY
    show schoolday_1_1auditorium_wprebody 3 at ZoomSTXY
    show schoolday_1_1auditorium_wpreface s1 at ZoomSTXY
    show schoolday_1_1auditorium_hero_wnei_wsis_body at ZoomSTXY
    show schoolday_1_1auditorium_hero_wnei_wsis_face 1 at ZoomSTXY

    wnei "Sorry{nw}"
    show schoolday_1_1auditorium_wprebody 2
    show schoolday_1_1auditorium_wpreface s1

    #$ pygame.event.set_blocked(None)

    wnei "Sorry{fast} for before, {nm}[fnamehero]{/nm}!{w=[wt3]} I got upset with ya with no reason!"

    scene schoolday_1_1auditorium_bg 1a
    hide schoolday_1_1auditorium_herobody 1
    show schoolday_1_1auditorium_wprebody 2
    show schoolday_1_1auditorium_wpreface s1
    show schoolday_1_1auditorium_hero_wnei_wsis_body
    show schoolday_1_1auditorium_hero_wnei_wsis_face 2
    wpre "{aw}H{w=[wt1]}-hey, Miss!{w=[wt2]} T{w=[wt1]}-this is inappropriate!{/aw}"

    show schoolday_1_1auditorium_hero_wnei_wsis_face 3
    if personality[0] == "Hentai":
        wsis "{aw}{nm}[fnamewnei]{/nm}!{w=[wt1]} Stop hugging this pervert like this!{/aw}"
    else:
        wsis "{aw}{nm}[fnamewnei]{/nm}!{w=[wt1]} Stop hugging him like this!{/aw}"

    show schoolday_1_1auditorium_hero_wnei_wsis_face 4
    wnei "But ya said I should apologize!"

    pause (0.5)
    play SE1 "Boing2.mp3"
    hide schoolday_1_1auditorium_hero_wnei_wsis_body
    hide schoolday_1_1auditorium_hero_wnei_wsis_face
    show schoolday_1_1auditorium_hero_wnei 1
    show schoolday_1_1auditorium_wprebody 3
    hide schoolday_1_1auditorium_wpreface
    show schoolday_1_1auditorium_wsisbody 1
    show schoolday_1_1auditorium_wsisface o0
    pause(0.3)
    play SE1 "Hit2.mp3"
    show schoolday_1_1auditorium_hero_wnei 2
    show schoolday_1_1auditorium_wpre 4
    hide schoolday_1_1auditorium_wprebody
    hide schoolday_1_1auditorium_wpreface
    with vpunch

    show schoolday_1_1auditorium_wsisface o1
    wsis "{aw}I{w=[wt1]}-I didn't say anything{w=[wt1]}, you liar!{/aw}"

    show schoolday_1_1auditorium_wsisface o0
    wnei "H{w=[wt1]}-hey{w=[wt2]}, ya can't press m{w=[wt1]}-my{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}"

    $ renpy.pause(0.25, hard=True)
    play SE1 "Boing1.mp3"
    show schoolday_1_1auditorium_hero_wnei 3a
    with Dissolve(0.08)
    show schoolday_1_1auditorium_hero_wnei 3b
    with Dissolve(0.08)
    show schoolday_1_1auditorium_hero_wnei 3c
    with Dissolve(0.08)
    $ renpy.pause(0.5, hard=True)
    hero "S{w=[wt1]}-sorry!{w=[wt3]} B{w=[wt1]}-by the way{w=[wt2]}, sit here and let me introduce you girls to {nm}[fnamewpre]{/nm}!"

    #----------------------------------------------------------------------------------------------------
    # Auditorium 2
    #----------------------------------------------------------------------------------------------------
    label schoolday_1_1_skip_2:
        if PercentData == 100:
            play BGM "audio/W2C - Fun.mp3"
        $ PercentData = 0
        $ PercentAdd = 0
        $ minigamestep = "schoolday_1_1_skip_3"
    #----------------------------------------------------------------------------------------------------

    $ zoomS1 = 10
    $ zoomT1 = 0
    $ zoomX1 = 0.65
    $ zoomY1 = 0.6
    $ zoomS2 = 1
    $ zoomT2 = 3
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1

    scene schoolday_1_1auditorium_bg 2 at ZoomSTXY
    show schoolday_1_1auditorium_bghero 1 at ZoomSTXY
    show schoolday_1_1auditorium_bgwpre 1 at ZoomSTXY
    show schoolday_1_1auditorium_bgwsis 1 at ZoomSTXY
    show schoolday_1_1auditorium_bgwnei 1a at ZoomSTXY
    show schoolday_1_1auditorium_fg at ZoomSTXY
    show schoolday_1_1auditorium_hprv 1a at ZoomSTXY
    show schoolday_1_1auditorium_hprvface 1 at ZoomSTXY
    show schoolday_1_1auditorium_wota 1a at ZoomSTXY
    show schoolday_1_1auditorium_wotaface1 2 at ZoomSTXY
    show schoolday_1_1auditorium_wdis 1a at ZoomSTXY
    show schoolday_1_1auditorium_wdisface1 1 at ZoomSTXY
    with pixellate

    wota "Hmp!{w=[wt2]} Who is that boy with silly face?{w=[wt2]} How dare he put those dirty hands on a pure princess!?"

    scene schoolday_1_1auditorium_bg 2
    show schoolday_1_1auditorium_bghero 1
    show schoolday_1_1auditorium_bgwpre 1
    show schoolday_1_1auditorium_bgwsis 1
    show schoolday_1_1auditorium_bgwnei 1a
    show schoolday_1_1auditorium_fg
    show schoolday_1_1auditorium_hprv 1a
    show schoolday_1_1auditorium_hprvface 1
    show schoolday_1_1auditorium_wota 1a
    show schoolday_1_1auditorium_wotaface1 1
    show schoolday_1_1auditorium_wdis 1c
    hide schoolday_1_1auditorium_wdisface1
    wdis "I think he's from our class.{w=[wt1]} Look!{w=[wt2]} He is chatting to our classroom president."

    show schoolday_1_1auditorium_wota 1a
    show schoolday_1_1auditorium_wotaface1 2
    show schoolday_1_1auditorium_wdis 1a
    show schoolday_1_1auditorium_wdisface1 1
    wota "Damn jerk!{w=[wt2]} Stop hitting on every good girl you see on the way!"

    show schoolday_1_1auditorium_wota 2a
    show schoolday_1_1auditorium_wdis 2b
    hide schoolday_1_1auditorium_wotaface1
    show schoolday_1_1auditorium_wotaface2 o0
    show schoolday_1_1auditorium_wdisface s1
    hide schoolday_1_1auditorium_wdisface1
    wdis "{aw}B{w=[wt1]}-but w-what if he's {color=#64C8FF}[fnamewnei]{/color}'s b{w=[wt1]}-b{w=[wt1]}-boyfriend?{/aw}"

    show schoolday_1_1auditorium_wota 2b
    show schoolday_1_1auditorium_wdis 2b
    show schoolday_1_1auditorium_wotaface2 o2
    show schoolday_1_1auditorium_wdisface s0
    wota "S{w=[wt1]}-shut up{w=[wt1]}, baka!{w=[wt2]} {nm}[fnamewnei]-chan{/nm} is too pure to have a b{w=[wt1]}-boyfriend!!!"

    show schoolday_1_1auditorium_wota 1b
    show schoolday_1_1auditorium_wdis 1c
    show schoolday_1_1auditorium_wotaface2 o0
    hide schoolday_1_1auditorium_wdisface
    wdis "{aw}B{w=[wt1]}-b{w=[wt1]}-but he t{w=[wt1]}-touch her b{w=[wt1]}-b{w=[wt1]}-{w=[wt1]}{/aw}{nw}"

    show schoolday_1_1auditorium_hprvfx1 1
    show schoolday_1_1auditorium_hprvface 2
    show schoolday_1_1auditorium_wota 2b
    show schoolday_1_1auditorium_wdis 2a at Scare
    show schoolday_1_1auditorium_wotaface2 o2
    show schoolday_1_1auditorium_wdisface s0 at Scare
    wota "{pa}AHHH!{w=[wt2]} SHUT UP!!!{/pa}{w=[wt3]} We don't have time to be jealous!{w=[wt2]} We need to call her to stay here with us!"

    show schoolday_1_1auditorium_wotaface2 o0
    show schoolday_1_1auditorium_wdisface o1
    show schoolday_1_1auditorium_hprvface 1
    wdis "Y{w=[wt1]}-you're right!{w=[wt3]} You know?{w=[wt2]} I feel conflicted now{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} {nm}[fnamewnei]{/nm} is in our school again{w=[wt1]}, but not in our class this year.{w=[wt3]} Also{w=[wt2]}, Why is she always with that nag?{w=[wt1]}{nw}"

    show schoolday_1_1auditorium_wota 1a
    show schoolday_1_1auditorium_wdis 1a
    show schoolday_1_1auditorium_wdisface1 2
    hide schoolday_1_1auditorium_wotaface2
    show schoolday_1_1auditorium_wotaface1 1
    hide schoolday_1_1auditorium_wdisface
    wdis "Y-you're right! You know? I feel conflicted now... {nm}[fnamewnei]{/nm} is in our school again, but not in our class this year. Also, Why is she always with that nag?{fast}{w=[wt3]} {aw}That's not fair!{/aw}"

    show schoolday_1_1auditorium_wota 1c
    show schoolday_1_1auditorium_wdis 1b
    hide schoolday_1_1auditorium_wdisface1
    hide schoolday_1_1auditorium_wotaface1
    wota "For now{w=[wt1]}, we have to rescue our baby from the claws of the {nm}Pink Demon{/nm}!{w=[wt4]} {nm}[fnamewdis]{/nm}{w=[wt2]}, You shall call her!"

    show schoolday_1_1auditorium_wota 2b
    show schoolday_1_1auditorium_wdis 2b
    show schoolday_1_1auditorium_wotaface2 o0
    show schoolday_1_1auditorium_wdisface s1
    wdis "{pa}E{w=[wt1]}-eh!?{/pa}{w=[wt3]} {aw}M{w=[wt1]}-me!?{/aw}{w=[wt3]} What if {nm}[fnamewsis]{/nm} gets mad!?{w=[wt2]} {pa}I{w=[wt1]}-I'll be her target!!!{/pa}"

    stop BGM fadeout 3
    hide schoolday_1_1auditorium_wota
    hide schoolday_1_1auditorium_wotaface2
    hide schoolday_1_1auditorium_wdisface
    show schoolday_1_1auditorium_wota 2c
    show schoolday_1_1auditorium_wotaface2 o1
    show schoolday_1_1auditorium_wdisface s0
    wota "Don't worry, baka!{w=[wt2]} I'm your friend.{w=[wt2]} You know I'm on your side!"

    play BGM "audio/W2C - Romance.mp3"
    show schoolday_1_1auditorium_wdis 2a
    show schoolday_1_1auditorium_wotaface2 o0
    hide schoolday_1_1auditorium_wdisface
    show schoolday_1_1auditorium_wdisfx
    show schoolday_1_1auditorium_wdisface a1
    hide schoolday_1_1auditorium_hprvfx1
    wdis "{nm}[fnamewota]{/nm}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} W{w=[wt1]}-would you face {nm}[fnamewsis]{/nm} to defend me?"
    show schoolday_1_1auditorium_wdisface a0
    show schoolday_1_1auditorium_wotaface2 a1
    wota "You're really an idiot, aren't you?{w=[wt4]} It is obvious that our friendship would not be limited to something as superfluous as this{w=[wt1]}, baka!{w=[wt3]} If the {nm}Pink Demon{/nm} gets you.{w=[wt2]} You can be sure{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{nw}"
    stop BGM fadeout 3
    show schoolday_1_1auditorium_wotaface2 a0
    wota "You're really an idiot, aren't you? It is obvious that our friendship would not be limited to something as superfluous as this, baka! If the {nm}Pink Demon{/nm} gets you. You can be sure...{fast}{w}{nw}"
    show schoolday_1_1auditorium_wotaface2 a1
    wota "You're really an idiot, aren't you? It is obvious that our friendship would not be limited to something as superfluous as this, baka! If the {nm}Pink Demon{/nm} gets you. You can be sure...{fast} That I'll pray for your soul!{nw}"
    play BGM "audio/W2C - Fun.mp3"
    show schoolday_1_1auditorium_wotaface2 a0
    show schoolday_1_1auditorium_wdisface o0
    wota "You're really an idiot, aren't you? It is obvious that our friendship would not be limited to something as superfluous as this, baka! If the {nm}Pink Demon{/nm} gets you. You can be sure... That I'll pray for your soul!{fast}"

    show schoolday_1_1auditorium_wota 2c
    show schoolday_1_1auditorium_wotaface2 o0
    show schoolday_1_1auditorium_wdis 2b
    show schoolday_1_1auditorium_wdisface o1
    wdis "Y{w=[wt1]}-your coward!!!{w=[wt2]} I'll do that only for {nm}[fnamewnei]{/nm}!"

    show schoolday_1_1auditorium_wota 3a
    hide schoolday_1_1auditorium_wotaface2
    show schoolday_1_1auditorium_wdis 3a
    hide schoolday_1_1auditorium_wdisface
    hide schoolday_1_1auditorium_wdisfx
    with dissolve

    show schoolday_1_1auditorium_wdis 3b
    show schoolday_1_1auditorium_bgwnei 2b
    wdis "{bt}Heeeey{w=[wt1]}, {nm}[fnamewnei]{/nm}!{/bt}{nw}"
    show schoolday_1_1auditorium_hprv 1b
    hide schoolday_1_1auditorium_hprvface
    wdis "{bt}Heeeey, {nm}[fnamewnei]{/nm}!{/bt}{fast}"

    show schoolday_1_1auditorium_wdis 3a
    show schoolday_1_1auditorium_hprv 2a
    show schoolday_1_1auditorium_bghero 2
    show schoolday_1_1auditorium_bgwpre 2
    show schoolday_1_1auditorium_bgwsis 2
    show schoolday_1_1auditorium_bgwnei 2a
    wnei "Woaah!{w=[wt2]} {nm}[fnamewdis]{/nm}!{w=[wt2]} {nm}[fnamewota]{/nm}!{w=[wt2]} Yar here!"
    show schoolday_1_1auditorium_wota 3b
    show schoolday_1_1auditorium_wotaface3 1
    pause(0.5)

    show schoolday_1_1auditorium_wotaface3 2
    show schoolday_1_1auditorium_hprv 2b
    show schoolday_1_1auditorium_bgwnei 2b
    wota "{size=-5}Hey{w=[wt1]}, you're acting {bt}sus...{/bt}{/size}"

    show schoolday_1_1auditorium_wotaface3 1
    hprv "{size=-5}H{w=[wt1]}-Hey {nm}[fnamewota]{/nm}!{w=[wt2]} I'm just picking up my dropped pen! {gg}He-he-he... {/gg}{/size}"

    show schoolday_1_1auditorium_wdis 3b
    wdis "Why don't you come sit with us?{w=[wt2]}{nw}"
    show schoolday_1_1auditorium_wota 3a
    hide schoolday_1_1auditorium_wotaface3
    wdis "Why don't you come sit with us?{fast} We've missed you so much!"

    show schoolday_1_1auditorium_hprv 2a
    show schoolday_1_1auditorium_bgwnei 2b
    wnei "{w=[wt3]}.{nw}"
    show schoolday_1_1auditorium_bgwnei 1a
    wnei ".{fast}{w=[wt3]}{nw}"
    show schoolday_1_1auditorium_bgwnei 1d
    wnei ".{fast} .{w=[wt3]}{nw}"
    show schoolday_1_1auditorium_bgwnei 2b
    wnei ". .{fast} .{w=[wt4]}{nw}"
    show schoolday_1_1auditorium_bgwnei 2a
    wnei ". . .{fast} Hey{w=[wt1]}, I prefer stay here with {nm}[fnamehero]{/nm} and {nm}[fnamewsis]{/nm}!{nw}"
    play SE1 "Hit2.ogg"
    show schoolday_1_1auditorium_wdis 3c
    with hpunch
    wnei ". . . Hey, I prefer stay here with {nm}[fnamehero]{/nm} and {nm}[fnamewsis]{/nm}!{fast}{w=[wt2]} I'll talk to ya later!"

    show schoolday_1_1auditorium_wdis 3a
    show schoolday_1_1auditorium_bgwnei 2b
    wdis "{aw}{size=-5}{color=#64C8FF}[fnamehero]{/color}, huh?{w=[wt2]}{/size}{/aw}{nw}"
    show schoolday_1_1auditorium_hprv 3a
    $ Y_pos = 300
    $ Y_spd = 3
    show schoolday_1_1auditorium_hprvphone 1 at Y_Move2
    wdis "{aw}{size=-5}{color=#64C8FF}[fnamehero]{/color}, huh?{fast}{w=[wt2]} How do you dare!?{/size}{/aw}"

    pause (0.5)
    show schoolday_1_1auditorium_hprvphone 2
    pause (1)

    show schoolday_1_1auditorium_wota 3b
    show schoolday_1_1auditorium_wotaface3 2

    show schoolday_1_1auditorium_bgwnei 1a
    show schoolday_1_1auditorium_bghero 1
    show schoolday_1_1auditorium_bgwpre 1
    show schoolday_1_1auditorium_bgwsis 1
    wota "{size=-5}Gotcha!{/size}{nw}"
    $ Y_pos = 300
    $ Y_spd = 0.1
    show schoolday_1_1auditorium_hprvphone 1 at Y_Move
    show schoolday_1_1auditorium_hprv 3b at Scare
    wota "{size=-5}Gotcha!{/size}{fast}"

    show schoolday_1_1auditorium_wotaface3 1
    show schoolday_1_1auditorium_hprv 2b
    hide schoolday_1_1auditorium_hprvphone
    hprv "{size=-5}{aw}W{w=[wt1]}-wait!{/aw}{/size}"

    hide schoolday_1_1auditorium_wotaface3
    show schoolday_1_1auditorium_wotaface1 1
    show schoolday_1_1auditorium_wota 1a
    with dissolve
    hide schoolday_1_1auditorium_wotaface1
    show schoolday_1_1auditorium_wota 1c
    wota "{size=-5}Do you still bring those snacks in your bag?{w=[wt2]} If you now give me one{w=[wt1]}, I may allow you to go unpunished.{/size}"
    show schoolday_1_1auditorium_wota 1a
    show schoolday_1_1auditorium_wotaface1 1
    show schoolday_1_1auditorium_hprv 4
    hprv "{size=-5}{aw}S{w=[wt1]}-sure!{w=[wt2]} I{w=[wt1]}-it's all y{w=[wt1]}-yours!!!{/aw}{/size}"

    show schoolday_1_1auditorium_hprv 1a
    show schoolday_1_1auditorium_hprvface 1
    show schoolday_1_1auditorium_wota 3c
    hide schoolday_1_1auditorium_wotaface1
    $ Y_spd = 10
    $ Y_pos = 50
    show schoolday_1_1auditorium_hprvfx2 at Y_Move
    with dissolve

    show schoolday_1_1auditorium_bgwnei 2b
    show schoolday_1_1auditorium_bgwsis 2
    show schoolday_1_1auditorium_bgwpre 2
    show schoolday_1_1auditorium_bghero 2
    wota "{bt}Heeeey, {color=#64C8FF}[fnamewnei]-chan{/color}!{/bt}{w=[wt2]} Look what I bought for us to eat together!"

    show schoolday_1_1auditorium_bgwnei 2c
    wnei "{pa}W{w=[wt1]}-Woaah!!!{/pa}{w=[wt3]}{nw}"
    show schoolday_1_1auditorium_bgwnei 1b
    wnei "{pa}W-Woaah!!!{/pa}{fast} Yo{w=[wt1]}, {nm}[fnamehero]{/nm}{w=[wt2]}{nw}"
    show schoolday_1_1auditorium_bgwnei 1c
    wnei "{pa}W-Woaah!!!{/pa} Yo, {nm}[fnamehero]{/nm}{fast}, {nm}[fnamewsis]{/nm}{w=[wt2]}{nw}"
    show schoolday_1_1auditorium_bgwnei 1b
    wnei "{pa}W-Woaah!!!{/pa} Yo, {nm}[fnamehero]{/nm}, {nm}[fnamewsis]{/nm}{fast}, and{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} H{w=[wt1]}-huh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} {nm}New girl{/nm}!{w=[wt2]} I'll talk to ya guys later!{w=[wt2]} See ya!"

    hide schoolday_1_1auditorium_bgwnei
    with dissolve
    show schoolday_1_1auditorium_wota 2b
    show schoolday_1_1auditorium_wotaface2 a0
    show schoolday_1_1auditorium_wdis 2b
    show schoolday_1_1auditorium_wdisface a2
    wdis "You did it!!!"

    show schoolday_1_1auditorium_wota 2a
    show schoolday_1_1auditorium_wotaface2 o1
    show schoolday_1_1auditorium_wdisface a0
    wota "But where will she sit?"

    show schoolday_1_1auditorium_wotaface2 o0
    hide schoolday_1_1auditorium_wdisface
    show schoolday_1_1auditorium_wdisfx
    show schoolday_1_1auditorium_wdisface a2
    wdis "I{w=[wt1]}-in my lap!{nw}"
    show schoolday_1_1auditorium_hprvfx1 1
    show schoolday_1_1auditorium_wdisface a0
    wdis "I-in my lap!{fast}"

    show schoolday_1_1auditorium_wota 2a
    wota "{w=[wt2]}.{w=[wt2]} .{w=[wt2]} .{w=[wt3]}{nw}"
    show schoolday_1_1auditorium_wota 2b
    show schoolday_1_1auditorium_wotaface2 a1
    wota ". . .{fast} H{w=[wt1]}-hey!{w=[wt1]} Before {nm}[fnamewnei]-chan{/nm} gets here{w=[wt1]}, lemme tell you something super cool gossip!{w=[wt3]} Did you see where {nm}[fnamewgal]{/nm} stood when we went here?"

    show schoolday_1_1auditorium_wotaface2 a0
    show schoolday_1_1auditorium_wdisface a1
    wdis "She was chatting on the balcony, right?"

    show schoolday_1_1auditorium_wotaface2 a1
    show schoolday_1_1auditorium_wdisface a0
    wota "Without panties!{w=[wt2]}{nw}"
    show schoolday_1_1auditorium_hprvface 2
    show schoolday_1_1auditorium_hprvfx1 2
    show schoolday_1_1auditorium_wdisface s0
    wota "Without panties!{fast} Anyone from downstairs can easily see{nw}"
    show schoolday_1_1auditorium_hprvfx3 at Y_Move
    wota "Without panties! Anyone from downstairs can easily see{fast} {bt}everything{/bt} if they look up!"

    show schoolday_1_1auditorium_wotaface2 a0
    show schoolday_1_1auditorium_hprvfx4 at Y_Move
    show schoolday_1_1auditorium_hprv 1c
    show schoolday_1_1auditorium_wdisface s1
    wdis "Oh{w=[wt1]}, God!{w=[wt2]}"

    show schoolday_1_1auditorium_wdisface s0
    show schoolday_1_1auditorium_hprv 5
    hide schoolday_1_1auditorium_hprvface
    hide schoolday_1_1auditorium_hprvfx1
    hide schoolday_1_1auditorium_hprvfx2
    hide schoolday_1_1auditorium_hprvfx3
    hide schoolday_1_1auditorium_hprvfx4
    hprv "(cof     ){fast}{w=[wt2]}{nw}"
    hprv "(cof cof){fast}{w=[wt2]}{nw}"

    hide schoolday_1_1auditorium_hprv
    with dissolve

    show schoolday_1_1auditorium_wotaface2 o2
    wota "Now!{w=[wt2]} Scoot over!{w=[wt2]} {pa}Hurry!!!{/pa}"

    show schoolday_1_1auditorium_wdisface s1
    show schoolday_1_1auditorium_wotaface2 a0
    wdis "{pa}E{w=[wt1]}-eh!?!?{/pa}"

    show schoolday_1_1auditorium_wdis 4
    show schoolday_1_1auditorium_wdisface4 1
    hide schoolday_1_1auditorium_wdisface
    hide schoolday_1_1auditorium_wdisfx
    with dissolve
    pause (0.5)
    show schoolday_1_1auditorium_wdisface4 2
    pause (0.5)

    wnei "Yo!!{w=[wt2]} Ya saved a place for me!"

    hide schoolday_1_1auditorium_wdisface4
    hide schoolday_1_1auditorium_wdis
    hide schoolday_1_1auditorium_wota
    hide schoolday_1_1auditorium_wotaface2
    show schoolday_1_1auditorium_wnei_wdis_wota_bg
    show schoolday_1_1auditorium_wnei_wdis_wota_face 1
    show schoolday_1_1auditorium_wnei_wdis_wota_hands 1
    show schoolday_1_1auditorium_wnei_wdis_wota_head 1
    with dissolve

    wdis "Everything for you, Honey!"
    wota "I'm your onee-chan{w=[wt1]}, baka!"

    pause (0.5)
    play SE1 "Hit1.mp3"
    show schoolday_1_1auditorium_wnei_wdis_wota_hands 2
    with dissolve
    pause (1.5)

    show schoolday_1_1auditorium_hsecbody at LL
    show schoolday_1_1auditorium_hsechand 1 at LL
    show schoolday_1_1auditorium_hsecbody at CC_slow
    show schoolday_1_1auditorium_hsechand 1 at CC_slow
    show schoolday_1_1auditorium_wnei_wdis_wota_face 2
    "Hey{w=[wt1]}, you.{w=[wt3]} No food in the auditorium!{nw}"
    show schoolday_1_1auditorium_hsecbody at OL_slow
    show schoolday_1_1auditorium_hsechand 2 at OL_slow
    show schoolday_1_1auditorium_wnei_wdis_wota_hands 3
    show schoolday_1_1auditorium_wnei_wdis_wota_head 2
    "Hey, you. No food in the auditorium!{fast}"
    show schoolday_1_1auditorium_wnei_wdis_wota_face 3
    with dissolve

    wnei "Eh?..."

    #----------------------------------------------------------------------------------------------------
    # Auditorium 3
    #----------------------------------------------------------------------------------------------------
    label schoolday_1_1_skip_3:
        $ PercentData = 0
        $ PercentAdd = 0
        $ minigamestep = "schoolday_1_1_skip_4"
    #----------------------------------------------------------------------------------------------------
    $ zoomS1 = 1
    $ zoomT1 = 0
    $ zoomX1 = 0.15
    $ zoomY1 = 0.5
    $ zoomS2 = 1.75
    $ zoomT2 = 0
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1

    scene schoolday_1_1auditorium_bg 1b at ZoomSTXY
    show schoolday_1_1auditorium_wprebody 1 at ZoomSTXY
    show schoolday_1_1auditorium_herobody 1 at ZoomSTXY
    show schoolday_1_1auditorium_heroface a0 at ZoomSTXY
    show schoolday_1_1auditorium_heroeyes l at ZoomSTXY
    show schoolday_1_1auditorium_wsis 2a at ZoomSTXY
    with Dissolve(1)

    show schoolday_1_1auditorium_wsis 2b
    wsis "Hmp!{w=[wt2]} Take that, you little traitor!"

    show schoolday_1_1auditorium_wsis 2a
    show schoolday_1_1auditorium_heroface a1
    hero "Hey{w=[wt1]}, {nm}[hero_to_wsis]{/nm}{w=[wt2]}, sit here!"

    show schoolday_1_1auditorium_wsis 2b
    show schoolday_1_1auditorium_heroface a0
    wsis "Huh?{w=[wt2]} Aren't you too full of yourself!?{w=[wt3]} Why am I the one who have to move closer to you{w=[wt1]}, moron?"

    show schoolday_1_1auditorium_wsis 2a
    show schoolday_1_1auditorium_heroface a2
    hero "Alright...{w=[wt3]}{nw}"

    $ zoomS1 = 1.75
    $ zoomT1 = 0
    $ zoomX1 = 0.15
    $ zoomY1 = 0.5
    $ zoomS2 = 1.75
    $ zoomT2 = 2
    $ zoomX2 = 1.0
    $ zoomY2 = zoomY1

    scene schoolday_1_1auditorium_bg 1b at ZoomSTXY
    show schoolday_1_1auditorium_wprebody 1 at ZoomSTXY
    show schoolday_1_1auditorium_wpreface a0 at ZoomSTXY
    show schoolday_1_1auditorium_herobody 2 at ZoomSTXY
    show schoolday_1_1auditorium_heroface 2a at ZoomSTXY
    show schoolday_1_1auditorium_wsis 2a at ZoomSTXY
    hide schoolday_1_1auditorium_heroeyes

    hero "Alright... {fast} Hey, {nm}[fnamewpre]{/nm}{w=[wt2]}, would you mind scooting over a little to this side?"

    $ zoomS1 = 1.75
    $ zoomT1 = 0
    $ zoomX1 = 1.0
    $ zoomY1 = 0.5
    $ zoomS2 = 1
    $ zoomT2 = 2
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1

    scene schoolday_1_1auditorium_bg 1b at ZoomSTXY
    hide schoolday_1_1auditorium_wprebody
    hide schoolday_1_1auditorium_wpreface
    hide schoolday_1_1auditorium_herobody
    hide schoolday_1_1auditorium_heroface
    show schoolday_1_1auditorium_hine at ZoomSTXY
    show schoolday_1_1auditorium_wsis 2c at ZoomSTXY
    show schoolday_1_1auditorium_wpre 5a at ZoomSTXY
    show schoolday_1_1auditorium_herobody 2 at ZoomSTXY
    show schoolday_1_1auditorium_heroface 2b at ZoomSTXY

    wpre "Of course not!{w=[wt2]} Let's{w=[wt1]}-{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"

    show schoolday_1_1auditorium_wpre 5b
    wpre "Of course not! Let's-...{fast} O{w=[wt1]}-oh{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{nw}"

    show schoolday_1_1auditorium_heroface 2c
    wpre "Of course not! Let's-... O-oh...{fast}"

    # Antibug
    scene schoolday_1_1auditorium_bg 1b
    hide schoolday_1_1auditorium_wprebody
    hide schoolday_1_1auditorium_wpreface
    hide schoolday_1_1auditorium_herobody
    hide schoolday_1_1auditorium_heroface
    show schoolday_1_1auditorium_hine
    show schoolday_1_1auditorium_wsis 2c
    show schoolday_1_1auditorium_wpre 5a
    show schoolday_1_1auditorium_herobody 2
    show schoolday_1_1auditorium_heroface 2b

    show schoolday_1_1auditorium_wsis 2d
    with dissolve
    hide schoolday_1_1auditorium_wpre 1
    show schoolday_1_1auditorium_wprebody 1
    show schoolday_1_1auditorium_wpreface a0
    with dissolve
    show schoolday_1_1auditorium_herobody 1
    show schoolday_1_1auditorium_heroface a3
    show schoolday_1_1auditorium_heroeyes c
    with dissolve
    mind "({w=[wt2]}. {w=[wt2]}. {w=[wt2]}. {w=[wt4]}I feel like with every passing minutes{w=[wt2]}, the atmosphere just gets more and more awkward.)"

    #----------------------------------------------------------------------------------------------------
    # Hallway
    #----------------------------------------------------------------------------------------------------
    label schoolday_1_1_skip_4:
        $ PercentData = 0
        $ PercentAdd = 0
        $ minigamestep = "schoolday_1_1_skip_5"
    #----------------------------------------------------------------------------------------------------

    stop BGM fadeout 3
    scene bg_0
    with Dissolve(3)

    play BGM "audio/W2C - Tranquility.mp3"

    mind "(The entrance ceremony was not very long.{w=[wt2]} Basically{w=[wt2]}, the principal just said everything that {nm}[fnamewpre]{/nm} has already explained to me.{w=[wt3]} It's amazing how that girl seems to know just about anything.{w=[wt3]} I believe the Student Council will be pleased with her.)"

    
    $ hero_mood = "A1"
    $ wpre_mood = "A1"
    $ wsis_mood = "O1"
    $ wnei_mood = "A1"
    $ wdis_mood = "A1"
    $ wota_mood = "A1" 
    $ hero_fx = 0
    $ wsis_fx = 0

    scene bg_school hallway1
    show WDIS at LC
    show WOTA at LL
    $ X_pos = 2800
    show HERO at X
    $ X_pos = 2200
    show WSIS at X
    $ X_pos = 3400
    show WPRE at X
    $ X_pos = 400
    show WNEI at X

    $ X_pos = 1100
    show WSIS at X_heavy
    $ X_pos = 1400
    show HERO at X_heavy
    show WPRE at RR_heavy
    with Dissolve(2)
    mind "(Oh{w=[wt1]}, {nm}[fnamewnei]{/nm} is there with those girls!)"

    $ X_pos = 1250
    show WNEI at X_slow
    wnei "Heeey!{w=[wt2]} I was waiting for you!"
    $ X_pos = 1000
    show WSIS at X_slow
    $ wsis_mood = "O2"
    wsis "Hunf!{w=[wt2]} I don't care!"

    $ wnei_mood = "O1"
    $ wdis_mood = "O1"
    $ wota_mood = "O1"
    wnei "A{w=[wt1]}-are you upset with me?"

    $ wsis_mood = "O1"
    wsis "{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt2]} N{w=[wt1]}-no!{w=[wt2]} S{w=[wt1]}-sorry...{w=[wt2]} L{w=[wt1]}-let's go back to our classroom, okay?"

    $ wnei_mood = "A1"
    wdis "{size=-5}That was close...{/size}"
    wota "{size=-5}We're alive!{/size}"

    show WOTA at Scare
    show WDIS at Scare

    wsis "{pa}What the idiots are whispering!?{/pa}"

    $ wota_mood = "A2"
    wota "T{w=[wt1]}-that w{w=[wt1]}-we love {nm}[fnamewnei]{/nm}!"

    $ wdis_mood = "A2"
    wdis "Y{w=[wt1]}-yes!{w=[wt2]} A{w=[wt1]}-and t{w=[wt1]}-t{w=[wt1]}-the b{w=[wt1]}-best thing we d{w=[wt1]}-did was replace {color=#64C8FF}[fnamehprv]{/color} with her!{nw}"

    show WOTA at Hit_R
    play SE1 "Hit1.ogg"
    show WDIS at Hurt_R

    $ wdis_mood = "O2"
    $ wota_mood = "O3"

    wdis "-yes! A-and t-t-the b-best thing we d-did was replace {color=#64C8FF}[fnamehprv]{/color} with her!{fast}{w=[wt1]} {aw}{b}Ouch!{/b}{/aw}"
    wsis "Eh!?{w=[wt2]} Wasn't that pervert with you?"

    $ wota_mood = "A1"
    wota "H{w=[wt2]}-he must have gone after {nm}[fnamewgal]{/nm} after I said she was without panties on the balcony..."

    $ wpre_mood = "O3"
    $ wsis_mood = "O2"
    wpre "That was very inelegant!{w=[wt2]} You should be punished for spreading such rumors about{pr}people!"

    $ wdis_mood = "O2"
    $ wota_mood = "O2"
    $ wsis_mood = "O3"
    wota "Ehh!?... I{w=[wt1]}-I{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."

    $ wpre_mood = "O2"
    $ hero_mood = "O1"
    wsis "Hunf!{w=[wt1]} If it's about this bitch{w=[wt1]}, then I can't tell if it's not true.{w=[wt2]} Hey{w=[wt2]}, was the redhead jerk with her?..."

    $ wdis_fx = 1
    $ wdis_mood = "O3"
    $ wota_mood = "O3"
    $ wnei_mood = "O1"
    wdis "His name is {color=#64C8FF}[fnamehriv]{/color}!!{w=[wt2]} And {b}YES{/b}{w=[wt2]}, he was!{w=[wt3]} And {b}NO{/b}!{w=[wt2]} H{w=[wt1]}-he's {b}NOT{/b} a jerk!{w=[wt2]} {pr}{pa}HE'S PERFECT, OKAY!?{/pa}"

    stop BGM fadeout 3

    $ wsis_mood = "O4"
    $ wota_mood = "O2"
    wsis "Enough of this crap!{w=[wt2]} You know that those jerks must be bullying the other idiot!{w=[wt3]} Hey{w=[wt1]}, {nm}[fnamewnei]{/nm}{w=[wt1]}, stay with {nm}[fnamehero]{/nm}.{nw}"
    show WSIS at OR_average
    wsis "Enough of this crap! You know that those jerks must be bullying the other idiot! Hey, {nm}[fnamewnei]{/nm}, stay with {nm}[fnamehero]{/nm}.{fast}"

    play BGM "audio/W2C - Adrenaline.mp3"

    wnei "W{w=[wt1]}-where will you go, {nm}[fnamewsis]{/nm}!?{w=[wt2]} Heey!!!"
    wota "That's bad.{w=[wt2]} She's certainly going there..."
    wdis "Ohh{w=[wt1]}, {aw}this girl gets on my nerves!!!{/aw}{w=[wt3]} If she does something with {nm}[fnamehriv]{/nm}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}."
    $ wdis_mood = "O1"
    show HERO at X_slow
    hero "E{w=[wt1]}-excuse me{w=[wt2]}, can you explain us what's happening?..."
    $ wdis_mood = "O3"
    wdis "For sure, {nm}[fnamewsis]{/nm} is going to start a fight or do some kind of bullshit!!{w=[wt3]} Oh, God!{w=[wt2]} I'll hate her so much if she puts a finger on {nm}[fnamehriv]{/nm}!!!{w=[wt4]} You're close to her, right?{w=[wt2]} Don't let her do any stupid thing!{w=[wt2]} Follow her!!!"
    hero "{aw}Ehhh...!?{/aw}{w=[wt2]} S{w=[wt1]}-sure!{nw}"
    show HERO at OR_average
    hero "{aw}Ehhh...!?{/aw} S-sure!{fast}"

    wpre "Could you better explain the whole situation?"

    $ wota_mood = "A3"
    show WOTA at LC_slow
    show WDIS at LL_slow
    wota "I'm glad you asked.{w=[wt4]}{nw}"
    $ wota_mood = "O1"
    wota "I'm glad you asked.{fast} {aw}AHEM!{/aw}{w=[wt3]} I will summarize the situation for you..."

    scene bg_0
    with Dissolve(1)
    pause (0.5)
    wota "Apparently{w=[wt2]}, the most devotee worshiper of the {nm}Pink Demon{/nm} has been captured by the{pr}{bt}{color=#64C8FF}Super Hot And Sexy Husbando Material{/color}{/bt}!{w=[wt4]} I{w=[wt1]}-I mean...{w=[wt3]} by t{w=[wt1]}-the {nm}Fallen Prince{/nm}{w=[wt3]}, who is under the command of the {nm}Slut Succubus{/nm}{w=[wt2]}, her arch-nemesis!{w=[wt4]} Then{w=[wt1]}, the {nm}Pink Demon{/nm}{w=[wt2]} is going in rescue of her worshiper{w=[wt2]}, and when they meet{w=[wt2]}.{w=[wt2]}.{w=[wt2]}."

    #----------------------------------------------------------------------------------------------------
    # LockerRoom
    #----------------------------------------------------------------------------------------------------
    label schoolday_1_1_skip_5:
        if PercentData == 100:
            play BGM "audio/W2C - Adrenaline.mp3"
        $ PercentData = 0
        $ PercentAdd = 0
        $ minigamestep = 0
        #hide screen SkipScene

    #$ pygame.event.set_allowed(None)
    #$ pygame.event.set_allowed(pygame.USEREVENT)

    $ zoomS1 = 3
    $ zoomT1 = 0
    $ zoomX1 = 0.55
    $ zoomY1 = 1.0
    $ zoomS2 = 1
    $ zoomT2 = 3
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1

    $ zoomS1_2 = 3
    $ zoomT1_2 = 0
    $ zoomX1_2 = 1
    $ zoomY1_2 = 1.0
    $ zoomS2_2 = 1
    $ zoomT2_2 = 3
    $ zoomX2_2 = 0.5
    $ zoomY2_2 = zoomY1

    scene schoolday_1_1lockermale_bg at ZoomSTXY
    show schoolday_1_1lockermale_wsis at ZoomSTXY_2
    show schoolday_1_1lockermale_fg at ZoomSTXY
    show schoolday_1_1lockermale_wgalbody at ZoomSTXY
    show schoolday_1_1lockermale_wgalface 1 at ZoomSTXY
    show schoolday_1_1lockermale_hprvbody at ZoomSTXY
    if persistent.gr:
        show schoolday_1_1lockermale_hprvfx at ZoomSTXY
    show schoolday_1_1lockermale_hrivface 1 at ZoomSTXY
    show schoolday_1_1lockermale_hrivbody at ZoomSTXY
    with Dissolve(3)

    pause(0.1)
    show schoolday_1_1lockermale_hrivface 2
    pause(0.5)
    show schoolday_1_1lockermale_wgalface 2
    pause(0.2)
    $ Y_spd = 5
    $ Y_pos = 75
    show schoolday_1_1lockermale_wgalbody at Scare
    show schoolday_1_1lockermale_wgalface 3 at Scare
    show schoolday_1_1lockermale_wgalfx at Y_Move
    pause(1)

    scene schoolday_1_1lockermale_bg
    show schoolday_1_1lockermale_wsis
    show schoolday_1_1lockermale_fg
    show schoolday_1_1lockermale_wgalbody
    show schoolday_1_1lockermale_wgalface 3
    show schoolday_1_1lockermale_wgalfx
    show schoolday_1_1lockermale_hprvbody
    if persistent.gr:
        show schoolday_1_1lockermale_hprvfx
    show schoolday_1_1lockermale_hrivface 2
    show schoolday_1_1lockermale_hrivbody

    $ _skipping = True
    $ pygame.event.set_blocked(None)

    wsis "You cowards!{w=[wt2]} {pa}Leave him alone!{/pa}"

    wota "{aw}. . . A catastrophe will happen!{/aw}{w=[wt3]} But don't worry.{w=[wt3]} According to the prophecy, a boy with a silly face like your friend is the chosen hero.{w=[wt2]} The man with the power to prevent chaos and destruction...{w=[wt3]} All we can do now is count on him."
    wnei "Ugh, {nm}[fnamewota]{/nm}!{w=[wt2]} Stop bad-mouthing my {nm}[fnamehero]{/nm} and {nm}[fnamewsis]{/nm} right now!!!"
    wota "Forgive me, master."

    $ hero_wear = "school"
    $ wsis_wear = "school"
    $ wgal_wear = "school"
    $ hriv_wear = "school"
    $ hprv_wear = "school"
    $ wsis_mood = "O3"
    $ wgal_mood = "O4"
    $ hriv_mood = "O2"
    $ hprv_mood = "O2"
    $ hero_mood = "O2"
    $ hprv_fx = 4
    scene bg_school locker_m
    show WSIS at LL
    show WGAL at RC
    show HRIV at RR
    $ X_pos = 1800
    show HPRV at X
    $ Y_spd=0
    $ yalign=0.5
    $ Y_pos=550
    show HPRV at Y_Move
    with Dissolve(1)

    wgal "Ugh{w=[wt1]}, serious!?{w=[wt2]} Did the {nm}miniature pinscher{/nm} really walk through the {bt}entire school{/bt} just to bug me?{w=[wt4]} Get lost, pest!"

    $ wgal_mood = "O2"
    show WSIS at LC_slow
    wsis "Let's{nw}"
    show WGAL at RR_fast
    wsis "Let's{fast} see who is{nw}"
    #show HRIV at RC_average
    wsis "Let's see who is{fast} the miniature pinscher when I break all your teeth!"

    $ hriv_mood = "O3"
    hriv "Hold on, {nm}[fnamewsis]{/nm}!{w=[wt3]} This jerk-off was under the balcony, taking pictures of {nm}[fnamewgal]{/nm}.{w=[wt4]} I'm just giving him a little lesson until he let us erase this photo."
    hprv "I already told you,{w=[wt2]} I removed the photo.{w=[wt3]} Return my cell phone please!"
    $ wgal_mood = "O3"
    wgal "How am I supposed believe you're not{w=[wt1]}, like{w=[wt1]}, {bt}totally making this up{/bt} to jerk off to my photo, you virgin!?"
    wsis "Heh{w=[wt1]}, I'm sure this bitch even posed for this photo!"
    $ wgal_mood = "A2"
    $ X_pos = 1150
    show WGAL at X_slow
    wgal "I'm not like the bitch that brought you into the world, baby!"
    $ wgal_mood = "O2"
    $ wsis_mood = "O4"
    show WGAL at Scare
    wsis "{pa}What!?{/pa}{nw}"
    show WGAL at RR_fast
    show HRIV at RC_average
    wsis "{pa}What!?{/pa}{fast}"
    hriv "Enough!{w=[wt3]} Look {nm}[fnamewsis]{/nm}{w=[wt2]}, you're being selfish.{w=[wt3]} What if it was you in her place, huh?{w=[wt2]} Would you let this disgusting worm to go out unpunished after taking pictures of your panties?{w=[wt3]} Would you be able to rest easy knowing that such a person has a picture of you like this?{w=[wt3]} Oh{w=[wt1]}, c'mon!{w=[wt3]} He's just a fucking jerk!"
    wsis "You don't fool me!{w=[wt2]} You're exactly like that.{w=[wt2]} {pa}All men are the same!!{/pa}{w=[wt2]}{nw}"
    $ hero_mood = "O1"
    wsis "You don't fool me!{w=[wt2]} You're exactly like that.{w=[wt2]} {pa}All men are the same!!{/pa}{fast}{w=[wt2]} Just leave him alone right now or..."
    $ hriv_mood = "A2"
    show HRIV at CC_slow
    hriv "Or what...?{nw}"
    $ wsis_mood = "O2"
    $ wgal_mood = "A2"
    $ X_pos = 500
    show WSIS at X_slow
    hriv "Or what...?{fast}{w=[wt4]} Go ahead then!{nw}"
    $ wgal_mood = "A4"
    show WGAL at Laugh
    hriv "Or what...? Go ahead then!{fast}"

    $ hero_fx = 0
    $ hero_mood = "O1"

    scene bg_school courtyard
    show HERO at RR
    with pushright

    "You are outside the men's locker room while a fight is about to happen.{w=[wt1]} What will you do?{w=[wt1]}{nw}"
    $ a_event_1 = 0

    $ Set_CharMap("hero", "school", "locker_m")
    show screen UI_stats

    menu:
        "You are outside the men's locker room while a fight is about to happen. What will you do?{fast}"

        "Dialogue, trying to calm the situation for everyone":
            hide screen UI_stats
            scene bg_school locker_m
            $ X_pos = 500
            show WSIS at X
            show HRIV at CC
            show WGAL at RR
            show WGAL at Laugh
            $ X_pos = 1800
            show HPRV at X
            $ Y_spd=0
            $ yalign=0.5
            $ Y_pos=550
            show HPRV at Y_Move
            with pushleft
            pause(0.5)
            $ hero_mood = "A2"
            $ hriv_mood = "O2"
            $ wgal_mood = "O1"
            show WGAL at RR
            show HERO at OL
            show HERO at LL_average

            $ add_stat("hprv", "love", 1)
            $ add_stat("hero", "cha_soc", 1)

            hero "Hey hey, guys...{w=[wt1]}{nw}"
            $ X_pos = 0
            show WSIS at LL_fast
            show HERO at X_fast
            hero "Hey hey, guys...{fast} Let's not fight here!{nw}"
            $ wsis_mood = "O3"
            show HERO at LC_fast
            hero "Hey hey, guys... Let's not fight here!{fast} The entrance ceremony has just ended and some people are coming near here.{w=[wt2]} It won't be good for anyone, you know?"

            $ add_stat("wgal", "love", 2)
            $ add_stat("hero", "cha_soc", 2)

            hriv "Huh...?{w=[wt2]} Who are you?{w=[wt3]} That's none of your business!"
            wsis "Get out, moron!"
            jump schoolday_1_2_transition

        "Face {nm}[fnamehriv]{/nm}, trying to solve this in a psychological combat":
            hide screen UI_stats
            scene bg_school locker_m
            $ X_pos = 500
            show WSIS at X
            show HRIV at CC
            show WGAL at RR
            show WGAL at Laugh
            $ X_pos = 1800
            show HPRV at X
            $ Y_spd=0
            $ yalign=0.5
            $ Y_pos=550
            show HPRV at Y_Move
            with pushleft
            pause(0.5)
            $ hero_mood = "O2"
            $ hriv_mood = "O2"
            $ wgal_mood = "O1"
            show WGAL at RR
            show HERO at OL
            show HERO at LL_average

            hero "{size=-5}There are inspectors{/size}{nw}"
            $ X_pos = 0
            show WSIS at LL_fast
            show HERO at X_fast
            hero "{size=-5}There are inspectors{fast} right outside.{/size}{nw}"
            $ wsis_mood = "O3"
            show HERO at LC_fast
            hero "{size=-5}There are inspectors right outside.{fast}{w=[wt2]} You better do what she says if you don't want me to call them right now.{/size}{nw}"

            $ a_event_1 = 5

            $ add_stat("hriv", "love", -2)
            hero "{size=-5}There's an inspector right outside. You better do what she says if you don't want me to call them right now.{/size}{fast}{nw}{w=[wt2]}"
            $ add_stat("wgal", "love", -1)
            hero "{size=-5}There's an inspector right outside. You better do what she says if you don't want me to call them right now.{/size}{fast}"

            $ add_stat("hprv", "love", 5)
            $ add_stat("hero", "cha_soc", 5)
            $ hriv_mood = "O2"
            $ wgal_mood = "O2"
            wsis "I don't need your help..."
            jump schoolday_1_2_fight

        "Face {nm}[fnamehriv]{/nm}, threatening to hit him":
            hide screen UI_stats
            scene bg_school locker_m
            $ X_pos = 500
            show WSIS at X
            show HRIV at CC
            show WGAL at RR
            show WGAL at Laugh
            $ X_pos = 1800
            show HPRV at X
            $ Y_spd=0
            $ yalign=0.5
            $ Y_pos=550
            show HPRV at Y_Move
            with pushleft
            pause(0.5)
            $ hero_mood = "O2"
            $ hriv_mood = "O2"
            $ wgal_mood = "O1"
            show WGAL at RR
            show HERO at OL
            show HERO at LL_average
            $ add_stat("hprv", "love", 5)
            $ add_stat("hero", "cha_soc", 5)

            hero "You better not approach{nw}"

            $ X_pos = 0
            show WSIS at LL_fast
            show HERO at X_fast

            hero "You better not approach{fast} her if you{nw}"
            $ wsis_mood = "O3"
            show HERO at LC_fast
            $ add_stat("wsis", "love", 5)
            $ add_stat("hero", "cha_soc", 5)

            hero "You better not approach her if you{fast} don't want to get hurt"

            $ add_stat("hriv", "love", -5)
            wsis "Go away!{w=[wt2]} I don't need your help{w=[wt1]}, moron!"
            jump schoolday_1_2_fight

#---------------------------------------------------------------------------
label schoolday_1_2_transition:
#---------------------------------------------------------------------------
    $ hriv_mood = "O2"
    hriv "What this asshole is to you, {nm}[fnamewsis]{/nm}?"
    wsis "That's none of your business!"
    $ wgal_mood = "A2"
    $ hriv_mood = "A2"
    hriv "{bt}Ohhh...?{/bt}{w=[wt3]} So are you that ashamed of your boyfriend?"

    if not 0 > 1:
        $ wgal_mood = "O1"
        $ hriv_mood = "O2"
        $ hero_mood = "O1"
        $ hero_fx = 1
        $ wsis_fx = 1

        hero "{aw}Ehhh!?{/aw}"
        $ wgal_mood = "A4"
        show WGAL at Laugh
        wgal "{lg}BWA HA HA HA...{/lg}{w=[wt2]} What a {bt}sooo boooring guy...{/bt}{w=[wt3]} It seems that he{w=[wt1]}, like{w=[wt2]}, {bt}TOTALLY COMBINE{/bt} with the nag!{w=[wt3]} But I{w=[wt1]}, like{w=[wt2]}, {bt}super bet{/bt} he's still a virgin that simps her in hope to fuck that fat bitch's ass{w=[wt1]}, while she plays coy with him as the sly bitch she is!"
        $ wsis_mood = "O4"
        $ hero_fx = 0
        jump schoolday_1_2_argue2

    else:
        menu:
            "Tell she's your sister":
                $ add_stat("wsis", "inti", 1)

                hero "She's my sister!"

                $ wgal_mood = "A4"
                $ hriv_mood = "O1"
                show WGAL at Laugh

                wgal "{lg}BWA HA HA HA...{/lg}{w=[wt3]} Oooh nooo!{w=[wt2]} Like{w=[wt2]}, serious{w=[wt1]}, I {bt}CAN'T{/bt}{w=[wt1]} believe!{w=[wt2]} No, no, no, no, serious, Look at them!{w=[wt2]} {bt}Totally nothing alike!{/bt}{w=[wt3]} Her mother really just spread her legs to{w=[wt1]}, like{w=[wt2]}, {bt}everyone on the way!{/bt} {lg}BWA HA HA HA...{/lg}{w=[wt3]} I wonder if she knows who is the father this time!"
                $ wsis_mood = "O4"
                jump schoolday_1_2_argue1

            "Tell she's your step-sister":
                hero "She's my step-sister!"

                $ add_stat("wgal", "love", 1)
                $ add_stat("hero", "cha_soc", 1)
                $ wgal_mood = "A4"
                $ hriv_mood = "O1"
                show WGAL at Laugh

                wgal "{lg}BWA HA HA HA...{/lg}{w=[wt3]} Did he say {bt}STEP?!{/bt}{w=[wt3]} No, no, no, no, serious!{w=[wt2]} Her mother wanted so much to have a husband who didn't leave her that she really just spread her legs to{w=[wt1]}, like{w=[wt2]}, {bt}everyone on the way!{/bt} {lg}BWA HA HA HA...{/lg}"
                $ wsis_mood = "O4"
                jump schoolday_1_2_argue1

            "Stay quiet":
                $ wgal_mood = "O1"
                $ hriv_mood = "O2"
                $ hero_mood = "O1"

                hero "..."
                $ wgal_mood = "A4"
                show WGAL at Laugh
                wgal "{lg}BWA HA HA HA...{/lg}{w=[wt2]} What a {bt}sooo boooring guy...{/bt}{w=[wt3]} It seems that he{w=[wt1]}, like{w=[wt2]}, {bt}TOTALLY COMBINE{/bt} with the nag!{w=[wt3]} But I{w=[wt1]}, like{w=[wt2]}, {bt}super bet{/bt} he's still a virgin that simps her in hope to fuck that fat bitch's ass{w=[wt1]}, while she plays coy with him as the sly bitch she is!"
                $ wsis_mood = "O4"
                jump schoolday_1_2_argue2

            "Fight":
                $ wgal_mood = "O1"
                $ hriv_mood = "O2"
                $ hero_mood = "O2"

                hero "That's enough.{w=[wt2]} You abused my patience."

                $ add_stat("wsis", "love", 1)
                $ add_stat("hero", "cha_soc", 1)
                $ a_event_0 = 0
                jump schoolday_1_2_fight

#---------------------------------------------------------------------------
label schoolday_1_2_fight:
#---------------------------------------------------------------------------
    $ hriv_mood = "A2"
    $ wgal_mood = "O2"
    if a_event_1 == 5:
        hriv "Let me get this straight.{w=[wt2]} Was that a threat?{w=[wt3]} You know who you're talking to, asshole?{w=[wt3]} I think I need to put you in your place."
    else:
        hriv "If that's what you want..."

    show WGAL at RC_average
    wgal "W{w=[wt1]}-wait!{w=[wt2]} Let's not fight here!{w=[wt2]} You know{w=[wt1]}, like{w=[wt2]}, if these loosers are here{w=[wt1]}, it means the entrance ceremony may have ended.{w=[wt2]} So{w=[wt2]}, like{w=[wt2]}, Let's just get out, okay?"
    $ hriv_mood = "O2"
    $ a_event_0 = 0
    jump schoolday_1_2_end

#---------------------------------------------------------------------------
label schoolday_1_2_argue1:
#---------------------------------------------------------------------------
    menu:
        "Defend {nm}[fnamewmom]{/nm}":
            show WGAL at RR
            if stat_cha >= 15 and stat_int >= 15:
                $ wgal_mood = "O1"
                $ hriv_mood = "O2"
                $ hero_mood = "A1"

                hero "Don't mock people from the stupid perception you have of their strawmen.{w=[wt3]} The only truth is that she is too amazing to describe with such empty words."
                $ add_stat("wsis", "love", 10)
                $ add_stat("wgal", "love", -1)
                $ add_stat("hriv", "love", -1)
                $ add_stat("hprv", "love", 6)

                wgal "What...?{w=[wt3]} Ugh{w=[wt1]}, you're a nerd...!{w=[wt3]} Disgusting!"

            elif stat_cha >= 10 and stat_int >= 10:
                $ wgal_mood = "O1"
                $ hriv_mood = "O2"
                $ hero_mood = "O2"

                hero "Stop mocking people.{w=[wt2]} You just say that cos you don't know how amazing she is!"

                $ add_stat("wsis", "love", 7)
                $ add_stat("wgal", "love", -1.5)
                $ add_stat("hriv", "love", -1.5)
                $ add_stat("hprv", "love", 4)

                wgal "You're a weirdo...{w=[wt3]} Just shut up!"

            elif stat_cha >= 10:
                $ wgal_mood = "O1"
                $ hriv_mood = "O2"
                $ hero_mood = "O2"

                hero "Remove what you said about her!"
                $ add_stat("wsis", "love", 5)
                $ add_stat("wgal", "love", -1.5)
                $ add_stat("hriv", "love", -1.5)
                $ add_stat("hprv", "love", 2)

                $ wgal_mood = "A2"
                wgal "What if I don't?..."

            else:
                $ wgal_mood = "A2"
                $ hriv_mood = "O2"
                $ hero_mood = "O2"

                hero "She's not like that!"
                $ add_stat("wsis", "love", 2)
                $ add_stat("wgal", "love", -2)
                $ add_stat("hriv", "love", -2)
                $ add_stat("hprv", "love", -1)

                wgal "Oh{w=[wt2]}, shut up, you weirdo!"

            hriv "Come on{w=[wt2]}, let's get out."
            wgal "{bt}Booooriiing...{/bt}"
            jump schoolday_1_2_end

                
        "Confront {nm}[fnamewgal]{/nm}":
            show WGAL at RR
            if stat_cha >= 15 and stat_int >= 15:
                $ wgal_mood = "O1"
                $ hriv_mood = "O1"
                $ hero_mood = "A2"

                hero "Oh, come on...!{w=[wt3]} You just say that cos no one wanna fuck someone with such opossum face like yours, isn't it?{w=[wt3]} Serious{w=[wt1]}, if someone is brave enough to put the dick on such a dry hole, they should put at least a bag to cover your face!{w=[wt3]} That's why you feel envious of successful people, am I right?"

                $ add_stat("wsis", "love", 15)
                $ add_stat("hprv", "love", 10)
                $ add_stat("wgal", "love", -10)
                $ add_stat("hriv", "love", -1)

                $ wgal_mood = "O4"
                $ wsis_mood = "A4"
                $ hprv_mood = "A2"
                $ hriv_mood = "A2"
                $ hero_mood = "A1"
                $ wgal_fx = 1
                show HRIV at Laugh
                show WSIS at Laugh

                wgal "W{w=[wt1]}-What!?"

                $ hriv_mood = "A3"
                hriv "{aw}Pfff...{/aw}{w=[wt1]} {lg}HA HA HA HA...{/lg}"
                wgal "Stop laughing!!!"

                show HRIV at CC
                hriv "Oh no, no, no, sorry {nm}[fnamewgal]{/nm}!{w=[wt2]} This got me off guard!{w=[wt2]} Come on{w=[wt1]}, let's get out."
                $ hriv_mood = "A1"
                $ wsis_mood = "A1"
                jump schoolday_1_2_end

            elif stat_cha >= 10 and stat_int >= 10:
                $ wgal_mood = "O1"
                $ hriv_mood = "O1"
                $ hero_mood = "A2"

                hero "Hey, hey{w=[wt2]}, you just say that cos you're ugly and no one gives you a damn.{w=[wt3]} You really should feel envious of successful people, aren't you?"

                $ add_stat("wgal", "love", -10)
                $ add_stat("wsis", "love", 10)
                $ add_stat("hprv", "love", 5)
                $ add_stat("hriv", "love", 2)

                $ wgal_mood = "O4"
                $ wsis_mood = "A4"
                $ hprv_mood = "A2"
                $ hriv_mood = "A2"
                $ hero_mood = "A1"
                $ wgal_fx = 1
                show WSIS at Laugh

                wgal "What did you say you fucking jerk!?"
                hriv "She's just too far out of your league, idiot.{w=[wt2]} Come on {nm}[fnamewgal]{/nm}, let's get out."
                wgal "Sure{w=[wt1]}, looking at these weirdos is already getting on my nerves!!!"
                $ hriv_mood = "A1"
                $ wsis_mood = "A1"
                jump schoolday_1_2_end

            elif stat_cha >= 10:
                $ wgal_mood = "O1"
                $ hriv_mood = "O2"
                $ hero_mood = "O2"

                hero "What an idiot like you know?"

                $ add_stat("wsis", "love", 2)
                $ add_stat("hprv", "love", 2)

                $ wgal_mood = "A2"
                wgal "{lg}BWA HA HA HA...{/lg}{w=[wt3]} What was that, you weird?{w=[wt3]} Get lost, please!"
                hriv "Come on {nm}[fnamewgal]{/nm}{w=[wt1]}, let's get out."
                wgal "{bt}Bye, virgins...{/bt}"
                jump schoolday_1_2_end

            else:
                $ wgal_mood = "O1"
                $ hriv_mood = "O2"
                $ hero_mood = "O2"

                hero "What do you know?{w=[wt2]} Stop judging people!"

                $ add_stat("wsis", "love", 1)
                $ add_stat("hprv", "love", 1)

                $ wgal_mood = "A2"
                wgal "{lg}BWA HA HA HA...{/lg}{w=[wt3]} But I don't judge, Dear...!{w=[wt3]} Who judges is life itself{w=[wt2]}, I just{w=[wt1]}, like{w=[wt2]}, mention facts!"
                hriv "Come on {nm}[fnamewgal]{/nm}{w=[wt1]}, let's get out."
                wgal "{bt}Bye, virgins...{/bt}"
                jump schoolday_1_2_end

        "Don't give in to the provocation":
            show WGAL at RR
            $ wgal_mood = "A2"
            $ hriv_mood = "O2"
            $ hero_mood = "A2"
            if stat_cha >= 10:
                hero "Don't worry.{w=[wt2]} Let's just let them say whatever they want."
                wsis "..."
                $ wgal_mood = "A1"
                hriv "Hunf...{w=[wt3]} This guy is just a chicken.{w=[wt3]} Come on {nm}[fnamewgal]{/nm}{w=[wt1]}, let's get out."
                wgal "{bt}Bye, virgins...{/bt}"
                jump schoolday_1_2_end
            else:
                hero "..."
                $ wsis_mood = "O4"
                $ hero_mood = "O1"
                wsis "{pa}Shut up! Don't make fun of my mother!!!{/pa}"
                hriv "Yeah{w=[wt1]}, shut up {nm}[fnamewgal]{/nm}{w=[wt1]}, you went too far.{w=[wt2]} Let's get out."

                $ wgal_mood = "O3"
                $ wsis_mood = "O3"
                wgal "Oh no!{w=[wt2]} Wait, wait, wait...{w=[wt3]} Like{w=[wt2]}, {bt}Helloooo...?{/bt}{w=[wt3]} Are you really{w=[wt1]}, like{w=[wt2]}, going to side with the {nm}miniature pinscher{/nm}?{w=[wt3]} Seriously?"
                $ wgal_mood = "O2"
                hriv "Come on{w=[wt1]}, let's get out."
                wgal "{bt}Booooriiing...{/bt}"
                jump schoolday_1_2_end

#---------------------------------------------------------------------------
label schoolday_1_2_argue2:
#---------------------------------------------------------------------------
    menu:
        "Defend your pride":
            show WGAL at RR
            $ hero_mood = "A2"
            $ wgal_mood = "A2"
            $ hriv_mood = "A3"
            hero "{bt}Ehhh...?{/bt}{w=[wt2]} I bet you couldn't stand it two minutes with this virgin in bed."

            show HRIV at Laugh
            $ wgal_fx = 1
            $ wsis_fx = 2
            $ add_stat("hriv", "love", 2)
            $ add_stat("wgal", "love", 2)
            $ add_stat("wsis", "love", -2)
            $ add_stat("hprv", "love", -2)
            $ wsis_know.append("Upset")
            $ wsis_know.append("Upset")
            $ wsis_know.append("Upset")
            $ msg.msg(renpy.translate_string("{nm}[fnamewsis]{/nm}'s anger {color=#32FF32}+")+str(round((25 - (a_event_2 * 5)) * sum(1 for buceta in wsis_know if buceta =="Upset"), 2))[:4]+renpy.translate_string("%{/color}. You better not piss her off."))

            wgal "What?...{w=[wt2]} Weirdo!"

            $ wgal_mood = "O2"
            hriv "{lg}Ha Ha Ha Ha...{/lg}{w=[wt3]} This one got me off guard.{w=[wt2]} The asshole have guts!{w=[wt2]} Come on{w=[wt1]}, let's get out."

            $ wgal_mood = "O3"
            wgal "You guys are {bt}soooo{/bt} stupid..."
            $ hriv_mood = "A2"
            jump schoolday_1_2_end

        "Defend {nm}[fnamewsis]{/nm}":
            show WGAL at RR

            $ wgal_mood = "O1"
            $ hriv_mood = "O2"
            $ hero_mood = "O2"

            hero "Remove what you said about her!"

            $ wsis_mood = "O2"
            $ wsis_fx = 1
            $ add_stat("wsis", "love", 2)
            $ add_stat("wgal", "love", -2)
            $ add_stat("hriv", "love", -2)
            $ add_stat("hprv", "love", 2)
            $ wgal_mood = "A2"

            wgal "What if I don't?..."
            hriv "Come on{w=[wt1]}, let's get out."
            wgal "{bt}Booooriiing...{/bt}"
            jump schoolday_1_2_end
                
        "Confront {nm}[fnamewgal]{/nm}":
            show WGAL at RR

            $ wgal_mood = "O1"
            $ hriv_mood = "O1"
            $ hero_mood = "A2"

            hero "You just say that cos you're ugly and feel envious of beautiful people, don't you?"

            $ add_stat("wgal", "love", -4)
            $ add_stat("wsis", "love", 2)
            $ add_stat("hprv", "love", 1)
            $ add_stat("hriv", "love", 1)

            $ wgal_mood = "O4"
            $ wsis_mood = "A4"
            $ hprv_mood = "A2"
            $ hriv_mood = "A2"
            $ hero_mood = "A1"
            $ wgal_fx = 1
            $ wsis_fx = 1
            show WSIS at Laugh

            wgal "What did you say you fucking jerk!?"
            hriv "She's just too far out of your league, idiot.{w=[wt2]} Come on {nm}[fnamewgal]{/nm}, let's get out."
            wgal "Sure{w=[wt1]}, looking at these weirdos is already getting on my nerves!!!"
            $ hriv_mood = "A1"
            $ wsis_mood = "A1"
            jump schoolday_1_2_end

        "Don't give in to the provocation":
            show WGAL at RR
            $ wgal_mood = "A2"
            $ hriv_mood = "O2"
            $ hero_mood = "A2"
            if not 0 > 1:
                hero "Don't worry.{w=[wt2]} Let's just let them say whatever they want."
                wsis "..."
                $ wgal_mood = "A1"
                hriv "Hunf...{w=[wt3]} This guy is just an chicken.{w=[wt3]} Come on {nm}[fnamewgal]{/nm}{w=[wt1]}, let's get out."
                wgal "{bt}Bye, virgins...{/bt}"
                jump schoolday_1_2_end
            else:
                hero "..."
                wsis "Shut up! He's my {nm}[wsis_to_hero]{/nm}!"
                $ wsis_mood = "O4"
                $ hero_mood = "O1"
                wgal "{lg}BWA HA HA HA...{/lg}{w=[wt3]} Oooh nooo!{w=[wt2]} Like{w=[wt2]}, serious{w=[wt1]}, I {bt}CAN'T{/bt}{w=[wt1]} believe!{w=[wt2]} No, no, no, no, serious, Look at them!{w=[wt2]} {bt}Totally nothing alike!{/bt}{w=[wt3]} Her mother really just spread her legs to{w=[wt1]}, like{w=[wt2]}, {bt}everyone on the way!{/bt} {lg}BWA HA HA HA...{/lg}{w=[wt3]} I wonder if she knows who is the father this time!"
                jump schoolday_1_2_argue1

#---------------------------------------------------------------------------
label schoolday_1_2_end:
#---------------------------------------------------------------------------
    if a_event_0 == 3:
        scene bg_school locker_m
        $ X_pos = 1000
        show HERO at X
        $ X_pos = 800
        show WSIS at X
        show HRIV at RC
        show WGAL at RR
        $ X_pos = 1800
        show HPRV at X
        $ Y_spd=0
        $ yalign=0.5
        $ Y_pos=550
        show HPRV at Y_Move
        with Fade(2,0,1)

    $ X_spd = 5
    show HRIV at OL_X
    show WGAL at OL_X

    if a_event_1 == 5:
        hriv "You better stay out of my way, asshole."

    elif hriv_love <= 0 and a_event_1 <= 5:
        hriv "You better stay out of my way, asshole."

    if not a_event_0 == 3:
        show HERO at CC_slow
        show WSIS at LC_slow

    pause (0.5)
    hprv "H{w=[wt1]}-hey!{w=[wt2]} My phone!{nw}"

    show HRIV at LL_slow
    hprv "H-hey! My phone!{fast}"

    stop BGM fadeout 6
    hriv "Oh{w=[wt1]}, right!{w=[wt2]} I almost forgot..."

    $ zoomS1 = 2
    $ zoomT1 = 0
    $ zoomX1 = 0.5
    $ zoomY1 = 0.0
    $ zoomS2 = 2
    $ zoomT2 = 3
    $ zoomX2 = zoomX1
    $ zoomY2 = 0.2

    scene schoolday_1_2lockermale_bg at ZoomSTXY
    show schoolday_1_2lockermale_wgal at ZoomSTXY
    show schoolday_1_2lockermale_hrivbody at ZoomSTXY
    show schoolday_1_2lockermale_hrivface o0 at ZoomSTXY
    show schoolday_1_2lockermale_hrivhand 1 at ZoomSTXY
    show schoolday_1_2lockermale_hrivleg 1 at ZoomSTXY
    with Dissolve(1)

    show schoolday_1_2lockermale_hrivface o1

    hriv "I couldn't find the photo anywhere{w=[wt2]}, so..."

    $ zoomS1 = 2
    $ zoomT1 = 0
    $ zoomX1 = 0.5
    $ zoomY1 = 0.2
    $ zoomS2 = 2
    $ zoomT2 = 0.5
    $ zoomX2 = zoomX1
    $ zoomY2 = 1.0

    scene schoolday_1_2lockermale_bg at ZoomSTXY
    show schoolday_1_2lockermale_wgal at ZoomSTXY
    show schoolday_1_2lockermale_hrivbody at ZoomSTXY
    show schoolday_1_2lockermale_hrivface o0 at ZoomSTXY
    show schoolday_1_2lockermale_hrivhand 2 at ZoomSTXY
    show schoolday_1_2lockermale_hrivleg 1 at ZoomSTXY
    show schoolday_1_2lockermale_phone 1 at Zoom_2

    pause(0.5)
    play SE1 "Hit2.mp3"

    $ zoomS1 = 2
    $ zoomT1 = 0
    $ zoomX1 = 0.5
    $ zoomY1 = 1.0
    $ zoomS2 = zoomS1
    $ zoomT2 = zoomT1
    $ zoomX2 = zoomX1
    $ zoomY2 = zoomY1

    show schoolday_1_2lockermale_phone 2 at ZoomSTXY
    pause(0.2)
    show schoolday_1_2lockermale_phone 3 at ZoomSTXY
    pause(0.75)
    play SE1 "Hit2.mp3"
    hide schoolday_1_2lockermale_phone
    show schoolday_1_2lockermale_hrivleg 2
    with dissolve
    pause(1)
    hriv "It's better to ensure that it is not going anywhere!"

    $ wsis_fx = 0
    $ hero_fx = 0
    $ wgal_fx = 0

    scene bg_school locker_m
    if not a_event_0 == 3:
        show HERO at CC
        show WSIS at LC
    else:
        $ X_pos = 1000
        show HERO at X
        $ X_pos = 800
        show WSIS at X
    show WGAL at OL
    $ X_pos = 300
    show HRIV at X
    $ X_pos = 1800
    show HPRV at X
    $ Y_spd=0
    $ yalign=0.5
    $ Y_pos=550
    show HPRV at Y_Move
    $ wgal_mood = "A4"
    $ wsis_mood = "O2"
    $ hero_mood = "O1"
    $ hriv_mood = "O1"
    with Dissolve(2)

    $ X_pos = 100
    show WGAL at X_slow
    wgal "{aw}OH{w=[wt2]} MY{w=[wt2]} GOSH!{/aw}{w=[wt3]} you're{w=[wt1]}, seriously{w=[wt2]}, {bt}THE BEST EVER!!!{/bt}{nw}"
    $ hriv_mood = "A2"
    show WGAL at Laugh
    wgal "{aw}OH MY GOSH!{/aw} you're{w=[wt1]}, seriously, {bt}THE BEST EVER!!!{/bt}{fast}"
    show HRIV at OL_slow
    hriv "C'mon!"
    $ wgal_mood = "A2"
    show WGAL at OL_slow
    wgal "{bt}Bye, loosers...{/bt}"

    pause(1)

    $ Y_spd=0.5
    $ yalign=1.0
    $ Y_pos=600
    show HPRV at Y_Move
    hprv "Oh, guy...{nw}"
    $ Y_spd=2
    $ yalign=1.0
    $ Y_pos=0
    show HPRV at Y_Move
    hprv "Oh, guy...{fast}{w=[wt2]} This dude is really a pain in the ass...{nw}"
    show HPRV at RR_slow
    hprv "Oh, guy... This dude is really a pain in the ass...{fast}{w=[wt4]} I still can't believe he chased me all this distance!"

    show HERO at CC_slow
    show WSIS at LC_slow
    wsis "I should have let him beat you to death, you stupid pervert!"
    hprv "H{w=[wt1]}-hey...{w=[wt2]} Come on {nm}[fnamewsis]{/nm}...!{w=[wt3]} You know these words from you hurt me more than the hurt on my face...{w=[wt3]} Rest assured I'd never do such things to you and {nm}[fnamewnei]{/nm}, okay?{w=[wt4]} It's just that{w=[wt1]}, the other girls from this school are...{w=[wt2]} well{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} n{w=[wt1]}-not respectable like you are!{w=[wt2]} With you is different!"
    wsis "I couldn't care less, you pervert!"

    $ hprv_mood = "A2"
    hprv "By the way{w=[wt2]}, about you, man...{w=[wt2]} Wooow!{w=[wt3]} {bt}You are so cool!{/bt}{w=[wt3]} You really faced {nm}[fnamehriv]{/nm} like a true hero!{w=[wt2]} Our victory against him will be recorded in historical tales, man!"
    $ wsis_mood = "O3"
    hero "{aw}E{w=[wt1]}-ehhh...!?{/aw}"
    wsis "What victory, moron!?{w=[wt2]} And {pa}''OUR''!?{/pa}{w=[wt3]} Did your stupidity reach another level or what?{w=[wt2]} Look at your face!!!"

    $ wsis_mood = "O2"
    hprv "Heh...{w=[wt2]} In fact{w=[wt1]}, my situation seems unfortunate{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt4]} But{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{nw}"
    play BGM "audio/W2C - Subtitle.mp3"
    $ hprv_mood = "A3"
    hprv "Heh... In fact, my situation seems unfortunate... But...{fast}{w=[wt4]} The truth is that before I was chased{w=[wt1]}, I quickly saved the picture in the {color=#64AFFF}B{/color}{color=#FF6464}o{/color}{color=#FFFF64}o{/color}{color=#64AFFF}b{/color}{color=#FF6464}l{/color}{color=#FFFF64}e{/color} {color=#64FF64}Cloud{/color}.{w=[wt3]} So{w=[wt1]}, as much as my phone has been destroyed{w=[wt1]}, I can still recover the photo!{w=[wt3]} The victory is ours, friends!{nw}"
    $ wsis_mood = "O4"
    $ wsis_fx = 1
    $ hero_mood = "O1"
    $ hero_fx = 1
    hprv "Heh... In fact, my situation seems unfortunate... But...{fast} The truth is that before I was chased, I quickly saved the picture in the {color=#64AFFF}B{/color}{color=#FF6464}o{/color}{color=#FFFF64}o{/color}{color=#64AFFF}b{/color}{color=#FF6464}l{/color}{color=#FFFF64}e{/color} {color=#64FF64}Cloud{/color}. So, as much as my phone has been destroyed, I can still recover the photo! The victory is ours, friends!{fast}"
    wsis "{pa}WHAT!?{/pa}"

    stop BGM fadeout 3
    $ hero_quest_2 = 2
    #$ is_specialevent = False

    scene bg_0
    with Dissolve(2)
    $ add_stat("wsis", "inti", 1)
    pause (0.5)
    $ add_stat("hprv", "inti", 1)
    pause (0.5)
    $ add_stat("hriv", "inti", 1)
    pause (0.5)
    $ add_stat("wgal", "inti", 1)
    scene bg_school locker_m
    with dissolve

    $ hero_fx = 0
    $ hprv_fx = 0
    $ hriv_fx = 0
    $ wsis_fx = 0
    $ wgal_fx = 0
    $ hero_mood = "A1"
    $ hprv_mood = "A1"
    $ hriv_mood = "A2"
    $ wsis_mood = "O1"
    $ wgal_mood = "A2"

    play BGM "audio/W2C - Tranquility.mp3"
    call gametime_wait(8, 0) from _call_gametime_wait_21
    $ is_specialevent = False
    call gametime from _call_gametime_94
    jump show_ui

#---------------------------------------------------------------------------
label schoolday_wsis_leaving:
#---------------------------------------------------------------------------
    call gametime from _call_gametime_95
    call hide_ui from _call_hide_ui_176

    $ is_specialevent = False
    $ hero_quest_2 = 3
    $ wsis_mood = "O1"
    $ wsis_wear = "school"
    if hero_wear == "school_swim":
        $ stat_hyg = 100
        $ hero_needs[0] = True
        $ msg.msg(renpy.translate_string("You are clean."))
        $ wsis_fx = 1
    show HERO at LC
    show WSIS at OR
    show WSIS at RC_heavy
    with Fade(1,0.5,2)
    if not Check_CharSameMap("hero", "wsis"):

        if hero_wear == "school_swim":
            wsis "F{w=[wt1]}-found you."
        else:
            wsis "Found you."

        $ hero_mood = "A2"
        hero "Hey{w=[wt2]}, don't speak as if I were hiding or something"
    wsis "I'm gonna home.{w=[wt2]} If you wanna come with me, hurry!"

    hero "Sure.{w=[wt2]} Let's go!"
    show HERO at OL_slow
    show WSIS at OL_slow

    scene bg_0
    with Dissolve(1)
    if not hero_wear == "school":
        $ hero_wear = "school"
        $ msg.msg(renpy.translate_string("You dressed your school uniform."))
        pause(1)
    $ add_stat("wsis", "inti", 1)
    pause(1)

    scene bg_home livingroom
    show HERO at OR
    show WSIS at RR
    show HERO at RR_slow
    show WSIS at RC_slow
    with dissolve

    wsis "Hey.{w=[wt2]} Don't forget that you have an appointment with {nm}[fnamewcou]{/nm} tonight.{w=[wt3]} By the way{w=[wt2]}, b{w=[wt1]}-be careful with her!"
    $ hero_mood = "O1"
    hero "Huh...?{w=[wt3]} Why?"
    $ wsis_mood = "O2"
    wsis "N{w=[wt1]}-nevermind.{nw}"
    show WSIS at OL_slow
    wsis "N-nevermind.{fast}"

    $ hero_wear = "home"

    $ gametimehour = 14
    $ gametimemin = 0
    call gametime from _call_gametime_96
    call goto_home_livingroom from _call_goto_home_livingroom_5

    $ StartAct("wsis", [(("moving", "home"), 0), (("staying", "bedroom_wsis"), 10)], True)

    jump show_ui
