label violetsub4_violethouse:
    $ clothes, hair = casualwear
    scene bg CityE
    show V SubCasual Sad at right
    show chelsea at left, enterScene(-0.3, 0.0, 0.3, 0.3)
    "As soon as you step out of the building, you see Violet waiting beside her car."
    show V SubCasual Happy
    V "I hope work went well, [domtitle]."
    pause 0.5
    show chelsea at exitScene(0.0, 0.5, 0.45, 0.45)
    show V SubCasual Worried
    "Nodding, you get into the car."
    hide V SubCasual with dissolve
    pause 0.5
    scene bg VioletHouseE with dissolve
    "Violet drives you to her house, stopping briefly at the gate."
    show chelsea confused with dissolve
    pcname "Is something wrong?"
    hide chelsea with dissolve
    show V SubCasual Blank at right with dissolve
    V "There's a sensor up here, [domtitle]."
    "She points to a small round piece of plastic attached to the windshield just behind the rearview mirror."
    show V SubCasual Sad
    V "If you don't have one, you have to hit that button there and security will buzz you in."
    "As she speaks, the gate swings open."
    hide V SubCasual with dissolve
    "Of course Violet's house would have something like this; you're not sure why you were surprised."
    show GHCMan with dissolve
    "Violet parks the car in front of the house, where a man rushes to open her door."
    show V Casual Pout at right with dissolve
    "Before she has a chance, he opens your door too."
    show chelsea at left with dissolve
    "Driver" "There you are, miss."
    hide GHCMan with dissolve
    "Violet passes him the keys and leads you toward the house, speaking softly."
    hide V Casual
    show V SubCasual Sad at right
    V "Follow me, [domtitle]."
    scene bg LuxParty with fade
    "As you reach the front door, it swings open."
    show GHCMan at midright with dissolve
    show V Casual Pout with dissolve
    show chelsea at left with dissolve
    "Butler" "Hello, Miss Violet. Your parents are home. Will you be joining them in the family room?"
    "You glance at Violet, waiting to see how she'll respond."
    "Her nose wrinkles."
    show V Casual Blank
    V "No, I don't think so. We're going to my rooms."
    show chelsea happy
    hide V Casual
    show V SubCasual Happy
    "Violet smiles at you, urging you further inside."
    "You barely have time to take in the entryway before she leads you past a grand piano and into the next room."
    show GCGirl at right with dissolve
    "Woman" "Violet, darling, you didn't tell me you were bringing a friend home."
    show V Casual Suprised with dissolve
    "You watch as Violet freezes in her tracks, turning slowly to face you."
    show V SubCasual Worried
    V "Sorry, mother. We ran into each other while I was out and I invited her back to study."
    show chelsea shocked at left with dissolve
    show V SubCasual Sad
    "Violet's eyes find yours, urging you to agree. Turning, you see a gorgeous, dark-haired woman standing with a glass of wine."
    show chelsea blank
    hide V SubCasual
    show V Casual Pout
    "Woman" "Well? Aren't you going to introduce us?"
    show V Casual Blank
    V "I was just about to, naturally."
    show chelsea happy
    V "Mother, this is my classmate [pcname]. [pcname], this is my mother, Rose Atwood."
    show chelsea laugh
    show V Casual Pout
    "She smiles."
    show chelsea sad
    show V Casual Suprised
    "Rose" "Please, just Rose. What does your family do, [pcname]?"
    show chelsea embarrassed
    hide V Casual
    show V SubCasual Sad
    if club == "track":
        pcname "Um, well... Nothing, I guess. They died."
    elif club == "cheer":
        pcname "Oh, I... I don't really have any family left."
    elif club == "yearbook":
        pcname "O-oh, um... Th-they're gone, so..."
    hide V SubCasual
    show V Casual Annoyed
    V "She's an orphan. Car accident. Very sad."
    "Her mother's eyes widen in surprise."
    show chelsea blank
    "Rose" "Oh dear, I had no idea. I'm so sorry."
    hide V Casual Annoyed
    show V SubCasual Worried
    "You shrug, not missing the pointed look she shoots in Violet's direction."
    show chelsea happy
    show V SubCasual Happy
    V "Anyway, we have a lot of studying to get done!"
    show chelsea blank
    hide V SubCasual
    show V Casual Annoyed
    "Rose" "Now, darling, don't be rude. You should introduce her to your father as well."
    "Violet's mother turns to you, beckoning you to follow."
    show chelsea confused
    "Rose" "Come, dear. Marshall will be happy to see Violet making some... public school friends."
    hide GCGirl with dissolve
    "You glance back at Violet, startled by her mother's commanding presence and Violet's clear unhappiness with the situation."
    show chelsea blank
    show V SubCasual Sad
    "Her eyes meet yours, begging your forgiveness."
    "Her mother leads you through the living room, past the dining room, and into - another? - living room."
    scene bg LuxParty with fade
    show GCGirl at midright with dissolve
    show chelsea with dissolve
    show V Casual Pout at left with dissolve
    "Rose" "Here's the family room."
    show chelsea happy
    "She gestures ahead of her, indicating the second living room."
    "Rose" "Marshall, we have a guest."
    show GHCMan at right with dissolve
    "A middle aged man with short black hair and reading glasses sits with a tablet."
    show chelsea blank
    "He glances up at you quickly, then looks back at the tablet."
    show chelsea shocked
    "After a moment, his eyes dart back up and he really looks at you."
    show V Casual Annoyed
    "{i}Really{/i} looks at you."
    show chelsea embarrassed
    "His eyes run down your body - from your hair, to your feet, and back up again."
    "With his wife and daughter standing on either side of you, you flush under his gaze."
    show V Casual Pout
    "Marshall" "And who is this?"
    show chelsea happy
    "Rose" "This is Violet's friend. From the public school."
    "Marshall" "Well, glad to hear it."
    show chelsea blank
    hide GHCMan with dissolve
    "And with that, he goes back to his tablet."
    "Rose smiles and turns to Violet."
    show V Casual Annoyed
    "Rose" "Don't forget that I have a fundraiser tomorrow, dear. You'll be helping me get set up, won't you?"
    show V Casual Blank
    "Violet sighs."
    show chelsea laugh
    hide V Casual
    show V SubCasual Happy at left
    V "Yes, mother."
    hide V SubCasual
    show V Casual Smile at left
    "Rose" "Don't say it so dramatically, dear."
    show chelsea embarrassed
    "She gives you a long-suffering smile, as if to say \"do you see what I deal with?\", before turning back to Violet."
    "Rose" "Well, I won't keep you. Go study, you two!"
    show chelsea blank
    show V Casual Pout
    V "Great. Thanks. Let's go, [pcname]."
    hide V Casual with dissolve
    menu violetsub5_parents:
        "It was nice to meet you." if True:
            if club == "track":
                show chelsea embarrassed
                pcname "It was nice to meet you guys."
                show chelsea sad
                "Violet's mother smiles uncomfortably."
                "Rose" "And you as well."
            elif club == "cheer":
                show chelsea laugh
                pcname "It was nice meeting you. You have a beautiful home."
                show chelsea embarrassed
                "Violet's mother smiles graciously."
                "Rose" "And you as well, dear."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I-it was nice... meeting you..."
                "Violet's mother smiles patiently."
                "Rose" "Of course. It was nice to meet you too, dear."
        "(Stay silent)" if True:
            "Waving awkwardly at her parents, you follow Violet out of the room."
    scene black with fade
    "Violet leads you out of the family room, through the living room, and back to the - foyer?"
    "Passing the grand piano, she leads you up a large staircase and along a balcony overlooking the living room."
    show V SubCasual Sad at center, enterScene(0.7, 0.5, 0.35, 0.35)
    V "My rooms are right down here..."
    show V SubCasual Blank at center, exitScene(0.5, 0.0, 0.30, 0.30)
    "Passing several closed doors, she comes to a stop and motions for you to open one of them."
    scene bg LuxParty with fade
    "You hurry to obey. Swinging the door open, you see... Another living room? What?"
    "Looking about, you barely notice Violet clicking the lock in place."
    show V SubCasual Worried at right with dissolve
    V "This is my sitting room, but I don't use it much."
    scene bg VioletBedroom with dissolve
    "She leads you past a small sitting area - outfitted with a sofa, chair, and coffee table - through a doorway, and into her bedroom."
    "Her bedroom is at least as big as your living room, and through the doors on the sides you see a large bathroom and a large walk-in closet."
    "Her \"rooms\" are easily the size of your entire apartment."
    show V Casual Pout
    with fade
    "Violet doesn't seem to notice your surprise, though."
    show V Casual Blank
    V "Now that {i}that's{/i} over with..."
    show V Casual Pout
    "She pauses, biting her lip."
    show V SubCasual Sad
    V "I... I had something for you..."
    "Her sudden timidity amuses you."
    show V SubCasual Worried
    show chelsea laugh at right with dissolve
    pcname "Well? Where is it?"
    show chelsea embarrassed
    hide V SubCasual with dissolve
    "Given permission, Violet steps into her walk-in closet to retrieve a small box."
    show V SubCasual Blank at left with dissolve
    "Removing the top, she holds it out to you."
    show chelsea confused
    "Inside are a pair of fur-lined cuffs, a leather flogger, and a feather teaser."
    show V SubCasual Sad
    pcname "And what are these for?"
    show chelsea blank
    show V SubCasual Worried
    V "I... I was hoping you would want to... Use them, [domtitle]."
    "Seeing her flustered is enough to bring a smile to your lips, but you keep your expression stern."
    pcname "I see."
    show V SubCasual Sad
    "Lifting the cuffs, you wave them in the air."
    show chelsea happy
    show V SubCasual Worried
    pcname "I guess you should undress and get on the bed then, hmm?"
    show chelsea blank
    "Swallowing hard, Violet nods."
    scene black with dissolve
    "Shedding her clothes in a hurry, she leads you to the bed. There, you can see several straps running under the bed."
    "The cuffs fasten around her wrists before hooking onto the straps."
    "When she's cuffed and fastened to the bed, her arms and legs are spread and pulled."
    show bg VSubBedroom1 with dissolve
    "Smiling, you look her body up and down before glancing back at the box."
    "It's a nice gift, but she {i}did{/i} get it without consulting you."
    "You could reward her for pleasing you - or punish her for making the decision without you."
    menu violetsub4_violethouse_react:
        "Reward her." if True:
            "Taking the feather teaser from the box, you hold it up so she can see it."
            "She sighs, though it's hard to tell whether she's relieved or disappointed."
            show bg VSubBedroom2 with dissolve

            "Approaching the bed, you hold the teaser above her, letting it drift up and down her body without quite touching her."
            "Her breathing comes in sharp, broken hisses as she anticipates sensations that never come."
            V "Ha-- Ah-- Mn!"
            "Eventually, you allow the feathers to brush the curve of her breast, drawing another sudden gasp."
            show bg VSubBedroom3 with dissolve

            "You spend a few minutes teasing her with the feathers, letting them brush her breasts and belly, trailing them over her pussy."
            "Slowly, her nipples darken, drawing up into stiff points."
            "Her labia grows plump and full, lightly glistening with moisture."
            "Her clit swells, peeking out from the folds of her pussy, demanding attention."
            "Panting, she twists beneath the feathers, savoring the sensation but desperate for more."
            "Lifting the teaser, you smile down at her."
            show bg VSubBedroom4 with dissolve
        "Punish her." if True:

            "You lift the flogger, holding it high enough for her to see."
            show bg VSubBedroom5 with dissolve

            "You're rewarded with a sharply drawn breath, though it's hard to tell whether her reaction stems from anticipation or fear."
            V "But-- But what did I...?"
            "Slapping the leather into your palm, you smile."
            pcname "Don't get me wrong; I'm very pleased with these."
            "You hold the flogger out, letting the strips of leather dance over her belly."
            pcname "But you didn't ask, did you? You didn't consult me at all."
            "You raise the flogger, shaking your head."
            pcname "You forgot who makes the decisions here. So now I have to remind you."
            "Bringing the flogger down - lightly, to start - you listen to the tiny, satisfying snaps it makes as the straps make contact with her flesh."
            show bg VSubBedroom6 with dissolve

            "Violet gasps, more surprised than pained."
            "You bring the flogger down again, this time catching her breast."
            "Again, striking the other breast."
            "Again over her belly."
            "Her thighs."
            "Her breasts."
            "The soft, sensitive mound of her pussy."
            V "Ahh!"
            "You pause, letting her catch her breath."
            show bg VSubBedroom7 with dissolve

            pcname "Do you have something you'd like to say?"
            "Her eyes widen and she nods."
            if violetcum > 2:
                V "Yes! I'm sorry, [domtitle]. I won't forget again!"
                "You smile down at her."
                pcname "Very good, Violet."
                "You lift the flogger again."
                pcname "But I think we should make sure the lesson sticks."
            elif True:
                V "Yes! I didn't mean to upset you, [pcname]."
                "You shake your head."
                pcname "I'm not upset, Violet. I'm disappointed."
                "You lift the flogger again."
                pcname "And it's [domtitle]."
            "Over and over, you flog her - occasionally pausing, running the strips soothingly over her skin, to let her recover."
            "Her nipples harden, straining toward you. Her labia sparkles with moisture, her clit peeking from the folds."
            show bg VSubBedroom8 with dissolve

            pcname "I think you're enjoying this. Did you learn your lesson?"
            "She nods, her breathing jagged and irregular."
            V "I won't make decisions without asking, [domtitle]. I promise!"
    "Nodding, you lower your hand, letting the toy fall to the floor."
    "Your own nipples strain against the fabric of your shirt."
    "Beneath your clothes, your panties are damp and hot."
    "Even your lips feel different - puffy and smooth, swollen with desire."
    if club == "track":
        pcname "I'm not finished with you yet..."
    elif club == "cheer":
        pcname "I don't think I'm done with you yet..."
    elif club == "yearbook":
        pcname "Well I... I'm not done yet..."
    "Violet watches from the bed, her eyes wide, as you quickly strip off your own clothes."
    "Climbing onto the bed, you crawl over her, pausing to lick a nipple along the way."
    "Grabbing the headboard, you straddle her face, holding your pussy just above her lips."
    show bg VSubBedroom9 with dissolve

    if club == "track":
        pcname "Well? You know what to do."
    elif club == "cheer":
        pcname "Well? Don't you want your reward?"
    elif club == "yearbook":
        pcname "W-well?"
    "Her eyes drift half-shut as she tilts her head back, lifting her mouth to meet you."
    show bg VSubBedroom10 with dissolve

    "Her tongue darts out, slipping between your labia."
    "She lets it run up and down your cunt, gently exploring."
    "It feels good, but you're too aroused; it's not enough."
    "Lowering your pussy, you press it to her mouth."
    show bg VSubBedroom11 with dissolve

    "Her eyes widen as you rock her hips."
    pcname "Use your tongue."
    V "Mmm mmmhm."
    "Her words are lost, but she does as you tell her, pressing her tongue into your pussy."
    "The hot, firm muscle wriggles inside of you, darting about."
    "Rocking your hips, you ride her face, fucking yourself with her tongue."
    "Releasing the headboard, you lift your hands to your breasts."
    show bg VSubBedroom12 with dissolve

    "As her tongue thrusts in and out of you, your fingers find your nipples."
    "Pinching, twisting, pulling - you tease their sensitive tips."
    "Rising up on your knees, you pull your cunt from Violet's mouth."
    show bg VSubBedroom13 with dissolve

    "She breathes hard, her mouth and chin coated in your juices."
    V "Please, may I-- May I touch myself, [domtitle]? May I... cum?"
    menu violetsub4_violethouse_cum:
        "Let her." if True:
            $ violetcum = 0
            "You lean down, unclipping her cuffs from the straps."
            pcname "You may."
            "You shuffle your weight, letting her slip her hands under your legs."
            "She moans as she begins pleasuring herself, and you silence her with your pussy."
            show bg VSubBedroom14 with dissolve

            "Rocking your hips, you run your pussy over her tongue."
            V "Mmm~ Mmmmmmm~"
            "Your nipples and clit ache with pleasure, throbbing as your orgasm builds inside you."
            "Rocking back and forth against her mouth, you pleasure yourself with her tongue."
            pcname "Ah~ Ohh~"
            V "Mmm~ Nnnnn~"
            "Leaning forward, you press your clit to her mouth. Instinctively, her lips fasten around it, sucking hard."
            "Pleasure floods you instantly - almost painfully - and you shudder above her."
            "Your body trembles, quaking as wave after wave of pleasure surges from your pussy."
            "Then Violet moans loudly, shivering beneath you, and you know she's found her own pleasure too."
            show bg VSubBedroom15 with dissolve

            "Heavy with pleasure, you pull yourself off of Violet, smiling as she takes a deep breath."
            "She sighs, well sated, her fingers still pressed to her breast and her pussy."
            show bg VSubBedroom17 with dissolve

            pcname "I've decided..."
            "Violet turns her head toward you, tilting it questioningly."
            if club == "track":
                pcname "You should order more things like that."
            elif club == "cheer":
                pcname "You should order more toys."
            elif club == "yearbook":
                pcname "You should order more... things. Like that. "
            pcname "But send them to my house so that {i}I{/i} get to decide where and when we use them."
            "She smiles."
            V "Of course, [domtitle]."
            "Glancing about, you spy your clothes."
            pcname "I guess I should get dressed."
            "Violet shakes her head in denial."
            V "No, you should stay. The driver can take you home in the morning..."
            "Smiling, you rejoin her in the bed, pulling the blankets up over both of you."
            show bg VSubBedroom18 with dissolve

            "Violet settles against you, sighing contentedly as your arm slides around to cup her breast."
            "Well-satisfied, Violet murmurs her approval and quickly drifts to sleep."
        "Don't let her." if True:
            $ violetcum += 1
            "Shaking your head, you smile down at her."
            pcname "Not this time."
            "She groans with frustration, but you silence her with your pussy, pressing it back to her lips."
            show bg VSubBedroom12 with dissolve
            "Rocking your hips, you run your pussy over her tongue."
            V "Mmm~ Mmmmmmm~"
            "Your nipples and clit ache with pleasure, throbbing as your orgasm builds inside you."
            "Rocking back and forth against her mouth, you pleasure yourself with her tongue."
            pcname "Ah~ Ohh~"
            V "Mmm~ Nnnnn~"
            "Leaning forward, you press your clit to her mouth. Instinctively, her lips fasten around it, sucking hard."
            show bg VSubBedroom16 with dissolve

            "Pleasure floods you instantly - almost painfully - and you shudder above her."
            "Your body trembles, quaking as wave after wave of pleasure surges from your pussy."
            "For a moment, all you know is pleasure."
            "Then it fades. You open your eyes, blinking, and lift yourself from Violet's face."
            show bg VSubBedroom19 with dissolve

            "She gasps, moaning her frustration, and pouts up at you."
            "You smile down at her, pleased with how she's behaving."
            pcname "I've decided..."
            "Violet watches you, listening intently. Hopefully."
            if club == "track":
                pcname "You should order more things like that."
            elif club == "cheer":
                pcname "You should order more toys."
            elif club == "yearbook":
                pcname "You should order more... things. Like that. "
            pcname "But send them to my house so that {i}I{/i} get to decide where and when we use them."
            V "Y-yes, [domtitle]..."
            "Glancing about, you spy your clothes and sigh."
            pcname "I guess I should get dressed..."
            "Violet shakes her head in denial."
            V "No, you should stay. The driver can take you home in the morning..."
            "Smiling, you rejoin her in the bed, unclipping her cuffs and pulling the blankets up over both of you."
            show bg VSubBedroom18 with dissolve

            "Violet settles against you, moaning as your arm slides around to cup her breast."
            "It takes a while, but eventually her breathing slows, deepening, and you know she's asleep."
    "You lie awake a little longer, enjoying the feeling of her in your arms."
    "The sex was incredible, but part of you thinks you could be content with just this."
    "Just... her."
    $ acts = 4
    $ day += 1
    $ daycount += 1
    $ wenttoschool = False
    $ wenttowork = False
    $ wenttoclub = False
    $ goingto = ""
    call events_end_day from _call_events_end_day_5
    call dayeval from _call_dayeval_5

    scene bg VioletBedroom with dissolve
    "You wake in the morning, alone in Violet's large bed."
    if club == "track":
        pcname "Where did she...?"
        pcname "Right, the charity thing with her mom..."
    elif club == "cheer":
        pcname "She's gone already?"
        pcname "She didn't seem interested in the charity thing with her mom. I'm surprised she went."
    elif club == "yearbook":
        pcname "What...?"
        pcname "Oh, she must have left with her mom... I forgot..."
    $ clothes = "naked"
    show chelsea with dissolve
    pause 0.5
    $ clothes, hair = casualwear
    pause 0.8
    show chelsea at exitScene(0.5, 1.0, 0.45, 0.45)
    "Dressing quickly, you make your way downstairs, feeling more than a little lost."
    scene bg LuxParty with fade
    show chelsea with dissolve
    show GHCMan at right with dissolve
    "Butler" "Miss [pcname], good morning. Your driver is ready, if you're ready to go home?"
    if club == "track":
        "You nod, a little uncomfortable with the formal atmosphere."
    elif club == "cheer":
        show chelsea embarrassed
        "You smile, thinking that you could get used to this."
    elif club == "yearbook":
        show chelsea sad
        "You nod nervously, unsure of what to say or do."
    "Butler" "Right this way."
    scene black with fade
    "He walks you to the foyer, holding the door open for you."
    "The driver waits outside and, as you approach, helps you into the back seat."
    "You ride home in silence, a smile playing over your lips as you think about the night before."

    jump home2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
