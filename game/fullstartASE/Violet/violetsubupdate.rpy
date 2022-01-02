label violetsub_orgasmcontrol:
    scene bg ClassroomD

    $ clothes = "school"
    show chelsea shocked with dissolve
    play sound PhoneVibration
    "As your second class is ending, you feel your phone vibrate."

    call screen TextingScene("Violet",
    [
        TextMessage("[pcname] I was thinking"),
        TextMessage("About what?", sender = False),
        TextMessage("The other night by my car"),
        TextMessage("Your fingers against me..."),
        TextMessage("And before that. At the party"),
        TextMessage("I was so horny... I'm still so horny..."),
        TextMessage("I went home and touched myself but..."),
        TextMessage("I haven't cum yet. I wanted to... but I wanted it to be with you")
    ])

    show chelsea happy
    "You smile, an idea forming."

    call screen TextingScene("Violet",
    [
        TextMessage("Meet me in the 2nd floor bathroom between classes", sender = False),
    ])

    show chelsea laugh
    "The bell rings as you tuck your phone away."
    show chelsea embarrassed at exitScene(0.5, 0.0, 0.4, 0.4)
    "Smiling, you pack your bag and walk to the bathroom."
    scene bg SchoolRestroom with dissolve
    if club == "track":
        "Two girls walk in, so you step into a stall and wait for them to leave."
    elif club == "cheer":
        "Two girls walk in, so you lean over the sink and check your makeup until they leave."
    elif club == "yearbook":
        "Two girls walk in, chatting loudly; you hide in a stall and hope they leave quickly."
    "As they step out into the hallway, Violet steps into the bathroom."
    show V School Annoyed at right with dissolve
    V "Are we seriously meeting in a {i}bathroom{/i}?"
    show chelsea at midright with dissolve
    if club == "track":
        "Putting on a cocky grin, you cross your arms over your chest."
        show chelsea happy
        show V School Suprised
        pcname "We meet wherever I tell you."
    elif club == "cheer":
        "Smiling, you wave a finger at her."
        show chelsea happy
        show V School Suprised
        pcname "Is that a problem?"
    elif club == "yearbook":
        "You know she likes when you're in control, so you try to look confident."
        show chelsea confused
        show V School Suprised
        pcname "Yeah... So?"
    show chelsea blank
    show V School Pout
    "Taken aback, she looks you up and down and shrugs."
    show chelsea embarrassed
    hide V School
    show V SubSchool Blank at right
    V "Well, I'm here now. What did you want?"
    hide chelsea with dissolve
    hide V SubSchool with dissolve
    "Grabbing her hand, you pull her into the biggest stall and press her up against the wall, kissing her hard."
    scene bg VSSB1 with dissolve
    "She moans against your lips, melting against you."
    "Your hands roam over her curves, fumbling with the buttons of her jacket."
    "Pulling it open, you grab her breast, squeezing gently."
    "She moans again, arching her back and pressing her breasts forward, eager for more."
    "You break the kiss, gasping for breath and press your lips to her neck."
    "Trailing kisses down her neck, you draw your other hand up her skirt, pressing your fingers to her panties."
    show bg VSSB2 with dissolve
    V "[pcname]!"
    "Her voice is an urgent whisper. She spreads her legs, letting your press your fingers closer to her hot pussy."
    V "I want you so much..."
    "Loosening her tie, you quickly unbutton her shirt, trailing kisses over the mounds of her breasts."
    "She reaches back, unhooking her bra and freeing her breasts."
    "Lifting one perfect globe, you take her nipple between your lips and suck hard."
    show bg VSSB3 with dissolve
    V "Ahh~"
    "You're rewarded with a rush of wetness against your fingers, her panties quickly growing slick and wet with arousal."
    "Her fingers curl into your hair, pulling you closer."
    "Satisfied, you release her breast, standing back up and smiling."
    scene bg SchoolRestroom with dissolve
    show chelsea embarrassed with dissolve
    show V SubSchool Sad at midright with dissolve
    V "What...?"
    show V SubSchool Worried
    "Both panting, you watch each other a moment. She shakes her head in confusion."
    hide V SubSchool
    show V School Suprised at midright
    pcname "We should get back to class."
    show chelsea laugh
    hide V School
    show V SubSchool Sad at midright
    V "But I thought..."
    show chelsea happy
    hide V SubSchool
    show V School Suprised at midright
    pcname "I know. We're at school and you were teasing me with all that dirty talk, weren't you?"
    show chelsea laugh
    hide V School
    show V SubSchool Sad at midright
    "She looks down, flushing."
    show chelsea embarrassed
    show V SubSchool Worried
    V "Maybe I wanted you to do {i}this{/i}..."
    "With one finger, you tilt her face up to meet your gaze."
    show chelsea happy
    show V SubSchool Sad
    pcname "But you don't get to decide that, do you?"
    show chelsea embarrassed
    hide V SubSchool
    show V School Pout at midright
    "She bites her lip - still puffy and red from your kiss - and shakes her head."
    show chelsea happy
    pcname "So now you're going back to class like this..."
    show chelsea embarrassed
    show V School Suprised
    "You run your hand up her skirt, drawing your fingers over her damp panties."
    hide V School
    show V SubSchool Blank at midright
    "She gasps, shuddering with pleasure."
    show chelsea blank
    show V SubSchool Sad
    pcname "And when you get home, you are not allowed to touch yourself. Do you understand?"
    show chelsea embarrassed
    hide V SubSchool
    show V School Suprised at midright
    "Her mouth falls open; clearly that was her plan."
    V "But--"
    show chelsea blank
    pcname "Until I say otherwise, you do not cum. Your orgasms belong to me."
    "She stares at you in disbelief."
    V "I--"
    show chelsea confused
    "Raising your brows, you challenge her to argue."
    hide V School
    show V SubSchool Sad at midright
    V "If... If that's what you want, [pcname]. I..."
    V "My orgasms belong to you..."
    show chelsea embarrassed
    "Withdrawing your hand again, you smile."
    pcname "Good. Get back to class then."
    jump events_end_period

label violetsub4_branch1:
    scene bg Cafeteria
    $ clothes = "school"
    show V SubSchool Happy with dissolve
    show chelsea at left with dissolve
    "At lunch, Violet places your tray in front of you, bowing her head slightly."
    hide V SubSchool
    show V School Pout
    "Taking her seat, she waits for you to begin eating."
    "You watch her a moment, thinking."
    show chelsea confused
    "The service is nice, but you want something more than just a servant at lunchtime."
    "Pondering a moment, you make a decision."
    menu violetsub4_branch1_choice:
        "Let's go shopping tonight." if True:
            $ violetsub4choice = "shop"
            $ violetsub4_options.remove("shop")
        "Take me to dinner tonight." if True:
            $ violetsub4choice = "dinner"
            $ violetsub4_options.remove("dinner")
    show chelsea happy
    show V School Suprised
    "Violet looks up, meeting your eyes with a smile."
    show V SubSchool Happy
    V "Really?"
    show chelsea embarrassed
    show V SubSchool Blank
    pcname "Yeah. Pick me up after work."
    show chelsea blank
    "Lifting your sandwich, you take a bite."
    "Violet nods, picking up her own sandwich."
    show V SubSchool Happy
    V "Of course."
    show chelsea embarrassed
    "You smile at her response, still impressed by her change in demeanor."
    "It's still a little strange, but you could definitely get used to this."
    jump events_end_period

label violetsub4_branch2:
    scene bg Cafeteria
    $ clothes = "school"
    show V SubSchool Happy with dissolve
    show chelsea at left with dissolve
    "At lunch, Violet places your tray in front of you, bowing her head."
    show V SubSchool Sad
    "Taking her seat, she fixes her eyes on the table and waits for you to begin eating."
    "You watch her a moment, thinking."
    show chelsea confused
    "You've never actually been to Violet's house. You can't help but wonder if she'll be this submissive there."
    menu violetsub4_branch2_choice:
        "Let's go shopping tonight." if 'shop' in violetsub4_options:
            $ violetsub4choice = "shop"
            $ violetsub4_options.remove("shop")
        "Take me to dinner tonight." if 'dinner' in violetsub4_options:
            $ violetsub4choice = "dinner"
            $ violetsub4_options.remove("dinner")
        "I want to see your house." if True:
            $ violetsub4choice = "violethouse"
            $ violetsub4_options.remove("violethouse")
    show chelsea happy
    show V SubSchool Happy
    "Violet smiles, keeping her eyes downcast."
    V "If that's what you'd like."
    show chelsea happy
    show V SubSchool Blank
    pcname "It is. Pick me up after work."
    "She nods, still waiting."
    show chelsea embarrassed
    "You smile, picking up your fork and pause."
    show chelsea blank
    hide V SubSchool
    show V School Pout
    "For the better part of a minute you feel her attention on you, though her gaze never leaves the table."
    "Spearing a bite of food with your fork, you slowly raise it to your lips."
    "As you chew, Violet waits. Patient. Still."
    show chelsea embarrassed
    hide V School
    show V SubSchool Happy
    "The moment you swallow, Violet lifts her own fork and begins eating."
    "It's a subtle submission, but it brings a smile to your lips anyway."
    jump events_end_period

label violetsub4_branch3:
    scene bg Cafeteria
    $ clothes = "school"
    show V SubSchool Happy with dissolve
    show chelsea at left with dissolve
    "At lunch, Violet places your tray in front of you, bowing her head and fixing her eyes on the table."
    show V SubSchool Sad
    "Taking her seat, she waits for you to begin eating."
    "You watch her a moment, thinking."
    show chelsea sad
    "You'd like to do something fun, but your apartment was really messy when you left this morning."
    show chelsea happy
    "You should probably clean it after work. Unless..."
    menu violetsub4_branch3_choice:
        "Let's go shopping tonight." if 'shop' in violetsub4_options:
            $ violetsub4choice = "shop"
            $ violetsub4_options.remove("shop")
        "Take me to dinner tonight." if 'dinner' in violetsub4_options:
            $ violetsub4choice = "dinner"
            $ violetsub4_options.remove("dinner")
        "I want to see your house." if 'violethouse' in violetsub4_options:
            $ violetsub4choice = "violethouse"
            $ violetsub4_options.remove("violethouse")
        "I want you to clean my apartment." if True:
            $ violetsub4choice = "clean"
            $ violetsub4_options.remove("clean")
    if violetsub4choice == "clean":
        show chelsea laugh
        hide V SubSchool
        show V School Suprised
        "Violet's mouth falls open."
        V "What?"
        show chelsea embarrassed
        "You smile, enjoying her shock."
        hide V School
        show V SubSchool Sad
        pcname "My apartment needs to be cleaned. You can do it while I'm at work."
        show chelsea blank
        V "I..."
        show V SubSchool Worried
        "She wants to refuse - you can see it in her face."
        "But, instead, she lowers her eyes and nods."
        show chelsea embarrassed
        show V SubSchool Happy
        V "If that's what you like."
        show chelsea laugh
        show V SubSchool Sad
        pcname "It is. I'll check it after work, so do a good job."
    elif True:
        show chelsea embarrassed
        show V SubSchool Happy
        "Violet smiles, keeping her eyes downcast."
        show chelsea happy
        V "If that's what you'd like."
        pcname "It is. Pick me up after work."
        show V SubSchool Blank
    "She nods, still waiting."
    show chelsea embarrassed
    "You smile, picking up your fork and taking a bite of food."
    show chelsea happy
    "This should be fun."
    jump events_end_period

label violetsub4_shop:
    scene bg CityE
    $ clothes, hair = casualwear
    show chelsea at right, enterScene(1.2, 1.0, 0.3, 0.3)
    "Stepping out of the building, you look at the nearby cars, searching for Violet."
    show chelsea embarrassed
    show V SubCasual Blank at midright with dissolve
    "As soon as she sees you, she steps out of the car and opens the door for you."
    show V SubCasual Happy
    hide chelsea with dissolve
    "Smiling, you take your seat."
    hide V SubCasual with dissolve
    "It's probably what she's used to, but you still feel like a celebrity every time she opens the door for you."
    scene black with dissolve
    show V SubCasual Happy at right with dissolve
    V "Did you have a good day at work?"
    hide V SubCasual with dissolve
    show chelsea with dissolve
    "For a moment, you're not sure what to say. Violet almost never shows an interest in your job."
    menu violetsub4_shop_day:
        "It was great." if True:
            show chelsea laugh
            pause 0.5
            hide chelsea with dissolve
            show V SubCasual Happy at right with dissolve
            V "Good! I'm glad you had a good day."
            hide V SubCasual with dissolve
            show chelsea happy with dissolve
            "Her eyes meet yours in the mirror and you smile back."
        "It could have been better." if True:
            show chelsea sad
            pause 0.5
            hide chelsea with dissolve
            show V SubCasual Sad at right with dissolve
            V "Oh. Um. I'm sorry to hear that...?"
            hide V SubCasual with dissolve
            show chelsea with dissolve
            "Her eyes meet yours in the mirror; she looks uncomfortable."
        "It's just work." if True:
            show chelsea confused
            pause 0.5
            hide chelsea with dissolve
            show V Casual Blank at right with dissolve
            V "Right. Sorry."
            hide V Casual with dissolve
            show chelsea with dissolve
            "Her eyes meet yours in the mirror. You shrug."
    hide chelsea with dissolve
    show V SubCasual Happy at right with dissolve
    V "Oh, here."
    hide V SubCasual with dissolve
    show chelsea shocked with dissolve
    "To your surprise, she passes the aux cord back to you."
    show chelsea blank
    "Plugging it into your phone, you pick a few songs and sit back in your seat."
    "It's strange to be so in control of things."
    show chelsea sad
    "There's an unexpected pressure: to make decisions, to know what to do."
    if club == "track":
        show chelsea embarrassed
        "It's exciting."
    elif club == "cheer":
        "It's exhausting sometimes."
    elif club == "yearbook":
        "It's a little scary sometimes."
    hide chelsea with dissolve
    "Violet pulls into the parking lot and finds a space."
    scene bg CityE with dissolve
    show V SubCasual Happy with dissolve
    "Circling the car, she holds your door open and bows her head."
    show chelsea embarrassed at left with dissolve
    "You can tell she's trying really hard to please you today."
    show chelsea blank at exitScene(0.0, 0.5, 0.3, 0.3)
    hide V SubCasual
    show V Casual Pout
    "Violet follows you into the store, doing her best to stay quiet and let you decide where to go."
    show V Casual Pout at exitScene(0.5, 1.0, 0.3, 0.3)
    scene bg Shop with fade
    if club == "track":
        show chelsea happy with dissolve
        "The first store that catches your eye is a shoe store."
        show chelsea laugh
        "There are tons of athletic shoes, including a really nice set of running shoes."
        show chelsea happy
        "You've heard August talk about the brand before, so you know they're top of the line."
        show chelsea sad
        "One look at the price tag, though, and you change your mind."
        show V SubCasual Sad at midright with dissolve
        V "You don't like those?"
        "You shake your head, frowning."
        show chelsea blank
        pcname "I can find a nice pair for less at Hizormart."
        hide V SubCasual
        show V Casual Pout at midright
        "For a moment, Violet looks confused - and then conflicted."
        "Reaching out, she picks up the box."
        show chelsea shocked
        show V Casual Blank
        V "Are these your size?"
        show chelsea sad
        show V Casual Pout
        pcname "Yeah, but--"
        "She shakes her head, looking determined."
        hide V Casual
        show V SubCasual Happy at midright
        V "I'm getting them. My master should have the best."
        show V SubCasual Worried
        "Still holding the box, she looks down, waiting for you to react."
        show chelsea blank at exitScene(0.5, 1.0, 0.3, 0.3)
        pause 0.5
        show V SubCasual Happy at exitScene(0.75, 1.25, 0.3, 0.3)
        "Shrugging, you walk her up to the register and let her buy them."
    elif club == "cheer":
        show chelsea happy with dissolve
        "The first store that catches your eye is a makeup store."
        show chelsea laugh
        "You've heard some of the other cheerleaders talking about the place, but you'd never actually seen one."
        show GFDoctor at right with dissolve
        "As soon as you step inside, an employee approaches."
        show chelsea blank
        show V SubCasual Worried at left with dissolve
        "Consultant" "Hello again, Miss Violet. Please let me know if there's anything we can assist you with."
        show chelsea confused
        show V SubCasual Happy
        "For a moment, Violet looks uncomfortable - and then she smiles."
        show chelsea blank
        V "I'm here with an important friend today. Please charge everything she wants to my account."
        hide V SubCasual
        show V Casual Pout at left
        "The employee turns to you. She smiles pleasantly, but her eyes quickly assess you."
        "Consultant" "Very good. Right this way, Miss...?"
        show chelsea happy
        pcname "[pcname]."
        "Consultant" "Did you have something specific you were looking for, Miss [pcname]?"
        "Consultant" "Or would you like me to help you?"
        show chelsea blank
        pcname "I could use some new eyeshadow, actually."
        scene black with dissolve
        "She leads you around the store, showing you several eyeshadow palettes that compliment your hair and skin tone."
        "In the end, you pick one out and she takes it up to the counter."
        scene bg Shop with fade
        show GFDoctor at right with dissolve
        show chelsea at midright with dissolve
        show V Casual Pout with dissolve
        "A short time later, she returns with your bag."
        "Consultant" "We've included a few samples in there as well. Please stop by anytime and we would be happy to assist you."
    elif club == "yearbook":
        show chelsea happy with dissolve
        "The first store that catches your eye is a photography store."
        show chelsea laugh
        "The shelves are filled with camera lenses, bags, and accessories."
        show chelsea sad
        "You'd been considering a camera bag, but..."
        show chelsea happy
        "A set of lenses catches your attention."
        "Fast prime lenses. A set of three with different focal lengths: 24mm, 50mm, and 80mm."
        show chelsea sad
        "As you reach out to look at it, your eyes catch the price tag and your fingers fall."
        show chelsea shocked
        show V SubCasual Sad at midright with dissolve
        V "Do you need some... of those?"
        show chelsea sad
        pcname "Oh. No... No, I don't need them."
        hide V SubCasual
        show V Casual Pout at midright
        "She frowns, looking a little conflicted."
        hide V Casual
        show V SubCasual Happy at midright
        "Then, smiling, she grabs the set of lenses."
        show chelsea shocked
        pcname "W-what are you doing...?"
        show V SubCasual Sad
        V "My master deserves nice things, so I'm going to buy them for her."
        "Her head tilts to the side, as if asking permission."
        show chelsea embarrassed
        show V SubCasual Happy
        "You nod, feeling grateful and... Empowered."
        show V SubCasual at exitScene(0.75, 1.0, 0.3, 0.3)
        "Violet takes the lenses to the register and pays for them."
    scene bg Shop with fade
    show V SubCasual Happy at right with dissolve
    show chelsea embarrassed at midright with dissolve
    V "What else do you need?"
    scene black with fade
    "You lead Violet into several more stores."
    "They aren't all as pricey as the first, but each time Violet steps forward to pay for anything you pick out."
    "It's exhilarating, not to worry about prices or sales, but you start to feel a little guilty too."
    scene bg Shop with dissolve
    show chelsea confused with dissolve
    "Near the end of the mall, you notice a lingerie store, and an idea begins to form."
    show chelsea embarrassed
    pcname "You've been very good today, Violet."
    show V SubCasual Worried at right with dissolve
    "Violet blushes a little, looking down."
    show chelsea happy
    pcname "I've picked out so many things. I think it's time we get you something too."
    show chelsea blank at left
    show V SubCasual Blank at center
    with fade
    "Inside, you find lots of different colors and styles of lingerie."
    show chelsea embarrassed
    "Some are cute and modest, while others barely cover the essentials - and some definitely {i}don't{/i} cover the essentials."
    show V SubCasual Worried
    "You've never picked lingerie for someone else before, and the selection is enormous."
    show chelsea blank
    pcname "Pick something you think I'll like and meet me outside. I want it to be a surprise."
    hide V SubCasual
    show V Casual Pout
    "Violet meets your smile with a serious nod."
    show chelsea embarrassed
    hide V Casual
    show V SubCasual Happy
    V "Thank you, [pcname]. I'll find something you'll really like!"
    scene black with fade
    "Stepping out of the store, you find a bench to sit on while you wait."
    "As much as you'd like to pick something yourself, you enjoyed how seriously Violet is taking the task."
    "And the surprise will be nice too."
    scene bg Shop with fade
    show chelsea with dissolve
    "After a few minutes, Violet steps out of the store with a new bag hanging from her arms."
    show chelsea happy
    show V Casual Pout at right with dissolve
    pcname "Did you find one?"
    "She nods."
    hide V Casual
    show V SubCasual Happy at right
    V "I think you'll really like it."
    show chelsea embarrassed
    pcname "Good. I think we're all set then. Let's go."
    scene bg HomeD with fade
    show chelsea sad with dissolve
    "Back at your apartment, Violet carries your bags in for you."
    show chelsea blank
    "You feel like you should thank her, but quickly remind yourself of your new role."
    hide chelsea with dissolve
    "Instead, you take a seat on the couch and toss the lingerie bag on the table."
    show V SubCasual Sad at left with dissolve
    pcname "Well? Let's see how you did."
    "Violet takes the bag, swallowing hard."
    show V SubCasual Worried
    V "Right."
    hide V SubCasual with dissolve
    "As Violet walks into the bathroom to change, it occurs to you that she's not used to being judged."
    "At least, not to her face. And from what you saw at the party, her last name protects her from most criticism."
    "You can't help but wonder what she'll do if you criticize her choice."
    "As you ponder this, you hear the click of the bathroom door unlatching."
    scene black with dissolve




    "Violet steps out in a blue teddy that looks like it's made of ribbon with patches of floral lace."
    "The top ties around her neck, while a thin strap holds the bust in place."
    "A bust covered in thick, curved bands, which cover very little."
    "The pinkness of her nipples peeks out from behind the strips of blue lace, drawing the eye."
    "Ribbon wraps the bottom of the bust, crossing over her stomach and dipping lower."
    "There, another bit of bold lace barely obscures her pussy."

    "She turns, and you see her bare cheeks framed by a band of ribbon that ends in a bow at the top of her ass."

    V "Do you... like it?"
    menu violetsub4_shop_react:
        "It's perfect!" if True:
            "Violet smiles, turning once more so you can see the whole thing."
            V "I'm glad. I was afraid it wasn't sexy enough."
            "Shaking your head, you smile."
            pcname "I love it. Actually..."
        "You thought I'd like this?" if True:
            "Violet's mouth falls open."
            V "You don't like it?"
            "She looks angry, and a little hurt."
            "You were right; she isn't used to being criticized."
            "A small smile plays over your lips."
            if club == "track":
                pcname "It's boring. What do you want me to say?"
            elif club == "cheer":
                pcname "I mean, it's not exactly {i}sexy{/i}."
            elif club == "yearbook":
                pcname "I was... expecting something different, I guess."
            "There's something about throwing her off that makes you feel powerful - in a way simple servitude doesn't."
            pcname "Still..."
    pcname "I'd hate for you to put it on for no reason."
    "Sensing where this is going, Violet bites her lip."
    V "Yeah...?"
    pcname "Get on your knees."
    "As Violet sinks to her knees, you debate what you want her to do next."
    menu violetsub4_shop_sex:
        "Oral." if True:
            "Standing, you pull off your top."
            "Dropping your panties and shorts, you kick them aside and take a seat."
            if club == "track":
                "Spreading your legs wide, you wave your hand towards your pussy."
                pcname "Well?"
            elif club == "cheer":
                "Sliding your knees apart, you smile down at her."
                pcname "Well?"
            elif club == "yearbook":
                "You smile down at her, in a way you hope looks confident, and slowly spread your legs."
                pcname "Well...?"
            "Violet crawls forward, a slow smile spreading over her lips."

            V "Yes, [pcname]..."
            "Dipping her head, she runs her tongue up your thighs and presses her lips to your cunt."

            "Staring up at you through long lashes, she dances her tongue over your sensitive skin."
            "Shivering with pleasure, you tilt your head back and close your eyes."
            "Her tongue runs up and down the outer lips of your cunt, before delving between them."
            pcname "Mmmm..."

            "Hot and wet, it gently explores the folds of your pussy, darting back and forth across your clit before sinking inside of you."
            "Lifting your legs, you angle your hips so she can sink her tongue deeper into you."

            "She wriggles her tongue. It squirms within you, teasing, until you moan with pleasure."
            pcname "Violet..."
            "Her tongue slips out of you, quickly replaced with two fingers."
            "Pressing them deep inside of you, she hooks them upward, rubbing them across your gspot."
            "Her tongue darts across your clit, flicking back and forth."

            "You moan as your fingers dig into your thighs, pulling your legs higher."
            "Her fingers massage your gspot, sending wave after wave of pleasure through your abdomen."
            "Jolts shoot out from your clit with every flick of her tongue."
            pcname "Ha~ Ha~"
            "Her fingers and tongue move together, pushing you closer and closer to your climax."
            "Your pussy tightens around her fingers and she presses her lips around your clit, sucking gently."
            pcname "Ohhh~"
            "Your muscles tense, your knees shake, and your hips buck as your orgasm floods over you."

            "Violet's mouth fastens around your clit, sucking harder as you cry out."
            pcname "V-Vio~let!"
            "For a moment, your eyes squeezed tightly shut, you lose track of everything."
            "Then, blinking, you look down at Violet's smiling face, hovering above your wet cunt."

            V "Did I do a good job?"
            "Nodding, you let your legs fall to the floor."
            pcname "That was... really good..."
            "Warm and heavy in the aftermath of your orgasm, you wave her off."
            "She stands, waiting for further instructions."
            "Pushing yourself upright, you smile."
            pcname "You can go now."
            V "But... I didn't..."
            pcname "Didn't what?"
            V "I'm still... horny."
            "You nod."
            pcname "But I'm not. So get dressed and let yourself out."
            "Her face falls, but she nods and walks to the bathroom."
            "As she steps out again, fully dressed, she looks as if she's going to argue - but then she thinks better of it."
            V "Is that all you want from me?"
            pcname "For tonight. Maybe next time I'll let you cum."
            "Releasing a long, shaky breath, she lets herself out of your apartment."
            $ violetcum += 1
        "Masturbate." if True:
            if club == "track":
                pcname "I think I'd like a little show. Touch yourself."
            elif club == "cheer":
                pcname "You must be really horny, right? Enough to touch yourself right now...?"
            elif club == "yearbook":
                pcname "What do {i}you{/i} want?"
                pcname "S-show me how you want to be touched."
            "Flushing, Violet lowers her eyes and lifts her hands."
            "Her fingers run up and down her thighs, before travelling up her belly to cup her breasts."

            "She gasps as her fingers find her nipples, rolling them gently."
            V "Ohh~"
            "She spreads her knees and you can see that the panties are crotchless."

            "Rolling her nipples between her fingers and thumbs, she gently tugs them."
            "She moans, her eyes fluttering as she pleasures herself."
            pcname "Mmmm, that's good..."
            "Releasing one breast, her hand drops to her pussy."
            "Sinking two fingers into her cunt, she slowly fingers herself."

            V "Ohh~"
            "Her eyes flutter again as she plunges her fingers in and out of her pussy."
            "A rush of heat fills your own cunt as you watch, sighing with pleasure."
            V "[domtitle]..."
            "Her hand moves faster and faster, her body trembling as she moans your name."
            V "[domtitle]... I want..."

            "Her eyes, half shut with pleasure, find yours."
            V "Please... I want... to cum..."
            "Smiling, you lean forward."
            pcname "What was that?"

            V "{i}Please{/i} let me cum... Please... Please..."
            "As she speaks, her fingers pump in and out of her pussy, moving faster and faster."
            menu violetsub4_shop_cum:
                "Let her finish." if True:
                    $ violetcum = 0
                    pcname "Okay, you can cum."
                    "Violet moans, dropping her other hand to her pussy as well."

                    "Rubbing her clit in tiny circles, she pounds her fingers into her cunt, practically screaming with pleasure."
                    "Almost immediately, her hands go still as her body shakes, trembling with the force of her orgasm."

                    "As her orgasm subsides, her fingers fall from her cunt and she slumps back on her heels, breathing heavily."
                    V "Th-thank you, [domtitle]..."
                    "You nod."
                    pcname "You're welcome."
                    "Standing, you smile down at her."
                    pcname "Now go get dressed. It's getting late."
                    "She dresses quickly, emerging from the bathroom with a contented smile."
                    pcname "Have a good night, Violet."
                    V "Yeah..."
                    "She drifts out the door, looking quite satisfied."
                "That's enough." if True:
                    $ violetcum += 1
                    pcname "Okay, you can stop now. I've seen enough."
                    "Breathing hard, Violet suddenly goes still."

                    V "W-what...?"
                    pcname "That's enough for tonight. You can get dressed now."
                    V "But..."
                    "Raising your brows, you stare down at her."
                    V "Sorry. I didn't mean..."
                    "She pulls her fingers from her pussy with a wet sucking sound."
                    "Standing, she slinks into the bathroom."
                    "When she emerges, biting her lip, she doesn't meet your eyes."
                    pcname "I know you're frustrated, but why can't you cum?"
                    "She lets out a sigh."
                    V "Because my orgasms belong to you, [domtitle]."
                    pcname "That's right. You cum when I want you to."
                    "She nods, trembling a little."
                    "You approach her, claiming her mouth in a hard kiss."
                    "When you release her, she bites her lip again."
                    pcname "Time to go. Be a good girl."
                    "She lets out a frustrated sound - half moan, half sigh - and lets herself out."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
