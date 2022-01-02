label bakery_conflicts2_matt:
    show chelsea at right with moveinright
    "You take your seat in homeroom, sitting your backpack under your chair."
    if defymatt:
        "Matt enters the room a few minutes later; you do your best to avoid his notice as he walks to his chair behind you."
    elif True:
        "When Matt enters the room a few minutes later, you automatically bow your head."
        "As he walks past, you keep your eyes focused on the desk, but you're aware of his every move."
    "In front of you, two boys are arm wrestling. You watch, vaguely amused by their antics, as they struggle to pin each other's hand."
    show Matt Angry at left with moveinleft
    m "What the hell is this?"
    "Matt rounds your desk and slaps a brochure down."
    "It's from Dr. White's office - he must have taken it out of your backpack."
    pcname "Did you go through my bag?"
    m "Are you getting surgery!?"
    menu bakery_conflicts2_matt_brochure:
        "Yes." if True:
            "His anger shifts to surprise."
            show Matt Question at left
            m "Wait, seriously?"
            show Matt Blank at left
            m "What are you getting done?"
        "No." if True:
            show Matt Blank at left
            "His anger fades immediately."
            m "Oh..."
            show Matt Smirk at left
            m "Honestly, I wouldn't mind if your boobs were a little bigger."
            m "Your ass could use some work too."
            if defymatt:
                if club == "track":
                    show chelsea angry
                    pcname "I don't really care {i}what{/i} you think!"
                elif club == "cheer":
                    show chelsea angry
                    pcname "Then leave me alone, if you think that!"
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "W-what?"
                show Matt Happy at left
                "He laughs."
            elif True:
                "You accept his critique, looking meekly at the desk."
                if club == "track":
                    pcname "I guess you're right..."
                elif club == "cheer":
                    pcname "You would know..."
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "Th-thank you..."
            show Matt Blank at left
            m "So why do you have the brochure then?"
    show chelsea blank
    pcname "My boss offered to pay for a boob job."
    "His mouth falls open; he's obviously shocked by this revelation."
    "Just as he collects himself, though, the bell rings."
    show Matt Angry at left
    m "We'll talk later."
    hide Matt Angry with moveoutleft
    "You collect your things and move to first period."
    "No sooner has class started when your phone vibrates."

    call screen TextingScene("Matt", 
    [
        TextMessage("Come to the cafeteria"),
        TextMessage("Now")
    ])

    "Your heart skips a beat as you think about what happened when you dyed your hair."
    if defymatt:
        "But you know what will happen if you don't go."
    menu bakery_conflicts2_matt_cafeteria:
        "Go" if True:
            pass
        "Don't go." if True:
            if defymatt:
                "With a cold feeling in the pit of your stomach, you tuck your phone away."
                "It doesn't matter if he shows everyone those pictures; you can't do this anymore!"
                $ mattblackmail = 2
                jump events_end_period
            elif True:
                $ mattblackmail = 1
                $ defymatt = True

                call screen TextingScene("Matt", [TextMessage("If you don't cum everyone is gonna see all those pics I took")])

                "You stare at your phone a few minutes, only putting it away as your hands begin to shake."

                "Matt's... blackmailing you?"

                menu bakery_conflicts2_matt_cafeteria2:
                    "Go to the cafeteria." if True:
                        pass
                    "Ignore him." if True:
                        show chelsea sad
                        "You feel sick at the thought of everyone seeing those pictures, but..."
                        "Until now, everything had been consensual. A little demeaning, but you'd enjoyed that..."
                        show chelsea blank
                        "You shake your head to clear your thoughts. No matter what happened before, now he's threatening you!"
                        "It doesn't matter if he shows everyone those pictures; he can't treat you like that!"
                        $ mattblackmail = 2
                        jump events_end_period
    "You raise your hand and ask to use the restroom."
    "The teacher signs your hallpass and tells you to hurry back because there will be a quiz later."
    "Smiling tremulously, you nod, though you're sure you'll miss the quiz."
    "Hurrying down the hall to the cafeteria, you find it empty except for Matt, who stands in a dark corner."
    "You approach him slowly, looking for the handcuffs."
    show Matt Blank at left with moveinleft
    if defymatt:
        pcname "Well, I'm here."
    elif True:
        pcname "You... needed me?"
    m "I want to know why your boss would offer to pay for a boob job?"
    "He crosses his arms, glaring down at you."
    show Matt Question at left
    m "Are you fucking him?"
    show chelsea shocked
    "Your eyes widen in surprise."
    pcname "What...?"
    show Matt Angry at left
    m "I know you're a slut, but you're supposed to be {i}my{/i} slut."
    show Matt Question at left
    m "Haven't you figured that out yet?"
    if defymatt:
        show chelsea angry
        show Matt Blank at left
        if club == "track":
            pcname "The fuck!? I'm not {i}your slut{/i}. I'm not your {i}anything{/i}!"
        elif club == "cheer":
            pcname "Seriously!? I'm not here because I {i}want{/i} to be!"
        elif club == "yearbook":
            pcname "W-what!?"
            "You swallow back your nervousness."
            pcname "I'm not a slut, Matt."
        pcname "You {i}force{/i} me to do this stuff!"
        show Matt Smirk at left
        "He smirks."
        m "You can tell yourself whatever makes you feel better."
        show chelsea blank
        m "But I know you want this. You {i}love{/i} it."
        m "I think you like it {i}better{/i} that I'm blackmailing you."
        "You stare at him, trying to make sense of what he's saying."
        show chelsea confused
        show Matt Blank at left
        "Does he really believe that?"
        show chelsea blank
        "Do you?"
        show Matt Smirk at left
        "He smiles, pulling you back from your sudden doubts."
    elif True:
        show chelsea confused
        if club == "track":
            pcname "Why would I think that? We're not {i}dating{/i} or anything."
        elif club == "cheer":
            pcname "You never told me {i}what{/i} we are... What was I supposed to think?"
        elif club == "yearbook":
            pcname "W-why would I have thought that?"
        show Matt Blank at left
        "He shakes his head."
        m "You're such a stupid cunt..."
    show Matt Question at left
    m "So you {i}are{/i} fucking him?"
    show chelsea shocked
    pcname "What? No!"
    show Matt Pleased at left
    m "Good."
    show Matt Blank at left
    show chelsea blank
    "He stares at you hard a moment, lost in thought. Then he smiles."
    show Matt Happy at left
    m "I wouldn't mind you getting a boob job, actually..."
    show Matt Blank at left
    m "But after you get it, you have to quit your job. I don't want you near that guy."
    if defymatt:
        show chelsea shocked
        pcname "What!? I'm not quitting my job!"
        pcname "I can't pay rent if I'm not working, Matt."
    elif True:
        show chelsea sad
        pcname "But... I can't pay rent if I'm not working."
    m "That's your problem, not mine."
    if defymatt:
        show Matt Angry at left
        m "If you don't quit, you know what's going to happen."
    elif True:
        show Matt Smirk at left
        m "If you don't, I'll have to start handing out all of those pictures I've taken..."
        $ mattblackmail = 1
        $ defymatt = True
        show chelsea confused
        pcname "You're... blackmailing me?"
        show Matt Pleased at left
        "He grins."
        m "If I have to."
    show Matt Blank at left
    m "So... what are you going to do?"
    show chelsea blank
    "There's no way you can quit your job."
    "But if you tell him you're getting the surgery and you're not going to quit..."
    show Matt Question at left
    m "Well?"
    menu bakery_conflicts2_matt_surgery:
        "I'm getting the surgery." if True:
            show Matt Blank at left
            m "And then you're going to quit?"
            pcname "I can't. I'll lose my apartment and..."
            show Matt Angry at left
            "Shaking his head, he glares at you as he walks away."
            m "You're going to be sorry..."
            $ mattrouteend = True
            $ bakeryboobjobapprove = True
            $ mattblackmail = 2
        "I won't get the surgery." if True:
            show Matt Pleased at left
            "He reaches out and grabs your breast, squeezing hard."
            m "That's too bad; I kinda liked the idea."
            show chelsea sad
            pcname "I can't quit my job."
            "He rolls his eyes and gives your breast another squeeze."
            "His other hand reaches for your shirt, quickly undoing the top button."
            show Matt Blank at left
            show chelsea shocked
            "{i}SNAP{/i}"
            "A sudden sound behind the counter startles you both and, as the lights flick on, Matt jumps away from you."
            show chelsea blank
            m "We'll finish this later."
            $ bakeryboobjobapprove = False
    scene bg black with dissolve
    "You wait until he's out of sight to walk back to your own class."
    "Just as you arrive, the bell rings. You definitely failed that quiz."
    $ intelligence -= 5
    jump events_end_period

label bakery_conflicts2_violet:
    show chelsea at right with moveinright
    show bg Cafeteria with dissolve
    if violetrelate == "Dom":
        "You get Violet's lunch for her and take your seat across from her."
        show V School Blank at left with moveinleft
        "As she plays around on her phone, you carefully arrange her tray the way she likes it."
        "Finally, she glances up from her phone."
        show V Smile at left
        V "So... I have tickets for a concert this Saturday. You're going with me."
    elif True:
        "You take your normal seat at lunch and wait for Violet to bring you your food."
        show V SubSchool Happy at left with moveinleft
        "As she sits it down, you look over the tray - it's exactly what you wanted."
        "Taking a bite of your sandwich, you notice Violet fidgeting in her seat."
        show chelsea confused
        pcname "Yes?"
        V "So... I have tickets for a concert on Saturday. Could we go together, please?"
    show chelsea blank
    "Saturday..."
    "That's the date of your surgery; there's no way you can go with her."
    pcname "Actually, I have a doctor's appointment that day, so..."
    V "You do? What doctor is open on a Saturday?"
    if violetrelate == "Dom":
        show V School Annoyed at left
        "She frowns, clearly assuming you're lying."
    elif True:
        show V SubSchool Worried at left
        "Remembering herself, she adds:"
        V "If you... don't mind my asking?"
    pcname "Dr. White. He's..."
    if violetrelate == "Dom":
        "Violet stands, her palms pressed against the table."
    elif True:
        show V School Annoyed at left
        "All semblance of submission disappears as Violet jumps up, palms pressed to the table."
    V "He's a plastic surgeon!"
    show chelsea shocked
    "You nod, surprised."
    V "{i}What{/i} are you seeing {i}him{/i} for!?"
    if club == "track":
        show chelsea blank
        "You shrug."
        pcname "I was going to surprise you with a new set."
        "You look pointedly at your chest."
    elif club == "cheer":
        show chelsea happy
        "You smile."
        pcname "I thought it would be a surprise, but..."
        "You grab a breast and bounce it playful."
    elif club == "yearbook":
        show chelsea blank
        pcname "I... I wanted bigger..."
        "You look down at your shirt, hoping she understands."
    if violetrelate == "Dom":
        V "That's not cheap, [pcname]. How the hell can you afford it?"
    elif True:
        V "Do you have that kind of money?"
    show chelsea happy
    show V School Pout at left
    pcname "Oh... My boss offered to pay, actually."
    pcname "And Lisa went for the consultation, so I'm sure I'll look amazing. She's really good at this kind of thing."
    if violetrelate == "Sub":
        "Violet stares at you a moment before sinking back into her chair."
        "You consider whether you should punish her for her outburst, but before you can decide she speaks up again."
        show V School Annoyed at left
        V "[pcname], I... I just can't pretend I'm okay with this."
        V "Your boss seems like a creep, honestly."
        V "And who is {i}Lisa{/i}, anyway? What is she to you?"
        hide V School Annoyed
        show V SubSchool Sad at left
        "She shakes her head miserably - it almost looks like she's about to cry."
        V "Please... Don't do this."
        menu bakery_conflict2_violetsub:
            "Remember your place." if True:
                hide V SubSchool Sad
                show V School Annoyed at left
                show chelsea shocked
                V "My place? My {i}place{/i}!?"
                show chelsea blank
                "She stands again and glares down at you."
                V "I'm not the one who needs to remember, [pcname]."
                V "Honestly... You've changed. And I don't know if I'm interested in this {i}arrangement{/i} anymore!"
                "Before you can defend yourself, she storms off, leaving her untouched tray behind."
                show chelsea confused
                pcname "What the...?"
                pcname "What's gotten into her?"
                "You finish your lunch in silence, wondering what to do now."
                scene bg black with dissolve
                $ violetrelate = "Sub hold"
                jump events_end_period
            "I won't do it." if True:
                show V School Smile at left with dissolve
                V "Really?"
                "She smiles - but it quickly turns to shock."
                show V SubSchool Sad at left
                V "I'm sorry I... I shouldn't have overstepped like that, should I?"
                V "You should probably punish me for it, huh?"
                show chelsea laugh
                "You can't help but laugh."
                pcname "I'm starting to think you'd like that."
                show V SubSchool Blank at left
                "Violet blushes, making you wish you could punish her {i}right now{/i}."
                "For the rest of lunch, she's biddable and submissive - you almost feel sorry for upsetting her like that."
                "After lunch, you call Dr. White's office and cancel the appointment."
                "Afterwards, you text Lisa."
                "She doesn't respond to your message, but you can imagine how angry she'll be."
                $ bakeryboobjobapprove = False
                jump events_end_period
    elif True:
        show V School Annoyed at left
        show chelsea shocked
        V "I can't believe you right now."
        V "After the conversation we had about your hair, I can't {i}believe{/i} you'd do something like {i}this{/i} without asking me!"
        V "And all because some bitch named Lisa thinks it's a good idea!?"
        V "Why do you care what she thinks? Is she more important to you than I am?"
        "You've never seen Violet this angry before."
        show chelsea sad
        "You want to calm her down, but you don't like the way she's talking about Lisa either."
        menu bakery_conflict2_violetsub2:
            "Apologize." if True:
                show V School Blank at left
                if club == "track":
                    pcname "Look... I'm sorry, okay?"
                elif club == "cheer":
                    pcname "Violet, I'm sorry, I just..."
                elif club == "yearbook":
                    pcname "I-I'm sorry, Violet. I didn't-- I just--"
                show chelsea embarrassed
                pcname "I wanted to look nicer. To be prettier."
                pcname "And Lisa... She keeps telling me to wear make up, or heels, or dye my hair, or..."
                "Violet jumps up from the table, glaring down at you."
                show V School Pout at left
                V "Is that so?"
            "Argue." if True:
                show chelsea angry
                if club == "track":
                    pcname "Lisa warned me this would happen."
                    pcname "She said other girls would be jealous. I just didn't think {i}you{/i} would be one of them."
                elif club == "cheer":
                    pcname "I can't believe you're {i}jealous{/i}."
                    pcname "Lisa told me this would happen. She said I'd make girls jealous, but..."
                elif club == "yearbook":
                    pcname "Y-you're jealous, aren't you?"
                    pcname "Lisa said... but I didn't think {i}you{/i} would be..."
                "Violet jumps up from the table, glaring down at you."
                V "Is that what you think?"
        show chelsea confused
        "Whirling around, she storms out of the cafeteria, leaving you unhappy and confused."
        scene bg black with dissolve
        $ violetrelate = "Dom hold"
        jump events_end_period

label bakery_conflicts2_violet2:
    show chelsea at right with moveinright
    show L Blank at left with moveinleft
    "You and Lisa stand at the counter, chatting about ideas for next season's cupcake flavors."
    L "What would you think of lemon and blueberry?"
    menu bakery_cupcake_flavor:
        "That sounds great!" if True:
            pass
        "I'm not so sure about that..." if True:
            show chelsea confused
            pass
    L "Really? I--"
    show chelsea blank
    "The phone rings, interrupting her."
    L "Hold on, I should answer that."
    hide L Blank with moveoutleft
    "She steps into Keith's office and shuts the door behind her."
    show chelsea shocked
    "Suddenly the front door slams open."
    show V Casual Annoyed at left with moveinleft
    "Violet storms inside, looking all around her."
    V "Well? Where is she?"
    pcname "Violet? What are you...?"
    V "Where's that bitch, Lisa!?"
    "Your mouth falls open in shock."
    show chelsea embarrassed
    if club == "track":
        pcname "What are you doing? Violet, you need to leave."
    elif club == "cheer":
        pcname "What the hell!? You can't do this here, Violet."
    elif club == "yearbook":
        pcname "V-Violet, please, don't cause a scene..."
    V "Lisa! LISA!"
    "Keith's office door swings open and Lisa steps out, pushing her glasses up."
    show V Casual Annoyed at center with move
    show L Question at left with moveinleft
    L "What is going on out here, [pcname]?"
    L "Who's this?"
    V "Who's this? {i}This{/i} is Violet Atwood. And {i}you{/i} must be Lisa."
    show L Blank at left
    show chelsea blank
    "Lisa glances at you, confusion plain on her face."
    show L Question at left
    L "I am. Did you need something?"
    "Violet steps toward her, lecturing her as she walks."
    V "{i}You{/i} need to keep your opinions to yourself and stop pressuring [pcname] to change her appearance!"
    show L Blank at left
    "Violet is nearly shouting in her face now, but Lisa barely reacts."
    L "If [pcname] had a problem with it, she would have told me so herself."
    show L Happy at left
    L "So, clearly, the only problem here is {i}your{/i} opinion of your own importance."
    V "Yeah, well it's {i}very{/i} inappropriate for her boss to offer to pay for elective surgery. And my {i}father{/i} will have something to say about {i}that{/i}."
    show L Blank at left
    "Lisa turns to you."
    L "[pcname], this is your friend. Please ask her to leave; this is very unprofessional."
    "Violet wheels to face you too."
    V "Tell {i}her{/i} that you're not having the surgery!"
    show chelsea sad
    "You can barely believe this is happening."
    "Violet is making a huge scene - you'll be surprised if you still have a job after this!"
    "But it's Violet... And she's clearly upset..."
    menu bakery_conflict2_violet2_ulimatum:
        "Violet... We're done." if True:
            show V Casual Suprised
            "Violet's mouth falls open."
            V "W-what...?"
            V "You're... You can't..."
            "You see the moment when shock gives way to rage play across her face."
            show V Casual Annoyed
            V "That's it. We're {i}done{/i}."
            V "I don't want to ever see you again!"
            "Your heart twists, but you say nothing as she storms out the door."
            hide V Casual Annoyed with dissolve
            show L Happy at left
            L "Wow... That was intense, wasn't it?"
            L "I bet you'll be glad to have such a childish person out of your life..."
            show L Blank at left
            L "Now where were we?"
            "Lisa asks your opinions on a few more flavors, but you just can't focus."
            "Violet didn't give you much choice, but you still can't stop the ache in your chest."
            scene bg black with dissolve
            $ violetrelate = "Enemies"
            $ bakeryboobjobapprove = True
            jump events_end_period
        "Lisa... I'm not getting the surgery." if True:
            if violetrelate == "Sub hold":
                $ violetrelate = "Sub"
            elif True:
                $ violetrelate = "Dom"
            show chelsea blank
            "Lisa's mouth falls open in surprise."
            show L Sad at left
            L "But, [pcname]... You can't let your friends influence you so easily."
            show V Casual Smile
            "Violet smiles triumphantly."
            V "You should know when you've lost, lady."
            V "I'm way more important to her than you'll ever be."
            "She turns to you."
            if violetrelate == "Sub":
                hide V Casual Smile
                show V SubCasual Worried
                V "I know I'll be in big trouble for this. I hope you won't punish me too hard."
                show V SubCasual Happy
            elif True:
                show V Casual Pout
                V "I hope you know that even though you made the right choice, I'll still have to punish you for this."
                show V Casual Smile
            "She walks to the door, winking at you before she leaves."
            hide V Casual Smile with dissolve
            hide V SubCasual Happy with dissolve
            "Lisa turns toward you, shaking her head."
            show L Disappoint at left
            L "I can't believe you'd change your mind just because your little friend threw a tantrum!"
            "She rubs her temples and sighs."
            L "Look, just... Think it over before Saturday, okay?"
            L "I already cleared my schedule for you, so why don't you text me Saturday morning if you still want to cancel?"
            "You think about Violet and how strongly she reacted. She'd never forgive you if you had this surgery..."
            pcname "I'm not changing my mind, Lisa. I'm going to cancel the appointment."
            "To prove your point, you pull up the number on your phone and call their office."
            "In less than a minute, your appointment is cancelled."
            L "I can't believe you wasted my time like this."
            L "If you want to keep looking like {i}that{/i}, then I guess that's your problem."
            L "I'll be in the back if there are any more problems. Don't fuck anything else up."
            "You barely see Lisa for the rest of your shift. You know she's disappointed, and you really do feel bad that she cleared her schedule for you."
            "You hope there's a way you can make it up to her, but you're definitely done trying to change yourself to make her and Keith happy."
            scene bg black with dissolve
            $ bakeryboobjobapprove = False
            jump events_end_period

label bakery_conflict2_matt2:
    if mattblackmail == 2:
        return
    show chelsea shocked
    show Keith Blank
    show L Blank at midright
    show Matt Blank at left with moveinleft
    "To your surprise, Matt walks in."
    show Matt Pleased at left
    "He looks you over, pausing to smile at your breasts."
    show chelsea embarrassed
    m "Those look great. I can't wait to see how they feel."
    "He leers, clearly imagining groping you."
    show Matt Blank at left
    m "But you know what you need to do now, right, slut?"
    show Keith Confused
    BM "And what do you mean by {i}that{/i}."
    "Keith circles the counter to stare Matt down."
    show Matt Smirk at left
    "Matt crosses his arms and stares right back, smirking."
    m "She's done working here, old man. But thanks for the new tits; I'm {i}really{/i} going to enjoy them."
    show Keith Smirk
    show chelsea shocked
    BM "As if you'd know what to do with them anyway."
    "You stare, mouth agape, as the two men argue about you."
    "Lisa leans in close and whispers:"
    show L Happy at midright
    L "This is cute, and it's {i}got{/i} to be good for your pride, but..."
    L "Maybe it's time you settle this?"
    "You nod and clear your throat."
    show L Blank at midright
    show chelsea angry
    if club == "track":
        pcname "Matt, that's enough! I already told you I'm not quitting!"
    elif club == "cheer":
        pcname "For the last time, I'm {i}not{/i} quitting!"
    elif club == "yearbook":
        pcname "I'm not quitting, Matt. I'm not!"
    show Matt Blank at left
    "Matt glares at you, his arms falling to his sides."
    show Matt Angry at left
    m "You know what I'll do if you don't!"
    if club == "track":
        pcname "I don't give a shit if you show everyone those pictures!"
        pcname "You can't control me anymore. I'm {i}done{/i} being your {i}whore{/i}!"
    elif club == "cheer":
        pcname "Good! I'm sick of you holding those pictures over me!"
        pcname "I'll {i}never{/i} let you touch me again!"
    elif club == "yearbook":
        pcname "Do whatever you want! You always do anyway!"
        pcname "You can't b-blackmail me anymore, Matt!"
    show Keith Confused
    show Matt Blank at left
    BM "You're blackmailing her into fucking you?"
    show Keith Laugh
    show chelsea embarrassed
    "Keith laughs and you find yourself hot with shame."
    show Keith Smirk
    BM "You're {i}pathetic{/i}. A {i}real{/i} man doesn't have to force a girl to do what he wants."
    BM "He's strong enough that they {i}want{/i} to serve him."
    show Keith Happy
    "Keith is smiling now and, for once, you're not afraid of him."
    BM "[pcname] already told you she's not interested in knowing you anymore."
    show Keith Neutral
    BM "So, if you know what's good for you, you'll delete those little pictures and forget you ever met her."
    show Keith Blank
    show Matt Question at left
    m "What's that supposed to mean!?"
    "Keith takes a step closer, looking down his nose at Matt."
    show Keith Smirk
    BM "It means that you're a {i}child{/i} and--"
    show Matt Angry at left
    m "I'm not a fucking child! I'm eighteen!"
    show Keith Blank
    "Pulling back his fist, Matt swings at Keith - who easily catches his hand in the air."
    "Instead of being angry, Keith smirks."
    show Keith Happy
    BM "Really? That's good..."
    "Keith takes a step back, still holding onto Matt's fist."
    show Keith Smirk
    BM "That means the charges won't be serious if I decide to show you the error of your ways."
    "Matt's eyes widen in surprise as Keith yanks him forward, shoving his other fist into Matt's stomach."
    show Matt Blank
    "Matt folds over Keith's fist, doubling over in pain. Taking another step back, Keith releases him."
    hide Matt Blank with moveoutbottom
    "Matt drops to the floor, clutching his abdomen and gasping for breath."
    show Keith Neutral
    BM "Now, you're not going to {i}speak{/i} to [pcname] again."
    show Keith Angry
    BM "And if those pictures get out, I will personally make sure that you regret it."
    "Matt drags himself off the ground, glaring between you and Keith."
    "For a moment, you think he's going to fight back - he's been so domineering with you, you know he won't just back down."
    show Matt Angry at left with moveinbottom
    m "Whatever. She's not worth it anyway."
    "With one final glare in your direction, he wheels around and storms out the door, slamming it behind him."
    hide Matt Angry with moveoutleft
    show Keith Happy
    BM "Well, that was fun..."
    "Keith is still smiling as he turns back to you and Lisa."
    if club == "track":
        show chelsea sad
        pcname "Um... Thanks for standing up for me, Keith."
    elif club == "cheer":
        show chelsea happy
        pcname "That was {i}amazing{/i}, Keith. Thank you!"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Th-thanks, Keith... I didn't know what to do about him."
    "Shaking his head, Keith shrugs."
    show Keith Neutral
    show chelsea blank
    BM "He thinks he's important, but he's just an upstart with a lot to learn."
    show Keith Smirk
    BM "Don't worry about it, [pcname]. I don't mind putting guys like that in their places."
    show Keith Happy
    "He pats your head as he walks past you; it almost feels affectionate."
    BM "I'll be in my office, ladies."
    hide Keith Happy with moveoutleft
    hide L Blank with dissolve
    show L Happy at left with dissolve
    "As soon as he's out of earshot, Lisa giggles."
    L "Well, {i}that{/i} was exciting, wasn't it? Two men fighting over you?"
    if club == "track":
        "You scowl."
    elif club == "cheer":
        show chelsea happy
        "You giggle."
    elif club == "yearbook":
        show chelsea embarrassed
        "You blush."
    pcname "Keith wasn't fighting over me. Matt was causing a scene so he took care of it."
    pcname "It was just... bad for business."
    show L Blank at left
    L "Maybe..."
    show chelsea happy
    if club == "track":
        "Even if you're right, you can't help the warm feeling you get when you think of him standing up for you."
    elif club == "cheer":
        "Even though you're sure that's all it was, you {i}did{/i} like the idea of them fighting over you."
    elif club == "yearbook":
        "You still can't help but think of Keith towering over Matt, threatening him on your behalf."
    "It felt really good to have someone like Keith on your side, looking out for you."
    "You smile at the thought as the doorbell chimes again."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
