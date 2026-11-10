image wmom_yoga2_bg defeat = Movie(play="images/Scene/WMOM - Yoga/wmom_yoga2_bg defeat.webm", loop=True)

screen wmom_flexibility_bar():
    hbox:
        yalign 0.5
        xalign 0.98
        spacing 25

#---------------------------------------------------------------------------
label wmom_yoga_0_0: # 1st Yoga Session
#---------------------------------------------------------------------------

    hide screen fx_morning
    hide screen fx_afternoon
    hide screen fx_night

    $ wmom_quest[2] = 1
    
    scene wmom_yoga1_bg
    show wmom_yoga1_wmom 0
    show wmom_yoga1_hero
    with Dissolve(2)

    show wmom_yoga1_wmom 1
    show screen wmom_flexibility_bar
    wmom "{gg}Tchee-Hee...{/gg} I'm glad you joined me, darling!"

    show wmom_yoga1_wmom 0
    hero "So, {nm}[hero_to_wmom]{/nm}{w=[wt1]}, it's kinda surprise to me that you are into yoga stuff."

    show wmom_yoga1_wmom 1
    wmom "Actually{w=[wt1]}, I don't understand much about the subject, dear.{w=[wt2]} I just saw a few times on TV.{w=[wt2]} They use to say it's good to reduce stress and anxiety, you know?{w=[wt2]} So a few month ago I decided to use my free time to start practicing."

    show wmom_yoga1_wmom 0
    hero "That's a nice start {nm}[hero_to_wmom]{/nm}!{w=[wt2]} So, what do we do here?"

    wmom "Well{w=[wt2]}, I saw on TV that girls do some poses that I can't do.{w=[wt3]} I'd like to increase my elasticity.{w=[wt2]} I was wondering if you could help me with this."

    hero "Of course!"

    wmom "Good!{w=[wt2]} Let me lay close to you{w=[wt1]}, and you hold my feet, okay?"

#    label wmom_yoga_0_0test:
#        show 2MOM
#        pause(1)

    stop BGM fadeout 2

    scene bg_0
    with Dissolve(1)

    pause(1)

    $ bar_time = 45
    $ bar_timemax = 45
    $ bar_action = 0
    $ bar_actionmax = 100
    $ config.allow_skipping = False
    $ config.skipping = False
    $ minigameid = "minigame_wmomyoga"
    $ minigame_timeup = 'minigame_wmomyoga_timeup'
    $ minigame_defeat = 'minigame_wmomyoga_defeat'
    $ minigame_victory = 'minigame_wmomyoga_victory'
    $ minigamestep = 0
    $ minigamestep1 = 0
    $ minigame_p1 = 0
    $ minigame_cpu = 0
    $ a_event_0 = 0
    $ a_event_1 = 1
    $ a_event_2 = 1.5

    play BGM "audio/W2C - SexyVibes.mp3"

    call gametimesec from _call_gametimesec_2
    scene 2MOM breathe
    with Dissolve(1)

    show screen minigameplay_hold
    show screen minigameshow_yoga
    with dissolve

    $ renpy.pause(hard=True)
    
    label minigame_wmomyoga_timeup:
        hide screen minigameplay_hold
        hide screen minigameshow_yoga
        $ renpy.block_rollback()
        $ config.rollback_enabled = False
        $ config.allow_skipping = False
        $ config.skipping = False

        play BGM "audio/W2C - Tranquility.mp3"

        scene bg_0
        with dissolve
        pause(0.5)
        scene wmom_yoga1_bg
        show wmom_yoga1_wmom 0
        show wmom_yoga1_hero
        with Dissolve(3)

        show wmom_yoga1_wmom 1
        wmom "So, Darling{w=[wt2]}, I think it's enough for today.{w=[wt3]} Thank you so much for making me company!{w=[wt2]} I love you."

        scene bg_0
        with Dissolve(2)
        $ add_stat("wmom", "love", 2)
        pause(1)

        stop BGM fadeout 1

        $ a_event_0 = ((17*2) - (2 * (gametimehour + (gametimemin/60))))
        $ add_stat("wmom", "inti", a_event_0)
        pause(1)

        $ quick_menu = True
        $ config.allow_skipping = True
        $ config.rollback_enabled = True

        $ gametimehour = 17
        $ gametimemin = 0
        call gametime from _call_gametime_106
        jump show_ui
    
    label minigame_wmomyoga_defeat:
        hide screen minigameplay_hold
        hide screen minigameshow_yoga
        $ renpy.block_rollback()
        $ config.rollback_enabled = False
        $ config.allow_skipping = False
        $ config.skipping = False

        play BGM "audio/W2C - Awkward.mp3"

        scene bg_0
        with dissolve
        pause(0.5)
        scene wmom_yoga2_bg defeat
        with Dissolve(3)

        show wmom_yoga2_face defeat
        wmom "Oh no, Darling!{w=[wt2]} This way it hurts too much!{w=[wt4]} You should be more gentle to Mommy next time, okay?"

        scene bg_0
        with Dissolve(2)
        play SE1 "FailurePiano.ogg"

        $ add_stat("wmom", "love", -2)
        pause(1)

        stop BGM fadeout 1

        $ a_event_0 = ((17*2) - (2 * (gametimehour + (gametimemin/60))))
        $ add_stat("wmom", "inti", a_event_0)
        pause(1)

        play BGM "audio/W2C - Tranquility.mp3"

        $ quick_menu = True
        $ config.allow_skipping = True
        $ config.rollback_enabled = True

        $ gametimehour = 17
        $ gametimemin = 0
        call gametime from _call_gametime_107
        jump show_ui

    label minigame_wmomyoga_victory:
        hide screen minigameplay_hold
        hide screen minigameshow_yoga
        $ renpy.block_rollback()
        $ config.rollback_enabled = False
        $ config.allow_skipping = False
        $ config.skipping = False

        play BGM "audio/W2C - Subtitle.mp3"

        scene bg_1
        with dissolve
        pause(0.5)
        scene wmom_yoga2_bg victory
        with Dissolve(3)

        show wmom_yoga2_face victory
        wmom "{bt}Look, Darling!{w=[wt1]} Look!{/bt}{w=[wt2]} I feel like I can stretch much better now!{w=[wt4]} That's all thanks to you!"

        scene bg_1
        with Dissolve(2)
        $ add_stat("wmom", "love", 5)
        pause(1)

        stop BGM fadeout 1

        $ a_event_0 = ((17*2) - (2 * (gametimehour + (gametimemin/60))))
        $ add_stat("wmom", "inti", a_event_0)
        pause(1)

        play BGM "audio/W2C - Tranquility.mp3"

        $ quick_menu = True
        $ config.allow_skipping = True
        $ config.rollback_enabled = True

        $ gametimehour = 17
        $ gametimemin = 0
        call gametime from _call_gametime_108
        jump show_ui

#---------------------------------------------------------------------------
label wmom_massage:
#---------------------------------------------------------------------------
    
    play SE1 "DoorOpen2.ogg"
    scene wmom_massage1_bg
    show wmom_massage1_wmom
    show wmom_massage1_face a0
    with Dissolve(2)

    play BGM "audio/W2C - Lust.mp3"

    if gametimeday == 1:
        mind "(Ehhh!?{w=[wt2]} She looks so{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} Vulnerable.{w=[wt3]} Am I really allowed to just enter like this?)"

        show wmom_massage1_face a2 with Dissolve(1)

        show wmom_massage1_face a1

        wmom "Oh, {nm}[wmom_to_hero]{/nm}{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Mommy was so tired that almost slept while waiting!{w=[wt1]} {gg}Tee-hee...{/gg}"

        show wmom_massage1_face a2
        hero "S{w=[wt1]}-sorry{w=[wt2]}, I just finished cleaning everything up."
        
        show wmom_massage1_face a1
        wmom "No!{w=[wt1]} That was not what I meant, {nm}[wmom_to_hero]{/nm}.{w=[wt2]} Of course it's not your fault.{w=[wt3]} You're such a sweetheart for taking care of me!{w=[wt4]} Please, come in!{w=[wt2]} Mommy needs a massage right now! ~❤"
        
        show wmom_massage1_face a2
        hero "S{w=[wt1]}-sure!"

    else:

        show wmom_massage1_face a2 with Dissolve(1)

        show wmom_massage1_face a1

        wmom "{bt}Ara ara...{/bt}{w=[wt2]} What a lovely surprise!{w=[wt3]} So{w=[wt2]}, what brings {nm}[wmom_to_hero]{/nm} to mommy's room at this hour?{w=[wt1]} {gg}Tee-hee...{/gg}"
        
        show wmom_massage1_face a2

        menu:
            "Offer massage":
                hero "Would you like a massage?"
                show wmom_massage1_face a1
                wmom "{bt}Ara ara...{/bt}{w=[wt2]} You're so sweet, {nm}[wmom_to_hero]{/nm}!{w=[wt3]} How could I say no to something like that?{w=[wt1]} {gg}Tee-hee...{/gg}{w=[wt4]} Please, come in!{w=[wt2]} Mommy could really use that right now."
            
            "Just chat":
                hero "Just wanted to talk a bit."
                show wmom_massage1_face a1
                wmom "Awn...{w=[wt2]} That's so sweet, {nm}[wmom_to_hero]{/nm}!{w=[wt3]} Please, come in!"
                $ wmom_know.append("interacting_hero")
                $ hero_map = "Home - Step-mother's bedroom"
                call check_playermap from _call_check_playermap_42
                jump wmom_interact_start
            
            "Return":
                hero "A{w=[wt1]}-actually{w=[wt2]}, maybe I should let you rest."
                show wmom_massage1_face a1
                wmom "{gg}Tee-hee...{/gg}{w=[wt3]} Well{w=[wt2]}, good night then, {nm}[wmom_to_hero]{/nm}!{w=[wt3]} Sweet dreams!{w=[wt3]} If you change your mind{w=[wt2]}, know mommy would really love to spend a little time with her big boy before sleep! ~❤"
                jump show_ui

        show wmom_massage1_face a2 with None

        jump wmom_massage_1

#---------------------------------------------------------------------------
label wmom_massage_1:
#---------------------------------------------------------------------------
    scene wmom_massage3_bg with Fade(1,0,2)

    wmom "{bt}Mmmmm...{/bt}{w=[wt3]} {bt}Right there, honey...{/bt}{w=[wt3]} {bt}You have such strong hands...{/bt}{w=[wt3]}"
    
    hero "Your shoulders are really tense{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} No wonder you've been having back pain."
    
    wmom "{bt}Ohhh...{/bt}{w=[wt3]} {bt}Yes...{/bt}{w=[wt4]} A bit lower please...{w=[wt4]} {bt}Ahhh...{/bt}"
    
    mind "(Her skin is so soft{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} And she keeps making those sounds!)"
    
    wmom "{nm}[wmom_to_hero!c]{/nm}, you're amazing at this!{w=[wt3]} Where did you learn to{w=[wt1]}- {bt}Ahhh...!{/bt}{w=[wt3]} {bt}Yes...{/bt}{w=[wt2]}, {bt}right there!{/bt}"
    
    hero "I{w=[wt1]}-I'm just trying my best. {gg}He-He...{/gg}"
    
    wmom "{bt}Mmmm...{/bt}{w=[wt4]} {bt}Such a good boy...{/bt}{w=[wt4]} Taking such good care of your{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt1]} {bt}Mmmm...{/bt}{w=[wt4]} {bt}Mommy...{/bt}"
    
    hero "I{w=[wt1]}-I think it's done {nm}[hero_to_wmom]{/nm}"

    wmom "That was wonderful{w=[wt1]} {nm}[wmom_to_hero]{/nm}.{w=[wt3]} Mommy feels so much better now!"
    
    hero "G{w=[wt1]}-glad I could help.{w=[wt3]} You should get some rest now."
    
    wmom "Thank you so much, {nm}[wmom_to_hero]{/nm}.{w=[wt1]} {gg}Tee-hee...{/gg}{w=[wt4]} Sweet dreams!"
    
    $ add_stat("wmom", "love", 1)
    $ wmom_lust += (1 + perk_cha_sex) * lustadd_wmom
    $ msg.msg(renpy.translate_string("{nm}[fnamewmom]{/nm}'s  lust {color=#32FF32}+")+str((1 + perk_cha_sex) * lustadd_wmom)[:4])
    $ add_stat("wmom", "inti", 0.6)
    $ add_stat("hero", "cha_sex", 1.6)

    $ gametimemin += 60

    scene bg_0 with Dissolve(1)

    if gametimeday == 1:
        $ hero_map = "Home - My bedroom"
        scene bg_home bedroom hero
        with Fade(3,1,3)
    else:
        $ hero_map = "Home - Hallway"

    jump show_ui
