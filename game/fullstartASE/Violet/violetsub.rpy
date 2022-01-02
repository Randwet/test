label violetsub1:
    show bg Cafeteria with fade
    show chelsea at right with moveinright
    show V SubSchool Sad at left with moveinleft
    "You walk into the lunch room and look for Violet."
    "She's sitting at the normal table, glancing around nervously."
    "As you approach, she straightens up in her chair."
    show V SubSchool Blank at left
    V "[pcname]! Is there anything I can get you?"
    if club == "track":
        show chelsea confused
        "Her sudden deference throws you off."
    elif club == "cheer":
        show chelsea shocked
        "You pause, surprised by her change of attitude."
    elif club == "yearbook":
        pcname "Um..."
    show chelsea blank
    menu violetsub1_orders:
        "Go get my food." if True:
            show chelsea happy
            "She nods."
        "I shouldn't have to tell you!" if True:
            "You decide to take a firm hand with her."
            if club == "track":
                show chelsea confused
                pcname "I shouldn't have to tell you to get my food!"
            elif club == "cheer":
                pcname "I shouldn't have to {i}tell{/i} you something so simple, should I?"
            elif club == "yearbook":
                pcname "You're waiting to be {i}told{/i} I need to eat?"
        "Nothing." if True:
            $ violetapproval -= 1
            "She sighs."
            V "Seriously? I thought we'd play around a little..."
            "You realize what she's looking for; this would have been a good opportunity to make her serve you."
            pcname "What you want isn't important."
            if club == "track":
                pcname "But since you're so eager to do something, go get my lunch."
            elif club == "cheer":
                pcname "But since you're annoying me, go get my lunch."
            elif club == "yearbook":
                pcname "But you can... go get my lunch, I guess."
    show chelsea blank
    show V SubSchool Happy at left
    V "What do you want to eat?"
    pcname "Hmmm... I'll have spaghetti with extra breadsticks, bottled water, and a pudding cup."
    "She nods, quite serious about your meal."
    hide V SubSchool Happy with dissolve
    "You play with your phone, not quite sure what to do while she's gone."
    "It's weird not getting your own tray."
    show V SubSchool Happy with moveinleft
    V "Here you go!"
    "Violet sets a tray in front of you. Spaghetti, a breadstick, bottled water, and a chocolate pudding cup."
    "Only one breadstick."
    V "Did I do a good job?"
    menu violetsub1_eval:
        "It's fine." if True:
            $ violetapproval -= 1
            show V SubSchool Worried at left with move
            pcname "Yep. Looks good."
            "Her mouth drops open, as if she's going to speak, but she closes it firmly, frowning."
            V "Are you sure?"
            "You were going to let it go, but..."
        "No." if True:
            if club == "track":
                pcname "No, actually..."
            elif club == "cheer":
                pcname "Well, not really."
            elif club == "yearbook":
                pcname "Um..."
    show chelsea angry
    pcname "You forgot the extra breadstick."
    show V SubSchool Sad at left with move
    "She blinks, glancing down at the tray."
    show chelsea blank
    V "Damn! I did, didn't I?"
    "She tilts her head, looking at you through her lashes."
    show V SubSchool Blank at left
    V "Does that mean you're going to punish me?"
    menu violetsub1_punishment:
        "Get on your knees and beg forgiveness." if True:
            show chelsea happy
            show V School Suprised at left
            V "Wh-What!?"
            if club == "track":
                show chelsea angry
                pcname "You heard me."
            elif club == "cheer":
                pcname "Or aren't you really sorry?"
            elif club == "yearbook":
                show chelsea confused
                pcname "W-Well?"
            show chelsea blank
            "Her mouth falls open, but she slowly sinks to her knees beside the table."
            show V SubSchool Sad at left
            V "[pcname], I'm very sorry that I got your lunch wrong. Please forgive me?"
            if club == "track":
                "You pause a moment, as if thinking, before nodding."
            elif club == "cheer":
                show chelsea happy
                "You pause a moment, savoring your new power over her, before nodding."
            elif club == "yearbook":
                "You pause a moment, wondering if people are watching, before nodding."
            show chelsea blank
            "Violet scrambles to her feet, brushing herself off."
            show V SubSchool at left
            "She takes her seat and lunch proceeds as normal - except, for once, Violet pauses her monologues to see what you have to say."
            "And she seems genuinely interested in hearing your opinions."
        "Only speak when spoken to." if True:
            pcname "For the rest of lunch, you can only speak when spoken to."
            show V SubSchool Worried at left
            "She opens her mouth to speak, but you silence her with a look."
            if club == "track":
                pcname "Now sit down and eat."
            elif club == "cheer":
                pcname "Well? Sit down and eat."
            elif club == "yearbook":
                pcname "You can still eat, though."
            show V SubSchool Sad at left
            "She takes her seat slowly, staring at her tray."
            "Lunch is quiet - you almost miss her self-absorbed rambling."
            "But without her narcissistic chatter, you feel like she's actual paying attention to {i}you{/i} for once."
    "When you've finished eating, you motion to your empty tray."
    show V SubSchool Blank at left
    pcname "You can take that now."
    show chelsea happy
    "Bowing her head, she dumps your tray out and returns to her seat."
    "Just as she sits back down, the bell rings for the end of lunch."
    if club == "track":
        pcname "You did great today, Violet. I'm really happy with you."
    elif club == "cheer":
        pcname "Lunch is over - you did a good job!"
    elif club == "yearbook":
        pcname "You did a good job today, Violet..."
    show V SubSchool Happy at left
    "She smiles, her cheeks flushing adorably."
    "You're struck by how {i}cute{/i} she looks when she's embarrassed - you would never have guessed!"
    V "Th-Thanks, [pcname]..."
    pcname "I'll talk to you later. See ya!"
    hide V SubSchool Happy with dissolve
    hide chelsea with dissolve
    jump events_end_period


label violetsub2:
    scene bg black with dissolve
    $ violetsub2count += 1
    play sound PhoneVibration
    "As you're leaving work, you get a text message."

    call screen TextingScene("Violet",
    [
        TextMessage("Hey I was wondering if we could hang out"),
        TextMessage("If you're free")
    ])

    menu violetSubPhoneResponse1:
        "What will you do?"
        "Meet at my place." if True:

            jump violetsub2_free
        "Make her wait." if True:
            jump violetsub2_wait

label violetsub2_wait:
    "Not this time. She can wait until it's convenient for {i}you{/i}."

    if violetsub2count == 3:
        $ violetapproval = 0

    jump events_end_period

label violetsub2_free:
    call screen TextingScene("Violet",
    [
        TextMessage("Meet me at my place.", sender = False),
        TextMessage("Be right there!")
    ])

    "You walk home, half expecting Violet to beat you there."
    show bg black with fade
    pause 0.3
    $ clothes, hair = casualwear
    show bg HomeE with dissolve
    "When she's not there, you take some time to tidy up a little."
    show bg HomeN with fade
    "An hour goes by before, just as you pick up your phone to text her, there's a knock on your door."
    show chelsea at right with moveinright
    show V SubCasual Blank at left with moveinleft
    menu violetsub2_late:
        "Scold her." if True:
            "You open the door, frowning."
            if club == "track":
                pcname "Did your car break down?"
                "She stares at you."
                V "What?"
                pcname "Why else would it take over an hour for you to get here?"
                pcname "I beat you here just walking!"
            elif club == "cheer":
                show chelsea confused
                pcname "I thought you wanted to hang out?"
                V "I do. Why else would I have come over?"
                pcname "I would've thought you'd get here faster, then."
            elif club == "yearbook":
                pcname "Running a little late? It's been over an hour..."
            show V SubCasual Sad at left
            V "Oh... Sorry!"
        "Ignore it." if True:
            $ violetapproval -= 1
            "You motion for her to come in."
    show chelsea blank
    "Violet shifts nervously. It's obviously difficult for her to let someone else take the lead."
    show V SubCasual Blank at left
    V "So... Now what?"
    pcname "I thought we'd stay in and watch a movie."
    show V SubCasual Worried at left
    V "Oh..."
    V "That's fine. I guess."
    "Ignoring her disappointment, you pick up the remote and take a seat."
    show V SubCasual Sad at left
    "As you flip through the channels, you consider your next move with her."
    menu violetsub2_movie:
        "Make her serve you." if True:
            if club == "track":
                pcname "I'm a little thirsty, actually."
                pcname "Get me a glass of water."
            elif club == "cheer":
                pcname "Hmm... I think I need a drink."
                pcname "Water, please."
            elif club == "yearbook":
                pcname "I... I'm thirsty."
                pcname "You should get me a glass of water."
            "It takes a moment for her to realize what you're doing."
            show V SubCasual Happy at left
            V "Of course!"
            "She brings a glass of water back."
            pcname "Hmmm... More ice, I think."
            "Nodding, she takes the glass away."
            "You hear her breaking the ice out of the ice tray as you pick a movie."
            "When she returns, you motion for her to sit."
            show V SubCasual Blank at left
            "As the movie goes on, you send her on little errands - first for a pillow, then for a blanket."
            "You feel a little bad that she's missing some of the movie, but it's nice not to have to get up."
            "And she actually seems more interested in making you comfortable than watching the movie anyway."
        "Make her give you a massage." if True:
            show chelsea happy
            show V SubCasual Happy at left
            if violetgivesmassage == False:
                pcname "I think you owe me a massage, don't you?"
            elif True:
                pcname "I really liked that massage; I think I need another."
            "Standing behind the couch, she massages your shoulders and neck while you watch the movie."
            "It's great, but after a long day at work, it's your feet that need it the most."
            show chelsea blank
            show V SubCasual Blank at left
            pcname "Come sit down."
            "As she takes a seat beside you, you lay across the couch and swing your feet onto her lap."
            pcname "My feet are killing me!"
            "She stares at them a moment before hesitantly taking the left one in her hands."
            "As you watch the movie, she rolls her thumbs across the arch of your foot, drawing out a satisfied moan."
            "Encouraged by your obvious pleasure, she takes her task seriously, finding all of the sore and tender spots on your foot and soothing them away."
            "Though you barely pay attention to it, you're almost sad when the movie ends."
    "Violet stands, stretching, and looks at her phone."
    V "It's getting pretty late. I guess I should go home, huh?"
    show V SubCasual Happy at left
    V "Unless I could convince you to let me stay a little longer?"
    menu violetsub2_stay:
        "Let her stay." if True:
            show V SubCasual Worried at left
            $ violetapproval -= 1
            "She stares at you for a moment."
            V "I thought... I figured I'd have to do {i}something{/i}..."
        "Ask if she deserves to stay." if True:
            show chelsea confused
            show V SubCasual Blank at left
            "She pauses, thinking."
            V "I think that I should work harder for it, don't you?"
    show chelsea blank
    menu violetsub2_stay2:
        "Let her convince you." if True:
            if club == "track":
                pcname "Alright... Convince me."
            elif club == "cheer":
                pcname "Let's see if you can convince me."
            elif club == "yearbook":
                pcname "Then... do something."
        "Let her leave." if True:
            if club == "track":
                pcname "Have a good night then!"
            elif club == "cheer":
                pcname "It's pretty late and I should get to bed..."
            elif club == "yearbook":
                pcname "I'm tired, so..."
            show V Casual Suprised at left
            V "What?"
            pcname "You're right. You shouldn't stay tonight."
            show V SubCasual Worried at left
            V "I didn't..."
            "Yawning, you stretch."
            pcname "Lock the door on your way out, okay?"
            "Without waiting, you head into the bathroom."
            "You hear the door shut as you're getting ready for bed."
            hide V SubCasual Worried with dissolve
            jump endday
    show chelsea happy
    show V SubCasual Happy at left
    scene bg black with dissolve
    "Tapping on her phone a few times, Violet turns on some music."
    "Blushing, she pushes you back onto the couch."
    show bg VStrip1 with dissolve
    "Then, standing in front of you, she sways to the rhythm of the song."
    show bg VStrip2 with dissolve
    "Slowly, she peels her shirt..."
    show bg VStrip3 with dissolve
    "...revealing her navel... her bra... her cleavage..."
    show bg VStrip4 with dissolve
    pause 0.1
    show bg VStrip5 with dissolve
    pause 0.1
    show bg VStrip6 with dissolve
    "As she drops the top away from her shoulders, she does a little turn, peeling it off one arm and then the other as she moves."
    show bg VStrip7 with dissolve
    "With the turn complete, she tosses the shirt aside and runs her hands over her breasts and down her sides."
    show bg VStrip8 with dissolve
    pause 0.1
    show bg VStrip9 with dissolve
    pause 0.2
    show bg VStrip10 with dissolve
    "As the song picks up, she strikes a dramatic pose, framing the top of her pants with splayed fingers."
    show bg VStrip11 with dissolve
    "Rippling her fingers a moment, as if to tease you, she slowly draws them closer to the button."
    show bg VStrip12 with dissolve
    "Unhooking it, she slowly draws the zipper down, exposing her lacy panties."
    show bg VStrip13 with dissolve
    pause 0.3
    show bg VStrip14 with dissolve
    "Turning suddenly, she twists to look back at you and slowly lowers her pants over her ass, revealing her thong."
    show bg VStrip15 with dissolve
    "Stepping out of one pant leg and then the other, she dances in her bra and underwear until the song ends."
    show bg VStrip16 with dissolve
    V "Well? Did I convince you?"
    if corruption > 20:
        pcname "Not yet."
        "Smiling, Violet turns a new song on."
        show bg VStrip17 with dissolve
        "Moving in time with the music, she unhooks her bra one-handed, clasping it to her with her other hand."
        show bg VStrip18 with dissolve
        "Shimmying her shoulders, she works the bra straps down her arms."
        show bg VStrip19 with dissolve
        "With a knowing look, she catches your eye and smiles before tossing the bra aside too."
        show bg VStrip20 with dissolve
        "Her nipples stiffen in the open air, rising into tempting peaks as you watch."
        "She raises her hands above her head, stretching her torso to give you an even better view."
        show bg VStrip21 with dissolve
        "Turning away from you, she hooks her thumbs in her panties."
        show bg VStrip22 with dissolve
        "You watch as she pulls them slowly over her hips and down her thighs, noting the way they stick to her pussy before finally pulling away."
        show bg VStrip23 with dissolve
        "She tosses her panties toward you; they land on your lap."
        show bg VStrip24 with dissolve
        "Running her hands down her legs, she wraps her hands around her ankles and smiles at you from between her legs."
        show bg VStrip25 with dissolve
        "Standing, she sways to the music, running her hands across her body."
        show bg VStrip26 with dissolve
        "Finally, she sashays to you, leaning down so her breasts are inches from your face."
        show bg VStrip27 with dissolve
        V "{i}Now{/i} can I stay the night?"
    show bg HomeN with dissolve
    show chelsea embarrassed at right with dissolve
    if club == "track":
        pcname "That will do."
    elif club == "cheer":
        pcname "I suppose so..."
    elif club == "yearbook":
        pcname "Y-yes..."
    show chelsea blank
    pcname "I'm going to get in the shower. Order something for us to eat."
    hide chelsea with moveoutright
    $ clothes = 'underwear'
    pause 1.0
    hide V SubTopless Blank with dissolve
    show chelsea at right with moveinright
    "You strip out of your clothes, unsurprised by the stickiness in your panties."
    hide chelsea with dissolve
    $ clothes = 'naked'
    pause 1.0
    show bg black with dissolve
    show chelsea with dissolve
    "As the water heats up, you step into the shower."
    "Your mind keeps drifting back to Violet's striptease."
    "Her perky breasts and round ass..."
    if corruption > 20:
        "Her hard nipples..."
        "The way her pussy peaked out when she bent over..."
    show chelsea embarrassed
    "As you think about it, your hands stray to your own breasts, massaging the wet, firm curves."
    "You imagine her breasts under your fingers, her hands caressing you..."
    "Licking your lips, you imagine taking one perfect nipple between them - sucking it as she gasps, wrapping her fingers in your hair..."
    "Twisting your own nipple between your fingers, your other hand drifts down between your legs."
    "Slipping two fingers into your folds, you slowly rub your clit, imagining Violet's face pressed between your legs."
    "Waves of pleasure crash over you as you rub your clit faster and harder, pinching your nipple and gasping for breath."
    "Releasing your nipple, you catch yourself against the side of the shower as your orgasm leaves you dizzy and breathless."
    "When you've recovered, you quickly wash up."
    pcname "At least that's convenient..."
    hide chelsea with moveoutright
    "Wrapping a towel around you, you step into the living room."
    show V SubCasual Blank at left with moveinright
    show bg HomeN with dissolve
    "Violet sits at the table, dressed, with a box of pizza in front of her."
    V "Sorry, I had to dress to answer the door."
    show chelsea laugh with dissolve
    "You laugh, but it gives you an idea..."
    show chelsea embarrassed
    if club == "track":
        "Maybe that's a little too much."
    elif club == "cheer":
        "What would the delivery guy think of {i}that{/i}."
    elif club == "yearbook":
        "You blush, imagining the delivery guy's face."
    V "Let me get you some pizza..."
    show chelsea blank
    "She has plates ready and carefully dishes out two slices for you."
    "You notice that she already has drinks and napkins laid out too."
    show V SubCasual Happy at left
    V "So... I just wanted to tell you that I really enjoyed lunch the other day. The... punishment."
    "As you eat, she explains herself."
    show V SubCasual Sad at left
    V "I... I know I'm a little too much sometimes, and people let me get away with {i}anything{/i}."
    V "So having someone hold me accountable... I don't know how to explain it."
    V "It's like... People just put up with whatever I do. Except you."
    show V SubCasual Blank at left
    show chelsea shocked
    V "You make me be better."
    "You're surprised by her honesty; so much that you're not sure what to say."
    show V SubCasual Happy at left
    show chelsea blank
    V "Anyway, I was thinking that maybe you should set some rules for me?"
    show V SubCasual Blank at left
    V "Just... expectations, I guess. So I know how you want me to behave."
    if club == "track":
        pcname "That sounds like a good idea."
    elif club == "cheer":
        pcname "I think we can do that..."
    elif club == "yearbook":
        pcname "I'll think about it..."
    "She looks around at the empty plates."
    V "Anyway, I really should get home now..."
    "She glances your way."
    show V SubCasual Worried at left
    V "If that's okay with you?"
    menu violetsub2_kiss:
        "Kiss her." if True:
            show chelsea embarrassed
            if club == "track":
                pcname "Not quite yet."
            elif club == "cheer":
                pcname "One last thing..."
            elif club == "yearbook":
                pcname "Um..."
            scene bg VSubKiss with dissolve
            "Leaning over, you grab her by the shoulders and pull her to you."
            "Her lips open beneath yours and she melts against you."
            "Your lips move slowly over each other as your tongues dance between them."
            "When you finally pull away, she sighs."
            show bg HomeN with dissolve
            show chelsea embarrassed with dissolve
            show V SubCasual Happy at left with dissolve
            V "Mmmm..."
            show chelsea happy
            pcname "Okay. You can go home now."
        "Make her clean up." if True:
            show chelsea happy
            if club == "track":
                pcname "Forgetting something?"
                "You motion to the empty plates."
            elif club == "cheer":
                pcname "Not with this mess!"
            elif club == "yearbook":
                pcname "What about all this?"
            show V Casual Annoyed at left
            V "Oh. Right..."
            "Lips curling in disgust, she slowly cleans up."
            pcname "Don't forget to wash the glasses too!"
            "She sighs, but turns on the sink and grabs a dishcloth."
            "After everything is clean, she turns toward you."
    show V SubCasual Happy at left
    V "This was fun. Please, think about those rules and... Maybe next time I can stay the night?"
    show chelsea happy
    pcname "Sounds like fun to me!"
    "Smiling, she lets herself out."
    hide V SubCasual Happy with dissolve
    $ acts = 0
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
