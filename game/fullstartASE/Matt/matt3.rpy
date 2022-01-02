label matt_scene3:
    "While sitting in class, you feel your phone vibrate."
    call screen TextingScene("Matt", [TextMessage("Come back to Harvey's room after school")])
    if defymatt:
        show chelsea sad with dissolve
        "Your stomach drops; what is he going to do this time?"
    elif True:
        show chelsea embarrassed with dissolve
        "Your pulse races; what is he going to do this time?"
    show chelsea blank
    "You spend the rest of the day in a bit of a daze, wondering what awaits you when the final bell rings."
    if defymatt:
        "What awful things will he make you do now..."
    elif True:
        "What does he have planned for you next..."
    show chelsea shocked
    "{i}{b}DING{/b}{/i}"
    "Startled from your wondering, you nearly jump from your seat."
    show chelsea blank
    "You walk to your locker, full of nervous energy, and put your books away."
    if defymatt:
        "Despite his threats, you {i}do{/i} still have a choice..."
    elif True:
        "Biting your lip, you make your decision."
    jump matt_scene3_gochoice

label matt_scene3_gochoice:
    menu matt_scene3_go:
        "Go to Mr. Harvey's room." if True:
            hide chelsea with moveoutright
            show bg black with dissolve
            jump matt_scene3_harveyroom
        "Leave." if True:
            if defymatt:
                show chelsea sad
                "You feel sick when you think of what the consequences might be, but you can't do this anymore."
                "Heart pounding against your ribs, you close your locker and leave the school."
                $ mattblackmail = 2
                jump events_end_period
            elif True:
                "The last time was too much for you, and today you've had plenty of time to consider what you've been doing."
                "Heart pounding against your ribs, you close your locker and leave the school."
                "As you step outside, however, your phone vibrates again."
                call screen TextingScene("Matt",
                [
                    TextMessage("You have 5 mins to get to Harvey's room"),
                    TextMessage("Or I'll put those pics all over the school")
                ])
                $ defymatt = True
                "With shaking hands, you put your phone back into your pocket."
                if club == "track":
                    pcname "That bastard!"
                elif club == "cheer":
                    pcname "Now what do I do..."
                elif club == "yearbook":
                    pcname "How could I let this happen...?"
                jump matt_scene3_gochoice

label matt_scene3_harveyroom:
    $ mattchain += 1
    "You walk down the hall to Mr. Harvey's room, stopping when you reach his door."
    "The lights are off; he must have left already. You're not even sure if the door will be unlocked."
    "Grasping the handle, you're surprised when it turns easily."
    show chelsea at right with moveinright
    "As you step inside, the lights flick on and you see Matt sitting atop a desk in the back of the room."
    show bg ClassroomE with dissolve
    show Matt Blank at left with moveinleft
    m "About time."
    "He leans back on the desk, bracing himself on one arm."
    m "Lock the door and get over here."
    "Reaching back, you flip the lock into place."
    if defymatt and mattblackmail == 0:
        if club == "track":
            show chelsea confused
            pcname "Are you really going to blackmail me?"
        elif club == "cheer":
            show chelsea blank
            pcname "Would you really share those pictures?"
        elif club == "yearbook":
            show chelsea sad
            pcname "A-are you blackmailing me...?"
        show Matt Happy at left
        "He laughs."
        show Matt Smirk at left
        m "I suggest you do what I tell you, unless you want to find out."
        $ mattblackmail = 1
    show Matt Blank at left
    show chelsea blank
    "You cross the room slowly; it feels almost as if your body is moving on its own."
    show Matt Pleased at left
    m "Alright, slut. Tell me what a dirty little whore you are."
    menu matt_scene3_dirtytalk:
        "Tell him." if True:
            if defymatt:
                "You force yourself to comply."
            if club == "track":
                pcname "I'm a dirty little whore, Matt."
            elif club == "cheer":
                pcname "I'm {i}such{/i} a dirty little whore..."
            elif club == "yearbook":
                pcname "I-- I'm a dirty... little... whore..."
            show Matt Smirk at left
            $ corruption += 2
            m "That's a good girl..."
            if defymatt:
                "You look away, disgusted."
            elif True:
                show chelsea embarrassed
                "Despite yourself, you can't help but smile at his praise."
        "Refuse." if True:
            if club == "track":
                show chelsea shocked
                pcname "What!?"
            elif club == "cheer":
                show chelsea angry
                pcname "I'm not saying that!"
            elif club == "yearbook":
                show chelsea sad
                pcname "I can't!"
            show Matt Question at left
            "He shakes his head, frowning."
            show chelsea blank
            m "I don't feel like arguing with you today..."
            if defymatt:
                show Matt Angry at left
                m "You're going to do {i}whatever{/i} I tell you or you know what I'll do."
                m "I don't want any more backtalk today, got it?"
                show chelsea sad
                "Swallowing your pride, you nod."
            elif True:
                "He pulls out his phone and lays it on the desk."
                show Matt Blank at left
                "Glancing down, you're shocked to see one of the pictures he took of you masturbating."
                m "You're going to do what I tell you to, or that will be posted all over the school."
                m "Got it?"
                "Shaken, you nod wordlessly."
                $ defymatt = True
                $ mattblackmail = 1
            show Matt Pleased at left
            m "Now tell me what a {i}dirty{/i} little {i}whore{/i} you are."
            show chelsea blank
            "Sucking in a shaky breath, you do as he says:"
            if club == "track":
                show chelsea sad
                pcname "I'm a dirty little whore."
            elif club == "cheer":
                show chelsea sad
                pcname "I'm a dirty little whore, Matt..."
            elif club == "yearbook":
                show chelsea sad
                pcname "I'm a... dirty... little... whore..."
    show Matt Smirk at left
    m "That's right..."
    show chelsea blank
    m "Now take off your clothes and get on your knees, slut."
    "Your fingers tremble as you begin stripping."
    "You can feel his eyes on you, roving over every inch of skin you bare."
    hide chelsea with fade
    $ clothes = 'underwear'
    show chelsea embarrassed at right with moveinright
    "The cool air slides over your body as you remove your skirt and blouse, tossing them aside."
    "As you unhook your bra and slide it off your shoulders, you shiver beneath his gaze."
    "He licks his lips, watching you peel your panties off and kick them away."
    hide chelsea with fade
    $ clothes = 'naked'
    show chelsea embarrassed at right with moveinright
    if defymatt:
        "Sinking to your knees, you glare up at him."
    elif True:
        "Sinking to your knees, you peer up at him."
    scene bg black with dissolve
    show bg MBS1 with dissolve
    m "You know better; get into position."
    if defymatt:
        "Begrudgingly, you put your hands behind your head and spread your knees wide."
    elif True:
        "You put your hands behind your head and spread your knees wide, trying to remember the exact position."
    m "Chin up; eyes down."
    "You comply. For some reason, lifting your chin makes you even more aware of your nakedness."
    if defymatt:
        "And worse, despite the situation, you feel a rush of warmth between your legs."
    elif True:
        "Perhaps because of that, you feel a rush of warmth between your legs."
    "He moves toward you."
    m "I've been thinking about this all day."
    m "You're going to sit there, without moving, while I do {i}whatever{/i} I want."
    show bg MBS3 with dissolve
    "To emphasize his point, he leans down and pinches your right nipple."
    if defymatt:
        "You gasp, but force yourself to stay still."
    elif True:
        "You gasp, doing your best to stay still."
    m "Good girl."
    "He emphasize his words by twisting your nipple gently between his fingers."
    if defymatt:
        "You're disgusted by yourself when a surge of heat floods your pussy."
    elif True:
        "A surge of heat floods your pussy, drawing a soft moan from your lips."
    show bg MBS4 with dissolve
    "Lifting his other hand, he presses two fingers to your lips."
    m "You don't deserve to suck my cock yet, but you can practice on these."
    show bg MBS5 with dissolve
    if defymatt:
        "Swallowing back your revulsion, you part your lips and allow him to thrust his fingers into your mouth."
    elif True:
        "Parting your lips, you bring your tongue up to meet his fingers, swallowing them hungrily."
    "He continues twisting your nipple in his fingers, occasionally pinching or pulling while you suck his fingers."
    if defymatt:
        "Unimpressed by your efforts, he thrusts them in and out of your mouth harshly."
    elif True:
        "Imagining it's a cock in your mouth, you bob your head forward and back eagerly."
    show bg MBS6 with dissolve
    "His hand moves to your other nipple, offering it the same treatment."
    "In response, you feel another rush of heat and a warm stickiness on the insides of your thighs."
    if defymatt:
        "Your cheeks burn with shame as you realize how much this is turning you on."
    "Suddenly he withdraws his fingers from your mouth and releases your nipple."
    m "Get up."
    show bg MBS7 with dissolve
    "You stand quickly despite the numb tingling in your legs."
    m "Remember, you don't move."
    show bg MBS8 with dissolve
    "Almost immediately, he drops his hand to cup the curve of your pussy."
    if club == "track":
        pcname "Matt!"
    elif club == "cheer":
        pcname "Matt..."
    elif club == "yearbook":
        pcname "M-Matt!"
    m "Tell me what you want."
    if defymatt:
        "You know what he wants to hear, so you force the words out."
    if club == "track":
        pcname "Touch me!"
    elif club == "cheer":
        pcname "I want you to touch me more."
    elif club == "yearbook":
        pcname "Y-You..."
    show bg MBS9 with dissolve
    "He slides his middle finger between your lower lips, allowing it to explore the folds of your cunt."
    m "Look how wet you are..."
    if defymatt:
        "A harsh moan, a mixture of lust and disgust, erupts from your throat."
    elif True:
        "A breathy moan escapes your lips."
    "His finger slips inside of you, teasing your throbbing opening."
    m "I bet you can't wait until I'm inside of you, slut."
    if defymatt:
        "You bite your lip, forcing yourself to stay still as he slides his finger deeper inside of you."
    elif True:
        "It's all you can do to stay still, fighting your body's urges as he slides his finger deeper."
    m "You want more, don't you?"
    "He grabs your jaw with his other hand, demanding a response."
    if defymatt:
        if club == "track":
            "Teeth grinding together, you practically spit the words at him."
        elif club == "cheer":
            "Shamed and aroused, you barely trust yourself to speak."
        elif club == "yearbook":
            "Cheeks hot with shame, you try to shake your head, but his hand holds you firmly."
    if club == "track":
        pcname "Yes!"
    elif club == "cheer":
        pcname "Y-yes... Oh..."
    elif club == "yearbook":
        pcname "P-please..."
    "His laugh is soft and low as he presses a second finger inside of you."
    "Fingering you slowly, he studies your face, watching your reactions."
    if defymatt:
        "You try to steel yourself - try to force yourself to be still and unresponsive."
        "Despite your best efforts, however, you can't help but react to his assault."
        "Breathing in short, airy gasps, your body clenching around his fingers, drawing them further inside of you..."
    elif True:
        "You whimper when he withdraws his fingers, your muscles clenching around them, as if to draw them back inside."
        "And then, each time he presses them into you again, a soft moan escapes your lips."
    "Suddenly his fingers slip from your pussy, leaving you swaying and breathless."
    m "Now let's see if you can stay still..."
    "Before the words have a chance to sink in, he slides his fingers - wet with your juices - across your clit."
    "The sensation is shockingly intense; you cry out wordlessly as you fight to stay still."
    if defymatt:
        m "Aren't you glad I made you come here?"
    elif True:
        m "You like that, slut?"
    "It takes all of your willpower to stay immobile as he rubs his fingers back and forth."
    "Wave after wave of near-painful pleasure shoots out from your swollen clit."
    "As your knees weaken, you feel the pleasure begin to overtake you."
    if defymatt:
        "Tears fill your eyes as your body betrays you."
    "You cry out as you cum; your body spasms and jerks against his fingers, and a hot flood of juices trickle down your thighs."
    "Swaying on unsteady legs, you fight to hold yourself upright as your orgasm slowly recedes."
    m "Not bad. I think you might finally deserve this..."
    "As he speaks, he unbuttons his pants and slowly pulls the zipper down."
    "His hard cock presses against the fabric of his boxers, straining toward you."
    if defymatt:
        "You want to look away, but you know it won't make a difference. If anything, it will only irritate him."
    show bg MBS10 with dissolve
    m "On your knees, slut."
    if defymatt:
        "You sink to your knees as if your body is caving in on itself; there's no fight left in you."
    elif True:
        "You obey him quickly, your tongue darting eagerly across your lips."
    "Already, you can smell the muskiness of the precum dripping from his cock."
    if defymatt:
        "Your eyes widen as the reality of your situation strikes you once again."
    elif True:
        if club == "track":
            "Your eyes widen as you nod, eager for the challenge he's presenting you."
        elif club == "cheer":
            "Your eyes widen as you nod, a small smile spreading across your lips."
        elif club == "yearbook":
            "Your eyes widen as you nod. You're both thrilled and frightened by this turn of events."
    m "Open up!"
    show bg MBS11 with dissolve
    "He presses his cock to your lips, barely waiting for your lips to part before he presses it inside."
    show bg MBS12 with dissolve
    if defymatt:
        "It's almost like an out of body experience, letting him use your mouth while you do nothing to stop him."
    elif True:
        "It's almost like an out of body experience, letting him use your mouth while you do nothing to encourage him."
    m "You like that, slut?"
    "With a mouth full of cock, it's impossible to do more than moan in response."
    "He puts his hand on your forehead, tilting your head back just a little."
    "Then, holding you in place, he press himself even further into your throat."
    if corruption > 25:
        "You take him in completely, letting his cock slide past your gag reflex."
        m "Holy fuck..."
        "His balls slap your chin as he thrusts in and out of your throat."
        "Between thrusts, you suck in a quick breath through your nose before your air is cut off again."
    elif True:
        "Your throat convulses as he hits your gag reflex, leaving you coughing and choking around him."
        m "Hold still!"
        "He presses his cock into your mouth again, careful not to press too deep."
    "Holding your head in one hand, he continues fucking your face."
    if defymatt:
        "Blinking back tears, all you can do is wait for him to finish with you."
    elif True:
        "Your eyes drift half-shut as you lose yourself to the sensations."
    "Salty pre-cum coats your tongue; you swallow it between thrusts."
    "As his climax nears, his movements come harder and faster until suddenly he pulls his cock from your lips."
    m "Keep it open!"
    menu matt3_cumonyou:
        "Open your mouth." if True:
            $ corruption += 5
            show bg MBS14 with dissolve
            "Pumping his cock with quick, jerky movements, he empties himself over your waiting tongue."
            "The hot, salty liquid fills your mouth, dribbling from your lips and over your chin."
            show bg MBS15 with dissolve
            "You look up at him, waiting for permission to swallow his load."
            m "Do you like my cum?"
            if defymatt:
                "Hoping that he's almost done with you, you nod your head."
            elif True:
                if club == "track":
                    "You nod, since that's what he wants to hear."
                elif club == "cheer":
                    "You nod, moving it around with your tongue."
                elif club == "yearbook":
                    "You nod slowly, embarrassed."
            m "Swallow it and get dressed."
            show bg MBS16
            "Tucking his cock back inside his pants, he watches you swallow his load."
            scene bg black with dissolve
        "Close your mouth." if True:
            show bg MBS17 with dissolve
            "You clamp your lips shut, forcing him to empty himself across your face instead."
            "Cum splashes over your cheeks, catching in your eye lashes and running down your chin."
            "It's more of a mess, but you feel a little more in control again."
            m "Bitch..."
            "Tucking his cock back inside his pants, he glares down at you."
            scene bg black with dissolve
    show bg ClassroomE with dissolve
    show Matt Pleased at left with moveinleft
    show chelsea sad at right with moveinright
    m "I'll text you when I want to see you again."
    if defymatt:
        show Matt Angry at left with moveinleft
        m "And you'd {i}better{/i} do what I say."
    "You nod as you retrieve your clothes."
    "As you pull them on, you hear the door click shut behind Matt."
    jump events_end_period

label matt_scene4:
    show chelsea at right with moveinright
    if job == "bakery":
        "You fill the hours at work the usual way. Helping prepare food, dealing with customers, and making sure the store is clean."
        "You’re at the front counter when you idly notice a middle-aged Asian woman with short dark hair approach. Her eyes snag on a newspaper left on the side of the countertop."
    if job == "cafe":
        "Today, you’re assigned to work outside the cafe, upfront, handing out fliers. In the cutesy maid uniform, you’re more the advertisement than they are."
        "A middle-aged Asian woman with short dark hair walks past, eyes idly scanning the storefronts. You start toward her, extending your hand to offer her a flier."
        "But, as you do, her glance catches on a newspaper left on one of the outdoor tables."
    "The lead story - an exposé on corruption in a local business - contains a picture of several well-dressed men in suits being led away in handcuffs."
    "You hadn't heard about it, but for some reason the woman seems shaken by it. She reaches towards the paper with one, trembling hand."
    show chelsea confused
    pcname "Ma’am, are you alright?"
    "Woman" "..."
    show chelsea shocked
    "You rush over as her movements become spastic and twitchy, as though something hostile had taken over her nervous system. This isn’t a normal response."
    pcname "Ma’am? Ma’am!?"
    "Thinking quickly, you grab a chair and help her to sit down. A challenging task, with her entire body shaking the way it is."
    "You’re left blinking, trying to think of what to do. After a short delay, you rush to get her a glass of water."
    "Woman" "Th-Thank y-you."
    show chelsea blank
    "By the time you return, the woman has steadied slightly. Her hand still spasms violently as she tries to grab the glass from you. Splashes of water hit the ground as she makes a shaky attempt to drink."
    "You wait for her to finish sipping at the water, trying not to stare. As fast as the episode began, it’s already receding."
    if club == "track":
        show chelsea sad
        pcname "What happened?"
    elif club == "cheer":
        show chelsea shocked
        pcname "Holy cow, what was that?"
    elif club == "yearbook":
        show chelsea sad
        pcname "A-are you okay?"
    "The woman gives a weak smile."
    "Woman" "Oh, it was just a dizzy spell. I get them from time to time."
    "Woman" "What's your name?"
    show chelsea happy
    pcname "[pcname]."
    "Woman" "Nice to meet you. I'm Judy Miyagawa. You can call me Judy if you like."
    show chelsea blank
    "The woman offers you her still trembling hand, making a feeble effort at a handshake."
    show chelsea happy
    if club == "track":
        pcname "It’s a pleasure to meet you, Judy"
    elif club == "cheer":
        pcname "That’s such a sweet name! It’s nice to meet you too, Judy."
    elif club == "yearbook":
        pcname "Just Ms. Miyagawa is okay, I guess. I don’t want to be forward."
    "With your help, Ms. Miyagawa makes it back up to her feet. She grows firmer and stronger with every passing second."
    "Ms. Miyagawa" "My word, it really would be terrible of me not to give you a nice {i}proper{/i} thank you."
    "Ms. Miyagawa" "Do you leave work soon?"
    show chelsea confused
    "You tilt an eyebrow."
    pcname "Yes...?"
    "Ms. Miyagawa" "I was just going to go to this {i}lovely{/i} new dessert restaurant in town. I was going to meet my son there in an hour."
    show chelsea shocked
    "Ms. Miyagawa" "You should come with. I’ll get you anything you want, my treat!"
    show chelsea laugh
    "You wave your hands and give a nervous laugh."
    if club == "track":
        pcname "I couldn't. I’d be imposing on you and your son."
    elif club == "cheer":
        pcname "Oh, you’ll make me blush. That would be imposing."
    elif club == "yearbook":
        pcname "Are you sure that’s okay...?"
    "Ms. Miyagawa" "Nonsense. Nonsense. My son knows the value of generosity and reciprocity. I raised him, after all. He won’t mind one bit."
    "Ms. Miyagawa" "You're not imposing."
    show chelsea blank
    "It takes some convincing, but eventually the eager woman persuades you to agree to come along with her after work."
    "You did help her after all, so is it really so wrong to accept a gift from her? It’s not like you did it with reward in mind."
    show bg black with dissolve
    hide chelsea with dissolve
    $ clothes, hair = casualwear
    "An hour later, you find Ms. Miyagawa standing in front of the dessert restaurant. She’s by herself."
    show bg CityE with dissolve
    show chelsea at right with moveinright
    "Ms. Miyagawa" "You made it!"
    "Ms. Miyagawa" "Oh, don’t worry about my son. He should be here any moment. He can be a bit free-spirited, so he isn't always on time."
    show chelsea shocked
    "You only have to wait a few minutes for her son to appear. When he arrives, though, you’re too stunned to greet him."
    show Matt Casual Happy at left with moveinleft
    "Matt" "Hey, Mom. I told you I wasn’t going to be here until after I-"
    show Matt Casual Question at left
    "Matt" "[pcname]?"
    show chelsea confused
    pcname "..."
    "All three of you look at each other in confusion. It takes you a moment to even fully process that he didn’t walk here by accident."
    "Ms. Miyagawa" "You two already know each other? Oh, is she a classmate?"
    "After a few seconds of gawking, your voice comes back to you."
    show chelsea embarrassed
    pcname "Y-yeah."
    show Matt Casual Angry at left
    "Matt’s face twists in reflexive anger. He runs a finger from you to his mother."
    "Matt" "[pcname]. How did you-? Why are you-?"
    "The longer he has time to process the information, the more his expression settles."
    show Matt Casual Blank at left
    "Matt" "Mom? Why are you two with each other?"
    show chelsea blank
    "Ms. Miyagawa" "This must be confusing, huh?"
    "You are forced to stand around awkwardly as she explains the situation to him."
    "He shoots you a distrustful glance when he hears that you even got her water. But, otherwise, the explanation seems to calm him."
    "Matt" "Hmph. I guess it would be wrong of me to complain, since she helped you."
    "He turns briskly and walks into the building."
    "Matt" "Come on. I’m hungry."
    "You walk in behind them, blinking every so often. The entire situation is almost too surreal. You’d almost believe it was a trap, if it weren’t for Matt’s obvious annoyance."
    "An annoyance that the woman that his mother seems blissfully unaware of."
    show bg DatePlace with dissolve
    show chelsea confused
    "You rack your brain to make sense of the situation. Something has to be wrong here."
    show chelsea shocked
    "As you take a seat across from them at the table, something occurs to you."
    show chelsea confused
    if club == "track":
        pcname "Wait, but your last name is Richards, isn't it?"
    elif club == "cheer":
        pcname "Isn’t your last name Richards or something?"
    elif club == "yearbook":
        pcname "I-I thought your last name was Richards, Matt...?"
    show Matt Casual Angry at left
    "Matt shoots you an annoyed stink eye, but his mother eagerly jumps in."
    "Ms. Miyagawa" "Oh, haha. That's actually my husband's last name. He’s not around anymore. I went back to my maiden name, but Matt didn’t want to change his."
    show Matt Casual Blank at left
    "Matt" "Why would I? It's always been my name."
    "Ms. Miyagawa" "Wait, but didn't you say that-"
    show chelsea blank
    "The two of them go back and forth on it. It’s strange seeing Matt so subdued. It’s the first time you’ve met an authority figure whom he doesn’t treat with utter contempt."
    "You look a little closer at Matt. The fact that Ms. Miyagawa is seemingly Japanese in ethnicity also keeps throwing you off. You’d never even considered that Matt might not be entirely white before."
    "But, the more you look at him, the more you can see hints of her features in him. These two people are clearly related."
    show chelsea confused
    "How had you never noticed this before? Was it obvious to everyone else?"
    show chelsea blank
    show Matt Casual Smirk at left
    "Eventually the topic moves back to you. When Matt glances to you, he briefly shines his normal, predatory stare."
    "But it melts fast; it’s hard to be intimidating with your mother doting in the neighboring seat."
    "Ms. Miyagawa" "Matt never mentioned you to me before. So just classmates, I assume? Not friends?"
    if defymatt:
        "Fighting back a sudden wave of nausea, you glance at Matt."
    elif True:
        show chelsea embarrassed
        "Trying not to blush, you push away thoughts of what you've been to Matt."
    show Matt Casual Pleased at left
    "Matt" "Something like that..."
    "Matt grimaces at the mere suggestion of it. It gives you a mischievous idea."
    show Matt Casual Blank at left
    if defymatt:
        show chelsea happy
        "After all, how often do you get a chance to needle Matt on an even playing field?"
    if club == "track":
        show chelsea happy
        pcname "Actually, we hang out pretty often. Matt’s always been the most friendly person in class. He even gave me a helping hand on my first day."
        pcname "I’d go so far as to call him my best friend in the entire class!"
    elif club == "cheer":
        show chelsea happy
        pcname "Matt? Oh my god, don’t say that! He doesn’t want to admit it, but Matt’s always been so helpful to me. He even gave me a hand on the first day of class!"
        "You give a little giggle."
        pcname "He’s a real sweetie. Definitely my favorite boy in the class."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Well... I don’t know about that. Matt, aren’t you being a little humble? You’ve been so helpful and everything... You even gave me a helping hand on the first day of class."
        "You give a sly little blush."
        pcname "Matt... You’re my best friend in class..."
    "Matt purses his lips at you. Perhaps teasing him in front of his mother isn’t the wisest idea. But, it’s too fun to totally resist."
    "Matt’s mother happily claps her hands together, wiggling excitedly in her seat."
    show chelsea blank
    "Ms. Miyagawa" "Matt! Why didn’t you say so! Oh, you’re so humble. And not wanting your dear mother to know about it too!"
    "Matt" "Mom..."
    "Ms. Miyagawa" "I can’t say I’m surprised. Matt has always been a charmer with the ladies. Oh, I remember he brought that old girlfriend of his over not too long ago. What was her name, again?"
    "Matt sighs and almost cups his face in his hands. You squint closer, trying to see if he’s blushing a little."
    "Matt" "Serena."
    "Ms. Miyagawa" "Oh, that’s the one. Cute, but a little shy."
    "The woman gives a little giggle."
    "Ms. Miyagawa" "I thought she was a bit of a dormouse, to tell the truth."
    "You lean back in your seat slightly. Serena...?"
    if defymatt:
        show chelsea confused
        "You don’t know any girl named Serena in class. The idea of Matt having a proper girlfriend is a fascinating change of pace though..."
        "How could she stand him?"
    elif True:
        show chelsea confused
        "You don't know any girl named Serena in class. The idea of Matt having a proper girlfriend though... You don't like the way that makes you feel."
        "What made her so special?"
    pcname "Serena? Have I met her?"
    show Matt Casual Angry at left
    "Matt grumbles."
    show Matt Casual Blank at left
    "Matt" "She left town right before you transferred. We weren’t together anymore. I guess we drifted apart."
    "Matt’s posture closes off. If he has had any tolerance for this event up until now, there’s definitely zero for this topic."
    "Matt" "I really wouldn’t waste my time asking about it."
    "Matt" "It’s not important."
    show chelsea shocked
    pcname "Are you-"
    show Matt Casual Angry at left
    "Matt" "It’s {i}not important{/i}."
    if defymatt:
        show chelsea blank
        "For a moment, you forgot the danger inherent in the situation. Every moment you spent here put you at risk of doing something new to anger him."
    elif True:
        show chelsea blank
        "Matt’s meaning was all too clear. The novelty of the situation blinded you to his anger - and you know who will pay the price later."
    show chelsea sad
    pcname "I see..."
    "You awkwardly rise from your seat."
    show chelsea happy
    show Matt Casual Blank at left
    pcname "You know, it’s been fun but I guess it’s time to head back."
    "Ms. Miyagawa" "Oh come now. Your food hasn’t even arrived yet! At least wait for that! Please!"
    show chelsea blank
    "You look at Matt."
    "Matt" "Eh, I guess your food hasn’t arrived."
    "Cautiously, you return to your seat. Ms. Miyagawa beams."
    if club == "track":
        pcname "Fine. I’ll stay a little longer."
    elif club == "cheer":
        pcname "I guess I'll stay a little bit longer."
    elif club == "yearbook":
        pcname "I can stay a little longer, I suppose..."
    show powerout with dissolve
    "You chat idly until food arrives. At this point, you’re watching for signs of anger from Matt. With his oblivious mother present, it could be a glance that tips you off to his mood or perhaps the tiniest gesture of his hand."
    "You try to avoid any sensitive or dangerous topics, but you don’t always succeed..."
    hide powerout with dissolve
    "Ms. Miyagawa" "You don’t live far away, do you? Oh, I hope that’s not why you were asking to go."
    pcname "No, no, I live close by."
    show Matt Casual Smirk at left
    "Suddenly, Matt perks up."
    "Matt" "Really?"
    "Matt" "Where?"
    "Ms. Miyagawa" "Matt! Don’t ask her that."
    show chelsea shocked
    if defymatt:
        "Your face pales. You {i}can't{/i} let him know where you live..."
    elif True:
        "Your face pales slightly. If Matt knew where you lived..."
    show Matt Casual Happy at left
    "Matt" "Why not? We're {i}best{/i} friends after all. Isn't that what you said, [pcname]?"
    show chelsea sad
    pcname "I..."
    if defymatt:
        "Too late, you realize what your needling would cost."
    elif True:
        "As usual, Matt has the upper hand."
    show chelsea happy
    pcname "Yeah, right. The best of friends."
    show chelsea blank
    pcname "My house is... just down that way."
    show Matt Casual Pleased at left
    m "C'mon. I can't believe you won't tell your best friend where you live."
    show chelsea embarrassed
    pcname "I..."
    show chelsea sad
    if defymatt:
        "You've already pissed him off today and you're sure that he could find out if he wanted to."
        "Drawing this out will probably just make things harder for you later, right?"
    elif True:
        "He was so angry when you teased him earlier. Maybe if you just tell him he'll be happier with you?"
    show Matt Casual Smirk at left
    m "Yeah?"
    "Ms. Miyagawa shifts uncomfortably. For a moment, you wonder if she knows what's happening here."
    show chelsea laugh
    pcname "I can't believe I've never told you before!"
    show chelsea blank
    "As you tell Matt how to get to your apartment, Ms. Miyagawa relaxes again."
    "Ms. Miyagawa" "I almost forgot, sweetie. I picked up some of your favorite cakes at the store today..."
    "Time flies as they talk, and soon you’re left staring at your finished plate. Ms. Miyagawa was right; this place was pretty good."
    "Ms. Miyagawa" "It is getting rather late. Would your parents get mad that you haven’t come home after work?"
    "Tell her what happened to your parents?"
    menu parentsdiedmiyagawa:
        "Yes" if True:
            "It's a sore topic, but you feel like you can tell her."
            pass
        "No" if True:
            "It's just too much of a sore topic to mention that they aren't around anymore so you just mention that you live alone."
            jump miyano
    show chelsea sad
    show Matt Casual Blank at left
    if club == "track":
        pcname "My parents died. Car accident."
    elif club == "cheer":
        pcname "My parents, they... They're gone. There was a car accident last year..."
    elif club == "yearbook":
        pcname "My parents... aren’t... with us anymore."
    "Ms. Miyagawa" "Oh my... That's terrible..."
    "Ms.Miyagawa is awash with sympathy, but Matt only raises an eyebrow."
    "Matt" "No parents. Is that so?"
    "Ms. Miyagawa" "Matt. Show some compassion."
    "Matt" "Sorry, Mom. It’s just horrible."
    label miyano:
        show Matt Casual Blank at left
    "You turn your head away. Even amongst more sympathetic conversation partners, this is normally a pretty challenging topic to broach."
    show chelsea blank
    pcname "I do suppose that I should be getting back anyway though. Even if there’s no one to get mad, I do still need to be up early in the morning."
    "Ms. Miyagawa gives you a soft smile."
    "Ms. Miyagawa" "Makes sense. Makes sense. Thank you, young lady. You were very helpful today. I’m sure Matt is going to be extra appreciative in class after this, right?"
    show Matt Casual Pleased at left
    "Matt" "Yeah, definitely."
    show chelsea confused
    "Somehow, you’re left doubting that."
    show chelsea happy
    "You say some polite goodbyes and make your way back home. Matt even waves as you leave."
    show chelsea blank
    "Of course, the moment you’re out of sight from them, you’re already going over the strange events of the past hour in your head."
    show chelsea confused
    "Certainly, Matt had been aggravated at parts. Especially at the beginning. But had he mellowed out some near the end?"
    show chelsea blank
    if defymatt:
        show chelsea shocked
        "With a start, you realize something that you’d missed."
        pcname "I’m an idiot!"
        "You met Matt’s {i}mother{/i}. If you'd wanted, you could have told her everything about how Matt was using pictures to blackmail you."
        "Maybe she could have forced his hand to free you, or added repercussions for him if he tried to use them against you."
        show chelsea sad
        "But, the light drains back from your eyes as you consider the idea more. As juicy a thought as it was, you're not sure if you could've done it."
        "After all, Ms. Miyagawa was such a nice woman. How could you deliberately ruin her positive mental image of her own son?"
        "But, more importantly, what would have happened to you if you failed to change her mind about him...?"
    jump events_end_period

label matt_scene5:
    $ clothes, hair = casualwear
    show bg black with fade
    show bg HomeE with dissolve
    show chelsea happy at right with moveinright
    "You return home for the evening and prepare to stretch out on the couch. It has been a long day, and you are looking forward to some nice time to yourself."
    show chelsea confused
    "Which is part of why you’re confused - and slightly annoyed - by the sound of a firm, demanding knock on the door."
    show chelsea angry
    pcname "One second!"
    show Matt Casual Smirk with dissolve
    show chelsea shocked
    "Matt is on the other side of the door with a skeezy grin on his face. While you’re still sputtering, he walks in uninvited and looks around the place."
    show chelsea blank
    "Matt" "Cozy. Spacious too."
    show Matt Casual Blank at left with move
    "Matt" "Does anyone else live here?"
    if defymatt:
        "You warily close the door behind you. Whatever he’s planning, it can’t be good."
        show chelsea confused
    elif True:
        show chelsea embarrassed
        "You slowly close the door behind you. Your heart beats fast. What plans does he have for you?"
    pcname "Did you want to talk about what happened yesterday with your mo-"
    show Matt Casual Angry at left
    "Matt" "Stop talking."
    show chelsea blank
    pcname "..."
    "His face turns dark in an instant; he strides in your direction. In such close quarters, his commanding height and larger frame are acutely felt."
    "Matt" "My goddamn mother is none of your concern. She was just feeling a bit woozy and you made a whole song and dance about it."
    show Matt Casual Smirk at left
    show chelsea confused
    "Matt" "Now stop running that mouth and go sit on the couch. I brought a gift for you."
    "You’re about to defend your actions from earlier in the week, but the last part stops you. Gift? What does he mean by a gift?"
    menu complainobey0:
        "Complain" if True:
            if defymatt:
                if club == "track":
                    show chelsea angry
                    pcname "Hey, you can't just show up to my house unannounced!"
                elif club == "cheer":
                    pcname "Matt! Come on. It’s totally creepy for you to just show up at my house unannounced. You can’t do that!"
                elif club == "yearbook":
                    show chelsea sad
                    pcname "Matt... you didn’t even tell me you were coming. I know that... I know that you have those pictures, but... I don’t like it when you show up without telling me. Please, you can’t do that..."
                show Matt Casual Blank at left
                "Matt" "Yes, I can."
                show chelsea shocked
                "Something about his tone makes your blood run cold."
                show Matt Casual Pleased at left
                "Matt" "I can do whatever I want. You need to learn a lesson, [pcname]. You’re my bitch now. I own you."
                show chelsea blank
                "As if to prove the point, he brushed a hand over your neck. There was no force to it, but you understand all the same; it would not take much effort to choke you."
                show Matt Casual Smirk at left
                "Matt" "Got that?"
                show chelsea sad
                "You take a step back, eyes wide. He’s right. He has all the power here."
                show chelsea blank
                if club == "track":
                    pcname "I just want to get some rest. I have track practice in the morning. I can’t-"
                elif club == "cheer":
                    pcname "Please, Matt! Not tonight. There’s cheer practice tomorrow. I just want to-"
                elif club == "yearbook":
                    show chelsea sad
                    pcname "Please, Matt... I’m begging you. I have yearbook in the morning too. I just want to get some-"
                show Matt Casual Angry at left
                "Matt" "Couch. Now."
                "You huff and pad over to the couch, sitting with your legs and arms crossed. You might obey, but you don’t have to be happy about it."
            elif True:
                if club == "track":
                    show chelsea confused
                    pcname "What exactly are we doing though? You never told me that you were going to come to my house."
                elif club == "cheer":
                    show chelsea happy
                    pcname "But, Matt, what do you want with me? I mean, isn’t it rude to come to a girl’s house without even giving her a text?"
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "But, why? I was so surprised when you appeared. You hadn’t, you know, texted me or anything. It was really scary."
                pcname "And you said that you had a-"
                show chelsea shocked
                "Matt presses a thumb to your lips, instantly silencing you. He pushes it past your resistance. It’s as though he were using it as a pacifier."
                show chelsea blank
                "Matt" "You really do need to learn to stop running that pretty little mouth of yours. You’re going to find out soon enough."
                "That silences the debate. Lowering your head, you make your way to the couch."
        "Obey" if True:
            $ corruption += 5
            show chelsea blank
            if club == "track":
                pcname "Yes, Sir."
            elif club == "cheer":
                pcname "Hmph. Yes, Sir."
            elif club == "yearbook":
                pcname "Yes, Sir..."
            "You pad your way over to your couch and sit down, calming your shaking hands by resting them on your knees."
    show Matt Casual Blank at left
    "Matt takes a seat on the opposite side of the couch and places a green, camouflage backpack on the ground."
    "He starts to rifle through it. You peak over, trying to see in, but he’s positioned it too far for you to have a clear view."
    if defymatt == False:
        "Everything about the situation feels awkward. The way he’s in command, in your own house, makes you feel like the one who's a guest."
        show chelsea confused
        pcname "Can I get you anything?"
        show chelsea blank
        if club == "track":
            pcname "I could bring out a Gatorade or something."
        elif club == "cheer":
            pcname "Maybe I could mix some lemonade?"
        elif club == "yearbook":
            pcname "I think I have some Cola in the fridge..."
        show Matt Casual Angry at left
        "He silences you with a stern look. Clearly, whatever he’s planning is more important to him than good hospitality."
    show Matt Casual Blank at left
    "Matt pulls a discreet brown shipping box from the bag, places it on the coffee table, and slides it in your direction."
    show Matt Casual Smirk at left
    show chelsea confused
    "Matt" "Open it up. It’s for you."
    show chelsea shocked
    "You tear the container open hesitantly. It feels like it contains some kind of small accessory. You pull it out and stare."
    "It’s a dog collar."
    show chelsea blank
    "Pink leather with rhinestone studs. Certainly not very expensive. Your hand brushes over the metal tag. All it has is the word {b}\"Bitch\"{/b} written on it in bold letters."
    "Matt smirks to himself."
    "Matt" "Today is about teaching you your place. You’re my bitch; nothing more."
    show Matt Casual Happy at left
    "Matt" "So we’re going to be playing house. And you’re not going to be playing the wife. Do you get me?"
    show Matt Casual Blank at left
    "You nod with a pale face. The details may be hazy, but the intentions couldn’t be more clear. Your fingers trail over the soft material of the leather."
    show Matt Casual Question at left
    "Matt" "Well, what are you waiting for? Are you stupid?"
    "Matt" "Put it on."
    if defymatt:
        show Matt Casual Angry at left
        show chelsea angry
        "You want to protest, but he's {i}here{/i}. In your apartment. The one place you thought you were in control."
    show chelsea blank
    show Matt Casual Blank at left
    "You raise your hair so you can take the collar and wrap it around your neck. The tag jingles. When it’s on, you fold your hands on your lap."
    show Matt Casual Smirk at left
    "Matt" "Tighter."
    if defymatt:
        "With a sigh, you give it another try."
    elif True:
        show chelsea embarrassed
        "Biting your lip, you give it another try."
    show chelsea shocked
    "This time, you pull the collar so tight that it makes you gasp slightly. The material digs in, making its presence constantly and powerfully felt."
    show chelsea confused
    pcname "L-like this?"
    show Matt Casual Pleased at left
    show chelsea blank
    "Matt" "As a start. But, we’re not done yet."
    show Matt Casual Blank at left
    "Matt" "On your feet. Off the couch."
    show chelsea embarrassed
    "A moment later, you’re standing in the middle of your own living room, with your arms dangling awkwardly to the side."
    show Matt Casual Smirk at left
    "Matt" "Good. Now strip for me. You’re wearing too much clothing for a dog."
    menu refuseobey1:
        "Obey" if True:
            $ corruption += 3
            show chelsea confused
            pcname "Strip?"
            show chelsea shocked
            "The full scale of intentions becomes increasingly clear. If you follow down this path, who knows what he’s going to do with you?"
            show chelsea embarrassed
            "But... Is it even possible for you to disobey him?"
            pcname "Yes, Sir..."
        "Refuse" if True:
            show chelsea blank
            "You cross your arms. Coming to your house announced in the middle of the night was one thing, but this...?"
            if club == "track":
                show chelsea angry
                pcname "Matt, this is way too far. Letting you in was one thing. But I don’t want to strip naked for you in my own house in the middle of the night."
            elif club == "cheer":
                show chelsea confused
                pcname "No way, Matt. Wearing a collar? Taking off my clothes? Just coming was one thing, but this is totally not okay."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Matt, please. That’s really... That’s really embarrassing. Let’s just stop here, okay...?"
            show Matt Casual Angry at left
            "Matt" "I don’t give a shit. Strip."
            show chelsea angry
            pcname "No."
            show Matt Casual Question at left
            "Matt raises an eyebrow. You can see the veins in his hand pop slightly. The temperature in the room is rising."
            show chelsea blank
            "Matt" "You get one warning. One."
            show chelsea angry
            "Matt" "Strip now."
            menu standfirmbackdown2:
                "Stand Firm" if True:
                    $ defymatt = True
                    pcname "..."
                    show chelsea blank
                    "You reach behind your neck and unclasp the dog collar. It falls to the ground at your feet. With it gone, you can breathe again."
                    show Matt Casual Angry at left
                    if club == "track":
                        pcname "This is my house, Matt. Get out. Never come back here."
                    elif club == "cheer":
                        pcname "Matt, you really need to get out of my house. If you don’t go, I’m going to tell everyone about this. This has to end now."
                    elif club == "yearbook":
                        pcname "Matt, I don’t really like any of this. I want you to leave my house now. None of this is okay."
                    "Matt rises from his seat and rushes towards you. A storm of testosterone and pride. Both his hands are balled into fists at his side."
                    show chelsea confused
                    pcname "What are you going to do now? Hit me?"
                    show chelsea blank
                    "You put your hands at your sides and stare him down."
                    "There’s a moment of frozen tension. Matt stares daggers at you, and you mirror the same expression back at him."
                    "Then, the tension in his arms lets loose. His fists open up."
                    show Matt Casual Blank at left
                    "But the darkness in his eyes doesn’t recede one bit."
                    "Matt" "No. I don’t need to hit you if I want to hurt you."
                    if defymatt:
                        "Matt storms past you, shoving you roughly to the side. You go down to your knees."
                        show Matt Casual Smirk at left
                        "Matt" "You should have obeyed me, slut."
                        show Matt Casual Blank at left
                        "Matt" "Bye."
                        hide Matt with dissolve
                        "The door slams shut behind him. You’re left alone in the room, arms crossed over your chest."
                        if mafiafavor == True:
                            show chelsea sad with dissolve
                            "While you try to put on a brave face, there is a sudden shake in your knees that renders you weak. You take a seat on the couch and try to calm the thundering beat of your heart."
                            "What can you do now? Matt has enough blackmail on you to destroy your reputation, not to mention how the school board will react..."
                            show chelsea embarrassed
                            pcname "How am I going to get out of this?"
                            show chelsea sad
                            "You pull out your phone with the intention of looking up if anyone else went through this situation. You can't be the only one, right?"
                            "But before you pull open your web browser, your contact list slides open, and Jun's phone number stares at you from the bright little screen."
                            show chelsea confused
                            pcname "Jun did offer me a favor... but can I really take him up on it for something like this?"
                            show chelsea blank
                            menu mattmafia1:
                                "Use Jun's favor to stop Matt." if True:
                                    $ mattsubmissive == False
                                    "Gripping the phone in your hand, you dial Jun's number."
                                    show chelsea sad
                                    "This is a last resort, but after all of Matt's blackmailing, you can't think of any other way to stop him."
                                    show chelsea blank
                                    "The phone rings for a few moments before picking up. There's a slight pause, and you catch your breath."
                                    "Jun" "Yeah?"
                                    if club == "track":
                                        show chelsea embarrassed
                                        pcname "Hey, Jun. Remember me?"
                                    elif club == "cheer":
                                        show chelsea laugh
                                        pcname "Hey Jun~! It's me, [pcname]."
                                    elif club == "yearbook":
                                        show chelsea sad
                                        pcname "H-Hi, Jun. It's me... [pcname]..."
                                    show chelsea embarrassed
                                    "Jun laughs on the other line, his gruffness suddenly disappearing as your voice confirms your identity."
                                    "Jun" "I was wondering when you'd call, [pcname]. What's going on? You think of something you need?"
                                    show chelsea sad
                                    pcname "That's what I'm calling about, actually. I--"
                                    show chelsea shocked
                                    "Jun" "Ah-ah, hold onto that thought, [pcname]."
                                    show chelsea blank
                                    "Jun" "If you're serious, why don't you meet me at the karaoke joint? We'll be in our usual room."
                                    show chelsea confused
                                    pcname "I thought you couldn't go there anymore?"
                                    "Jun" "We can spare an hour or so for a friend."
                                    show chelsea blank
                                    "Jun" "Be there at six tonight. We'll see you there."
                                    "The line clicks dead."
                                    pause 1.0
                                    show chelsea shocked
                                    pause 1.0
                                    show chelsea blank at exitScene(0.5, 0.0, 0.3, 0.3)
                                    "Glancing at your phone's clock, you realize there isn't much time. Hurriedly, you clean yourself up and gather your things before heading downtown."
                                    scene bg CityE with fade
                                    "'STAR LIGHT' shines like a beacon through the neon chaos that makes up downtown. It's barely past sunset, but the city lights brighten the street more than the sky itself."
                                    scene black with dissolve
                                    "You step into the small building. The cashier at the front desk looks up at you, his customer service face slackening with recognition."
                                    "Karaoke Guy" "Ah, you again. Welcome back."
                                    "Karaoke Guy" "Your usual room is ready for you."
                                    "He gestures vaguely down the hall before returning to his magazine. You waste no time following his directions."
                                    scene bg Karaoke2 with dissolve
                                    "It almost feels like old times as you step into the room; Jun and his lackeys are seated across the chairs, chatting and enjoying their beers as Diego poorly attempts a love song near the front."
                                    "He stops as you walk in, and all eyes turn on you."
                                    show Wareworker at right with dissolve
                                    "Diego" "[pcname]!"
                                    hide Wareworker with dissolve
                                    "Your name rings out like a cheer among the lackeys. Jun raises his beer in greeting and gestures for you to have a seat. Diego returns to his performance."
                                    "You sit in the empty spot beside Jun. He leans forward, raising his voice so you can hear him."
                                    show GHCMan at left with dissolve
                                    "Jun" "This is a good place for meetings if you don't want to be overheard-- although Diego's singing might just kill us in the process."
                                    "Diego shoots his boss a glare but continues singing."
                                    "Jun" "So, what is it you wanted to talk to us about?"
                                    show chelsea with dissolve
                                    "The other men lean in, their expressions serious as they wait for your story."
                                    show chelsea angry
                                    pause 0.5
                                    show black with fade
                                    "And you tell it-- everything-- from the first day you met Matt, and every moment of blackmail and harassment afterward."
                                    "It's embarrassing to confess everything, even moreso to these men that have likely never experienced your position, but you gain a few sympathetic nods and some shaking heads."
                                    hide black
                                    show chelsea sad
                                    with fade
                                    "When you're done, Jun nods to himself thoughtfully."
                                    show chelsea embarrassed
                                    "Jun" "Don't worry about it, [pcname]. We'll take care of this guy for you."
                                    "Relief floods through your chest. You had no idea how much you needed to hear those words until Jun said them."
                                    show chelsea blank
                                    "Jun" "But remember, this is a one time favor. We won't be around to help you if you get in anymore trouble."
                                    "Jun" "That being said, you sure this is what you want?"
                                    show chelsea angry
                                    pcname "I'm sure."
                                    show chelsea blank
                                    "You can't imagine getting yourself into more trouble than you have with Matt, anyway. And after telling Matt off, there's no way he's going to keep his mouth shut."
                                    show chelsea sad
                                    "This is your only option."
                                    show chelsea blank
                                    "Jun nods in understanding, then gestures toward two of his friends. They stand without a word and leave the room."
                                    show chelsea confused
                                    pause 0.5
                                    show chelsea blank
                                    "Before you can ask where they're going, Jun turns to you with a smile."
                                    "Jun" "Since you're here, why don't you stay for a few rounds? I don't think I can stand to hear Diego shriek all night."
                                    show chelsea embarrassed
                                    show Wareworker at right with dissolve
                                    "Diego" "Hey!"
                                    scene black with fade
                                    "You chuckle, then nod. After the stress of today, you could use some relaxation."
                                    $ MafiaFavorMatt = True
                                    $ chelseaContacts.contactsListed.pop("Matt")
                                    $ acts-=1
                                    jump events_end_period
                                "Save Jun's favor for later." if True:
                                    show chelsea sad
                                    "With a sigh, you close your contact list."
                                    show chelsea embarrassed
                                    "What's happening with Matt is high school stuff; there's no way you can justify getting the mafia involved for that."
                                    show chelsea sad
                                    pcname "I'll just need to find another way to stop Matt..."
                                    scene black with fade
                                    "But something tells you such a feat may not be possible."
                                    jump events_end_period
                        elif True:
                            "What you just did took all the bravery you have. Now all that’s left is to see what consequences follow..."
                        show bg black with dissolve
                        $ mattblackmail = 2
                        jump events_end_period
                    elif True:
                        $ mattblackmail = 1
                        "He flips open his phone and turns it toward you, swiping it again and again."
                        "Picture after picture of the things you've done with him..."
                        show Matt Casual Smirk at left
                        m "Last chance, slut. Take off your clothes or everyone sees these."
                        "Numb with shock, you can barely shake your head."
                        menu standfirmbackdown2_blackmail:
                            "Give in." if True:
                                $ corruption += 3
                                show chelsea embarrassed
                                pcname "Fine... I..."
                                show chelsea sad
                                "You can barely breathe as you lift your hands to obey him."
                            "Refuse." if True:
                                "Matt storms past you, shoving you roughly to the side. You go down to your knees."
                                show Matt Casual Smirk at left
                                "Matt" "You should have obeyed me, slut."
                                show Matt Casual Blank at left
                                "Matt" "Bye."
                                hide Matt with dissolve
                                "The door slams shut behind him. You’re left alone in the room, arms crossed over your chest."
                                if mafiafavor == True:
                                    show chelsea sad with dissolve
                                    "While you try to put on a brave face, there is a sudden shake in your knees that renders you weak. You take a seat on the couch and try to calm the thundering beat of your heart."
                                    "What can you do now? Matt has enough blackmail on you to destroy your reputation, not to mention how the school board will react..."
                                    show chelsea embarrassed
                                    pcname "How am I going to get out of this?"
                                    show chelsea sad
                                    "You pull out your phone with the intention of looking up if anyone else went through this situation. You can't be the only one, right?"
                                    "But before you pull open your web browser, your contact list slides open, and Jun's phone number stares at you from the bright little screen."
                                    show chelsea confused
                                    pcname "Jun did offer me a favor... but can I really take him up on it for something like this?"
                                    show chelsea blank
                                    menu mattmafia2:
                                        "Use Jun's favor to stop Matt." if True:
                                            $ mattsubmissive = False
                                            "Gripping the phone in your hand, you dial Jun's number."
                                            show chelsea sad
                                            "This is a last resort, but after all of Matt's blackmailing, you can't think of any other way to stop him."
                                            show chelsea blank
                                            "The phone rings for a few moments before picking up. There's a slight pause, and you catch your breath."
                                            "Jun" "Yeah?"
                                            if club == "track":
                                                show chelsea embarrassed
                                                pcname "Hey, Jun. Remember me?"
                                            elif club == "cheer":
                                                show chelsea laugh
                                                pcname "Hey Jun~! It's me, [pcname]."
                                            elif club == "yearbook":
                                                show chelsea sad
                                                pcname "H-Hi, Jun. It's me... [pcname]..."
                                            show chelsea embarrassed
                                            "Jun laughs on the other line, his gruffness suddenly disappearing as your voice confirms your identity."
                                            "Jun" "I was wondering when you'd call, [pcname]. What's going on? You think of something you need?"
                                            show chelsea sad
                                            pcname "That's what I'm calling about, actually. I--"
                                            show chelsea shocked
                                            "Jun" "Ah-ah, hold onto that thought, [pcname]."
                                            show chelsea blank
                                            "Jun" "If you're serious, why don't you meet me at the karaoke joint? We'll be in our usual room."
                                            show chelsea confused
                                            pcname "I thought you couldn't go there anymore?"
                                            "Jun" "We can spare an hour or so for a friend."
                                            show chelsea blank
                                            "Jun" "Be there at six tonight. We'll see you there."
                                            "The line clicks dead."
                                            pause 1.0
                                            show chelsea shocked
                                            pause 1.0
                                            show chelsea blank at exitScene(0.5, 0.0, 0.3, 0.3)
                                            "Glancing at your phone's clock, you realize there isn't much time. Hurriedly, you clean yourself up and gather your things before heading downtown."
                                            scene bg CityE with fade
                                            "'STAR LIGHT' shines like a beacon through the neon chaos that makes up downtown. It's barely past sunset, but the city lights brighten the street more than the sky itself."
                                            scene black with dissolve
                                            "You step into the small building. The cashier at the front desk looks up at you, his customer service face slackening with recognition."
                                            "Karaoke Guy" "Ah, you again. Welcome back."
                                            "Karaoke Guy" "Your usual room is ready for you."
                                            "He gestures vaguely down the hall before returning to his magazine. You waste no time following his directions."
                                            scene bg Karaoke2 with dissolve
                                            "It almost feels like old times as you step into the room; Jun and his lackeys are seated across the chairs, chatting and enjoying their beers as Diego poorly attempts a love song near the front."
                                            "He stops as you walk in, and all eyes turn on you."
                                            show Wareworker at right with dissolve
                                            "Diego" "[pcname]!"
                                            hide Wareworker with dissolve
                                            "Your name rings out like a cheer among the lackeys. Jun raises his beer in greeting and gestures for you to have a seat. Diego returns to his performance."
                                            "You sit in the empty spot beside Jun. He leans forward, raising his voice so you can hear him."
                                            show GHCMan at left with dissolve
                                            "Jun" "This is a good place for meetings if you don't want to be overheard-- although Diego's singing might just kill us in the process."
                                            "Diego shoots his boss a glare but continues singing."
                                            "Jun" "So, what is it you wanted to talk to us about?"
                                            show chelsea with dissolve
                                            "The other men lean in, their expressions serious as they wait for your story."
                                            show chelsea angry
                                            pause 0.5
                                            show black with fade
                                            "And you tell it-- everything-- from the first day you met Matt, and every moment of blackmail and harassment afterward."
                                            "It's embarrassing to confess everything, even moreso to these men that have likely never experienced your position, but you gain a few sympathetic nods and some shaking heads."
                                            hide black
                                            show chelsea sad
                                            with fade
                                            "When you're done, Jun nods to himself thoughtfully."
                                            show chelsea embarrassed
                                            "Jun" "Don't worry about it, [pcname]. We'll take care of this guy for you."
                                            "Relief floods through your chest. You had no idea how much you needed to hear those words until Jun said them."
                                            show chelsea blank
                                            "Jun" "But remember, this is a one time favor. We won't be around to help you if you get in anymore trouble."
                                            "Jun" "That being said, you sure this is what you want?"
                                            show chelsea angry
                                            pcname "I'm sure."
                                            show chelsea blank
                                            "You can't imagine getting yourself into more trouble than you have with Matt, anyway. And after telling Matt off, there's no way he's going to keep his mouth shut."
                                            show chelsea sad
                                            "This is your only option."
                                            show chelsea blank
                                            "Jun nods in understanding, then gestures toward two of his friends. They stand without a word and leave the room."
                                            show chelsea confused
                                            pause 0.5
                                            show chelsea blank
                                            "Before you can ask where they're going, Jun turns to you with a smile."
                                            "Jun" "Since you're here, why don't you stay for a few rounds? I don't think I can stand to hear Diego shriek all night."
                                            show chelsea embarrassed
                                            show Wareworker at right with dissolve
                                            "Diego" "Hey!"
                                            scene black with fade
                                            "You chuckle, then nod. After the stress of today, you could use some relaxation."
                                            $ MafiaFavorMatt = True
                                            $ chelseaContacts.contactsListed.pop("Matt")
                                            $ acts-=1

                                            jump events_end_period
                                        "Save Jun's favor for later." if True:
                                            show chelsea sad
                                            "With a sigh, you close your contact list."
                                            show chelsea embarrassed
                                            "What's happening with Matt is high school stuff; there's no way you can justify getting the mafia involved for that."
                                            show chelsea sad
                                            pcname "I'll just need to find another way to stop Matt..."
                                            scene black with fade
                                            "But something tells you such a feat may not be possible."
                                            jump events_end_period
                                elif True:
                                    "What you just did took all the bravery you have. Now all that’s left is to see what consequences follow..."
                                show bg black with dissolve
                                $ mattblackmail = 2
                                jump events_end_period
                "Back Down" if True:
                    if defymatt:
                        show chelsea angry
                        "Part of you wants to fight. Part of you wants to take off the stupid degrading collar and throw it on the ground, right here right now."
                        show chelsea sad
                        "But, then you remember all of the material he has on you. The pictures. If Matt wanted too, he could ruin your life."
                        "So, with a resigned sigh, you obey."
                        pcname "Yes, Sir..."
                        show Matt Casual Smirk at left
                        "Matt’s smirk returns. There is nothing he loves quite as much as winning."
                    elif True:
                        show chelsea embarrassed
                        "Your heart hammers against your ribs. He sounds so {i}powerful{/i}..."
    show bg black with dissolve
    hide chelsea with dissolve
    hide Matt Casual Smirk with dissolve
    "You slip out of your jacket and pull your shirt up over your head. Neither is an especially artful act. The situation is already mortifying enough."
    "Matt" "You call that stripping? Wiggle that ass a bit. Make it fun."
    if violetrelate == "Sub":
        "You can’t help but let out a giddy giggle. A certain memory returns to your mind."
        "Matt" "Is something funny, slut?"
        pcname "No, Sir. Sorry, Sir."
        "What Matt doesn’t know is that you’d been in this very room once before while a girl gave an erotic striptease for her dominant. Only that girl wasn’t you."
    "You make a show of shaking your hips back and forth as you work down your shorts. In the process, you bend over to give him a clear view of your ass."
    if club == "track":
        "Your dance is workmanlike but competent. If your task is turning Matt on, then at least you can do it well."
    elif club == "cheer":
        "Your movements are practiced. Even if it’s in a more embarrassing context, there’s a certain thrill that comes with knowing that you’ve captured his eyes."
    elif club == "yearbook":
        "You doubt that you do a good job of it. All your movements are stiff and awkward. It’s hard to be sexy when his gaze makes you want to cower."
    "Afterwards, you find yourself standing in your underwear. Without thinking, your arms cross over your chest."
    "Matt" "Naked. Dogs don’t wear clothes, do they?"
    "You sigh. How did you know he would say that?"
    "It's a little awkward to make sexy, but you undo the clasps of your bra, working the process into your little dance."
    "For a moment, you hold your hands over your bra - that last bit of protection between you and exposure."
    "Then, taking a deep breath, you pull them away. Your bra flutters to the ground."
    "You turn your back to him and move to slip off your panties. Unable to see him, you can only guess where he’s looking, what he’s thinking."
    "Then you turn back to him. For the first time, you’re totally aware of the collar. Clothed, you could focus on something else."
    "But exposed, the tightness around your neck dominates your senses. It’s impossible not to focus on it."
    "Matt takes his time rolling his eyes up and down your body. Everywhere he stares, it feels like his eyes will bore a hole. Your cheeks burn."
    "Matt" "Hmm. That’s better, but you still needed way too much coaxing."
    "Matt" "Sometimes, I don’t even know why I even bother with you."
    if defymatt:
        "You wish he’d bother with you less, really."
    elif True:
        pcname "Sorry, Sir."
        "Matt just grunts."
    "Matt" "Don’t get too relaxed, Bitch. Something’s still wrong here."
    "Matt" "See, I have a dog back at home. She’s a good girl, so I know what a proper bitch looks like."
    "He reclines back on your sofa and points down to the floor."
    "Matt" "And you know what I’ve ever seen her do? Stand."
    "Matt" "Get down on all fours, Bitch. Now."
    show bg MDS3 with dissolve
    "Your head hangs low as you slowly sink to your hands and knees. Even naked but for a dog collar, there was still some dignity in standing. Did he mean to truly treat you like an animal?"
    pcname "I-"
    "Matt snarls."
    "Matt" "Stop. Do bitches speak?"
    pcname "N-"
    "Matt" "I said stop. Are you deaf? Do I need to give your ass a few whacks with my belt until you understand?"
    "Matt" "Don’t talk. {i}Bark{/i}."
    "The command seems strange to you, but you’re not in a position to disobey. You try giving a half-hearted yelp, but it comes across more like a dying bird."
    "You giggle nervously, but that proves a mistake."
    "Matt" "It’s not fucking funny."
    show bg MDS1 with dissolve
    "He rises from his seat and stands over you. If he towered over you when you were on two feet, now he’s a giant."
    "You can merely cower as he grips a hand in your hair and roughly pulls your head up to face him. An involuntary gasp slips out."
    "Matt" "No more jokes. No more games. Tonight you’re going to be my bitch. And you’re going to crawl on all fours. And you’re going to fucking bark like you mean it."
    "Matt" "You’re not a person. You’re just a disobedient {i}bitch{/i}."
    "Matt" "Now stop pussyfooting around and {i}bark{/i}."
    menu fightbacktryharder3:
        "Fight back." if True:
            "You clutch at his arm desperately. Your eyes are wide with desperation."
            pcname "Please. That hurts, Matt..."
            "Matt glares, as if trying to determine if he wants to punish you for that small act of defiance. But then his grip on your hair loosens."
            "Matt" "One more chance. Impress me."
            "You nod fearfully. You’re in too deep now to truly fight back."
            "You wonder if this is the kind of humiliation that leaves a person too subdued to act willfully. Try as you might to resist, it’s getting to you."
        "Try harder." if True:
            $ corruption += 2
            pass
    "You back up slightly and take in a deep breath. He waits overhead, radiating an aura that commands your best effort."
    pcname "Yip! Yip!"
    pcname "Bark!"
    "With a sigh, he releases you and storms back to the couch. You pant, trying to catch your breath, and lower yourself even closer to the floor."
    "Matt" "That’s better. It seems you can at least be trained."
    "You hide your face behind your hair. Every word drives the shame deeper and deeper. When you first put on the collar, you hadn’t expected it to be this degrading."
    "Matt" "Now, let’s kick this up a notch."
    "Matt" "You know what a dog’s begging position is, right? If I have to explain that, you’re really as dumb as you look right now."
    "Matt snaps his fingers."
    "Matt" "Beg, Bitch."
    "You slowly adopt the posture, sitting up straight on your hind legs with wrists bent in front of you. It’s your best approximation of a dog."
    "Matt" "Legs spread more. You don't get to have any shame."
    "You slam your eyes shut and whine, but he’s already driven the defiance out of you. Your legs open wider, exposing your sex to him."
    "It’s nothing he hasn’t seen already, but in this pose there is something exponentially more shameful about it."
    "And that’s when you hear a loud snap sound. A camera taking a picture."
    show bg MDS2 with flash
    "You open your eyes wide. Matt has his phone in hand and a ghoulish grin on his face. With every snap, he immortalizes you in your most degraded moment."
    "{i}Snap. Snap. Snap.{/i}"
    pcname "Wait, don’t-"
    "Matt glares."
    "Matt" "Bitches don’t talk. Shut that mouth and hold the position."
    "You squeeze your eyes tight, obediently holding position even as he takes more and more pictures of you. Any one of them could ruin your life, and now his entire camera roll is filled with it."
    "There’s a strange, hypnotic quality to the sound of the camera. Every time you hear it, your head grows a little fuzzier, as though the shame is too much."
    "Matt" "Now on your back. Roll over."
    "You already know what’s going to happen. More pictures for Matt’s photo roll. It’s too overwhelming to comprehend. Your body moves on autopilot as you settle in on your back with legs spread."
    "{i}Snap. Snap. Snap.{/i}"
    "You let out an involuntary whine. How did he make you so helpless? The thought is an ocean to swim in."
    "You barely notice when the snapping stops. Your senses feel dull - maybe even dead."
    show bg MDS1 with dissolve
    "Matt has to wave a bright red rubber ball in front of your face for a minute to ground you back in reality."
    "Matt" "I think you know what this is for, don’t you, girl? Time to play a little game."
    "You blink twice. He doesn’t actually want to play fetch with you, does he?"
    "Tossing the ball across the room, Matt points to it and gestures you forward. Dark little laughs burst out in between his words."
    "Matt" "Fetch, girl. Fetch!"
    "Groaning involuntarily, you move to grab it. The action is almost silly; something you can do with your mind turned off."
    "You pick up the ball with your hand and bring it back to him. Matt gives a little disappointed noise when he sees how you grabbed the ball."
    "Still, he doesn’t force the point. Instead, he turns in the opposite direction and throws the ball again. You watch it sail through the air. The entire moment feels numbly surreal."
    "Matt" "Get the ball, slut. Get the ball."
    menu getingorwary4:
        "Get into it" if True:
            $ getintoit = True
            $ corruption += 5
            "You soon discover that there is something strangely freeing about this little game. Perhaps it’s the surrealness of it, mixed with the mortifying humiliation from moments before."
            "But, there’s something about it that allows your mind to just... melt away."
            "You let go, sinking into the moment and letting go of your worries about how you look or if what you’re doing makes sense."
            "You start to just... get the ball."
            if club == "track":
                "You rush to the ball each time with astonishing speed. Trying to reach the ball as fast as you can becomes a game unto itself."
            elif club == "cheer":
                "Without thinking, you make a show of wiggling your rear like a playful puppy whenever you move to get it. It simply comes naturally."
            elif club == "yearbook":
                "Your first few attempts are timid, but you're motivated by the way that Matt responds."
                "He's giving you... encouragement? Or at the very least, as close to it as Matt has ever given."
            "At first, you continue grabbing the ball with your hand. But one time, without thinking, you grab it with your teeth. After all, that’s just how playing fetch works, right?"
            "After that, you use your mouth on every chase. Eventually, you drag the ball back, drop it at his feet, and give a little pant."
            "At once, your inhibitions return, and realization of what you did hits you."
            "Did you just act like a dog without prompting?"
            "You hide your face in your hair, so he doesn’t see the blush."
            "Not that it stops Matt. He lets out a playful little laugh; no doubt at your embarrassment as much as what you just did. Afterward, he returns the ball to his backpack."
        "Remain Wary" if True:
            "You do as he commands, fetching several times - but always with a rigid posture and by grabbing the ball with your hands."
            "Even by the fourth or fifth time, the game never feels less degrading."
            "Matt, of course, starts excited and amused by the game. But without a reaction from you, he loses steam rather fast."
            "After just a few repetitions, he returns the ball to his backpack."
    "He reclines in his seat, like a king looking down upon his subject. Without thinking, you lower your posture slightly into a deeper bow."
    if getintoit == True:
        "Matt" "You’re not bad. Eager, at least, even if you don’t know how to show it. But I clearly have my work cut out for me."
    elif True:
        "Matt" "Horrible. You barely even tried. The only thing worse than a bitch is a dumb bitch."
    "Matt" "Tsk."
    "Matt" "Not remotely as good as Sandy, back home. If I tell her to beg, she gets right in position. Really, she’s a lot better than you."
    "There are few things at this point that would make you hang your head low, but being compared unfavorably to an actual dog is one of them."
    "Matt" "Hmm."
    "He smiles deviously."
    "Matt" "You know, sometimes though... Sandy can be a bit disobedient. See, bitches get into heat sometimes and they can’t control themselves."
    "Matt" "How about it, Bitch? Are you in heat? Is that why you're not listening?"
    "It takes a second for the words he’s saying to even become comprehensible. Does he want you to...?"
    "Matt" "Roll onto your back and spread your legs. Let’s see if you’re in heat."
    "At his command, you roll over. Against this newest humiliation, the power of his gaze is too strong. You glance to the side, waiting for his judgment to come."
    if getintoit == True:
        "Matt" "Would you look at that. You’re fucking soaked, bitch."
        "Matt" "You must really get off on being treated like a fucking dog, huh?"
        "Your cheeks burn. You hadn’t really noticed until now, but he’s right. Your clit is swollen and your labia are practically dripping."
        "And now that he’s drawn your attention to it, it's all you can think about."
        "Are you... enjoying this?"
        if defymatt:
            "What is he doing to you?"
    elif True:
        "Matt" "Hmm. Not good enough. Clearly a bit more stimulation is required."
        "You fidget in place. Whatever he has in mind, it’s going to be mortifying."
    "Matt" "You know, when she goes into heat, she really can’t control herself. She’ll hump anything. My desk. The lamp post by the street..."
    m "...even my leg."
    "To punctuate this, Matt stretches out his leg. You stare at it, stunned. Every time you think you’ve reached a new low, Matt finds somewhere more pathetic to take you."
    menu surrenderplead5:
        "Surrender to him." if True:
            $ corruption += 2
            "Lowering your head, you obediently crawl forward. Humping his leg like a dog... would you even be able to get off doing that? It seems so strange."
        "Plead." if True:
            pcname "Matt, please... That’s..."
            "Your voice comes out in a croak. The events of the evening have beaten you down to the point where vocalizing your thoughts is hard. Not that Matt listens."
            "Matt" "Bitches don’t talk."
            "Matt" "You know what you have to do."
            "You plead with your eyes, wide and desperate. It seems impossible to escape this latest degradation."
            "Matt" "Now, cunt. My leg isn’t exactly going to hump itself, is it?"
            "Had he started with this command, you almost certainly would have refused. But, after he took pictures of you begging like a dog, was there even a line anymore?"
            "Your cheeks burn as you crawl towards him, head down and unwilling to meet his eyes."
    show bg MDS3 with dissolve
    "You turn around and position yourself so his leg is between your legs. It takes some experimentation, but you find that by rubbing back and forth you actually get the stimulation you need."
    "The sensation starts to build and, as difficult as it is to admit, it feels good."
    pcname "Mmmmm."
    "Your pace quickens, going from timid movements to the kind of thrusting and sliding that produces actual friction."
    "You’re actually doing it. You’re humping his leg."
    if getintoit == True:
        "Your panting grows louder and louder. Your head fogs. The longer you use his leg to get off, the less and less it seems strange. All you can focus on is how badly you want to get off. How turned on you’re becoming."
    elif True:
        "The thought is a shameful one. You swear in a small voice between pants. If anyone discovered you’d did this, you’d be mortified."
        if damienrelate == "dating":
            "Especially Damien..."
        elif violetrelate == "Sub":
            "Especially Violet..."
        elif katerelate == "girlfriend":
            "Especially Kate..."
    "Matt" "Faster, cunt. Faster!"
    "Your body obeys his command. You leave liquid proof of your lust all over his leg. Lubrication to make humping it an easier task."
    pcname "Haaa... Haaa..."
    if getintoit == True:
        "Your head grows more and more empty. It’s hard to think. It’s hard to process anything. It doesn’t matter how shameful, how degrading a position you’re in. You just want to cum against his leg. You just want to cum."
        "You ride the high, panting and moaning. The sensation you’re hunting grows closer. The tension, the ache, rises to a fever pitch. Like a dam that’s about to burst."
        pcname "Ah... Ahhh!"
        "A single shiver fires up your spine. And then you explode."
        pcname "Ahh, fuck... Oh... Ahhh!"
        "You spasm and fall forward, panting and moaning in heated desperation. Matt’s foot withdraws, but you’re still left riding the wave."
        "You slump onto the floor, your face dirtied by its surface. As the spasms recede, you’re left blinking a few times. Comprehension of what just happened returns in half-formed glimpses."
    elif True:
        "You just want it to end. The shame is too much. The intensity is too much. It doesn’t matter how good his leg feels. Your limit is fast approaching."
        "So, rather than wait for the sessions to come to a natural end, you decide to act."
        pcname "Ah! Ahhhh!"
        "You simulate the shaking and moaning of an actual orgasm. Faking it isn’t something you’ve had much practice with, but Matt seems to buy your little performance and pull his leg back."
    "Without thinking, your hand goes to the tag on the collar. Your lungs look for air, but the firm leather only lets so much in at one moment."
    "Matt" "Hmm. Good enough, slut."
    "He doesn’t even give you time to recover, he just grabs your hair and forces you back up to your knees. There’s little strength in your body. He’s the only thing keeping you up."
    "In a blink, he has his fly open and his cock out. It waves in front of you, so close you catch its scent, so familiar you can almost taste it."
    "Matt takes a hand to it and starts to stroke. He doesn’t go slow. If there is a goal, it’s not to savor the sensation. He’s trying to cum fast."
    "You stare, mouth slightly parted, at his manhood, struggling to decide what to do."
    "Matt" "Open wide, bitch. It’s time for your favorite treat."
    show bg MDS4 with dissolve
    "You only have a split second to prepare yourself. He must have enjoyed the earlier play quite a bit, because it takes less than a minute of stroking before he cums all over your face."
    "He releases your hair. No longer supported by his hand, you sink back down to the ground, cum dripping from your face."
    "You’re left in an exhausted heap. It’s hard to move or think, as if your brain has been totally overwhelmed."
    "Back near the couch, you hear the sound of a zipper."
    show bg black with fade
    show bg HomeE with dissolve
    show Matt Casual Angry with dissolve
    "Matt" "Mediocre. Everything about your performance was mediocre."
    "Matt" "It’s a good thing I actually like training or else you’d be fucking hopeless."
    show Matt Casual Pleased
    "You let out a long groan. It takes another few seconds before Matt’s words start to sink in."
    show Matt Casual Happy
    "Matt" "Fucking talk again. Jeez."
    pcname "...Yes, Sir..."
    show Matt Casual Angry
    "Matt" "Oh yeah, don’t mention my mother to me ever again. Don’t speak to her either. That’s my life. Mine. If I fucking wanted to take you to my god damn family, I would. My toys don’t need to meet my parents."
    show Matt Casual Question
    "Matt" "We clear?"
    "You shake your head slowly."
    show Matt Casual Blank
    "Matt" "Good. Clean yourself up. The collar is yours to keep. I’m expecting you to hold on to it."
    "You wipe your face with your hand. It’s filthy. You look up and see Matt briskly leaving, backpack in arm. He doesn’t so much as say goodbye."
    "The door slams."
    hide Matt Casual Blank with dissolve
    "It takes another few minutes before full comprehension returns to you. You’re sitting on the floor naked and shivering. Your neck still sports the dog collar, and your face is covered in cum."
    if getintoit == True:
        "Without thinking, you let out a soft sigh. Was that mortifying? Enjoyable? Your brain is too muddled to sort through these conflicted feelings."
    elif True:
        "Your eyes start to water up. That was intense. Perhaps more intense than you’re able to handle..."
    "Without thinking, you reach behind your neck and unbuckle your new collar. It slips down to the floor. One word hangs prominently in the front."
    "{b}\"Bitch\"{/b}"
    show bg black with dissolve
    if mafiafavor == True:
        show bg HomeE with dissolve
        show chelsea sad with dissolve
        "While you try to put on a brave face, there is a sudden shake in your knees that renders you weak. You take a seat on the couch and try to calm the thundering beat of your heart."
        "What can you do now? Matt has enough blackmail on you to destroy your reputation, not to mention how the school board will react..."
        show chelsea embarrassed
        pcname "How am I going to get out of this?"
        show chelsea sad
        "You pull out your phone with the intention of looking up if anyone else went through this situation. You can't be the only one, right?"
        "But before you pull open your web browser, your contact list slides open, and Jun's phone number stares at you from the bright little screen."
        show chelsea confused
        pcname "Jun did offer me a favor... but can I really take him up on it for something like this?"
        show chelsea blank
        menu mattmafia3:
            "Use Jun's favor to stop Matt." if True:
                $ mattsubmissive = False
                "Gripping the phone in your hand, you dial Jun's number."
                show chelsea sad
                "This is a last resort, but after all of Matt's blackmailing, you can't think of any other way to stop him."
                show chelsea blank
                "The phone rings for a few moments before picking up. There's a slight pause, and you catch your breath."
                "Jun" "Yeah?"
                if club == "track":
                    show chelsea embarrassed
                    pcname "Hey, Jun. Remember me?"
                elif club == "cheer":
                    show chelsea laugh
                    pcname "Hey Jun~! It's me, [pcname]."
                elif club == "yearbook":
                    show chelsea sad
                    pcname "H-Hi, Jun. It's me... [pcname]..."
                show chelsea embarrassed
                "Jun laughs on the other line, his gruffness suddenly disappearing as your voice confirms your identity."
                "Jun" "I was wondering when you'd call, [pcname]. What's going on? You think of something you need?"
                show chelsea sad
                pcname "That's what I'm calling about, actually. I--"
                show chelsea shocked
                "Jun" "Ah-ah, hold onto that thought, [pcname]."
                show chelsea blank
                "Jun" "If you're serious, why don't you meet me at the karaoke joint? We'll be in our usual room."
                show chelsea confused
                pcname "I thought you couldn't go there anymore?"
                "Jun" "We can spare an hour or so for a friend."
                show chelsea blank
                "Jun" "Be there at six tonight. We'll see you there."
                "The line clicks dead."
                pause 1.0
                show chelsea shocked
                pause 1.0
                show chelsea blank at exitScene(0.5, 0.0, 0.3, 0.3)
                "Glancing at your phone's clock, you realize there isn't much time. Hurriedly, you clean yourself up and gather your things before heading downtown."
                scene bg CityE with fade
                "'STAR LIGHT' shines like a beacon through the neon chaos that makes up downtown. It's barely past sunset, but the city lights brighten the street more than the sky itself."
                scene black with dissolve
                "You step into the small building. The cashier at the front desk looks up at you, his customer service face slackening with recognition."
                "Karaoke Guy" "Ah, you again. Welcome back."
                "Karaoke Guy" "Your usual room is ready for you."
                "He gestures vaguely down the hall before returning to his magazine. You waste no time following his directions."
                scene bg Karaoke2 with dissolve
                "It almost feels like old times as you step into the room; Jun and his lackeys are seated across the chairs, chatting and enjoying their beers as Diego poorly attempts a love song near the front."
                "He stops as you walk in, and all eyes turn on you."
                show Wareworker at right with dissolve
                "Diego" "[pcname]!"
                hide Wareworker with dissolve
                "Your name rings out like a cheer among the lackeys. Jun raises his beer in greeting and gestures for you to have a seat. Diego returns to his performance."
                "You sit in the empty spot beside Jun. He leans forward, raising his voice so you can hear him."
                show GHCMan at left with dissolve
                "Jun" "This is a good place for meetings if you don't want to be overheard-- although Diego's singing might just kill us in the process."
                "Diego shoots his boss a glare but continues singing."
                "Jun" "So, what is it you wanted to talk to us about?"
                show chelsea with dissolve
                "The other men lean in, their expressions serious as they wait for your story."
                show chelsea angry
                pause 0.5
                show black with fade
                "And you tell it-- everything-- from the first day you met Matt, and every moment of blackmail and harassment afterward."
                "It's embarrassing to confess everything, even moreso to these men that have likely never experienced your position, but you gain a few sympathetic nods and some shaking heads."
                hide black
                show chelsea sad
                with fade
                "When you're done, Jun nods to himself thoughtfully."
                show chelsea embarrassed
                "Jun" "Don't worry about it, [pcname]. We'll take care of this guy for you."
                "Relief floods through your chest. You had no idea how much you needed to hear those words until Jun said them."
                show chelsea blank
                "Jun" "But remember, this is a one time favor. We won't be around to help you if you get in anymore trouble."
                "Jun" "That being said, you sure this is what you want?"
                show chelsea angry
                pcname "I'm sure."
                show chelsea blank
                "You can't imagine getting yourself into more trouble than you have with Matt, anyway. And after telling Matt off, there's no way he's going to keep his mouth shut."
                show chelsea sad
                "This is your only option."
                show chelsea blank
                "Jun nods in understanding, then gestures toward two of his friends. They stand without a word and leave the room."
                show chelsea confused
                pause 0.5
                show chelsea blank
                "Before you can ask where they're going, Jun turns to you with a smile."
                "Jun" "Since you're here, why don't you stay for a few rounds? I don't think I can stand to hear Diego shriek all night."
                show chelsea embarrassed
                show Wareworker at right with dissolve
                "Diego" "Hey!"
                scene black with fade
                "You chuckle, then nod. After the stress of today, you could use some relaxation."
                $ MafiaFavorMatt = True
                $ chelseaContacts.contactsListed.pop("Matt")
                $ acts-=1

                jump events_end_period
            "Save Jun's favor for later." if True:
                show chelsea sad
                "With a sigh, you close your contact list."
                show chelsea embarrassed
                "What's happening with Matt is high school stuff; there's no way you can justify getting the mafia involved for that."
                show chelsea sad
                pcname "I'll just need to find another way to stop Matt..."
                scene black with fade
                "But something tells you such a feat may not be possible."
                jump events_end_period
    $ acts-=1
    show bg black with dissolve
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
