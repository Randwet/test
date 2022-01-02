label cafeconflict1_Matt:
    show chelsea at right with moveinright
    $ clothes = 'school'
    "Matt walks into homeroom and glares at you."
    show Matt Angry at left with moveinleft
    show chelsea sad
    if defymatt:
        "Your stomach sinks as you wonder why he's mad. And what he'll do about it."
    elif True:
        "You can't help but wonder what you've done to disappoint him."
    m "I heard you're working at a bar now? I thought you were at that Maid Cafe?"
    if club == "track":
        pcname "I was. I quit."
    elif club == "cheer":
        pcname "I was sick of that place, so I quit."
    elif club == "yearbook":
        pcname "I... don't work there anymore."
    show Matt Smirk at left
    m "Why? I was thinking of going there sometime. I'd like you to call me \"Master\" in public."
    if defymatt:
        show chelsea confused
        "You roll your eyes."
    elif True:
        show chelsea happy
        "You look down at your desk, smiling softly."
    show Matt Angry at left
    m "So?"
    menu cafeconflict1_Matt_why:
        "Tell the truth." if True:
            if club == "track":
                show chelsea happy
                pcname "Fucked a customer after work and my boss found out."
            elif club == "cheer":
                show chelsea blank
                pcname "I was... entertaining customers in ways my boss didn't approve of."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Someone saw me... Doing things... With a customer."
                m "\"Doing things\"? What kind of things?"
                "You blush."
                pcname "...dirty things..."
            show chelsea shocked
            "To your surprise, Matt stands up and slaps his hand down on his desk."
            m "You're a fucking {i}slut{/i}!"
            show Harley Angry with dissolve
            T "Matt! That language is unacceptable."
            m "Whatever, old man."
            T "That's enough. Go to the principal's office. {i}Now{/i}!"
            hide Harley Angry with moveoutright
            "Matt glares at you, kicking his chair and storming out of the room."
            hide Matt Angry with moveoutleft
        "Lie." if True:
            show chelsea blank
            pcname "I just didn't like it anymore."
            "He crosses his arms over his chest."
            m "So you went to a bar?"
            "His eyes narrow."
            m "Don't lie to me. What really happened?"
            if defymatt:
                if club == "track":
                    show chelsea happy
                    pcname "Fucked a customer after work and my boss found out."
                elif club == "cheer":
                    show chelsea blank
                    pcname "I was... entertaining customers in ways my boss didn't approve of."
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "Someone saw me... doing things... with a customer."
                    m "\"Doing things\"? What kind of things?"
                    "You blush."
                    pcname "...dirty things..."
            elif True:
                show chelsea blank
                pcname "I wanted better tips, and the customers tipped better if I... did them some favors."
                m "You fucked them?"
                if club == "track":
                    show chelsea angry
                    pcname "Not all of them!"
                elif club == "cheer":
                    show chelsea sad
                    pcname "Some of them..."
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "No! Well... S-some of them?"
            show chelsea shocked
            "To your surprise, Matt stands up and slaps his hand down on his desk."
            m "You're a fucking {i}slut{/i}!"
            show Harley Angry with dissolve
            T "Matt! That language is unacceptable."
            m "Whatever, old man."
            T "That's enough. Go to the principal's office. {i}Now{/i}!"
            hide Harley Angry with moveoutright
            "Matt glares at you, kicking his chair and storming out of the room."
            hide Matt Angry with moveoutleft
    show chelsea sad
    "You stare at your desk, aware of several people staring and whispering."
    "Thankfully, by halfway through your first class, everyone seems to have forgotten."

    call screen TextingScene("Matt",
    [
        TextMessage("Come to the principal's office"),
        TextMessage("Now")
    ])

    if defymatt:
        call screen TextingScene("Matt", [TextMessage("You know what happens if you don't")])

    jump cafeconflict1_Matt_blackmail

label cafeconflict1_Matt_blackmail:
    show chelsea at right
    $ clothes = 'school'
    menu cafeconflict1_Matt_go:
        "Go." if True:
            jump cafeconflict1_Matt_principal
        "Don't go." if True:
            if defymatt:
                "You feel sick when you think of what the consequences might be, but you can't do this anymore."
                "Heart pounding against your ribs, you tuck your phone away again."
                "You know you might be making a big mistake, but you won't let him control you anymore."
                hide chelsea with dissolve
                $ mattblackmail = 2
                jump events_end_period
            elif True:
                "The last time was too much for you, and today you've had plenty of time to consider what you've been doing."
                "Heart pounding against your ribs, you tuck your phone away."
                "A moment later, though, it vibrates again."

                call screen TextingScene("Matt",
                [
                    TextMessage("You have 5 minutes"),
                    TextMessage("Or I'll put those pics all over the school")
                ])

                $ defymatt = True

                "With shaking hands, you put your phone back into your pocket."

                if club == "track":
                    show chelsea angry
                    pcname "That bastard!"
                elif club == "cheer":
                    show chelsea sad
                    pcname "Now what do I do..."
                elif club == "yearbook":
                    show chelsea sad
                    pcname "How could I let this happen...?"

                hide chelsea with dissolve

                jump matt_scene3_gochoice

label cafeconflict1_Matt_principal:
    show chelsea at right with moveinright
    "You enter the principal's office."
    "Matt is sitting at the principal's desk."
    show Matt Angry at left with moveinleft
    m "I have detention all week, thanks to you."
    if defymatt:
        if club == "track":
            show chelsea angry
            pcname "None of this is {i}my{/i} fault."
        elif club == "cheer":
            show chelsea confused
            pcname "I didn't call {i}you{/i} a slut."
        elif club == "yearbook":
            show chelsea confused
            pcname "M-me??"
    elif True:
        show chelsea sad
        pcname "I'm sorry, Matt, I--"
    m "Shut up."
    show chelsea blank
    "He stands up and walks around the desk."
    show Matt Blank at left
    m "He lectured me for a while and then told me to go back to class."
    show Matt Smirk at left
    m "But then I heard him tell the secretary that he had a meeting to go to."
    m "He won't be back until the afternoon."
    if defymatt:
        show chelsea confused
        pcname "So?"
    elif True:
        show chelsea sad
        "You swallow down your growing nervousness."
    show Matt Blank at right with moveinleft
    "Stepping behind you, Matt shuts the door. You hear the lock click into place."
    show Matt Smirk with move
    m "So you're gonna take off all your clothes and take a seat."
    if defymatt:
        if club == "track":
            show chelsea confused
            pcname "I don't think so."
        elif club == "cheer":
            show chelsea angry
            pcname "No way!"
        elif club == "yearbook":
            show chelsea embarrassed
            pcname "I can't do that!"
        show Matt Blank at left
        m "You can't say no to me, [pcname]. I have way too much leverage."
        show chelsea embarrassed
        "Thinking of the pictures, you swallow your pride and start to undress."
    elif True:
        show chelsea embarrassed
        pcname "Yes, Matt."
    show Matt Smirk at left with moveoutleft
    "As you pull off your shirt, he smirks."
    $ clothes = 'underwear'
    m "Call me \"Master\"."
    if defymatt:
        show chelsea angry
        "You glare, pulling your skirt down."
    pcname "Yes, Master."
    show chelsea with dissolve
    show Matt at left with moveinleft
    $ clothes = 'naked'
    "When you finish, you take a seat in the principal's chair, trying not to think about where you are and what you're doing."
    "If the principal found out..."
    show Matt Smirk at left
    m "I found these in a desk drawer..."
    "He holds up several ties, waving them in front of you."
    show Matt Happy at left
    m "Think the old man ever used them for this?"
    show Matt Smirk at left
    if defymatt:
        show chelsea shocked
        "Heart pounding - you're going to be tied up, at his mercy - you stubbornly refuse to answer."
    elif True:
        show chelsea embarrassed
        "Heart pounding - you're going to be tied up, at his mercy - you sigh with pleasure."
        pcname "No, Master..."
    "He grins and kneels before you."
    "Spreading your legs wide, he ties your feet to the bottom of the chair."
    show Matt Angry at left
    m "Fuck... I wish I'd planned this..."
    show Matt Blank at left
    "He stares at you a moment, clearly imagining what else he could do if he had more time, and the grabs your wrist."
    "Using the other two ties, he binds one wrist to each of the chair's arms."
    show Matt Smirk at left
    m "Much better."
    show Matt Blank at left
    m "Now, tell me you're sorry for getting me in trouble."
    if defymatt:
        show chelsea sad
        pcname "But I--"
        show Matt Angry at left
        show chelsea shocked
        "He grabs your nipple, twisting hard."
        pcname "Ah!"
        "He twists it again - it hurts, but a familiar heat floods your pussy."
        m "What was that?"
    show chelsea embarrassed
    pcname "I'm sorry, Master."
    show Matt Blank at left
    "Your heart thuds against your chest; what will he do to you?"
    show Matt Smirk at left
    m "Don't worry. I'm going to let you make it up to me."
    "Unzipping his pants, he pulls out his dick and presses it toward your lips."
    m "Open up, slut."
    if defymatt:
        show chelsea angry
        "Glaring up at him, you begrudgingly open your mouth."
    elif True:
        show chelsea embarrassed
        "You cast your eyes down, just the way he taught you, your lips parting eagerly."
    show Matt Blank at left
    m "Go on. Suck it."
    "Strapped to the chair, you can't use your hands at all."
    "Awkwardly, you use your tongue to direct him into your mouth."
    show chelsea embarrassed
    m "Come on. A slut like you should be able to do this with her hands tied behind her back."
    show Matt Smirk at left
    m "Or to a chair."
    show Matt Blank at left
    "You stretch forward, taking as much of him as you can get."
    "Leaning back and forth, you do your best to suck him off."
    m "This is pathetic. You can take more than that."
    if defymatt:
        "You don't want to blow him, but his words prick your pride."
    "You strain to take more, throwing your weight forward to move the chair closer to him."
    "Throwing your whole torso forward and back, you press your tongue against the underside of his cock."
    "Moving as fast as you can and ignoring the spit running down your chin, you rock forward and back, his cock sliding in and out of your mouth."
    show Matt Angry at left
    m "You're fucking useless for this. Here."
    "He grabs the back of your head and pulls you forward."
    show chelsea shocked
    "His cock presses to the back of your throat - and then further."
    show chelsea sad
    "Your eyes water as you hold back your gag reflex and swallow his cock."
    show Matt Happy at left
    "Laughing, he holds you in place."
    m "You like that, slut? You like choking on my dick?"
    show Matt Smirk at left
    show chelsea shocked
    "You can't move; his hands hold you firmly in place. You start to panic, unable to breathe."
    show Matt Blank at left
    m "It feels a lot better than your pathetic attempt."
    show chelsea embarrassed
    show Matt Smirk at left
    "He pulls your head back and you manage to take a full breath before he thrusts back down your throat."
    "Yanking your head back and forth, he fucks your face, balls slapping against your chin with the force of his thrusts."
    if defymatt:
        "Tears streak your face - you feel completely helpless."
    elif True:
        "Tears streak your face, but you barely notice. Your attention is focused on the cock sliding in and out of your throat."
        "You want to impress Matt more than anything."
    show Matt Happy at left
    m "{i}That's{/i} how you take a dick."
    show Matt Smirk at left
    "He shoves his cock down your throat until it feels raw."
    "Finally, he pulls out."
    show Matt Blank at left
    m "Keep your mouth open."
    "Breathing heavily, you hold your mouth open while he strokes his cock."
    "Hot strands of cum hit your lips and cheeks, running into your mouth and down your chin."
    show Matt Smirk at left
    "He tucks his cock back into his pants and looks down at you, smiling cruelly."
    m "What do you say?"
    if defymatt:
        show chelsea angry
        "Glaring up at him, you clamp your mouth shut, swallowing silently."
        show Matt Blank at left
        "He takes his phone out and snaps a picture."
        show Matt Angry at left
        m "What did you say?"
        show chelsea embarrassed
        "Your face flushes with shame and anger, but you have no choice."
        pcname "Thank you, Master."
    elif True:
        show chelsea happy
        "You smile, dazed but content."
        pcname "Thank you, Master."
    show Matt Smirk at left
    m "That's better..."
    "Grabbing your breast, he squeezes it harshly."
    show chelsea shocked
    pcname "Ah!"
    show Matt Angry at left
    m "You think you can just fuck whoever you want, huh?"
    "He pinches your nipple, twisting until you cry out again."
    show chelsea sad
    pcname "I'm sorry, Master!"
    m "You're not sorry. You're a slut."
    m "All you think about is how to get another dick in you, huh?"
    "He pulls your nipple before releasing it."
    show chelsea shocked
    pcname "Ah!"
    "Grabbing the other one, he twists it too."
    m "Say it!"
    show chelsea sad
    pcname "Yes, Master. Yes!"
    "He grabs the first again, twisting them both until you cry out."
    show chelsea shocked
    pcname "Yes, Master! I'm a slut! All I want is dick!"
    show Matt Smirk at left
    show chelsea embarrassed
    "Smiling, he releases your nipples. They throb, edging between pain and pleasure."
    m "Well you're not getting one today."
    show Matt Blank at left
    "His hand snakes between your legs, cupping the mound of your pussy."
    "Pressing his fingers into your folds, he finds your clit and rolls it between them."
    "You gasp at the too-strong sensation."
    show chelsea shocked
    pcname "M-Master!"
    show Matt Angry at left
    m "You're mine, slut. You fuck who I want, when I want."
    show chelsea embarrassed
    "He rolls your clit back and forth between his fingers. Your hips buck and you twist against him, but you can't move."
    show Matt Smirk at left
    pcname "Yes, Master! I'm yours!"
    "Like your nipples, your clit throbs with a pleasure that's quickly becoming pain."
    "Suddenly he releases your clit, his fingers probing lower."
    show chelsea shocked
    "Pressing them into your opening, he begins fingering you hard and fast."
    show Matt Blank at left
    m "Fuck, you're wet."
    if defymatt:
        show Matt Smirk at left
        m "You act like you don't want this, but you fucking {i}love{/i} it, don't you?"
        "You want to tell him you {i}hate{/i} this, but you can barely think, let alone speak."
    show chelsea embarrassed
    "His fingers pump in and out of your cunt; your nipples and clit throb with pleasure."
    "The sensations build until they're almost unbearable."
    show Matt Smirk at left
    m "Are you gonna cum, slut?"
    pcname "I... I want to cum..."
    if defymatt:
        m "That's right. You pretend to hate this, but you know it's what you deserve."
    elif True:
        m "That's right. You're just a dirty slut."
        m "You need a guy like me to tell you what to do, don't you?"
        "Your answer is lost in another moan of pleasure."
    m "Go on, slut."
    show Matt Blank at left
    "He presses his thumb to your clit, working it in circles as he continues thrusting his fingers into your pussy."
    "The pleasure is overwhelming. Almost immediately, you feel your climax flood through you, soaking his hand in your juices."
    show Matt Smirk at left
    "Matt stands back, smiling down at you."
    m "You made a pretty big mess on the principal's chair."
    "Looking down, you see a large wet stain spreading beneath you."
    m "What do you think he'll say what he sees you like this?"
    show chelsea shocked
    "Your eyes widen and your mouth falls open in shock."
    pcname "You can't!"
    m "I can..."
    "He leans down, putting his face close to yours."
    m "Do you think he he'd be mad? Or maybe that's why he keeps all those ties in his desk?"
    menu cafeconflict1_Matt_principal_beg:
        "Beg him not to." if True:
            show chelsea sad
            "Shaking your head, you try to plead with him."
            if club == "track":
                pcname "Please, you can't!"
            elif club == "cheer":
                pcname "You wouldn't do that, would you?"
            elif club == "yearbook":
                pcname "P-Please don't. I can't..."
            show Matt Happy at left
            "Laughing, he takes a step back again."
            m "Who's your master?"
            if defymatt:
                "Swallowing back your pride, you tell him what he wants to hear."
            show chelsea embarrassed
            pcname "You are, Master."
            show Matt Smirk at left
            m "That's right."
        "Stay silent." if True:
            show chelsea embarrassed
            if defymatt:
                "Humiliated, you look away."
            elif True:
                "Keeping your eyes downcast, you wait for him to decide."
            show Matt Happy at left
            "Laughing, he takes a step back."
    show Matt Smirk at left
    m "You're lucky - this time."
    show Matt Angry at left
    m "But next time you {i}will{/i} regret it."
    show Matt Blank at left
    "He unties you and you flex your wrists, working the blood back into your hands."
    $ clothes = 'underwear'
    "As you slip your clothes back on, Matt unlocks the door."
    show Matt Smirk at right with moveinright
    show chelsea shocked
    m "Better hurry up. I might have misheard what time he'll be back."
    show Matt Happy at right
    "He laughs, leaving you hurriedly pulling your shirt back over your head."
    hide Matt Happy with moveoutright
    hide chelsea with dissolve
    jump events_end_period

label cafeconflict1_Damien:
    show chelsea at left with moveinleft
    $ clothes = 'school'
    "The cafeteria is brimming with activity as you enter, a mass hoard of students making a mad dash for the lunch line as the countdown to class begins."
    "You start to make your way toward the line when Damien waves you over from a nearby table, a bright smile on his face."
    "You discard the line to join him."
    show chelsea with move
    show Damien Happy at right
    D "Hey, [pcname]. Here."
    show chelsea confused
    "You're surprised to see two brown lunch sacks in Damien's hands. He offers one to you."
    D "I had some extra time this morning and thought I'd surprise you. I hope you like stir fry. It should still be warm."
    "Sure enough, you pull out a variety of tupperware containers holding chicken stir fry, some vegetables with ranch, and what looks like a homemade brownie."
    show chelsea happy
    "Your heart melts at the sight of it; he went through all of this trouble for you?"
    if club == "track":
        pcname "Whoa, you seriously went all out! Thanks!"
    elif club == "cheer":
        pcname "Aw, aren't you sweet? Thanks, Damien!"
    elif club == "yearbook":
        show chelsea shocked
        pcname "Y-You didn't have to do all of this...!"
    show chelsea blank
    D "It's no problem. I was making it for myself this morning anyways and thought you might like some, too."
    show chelsea happy
    "You grin and take a bite of the stir fry; it's even better than you expected!"
    "You dig in without a second thought, suddenly reminded of just how empty your stomach is."
    pcname "Thank you so much!"
    "Damien grins back, pleased that you enjoy his cooking so much, and starts to consume his own meal."
    show chelsea blank
    show Damien Neutral at right
    "You sit in silence for a few moments as you eat, the flavors of the stir fry dancing along your taste buds, far better than anything you could have gotten at the cafeteria."
    show Damien Shocked at right
    D "Oh!"
    show Damien Neutral at right
    D "Speaking of food, are you free tonight? There's a new place that opened up down the street from my house and I was thinking we could try it out."
    show chelsea happy
    pcname "Yeah, that sounds great!"
    show Damien Happy at right
    D "Perfect! I'll pick you up at the cafe and we'll head straight over there when you're done working."
    show chelsea shocked
    "You feel your body tense as you freeze up, the bit of stir fry on your fork falling back into the container."
    "Crap. You still haven't told him about your change in job, and you {i}especially{/i} haven't told him {i}why{/i} you had to leave the cafe..."
    "You can only imagine how poorly Damien would react if he knew the whole truth about your situation, but it's not like you can keep your job at the bar a secret forever."
    show Damien Blank at right
    "Damien peers over at you, noticing the sudden shift at the table."
    show Damien Neutral at right
    D "What's wrong? Is everything okay, [pcname]?"
    show chelsea sad
    "His concern makes you feel even more guilty. You take a large bite of your brownie, stalling."
    if club == "track":
        show chelsea blank
        pcname "Yeah, I'm fine. I don't work at the cafe anymore, though. I guess I should have told you sooner, but it slipped my mind."
    elif club == "cheer":
        show chelsea blank
        pcname "Yeah, of course. I just, well, I don't work at the cafe anymore, actually."
    elif club == "yearbook":
        "You can't bring yourself to meet his gaze and instead drop your focus onto the homemade meal splayed out on the table."
        pcname "I-I... I don't work at the cafe anymore..."
    show Damien Shocked at right
    "You hope that he'll leave it at that and drop the subject but Damien's eyebrows shoot straight up in surprise."
    D "What? Why don't you work there anymore?"
    menu cafeconflict1_Damien_ConfessToCheating:
        "Tell the truth." if True:
            show Damien Blank at right
            "Looking into his eyes, you can't bring yourself to keep this from him anymore. Lying to him would only prolong the inevitable."
            "Taking a deep breath, you confess."
            if club == "track":
                show chelsea confused
                pcname "Some of the customers offered me extra money to do some stuff for them after hours and Emilia found out."
                pcname "She got pissed off and fired me."
            elif club == "cheer":
                pcname "Some of the customers wanted to spend some extra time together after hours and Emilia found out, so she fired me."
                show Damien Glare at right
                "Damien regards you suspiciously, his lips pressed into a tight line."
                D "Extra time together how?"
                show chelsea blank
                pcname "Oh. You know, just doing stuff for them."
            elif club == "yearbook":
                pcname "I-I... I was with some of the customers after the store closed... Emilia got mad and fired me."
                "The confidence- whatever there was of it- in your voice widdles down to a whisper, barely at hearing level."
                show Damien Glare at right
                D "What do you mean 'with' them?"
                pcname "J-Just... doing things for them..."
            show Damien Worry at right
            "You can feel the tension at the table building between you like a brick wall. You notice how Damien scoots a little further away from you, his body language no longer welcoming."
            D "...What kind of things were you doing for them, [pcname]?"
            show chelsea shocked
            "You open your mouth to respond but nothing comes out. How much can you tell him without going into specifics?"
            if club == "track":
                show chelsea happy
                "You look him head on, trying to emit as much bravado as you can muster. But in this situation, it isn't much."
                pcname "Just, y'know, hanging out with some guys. They asked me to give them some extra attention, so I did."
            elif club == "cheer":
                show chelsea blank
                "Your toss your hair to the side and try to play it off in a bored tone."
                pcname "Nothing much. You know how men are."
                "While you had hoped to leave it at that, it doesn't seem to be enough to satisfy him."
            elif club == "yearbook":
                show chelsea sad
                "You feel your body begin to tremble- the fear and guilt of Damien's reaction weighing down on you- as the blood creeps up to your cheeks in shame."
                pcname "I-I..."
                "The words die in your throat, the lack of an answer damning you. You look away and it's enough to confirm his suspicions."
            "The kindness Damien showed earlier as lunch is gone, replaced with a calm anger you've never seen from him before. He grips his tupperware container, hand shaking."
            show Damien Glare at right
            D "Be honest with me. Did you have sex with them, [pcname]?"
            "There's a moment of hesitation as you try to determine how to answer him. That hesitation is all he needs."
            show chelsea shocked
            show Damien Angry at right
            "Damien slams a hand down on the table, startling you. You open your mouth to scold him but stop when you see the tears brimming at his eyes."
            D "Are you serious, [pcname]? You cheated on me?! I can't believe you!"
            D "I thought you were better than that!"
            show chelsea sad
            "You flinch at the raw hurt in his voice. His pain hurts almost as bad as the words thrown at you."
            if club == "track":
                show chelsea confused
                pcname "Is it really cheating if they paid me, though?"
            elif club == "cheer":
                show chelsea confused
                pcname "But it's not like, really cheating if they paid me, right?"
            elif club == "yearbook":
                show chelsea sad
                pcname "I-I didn't think of it as cheating... T-They paid me..."
            show Damien Glare at right
            "Damien glares at you."
            D "Did you consent to it?"
            pcname "...Yes."
            "Damien shakes his head and stands up, collecting his lunch and yours."
            menu cafeconflict1_Damien_fixthings:
                "Try to fix things." if True:
                    "You reach out and grab onto his sleeve, halting him in place."
                    "You knew telling him the truth would hurt him, but you never thought it would get this bad."
                    if club == "track" or "cheer":
                        show chelsea shocked
                        pcname "Damien, just wait a second! Please! Let's talk about this."
                        show chelsea sad
                        pcname "I'm sorry. I shouldn't have done it."
                        pcname "Just hear me out-"
                    elif club == "yearbook":
                        pcname "D-Damien, wait! Please! I-I want to talk about this."
                        "Tears well up in your eyes as you clutch onto his sleeve. Damien continues to take your lunch away but doesn't push you off of him."
                        pcname "I-I'm sorry! I just want to talk... please..."
                    show Damien Angry at right
                    D "{i}No.{/i} Now get off of me."
                    "The ice in his voice is enough for you to drop your hand and pull away. He tosses the rest of your lunch and his into paper bags before yanking them away."
                    D "I don't want to hear whatever you have to say. I don't want to hear anything you have to say again."
                    D "Forget about dinner tonight. In fact, just forget about us- everything. It's done."
                    pcname "Damien..."
                    "He doesn't stay any longer to listen. Damien grabs his things and storms out of the cafeteria, angrier than you've ever seen him before."
                    hide Damien Angry with moveoutright
                    "You sit alone for the rest of lunch, your stomach growling and thoughts mulling over the end of your relationship."
                    $ damienrelate= "breakup"
                    hide chelsea with dissolve
                    jump events_end_period
                "Break up with him." if True:
                    show chelsea shocked
                    "As you watch him take the lunch he made for you, a realization occurs."
                    show chelsea blank
                    "Maybe the reason you went through with all those guys at the cafe anyways was because things with Damien just weren't working out. Maybe, in the end, this is a good thing."
                    if club == "track":
                        pcname "We need to break up."
                    elif club == "cheer":
                        show chelsea confused
                        pcname "I think we should break up."
                    elif club == "yearbook":
                        show chelsea sad
                        pcname "I-I want to break up."
                    "Damien pauses, a container of food halfway lifted from the table, but he doesn't look at you."
                    show Damien Neutral at right
                    "From the limited view of his face, you can see a brief flicker of surprise before he continues packing your lunches away."
                    if club == "track":
                        show chelsea confused
                        pcname "It's been a fun run, but look, shit happens. Maybe it would be better if we went our separate ways."
                    elif club == "cheer":
                        show chelsea confused
                        pcname "I mean, look at us. You're a nerd, I'm a cheerleader, you have a problem with me sleeping for money, and I have a problem with guys that won't talk things out."
                        pcname "We're two completely different people. I think it's best if we just split up."
                    elif club == "yearbook":
                        show chelsea sad
                        pcname "I... I just think... Maybe it isn't working out. W-We're too different..."
                    show Damien Shocked at right
                    "Damien stares at you incredulously, obviously surprised by your sudden suggestion, but nods."
                    show Damien Sad at right
                    D "Yeah. Finally. Something we can agree on."
                    show Damien Glare at right
                    show chelsea shocked
                    D "Good luck spreading STDs around the world."
                    "Damien throws the rest of your lunches into his bag, gives a mock salute, and abruptly leaves you and the cafeteria behind."
                    hide Damien Glare with moveoutright
                    show chelsea sad
                    "You sit there for a moment, a little stung by his final response, but let him go. It's obvious you two wouldn't have worked out anyway..."
                    "Still, you can't help but feel bad about it as your stomach growls throughout the rest of lunch."
                    hide chelsea with dissolve
                    $ damienrelate= "breakup"
                    jump events_end_period
        "Lie." if True:
            "Looking at the raw worry on his face, you can't bring yourself to tell him what really happened at the cafe; there's no way he would understand."
            "With no other options, you lie."
            if club == "track":
                show chelsea angry
                pcname "These bitches at the cafe got jealous because I was bringing in more tips than them, so they spread some nasty rumors about me to get me fired."
            elif club == "cheer":
                show chelsea confused
                pcname "Oh, you know how girls are. Some of the other maids were jealous because the guys would tip me more, so they told my boss some gross rumors and I was fired."
            elif club == "yearbook":
                show chelsea sad
                pcname "W-Well, um... Some of the girls there didn't like me so much... so they spread a lot of rumors to my boss and she fired me."
            show Damien Worry at right
            "You're almost relieved when Damien's gaze softens and he reaches an arm around your shoulders, hugging you close to his side."
            show chelsea happy
            "You try to push down the swell of guilt in your stomach and smile sadly back at him."
            show chelsea blank
            D "That's... That's awful, [pcname]. I'm so sorry to hear that."
            D "Did you try talking to your boss about it? Did they have any proof?"
            show chelsea sad
            pcname "I tried to talk to her, but it didn't matter. She had made up her mind already at that point."
            show Damien Sad at right
            "Damien frowns. He grips you a little tighter against him and strokes down your arm in a comforting gesture."
            D "I'm so sorry. I know you needed that job to pay rent and everything... do you know what you're going to do now?"
            show chelsea happy
            pcname "I got a new job offer, actually. I just started recently..."
            show Damien Happy at right
            D "Really? That's great news, [pcname]! Where is it?"
            pcname "The Cock and Crow."
            show Damien Shocked at right
            "Damien blinks, puzzled. He cocks his head to the side and reaches back to scratch behind his ear."
            D "...Isn't that a bar? Like, a really shady bar?"
            show chelsea blank
            "You shrug but there's no denying it; the bar does have its less than moral qualities."
            pcname "It is, but it pays even better than the cafe, and the hours are better, too."
            show Damien Worry at right
            "Damien looks hesitant to accept your explanation, but he reluctantly nods."
            show Damien Happy at right
            D "Huh. Well, as long as you're enjoying it and staying safe..."
            show Damien Worry at right
            D "You will be careful, won't you? I've heard some pretty bad things about that side of town, especially around that bar, and... well, it kind of worries me that you'll be there at night all the time now..."
            show chelsea embarrassed
            pcname "I'll be careful. I promise."
            show Damien Happy at right
            "He smiles wearily, unconvinced."
            D "Thanks."
            show Damien Neutral at right
            D "So, uh, I'll pick you up from there after you're done with work then."
            show chelsea happy
            pcname "That sounds great!"
            show Damien Happy at right
            "You both share an awkward grin before finishing the rest of your lunch."
            hide Damien Happy with dissolve
            hide chelsea with dissolve
            jump events_end_period

label cafeconflict1_Damien_afterwork:
    show chelsea at right with moveinright
    $ clothes = 'bar'
    "You finish wiping down the bar at work and look around the near empty room. It's been a slow night, but at least you're almost done."
    "Dan meanders out of his office and surveys the scene."
    show D Blank at left with moveinleft
    Dan "Hey, how about you wrap things up and we'll get you out of here early? I can take on the rest from here."
    show chelsea shocked
    pcname "Are you sure?"
    show chelsea blank
    show D Neutral at left
    Dan "Yeah, might as well. Slow night."
    show chelsea happy
    "You nod in thanks and quickly finish cleaning up the bar before counting your tips and clocking out."
    "Dan takes your spot behind the bar and waves farewell as you grab your things and leave."
    hide chelsea with dissolve
    hide D Neutral with dissolve
    show bg black with fade
    pause 0.5
    show chelsea with moveinright
    "As you step out of the door, your phone buzzes and you remember Damien's offer for dinner."
    show chelsea sad
    pcname "He probably needs the address again..."
    show chelsea blank
    "You pull out your phone and peer down at your texts."

    call screen TextingScene("Damien",
    [
        TextMessage("Hey, I'm really sorry, [pcname], but something came up and I can't go out tonight."),
        TextMessage("Aw. What happened?", sender = False),
        TextMessage("My mom really needs me to watch my little brother while she and my dad go out for their anniversary."),
        TextMessage("Oh. That sucks.", sender = False),
        TextMessage("Yeah. I'm really sorry, [pcname]. I promise I'll make it up to you!"),
        TextMessage("I have to go now, but be careful getting home, okay?"),
        TextMessage("Goodnight <3")
    ])

    show chelsea sad
    "You frown and tuck your phone away. You had been looking forward to going out with him tonight, of course, but you can understand him staying home for his parents' sake."
    "No, what's really bothering you is the guilt festering inside of your chest."
    "Damien is such a sweet boy, willing to drop everything to help others out. And he trusts you so completely... And yet you lied to him."
    show chelsea shocked
    "Not just lied to him, but you've {i}cheated{/i} on him."
    show chelsea sad
    "You know he doesn't deserve this, and yet... you can't help yourself. There's just something about fucking other men that really gets you going..."
    "And not to mention it pays better than anything you've ever done before."
    "You sigh and begin the trek home. Damien is a problem you'll leave for another day."
    hide chelsea with dissolve
    jump events_end_period

label cafeconflict1_VioletSub:
    show chelsea at left with moveinleft
    $ clothes = 'school'
    show V SubSchool Worried at right with moveinright
    "As usual, Violet gets your lunch for you."
    V "Can I get you anything else...?"
    pcname "No, sit down."
    "Nodding, Violet takes a seat across from you and waits."
    show chelsea confused
    "You check over your tray, making sure she got everything you asked for."
    show chelsea happy
    pcname "It looks good."
    show V SubSchool Happy at right
    "She smiles, still waiting for you to start eating."
    show chelsea blank
    "You take your time, arranging your utensils and looking at each item carefully."
    "Slowly, you pick up your fork and spear a roasted potato."
    "Raising it to your lips, you hesitate a moment."
    show V SubSchool Worried at right
    "Violet waits. Her eyes are focused on the table, but you can feel the weight of her full attention on you."
    "The air feels charged with anticipation."
    "The potato is salty and oily on your tongue. You smash it between your teeth, the tension shattering like a glass globe walling the two of you off from the rest of the students."
    show V SubSchool Happy at right
    "Violet picks up her own fork and begins eating."
    if club == "track":
        show chelsea confused
        pcname "Doing anything tonight?"
    elif club == "cheer":
        show chelsea blank
        pcname "Do you have any plans tonight?"
    elif club == "yearbook":
        show chelsea sad
        pcname "Are you... doing anything tonight?"
    show V SubSchool Blank at right
    V "Actually..."
    show V SubSchool Worried at right
    V "There's a movie I wanted to see."
    pcname "Which one?"
    "She wrinkles her nose."
    show V School Annoyed at right
    V "The Revenger Squad."
    show chelsea confused
    pcname "I didn't think you liked superhero movies?"
    "She rolls her eyes."
    V "My cousin got a small part and won't stop talking about it."
    show V School Smile at right
    V "I just want to see how {i}awful{/i} it is."
    if club == "track":
        show chelsea laugh
        pcname "That sounds more like you."
    elif club == "cheer":
        show chelsea happy
        pcname "Oooh, that makes sense."
    elif club == "yearbook":
        show chelsea shocked
        pcname "Oh. O-okay."
    show V SubSchool Worried at right
    show chelsea blank
    V "So... I was hoping we could go together? If that's okay with you?"
    "She looks at you hopefully."
    if club == "track":
        show chelsea happy
        pcname "You {i}have{/i} been on your best behavior..."
    elif club == "cheer":
        show chelsea happy
        pcname "Hmmm... I guess we {i}could{/i}..."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "I... I suppose so..."
    pcname "I have work, but we can go right after."
    show V SubSchool Happy at right
    "Grinning, she pulls out her phone."
    V "Great, I'll buy the tickets now and pick you up at the cafe. Do you need me to bring a change of clothes for you?"
    show chelsea shocked
    if club == "track":
        pcname "Oh. Um..."
    elif club == "cheer":
        pcname "Uhhh..."
    elif club == "yearbook":
        pcname "I... That is..."
    show chelsea sad
    pcname "I don't work at the cafe anymore."
    show V School Suprised at right
    "Her hand drops to the table as she looks up in surprise."
    V "What...?"
    show V SubSchool Sad at right
    if club == "track":
        show chelsea laugh
        "You laugh."
        pcname "Yeah, I work at the Cock and Crow Lounge now."
    elif club == "cheer":
        show chelsea laugh
        "You giggle."
        show chelsea happy
        pcname "Did I really forget to tell you? I work at the Cock and Crow Lounge now."
    elif club == "yearbook":
        show chelsea embarrassed
        "You giggle nervously."
        pcname "I... must not have told you. I work at the Cock and Crow Lounge now."
    show V School Suprised at right
    V "What!? What happened?"
    menu cafeconflict1_VioletSub_newjob:
        "Tell the truth." if True:
            if club == "track":
                show chelsea angry
                pcname "It was stupid..."
            elif club == "cheer":
                show chelsea confused
                pcname "It's not a big deal..."
            elif club == "yearbook":
                show chelsea sad
                pcname "I just... I..."
            show chelsea blank
            pcname "Tips were awful and some of the customers offered to pay me for helping them out after hours."
            "You shrug."
            if club == "track":
                show chelsea confused
                pcname "Emilia found out and overreacted."
            elif club == "cheer":
                show chelsea angry
                pcname "Emilia found out and she was {i}such{/i} a {i}bitch{/i} about it."
            elif club == "yearbook":
                show chelsea sad
                pcname "Emilia... wasn't very happy."
            pcname "So I quit."
        "Lie." if True:
            if club == "track":
                show chelsea blank
                pcname "I was making a lot in tips and some of the other girls didn't like it."
                show chelsea angry
                pcname "They made up some shit and I got in trouble."
            elif club == "cheer":
                show chelsea happy
                pcname "I was making a {i}lot{/i} in tips and some of the other girls were jealous."
                show chelsea sad
                pcname "They lied to Emilia and she confronted me."
            elif club == "yearbook":
                show chelsea sad
                pcname "I... made a lot from tips and the other girls were jealous."
                pcname "They tried to get me in trouble and Emilia believed them."
            pcname "I was upset, so... I quit."
    show V SubSchool Sad at right
    V "And you... didn't tell me?"
    show V School Suprised at right
    V "Not that you had to! I just... I was surprised."
    show chelsea blank
    show V SubSchool Sad at right
    pcname "It's not important. The bar pays better anyway and I really like it there."
    show chelsea confused
    pcname "Just forget about it, okay? You can pick me up from the bar and we'll go to the movies."
    "She still looks upset, but she nods."
    show chelsea happy
    pcname "So you'll wear something nice, right?"
    show V SubSchool Happy at right
    "As expected, she smiles."
    V "Of course I'll wear something nice for you..."
    show V SubSchool Blank at right
    "You finish your lunch while she talks about the new outfits she recently bought."
    "By the time lunch ends, she seems fine with your job change."
    hide V SubSchool Neutral with dissolve
    hide chelsea with dissolve
    jump events_end_period

label cafeconflict1_VioletSub2:

    show chelsea at right with moveinright
    $ clothes, hair = casualwear
    "As you leave the bar, you see Violet's car."
    show V SubCasual Happy at left with moveinleft
    "She jumps out and opens your door for you, smiling while you get inside."
    show V SubCasual Worried at left
    "Glancing nervously at the bar, she closes your door and walks back to the driver's side."
    "Settling in, she puts the car in drive and starts toward the theatre."
    show bg CityE with dissolve
    show V Casual Blank at left
    V "It doesn't {i}look{/i} like a nice place to work, does it?"
    show chelsea confused
    "Annoyed, you scowl at her."
    if club == "track":
        pcname "Good thing you don't work there, then."
    elif club == "cheer":
        pcname "It's not really your problem, is it?"
    elif club == "yearbook":
        pcname "That... Just forget about it."
    show chelsea angry
    pcname "If you bring it up again you'll be punished."
    show V Casual Pout at left
    "Her face tightens, but she doesn't say anything else."
    show chelsea confused
    "You're annoyed - she's usually so talkative - but she's doing as you asked, so you don't complain."
    show chelsea blank
    pcname "So who does your cousin play?"


    show V SubCasual Happy at left
    V "Oh! She's a minor character, but she's got quite a few lines, I guess."
    show V SubCasual Blank at left
    V "I can't remember her {i}name{/i} though... It's something stupid like Jane or Mary."
    "By the time you pull up to the movie theatre, she's talking easily again."
    "She flashes her digital tickets at the ticket stand impatiently."
    "Theatre Employee" "Theatre 4, ladies."
    show chelsea happy
    pcname "Thanks!"
    "You look for the signs for Theatre 4, noticing how empty the theatre is."
    pcname "Looks like we're that way."
    "You point down the hallway to the left and Violet nods."
    show V SubCasual Blank at left
    V "Do you want any snacks?"
    menu cafeconflict1_VioletSub2_popcorn:
        "Popcorn!" if True:
            show V SubCasual Sad at left
            "She winces."
            V "That's a lot of butter, but if that's what you want..."
            "You wait while she buys the popcorn, then make your way to Theatre 4 together."
            hide V SubCasual Sad with moveoutleft
            hide chelsea with moveoutright
        "Just soda." if True:
            show V SubCasual Worried at left
            V "Diet, right?"
            if club == "track":
                show chelsea happy
                show V SubCasual Sad at left
                pcname "C'mon, a little sugar won't kill you!"
            elif club == "cheer":
                show chelsea happy
                show V SubCasual Happy at left
                pcname "Right. Don't need all that sugar!"
            elif club == "yearbook":
                show chelsea confused
                show V SubCasual Happy at left
                pcname "Um, sure."
            "She orders a drink for you both to share, then follows you to Theatre 4."
            hide V SubCasual Happy with moveoutleft
            hide V SubCasual Sad with moveoutleft
            hide chelsea with moveoutright
        "A little of everything." if True:
            show V Casual Suprised at left
            "Her eyes widen."
            V "But the butter, and the sugar, and..."
            if club == "track":
                show chelsea confused
                pcname "Calling me fat?"
                show V SubCasual Worried at left
                V "No! Of course not! But..."
            elif club == "cheer":
                show chelsea confused
                pcname "So? We can cheat a little, right?"
                show V SubCasual Sad at left
                V "Right..."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "...flavor?"
                show V SubCasual Sad at left
                "She sighs."
            show V SubCasual Sad at left
            V "I'm going to have to go to the gym tomorrow..."
            "She follows you to Theatre 4 with arms full of candy, popcorn, and drinks."
            hide V SubCasual Sad with moveoutleft
            hide chelsea with moveoutright
    show chelsea at left with moveinright
    $ clothes, hair = casualwear
    show V SubCasual Blank at right with moveinright
    "The room is mostly empty, so you take a seat toward the middle and settle in."
    show chelsea shocked
    pcname "I'm surprised there aren't more people here..."
    show V SubCasual Blank at right
    V "Oh, it's been out for a few weeks now, so everyone's probably seen it already."
    show chelsea confused
    pcname "Really? I guess we're late to the party, huh?"
    show V SubCasual Happy at right
    "She glances over at you, smiling impishly."
    V "I don't mind."
    show chelsea happy
    "You smile back, running your hand up her leg."
    pcname "I don't mind either..."
    show V Casual Suprised at right
    show chelsea shocked
    "Your flirting is interrupted by a poorly-timed yawn."
    show V SubCasual Sad at right
    V "Am I... boring you?"
    if club == "track":
        show chelsea blank
        pcname "Just a long night at work; don't worry about it."
    elif club == "cheer":
        show chelsea happy
        pcname "Not at all. Just tired from work."
    elif club == "yearbook":
        show chelsea sad
        pcname "No, I... I'm just tired. From work."
    "Violet takes a deep breath and looks away."
    show V Casual Blank at right
    V "[pcname]... I know you don't want to talk about it, but is a bar {i}really{/i} a good place to--"
    if club == "track":
        show chelsea angry
        show V Casual Suprised at right
        pcname "That's it. Enough!"
    elif club == "cheer":
        show chelsea confused
        show V Casual Pout at right
        pcname "This {i}again{/i}?"
    elif club == "yearbook":
        show chelsea confused
        show V Casual Pout at right
        pcname "I told you we're done talking about that..."
    "The lights dim as the previews begin."
    show chelsea blank
    show V Casual Pout at right
    "Shaking your head, you sigh."
    pcname "On your knees."
    show V Casual Annoyed at right
    V "What? The floor is {i}disgusting{/i}."
    if club == "track":
        show chelsea angry
        show V Casual Pout at right
        pcname "I didn't ask."
    elif club == "cheer":
        show chelsea confused
        show V Casual Pout at right
        pcname "Are you {i}refusing{/i} me?"
    elif club == "yearbook":
        show chelsea confused
        pcname "Then you shouldn't have brought it up again."
        show V Casual Pout at right
    pcname "On your {i}knees{/i}."
    show chelsea blank
    "Her mouth moves but no words come out."
    show V Casual Annoyed at right
    "Composing herself, she slowly sinks to the theatre floor, glaring up at you."
    show chelsea confused
    pcname "Well you don't {i}look{/i} sorry."
    show V Casual Blank at right
    V "I--"
    if club == "track":
        show chelsea angry
        pcname "Shut up."
    elif club == "cheer":
        show chelsea angry
        pcname "Enough."
    elif club == "yearbook":
        show chelsea confused
        pcname "Shh."
    pcname "I didn't tell you to speak."
    show V Casual Suprised at right
    "Your sternness surprises her into silence."
    show chelsea blank
    pcname "Better, but..."
    show V SubCasual Worried at right
    "Reaching under your skirt, you pull your panties off and spread your legs."
    show chelsea happy
    if club == "track":
        pcname "Well? Better hurry, or you'll miss the movie."
    elif club == "cheer":
        pcname "Maybe this will keep you quiet."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Well...? "
    show V Casual Blank at right
    "Her eyes move to your thighs, her tongue darting over her lips as she moves between them."
    "You slide forward, put your feet against the chair in front of you, and lean back."
    "Her shoulders disappear under your thighs. In the dim lighting, all you can see is her eyes peaking over your pubic mound."
    show chelsea embarrassed
    "Her tongue runs slowly up one side of your labia, leaving a cool, wet trail of saliva in its wake."
    "You shiver as she licks the other side, her tongue unbearably close to your slit."
    "Eyes fixed on your face, she draws her tongue up your slit as gently as possible, without ever dipping inside."
    menu cafeconflict1_VioletSub2_hurry:
        "Tell her to stop teasing you." if True:
            if club == "track":
                show chelsea angry
                pcname "Violet... Stop teasing me!"
            elif club == "cheer":
                show chelsea confused
                pcname "I don't think you're taking this seriously."
            elif club == "yearbook":
                show chelsea sad
                pcname "D-don't tease me like that."
            show chelsea happy
            show V SubCasual Happy at right
            "Her eyes crinkle; though you can't see it, you know she's smiling."
            show V Casual Smile at right
            "Pressing her tongue between your labia, she licks your slit deeply."
        "Let her do what she wants." if True:
            "She runs her tongue over your labia a few more times, until you're trembling with anticipation."
            "Finally, she presses her tongue inside, licking deeply."
    show chelsea sad
    pcname "Ohhh..."
    show chelsea embarrassed
    "Pressing your hand to your mouth, you stifle your moan and tilt your head back."
    "Violet wraps her arms around your thighs, pulling them slightly further apart to give herself more access."
    "Her tongue plunges in and out of your cunt, lapping slowly and deeply."
    "Each time she exhales, her breath rushes over your clit, leaving it throbbing with the need for contact."
    "Her fingers dig into your thighs as she presses her face closer, thrusting her tongue deeper inside of you."
    "Her tongue wriggles within you; you press your hand tighter to your mouth, stifling another moan."
    "The throbbing in your clit is almost painful now; you need {i}contact{/i}."
    "As if sensing this, Violet begins stroking your cunt with her tongue again - this time ending each stroke on your clit."
    "Powerful waves of pleasure radiate from the tiny nub each time her tongue flicks across it."
    menu cafeconflict1_VioletSub2_hair:
        "Keep your hand on your mouth." if True:
            "The pleasure is overwhelming; you want to moan - to cry out - but you don't want anyone to hear you, so you keep your hand pressed tightly to your mouth."
            "It helps, but it's almost not enough. Especially when her lips fasten around your clit, sucking gently."
            "Despite the gentle suction, it feels like every nerve in your body is being sucked to that single point."
            "Like a black hole, sucking everything into it, your clit becomes the sole focus of your entire body."
            show chelsea sad
            "Then it collapses in on itself and bursts wide - pleasure pulses from your clit like a blast of energy from your pussy to your fingertips."
            "Your eyes squeeze shut, your thighs tightening as your orgasm courses through you."
            "Eventually you go limp. Your hand slips from your mouth and you gasp for breath, barely feeling it when her lips release your clit."
        "Grab her hair." if True:
            show V Casual Suprised at right
            "Both hands sink into her hair, twisting the dark locks between your fingers and pulling her closer to you."
            "She moans as you pull her tight against you, her tongue focused entirely on your clit."
            show V Casual Smile at right
            "She flicks it back and forth until bolts of pleasure shoot out from your clit."
            "Your legs stiffen, clenching your thighs tight around her face; your hands clench in her hair, pressing her face even tighter against you."
            "Mouth uncovered, you can't muffle your gasps and cries of pleasure."
            show chelsea sad
            "Your orgasm surges through you, electrifying your limbs and leaving you thrashing in your seat."
            "Eventually you go limp. Your hands slipping from her hair as you gasp for breath, barely feeling it when her lips release your clit."
    show chelsea embarrassed
    show V SubCasual Happy at right
    "You blink your eyes open; Violet watches you, licking your juices from her lips and smiling."
    "You let her sit there while you pull your panties back on and readjust yourself in your seat."
    show chelsea blank
    pcname "The movie's already started. Get in your seat."
    show V SubCasual Blank at right
    "Violet does as she's told, sitting quietly for the rest of the movie."
    "Filled with a familiar post-sex heaviness, you can barely focus on the movie."
    show chelsea embarrassed
    "Your clit pulses with remembered pleasure; your nipples press hard against the fabric of your shirt."
    "By the time the movie ends, you almost feel normal again - except for the lingering wetness between your legs."
    show chelsea blank
    "As the credits roll, you stand and stretch before walking out into the lobby."
    hide V SubCasual Sad with moveoutright
    hide chelsea with moveoutright
    pause 0.5
    show chelsea blank at left with moveinright
    $ clothes, hair = casualwear
    show V SubCasual Blank at right with moveinright
    "You turn to look at Violet as you walk."
    show chelsea happy
    pcname "So... What did you think of the movie?"
    show V SubCasual Worried at right
    "She smiles, cheeks pink, and looks down."
    V "I... Didn't pay much attention, honestly."
    show chelsea confused
    pcname "What? Not even to your cousin?"
    show V SubCasual Happy at right
    "She laughs, still not quite meeting your eyes."
    show V SubCasual Blank at right
    V "I could... smell you. On my lips."
    if club == "track":
        show chelsea laugh
        pcname "Yeah? You liked that?"
    elif club == "cheer":
        show chelsea laugh
        pcname "Could you really?"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "You... could?"
    show V SubCasual Blank at left with moveinright
    "She darts past you to open the door for you."
    "As you cross the threshold, her eyes meet yours and she nods, a smile slowly spreading across her lips."
    show V SubCasual Happy at right with moveinleft
    V "I still can."
    show chelsea embarrassed
    "Your breath catches in your throat; you suddenly want her {i}so much{/i}."
    show V SubCasual Worried at right
    V "May I... give you a ride home?"
    show chelsea happy
    pcname "Of course."
    "You walk to her car and wait. She opens the car door and shuts it behind you."
    "Starting the car, she puts it in drive and pulls onto the road."
    show chelsea laugh
    pcname "Well? Aren't you going to thank me?"
    show V SubCasual Worried at right
    V "Thank you?"
    show chelsea confused
    if club == "track":
        pcname "For letting you eat my pussy."
    elif club == "cheer":
        pcname "For letting you go down on me."
    elif club == "yearbook":
        pcname "For letting you...?"
    show V Casual Suprised at right
    V "Oh!"
    show V SubCasual Happy at right
    "She grins."
    V "Thank you for letting me eat your pussy, [pcname]."
    if club == "track":
        show chelsea happy
        "You can't help but grin back."
    elif club == "cheer":
        show chelsea happy
        "Her words send a rush of warmth between your legs."
    elif club == "yearbook":
        show chelsea embarrassed
        "Your cheeks flush."
    show V SubCasual Blank at right
    pcname "And you're going to apologize."
    show V Casual Suprised at right
    "Her smile fades immediately."
    V "What!?"
    show chelsea blank
    pcname "For disobeying me."
    show V SubCasual Sad at right
    V "I... But I just..."
    show chelsea confused
    if club == "track":
        pcname "But nothing. Now, your apology?"
    elif club == "cheer":
        pcname "Clearly you enjoyed your punishment too much..."
    elif club == "yearbook":
        pcname "No buts. You're sorry, right?"
    show V Casual Annoyed at right
    V "Hmph! I'm sorry, okay? I shouldn't have questioned you."
    "She parks her car outside of your apartment and sinks back against her seat."
    show V SubCasual Sad at right
    V "I just... I don't like that place."
    V "But if you do, then that's good. I don't work there."
    show V SubCasual Worried at right
    V "I won't bother you about it anymore."
    show chelsea happy
    pcname "Thank you."
    show V SubCasual Blank at right
    "She turns to you, smiling faintly."
    pcname "Now give me a kiss goodbye."
    show V SubCasual Happy at right
    "Her smile deepens as she leans toward you, pressing her lips to yours."
    "She kisses you deeply and, though her taste is all her own, you can still smell yourself on her lips."
    hide V SubCasual Happy with dissolve
    hide chelsea with dissolve
    jump events_end_period

label cafeconflict1_VioletDom:
    show chelsea at left with moveinleft
    "As you change out of your uniform, your phone vibrates."

    call screen TextingScene("Violet", [TextMessage("I'm outside waiting for you")])

    "Your heart thuds painfully; you didn't tell Violet about your new job!"

    call screen TextingScene("Violet",
    [
        TextMessage("I'm not at the cafe. I'm at the Cock and Crow Lounge", sender = False),
        TextMessage("What????"),
        TextMessage("Omw")
    ])

    show chelsea sad
    "You put your phone away and sigh."
    "You're {i}definitely{/i} going to be in trouble."
    "Walking outside, you wait at the curb until Violet pulls up with her window rolled down."
    show V Casual Blank at right
    V "Get in!"
    show chelsea shocked
    "You hesitate - you're supposed to drive her around. Does she want you to open her door?"
    show V Casual Annoyed at right
    V "What are you waiting for? Get in the car!"
    show chelsea sad
    "Doing as she asks, you get into the passenger's side, barely shutting the door before she peels out."
    V "What the hell are you doing at a {i}bar{/i}, [pcname]?"
    menu cafeconflict1_VioletDom_newjob:
        "Tell the truth." if True:
            if club == "track":
                show chelsea confused
                pcname "It was stupid..."
            elif club == "cheer":
                show chelsea confused
                pcname "It's not a big deal..."
            elif club == "yearbook":
                show chelsea sad
                pcname "I just... I..."
            pcname "Tips were awful and some of the customers offered to pay me for helping them out after hours."
            "You shrug."
            if club == "track":
                show chelsea confused
                pcname "Emilia found out and overreacted."
            elif club == "cheer":
                show chelsea angry
                pcname "Emilia found out and she was {i}such{/i} a {i}bitch{/i} about it."
            elif club == "yearbook":
                show chelsea sad
                pcname "Emilia... wasn't very happy."
            show chelsea blank
            pcname "So I quit."
        "Lie." if True:
            if club == "track":
                pcname "I was making a lot in tips and some of the other girls didn't like it."
                pcname "They made up some shit and I got in trouble."
            elif club == "cheer":
                pcname "I was making a {i}lot{/i} in tips and some of the other girls were jealous."
                pcname "They lied to Emilia and she confronted me."
            elif club == "yearbook":
                pcname "I... made a lot from tips and the other girls were jealous."
                pcname "They tried to get me in trouble and Emilia believed them."
            pcname "I was upset, so... I quit."
    show V Casual Blank at right
    V "Why didn't you tell me when it happened?"
    show V Casual Annoyed at right
    V "{i}Especially{/i} before you took a job somewhere like {i}that{/i}."
    show chelsea sad
    show V Casual Pout at right
    "You try to think of something to calm her, but she keeps going."
    show V Casual Annoyed at right
    V "I was {i}going{/i} to pick you up after work so we could go see a movie. But it's already started now."
    show V Casual Pout at right
    if club == "track":
        pcname "Look, I'm sorry, I--"
    elif club == "cheer":
        pcname "I {i}know{/i} I should've told you. I meant to, I just--"
    elif club == "yearbook":
        pcname "I... I'm sorry, I--"
    show V Casual Annoyed at right
    V "You're {i}sorry{/i}? Not sorry enough!"
    "With one hand on the wheel, she rifles through her purse with the other."
    V "Where is it? It's too big to lose... There!"
    "Pulling out a pink rabbit-style vibrator, she tosses it onto your lap."
    V "Well? You know how to use one, right?"
    if club == "track":
        show chelsea confused
        pcname "Yeah...?"
    elif club == "cheer":
        show chelsea confused
        pcname "Of course..."
    elif club == "yearbook":
        show chelsea shocked
        pcname "Uh... I..."
    show V Casual Pout at right
    V "You're going to use it until we get to your apartment, but you're {i}not{/i} allowed to cum."
    V "Understood?"
    show chelsea sad
    "Nodding, you kick off your shoes and pull your shorts off."
    "The car comes to a stop at a traffic light; you can hear people talking as they walk past on the sidewalk."
    "Tilting your seat back, you lay down - hopefully out of sight - and peel your panties off too."
    "The vibrator is large. Firm, but pliable."
    "There is a band of beads inside the shaft, a protrusion that will rest against your clit when fully inserted, and a series of buttons along the base."
    show V Casual Blank at right
    V "Well? Are you {i}sure{/i} you know what you're doing?"
    if club == "track":
        show chelsea confused
        pcname "Yes, Violet."
    elif club == "cheer":
        show chelsea confused
        pcname "Just getting ready..."
    elif club == "yearbook":
        show chelsea shocked
        pcname "Y-yes..."
    show chelsea blank
    "Lowering the vibrator, you slide the tip between your labia, running it up and down your opening."
    "When it's well lubed, you press it inside, allowing it's width to stretch you wide."
    show chelsea embarrassed
    "Your breath comes in short huffs as you work the shaft in and out, taking more each time."
    show V Casual Smile at right
    V "There you go..."
    "After a few more thrusts - each stretching you wider than the last - the protrusion presses against your clit; it's in as far as it will go."
    show V Casual Annoyed at right
    V "Aren't you going to turn it on?"
    "You try one of the buttons and the vibrator hums to life, trembling in your hand."
    show chelsea shocked
    pcname "Oh!"
    show chelsea embarrassed
    "Working the shaft in and out, you slowly fuck yourself."
    show V Casual Smile at right
    V "Ohh..."
    "Violet shifts in her seat, her eyes darting between the road and your pussy."
    V "That's it..."
    "You fuck yourself faster, eager for {i}more{/i} - more sensation and more praise."
    V "That's not all it does. Try another button."
    "Following her direction, you hit another button."
    show chelsea shocked
    "This time the band of beads begins spinning. Each rotation presses a new bead against your g-spot."
    pcname "Ah!"
    show chelsea sad
    "Another button. This one increases the vibration in the shaft."
    pcname "Ahhh..."
    show chelsea shocked
    "Another button. The beads spin faster, massaging your g-spot."
    pcname "I... I can't..."
    show chelsea embarrassed
    "Moving the shaft back and forth, you fuck yourself harder and faster."
    "Each movement moves the band of beads back and forth across your g-spot."
    "The pleasure hits you in waves, ebbing and flowing each time you thrust it inside of you."
    show chelsea sad
    "You're too close to cumming; you hold it inside of you, breathing deeply until you regain control."
    "The car stops and starts as Violet drives through the city. At one stop light, Violet laughs."
    V "Look at all the people around us. Do you think they know what you're doing over there?"
    show chelsea embarrassed
    "You resist the urge to look out the window; you don't want anyone to see you right now."
    "The vibrator whirs, the beads massaging your g-spot, the nub on top pressing against your clit."
    "The light turns green and Violet makes another turn. She's clearly taking a longer route or you'd be home by now."
    show V Casual Blank at right
    V "[pcname], that's a long enough break. I'm getting bored."
    show chelsea sad
    "Moaning, you pull the vibrator out and thrust it back into you."
    "You fuck yourself with it over and over, each time getting close to climax and pulling yourself back from the edge."
    "Finally, Violet pulls up to your apartment and parks the car."
    show V Casual Smile at right
    V "Do you want to cum now?"
    menu cafeconflict1_VioletDom_cum:
        "Beg to cum." if True:
            if club == "track":
                pcname "Please, Violet, I really want to cum... Fuck..."
            elif club == "cheer":
                pcname "Please, Violet... I... I really, really want to..."
            elif club == "yearbook":
                pcname "I... P-please, Violet, I... I..."
            "Reaching over, she pulls your hand off the vibrator and grabs hold of it."
            V "I don't think you deserve to cum yet. You've been very, {i}very{/i} bad."
            "She pulls the vibrator out of you, wiping it on your leg and slipping it into a silk bag."
            "You nearly sob with frustration. Your clit throbs and your pussy aches to be filled again."
            "She slips the bag back into her purse and turns toward you."
            show V Casual Annoyed at right
            V "You can't just {i}forget{/i} to tell me about important things like changing your job."
            V "And you certainly can't waste my time like you did tonight. Do you understand?"
            "Still hopeful that she'll change her mind and let you cum, you nod immediately."
            show chelsea embarrassed
            pcname "Yes, Violet."
            show V Casual Smile at right
            V "Good. Now... Since you've been {i}so{/i} naughty, you're going to go inside and be a good girl."
            V "You won't cum until I give you permission. It might be tomorrow. It might be next week."
            show V Casual Annoyed at right
            show chelsea sad
            V "If you fail, your punishment will be {i}much{/i} worse. Do you understand?"
            "You nod miserably."
            pcname "Yes, Violet."
            show V Casual Smile at right
            V "Good. Now go."
            "You slip your panties and shorts back on and get out of the car."
            hide V Casual Smile with moveoutright
            "Your panties are drenched by the time you reach your apartment."
            show chelsea blank
            $ clothes = 'naked'
            "Sighing, you strip and take a hot bath. The water feels good - and it helps you relax - but you can't stop wondering how long Violet will make you wait to cum."
            "To distract yourself, you tidy up the apartment and make a shopping list."
            if catadopt:
                "You play with [kittenname], and fill up his water bowl."
            "For a while, you forget about Violet's command. But as you slip into bed, you remember."
            show chelsea sad
            "Tossing and turning, you wonder if you'll ever fall asleep."
            "You imagine yourself as she saw you, legs spread on the car seat, vibrator buried in your cunt."
            "You can almost hear the whir of the beads, spinning against your g-spot..."
            show chelsea embarrassed
            "Nipples stiffening against your sheets, your body responds to your thoughts."
            "The response is almost immediate; your clit throbbing almost as hard as in the car."
            "You're so horny that you almost believe you could orgasm without touching yourself."
            show chelsea shocked
            "A sudden noise breaks you free from your thoughts. Your phone glows faintly on your desk."

            call screen TextingScene("Violet",
            [
                TextMessage("[pcname]"),
                TextMessage("Yeah?", sender = False),
                TextMessage("I just came SO hard"),
                TextMessage("I was thinking about the way you fucked yourself in my car"),
                TextMessage("So I got out that vibrator you were using"),
                TextMessage("And I fucked myself with it while I thought about you using it")
            ])

            "Your pussy clenches at the thought; she masturbated while imagining you?"

            call screen TextingScene("Violet",
            [
                TextMessage("I had the best orgasm I've ever had"),
                TextMessage("No joke"),
                TextMessage("I'm glad", sender = False),
                TextMessage("So I was thinking"),
                TextMessage("Since I'm feeling so generous now"),
                TextMessage("I'll let you off easy this time. I want you to cum right now"),
                TextMessage("Text me when you're done")
            ])

            show chelsea embarrassed
            "You don't hesitate before dropping the phone to the bed and letting your hands run over your body."
            "Your nipples are so hard they ache, and your pussy is wetter than you've ever felt it."
            show chelsea shocked
            "But it's your clit that you focus on; the moment it meets your fingers you feel a jolt of pleasure."
            show chelsea embarrassed
            "You rub the nub in circles, your pace quickening as the pleasure grows exponentially."
            "As you do, you imagine Violet lying in her bed, the vibrator buried in her pussy while she whispers your name."
            V "{i}...[pcname]...{/i}"
            "You can practically hear her voice, breathless with pleasure, and the sounds of the vibrator squelching and humming as she fucks herself with it."
            show chelsea sad
            "It's too much; you cry out as your orgasm crashes over you."
            "Moaning and twitching, all of your attention is focused on the intense pleasure overcoming your body."
            show chelsea embarrassed
            "As it fades, you roll over. Your pleasure-heavy limbs are nearly useless, but you manage to pick up your phone."

            call screen TextingScene("Violet",
            [
                TextMessage("Thank you Violet", sender = False),
                TextMessage("You came already? That was quick"),
            ])

            if club == "track":
                call screen TextingScene("Violet", [TextMessage("I really needed to", sender = False)])
            elif club == "cheer":
                call screen TextingScene("Violet", [TextMessage("I thought of you", sender = False)])
            elif club == "yearbook":
                "You feel yourself flush with embarrassment."
                call screen TextingScene("Violet", [TextMessage("Yeah", sender = False)])

            call screen TextingScene("Violet",
            [
                TextMessage("Don't think that because I was generous this time it means I wasn't mad"),
                TextMessage("Next time I'll make your punishment MUCH worse"),
                TextMessage("Now I'm going to bed. Good night"),
                TextMessage("Good night Violet", sender = False)
            ])

            show chelsea happy
            "You let your hand drop back onto the bed, not even bothering to put your phone back on the desk."
            "The pleasure has mostly faded, replaced by a heavy peacefulness."
            "You drift easily to sleep."
            jump endday
        "Only if she wants you to." if True:
            show chelsea sad
            if club == "track":
                pcname "Only if you think I've learned my lesson."
            elif club == "cheer":
                pcname "Only if {i}you{/i} want me to..."
            elif club == "yearbook":
                pcname "If you... want me to..."
            show V Casual Smile at right
            "Violet smiles down at you."
            V "That's right. Your desires don't matter at all."
            show V Casual Blank at right
            V "If I want you to wait days - or even weeks - you will."
            show chelsea shocked
            "Her words draw a despairing moan from you as you imagine waiting weeks to cum again."
            show V Casual Smile at right
            V "Don't worry, I can tell that's not necessary today."
            "She runs her hand under your shirt, pinching your nipple and twisting it between her fingers."
            V "You've been a good girl. Go ahead and cum."
            show chelsea embarrassed
            "You thrust the toy in and out of your cunt, frantically fucking yourself while Violet plays with your nipples."
            "Your pussy and clit are so overstimulated, they're almost numb to the sensations now."
            "But her fingers twisting and pulling at your nipples leave you almost blind with pleasure."
            show chelsea sad
            "It's enough to tip you over the edge - your pussy clenches hard around the vibrator, the beads assaulting your g-spot as you thrash on your seat."
            "Your orgasm hits you hard and fast, sending waves of unbearable pleasure over you almost in an instant."
            "Almost as soon as it begins, though, it's over."
            show chelsea shocked
            "Violet switches the vibrator off and pulls it free of your cunt."
            show chelsea sad
            "Wiping it on your leg, she slips it into a silk bag and puts it back in her purse."
            "She waits a few minutes to speak, until your breathing starts to normalize."
            show V Casual Pout at right
            V "So next time something important happens, you'll tell me right away so you don't waste my time again like you did tonight?"
            pcname "Yes, Violet."
            show V Casual Blank at right
            V "Good. Now, thank me for letting you cum."
            show chelsea embarrassed
            if club == "track":
                pcname "Thank you, Violet."
            elif club == "cheer":
                pcname "Thank you for letting me cum, Violet."
            elif club == "yearbook":
                pcname "Th-thank you, Violet."
            show V Casual Smile at right
            V "Good girl. Put your clothes back on and go inside."
            V "I'm still not happy with you, but you did make up to me a little tonight."
            "You slip your panties and shorts back on and get out of the car."
            hide V Casual Smile with moveoutright
            $ clothes = 'naked'
            show chelsea blank
            "Your panties are drenched by the time you reach your apartment, so you quickly strip and take a hot bath."
            "The water feels good - and it helps you relax after the day you've had."
            "After your bath, you tidy up the apartment and make a shopping list."
            if catadopt:
                "You play with [kittenname], and fill up his water bowl."
            "When everything is done, you turn off the lights and go to bed."
            "Still feeling the afterglow of your orgasm, you quickly drift to sleep."
            show chelsea shocked
            "A sudden noise wakes you. Your phone glows faintly on your desk."

            call screen TextingScene("Violet",
            [
                TextMessage("[pcname]"),
                TextMessage("I know you're probably asleep"),
                TextMessage("But I just came SO hard"),
                TextMessage("I was thinking about the way you fucked yourself in my car"),
                TextMessage("So I got out that vibrator you were using"),
                TextMessage("And I fucked myself with it while I thought about you using it"),
                TextMessage("I had the best orgasm EVER"),
                TextMessage("I just wanted you to know about it")
            ])

            show chelsea happy

            "You put the phone back on the nightstand, smiling to yourself."
            "The thought of Violet fucking herself while thinking of you..."
            "If you weren't so content already, you'd be horny just thinking about it."
            "It'll definitely give you something to think about the next time you masturbate though..."

            hide chelsea with dissolve

            jump endday
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
