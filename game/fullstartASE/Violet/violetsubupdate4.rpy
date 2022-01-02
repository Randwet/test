label violetsub4_clean:
    $ violetAttire(1)
    $ acts -= 1
    scene bg CityN
    $ clothes, hair = casualwear
    show chelsea at center, enterScene(0.8, 0.5, 0.4, 0.4)
    "After work, you walk home, wondering if Violet really cleaned the apartment."
    show chelsea embarrassed
    "Does she even know how to clean? The thought brings a smile to your lips."
    if club == "track":
        show chelsea blank
        "Preparing to open the door, you put on your game face; you're ready to judge her work."
    elif club == "cheer":
        show chelsea blank
        "As you unlock the door, you let the smile drop; you're ready to evaluate her work."
    elif club == "yearbook":
        show chelsea sad
        "As you prepare to open the door, you feel a little nervous. If she didn't clean well, you'll have to punish her."
    scene bg HomeN with dissolve
    show chelsea shocked at right with dissolve
    pause 1.0
    show chelsea laugh
    "Swinging the door open, the first thing you see is Violet - sprawled out on your couch, watching TV."
    show chelsea blank
    show V Casual Suprised at moveupfast(1.0, -0.075, 0.1)
    "She grabs the remote and turns the TV off, practically jumping to her feet."
    V "Sorry, [domtitle], I didn't realize what time it was!"
    hide V Casual
    show V SubCasual Worried at left
    "Glancing around the room, you can tell she's done some cleaning."
    show chelsea angry
    show V SubCasual Sad
    pcname "Wait here while I check your work."
    scene bg RoomE
    show chelsea blank
    with dissolve
    "You check the bedroom first, noting the unmade bed. It looks like she took the glass you'd left by your bed to the kitchen, though."
    show chelsea confused
    "The bathroom is tidy, but the mirror is streaked and smudged. She cleaned it, but not well."
    show chelsea sad
    "In the kitchen, the dishes are clean and neatly stacked on the drying rack, but they've clearly been dry a while."
    show chelsea shocked
    "And it looks like all of the garbage she gathered from other rooms is piled into the trashcan."
    show chelsea blank at exitScene(0.5, 1.0, 0.3, 0.3)
    "Sighing, you walk back to the couch, where Violet waits with a smile."
    scene bg HomeN with dissolve
    show V SubCasual Happy with dissolve
    pause 0.5
    show chelsea at left, enterScene(-0.5, 0.0, 0.4, 0.4)
    V "Well? Good, right?"
    show chelsea sad
    "Shaking your head, you gesture at the bedroom."
    show chelsea angry
    show V SubCasual Sad
    pcname "The bed isn't made. And the bathroom mirror is streaked. Don't you know how to clean glass?"
    "As you speak, her smile fades. But you continue."
    show V SubCasual Worried
    pcname "The dishes are clean but you didn't put them away - and you didn't take the trash out."
    V "Oh. Right. I forgot about that..."
    show chelsea blank
    "Crossing your arms, you give her a hard stare."
    show V SubCasual Sad
    pcname "You {i}forgot{/i}?"
    V "I..."
    show V SubCasual Worried
    "Sensing her error, she flushes a little."
    show chelsea sad
    V "I took a break and started watching TV, and I guess I got distracted..."
    "You sigh."
    show chelsea blank
    show V SubCasual Sad
    pcname "Okay. Obviously, this isn't acceptable."
    show V SubCasual Blank
    "She nods, a small smile playing over her lips."
    show chelsea shocked
    "She {i}wants{/i} to be punished, you realize."
    show chelsea blank
    show V SubCasual Worried
    pcname "So, here's your punishment."
    "You look her up and down, letting her anticipation build."
    show chelsea angry
    show V SubCasual Blank
    pcname "Strip. Now."
    show chelsea embarrassed
    "She obeys quickly - eagerly - and you smile."
    pcname "Very nice. Now, start with the bedroom and hurry up."
    hide V SubCasual
    show V Casual Suprised
    "Violet's mouth falls open."
    if violetcum < 2:
        V "Are you {i}serious{/i}?"
        show V Casual Pout
        "Her lower lip juts forward in a pout."
        show chelsea angry
        hide V Casual
        show V SubCasual Worried
        pcname "Completely. And you will call me [domtitle] or this will get {i}much{/i} worse for you."
        "Her eyes widen and she nods."
    elif True:
        hide V Casual
        show V SubCasual Sad
        V "I..."
        show V SubCasual Worried
        "Whatever she was going to say, she suddenly thinks better of."
        show V SubCasual Sad
        V "Yes, [domtitle]."
    scene black with dissolve
    "She gets to work, starting with the bed."

    "You watch as she completes each task, admiring the way her body looks as she bends and stretches."
    "The curve of her ass and breasts. The way her pussy peaks out as she bends over."

    "The way her nipples wrinkle and pucker when they graze the cold bathroom vanity."

    "She's gorgeous. And sexy. And yours."

    "As she finishes replacing the garbage bag, her eyes dart from the full bag of garbage, to the front door, and back again."
    V "Um, [domtitle]?"
    "You smile; you've already realized her problem."
    V "How can I take the trash out like this?"
    "She motions to herself, and her lack of clothes."
    pcname "What do you mean?"
    "Her eyes widen, but she doesn't want to believe her own thoughts."
    V "Can I put my clothes back on...?"
    "Your smile widens."
    pcname "If you'd taken it out before I got home, you'd have had your clothes on, wouldn't you?"
    "Her mouth moves silently, the words never making it from brain to tongue."
    pcname "It's dark out. If you hurry, I'm sure nobody will see you."
    V "What...? But-"
    "She bites her lip, recognizing your resolve."
    V "Yes, [domtitle]."
    "Lifting the bag, she holds it awkwardly in front of her."
    "It covers her well enough that - at first glance - you might not realize she's naked."
    "She seems to realize this, pulling the bag closer and wrinkling her nose."
    "Pulling the door open, she hurries out of the apartment, disappearing down the hallway."
    "You stand at the door, listening. While you want her to be thoroughly embarrassed, you don't want her to be in any danger."

    "As soon as you see her reappear in the hallway, you step back into the apartment."
    "She practically runs inside, shutting the door behind her and leaning back against it, breathing hard."
    V "There... Done..."
    pcname "Good. Now, I think you should apologize for wasting my time."

    if violetcum < 2:
        V "What? But you already got a show, and-"
        "She stops, realizing what she's doing."
        "Sighing, she crosses the room and drops to her knees."
        V "I'm sorry, [domtitle]. I should have cleaned right the first time."
        "While she's saying all the right things, it doesn't {i}sound{/i} like she means it."
        if club == "track":
            pcname "I think I've been letting you cum too often. You're not as obedient as I'd like."
        elif club == "cheer":
            pcname "Is that the best you can do? Maybe I'm letting you cum too much..."
        elif club == "yearbook":
            pcname "R-really? That's it? I've been too lenient with you lately..."
        V "No! I'm sorry, you're right. I was bad and I deserved to be punished."
    elif True:
        "She crosses the room, dropping to her knees."
        V "I'm sorry, [domtitle]. I should have cleaned better the first time."
        V "I've learned my lesson, I promise. I'll do better next time."
        "You're surprised by her sincerity. Clearly witholding her orgasms has been working."
    V "Is there anything else I can do to make it up to you?"
    "She looks up at you hopefully; you know what she's {i}really{/i} asking."
    "Part of you wonders if you should reward her behavior, but another part of you - the part that spent the last hour watching Violet cleaning in the nude - wants the same thing."
    menu violetsub4_clean_reward:
        "Let her pleasure you." if True:
            pcname "There might be {i}something{/i}..."
            "Leaving Violet on her knees, you slowly undress."
            "She watches, licking her lips in anticipation."
            "Strolling to the couch, you get on your hands and knees, lifting your ass in the air."

            "Peering back, you smile at Violet."
            pcname "Get over here. I have something else for you to \"clean\"."
            "She gets to her feet and approaches the couch, waiting for more instructions."
            "You wiggle your ass, smiling back at her."

            if club == "track":
                pcname "Have you ever eaten ass before?"
            elif club == "cheer":
                pcname "Well? My asshole isn't going to lick itself."
            elif club == "yearbook":
                pcname "Ready to... to lick my ass...?"
            "Her eyes widen."
            V "Your {i}ass{/i}?"
            pcname "And I hope you're better at that than you are at cleaning."
            "Hesitantly, she approaches the couch, taking up a position behind you and leaning toward you."
            "Her hands cup your ass cheeks, spreading them gently."

            "Pausing a moment, she prepares herself, then lowers her head and swipes her tongue over your asshole."
            "Your sphincter clenches at the contact and you gasp."

            "Violet hesitantly licks your ass again. Her hot, wet tongue teasing your opening."
            if club == "track":
                pcname "You wanted to make it up to me, so stop being so shy about it."
            elif club == "cheer":
                pcname "Come on, Violet. Show me how {i}sorry{/i} you are."
            elif club == "yearbook":
                pcname "Is that the best you can do...?"
            "Violet takes a deep breath and exhales - the air running over your ass and pussy, making you shiver."
            V "Sorry, [domtitle]."
            "She presses her tongue to your ass again, wiggling it into the tight hole."

            "You gasp, moaning softly and pressing your ass toward her."
            "Her tongue squirms inside of you, her fingers digging into your butt cheeks."
            "She pulls her tongue back, flicking it over your opening."

            pcname "Mmmm~"
            "Getting into it now, she flicks her tongue over your hole again and again."
            "The hot, wet flesh teasing the sensitive rim of your ass draws another moan from you, even as you feel her saliva trailing down your pussy."

            "Her tongue circles your hole - stroke, teasing, tantalizing..."
            V "Mmm~ Uhhnn~"
            "Her hands massage your ass, lifting and squeezing your cheeks."
            "Her tongue slips down, brushing the edge of your pussy before running up your crack again."
            pcname "Ahhh~"
            "Over and over, Violet runs her tongue from your pussy to your ass, teasing both."
            V "Please, [domtitle]... May I lick your pussy too?"
            pcname "Yes..."

            "Her tongue dives into your cunt, lapping your juices eagerly."
            pcname "Ohhh~ Fuck~"
            "You shudder as her tongue plunders your pussy - stroking, flicking, and caressing your insides."
            "It returns to your ass, her fingers stretching you wide."
            "The soft flesh wriggles into the tight ring of your asshole, writhing and pressing into you."
            "Your clit throbs, aroused and neglected, and you reach down to rub the sensitive nub."

            "No longer reserved, Violet eats your pussy and ass in turns, eagerly tasting one and then the other."
            "Your muscles begin to tense, your cunt tightening as your orgasm draws close."
            "Violet focuses on your ass again, spreading your cheeks and thrusting her tongue inside."
            "She fucks your ass with her tongue, plunging it inside again and again."
            "Your clit throbs with pleasure as you rub it, and a familiar ache spreads through your abdomen."
            "Your sphincter clenches as your climax rushes over you, and Violet flicks her tongue against it over and over."
            pcname "Ohhhh~ Fu~UCK~"

            "Shuddering and moaning, you sink forward on the couch, breathing heavily."
            "Violet waits as you catch your breath. Eventually, you roll over, smiling up at her."
            V "May I... May I cum too, [domtitle]?"

            "Looking at her again, you see her nipples - red and puckered with arousal - jutting toward you."
            "Her lips are puffy and pink; her swollen clit peeks out from her labia."
            "And her chin is coated in a mixture of saliva and your own juices."
            menu violetsub4_clean_cum:
                "You may." if True:
                    $ violetcum = 0
                    "She smiles, trembling with relief."
                    "Her fingers drop to her pussy, one hand focused on her clit while the other sinks inside of her."

                    "Already aroused, her fingers plunge easily into her dripping cunt."
                    "She pounds them into her, fingering herself with wild abandon."
                    "With her other hand, she rubs her clit in small, quick circles. Her eyes roll back, the lids fluttering as she races toward her own orgasm."

                    V "Oh shit... [domtitle]... [domtitle]..."
                    "Her limbs go stiff, her body shaking as she cums hard."

                    "As the pleasure fades, her eyes focus on you and a slow smile spreads over lips still wet with your juices."
                    V "Th-thank you, [domtitle]."
                    "Smiling back, you pull her in for a wet kiss."

                    "Releasing her, you pull yourself up from the couch and stretch."
                    scene bg HomeN with dissolve
                    $ clothes = "naked"
                    show chelsea with dissolve
                    pcname "I guess you should get dressed now."
                    V "R-right."
                    "She stands too, shivering slightly, and stumbles toward her clothes."
                    show chelsea embarrassed
                    "You watch her dress, a bittersweet smile on your lips."
                    show V SubCasual Worried at right with dissolve
                    "As she reaches for the door, she turns back to you."
                    show chelsea blank
                    show V SubCasual Sad
                    V "I'll do better next time, [domtitle]. Promise."
                    pcname "Good. I expect you to."
                    hide V SubCasual with dissolve
                    "She bows her head and lets herself out."
                "Not this time." if True:
                    $ violetcum += 1
                    pcname "Oh, Violet... It's too late for that."
                    pcname "You don't get a reward for the job you did today."
                    "Her lower lip trembles; her eyes brim with frustrated tears."
                    "Sitting up, you cup her cheek in your hand and smile."

                    pcname "I'm glad you're taking this seriously now."
                    pcname "Do better next time, and maybe I'll be more generous."
                    "Violet nods, taking a deep breath."
                    V "Yes, [domtitle]. I'll do better next time."
                    pcname "I'm sure you will. Now get dressed."
                    scene bg HomeN with dissolve
                    $ clothes = "naked"
                    show chelsea embarrassed with dissolve
                    "You watch as she pulls her clothes on, a bittersweet smile on your lips."
                    show chelsea blank
                    show V SubCasual Worried at right with dissolve
                    "As she reaches for the door, she turns back to you."
                    show V SubCasual Sad
                    V "I really {i}will{/i} do better next time, [domtitle]. Promise."
                    show chelsea blank
                    pcname "Good. I expect you to."
                    hide V SubCasual with dissolve
                    "She bows her head and lets herself out."
        "Send her home." if True:
            "Crossing your arms, you shake your head."
            pcname "I really wanted to come home to a clean apartment, so we could spend the rest of the night having fun."
            pcname "But that's not what happened, is it?"
            "Violet shakes her head, her eyes still hopeful."
            pcname "I can tell how much you want to cum, but I don't think your performance tonight deserves a reward."
            pcname "And I think pleasuring me is too much of a reward too."
            "She bites her lip, trying not to look disappointed."
            pcname "So tonight, you're going home. You aren't going to touch yourself. You're going to think about how you failed me."
            pcname "And next time, you'll do better. Do you understand?"
            "Her eyes brim with tears of frustration, but she nods."
            V "Yes, [domtitle]. I understand..."
            pcname "Then hurry up and get dressed. I've wasted my whole night correcting you."
            scene bg HomeN with dissolve
            "Miserable, she nods again and rushes to dress."
            show V SubCasual Sad at right with dissolve
            V "I'm really sorry, [domtitle]. I promise I'll do better next time. I will!"
            show chelsea embarrassed with dissolve
            "You nod, pleased by how effective your punishment has been."
            show chelsea blank
            pcname "Just remember this the next time I give you an opportunity to please me."
            show V SubCasual Worried
            V "Yes, [domtitle]. Thank you."
            show V SubCasual Sad
            "She pauses at the door, perhaps hoping you'll change your mind, before letting herself out."
            pause 0.8
            hide V SubCasual with dissolve
            pause 0.8
    $ violetAttire()
    $ clothes, hair = casualwear
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
