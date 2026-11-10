# ----------------------------------------------------------------------------------------------------
# CHANGING ROOM — data-driven cast display (images/Action/Changing/)
# ----------------------------------------------------------------------------------------------------
# Nothing here is per-character: the cast is built from the image NAMES, so dropping new files in images/Action/Changing/ is the whole job of adding a girl or an outfit — no code change needed.
#
#   Naming pattern
#       1. Body      -> `action_change_<char_id>_<variant>_body`      (file: action_change_wnei_1_body.webp)
#       2. Outfit    -> `action_change_<char_id>_<variant>_wear <id>` (file: action_change_wnei_1_wear school.webp)
#       3. Room      -> `action_change_bg <room_id>`                  (file: action_change_bg school_locker_f.webp)
#
#   Art specs
#       1. Sprites are vertical 1080x1920 (high-res for zoom/close-ups), anchored mid-bottom on the floor.
#       2. Backgrounds and midgrounds are 1920x1080 (full screen).
#
#   Outfit fallback (per spec): requested wear -> "under" -> nothing (body only).
# ----------------------------------------------------------------------------------------------------

define CHANGE_ROOM = "school_locker_f"                          # default room bg attribute
define CHANGE_ART_SIZE = (1080, 1920)                           # source sprite resolution
define CHANGE_SCALE = 0.50                                      # stage zoom of a sprite (tune here, room is near-orthographic)
define CHANGE_TAG = "chg"                                       # show-tag prefix, one tag per SLOT (a char can fill several)
define CHANGE_Z_STEP = 10                                       # zorder gap between slots, so midgrounds can sit between them
define CHANGE_Z_FX = 500                                        # `fx_light` on top of everything

# Floor slots as (x, y) of the sprite's MID-BOTTOM, listed BACK-TO-FRONT — list order is the draw order, so a cast placed in order is already Y-sorted. Slots 6-7 stand below the screen edge (cropped legs).
define CHANGE_SLOTS = [
    (1050,  900), # 1
    ( 800,  950), # 2
    # `action_change_mg_2 school_locker_f`
    (1500,  975), # 3
    (1700, 1050), # 4
    ( 650, 1100), # 5
    ( 250, 1200), # 6
    # `action_change_mg_1 school_locker_f`
    (1350, 1150), # 7
    ( 990, 1250), # 8
    ]

define CHANGE_SLOT_SCALE = {}                                   # optional per-slot zoom override, e.g. {0: 0.58}
define CHANGE_SLOT_FLIP = []                                    # optional slot indexes to mirror horizontally

# Room midgrounds (`action_change_mg_<n> <room_id>`), keyed by the slot they are drawn BEHIND — so mg_2 covers slots 0-1 (the back pair) and mg_1 covers slots 0-5 (everything but the front pair).
define CHANGE_MG = {2: 2, 6: 1}

# ----------------------------------------------------------------------------------------------------
# CLOSE-UP CAMERA (view 2) — zoom the whole stage so a sprite reads at its native size
# ----------------------------------------------------------------------------------------------------
# The room is drawn near-orthographic and the girls stand at CHANGE_SCALE, so zooming the master layer by 1/CHANGE_SCALE puts a sprite at 100% and the scenery at 200% — no second set of art.
define CHANGE_ZOOM = 1.0 / CHANGE_SCALE                         # stage zoom for the close-up (0.50 -> 2.0)
define CHANGE_ZOOM_FOCUS = 0.80                                 # focus point up the body (1.0 = her head, 0 = her feet)
define CHANGE_ZOOM_AT = (0.5, 0.45)                             # where that point sits on screen (xalign, yalign)
define CHANGE_ZOOM_TIME = 0.5                                   # ease time when stepping to another girl

# ----------------------------------------------------------------------------------------------------
# JUDGEMENT (views 3-4) — the confrontation panel and its verdict
# ----------------------------------------------------------------------------------------------------
define CHANGE_PANEL_SIZE = 4                                    # girls who step up to judge HERO
define CHANGE_PANEL_AT = ["LC", "CC", "RC", "RR"]               # their stage marks (HERO takes LL)

# What the panel girls have ON when the scene cuts to base sprites. These are NOT shares of 100 — they are independent chances walked as a chain, and a step is skipped when either its roll fails or she has no sprite for it: target -> towel -> under -> nude. So nudity is never a probability of its own, it is only what is left when a girl has no `under` art to fall back on.
define CHANGE_PANEL_DRESSED = 50                                # % already in the outfit she was changing into
define CHANGE_PANEL_TOWEL = 25                                  # % in a towel (art: wsis/wmom only, so far)
define CHANGE_PANEL_UNDER = 100                                 # % in underwear (art: wsis/wmom/wnei/wcou)

# Verdict roll (Ideas.md §6.1, approved 2026-07-16 — tuning expected now that it is playable):
#   forgive% = CHANGE_FORGIVE_BASE + inti*0.5 + love*0.2 - chastity*0.35 + purity³*0.0001 + <explanation modifier>
define CHANGE_FORGIVE_BASE = 10
define CHANGE_FORGIVE_INTI = 0.5
define CHANGE_FORGIVE_LOVE = 0.2
define CHANGE_FORGIVE_CHASTITY = -0.35
define CHANGE_FORGIVE_PURITY = 0.0001

define CHANGE_MOD_MISSION = 25                                  # SC errand, and the errand is real
define CHANGE_MOD_LIE = -15                                     # SC errand claimed with no quest active
define CHANGE_MOD_SORRY = 10                                    # the mid option — more answers can be added as new menu branches + their own CHANGE_LINES_ANSWER_* table

define CHANGE_REACT_LADDER = [100, 80, 60, 40, 20]              # §5.1 — chance the Nth girl reacts at all
define CHANGE_CROSS_CHANCE = 50                                 # % a judging girl answers the one before her

# How flustered she looks, from chastity: below SHY nothing, below FLUSH a light blush, above it the strong one. The roll jitters her chastity by ±CHANGE_FX_RANDOM so the same girl is not identical every time.
define CHANGE_FX_SHY = 30
define CHANGE_FX_FLUSH = 60
define CHANGE_FX_RANDOM = 0.15

# Moods used across the scene, named so the intent is readable at the call sites: A1 happy, A2 relieved/sheepish/compassionate, O1 angry, O2 sad.
define CHANGE_MOOD_SOFT = "O2"                                  # sad — she is upset but not hostile
define CHANGE_MOOD_ANGRY = "O1"
define CHANGE_MOOD_WARM = "A2"                                  # relieved / won over
define CHANGE_MOOD_HAPPY = "A1"

# ----------------------------------------------------------------------------------------------------
# DIALOGUE TABLES — keyed by char_id with a "*" fallback, so giving a girl her own voice is a data edit
# ----------------------------------------------------------------------------------------------------
define CHANGE_LINES_REACT = {
    "wsis": [
        "{aw}Ugh{/aw}{w=[wt2]}, you pervert!{w=[wt4]} {pa}GET OUT OF HERE!!!{/pa}",
        ],
    "wnei": [
        "Oh{w=[wt2]}, ya here!{w=[wt3]} Wait just a little bit.{w=[wt2]} I'm almost ready!",
        "Oh{w=[wt2]}, [C_Nam][fnamehero][C_Off]!{w=[wt2]} Are ya feeling like a girl?",
        "Hey, [C_Nam][fnamehero][C_Off]!",
        "Hey, [C_Nam][fnamehero][C_Off]{w=[wt2]}, did ya come to help me?",
        ],
    "wpre": [
        "{aw}Ehhh!?{/aw} [C_Nam][fnamehero][C_Off]{w=[wt2]}, what are you doing here!?{w=[wt2]} This is a {i}restricted{/i} area.{w=[wt2]} Y{w=[wt1]}-you are in serious violation right now.",
        "[C_Nam][fnamehero][C_Off]{w=[wt1]}-[C_Nam][fnamehero][C_Off]!?{w=[wt2]} Please, face the door.{w=[wt2]} {size=+10}Now!{/size}{w=[wt3]} Everyone stay calm.",
        ],
    "wric": [
        "How {b}dare{/b} you!?{w=[wt2]} Do you have any idea whose body you are looking at!?",
        "Unbelievable.{w=[wt2]} Commoners truly have no shame whatsoever!",
        ],
    "wgal": [
        "Oh{w=[wt2]}, seriously?{w=[wt3]} Like{w=[wt2]}, are you looking for your mom?{w=[wt2]} At this hour she's out there turning tricks!{w=[wt3]} {aw}Get out!!!{/aw}",
        "{aw}Kyaaahh!{/aw}{w=[wt4]} Go spy that bitch of your mother{w=[wt2]}, asshole!",
        ],
    "wdis": [
        "{aw}Kyaah!{/aw}{w=[wt2]} I{w=[wt1]}-{w=[wt1]}I{w=[wt1]}-{w=[wt1]}sorry! Wait{w=[wt2]}, why am {b}I{/b} sorry?!",
        "{aw}Eep!{w=[wt2]} P{w=[wt1]}-please{w=[wt2]}, don't look{w=[wt2]}, don't look!{/aw}",
        ],
    "wota": [
        "{aw}Kyaah!{/aw}{w=[wt2]} Damn, this is {i}exactly{/i} how the ecchi scene starts.",
        "{aw}Kyaah!{/aw}{w=[wt2]} H{w=[wt1]}-{w=[wt1]}hold on{w=[wt2]}, T{w=[wt1]}-this is way too fast for a first event!",
        ],
    "wdel": [
        "Yo, {size=+10}dude{/size}.{w=[wt2]} Pussies only!",
        "{bt}Ehhh...!?{/bt}{w=[wt2]} Feeling like a girl today?{w=[wt2]} You'd better turn around before I turn you into a real one by kicking you in the balls so hard!",
        "Seriously, bro?{w=[wt2]} You better have a good explanation before I make this a problem.",
        ],
    "wgot": [
        ".{w=[wt1]}.{w=[wt1]}.{w=[wt2]}Of course.{w=[wt2]} Of course today would end like this.",
        ],
    "wlaz": [
        "{aw}Ugh{/aw}{w=[wt2]} Man{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Seriously...?{w=[wt3]} What a drag, huh?"
        ],
    "wuza": [
        "{bt}Ehhh!?!?{/bt}{w=[wt2]} What are you doing here, buddy!?!?",
        "{aw}Whoa whoa whoa{/aw} dude!{w=[wt2]} That's the female locker room, you know?",
        "Heh!?{w=[wt2]} Are you feeling like a girl today?",
        ],
    "*": [
        "Get {size=+10}OUT{/size} of here!",
        "{aw}Kyaaah!{/aw}{w=[wt2]} What are you doing here!?",
        "H{w=[wt1]}-hey!{w=[wt2]} This is the {b}girls'{/b} locker room!",
        "{pa}KYAAAH!!!{/pa}",
        "{pa}A PERVERT!!!{/pa}",
        ],
    }

# Round 3 — each panel girl states where she stands.
define CHANGE_LINES_FORGIVE = {
    "wsis": [
        "{aw}Ugh{/aw}{w=[wt2]}, I'll have to vouch for him.{w=[wt2]} He's not stupid enough to walk in here without a reason.",
        ],
    "wnei": [
        "I gotcha, [C_Nam][fnamehero][C_Off]{w=[wt2]}! We know you're a super duper cool guy!",
        "Ohhh{w=[wt2]}, so that was just a bad time then, right?{w=[wt3]} Gotcha!",
        "Well{w=[wt2]}, don't worry.{w=[wt3]} If you change clothes here with us from now on it'll be way more fun!",
        ],
    "wpre": [
        "Understood.{w=[wt2]} So that was the case.{w=[wt4]} Please{w=[wt2]}, just be more attentive before entering next time.",
        "So that was it.{w=[wt2]} I trust you, [C_Nam][fnamehero][C_Off].{w=[wt3]} Please be more careful.",
        ],
    "wric": [
        "{aw}Hmph!{/aw}{w=[wt2]} I refuse to have my name attached to a {b}scandal{/b} over this.{w=[wt3]} Let's just let him go.",
        "He is beneath my concern.{w=[wt2]} Punishing him would only prolong it.",
        ],
    "wgal": [
        "Okay{w=[wt2]}, you really seem to be just too stupid.{w=[wt3]} I'll let this one slide.",
        ],
    "wdis": [
        "I walk into wrong rooms like{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} constantly.{w=[wt2]} I can't judge him.",
        "It was an accident!{w=[wt2]} I{w=[wt1]}-{w=[wt1]}I know what those look like!",
        ],
    "wota": [
        "The accidental route is a {i}classic{/i}.{w=[wt2]} You don't punish the classic.",
        ],
    "wdel": [
        "He froze like a chicken.{w=[wt2]} That ain't a criminal{w=[wt2]}, that's a dumbass.{w=[wt3]} Let him walk.",
        ],
    "wgot": [
        "Ruining someone over a mistake{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} That's uglier than what he did.",
        ],
    "wlaz": [
        "Reporting stuff is so much work.{w=[wt2]} He's fine.{w=[wt2]} Moving on.",
        "Eh.{w=[wt2]} Nobody died.{w=[wt2]} Can we just get dressed?",
        ],
    "wuza": [
        "{lg}GAH HA HA HA...{/lg}{w=[wt2]} SO THAT WAS IT! {bt}HOW FUNNY!!! HOW FUNNY!!!{/bt}",
        "{bt}OHHHH!{/bt}{w=[wt2]} So that means you're neither a pervert nor gay!?{w=[wt2]}{pr}{pa}GOTCHA!!!{/pa}",
        ],
    "*": [
        "Yeah{w=[wt2]}, it really seems to be an accident.{w=[wt2]} I think he didn't {i}plan{/i} this.",
        "It's okay.{w=[wt2]} I think he's telling the truth.{w=[wt3]} Look at his face.{w=[wt2]} He's more scared than we are.",
        "Okay{w=[wt2]}, it seems he's telling the truth.{w=[wt2]} Just let's let it go.",
        ],
    }

define CHANGE_LINES_PUNISH = {
    "wsis": [
        "{aw}Ugh{/aw}{w=[wt2]}, no.{w=[wt2]} He gets away with {b}everything{/b} .{w=[wt3]} Not this time!",
        "I know him and I'm {b}still{/b} not covering for this one.{w=[wt2]} Report it.",
        ],
    "wnei": [
        "Gals are saying ya can't stay here.{w=[wt2]} We better another time.",
        ],
    "wpre": [
        "If I may{w=[wt1]}.{w=[wt1]}.{w=[wt1]}.{w=[wt3]} Rules exist precisely for moments like this.{w=[wt3]} I cannot let it pass.{w=[wt3]} Sorry, [C_Nam][fnamehero][C_Off].",
        "I'm sorry, [C_Nam][fnamehero][C_Off]{w=[wt2]}, but if I ignore this, I have no standing the next time it happens to someone else.",
        ],
    "wric": [
        "{aw}Tsk tsk.{/aw}{w=[wt2]} He will learn that some doors are simply not his to open.",
        "Let it be documented.{w=[wt2]} My family does not tolerate {i}this{/i} sort of thing.",
        ],
    "wgal": [
        "Nuh{w=[wt2]}-uh{w=[wt2]}, like{w=[wt2]}, this is {bt}SOOO{/bt} gross, you know?{w=[wt2]} And {bt}EVERYONE{/bt}'s gonna know about it, you total {b}looser{/b}!",
        "{bt}TOTALLY{/bt} not my problem now.{w=[wt3]} {aw}Ugh...!{/aw}{w=[wt3]} {bt}Disgusting!{/bt}{w=[wt3]} You won't pass this, you stupid jerk!",
        ],
    "wdis": [
        "I{w=[wt1]}-{w=[wt1]}I'm sorry{w=[wt2]}, but I was really scared!{w=[wt3]} That's not nothing{w=[wt1]}, right{w=[wt1]}...?",
        "Even if it was an accident{w=[wt1]}.{w=[wt1]}.{w=[wt1]}{w=[wt2]} accidents still {b}hurt{/b} people...",
        ],
    "wota": [
        "You're abusing your protagonist powers, you idiot.{w=[wt3]} Don't think you're going to get away with this so easily!",
        "{aw}That is unforgivable!{/aw}{w=[wt3]} If I can't walk into the men's restroom by mistake and see you guys showering together while soaping and rubbing your wet bodies against each other, {b}THEN YOU CAN'T JUST COME IN HERE TOO!{/b}{w=[wt4]} I vote for your eternal condemnation!!!",
        ],
    "wdel": [
        "Nah{w=[wt2]}, bro.{w=[wt2]} You stare{w=[wt1]}, you pay.{w=[wt3]} That's just how it works{w=[wt1]}, {i}ya hear{/i}?",
        "He had a way out and he just {b}stood{/b} there like an asshole.{w=[wt3]} That's a choice.{w=[wt3]} How about we make him drink water from the toilet?",
        "I don't give a shit, dude.{w=[wt3]} The cure for a perversion is a punch!",
        ],
    "wgot": [
        "Poor thing.{w=[wt3]} You were overcome by your most primitive instincts and couldn't control yourself.{w=[wt2]} Now you are being judged by your own victims.{w=[wt3]} I hope your death is painless.",
        "His upper head was betrayed by the one down below.{w=[wt3]} Maybe we should cut it off.{w=[wt3]} Would someone have a knife?",
        "How sadly tragic.{w=[wt3]} You gazed at every part of my nude body with those wicked eyes that drained my soul.{w=[wt3]} Now I can no longer marry.{w=[wt3]} You shall pay with your life.",
        "How painful.{w=[wt3]} You should have just killed me faster than made me suffer from all this embarrassment.",
        ],
    "wlaz": [
        "Yeah{w=[wt1]}, no.{w=[wt2]} If I gotta deal with this{w=[wt1]}, so does he.",
        "Eh!?{w=[wt2]} What do you think you are?{w=[wt2]} The protagonist of a hentai visual novel game?{w=[wt4]} That’s not going to fly, dude!",
        "Doing something about it is going to be a hassle{w=[wt1]}, but letting it slide will be an even bigger hassle{w=[wt1]}, cause he'll know he can get away with it.{w=[wt4]} What a drag...",
        ],
    "wuza": [
        "{gg}Gee-Hee-Hee...{/gg}{w=[wt1]} What do we do with him, huh?{w=[wt3]} {bt}What to do...? What to do...?{/bt}{w=[wt4]} Oh!{w=[wt2]} How about tying him up and locking him in the toilet stall?{w=[wt3]} {bt}Let's do it...! Let's do it...!{/bt}",
        "{lg}CHA HA HA HA!!!{/lg}{w=[wt2]} {bt}Nice one, bro...! Nice one...!{/bt}{w=[wt4]}{pr}{pa}RIGHT!{/pa}{w=[wt3]} {bt}Time to call the police!{/bt}",
        ],
    "*": [
        "Accident or not, you {b}stood there{/b}.{w=[wt2]} That can't pass.",
        "No.{w=[wt2]} If we let this slide, he'll just do it again.",
        "Your excuses don't even make sense!",
        "I don't care.{w=[wt2]} You shouldn't be here!",
        "Don't let him fool you!{w=[wt2]} He did something very pervert!",
        ],
    }

# Round 2 — one girl answers HERO's excuse on the spot. One table per menu option, so nothing in this scene is a hard-coded line any more.
define CHANGE_LINES_ANSWER_LIE = {                              # he claimed an SC errand that does not exist
    "wsis": ["Nice try.{w=[wt2]} I'd {i}know{/i} if you had a job here, genius."],
    "wnei": ["Oh!{w=[wt2]} But{w=[wt1]}...{w=[wt2]} nobody told me about that, and I'd have heard?"],
    "wpre": ["I sign every locker-room errand personally.{w=[wt2]} I signed nothing today."],
    "wric": ["A liar {i}and{/i} a peeper.{w=[wt2]} How thoroughly common."],
    "wgal": ["Babe.{w=[wt2]} {i}Babe.{/i}{w=[wt2]} That is such a lie, I can't even."],
    "wdis": ["B{w=[wt1]}-{w=[wt1]}but the Council would have put a sign up{w=[wt1]}...{w=[wt2]} wouldn't they?"],
    "wota": ["Weak excuse.{w=[wt2]} Zero out of ten, wouldn't believe again."],
    "wdel": ["Bro.{w=[wt2]} You're bad at this.{w=[wt2]} Real bad."],
    "wgot": ["Funny.{w=[wt2]} The Council didn't send {i}anyone{/i} today."],
    "wlaz": ["Mm.{w=[wt2]} Nah.{w=[wt2]} Made that up on the spot, huh."],
    "wuza": ["Wrong answer.{w=[wt2]} Try the {i}true{/i} one."],
    "*": ["Funny.{w=[wt2]} The [C_Dat]Council[C_Off] didn't send {i}anyone{/i} today."],
    }

define CHANGE_LINES_ANSWER_MISSION = {                          # the errand is real, and it still does not help
    "wsis": ["Oh, so it's {i}official{/i} business.{w=[wt2]} That makes it {i}so{/i} much better."],
    "wnei": ["Oh, you're working!{w=[wt2]} Um{w=[wt1]}...{w=[wt2]} should we wait outside, then?"],
    "wpre": ["Your errand does not suspend the rules on this door.{w=[wt2]} It only explains you."],
    "wric": ["An errand.{w=[wt2]} How convenient for you that it led {i}here{/i}."],
    "wgal": ["Okay, but like{w=[wt1]}...{w=[wt2]} that's still not a {i}knock{/i}, is it?"],
    "wdis": ["Th{w=[wt1]}-{w=[wt1]}then you should have said so from the door!"],
    "wota": ["Ah, the plot-mandated excuse.{w=[wt2]} Convenient timing, protagonist."],
    "wdel": ["And that's supposed to fix this how, exactly?"],
    "wgot": ["A reason isn't the same as permission.{w=[wt2]} Remember that."],
    "wlaz": ["Sure, whatever.{w=[wt2]} Still didn't knock though."],
    "wuza": ["Errand or not, you had a door and a voice.{w=[wt2]} Use them."],
    "*": ["And that's supposed to make it {i}better{/i}?!"],
    }

# Round 3 cross-talk — she answers the girl who spoke before her. AGREE is stance-neutral; the two DISAGREE tables are NOT, so they are picked by HER OWN verdict (a forgiving girl must never use a harsh line).
define CHANGE_LINES_AGREE = {
    "*": [
        "She's right.{w=[wt2]} I was thinking the same.",
        "Yeah{w=[wt1]}...{w=[wt2]} yeah, that's fair.",
        "Two of us, then.",
        "Same. Put me down with her.",
        ],
    }

define CHANGE_LINES_DISAGREE_SOFT = {                           # she forgives, the girl before her did not
    "*": [
        "Whoa{w=[wt1]}-{w=[wt1]}that's a bit much, isn't it?",
        "Come on, you don't really mean that.",
        "I think you're being way too hard on him.",
        "Hold on.{w=[wt2]} Let's not ruin somebody over this.",
        ],
    }

define CHANGE_LINES_DISAGREE_HARD = {                           # she punishes, the girl before her forgave
    "*": [
        "Are you {i}serious{/i}?{w=[wt2]} You can't be soft about this.",
        "That's easy for {i}you{/i} to say.",
        "No.{w=[wt2]} I don't see it that way at all.",
        "You're really going to defend him right now?",
        ],
    }

# Round 4 — one girl who already spoke announces where it landed. The table is chosen by the verdict AND by HER OWN vote, so she never argues one way and then narrates the other.
define CHANGE_LINES_END_FORGIVE = {                             # verdict: forgiven — and she voted for it
    "wsis": ["You're off the hook.{w=[wt2]} And you {i}owe{/i} me, so wipe that look off your face.{w=[wt2]} Knock. Next. Time."],
    "wnei": ["Everyone's okay!{w=[wt2]} Just{w=[wt1]}...{w=[wt2]} please say something before you come in, okay?"],
    "wpre": ["No report will be filed.{w=[wt2]} Consider this a formal warning, and knock in future."],
    "wric": ["You may go.{w=[wt2]} Do try to remember which doors are yours."],
    "wgal": ["We're letting it slide, babe.{w=[wt2]} But like{w=[wt1]}...{w=[wt2]} {i}knock{/i}. It's free."],
    "wdis": ["W{w=[wt1]}-{w=[wt1]}we're okay!{w=[wt2]} Just knock next time{w=[wt1]}...{w=[wt2]} for both our sakes."],
    "wota": ["Route cleared.{w=[wt2]} Next time, though?{w=[wt2]} Knock first. It's basic etiquette."],
    "wdel": ["You're good, bro.{w=[wt2]} Knock next time or I {i}will{/i} change my vote."],
    "wgot": ["It's over.{w=[wt2]} Nobody's saying anything{w=[wt1]}...{w=[wt2]} but knock. Please."],
    "wlaz": ["Cool, we're done.{w=[wt2]} Just knock next time so I don't gotta do this again."],
    "wuza": ["We're square.{w=[wt2]} Knock next time and we'll stay that way."],
    "*": [
        "We're{w=[wt1]}...{w=[wt2]} letting it go.{w=[wt2]} But {size=+10}knock{/size} next time, okay?",
        "Nobody's telling anyone.{w=[wt2]} Just{w=[wt1]}-{w=[wt1]}announce yourself, {i}please{/i}.",
        ],
    }

define CHANGE_LINES_END_FORGIVE_GRUDGE = {                      # verdict: forgiven, but she wanted otherwise
    "*": [
        "They're letting it go.{w=[wt2]} {i}I'm{/i} not{w=[wt1]}-{w=[wt1]}but I'm outvoted, so go.",
        "You got lucky.{w=[wt2]} That's all this is.{w=[wt2]} Luck.",
        "Fine.{w=[wt2]} Majority wins.{w=[wt2]} I'll be watching you though.",
        ],
    }

define CHANGE_LINES_END_PUNISH_SORRY = {                        # verdict: punished, and she argued against it
    "wsis": ["I {i}tried{/i}, okay?{w=[wt2]} I actually stuck my neck out for you{w=[wt1]}...{w=[wt2]} it wasn't enough."],
    "wnei": ["I'm sorry{w=[wt1]}...{w=[wt2]} I said you didn't mean it, I promise I did.{w=[wt2]} They didn't listen."],
    "wpre": ["I argued for a warning and I lost the room.{w=[wt2]} It goes on the record now."],
    "wric": ["I spoke on your behalf{w=[wt1]}-{w=[wt1]}do {i}not{/i} make me regret it.{w=[wt2]} It is out of my hands."],
    "wgal": ["I was totally on your side, babe!{w=[wt2]} But like{w=[wt1]}...{w=[wt2]} it's out there now."],
    "wdis": ["I said it was an accident{w=[wt1]}...{w=[wt2]} I'm sorry, I couldn't change their minds."],
    "wota": ["Bad end.{w=[wt2]} I voted for the good one, for what it's worth."],
    "wdel": ["I had your back, bro.{w=[wt2]} Got outnumbered.{w=[wt2]} It's going up the chain."],
    "wgot": ["I tried.{w=[wt2]} People rarely choose mercy{w=[wt1]}...{w=[wt2]} I should have expected it."],
    "wlaz": ["I said leave it alone.{w=[wt2]} Nobody listens to the lazy one, huh."],
    "wuza": ["I fought your corner and I lost it.{w=[wt2]} Take it standing up."],
    "*": [
        "I tried to talk them down.{w=[wt2]} I'm sorry{w=[wt1]}...{w=[wt2]} this one's going further.",
        "It's out of my hands now.{w=[wt2]} They want it reported.",
        ],
    }

define CHANGE_LINES_END_PUNISH_HARD = {                         # verdict: punished, and she wanted it
    "*": [
        "It's decided.{w=[wt2]} This is going where it needs to go.",
        "You should have left when you had the chance.{w=[wt2]} Now it's official.",
        "That's it.{w=[wt2]} We're reporting it!",
        ],
    }

# Master-layer camera. Applied with reset=False so a new call EASES from wherever the camera already is.
transform change_camera(ox, oy, z, t):
    ease t zoom z xoffset ox yoffset oy

transform change_camera_reset:
    zoom 1.0 xoffset 0 yoffset 0

init python:

    # --------------------------------------------------
    def Change_Variants(char_id): # Pose variants that actually have a body image, low to high
    # --------------------------------------------------
        found = []
        for n in range(1, 10):
            if renpy.has_image("action_change_" + char_id + "_" + str(n) + "_body", exact=True):
                found.append(n)
        return found

    # --------------------------------------------------
    def Change_HasArt(char_id): # True when the char can appear in a changing scene at all
    # --------------------------------------------------
        return bool(Change_Variants(char_id))

    # --------------------------------------------------
    def Change_Variant(char_id, variant=None): # Resolve a usable variant (lowest available by default)
    # --------------------------------------------------
        found = Change_Variants(char_id)
        if not found:
            return None
        if variant in found:
            return variant
        return found[0]

    # --------------------------------------------------
    def Change_Wears(char_id, variant=None): # Outfit ids this char has art for, from the image attributes
    # --------------------------------------------------
        variant = Change_Variant(char_id, variant)
        if variant is None:
            return []
        tag = "action_change_" + char_id + "_" + str(variant) + "_wear"
        wears = set()
        for attrs in renpy.get_available_image_attributes(tag):
            for a in attrs:
                wears.add(a)
        return sorted(wears)

    # --------------------------------------------------
    def Change_WearImage(char_id, wear, variant=None): # Outfit image name, or None when she stays undressed
    # --------------------------------------------------
        # Spec fallback: the asked outfit, else "under", else no outfit layer at all.
        variant = Change_Variant(char_id, variant)
        if variant is None:
            return None
        base = "action_change_" + char_id + "_" + str(variant) + "_wear "
        for w in (wear, "under"):
            if w and renpy.has_image(base + w, exact=True):
                return base + w
        return None

    # --------------------------------------------------
    def Change_Wear(char_id): # The outfit she SHOULD be wearing right now (target of her `changing` activity)
    # --------------------------------------------------
        # While changing, `<char>_activity_current` is ("changing", "<wear>") — that param is the goal outfit.
        act = getattr(store, char_id + "_activity_current", None)
        if isinstance(act, tuple) and act[0] == "changing" and len(act) > 1:
            return act[1]
        return Get_NPCWear(char_id)                             # not changing: whatever she has on (None while bathing)

    # --------------------------------------------------
    def Change_Sprite(char_id, wear=None, variant=None): # Body + outfit stacked into one displayable
    # --------------------------------------------------
        variant = Change_Variant(char_id, variant)
        if variant is None:
            return None
        body = "action_change_" + char_id + "_" + str(variant) + "_body"
        outfit = Change_WearImage(char_id, wear, variant)
        if outfit is None:
            return body
        return Composite(CHANGE_ART_SIZE, (0, 0), body, (0, 0), outfit)

    # --------------------------------------------------
    def Change_At(slot): # Mid-bottom placement transform for a floor slot
    # --------------------------------------------------
        x, y = CHANGE_SLOTS[slot % len(CHANGE_SLOTS)]
        zoom = CHANGE_SLOT_SCALE.get(slot, CHANGE_SCALE)
        if slot in CHANGE_SLOT_FLIP:
            zoom = -zoom
        return Transform(pos=(int(x), int(y)), anchor=(0.5, 1.0), zoom=abs(zoom), xzoom=(-1 if zoom < 0 else 1))

    # --------------------------------------------------
    def Change_Z(slot): # Draw order of a slot, spaced so midgrounds fit between two girls
    # --------------------------------------------------
        return CHANGE_Z_STEP * (slot + 1)

    # --------------------------------------------------
    def Change_Show(char_id, slot, wear=False, variant=None): # Place one girl on a slot, returns True if shown
    # --------------------------------------------------
        # wear=False means "ask the schedule"; pass an explicit id (or None) to force one.
        sprite = Change_Sprite(char_id, Change_Wear(char_id) if wear is False else wear, variant)
        if sprite is None:
            return False
        renpy.show(CHANGE_TAG + "_" + str(slot), what=sprite, at_list=[Change_At(slot)], zorder=Change_Z(slot))
        return True

    # --------------------------------------------------
    def Change_ShowCast(char_ids, wears=False, start_slot=0): # Fill the slots back-to-front, returns the placed ids
    # --------------------------------------------------
        # Chars with no body art are skipped (girl-by-girl rollout), so the slots never leave a gap. The returned list is slot-ordered: placed[i] stands on slot start_slot + i. `wears`: False = ask the schedule, a dict = per char, anything else = that outfit for everyone.
        placed = []
        slot = start_slot
        for char_id in char_ids:
            if slot >= len(CHANGE_SLOTS):
                break
            wear = wears.get(char_id, False) if isinstance(wears, dict) else wears
            if Change_Show(char_id, slot, wear):
                placed.append(char_id)
                slot += 1
        return placed

    # --------------------------------------------------
    def Change_ShowRoom(char_ids, room=None, wears=False): # Whole stage in one go — bg + cast + midgrounds + light
    # --------------------------------------------------
        # Everything is shown WITHOUT a transition so the caller can fade the finished stage in one `with`; dissolving the bg first and then the girls made them pop in after the room.
        room = room or CHANGE_ROOM
        renpy.scene()
        renpy.show("action_change_bg " + room, zorder=0)
        placed = Change_ShowCast(char_ids, wears)
        for slot, n in CHANGE_MG.items():
            mg = "action_change_mg_" + str(n) + " " + room
            if renpy.has_image(mg, exact=True):
                renpy.show(mg, zorder=Change_Z(slot) - 1)
        renpy.show("fx_light", zorder=CHANGE_Z_FX)
        return placed

    # --------------------------------------------------
    def Change_Hide(slot=None): # Hide one slot, or every girl on stage
    # --------------------------------------------------
        for s in ([slot] if slot is not None else range(len(CHANGE_SLOTS))):
            renpy.hide(CHANGE_TAG + "_" + str(s))

    # --------------------------------------------------
    def Change_Cast(map_main="school", map_sub="locker_f", art=True): # Girls actually changing in that room
    # --------------------------------------------------
        # Same detection as the shower-stall bather scan (Action.rpy) — real schedule, no hand-written roster. art=False returns everyone mid-change including girls with no changing art, which is what the scene's replay guard needs: walking in must burn the window for the WHOLE room, drawn or not.
        room = Get_MapName(map_main=map_main, map_sub=map_sub)
        cast = []
        for c in NPC_IDS:
            if not c.startswith("w") or (art and not Change_HasArt(c)):
                continue
            if getattr(store, c + "_map", "") != room:
                continue
            act = getattr(store, c + "_activity_current", None)
            if (act[0] if isinstance(act, tuple) else act) == "changing":
                cast.append(c)
        return cast

    # --------------------------------------------------
    def Change_OopsCast(): # The crowd that triggers `action_change_oops`, slot-ordered — empty means no scene
    # --------------------------------------------------
        # Same gates as room_entry_exposure: unseen this change window, and she must know HERO (tier 1+).
        cast = [c for c in Change_Cast()
                if getattr(store, c + "_exposure_seen", None) != getattr(store, c + "_activity_time_start", 0)
                and intimacy_tier(c) >= 1]
        return Change_Order(cast)

    # --------------------------------------------------
    def Change_Order(cast): # Slot order: closest girls to the front, capped at the slot count
    # --------------------------------------------------
        # Design §2.4 — v1 places by `inti` alone; true friendship placement waits on Club Reputation §6.
        return sorted(cast, key=lambda c: stat_value(c, "inti"))[-len(CHANGE_SLOTS):]

    # --------------------------------------------------
    def Change_Speaker(cast, exclude=None): # Pick who talks, weighted by raw inti (closer girls speak more)
    # --------------------------------------------------
        pool = [c for c in cast if c != exclude]
        if not pool:
            return None
        weights = [1 + max(0, stat_value(c, "inti")) for c in pool]
        return renpy.random.choices(pool, weights=weights)[0]

    # --------------------------------------------------
    def Change_Line(lines, char_id): # One line from a table, personality table first when it has one
    # --------------------------------------------------
        # Tables are keyed by char_id with a "*" fallback, so writing a girl her own voice is a data edit.
        pool = lines.get(char_id) or lines.get("*")
        return renpy.random.choice(pool)

    # --------------------------------------------------
    def Change_Says(char_id, lines): # Speak one line from a table as that character
    # --------------------------------------------------
        # Dynamic speaker: these lines do NOT extract into tl/ — same accepted trade-off as the date hub.
        renpy.say(getattr(store, char_id), Change_Line(lines, char_id))

    # ------------------------------------------------------------------ close-up camera

    # --------------------------------------------------
    def Change_CameraAt(slot): # Layer offset that frames the girl on `slot` at native size
    # --------------------------------------------------
        # A layer scales from its top-left, so a room point lands at room_point*zoom + offset. Solve that for "her focus point sits at CHANGE_ZOOM_AT on screen", then clamp so the zoomed room always covers the screen (no empty edges at the walls).
        x, y = CHANGE_SLOTS[slot % len(CHANGE_SLOTS)]
        scale = abs(CHANGE_SLOT_SCALE.get(slot, CHANGE_SCALE))
        focus_y = y - CHANGE_ART_SIZE[1] * scale * CHANGE_ZOOM_FOCUS
        w, h = config.screen_width, config.screen_height
        ox = w * CHANGE_ZOOM_AT[0] - x * CHANGE_ZOOM
        oy = h * CHANGE_ZOOM_AT[1] - focus_y * CHANGE_ZOOM
        return (int(max(w - w * CHANGE_ZOOM, min(0, ox))),
                int(max(h - h * CHANGE_ZOOM, min(0, oy))))

    # --------------------------------------------------
    def Change_CameraTo(slot, time=None): # Ease the stage camera onto one girl
    # --------------------------------------------------
        ox, oy = Change_CameraAt(slot)
        t = CHANGE_ZOOM_TIME if time is None else time
        renpy.show_layer_at([change_camera(ox, oy, CHANGE_ZOOM, t)], layer="master", reset=False)

    # --------------------------------------------------
    def Change_CameraReset(): # Back to the plain full-room framing (MUST run before leaving the scene)
    # --------------------------------------------------
        renpy.show_layer_at([change_camera_reset], layer="master", reset=True)

    # ------------------------------------------------------------------ judgement panel

    # --------------------------------------------------
    def Change_SpriteWear(char_id, wear): # True when her BASE sprite has art for that outfit
    # --------------------------------------------------
        return renpy.loadable("images/Sprite/%s/%s body_wear %s.webp" % (char_id, char_id, wear))

    # --------------------------------------------------
    def Change_SpriteBare(char_id): # True when her base sprite has the undressed body (`body 0`)
    # --------------------------------------------------
        # Sprites using the two-body convention swap to `body 0` when `<char>_wear` is not a string. Girls drawn with a single `body` (WRIC) have no undressed state and must stay dressed.
        return renpy.loadable("images/Sprite/%s/%s body 0.webp" % (char_id, char_id))

    # --------------------------------------------------
    def Change_PanelWear(char_id): # Roll what she is wearing when the scene cuts to base sprites
    # --------------------------------------------------
        # A chain, not a single banded roll: each step needs BOTH its own chance and the art to exist, and a step that fails either way just hands over to the next one. Every step is checked against the real sprite file, because a `body_wear` entry can exist in the ConditionSwitch while resolving to `Null()`. renpy.random so a rollback re-shows the SAME outfit instead of redressing her mid-scene.
        for chance, wear in ((CHANGE_PANEL_DRESSED, Change_Wear(char_id)),
                             (CHANGE_PANEL_TOWEL, "towel"),
                             (CHANGE_PANEL_UNDER, "under")):
            if wear and renpy.random.randint(1, 100) <= chance and Change_SpriteWear(char_id, wear):
                return wear

        # Nothing in the chain landed. `body 0` girls end up undressed; a girl drawn with a single `body` (WRIC) has no undressed state, so she keeps her outfit rather than rendering as a dressed body wearing nothing.
        return None if Change_SpriteBare(char_id) else Change_Wear(char_id)

    # --------------------------------------------------
    def Change_Panel(cast, size=None): # The girls who confront HERO, inti-weighted, base-sprite gated
    # --------------------------------------------------
        pool = [c for c in cast if renpy.has_image(c.upper(), exact=True)]
        panel = []
        while pool and len(panel) < (CHANGE_PANEL_SIZE if size is None else size):
            pick = Change_Speaker(pool)
            pool.remove(pick)
            panel.append(pick)
        return panel

    # --------------------------------------------------
    def Change_ShowPanel(panel): # Place HERO + the panel on the marks, returns state to restore later
    # --------------------------------------------------
        # Their appearance is driven by the live <char>_wear/_mood/_fx vars the sprites read. Mood and fx are handed back to the caller to restore, but the rolled outfit is PINNED with `<char>_wear_override` instead: she keeps what she was caught in until her changing activity ends, rather than snapping back to her uniform the moment the scene fades.
        saved = {}
        for i, c in enumerate(panel):
            saved[c] = (getattr(store, c + "_mood", "A1"), getattr(store, c + "_fx", 0))
            _wear = Change_PanelWear(c)
            setattr(store, c + "_wear", _wear)
            setattr(store, c + "_wear_override", (_wear, getattr(store, c + "_activity_time_start", None)))

            # She opens sad if she is inclined to hear HERO out, angry if she is not — so the room reads before anyone speaks. How flustered she looks comes from her chastity.
            setattr(store, c + "_mood", CHANGE_MOOD_SOFT if Change_Lenient(c) else CHANGE_MOOD_ANGRY)
            setattr(store, c + "_fx", Change_Fx(c))
            renpy.show(c.upper(), at_list=[getattr(store, CHANGE_PANEL_AT[i % len(CHANGE_PANEL_AT)])])
        renpy.show("HERO", at_list=[store.LL])
        return saved

    # --------------------------------------------------
    def Change_RestorePanel(saved): # Give the schedule its mood/fx back
    # --------------------------------------------------
        # Wear is deliberately NOT restored — `<char>_wear_override` owns it until her changing activity ends.
        for c, (mood, fx) in (saved or {}).items():
            setattr(store, c + "_mood", mood)
            setattr(store, c + "_fx", fx)

    # ------------------------------------------------------------------ verdict

    # --------------------------------------------------
    def Change_Reactors(cast): # Round 1 — who reacts at all, on the 100/80/60/40/20 ladder
    # --------------------------------------------------
        pool, speakers = list(cast), []
        for chance in CHANGE_REACT_LADDER:
            if not pool or renpy.random.randint(1, 100) > chance:
                break
            pick = Change_Speaker(pool)
            pool.remove(pick)
            speakers.append(pick)
        return speakers

    # --------------------------------------------------
    def Change_Fx(char_id): # How flustered she looks, from chastity (0 none / 1 blush / 2 strong)
    # --------------------------------------------------
        # renpy.random keeps the same girl looking the same across a rollback.
        chastity = stat_value(char_id, "chastity") * renpy.random.uniform(1.0 - CHANGE_FX_RANDOM, 1.0 + CHANGE_FX_RANDOM)
        if chastity < CHANGE_FX_SHY:
            return 0
        elif chastity < CHANGE_FX_FLUSH:
            return 1
        return 2

    # --------------------------------------------------
    def Change_Mood(char_id, mood, panel=None): # Set her expression and redraw her on her mark
    # --------------------------------------------------
        setattr(store, char_id + "_mood", mood)
        if panel and char_id in panel:
            renpy.show(char_id.upper(), at_list=[getattr(store, CHANGE_PANEL_AT[panel.index(char_id) % len(CHANGE_PANEL_AT)])])

    # --------------------------------------------------
    def Change_ForgiveChance(char_id, modifier): # Her forgive% before the die is rolled (Ideas.md §6.1)
    # --------------------------------------------------
        chance = (CHANGE_FORGIVE_BASE
                  + stat_value(char_id, "inti") * CHANGE_FORGIVE_INTI
                  + stat_value(char_id, "love") * CHANGE_FORGIVE_LOVE
                  + stat_value(char_id, "chastity") * CHANGE_FORGIVE_CHASTITY
                  + (stat_value(char_id, "purity") * stat_value(char_id, "purity") * stat_value(char_id, "purity")) * CHANGE_FORGIVE_PURITY
                  + modifier)
        return max(0, min(100, chance))

    # --------------------------------------------------
    def Change_Forgives(char_id, modifier): # One girl's verdict — True forgives
    # --------------------------------------------------
        return renpy.random.randint(1, 100) <= Change_ForgiveChance(char_id, modifier)

    # --------------------------------------------------
    def Change_Lenient(char_id): # Which way she LEANS before HERO has said anything (drives her opening mood)
    # --------------------------------------------------
        return Change_ForgiveChance(char_id, 0) >= 50

    # --------------------------------------------------
    def Change_Verdict(votes): # Majority of the panel; a tie goes the way the closest girl voted
    # --------------------------------------------------
        # `votes` is [(char_id, forgives)] in speaking order.
        yes = [c for c, v in votes if v]
        no = [c for c, v in votes if not v]
        if len(yes) != len(no):
            return len(yes) > len(no)
        closest = max(votes, key=lambda v: stat_value(v[0], "inti"))
        return closest[1]

# ----------------------------------------------------------------------------------------------------
label action_change_oops: # Walking in on the changing crowd — called from goto_school_locker_f (GameCheck.rpy)
# ----------------------------------------------------------------------------------------------------
# Phase 1 room view (the changing art) -> phase 2 free-look close-ups -> phase 3 the panel steps up on base sprites -> phase 4 the judgement rounds. Ideas.md § Changing Room Scene §5-6.
#
# LOW-SCOPE NOTE: the changing art has no face/mouth layers, so every SPOKEN round runs on the base standing sprites (which do animate `MOUTH` and carry `_mood`/`_fx`). The changing art carries the two silent views.
# ----------------------------------------------------------------------------------------------------
    python:
        _oops_cast = Change_OopsCast()

    if not _oops_cast:
        return

    call hide_ui from _call_hide_ui_137

    python:

        # One group scene per visit — cleared only when HERO walks back in from another room.
        store.hero_locker_oops_visit = True

        # Replay guard FIRST (same key as room_entry_exposure) so re-entering the room mid-change won't refire. It stamps EVERY girl changing in the room, not just the ones who made it on stage: `Change_OopsCast` caps at the slot count, so with more girls than slots the overflow stayed unstamped and immediately re-triggered the whole scene with the leftovers. Walking in once burns the whole change window.
        for _c in Change_Cast(art=False):
            setattr(store, _c + "_exposure_seen", getattr(store, _c + "_activity_time_start", 0))

        # wears=False -> ask the schedule, so each girl wears the outfit she is changing INTO. Change_WearImage still falls back to her "under" art when that outfit has no changing sprite, so the whole room is never one flat state.
        _oops_cast = Change_ShowRoom(_oops_cast, wears=False)
        _oops_girl = Change_Speaker(_oops_cast)

    stop BGM fadeout 3

    with Dissolve(1)

    play SE1 "Wow1.mp3"

    $ hero_lust = min(100, hero_lust + 5)

    pause

    mind "(oops...)"

    play BGM "audio/W2C - Awkward.mp3"

# ---------------------------------------- Round 1 — Reaction (§5.1): the ladder decides how many speak
    python:
        # These lines land on the changing art, which has no mouth layer — that is the caught beat, and it is why every later round waits for the base sprites. Ideas.md §8.1 upgrade path covers closing this.
        for _c in Change_Reactors(_oops_cast):
            Change_Says(_c, CHANGE_LINES_REACT)

# ---------------------------------------- View 2 — free-look close-ups, player-driven
    python:
        _zoom_i = _oops_cast.index(_oops_girl) if _oops_girl in _oops_cast else 0

        while True:
            Change_CameraTo(_zoom_i)
            _zoom_r = renpy.call_screen("change_view_ui")
            if _zoom_r == "close":
                break
            _zoom_i = (_zoom_i + (1 if _zoom_r == "right" else -1)) % len(_oops_cast)

        Change_CameraReset()                                    # the camera outlives `scene` — always reset it

# ---------------------------------------- View 3 — the panel steps up (base sprites, rolled outfits)
    python:
        _oops_panel = Change_Panel(_oops_cast)
        _oops_saved = {}

    if not _oops_panel:
        jump change_oops_leave                                  # nobody present has a base sprite

    scene bg_school locker_f

    $ _oops_saved = Change_ShowPanel(_oops_panel)

    with Fade(1, 0, 3)

# ---------------------------------------- Round 2 — Explanation (§5.2): HERO answers to their faces
    $ hero_mood = "O1"

    # One of them answers him back. Picked by weighted inti like every other speaker, so it is not always the girl on the left mark.
    $ _oops_answer = Change_Speaker(_oops_panel) or _oops_panel[0]

    python:
        for _c in _oops_cast:
            add_stat(_c, "inti", 0.5)

    menu:
        "Apologize":
            hero "S{w=[wt1]}-{w=[wt1]}sorry!{w=[wt2]} I didn't know anyone was in here{w=[wt1]}-{w=[wt1]} I'm going!"

            $ _oops_mod = CHANGE_MOD_SORRY

            python:
                for _c in _oops_cast:
                    add_stat(_c, "love", -1)

        "Say the Student Council sent you":
            hero "The [C_Dat]Student Council[C_Off] sent me!{w=[wt2]} I{w=[wt1]}-{w=[wt1]}I have a job to do in here!"

            # The lie is allowed on purpose — claiming an errand nobody granted is the -15 branch. Reads `hero_locker_f_excuse`, stamped when he walked in: `hero_locker_f_access` is already spent by then, so testing it here called an honest answer a lie.
            $ _oops_mod = CHANGE_MOD_MISSION if hero_locker_f_excuse else CHANGE_MOD_LIE

            if _oops_mod == CHANGE_MOD_LIE:

                python:
                    for _c in _oops_cast:
                        add_stat(_c, "love", -3)
                $ add_stat("hero", "club_stco", CHANGE_REP_LIE)
                $ Change_Says(_oops_answer, CHANGE_LINES_ANSWER_LIE)

            else:
                $ Change_Says(_oops_answer, CHANGE_LINES_ANSWER_MISSION)

# ---------------------------------------- The room makes up its mind — every face turns before anyone speaks
    python:
        # Verdicts are rolled HERE rather than one at a time in Round 3, so the whole panel can react to HERO's answer at once: won over girls warm up, the rest harden. Round 3 then only voices a decision that is already on their faces.
        _oops_votes = [(_c, Change_Forgives(_c, _oops_mod)) for _c in _oops_panel]

        for _c, _v in _oops_votes:
            Change_Mood(_c, CHANGE_MOOD_WARM if _v else CHANGE_MOOD_ANGRY, _oops_panel)

        _oops_forgiven = Change_Verdict(_oops_votes)

# ---------------------------------------- Round 3 — Judgement (§5.3): every panel girl casts her verdict
    python:
        for _i, (_c, _v) in enumerate(_oops_votes):

            # She answers the girl before her when their verdicts differ — or backs her when they match. The disagreement table is picked by HER OWN stance, never by the disagreement alone: using one harsh table for both directions made a girl scold the room for being soft and then defend HERO.
            if _i and renpy.random.randint(1, 100) <= CHANGE_CROSS_CHANCE:
                if _v == _oops_votes[_i - 1][1]:
                    Change_Mood(_c, CHANGE_MOOD_WARM, _oops_panel)
                    Change_Says(_c, CHANGE_LINES_AGREE)

                else:
                    Change_Mood(_c, CHANGE_MOOD_SOFT, _oops_panel)
                    Change_Says(_c, CHANGE_LINES_DISAGREE_SOFT if _v else CHANGE_LINES_DISAGREE_HARD)

                # Back to the face her own verdict deserves before she states it.
                Change_Mood(_c, CHANGE_MOOD_WARM if _v else CHANGE_MOOD_ANGRY, _oops_panel)

            Change_Says(_c, CHANGE_LINES_FORGIVE if _v else CHANGE_LINES_PUNISH)

# ---------------------------------------- Round 4 — Conclusion (§5.4): a girl who already spoke closes it
    python:
        # §5.4 — never a silent bystander. Every panel girl voted aloud in Round 3, so the panel IS the "already spoke" pool; the Round 1 reactors who are not on a mark cannot close the scene.
        _oops_last = Change_Speaker([v[0] for v in _oops_votes]) or _oops_panel[0]
        _oops_last_vote = dict(_oops_votes).get(_oops_last, _oops_forgiven)

        # Her closing line is chosen by the verdict AND by how SHE voted, so the girl who argued to report him never reads out "I tried to talk them down" — that was the other half of the contradiction. Her face follows the same pair: happy only when the outcome is the one she wanted, sad when she lost the argument on his behalf.
        if _oops_forgiven:
            _oops_end = CHANGE_LINES_END_FORGIVE if _oops_last_vote else CHANGE_LINES_END_FORGIVE_GRUDGE
            _oops_face = CHANGE_MOOD_HAPPY if _oops_last_vote else CHANGE_MOOD_ANGRY

        else:
            _oops_end = CHANGE_LINES_END_PUNISH_SORRY if _oops_last_vote else CHANGE_LINES_END_PUNISH_HARD
            _oops_face = CHANGE_MOOD_SOFT if _oops_last_vote else CHANGE_MOOD_ANGRY

        Change_Mood(_oops_last, _oops_face, _oops_panel)
        Change_Says(_oops_last, _oops_end)

# ---------------------------------------- Settle
    python:
        for _c in _oops_panel:
            add_stat(_c, "inti", 1)
            add_stat(_c, "love", 0 if _oops_forgiven else -1)

        if not _oops_forgiven:
            # Seed for the punishment system (Ideas.md §6.6) — nothing reads this yet, by design.
            store.hero_locker_punish = hero_locker_punish + 1
            add_stat("hero", "club_stco", CHANGE_REP_CAUGHT)

            # Barred for the rest of the day: the nav button disappears until `passday` clears it.
            store.hero_locker_f_ban = True
            msg.msg(renpy.translate_string("You are not welcome in the female locker room for the rest of the day."))

        else:
            msg.msg(renpy.translate_string("They agreed to let it go."))

        Change_RestorePanel(_oops_saved)

label change_oops_leave:

    play SE1 "DoorBam.ogg"

    # Thrown out on a bad verdict. This is not just flavour: `check_playermap` re-calls `goto_school_locker_f` on EVERY gamecheck while HERO stands in the room, so staying put keeps re-arming the scene for any girl who starts changing next. Moving him out is what actually stops it — `show_ui` -> `gamecheck` -> `check_playermap` then scenes whatever room `hero_map` now points at.
    if hero_locker_f_ban:
        $ hero_map = hero_map_prev or (MAP_DATA["school"]["name"] + " - " + MAP_DATA["school"]["map"]["courtyard"]["name"])
        $ msg.msg(renpy.translate_string("You were shoved out of the female locker room."))

        scene bg_0

    else:
        scene bg_school locker_f

    with Dissolve(1)

    jump show_ui

# ----------------------------------------------------------------------------------------------------
screen change_view_ui(): # Check girls in zoom
# ----------------------------------------------------------------------------------------------------
    hbox:
        spacing 25
        xalign 1.0
        yalign 1.0
        xoffset -110
        yoffset -25
        imagebutton:
            idle At("images/UI/QUICK_Arrow_4.webp", ButtonIdle)
            hover At("images/UI/QUICK_Arrow_4.webp", ButtonHover)
            action Return("left") # Move to left
        imagebutton:
            idle At("images/UI/QUICK_Arrow_6.webp", ButtonIdle)
            hover At("images/UI/QUICK_Arrow_6.webp", ButtonHover)
            action Return("right") # Move to right
        imagebutton:
            idle At("images/UI/QUICK_Hide.webp", ButtonIdle)
            hover At("images/UI/QUICK_Hide.webp", ButtonHover)
            action Return("close") # Jump to next phase
