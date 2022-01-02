label matt_cafeteriaspill:
    show bg Cafeteria with dissolve
    show chelsea at right with moveinright
    "As you approach the cafeteria, you're dismayed to find the lunch line is longer than usual."
    show chelsea angry
    pcname "{i}This is going to take forever to get through...{/i}"
    show chelsea blank
    "You reluctantly join the other students in line, doing your best to peer up at the available snacks and desserts on display."
    show chelsea sad
    pcname "{i}I hope they still have brownies up there when it's my turn...{/i}"
    show chelsea blank
    "While you're busy surveying the desserts, someone with a full tray tries to squeeze past you toward the condiments."
    "The tray catches on your shoulder and their carton of milk topples over, spilling all over your hair."
    show chelsea shocked
    pcname "Gah!"
    show chelsea angry
    "You turn around to confront them, but they're already lost in the crowd."
    "Frustrated, you tap the shoulder of the boy in front of you."
    pcname "Hey, did you see who bumped into me?"
    "He shakes his head. You continue to ask a few more people in line, hoping at least {i}someone{/i} saw what happened, but everyone brushes you off."
    show chelsea blank
    pcname "Great."
    menu cafeteria_cleanup:
        "Shower it off." if True:
            "As much as you wish you could get your lunch and then shower, there's only enough time to do one of the two before class starts."
            pcname "{i}I better clean this up...{/i}"
            if club == "track":
                pass
            elif club == "cheer":
                pass
            elif club == "yearbook":
                "...Except you have no idea where the showers are."
                "You reluctantly pull out of line and scan the crowd for someone that could help. Across the room, you see Mr. Harley walking to the teacher's lounge, his attention focused on an open book in his hands."
                show chelsea embarrassed
                pcname "Ah, Mr. Harley...?"
                show Harley Question at left with dissolve
                "Mr. Harley jumps, startled, and looks up from his book."
                show Harley Happy at left
                T "Oh, [pcname]. How can I help you? Is everything alright?"
                show Harley Blank at left
                pcname "S-Sort of."
                "You gesture to your hair miserably."
                pcname "Could you tell me where the showers are? I need to get this out right away..."
                show Harley Question at left
                "Mr. Harley makes a face at your hair, clearly noticing the smell on his own, before pointing down the hall."
                show Harley Neutral at left
                T "Oh. Of course. Down that hall, make a left when you reach the art hall. It'll be next to the pool."
                show Harley Blank at left
                show chelsea happy
                pcname "Thank you, Mr. Harley."
                hide Harley Blank with dissolve
            "With a sigh, you leave the cafeteria and make your way to the locker room showers. So much for enjoying your lunch..."
            if club == "track" or club == "cheer":
                show chelsea confused
                pcname "Huh. I've never been down this hall before..."
                show chelsea blank
                "Various art projects hang up in between the art room doors, creating a colorful collage against the otherwise dreary hallway. Everything from stained glass to canvas art, woodwork, and jewelry decorate the hall."
                "Even the yearbook club displays a large gallery of portraits beside their door."
                show chelsea happy
                pcname "These look so cool! I wonder when they'll take pictures of my club for the yearbook."
            elif club == "yearbook":
                show chelsea blank
                "The art hall is pretty easy to find, as you've been down here plenty of times for club. You smile a little as you pass the yearbook club's photography display outside of the front door."
                show chelsea happy
                pcname "I wonder if I'll see my pictures up there anytime soon..."
            show chelsea blank
            show bg Lockeroom with dissolve
            "You make your way to the locker rooms, surprised by how large they are when emptied. Rows and rows of lockers spread out before you, complimented by benches in the middle and sinks on either side."
            "Near the back, you find toilet stalls and rows of curtained showers. White stone walls rise around the showers, open near the top to let the steam out."
            "Your footsteps echo loudly across the tile floor as you step into the eerily silent room."
            show chelsea confused
            pcname "Hello?"
            show chelsea sad
            pcname "{i}It's so creepy in here without anyone around. I feel like I'm in a horror movie...{/i}"
            show chelsea blank
            "It's only when you arrive at the showers that you realize you don't have anything to wash up with."
            show chelsea shocked
            pcname "{i}Crap! How am I going to clean this up?{/i}"
            show chelsea embarrassed
            "You search around the empty locker room, hoping to find a stray student or coach nearby. Even a discarded bar of soap would be nice."
            pcname "Hello? Anyone there?"
            "You hear a few footsteps from the boys' locker room next door, but otherwise you're met with silence. Luckily, as you take a second lap past the lockers, you find a small basket full of travel-sized hygiene products."
            show chelsea happy
            pcname "Oh, thank goodness..."
            "Pleased with your find, you select a shower near the back and peel off the layers of your uniform. You're pleased to find that the milk has only found its way into your hair."
            show bg black with dissolve
            hide chelsea with dissolve
            pause 1.0
            $ clothes = 'underwear'
            show chelsea at right with moveinright
            pause 1.0
            hide chelsea with dissolve
            pause 1.0
            $ clothes = 'naked'
            show chelsea at right with moveinright
            pcname "At least that's one less thing to worry about."
            show chelsea at center with move
            "The faucets screech loudly as you turn them on. You step into the shower, enjoying the splash of warm water as it smacks against your back. The pressure from the showerhead is even better than the one at home."
            "Lathering up some shampoo between your hands, you take your time washing the milk out of your hair."
            "As you scrub the soap into your scalp, you find yourself relaxing into the warm water as it rolls down your breasts and drips from the curve of your ass."
            "You close your eyes, humming absently to a tune as you bathe. It's been a long time since you've had such a relaxing moment to yourself..."
            "{i}Click!{/i}"
            show chelsea confused
            "Your eyes snap open, startled by the noise. You pull your head out of the showerhead to better your hearing."
            pcname "Hello?"
            "There's a long moment of silence. You peek out of the curtain, but nothing seems out of the ordinary."
            show chelsea blank
            pcname "Weird..."
            "You relax back into the shower and resume bathing."
            "Once the milk is gone and your hair is clean, you find yourself at an odd time between lunch and class. There isn't enough time to eat, so returning to the cafeteria already would be useless."
            pcname "I guess I might as well take a full shower while I'm here."
            "You lather up again and continue bathing, making sure to scrub thoroughly where sweat has gathered under your breasts and between your thighs."
            "Once you're rinsed and clean, you turn the faucets off. You're surprised to hear another quiet click."
            show chelsea confused
            pcname "{i}Maybe it's a leak. Someone should really fix that...{/i}"
            show chelsea blank
            "You shrug it off and take your time drying off. You reluctantly pull your clothes back on, shimmying into your panties and rolling up your socks."
            show bg Lockeroom with dissolve
            hide chelsea with dissolve
            pause 1.0
            $ clothes = 'underwear'
            show chelsea at right with dissolve
            "When it comes to your bra, you struggle to snap it back in place."
            show chelsea angry
            pcname "Urgh... This stupid thing..."
            "You finally manage to clasp it back on, but one of the clasps in the back feels bent."
            show chelsea blank
            pcname "I guess I'll need to buy a new one..."
            "You grab the front of your breasts and adjust them to fit comfortably in your bra before pulling on the rest of your uniform."
            hide chelsea with dissolve
            pause 1.0
            $ clothes = 'school'
            show chelsea at right with dissolve
            pause 1.0
            show chelsea at right with move
            "By the time you're finished, you have to run to make it back to class on time."
            "It's a struggle to get through the rest of the day with an empty stomach, but you do feel better now that you aren't covered in milk anymore."
            $ Showerblackmail = True
            $ mattchain += 1
            jump events_end_period
        "Get your lunch." if True:
            show chelsea sad
            "While the idea of smelling like spoiled milk for the rest of the day is unappealing to say the least, the idea of going through the rest of your day on an empty stomach is somehow worse."
            show chelsea blank
            "You continue through the lunch line and carry your tray to one of the seats. You barely have enough time to scarf down your food before class begins."
            "As the day goes on, you notice more and more disgusted looks tossed in your direction as the milk dries in your hair."
            "While you make your way toward math, you overhear a conversation between two of your classmates in the hallway."
            show chelsea sad
            "Student 1" "God, that reeks! What the hell is that?"
            "Student 2" "Keep it down, she'll hear you."
            "Student 1" "Wait, that's {i}[pcname]?{/i} What the fuck?"
            "Student 2" "I know, right? It's so gross."
            "As you walk nearer to them, they quickly change the subject, pretending to focus on the interior of their lockers instead. You bite your tongue and head to class, shame creeping up on your cheeks."
            pcname "{i}This is humiliating...{/i}"
            "You try to ignore the stares that follow you around the rest of the day, each whisper burrowing into your memory like a parasite."
            "Before you can leave your last class, a small note finds its way on your desk. You carefully open it up."
            "{i}As if you didn't already look like a cow, now you smell like one!!{/i}"
            "You turn around to see who send it. No one meets your eye, but you catch a few girls giggling in the back."
            "You crumple up the note and try to hold back the tears brimming at your eyes."
            pcname "{i}Only thirty more minutes to go...{/i}"
            "You struggle to pay attention to the rest of the lesson, your mind wandering back to the hurtful things said to you during the day."
            "As the class finishes and you gather your bag, a boy in the seat beside you turns in your direction."
            "Boy" "You smell really fucking terrible. Is the shower broken at your house?"
            "Mortified, you keep your head down and duck out of the room, racing back to your apartment as quickly as possible."
            "It's only once you slam the door to your living room shut that a sob releases from your throat and tears spill over your reddened cheeks."
            "The idea of attending school again breaks you a little inside. You sob on your way to the shower, turning up the heat as high as it will go before stepping in."
            "You sit in the tub for a while and let the tears flow. It's comforting, sitting in the heat of the shower as you cry your feelings out."
            "You feel humiliated after the day's events, the memory of their comments filling you with shame."
            "After your throat's dry and the tears cease, you carefully scrub your hair clean, washing it once. Twice. Thrice. As many times as you have to, until the memory of this day is washed away as well."
            $ mattchain = 0
            $ mattsubmissive = False
            $ defymatt = False
            jump events_end_period

label matt_scene2:
    if Showerblackmail == True:
        show chelsea at right with moveinright
        "As you walk into class, you find an envelope resting on your desk."
        show chelsea confused
        "Confused, you sit down and open it up."
        show chelsea shocked
        "Inside is a small stack of photos. You take the first photo out and gasp."
        pcname "These are...!"
        hide chelsea with dissolve
        show bg Mphoto with dissolve
        "Sure enough, the envelope is filled with naked photos of you showering in the locker room. You flip through the stack, your hands visibly shaking as you try to hold back your tears."
        "You glance over your shoulder, quickly slamming the pictures down onto your desk. What if someone around you saw?"
        "The students around you seem too preoccupied with their own conversations to pay attention to you. Even so, you can't help but feel paranoid."
        pcname "Who would do something like this?"
        "As you quickly shove the photos back inside, you catch handwriting on one of the photos. You cup it in your hands, covering it as much as you can in case anyone else tries to look."
        "{i}Come to the locker room if you don't want these getting out.{/i}"
        "You shove the photo back into the envelope and tuck it safely into your breast pocket."
        show bg ClassroomD with dissolve
    elif True:
        show chelsea at right with moveinright
        "As you walk into class, you find another note on your desk."
        "{i}Meet me in the boys' locker room after school.{/i}"
    show chelsea at right with dissolve
    "You glance over your shoulder at Matt, but he pretends not to notice."
    "As the school day drags by, you wonder what he has planned."
    "When the final bell rings, you stop by your locker and get ready to leave."
    "Walking past the boys' locker room, you have a decision to make..."
    menu matt_scene2go:
        "Meet Matt" if True:
            show chelsea embarrassed
            "You duck into the locker room, hoping nobody notices you."
        "Go home" if True:
            "Whatever Matt has planned, you'd rather not be part of it."
            $ defymatt = True
            $ mattblackmail = 1
            "However, as soon as you've past the locker room door, you hear it swing open."
            show Matt Smirk at left with moveinleft
            m "Where are {i}you{/i} going?"
            pcname "I'm not interested, Matt."
            "He chuckles, shaking his head."
            "Stepping closer, he pulls his phone out and turns it toward you."
            if Showerblackmail == True:
                m "You just can't wait for those pictures to get out, can you?"
                "You freeze in place, the naked pictures of you in the shower burning a hole in your pocket."
                m "So why don't you follow me inside and we'll talk about what I'm going to do with these?"
            elif True:
                m "Remember this?"
                show MattPhone with dissolve
                "An icy chill runs down your spine; on his phone is a picture of you lifting your skirt in the men's bathroom."
                show Matt Blank at left
                m "So why don't you follow me inside and we'll talk about what I'm going to do with this?"
            "Before you can answer, he slips back inside the locker room."
            "You have no choice but to follow him."
            hide MattPhone with dissolve
    show bg Lockeroom with fade
    $ mattchain += 1
    show Matt Smirk at left with moveinleft
    show chelsea at right with moveinright
    m "There's the little slut."
    menu matt_scene2slut:
        "Defend yourself" if True:
            if club == "track":
                show chelsea angry
                pcname "Don't call me that!"
                "He sneers."
                m "You think you're not?"
            elif club == "cheer":
                show chelsea angry
                pcname "Hey! You can't just call me that!"
                "He sneers."
                m "You don't think so?"
            elif club == "yearbook":
                show chelsea sad
                pcname "I-I'm not a slut!"
                "He sneers."
                m "You don't think so?"
            $ mattscore -= 1
            m "We'll see about that..."
        "Keep quiet" if True:
            $ mattscore += 1
            $ corruption += 2
            show chelsea embarrassed
            "You look down at the floor."
    show Matt Blank at left
    show chelsea blank
    if defymatt == True:
        m "So here's how this works."
        m "If you don't want the whole school to see that picture, you're going to be {i}really{/i} nice to me."
        m "Got it?"
        menu matt_scene2blackmail:
            "I understand." if True:
                if club == "track":
                    show chelsea angry
                    "You glare at him."
                    pcname "Yeah, I got it."
                elif club == "cheer":
                    show chelsea angry
                    pcname "I can't believe you..."
                elif club == "yearbook":
                    pcname "...I got it..."
            "I don't care!" if True:
                m "Fine; leave if you want to."
                m "Just remember that I gave you a choice."
                $ endgame = True
                $ mattblackmail = 2
                jump events_end_period
    m "Now..."
    m "We have about half an hour before the football team will be in for practice."
    show Matt Smirk at left
    m "So why don't you show me those tits?"
    menu matt_scene2tits:
        "Refuse" if True:
            $ mattscore -= 1
            if club == "track":
                show chelsea confused
                pcname "What?"
            elif club == "cheer":
                show chelsea angry
                pcname "I don't think so!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "W-we're still in the school!"
            if defymatt:
                show Matt Question at left
                m "I'm starting to think you {i}want{/i} that picture to get out..."
            elif True:
                show Matt Question at left
                m "C'mon. Why did you think I wanted you to meet me here?"
                menu matt_scene2tits2:
                    "Give in." if True:
                        pass
                    "Refuse again." if True:
                        $ defymatt = True
                        $ mattblackmail = 1
                        m "Looks like you need some more incentive, huh?"
                        "He pulls out his phone and turns it toward you."
                        "You gasp; it's a picture of you pulling up your skirt in the men's room."
                        m "Unless you want the whole school seeing that picture, you'd better do what I tell you to."
                        m "Now show me your tits, slut."
                        menu matt_scene2tits3:
                            "Fine, I'll do it." if True:
                                pass
                            "I don't care!" if True:
                                m "Fine; leave if you want to."
                                m "Just remember that I gave you a choice."
                                $ endgame = True
                                $ mattblackmail = 2
                                jump events_end_period
        "Lift your shirt" if True:
            $ mattscore += 1
            $ corruption += 1
    scene bg black with fade
    show bg MLock1 with fade
    "Your cheeks burn with shame as you slowly pull off your shirt to show him your breasts."
    "He licks his lips."
    m "Bra too."
    show bg MLock2 with dissolve
    "You begin to unhook your bra, letting the right side fall first."
    "Your nipples stiffen as the air hits them, making you gasp."
    m "Sensitive slut, aren't you?"
    "He grins, staring at your chest."
    m "Alright. Now take the rest off."
    menu matt_scene2undress:
        "Protest" if True:
            if club == "track":
                pcname "Anyone could walk in!"
                m "And?"
            elif club == "cheer":
                pcname "In here!?"
            elif club == "yearbook":
                pcname "I... I can't!"
            $ mattscore -= 1
            "He shakes his head."
            if defymatt:
                m "Do I have to keep threatening you?"
            elif True:
                m "Do you wanna make me happy or not?"
            if club == "track":
                pcname "Fine..."
            elif club == "cheer":
                pcname "I do..."
            elif club == "yearbook":
                "Blushing, you look away."
        "Undress" if True:
            $ mattscore += 1
            $ corruption += 2
    show bg MLock3 with dissolve
    "Unhooking your bra, you shrug out of it and cross your arms over your breasts self-consciously."
    m "You're not done yet."
    show bg MLock4 with dissolve
    "Taking a deep breath, you unbutton your skirt and let it fall to the floor."
    "Wearing nothing but your socks and panties, you shiver in the cool air."
    m "And?"
    menu matt_scene2underwear:
        "Finish" if True:
            $ mattscore += 1
            $ corruption += 1
        "Protest" if True:
            $ mattscore -= 1
            if club == "track":
                pcname "Seriously?"
            elif club == "cheer":
                pcname "But I..."
            elif club == "yearbook":
                pcname "I don't..."
            "You shift bashfully, uncomfortable under his gaze."
            m "Keep going."
    show bg MLock5 with dissolve
    "Your heart pounds as you slowly pull your panties down over your hips, letting them fall to the floor."
    "Stepping out of them, you bend to pull off your socks."
    show bg MLock6 with dissolve
    "With all of your clothes in a pile on the floor, you glance up at Matt."
    "His eyes sweep over you, lingering on your breasts and pussy."
    m "Time for your inspection."
    m "I want you to kneel on the floor and put your hands behind your head."
    menu matt_scene2inspection:
        "Kneel" if True:
            $ mattscore += 1
            $ corruption += 2
        "Ask why" if True:
            $ mattscore -= 1
            pcname "Why-"
            "He holds up a hand."
            m "Just do what you're told, slut."
            if club == "track":
                "Your first impulse is defiance, but you know that will make him angry."
            elif club == "cheer":
                "You pout at his insult."
            elif club == "yearbook":
                "You blush, shamed by the casual degradation."
    show bg MLock7 with fade
    "Sinking to your knees, you put your hands behind your head just like he told you."
    m "Spread your knees and lift your chin. No, keep your eyes down. You don't get to look at me."
    show bg MLock8 with dissolve
    "As you comply, he gives you more instructions."
    m "Sit on your heels. And sit up straight so I can see all of you."
    show bg MLock9 with dissolve
    "He circles you slowly."
    m "Tits aren't bad, but your nipples are too small."
    m "Too skinny. When I finally get around to fucking you, there won't be anything to hold on to."
    "Your cheeks grow hotter and you bite your lip. His harsh criticism is mortifying."
    m "Nice, firm stomach, but your ass is pathetic and your feet are too big."
    m "And next time, shave your pussy."
    if club == "track":
        "Angry tears sting your eyes as he continues degrading you."
        if defymatt:
            pcname "I didn't exactly plan to do this!"
    elif club == "cheer":
        "Tears sting your eyes as he continues degrading you."
        if defymatt:
            pcname "I'm not really here willingly!"
    elif club == "yearbook":
        "You fight back tears, hurt by his continued degradation."
        if defymatt:
            pcname "I-- Please stop saying things like that..."
    m "I hope you're at least tight. There's barely anything else worth my time."
    "He finishes his circle, stopping in front of you."
    m "Let's see if you can put on a good show."
    pcname "Wha-"
    m "Talking isn't going to impress me. Go on, touch yourself. I wanna see what you look like when you cum."
    show bg MLock10 with dissolve
    "Blinking back the tears, you raise your hands to your breasts."
    "Cupping one in each hand, you squeeze them gently, pinching your nipples."
    "You gasp, twisting them between your fingers."
    "Despite your humiliation, a hot, wet rush between your legs signals your growing arousal."
    "You can feel Matt's eyes on you. Your breath grows short and harsh as you continue tormenting your nipples."
    "Soon they're so sensitive it hurts, but you can't help enjoying it too."
    "The hot wetness between your legs intensifies, making it impossible to resist touching yourself there."
    show bg MLock11 with dissolve
    "Dropping one breast, you reach down to stroke yourself."
    if defymatt:
        "Though you try not to, you hear Matt's breath catch as you slide a finger between your labia."
    elif True:
        "You hear Matt's breath catch as you slide a finger between your labia."
    "Stroking yourself in slow circles, a sudden moan escapes your throat."
    m "That's it, keep going. But..."
    m "...you can't cum until I tell you."
    if defymatt:
        "You squeeze your eyes tight, struggling to forget he's there, watching."
    elif True:
        "You shudder at his words. The feeling of his control over you is almost physical."
    "With one hand still on your breast, you slide a finger into your hot, wet cunt."
    if club == "track":
        pcname "Oh shit..."
    elif club == "cheer":
        pcname "Oh... yes..."
    elif club == "yearbook":
        pcname "Oh!"
    "The penetration feels good, but it's not nearly enough."
    "You're so wet that a second finger slides easily beside the first."
    show bg MLock12 with dissolve
    "Moaning wantonly, you finger yourself on the locker room floor."
    "You feel your juices running down your knuckles as you plunge your fingers in and out of your pussy."
    if defymatt:
        "Matt's breathing is loud and harsh. You can tell he's enjoying the show and it makes you feel even dirtier."
        "Despite the situation, you're so aroused that you could probably cum already."
    elif True:
        "Matt's breathing is loud and harsh. You can tell he's enjoying the show and it makes you even wetter."
        "You're so aroused that you could probably cum already."
    menu matt_scene2ask:
        "Ask permission" if True:
            $ mattscore -= 1
            pcname "Can I... cum yet...?"
            m "You cum when I tell you. Keep going."
        "Wait" if True:
            $ mattscore += 1
    "It's not enough. You slide a third finger in with a breathy moan."
    m "How does that feel?"
    if defymatt:
        if club == "track":
            pcname "F-fuck you..."
        elif club == "cheer":
            "Your face burns with shame, but you can't help telling the truth."
            pcname "It feels... so good..."
        elif club == "yearbook":
            "You sniffle, trying to hold back tears."
            pcname "P-Please... don't ask... things like that..."
    elif True:
        if club == "track":
            pcname "It feels really good..."
        elif club == "cheer":
            pcname "It feels... so good..."
        elif club == "yearbook":
            pcname "P-Please... don't ask... things like that..."
    m "It'll feel a lot better when it's me fucking you."
    if defymatt:
        "Your eyes fly open. His words shock you; could he really take it that far?"
    m "But I don't know if you deserve that yet."
    if club == "track":
        "You whimper, torn between outrage at his arrogance and desperation for... more."
    elif club == "cheer":
        "You whimper, your arousal building to an almost painful throbbing."
    elif club == "yearbook":
        "You whimper. His callous treatment of you is almost more than you can stand."
    "Your nipple aches with pleasure, growing more and more sensitive between your fingers."
    "You rub your thumb across your clit, crying out as it makes contact with the swollen nub."
    "It's almost more than you can take; you squeeze your eyes shut, forcing your climax down."
    menu matt_scene2askagain:
        "Ask permission" if True:
            $ mattscore -= 1
            pcname "Can I... cum yet...?"
            m "You cum when I tell you. Keep going."
        "Wait" if True:
            $ mattscore += 1
            m "You're getting close, aren't you?"
            m "Good girl. Keep going."
    "You finger yourself harder and faster, crying out each time."
    "Your clit throbs under your thumb. Tears fill your eyes as you fight back your orgasm."
    "It's too much... you can't..."
    if mattscore > 4:
        m "Okay, that's good. I want to see what you look like when you cum."
        show bg MLock13 with dissolve
        "As if his words were all your body needed, you feel yourself clench hard around your fingers."
        "You squeeze your eyes tighter, crying out as your orgasm sweeps over you."
        m "Mmm, yeah... That's good..."
        "When your breathing starts to slow again, he tells you to get dressed."
    elif True:
        m "Okay, that's enough."
        show bg MLock14 with dissolve
        "You force yourself to stop, gasping for breath."
        pcname "But- Can I-"
        m "Cum? Yeah... I don't think so. You weren't very well behaved today, were you?"
        if club == "track":
            pcname "What!?"
        elif club == "cheer":
            pcname "But I'm so..."
        elif club == "yearbook":
            pcname "I-I'm sorry, I..."
        m "Maybe next time you'll do what I tell you without questioning me so much."
        m "Now get dressed before the football team gets here."
    show bg Lockeroom with fade
    "You gather up your clothes, trying to ignore the small puddle you left on the floor."
    "As soon as you're dressed, he turns his phone toward you."
    m "Just in case you were wondering..."
    "You gasp, staring as he flips through picture after picture of you masturbating."
    $ blackmailpics = "masturbate"
    if defymatt:
        m "If you thought the other pictures were bad..."
    elif True:
        m "I think I'll hold onto these..."
    "He turns his phone back away from you."
    m "Now then..."
    "To your surprise, he passes you his phone."
    show chelsea at right with moveinright
    show Matt Blank at left with moveinleft
    show MattPhone3 with dissolve
    "You glance at the screen. It's a new contact template. The name at the top says {i}Fucktoy{/i}."
    m "You're going to give me your number. That way I can use you whenever I want. {i}However{/i} I want."
    "You have an idea now what you'll be agreeing to if you give him your number."
    if defymatt:
        "And you know you don't really have a choice."
    m "And just in case you're considering it, I should tell you that all of my pictures sync to the cloud."
    hide MattPhone3 with dissolve
    m "So there's no point trying to delete them."
    jump matt_scene2phonechoice

label matt_scene2phonechoice:
    menu matt_scene2phone:
        "Give him your number" if True:
            if defymatt:
                $ corruption += 5
                if club == "track":
                    show chelsea angry
                    "You're pissed, but you really don't want those pictures getting out."
                elif club == "cheer":
                    show chelsea embarrassed
                    "You hate that he has this power over you, but you don't see any other choice."
                elif club == "yearbook":
                    show chelsea embarrassed
                    "You feel trapped; what can you do but give in?"
            elif True:
                $ corruption += 5
                if club == "track":
                    "His cockiness is annoying, but you've never been this turned on."
                elif club == "cheer":
                    show chelsea embarrassed
                    "Your clit still throbs beneath your clothes--there's no way you're passing up more of this!"
                elif club == "yearbook":
                    show chelsea embarrassed
                    "Despite the humiliation, you find that you {i}want{/i} to please him."
            "You put your number into his phone and hand it back to him."
            $ chelseaContacts.contactsListed["Matt"] = "Matt"
            show Matt Pleased at left
            m "Good. When I text you, I expect an immediate response no matter where you are."
            if defymatt:
                "You bite your lip, forcing back the tears threatening to fall at the thought of his new power over you."
            elif True:
                "You nod. You know you've given him a lot of power over you, but you can't help feeling excited anyway."
            $ mattphone = True
        "Give him the phone back" if True:
            "You hand him the phone, shaking your head."
            show Matt Angry at left
            if defymatt==False:
                m "Maybe you didn't understand what I was saying before."
                m "Those pictures I just showed you are insurance that you'll do {i}whatever{/i} I want."
                if club == "track":
                    pcname "You're blackmailing me!?"
                elif club == "cheer":
                    pcname "You can't do that!"
                elif club == "yearbook":
                    pcname "But--"
                    "Staring at him, you realize what he's saying; he's blackmailing you."
                m "So let's try that again..."
                $ defymatt = True
                $ mattblackmail = 1
                jump matt_scene2phonechoice
            elif True:
                m "Your loss."
                m "Expect to see those pictures all over the school real soon."
                $ endgame = True
    show Matt Blank at left
    show chelsea blank
    m "I think I hear the team coming. Guess you better get out of here."
    "He grins as the locker room door swings open."
    "You dash out the door, squeezing between the football players and hoping they won't recognize you."
    jump events_end_period

label matt_blackmail_endgame:
    show chelsea with dissolve
    "As you walk into school, you notice everyone is whispering about something. They glance in your direction as you pass before gossiping amongst themselves."
    show chelsea confused
    "You try to ignore the stares as you pass by, but every awkward smile you give leads to another burst of giggles, a round of whispers, and smoldering eyes."
    show chelsea embarrassed
    "An uneasy feeling settles in your stomach, but you try to push it down."
    show chelsea confused
    pcname "{i}This is weird... Maybe I'm just being paranoid.{/i}"
    show chelsea happy
    "Deciding to prove to yourself everything is fine, you catch the gaze of a shy boy from your math class and give him a smile."
    pcname "Hey, Jacob."
    show chelsea confused
    "His face flushes a deep red. Two of his friends gape between you two before bursting into riotous laughter. Jacob sinks further into his uniform and uses his book to block you from his view as he passes."
    pcname "What? Did I say something?"
    "A group of girls giggle loudly from behind you before whispering amongst themselves. Even as you walk away, with every new face you meet, you can't help but feel their gazes burning into you."
    pcname "{i}What the hell is going on?{/i}"
    show chelsea blank
    "You head to your first class, doing your best to ignore the weird glances you receive on the way there."
    "As you take your seat, you hear a burst of gasps from the girls in the back."
    "A small group of boys approach your desk, their gazes roving over your body hungrily. You shift in your seat, uncomfortable."
    show chelsea confused
    pcname "Ah...Can I help you?"
    show GSBoy with dissolve
    "Boy 1" "Yeah. You're [pcname], right? I heard you could give us something."
    "The boys snicker in spite of your confusion."
    pcname "What? I don't have..."
    show chelsea shocked
    "One of the boys takes out his phone from his pocket and shows it to you. Your heart drops."
    show chelsea angry
    pcname "{i}Matt...{/i}"
    show chelsea sad
    if Showerblackmail == True:
        "Sure enough, displayed on his screen is a picture of you showering in the locker rooms."
    elif True:
        "Sure enough, displayed on his screen is a picture of you masturbating in the school bathroom."
    "Boy 1" "We heard you liked to give guys a good time."
    "One of the boys settles his hand on his belt, as if he'll pull himself out right now."
    "Boy 2" "You're supposed to be a pretty good fuck around here."
    "Boy 3" "How about you meet us after class? We want to see if you live up to the hype."
    "You're unable to control the rush of shame that heats your face. Tears prick the corner of your eyes, threatening to spill over."
    if club == "track":
        show chelsea shocked
        pcname "Excuse me?!"
    elif club == "cheer":
        show chelsea shocked
        pcname "You're dreaming if you think I'm going to have sex with any of {i}you.{/i}"
    elif club == "yearbook":
        "Your pulse jumps. You look between the boys, each leaning over you with lust in their eyes, and the tears fall."
        pcname "N-No! I-I don't do that! Please! Please believe me!"
        "Boy 3" "Heh, is this how you play hard to get? Kinky."
        pcname "I-It's not like that! I don't- I would never-"
    "Boy 1" "C'mon, don't be like that. We'll show you a good time."
    "One boy reaches for your shoulder. You slap his hand away and rise to your feet."
    show chelsea angry
    pcname "Don't touch me!"
    "Boy 2" "Tch. Fucking whore. You're willing to put out for everyone else, why not add to the list?"
    show chelsea sad
    "Boy 3" "C'mon, we don't bite. Much."
    "He snaps his teeth at you playfully, desire glazing his eyes. You push past them and rush out into the hall before class can begin."
    "You think you hear their footsteps follow, but maybe it's the other boys in the hall; ones running late to class and looking for a fun time."
    "A distorted chorus of wolf whistles greet you as you turn down one of the halls, their gazes piercing into you, beneath your clothes, beneath your {i}skin.{/i} You can feel every deep, lust-rooted desire they wish to take out on your body."
    "Hall boy 1" "Hey, [pcname]!"
    "One of your classmates performs a lewd gesture with his fingers. Another mimics him, thrusting his hips in your direction."
    pcname "Stop it..."
    "Hall boy 2" "Where you going? We're right here!"
    "Hall boy 1" "Don't run out on us! C'mon, we don't even need to wait for school to end!"
    "You feel them closing in on you, boy after boy, their hands ready to rip apart your clothes whether you want it or not."
    pcname "I said stop it!"
    hide GSBoy with dissolve
    "You shove past them and dig the heel of your palms against your ears, trying to block out the taunts and sexual innuendos thrown at you. You just want to get out, get out, {i}get out-{/i}"
    "As you hurry down the hall searching for somewhere, {i}anywhere{/i}, that will give you some ounce of privacy, you see something stuck on your locker door."
    if Showerblackmail == True:
        "A large printed poster of you, naked and showering, is taped to your locker. A caption underneath reads '{i}[pcname] wants YOU to join her after school!{/i}'"
    elif True:
        "A large printed poster of you masturbating in the school bathroom is taped to your locker. A caption underneath reads '{i}[pcname] is offering her services after school!{/i}'"
    "You rip the poster off with shaky hands, unable to control your trembling. The boys' taunting fills your ears, crawling like vermin under your skin. Their whistles feel strong enough to lift your skirt. And even the girls, with their gossiping whispers and high-pitched giggles, feels like a damnation."
    pcname "I just... {i}Hic!{/i} I just...!"
    "You collapse into a ball on the floor, hugging your knees tightly to your chest. Violent sobs rack through your body, and tears flood your swollen red face."
    pcname "Please stop... Just please stop... Please..."
    "The bell for first period rings, startling you. It's followed by the principal's voice over the speaker."
    P "[pcname], can you please come to the office? [pcname], come to the office. Thank you."
    "His voice settles something inside of you, providing enough of a jarring discontent to cease your sobbing. When you peer up over your knees, you realize the hall is empty."
    show bg black with dissolve
    hide chelsea with dissolve
    "Wiping your eyes dry, you shakily rise to your feet. Dread knots in your stomach as you approach the principal's office. You find him seated behind his desk with a manilla folder in front of him. He gestures toward the chairs across from him."
    show bg Office with dissolve
    show chelsea sad at right with moveinright
    show P Blank at left with moveinleft
    P "[pcname], please have a seat."
    "You do so, your gaze stuck to the folder on his desk. Your name is listed on a label on its tab."
    "The principal takes a deep breath, struggling to look you in the eyes as he starts his speech."
    P "I've been made aware of some rumors circulating around the school about your... {i}illicit{/i} activities."
    pcname "Y-You don't understand. Please..."
    "Your stomach twists as he lifts the front of the folder and nudges a face-down photo toward you. You don't need to pick it up to know it's Matt's blackmail."
    P "We don't condone this kind of behavior here under any circumstances."
    pcname "I know! Those- Those photos were never supposed to get out. Please, believe me. Matt... He was blackmailing me."
    "The principal looks momentarily stunned. He peers down at the photos with a grim expression."
    P "The... circumstances being what they are... Oh dear."
    pcname "Please. I haven't done anything wrong!"
    P "Now, I wouldn't go that far, [pcname]. These photos are still taken on school grounds."
    P "Seeing as you are {i}legally{/i} an adult and these photos have come into contact with minors, in addition to breaking the rules of conduct, I have no choose but to expel you from this school."
    "For a moment, it feels as if the world has stopped. You stare at him, mouth gaping, the air coming too slowly to your lungs. Your throat tightens as you try to choke out the words."
    pcname "E-Expel?"
    pcname "{i}No!{/i} You- You can't expel me! I just moved here, I just started my {i}life{/i} here! I'm so close to graduation!"
    P "You should have thought of that before these photos were taken."
    "The weight of his declaration crashes down on you. You fumble with your words between heavy sobs, begging for any scrap of mercy he'll provide."
    pcname "Please, {i}please{/i} don't expel me. I need to stay in school! This- This is more important to me than anything. {i}Please, I'm begging you!{/i}"
    "The principal frowns, clearly wishing there was some way to help as he avoids your gaze."
    P "I'm sorry, [pcname], but I really have no other choice. It's out of my hands."
    "The principal pulls out another paper from your file and passes it to you with a pen. You stare at the paper, then back at him imploringly."
    pcname "Please... Please, I'll do anything..."
    P "Please sign this document."
    "His words are a slap to the face."
    "You numbly sign the document, your hands trembling with anxiety. The principal carefully avoids your gaze as you sign."
    "He places the papers in your file once you're finished and stands up."
    P "I'll escort you to your locker to make sure you have everything before you go."
    "The principal follows you out to the hallway, hushing a few students walking by that dare to call you a skank as they're passing."
    "You empty your locker into your backpack and walk outside the school. As you leave, you see Matt walk by. He gives you a shit-eating grin before returning to his classroom."
    "The unfairness of it all hits you. Why should he walk free when he was the one blackmailing you? How is this fair?"
    "The principal swings the front door open and waits for you to step through."
    P "Good luck, [pcname]. I hope you find a better place elsewhere."
    "Even though his words have a nice meaning, they come out disappointed. You've certainly let him down in your short time here."
    "Your heart breaks as you stare out of the front door. You came here with so much potential, ready to soar into your future. Now it feels like someone's nailed you to the ground and plucked off your wings."
    "With your head hung in shame, you leave East Uni High, failing one of the goals you set out to complete."
    scene bg black with dissolve
    pause 0.5
    "Bad End. Better luck next time."
    $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
