label MattMafiaResolution:
    scene bg School with fade
    "As you step into school for the day, there is a sudden, choking atmosphere around the halls."
    "Panic settles into your chest. Did Matt get those photos out before Jun and his friends could do anything?"
    scene black with dissolve
    "You keep your head down and ears perked as you walk through the halls, straining to overhear what everyone is whispering about."
    show chelsea at center, enterScene(1.0, 0.5, 0.6, 0.6)
    pause 1.5
    show chelsea shocked
    "To your surprise, no one pays you any attention-- in fact, they don't even seem to notice you're there."
    show chelsea confused
    "If Matt released the photos, they would be talking about you, right? So why hasn't anyone even glanced in your direction?"
    show bg ClassroomD behind chelsea with dissolve
    hide black
    pause 0.5
    show chelsea shocked
    V "[pcname]! There you are."
    show V School Smile at left, enterScene(-0.5, 0.0, 0.6, 0.6)
    V "Have you heard the news?"
    show chelsea blank
    "You look up to see Violet half-walking and half-strutting toward you down the hall, her eyes lit up with excitement and curiosity."
    show V School Pout
    show chelsea confused
    pcname "No, what news?"
    show V School Blank
    show chelsea shocked
    V "Matt's missing. Like, {i}actually{/i} missing."
    show V School Smile
    show chelsea sad
    V "Apparently he didn't come home last night. It's too soon for his mom to put out a missing person's report, but she hasn't stopped harassing kids and their parents all night."
    show V School Pout
    pcname @ shocked "O-Oh. Wow."
    "Matt. Missing. You aren't sure how to feel about it; this is what you asked for, right? But suddenly it all feels so real, maybe too real."
    if club == "track":
        pcname @ angry "{i}It's what he deserves. At least he can't try to blackmail me now.{/i}"
    elif club == "cheer":
        pcname @ angry "{i}If I didn't do it, someone else was going to. I hope those photos got deleted.{/i}"
    elif club == "yearbook":
        pcname "{i}T-This is okay, right? At least he can't blackmail me now...{/i}"
    show V School Annoyed
    show chelsea blank
    V "I think she's totally overreacting; Matt is a little prick that does whatever he wants. He probably passed out with his hand down his pants in an alley somewhere."
    show V School Pout
    show chelsea embarrassed
    pcname "Yeah, maybe..."
    show V School Smile
    show chelsea blank
    V "I had no idea his mom was such a helicopter parent, though! How embarrassing. I'd die if my parents harassed the school like this."
    show V School Blank
    V "Speaking of, did you hear about Andrea? She was caught trying to OD in chem--"
    hide V School
    hide bg ClassroomD
    show black behind chelsea
    with dissolve
    "You tune Violet out as she goes on yet another high school gossip tangent, her interest immediately veering off onto another track."
    show chelsea embarrassed
    "Jun and his gang really came through. You smile a little to yourself as you move onto class, the fear of Matt's blackmail fading behind you."
    jump events_end_period

label MattMafiaResolution2:
    scene bg School with fade
    "A week passes without sight of Matt. It's maybe the best week of your life-- no one texting you to randomly meet him for a quickie in the bathroom, no constant beration over your looks and behavior."
    "School has actually become a safe place for you. Mostly."
    show chelsea at center, enterScene(1.0, 0.5, 0.6, 0.5)
    pause 1.5
    show chelsea confused
    "As you head to school for a fresh new week of Matt-free classes, you notice a strange abundance of police cars parked around the school grounds."
    "Their lights flash red and blue over the wet parking lot, their flashes blurred by the onslaught of rain outside."
    show chelsea blank
    "Closing your umbrella, you duck into the safety of the building."
    scene black with fade
    "There are no signs of the owners of said police vehicles, but you can sense the electric buzz of excitement among the students and the concern among faculty."
    show V School Pout at left
    show chelsea shocked at left, moveSprite(0.2, 0.2, 0.0)
    with dissolve
    "Violet grabs your elbow almost as soon as you enter, yanking you to her side."
    show V School Smile
    show chelsea confused
    V "You won't believe what happened."
    show bg ClassroomD behind chelsea, V
    show Alice Confused at center, moveSprite(0.7, 0.7, 0.0)
    hide black
    with dissolve
    show chelsea blank
    show V School Pout
    pause 1.0
    hide Alice with dissolve
    pause 0.5
    show FPO at center, moveSprite(0.7, 0.7, 0.0)
    show Sophie Shy at center, moveSprite(0.8, 0.8, 0.0)
    with dissolve
    "As Violet leads you down the hall, you now see where all the cops went; they've occupied one of the empty classrooms, using it as an interrogation room. A confused student leaves, and an officer returns with a replacement."
    hide FPO
    hide Sophie
    with dissolve
    pause 1.0
    show chelsea sad
    "You shudder."
    show chelsea confused
    pcname "What happened? Why are all these cops here?"
    show chelsea sad
    "But deep in your conscious, you know. You know exactly why they're here; Matt is missing, and it's your fault."
    "And now they want to find him."
    if club == "track":
        show chelsea sad
        pcname "{i}But I don't even know where he is. Even if they asked me, I wouldn't have an answer for them.{/i}"
        "Somehow, that doesn't make you feel any better."
    elif club == "cheer":
        show chelsea angry
        pcname "{i}Maybe if he hadn't tried blackmailing me, he wouldn't be missing. It's a good thing Jun didn't tell me anything.{/i}"
        show chelsea sad
        "But a small pang of guilt stabs at you anyway."
    elif club == "yearbook":
        show chelsea sad
        pcname "{i}O-Oh no. What if they find out I was behind it? I-I have no idea what Jun did, but if they interrogate me, what will I say?{/i}"
        "Guilt consumes you, squeezing your chest tight."
    show V School Smile
    show chelsea blank
    V "It's kind of obvious, isn't it?"
    show V School Pout
    "You look at Violet blankly. She smirks and leans forward to whisper in your ear."
    show chelsea shocked
    show V School Smile
    V "They found Matt's body, and now they need to find the killer."
    show chelsea sad
    "You feel your heart jump into your throat. Oh no. Oh no, oh no, {i}oh no--{/i}"
    show V SubSchool Happy
    "Violet pulls back and laughs."
    show chelsea shocked
    V "I'm kidding! God, learn to take a joke, [pcname]. You look like you've seen a ghost."
    show V School Blank
    show chelsea blank
    V "He's still missing, though. They think someone close to him might know something."
    if club == "track":
        show chelsea angry
        show V SubSchool Happy
        pcname "Ugh, Vi, seriously?"
        "You channel your relief into annoyance instead. She nearly gave you a heart attack."
    elif club == "cheer":
        show chelsea angry
        show V SubSchool Happy
        pcname "Vi! Ugh, you're the worst! You totally freaked me out."
        "You pout at her in irritation."
    elif club == "yearbook":
        show V School Pout
        show chelsea blank
        pcname "O-Oh..."
        show chelsea embarrassed
        "You breath out an unsteady sigh of relief. At least you don't have to put {i}murderer{/i} on your resume anytime soon."
    show chelsea confused
    show V School Pout
    pcname "Are they talking to everyone in the school then?"
    show chelsea blank
    "You try to keep your voice light and casual as you follow Violet through the hall, but getting the words out feels like someone is clawing them from your throat."
    "Violet shrugs."
    show V School Blank
    V "I don't know. They haven't talked to me yet, but Matt's been shitty to everyone here. It wouldn't surprise me if someone here was involved."
    show chelsea shocked
    show V School Smile
    V "You know, this reminds me of the time my nanny tried to kidnap me for ransom as a kid."
    show V School Blank
    V "She didn't get far, though; the security guards shot her down before she made it to the gate."
    show V School Pout
    show chelsea sad
    "Violet says this casually and nonchalantly, even inspecting her nails as she talks without a care in the world."
    show chelsea shocked
    hide V with dissolve
    "The bell rings, startling you. Violet doesn't notice your jumpy attitude as she turns and walks in the opposite direction to class."
    show chelsea sad
    pause 1.0
    hide chelsea with dissolve
    "You shuffle to your own classroom, your chest weighed down with stress."
    "The panic doesn't subside in class, or after, or even at lunch."
    scene bg Cafeteria with fade
    "The police haven't interrogated you, but you've seen several students pulled from class and returned some time later, going through their day as if nothing happened."
    show chelsea happy with dissolve
    pause 1.0
    show MPO at left with dissolve
    show chelsea sad
    "As you bite into your pizza at lunch, you notice an officer approach your table. Your throat tightens, a sudden panic settling in."
    show MPO at exitScene(0.0, 0.7, 0.7, 0.7)
    pause 1.0
    show chelsea embarrassed
    "It's only when he passes by you, his sights set on another student, that you let out a shaky breath."
    show chelsea sad
    "How are you supposed to get through the rest of the day like this?"
    show chelsea shocked
    "Your phone suddenly buzzes on the table, and you have to hold back a shriek as you're startled by the noise."
    show chelsea sad
    "You shakily pick up the device and look it over."
    call screen TextingScene("Jun",
    [
        TextMessage("You forgot your keys at karaoke the other night."),
        TextMessage("Meet me at 1316 Sturgent Avenue at 4pm."),
    ])
    show chelsea confused
    pcname "My keys?"
    "You regard the message for a moment in confusion. Did Jun text the wrong person? You definitely didn't forget your keys; how else would you have gotten home?"
    show chelsea shocked
    "Then, realization clicks. There's no way he could give you the real reason for meeting him, not over text."
    show chelsea blank
    "You type the address into your phone's GPS. It's an old mattress warehouse in the southside."
    show chelsea happy
    "If that isn't a message, you don't know what is."
    call screen TextingScene("Jun",
    [
        TextMessage("Thanks, I've been looking everywhere for them.", sender = False),
        TextMessage("I'll meet you there.", sender = False),
    ])
    show chelsea blank
    "Jun doesn't respond, but you don't need him to. Whatever is happening around the school, with the police, with Matt-- you can tell Jun everything when you see him. He'll know what to do."
    show chelsea sad
    "Now you just need to make it through the rest of the day."
    scene black with fade
    "It's easier said than done-- school drags on, and each near police encounter leaves you with an increased heart rate and a sick, sinking sensation in your stomach."
    "You don't even bid your friends at school goodbye as you rush to the train station downtown."
    scene black with dissolve
    pause 0.5
    "The warehouse, surprisingly, still looks in use. Men steer large pallets of sealed mattresses into moving trucks, lost in the daily operation of their jobs."
    "Diego stands among them, ordering workers around for where to place which pallet."
    show chelsea with dissolve
    "He stops when he sees you approach, a smile breaking out on his face."
    show Wareworker at right with dissolve
    "Diego" "Mija! Right on time. Give me just a second-- Oi! Those go in the red truck! What, are you deaf?"
    hide Wareworker with dissolve
    "Diego storms off momentarily to yell at one of the employees. You catch a glimpse of the pallet marked separately with red paint, although you can't tell its purpose."
    "The worker apologizes before moving the pallet to the correct truck. Diego shakes his head as he walks back, muttering under his breath."
    show Wareworker at right with dissolve
    "Diego" "Sorry, mija. Gotta do everything by myself out here."
    "Diego" "Jun is inside-- his office is right down the hall. Come find me if you have problems."
    show chelsea embarrassed
    pause 1.0
    hide Wareworker with dissolve
    pause 1.0
    hide chelsea with dissolve
    "He squeezes your shoulder affectionately before returning to his job. You head inside, following Diego's directions."
    scene black with fade
    "Everything looks normal; the warehouse seems to be in use, and everyone is busy at their job. This is the last place you expected Jun to invite you to."
    show chelsea embarrassed with dissolve
    pcname "I thought he was going to take me somewhere really shady... But this isn't so bad..."
    scene bg BakeryOffice with fade
    "You follow the halls down to Jun's office-- the nicest room in the whole warehouse, you'd gamble. There is a solid wood desk and a comfortable leather chair, with new computers and several filing cabinets to the side."
    show GHCMan at left with dissolve
    "Jun looks up-- irritation on his face softening when he realizes it's you-- and gestures for you to have a seat."
    "Jun" "Ah, you're a bit early. Just a moment while I finish this."
    hide GHCMan with dissolve
    pause 1.0
    show chelsea with dissolve
    "Jun types a few things onto his computer, leaving you to glance around his office in silence."
    "It's pretty standard, for the most part-- nothing too out of place-- but you notice a dark stain on the rug that couldn't quite be scrubbed out. It's hardly noticeable, but it's enough to make you wonder where it came from."
    show GHCMan at right with dissolve
    show chelsea shocked
    "Jun" "[pcname]?"
    show chelsea blank
    "You're surprised to find Jun standing near the door, a polite look on his face as he regards you."
    "Jun" "Are you ready?"
    show chelsea confused
    pause 1.0
    show chelsea blank
    "Ready for what? You're not sure. But you nod anyway and follow Jun out of his office and through the warehouse."
    scene black with fade
    "Jun" "Sorry for the mess-- it's our busiest time of the year, you see. Everyone wants a comfortable bed by the time winter rolls around."
    "You walk past several mattress pallets and workers engrossed in their tasks, transporting mattresses in and out of the trucks attached to the gaping square holes in the building."
    "Jun takes you through the warehouse and around to the back corner, away from all of the work at play. A metal door marked 'FIRE EXIT' sits against the far wall."
    "When he opens it up, another room stretches out before you."
    "The only use of this room-- at least that you can think of-- is for extra stock, maybe office supplies. It's not big enough for loading, but it's too large to be much use as an office."
    "Jun seems to have found a compromise; the room is used for his {i}other{/i} business instead."
    show bg MattMafia1 with dissolve
    "Matt sits in a chair against a large metal pole, his wrists and ankles bound with zip ties. A dirty cloth gags his mouth, but you can see the blood both fresh and dried over the fabric."
    "He hardly looks like Matt anymore-- even with the blindfold, you can tell his right eye is swollen shut entirely."
    "Several beatings have made his face and limbs red and purple and puffy, like he's been inflated and stretched too thin. His left arm looks wonky, as if the bone has snapped the wrong way."
    "He hasn't changed clothes since he was at your house; his uniform is stained with blood, and you're certain you can smell an infection festering somewhere on his broken skin."
    show bg MattMafia2 with dissolve
    "You gag and turn away, unable to face him any longer."
    "Jun" "The boys had a little too much fun with him, as you can see, but they were pretty upset after hearing what he did to you."
    "Jun" "Can you blame them? You're our little karaoke buddy."
    show bg MattMafia3 with dissolve
    "Jun smiles at you, but you can't bring yourself to smile back."
    "Somewhere deep inside of you is pleased about this-- having these men back you up, seeing Matt suffer for all the pain he's inflicted on yourself and others, is gratifying in its own way."
    "But you're not a monster, either. A tiny part of you feels guilty about this. You try to push the thought away."
    "Jun" "Assuming you don't want him dead--"
    show bg MattMafia4 with dissolve
    "Matt's body tenses, the only sign that he's conscious and listening."
    show bg MattMafia5 with dissolve
    "Jun" "Now is a good time to list your demands to him. We'll make sure he stays in line, won't we, Matty?"
    "Matt flinches as June's hand clamps down on his shoulder. You hear Matt whimper slightly, his words cut off by the gag."
    "You step forward. Even if he can't see you, you hold yourself up a little taller."
    show bg MattMafia6 with dissolve
    pcname "Who's the bitch now, Matt?"
    "You hear a question mumble itself through the gag, recognition in its tone, but you disregard it. As long as he can't see you, he doesn't know."
    "And if he says anything to anyone, it sounds like Jun will take care of it."
    pcname "Here is what you're going to do; you're going to stop blackmailing girls. {i}All{/i} girls. And you're going to never, {i}never{/i}, bother us at school again."
    pcname "I want photos deleted, videos deleted, whatever crap you have on us gone. And if you break any of these rules, or tell anyone what happened, my friends will finish the job."
    pcname "Understood?"
    "There's a moment of silence, but Matt nods, the only form of agreement he can give."
    show bg MattMafia7 with dissolve
    pcname "Good."
    "Jun waits a moment longer to make sure you're finished before leading you back to the warehouse."
    scene black with fade
    show GHCMan at right with dissolve
    "Jun" "That was good, [pcname]. The kid is pretty jumpy, but we'll make sure he stays in line."
    show chelsea sad with dissolve
    pcname "Is he going to be returned home soon? The police have started asking about him--"
    show chelsea embarrassed
    "Jun" "Don't worry, we'll have him cleaned up and on his way tonight."
    "Jun" "Go home and relax; we have it all taken care of."
    pcname "Thank you, Jun."
    scene black with fade
    "You smile and make your way back home. Whatever guilt and panic you felt earlier seems to melt away with the reassurance that Matt won't be bothering you-- or any girl at school-- any longer."
    jump events_end_period

label MattMafiaResolution3:
    scene bg School with fade
    "The police stop coming to school the next day, and the buzz of Matt's disappearance dies down with the announcement that he's in the hospital."
    "You hear everything secondhand from Violet and a few whispering students, but the undercurrent of excitement and curiosity seems to radiate throughout the school during the week."
    scene black with fade
    "But it's a whole new brand of chaos when you step into school today."
    scene bg Cafeteria with fade
    "Your thoughts of club and plans for the upcoming weekend die down when you see Matt and Alex standing in the hallway-- Alex's glare keeping the rest of the crowd at a distance, but a million eyes cast their way."
    show Matt Beaten with dissolve
    "Matt looks better than the last time you saw him-- the swelling has gone down, and his arm is in a sturdy white cast. His cuts have been cleaned and bandaged, but a few purpling bruises stand out on his cheeks and busted lip."
    show Alex Neutral at midright with dissolve
    "Alex" "C'mon, man. Just tell me what happened. You know my dad's a cop-- he'll take care of it."
    show Alex Blank
    "Matt doesn't look at his friend, his eyes vacant and empty as he stares out across the hall."
    show chelsea at left with dissolve
    pause 1.0
    show Matt Scared
    "When his gaze lands on you there is a question in his eyes, along with fright, but he says nothing. Whatever fight he had in him was beaten out by Jun and his gang."
    show Alex Serious
    "Alex" "Matt, dude, you gotta talk to me--"
    show Matt at exitScene(0.5, 1.0, 0.3, 0.3)
    pause 1.0
    hide Alex with dissolve
    "Matt turns away and shuffles down the hall, putting as much distance from you as he can. Alex chases after him, drilling him for answers his friend won't give."
    show chelsea embarrassed
    "At least you know your secret is safe."
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
