label violetdom7_music:
    scene bg RoomE

    $ clothes = "naked"
    show chelsea laugh with dissolve
    "As you sit up in bed and begin to stretch, you hear a knock at your door."
    if mattsubmissive:
        show chelsea blank
        "Your chest tightens a little; Matt's the only one who shows up unannounced."
        if defymatt:
            show chelsea sad
            "What a bad way to start your day."
        elif True:
            show chelsea embarrassed
            "What a way to start your day..."
    elif True:
        show chelsea confused
        pcname "Who could that be? Rent isn't due yet..."

    show chelsea blank
    $ clothes, hair = casualwear

    pause 0.3

    show chelsea at exitScene(0.5, 0.2, 0.4, 0.4)
    pause 0.2
    hide chelsea
    hide bg RoomE
    show bg HomeE
    with fade
    show chelsea with dissolve
    "Walking to the door, you peek through the peephole."
    show chelsea happy
    "It's... Violet!"
    if mattsubmissive:
        if defymatt:
            show chelsea blank
            "Sighing with relief, you quickly open the door."
        elif True:
            show chelsea sad
            "For a moment, you feel conflicted."
            "You're not disappointed; you {i}like{/i} spending time with Violet..."
            show chelsea embarrassed
            "In a lot of ways, they're similar. Both like to be in control - to tell you what to do."
            "But at the same time, they're {i}so{/i} different."
            show chelsea happy
            "You {i}deserve{/i} Matt. But Violet..."
            show chelsea shocked
            "Another knock startles you from your thoughts."
    show chelsea embarrassed
    pcname "Sorry, Mistress."
    show V Casual Pout at right, enterScene(1.5, 1.0, 0.5, 0.6)
    "As the door swings open, Violet pushes her way inside."
    show chelsea shocked
    show V Casual Smile
    V "Put this on and get dressed; we're going shopping."
    "She pushes a box into your hands as she motions for you to get ready."
    show chelsea confused
    if club == "track":
        "Brows furrowing, you yank the box open."
    elif club == "cheer":
        "With a quizzical look at Violet, you open the box with a smile."
    elif club == "yearbook":
        "Brows furrowing, you carefully open the box."
    show chelsea sad
    show V Casual Pout
    "Inside is a smooth, purple, u-shaped... {i}Thing{/i}."
    if club == "track":
        pcname "It's, um...?"
    elif club == "cheer":
        pcname "That looks like... A, um...?"
    elif club == "yearbook":
        pcname "It... It's...?"
    show V Casual Blank
    V "You've never seen one, have you?"
    show chelsea shocked
    show V Casual Pout
    "Sighing, she picks it up and, making a scooping motion with one side of the U, waves it in your face."
    show V Casual Smile
    V "This side goes {i}inside{/i} of you, and {i}this{/i} goes against your clit. Get it?"
    show chelsea embarrassed
    if club == "track":
        "You grin."
        pcname "Yeah, I get it."
    elif club == "cheer":
        "A slow smile spreads across your face."
        pcname "Oh, I get it..."
    elif club == "yearbook":
        "You swallow hard."
        pcname "Y-yeah, I get it..."
    show V Casual Blank
    V "Well, what are you waiting for then?"
    show chelsea at exitScene(0.5, 0.0, 0.3, 0.3)
    show V Casual Pout
    "Hurrying into your bedroom, you undress and grab the device."
    $ clothes = "naked"
    scene bg RoomE with dissolve
    show chelsea with dissolve
    "There's a small bottle of lubricant in the package beneath it."
    "Taking a moment, you lightly lubricate one half of the device."
    show chelsea embarrassed
    "You position it against your opening; its cold, hard exterior makes you shiver as you push it inside."
    if club == "track":
        pcname "Oh fuck..."
    elif club == "cheer":
        pcname "Ohhh~"
    elif club == "yearbook":
        pcname "Ah!"
    scene black with dissolve


    "It settles in place, half inside of you, half wrapping around to cradle your clit."
    "As you dress, you feel it shifting inside of you, rubbing gently against your g-spot."
    "Though you weren't wet when you inserted it, you notice yourself growing warm and aroused as the device shifts inside of you."
    "By the time you're finished dressing, you feel warm and... sensitive."
    "Your nipples have begun hardening; you can feel them dragging against the lace of your bra as you move."
    "It's strange to think that so little contact could make you so {i}aware{/i} of your own body."
    V "Are you ready yet?"
    pcname "Yes, Mistress. I'm coming."
    "Violet chuckles at your phrasing, and you feel your cheeks warming."
    "Tossing you the keys, Violet waits for you to open the door for her."
    $ clothes, hair = casualwear
    scene bg HomeE with dissolve
    show chelsea at right with dissolve
    show V Casual Pout at midright with dissolve
    "Following her downstairs, you try to focus on her words, but the shifting of the device with each step is too distracting."
    scene bg CityE with dissolve
    show chelsea at midright with dissolve
    show V Casual Pout at right with dissolve
    pause 0.7
    hide V Casual with dissolve
    hide chelsea with dissolve
    scene black with dissolve
    "After helping Violet into the back seat, you slide into the driver's seat and check the GPS."
    show V Casual Blank with dissolve
    V "It's set for the mall. Let's go."
    hide V Casual with dissolve
    show chelsea embarrassed at right with dissolve
    $ acts -= 1
    pcname "Yes, Mistress."
    hide chelsea with dissolve
    "As you shift the car into reverse, you check the rearview and see Violet on her phone."
    V "Let's see... What song should we play..."
    "Shifting the car into drive, you ease toward the road and put your turn signal on."
    "As you pull onto the road, a pop song starts playing over the speakers."
    "Immediately, the device inside of you pulses along to the beat."
    scene black with dissolve

    if club == "track":
        pcname "What the--"
    elif club == "cheer":
        pcname "Oh~"
    elif club == "yearbook":
        pcname "Ah!"
    "As the beat picks up, it vibrates inside of you and against your clit, in time with the music."
    V "Do you like that? I thought it looked like fun..."
    if club == "track":
        pcname "It's... different..."
    elif club == "cheer":
        pcname "It's... nice..."
    elif club == "yearbook":
        pcname "I-I wasn't... expecting it..."
    "Violet laughs, her eyes meeting yours in the rearview mirror."
    V "What should we play next..."
    "As the first song ends, the pulsing fades."
    "For several seconds you wait, holding your breath in anticipation for the next song."
    "It starts suddenly, with a long, low thrum."
    "The song is bass-heavy, leading to long, intense vibrations, but at a slower tempo than the last song."

    "At first, each vibration makes you shudder a little, but by the time you're halfway through the song, the steady rhythm has lost its impact."
    "There's still something about the device thumping in time with the music that bespells your senses, but you find yourself adjusting to it."
    "As the song ends - on one last, powerful bass note that thunders through you - you let out a quavering sigh."
    V "Are you enjoying this?"
    pcname "Yes, Mistress, I--"
    "Before you can finish your sentence, the next song starts pounding through the speakers."
    "It's a popular club song - fast and bouncy - and you know you've heard it before."
    "{i}Bv bv bv bv bvvvv... Bvv bvv... Bv bv bv bv bvvvv...{/i}"
    "The rhythm is strong, almost erratic; you gasp, smothering a moan as it pulses, alternating between your clit and g-spot."
    "As the song continues, you feel your control slipping - and then you remember the bass drop."
    "A moan escapes your lips - part pleasure, part dread."

    V "I think I found your favorite song."
    "The bass slows to a faint echo of itself, the device barely pulsing before stopping for a full second, and then..."
    "{i}BV BV BV BV BVVVV...{/i}"
    if club == "track":
        pcname "Oh fuck!"
    elif club == "cheer":
        pcname "Ohh~"
    elif club == "yearbook":
        pcname "Ah! Ah~"
    "Shuddering, you force your eyes open as the beat blasts through you, rumbling against your clit and g-spot."
    pcname "V-Violet, I can't..."
    V "Ah, ah... {i}Mistress{/i}."
    pcname "Ahh~"
    "Panting for breath, you grip the wheel hard."

    "The pulsing, bouncing beat and deep, thundering bass wash you in sensations, bringing you close to the edge."
    "Then, just as you begin to wonder how you're going to drive while cumming, the song ends in a final blast of bass."
    V "Well, that sounded fun... Wanna hear it again?"
    "Your eyes widen and you begin shaking your head when--"
    "{i}Bv bv bv bv bvvvv... Bvv bvv...{/i}"
    "Your breath catches in your throat. Your clit still throbs from the first time through this song."
    "Abs tightening, your pussy clenches around the device, pressing it harder against your insides."

    "Through the growing fog of pleasure, you try to speak:"
    if club == "track":
        pcname "Oh, fuck... Fuck..."
    elif club == "cheer":
        pcname "M-mistress, I..."
    elif club == "yearbook":
        pcname "Oh... Oh, I... I..."
    pcname "I can't... I can't..."
    "Again, the bass fades before:"
    "{i}BV BV BV BV BVVVV...{/i}"
    pcname "AH~"
    "The heavy beat rocks your body, rumbling against your clit and sending waves of pleasure through your tight, clenching cunt."
    "A low moan escapes your throat as you struggle to keep your eyes focused on the road ahead."
    "Gasping, panting, you moan over and over, almost dazed with pleasure."
    "So close... So close..."

    "And then the song ends."
    "As you catch your breath, you realize that you're practically at the mall already."
    V "Park by that door there."
    "Shuddering, your body still echoing the song's beat, you turn into the parking lot and find a spot to park."
    scene bg CityE with dissolve
    show chelsea at midright with dissolve
    "Your legs feel weak and heavy as you get out of the car; for a moment, you wonder if they'll support you at all."
    show V Casual Smile at right with dissolve
    "Violet smiles up at you as you open the door for her."
    V "Did you enjoy that?"
    if club == "track":
        pcname "Fuck... Yes, Mistress."
    elif club == "cheer":
        pcname "Yes, Mistress. It was... Incredible."
    elif club == "yearbook":
        pcname "Y-yes, Mistress, but... It was hard to drive..."
    show V Casual Pout at exitScene(1.0, 0.5, 0.4, 0.4)
    "Chuckling, Violet steps past you, walking towards the mall."
    show chelsea at exitScene(0.7, 0.2, 0.4, 0.4)
    "Now more than ever, you're highly aware of the device inside of you."
    scene bg Shop with dissolve
    show chelsea at midright with dissolve
    show V Casual Pout with dissolve
    "As you follow Violet - carrying her bags and holding doors for her - your clit throbs against the device."
    show chelsea sad
    "Though it's not vibrating, the presence of the device is just enough to keep you on edge for the next hour."
    show chelsea blank
    "Slowly, though, you start to forget about it."
    show chelsea happy
    if club == "track":
        "As you follow Violet, a store catches your gaze."
        show chelsea laugh
        "It's a popular shoe store, the shelves full of the best athletic shoes you've ever seen."
        show V Casual Suprised
        "Brands that, until now, you'd only heard of."
    elif club == "cheer":
        "As you follow Violet, a store catches your eye."
        "It's an accessory store, and the brands you see are {i}expensive{/i}."
        show chelsea sad
        "The purses look gorgeous, but you know they must cost a fortune."
        show V Casual Suprised
        "You could easily spend several paychecks on just one item there."
    elif club == "yearbook":
        "As you follow Violet, a store catches your eye."
        show chelsea laugh
        "A whole display of cameras and accessories fill the window."
        show V Casual Suprised
        "Inside, you see even more accessories. Straps, bags, lenses..."
    show V Casual Smile
    "Violet catches the direction of your gaze, and a slow smile spreads over her face."
    show chelsea shocked
    V "I want to go in this one."
    show chelsea at exitScene(0.7, 0.2, 0.3, 0.3)
    show V Casual at exitScene(0.5, 0.0, 0.3, 0.3)
    "She leads you into the very store you'd been looking at."
    scene bg Shop with fade
    show chelsea at left with dissolve
    if club == "track":
        show chelsea happy
        "Almost without thinking, you approach the racks and pick up a pair of running shoes."
        "They're amazing, with lots of cushioning foam and a carbon-fiber plate."
        show chelsea sad
        "But the price tag... $250."
        "Regretfully, you set them back on the shelf."
        show chelsea shocked
        show V Casual Blank with dissolve
        V "Isn't that your size?"
        show chelsea sad
        show V Casual Pout
        pcname "Oh, yeah, but... I can't afford those."
        show chelsea shocked
        "Violet reaches out, grabbing the box from the shelf."
        show chelsea sad
        show V Casual Smile
        V "I can."
        show V Casual Pout
        "Your stomach drops."
        pcname "No, I... I wouldn't feel right..."
        show chelsea shocked
        show V Casual Smile
        "She gives you an amused smile."
        show chelsea embarrassed
        V "No? Did I ask?"
        show V Casual Pout
        "Swallowing hard, you shake your head."
        pcname "No, Mistress..."
        show V Casual Smile
        V "Good. Then follow me."
        scene bg Shop with fade
        show GFDoctor at right with dissolve
        show V Casual Pout at midright with dissolve
        show chelsea with dissolve
        "She strolls up to the cashier, dropping the box onto the counter."
        show V Casual Blank
        "The cashier chats with her as she rings up the shoes. Violet runs her card and tucks it into her purse, motioning for you to take the bag."
        scene bg Shop with fade
        show V Casual Pout at left with dissolve
        show chelsea shocked with dissolve
        "As you leave the store, you stare down at the bag, barely believing what just happened."
        show chelsea sad
        pcname "Mistress, I..."
        show chelsea embarrassed
        show V Casual Smile
        V "It's a gift. For being such a {i}good{/i} girl for me."
        "Her words make your heart skip a beat. Though you know it probably means a lot less to her, you can't help feeling touched by the gift."
        "It's rare that Violet is so thoughtful."
    elif club == "cheer":
        "You're not surprised; Violet probably buys all of her accessories here."
        show V Casual Pout with dissolve
        "She picks up a pair of sunglasses, turning them over in her hand."
        show chelsea happy
        "While she examines them, you look over the racks, your eyes stopping on a chic purse."
        "You find yourself lifting it, running your fingers over the soft leather exterior."
        show chelsea sad
        "It's amazing, but one glance at the price tag - $750 - and you shove it back onto the shelf."
        show chelsea embarrassed
        show V Casual Blank
        V "That would look cute on you."
        show chelsea sad
        show V Casual Pout
        "Smiling weakly, you shake your head."
        pcname "I {i}wish{/i}. I can't afford anything in here."
        show chelsea happy
        show V Casual Smile
        V "I can."
        show chelsea embarrassed
        "Your heart thumps against your ribs."
        show chelsea sad
        show V Casual Pout
        pcname "No, I couldn't ask you to..."
        "She gives you an amused smile."
        show chelsea shocked
        show V Casual Smile
        V "No? Did I ask if I could?"
        show chelsea embarrassed
        show V Casual Pout
        "Swallowing hard, you shake your head."
        pcname "No, Mistress..."
        show V Casual Blank
        V "Good. Then follow me."
        scene bg Shop with fade
        show GFDoctor at right with dissolve
        show V Casual Pout at midright with dissolve
        show chelsea with dissolve
        "She strolls up to the cashier, dropping the bag onto the counter."
        show V Casual Blank
        "The cashier chats with her as she rings up the handbag. Violet runs her card and tucks it into her purse, motioning for you to take the bag."
        hide chelsea with dissolve
        hide V Casual with dissolve
        hide GFDoctor with dissolve
        scene bg Shop with fade
        show V Casual Pout at left with dissolve
        show chelsea shocked with dissolve
        "As you leave the store, you stare down at the bag, barely believing what just happened."
        pcname "Mistress, you shouldn't have..."
        show chelsea happy
        show V Casual Smile
        V "It's a gift. For being such a {i}good{/i} girl for me."
        show chelsea embarrassed
        "Her words make your heart skip a beat. Though you know it probably means a lot less to her, you can't help feeling touched by the gift."
        "It's rare that Violet is so thoughtful."
    elif club == "yearbook":
        "As soon as you enter, your eyes search for your camera brand."
        "Drifting towards it, you look over the lenses."
        show chelsea happy
        "There, a set of fast prime lenses catches your eye. It comes with three lenses of different focal lengths: 24mm, 50mm, and 80mm."
        show chelsea sad
        "As you reach out to look at it, your eyes catch the price tag and your fingers fall."
        "$650"
        show chelsea shocked
        show V Casual Blank with dissolve
        V "Is that the kind you use? I don't know anything about cameras."
        show chelsea sad
        show V Casual Pout
        pcname "Oh, yeah, but..."
        show chelsea shocked
        "She reaches out, grabbing the set of lenses you were just reaching for."
        show chelsea embarrassed
        show V Casual Blank
        V "So you'd like these?"
        show V Casual Pout
        "Your heart thumps against your ribs."
        show chelsea sad
        pcname "No! I mean, yes, but..."
        "She gives you an amused smile."
        show chelsea embarrassed
        show V Casual Smile
        V "So you can use these?"
        show chelsea sad
        show V Casual Pout
        "Swallowing hard, you shake your head."
        pcname "Y-yes, Mistress, but..."
        show chelsea shocked
        show V Casual Smile
        V "Good. Then follow me."
        scene bg Shop with fade
        show GFDoctor at right with dissolve
        show V Casual Pout at midright with dissolve
        show chelsea embarrassed with dissolve
        "She strolls up to the cashier, casually placing the box on the counter."
        show V Casual Blank
        "The cashier chats with her as she rings up the lenses. Violet runs her card and tucks it into her purse, motioning for you to take the bag."
        hide GFDoctor with dissolve
        hide V Casual with dissolve
        hide chelsea with dissolve
        scene bg Shop with fade
        show V Casual Pout at left with dissolve
        show chelsea sad with dissolve
        "As you leave the store, you stare down at the bag, barely believing what just happened."
        pcname "Mistress, you shouldn't have..."
        show chelsea shocked
        show V Casual Smile
        V "It's a gift. For being such a {i}good{/i} girl for me."
        show chelsea embarrassed
        "Her words make your heart skip a beat. Though you know it probably means a lot less to her, you can't help feeling touched by the gift."
        "It's rare that Violet is so thoughtful."
    scene black with dissolve
    "You follow her through the rest of the mall, giddy with excitement over your gift."
    "Violet picks up a few more things, each time motioning for you to take her bags, before leading you out of the mall."
    "You help her into the car and stack all of the bags in the trunk."
    "Taking your place in the driver's seat, you put your bag on the seat next to you."
    "You back out of the parking space and navigate your way out of the parking lot."
    "As you turn onto the road, a familiar song begins playing."
    "Immediately, the device - nearly forgotten - comes to life inside of you."
    "{i}Bv bv bv bv bvvvv... Bvv bvv...{/i}"
    pcname "Ah~"

    "Your pussy tightens around the device, clamping hard. Your pulse quickens as you wait for the bass drop."
    "{i}BV BV BV BV BVVVV...{/i}"
    if club == "track":
        pcname "Oh fuck..."
    elif club == "cheer":
        pcname "Oh god..."
    elif club == "yearbook":
        pcname "O-oh..."
    "The vibrators pulse in time with the bass, edging you closer to your climax."

    "Just as the sensation builds - a wave of pleasure flooding over you - the song ends."
    "Almost immediately, it begins again."
    V "Since you like it so much, I thought I'd put it on repeat."
    V "Should I turn the volume up?"
    "As she speaks, she taps her phone and the volume gets louder. And so do the vibrations."
    "{i}Bv bv bv bv bvvvv... Bvv bvv...{/i}"
    "Jolts of pleasure surge from your clit as the device rumbles against it."
    "Inside of you, your cunt clenches the hard plastic. Each vibration sends another wave of pleasure crashing over you."

    if club == "track":
        pcname "Oh fuck... Oh fuck... Oh~"
    elif club == "cheer":
        pcname "Oh my god... oh my god... Oh god~"
    elif club == "yearbook":
        pcname "Oh... oh... oh~"
    "The bass drops again and you cry out in pleasure."
    "Gasping, panting, you grip the wheel hard and fight to keep your eyes on the road."
    "As the song ends, you sigh in relief - and then it starts again, even louder."
    pcname "M-mistress, please, I can't..."
    pcname "I can't... It's too much..."
    "Panic builds as the song continues. The bass drop is coming. You won't be able to-"

    "The bass reverberates in time with the vibrators - it feels almost as if the vibrators are pressed against your whole body."
    "Your pussy clamps down on the hard plastic, the tightening muscles making the vibration even stronger."
    "Your clit - at once numb and aching - throbs almost painfully with every thumping beat."
    "As the song ends again, you pant hard, trying desperately to catch your breath."
    "Listening anxiously, you wait for the song to start again."
    V "Don't miss your turn."
    "Glancing about, you realize you're home."
    "Turning into the parking lot, you swing into a space and shift the car into park."
    "Inhaling deeply, you let out a long, shaky breath."
    V "How are you feeling?"
    if club == "track":
        pcname "Really fucking horny..."
    elif club == "cheer":
        pcname "I'm {i}so{/i} horny..."
    elif club == "yearbook":
        pcname "I... I'm really..."
        V "Really what?"
        pcname "H-horny...?"
    "She giggles and your chest tightens at the sound."
    V "I think I can help with that. Open my door."
    scene black with dissolve
    "Scrambling to obey, you grab your bag from the passenger's seat and rush to her door."
    "Violet leads you up to your apartment, acting as if she owns the place."
    "Once inside, she turns and motions toward you."
    scene bg RoomE with dissolve
    show V Casual Blank with dissolve
    show chelsea at midright with dissolve
    V "Well? Strip."
    $ clothes = "naked"
    show V Casual Smile
    if club == "track":
        "Eagerly, you pull your clothes off, tossing them aside."
    elif club == "cheer":
        "Smiling, you watch her reaction as you pull your clothes off, dropping them to the floor."
    elif club == "yearbook":
        "For once, you feel no shame as you strip your clothes off, baring yourself for her."
    scene black with dissolve

    "Standing naked before her, you watch her eyes travelling over your skin."
    V "Now... Get on your knees and beg me to let you cum."
    menu violetdom7_music_beg:
        "Beg for mercy." if True:
            "Dropping to your knees, you look up at her with large, pleading eyes."

            pcname "Please, Mistress. I want to cum so bad..."
            "She looks unmoved, so you continue."
            pcname "I tried to be good for you today. I carried the bags and opened the doors..."
            pcname "And I... I drove you around even though I could barely... barely control myself when..."
            "You shudder - even though the device is still inside of you, you can almost feel the beat anyway."
            "Again, Violet smiles and you feel something inside of you melt."
        "Kiss her feet." if True:
            "Dropping to your knees, you crawl to her feet."
            "Leaning down, you press your lips to the skin just above her black heels."

            pcname "Please, Mistress..."
            "You trail kisses over one foot, then the other."
            pcname "I want to cum so bad..."
            "Smirking, she lifts her foot so you can kiss the tip of her shoe."
            "As you do, her smirk fades to a pleased smile - and something inside of you melts."
    V "Okay, I think you deserve some relief."
    V "Touch yourself."
    "Immediately, your hands drop to your breasts, groping them boldly."

    "Your nipples - already hard, stiff peaks - throb almost painfully as you twist them between your fingers."
    pcname "Ha~"
    "Panting, you massage your breasts, your fingers twisting and pulling at your nipples, your--"
    "{i}Bv bv bv bv bvvvv... Bvv bvv...{/i}"
    "You moan as the device jolts to life, the song playing over her phone louder than ever."

    V "Look at me. I want to see you cum."
    "Quivering, you force your eyes open, shuddering as Violet smiles down at you."
    V "That's good. Just a little bit longer..."
    "The song stretches towards the bass drop, the rhythm building a little before falling off. And then... and then..."
    "{i}BV BV BV BV BVVVV...{/i}"

    "It's more than you can take. Jolts of pleasure shoot out from your clit, while your pussy spasms around the toy, clenching it tightly."

    "Gasping and shuddering, you force yourself to meet her eyes as you cum."
    "Her smile widens; her tongue darts over her lips as she leans toward you."
    "Your orgasm fades as the song ends and you sink to the floor, suddenly heavy and exhausted."
    V "That was {i}very{/i} nice..."
    "Leaning down, Violet hooks her finger between the bottom of the device and your skin."
    "Pulling - gently but firmly - she tugs the toy from your pussy, leaving it empty."
    "Her lips brush your ear, and she whispers:"
    V "I'll never be able to listen to that song again without thinking of this..."
    "Another shiver of pleasure runs over you as she stands, tucking the toy into the box and slipping it into her purse."
    "She lets herself out, leaving you naked on the floor, a trail of your own juices running down your thighs."
    $ clothes, hair = casualwear
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
