label violetdom6_date:
    $ clothes, hair = casualwear
    show bg CityE
    show chelsea at right with moveinright
    "Stepping out of work, you check your phone and see a text from Violet."
    play sound PhoneVibration
    call screen TextingScene("Violet",
    [
        TextMessage("Text me when you're off work!"),
        TextMessage("I'm off work", sender = False),
        TextMessage("Perfect"),
        TextMessage("I'm almost there"),
        TextMessage("We're going to dinner")
    ])
    show chelsea happy
    "Smiling, you tuck your phone away and wait."
    show chelsea blank
    "You spend a few minutes looking up and down the street for her car."
    show chelsea embarrassed
    "As she pulls up to the curb, you begin circling to the other side - but the passenger side window rolls down."
    show chelsea shocked
    show V Party Blank with dissolve
    V "Get in the back seat!"
    show chelsea confused
    show V Party Pout
    "Startled, you begin to ask why; then, remembering your place, you do as she says."
    hide chelsea with dissolve
    hide V Party with dissolve
    show black with dissolve
    hide bg CityE
    "It feels strange to sit in the back."
    show V Party Smile with dissolve
    V "There's a bag on the seat. Put everything in there on."
    hide V Party with dissolve
    show chelsea embarrassed at right with dissolve
    "Your pulse quickens; did she really bring something for you to wear?"
    "How expensive will this place be?"
    show chelsea blank
    "Reaching into the bag, you pull out a classy blue dress, a pair of heels, and lacy underwear."
    "You glance around the car. The windows are heavily tinted, making it very hard to see inside, but..."
    if club == "track":
        show chelsea happy
        "You shrug; you can change quickly."
        hide chelsea with dissolve
    elif club == "cheer":
        show chelsea embarrassed
        "You smile, remembering Violet naked in the same seat."
        "If she was comfortable doing {i}that{/i}, you can change quickly."
        hide chelsea with dissolve
    elif club == "yearbook":
        show chelsea sad
        pcname "Right... here...?"
        hide chelsea with dissolve
        show V Party Blank with dissolve
        V "The windows are tinted. Besides, {i}I've{/i} taken my clothes off back there, haven't I?"
        hide V Party with dissolve
        show chelsea embarrassed at right with dissolve
        pcname "R-right..."
        hide chelsea with dissolve
        "Swallowing back your fears, you begin undressing."
    $ clothes = "underwear"
    show chelsea at right with dissolve
    "Stripping down to just your bra, you pull the dress over your head and settle it around your waist."
    $ dressList.dresses[0].bought = True
    $ clothes = "bluedress"
    "With the more visible parts of your body covered, you slip your panties off and grab the lacy pair Violet bought for you."
    "As you slip it over your feet, though, you notice something strange. It seems... heavier than you'd expected."
    "Pulling it up your legs, you situate it around your hips - immediately, you feel something hard against your pussy."
    show chelsea confused
    pcname "What the..."
    hide chelsea with dissolve
    show V Party Smile with dissolve
    "Violet laughs as you reach down, pressing your fingers to the hard, round object inside your panties."
    show V Party Pout
    "Lifting her hand, Violet waves a small remote at you."
    show V Party Blank
    V "Ready?"
    hide V Party with dissolve
    show chelsea confused at right with dissolve
    pcname "For what?"
    "She hits a button and suddenly your panties begin vibrating."
    show chelsea shocked
    pcname "Ah!"
    hide chelsea with dissolve
    show V Party Smile with dissolve
    V "Wow, they really {i}are{/i} quiet, aren't they?"
    show V Party Pout
    "She hits the power button again, turning the panties off."
    show V Party Blank
    V "Well, now that you're changed it's time to change seats."
    hide V Party with dissolve
    "Pulling the heels on quickly, you get out of the car and open her door for her."
    "As she settles into the back seat, you check your mirrors."
    "In the rearview, you see Violet holding the remote again."
    show V Party Blank at right with dissolve
    V "The GPS is already set. Just follow it."
    hide V Party with dissolve
    "Taking a deep breath, you shift the car into drive and pull onto the road."
    "Just as you get up to speed, your panties come alive again."
    pcname "Ah~"
    "She hits another button and the tiny vibrator begins pulsing instead."
    "You squirm - the vibrator sits right against your clit, thrilling the bundle of nerve endings each time it rumbles."
    "It was hard to focus before, with Violet touching herself in the back seat. This though..."
    show V Party Blank at right with dissolve
    V "Is that a good one? Or maybe..."
    show V Party Pout
    "The pattern shifts again, now alternating between long and short pulses."
    show V Party Smile
    V "Ohhh, I like that one..."
    hide V Party with dissolve
    "You like it too. Leaning forward, you press your clit firmly against it."
    pcname "Ahh~"
    "It's too much; you lean back again, giving your clit some relief."
    "Violet hits another button and the intensity kicks up a notch."
    if club == "track":
        pcname "Oh shit..."
    elif club == "cheer":
        pcname "Oh... fuck..."
    elif club == "yearbook":
        pcname "O-oh! Ohh..."
    show V Party Blank at right with dissolve
    V "Do you like that?"
    show V Party Pout
    "Your grip tightens on the wheel as you squirm, noting the growing wetness of the lace."
    show V Party Smile
    V "You're going to wear these the whole way through dinner."
    hide V Party with dissolve
    "Glancing at the rearview mirror, you see her smirking back at you."
    pcname "Please, Mistress..."
    "You pause, surprised at how easily the word came to your lips."
    show V Party Smile at right with dissolve
    V "That's good. You can call me that anytime we're alone, not just in the bedroom."
    hide V Party with dissolve
    "The GPS directs you to a very nice part of town, as you'd expected."
    "Just as you pull into a parking space, Violet hits the power button again."
    "Shivering, you feel your clit continue pulsing, echoing the rhythm of the now-still vibrator."
    "Hurrying from the car, you open Violet's door for her."
    "Violet walks confidently into the restaurant - a chic italian place, from what you can tell - and gives her name to the hostess."
    scene black with dissolve
    show chelsea at left, moveSprite(0.25, 0.25, 0.0)
    show V Party Blank
    show GWaitress at midright
    with dissolve
    "Hostess" "Of course, Ms. Atwood. Right this way."
    hide GWaitress
    hide V Party
    hide chelsea
    with dissolve
    "She leads the two of you to your table. Along the way, you take in the dim lighting and intimate atmosphere."
    "The tables are covered in fine white tablecloths, set with several glasses and lots of silverware, and most have only two chairs each."
    "Hostess" "I hope this is acceptable, Miss?"
    "She pulls back the curtains to reveal a very private booth set into an alcove in the wall."
    show chelsea at left, moveSprite(0.25, 0.25, 0.0)
    show V Party Smile
    show GWaitress at midright
    with dissolve
    V "Yes, perfect."
    show chelsea embarrassed
    "Your heart jumps as you realize that this is a {i}very{/i} romantic restaurant."
    scene black with dissolve
    "The hostess waits until you both take a seat, then lays a menu in front of each of you."
    show bg VDDDS1 with dissolve
    "Hostess" "Your waiter will be right with you."
    "As she walks away, you look at the menu, feeling more and more out of place."
    if club == "track":
        "This isn't the kind of place you {i}ever{/i} thought you'd be in."
    elif club == "cheer":
        "This is the kind of place you only {i}dreamed{/i} you'd find yourself in."
    elif club == "yearbook":
        "There are so many utensils, and two glasses - why are there two glasses? - and..."
        "You take a deep breath, trying to control your racing thoughts."
    V "Do you like veal? The Tonnato is shaved veal and tuna sashimi."
    "You pick up the menu, staring at the unfamiliar words."
    V "Or the Fegato is good. It's chicken liver mousse on piccolina toast with some roasted pear..."
    "You've had chocolate mousse, but chicken liver? You don't know how to feel about that - let alone with pear..."
    V "But those are appetizers. Do you know what you want for your main course?"
    "You recognize some of the words, but the descriptions don't make sense to you."
    "Each item has a name, followed by several other words in a list."
    "Carmelle di Gorgonzola con Pera. Bleu Cheese. Red Wine. Poached Pear."
    "You know the words - most of them, anyway - but you have no idea what the dish will look like. Or taste like."
    "Your eyes catch the word spaghetti and, for a moment, you sigh with relief."
    "Spaghetti. Blue crab. Lemon. Bottarga. Chilies."
    "What does that {i}mean{/i}?"
    V "I usually get the Anatra. It's duck with fregola, radish, and quince, in a chicken au jus."
    "Violet looks up from her menu, watching your reaction."
    if club == "track":
        pcname "I don't really know what most of this says..."
    elif club == "cheer":
        pcname "That sounds... great."
    elif club == "yearbook":
        pcname "R-right. That... That sounds..."
    "Chuckling, she tilts her head and stares into your face."
    "You can't help but shift in your seat, the weight of her gaze heavy on your shoulders."
    "You know she's judging you, and you can't blame her."
    "She's used to places like this; you can only imagine how unsophisticated you look next to her."
    "Suddenly, she plucks the menu from your fingers."
    show bg VDDDS2 with dissolve
    V "It doesn't matter; I'll be ordering for you anyway."
    "Swallowing the hard lump of self-doubt that was forming in your throat, you nod."
    pcname "Thank you, Mistress."
    "She smiles, and just that quickly the weight lifts and all of your worries seem to fade."
    "Violet knows how to navigate this place and she will make the decision for you. There's nothing to worry about."
    show bg VDDDS3 with dissolve
    "Waiter" "Good evening, ladies. May I get you anything to drink?"
    V "Two glasses of the rosé."
    "You wait for him to ask for your ID - you're both clearly underage - but he doesn't even pause."
    "Waiter" "Very good."
    "As Violet orders the rest of the food, you glance over the wine list."
    "There's only one rosé amid all the other wines, and it's $26. {i}Per glass.{/i}"
    "Only then do you realize that, amid the strange menu descriptions, you hadn't looked for prices."
    "He collects the menu and walks away. Smiling, Violet produces a small object and sets it on the table."
    show bg VDDDS4 with dissolve
    "The remote."
    V "Did you forget about this?"
    "Glancing around the room, you respond in a whisper."
    pcname "You can't use that {i}here{/i}!"
    "A slow smile spreads over her face as she reaches down and presses the power button."
    "Immediately the vibrator comes to life, humming softly against your clit."
    show bg VDDDS5 with dissolve
    "Sucking in a quick breath, you shift in your seat as the waiter approaches again."
    "Waiter" "Water."
    "He holds up a glass decanter and, lifting one of your glasses, fills it with water."
    "Waiter" "And your rosé..."
    show bg VDDDS6 with dissolve
    "He holds a small bottle up. Plucking your wine glass from the table, he carefully fills it."
    "As he lifts Violet's wine glass, the vibrator suddenly switches to a pulsing rhythm."
    pcname "Ah~"
    "Alarmed, the waiter turns to you."
    "Waiter" "Is everything all right, Miss?"
    show bg VDDDS7 with dissolve
    pcname "It... It looks so good!"
    "You force a smile, shifting in your seat again."
    "Waiter" "It is an excellent vintage. Miss Atwood has impeccable taste."
    "Nodding, you throw Violet a tense smile."
    "As the waiter departs, you suck in a quavering breath."
    show bg VDDDS8 with dissolve
    "Violet leans toward you, lifting her wine glass to her lips."
    V "Try to be a little less suspicious."
    "Her hand falls to the remote again; the rhythm changes to a series of increasingly more intense pulses."
    "Bz... Bzz... Bzzz... Bzzzz... BZZZZZ!"
    "There's a short pause, and then the pulsing begins again."
    "Bz... Bzz... Bzzz... Bzzzz... BZZZZZ!"
    "Your muscles tense as the sensation builds."
    "By the time it reaches its peak, you catch yourself holding your breath."
    show bg VDDDS9 with dissolve
    "Exhaling, you wait - helpless - for it to begin again."
    "Bz... Bzz..."
    show bg VDDDS10 with dissolve
    "Violet licks her lips, watching you intently."
    "Bzzz... Bzzzz..."
    "Your muscles tense again as you wait for the final pulse."
    "BZZZZZ!"
    "Trembling in the wake of that powerful thrum directly against your clit, you let out a shaky breath."
    "Again the pulse begins, slow and gentle."
    "Bz... Bzz..."
    "Your abdomen clenches in anticipation of the final pulse. As it does, you feel a surge of heat in your pussy."
    pcname "Violet..."
    "She smiles and your heart flips."
    "And then you shudder as the final pulse sends waves of pleasure through your belly."
    "Her hand moves to the remote again and, on the verge of panic, your eyes widen."
    "If she turns it up again, you know you won't be able to take it. It's almost too much already."
    "To your relief, she presses the power button instead."
    V "Did you need a little break?"
    "Still trembling, you respond slowly, your voice weak."
    if club == "track":
        pcname "Thank you, Mistress."
    elif club == "cheer":
        pcname "Yes, thank you, Mistress."
    elif club == "yearbook":
        pcname "Th-thank you, Mistress."
    "Violet smiles, and again your heart flips beneath your breast."
    "As your breathing slows, Violet takes another sip of her wine."
    V "So what do you think of this place?"
    menu violetdom6_date_opinion:
        "It's amazing!" if True:
            "She laughs."
            V "It's okay. My father knows the owner, so I can always get a reservation without waiting."
            V "Apparently the waiting list is a few months long."
            if club == "track":
                "She says it so casually; you can't imagine what her life is like."
                "You're not sure if you've {i}ever{/i} made a reservation."
            elif club == "cheer":
                "Once again, you're blown away by the life she leads."
                "That you know someone so important, who can call a place like this and just get a table..."
            elif club == "yearbook":
                "For a moment, you don't know what to say."
                "Her life is so different from yours, and she's so {i}confident{/i}..."
        "It seems expensive." if True:
            "She shrugs."
            V "I guess so. Usually we order a {i}prix fixe{/i} with four courses. That's over $100 per person."
            "She pauses."
            V "Well, $200 if you get it with wine pairing."
            if club == "track":
                "You blink, astonished."
                "$200 per person!?"
            elif club == "cheer":
                "Your eyes widen; you try to wrap your mind around what she just said."
                "That's almost as much as you pay for groceries for a whole month!"
            elif club == "yearbook":
                "You shake your head, unwilling to believe what you're hearing."
                "$200? {i}Per person{/i}?"
        "I don't think I fit in here." if True:
            "She laughs."
            V "You're with me; you don't need to fit in."
            "She leans over the table, lowering her voice."
            V "You could eat with your fingers and they wouldn't say a thing."
            if club == "track":
                "Your cheeks warm; you {i}do{/i} eat with your fingers sometimes."
                "But just for things like wings."
                "Do they have wings here? How do you eat wings without using your fingers?"
            elif club == "cheer":
                "Your cheeks warm; you'd never do {i}that{/i}."
                "But it's nice to know that nobody will judge you."
            elif club == "yearbook":
                "Your cheeks warm and you look down."
                "Would they really just ignore any mistakes you make?"
                "Is that why Violet's so confident?"
    V "But don't worry about it. Just let me take care of you."
    "Her eyes run over your body."
    V "And when we get home, {i}you{/i} can take care of {i}me{/i}."
    "Lifting your water glass, you take a long sip, trying not to squirm under her lewd gaze."
    "As you set your glass down, the waiter returns."
    show bg VDDDS11 with dissolve
    "Waiter" "Your antipasti. The liver is blended with walnuts and fresh anchovy, spread across fire-toasted artisan bread, then topped with vanilla roasted pears."
    "He places a platter on the table. You look down to find four small rounds of toasted bread covered in a reddish-brown paste."
    "The paste is topped with thinly sliced pear."
    "Waiter" "Please, enjoy."
    if catadopt:
        "You stare down at the paste. It looks like something you'd feed [kittenname]."
    elif True:
        "You stare down at the paste. It looks like cat food."
    V "I know it doesn't {i}sound{/i} good, but just try it."
    V "And don't worry; it's a finger food."
    "Smiling, Violet reaches down and takes one of the paste-covered slices of toast."
    "Hesitantly, you do the same."
    "It doesn't {i}smell{/i} bad..."
    "Violet takes a bite, closing her eyes and sighing contentedly."
    "Still unsure, you take a tiny bite."
    "To your surprise, it has a very complex taste and texture."
    "Crisp bread, smooth pâte, and tender pears make a salty-sweet mixture of flavors."
    "It's not bad. Actually - you take a second bite - it might even be {i}good{/i}."
    "You eat both pieces of toast and lean back from the table."
    "The flavor lingers on your tongue, making you want another bite."
    V "It's very rich but I always want more."
    "Nodding, you smile."
    pcname "I was just thinking the same thing."
    "You don't notice Violet's hand, which was resting on the table, slowly move to the remote."
    "Bz..."
    "You gasp as your panties surge to life."
    "Bzz..."
    "Your clit, still swollen sensitive from before, thrums with pleasure."
    "Bzzz..."
    "Your pulse quickens in anticipation."
    "Bzzzz..."
    "Your breath catches in your throat as you wait for the final pulse..."
    "BZZZZZ!"
    show bg VDDDS12 with dissolve
    "Your eyes squeeze shut and your body stiffens as pleasure momentarily floods your senses..."
    "And then it's over."
    "Bz..."
    "Waiter" "I'll take the plate."
    "Heat rushes over your face as your eyes flutter open."
    "Bzz..."
    "Your eyes find Violet's, silently pleading with her to turn off the device."
    "Bzzz..."
    "Waiter" "Would you like more water?"
    "Bzzzz..."
    show bg VDDDS13 with dissolve
    "Your body stiffens as you turn to meet his eyes, shaking your head slightly."
    pcname "N-no, thank you..."
    "He nods, turning away just as the last pulse begins."
    "BZZZZZ!"
    "Shuddering in your seat, you stifle a moan."
    V "Oh, that was {i}close{/i}."
    "She leans over the table, her voice low."
    "Bz..."
    V "Do you think he noticed?"
    "Your breathing grows labored as you fight back both shame and arousal."
    "Bzz..."
    V "You look delicious when you're aroused..."
    "Biting your lip, you can't help but think of the last time you were together."
    "Her tongue on your..."
    "Bzzz..."
    "You can't hold back a soft moan, bringing a knowing smile to Violet's lips."
    "Lips that you've felt against your skin..."
    "Bzzzz..."
    show bg VDDDS12 with dissolve
    "It's too much! You shift in your seat, squirming with anticipation and dread."
    "Violet chuckles, and the last pulse never comes."
    "Shuddering, you force yourself to relax."
    "Your clit throbs with excitement, eager for {i}more{/i}..."
    show bg VDDDS13 with dissolve
    "Waiter" "Here you are, ladies."
    show bg VDDDS11 with dissolve
    "You glance away, unwilling to meet his gaze, barely hearing him as you try to calm your thundering heartbeat."
    "When he walks away, you glance down at your meal."
    show bg VDDDS14 with dissolve
    "A small nest of spaghetti sits in the middle of a large plate, circled with lemon wedges. Atop the spaghetti rests a mound of crab meat, sprinkled with chile flakes and tiny orange crumbs."
    V "You like spaghetti, right?"
    "This is unlike any spaghetti you've ever seen, but you nod anyway."
    "Lifting your fork and spoon, you twirl the spaghetti on your fork, holding it against your spoon to keep it from sliding off."
    "Pushing down your nerves, you take a bite of the pasta."
    "The firm noodles are coated in a garlicky, lemony butter. The crab is juicy and flavorful, while the chilies warm your mouth."
    "But the orange crumbs are... Salty? Sweet? Almost like cheese, but not quite..."
    V "Do you like it? Bottarga can be a little strange at first."
    pcname "Is it cheese?"
    show bg VDDDS15 with dissolve
    "Violet covers her mouth in an attempt to stifle a laugh."
    V "Cheese!? No!"
    "Frowning, you examine the orange stuff more closely. It kind of looks like the powdered cheese you put in the cheap, boxed macaroni."
    show bg VDDDS14 with dissolve
    pcname "Then... what is it?"
    V "It's dried, grated fish roe sac."
    show bg VDDDS15 with dissolve
    "One look at your reaction and Violet bursts out laughing again."
    "Peering incredulously at your plate, you shake your head."
    pcname "No it's not."
    "Still smothering her laughter, she nods."
    V "It is!"
    show bg VDDDS14 with dissolve
    "You glance at her plate - some kind of fish wrapped in thin slices of meat, topped with purplish onions and finely chopped herbs."
    V "I got prosciutto wrapped sea bass with cipollini onions, fennel, and an herb aioli."
    "You barely recognize any of those words."
    "Looking back at your own plate, you debate taking another bite."
    "It wasn't {i}bad{/i}, but the thought of dried fish egg sac makes you feel, well, {i}weird{/i}."
    "Taking a deep breath, you twirl another forkful."
    "Now that you know what it is, you can taste a faintly-fishy flavor. Or maybe it's just the crab..."
    "The flavor is complex - buttery, lemony, garlicky, salty, and slightly sweet. It lingers on your tongue, making you want another bite."
    pcname "It's... actually pretty good."
    "Violet smiles indulgently."
    show bg VDDDS15 with dissolve
    V "Don't let them hear you say it's only \"pretty good\"."
    "Ducking your head, you take another bite."
    pcname "Now that I know what to expect, I think I like it."
    show bg VDDDS14 with dissolve
    "She watches you eat, seemingly enjoying your reactions more than her own meal."
    "Which, for as much as she's paying, is very flattering."
    "Her gaze makes you self-conscious, though, and you find yourself hyper-aware of your own body."
    "Your movements, expressions... Everything you do feels like a performance."
    "As you finish your meal, Violet pushes her own plate forward."
    V "I think we'll skip dessert. I have something back home for you to eat."
    "Standing, she tosses a couple of bills on the table."
    "It only looks like $40."
    pcname "Should we wait for the check? That doesn't look like enough..."
    "Violet rolls her eyes."
    V "That's the tip, [pcname]. They'll charge my dad's account for the rest."
    if job=="bakery":
        "You shake your head. $40 is almost as much as you make in a whole shift at the bakery."
    elif True:
        "You glance back at the table, imagining a $40 tip. That's more than you make most nights."
    $ acts -= 1
    scene bg black with dissolve
    "Violet leads you back to her car, where you help her into the back seat."
    "Taking the driver's seat, you start the car and pull onto the road."
    "Bz..."
    "Jumping in your seat, you grab the wheel tightly."
    "Bzz..."
    "Your eyes meet Violet's in the rearview; she smirks back at you."
    "Bzzz..."
    "Your clit throbs, the swollen nub still sensitive from her earlier teasing."
    "Bzzzz..."
    V "I can't wait to get home and get these clothes off..."
    "BZZZZZ!"
    "The sudden burst of pleasure nearly takes your breath away."
    V "Are you sick of that one yet? I could try a different one..."
    "Bzz... Bzz... BZZZ! Bzz... Bzz... BZZZ!"
    "The new rhythm - shorter and quicker - is less intense, but never pauses for you to relax."
    "Bzz... Bzz... BZZZ!"
    V "That's a good one, isn't it?"
    "Bzz... Bzz... BZZZ!"
    pcname "V-Violet..."
    V "Ah-ah, we're alone right now. What do you call me?"
    "Bzz... Bzz... BZZZ!"
    pcname "M-Mistress..."
    "Bzz... Bzz... BZZZ!"
    "Shuddering, you cling to the steering wheel, panting for breath."
    "Bzz... Bzz... BZZZ!"
    pcname "P-please... I can't..."
    "The vibrations stop and Violet chuckles."
    V "Okay, fine. I'll be nice."
    V "For {i}now{/i}..."
    "You're still quivering when you pull up in front of her house."
    "The driver approaches the car, opening each of the doors and taking the keys."
    if club == "track":
        "You look away, hoping he can't tell how aroused you are."
    elif club == "cheer":
        "You smile, wondering if he can tell how aroused you are."
    elif club == "yearbook":
        "You hurry away, sure that he can tell how aroused you are."
    "Again, the butler opens the front door, greeting you both."
    show bg LuxParty with dissolve
    "Violet ignores him, leading you through the foyer and upstairs."
    "She waits for you to open her bedroom door. Stepping inside, she waits for the door to close before pulling the remote out again."
    scene black with fade
    V "I want you in nothing but those heels and those panties. Take the rest off."
    "Swallowing hard, you grab the neck of the dress and slip it over your shoulders."
    "It slips to the floor, pooling around your feet."
    "Unhooking your bra, you toss it aside and step out of the dress."
    "Violet eyes you up, a slow, lewd smile spreading over her lips."
    "Taking a seat on one of the cushioned chairs, she flips the skirt of her dress to one side and spreads her legs."
    show bg VDomAD1 with dissolve
    "You gasp; she's not wearing any panties."
    V "Like what you see?"
    "Reaching behind her neck, she pulls the string holding her top up."
    show bg VDomAD2 with dissolve
    "It slides down, baring her breasts; her nipples immediately tense in the open air."
    "Somehow, Violet's casual nudity makes her look even more powerful, while your own just makes you feel more exposed."
    V "Well? I asked if you like what you see."
    "Your mouth is suddenly dry, but you force the words out in a husky whisper."
    pcname "Yes, Mistress."
    "She smiles, leaning back in the chair and spreading her legs over its arms."
    V "Ready for your dessert?"
    "Sinking to your knees, you crawl across the floor to Violet's chair."
    show bg VDomAD3 with dissolve
    "As you lay your hands on the insides of Violet's knees, your panties begin to vibrate again."
    "Bzz... Bzz... BZZZ!"
    "Shuddering, you lean forward to kiss Violet's thighs."
    show bg VDomAD4 with dissolve
    V "Mmmm..."
    "Bzz... Bzz... BZZZ!"
    "The vibrator thrums against your clit, sending waves of pleasure through your abdomen."
    "You kiss your way up her thighs, pausing as your panties pulse again."
    "Bzz... Bzz... BZZZ!"
    V "Keep going. You're not allowed to cum until I do."
    "The scent of her pussy fills your nose as you lean down to kiss the top of it."
    "Bzz... Bzz... BZZZ!"
    "Your tongue delves into its folds, tasting the sticky nectar."
    show bg VDomAD5 with dissolve
    "Bz..."
    "You stiffen, recognizing the new rhythm."
    "Bzz..."
    "Drawing your tongue up and down her slit, you lick the length of her cunt."
    V "Mmmm~"
    "Bzzz..."
    "Slipping your tongue into her, you flick it up and down, back and forth."
    "Bzzzz..."
    V "Ahh~"
    show bg VDomAD6 with dissolve
    "BZZZZZ!"
    "Shuddering, you try to ignore the pleasure running through you."
    "Bz..."
    "The wetness of your panties..."
    "Bzz..."
    "The way your clit throbs..."
    "Bzzz..."
    "You focus on Violet, thrusting your tongue in and out of her pussy, lapping up her juices."
    "Bzzzz..."
    V "Oh~"
    "BZZZZZ!"
    "Your whole body tenses as another wave of pleasure crashes over you."
    "It's too much. You're too close..."
    "Bz..."
    "Fighting back the sensations threatening to overwhelm you, you run your tongue up and down Violet's slit."
    "Your own juices soak through your panties, running down your thigh."
    "Bzz..."
    "Dipping your tongue inside of her, flicking it over her clit, you do everything you can to bring her to a climax."
    V "Ohhh~"
    "Bzzz..."
    "Near panic, you flick your tongue over her clit as fast as you can, desperate to make her cum."
    V "Oh fuck..."
    "Bzzzz..."
    "Her thighs tense; you know she's close."
    "Running your hand down her thigh, you press two fingers into her dripping cunt."
    show bg VDomAD7 with dissolve
    V "Ohh!"
    "You hold your breath, trying to weather the next pulse of vibration."
    "BZZZZZ!"
    "Your clit throbs with a pleasure so strong it drags an unwilling moan from your throat."
    V "Not yet!"
    "Exhaling through your nose, you thrust your fingers up, rubbing them hard against her g-spot."
    "Bz..."
    "She moans as your mouth fastens on her clit, sucking hard."
    "Bzz..."
    "Her hand grips your hair, pushing your face further against her."
    V "Oh fuck~"
    "Bzzz..."
    "Sucking her clit, you rub her g-spot harder; her pussy clamps down on your fingers."
    "She's close, you just have to..."
    "Bzzzz..."
    V "I'm... gonna... gonna..."
    show bg VDomAD8 with dissolve
    "Violet cries out as her legs stiffen. Her thighs clamp around your face and she shudders against you."
    "As her thighs relax, you pull your head back and cry out, surrendering to your own orgasm."
    "BZZZZZ!"
    show bg VDomAD9 with dissolve
    "Pleasure thunders through you, leaving you quivering and breathless."
    "Your panties keep vibrating, prolonging the orgasm until you can barely stand it."
    pcname "M-Mistress, please..."
    "Smiling down at you, she holds the remote up, her finger on the power button."
    pcname "{i}Please{/i}..."
    "Finally, she relents. As the vibrations stop, you slump forward, resting your face on her thighs."
    show bg black with dissolve
    V "Did you enjoy that?"
    "Heavy with pleasure, you struggle to speak."
    pcname "Y-yes... Th-thank you."
    V "Very good."
    "She sighs contentedly, her fingers falling from your hair."
    V "I'll have the driver take you home, since you don't have a change of clothes for school tomorrow."
    V "Maybe we should buy you some to keep here, just in case."
    "Nodding, you pull yourself to your feet and start dressing."
    "Violet watches, not bothering to cover herself."
    "Your eyes are drawn to her, her wet pussy glistening, her nipples standing in taut pink peaks."
    V "Have a good night, [pcname]."
    pcname "Thank you, Mistress. I already have."
    "She smiles again, watching you leave."
    $ clothes, hair = casualwear
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
