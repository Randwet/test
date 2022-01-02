label bully_gangbang:
    "Homeroom is as lively as ever today."
    "As soon as you sit down, though, a low, breathy voice sends a chill down your spine."
    show Matt Smirk at left with moveinleft
    m "Meet me back here after school."
    "Matt sinks into his chair behind you without waiting for your answer."
    hide Matt Smirk with moveoutleft
    if defymatt:
        "A cold chill sweeps over you, settling in your stomach."
    "Though you try to pay attention for the rest of the day, you can't help wondering what Matt has planned."
    "When the last bell rings, you put your belongings in your locker and mull over what to do next."
    show chelsea at right with moveinright
    show bg ClassroomE with dissolve
    menu gangbang_meetmatt:
        "Go home." if True:
            if defymatt:
                "Despite his threats, you can't bring yourself to follow his orders anymore."
                jump events_end_period
                $ mattblackmail = 2
            elif True:
                $ defymatt = True
                "Something about the situation makes you nervous."
                "With a glance back toward the classroom, you walk toward the exit."
                m "Where do you think you're going?"
                "You turn back to see Matt walking toward you."
                m "You don't want to do that..."
                "He leans in close to you, whispering:"
                m "I have some {i}very{/i} nice pictures of you."
                m "And the whole school will see them if you don't follow me."
                "He doesn't wait for your response, leaving you staring after him in the hallway."
                menu gangbang_meetmatt2:
                    "Follow him." if True:
                        "Despite your misgivings, you have no choice; with leaden feet, you slowly make your way to the classroom door."
                    "Leave anyway." if True:
                        "Despite his threats, you can't bring yourself to follow him."
                        "Turning around, you leave the school as fast as you can."
                        $ mattblackmail = 2
                        jump events_end_period
        "Meet Matt." if True:
            "Your heart thumps as you walk back to the classroom."
    "Ducking inside, you take a deep breath and look for Matt."
    "He stands at the front of the room, near the desk."
    show Matt Pleased at left with moveinleft
    m "There's my little slut."
    m "You've been a naughty girl, haven't you?"
    if defymatt:
        if club == "track":
            pcname "Only when you {i}make{/i} me!"
        elif club == "cheer":
            pcname "What do you want, Matt?"
        elif club == "yearbook":
            "You look away, remembering the last time you were with him."
    elif True:
        show chelsea embarrassed
        if club == "track":
            pcname "What?"
        elif club == "cheer":
            pcname "Oh, have I?"
        elif club == "yearbook":
            pcname "N-no?"
    show Matt Blank at left
    m "I think you've already met my friend?"
    "He motions behind you."
    show Alex Happy with dissolve
    "Heart pounding, you turn to see the tall boy from the other day. The one you confronted when he was bullying Damien."
    "Walking toward you, he makes a point of raking his eyes down your body."
    show Matt Smirk at left
    m "This is Alex. I think you owe him an apology?"
    "You're pretty sure you know what kind of \"apology\" Matt has in mind."
    menu gangbang_apology:
        "Apologize." if True:
            $ corruption += 1
            show chelsea blank
            pcname "I'm sorry, Alex. I shouldn't have stepped in..."
            "You bow your head in his direction."
            pcname "Please forgive me?"
        "Protest." if True:
            show chelsea angry
            pcname "I don't have anything to apologize for!"
            "Matt frowns at your refusal."
            show Matt Angry at left
            m "I don't think you get it. You embarrassed my friend."
            m "If you want to stay on my good side, you need to apologize."
            show chelsea blank
            menu gangbang_apology2:
                "Give in." if True:
                    show chelsea embarrassed
                    pcname "I-I'm sorry, I--"
                    "You turn toward Alex."
                    pcname "I'm sorry for embarrassing you! I didn't mean to--"
                "Stand your ground." if True:
                    show chelsea angry
                    if defymatt:
                        "You know what's at stake, but you don't care."
                        $ mattblackmail = 2
                        if club == "track":
                            "Blood boiling, you ignore Matt's veiled threat."
                            pcname "You can't be serious! I would never apologize to someone like him!"
                            "Spinning on your heel, you storm out of the classroom."
                        elif club == "cheer":
                            "Annoyed, you shake your head."
                            pcname "Please, I'm not apologizing to {i}that{/i}!"
                            "Spinning on your heel, you flip your hair back and saunter out of the classroom."
                        elif club == "yearbook":
                            "Shaking your head, you try to protest."
                            pcname "I-- I can't--"
                            "Spinning on your heel, you flee the classroom."
                        jump events_end_period
                    elif True:
                        $ defymatt = True
                        $ mattblackmail = 1
                        if club == "track":
                            "Blood boiling, you ignore Matt's veiled threat."
                            pcname "You can't be serious! I would never apologize to someone like him!"
                            "Spinning on your heel, you try to leave, but Matt's words stop you dead in your tracks."
                        elif club == "cheer":
                            "Annoyed, you shake your head."
                            pcname "Please, I'm not apologizing to {i}that{/i}!"
                            "Spinning on your heel, you flip your hair back and saunter away."
                            "Unfortunately, Matt's next words stop you."
                        elif club == "yearbook":
                            "Shaking your head, you try to protest."
                            pcname "I-- I can't--"
                            "Spinning on your heel, you try to leave, but Matt's next words stop you."
                        m "So you don't care if everyone sees these pictures of you?"
                        if blackmailpics == "panties":
                            "He holds up his phone; there's a picture of you holding up your skirt in the men's room."
                        elif blackmailpics == "masturbate":
                            "He holds up his phone; there's a picture of you masturbating in the men's locker room."
                        pcname "You... You wouldn't..."
                        m "I will, unless you get back over here and apologize."
                        menu gangbang_apology3:
                            "Apologize." if True:
                                show chelsea embarrassed
                                "You feel numb, as if someone else is speaking through you."
                                pcname "I'm sorry."
                                "You turn toward Alex."
                                pcname "I'm sorry for embarrassing you. I didn't mean to."
                            "Refuse again." if True:
                                "You know what's at stake, but you don't care."
                                $ mattblackmail = 2
                                if club == "track":
                                    pcname "Fuck off!"
                                    "Despite his threats, you storm out of the classroom."
                                elif club == "cheer":
                                    pcname "You're crazy if you think I'm giving in to {i}you{/i}."
                                    "With more confidence than you feel, you walk away."
                                elif club == "yearbook":
                                    "Shaking your head, you back away from him."
                                    pcname "I-- I still can't--"
                                    "You ignore his threats; you're more afraid of what they have planned {i}now{/i}."
                                    "Fleeing the classroom, you run most of the way home."
                                jump events_end_period
    show Matt Smirk at left
    "Matt grins."
    show Alex Neutral
    "Alex" "I don't think she really means it, Matt."
    show Alex Happy
    show Matt Blank at left
    m "Hmmm. Maybe you're right."
    show chelsea shocked
    pcname "No, I--"
    show Matt Angry at left
    m "Shut up and take off your jacket. Tie too."
    "Your fingers tremble as you unbutton your jacket and loosen your tie."
    "Dropping them both to the side, you wrap your arms around your almost-bare body."
    "Matt doesn't seem impressed."
    show Matt Pleased at left
    m "Get into position."
    hide chelsea
    hide Matt Pleased
    scene bg MApt11 with dissolve
    "You drop to your knees, falling into the same position he had you in before: knees spread and hands behind your head."
    "Alex" "Shit, you weren't kidding..."
    m "She does whatever I tell her. Don't you, slut?"
    menu gangbang_slutresponse:
        "Agree." if True:
            if club == "track":
                "It takes you a moment to push down your pride so that you can respond appropriately."
            elif club == "cheer":
                "A thrill of anticipation runs down your spine."
            elif club == "yearbook":
                "Squeezing your eyes shut, you force out a response."
            pcname "Y-Yes."
        "Stay silent." if True:
            "Staring down at the floor, you stay silent."
            m "Speak when I ask a question!"
            if club == "track":
                pcname "Yes!"
            elif club == "cheer":
                pcname "Yes..."
            elif club == "yearbook":
                "You wince."
                pcname "Y-yes..."
    "They laugh. Matt slowly crosses the room."
    "When he reaches the door, you hear the {i}click{/i} as he locks it - then a rustling sound as he pulls down the blinds."
    m "Now we won't be interrupted."
    "You hear his footsteps drawing closer as he walks back to the front of the room."
    m "So why don't you show Alex just how sorry you are?"
    pcname "H-How?"
    "Matt reaches down and grabs the front of your shirt."
    "His fingers make short work of the buttons, leaving your breasts exposed."
    show bg MApt12
    "You gasp as he grabs one, pulling it from your bra and squeezing hard."
    "As he gives you his next instruction, Matt moves on to the other one."
    m "Start with your mouth."
    "Alex steps closer, already unzipping his pants."
    if defymatt:
        "You stare up at him, half-frozen with shock."
    elif club == "track":
        "Taking a deep breath, you mentally prepare yourself."
    elif club == "cheer":
        "You lick your lips in anticipation."
    elif club == "yearbook":
        "You gasp again, shaking your head slowly."
    "He grins down at you as he frees his cock; he's only half hard, but it's already quite thick."
    "Matt releases you and steps back."
    m "Stroke him until he's hard."
    show bg MApt13
    if defymatt:
        "Hesitantly, you take his cock into your hand."
        "You feel its heat as you pump it slowly, almost mechanically."
    elif True:
        "Obediently, you take his cock into your hand - then use your wrist to maintain a slow, almost teasing rhythm."
    "Alex" "Fuck..."
    "His shaft pulses in your hand, growing larger and harder by the second."
    if defymatt:
        "To your shame, you feel a familiar warmth between your thighs."
    elif club == "track":
        "Despite yourself, there's a growing wetness between your thighs."
    elif club == "cheer":
        "The heavy weight of his cock feels just right in your hand."
    elif club == "yearbook":
        "You can barely believe what's happening. And yet..."
    if defymatt:
        "You know what's coming next, and you can't help but imagine your lips stretching around his girth."
    elif True:
        "You lick your lips, imagining what it will feel like to have them stretched around his girth."
    "Alex" "Just suck it already!"
    m "You heard the man."
    show bg MApt14
    "Shifting positions, you press your lips to the head of his cock, circling with your tongue to lubricate it."
    "Then you open your lips wide and slowly take him in."
    show bg MApt15
    m "You can do better than that, can't you?"
    "The corners of your mouth ache as you force more of him past your lips."
    "Slowly, you move your head back and forth, working a little more of him in each time."
    m "There you go; that's my little slut."
    if defymatt:
        "You glare up at Matt."
        if club == "track":
            pcname "And yet... Despite the situation, you can't help but be a little proud of your performance."
        elif club == "cheer":
            pcname "You're surprised to realize that you {i}like{/i} the praise, even if you hate {i}him{/i}."
        elif club == "yearbook":
            pcname "His praise warms you, despite your situation. Which almost makes it worse."
        m "Well? Keep going."
    elif True:
        "Matt's praise is all the encouragement you need to push yourself further."
        if club == "track":
            "While you hate being called a slut, you can't help but be proud of your performance."
        elif club == "cheer":
            "You barely hear him; all of your attention is focused on the cock in your mouth."
        elif club == "yearbook":
            "You can't help but be pleased by his approval, despite the humiliating things he says."
    "Fighting back your gag reflex, you stuff Alex's cock further into your mouth, tasting his salty precum on the back of your tongue."
    m "Make a little more noise so we know how much you're enjoying it."
    if defymatt:
        "You want to scream that he's making you do this, but there's a large cock in your mouth."
    pcname "Mmnf~"
    "You bob your head a little faster, letting the wet slurping sounds fill the room."
    "Alex" "Oh shit..."
    "Your jaw already aches, but you try to ignore it; instead, you focus on his thick cock pulsing against your tongue."
    m "Is that really all you can take?"
    if corruption > 10 and defymatt == False:
        "Eager to please Matt, you go until Alex's dick presses against the back of your throat."
        "Tears well in your eyes as you struggle not to gag."
        "Alex" "Fuck she's good..."
    elif corruption > 15 and defymatt == True:
        "Glaring up at Matt, you press your mouth further down Alex's dick, until it presses against the back of your throat."
        "Tears well in your eyes as you struggle not to gag."
        "Alex" "Fuck she's good..."
    elif True:
        "You try to take more of his dick in your mouth, but it's just too much."
        m "I guess you're not as good as I thought you'd be."
    m "That's enough of a warm up."
    "Pulling your head back, you release Alex's cock with a wet {i}pop{/i}."
    "Alex runs his hands through his hair, breathing hard."
    hide bg MApt14
    show bg ClassroomE with dissolve
    show Matt Smirk at left with moveinleft
    m "Get undressed."
    "Wiping saliva and precum from your chin, you pull yourself to your feet and quickly shed your uniform."
    $ clothes = 'underwear'
    if defymatt:
        m "All of it."
    if club == "track":
        "Glancing around the room, you slip off your panties and bra."
        "You know there's nobody else there, but you still feel really exposed."
    elif club == "cheer":
        "Lifting your chin, you slip out of your panties and bra, dropping them casually to the floor."
        "It's actually kind of exciting being naked in a classroom."
    elif club == "yearbook":
        "Your cheeks burn and you glance around the classroom as you remove your bra and panties."
        "Though you know there's nobody but the three of you, you can't help but feel particularly exposed here."
    show chelsea embarrassed
    $ clothes = 'naked'
    show chelsea at right with moveinright
    show Matt Pleased at left
    m "Alright, slut. Come over here."
    "He motions to the teacher's desk."
    "Hesitantly, you approach and wait for further instructions."
    m "Lay on your back and spread your legs. Alex wants to make sure you're {i}really{/i} sorry."
    if defymatt:
        pcname "I..."
        m "Hurry up!"
    "Your heart pounds as you lift yourself up and lay across the cool surface."
    "With one foot on each corner of the desk, you let your legs fall open."
    hide chelsea with dissolve
    scene bg MApt21 with dissolve
    "Alex" "Guess she really is a natural redhead, huh?"
    "He strokes your mound, running his fingers down your slit and pressing one inside of you."
    "The suddenness of his intrusion forces a gasp from you."
    "Alex" "Like that, bitch?"
    m "She likes whatever I tell her to, isn't that right?"
    if defymatt:
        "As if you had a choice!"
    if club == "track":
        "You have to force yourself not to glare at him."
    elif club == "cheer":
        if defymatt:
            "Despite yourself, you feel your pulse quicken."
        elif True:
            "Your pulse quickens."
    elif club == "yearbook":
        "You squeeze your eyes shut."
    pcname "Y-Yes."
    "Matt reaches out and pinches one of your nipples."
    pcname "Ah!"
    m "Now, Alex is going to fuck you. And if it looks like it's worth my time, I might even take a turn."
    m "But first, you have to ask him nicely."
    if defymatt:
        "You know that you have no choice, but the words stick in your throat."
        "Swallowing your pride, you force them out:"
    elif True:
        if club == "track":
            pcname "Please?"
        elif club == "cheer":
            pcname "Oh, please..."
        elif club == "yearbook":
            pcname "P-Please?"
    "He gives your nipple a hard twist, making you cry out again."
    m "You can do better than that."
    if defymatt:
        "There's little fight left in you. You got yourself into this mess, after all."
        "If you'd screamed that first day... Or refused to meet him in the bathroom... Or..."
        "It's your fault that you're here. Some part of you {i}must{/i} have wanted this..."
        "Why resist now?"
    pcname "Please fuck me, Alex. Please?"
    "Matt nods to Alex, who quickly removes his finger and presses his cock against your dripping cunt."
    "Without any hesitation, he pushes his cock inside of you, stretching you wide."
    show bg MApt22
    if defymatt:
        "You gasp at the sudden intrusion."
        "You asked for this. You asked him to fuck you. You even said please."
    elif True:
        pcname "Ohhhh..."
    "Alex" "Fuck she's tight..."
    "He pulls back a little and thrusts again, filling you."
    "Matt grabs your other breast, squeezing it hard; his fingers continue tormenting your nipple."
    "Alex moves inside of you, thrusting with slow, steady movements."
    "His thick cock presses against your gspot, leaving you aching with pleasure."
    if defymatt:
        "If you didn't want this, it wouldn't feel so good... Would it?"
    "Just as the sensation starts to overwhelm you, Matt releases your breasts."
    m "Alright, Alex, I think I'm convinced."
    "Alex" "Already?"
    "Matt laughs."
    m "Don't worry. You'll get another turn."
    m "Right now, I want this slut to scream {i}my{/i} name."
    "Alex steps back, pulling his cock from you. You cover your mouth to stifle a disappointed moan."
    "Matt wastes no time, filling you with a single, hard thrust."
    show bg MApt23
    pcname "Oh!"
    m "You like that, slut?"
    if defymatt:
        "You do, don't you? You're so aroused... You must like it, right?"
    if club == "track":
        "You refuse to admit to it."
    elif club == "cheer":
        pcname "Yes! Oh yes...!"
    elif club == "yearbook":
        pcname "I... I..."
    "He grabs your legs and, using them for leverage, fucks you hard."
    "As Matt fucks you, Alex massages your breasts, dipping his head to take a nipple in his mouth."
    if defymatt:
        "Whatever your feelings - and you're no longer sure you know what they are - your body responds."
    "Between the fingers and lips on your breasts and the cock slamming into your pussy, you begin to feel like you're floating on waves of pleasure."
    "Then, suddenly, Matt pulls out."
    "A whimper leaves your lips, as you struggle to understand why Matt's cock is gone."
    m "Want some more, slut?"
    if defymatt:
        "You were so close... It felt so good..."
    if club == "track":
        "You can't bring yourself to admit it."
    elif club == "cheer":
        "You're too aroused to care about anything else right now..."
        pcname "Yes!"
    elif club == "yearbook":
        pcname "P-please?"
        "You're not quite sure what you're asking for."
    m "What do you think, Alex? Should we make her beg for it?"
    "Alex releases your breasts and grins down at you."
    "Alex" "I'd like to hear her beg."
    m "If you want us to keep fucking you, you'll have to beg for our cum."
    "Your face burns as you look between the two leering men."
    pcname "Please..."
    m "Please what?"
    if club == "track":
        "You bite your lip; you want to climax, but begging..."
    elif club == "cheer":
        pcname "Oh god..."
    elif club == "yearbook":
        "Unable to face them, you turn your head away."
    pcname "Please... can I have your cum?"
    m "You want both of us to fuck you?"
    if defymatt:
        "You're ashamed of your own reaction."
    elif True:
        if club == "track":
            "It sounds awful - and you want it."
        elif club == "cheer":
            "It sounds amazing!"
        elif club == "yearbook":
            "You can't believe the words coming out of your mouth..."
    pcname "Yes! Please!"
    m "What do you think, Alex?"
    "Alex" "I don't know. I'm not convinced she really wants it."
    "Your cunt throbs with the memory of their cocks, and your lips are swollen and puffy from the way they stretched around Alex."
    pcname "Please let me have your cum, Matt. Please!"
    "He tilts his head, as if trying to decide."
    m "Alex, why don't you go up there and let her finish what she started?"
    "Alex" "Fuck yeah."
    "As Alex makes his way to the other side of the desk, Matt grabs your legs again."
    "Taking your head between his hands, Alex tilts your face up and presses his cock against your lips."
    show bg MApt24
    "Both men enter you at the same time - Matt thrusting hard into your pussy, Alex pushing his cock into your mouth."
    "A loud moan fills your throat and you lift your hands to your breasts, pinching and twisting your throbbing nipples."
    m "You really are a good little slut, aren't you?"
    "With Alex's dick in your mouth, it's impossible to do more than moan in response."
    "Matt's fingers dig into your thighs as he slams into you again and again."
    "You struggle against your gag reflex as Alex's cock presses against the back of your throat."
    "Still holding your head in place, he thrusts into your mouth, fucking it slowly."
    "Tears well in your eyes; the sensations are overwhelming."
    "Precum coats your tongue and your pussy begins clenching around Matt's cock as your climax nears."
    "You're barely aware of your fingers still twisting frantically at your nipples."
    "Suddenly your cunt clenches tight around Matt's cock and you lose control completely."
    "Your throat tightens around Alex's cock, pushing him over the edge. He pulls back just in time to shoot strings of hot cum all over your face."
    "Matt thrusts hard and fast against your clenching muscles, moaning as you spasm around him."
    "Just as you lose yourself in the waves of pleasure, you feel him fill you in hot spurts."
    "When the last shock of your orgasm fades, you open your clenched eyes hesitantly."
    "The room looks too bright, leaving you blinking and wiping the tears from your lashes."
    show bg MApt25
    "Licking your swollen lips, you taste the salty cum covering your face."
    m "I think she likes the way you taste, Alex."
    "You look toward the sound of their laughter; they're already dressed."
    m "Good job, slut. I'm actually pretty happy with you today."
    if defymatt:
        "Suddenly aware of everything that just happened - everything that you did - you tremble on the desk, still feeling the aftermath of your orgasm."
    elif True:
        "Smiling, you sigh contentedly, still heavy with the aftermath of your orgasm."
    m "Better get yourself cleaned up, though. Who knows who might come in?"
    "Bolting upright, you stare as they open the door and exit the classroom, leaving you naked, alone, and covered in their juices."
    "You jump off the desk, knees shaking as you stumble to your discarded uniform."
    "As you dress yourself, you feel Matt's cum trickling down your inner thigh."
    "Your eyes are drawn to the desk; there's a wet spot staining the wood."
    "A sound in the hallway draws your attention. Your heart is racing as you finally leave."
    if defymatt:
        "The entire way home, your mind is a mess."
        "You're not sure what you feel... Shock that you're being blackmailed."
        "Horror at what you were forced to do."
        "And yet, with the proof of your own arousal still sticky between your legs..."
        "You gave in. You asked them to fuck you. You... wanted it?"
        "You came. You got off from what they made you do. What they did to you."
        "You {i}enjoyed{/i} it, whether you wanted it or not."
        "And you didn't have to stay. You could have left."
        "You shake your head, pushing all of those thoughts away."
        pcname "It doesn't matter. I'm not hurt. I'm fine!"
    elif club == "track":
        "Despite yourself, you're impressed that you could handle both of them at once."
    elif club == "cheer":
        "As you walk out of the school, you run your fingers over your sex-bruised lips and smile."
    elif club == "yearbook":
        "The whole way home, you can't help but think of Matt's sticky cum between your thighs."
    $ deskstain = True
    show bg black with dissolve
    jump events_end_period

label bully_gangrape:
    show chelsea blank at right with moveinright
    "You take a walk around town, hoping to find something new."
    "There's a sign for the grand opening of a new Chinese restaurant."
    menu bully_gangrape_restaurant:
        "Check it out." if True:
            "You put the address into your phone's GPS."
            "Thankfully, it's only a 15 minute walk."
            "The building looks nice from the outside, but as you near the door you realize they've already closed for the evening."
            show chelsea sad
            pcname "Guess I'll have to come back another time..."
            "Disappointed, you turn toward home with a sigh."
        "Keep looking around." if True:
            "You're not in the mood for Chinese right now, so you keep walking."
            "After thirty minutes, you decide there's nothing to see and head toward home."
    show chelsea blank
    "It's getting pretty late and there aren't many people out, so the walk home is pretty quiet."
    show chelsea shocked
    "Suddenly, large arms close around your waist, a hand covers your mouth, and you're lifted off the ground."
    "You try to scream as you're dragged toward an alley, but your attacker pinches your nose shut, releasing only when your vision starts to dim."
    "Breathing heavily through your nose, you fight back your growing panic. Your assailant carries you further into the alley before ducking into a small alcove."
    "Footsteps behind you give you a burst of hope - until you hear a voice."
    show Matt Casual Smirk at left with moveinleft
    m "So, it looks like you're in a rough situation, doesn't it?"
    "The man holding you turns and you see Matt standing behind you. He smirks as he looks up and down your body."
    m "See, you've embarassed me {i}and{/i} my friend Alex now."
    show Alex Happy with dissolve
    "Alex" "And we think it's time you pay for it."
    show Alex Blank
    "You recognize the other man--Alex--as the bully who was picking on [damienname]."
    "Just as the realization hits you, Alex pulls your hands behind your back and pins them together."
    "He clamps his other hand back over your mouth; his grip is tight, but you might be able to get free."
    "This could be your only chance to avoid what they have planned."
    menu bully_gangrape_run:
        "Run for it!" if True:
            show chelsea angry
            "Adrenaline surges through your body as you bring your heel down sharply on his toes."
            show Alex Angry
            show Matt Casual Angry at left
            "Surprised, Alex releases you with a howl."
            "Alex" "FUCK!"
            "Alex" "I think the bitch broke my toes!"
            "You feel a thrill of satisfaction, but there's no time to enjoy it."
            "Running as fast as you can, you flee the alley."
            m "She's getting away!"
            "Alex" "Chase her if you want. I can barely walk!"
            "Their voices disappear as you put more and more distance between you."
            hide Matt Casual Angry with moveoutleft
            "You don't stop running until you reach your front door."
            "Slamming it behind you, you throw the locks in place and sink to the floor."
            show chelsea sad
            "For a while, all you can do is sob. That was really, really close."
            "You debate calling the police, but with no witnesses and no proof, you know there's nothing they could do - and you {i}really{/i} don't want to talk about it."
            "Unwilling to leave your house again, you decide just to go to bed."
            "It takes a long, long time to go to sleep."
            jump endday
        "Don't take the chance." if True:
            pass
    show chelsea sad
    "Escape seems unlikely, and trying will probably just make things worse."
    "While Alex holds you in place, Matt approaches; your heart skips a beat when he flips open a knife."
    hide chelsea with fade
    scene bg black with dissolve
    m "Let's see those tits."
    "He lifts the front of your shirt away from your body, then slowly cuts it open."
    m "Not bad!"
    "He hooks the knife under your bra, drawing it up. Your bra splits with a {i}snap{/i}."
    show bg MAA1 with dissolve
    m "What do you think, Alex?"
    "Alex's breath is hot on your neck as he peers down over your shoulder."
    "Alex" "Seen better."
    "Your face burns with shame as the cool night air licks your exposed flesh."
    show bg MAA2 with dissolve
    "Matt laughs and grabs one of your breasts, squeezing hard."
    m "Nice and firm, though."
    "He releases you with a smirk."
    m "And look, her nipples are already getting hard. Guess you're into this kind of thing, huh?"
    if club == "track":
        "Tears well in your eyes. You've never felt so humiliated - and you have a terrible feeling this is only the beginning."
    elif club == "cheer":
        "Tears well in your eyes. You've never felt so humiliated - and yet..."
    elif club == "yearbook":
        "Tears well in your eyes. You've never felt so humiliated!"
    "Alex" "She's a fucking slut, ain't she?"
    m "Let's see what else she likes."
    "Matt leans in close and grabs a fistful of your hair. Yanking your head back, he hisses a threat."
    m "Alex is going to take his hand off your mouth. If you scream, I swear I'll make sure you regret it."
    m "You understand?"
    "You nod, your hair pulling painfully in his grasp."
    show bg MAA3 with dissolve
    "Alex's hand falls off your mouth, then moves to your other breast."
    "Alex" "You're right. They're hard enough to cut glass!"
    "You try to turn your head, unable to hold back a sob as he pinches your nipple, but Matt's grip on your hair holds you in place."
    m "Enough playing around. Time to show you how much you embarrassed us."
    "He pulls your head down, forcing you to the ground."
    "Your knees scrape against the pavement, but you manage to suppress a pained cry."
    "You can't see Alex, but you hear the sound of his zipper."
    m "Now, I'm going to let you go and you're going to suck us both off. Got it?"
    menu bully_gangrape_blowjob:
        "Accept it" if True:
            "You nod your head as best you can, ignoring the tears that spill down your cheeks."
        "Beg" if True:
            pcname "Please don't do this..."
            "Alex" "{i}Please don't do this{/i}. Listen to her. She has better manners already."
            m "Too late for that, bitch."
    show bg MAA4 with dissolve
    "Matt releases your hair as Alex steps in front of you, his thick, hard cock swinging inches from your face."
    "Alex" "Open wide."
    menu bully_gangrape_openmouth:
        "Do as he says." if True:
            "With a glance at Matt, still holding the knife, you open your mouth."
            show bg MAA5 with dissolve
            "He grabs the back of your head, tilting it slightly back."
        "Resist." if True:
            if club == "track":
                "Glaring up at him, you shake your head."
            elif club == "cheer":
                "Part of you is excited by what's happening, but you refuse to make it easy for them!"
            elif club == "yearbook":
                "Clamping your lips together, you shake your head."
            "{i}CRACK{/i}"
            "Your head wrenches to the side as Alex backhands you."
            "His fingers dig into your cheeks, forcing your teeth apart."
            show bg MAA5 with dissolve
            "Then he moves to the back of your head and forces it back."
    "Alex" "Bite me and you'll regret it."
    "He presses his cock against your lips, forcing you to open wider to accommodate his girth."
    if corruption > 10:
        "Alex" "Fuck... Most girls struggle with my size..."
    elif True:
        "Alex" "Bitch can barely get her mouth around me!"
    "Holding the back of your head, he works his cock in and out of your mouth."
    m "Don't forget about me."
    "Grabbing your hand, Matt spits into your palm and presses it against his cock."
    m "What're you waiting for?"
    "You have no choice but to stroke him while Alex violates your mouth."
    "It's all you can do to hold back a sob as you work your hand up and down Matt's length, trying not to gag around the thick dick pressing to the back of your throat."
    "After a few minutes, Alex releases your head and pulls away, leaving a trail of saliva trailing down your chin."
    "Alex" "Want a turn?"
    m "Hell yeah!"
    "Matt grabs your hair, forcefully turning you toward him."
    show bg MAA6 with dissolve
    "Without hesitation, he thrusts his cock into your mouth."
    "Alex" "Forgetting something?"
    "Alex slaps his cock against the side of your head. You reach up to defend yourself, but he presses himself into your hand."
    "Alex" "Eager little bitch, aren't you?"
    "His cock is dripping with your saliva, making it easy for you to pleasure him in long, firm strokes."
    "Matt grips your hair hard, holding you firmly in place as he fucks your face."
    "His dick strikes the back of your throat with every thrust."
    "Tears sting your eyes and drool runs down your chin as you struggle vainly to suppress your gag reflex."
    "Alex" "Oh fuck..."
    "Alex's cock grows slicker with precum. Maybe if you can get them both off, they'll let you go?"
    "Suddenly, Matt jerks your head hard, forcing his cock down your throat and holding you tight against him."
    "You can't help but gag around his cock, your grip on Alex tightening as you fight the urge to vomit."
    "Just when you think you can't hold back any longer, Matt releases you."
    "His cock slips from your mouth, leaving you gasping for breath."
    "Alex" "I need to feel {i}that.{/i}"
    "Before you realize what's happening, Alex grabs your head and presses his dick into your mouth."
    show bg MAA7 with dissolve
    "His cock is salty with precum, and he thrusts it straight down your throat."
    "Your muscles clench tight around him, and you find yourself gagging again and again."
    "Alex" "Like that, bitch?"
    "A ragged moan rattles through your throat as he finally releases you."
    "Sobbing and sniffling, you smear the tears from your cheeks and wrap your arms around your breasts."
    m "We're not done yet. Get up!"
    show bg MAA8 with dissolve
    "Shakily, you pull yourself to your feet."
    m "I think it's time to see the rest of the goods."
    "Alex" "And test them out."
    "Pulling his knife out again, Matt quickly cuts the rest of your clothes from your body."
    "As your ruined panties fall to the dirty concrete, Matt grabs your cunt and presses two fingers against your opening."
    m "Fuck... She's already dripping."
    "He pulls his hand back and smears your juices across your tear-stained face; then, he circles you like a predator eyeing a piece of meat."
    "Alex" "Told you she's an eager bitch."
    "He reaches between your legs and presses a finger into you. Your muscles tense at the violation."
    "Alex" "Feels like she's desperate for some dick."
    m "Let's not keep her waiting then..."
    "Grabbing your hips, Matt forces his knee between your legs and spreads them apart."
    m "Bend over, bitch."
    show bg MAA9 with dissolve
    "Alex grabs your hair and pulls your head down, while Matt presses his cock against your opening."
    "You can't hold back the cry that rips through your throat as Matt thrusts into you, filling you in a single stroke."
    m "Shut her up!"
    show bg MAA10 with dissolve
    "Alex pulls your hair, tilting your head back, and presses his dick against your lips."
    "As Matt thrusts into you again, you cry out and Alex stuffs his dick into your mouth."
    "Matt fucks you hard, each thrust pressing Alex's dick farther down your throat."
    "After a while, Matt pulls out of you and slaps your ass."
    m "Come feel how tight she is."
    "Matt grabs a handful of hair, holding you in place as Alex releases you."
    "As Alex circles behind you, Matt smirks, rubbing his cock across your cheeks."
    m "Ready to find out how you taste?"
    show bg MAA11 with dissolve
    "He presses his dick into you, filling your mouth with the taste of your own pussy."
    "Alex" "I bet the bitch likes it."
    "Digging his fingers into your hips, Alex presses himself against your opening."
    "You feel yourself stretching around his thick cock as he enters you."
    "He fills you in long, deep strokes, each thrust rocking your face forward and back around Matt's cock."
    "Matt tilts your face a little more, forcing his cock deep into your throat."
    "For several minutes, you're helpless between them as they fuck you from both ends - until, suddenly, Matt pulls free from your mouth."
    m "You ready for my cum?"
    "Holding your head with one hand, he points his cock toward your face with the other."
    m "Open wide."
    if club == "track":
        "Unwilling to fight anymore, you hold your mouth open - gasping each time Alex thrusts into you - and wait for Matt's cum."
    elif club == "cheer":
        "You hold your mouth open, gasping each time Alex thrusts into you, and wait for Matt's cum."
    elif club == "yearbook":
        "Sobbing with each of Alex's thrusts, you open your mouth and wait for Matt's cum."
    show bg MAA12 with dissolve
    "He jerks himself off, coating your lips and chin with hot strings of thick fluid."
    "As he wipes the last drops off on your cheek, Alex pulls out."
    "Alex" "On your knees, bitch."
    "You fall to your knees without a second thought, willing to do anything if they'll just finish."
    "Alex" "Open up and stick your tongue out."
    "You do as he tells you, tilting your head back to receive his cum."
    show bg MAA13 with dissolve
    "He jerks himself off hard and fast, spraying his juices across your face in messy spurts."
    "Alex" "What a fucking mess."
    "They look down at you, sneering in disgust as they tuck their dicks back into their pants."
    m "Aren't you going to clean yourself up, bitch?"
    menu bully_gangrape_clean:
        "Use your clothes." if True:
            show bg MAA14 with dissolve
            "Grabbing your ruined panties, you drag them across your face."
            "They laugh as you try - and fail - to wipe yourself clean."
            "Alex" "Stupid bitch, using her dirty panties..."
            "Too late, you realize that you'd smeared dirt across your cheeks, turning it to mud as it met the fluids there."
            "They shake their heads, still laughing."
        "Use your fingers." if True:
            show bg MAA15 with dissolve
            "With nothing to use but your fingers, you wipe the cum from your face."
            "Alex" "Well, don't waste it."
            "You look down at your cum-covered fingers, confused."
            m "Yeah, you know you want to taste it."
            "Numbly, you raise your hand to your lips and suck the lukewarm cum from your fingertips."
            "Alex" "What a fucking slut..."
    m "Now, we're going to take your clothes and let you go - but if you try to tell anyone what happened here, you're going to regret it."
    m "See, Alex's dad is the Chief of Police. If you try going to them, the whole town's going to hear {i}our{/i} story first."
    "Alex" "All about how you {i}begged{/i} us to let you suck our cocks."
    m "Exactly."
    "You can barely react. You already knew that it would be your word against theirs - especially if they take your shredded clothes."
    "Alex" "I think she gets it. Don't you, bitch?"
    "You nod slowly."
    m "Good. You know, I think we had a lot of fun. Didn't we, Alex?"
    "Alex" "Sure did."
    m "Maybe we'll catch you again sometime."
    show bg black with dissolve
    "You stare numbly ahead as they walk away, their laughter ringing in your ear."
    "A long time after you've heard the last of their footsteps, you pull yourself to your feet."
    "Taking a filthy blanket from a nearby trashcan, you wrap it around yourself and make your way home."
    "As you open the door, you drop the makeshift coat and kick it back outside."
    "The first thing you do is take a long shower - only stepping out when the water turns cold."
    "It's not until much later, as you lie in bed staring vacantly at the ceiling, that the numbness fades away."
    "The dam holding your emotions back finally breaks; suddenly, you find yourself sobbing uncontrollably into your pillow."
    "Eventually - an eternity later - you give in to your exhaustion and allow sleep to claim you."
    $ gangrape = True
    $ alleyscene += 1
    jump endday
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
