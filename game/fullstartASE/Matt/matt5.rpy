label matt_subspace:


    show bg HomeE with dissolve
    "Heading home from work, you strip to your underwear, change into your pajamas, and flop onto the couch."
    "Between school and work, the day was way more stressful than you expected. It's nice to finally relax."
    "Things could have been worse, though. Matt's mom was really sweet..."
    "A short, bitter laugh escapes your lips. How sad is your life that you're thankful for Matt's mother's attention?"

    $ clothes = "underwear"
    show chelsea shocked at right, moveupfast(3.0, 1.0, 0.2)
    "{b}*THUD THUD THUD*{/b}"
    "You nearly jump off the couch as the loud knocking echoes through your apartment."
    show chelsea confused
    if club == "track":
        pcname "What the hell..."
    elif club == "cheer":
        pcname "It's not time for rent, is it?"
    elif club == "yearbook":
        pcname "Who...?"
    "Crossing to the door, you peek out the peephole."
    "Matt stands with his arms crossed, glowering at your door."
    show chelsea sad
    if defymatt:
        "Your stomach tightens with dread; you knew he was angry, but you'd almost forgotten."
    elif True:
        "Your heart skips a beat. You'd almost forgotten how angry he looked this afternoon."
    m "I know you're home. The light's on."
    "Swallowing the lump in your throat, you unlock the door and slowly swing it open."
    show Matt Casual Blank with dissolve
    "Matt pushes into the room, his eyes roving across your body."
    show chelsea shocked
    show Matt Casual Angry
    m "You need something sexier to wear when I come over."
    if defymatt:
        if club == "track":
            show chelsea angry
            pcname "That's not gonna happen."
        elif club == "cheer":
            show chelsea angry
            pcname "If I knew you were coming, I wouldn't be here."
        elif club == "yearbook":
            show chelsea blank
            pcname "I... don't think so."
    elif True:
        show chelsea sad
        "Your stomach sinks."
        pcname "I didn't realize you were coming over."
    show Matt Casual Blank
    "Rolling his eyes, Matt strolls further into the apartment."
    "He turns suddenly, fists balled at his sides."
    show Matt Casual Angry
    show chelsea blank
    m "I thought I told you not to talk to my fucking mom again."
    "Tired and frustrated after the day you've had, you snap back at him."
    show chelsea angry
    pcname "{i}I{/i} didn't talk to {i}her{/i}. She came up to {i}me{/i}!"
    "Matt takes a single, menacing step toward you, and your pulse quickens."
    show chelsea blank
    show Matt Casual Question
    m "So it's her fault, huh?"
    m "She's too nice. She doesn't know what a {i}whore{/i} you are."
    show chelsea angry
    if defymatt:
        pcname "I'm not a whore! You {i}force{/i} me to do what you want!"
        show Matt Casual Smirk
        "He sneers."
        show chelsea sad
        m "Aren't we past that excuse? You don't even try to get out of it anymore."
        m "You used to plead and beg me not to do it."
        m "Now you just do what I tell you without any threats at all."
        "Your stomach turns as he continues speaking."
        "It's not an excuse! Just because you've stopped begging doesn't mean you want it!"
        "Even if he degrades you, you can still have enough pride left not to beg. Right?"
        show chelsea embarrassed
        "Right...?"
    elif True:
        pcname "That's not fair! I {i}tried{/i} to do what you told me to!"
        show chelsea blank
        show Matt Casual Blank
        "You're not sure why you're being defiant. Normally you'd agree with whatever Matt says, but this time you just can't."
        "You {i}know{/i} you're worthless, but you always {i}try{/i} to do what Matt wants. It's not right for him to blame you for this."
        show chelsea sad
        "There are enough things you already blame yourself for."
    show Matt Casual Angry
    m "Get those clothes off and shut the fuck up."
    show chelsea blank
    "Glaring at him, you stand your ground."
    show chelsea angry
    if club == "track":
        pcname "Make me!"
    elif club == "cheer":
        pcname "I don't think so."
    elif club == "yearbook":
        pcname "N-no!"
    show chelsea blank
    if defymatt:
        show Matt Casual Smirk
        m "Do I need to remind you what will happen if you don't?"
    elif True:
        show Matt Casual Blank
        m "So this is how it's going to be tonight, huh?"
        m "Do you really want to defy me?"
    "You stare at him a moment longer, debating whether it's worth it or not."
    "Finally, with a huff of annoyance, you start undressing."
    show Matt Casual Pleased
    if defymatt:
        show chelsea sad
        "As much as you hate him, you're still afraid of what he'll do with those pictures."
    elif True:
        "As frustrated as you are, you still want to please him."
        show chelsea sad
        "There has to be {i}something{/i} you can do right. Someone you can make happy."
    show chelsea blank
    show Matt Casual Smirk
    "As you strip, he sits on the middle of the couch, watching with a smirk."
    $ clothes = "naked"
    if club == "track":
        show chelsea blank
        "When you finish undressing, you glare down at him and wait."
    elif club == "cheer":
        show chelsea sad
        "Dropping the last of your clothes onto the floor, you shiver a little."
    elif club == "yearbook":
        show chelsea blank
        "Naked, you wrap your arms around yourself and stare at the floor."
    m "Get over here."
    "Moving to obey, you approach the couch slowly."
    hide chelsea with dissolve
    hide Matt Casual with dissolve
    with fade

    "As you near, he beckons you onto the couch."
    "You put your knees on the couch next to him, waiting to see how he wants you to position yourself."
    "Suddenly, he grabs your arm and pulls you forward, sending you sprawling over his lap."
    pcname "Wah!"
    "A startled cry escapes your throat - and then another, as his open palm comes down over your right buttcheek."
    "{i}*Crack*{/i}"
    pcname "Hey!"
    "He laughs, rubbing his hand over your tingling flesh."
    "His strike was more unexpected than painful, and the sensation fades quickly."
    m "I told you that you'd be punished. You've been a bad girl..."
    "{i}*Crack*{/i}"
    "Another slap - harder than the first, and on the opposite cheek. This one stings, but you're still more outraged than concerned."
    pcname "I didn't do anything wrong!"
    "{i}*Crack*{/i}"
    "A third strike, on the same side as the first but a little lower."
    m "Keep arguing, slut. I'll just keep spanking you until you apologize."
    "He doesn't wait for you to respond."
    "{i}*Crack*{/i}"
    pcname "I won't!"
    "You try to push yourself up, but he still has hold of your wrist."
    "{i}*Crack*{/i}"
    "He twists your wrist behind your back, pinning you to the couch."
    "{i}*Crack*{/i}"
    "His strikes rain down on your ass, slowly but insistently."
    "Your face flushes with indignation, but there's nothing you can do to stop him."
    "{i}*Crack*{/i}"
    "Your ass grows warm as the spanking continues; the stinging barely fades before the next strike."
    "{i}*Crack*{/i}"
    "He spaces his slaps over your entire ass, leaving no skin untouched."
    "{i}*Crack*{/i}"
    "Soon your whole ass is a burning, tingling mass of nerves."
    m "Ready to apologize?"
    "You don't trust yourself to speak, so you just shake your head."
    "{i}*Crack*{/i}"
    "The pain begins to radiate out, no longer confined to the spot where his palm lands."
    "{i}*Crack*{/i}"
    "Your breath hisses as you inhale sharply; that one {i}really{/i} hurt."
    m "Ready yet?"
    "Ignoring him, you focus on your breathing and wait for the next blow."
    "{i}*Crack*{/i}"
    "{i}*Crack*{/i}"
    "{i}*Crack*{/i}"
    "Three blows fall one after the other, until you're gasping for breath."
    "The pain overwhelms your nerve endings, leaving you writhing to avoid the next strike."
    "Suddenly his hand strokes your ass. His touch is gentle, but it only ignites your nerve endings further."
    "The pain fades quickly under his soft caresses. Slowly, muscles you didn't realize you'd tensed begin to relax."
    "By the time he lifts his hand, your breathing is almost normal again."
    "{i}*Crack*{/i}"
    pcname "Ah!"
    "You cry out, surprised by his sudden assault."
    m "Did you want to say something?"
    "Gritting your teeth, you prepare for another strike."
    "{i}*Crack*{/i}"
    "This one lands lower, nearly touching the bottom of your labia."
    "A thrill of fear runs through you. How much would it hurt if he hit that sensitive flesh?"
    "{i}*Crack*{/i}"
    "Your breathing grows ragged as he continues spanking you. It's all you can do not to cry out as your nerve endings burn under his blows."
    m "Ready to apologize?"
    if defymatt:
        "You ignore him, the pain making you nearly feral."
        "You've never felt like this before. You'd heard of the 'fight or flight' response, but now you {i}feel{/i} it."
        "And while your body is screaming for flight, you've chosen to {i}fight{/i}."
    elif True:
        "You ignore him, waiting for his next strike."
        "All of the darkness of the day - of the last year - seems to have led you to this point."
        "You've done bad things. {i}You're{/i} bad. You {i}deserve{/i} this beating."
    "{i}*Crack*{/i}"
    "{i}*Crack*{/i}"
    "{i}*Crack*{/i}"
    pcname "Ahh!"
    "Matt chuckles darkly, caressing your ass again."
    "This time, though, you know it's only a short reprieve."
    "When his hand lifts again, you prepare for another blow. Sucking in a deep breath, you wait."
    "And wait."
    "And then his fingers softly run over your skin again, soothing the tingling skin."
    "You exhale, releasing the breath you'd been holding and relaxing momentarily."
    "Matt raises his hand quickly and brings it down hard."
    "{i}*CRACK*{/i}"
    pcname "AHH!"
    "Your throat aches in the wake of your pained cry. Your breath comes in short pants, leaving you feeling like you're hyperventilating."
    m "Well?"
    "It takes a moment to remember what he's asking you for. Your mind moves slowly, barely processing anything beyond the pain."
    "Matt takes your hesitance as refusal."
    "{i}*Crack*{/i}"
    "{i}*Crack*{/i}"
    "{i}*Crack*{/i}"
    "You cry out between each blow now, unable to hold back."
    "And then, suddenly, you {i}melt{/i}."
    "Your muscles relax, even as his next strike cracks across your ass, and your breathing begins to slow again."
    "The pain radiates out from his palm, but it's dull now."
    "Instead, the warmth spreads out, creeping over your back and down your thighs, until it covers your entire body."
    "Warm and languid, you feel almost as if you're floating."
    if club == "track":
        "It's almost like the euphoria you feel sometimes when you push yourself during track."
    elif club == "cheer":
        "It's like the few seconds post-orgasm, when the whole world disappears. But it stretches on and on, with no end in sight."
    elif club == "yearbook":
        "It's like what you imagine it's like to get high - on ecstasy or something."
    "You feel light, almost weightless."
    "Peaceful."
    "Just as suddenly as it began, you feel it slipping away."
    m "Had enough yet?"
    pcname "No..."
    "Your voice comes out in a dreamy whisper - you barely recognize it as your own."
    "{i}*Crack*{/i}"
    "Another blow comes down, but you barely feel it. You raise your ass a bit, as if taunting him to strike you again."
    "{i}*Crack*{/i}"
    "{i}*Crack*{/i}"
    "{i}*Crack*{/i}"
    "Each new blow pushes you higher and higher, until you no longer feel them at all."
    "All thought stops as you float on this high."
    "You don't think, don't feel, don't... anything."
    "It's as if time itself stops. And all of your worries are just... {i}gone{/i}."
    "Then, from far away, you hear Matt's voice."
    m "Ready to apologize, slut?"
    "You know you didn't want to apologize before, but it doesn't seem to matter anymore."
    "Forming words is harder than you remember, but you manage a single word."
    pcname "...sorry..."
    "You barely feel his hand moving over your ass, caressing it gently."
    m "That's better..."
    "His hand moves between your legs, sliding up your slit and back down."
    m "You're so fucking wet..."
    "Two fingers press inside you. You lift your hips, pushing your ass into the air so he has better access."
    "Your pussy feels puffy and warm, but - to your surprise - you barely feel Matt's fingers pumping in and out of you."
    "You rock against his hand, eager to feel {i}more{/i}."
    pcname "Matt..."
    "Suddenly, he pushes you forward, sending you sprawling across the couch."
    "He lifts your legs, sliding out from under you, and leaves you alone on the couch."
    "In your dazed state, you lay where he left you, barely comprehending what's happening."
    "You want his fingers back. You want to feel the pleasure you know they can bring."
    "And then you feel his weight behind you on the couch. His hands on your hips, pulling you up onto all fours."
    "His cock pressing against your opening."
    "You lean back against him, eager to be filled."
    m "You want something, slut?"
    "Moaning, you lean back further, until his tip presses inside of you."
    "Spreading your legs further, Matt pulls your hips back, filling you in a single, hard thrust."
    "You moan again, the sensation pushing you further into this floaty high."
    pcname "...harder..."
    "You urge him on, chasing the high."
    "He thrusts into you, his balls slapping against the backs of your thighs."
    pcname "...{i}harder{/i}..."
    "Over and over, he batters your pussy with his cock, rocking your body with the force of his thrusts."
    "And each time, you find yourself drifting further and further from your self, until his cock is the {i}only{/i} thing you can focus on."
    "You barely hear your own moans of pleasure. Your only thought is the cock inside of you."
    "Long, hard, powerful... It pounds against your insides."
    "You feel a familiar pressure as your body responds; a tightening of muscles, a throbbing in your clit."
    "Riding this high, though, you don't realize what it means until your body begins shuddering."
    "Your orgasm hits you hard, but the pleasure is dulled by this new high."
    "Matt fucks you through your climax, gasping as your pussy clamps down on his cock."
    "Almost as soon as your orgasm ends, though, you feel the pressure quickly building again."
    "This time the pleasure finds its way through the fog. You cry out as your body spasms again, twitching and shuddering before falling limply forward."
    "As your orgasm finishes, Matt releases you. You slump forward, too heavy to hold yourself up."
    "Your mind is still foggy, and it takes a few seconds for Matt's words to reach you."
    m "Get up."
    if defymatt:
        "You obey immediately; it no longer matters why you're letting Matt do this."
        "All that matters is that {i}he{/i} can make you feel like {i}this{/i}."
    elif True:
        "You obey immediately, no longer concerned with your anger from before."
        "It doesn't matter why you were angry; all that matters is that {i}he{/i} can make you feel like {i}this{/i}."
    "Stumbling toward him - your body heavy and sluggish, barely responding to your desires - you try to focus again."
    m "On your knees."
    "It's easier not to think, just to obey. So you sink to your knees in front of him, waiting for his next command."
    "He presses his cock to your lips and you open wide."
    m "Time to thank me for making you cum twice."
    "Immediately, you begin by licking his shaft, running your tongue and lips up and down his length."
    "Mindlessly, you take his cock - already well-lubed with your juices - into your mouth."
    "Bobbing your head, you eagerly swallow his hard member again and again."
    "Through the fog in your mind, you barely feel your gag reflex - and it's easier than ever to just ignore it."
    "Your body feels like a tool you can use, not like a part of you at all."
    "So you use it to pleasure him, the man who brought you to this place where nothing else matters."
    "His breath is the loudest sound in the room - and the only sound you care about."
    "Suddenly his hand presses against the back of your head, holding your face tight against him."
    "His hips buck and a flood of hot, thick liquid surges down your throat."
    "Then he releases you, his cock slipping from your lips as he steps back."
    m "Fuck..."
    "Matt stares down at you, taking in your dreamy, heavy-lidded expression."
    m "You really got into that, didn't you, slut?"
    "You nod without thinking. Your mind is still moving sluggishly, but you can slowly feel reality starting to return."
    m "You want to do it again, don't you?"
    "You nod again."
    "A sly smile touches Matt's lips. You know you should be wary when he looks like that, but you can't quite make yourself do it."
    m "You like it when I fuck you, don't you?"
    "Nodding again, a slow smile spreads over your face as you remember your orgasm."
    if defymatt:
        m "I don't even have to blackmail you, do I? You pretend to hate it, but you {i}love{/i} what I do to you."
        "You nod again, happy to agree with anything he says."
        "His smile turns to a sneer."
    m "I knew it. You're a dirty slut, aren't you?"
    "Sighing with contentment, you nod again."
    "Matt chuckles, and for the first time, you realize he's taken his pants off."
    "You suppose you must have known it - how else did he fuck you? - but your hazy mind never really noticed."
    "He catches your eyes on his nakedness and shakes his head."
    m "Miss it already?"
    "He seems pleased with you, so you smile."
    m "Don't worry; I'll take care of you again real soon."

    with fade
    show Matt Casual Pleased with dissolve
    show chelsea sad at right with dissolve
    "You watch him dress, a little sad that he's leaving you here alone."
    show Matt Casual Blank
    "As he finishes, he looks over to you again and pauses, frowning."
    m "I think you should go to bed now."
    show chelsea happy
    "Smiling, you hold your arms out to him."
    show Matt Casual Angry
    m "What the fuck..."
    "Despite his reaction, he pulls you to your feet and walks you into the bedroom."
    hide Matt Casual with dissolve
    hide chelsea with dissolve
    scene bg RoomN with fade
    "You feel safe, letting him guide you to your bed."
    "Almost as soon as your head hits the pillow, you drift off to sleep."
    with Fade(0.5, 2.0, 0.5)
    "You wake with a start. It's still dark outside."
    "Looking at your clock, you see that your alarm won't go off for another hour."
    "Settling back against your pillow, you take a deep breath and turn onto your side."
    "A tenderness between your legs catches your attention."
    pcname "What..."
    "Memories flood back into your mind. Matt spanking you, insisting you apologize for talking to his mother."
    "Your defiance. The pain. The... pleasure?"
    "The fogginess, you apologizing, your eagerness as he fucked you, the - two! - orgasms..."
    "Sucking his cock. All of the questions he asked you. And agreeing to all of them..."
    if defymatt:
        pcname "No..."
        "It wasn't you, was it? You weren't thinking straight."
        "Him spanking you did something to you. You couldn't think at all. It was like you were high. You didn't--"
    elif True:
        pcname "Did that really happen?"
    "But you remember your uncharacteristic defiance."
    "You pushed him to punish you more. To hit you harder."
    "And when you finally snapped - when your brain turned off and there was {i}nothing{/i} - you encouraged him."
    "You wanted that feeling, that high. You enjoyed it."
    "All shame, all guilt, all worries... You were {i}free{/i}."
    if defymatt:
        "Maybe that's why you resisted him."
        "You let him grab you that first day, and then you refused to keep letting him have his way."
        "Why? Unless you wanted to antagonize him. To push him to hurt you."
    elif True:
        "Maybe that's why you gave into Matt in the first place."
        "You told yourself that was what you deserved."
        "That you were the dirty slut he said you were. That he was the only one who knew what you really were."
    "Maybe this is what you wanted all along."
    "Your limbs are still heavy, and there's that tender, well-used feeling between your legs."
    "And, despite your beleaguered thoughts, you find you still feel that inner peace."
    "Letting go of your worries for a little longer, you let yourself drift back to sleep."
    jump endday

label matt_petplay2:
    scene bg CityN with fade
    "After work, you head home to spend a relaxing evening in front of the TV."
    $ clothes, hair = casualwear
    show chelsea shocked with dissolve
    "Nearing your apartment, though, you see a dark figure near your door."
    "Freezing, you consider running, but then the figure turns and you recognize him."
    show Matt Casual Smirk at left with dissolve
    "Matt."
    if defymatt:
        show chelsea sad
        "You consider running again, but you know it's no use."
    show chelsea embarrassed
    "Your pulse quickens as you approach, wondering what he has planned for you."
    m "Miss me, slut?"
    if defymatt:
        show chelsea blank
        "You ignore him, unlocking the door and stepping inside."
    elif True:
        show chelsea happy
        "You smile, unlocking the door and stepping inside."
    hide chelsea with dissolve
    show Matt Casual Pleased
    "Matt follows you, almost slamming the door shut behind him."


    hide Matt Casual with dissolve


    hide bg CityN
    scene bg HomeN
    with fade


    show chelsea
    show Matt Casual Pleased at right
    with dissolve
    if club == "track":
        show chelsea blank
        "You wince at the show of force, but you refuse to let him intimidate you."
    elif club == "cheer":
        show chelsea shocked
        "You wince at the show of force, turning to him with wide eyes and a hesitant smile."
    elif club == "yearbook":
        show chelsea shocked
        "Wincing at the sudden show of force, you wheel toward him, eyes wide."
    m "Here you go. Ready to play?"
    show Matt Casual Question
    "He looks around."
    show chelsea confused
    m "Well? Where's your collar, bitch?"
    show chelsea shocked
    "You stare at him, uncomprehending. Then you realize what he wants."


    hide chelsea with dissolve



    hide Matt Casual
    hide bg HomeN
    scene bg RoomN
    with fade


    show chelsea embarrassed at right with dissolve
    "Walking into your bedroom, you reach under your mattress where you stashed the collar."
    "You didn't want to chance anyone else seeing it, but you couldn't throw it away."
    "Pulling it out, you carry it into the living room."


    hide chelsea with dissolve



    hide bg RoomN
    scene bg HomeN
    show Matt Casual Blank at right
    with fade


    show chelsea with dissolve
    "You pause, staring at the familiar pink leather, the rhinestones... And the tag, the word \"Bitch\" glinting in the lamplight."
    show Matt Casual Smirk
    m "Well?"
    show chelsea happy
    "You know what he expects, so you get to it."
    hide chelsea with dissolve
    hide Matt Casual with dissolve
    with fade

    "You lift the collar to your throat and cinch it tightly in place."
    "The leather digs into your skin and, as you strip your clothes off, the tag jingles playfully."
    "Stripping off your clothes, you toss them aside."
    "Then, naked, you get down on all fours and look up at Matt, waiting for his first command."
    "Matt stands open mouthed, staring down at you."
    m "You're ready to be a good girl today, huh?"
    "For a moment, you're not sure what he means - and then the realization hits you."
    "You obeyed immediately, without a single word of protest."
    "He didn't even tell you to strip, just handed you the collar and waited."
    "As you work through all of this, Matt smiles."
    m "And you learned not to speak. You really {i}are{/i} a good girl today."
    if defymatt:
        "Your cheeks grow hot with anger, but you're still too disconcerted to argue."
    elif True:
        "Your cheeks grow warm with pride; you didn't realize it, but you're doing everything right."
    m "Alright then. Speak, girl!"
    "Your cheeks grow even hotter."
    pcname "Arf?"
    "For the first time, Matt frowns."
    m "You can do better than that."
    if defymatt:
        "It's no use fighting him; he'll only make it harder for you."
    elif True:
        "Fighting back the shame, you try again."
    pcname "Woof!"
    m "Better. But that's not the only trick you know, is it?"
    "His smile widens and he snaps his fingers."
    m "Beg, bitch."
    "Sitting on your hind legs, you raise your hands limply in front of you."
    "Recalling your last time in this position, you squeeze your eyes shut and spread your knees wide."
    m "That's a good girl!"
    if defymatt:
        "You feel a strange surge of pride, though you tell yourself it's just relief that he's not unhappy with you."
        "Who knows how much worse it would get then."
    elif True:
        "You feel a strange surge of pride. Even though it's degrading to be treated like a dog, at least he's happy with you."
    m "Okay, now roll over!"
    "You drop to all fours and then roll onto your back, holding your hands and feet in the air."
    m "Good! Now {i}stay{/i}!"
    "Your eyes flutter open as you hear him moving around, but you can't see anything."
    "Suddenly, you feel something cold and wet on your belly."
    "Tilting your chin to your chest, you see Matt pressing a black marker to your skin."
    menu matt_puppy2_protest0:
        "Protest!" if True:
            pcname "Hey! What are you--"
            m "Shhh! Dogs don't talk, remember?"
            pcname "I don't care, you can't--"
        "Stay." if True:
            "Your stomach flutters as you wonder what he's doing."
            "His marker dances over your skin, tickling, but you hold your position."
    "He stands, smiling down at his work."
    m "It's a good thing dogs can't read."
    "You look down at your belly, stretching to read the word."
    "'Whore'"
    m "I didn't want you to forget what you are."
    "He grabs the back of your knee, pushing your leg higher, and presses the marker against your skin again."
    menu matt_puppy2_protest1:
        "Stop!" if True:
            pcname "Stop! That's enough!"
            "Matt frowns, his grip tightening on your leg."
            m "Shut up, bitch. Be a good girl!"
        "Stay silent." if True:
            "Gritting your teeth, you try to stay still."
    "The marker trails over the back of your thigh, cold and wet."
    "As he draws, he says the words aloud, speaking slowly."
    m "Fill... these... holes..."
    "He finishes with two arrows - one pointing to your ass, the other to your pussy."
    "Dropping your leg, he puts a finger to his chin, looking over your body."
    m "Now anyone who sees you will know what to do with you."
    if defymatt:
        "You practically tremble with outrage, but manage to bite your tongue."
        "Angering him will only make things worse."
    elif True:
        "Trembling with shame, you turn your head aside."
    m "I think you need one more..."
    "He leans over you, pressing the marker to your right breast."
    "You squeeze your eyes shut, willing him to stop."
    m "That's right. Since you're my pet, I can do whatever I want to you."
    "He traces several letters on that breast, then switches to the other."
    m "There you go."
    "You open your eyes, blinking. He puts the cap back on the pen, staring gleefully at his handiwork."
    "Tilting your chin down, you stare at your breasts, trying to read the upside down letters backwards."
    "'Fuck Toy', with one word on each breast."
    m "Now sit, girl."
    "You roll onto all fours, settling back on your heels again."
    "As you do, he produces the same red ball as before."
    m "You wanna play fetch?"
    "He waves it in front of you, waiting."
    m "Well? Are you excited?"
    "You wiggle your butt, trying to mimic an excited puppy. Matt laughs."
    m "Fetch, girl!"
    "He throws the ball across the room."
    if getintoit:
        "You race to the ball, grabbing it in your mouth and crawling back to him."
        "Your shame is quickly forgotten as you get into the game again."
        m "What a good girl! Go get it!"
        "He tosses the ball a few more times, praising you each time."
        "Soon you really start enjoying it, making a game of grabbing the ball as fast as you can and rushing back to drop it into his waiting hand."
    elif True:
        "You crawl across the room and reach for the ball."
        "Then, thinking better of it, you bend forward and grab it in your mouth."
        "As you sit at his feet again, he ruffles your hair."
        m "That's it! Good job, girl!"
        "An odd mixture of shame and pride whirls within you. You hate behaving this way, but he seems so happy with you..."
        m "Go get it!"
        "He tosses the ball a few more times, praising you each time."
        "After the first few tosses, you actually start to get into it."
        "It's kind of fun, challenging yourself to grab the ball quickly and race back to him."
    "You drop the ball into his hand again, watching expectantly for the direction he'll send you next."
    "But instead, Matt puts the ball back in his pocket."
    "You can't help but feel a little disappointed that the game is over, but your focus on him, anticipating his next command."
    m "Hmmm. Let's see..."
    "He glances down at you, clearly pondering something."
    "You tilt your head to one side, curiously."
    m "Alright. Stay."
    "Remaining in the sitting position, your eyes follow him around the room."
    "He steps out of the living room and into the kitchen, opening cupboards as he makes his way toward the refrigerator."
    m "There we go..."
    "Your eyes widen as he pulls out a jar of peanut butter."
    m "Sandy loves peanut butter. We put it in a rubber toy and she goes crazy trying to get it all out."
    "As he speaks, he unscrews the jar and reaches two fingers inside."
    "Scooping out a glob of peanut butter, he slowly crosses the room and waves it in front of your nose."
    "You can't help it; the scent makes your mouth water."
    "Licking your lips, you swallow hard."
    m "You want some, girl?"
    "Matt holds his fingers in the air, just out of your reach, while his other hand moves to his zipper."
    "He unzips his pants and pulls them down to his knees, exposing his rigid cock."
    "As you watch, he smears the peanut butter down his cock and smiles down at you, echoing his earlier question."
    m "You want some, girl?"
    "Knowing what he expects, you wiggle your ass again."
    m "Here you go..."
    "He sticks his fingers in your face, holding them for you to lick clean."
    "You lap the creamy peanut butter from his fingers, pausing occasionally to swallow the thick, sticky substance."
    "When his fingers are clean, he gestures to his cock."
    m "Want more?"
    "Your eyes meet his and he smirks."
    m "Beg."
    "You sit back on your hind legs again and lift hands to your chest. This time, you put your tongue out and pant, like an excited dog waiting for a treat."
    m "That's right. What a good girl."
    "He steps closer, his cock waving just above your nose."
    m "Go on, girl. Take it."
    "You reach up to steady his cock, but catch yourself."
    "{i}Dogs don't use their hands,{/i} you remind yourself."
    "Sticking your tongue out, you slowly lick the peanut butter from his skin."
    m "Good girl. Lick it {i}all{/i} off."
    "Your tongue spreads the peanut butter around, too, forcing you to go back over the same spots again and again."
    "He hums with approval as you move your tongue up and down his cock, lapping up all of the thick, sweet spread."
    "His reaction inspires you to keep going, even after the peanut butter is gone."
    "You take his balls in your mouth, sucking one and then the other."
    "Then you lick your way back up his shaft, pressing the head to your lips and swirling your tongue around."
    m "Fuck..."
    "Pleased with his response, you slowly lower your mouth around him."
    m "That's right, bitch. Take it all."
    "You raise your eyes to his, bobbing your head up and down his cock."
    "Relaxing your throat, you push your face towards his hips, until your nose presses into his groin."
    "Holding the position, you wait with his cock sheathed in your throat."
    m "Good girl..."
    "Pulling back, your nose flares as you suck in a deep breath."
    m "Again."
    "You swallow his cock again, pressing your face tight against him."
    "You wait for his praise, holding your position until you start to tremble."
    "Your chest burns with the need to breathe, but you wait for his permission."
    m "Fuck... That's a good girl..."
    "Pulling back again, you draw a few desperate breaths through your nose, slightly lightheaded."
    m "Again."
    "Swallowing his cock again, you hold position until tears prick your eyes and your head starts to swim."
    "Your hands flutter at your sides, barely resisting the urge to push him away so you can breathe again."
    "For a moment, you wonder what he'll do if you pass out."
    m "That's it. Good girl..."
    "You sit back on your heels, his cock dropping from your lips as you cough, gasping for breath."
    m "I didn't tell you to stop, did I? Get that dick back in your mouth, bitch."
    "You nuzzle your face against him, struggling to get his cock back in your mouth without using your hands."
    "As soon as you get your lips around it, his cock slides back down your throat, choking you again."
    "He doesn't make you hold it as long this time, stroking your hair after a few long seconds."
    m "That's a good girl..."
    "Pulling back, you catch your breath and lower your head again, without being told."
    m "Mmmmm... Good girl."
    "You repeat the process again."
    "Suddenly, a familiar sense of detachment sweeps over you."
    "You stop struggling to hold your breath, content to breathe only when he allows you."
    "As you do, you find yourself relaxing."
    "Matt won't let you suffocate. He won't push you further than you can handle; he never has."
    "He knows exactly what you can take. Better than you do."
    "Your senses dull until the only thing you can feel or hear are the words 'good girl'."
    "Over and over, you deep-throat his dick, holding it in your throat until he says those words."
    "Each time you hear them, it's like a release of pressure - mentally and physically."
    "Eventually, he steps back. You can hear yourself panting from exertion, but you feel light and free."
    m "I think you deserve a treat now."
    "You get back into a begging position, sticking your tongue out."
    "He jerks himself off, cumming after only a few strokes. His cum spurts across your cheeks and tongue, running down your chin."
    "Licking up as much of it as you can, you give him a happy yiff in thanks."
    "Chuckling, he tucks his cock back in his pants."
    m "Did you like your treat?"
    pcname "Ruff! Rufff!"
    m "That's right. My little bitch likes whatever her master gives her."
    "He ruffles your hair, rubbing the top of your head."
    m "You did a lot better today. Clearly you learned a lot from our last lesson."
    m "I think that deserves a reward..."
    "He stares down at you a moment, a slow smile spreading over his face."
    m "Do you know how a bitch in heat presents herself to be fucked?"
    "Your cheeks grow hot as you nod your head."
    m "Then get in position, bitch."
    "You sink to your hands and knees, lifting your ass high into the air."
    m "That's it. That's how you show a stud you want to be fucked."
    "An involuntary whine escapes you as he runs his fingers up and down your slit."
    m "Look how wet you are. You {i}really{/i} like being my bitch, don't you?"
    "You whine again, wiggling your hips."
    "After all you've been through, the least he can do is get you off."
    "But he takes his time, gently running his fingers up and down your slit, pulling them back when you try to press your pussy back toward him."
    m "Poor girl. You really want it bad, don't you?"
    "You can't help it; you whine again, wiggling your hips."
    "His fingers find your clit, rubbing hard, and you gasp."
    m "Remember, dogs can't speak."
    "Your clit throbs as he presses his fingers tight against it, rubbing harder and harder."
    "Panting, you wriggle against his hand, both craving the contact and trying to pull away from it."
    "Sensitive as you are, his harsh treatment is almost too much, but you don't want him to stop touching you."
    "He rubs your clit in rough circles, chuckling at the way you writhe against his hand."
    m "What a horny bitch you are..."
    "Your climax builds quickly, in spite of his roughness. Within minutes, you sink forward, shuddering as your pleasure crashes over you."
    "With your ass still in the air, you drift on a wave of sensation, nearly senseless with pleasure."
    "Matt presses his fingers to your mouth, letting you suck your juices from them."
    m "Good girl."
    "It isn't until you hear him walking away that you realize your eyes are still shut."
    "Blinking them against the light, you look for Matt. Your eyes catch him as he reaches the door."
    "Pushing yourself up onto your hands and knees, you look toward him."
    m "Stay, girl. I'll come back soon, okay?"
    "He laughs as he lets himself out of your apartment."
    "You wait for several minutes, sitting back on your heels and watching the door, before you realize he didn't mean tonight."
    "With trembling fingers, you unhook the collar and cradle it in your lap."
    if defymatt:
        "{i}Why{/i} do you let him do this to you?"
        "You barely even protest this time. You stripped without being told. You whined for him to finger you. You..."
        "Pushing the thoughts from your mind, you stand."
    elif True:
        "That was degrading. Dehumanizing."
        "Incredible."
        "Still a little lightheaded, you slowly stand."
    "It feels... strange, to be on your feet again, instead of your hands and knees."
    "Tucking the collar back under your mattress, you look down at yourself."
    "Your breasts are besmirched with his vulgar words, the ink running from the saliva and cum that dripped from your chin."
    "Below them, your stomach is equally stained with ink and, though you can't see it, you can almost feel it on the back of your thigh as well."
    "Stepping into the bathroom, you turn on the shower. It'll take a lot of scrubbing, but you have to get the ink off."
    if damienrelate == "dating":
        "What would Damien think if he saw those words?"
    if katerelate == "girlfriend":
        "Kate would be horrified..."
    if violetrelate == "Sub":
        "Violet wouldn't say anything - if she did, you'd have to punish her - but she'd be furious."
    if violetrelate == "Dom":
        "And if Violet saw, who knows what she'd do to you?"
    "You grab a washcloth and soap and start scrubbing."

    "You've reached the end of the current content in Matt's route! Stay updated on our Patreon for when the next event gets added!"

    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
