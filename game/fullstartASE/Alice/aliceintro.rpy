label aliceintrotown:
    "You decide that it’s time to head a little farther downtown on your walk today."
    "Along the way, you see an ad for \"Toxin\" headphones."
    "The design looks quite elegant, and you begin to wonder what the price is."
    $ AliceClothes = 1
    show Alice Thinking at right with moveinright
    "???" "Looks like there's a new model out, I wonder what the specs are? Are they any good?"
    show chelsea at left with dissolve
    "Looking over towards the voice you spot a girl you do not recognize standing near you."
    show chelsea confused
    pcname "Are you talking to me?"
    show Alice Happy
    "???" "Huh? Oh no, sorry. I was just thinking out loud."
    show chelsea blank
    menu alice_introchoice1:
        "Are you a fan?" if True:
            $ alicechoice = 1
            show Alice Laughing
            "???" "Maybe a little..."
            show Alice Happy
            "???" "Toxin makes really good headphones and I love working with music. So I'm a bit of an audiophile when it comes to this stuff."
            show Alice Laughing
            "The girl gives out a small giggle as she admits this."
        "Would you recommend them?" if True:
            $ alicechoice = 2
            show Alice Laughing
            "???" "Not sure, I'd have to try them first. though Toxin does make really good headphones."
    show Alice Neutral
    "???" "Do you listen to a lot of music? Do you use any particular headphones?"
    show Alice Blank
    if club == "track":
        show chelsea happy
        pcname "I mostly use them when I'm running or exercising"
    elif club == "cheer":
        show chelsea happy
        pcname "Sometimes I'll use them with my phone when I'm taking a break from practice."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Umm... mostly just with my laptop at home when I'm browsing around."
    show Alice Happy
    "???" "So not much of an audio enthusiast huh? It could definitely improve your mood to listen to music through some good quality headphones."
    show chelsea blank
    show Alice Thinking
    "???" "There's all different types that perform better with bass if you like that or better mids or..."
    show chelsea shocked
    if alicechoice == 1:
        "This girl that you just met rambles on about the different types of headphones and what's best for each genre of music. To say she is a fan is an understatement."
    elif True:
        "This girl that you just met rambles on about the different types of headphones and what's best for each genre of music. What started as a simple recommendation has turned into a full review."
    if club == "yearbook":
        show chelsea embarrassed
    elif True:
        show chelsea happy
    "It's certainly entertaining watching someone talk so passionately about their interests."
    "Even if you don't understand any of it..."
    show Alice Blank
    "She catches herself suddenly once she's realized the tangent she's gone on."
    show Alice Laughing
    "???" "Heh, Sorry about that. I work with a lot of audio in my spare time as a hobby so I get a little carried away whenever the topic comes up."
    show Alice Blank
    if club == "track":
        pcname "That's fine! Seeing someone talk so passionately really gets me motivated!"
    elif club == "cheer":
        pcname "I totally understand. I'm the same way when it comes to hair, makeup, and shopping; or just about anything to do with looking good."
    elif club == "yearbook":
        pcname "It's okay, kinda intimidating but fun to listen to."
    show chelsea blank
    show Alice Neutral
    "???" "Oh! I'm sorry I haven't introduced myself yet have I?"
    show Alice Happy
    A "My name is Alice, I was just heading to an arcade before that new billboard caught my eye."
    show Alice Blank
    show chelsea happy
    if club == "track":
        "Nice to meet you [A], I'm [pcname]. There's an arcade near here?"
        show Alice Neutral
        A "Yeah, it's a nice little place further downtown. I don't go there too often since it's a bit further away than I'd like."
    elif club == "cheer":
        "Nice meeting you [A], I'm [pcname]; I didn't know there was an arcade around here."
        show Alice Neutral
        A "Yeah, it's a nice little place further downtown. I don't go there too often since it's a bit further away than I'd like."
    elif club == "yearbook":
        "I'm [pcname], it's nice to meet you [A]."
        show Alice Laughing
        A "You remind me so much of my sister actually."
    show Alice Neutral
    A "Well, I guess I'll see you around [pcname]. Need to head out before it gets any later or my parents will be pissed."
    pcname "See you later then."
    show chelsea blank
    show Alice Happy
    "With that she waves and continues walking to her destination."
    hide Alice with moveoutright
    show chelsea confused
    pause 1.0
    scene black with dissolve
    "What an odd encounter. Maybe you'll see her again sometime."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
