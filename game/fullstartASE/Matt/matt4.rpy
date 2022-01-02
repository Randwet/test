label matt_bullydamien:
    $ DamienAngry = "Characters/Damien/School Uniform/Angry.png"
    $ DamienBlank = "Characters/Damien/School Uniform/Blank.png"
    $ DamienGlare = "Characters/Damien/School Uniform/Glaring.png"
    $ DamienLaugh = "Characters/Damien/School Uniform/Laughing.png"
    $ DamienNeutral = "Characters/Damien/School Uniform/Neutral.png"
    $ DamienSad = "Characters/Damien/School Uniform/Sad.png"
    $ DamienShocked = "Characters/Damien/School Uniform/Shocked.png"
    $ DamienSmiling = "Characters/Damien/School Uniform/Smiling.png"
    $ DamienWorrying = "Characters/Damien/School Uniform/Worrying.png"
    $ clothes = 'school'
    show chelsea confused at right with moveinright
    "Walking between classes, you hear a familiar voice."
    show chelsea blank
    m "I bet you've never even seen boobs in {i}real{/i} life."
    if defymatt:
        "You're almost glad it's not you he's bullying this time, but you can't help feeling a pang of sympathy for whoever his current victim is."
    "Your eyes pan over the crowded hallway."
    show Matt Pleased at left with moveinleft
    show Damien Sad with dissolve
    if damienrelate=='dating':
        show chelsea sad
        "Your heart sinks when you see Damien, hands balled into fists at his sides."
    elif bullytelloff == 1:
        "You recognize the guy he's picking on; it's the guy you stood up for when Alex was bullying him. Damien."
    elif True:
        "Your gaze settles on Matt, but you don't recognize the guy he's tormenting."
    "As if he hears your thoughts, Matt's eyes fasten on yours."
    show Matt Smirk
    m "[pcname], get over here."
    if damienrelate == 'dating':
        jump matt_bullydamien_dating
    elif bullytelloff == 1:
        jump matt_bullydamien_talked
    elif True:
        jump matt_bullydamien_strangers



label matt_bullydamien_dating:
    show Damien Shocked
    "Damien's eyes widen as he hears your name."
    show Damien Glare
    D "Leave her out of it."
    show Matt Pleased at left
    "Matt grins."
    m "What are you gonna do about it?"
    show Matt Blank
    m "Well, [pcname]? What are you waiting for?"
    show chelsea sad
    show Matt Smirk
    "With leaden feet, you cross the hallway to stand beside them."
    "Damien stares Matt down, while you carefully avoid meeting his eye."
    show chelsea shocked
    "What if Damien tells him you're his girlfriend? What would Matt do...?"
    if defymatt:
        "Worse, what if Matt brings up the blackmail?"
    elif True:
        "Worse, what if Matt brings up all of the things you've done with him..."
    show Matt Happy
    m "You want to see a pair of tits? [pcname], show him yours."
    "Your eyes widen and your mouth falls open. Your mind races as you try to find a way out of this..."
    show Matt Question
    show Damien Angry
    D "No!"
    show Matt Blank
    "Damien's face is red - though whether he's embarrassed or angry, you can't tell."
    show Damien Neutral
    D "[pcname], just ignore him."
    "What should you do? Stand up to Matt or just stay quiet?"
    "If you stand up to Matt, he'll be furious. Who knows what he would say or do?"
    show chelsea sad
    "But if you stay quiet, it could be just as bad..."
    show Matt Question
    m "So you don't want to see her tits?"
    show Matt Happy
    show Damien Glare
    "Matt laughs."
    m "Are you a fag? Look at those tits; they're great."
    "Damien's fists tremble as he squeezes them tighter."
    show Damien Angry
    D "Shut up! Don't talk about her like that!"
    show Matt Smirk
    show Damien Glare
    m "Aww, I think he has a crush, [pcname]."
    "You know what Damien is going to say next, and it's the {i}last{/i} thing you want him to tell Matt."
    "If Matt knew you were dating Damien..."
    show chelsea angry
    show Damien Shocked
    pcname "Matt, just leave him alone."
    show Damien Blank
    show Matt Question
    "You blurt it out without thinking and the moment Matt turns toward you, you realize your mistake."
    show Matt Angry
    m "{i}You{/i} don't tell {i}me{/i} what to do..."
    show chelsea sad
    pcname "I just meant that..."
    "You give Damien an apologetic look, hoping he'll understand what you're trying to do."
    show chelsea embarrassed
    show Matt Blank
    if club == "track":
        pcname "I mean... Look at him."
    elif club == "cheer":
        pcname "He's not worth your time."
    elif club == "yearbook":
        pcname "He's... not really worth it... Is he?"
    show chelsea sad
    show Damien Shocked
    "The words leave a bitter taste in your mouth, but Matt seems to buy it."
    show Matt Pleased
    "Sneering, he turns back to Damien."
    m "Sorry, man. Looks like she has better taste than that."
    show Damien Sad
    "Damien stares at you, wide-mouthed, for a long moment, then slowly lowers his gaze to the floor."
    show Matt Happy
    "Matt laughs."
    m "Look, you broke his heart!"
    show GHCMan at midright with dissolve
    "Teacher" "Alright, you three. Get to class."
    hide GHCMan with dissolve
    show Matt Blank
    m "Whatever."
    "He turns back to Damien."
    show Matt Smirk
    m "Let me know if you change your mind about those tits."
    show Matt Happy
    "Laughing, he leaves you and Damien staring after him."
    hide Matt with moveoutleft
    if club == "track":
        pcname "Well, that was fun..."
    elif club == "cheer":
        pcname "Ugh, he's such a creep..."
    elif club == "yearbook":
        pcname "I-I'm..."
    "Damien shakes his head."
    show Damien Neutral
    D "I'm sorry, [pcname]. I shouldn't have let him talk about you like that."
    show Damien Blank
    pcname "No, {i}I'm{/i} sorry! I didn't mean what I said, I just..."
    show Damien Worry
    "He lets out a short, bitter laugh."
    D "I know. You were trying to rescue me. Again."
    show Damien Blank
    "The bell rings, signaling the start of class."
    show Damien Neutral
    D "And now I've made you late for class..."
    show chelsea happy
    if club == "track":
        pcname "It's fine. Really."
    elif club == "cheer":
        pcname "No big deal. I'll say I was having feminine problems."
    elif club == "yearbook":
        pcname "Th-that's okay..."
    show Damien Sad
    show chelsea blank
    "He tries to smile, but his eyes look sad."
    show Damien Neutral
    show chelsea sad
    D "I'll do better, I promise. I'll be the kind of boyfriend you deserve."
    show Damien Blank
    "Your heart wrenches."
    pcname "Damien..."
    show Damien Happy
    D "Better get to class before we get in trouble. I'll see you later, okay?"
    show chelsea happy
    show Damien Blank
    pause 1.0
    hide Damien Blank with dissolve
    "Smiling, you nod and watch him walk away."
    show chelsea shocked
    play sound PhoneVibration
    "{i}*Bzzt*{/i}"
    show chelsea sad
    "Frowning, you glance at your phone."
    call screen TextingScene("Matt",
    [
        TextMessage("What the fuck was that"),
        TextMessage("Meet me at the bathroom by the gym")
    ])
    "You might have saved Damien, but you knew what it would cost."
    "Taking a deep breath, you make your way to the bathroom."
    hide chelsea with moveoutright
    show black
    show Matt Blank
    show chelsea sad at right
    with fade
    "Matt stands outside, arms crossed."
    if club == "track":
        pcname "Sorry, I--"
    elif club == "cheer":
        pcname "I didn't mean to--"
    elif club == "yearbook":
        pcname "I-I'm sorry, I--"
    elif True:
        "..."
    show Matt Angry
    m "Shut up and follow me."
    if defymatt:
        "Against your better judgement, you follow him to a windowless door."
    elif True:
        "Dropping your gaze to the floor, you follow him silently to a windowless door."
    "He pulls it open, revealing a large janitor's closet."
    show Matt Smirk
    show chelsea shocked
    m "Well? Get inside, cunt."
    show chelsea sad
    pause 1.0
    hide chelsea with dissolve
    hide Matt with dissolve
    "Wincing at the insult, you dutifully step inside. He follows, closing the door behind him and engaging the lock."

    show chelsea with dissolve
    show Matt Question at left with dissolve
    m "So you thought you'd tell me what to do, huh?"
    if defymatt:
        if club == "track":
            show chelsea angry
            pcname "It's not like I {i}want{/i} to do what you tell me."
        elif club == "cheer":
            show chelsea blank
            pcname "Why not? You do it to me all the time."
        elif club == "yearbook":
            show chelsea sad
            pcname "I just... I don't like it when you pick on people..."
        show Matt Smirk
        "He sneers."
        m "Pretending you don't like it is getting really old, you know."
        show chelsea angry
        "You glare defiantly, but think better of arguing. You're already in trouble."
    elif True:
        pcname "I didn't mean to, I promise."
        show Matt Smirk
        "He sneers."
        show Matt Blank
        m "I don't really care what you meant."
    m "Get into position."
    hide chelsea
    hide Matt
    show bg MCCS1
    hide black
    with fade
    "You drop to your knees, putting your hands behind your head and lifting your chin."
    "Careful to keep your eyes downcast, you wait for your next instruction."
    if defymatt:
        "Your heart sinks as you realize how quickly you obeyed him."
        "You didn't even {i}try{/i} to argue."
        "Is it just that you know it won't help, or has he really broken you down that much?"
    elif True:
        "A sense of peace fills you as you wait. This is where you belong, on your knees and waiting to be told what to do."
    m "Put your hands behind your back and keep them there."
    "Hesitantly, you do as he tells you, tucking your hands behind your back."
    m "A slut like you doesn't tell {i}me{/i} what to do."
    "As he speaks, he unbuttons his pants and pulls his zipper down."
    m "A slut like you doesn't speak unless told. She knows her mouth is only useful when it's full of dick."
    "Freeing his cock, he waves it in your face. Instinctively, you lick your lips."
    m "Well? Open up."
    show bg MCCS2 with dissolve
    "As your lips part, he presses his cock against them, slapping it lightly all over your cheeks, lips, and chin."
    "It doesn't hurt, and compared to other things he's done, it's not particularly distasteful. But for some reason your cheeks burn with shame."
    "It's almost like your mouth isn't even worth his time right now."
    if defymatt:
        "Even if you don't want to suck him off, it's a blow to your pride."
    "After a few more slaps of his cock, Matt presses the head to your lips."
    if corruption > 40 and defymatt==True:
        "Instinctively, you open your mouth wider. You've sucked enough dick that it doesn't matter {i}why{/i} there's one in your mouth."
    elif corruption > 30:
        "Instinctively, you open your mouth wider. Matt's cock is so familiar, you know exactly how wide you need to go."
    elif True:
        "He pushes his cock into your mouth, barely giving you time to open wide enough for him."
    show bg MCCS3 with dissolve
    "You can tell how angry he is by the way he fucks your face, giving you no time to adjust to his girth before pressing himself to the back of your throat."
    if corruption > 25:
        "Thankfully, you're used to suppressing your gag reflex."
    elif True:
        "You struggle to suppress your gag reflex, tears welling in your eyes."
    m "That's right, slut. This is all your mouth is good for."
    show bg MCCS4 with dissolve
    "Grabbing hold of your head, he fucks your mouth hard, his balls slapping against your chin with every thrust."
    "It takes all of your control to keep your hands on your knees while he uses your mouth relentlessly."
    if defymatt:
        "You knew this would happen if you stood up to him. Why did you even try?"
        "Did you... want this?"
        "Your mind rebels at the thought. No! He's blackmailing you. There's no way you'd do this otherwise!"
    elif True:
        "You knew this would happen if you crossed him. You could pretend you were doing it for Damien, but deep down you know the truth."
        "You love it when Matt treats you like this. You deserve to be treated like this and he's the only one who will do it."
        "Damien might love you, but you don't {i}deserve{/i} love. You deserve to be used like the whore you are."
    "The salty taste of precum coats your mouth as Matt continues jamming his cock down your throat."
    if corruption > 25:
        "You work the muscles of your throat around his cock, edging him even closer to his climax."
        m "Fuck... You don't even gag anymore. Do you, slut?"
    elif True:
        "Tears trail down your cheeks as you try not to gag on his cock, barely holding it back."
        m "That's right. Choke on it, slut."
    "Suddenly he pulls back, jerking his cock in his fist as you gasp for breath."
    show bg MCCS6 with dissolve
    if defymatt:
        "Cum rains over your face. You try to catch as much in your mouth as you can; it'll make clean-up easier."
    elif True:
        "Cum rains over your face. You try to catch as much in your mouth as you can; that should make Matt happier."
    m "That's right. You love to eat my cum, don't you?"
    m "You're just a cum-guzzling little whore..."
    "You settle back into position, your hands still behind your back."
    "It's almost a point of pride now, that you could keep them there the entire time."
    if defymatt:
        "You force back the little surge of satisfaction; there's nothing to be proud of where Matt's concerned."
    elif True:
        "Your chest swells with a little surge of satisfaction."
    show bg MCCS5 with dissolve
    m "Have you learned your lesson, slut?"
    pcname "Yes, Matt."
    m "Good. Though I wouldn't mind repeating the lesson, if I have to..."
    if defymatt:
        "You barely restrain yourself from glaring at him."
    elif True:
        "You smile at the thought."
    m "And next time I tell you to show your tits to someone, you fucking show them."
    "Swallowing the lump that thought brings to your throat, you nod."
    "He leaves you on the floor, with your hands still tucked behind your back."
    show bg black with dissolve

    jump events_end_period

label matt_bullydamien_talked:
    show Damien Shocked
    show chelsea sad
    "Damien's eyes widen as he hears your name."
    show Damien Angry
    D "Leave her out of it."
    "Matt grins."
    m "What are you gonna do about it?"
    m "Well, [pcname]? What are you waiting for?"
    "With leaden feet, you cross the hallway to stand beside them."
    show Damien Glare
    "Damien stares Matt down, while you carefully avoid meeting his eye."
    show Matt Happy at left
    m "You want to see a pair of tits? [pcname], show him yours."
    show chelsea shocked
    "Your eyes widen and your mouth falls open. Your mind races as you try to find a way out of this..."
    show Matt Question
    show Damien Angry
    D "No!"
    show Matt Blank
    "Damien's face is red - though whether he's embarrassed or angry, you can't tell."
    show Damien Neutral
    D "[pcname], just ignore him."
    show chelsea sad
    "What should you do? Stand up to Matt or just stay quiet?"
    "If you stand up to Matt, he'll be furious. Who knows what he would say or do?"
    "But can you really flash this guy in the middle of the hallway?"
    show Matt Question
    m "So you don't want to see her tits?"
    show Matt Happy
    show Damien Glare
    "Matt laughs."
    m "Are you a fag? Look at those tits; they're great."
    show Matt Smirk
    "As if to make his point, Matt reaches over and squeezes one of your breasts."
    show chelsea shocked
    show Damien Shocked
    "You gasp."
    show Damien Angry
    D "H-hey! Knock it off! You can't just touch her like that!"
    m "Aww, I think he has a crush, [pcname]."
    show chelsea sad
    show Damien Glare
    "You can't meet Damien's eyes. He's trying to stand up for you, but he doesn't know that this is {i}nothing{/i} compared to the stuff Matt's already done to you."
    show Matt Pleased
    m "What do you say, Damien? You come to the bathroom with us and you can touch them too."
    show chelsea embarrassed
    "Your cheeks burn at Matt's words. Would he really do that?"
    show Damien Shocked
    if club == "track":
        pcname "What? You can't be serious!"
    elif club == "cheer":
        pcname "You wouldn't, would you?"
    elif club == "yearbook":
        pcname "No, p-please, Matt..."
    show Matt Happy
    "Laughing, he lets go of your breast."
    show Matt Smirk
    m "Sorry, man. Looks like she has better taste than that."
    show Damien Sad
    "Damien stares at you, wide-mouthed, for a long moment, then slowly lowers his gaze to the floor."
    show Matt Happy
    "Matt laughs."
    m "Look, you broke his heart!"
    show GHCMan at midright with dissolve
    "Teacher" "Alright, you three. Get to class."
    hide GHCMan with dissolve
    show Matt Blank
    m "Whatever."
    "He turns back to Damien."
    show Matt Smirk
    m "Let me know if you change your mind about those tits."
    m "C'mon, [pcname], let's go."
    "You follow him, glad you won't have to talk to Damien after this."
    hide Matt with dissolve
    hide chelsea with dissolve
    hide Damien
    show black
    with fade
    "To your surprise, he leads you to a windowless door."
    "Swinging it open, he ushers you inside."
    show chelsea with dissolve
    show Matt Blank at left with dissolve
    "He follows, locking the door behind him before turning back to you."
    show Matt Angry
    m "Man, that guy is lame... He wouldn't know what to do with a slut like you."
    show Matt Pleased
    m "Seeing your tits would probably give him a nosebleed."
    "As he speaks, he reaches out and grabs your breast again, squeezing it hard."
    show chelsea shocked
    pcname "Ah!"
    if defymatt:
        "You try to pull away."
        if club == "track":
            show chelsea angry
            pcname "Can't you just leave me alone?"
        elif club == "cheer":
            show chelsea angry
            pcname "You don't know what to do either."
        elif club == "yearbook":
            show chelsea sad
            pcname "No, s-stop..."
        show Matt Smirk
        "Matt sneers."
        m "Y'know, I'm getting really bored with you pretending you don't like this."
    elif True:
        show Matt Happy
        "Matt laughs."
        m "He'd probably cream his pants if he touched these."
    "With another squeeze, he steps back, releasing your breast as he looks over you."
    show Matt Smirk
    show chelsea sad
    m "Hurry up and strip."
    hide chelsea
    hide Matt
    hide black
    show bg MCCS7
    with fade
    "After a quick glance around the closet, you quickly pull off your shirt and drop your skirt."
    "His eyes rake over your body, but he's not happy yet."
    m "All of it."
    "Unhooking your bra, you drop it on top of your other clothes. Then you hook your thumbs in your panties and pull them down."
    "Kicking them aside, you wait for Matt's instructions."
    if defymatt:
        "Even though you don't want Matt, your body knows what's coming."
        "To your shame, you feel a rush of warmth flood your pussy."
    elif True:
        "Warmth floods your pussy as your body prepares itself for what's coming."
    m "He really wouldn't know what to do now, would he?"
    "You shake your head."
    m "Maybe I should go get him and see if he can figure it out..."
    "You can't hold back the small whimper that escapes your throat. Matt wouldn't {i}really{/i} do that..."
    "Would he?"
    show bg MCCS8 with dissolve
    "Laughing darkly, Matt reaches down to cup your pussy."
    "His finger presses against your slit, parting your labia and pushing against your opening."
    m "What a little whore you are, getting so wet thinking about me whoring you out."
    m "That's not a bad idea, actually..."
    "His finger presses inside of you as he considers the idea."
    pcname "Matt..."
    "You stop yourself mid-protest. Would that just encourage him?"
    if defymatt:
        "It's bad enough that Matt uses you for his own pleasure. Giving you to someone else?"
        "You expect your stomach to roll at the thought, but for some reason it doesn't."
    elif True:
        "Does it matter? If Matt wants to give you to someone else, you can't stop him."
        "If it's what he wants, you'd do it, wouldn't you?"
        "Your heart beats faster at the thought."
    show bg MCCS9 with dissolve
    "As you fret over his comments, he draws his finger out of you and drops his hands to his zipper."
    show bg MCCS10 with dissolve
    "Pulling his cock free, he lifts your leg, throwing you off balance."
    "Leaning back against the table, you catch yourself on your elbows."

    "Holding your leg in the air, Matt presses his dick to your opening, teasing you with the head of his cock."
    show bg MCCS11 with dissolve
    "His other hand grabs your breast, squeezing hard."
    show bg MCCS12 with dissolve
    "As you tilt your head back, he thrusts into you."
    if corruption > 40:
        "You're pleasantly surprised as he fills you in a single thrust, your body stretching eagerly to accommodate him."
    elif True:
        "Your body protests as he fills you in a single thrust, stretching you before you're ready, but you soon adjust."
    m "That's it, slut. You can take it all at once."
    pcname "Matt..."
    if defymatt:
        "Though you know you're being forced to do this, your body responds to his movements."
        "And, at this point, you might as well let yourself enjoy it..."
    m "What do you want, slut?"
    menu matt_bullydamien_talked_fuck:
        "Harder!" if True:
            if club == "track":
                pcname "Fuck me harder!"
            elif club == "cheer":
                pcname "I want you to fuck me harder!"
            elif club == "yearbook":
                pcname "I... Please! Harder!"
            show bg MCCS13 with dissolve
            "His fingers dig into your breast as he thrusts again and again."
            "Your pussy clenches around his cock, squeezing him tight."
            "Tucking your knee up on his shoulder, he grabs your hip with his other hand, using it for leverage so he can slam his cock into your pussy even harder."
            "Your body rocks with every thrust, and the pleasure quickly builds until you can't take any more."
            "Clamping a hand over your mouth, you cry out your pleasure as your orgasm leaves you shuddering on the table."
            "Matt thrusts into your shivering body, moaning as your pussy clamps around his cock in spasming delight."
            "As wave after wave of pleasure crashes over you, he empties himself into you in hot spurts."
        "Don't stop!" if True:
            if club == "track":
                pcname "Just... Don't stop!"
            elif club == "cheer":
                pcname "Don't stop, Matt!"
            elif club == "yearbook":
                pcname "D-don't stop!"
            show bg MCCS14 with dissolve
            "His fingers twist at your nipple, drawing another gasp from your throat."
            "He thrusts into you over and over, filling you with his cock until you can barely think."
            m "Touch yourself."
            "You obey him immediately, your hand slipping between your legs to play with your clit."
            "The little nub is swollen and hard; the moment you touch it, pleasure shoots out like a jolt of electricity."
            "Your fingers rub slow circles while Matt plunges his dick in and out of your dripping cunt."
            "It doesn't take long before those jolts of pleasure become a thunderous storm and you cry out as you cum."
            "But Matt doesn't stop thrusting, and as your fingers go still he barks another order."
            m "I didn't tell you you could stop. Touch yourself."
            "You move to obey, your fingers moving slowly over your swollen, tender clit."
            "The pleasure is so intense it almost hurts, but you do as Matt says and rub it until you can barely take anymore."
            pcname "M-Matt..."
            "He moans, emptying himself into you in hot spurts."
    "As soon as he catches his breath, he pulls his cock out of you."
    m "Get up."
    show bg MCCS16 with dissolve
    "Limbs heavy, you pull yourself off the bench and stand."
    m "On your knees."
    "You sink slowly to your knees, still a little off balance."
    "As soon as you look up at him, he pushes his cock toward you."
    m "Lick it clean."
    show bg MCCS17 with dissolve
    "You wet your lips with your tongue and begin licking his dick."
    "Swirling your tongue over the tip, you taste your juices mixed with his."
    if defymatt:
        "Still lightheaded from your orgasm, it's easy to forget the blackmail and just lose yourself in the flavors and sensations."
    elif True:
        "Still lightheaded from your orgasm, you let your eyes drift shut and your mind clear, losing yourself in the flavors and sensations."
    "When he's satisfied, he steps back, tucking his cock into his pants."
    m "Maybe next time I'll let him watch. Would you like that, slut?"
    if club == "track":
        "You hold back a glare, forcing your expression to remain neutral."
    elif club == "cheer":
        "Your eyes widen and you bite your lip."
    elif club == "yearbook":
        "Your cheeks burn. Your eyes drop to the floor."
    if defymatt:
        "You're sure that anything you say will only encourage him, and that's the last thing you want."
        "Isn't it?"
    elif True:
        "Your heart pounds against your ribs as you consider it."
        "It would be mortifying, but isn't that what you deserve?"
        "To be used, abused, and degraded like the whore you are?"
    "Matt laughs as he turns away, leaving you naked on the floor, with his cum running down your thighs."

    jump events_end_period

label matt_bullydamien_strangers:
    show Damien Shocked
    "The boy's eyes widen as he hears your name."
    "Boy" "What are you doing...?"
    show Matt Smirk at left
    "Matt grins."
    show Damien Glare
    m "What are you gonna do about it?"
    m "Well, [pcname]? What are you waiting for?"
    show chelsea sad
    "With leaden feet, you cross the hallway to stand beside them."
    "The boy stares Matt down, while you carefully avoid meeting his eye."
    show Matt Pleased
    m "You want to see a pair of tits? [pcname], show him yours."
    show chelsea shocked
    show Damien Shocked
    "Your eyes widen and your mouth falls open. Your mind races as you try to find a way out of this..."
    show Damien Angry
    "Boy" "No!"
    "His face is red - though whether he's embarrassed or angry, you can't tell. He turns to you, shaking his head."
    show Damien Blank
    "Boy" "You don't have to do that! Just ignore him."
    show chelsea sad
    "What should you do? Stand up to Matt or just stay quiet?"
    "If you stand up to Matt, he'll be furious. Who knows what he would say or do?"
    "But can you really flash this guy in the middle of the hallway?"
    show Matt Question
    m "So you don't want to see her tits?"
    show Matt Happy
    "Matt laughs."
    m "Are you a fag? Look at those tits; they're great."
    show chelsea shocked
    show Matt Smirk
    "As if to make his point, Matt reaches over and squeezes one of your breasts."
    show chelsea shocked
    show Damien Shocked
    "You gasp."
    show Damien Angry
    "Boy" "H-hey! Knock it off! You can't just touch her like that!"
    m "Aww, I think he has a crush, [pcname]."
    show chelsea sad
    show Damien Glare
    "You can't meet the boy's eyes. He's trying to stand up for you, but he doesn't know that this is {i}nothing{/i} compared to the stuff Matt's already done to you."
    m "What do you say, Damien? You come to the bathroom with us and you can touch them too."
    show chelsea embarrassed
    "Your cheeks burn at Matt's words. Would he really do that?"
    show Damien Shocked
    if club == "track":
        pcname "What? You can't be serious!"
    elif club == "cheer":
        pcname "You wouldn't, would you?"
    elif club == "yearbook":
        pcname "No, p-please, Matt..."
    show Matt Happy
    "Laughing, he grabs your breast harder."
    show Matt Pleased
    m "Why not? Look at him! Someone should take pity on the poor guy."
    show Damien Sad
    "Damien stares at you, wide-mouthed, for a long moment, then slowly lowers his gaze to the floor."
    show Matt Happy
    "Matt laughs."
    m "Look, he's not protesting anymore."
    show GHCMan at midright with dissolve
    "Teacher" "Alright, you three. Get to class."
    show Matt Pleased
    m "Whatever. He was just asking where the bathroom was, weren't you, Damien?"
    show Damien Neutral
    "He turns back to Damien, who looks ready to run."
    D "Uhh... Yeah, that's right."
    hide GHCMan with dissolve
    "As the teacher walks away, Matt grabs Damien by the arm."
    show Matt Smirk
    m "C'mon, [pcname], let's show him where the bathroom is."


    hide Matt with dissolve
    hide Damien with dissolve
    hide chelsea with dissolve



    show black
    with fade


    show Matt Pleased at left with dissolve
    show Damien Worry at center with dissolve
    show chelsea sad at right with dissolve
    "Heart racing, you follow them toward the men's room, but he stops short and opens a different door."
    m "Well? Get in there you two."
    show Damien Shocked
    "Damien begins shaking his head, but Matt pushes him inside."
    hide Damien with dissolve
    show Matt Happy
    m "Get in there, [pcname]."
    hide chelsea with dissolve
    hide Matt with dissolve
    "He follows, locking the door behind him before turning back to you and Damien."
    hide bg black with dissolve
    show bg MCDCS1 with dissolve
    m "Alright, now let's get this shirt off."
    D "You can't be serious. Just let us leave!"
    D "[pcname], you don't have to do this!"
    m "Her? She's a fucking {i}slut{/i}. She'd {i}love{/i} to show off her tits. Isn't that right, slut?"
    if defymatt:
        "Your face burns with shame as you listen to Matt's words. But you know what will happen if you disagree with him."
        "And you can think of plenty of ways he could make things so much worse for you."
        if club == "track":
            pcname "Yeah, whatever..."
        elif club == "cheer":
            pcname "You know me, Matt..."
        elif club == "yearbook":
            pcname "O-of course..."
    elif True:
        "As much as you hate to admit it, he's right. Something about this situation really turns you on."
        "As usual, Matt knows exactly what you want - even if you don't."
    "Matt grins."
    m "See? She wants to."
    "Shocked and confused, Damien can only stare at you."
    m "So? Let's see those tits."
    "After a quick glance around the closet, you quickly pull off your shirt and wrap your arms around yourself."
    "Matt's eyes rake over your body, but he's not happy yet."
    m "Bra too. Don't tease the poor guy."
    "Biting your lip, you reach behind your back and unhook your bra."
    "Slipping it down your arms, you toss it onto your discarded shirt."
    m "Well? Go on, Damien. Touch them."
    "Damien shakes his head, but his eyes are drawn to your breasts."
    "You can feel your nipples stiffen in the cool air - or, at least, you tell yourself that's the reason."
    show bg MCDCS2 with dissolve
    "Matt reaches out and pinches one of your nipples, eliciting a surprised gasp."
    m "Listen to her; she likes it."
    "Damien licks his lips, but shakes his head again."
    if defymatt:
        "You want to sympathize with Damien; he's as much a victim as you are."
        if club == "track":
            "But you can barely believe how spineless he is."
            "At least Matt is honest about what he wants; Damien's face might be saying no, but his eyes haven't left your body."
        elif club == "cheer":
            "But you can tell how much he wants to touch you. Even as he shakes his head, his eyes are fixed on your breasts."
        elif club == "yearbook":
            "You thought he might refuse, but now..."
            "Heat suffuses your cheeks as you realize that he can't seem to take his eyes off your breasts."
        "He may act like he's better than Matt, but you have your doubts."
    elif True:
        "Though you felt sorry for him at first, you find it difficult to pity Damien."
        if club == "track":
            "You can barely believe how spineless he is."
            "At least Matt is honest about what he wants; Damien's face might be saying no, but his eyes haven't left your body."
        elif club == "cheer":
            "You can tell how much he wants to touch you. Even as he shakes his head, his eyes are fixed on your breasts."
        elif club == "yearbook":
            "You thought he might refuse, but now..."
            "Heat suffuses your cheeks as you realize that he can't seem to take his eyes off your breasts."
        "No wonder Matt was harassing him; he's such an easy target."
    m "Seriously? Just touch her."
    show bg MCDCS3 with dissolve
    "Tired of Damien's reservations, Matt grabs him by the wrist and pushes his hand over your breast."
    D "Hey!"
    "Matt rolls your nipple between his fingers until you can't hold back a moan."
    pcname "Mmmm..."
    "Mistaking your moan as a reaction to him, Damien seems conflicted."
    "Slowly, his fingers tighten around your breast, lifting it slightly."
    if defymatt:
        "You can barely believe what's happening to you."
        "You barely know this guy and here he is, groping you in a closet."
        "Worse, you can feel your body responding to the assault regardless of your own wishes."
    elif True:
        "Matt was right, as usual. Damien might have pretended not to want this, but he's not protesting now."
    "As you watch, Damien's breathing quickens as he lifts your breast, feeling the weight of it in his hand."
    "His thumb runs over your nipple and he gasps as it stiffens even more."
    show bg MCDCS4 with dissolve
    m "Don't be a pussy. Give it a good pinch; she likes it."
    "Matt twists your nipple until you cry out again."
    pcname "Ohh~!"
    "Following his lead, Damien pinches your nipple between his pointer and thumb and gives it a little twist."
    pcname "Ah~!"
    "Encouraged, Damien twists harder, licking his lips as you shudder."
    pcname "Ohh~!"
    "Matt releases your nipple and takes a step back, smiling smugly as Damien continues toying with your nipple."
    m "Don't forget the other one."
    "Damien slowly lifts his other hand, his eyes searching your face for any sign of disapproval."
    "Finding none, he cups your other breast too, gently twisting both of your nipples between his fingers."
    pcname "Ahh~!"
    "Your nipples ache with pleasure as he teases them. Rolling them between his fingers, he watches your reaction, gasping when you do."
    m "See how much she likes it?"
    "Damien nods, enspelled by your responses."
    m "Alright, slut, get on your knees."
    if defymatt:
        "Your mouth drops open, but you can't find the words. What choice do you have?"
        "You can let one person see what Matt does to you - or let the whole school see."
    elif True:
        "You lick your lips. Matt's never made you perform for someone else before..."
        "But if it's what he wants, you know you'll do it."
    "Damien releases your nipples as you sink to your knees."
    show bg MCDCS5 with dissolve
    "Looking up at Matt, you wait to hear what else he has planned for you."
    "Without a word, he unzips his pants and pulls his cock free."
    D "What are you...?"
    m "Shut up and see if you can learn something."
    show bg MCDCS6 with dissolve
    "Matt steps toward you, his dick aimed at your lips."
    if defymatt:
        "To your shame, you open your mouth without being told."
    elif True:
        "Anticipating his desires, you open your mouth eagerly."
    m "See how much she loves sucking dick?"
    if defymatt:
        if club == "track":
            "You force yourself to stay quiet; who knows what Matt will do if you argue?"
        elif club == "cheer":
            "You try to ignore him, preparing to suck him off by relaxing your throat and flattening your tongue."
        elif club == "yearbook":
            "You flush with embarrassment, but you're sure neither of them notice."
    elif True:
        if club == "track":
            "You nod, licking your lips."
        elif club == "cheer":
            "You smile and lick your lips."
        elif club == "yearbook":
            "Blushing, you lick your lips."
    if corruption > 25:
        "Sticking your tongue out, you slather his cock with your saliva until he's well lubed."
        "Matt presses himself between your lips and you open wide, taking him easily."
        m "Fuck... Look how much she can swallow at once."
        "Bobbing your head, you relax your throat. His balls slap against your chin as you swallow his cock."
        "Damien gasps as you push your face tight to Matt's hips, holding your breath as long as you can."
        "Your nose flares as you pull back, taking a deep breath before deep-throating him again."
        "Over and over you swallow Matt's cock, working the muscles of your throat around him."
        if defymatt:
            "Despite the situation, you take a certain pride in your performance."
            "Especially when you notice Damien's cock straining hard against the front of his uniform."
        elif True:
            "Your chest swells with pride; you know most girls can't suck cock as well as you can."
            "You know Matt's trained you well - especially when you see Damien's growing bulge."
        "Damien's hand falls to his pants, absently rubbing himself."
        "You meet Damien's eyes, holding his gaze as you swallow Matt's cock again."
        show bg MCDCS7 with dissolve
        "Damien moans, unzipping his pants and freeing his erection."
        "As he beats himself off, you continue sucking Matt's cock, bobbing your head faster and faster."
        if defymatt:
            "For a moment, you forget how much you hate Matt for forcing you to do this - or that you're being forced at all."
        "Two men are overcome with their lust for you; the power is almost intoxicating."
        "As you pull back for another breath, you watch as Damien's eyes practically roll back in his head."
        if corruption > 40:
            "Reaching toward him, you beckon him closer."
            show bg MCDCS8 with dissolve
            "He steps forward and you wrap your hand around his cock."
            "Sinking your face back down on Matt's dick, you begin stroking Damien's."
            show bg MCDCS9 with dissolve
            "It's too much for Damien; in less than a minute his hips jerk back and forth, and he empties himself into your hand."
            "He steps back, flushing with shame and arousal, his eyes still fixed on your mouth around Matt's cock."
            "Refocusing your attention, you bob your head faster and faster, until the sound of Matt's balls slapping against your chin echo through the closet."
            "Salty precum coats your tongue and saliva drips over your chin, as you bring him closer and closer."
            m "Fuck... Fuck..."
            show bg MCDCS10 with dissolve
            "Suddenly his hips jerk and he grabs the back of your head, grinding against your face."
            "His cock spasms, pouring cum down your throat in hot, sticky spurts."
            show bg MCDCS11 with dissolve
            "When he finally releases you, you sit back on your heels, gasping for breath."
            "Cum and saliva coat your chin. You go to wipe it, but realize your fingers are still sticky with Damien's load."
            m "Guess you have more to swallow, huh?"
            "Damien's mouth falls open as he realizes what Matt means."
            D "You don't have to--"
            show bg MCDCS12 with dissolve
            "He goes silent as you thrust your fingers into your mouth, sucking them clean."
            "Then you wipe your chin off and lick the cum from your fingers again."
            m "See what I mean? She can't get enough."
            if club == "track":
                "You can't argue, so you just shrug."
            elif club == "cheer":
                "You smile, licking your lips clean too."
            elif club == "yearbook":
                "Blushing, you lick the last bit of cum from your lips."
        elif True:
            "Even though he'd barely begun touching himself, you can tell Damien's nearing his own climax."
            show bg MCDCS13 with dissolve
            "In less than a minute his hips jerk back and forth, and he empties himself into his own hand."
            "Face flush with shame and arousal, he looks for something to clean his hand with."
            "As he searches, you taste the familiar flavor of Matt's precum coating your tongue."
            m "Fuck... Fuck..."
            "Suddenly his hips jerk and he grabs the back of your head, grinding against your face."
            "His cock spasms, pouring cum down your throat in hot, sticky spurts."
            "When he finally releases you, you sit back on your heels, gasping for breath."
            m "Need help with that?"
            "You look at Damien, who still hasn't found a way to clean his hand off."
            m "Help him out, slut."
            "Reaching toward him, you take Damien's hand by the wrist and draw him closer."
            "Sucking each one, you use your lips and tongue to clean the cum from his fingers before licking the rest off his palm."
            "Then you wipe your chin off and lick the cum from your fingers."
            m "See what I mean? She can't get enough."
            if club == "track":
                "You can't argue, so you just shrug."
            elif club == "cheer":
                "You smile, licking your lips clean too."
            elif club == "yearbook":
                "Blushing, you lick the last bit of cum from your lips."
    elif True:
        "Matt presses himself between your lips. You open wide, but struggle to take more than a few inches."
        m "Well, she loves it, but she's still not very good at it."
        "Wrapping your hand around his cock, you stroke him while you suck, trying to make up for your lack of skill."
        "Damien doesn't seem to care that you can't deep-throat; he gasps as you bob your head, taking in as much as you can."
        if defymatt:
            "Despite Matt's words, you take a certain pride in your performance when you notice Damien's cock straining hard against the front of his uniform."
        elif True:
            "Afraid of disappointing Matt any further, you do your best to make up for any lack of skill."
            "You know Matt's trained you well when you see Damien's growing bulge."
        "Damien's hand falls to his pants, absently rubbing himself."
        "You meet Damien's eyes, holding his gaze as you swallow Matt's cock again."
        show bg MCDCS7 with dissolve
        "Damien moans, unzipping his pants and freeing his erection."
        "As he beats himself off, you continue sucking Matt's cock, bobbing your head faster and faster."
        if defymatt:
            "For a moment, you forget how much you hate Matt for forcing you to do this - or that you're being forced at all."
        "Two men are overcome with their lust for you; the power is almost intoxicating."
        "As you bob your head again, you watch as Damien's eyes practically roll back in his head."
        "Even though he'd barely begun touching himself, you can tell Damien's nearing his own climax."
        show bg MCDCS13 with dissolve
        "In less than a minute his hips jerk back and forth, and he empties himself into his own hand."
        "Face flush with shame and arousal, he looks for something to clean his hand with."
        "As he searches, you taste the familiar flavor of Matt's precum coating your tongue."
        m "Fuck... Fuck..."
        "Suddenly his hips jerk and he grabs the back of your head, grinding against your face."
        "You gag as his cock hits the back of your throat, pouring cum down your throat in hot, sticky spurts."
        "When he finally releases you, you sit back on your heels, coughing and gasping for breath."
        m "Need help with that?"
        "You look at Damien, who still hasn't found a way to clean his hand off."
        m "Help him out, slut."
        "Reaching toward him, you take Damien's hand by the wrist and draw him closer."
        "Sucking each one, you use your lips and tongue to clean the cum from his fingers before licking the rest off his palm."
        "Then you wipe your chin off and lick the cum from your fingers."
        m "See what I mean? She can't get enough."
        if club == "track":
            "You can't argue, so you just shrug."
        elif club == "cheer":
            "You smile, licking your lips clean too."
        elif club == "yearbook":
            "Blushing, you lick the last bit of cum from your lips."
    if defymatt:
        "As they tuck their dicks into their pants, you realize how you must look."
        "You barely put up any fight at all; what must Damien think of you?"
        "He's barely taken his eyes off of you the whole time. He'll probably think of this when he..."
    elif True:
        "As they tuck their dicks into their pants, you smile to yourself."
        "You can only hope that Damien thinks about this the next time he's with a girl."
        "...if that ever happens."
    m "Don't look so sad, slut. You can suck it again soon."
    "Blushing, you wait for Matt to give you more instructions."
    D "I can't believe that really happened..."
    "Damien takes a step toward the door, glancing back and forth between you and Matt."
    D "I need to get to class. I'm going to be in trouble..."
    "Matt laughs as Damien flees the room."
    m "I can guarantee that's the closest to sex he's ever gotten."
    if defymatt:
        "You want to rage at Matt for letting someone else see you like that, but you're suddenly too tired to do it."
        "It never helps; he still just does whatever he wants to you anyway."
    elif True:
        "You smile; you know he's right."
        "And showing off Matt's training was surprisingly exciting."
    m "Alright, get dressed before the janitor comes in. Maybe he wouldn't tell if you sucked him off too, but I wouldn't want to find out."
    "Laughing, he lets himself out, leaving you topless on the floor."

    jump events_end_period

label matt_lending:
    show Harley Neutral
    T "Now that everyone has the handout, you may work on that for the remainder of class. Anything you don't finish is homework."
    hide Harley with dissolve
    if intelligence >= 40 and intelligence <=50:
        "You diligently work on the packet of papers."
    elif intelligence >= 20 and intelligence < 40:
        "You look over the worksheet, answering the easy questions first."
    elif True:
        "You toss the papers aside and pull out your phone."
    "After a few minutes, a conversation catches your attention."
    show Matt Smirk with dissolve
    show GSBoy at left with dissolve
    m "Yeah, well I have a girl who will do {i}anything{/i} I tell her to."
    "Classmate" "Yeah, sure, Matt."
    show Matt Happy
    if bullytelloff == 1:
        m "One time she pissed off a friend of mine, so we both had her on the teacher's desk after school."
    elif True:
        m "One time I went over to her house, made her strip, then slapped a collar on her and made her fetch like a dog."
    show chelsea sad at right with dissolve
    if defymatt:
        "Your chest tightens as you realize what he's saying."
    elif True:
        "Your chest tightens."
        show chelsea embarrassed
        "It's embarrassing, but you can't help feeling just a little pleased that Matt would brag about you like this."
    "Classmate" "You're full of shit. If that's true, let me meet her."
    show chelsea shocked
    show Matt Smirk
    play sound PhoneVibration
    "You can't hear Matt's response, but when you're phone suddenly vibrates a few seconds later, you know it must be him."
    call screen TextingScene("Matt",
    [
        TextMessage("Skip your next class"),
        TextMessage("Meet me in the janitor's closet")
    ])
    if defymatt:
        show chelsea sad
        "There's a weight in your stomach when you think about the janitor's closet."
    elif True:
        show chelsea happy
        "You smile, recalling your last time in the janitor's closet."
        show chelsea embarrassed
    "And if you heard them correctly, you have a feeling Matt won't be alone."
    if defymatt:
        "You don't know if you can keep doing this."
        "Every time you let Matt degrade you, you can't help but wonder if it's worth it."
        "Why would you let him do these things to you? Does it matter if those pictures get out, if it means you won't have to do this anymore?"
        "Or do you let it continue because some part of you is enjoying it?"
        hide Matt with dissolve
        hide GSBoy with dissolve
        menu matt_lending_choice:
            "Ignore him." if True:
                show chelsea angry
                "No! You hate what he makes you do. You hate {i}him{/i}."
                "And you've had enough. When the bell rings, you walk directly to your next class, heart pounding."
                show chelsea shocked
                "As you take your seat, you feel a moment of panic as you wonder if you're doing the right thing."
                show chelsea happy
                "Then the bell rings and, for the first time in a long time, you feel... free."
                show chelsea laugh
                "Matt can do his worst; you won't let him control you anymore."
                $ mattblackmail = 2
                jump events_end_period
            "Go to the closet." if True:
                "You don't want to think about why; you just know that nobody can ever see those pictures."
                "As soon as the bell rings, you make your way to the closet and step inside."
    elif True:
        hide Matt with dissolve
        hide GSBoy with dissolve
        "Your heart races as you wait for the bell to ring, wondering what Matt has planned for you."
        "Nervousness wars with excitement; you're not even sure {i}who{/i} Matt was talking to."
        hide chelsea with dissolve
        "As soon as the bell rings, you make your way to the closet and step inside."
    with fade

    "A few minutes later, the door swings open and Matt ushers another boy inside."
    "You recognize him immediately, though you've never spoken before. You're pretty sure his name is Drew."
    m "See, what did I tell you?"
    "Drew" "[pcname]? Are you serious?"
    if club == "track":
        "You shrug. Who is he to judge you?"
    elif club == "cheer":
        "You smile, giving him a little shrug."
    elif club == "yearbook":
        "You look down, embarrassed."
    m "Watch."
    "Your eyes dart to Matt and you wait to hear what he wants from you."
    m "Strip, slut."
    "Drew" "Dude, she's not going to--"
    if defymatt:
        "There's no point arguing; you knew what would happen if you came here."
        "Taking a deep breath, you begin by pulling your shirt over your head and dropping it hesitantly to the floor."
    elif True:
        pcname "Of course."
        "You pull your shirt over your head and casually drop it on the floor."
    "Drew stares, his mouth hanging slightly ajar as your bra joins your shirt."
    if defymatt:
        "You try to ignore his eyes on you as you let your skirt pool around your ankles."
    elif True:
        "You watch, a little satisfied by his reaction, as you let your skirt pool around your ankles."
    "Sliding your panties over your hips, you let them fall to the floor as well, kicking them aside."
    "Drew" "Holy shit. You can't be serious."
    m "I told you. And that's not all."
    "Matt smirks."
    m "Tell Drew what a slut you are."
    if defymatt:
        "You stare at Matt, but you know it's too late to argue. You've already stripped in front of Drew, why defend yourself now?"
    "You think about all the things Matt's said about you, trying to come up with something that will please him."
    if club == "track":
        pcname "I'm a dirty whore who can't live without a {i}hard{/i} cock."
    elif club == "cheer":
        pcname "I'm a dirty little slut, and I can't get enough cum."
    elif club == "yearbook":
        pcname "I-I'm a dirty slut. Can't you tell...?"
    "Drew's bewildered expression slowly turns to a grin."
    "Drew" "Is that so?"
    "Whatever concerns he had about the situation disappear with your confession."
    if defymatt:
        "As always, Matt makes you complicit in your own degradation."
    m "Don't just stand there. Get on your knees and show him."
    if defymatt:
        "You knew this was coming and, suddenly, you don't have the will to resist."
        "Better just to do as he says and get it over with, right?"
    elif True:
        "You knew this was coming, didn't you?"
        "And this is all you're good for, so who cares if Matt wants you to blow some other guy?"
    "You drop to your knees and look up at Drew, waiting."
    "But it seems he's too surprised to react."
    m "Well? Do you want to suck his dick or not?"
    "Crawling to him, you look up at Drew as you unzip his pants."
    "His dick strains against his boxers, practically leaping toward you as you spread the front of his pants open."
    "Pulling his pants down, you slowly lower his boxers until his cock springs free."
    "As it waves in your face, you lift your eyes to his and run your tongue over his tip."
    "You circle the head of his cock with your tongue before lifting it so you can lick his balls."
    "Drew" "Oh fuck..."
    "You lick and suck one and then the other, running your tongue up his sack between them, and the whole way up to the head of his cock again."
    "Sliding your tongue up and down his cock, you get him good and wet before wrapping your lips around his cock and slowly lowering your head on it."
    if corruption > 40:
        "You swallow his cock easily, not stopping until his balls slap lightly against your chin."
        "Looking up, you press your nose against his pubic bone and work the muscles of your throat around his dick, massaging it."
        "You hold him there as long as you can, only pulling back long enough to catch your breath before swallowing him again."
        "As you do, you slip a hand between your thighs."
        "Two fingers sink into your cunt while your thumb rubs slow circles over your clit."
        "All the while, you continue deep-throating his cock."
    elif corruption > 25:
        "Taking a deep breath, you relax your throat and take him into your mouth."
        "He gasps when his cock slides down your throat, his balls pressing against your chin."
        "You struggle a little against your gag reflex, but he seems to enjoy the way your muscles flex around his cock."
        "A few seconds later, you pull back again, gasping for air."
        "After a few more times of swallowing his cock, though, your throat adjusts to the invasion and you stop struggling."
        "As you grow more comfortable, your hand slips between your thighs, where two fingers sink into your cunt and your thumb rubs across your clit."
    elif True:
        "You take as much of him in as you can, gagging when his cock touches the back of your throat."
        "Despite several attempts, you can't suppress your gag reflex enough to fully take his dick in your mouth."
        "Instead, you wrap one hand around the base of his cock, comfortably sucking the rest."
        "As you stroke and suck, you let your other hand drift between your thighs."
        "Pressing two fingers into your cunt, you allow your thumb to rub over your clit in slow circles."
    "Drew" "Oh shit..."
    "As you suck him off, a shadow falls over your face."
    "Matt stands to your side, his hard cock jutting toward you."
    if corruption < 26:
        "Releasing Drew's cock, you take hold of Matt's and begin stroking it."
    elif True:
        "With your free hand, you take hold of Matt's dick and begin stroking it."
    m "That's right. You couldn't wait to get your hand on another dick, could you, slut?"
    if defymatt:
        "He's right; he didn't even have to tell you this time. What's wrong with you?"
    elif True:
        pcname "Mmmhmmm..."
        "You hum your approval around the dick in your mouth."
    "Your fingers work in and out of your pussy as you continue sucking one cock and jerking off the other."
    "Heavy breathing and the wet, sloppy sounds of suction, spit, and your drooling cunt fill the room."
    m "Alright, my turn."
    "Matt grabs your hair and pulls you off Drew's cock. Twisting your head toward him, he jams his dick into your mouth."
    if corruption > 25:
        "You swallow his cock easily, your eyes meeting his as your nose presses into his skin."
    elif True:
        "You gag, unprepared for the sudden change."
        "Matt laughs, pulling back just a little."
    "As you begin sucking him off, you hold your now-free hand toward Drew."
    "He slips his cock against your palm and you wrap your fingers around his spit-soaked shaft."
    "Drew" "Shit, you weren't kidding..."
    "Matt holds your head in place, using your mouth while you stroke Drew's cock."
    "As you pleasure them, you feel your pussy reacting."
    "Your labia and clit swell, your cunt tightens around your fingers, and your juices drip down your hand."
    m "Fuck..."
    "He yanks your hair again, pulling you off of his cock."
    "Saliva drips down your chin as he turns you back toward Drew."
    "You guide it into your mouth, taking Matt's cock in your hand again."
    "Encouraged by Matt's rough treatment, Drew puts his hand on the back of your head and pulls you down on him."
    if corruption > 40:
        pcname "Mmmmm..."
        "You swallow his cock eagerly, past the point of caring who you're sucking off."
        pcname "Mmm... Mmm..."
        "His cock slams down your throat over and over, his balls slapping loudly against your chin."
    elif corruption > 25:
        "You're surprised, but adjust quickly, swallowing his cock with ease."
        "Drew" "Oh fuck..."
        "Encouraged by his reaction, you bob your head faster, his balls slapping lightly against your chin."
    elif True:
        "You gag and sputter, but he holds you there until your eyes brim with tears."
        "He eases his grip, allowing you to lean back before you lose control of your gag reflex."
        "Bobbing your head faster and faster, you do your best to please him without gagging yourself."
        "Drew" "Shit that's good..."
    "Your pussy spasms around your fingers, clenching tightly, but it's not enough."
    menu matt_lending_fuck:
        "Rub yourself off." if True:
            "Pumping your fingers in and out of your pussy, you frantically rub your thumb over your clit."
            "Focused on your own pleasure, you barely notice when they switch places again."
            "All you know is there's a cock in your hand and a cock in your mouth, and you want to get off {i}so bad{/i}."
            "Your clit throbs with near-painful pleasure and your pussy clenches spasmically around your fingers."
            "It's almost enough... Almost... Almost..."
            "Your orgasm breaks over you like a dam releasing, flooding you with wave after wave of pleasure."
            "You shudder between them, eyes rolling back as one of them fucks your face."
            "Hot, salty cum floods your mouth and another dick replaces the first."
            "Your thumb still circles your clit, prolonging your orgasm until you feel weak and heavy."
            "Another mouthful of cum fills your mouth and throat; you swallow it eagerly."
            "When you slowly open your eyes, the world is slightly blurry."
            "Blinking back tears, you clear your vision and look down at yourself dazedly."
            "Your breasts are lined with trails of saliva and cum trickling down from your chin."
            "The guys both smile down at you, tucking their cocks back into their pants."
            "Drew" "Did you like that, slut?"
            if defymatt:
                "Shame rises in you once again, but you slowly nod your head."
            elif True:
                "You nod, still dazed from the force of your orgasm."
        "Ask Matt to fuck you." if True:
            if defymatt:
                "In the heat of the moment, you forget everything but your need to cum."
            "As Drew pulls his cock from your lips, you manage to gasp Matt's name."
            m "That eager for more of my dick?"
            if club == "track":
                pcname "Yeah... I want you to fuck me with it."
            elif club == "cheer":
                pcname "Yes. In my pussy please, Matt."
            elif club == "yearbook":
                pcname "P-please, I want you to... fuck me..."
            "Matt laughs."
            m "See what I mean? She's begging for it."
            m "Alright, whore. Stand up."
            "You slowly rise as Matt circles behind you."
            "As soon as you get to your feet, Matt grabs your hips and spreads your legs apart."
            m "Don't just stand there. Drew still needs his cock sucked."
            "Reaching out, you take Drew's cock in your hand and lean forward to wrap your lips around it."
            "Before you have the chance, Matt presses his cock against your opening and thrusts inside, filling you suddenly."
            "You gasp in surprise, aroused enough that the intrusion brings a spasm of pleasure."
            "{i}This{/i} is what your body was craving."
            "Drew takes advantage of your open mouth, sliding his cock between your lips and fucking your face."
            "As both of them fuck you, one in your pussy and one in your mouth, you lose yourself in the sensations."
            if corruption > 25:
                "Drew's cock sheathes itself in your throat, and you instinctively regulate your breathing between his thrusts."
            elif True:
                "With each thrust, Drew's cock presses against the back of your throat."
                "To your surprise, you instinctively relax, letting him slide past your gag reflex for the first time."
            "Fingers dig into your hips as Matt pounds himself into you, sending wave after wave of pleasure through your body."
            "The wet, sticky sounds of their cocks pumping in and out of your holes fill the room, mixing with your muffled moans."
            "Suddenly Drew thrusts himself down your throat, shuddering against your face as you struggle to swallow his load."
            "Satisfied, he steps back, his cock falling from your lips. You gasp for breath while Matt slams into your pussy again and again."
            pcname "Ah... Ah... Ahh...."
            "Your knees go weak and you struggle to stay on your feet, your cunt clamping tight around him as you reach your own climax."
            pcname "Ahh~!"
            m "Fuck!"
            "He thrusts into your tightening hole a few more times before emptying himself inside of you."
            "As he pulls away, your pussy clenches again, gushing cum. As you shakily stand, you feel it trailing down the back of your thigh."
            "The guys both smile down at you, tucking their cocks back into their pants."
            "Drew" "Did you like that, slut?"
            if defymatt:
                "Shame rises in you once again, but you slowly nod your head."
            elif True:
                "You nod, still dazed from the force of your orgasm."
    "Satisfied, he turns to Matt."
    "Drew" "Okay, I can't believe it, but you were right."
    "Matt smirks and gestures in your direction."
    m "As you can see, I don't need to lie."
    "Drew" "Fuck... I still can't believe this really happened."
    "Matt shrugs."
    m "I guess I'm just used to it. I can text her anytime, anywhere."
    "Drew shakes his head in disbelief."
    "Drew" "You're one lucky fucker."
    if corruption > 40:
        m "Yeah, she's pretty good."
    elif corruption > 25:
        m "She's not too bad. Still working on her performance."
    elif True:
        m "I guess. She's got a lot to learn though."
    "Laughing, Drew runs his eyes over your body one last time."
    "Drew" "Think I could borrow her sometime?"
    if defymatt:
        "Your heart drops. It's bad enough that Matt made you do this; would he really just lend you out to someone else?"
    elif True:
        "Your heart skips a beat. Would Matt really just lend you out like that? Without asking you?"
        "For some reason, the idea doesn't bother you nearly as much as you thought it would."
    "Matt pauses, as if in thought."
    m "I'll think about it."
    "With a final leer, Drew tears his eyes off of you."
    "Drew" "Guess I should get back to class. Let me know when you make up your mind."
    m "Clean yourself up, slut. Or do you enjoy our cum drying on your body? Are you saving it for later?"
    "He laughs as he follows Drew out of the closet, leaving you naked and alone."
    "Grabbing a rag off the shelf, you hastily wipe the cum from your body and pull on your uniform."
    "As you walk back to class, still lightheaded from your orgasm, you wonder how you'll look at Drew in class tomorrow."

    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
