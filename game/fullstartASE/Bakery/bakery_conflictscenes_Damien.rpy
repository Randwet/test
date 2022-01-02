label bakery_damienconflict2:
    $ DamienAngry = "Characters/Damien/Casual/Angry.png"
    $ DamienBlank = "Characters/Damien/Casual/Blank.png"
    $ DamienGlare = "Characters/Damien/Casual/Glaring.png"
    $ DamienLaugh = "Characters/Damien/Casual/Laughing.png"
    $ DamienNeutral = "Characters/Damien/Casual/Neutral.png"
    $ DamienSad = "Characters/Damien/Casual/Sad.png"
    $ DamienShocked = "Characters/Damien/Casual/Shocked.png"
    $ DamienSmiling = "Characters/Damien/Casual/Smiling.png"
    $ DamienWorrying = "Characters/Damien/Casual/Worrying.png"
    $ clothes, hair = casualwear
    scene bg RoomE with dissolve
    show chelsea happy at right with moveinright
    "Despite how busy you've been, you're pleased when Damien suggests having a movie night at your house after work."
    "As you settle into some comfortable clothes, your phone buzzes with a new text."
    hide chelsea with moveoutleft

    call screen TextingScene("Damien",
    [
        TextMessage("I'm outside with the goods."),
        TextMessage("Be right there!", sender = False)
    ])

    show bg HomeE with dissolve
    show chelsea at right with moveinright
    show Damien Happy at left with dissolve
    "You head into the living room and open the front door. Damien stands outside with a wide grin and a box set of movies in his hands."
    "You can make out an angry set of dwarves on the front cover crowded around a ring."
    show chelsea happy
    pcname "What happened to watching {i}one{/i} movie?"
    show Damien Laugh at left
    D "Well, I may have gotten a little carried away..."
    "Damien gives you an embarrassed smile and steps inside, careful to remove his shoes. You can't help but smile back."
    show chelsea laugh
    pcname "Don't get mad if I fall asleep on you."
    show Damien Happy at left
    D "Oh, I won't mind."
    show chelsea happy
    "Damien heads to your television set. While he sets the movie up, you retreat to the kitchen and toss some popcorn in the microwave."
    hide Damien Happy with moveoutleft
    "After a few minutes, you pour the hot snack into a bowl and carry it back into the living room."
    show Damien Blank at left with moveinleft
    "Clips from the film play out on a main menu screen on the TV while fantasy music plays loudly over the speakers."
    "You expect to find Damien waiting for you, eager to start the film. Instead you're surprised to see him standing by your coffee table, a piece of paper in hand."
    "He looks up as you set the bowl of popcorn down, finally noticing you."
    show Damien Neutral at left
    D "What is this?"
    show Damien Blank at left
    "He holds out the piece of paper. You take it from his hand. Upon closer inspection you see that it's the sheet of plastic surgeons Lisa gave you."
    show chelsea blank
    pcname "Oh. My coworker, Lisa, gave it to me."
    "You set it back down on the table and recline against the couch. Damien stares at you, troubled."
    show Damien Neutral at left
    D "Your coworker?"
    show Damien Worry at left
    D "You aren't actually considering getting breast implants, are you?"
    menu bakery_damienconflict_implants:
        "I am, actually." if True:
            show Damien Blank at left
            "Damien stares at you, trying to register what you just said."
            show Damien Neutral at left
            D "But... {i}Why?{/i}"
            show Damien Worry at left
            D "[pcname], you are beautiful just the way you are. You seriously don't need to make these kind of changes to your body."
            show Damien Blank at left
            pcname "I know that, but..."
            show chelsea sad
            "You look down at your breasts, discouraged. You can't help but think of everything Keith and Lisa have said about them."
            if club == "track":
                show chelsea blank
                pcname "There's nothing {i}wrong{/i} with making changes to my body."
                show chelsea happy
                pcname "In fact, since I've dyed my hair, I've been feeling more confident about these sort of changes."
                pcname "I feel like- like I have more control over my femininity, you know?"
                pcname "It helps that my coworkers at work have been really encouraging about it."
            elif club == "cheer":
                pcname "My body feels almost too... childish as it is."
                show chelsea happy
                pcname "I want to look a little more mature, you know?"
                pcname "Besides, everyone at work loves the idea."
            elif club == "yearbook":
                pcname "I... I want to feel more... more confident."
                show chelsea embarrassed
                pcname "E-everyone at work thinks it's a good idea..."
            show Damien Neutral at left
            D "At work? Is that why you're doing this, [pcname]?"
            show chelsea blank
            show Damien Blank at left
            "Damien sits down beside you. He places his hand on top of yours, his expression serious."
            show Damien Neutral at left
            D "Are they pressuring you into this, [pcname]?"
            menu bakery_damienconflict_pressure:
                "Yes." if True:
                    "You think back to how often Lisa has brought up the idea of a boob job and Keith's enthusiasm for the idea. Even if you didn't notice it right away, you can't deny there's a certain pressure you feel to go through with it."
                    show chelsea sad
                    if club == "track":
                        pcname "I mean, yeah. I guess so."
                    elif club == "cheer":
                        pcname "I don't know. Maybe? In a way..."
                    elif club == "yearbook":
                        pcname "I-I... Well... Y-Yes..."
                    show Damien Angry at left
                    D "Seriously? That's... That's bullshit!"
                    show chelsea shocked
                    "You stare at him in shock. You're not sure you've ever heard Damien swear, much less raise his voice."
                    show Damien Glare at left
                    "He notices your reaction and frowns. He takes a deep breath, trying to calm down, but he's still clearly bothered."
                    show chelsea blank
                    show Damien Neutral at left
                    D "I'm sorry. I just-"
                    show Damien Glare at left
                    D "This is not okay. {i}None{/i} of this is okay."
                    show Damien Neutral at left
                    D "Your job isn't worth this."
                    D "This is a {i}huge{/i} change they're asking you to make on {i}your{/i} body. Not to mention risky, and expensive-"
                    show Damien Blank at left
                    pcname "I'm not worried about the money."
                    show Damien Neutral at left
                    "Damien stops, confused."
                    show Damien Worry at left
                    show chelsea happy
                    pcname "Keith knows about it. He's willing to give me a loan for it."
                    show Damien Glare at left
                    "Although you hope the confirmation that you had at least thought some of this through would be a comfort to Damien, it only seems to upset him further."
                    show Damien Angry at left
                    D "Why is {i}Keith{/i} involved in any of this?"
                    D "That's really inappropriate."
                    show Damien Glare at left
                    show chelsea blank
                    pcname "Maybe, but it would help cover the medical bill."
                    "Damien taps his fingers against the armrest of your couch, leaning away from you. Despite being right next to him, you can't help but feel there's a wall building up between you."
                    show Damien Neutral at left
                    D "Why don't you tell me more about Keith? You never mentioned him before, but you seem to be talking about him a lot more now."
                    show Damien Blank at left
                    show chelsea sad
                    "Your body tenses under his gaze. Although his words are gentle, you can hear the suspicion in his voice."
                    show chelsea blank
                    "You have a feeling that no matter what you tell him, Damien won't be satisfied with the answer."
                    show chelsea confused
                    pcname "He's my boss. There isn't much to tell."
                    show Damien Angry at left
                    D "There must be {i}something{/i} if he's willing to pay for a boob job, [pcname]."
                    show Damien Blank at left
                    "His words are cold. His eyes flicker over you, suspicious and nervous."
                    "He's jealous, but you can't fathom why."
                    pcname "There's nothing going on between me and Keith, Damien."
                    show Damien Glare at left
                    D "Then why won't you tell me something about him?"
                    show chelsea confused
                    pcname "What do you want to know?"
                    show Damien Sad at left
                    D "{i}Something.{/i} Please, [pcname]."
                    show chelsea blank
                    show Damien Blank at left
                    "You rack your brain, trying to find something to satisfy him."
                    show chelsea confused
                    pcname "He has red hair."
                    show Damien Sad at left
                    "Damien sighs."
                    show Damien Neutral at left
                    D "That's not what I was looking for."
                    show chelsea blank
                    show Damien Blank at left
                    pcname "I don't know what else to tell you, Damien."
                    "Damien sits quietly for a moment."
                    "He reaches for the remote and sighs."
                    show Damien Worry at left
                    D "Let's just watch the movie."
                    show Damien Blank at left
                    "You're grateful that he's decided to drop the topic, but there is an obvious intensity in the air between you."
                    "You lean back against the other side of the couch away from him."
                    pcname "Okay."
                "No." if True:
                    show chelsea shocked
                    "You can't help but feel a little offended at his suggestion. Doesn't he trust your ability to think for yourself?"
                    show chelsea angry
                    show Damien Shocked at left
                    if club == "track":
                        pcname "I'm allowed to make my own decisions with my body."
                    elif club == "cheer":
                        pcname "I can think for myself, you know."
                    elif club == "yearbook":
                        pcname "I-I decided it by myself. I don't always need outside influences..."
                    show Damien Worry at left
                    "Damien seems to realize the error of his suggestion. He shakes his head quickly."
                    show Damien Neutral at left
                    D "That... I'm sorry. That came out wrong."
                    show chelsea blank
                    D "I wasn't trying to suggest that."
                    D "I'm just-"
                    show Damien Glare at left
                    "Damien fumbles with his words, struggling to say the right thing. He takes a deep breath and seems to try to organize his thoughts."
                    show Damien Neutral at left
                    D "I'm trying to say that you're beautiful just the way you are, [pcname]."
                    D "You don't need a surgery like this, and I don't want you thinking that you do."
                    show Damien Blank at left
                    if club == "track":
                        pcname "Well that's my decision, and I'll do what I want."
                    elif club == "cheer":
                        pcname "I don't care. This is {i}my{/i} body and {i}my{/i} choice. I can do whatever I want."
                    elif club == "yearbook":
                        pcname "This... This is {i}my{/i} decision. I'll do what I want with my body."
                    "Frustrated, Damien gestures to your head."
                    show Damien Neutral at left
                    D "Like what you did with your hair?"
                    show chelsea shocked
                    "You feel your jaw drop a little as his words sting you. He had said he was happy with it if you were, didn't he? Why is he taking that back now?"
                    show Damien Glare at left
                    "You see his face twist in regret as he realizes what he's said, but it's too late. You feel an anger rise in your chest."
                    show chelsea angry
                    if club == "track":
                        pcname "Yes! Just like my hair that {i}I{/i} chose for {i}my{/i} body."
                    elif club == "cheer":
                        pcname "What about my hair? What about it, Damien? Is this a fight you really want to start right now?"
                    elif club == "yearbook":
                        pcname "Y-You said you were fine with it!"
                    show Damien Sad at left
                    "Damien sways lightly in place, guilty. He avoids your gaze, focusing on his shoes instead."
                    D "I-I'm really sorry. I shouldn't have said that, [pcname]."
                    show chelsea blank
                    "He bites his lip, trying to think of something to say. You stare at him expectantly, refusing to be the first to break the silence."
                    show Damien Neutral at left
                    D "H-Hey, let's watch the movie now. Is that okay?"
                    if club == "track":
                        "You cross your arms over your chest."
                        pcname "Fine."
                    elif club == "cheer":
                        pcname "Whatever."
                    elif club == "yearbook":
                        pcname "I... I guess..."
                    show Damien Sad at left
                    "Damien carefully sits back down on the couch, curling up in a corner away from you, as though he's afraid to disturb you."
                    show Damien Blank at left
                    "Still hurt and upset, you sit on the opposite side of the couch, leaving plenty of room between the two of you."
            show bg HomeN with dissolve
            "You barely pay attention to the movie, despite how long it is. You feel Damien glancing over toward you, as though willing you to forgive him through his gaze."
            "Still hurt, you continue to stare ahead, not in the mood to engage in further conversation."
            "When the movie ends, it's time for bed. You and Damien engage in an awkward silence as he puts on his shoes and collects his things."
            "Before stepping out, Damien takes your hand in his and gives it a firm squeeze."
            show Damien Neutral at left
            D "Hey, so... I'm sorry. I don't want to fight over this."
            D "But I want you to know that you're beautiful, [pcname]. You don't need to change a thing."
            show Damien Happy at left
            D "I want to be someone you can rely on, so please consider coming to me for help instead, okay?"
            "You aren't sure what to say, but it seems Damien wasn't expecting a response. He gives you a small wave and ducks out of the apartment."
            hide Damien Happy with dissolve
            scene bg black with dissolve
            $ DamienAngry = "Characters/Damien/School Uniform/Angry.png"
            $ DamienBlank = "Characters/Damien/School Uniform/Blank.png"
            $ DamienGlare = "Characters/Damien/School Uniform/Glaring.png"
            $ DamienLaugh = "Characters/Damien/School Uniform/Laughing.png"
            $ DamienNeutral = "Characters/Damien/School Uniform/Neutral.png"
            $ DamienSad = "Characters/Damien/School Uniform/Sad.png"
            $ DamienShocked = "Characters/Damien/School Uniform/Shocked.png"
            $ DamienSmiling = "Characters/Damien/School Uniform/Smiling.png"
            $ DamienWorrying = "Characters/Damien/School Uniform/Worrying.png"
            jump events_end_period
        "No! Of course not." if True:
            show chelsea laugh
            show Damien Happy at left
            "Damien sighs in relief, settling onto the couch beside you. He hangs an arm over your shoulder and pulls you against his side, still troubled."
            D "Why would your coworker give you {i}that?{/i} That's super inappropriate, {i}especially{/i} at work."
            show chelsea blank
            pcname "She's really been encouraging me to get it done."
            show Damien Neutral at left
            D "Seriously? That's even worse. You shouldn't have to put up with that."
            D "Have you talked to your boss about it?"
            show Damien Blank at left
            "You think back to Keith's reaction when he saw the piece of paper himself. He had been more than encouraging about the idea."
            show chelsea embarrassed
            pcname "Keith approves the boob job, actually..."
            show Damien Glare at left
            "Damien tenses beside you. You glance up at him, taking note of the disturbed look he has on his face."
            show Damien Neutral at left
            show chelsea blank
            D "Say, [pcname]..."
            D "You'd tell me if your boss was doing anything else inappropriate at work, right?"
            show Damien Blank at left
            if bakery_eavesdrop == True:
                "You can't help but think of what you witnessed in Keith's office between himself and Lisa."
                "There's no way their sexual acts are appropriate for work."
            elif True:
                if bakeryagree >= 10:
                    "Although Keith can be mean at times, you've found him to be more agreeable as of late. His actions toward you, especially when you first started working there, have been less than appropriate, though..."
                elif True:
                    "You think about all of the mean, hurtful ways Keith has treated you since you started. His behavior towards you definitely hasn't been appropriate for work."
            menu bakery_damienconflict_tellonkeith:
                "Tell Damien about Keith and Lisa." if bakery_eavesdrop == True:
                    show chelsea embarrassed
                    pcname "Well... There was one time..."
                    "Damien watches you intently. You can feel his fingers digging into your shoulder with anxiety."
                    if club == "track":
                        if bakerymakeup == True or bakeryhalfmakeup == True:
                            pcname "I sort of caught Keith and Lisa having sex on his desk."
                        elif True:
                            pcname "I sort of caught Lisa giving him a blowjob in his office."
                    elif club == "cheer":
                        if bakerymakeup == True or bakeryhalfmakeup == True:
                            pcname "I caught Keith fucking Lisa on his desk."
                        elif True:
                            pcname "I saw Lisa sucking his dick in his office."
                    elif club == "yearbook":
                        "You feel your face heat up at the memory. Even thinking about it embarrasses you..."
                        if bakerymakeup == True or bakeryhalfmakeup == True:
                            pcname "K-Keith and Lisa... T-they were... naked on the desk... and..."
                        elif True:
                            pcname "L-Lisa was on her knees... With his... in her mouth..."
                    show Damien Shocked at left
                    "Damien's gapes at you."
                    D "They- They {i}what?{/i}"
                    show Damien Angry at left
                    D "[pcname], that's not okay! That's not even {i}remotely{/i} okay!"
                    show Damien Glare at left
                    "Damien jumps to his feet and paces in front of your couch in a panic."
                    show chelsea shocked
                    "The sight surprises you. Usually Damien is so relaxed and shy."
                    "You realize you've never actually seen him upset about anything before."
                    show chelsea blank
                    show Damien Angry at left
                    D "You need to quit! Or we need to call the police, or the health department, or something!"
                    D "This is totally unacceptable!"
                    "You watch him pace in a frenzy. While you understand why he's so upset, you still need a job. You have bills to pay, after all."
                    if club == "track":
                        pcname "Damien... It's okay. Sit down. It doesn't matter."
                    elif club == "cheer":
                        pcname "It's not that big of a deal, Damien. Come sit down."
                    elif club == "yearbook":
                        pcname "D-Damien... It's okay... Please sit down..."
                    D "How are you so relaxed right now? Your boss is a total pervert!"
                    D "Has he done anything like this to you, [pcname]?"
                    show chelsea shocked
                    pcname "No! Of course not."
                    show chelsea blank
                    "Damien runs a hand through his hair. His voice softens with his confusion."
                    D "Why aren't you upset about this?"
                    pcname "I {i}am{/i} upset. But it isn't that simple..."
                    pcname "I still need to work. I have bills and rent to pay."
                    pcname "And I really don't want to cause a big scene at my job."
                    pcname "You understand that, don't you?"
                    show Damien Glare at left
                    "Damien sighs, shaking his head. He resumes his seat beside you, stretching out across the couch and pulling you into a cuddling position against his chest."
                    show Damien Blank at left
                    "You relax in his embrace, enjoying his warmth. His fingers lightly play with your hair."
                    show Damien Neutral at left
                    D "I'm going to figure something out, [pcname]. You don't have to worry."
                    show Damien Blank at left
                    "You strain your neck to look up at him."
                    show chelsea confused
                    pcname "What do you mean by that?"
                    show chelsea blank
                    "He shrugs."
                    show Damien Happy at left
                    D "Dunno. Gotta figure it out first."
                    "Damien gives you one of his shy smiles. It's a sweet gesture, although you find yourself worrying about what he's planning."
                    "He reaches past you for the remote and starts up the movie."
                    $ telldamien = True
                "Tell Damien about Keith's insults." if True:
                    if bakery_eavesdrop == True:
                        "You briefly consider telling Damien about what you saw in Keith's office but quickly shake the thought away."
                        "Damien has already expressed his discomfort about Keith. You don't want to give him any more reasons to hate your boss."
                    elif True:
                        "While you can't think of anything drastic, Keith's behavior definitely hasn't been appropriate."
                    if club == "track":
                        if bakeryagree >= 10:
                            pcname "Well, he talks down to me a lot, but that's basically everyone in food service, right?"
                            show Damien Glare at left
                            D "That still doesn't give him a right to treat you badly."
                        elif True:
                            "You grit your teeth as memories of all the rude things he's said to you comes to the forefront of your mind."
                            pcname "He's a dick. He's always talking down to me and shit."
                    elif club == "cheer":
                        if bakeryagree >= 10:
                            "Although Keith has certainly had his fair share of bad moments, you don't see it as enough to warrant getting Damien worked up too much."
                            pcname "He has trouble controlling his temper, but he's not that bad. You just need to, like, suck up to him and he's fine to deal with."
                        elif True:
                            "You're unable to contain the sour look on your face as you think of some of the things Keith has said to you."
                            pcname "He's a God-awful prick. He's always berating me. Sometimes in front of customers."
                            show Damien Neutral at left
                            D "That's awful, [pcname]."
                    elif club == "yearbook":
                        if bakeryagree >= 10:
                            "You try not to show Damien how much the mean things Keith has said to you hurts. It would only worry him further."
                            pcname "H-He's... he's mean to me, but he's not that bad... It's my fault..."
                            show Damien Glare at left
                            D "I doubt that, [pcname]."
                        elif True:
                            show chelsea sad
                            "You feel your eyes water a little as you think of all the horrible things Keith has said to you."
                            pcname "H-He's... {i}awful{/i}, Damien..."
                    show Damien Neutral at left
                    D "What kind of stuff does he say to you?"
                    show chelsea sad
                    if club == "track":
                        if bakeryagree >= 10:
                            pcname "Sometimes he calls me stupid or points out things wrong with my body. He's a dick, but who isn't?"
                        elif True:
                            pcname "He's always calling me stupid and pointing out my flaws. He acts like he's so much better than me. Tch."
                            pcname "I don't even want to get started on the crap he says about my body."
                    elif club == "cheer":
                        if bakeryagree >= 10:
                            pcname "He just, like, points out things when he's upset. It's not an all the time thing."
                            show Damien Neutral at left
                            D "But what is he {i}saying{/i} to you?"
                            pcname "Just, like, stuff about me being stupid, or he'll say something about my body or whatever. It's whatever."
                        elif True:
                            pcname "He yells at me for every little thing. He's always finding reasons to berate me, whether it's my brains or my looks... It's exhausting."
                    elif club == "yearbook":
                        if bakeryagree >= 10:
                            show chelsea embarrassed
                            "You stare down at your lap and try to distract your nervous hands with a loose thread on your shirt. You don't want Damien to be too upset..."
                            pcname "W-Well, he, um, sometimes... calls me dumb... But it's only when I do something really dumb! A-And same with my looks... It's really my fault..."
                            D "It's not your fault at {i}all{/i}, [pcname]."
                        elif True:
                            show chelsea embarrassed
                            "Even though you try to hold it in, you can feel a couple of tears spill over your cheeks. You quickly wipe them away, embarrassed."
                            pcname "H-He calls me stupid a lot. A-And he talks about my looks and... and..."
                    show Damien Angry at left
                    D "He calls you {i}stupid?{/i} And talks about your {i}body?{/i}"
                    D "How can he treat his own employee so horribly? This is harassment! Sexual harassment!"
                    D "You should quit. You should definitely quit."
                    show chelsea blank
                    "Damien paces in front of the couch, hunched over in thought."
                    "While you understand why he's so upset, you still need a job. You have bills to pay, after all."
                    if club == "track":
                        pcname "Damien, it's fine. Sit down. It doesn't matter."
                    elif club == "cheer":
                        pcname "It's whatever, Damien. It's not that big of a deal. Come sit down."
                    elif club == "yearbook":
                        show chelsea sad
                        pcname "D-Damien... It's okay... Please sit down..."
                    D "How are you so relaxed right now? Your boss is a total asshole!"
                    if club == "track":
                        pcname "Yeah, no shit."
                    elif club == "cheer":
                        pcname "Uh, no duh."
                    elif club == "yearbook":
                        pcname "Y-Yes, but..."
                    "Damien runs a hand through his hair. His voice softens with his confusion."
                    show Damien Glare at left
                    show chelsea blank
                    D "Why aren't you upset about this?"
                    pcname "I {i}am{/i} upset. But it isn't that simple..."
                    pcname "I still need to work. I have bills and rent to pay."
                    pcname "And I really don't want to cause a big scene at my job."
                    pcname "You understand that, don't you?"
                    show Damien Blank at left
                    "Damien sighs, shaking his head. He resumes his seat beside you, stretching out across the couch and pulling you into a cuddling position against his chest."
                    "You relax in his embrace, enjoying his warmth. His fingers lightly play with your hair."
                    show Damien Neutral at left
                    D "I want to help you take care of this. Maybe we'll go talk to him together, so you won't have to be alone."
                    show Damien Blank at left
                    "You strain your neck to look up at him."
                    show chelsea sad
                    pcname "I don't want to do anything, Damien. I just want to let it go."
                    show Damien Glare at left
                    D "He's treating you horribly, [pcname]. It's only going to get worse."
                    show Damien Neutral at left
                    D "Please let me help you. I'll think of something won't embarrass you."
                    show Damien Happy at left
                    show chelsea blank
                    "Damien gives you one of his shy smiles. It's a sweet gesture, although you find yourself worrying about what he's planning."
                    "You sigh but say nothing."
                    "He reaches past you for the remote and starts up the movie."
            show chelsea happy
            "The movie is a lot longer than you thought it would be. By the time it ends, it's time for you to go to bed."
            "As you walk Damien to the front door, he gives your hand a gentle squeeze and kisses your cheek."
            "You smile, ready to part, but Damien pulls you into his arms. His lips press against yours, clumsy and inexperienced, but just as warm and sweet as you know he can be."
            "He holds you against him as he deepens the kiss, his tongue pushing past your lips and exploring the inside of your mouth."
            "You eagerly reciprocate, pressing your breasts against his chest."
            "You tangle your fingers in his brown hair as his hands settle on your hips, stroking soft circles with his thumbs."
            "You grip his hair, eliciting a small sound from the back of his throat. He moans in your mouth and one hand tangles itself in your hair."
            "Damien pulls away too soon. You're left breathless and a little disappointed. Your fingers twitch, desperate to have his mouth on yours again."
            "Damien presses his forehead against yours gently, his voice soft and low."
            D "I like you a lot, [pcname]."
            D "You are beautiful just the way you are."
            "He cups your face between his hands, his thumb stroking along your cheek."
            D "I want to be someone you can rely on."
            "He lifts his chin a little, pressing a soft kiss to your forehead before pulling away."
            D "So let me take care of you, okay?"
            "Damien pulls his shoes back on and gives you a little wave goodbye, stepping outside."
            hide Damien Happy with dissolve
            "As you begin to clean up your living room and get ready for bed, you think about Damien's insistence to help your situation at work."
            menu bakery_damienconflict_helping:
                "You like Damien's help." if True:
                    "While you don't want to cause a scene at work, you can't help but feel touched at Damien's worry over you."
                    "He really does care about you and is willing to go out of his way to make sure you aren't burdened in a stressful work environment."
                    "The thought is so sweet. You smile to yourself as you climb into bed, allowing thoughts of Damien to put you to sleep."
                    $ damienlove +=1
                "You dislike Damien's help." if True:
                    show chelsea blank
                    "While you appreciate Damien's worry for you, the more you think about it, the more annoyed you become at his insistence on helping you."
                    "You had made it clear that you really don't want to start anything at work and no matter how good his intentions are, he should respect that."
                    "You sigh and crawl into bed, trying to push thoughts of Damien out of your mind as you go to sleep."
                    $ damienlove -=1
            scene bg black with dissolve
            $ DamienAngry = "Characters/Damien/School Uniform/Angry.png"
            $ DamienBlank = "Characters/Damien/School Uniform/Blank.png"
            $ DamienGlare = "Characters/Damien/School Uniform/Glaring.png"
            $ DamienLaugh = "Characters/Damien/School Uniform/Laughing.png"
            $ DamienNeutral = "Characters/Damien/School Uniform/Neutral.png"
            $ DamienSad = "Characters/Damien/School Uniform/Sad.png"
            $ DamienShocked = "Characters/Damien/School Uniform/Shocked.png"
            $ DamienSmiling = "Characters/Damien/School Uniform/Smiling.png"
            $ DamienWorrying = "Characters/Damien/School Uniform/Worrying.png"
            show bg black with dissolve
            $ acts-= 1
            jump bed2

label bakery_damienconflict3:
    $ DamienAngry = "Characters/Damien/Casual/Angry.png"
    $ DamienBlank = "Characters/Damien/Casual/Blank.png"
    $ DamienGlare = "Characters/Damien/Casual/Glaring.png"
    $ DamienLaugh = "Characters/Damien/Casual/Laughing.png"
    $ DamienNeutral = "Characters/Damien/Casual/Neutral.png"
    $ DamienSad = "Characters/Damien/Casual/Sad.png"
    $ DamienShocked = "Characters/Damien/Casual/Shocked.png"
    $ DamienSmiling = "Characters/Damien/Casual/Smiling.png"
    $ DamienWorrying = "Characters/Damien/Casual/Worrying.png"
    show chelsea at right with moveinright
    "It's still early into your shift when Keith steps out of his office to begin counting the inventory."
    "As he marks items off on his clipboard, he glances at you behind the counter."
    show Keith Neutral at left with moveinleft
    BM "Ah, [pcname]. Have you taken a look at that paper Lisa gave you yet?"
    show Keith Blank at left
    "You think back to your discussion with Damien when he saw the sheet."
    menu bakery_damienconflict_sheet:
        "Yeah, I had a look at it." if True:
            show chelsea happy
            show Keith Neutral at left
            BM "That's good. Don't forget about my offer."
            BM "I'd be happy to help you out with the money if you need it."
        "No, I haven't had a chance to yet." if True:
            show Keith Confused at left
            BM "Tch. What else have you been wasting your time on instead?"
            show Keith Neutral at left
            BM "You should make time to look it over. It should be a priority."
    "Before you can respond, the front door bell jingles."
    show chelsea happy
    "You turn with a smile, prepared to greet your new customer."
    show Keith Blank at center with move
    show Damien Happy at left with moveinleft
    show chelsea shocked
    "You're surprised to see Damien instead with a bouquet of flowers in his hands. He smiles nervously as he approaches the counter."
    show chelsea happy
    D "Hey. Surprise."
    "Damien's smile falters as he glances up at Keith."
    "Keith doesn't seem to notice him, focusing on counting the inventory."
    show chelsea embarrassed
    pcname "Damien..."
    "Keith looks up, glancing between you and Damien."
    show Keith Neutral
    BM "You know him?"
    show Keith Blank
    show chelsea happy
    pcname "Yeah. This is Damien, my boyfriend."
    "You gesture toward Damien. Keith is unimpressed."
    pcname "Damien, this is my manager, Keith."
    D "Hello."
    show Damien Blank at left
    "Damien's greeting doesn't sound friendly at all. He squares his shoulders, but even so he still looks scrawny."
    "Keith doesn't spare him a second glance. He turns to you, irritated."
    show Keith Angry
    BM "You're supposed to be working, [pcname]. This isn't some hangout for you and your boyfriend."
    menu bakery_damienconflict_shift:
        "Defend yourself." if True:
            show chelsea angry
            pcname "I didn't know he would be coming in here-"
            BM "Don't try to give me excuses! Do you see Lisa's friends coming to hang out in here?"
            BM "No. It's because they know she's at {i}work.{/i}"
        "Accept his lecture." if True:
            show chelsea sad
            pcname "I understand, sir."
            pcname "It won't happen again."
            BM "It better not. I'm paying you to work, not waste time with your friends."
    show Damien Angry at left
    D "Hey. You can't talk to her like that."
    show Keith Confused
    show chelsea shocked
    "Damien glares up at Keith, the bouquet of flowers clutched in his hands."
    "You know how shy Damien is naturally, so seeing him stand up to someone, especially a person of authority, surprises you."
    show chelsea blank
    "Damien seems surprised by his own courage as well. You can see his body shaking slightly, but he puts on a brave face."
    BM "She's {i}my{/i} employee, and while she's on the clock, I'll reprimand her whenever I need to."
    show Keith Angry
    BM "{i}You{/i} shouldn't be here. I'm trying to run a business."
    if telldamien == True:
        show Damien Glare at left
        D "A pretty shady business if you ask me."
        show Keith Confused
        BM "Excuse me? What's that supposed to mean?"
        show Keith Blank
        "Keith steps in front of Damien. Even though Damien isn't that much shorter, it still feels as though Keith is towering over him."
        "Damien shrinks back a little, but tries to hold his ground."
    D "I know all about the crap that goes on here."
    D "You can't treat your employees like this. It's unacceptable."
    D "You're lucky I haven't reported you."
    "Damien's attempts to intimidate Keith fall short. Keith lets out a mocking laugh."
    show Keith Laugh
    BM "Report me? For {i}what{/i}, kid?"
    show Keith Angry
    BM "Stop trying to be a white knight and get out of here before I force you out. You're trespassing on {i}my{/i} property."
    show Damien Glare at left
    show Keith Blank
    menu bakery_damienconflict_routelock:
        "Defend Damien." if True:
            show chelsea sad
            "You can't help but feel sorry for Damien as Keith talks down to him."
            show chelsea blank
            "After all, Damien was only trying to defend you."
            show Damien Shocked at left
            if club == "track":
                show chelsea angry
                pcname "Don't talk to him like that, Keith. He's just worried about me."
            elif club == "cheer":
                show chelsea angry
                pcname "Leave him alone, Keith. He hasn't done anything wrong."
            elif club == "yearbook":
                pcname "Keith... Leave him alone, please."
            show Damien Happy at left
            "Keith rounds on you, his eyes narrowed."
            show Damien Angry at left
            show Keith Angry
            BM "Don't you tell me what to do!"
            if club == "track":
                pcname "I'm just saying. He isn't going to do anything."
                pcname "If you were nicer, this wouldn't be a problem in the first place."
            elif club == "cheer":
                pcname "Well maybe if you treated us a little better, this wouldn't be an issue..."
            elif club == "yearbook":
                show chelsea angry
                pcname "Y-You should be nicer to us. That's the only reason he's upset..."
            BM "So you don't think I'm 'nice'?"
            BM "I don't have to be {i}nice!{/i} I'm your {i}boss!{/i}"
            if club == "track":
                "You feel your teeth grind together as you try to hold in your frustration."
                pcname "Yeah, I get that, but you don't have to scream at him for it."
                pcname "The only reason he's pissed in the first place is because he feels like you're harassing me."
            elif club == "cheer":
                "You have to refrain from rolling your eyes."
                pcname "Well, {i}duh{/i}. But give the kid a break."
                pcname "He's only upset because he feels like you're harassing me."
            elif club == "yearbook":
                "You flinch at his harsh tone. It's difficult for you to summon the courage to stand up to him."
                pcname "I-I understand, but Damien's only upset b-because he feels... feels like you've been..."
                show Damien Glare at left
                D "Harassing her."
            BM "{i}Harassing you?{/i} Where the fuck is that coming from?"
            if club == "track":
                pcname "Do you hear yourself? You're yelling at me right now!"
                pcname "And I mean, Damien's kinda got a point. Your comments on my body are a little weird."
            elif club == "cheer":
                "You let out a frustrated sigh."
                pcname "Well, you {i}do{/i} yell at me a lot."
                pcname "And I guess your comments on my boobs aren't totally appropriate either..."
            elif club == "yearbook":
                show chelsea sad
                pcname "W-Well... Y-You get upset a lot... and swear at me..."
                "You bite your lip and look down, unable to meet his furious gaze."
                pcname "A-And m-maybe you s-shouldn't t-talk about my... my body..."
            BM "Then maybe you shouldn't bring your goddamn personal life into work!"
            BM "I've done nothing but try to help your ass-"
            show Damien Angry at left
            D "By encouraging her to get {i}breast implants?{/i}"
            D "That's sexual harassment!"
            if club == "track":
                show chelsea angry
                pcname "Hey! Stop fighting!"
                pcname "God, can we just forget about the implants? I don't even want them anymore!"
            elif club == "cheer":
                show chelsea blank
                pcname "Can we stop yelling at each other already?"
                pcname "Like, if it's going to be such a big deal, I don't even want them."
            elif club == "yearbook":
                show chelsea sad
                pcname "P-Please stop fighting!"
                pcname "I-I don't want them anymore. So please stop fighting..."
            BM "What?"
            BM "You're backing out because you'd rather listen to this little shit?"
            show chelsea angry
            if club == "track":
                pcname "I'm backing out because it's causing more trouble than it's worth."
                pcname "I can be just as feminine without inflated tits."
            elif club == "cheer":
                pcname "Uh, yeah."
                pcname "I mean, what's the use if my boyfriend isn't even gonna like them? It'd be a waste."
            elif club == "yearbook":
                pcname "H-He's not... that!"
                pcname "He's my boyfriend, a-and... it's not worth fighting..."
            show Keith Confused
            show Damien Glare at left
            BM "Alright. Then you can follow your boyfriend on his way out."
            show Keith Blank at left
            "Your heart drops."
            show chelsea shocked
            pcname "W-What?"
            show Keith Angry
            BM "Boyfriend, you're banned for life. I better not see you around my bakery again."
            BM "As for you, [pcname]..."
            BM "Get out. I don't want to see you 'till your next shift, got it?"
            "You stand there gaping at him. While you're relieved he's not firing you, you still can't contain the anxiety that spreads through your chest."
            show chelsea sad
            pcname "But- Keith-"
            "He points toward the front door."
            BM "{i}Out.{/i}"
            BM "You better thank Lisa. She's gonna have to stay late to cover your ass."
            hide Keith Angry with dissolve
            hide chelsea with dissolve
            hide Damien Glare with dissolve
            "Ashamed, you shakily step out from behind the counter and follow Damien out onto the sidewalk. You still aren't entirely convinced he won't fire you later."
            scene bg black with dissolve
            pause 0.5
            show bg CityE with dissolve
            show Damien Happy at midright
            show chelsea shocked
            "Damien pulls you into his arms and hugs you for a long time."
            show chelsea sad
            D "It's... It's going to be okay, [pcname]."
            D "Thank you for standing up for me. More than once now, I guess."
            show chelsea happy
            "He lets out a nervous laugh. You give him a small smile."
            "Damien leans forward and presses his lips against yours. You close your eyes, enjoying the softness of his lips."
            "Even if things at the bakery go south, it's nice to know you can rely on Damien."
            scene bg black with dissolve
            $ bakeryboobjobapprove = False
            $ DamienAngry = "Characters/Damien/School Uniform/Angry.png"
            $ DamienBlank = "Characters/Damien/School Uniform/Blank.png"
            $ DamienGlare = "Characters/Damien/School Uniform/Glaring.png"
            $ DamienLaugh = "Characters/Damien/School Uniform/Laughing.png"
            $ DamienNeutral = "Characters/Damien/School Uniform/Neutral.png"
            $ DamienSad = "Characters/Damien/School Uniform/Sad.png"
            $ DamienShocked = "Characters/Damien/School Uniform/Shocked.png"
            $ DamienSmiling = "Characters/Damien/School Uniform/Smiling.png"
            $ DamienWorrying = "Characters/Damien/School Uniform/Worrying.png"
            jump events_end_period
        "Defend Keith." if True:
            show Damien Blank at left
            "Damien looks to you, as though expecting you to rush in and agree with him. His face falls when he realizes you aren't."
            show Damien Sad at left
            D "[pcname]-"
            show chelsea sad
            pcname "You should go home, Damien."
            show Keith Blank
            show Damien Shocked at left
            "He stares at you, trying to process what you've said to him. You stare back at him, waiting for him to leave."
            show Damien Sad at left
            D "[pcname], come on. You can't seriously be okay with putting up with this."
            show Damien Neutral at left
            D "No one has any right to disrespect you like that."
            show Keith Happy
            show chelsea angry
            pcname "You don't have any right to come in here and make a scene while I'm working."
            show Damien Glare at left
            show chelsea blank
            D "I wasn't trying to make a scene! I just..."
            "Damien glances between you and Keith. Keith doesn't bother to hide the smug grin on his face."
            show Damien Sad at left
            "When he seems to realize that you will not support him, Damien drops the bouquet of flowers on the ground."
            "He shoves his hands in his pockets and ducks his head, his face red with shame and embarrassment."
            show chelsea sad
            pcname "Damien-"
            "He holds up a hand to stop you."
            D "I get it. I'm leaving."
            D "I'm not really interested in keeping up this relationship anyway. Let's just make things easy and break it off."
            D "Good luck, [pcname]."
            hide Damien Sad with dissolve
            "His gaze drifts between you and Keith one last time before he walks dejectedly out of the bakery."
            "Keith pats your shoulder. The contact startles you."
            BM "Better off without a nerd like that, [pcname]. They'll only drag you down."
            BM "Wait until you get yourself a real man. It's a world changer."
            "You watch as Keith finishes counting the inventory and retreats back into his office."
            show chelsea sad
            "Even though he didn't say much, you take comfort in Keith's words."
            scene bg black with dissolve
            $ bakeryboobjobapprove = True
            jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
