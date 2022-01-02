label violetdom4_car:
    $ VCasualBlank = "Characters/Violet/Casual 2/Neutral.png"
    $ VCasualPout = "Characters/Violet/Casual 2/Pouting.png"
    $ VCasualAnnoyed = "Characters/Violet/Casual 2/Annoyed.png"
    $ VCasualSmile = "Characters/Violet/Casual 2/Smile.png"
    $ VCasualSuprised = "Characters/Violet/Casual 2/Suprised.png"
    $ clothes, hair = casualwear

    show bg CityE
    show chelsea at right with moveinright
    "As you step outside, you huddle under the building's overhang and stare into the streets; it's pouring down rain so heavily you can feel the mist hitting your face from here."
    show chelsea sad
    "Sighing, you prepare for a long, wet walk home."
    show chelsea confused
    play sound PhoneVibration
    "And then your phone vibrates."
    call screen TextingScene("Violet",
    [
        TextMessage("Finally! Hurry up"),
        TextMessage("What?", sender = False),
        TextMessage("I've been waiting forever. Get in the car!")
    ])
    show chelsea blank
    "You glance around, squinting through the heavy rain until you find her car several parking spaces away."
    show chelsea at exitScene(1.0, -0.5, 0.4, 0.25)
    "Tucking your phone into your pocket, you make a mad dash for the car."
    show black
    hide bg CityE
    hide chelsea
    with dissolve
    "Rain pelts your skin as you circle the car and pull the driver's side door wide."
    "Practically throwing yourself inside, you can hear Violet's laughter filling the back seat."
    show V Casual Smile at left with dissolve
    show chelsea shocked at right with dissolve
    V "I thought you'd like a ride home since it's raining."
    if club == "track":
        "It's odd for Violet to be so thoughtful, but you aren't about to complain."
        show chelsea happy
        pcname "Yeah, thanks. It's a mess out there."
    elif club == "cheer":
        "You're surprised she's being so considerate. It's just not like her."
        pcname "Oh, I would have been {i}drenched{/i}. Thanks!"
    elif club == "yearbook":
        show chelsea confused
        "For a moment, you don't know what to say. Is Violet saying she... thought about you?"
        show chelsea embarrassed
        pcname "Oh, I... Th-thanks!"
    show chelsea happy
    show V Casual Pout
    V "Well, go on and drive. I've wasted a lot of time waiting for you out here."
    show chelsea embarrassed
    show V Casual Smile
    pcname "Yes, Violet. Thank you."
    hide chelsea with dissolve
    hide V Casual Smile with dissolve
    "You catch her smile in the rearview mirror as you shift the car into drive."
    "The rain is still crashing down around the car, obscuring your vision. Carefully, you ease the car onto the road."
    "Driving slowly, you grip the wheel hard and try to watch for lights through your windshield wipers."
    "The car creeps forward and it seems to take forever to make it a single block."
    V "Ha~"
    "A sound catches your attention."
    scene bg VBackseat1 with dissolve
    "Your eyes dart to the rearview mirror, where you find Violet is now topless."
    "Her back is arched and her hands are each cupping one of her breasts."
    "Her fingers gently pinch and pull, teasing a soft gasp of pleasure from her lips."
    if club == "track":
        "Licking your lips, you force your eyes back to the road."
        pcname "Having fun back there?"
    elif club == "cheer":
        "Your pulse quickens as you look back and forth between the mirror and the road."
        pcname "I think you're teasing me..."
    elif club == "yearbook":
        pcname "Oh!"
        "Your surprised gasp brings a smile to her lips."
    V "Eyes on the road. It's {i}really{/i}... {i}wet{/i}... outside."
    "Your body reacts immediately; your lips grow hot and your nipples stiffen beneath your shirt."
    "Heat floods your sex, leaving you shifting uncomfortably in your seat."
    "But you fix your eyes onto the road ahead, resisting the urge to watch her touch herself."
    "For another block, you maintain your focus. But as you stop at a traffic light, another sound catches your attention."
    V "Haa~ haa~"
    show bg VBackseat2 with dissolve
    "You glance back at the mirror and away - and then immediately back to the mirror, your pulse jumping."
    "Violet has her skirt hiked up and her legs spread wide. You don't see her panties, and you're too focused on what you {i}can{/i} see to look for them."
    "The view is incredible."
    "{b}HONK{/b}"
    "Startled, you look around the car a moment before noticing the light has turned green."
    V "You'd better pay attention. The windows are tinted, so nobody can see me now."
    V "But I would be very angry if you got pulled over while I'm busy back here."
    "Swallowing hard, you nod."
    pcname "R-right, sorry."
    "Shifting again in the seat, your damp panties pull tight against your skin."
    "The rain falls as hard as ever - but you barely notice. It takes all of your concentration to resist looking at the mirror again."
    V "Ohhhh~"
    "The soft moan breaks your will and you allow yourself another fleeting glance."
    show bg VBackseat3 with dissolve
    "One hand cups her breast, her fingers leaving soft dimples in the soft flesh."
    "The other..."
    "Your breath catches in your throat."
    "Her other hand hovers over her neatly trimmed pubic hair, plunging two fingers in and out of her dripping cunt."
    "Forcing your eyes back to the road, you lick your lips."
    "{i}Squelch... squelch... squelch...{/i}"
    "You can't help it; your eyes dart back to the mirror again."
    show bg VBackseat4 with dissolve
    "Her head is tilted back, her eyes squeezed tight as her fingers work on her nipple and pussy."
    "A car throws water up on the windshield, startling your focus back to the road."
    V "Ahh~"
    V "Mmmm~"
    "Her moans of pleasure draw your attention back to the mirror again."
    "Her hand has moved to the other breast. The other moves faster and faster..."
    "Pulling your eyes from the mirror, you grip the wheel tighter."
    "Your own breathing grows labored as you listen to her pleasure herself."
    V "Ahh~ Ahhh~"
    "A rush of heat fills your pussy. Shifting again, you wonder if you've soaked through to the seat beneath you yet."
    "As you hit the last stretch of road before your apartment, you allow yourself another glance."
    show bg VBackseat5 with dissolve
    "Violet's nipples are stiff red peaks. You can imagine how sensitive they must be, and your own throb in sympathy."
    "Lower, three fingers plunge in and out of her pussy, moving faster and faster."
    "You nearly miss your turn as you watch her fingering herself. As you hit the breaks, Violet moans her disapproval."
    V "Hey! Ohh~"
    "You turn into your parking space and shift the car into park with a sigh of relief."
    "Sitting impatiently, you wait for new instructions."
    V "Mmmm~"
    "But Violet is too engrossed in what she's doing; you're not even sure she knows the car isn't moving."
    "Eyes on the mirror, you watch as her left hand drops from her breast to rub her clit."
    show bg VBackseat6 with dissolve
    V "Ahh~ Ahh~ Mmmmmm~"
    "You want to touch yourself too, but she didn't tell you to yet."
    "Still, one hand drops to your lap, pressing against the fabric of your pants."
    "You can feel the damp heat of your arousal through the thin fabric. Your fingers draw a trail of fire over the sensitive flesh."
    "You gasp at the sensation. It feels nice, but it's not enough."
    "As her climax nears, Violet's hands move faster, her moans growing louder and more urgent."
    V "Ahh~ Ahhhh~ AHHHHH~"
    "Her fingers sink deep into her pussy as her legs begin shaking."
    "Rubbing her clit in tight circles, she cries out her pleasure."
    show bg VBackseat7 with dissolve
    "Suddenly her voice cuts out. Her lips move up and down wordlessly, while her whole body stiffens and trembles."
    "Then she sinks into her seat, panting. Her fingers slip from her pussy, leaving a thin trail across the seat."
    "Slowly, she pulls her clothes back on until the only sign of her arousal is her pink, puffy lips."
    show bg black with dissolve
    show V Casual Smile at left with dissolve
    show chelsea at right with dissolve
    V "Did you enjoy the show?"
    show chelsea embarrassed
    "Her eyes meet yours in the mirror and your cheeks grow warm under her gaze."
    if club == "track":
        pcname "It wasn't very fair. I wish I could have joined..."
    elif club == "cheer":
        pcname "It was hard to keep my eyes off you."
    elif club == "yearbook":
        pcname "I... Y-yes..."
    V "Good. I wanted you to watch."
    "She smiles and you're suddenly aware once again just how wet your panties are."
    show V Casual Blank
    show chelsea shocked
    V "Anyway, you're home now, so aren't you going to open the door for me?"
    pcname "Right. Sorry!"
    scene bg CityE with fade
    show chelsea blank at midright with dissolve
    "Practically jumping out of the car, you pull her door open and close it behind her."
    show V Casual Smile at right with dissolve
    "She smiles, as if there's a secret she's about to fill you in on..."
    show chelsea confused
    "...and then she takes a seat behind the wheel."
    "You stare, not quite understanding what's happening."
    show chelsea confused
    pcname "Aren't you... coming in?"
    show chelsea embarrassed
    "She laughs and your chest tightens."
    V "Why would I?"
    if club == "track":
        pcname "I just thought... I'm really horny after that."
    elif club == "cheer":
        pcname "I thought we could continue what you were doing..."
    elif club == "yearbook":
        pcname "I just... I thought..."
    show V Casual Blank
    show chelsea sad
    V "Oh. Well, I {i}was{/i} horny. But I'm feeling pretty satisfied now..."
    show V Casual Pout
    "She motions to the door again, and you push it gently shut."
    show V Casual Smile
    "Rolling the window down, she smiles up at you sympathetically."
    V "Oh, don't look so disappointed. I'll tell you what..."
    show chelsea embarrassed
    V "You be a good girl tonight and don't touch yourself, and tomorrow we'll see what happens."
    hide V Casual Smile with dissolve
    "Nodding, you watch as she rolls the window up and backs out of the parking space."
    show chelsea blank at exitScene(0.75, 0.5, 0.2, 0.2)
    "As you walk back into the house, you feel a strange mix of emotions: frustration, arousal, disappointment, anticipation..."
    hide chelsea
    "Too many things to possibly unwind."
    show bg HomeE with dissolve
    show chelsea with dissolve
    "And beneath all of it, you're still aware of the dampness in your panties."
    "Your nipples pressing hard against the fabric of your bra."
    "And the swollen nub of your clit, lightly thrumming with your still-quickened pulse."
    $ clothes = "naked"
    "Frustration wars with anticipation as you slowly undress."
    "Your panties cling to the wetness of your cunt, like a wet t-shirt after getting caught in the rain."
    show chelsea embarrassed
    "The slight suction as they pull free reminds you of lips, and you imagine Violet's face between your legs, her lips fastened to your pussy. Her tongue..."
    pcname "Ohh~"
    "Tossing your clothes aside, you step into the shower and try to think about something else."
    "But your hands are drawn to your flesh - the roundness of your breasts, the heat of your cunt - like Violet's in the car when she..."

    $ VCasualBlank = "Characters/Violet/Casual/Casual Neutral.png"
    $ VCasualPout = "Characters/Violet/Casual/Casual Pouting.png"
    $ VCasualAnnoyed = "Characters/Violet/Casual/Casual Annoyed.png"
    $ VCasualSmile = "Characters/Violet/Casual/Casual Smile.png"
    $ VCasualSuprised = "Characters/Violet/Casual/Casual Suprised.png"

    menu violetdom4_car_masturbate:
        "Be a good girl." if True:
            show chelsea sad
            "Inhaling sharply, you turn the water as cold as you can bare."
            "Violet told you not to touch yourself, and you're going to do your best to listen."
            "You force yourself to stand under the cold water until you can't stand it anymore."
            show chelsea blank
            "It's miserable, but by the time you get out of the shower you have control of your thoughts again."
            "As much as you'd like to get off, you're sure whatever reward Violet has planned will be worth it."
            "You remind yourself of that as you lay awake in bed, trying not to think of her in the back seat."
            show chelsea embarrassed
            "It'll be worth it..."
            $ acts -= 1
            $ clothes, hair = casualwear
            jump room2
        "Touch yourself." if True:
            $ violetdom4masturbate = True
            scene bg VBackseat11 with dissolve
            "Unable to resist, you remember every moment of the car ride as you let your hands wander over your body."
            "You remember your first glimpse of Violet topless in the back seat as your fingers find your nipples."
            "Her skirt hiked up. Her knees opened wide..."
            "You mimic her movements, putting your foot on the side of the tub to spread your legs."
            "Her fingers pressing inside just like..."
            "Plunging your fingers into your pussy, you lean forward, propping yourself against the shower wall."
            "The hot water rains over your back as you finger yourself hard and fast, your mind still focused on memories of Violet."
            "The way her face looked when she..."
            "Your climax hits you hard and fast; your pussy clamps around your fingers, spasming wildly as you cry out."
            "As the pleasure fades, you lean against the wall a little longer."
            "When you catch your breath, you begin washing up."
            "Guilt wells within you; as good as that felt, you know Violet will be disappointed."
            "You finish washing up quickly, dry off, and get ready for bed."
            show bg black with dissolve
            $ acts -= 1
            $ clothes, hair = casualwear
            jump room2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
