label violetdom5_carresolution:
    show bg Cafeteria
    $ clothes = "school"
    show chelsea at center with moveinright
    "Placing Violet's tray in front of her, you take your seat across from her and wait patiently."
    show chelsea happy
    show V School Blank at left with dissolve
    V "Very good. You got everything I asked for."
    show V School Pout
    "Her eyes move back to her phone, where she swipes and taps the screen."
    if violetdom4masturbate:
        show chelsea sad
        "Shifting nervously, you wait for her to ask about last night."
    elif True:
        show chelsea embarrassed
    show V School Blank
    "Violet picks up her sandwich and takes a bite, still tapping away on her phone."
    show chelsea happy
    show V School Pout
    "Now that she's begun eating, you take a bite of your own sandwich."
    show V School Smile
    V "So..."
    show chelsea blank
    "She slides the phone to the side and studies your face."
    V "Were you a good girl last night?"
    menu violetdom5_carresolution_choice:
        "Yes!" if not violetdom4masturbate:
            show chelsea happy
            show V School Blank
            V "Really? You didn't touch yourself?"
            show chelsea confused
            show V School Pout
            "She frowns, making you wonder if you've done something wrong."
            show chelsea embarrassed
            if club == "track":
                pcname "No...?"
            elif club == "cheer":
                pcname "No, I promise!"
            elif club == "yearbook":
                "Glancing about nervously, you shake your head."
            show V School Blank
            V "Didn't you want to?"
            "You feel your cheeks warming."
            show V School Smile
            if club == "track":
                pcname "Yeah, of course I did."
            elif club == "cheer":
                pcname "Well, yeah..."
            elif club == "yearbook":
                pcname "Y-yes..."
            V "So why didn't you?"
            show chelsea confused
            show V School Pout
            "Your mind races. She told you not to, didn't she?"
            "Why would she be upset now?"
            show chelsea happy
            pcname "Because you told me not to."
            show chelsea embarrassed
            show V School Smile
            "She watches your face a moment longer, then smiles."
            "As her lips turn up, you feel yourself relaxing."
            show chelsea happy
            V "Very good, [pcname]."
            show V School Pout
            V "I guess that means you deserve a reward. Hmmm..."
            show chelsea embarrassed
            show V School Smile
        "No..." if violetdom4masturbate:
            show chelsea sad
            show V School Pout
            "Violet frowns."
            show V School Blank
            V "I'm glad you're being honest, but..."
            show chelsea embarrassed
            "Your pulse quickens as she speaks."
            show chelsea shocked
            V "I'm really disappointed. I told you to behave yourself and you didn't obey me."
            show chelsea sad
            "Chest tight, you nod your head."
            show V School Annoyed
            if club == "track":
                pcname "I tried! It's just-- You were so--"
            elif club == "cheer":
                pcname "I did {i}try{/i} to behave. It was just so hard..."
            elif club == "yearbook":
                pcname "I-I'm sorry. I--"
            V "I understand, but it wouldn't have been a test if it wasn't hard."
            show chelsea embarrassed
            "She taps the table, watching you squirm beneath her gaze."
            show chelsea shocked
            show V School Blank
            V "Well, I suppose I'll have to punish you then, won't I?"
            show chelsea embarrassed
            "Your heart leaps at her words, but you can't tell if you're afraid or excited."
            show chelsea embarrassed
            show V School Smile
            if club == "track":
                pcname "Yes, Violet."
            elif club == "cheer":
                pcname "Yes, Violet."
            elif club == "yearbook":
                pcname "Y-yes, Violet..."
        "Yes..." if violetdom4masturbate:
            $ violetdom5lie = True
            show chelsea embarrassed
            show V School Blank
            V "Really? You didn't touch yourself?"
            show chelsea sad
            show V School Pout
            "She frowns and your mind races."
            show chelsea shocked
            "Does she know? How would she know?"
            show chelsea happy
            if club == "track":
                pcname "No...?"
            elif club == "cheer":
                pcname "No, I promise!"
            elif club == "yearbook":
                show chelsea embarrassed
                "Glancing about nervously, you shake your head."
            show V School Smile
            V "Didn't you want to?"
            show chelsea embarrassed
            "You feel your cheeks warming."
            if club == "track":
                pcname "Yeah, of course I did."
            elif club == "cheer":
                pcname "Well, yeah..."
            elif club == "yearbook":
                pcname "Y-yes..."
            V "So why didn't you?"
            show chelsea sad
            "She has to know. Why would she ask all these questions if she didn't?"
            show V School Pout
            pcname "I... I..."
            show V School Blank
            V "Well?"
            show V School Pout
            "Under the weight of her stare, you feel yourself cracking."
            show chelsea embarrassed
            show V School Annoyed
            pcname "I couldn't help myself!"
            V "I'm really disappointed. I told you to behave yourself and you didn't obey me."
            show chelsea sad
            V "And then you {i}lied{/i} about it."
            "Your chest tightens with shame."
            pcname "I'm sorry! I didn't mean to lie, I just didn't want to disappoint you."
            "Shaking her head, she crosses her arms over her chest."
            V "Then you should have done what I told you."
            show chelsea embarrassed
            show V School Pout
            if club == "track":
                pcname "I tried! It's just-- You were so--"
            elif club == "cheer":
                pcname "I did {i}try{/i} to behave. It was just so hard..."
            elif club == "yearbook":
                pcname "I-I'm sorry. I--"
            show V School Annoyed
            V "I understand, but it wouldn't have been a test if it wasn't hard."
            show chelsea sad
            "She uncrosses her arms and taps the table, watching you squirm beneath her gaze."
            show chelsea embarrassed
            show V School Pout
            V "Well, I suppose I'll have to punish you then, won't I?"
            show chelsea happy
            show V School Annoyed
            V "Twice, actually. Once for disobeying and once for lying."
            show chelsea embarrassed
            "Your heart leaps at her words, but you can't tell if you're afraid or excited."
            show V School Smile
            if club == "track":
                pcname "Yes, Violet."
            elif club == "cheer":
                pcname "Yes, Violet."
            elif club == "yearbook":
                pcname "Y-yes, Violet..."
    V "Good. Then I'll pick you up after work tonight. Try not to be too late."
    show chelsea blank
    show V School Pout
    "Nodding your head, you take another bite of your sandwich and wonder:"
    "What does she have planned for you?"
    jump events_end_period

label violetdom5_afterwork:
    $ VCasualBlank = "Characters/Violet/Casual 2/Neutral.png"
    $ VCasualPout = "Characters/Violet/Casual 2/Pouting.png"
    $ VCasualAnnoyed = "Characters/Violet/Casual 2/Annoyed.png"
    $ VCasualSmile = "Characters/Violet/Casual 2/Smile.png"
    $ VCasualSuprised = "Characters/Violet/Casual 2/Suprised.png"

    $ VSubCasualBlank = "Characters/Violet/Casual 2/Sub/Neutral.png"
    $ VSubCasualHappy = "Characters/Violet/Casual 2/Sub/Happy.png"
    $ VSubCasualSad = "Characters/Violet/Casual 2/Sub/Sad.png"
    $ VSubCasualWorried = "Characters/Violet/Casual 2/Sub/Worried.png"

    $ clothes, hair = casualwear

    show bg CityE
    show chelsea happy at right, enterScene(1.2, 1.0, 0.4, 0.45)
    "As soon as you walk out of the building, you see Violet's car parked right out front."




    show chelsea at exitScene(1.0, 0.6, 0.3, 0.3)
    pause 0.3
    hide chelsea
    hide bg CityE
    show black
    with fade

    "Walking to the driver's side, you take a seat and glance into the rearview mirror."
    show chelsea embarrassed at right
    show V Casual Smile
    with dissolve
    if violetdom4masturbate:
        "Violet smiles and your chest tightens."
        "How is she going to punish you?"
    elif True:
        "Violet smiles and you return the expression."
        "How is she going to reward you?"
    V "Well? Aren't you eager to get to my place?"
    "Nodding slowly, you shift the car into drive and pull out onto the road."
    hide chelsea
    hide V Casual
    with dissolve
    "The GPS is already set for her address, so you follow its directions at the first light."
    V "Mmmm~"
    hide black
    show bg VBackseat1
    with dissolve
    "Glancing in the rearview, you see that Violet has her top off again."

    "Her hands run over her breasts, lifting and squeezing them."
    "Her fingers pause at her nipples, pinching and twisting briefly."
    V "Mmm~ I wish I could feel {i}your{/i} hands on me, [pcname]."
    "Gripping the wheel harder, you maneuver the car around the next turn."
    V "You could use more than just your hands too..."
    V "You could lick my nipples... Suck them... {i}Bite{/i} them..."
    "Your breath catches in your throat. Warmth floods your panties, leaving you squirming in your seat."
    V "There's other things you can do with your mouth too. Do you want to taste my pussy, [pcname]?"
    "At those words, an unexpected moan escapes your lips."
    V "Mmm~ It {i}sounds{/i} like you'd like that..."
    hide bg VBackseat1
    show bg VBackseat2
    with dissolve

    "Glancing in the mirror again, you see Violet has her skirt hiked up again."
    "Her panties are off and her legs are spread wide, showing off the parts she's describing."
    V "You could slide your tongue up and down... Up and down..."
    "Her fingers trace the path she describes. You can practically taste her on your tongue..."
    V "Maybe if you're {i}really{/i} good, I'll let you taste me."
    V "Can you be a good girl?"
    if club == "track":
        pcname "Yes, Violet. I can be whatever you want."
    elif club == "cheer":
        pcname "Yes, Violet. I can be a good girl for {i}you{/i}."
    elif club == "yearbook":
        pcname "Y-yes, Violet..."
    if violetdom4masturbate:
        V "Are you sure? You weren't last time I told you to."
        "Your cheeks redden. She's right."
    elif True:
        V "I know you can. You were a good girl last night too."
        "You nod, your cheeks warming at her praise."
    hide bg VBackseat2
    show bg VioletHouseD
    with fade
    "As the GPS routes you up to a gate, you stop the car and glance back at her."
    "She's pulling her clothes back in place, but pauses to give you instructions."
    show V Casual Smile with dissolve
    V "Wait just a second and... There you go!"
    hide V Casual with dissolve
    "You take your foot off the brake as the gate slowly swings open."
    show V Casual Blank with dissolve
    V "There's a sensor behind the rearview mirror that opens the gate. Otherwise, you have to hit the call button so security can let you in."
    hide V Casual with dissolve
    "It's hard to imagine having a gate like this at your house, but it doesn't surprise you that Violet has one."
    "Now that you think about it, though, this is the first time you've actually been to Violet's house."
    "Realizing that, your anticipation grows a nervous edge."
    show V Casual Blank with dissolve
    V "Just pull up there and we'll have the driver park for us."
    hide V Casual with dissolve
    show chelsea confused with dissolve
    if club == "track":
        pcname "Driver?"
    elif club == "cheer":
        pcname "You have a driver?"
    elif club == "yearbook":
        pcname "You have... a driver?"
    hide chelsea with dissolve
    show V Casual Smile with dissolve
    V "Yeah, of course. He's my father's driver, but sometimes he drives my mother or me around too."
    hide V Casual with dissolve
    show chelsea shocked with dissolve
    if club == "track":
        pcname "Oh. Wow."
    elif club == "cheer":
        pcname "Oh wow..."
    elif club == "yearbook":
        pcname "Oh..."
    hide chelsea with dissolve
    "Pulling up in front of the house, you start to open the door but find it already opening."
    show GHCMan with dissolve
    "Driver" "Sorry, miss. Allow me."
    show chelsea at right with dissolve
    "If he's surprised to see you instead of Violet, you can't tell."
    show V Casual Pout at left with dissolve
    "As soon as your door is shut, he opens the door for Violet as well."
    show V Casual Blank
    V "Give him my keys, [pcname]. He'll take it from here."
    show chelsea embarrassed
    show V Casual Pout
    hide GHCMan with dissolve
    "The man nods and extends his hand. You drop the keys into his palm, smiling nervously."
    show chelsea blank
    show V Casual Blank
    V "Come on, let's go."
    hide V Casual with dissolve
    hide chelsea with dissolve
    "You know you're supposed to open doors for her, but as soon as you get to the front door it swings open."
    scene bg LuxParty with dissolve
    show GHCMan at right with dissolve
    show chelsea shocked with dissolve
    show V Casual Pout at left with dissolve
    "Butler" "Hello, Miss Violet. Your parents are home. Will you be joining them in the family room?"
    show chelsea embarrassed
    "You glance back at Violet, feeling more and more like a fish out of water."
    "Her nose wrinkles."
    show V Casual Blank
    V "No, I don't think so. We're going to my room."
    show chelsea shocked
    show V Casual Pout at exitScene(0.0, 1.0, 0.4, 0.3)
    "Violet breezes past you, leaving you rushing to catch up."
    show chelsea at exitScene(0.5, 1.5, 0.4, 0.3)
    pause 0.3
    hide GHCMan
    hide V Casual
    hide chelsea
    with dissolve
    "You barely have time to take in the entryway before she leads you past a grand piano and into the next room."
    show GCGirl with dissolve
    "Woman" "Violet, darling, you didn't tell me you were bringing a friend home."
    show V Casual Suprised at right
    show chelsea at midright
    with dissolve
    "You watch as Violet freezes in her tracks, turning slowly to face you."
    hide V Casual
    show V SubCasual Blank at right
    V "Sorry, mother. We ran into each other while I was out and I invited her back to study."
    hide V SubCasual
    show V Casual Pout at right
    "Violet's eyes find yours, urging you to agree. Turning, you see a gorgeous, dark-haired woman standing with a glass of wine."
    show chelsea embarrassed
    "Woman" "Well? Aren't you going to introduce us?"
    show chelsea happy
    show V Casual Blank
    V "I was just about to, naturally."
    V "Mother, this is my classmate [pcname]. [pcname], this is my mother, Rose Atwood."
    show V Casual Pout
    "She smiles."
    show chelsea sad
    show V Casual Suprised
    "Rose" "Please, just Rose. What does your family do, [pcname]?"
    show V Casual Pout
    if club == "track":
        pcname "Um, well... Nothing, I guess. They died."
    elif club == "cheer":
        pcname "Oh, I... I don't really have any family left."
    elif club == "yearbook":
        pcname "O-oh, um... Th-they're gone, so..."
    show chelsea embarrassed
    show V Casual Blank
    V "She's an orphan. Car accident. Very sad."
    show chelsea blank
    show V Casual Pout
    "Her mother's eyes widen in surprise."
    "Rose" "Oh dear, I had no idea. I'm so sorry."
    hide V Casual
    show V SubCasual Sad at right
    "You shrug, not missing the pointed look she shoots in Violet's direction."
    show chelsea embarrassed
    show V SubCasual Happy
    V "Anyway, we have a lot of studying to get done!"
    show chelsea sad
    hide V SubCasual
    show V Casual Pout at right
    "Rose" "Now, darling, don't be rude. You should introduce her to your father as well."
    "Violet's mother turns to you, beckoning you to follow."
    show V Casual Annoyed
    hide GCGirl with dissolve
    "Rose" "Come, dear. Marshall will be happy to see Violet making some public school friends."
    "You glance back at Violet, helplessly torn between her mother's commanding presence and Violet's clear unhappiness with the situation."
    hide V Casual with dissolve
    "Violet rolls her eyes and follows, easing some of your concern."
    hide chelsea with dissolve
    "Her mother leads you through the living room, past the dining room, and into - another? - living room."
    "Rose" "Here's the family room."
    "She gestures ahead of her, indicating the second living room."
    show GCGirl at midright
    show chelsea
    show V Casual Pout at left
    with dissolve
    "Rose" "Marshall, we have a guest."
    show GHCMan at right with dissolve
    "A middle aged man with short black hair and reading glasses sits with a tablet."
    "He glances up at you quickly, then looks back at the tablet."
    show chelsea embarrassed
    "After a moment, his eyes dart back up and he really looks at you."
    "{i}Really{/i} looks at you."
    show V Casual Annoyed
    "His eyes run down your body - from your hair, to your feet, and back up again."
    "With his wife and daughter standing on either side of you, you flush under his gaze."
    show V Casual Pout
    "Marshall" "And who is this?"
    "Rose" "This is Violet's friend. From the public school."
    "Marshall" "Well, glad to hear it."
    show chelsea blank
    hide GHCMan with dissolve
    "And with that, he goes back to his tablet."
    "Rose smiles and turns to Violet."
    show V Casual Suprised
    "Rose" "Don't forget that I have a fundraiser tomorrow, dear. You'll be helping me get set up, won't you?"
    show V Casual Blank
    "Violet sighs."
    hide V Casual
    show V SubCasual Happy at left
    V "Yes, mother."
    hide V SubCasual
    show V Casual Smile at left
    "Rose" "Don't say it so dramatically, dear."
    show chelsea laugh
    show V Casual Pout
    "She gives you a long-suffering smile, as if to say \"do you see what I deal with?\", before turning back to Violet."
    show chelsea embarrassed
    show V Casual Annoyed
    "Rose" "Well, I won't keep you. Go study, you two!"
    show V Casual Blank
    V "Great. Thanks. Let's go, [pcname]."
    hide V Casual with dissolve
    menu violetdom5_parents:
        "It was nice to meet you." if True:
            if club == "track":
                show chelsea blank
                pcname "It was nice to meet you guys."
                "Violet's mother smiles uncomfortably."
                "Rose" "And you as well."
            elif club == "cheer":
                show chelsea happy
                pcname "It was nice meeting you. You have a beautiful home."
                "Violet's mother smiles graciously."
                "Rose" "And you as well, dear."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I-it was nice... meeting you..."
                "Violet's mother smiles patiently."
                "Rose" "Of course. It was nice to meet you too, dear."
            hide chelsea
            hide GCGirl
            with dissolve
        "(Stay silent)" if True:
            hide chelsea
            hide GCGirl
            with dissolve
            "Waving awkwardly at her parents, you follow Violet out of the room."
    "Violet leads you out of the family room, through the living room, and back to the - foyer?"
    "Passing the grand piano, she leads you up a large staircase and along a balcony overlooking the living room."
    show V Casual Blank at center, enterScene(0.8, 0.5, 0.4, 0.4)
    V "My rooms are right down here..."
    show V Casual Blank at center, exitScene(0.5, 0.0, 0.45, 0.45)
    "Passing several closed doors, she comes to a stop and motions for you to open one of them."
    "You hurry to obey. Swinging the door open, you see... Another living room? What?"
    "Looking about, you barely notice Violet clicking the lock in place."
    scene black with dissolve
    V "This is my sitting room, but I don't use it much."
    "She leads you past a small sitting area - outfitted with a sofa, chair, and coffee table - through a doorway, and into her bedroom."
    "Her bedroom is at least as big as your living room, and through the doors on the sides you see a large bathroom and a large walk-in closet."
    "Her \"rooms\" are easily the size of your entire apartment."
    scene bg LuxParty
    show V Casual Pout
    with fade
    "Violet doesn't seem to notice your surprise, though."
    show V Casual Smile
    V "Now that {i}that's{/i} over with..."
    show chelsea happy at midright with dissolve
    show V Casual Pout
    "She turns to face you, looking you up and down."
    show V Casual Smile
    V "Take off your clothes. All of them."
    show chelsea embarrassed
    if club == "track":
        "You recover with a grin."
        pcname "Yes, Violet."
    elif club == "cheer":
        "Smiling impishly, you forget about the room for the moment."
        pcname "Yes, Violet."
    elif club == "yearbook":
        "Taking a deep breath, you glance around the room one last time."
        pcname "Um... Yes, Violet."
    $ clothes = "naked"
    "In moments, your clothes are heaped on the floor."
    "Standing in the center of her bedroom, you wrap your arms around yourself nervously."
    show V Casual Pout
    "Violet, still fully dressed, motions toward the bed."
    show V Casual Smile
    V "I set this up last night..."
    show chelsea happy
    show V Casual Pout
    "Reaching down along each of the four corners, Violet pulls a fur-lined cuff up onto the bed."
    V "It wraps under the bed, so it's not too noticeable. And the maids know better than to go squealing to my mother."
    show chelsea embarrassed
    show V Casual Smile
    if club == "track":
        pcname "You're going to cuff me to the bed?"
    elif club == "cheer":
        pcname "So you wanna tie me up?"
    elif club == "yearbook":
        pcname "You want me to...?"
    "Grinning wickedly, Violet motions to the bed again."
    V "I want you to get on the bed. Now."
    scene bg black with dissolve
    "You climb onto the bed, resting your head on the soft, fluffy pillows."
    "As you stretch your arms and legs out, Violet secures the cuffs around your wrists and ankles."
    show bg VDomBedroom1 with dissolve
    V "Perfect. Now, where did I put that..."
    "She walks into her closet, disappearing for a moment."
    "While she's gone, you test your restraints."
    "There's a little give, but not much, allowing you to move your hands and feet a few inches at most."
    "Even though you can't free yourself, it's reassuring to know you can move a little, at least."
    V "Here it is!"
    if violetdom4masturbate:
        "She returns from the closet with a leather flogger in hand."
        V "Since you misbehaved last night, I'll be using {i}this{/i} to punish you."
        show bg VDomBedroom2 with dissolve
        "Shaking the flogger, she watches you intently."
        "Your pulse quickens; is she really going to flog you with that?"
        V "But first, I want to make sure you understand why I'm doing this."
        "She approaches the bed and lowers the flogger, letting the strips of leather rest against your chest."
        V "Tell me what you did to deserve this, [pcname]."
        "As she speaks, she runs the leather down your chest. The strips tickle your breasts and belly before pooling between your thighs."
        show bg VDomBedroom3 with dissolve
        "Inhaling sharply, you force the words out."
        if club == "track":
            pcname "I touched myself after you told me not to."
        elif club == "cheer":
            pcname "I was a bad girl. I touched myself even though you told me not to."
        elif club == "yearbook":
            pcname "I... I touched myself...?"
        "She runs the flogger all the way down to your feet, then starts running it back up again."
        if violetdom5lie:
            V "And...?"
            "Flushing, you look away."
            if club == "track":
                pcname "And I lied to you about it."
            elif club == "cheer":
                pcname "And I didn't tell the truth when you asked."
            elif club == "yearbook":
                pcname "I... I lied about it..."
        V "That's right..."
        "As the flogger skims your breasts again, Violet lifts it."
        "Your chest tightens - though whether from anxiety or anticipation, it's hard to say."
        V "You've got to learn to obey your Mistress. So now I'll have to punish you."
        "Violet brings the flogger down on your belly; the leather straps crackling like a light rain as they hit your skin."
        show bg VDomBedroom4 with dissolve
        "They sting, but it's not too bad. Certainly not as bad as you expected."
        V "Well? Say thank you."
        if club == "track":
            pcname "Thank you, Violet."
        elif club == "cheer":
            pcname "Thank you, Violet..."
        elif club == "yearbook":
            pcname "Th-thank you, Violet..."
        V "Good girl."
        "She brings the flogger down again, this time striking your left thigh."
        show bg VDomBedroom5 with dissolve
        "The sting is sharper now, the flesh more sensitive, but it's still not too bad."
        "She waits, watching you expectantly."
        pcname "Thank you, Violet."
        "Pausing a moment, she shakes her head."
        V "In this room, you'll call me \"Mistress\". Do you understand?"
        if club == "track":
            pcname "Yes, Mistress."
        elif club == "cheer":
            pcname "Yes, Mistress..."
        elif club == "yearbook":
            pcname "Yes, M-mistress..."
        "Smiling, she brings the flogger down again - this time on your breasts."
        show bg VDomBedroom6 with dissolve
        "You gasp; it's no more sensitive than your thighs, but for some reason it {i}feels{/i} different - more vulnerable."
        if club == "track":
            pcname "Thank you, Mistress."
        elif club == "cheer":
            pcname "Thank you, Mistress..."
        elif club == "yearbook":
            pcname "Th-thank you, Mistress..."
        "The flogger strikes your belly again, leaving tiny, stinging bursts of warmth in its wake."
        pcname "Thank you, Mistress..."
        "Again and again she brings the flogger down, raining soft blows over your skin. And each time, you thank her for doing it."
        "Even though it doesn't really hurt, you soon find yourself wincing and writhing on the bed, your nerve endings overwhelmed by the sensations."
        "Then, suddenly, she brings the flogger down harder, cracking the straps against your sensitive breasts."
        "You gasp and freeze, your muscles tensing, and for a moment you feel as if you don't remember how to breathe."
        show bg VDomBedroom7 with dissolve
        "The moment quickly fades; your muscles relax and you exhale."
        pcname "Th-thank you, Mistress..."
        "Violet smiles, hearing the change in your voice."
        "The next few strokes are soft again, giving you time to relax. And then she brings it down hard on your thigh."
        "Your skin burns where the straps landed, your nerve endings tingling painfully."
        "Again, you can't breathe for just a moment - and then the moment passes."
        pcname "Thank you... Mistress..."
        "Her strokes turn soft again. Accustomed to them now, they almost tickle."
        pcname "Ah!"
        "You cry out as the strips of leather land on your labia - more from surprise than pain."
        show bg VDomBedroom8 with dissolve
        V "Shhh. My parents are home, remember?"
        pcname "Th-thank you, Mistress. I'll be quieter."
        V "I think you're starting to enjoy this."
        "She waves the flogger to your breasts. Your nipples stand up from your chest in hard, pink peaks."
        V "Well? Do you like being flogged, [pcname]?"
        "Your mind feels hazy, and for a moment you can't answer."
        "{i}Do{/i} you like it? Does Violet want you to?"
        "It's supposed to be a punishment, so maybe she'll be angry if you do?"
        "But it sounds like she wants you to..."
        "The flogger strikes your thighs again, leaving your skin hot and pink."
        V "Well? Answer me when I ask you a question."
        pcname "I..."
        menu violetdom5_punishment:
            "I like it!" if True:
                "She smiles."
                V "I thought so. Maybe I'm not doing it hard enough..."
            "I deserve it!" if True:
                "She smiles."
                V "That's true. So I should probably make sure you learn your lesson..."
        "She brings the flogger down three more times, each harder than the last."
        "The first strike lands on your thighs, the second on your belly, and the last one leaves your breasts on fire."
        show bg VDomBedroom9 with dissolve
        pcname "Ah! Ahh!"
        "Your muscles stiffen as the last stroke lands and you pull at your restraints involuntarily."
        V "That's a good girl..."
        "Violet's hand runs over your belly and up to your breasts, caressing each of them."
        show bg VDomBedroom10 with dissolve
        "At her touch, the pain turns to pleasure, confounding your nerve endings."
        "Her fingers trail over your nipples; your back arches instinctively, eager for her soothing caress."
        "Exhaling a breath you didn't know you were holding, you relax under her hand."
        "Her hand travels lower, brushing lightly over all of the sensitive places her flogger has landed."
        "Sighing with relief, you speak shakily:"
        pcname "Th-thank you, Mistress..."
        "Her hand runs over your belly, her fingers dancing over your labia."
        "Sucking in another sharp breath, you squirm beneath her, both eager for her touch and suddenly overwhelmed by it."
        V "Have you had enough?"
        "Your eyes search her face for some sign of what she wants to hear. She smiles down at you."
        pcname "Y-yes, Mistress...?"
        "She watches you a moment longer, then nods."
        V "Then tell me you're sorry."
        pcname "I'm sorry, Mistress. Thank you for correcting me."
        "She smiles at your humility and tosses the flogger aside."
    elif True:
        "She returns from the closet with a feather teaser in hand."
        V "Since you were so good last night, I'll be using {i}this{/i} instead of a flogger."
        show bg VDomBedroom11 with dissolve
        V "Doesn't that make you happy?"
        "Swallowing hard, you nod your head."
        "Beginning just under your chin, she draws the teaser down your neck, over your collar bone, and around the curve of your breast."
        "The feathers tickle your skin, leaving you shivering and giddy."
        show bg VDomBedroom12 with dissolve
        "But Violet frowns."
        V "I said, doesn't that make you happy?"
        if club == "track":
            pcname "Yes, Violet."
        elif club == "cheer":
            pcname "Yes, Violet..."
        elif club == "yearbook":
            pcname "Y-yes, Violet..."
        "She nods, but her frown lingers."
        V "In this room, you'll call me Mistress. Understand?"
        "The word sends a thrill through you - a thrill that settles, hot and moist, between your legs."
        if club == "track":
            pcname "Yes, {i}Mistress{/i}."
        elif club == "cheer":
            pcname "{i}Yes{/i}, Mistress..."
        elif club == "yearbook":
            pcname "Y-yes, Mistress..."
        "Smiling down at you, Violet draws the feathers over your breast, grazing the nipple."
        "Circling one breast, then the other, she teases your nipples with the feathers until you're gasping and squirming."
        show bg VDomBedroom13 with dissolve
        V "Do you like that?"
        "You begin to nod, before remembering her new rule."
        pcname "Yes, Mistress."
        "Violet smiles again and trails the teaser lower."
        "It tickles its way over your belly and down the outside of your leg, before crossing over your knee and trailing up between your thighs"
        show bg VDomBedroom14 with dissolve
        "You {i}know{/i} where the teaser is going and as it nears your pussy the anticipation grows."
        "But she stops just below your labia, drawing it back over your hip and up your belly."
        show bg VDomBedroom13 with dissolve
        "Violet runs the feathers over your breasts again, circling each of them."
        "Each time she moves from one breast to the other, she grazes your nipples with the teaser, making you gasp."
        "Squirming against the cuffs, you shiver with pleasure."
        "The feathers feel nice - soft and warm against your sensitive skin - but the sensation just leaves you wanting {i}more{/i}"
        "She draws the teaser lower again, trailing it over your belly."
        "You wait for her to divert it again, running it down your legs instead, but this time she trails it directly over your labia."
        show bg VDomBedroom15 with dissolve
        "Gasping, you stiffen, your back arching involuntarily."
        V "I think you liked that..."
        "A soft moan escapes your lips as she runs the teaser down your thighs."
        pcname "Yes, Mistress..."
        "She draws it back up, agonizingly slowly, pausing just before she reaches your pussy."
        "Shivering, you wait to see where she'll move it next."
        "Your skin tingles with anticipation; your clit pulsing from the little contact she's offered it."
        "She draws the teaser away, smiling down at you."
        V "This is fun, but..."
        "Letting the teaser drop to the floor, she leans over you."
    V "Now I'm horny again..."
    "She climbs onto the bed, crawling across you on all fours."
    show bg VDomBedroom17 with dissolve
    "Turning, she straddles your chest and moves back, positioning her pussy over your face."
    V "Well? Didn't you want to taste it?"
    "You barely recognize your own voice, husky with desire."
    pcname "Yes, Mistress..."
    "Lifting your face to her cunt, you run your tongue over her smooth, soft labia."
    show bg VDomBedroom18 with dissolve
    "She gasps as you circle her opening, running your tongue down one side and up the other."
    "You can smell the musky sweet scent of her pussy and, as you dip your tongue between her labia, taste the evidence of her arousal."
    V "Ahh~"
    "She shudders above you, pressing her cunt back against your face."
    show bg VDomBedroom19 with dissolve
    "Her juices run down your chin as she moves her hips, dragging your tongue up and down her opening."
    V "Ahh~ Ahh~"
    "Gasping and shuddering, she rubs her pussy over your mouth, giving you little choice but to eat her out."
    show bg VDomBedroom20 with dissolve
    "As you press your tongue into her, Violet dips her head down and flicks her tongue over your clit."
    "Moaning against her pussy, you eagerly thrust your tongue further into her."
    show bg VDomBedroom21 with dissolve
    V "Haa~ Haa~"
    "Her tongue dances over your clit, which throbs almost painfully with pleasure."
    "Your body, still on edge from earlier, reacts more strongly than ever."
    "Violet shifts above you, tilting her hips up and leaning forward to slip her tongue down your opening."
    "Your tongue finds her clit, flicking back and forth over the swollen nub."
    V "Ohh~"
    "Violet's lips circle your clit and she sucks gently, sending waves of pleasure through your whole body."
    "Flicking your tongue faster and faster, you quickly draw her to the edge of her own climax."
    show bg VDomBedroom22 with dissolve
    "Her thighs suddenly clench and, as her legs begin shaking, she sucks your clit hard."
    "Pleasure so intense it hurts shoots from your clit in jolts. Your hips buck against her face - though whether you're trying to get closer to her or push her away, you can't be sure."
    show bg VDomBedroom23 with dissolve
    "She collapses against you where, together, you shudder as the last throes of pleasure surge through you both."
    show bg black with dissolve
    "Eventually she rolls off of you and, moving slowly, removes the cuffs from your ankles and wrists."
    "Crawling into bed beside you, she cuddles in close."
    V "Just sleep here tonight. I'll have someone drive you home in the morning."
    "Your limbs feel heavy, but you manage to curl towards her, whispering:"
    pcname "Yes, Mistress..."
    "Well-satisfied, Violet murmurs her approval and quickly drifts to sleep."
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
    call events_end_day from _call_events_end_day_4
    call dayeval from _call_dayeval_4

    scene black with dissolve
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
    $ clothes, hair = casualwear
    show chelsea with dissolve
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
    hide GHCMan
    hide chelsea
    with dissolve
    "Butler" "Right this way."
    show bg black with dissolve
    "He walks you to the foyer, holding the door open for you."
    "The driver waits outside and, as you approach, helps you into the back seat."
    "You ride home in silence, still a little in awe of how Violet lives."

    $ VCasualBlank = "Characters/Violet/Casual/Casual Neutral.png"
    $ VCasualPout = "Characters/Violet/Casual/Casual Pouting.png"
    $ VCasualAnnoyed = "Characters/Violet/Casual/Casual Annoyed.png"
    $ VCasualSmile = "Characters/Violet/Casual/Casual Smile.png"
    $ VCasualSuprised = "Characters/Violet/Casual/Casual Suprised.png"

    $ VSubCasualBlank = "Characters/Violet/Casual/Sub/Neutral.png"
    $ VSubCasualHappy = "Characters/Violet/Casual/Sub/Happy.png"
    $ VSubCasualSad = "Characters/Violet/Casual/Sub/Sad.png"
    $ VSubCasualWorried = "Characters/Violet/Casual/Sub/Worried.png"

    jump home2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
