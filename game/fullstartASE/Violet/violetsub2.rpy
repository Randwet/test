label violetsub3:
    show bg Cafeteria with fade
    show V SubSchool Blank at left with moveinleft
    show chelsea at right with moveinright
    "At lunch, Violet returns with your tray - it's perfect this time."
    "You debate how to react: you could praise her, but she seems to like getting in trouble..."
    menu violetsub3_compliment:
        "Good job." if True:
            show V SubSchool Happy at left
            show chelsea happy
            "She smiles a little."
            V "Thank you, [pcname]."
        "Finally got it right, huh?" if True:
            show V SubSchool Worried at left
            "She flushes."
            V "Yes, [pcname]. I learned from last time."
            if club == "track":
                show chelsea happy
                "You nod, satisfied."
                pcname "Good!"
            elif club == "cheer":
                show chelsea happy
                "You smile at the memory."
                pcname "I bet you did..."
            elif club == "yearbook":
                show chelsea embarrassed
                "You flush a little yourself."
                pcname "I'm glad..."
    show V SubSchool at left
    show chelsea blank
    "Violet watches you, waiting for you to take a bite so that she can start eating too."
    menu violetsub3_eat:
        "Take a bite." if True:
            "Feeling generous, you take a bite of your sandwich and nod at her."
            show V SubSchool Happy at left
            "She lowers her eyes, acknowledging your permission, and takes a bite of her own sandwich."
        "Make her wait." if True:
            "Ignoring her, you play around on your phone for a minute or two while watching her."
            "She shifts impatiently in her chair, obviously hungry."
            show V SubSchool Sad at left
            "Her eyes meet yours - you smile a little and go back to your phone."
            "When you look up again, she's sitting still with her eyes downcast."
            show chelsea happy
            "Pleased, you lift your sandwich and take a bite."
            show V SubSchool Happy at left
            "She glances up at your face; you nod and she begins eating."
    show V SubSchool Blank at left
    V "So, [pcname]... I was wondering..."
    show chelsea confused
    pcname "About?"
    show chelsea blank
    V "There's a party I was invited to this Saturday. The host is the son of one of my father's coworkers; I've never even met him."
    V "I won't know anyone there, but I thought it might be fun if we went together."
    show chelsea shocked
    pcname "Oh?"
    show chelsea blank
    show V SubSchool Worried at left
    V "If you wanted, you could pretend to be me..."
    V "...and I could be your personal assistant."
    "You consider it a moment. It {i}would{/i} be a great chance to have some fun..."
    menu violetsub3_datedecision:
        "Let's do it!" if True:
            show chelsea happy
            $ violetdateflag = True
            $ violetapproval += 1
            if club == "track":
                pcname "Sounds like a good time!"
            elif club == "cheer":
                pcname "That could be fun..."
            elif club == "yearbook":
                pcname "I think we could do that..."
        "Rather not." if True:
            if club == "track":
                pcname "Nah. Not into lying to people."
            elif club == "cheer":
                pcname "I have other plans that day, actually."
            elif club == "yearbook":
                pcname "That would be a lot of people..."
                pcname "I don't think I can do that..."
            show V SubSchool Sad at left
            "Violet opens her mouth to protest, but quickly remembers her place."
            V "You're right. I'll just make an appearance and leave."
            "She's quiet for the rest of lunch. You know she's disappointed, but she does a good job keeping it to herself for once."
            jump events_end_period
    show V SubSchool Happy at left
    V "Great. So I'll pick you up Saturday?"
    if club == "track":
        pcname "Sounds good!"
    elif club == "cheer":
        pcname "It's a date!"
    elif club == "yearbook":
        pcname "Yep!"
    "You chat together over lunch, and when the bell rings Violet dumps your tray for you."
    "As you walk to your next class, you think about the party."
    if club == "track":
        "You have the confidence to pull it off, but Violet..."
        pcname "I guess we'll see if she can handle it."
    elif club == "cheer":
        "You already have a few ideas..."
        "You enter the classroom still smiling to yourself."
    elif club == "yearbook":
        show chelsea embarrassed
        "You're nervous, but the thought of people treating you the way they treat Violet..."
        "A chill of anticipation courses through you."
    jump events_end_period

label violetsub3_date:
    $ violetdatescore = 0
    $ violetdateflag = False
    $ clothes, hair = casualwear
    play sound PhoneVibration
    "Your phone vibrates."

    call screen TextingScene("Violet",
    [
        TextMessage("I'm leaving soon"),
        TextMessage("Hope you're ready for the party")
    ])

    menu violetsub3_cancel:
        "Get ready." if True:
            pass
        "Cancel." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("Sorry, I can't today", sender = False),
                TextMessage("You'll have to go without me", sender = False),
                TextMessage("What?"),
                TextMessage("I mean"),
                TextMessage("Is everything okay?"),
                TextMessage("Yes thx", sender = False),
                TextMessage("Have fun!", sender = False)
            ])

            "You can't help but smile."
            "She was obviously mad, but she held it in check."
            "Clearly learning to be submissive is helping her self-control. It almost makes you regret cancelling."

            jump eventengine

    show chelsea at right with moveinright
    show bg RoomE with dissolve
    "You walk into the bedroom and look yourself over."
    "Just as you finish getting ready, you get another text."

    call screen TextingScene("Violet", [TextMessage("I'm here!")])

    show bg black with dissolve
    "You head outside. Violet is standing by the car, already holding the door for you."
    show bg CityE with dissolve
    show V SubCasual Happy at left with moveinleft
    V "Ready, Miss Violet?"
    show chelsea laugh
    "You slide into the back seat and buckle your seatbelt while Violet walks around the car."
    hide V SubCasual Happy with dissolve
    show chelsea happy
    "She slips in, plugging her phone into the aux cord and turning on music."
    "As she drives, you both tease each other using the other's name."
    "It's silly, but by the time you arrive you feel like you might not forget to answer to Violet now."
    "Just as you start feeling confident, though, Violet pulls up to a large gate and speaks into a speaker."
    V "Miss Violet Atwood."
    show chelsea shocked
    "The gate opens and Violet drives inside, down a long, smooth driveway, only stopping when she rounds a large fountain."
    "Two men approach the car, opening each of your doors and ushering you out."
    show chelsea blank
    "Violet drops the keys casually into one of their hands - you realize with a start that they are {i}valets{/i}."
    show chelsea shocked
    if club == "track":
        show chelsea shocked
        "You barely know what a valet {i}is{/i}."
    elif club == "cheer":
        show chelsea shocked
        "You've only seen them in movies!"
    elif club == "yearbook":
        show chelsea shocked
        "You've seen them mentioned in books, but you never imagined you'd be somewhere that had one..."
    "And this isn't even a fancy hotel - it's someone's house!"
    show V SubCasual Blank at left with moveinleft
    show chelsea blank
    "Violet quirks a brow at you, clearly amused, and you remember that you're supposed to be her tonight."
    if club == "track":
        show chelsea happy
        "It's a good thing you like a challenge!"
    elif club == "cheer":
        show chelsea happy
        "This should be fun!"
    elif club == "yearbook":
        "You swallow hard and try to look confident."
    show chelsea blank
    show V SubCasual Happy at left
    show bg black with dissolve
    show bg LuxParty with dissolve
    "Violet leads you into the house, introducing you as Violet Atwood - and herself as your personal assistant, [pcname]."
    "An attractive man, only a few years older than you, beams at you."
    show V SubCasual Blank at left
    "Niles" "Violet! So glad you could make it. I'm Niles Bradford."
    "He takes your hand, squeezing it gently, and meets your eyes."
    show chelsea shocked
    "Your heart skips a beat; his eyes are {i}so{/i} blue!"
    "Niles" "You have to meet Jessica - our fathers were all in the same graduating class..."
    show chelsea happy
    "He ignores Violet entirely, whisking you away to meet several men and women."
    "They're all beautifully dressed - much better than you are - and their demeanor makes it quite clear that you're in a different world right now."
    "And yet... When they hear your name - Violet's name - they seem {i}excited{/i}."
    "Niles leaves you with a small group of people while he goes to welcome the rest of his guests."
    if club == "track":
        "You listen to them speak. They're only people, so you're sure you can hold your own."
        "Occasionally, you catch one of them watching you."
        "It feels amazing to be so important."
    elif club == "cheer":
        "You listen to them speak, excited to be included in such an elite group."
        "Occasionally, you catch one of them watching you, and you can't help but enjoy the attention."
    elif club == "yearbook":
        "You listen, feeling more than a little nervous."
        "Occasionally, you catch one of them watching you."
        "It's weird - and intimidating - but it makes you feel good too. Powerful."
    show chelsea blank
    "Suddenly, everyone's attention is on you."
    "James" "That's right, you've been going to Uni High, haven't you?"
    "Darcy" "I forgot about that! You poor thing..."
    "Jessica" "What? Why would you go {i}there{/i}?"
    "James" "Her father made a comment during his campaign that he stands by our public schools."
    "James" "When his rival challenged him, he said that his own daughter would attend a public school."
    "You'd often wondered why Violet's family hadn't sent her to a private school..."
    "Darcy" "It must have been awful. You're probably so happy to be a senior this year..."
    "Jessica" "Where {i}are{/i} you planning to go to college?"
    show chelsea shocked
    "For a moment, you panic."
    show chelsea happy
    "But then you remember: they don't know who you are and you'll never see them again."
    "It's freeing. You can say whatever you want."
    menu violetsubparty_college:
        "Make something up." if True:
            show V SubCasual Sad at left
            show chelsea confused
            pcname "Oh, me? I--"
            pcname "I'm going to Uni University, I guess."
            show chelsea blank
            "They all gasp."
            "Jessica" "But that... That's so {i}common{/i}. It's another public school, you know?"
            "Darcy" "They make everyone stay in dorms. {i}Everyone{/i}."
            "James" "Not just dorms. Shared with not one, but {i}two{/i} roommates."
            show V SubCasual Worried at left
            "You glance at Violet as they speak. She's staring at the floor, her cheeks flushed."
            "Clearly you've embarrassed her."
            "And she's cute when she's embarrassed."
        "Deflect to Violet." if True:
            show chelsea confused
            $ violetdatescore += 1
            pcname "Oh, [pcname], which one was it?"
            show V SubCasual Happy at left
            show chelsea blank
            "Violet smiles, shrugging."
            V "Three schools have tried to recruit you, Miss Atwood, but you insisted on taking a year off to travel before you would {i}consider{/i} one of them."
            "Jessica" "Three?"
            "Darcy" "Three {i}private{/i} schools are trying to recruit you?"
            "James" "I'm hardly surprised. The Atwoods are known around here."
            show chelsea happy
            "You smile, hoping it seems both gracious and proud, and the conversation moves on."
    show V SubCasual Blank at left
    show chelsea blank
    "Darcy" "I almost forgot! Selena Kohl's new line was released today!"
    "Jessica" "I know! There's already a waiting list..."
    "James" "I guess you didn't get anything then, hmmn?"
    "Darcy" "I bet Violet did, though."
    "All eyes fall on you once again."
    menu violetsubparty_selena:
        "Make something up." if True:
            show chelsea happy
            if club == "cheer":
                pcname "Oh, yeah, I bought something."
                show V SubCasual Worried at left
                "Darcy" "Something?"
                "James" "Yes, {i}which{/i} something?"
                pcname "Just... shoes."
                "They eye you skeptically - you're sure they don't believe you."
                $ violetdatescore -= 1
            elif club == "track":
                pcname "Oh, well... I wasn't that impressed, honestly."
                show V SubCasual Worried at left
                "Darcy" "{i}What{/i}!?"
                "Jessica" "You weren't {i}impressed{/i} by {i}Selena Kohl{/i}?"
                "James snorts in disbelief."
                "They eye you skeptically, unsure whether to believe you or not."
            elif club == "yearbook":
                show chelsea confused
                pcname "Um... Who?"
                show V SubCasual Sad at left
                "Jessica laughs - until she realizes you aren't joking."
                "Darcy" "She's... She's {i}Selena Kohl{/i}."
                pcname "Right, but... Who is that?"
                "James fans himself dramatically while the girls gape at you."
                "It's clear that you {i}should{/i} have known who she is."
                $ violetdatescore -= 1
            show chelsea blank
            "As they resume their discussion of the new line, you spare Violet a glance."
            "Her face is redder than you've ever seen it; she looks mortified."
            "You're struck again by how attractive she is when she's embarrassed."
            "Is that what she'll look like when her face flushes during--"
        "Deflect to Violet." if True:
            $ violetdatescore += 1
            pcname "[pcname], I did get {i}something{/i}, didn't I?"
            show V SubCasual Happy at left
            V "Yes, Miss Atwood. Three dresses and two purses were delivered this morning."
            "The girls' mouths drop open and James's brows shoot toward his hairline."
            "They're all {i}very{/i} impressed."
            "Darcy" "Violet, you're--"
    show chelsea blank
    show V SubCasual Blank at left
    "A familiar voice cuts in - you didn't even hear Niles approach."
    "Niles" "Sorry, but I'm afraid I need to borrow Violet for a moment. If you'll excuse us?"
    "He gestures for you to walk with him, ignoring Violet trailing behind you."
    "Niles" "I hope you're enjoying the party so far?"
    if club == "track":
        pcname "It's not bad."
    elif club == "cheer":
        show chelsea happy
        pcname "You have a lovely house."
    elif club == "yearbook":
        show chelsea happy
        pcname "It's... nice."
    "Niles" "I was thrilled when my father told me he'd invited you."
    "He stops, turning toward you, and leans in, speaking softly."
    show chelsea blank
    "Niles" "I've wanted to meet you for a while, Violet."
    show chelsea shocked
    "Your heart races; he's flirting with you!"
    "You want to see Violet's reaction - is she jealous? Angry? - but Niles is waiting for a response."
    menu violetsubparty_niles:
        "Flirt with him." if True:
            $ nilesflirt = True
            if club == "track":
                show chelsea happy
                pcname "Have you?"
                "Niles" "Yes. And I'm not disappointed."
            elif club == "cheer":
                show chelsea confused
                pcname "And now?"
                "Niles" "Now I'd like to get to know you better."
            elif club == "yearbook":
                show chelsea confused
                pcname "You did?"
                "Niles" "From the moment I heard your name."
            show chelsea blank
            "He's certainly coming on strong and, despite how handsome he is, it just seems... silly."
            "He doesn't know who you are at all. Or who Violet is."
            "If he's interested in you - or her - it's only because of her father's money."
            "Niles" "I hope we can speak again sometime? Maybe more privately?"
            "Niles" "Dinner next weekend, perhaps?"
            show chelsea shocked
            pcname "Oh, I-"
            show chelsea happy
            "An idea strikes you."
            show chelsea blank
            pcname "I'll have my assistant, [pcname], check my schedule and get back to you."
            "He smiles, not the least put off by that."
            "Niles" "As much as I'd like to, I can't ignore my other guests."
            "Niles" "I'll be waiting for your assistant's call."
            "He winks as he turns away from you."
        "Brush him off." if True:
            $ violetdatescore -= 1
            if club == "track":
                show chelsea confused
                pcname "Really? I hadn't heard about you until my father told me about this party."
            elif club == "cheer":
                show chelsea blank
                pcname "I hear that a lot, actually."
                "You brush past him and look around, as if bored."
            elif club == "yearbook":
                show chelsea embarrassed
                "You try to discourage him, but you can't seem to think of anything to say."
                pcname "I- I-"
                "A painting catches your eye and you blurt out the first thing that comes to mind."
                show chelsea shocked
                pcname "That's an ugly painting!"
            "He looks annoyed, but hides it quickly."
            "Niles" "I apologize. I should get back to my guests. Perhaps we'll speak another time."
            "He smiles tightly, inclining his head, and practically flees from your side."
    show chelsea blank
    pcname "I think that's enough excitement for the night, don't you?"
    show V SubCasual Worried at left
    "Violet nods her head, face flushed, but doesn't speak - is she upset, you wonder?"
    show bg black with dissolve
    "As you leave, she holds the door for you."
    "The valets get the car doors. You're surprised by your own disappointment; it's nice having Violet do things for you."
    show bg CityD with dissolve
    "As she pulls out of the big gate, you meet her eyes in the mirror."
    show V SubCasual Blank at left
    V "That was... strange."
    if violetdatescore < 2:
        show V SubCasual Sad at left
        V "And... mortifying."
        V "I've never been so embarrassed. The things you said to those people..."
        "She shakes her head."
        show V SubCasual Blank at left
        V "But the entire time, I was so helpless and... {i}I liked it{/i}."
    elif True:
        show V SubCasual Happy at left
        V "But you were great. I would never have thought you could act so well."
        V "Honestly, it was pretty hot, watching the way you handled all of them..."
    show V SubCasual Worried at left
    V "I've never been ignored like that."
    V "It was amazing, being able to look around the room without worrying what people thought about me."
    V "I never realized how good it would feel to be so unimportant."
    "She pulls into your apartment building and circles around the car to open your door."
    show V SubCasual Happy at left
    "As you step out, she smiles."
    V "Time to say goodnight, I guess..."
    $ acts -= 2
    menu violetsubparty_night:
        "Kiss her." if True:
            show V SubCasual Blank at left
            show chelsea happy
            if club == "track":
                "Grabbing her by the shoulders, you push her against the car and sink against her."
                "Your lips crush against hers as you kiss her roughly."
                "She whimpers, surprised by the force of your kiss, but opens her mouth eagerly."
                "As your tongues dance together, she brings one hand up to cup the side of your face."
                "Eventually you draw back, breathless, and smile down at her."
                show V SubCasual Happy at left
                V "What was that for?"
                pcname "I thought you deserved a reward for being so well behaved tonight."
            elif club == "cheer":
                "Pressing your body to hers, you push her back against the car and claim her lips with your own."
                "Your lips move over hers softly, drawing a sigh as she parts them before your tongue."
                "As your tongues dance together, she cups your face with one hand, letting it curl into your hair."
                "Eventually you draw away, breathless, and smile down at her."
                show V SubCasual Happy at left
                V "What was that for?"
                if violetdatescore <3:
                    pcname "I couldn't help it. You are too cute when you're embarrassed."
                elif True:
                    pcname "You did a great job tonight, so I thought I'd give you a little treat..."
            elif club == "yearbook":
                "Still reeling from your feelings at the party, you feel powerful and in control."
                "Emboldened, you push her back against the car, smiling at her look of shock, and press your lips to hers."
                "She melts against you, her lips parting under yours, inviting you to do whatever you want."
                "You slip your tongue past her lips, exploring her mouth."
                "Finally, breathless, you pull away and smile down at her."
                V "Wow... What was that for?"
                pcname "I just... wanted to."
                show V SubCasual Happy at left
                "She smiles."
                V "Good enough for me."
            show V SubCasual Blank at left
            "As you step back, she sighs."
            show chelsea blank
            V "I really wish I didn't have to go home tonight."
            "She glances at you slyly."
            show V SubCasual Happy at left
            V "Next time, do you think we could spend a little... private time together?"
            show V SubCasual Blank at left
            show chelsea happy
            "You know what she's asking; you smile."
            show chelsea laugh
            pcname "Maybe. If you're {i}really{/i} good."
            show V SubCasual Happy at left
            "She smiles back."
            V "I guess I'll be on my best behavior then."
            show V SubCasual Blank at left
            show chelsea blank
            V "May I leave now?"
            "Lifting your fingers to her face, you draw your thumb gently across her lower lip."
            "It's soft, and still moist from your kiss."
            show chelsea happy
            pcname "I suppose so..."
            "She bites her lip and sighs."
            V "I {i}really{/i} want some time alone with you..."
            "You can't help but giggle - it feels good to have this kind of affect on someone."
            "You watch her get back in the car, only going into your apartment when she's driven out of sight."
            jump events_end_period
        "Ask her how much she enjoyed tonight." if True:
            show V SubCasual Worried at left
            "She blushes immediately."
            V "Honestly, I..."
            if violetdatescore <3:
                V "I was really embarrassed, but..."
                V "It kinda made me..."
            elif True:
                V "You were amazing. You were in complete control of the situation..."
                V "It... kinda made me..."
            show V SubCasual Blank at left
            show chelsea shocked
            "She reaches for your hand, pulling it under her dress, and presses your fingers against her panties."
            show V SubCasual Worried at left
            "You can feel how wet they are; she turns her face away to hide her embarrassment and releases your hand, having made her point."
            show chelsea happy
            if club == "track":
                "Heart pounding, you run your fingers up and down the hot wetness, enjoying how the fabric dips slightly between her pussy lips."
            elif club == "cheer":
                "Licking your lips, you run your fingers up and down the hot wetness, aware of the heat filling your own panties."
            elif club == "yearbook":
                "With trembling hands, you run your fingers up and down the hot wetness, aware that you're both standing outdoors where anyone could see."
            show V SubCasual Blank at left
            "She gasps, her eyes fluttering shut as she tilts her head back."
            "You press harder, stretching her panties between her labia and rubbing across her clit."
            "Violet reaches back to grasp the car, swaying unsteadily."
            V "[pcname]..."
            "A car door slams shut across the street, startling you both."
            show chelsea shocked
            show V SubCasual Sad at left
            "Violet jumps back with a yelp, then giggles."
            show chelsea happy
            V "I really wish I didn't have to go home tonight."
            "She glances at you slyly."
            V "Next time, do you think we could spend a little... private time together?"
            "You know what she's asking; you smile."
            pcname "Maybe. If you're {i}really{/i} good."
            show V SubCasual Happy at left
            "She smiles back."
            V "I guess I'll be on my best behavior then."
            V "May I leave now?"
            "Lifting your fingers to her face, you draw your thumb gently across her lower lip."
            pcname "I suppose so..."
            "She bites her lip and sighs."
            V "I {i}really{/i} want some time alone with you..."
            "You can't help but giggle - it feels good to have this kind of affect on someone."
            "You watch her get back in the car, only going into your apartment when she's driven out of sight."
            hide V SubCasual Happy with dissolve
            $ violetdateflag = False
            jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
