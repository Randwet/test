
label bar_intro:
    $ clothes, hair = casualwear
    show bg CityD with dissolve
    show chelsea at right with moveinright
    "The Cock and Crow looks nicer than you expected, but it's definitely in a shady area of town."
    if corruptkate:
        show K Casual Sad at left with dissolve
        "As you approach, you see Kate standing outside, arms wrapped nervously around herself."
        show K Casual Blank at left
        K "[pcname]!"
        show chelsea happy
        pcname "Hey, Kate!"
        show K Casual Laugh at left
        K "I was starting to wonder if you'd changed your mind."
        if club == "track":
            pcname "Not gonna happen. I'm done with the cafe."
        elif club == "cheer":
            show chelsea confused
            pcname "After the way I left the cafe? I don't think Emilia would ever let me back."
        elif club == "yearbook":
            pcname "I wouldn't do that to you!"
        show K Casual Happy at left
        "Kate nods, smiling slightly."
        show chelsea blank
        show K Casual Blank at left
        K "Are we really going to work here?"
        show chelsea confused
        pcname "Didn't you like Daniel?"
        show K Casual Embarrassed at left
        "Her cheeks turn bright pink at the memory."
        K "Y-yeah..."
        show chelsea laugh
        pcname "I'm sure he'll be great to work for. And the tips will probably be better too!"
        show K Casual Happy at left
        K "Yeah! Let's do it!"
        show K Casual Blank at left
    elif True:
        show chelsea sad
        "For a moment, you wonder if you're doing the right thing."
        "But the way you left the cafe..."
        if club == "track":
            show chelsea blank
            pcname "No looking back!"
        elif club == "cheer":
            show chelsea happy
            pcname "I'm sure this is going to be a {i}lot{/i} more fun!"
        elif club == "yearbook":
            show chelsea blank
            pcname "Right. This is better."
    "Taking a deep breath, you open the door and step inside."
    show bg Bar with dissolve
    "There's a girl waiting tables. She's wearing a very short skirt, heels, and a low-cut crop top."
    if corruptkate:
        show K Casual Happy at left
        K "Look at the uniform!"
        "Waitress" "Hello, ladies! ID please?"
        show chelsea happy
        pcname "Oh, we're not customers. We're here to see Daniel."
        show K Casual Blank at left
    elif True:
        "Waitress" "Hi! Can I see your ID?"
        show chelsea blank
        if club == "track":
            pcname "I'm here to see Daniel, actually."
        elif club == "cheer":
            pcname "Actually... Is Daniel here?"
        elif club == "yearbook":
            pcname "Oh! I... I'm here to see Daniel."
    show chelsea blank
    "Waitress" "Oh, he said you'd be stopping by. Just a sec."
    if corruptkate:
        show K Casual Happy at left
        show chelsea happy
        "As she walks away, you and Kate exchange nervous smiles."
        show K Casual Blank at left
    show chelsea blank
    "While she's gone, you look around the bar."
    "The lighting is low, but it's clean and comfortable - laid back, like Daniel - with a pool table and lots of seating."
    show D Happy with dissolve
    show chelsea happy
    if corruptkate:
        Dan "Hey, Red! Katie! Glad you came by."
    elif True:
        Dan "Hey, Red, glad you came by!"
    show D Neutral
    Dan "Let's take a little look around and I'll give you your uniforms."
    show D Smirk
    "Daniel leads you around, showing you the bar, kitchen, stock room, and his office."
    "It's much smaller than the cafe - and so is the uniform - but you think you'll like it here."
    "There's a lot less rules and a lot more freedom."
    show D Happy
    Dan "Long as I don't get reported, have fun with the customers and send them home happy!"
    show D Blank
    "He smiles and pulls out a cigarette. Lighting it up, he takes a long drag and blows it up at the ventilation system."
    show D Smirk
    Dan "And if you need some extra cash, just let me know. I can arrange a \"bonus\", let's call it."
    if corruptkate:
        show K Casual Embarrassed at left
        show D Laugh
        "Kate turns adorably red."
        Dan "Guys are gonna love you, Katie."
    elif True:
        if club == "track":
            show chelsea laugh
            "You laugh."
            pcname "Thanks, I'll keep that in mind."
        elif club == "cheer":
            show chelsea happy
            "You smile."
            pcname "And you have a {i}big{/i} bonus. I remember."
        elif club == "yearbook":
            show chelsea embarrassed
            "You blush."
            pcname "Th-thanks... I... I'll do that."
    show D Neutral
    Dan "For the record, though... Fucking me won't get you ahead here."
    if corruptkate:
        "Kate's eyes widen."
    if club == "track":
        pcname "I didn't think it would."
    elif club == "cheer":
        pcname "That's too bad..."
    elif club == "yearbook":
        pcname "R-right. Of course."
    show D Happy
    Dan "Not saying I won't help you scratch an itch, of course. Just not going to do you any favors for it."
    show chelsea blank
    pcname "Understood."
    show D Neutral
    Dan "Great. Get outta here then."
    show D Blank
    if corruptkate:
        show D Neutral
        Dan "Don't forget to check the schedule. I'll see you both around."
    elif True:
        show D Neutral
        Dan "Just don't forget to check the schedule and I'll see you around."
    jump events_end_period

label bar_scene1:
    show chelsea at right with moveinright
    "It's a rough night; the bar is crowded and the customers are particularly rowdy."
    "You work hard to keep everyone's glasses full, but it's hard to keep up."
    show chelsea shocked
    "As you carry a pitcher of beer to a crowded table, a man reaches out and grabs your right breast, giving it a rough squeeze."
    menu bar_scene1_grabbed:
        "Scold him." if True:
            $ corruption -= 1
            show chelsea angry
            if club == "track":
                pcname "Hey! You can't just grab someone like that!"
            elif club == "cheer":
                pcname "Hey! Hands to yourself!"
            elif club == "yearbook":
                pcname "Y-you can't do that!"
            "He laughs and grabs your other breast, squeezing it too."
            "Man" "Gotta be a little nicer to your customers, girly."
            "Glaring at him, you \"accidentally\" spill the pitcher of beer on his lap."
            "Man" "Fuck! Stupid bitch!"
            show chelsea blank
            "He jumps up and rushes to the bathroom. You hurry back to the bar to get another pitcher of beer."
            "Later, Daniel approaches you."
            show D Confused with dissolve
            Dan "Got a complaint about you, Red. Man says you spilled a pint of beer on him?"
            "You can see the disappointment in his eyes."
            if club == "track":
                pcname "It was a pitcher, actually."
            elif club == "cheer":
                pcname "It was just an accident?"
            elif club == "yearbook":
                show chelsea confused
                pcname "I-I didn't mean to?"
            show chelsea blank
            show D Blank
            "He shakes his head and sighs."
            show D Neutral
            Dan "Can't be doing that, Red."
            show chelsea angry
            pcname "He grabbed my boob, and when I told him to stop he grabbed the other one!"
            show chelsea confused
            pcname "What was I supposed to do?"
            show D Laugh
            "To your surprise, he laughs."
            show D Smirk
            Dan "Didn't know you were such a prissy thing, considering how we met."
            show chelsea embarrassed
            "Your cheeks flush at the memory."
            pcname "That's different..."
            show D Neutral
            Dan "So what if he cops a feel? Let the guys have a little fun and they'll keep comin' back."
            show D Happy
            Dan "I thought you'd be alright with that. That's why I hired you."
            show chelsea blank
            "You can understand Dan's confusion, but even if you slept with him that doesn't mean you want {i}everyone{/i} feeling you up whenever they want."
            show D Blank
            "Seeing the displeasure on your face, he shakes his head."
            show D Neutral
            Dan "Just don't assault my customers again, Red."
            show D Blank
            Dan "Oh, and you'll be paying for his dry cleaning bill. I'm taking it out of your tips."
            $ tips -= 20
            jump events_end_period
        "Tell him that costs extra." if True:
            $ corruption += 3
            hide chelsea with dissolve
            if club == "track":
                show bg BGS1 with dissolve
                "You stick your nose up and give him an unamused look."
                pcname "I hope you're going to pay for that; it costs extra."
            elif club == "cheer":
                show bg BGS2b with dissolve
                "You smile and wink at him."
                pcname "That's not on the menu, but for a little extra I might not complain."
            elif club == "yearbook":
                show bg BGS2b with dissolve
                "You do your best to play it off lightly."
                pcname "H-hey! No touching. At least... not for free?"
            "Man" "In that case, I want to get my money's worth!"
            show bg BGS3 with dissolve
            "He pulls you onto his lap, laughing as you try not to spill the pitcher of beer."
            pcname "Hey!"
            show bg BGS4 with dissolve
            "His arms snake around you, each hand cupping a breast and squeezing roughly."
            "Giggling, you set the pitcher on the table and shift on his lap, rubbing your ass against his crotch."
            show bg BGS5 with dissolve
            "Man" "That's a good girl."
            "Second Man" "Let me have some of what he's having!"
            "The first man shoves a $10 bill down your shirt and pushes you toward the other man."
            show bg BGS6 with dissolve
            "Before you know it, you're being passed from lap to lap, each man groping your breasts and pinching your nipples before shoving money down your shirt and pushing you toward the next one."
            "A dark haired man turns you toward him so that you're straddling him, your skirt pushed up, and his cock pressing hard against you."
            "You gasp as he digs his fingers into your hips and grinds himself against you."
            "Dark Haired Man" "Too bad you have those panties on..."
            "Third Man" "My turn!"
            "The dark haired man presses you tight against him one last time before pushing you over to the next man."
            "You settle on his lap with a breathless giggle, flustered from being passed around and all of the attention you've been getting."
            "His hand travels up your thigh and under your skirt."
            pcname "Hey!"
            "Third Man" "Don't try to pretend now. I can feel how wet you are through your panties."
            "Your cheeks burn - you can't deny what he's saying. Your pussy {i}is{/i} hot and slick with arousal."
            "Third Man" "Why don't you let me help..."
            show bg BGS7 with dissolve
            "One finger slips beneath the edge of your panties, penetrating you suddenly."
            pcname "Oh!"
            "The other men laugh at your reaction, quickly realizing what's happening."
            "A second finger joins the first and you squeeze your eyes shut, trying not to cry out again."
            "Man" "She likes that!"
            "He fingers you roughly, unable to penetrate you enough to do more than tease."
            Dan "Alright guys, that's enough. Let her get back to work!"
            "You jump up, startled to hear your boss's voice."
            show bg black with dissolve
            "Straightening your dress, you grab the pitcher and take it to the waiting table."
            show bg Bar with dissolve
            show chelsea blank at right with dissolve
            "When you reach the bar again, Daniel stops you."
            show D Smirk with dissolve
            Dan "Having fun out there?"
            if club == "track":
                show chelsea happy
                pcname "Gotta keep them happy, right?"
            elif club == "cheer":
                show chelsea laugh
                pcname "Always!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Y-yeah..."
            "Your panties are soaked through and you're sure your face is flushed with arousal too."
            show D Confused
            Dan "How much did they give you?"
            show chelsea shocked
            show D Happy
            pcname "I lost track."
            show chelsea happy
            "Digging the bills out of your shirt and bra, you quickly count up your tips."
            show chelsea shocked
            pcname "Oh, wow... There's almost $200 here!"
            $ tips += 190
            show D Neutral
            Dan "Not bad, not bad..."
            show D Smirk
            show chelsea blank
            Dan "About time for your break, though, if you want to take a minute to... cool off."
            "You get his meaning well enough. You're incredibly horny and could really use the release."
            "Pulling out your phone, you consider your options."
            menu bar_scene1_fuck:
                "Text Matt." if mattsubmissive == True and defymatt == False:
                    $ corruption += 1
                    call screen TextingScene("Matt",
                    [
                        TextMessage("Matt", sender = False),
                        TextMessage("What do you want slut?"),
                        TextMessage("I'm at work and I'm really horny", sender = False)
                    ])
                    "You wait for a few minutes and..."
                    show chelsea sad
                    "Nothing."
                    show chelsea blank
                    "Maybe there's someone else who could help you out?"
                    "Just as you start considering your options, you hear a familiar voice at the bar."
                    show chelsea confused
                    m "I'm here to see [pcname]."
                    show D Neutral with dissolve
                    Dan "[pcname]! Someone here to see you."
                    show D Blank
                    "You step out from the back and smile gratefully at Matt."
                    show D Neutral
                    Dan "Make it quick, Red."
                    hide D Neutral with dissolve
                    "Matt smirks."
                    m "Need something?"
                    if club == "track":
                        show chelsea happy
                        pcname "Yeah, you."
                    elif club == "cheer":
                        show chelsea happy
                        pcname "If you don't mind..."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        "You nod, hoping he won't make you say it."
                    m "I told you you're a slut..."
                    "He grabs your wrist and pulls you into the men's bathroom, pushing you into the stall and locking the door behind him."
                    show chelsea blank
                    m "How long is your break?"
                    pcname "Almost over."
                    m "Then I guess you better ask me nicely if you want me to fuck you before you have to go back to work."
                    show chelsea embarrassed
                    "You feel a new rush of warmth beneath your panties as you look up at him."
                    if club == "track":
                        pcname "Please fuck me, Matt?"
                    elif club == "cheer":
                        pcname "Please... I need you inside of me..."
                    elif club == "yearbook":
                        pcname "P-please? I'm so... so horny..."
                    show bg black with dissolve
                    hide chelsea with dissolve
                    show bg MBarS1 with dissolve
                    "He spins you around and bends you over; you grab a metal bar to keep your balance."
                    "Pulling your panties down roughly, he spreads your legs wide."
                    "You hear his zipper and then his cock presses against your dripping pussy and slides inside."
                    pcname "Oh!"
                    "He thrusts into you again and again, fucking you so hard that it's all you can do to stay on your feet."
                    m "You're such a dirty... fucking whore... aren't you?"
                    pcname "Yes! Oh, fuck... Yes!"
                    "You're willing to say almost anything if he'll keep fucking you."
                    "His cock rams into you over and over, sending wave after wave of pleasure through your body."
                    m "You like that cock, you little slut?"
                    if club == "track":
                        pcname "Fuck, yes... Oh fuck... I love your cock..."
                    elif club == "cheer":
                        pcname "Yes, oh yes... I love it! I love it so much!"
                    elif club == "yearbook":
                        pcname "Yes! Yes, I love it... I... Ohhhh..."
                    m "You gonna cum already?"
                    "You can't even respond before your climax hits you."
                    pcname "Ohhhhh..."
                    "Clinging to the metal bar, your arms and legs tremble as you try to stay standing."
                    "Matt continues thrusting, moaning as your pussy squeezes around his cock."
                    "Soon it's more than he can take; he pulls out, shooting his load across your ass in hot spurts."
                    m "Now you really are a {i}dirty{/i} whore."
                    "Laughing at his own joke, he tucks his cock back into his pants."
                    m "Aren't you going to thank me? I came all the way over here just for this."
                    "You've barely caught your breath and your head is still spinning."
                    pcname "Th-thank you, Matt."
                    m "For what?"
                    if club == "track":
                        pcname "For fucking me."
                    elif club == "cheer":
                        pcname "For fucking me so good."
                    elif club == "yearbook":
                        pcname "For..."
                        "You look away, blushing furiously."
                        pcname "For fucking me..."
                    m "Good girl."
                    "He unlocks the stall door, leaving it swing wide open behind him."
                    "You quickly grab some toilet paper, wipe most of the cum from your ass, and pull up your panties before anyone else comes in."
                "Text Violet." if violetrelate=="Dom":
                    hide D Smirk with dissolve
                    call screen TextingScene("Violet",
                    [
                        TextMessage("I'm really, really horny", sender = False),
                        TextMessage("Can you please help?", sender = False),
                        TextMessage("Now?"),
                        TextMessage("Aren't you at work?"),
                        TextMessage("Yeah. On break now", sender = False),
                        TextMessage("Guess you'll have to wait"),
                        TextMessage("I'll pick you up after work. Keep your work clothes on.")
                    ])
                    show chelsea sad
                    "Sighing, you put your phone away."
                    "You're so horny, but if Violet wants you to wait..."
                    $ violetbarpickup = True
                "Text Violet." if violetrelate=="Sub":
                    hide D Smirk with dissolve
                    call screen TextingScene("Violet",
                    [
                        TextMessage("I'm really, really horny", sender = False),
                        TextMessage("Get over here", sender = False),
                        TextMessage("Now?"),
                        TextMessage("Aren't you at work?"),
                        TextMessage("Yeah. On break now", sender = False),
                        TextMessage("Be right over")
                    ])
                    show chelsea happy
                    "You smile as you put your phone away."
                    hide chelsea with dissolve
                    show bg black with dissolve
                    pause 0.5
                    show bg Bar with dissolve
                    show chelsea with moveinright
                    show V SubCasual Happy at left with moveinleft
                    "A few minutes later, you see Violet walk into the bar with a disgusted sneer on her face."
                    show V SubCasual Blank at left
                    V "So where did you want to...?"
                    "You can tell by her face that she doesn't want to be here."
                    pcname "How about we go out to your car?"
                    show V SubCasual Happy at left
                    V "I guess that's the only option."
                    show V SubCasual Blank at left
                    "She opens the door for you and leads you behind the bar to the employee lot."
                    show bg CityE with dissolve
                    show chelsea blank
                    V "I figured I could park back here since I was coming to see you."
                    "She opens the door for you; you lean the seat back while she gets in the other side."
                    show V SubCasual Happy at left
                    V "So... What would you like me to do?"
                    menu bar_scene1_violetsub:
                        "Oral." if True:
                            hide chelsea with dissolve
                            hide V SubCasual Happy with dissolve
                            show bg black with dissolve
                            if club == "track":
                                pcname "Put those pretty lips to use."
                            elif club == "cheer":
                                pcname "Mmmm... How about you go down on me?"
                            elif club == "yearbook":
                                "You reach out to touch her lips."
                                pcname "Maybe...?"
                            "She smiles as you push yourself up the seat to give her room."
                            "She crawls over on top of you, lifting your skirt."
                            "Dropping her lips to your panties, she kisses you through them, sending a wave of heat radiating from your pussy."
                            show bg VBC1 with dissolve
                            pcname "I don't have much time..."
                            "Pouting prettily, she pulls your panties down and slowly licks your labia."
                            "Her tongue darts between them, dipping into your folds and sending electric waves of pleasure over you."
                            pcname "Oh!"
                            "She dips her tongue deeper, running it along your slit."
                            "Spreading your thighs further apart, she presses her mouth tight to your pussy, slipping her tongue deep into you."
                            "Working it back and forth, she strokes your cunt with her tongue until you're twisting and moaning beneath her, desperate for more."
                            pcname "Violet..."
                            "She pulls back, smiling up at you, her lips glistening with your juices."
                            "Then she lowers her mouth again, swirling her tongue around your clit."
                            "Your clit throbs with a nearly painful pleasure."
                            "You feel your climax building quickly, but Violet takes her time, teasing you with her tongue for several minutes before fastening her lips around your clit and sucking gently."
                            "The suction fills you with an almost unbearable pleasure, and you clamp your hands over your mouth to muffle your ecstatic cries."
                            "She sucks harder, flicking her tongue back and forth across your clit."
                            "Your thighs tighten around her head, holding it firmly in place as your hips buck up, pressing your pussy tight against her face."
                            "Your orgasm hits you hard and fast, leaving you shuddering beneath her, thighs squeezing her tightly."
                            "As your senses return, you relax and Violet gasps for breath before smiling down at you."
                            V "Better?"
                            "Limbs heavy, you smile up at her."
                            pcname "Much..."
                            "She licks her lips and moves off of you, returning to her side of the car."
                        "Use your fingers." if True:
                            hide chelsea with dissolve
                            hide V SubCasual Happy with dissolve
                            show bg black with dissolve
                            "You grab her hand and pull it to your panties."
                            if club == "track":
                                pcname "We don't have much time. Just use your fingers."
                            elif club == "cheer":
                                pcname "Fingers will be fine, just hurry."
                            elif club == "yearbook":
                                "Smiling hesitantly, you rub her fingers back and forth."
                            V "Oh, you're {i}so{/i} wet..."
                            "She smiles dreamily, drawing her finger up and down your panties."
                            V "Can I take them off?"
                            "You lift your ass, watching her expression as she peels your panties off."
                            "Her eyes widen in excitement as she looks as your bared pussy."
                            show bg VBC2 with dissolve
                            pcname "I don't have a lot of time."
                            "She nods, her cheeks slightly flushed, and lightly trails her fingers over your labia."
                            "You suck in a sharp breath, surprised at how {i}good{/i} it feels even though she's barely touching you."
                            "She smiles as her fingers dip between your labia, stroking your opening."
                            "You take another quick breath, arching yourself towards her."
                            pcname "Stop teasing!"
                            "Her smile widens and her cheeks grow pinker. She presses a finger inside, gently entering you."
                            "She fingers you slowly, using only one finger until you're wiggling in the seat, desperate for {i}more{/i}."
                            pcname "{i}Violet{/i}!"
                            "Giggling, her eyelids heavy with desire, she pushes a second finger into you, angling them upward."
                            "She curls her fingers, rubbing them against the upper wall of your pussy."
                            "As they make contact with your g-spot, you gasp, your legs stiffen, and your toes curl."
                            "She rubs the spot mercilessly, sending waves of searing pleasure through your abdomen and down your legs."
                            "The pleasure is so intense that you can barely think, mumbling her name as you writhe on the car seat."
                            pcname "V-Violet... Oh... Oh... Violet... {i}Vi-o-let!{/i}"
                            "She places her other hand on your lower abdomen, pressing her thumb to your clit and rubbing it in slow circles."
                            "The pleasure is overwhelming and you feel an unexpected pressure building in your clit."
                            "Suddenly the pressure releases and you cum hard, drenching Violet's hand in a wave of fluid as your legs stiffen and shake."
                            "Sighing contentedly, she pulls her fingers from your cunt and moves back to her own seat."
                            "You feel lightheaded and your lips tingle; you realize, to your surprise, that you were so focused on the pleasure you forgot to breath for a while."
                            if club == "track":
                                pcname "Holy shit..."
                            elif club == "cheer":
                                pcname "That was {i}perfect{/i}..."
                            elif club == "yearbook":
                                pcname "That was... Wow."
                    show bg CityE with dissolve
                    show chelsea happy at right with dissolve
                    show V SubCasual Sad at left with dissolve
                    "She pouts."
                    V "I guess you have to get back to work, huh?"
                    show chelsea blank
                    "You sigh, knowing she's right."
                    show chelsea sad
                    pcname "Yeah..."
                    show V SubCasual Happy at left
                    V "I'm glad I could help, at least, but I wish we had a little more time..."
                    show chelsea happy
                    "You smile over at her."
                    pcname "Me too. But I do have to get back."
                    "You let yourself out of the car and adjust your clothes, waving to her as you walk back inside."
                    hide V SubCasual Happy with dissolve
                "Text Damien." if damienrelate=="dating":
                    hide D Smirk with dissolve
                    $ DamienAngry = "Characters/Damien/Casual/Angry.png"
                    $ DamienBlank = "Characters/Damien/Casual/Blank.png"
                    $ DamienGlare = "Characters/Damien/Casual/Glaring.png"
                    $ DamienLaugh = "Characters/Damien/Casual/Laughing.png"
                    $ DamienNeutral = "Characters/Damien/Casual/Neutral.png"
                    $ DamienSad = "Characters/Damien/Casual/Sad.png"
                    $ DamienShocked = "Characters/Damien/Casual/Shocked.png"
                    $ DamienSmiling = "Characters/Damien/Casual/Smiling.png"
                    $ DamienWorrying = "Characters/Damien/Casual/Worrying.png"
                    call screen TextingScene("Damien",
                    [
                        TextMessage("I miss you", sender = False),
                        TextMessage("I miss you too!"),
                        TextMessage("Aren't you at work?"),
                        TextMessage("Yeah. On break now", sender = False),
                        TextMessage("Wanna come see me?", sender = False),
                        TextMessage("Of course! I'll be right there")
                    ])
                    show chelsea happy
                    "You tuck your phone away and wait impatiently for Damien to arrive."
                    show chelsea blank
                    "Each passing second feels like agony. Where is he...?"
                    "Before you have a chance to give up and take care of yourself in the bathroom, you see Damien peek nervously into the bar."
                    show Damien Worry at left with moveinleft
                    show chelsea happy
                    "He peers around the seedy environment, uncertainty lacing his features. You're almost tempted to laugh at the adorable confusion on his face as he searches for you."
                    show Damien Shocked at left
                    pcname "Over here, Damien."
                    show Damien Happy at left
                    "Relief washes over him as Damien takes you in at the end of the bar. He smiles at you as he approaches, but you can tell by the glances he gives around the room that he doesn't care for your place of work."
                    D "Hey, [pcname]. How are you doing?"
                    "He leans in to press a small kiss to your cheek. You relish in the softness of his touch, so different from all of the rough hands grabbing you earlier..."
                    pcname "Hey. Everything's fine, I just really missed you."
                    "You wrap your arms around his waist and press into him close. He hugs you back, oblivious to the desire growing in your body."
                    "You almost want to tell him about all the men that touched you just to see his jealous reaction, but knowing Damien that can only end poorly."
                    show Damien Shocked at left
                    "Hoping he'll get the point, you squish your breasts against him, a sultry look glazing over your eyes."
                    show chelsea embarrassed
                    pcname "I {i}really{/i} missed you."
                    D "I- {i}Oh.{/i}"
                    "Understanding crosses his face. Damien blinks, a soft blush creeping up into his cheeks."
                    show chelsea happy
                    D "Like, right here? Right now? I don't... I don't know about that..."
                    show Damien Worry at left
                    "Damien fumbles with his hands anxiously, trying not to look you in the eye. You can't help but pout up at him."
                    show chelsea sad
                    pcname "But I {i}really{/i} need it, Damien. I haven't been able to stop thinking about you..."
                    "You run a nail lightly down his chest. He shudders at the movement."
                    pcname "And I don't have much time left on my break..."
                    "You rest your fingers at his belt, just barely slipping underneath his pants to grip the edge of his underwear."
                    show chelsea confused
                    pcname "So...?"
                    show Damien Neutral at left
                    "He considers for a moment, mouth gaping open with silent protest. Nothing comes out and he relents."
                    show chelsea happy
                    D "R-Right. Um... Okay, I guess. Is there somewhere...?"
                    show Damien Glare at left
                    "He trails off, glancing around the bar. Since neither of you have a car and your apartment is too far away, your options are pretty limited."
                    "Looking to the back of the bar, an idea comes to mind."
                    show chelsea laugh
                    pcname "Come with me."
                    "Damien shoves his hands into his pockets and follows you to the walk-in beer cooler in the back. The sharp tang of cold air hits you as you enter, sending your nerves on fire."
                    show Damien Blank at left
                    show chelsea happy
                    "Your boyfriend looks uncertain, even going so far as to grip his jacket a little tighter around his body."
                    D "It's {i}freezing{/i} in here! Are you sure you want to-?"
                    pcname "Don't worry; you're going to warm me up."
                    "All arguments die on his tongue as you shove Damien against the cold cement wall and kiss him hard. His hands hover above your waist at first, hesitant, before he slowly strokes up and down your sides."
                    "Used to a slower start, Damien's eyebrows in surprise raise as you reach for his belt and begin unbuckling."
                    show Damien Shocked at left
                    D "Aha... Already?"
                    show chelsea blank
                    pcname "I don't have a lot of time."
                    show Damien Worry at left
                    D "Ah, right..."
                    show bg black with dissolve
                    hide Damien Worry with dissolve
                    hide chelsea with dissolve

                    "You rush to peel off your clothes and his, stripping down until you're naked and shivering in the cold air."
                    show bg DBS1 with dissolve
                    "For a moment you reconsider your plan to have sex in the walk-in, but Damien gently grabs for your hips and pulls you against him, the touch of his bare skin warming you up."
                    "Pressed for time and unable to wait any longer, you push Damien down onto the hard floor, ignoring his discomfort as you climb over him and grip his cock in your palm."
                    D "Ngh! [pcname]..."
                    if club=="track":
                        "You press a hand down on his bare chest and smirk down at him. Damien's cock throbs in your hand, eager to be in the wet folds of your pussy."
                        pcname "I need it, Damien. I can't wait anymore."
                    elif club=="cheer":
                        "You curl your lips into an impish smile, pressing a hand down on his bare chest. His cock throbs in your palm and you can't resist stroking the tip a little in anticipation."
                        pcname "Be a good boy for me, okay, Damien?"
                    elif club=="yearbook":
                        "You shyly stroke his cock with your fingertips, enjoying the feel of his member twitching in pleasure at your touch."
                        pcname "I-I really need your help, Damien. Please... Please help me get off..."
                    "Damien's eyes widen, but before he can object, you turn around and position your pussy over his face and bend over his cock."
                    "His hot breath tickles your slit, already slick with warm fluids as you take Damien's tip into your mouth. He lets out a sharp breath."
                    D "[pcname]...!"
                    pcname "Don't just keep me waiting..."
                    "Slowly, Damien cups your ass in his palms and inches you down over his mouth. You moan as he slides his tongue along your folds."
                    "He's hesitant at first, but after a few moments Damien falls into a steady rhythm, his tongue tracing up and down your slit and flicking your clitoris."
                    "You lick along his length before pulling his cock further into your mouth, moaning around his sensitive member."
                    "His cock twitches in response and Damien darts his tongue into your pussy with increased ferocity."
                    "You rock your hips against his face, grinding your clit against his chin as Damien strokes his tongue inside of you."
                    "Each of your moans reverberate around his cock and Damien juts his hips up to meet your movements, thrusting down your open throat."
                    "You feel a tightness coil in your lower abdomen as your climax approaches."
                    "Each rub of your clit against his face feels harsh and intense mixed with the freezing air, creating a new kind of heat that fills your body with pleasure."
                    pcname "Mmmph... Mmph... Oh...!"
                    "Damien cums first, his hips jerking frantically against your cheeks as he releases his cum into your mouth. You swallow easily, too focused on the building pressure in your body to mind."
                    "He continues to eat you out, his tongue deep into your cunt as your legs quake around him and your thighs squeeze shut with your orgasm."
                    pcname "D-Damien! {i}Fuck! Yes!{/i}"
                    "You cum against his mouth, your hot fluids dripping onto his tongue and down his chin as you finish your orgasm."
                    "When you pull away, the frigid air of the cooler helps calm the flush on your cheeks."
                    "You both get dressed quickly, Damien's hands still shaking as he struggles to grasp what he's just participated in."
                    "You give him a reassuring smile and lick a bit of your juices from his chin."
                    show bg Bar with dissolve
                    show chelsea laugh at right with dissolve
                    pcname "Missed a spot."
                    show Damien Shocked at left
                    D "O-Oh. Yeah..."
                    show chelsea happy
                    show Damien Worry at left
                    D "I guess you have to get back to work now..."
                    show Damien Sad at left
                    "Damien frowns at the idea, clearly wishing he could spend more intimate time with you."
                    show Damien Happy at left
                    "You give him a gentle smile and press a kiss to his cheek."
                    pcname "Yeah, but I'll text you when we're slow tonight."
                    "This seems to cheer him up a bit. Damien shyly takes your hand in his as you lead him out of the walk-in cooler and back into the bar."
                    show chelsea blank
                    "You're careful to avoid Daniel as you see Damien out and reluctantly return to work; the last thing you need is a scolding for taking your boyfriend back there."
                    hide Damien Happy with dissolve
                "Ask Daniel to help." if True:
                    $ corruption += 1
                    "You tuck your phone away and look back up at Daniel."
                    show chelsea embarrassed
                    if club == "track":
                        pcname "What if I don't want to cool off?"
                    elif club == "cheer":
                        pcname "What if I need help...?"
                    elif club == "yearbook":
                        pcname "Could you... maybe...?"
                    show D Smirk
                    "With a lazy grin, he throws his towel on the table."
                    show D Happy
                    Dan "Might have a few minutes."
                    show chelsea happy
                    "He hollers for one of the other girls to cover the bar and motions for you to step into the back."
                    show D Blank
                    "He leads you into his office - it's small, with little space for more than a desk and chair."
                    Dan "Bend over, and don't worry about the papers."
                    show bg black with dissolve
                    hide D Blank with dissolve
                    hide chelsea with dissolve
                    show bg BDanielS1 with dissolve

                    "You do as he says, bending over and holding onto the edge of the desk."
                    "Daniel gets right to business, pulling your panties down and pressing his cock against your pussy."
                    Dan "Really enjoyed yourself out there, huh, Red?"
                    "He presses himself inside of you, slowly but steadily stretching you around him."
                    pcname "Ah!"
                    "He doesn't stop until he's fully inside of you, sighing happily."
                    Dan "Damn you feel good..."
                    Dan "Too bad we don't have more time."
                    "Without warning, he pulls back and thrusts again, fucking you hard and fast."
                    "Over and over, he pounds his cock into your pussy, leaving you gasping and moaning with every thrust."
                    pcname "I-- Oh! Ohhh!"
                    "He grabs your shoulder, using it for leverage, and fucks you harder still."
                    "It's too much; his hard use brings you to a quick and sudden climax."
                    "Clutching the desk, you shudder beneath him while he continues pounding his cock into your clenching cunt."
                    "He pulls out at the last second, blowing his load across your inner thigh."
                    Dan "Fuck, almost didn't make it."
                    "You stand up, turning around on shaking legs."
                    "He runs his hand through his hair."
                    Dan "Need a smoke after that. Here."
                    "He passes you a folded bill, which you quickly see is $50."
                    $ Cash += 50
                    Dan "You know, if you're ever looking for extra cash, I can find some extra work for you around here..."
                    "He doesn't wait for a response."
                    "While he steps out to smoke, you pocket the money and clean yourself up."
                    "It takes a few minutes for you to feel ready to go back to work, but you definitely feel better."
                    show bg Bar with dissolve
                    show chelsea at right with dissolve
    show chelsea blank
    show bg Bar with dissolve
    "As you return to the bar, Daniel gives you a knowing look."
    show D Neutral with dissolve
    Dan "Feeling better, Red?"
    show chelsea embarrassed
    show D Smirk
    "Heat floods your cheeks, but you manage a smile and hurry back to work."
    hide D Smirk with dissolve
    jump events_end_period


label bar_scene1_domviolet:
    $ acts -= 1
    show chelsea at right with moveinright
    "As soon as you step out of the bar, you see Violet sitting on the passenger's side of her car."
    "You open the driver's side door and get inside."
    show V Casual Pout at left with dissolve
    "Violet looks up from her phone, giving you a suspicious look."
    show V Casual Blank at left
    V "So, you got really horny at work, huh?"
    if club == "track":
        "You shrug."
        pcname "Some of the guys got a little handsy and, well..."
    elif club == "cheer":
        show chelsea happy
        "You smile."
        pcname "The customers couldn't keep their hands to themselves tonight..."
    elif club == "yearbook":
        show chelsea embarrassed
        "You look down."
        pcname "I... guess so."
        show V Casual Smile at left
        V "You sounded pretty sure in your texts. What happened?"
        pcname "Some of the customers were... They kept touching me and..."
        show V Casual Blank at left
        "You fall silent, wrapping your arms around your chest."
    V "Is that so?"
    show V Casual Blank at left
    "Her face turns thoughtful."
    show V Casual Annoyed at left
    show chelsea sad
    V "Hmmm... I don't think you should be rewarded for letting strange men turn you on..."
    show V Casual Blank at left
    "She pauses and, for a moment, you think she's going to punish you."
    show V Casual Smile at left
    V "But you {i}did{/i} ask {i}me{/i} for help instead of someone else..."
    show V Casual Blank at left
    show chelsea blank
    "She looks back at her phone and taps the screen a few times."
    "You shift uncomfortably in your seat, wondering what she's going to do next."
    show V Casual Smile at left
    "A minute later, she glances over at you and smiles."
    V "Let's go for a little drive..."
    show bg black with dissolve
    hide V Casual Smile with dissolve
    hide chelsea with dissolve
    scene bg VBarDomScene1 with dissolve
    V "Drive up to that light and turn right."
    "Putting the car in drive, you follow her directions."
    show bg VBarDomScene2 with dissolve
    "After a few blocks, you feel her hand on your leg."
    "She slowly runs her fingers up your thigh, pushing your skirt up around your hips."
    V "Turn left at the next light."
    "Her fingers slide back down your leg, trailing along your inner thigh."
    V "Now... Take your panties off."
    show bg VBarDomScene3 with dissolve
    "Swallowing hard, you grip the wheel hard in one hand. Lifting your hips, you use the other to pull your panties down to your knees."
    "The car seat feels strange against your bare ass, and the cool air makes you even more aware of how wet you are."
    "Eyes fastened to the road, you lean forward to pull your panties down, slipping them off one foot and then the other."
    V "Keep driving."
    show bg VBarDomScene4 with dissolve
    "Her fingers dance across your thighs before sliding between them and up toward your slick cunt."
    "She stops just short of making contact, running her hand back down to your knee and back up again."
    show bg VBarDomScene5 with dissolve
    "After several more teasing caresses, she reaches up and pulls the front of your blouse down, exposing your bra."
    V "Mmmm..."
    show bg VBarDomScene6 with dissolve
    "A chill runs down your spine as she brushes her fingers over your cleavage, barely touching them."
    pcname "Violet..."
    V "Shhh... Just keep driving."
    "At the next light, you come to a stop and glance nervously around."
    "It's getting late, so there aren't many people out, but another car pulls up beside you."
    "There's a middle-aged man inside, staring impatiently at the light as if willing it to turn green."
    pcname "Violet, there's someone--"
    show bg VBarDomScene7 with dissolve
    "You gasp as she pulls your bra down under your breasts and pinches a nipple."
    "Wiggling in your seat, you stare up at the light, not daring to see if the man is watching."
    "Your breath catches in your throat as Violet toys with one nipple and then the other."
    "The light changes and you press the gas pedal - perhaps a little too hard, the car jumping forward before you ease off."
    show bg VBarDomScene8 with dissolve
    V "Careful..."
    "She chuckles, moving from one nipple to the other, pinching and twisting until you're gasping for breath."
    V "Turn right here."
    "You have no idea where she's taking you and you're not sure if you care. Not while your clit pulses, almost aching to be touched."
    "Releasing your nipple, she shifts in her seat and leans toward you."
    show bg VBarDomScene9 with dissolve
    "Lifting your right breast with one hand, she fastens her lips around your nipple and sucks hard."
    pcname "Ah!"
    "Your hands tighten involuntarily, clutching the wheel while you fight to keep your eyes focused on the road."
    pcname "Violet!"
    "Her hand moves to your thigh and travels upward, gently pressing against your pussy."
    pcname "S-stop... I can't..."
    "In spite of yourself, you spread your legs, inviting her inside."
    "She drags her teeth across your nipple, making you yelp in surprise, and she presses two fingers inside of you."
    "She curls her fingers, pressing them hard against your g-spot."
    pcname "{i}Violet!{/i}"
    "After gently nipping at your nipple, she releases it and chuckles."
    show bg VBarDomScene10 with dissolve
    "She presses her lips to your ear and whispers:"
    V "Pull over."
    "You obey immediately, pulling into the nearest parking space you can find and shifting the car into park."
    V "Lay your seat back."
    show bg VBarDomScene11 with dissolve
    "As you lean back, she curls her fingers again, stroking your g-spot."
    pcname "Ohh!"
    "She leans over, taking your other nipple into her mouth and nibbling."
    "Her teeth are rough but gentle, making your nipples prickle with pleasure."
    "As she does, she works her fingers in and out of your pussy, fingering you slowly."
    "You writhe in your seat, torn between wanting her to stop biting your nipple or bite it harder."
    "Her fingers press against your g-spot each time she pushes them into you, but withdraw quickly, leaving you desperate for more."
    pcname "Violet... {i}Please...{/i}"
    show bg VBarDomScene12 with dissolve
    "She sucks your nipple hard, releasing it with a wet {i}pop{/i}, and smiles up at you."
    V "You were a bad girl tonight, letting all those men touch you."
    V "Don't you think you deserve to be punished?"
    menu bar_scene1_violetdom_deserveit:
        "I didn't mean to!" if True:
            pcname "I didn't... I didn't mean to..."
            "She shakes her head, rubbing her fingers hard against your g-spot."
            pcname "Ah! Too much!"
            V "But you {i}did{/i}."
        "I do!" if True:
            pcname "I do! I deserve it!"
            "She smiles, rubbing her fingers hard against your g-spot."
            pcname "Ah! Too much!"
            V "That's right..."
    V "That's why you aren't allowed to cum until I say so."
    V "And you'll have to be {i}very{/i} convincing..."
    show bg VBarDomScene13 with dissolve
    "Smiling up at you, she pulls her fingers back and plants her thumb against your clit."
    "Working her fingers and thumb at the same time, she alternates between rubbing your clit and g-spot."
    "You clamp your hands to your mouth, trying to muffle your sobs of pleasure as she quickly brings you to the edge of orgasm."
    "Her mouth drops back to your nipple, flicking her tongue back and forth across its aching tip."
    "The pleasure is almost unbearable and you know you can't hold back your orgasm like this."
    "Arching and twisting, you struggle to break some of the contact, but she presses her hand harder to you while her lips catch your nipple, sucking hard."
    "You grab the folds of your skirt, squeezing hard."
    pcname "Violet, I can't! Please, I'm going to--"
    "Releasing your nipple, she shakes her head."
    V "Not until I say so!"
    "Twisting and writhing on your seat, you bite your lip hard, struggling not to cum."
    "Your clit throbs with near-painful pleasure, while her fingers hit your g-spot over and over."
    if club == "track":
        pcname "Fuck! I need to cum, Violet. I need to... Oh, fuck!"
    elif club == "cheer":
        pcname "Please, Violet! I want to cum. I want to cum {i}so{/i} bad!"
    elif club == "yearbook":
        pcname "P-please! I-I can't... I need to cum... I... Ohhh!"
    "She leers down at you, smiling."
    V "Not until I say so..."
    "Your nipples are so hard they ache; you can still feel small indentations where her teeth pressed against them."
    "You're so close to cumming that you can barely think, but you can't cum yet. You can't, you can't..."
    if club == "track":
        pcname "Please let me cum. Fuck! {i}Fuck{/i}!"
    elif club == "cheer":
        pcname "Please let me cum. {i}Please{/i}..."
    elif club == "yearbook":
        pcname "It's... too much. I can't... Please..."
    V "You want to cum?"
    pcname "Yes!"
    V "You're sorry you let all those {i}dirty{/i} men touch you?"
    "You think about their hands on you, their fingers inside of you, their cocks pressing against your ass and thighs..."
    "But it's Violet's thumb rubbing your clit, her fingers thrusting into you, {i}her{/i} permission you need to get your release."
    pcname "Yes. Yes! Please, Violet, I'm sorry! I-- I--"
    V "Good. Then you can cum."
    show bg VBarDomScene14 with dissolve
    "She pulls her fingers free of your pussy and presses them hard on your clit."
    "Rubbing hard and fast, she pushes you over the edge almost instantly - and then keeps going."
    "Your legs stiffen and shake; your back arches, thrusting your breasts into the air."
    "And she keeps rubbing her fingers across your clit, drawing your orgasm out until you're screaming from the force of it."
    show bg VBarDomScene15 with dissolve
    "Finally satisfied, she pulls her hand back and wipes it on your skirt."
    "For several minutes you lay there, breathing heavily as your heart rate slowly returns to normal."
    V "We're still out in public. Don't you think you should put your clothes back on?"
    "Startled, you sit up and adjust your clothes, glancing around to see if anyone was watching."
    "She laughs at your discomfort, pulling her phone back out."
    V "All right. We'll switch at your apartment."
    "She switches on some music and you drive home."
    show bg black with dissolve
    jump events_end_period

label bar_scene2:
    if corruptkate:
        show chelsea at right with moveinright
        show K Bar Happy at left with moveinleft
        K "Hey, [pcname]!"
        show chelsea happy
        "Kate waves to you as you walk into the bar."
        "You wave back. Since she's not in school, Kate works different hours than you most of the time."
        show K Bar Blank at left
        "A customer slaps her ass, distracting her, and you get ready to start your shift."
        hide K Bar Blank
    show chelsea blank at right with moveinright
    "It's a pretty slow night and the hours drag by."
    "A married couple come in - regulars - and sit in a corner, engrossed in a private conversation."
    "You try not to interrupt too much, but there aren't many other customers."
    "Husband" "That one? Really?"
    "Wife" "You don't like her?"
    show chelsea happy
    pcname "Just checking in on you guys. Need anything here?"
    show chelsea confused
    "The wife looks you up and down, her expression a mixture of desire and... criticism?"
    "Wife" "I think we're fine, thanks."
    show chelsea blank
    "Husband" "Slow night, huh?"
    "He smiles up at you. His voice and expression are far more inviting than his wife's."
    pcname "Yeah..."
    "Husband" "Here."
    show chelsea shocked
    "He pushes some bills across the table."
    "Husband" "We'll be out of your hair soon, but I feel like we should be generous, since you don't have many other customers."
    pcname "Wow, thanks!"
    $ Cash += 15
    show chelsea happy
    "Pocketing the money - it doesn't feel right to count it now, but it looks like quite a bit - you look for other ways to keep busy."
    "Near the end of your shift, there are only three guys left."
    show chelsea blank
    if corruptkate:
        "One sits at the bar, chatting with Kate, who giggles and blushes as she pours his drinks."
    elif True:
        "One sits at the bar, chatting with the bartender, who giggles and blushes as she pours his drinks."
        "He looks familiar - maybe from the Cafe? - and you catch yourself looking at him occasionally."
    "The other two sit at separate tables."
    "At the first sits an older man who usually tips really well."
    "He's a bit of a perv, leering and licking his lips at the girls, but he's not too bad."
    "At the other table is a younger guy with bulging muscles and a {i}really{/i} aggressive personality."
    show chelsea shocked
    "You're not sure if he means to, but every time he finishes a drink he slams the glass down so hard you're afraid it'll shatter."
    show chelsea blank
    "Maybe he doesn't know his own strength."
    "Since you know you'll be asked to do it before you clock out, you decide to check the women's bathroom now."
    "You walk into the first stall and check the toilet paper."
    "It's empty."
    if club == "track":
        pcname "Hope nobody's tried to use this one..."
    elif club == "cheer":
        show chelsea angry
        pcname "Ugh, seriously?"
    elif club == "yearbook":
        pcname "Guess I need to fill it..."
    show chelsea blank
    "You check the other stall, which still has half a roll, and head back out to get more toilet paper."
    "Grabbing a roll from the storage closet, you head back to the bathroom."
    if corruptkate:
        show chelsea confused
        "As soon as you walk in, you hear heavy breathing coming from the second stall."
        "Girl" "Oh!"
        show chelsea blank
        "It's that kind of bar, so you're not really surprised - except the voice sounds {i}familiar{/i}."
        K "Nnn... Nnn..."
        show chelsea confused
        "You're {i}sure{/i} that's Kate's voice."
        show chelsea blank
        "There's a small gap around the stall door. You can't see inside from this far away, but if you got closer..."
        menu bar_scene2_kate:
            "Peak through the gap." if True:
                "You open the bathroom door and let it swing shut again."
                K "They left! I thought they were going to hear..."
                show chelsea embarrassed
                "Moving as quietly as possible, you inch toward the stall door, straining to see inside."
                hide chelsea
                show bg black with dissolve
                show bg BKS1 with dissolve

                "As you get closer, you see a man sitting on a closed toilet seat. His pants are bunched around his knees."
                "On his lap sits Kate, her eyes are half-shut, her cheeks pink with pleasure."
                "His arms are wrapped around her, stretching the neck of her shirt down so that he can reach her breasts."
                K "So... good..."
                "She bounces up and down, riding his cock while he gropes her breasts, his fingers digging into the small mounds."
                "Lips parted, she gasps each time she sinks down onto his dick."
                K "Haa... haa..."
                show bg BKS2 with dissolve
                "You reach a hand down the front of your shirt to cup your own breast, mimicking them."
                "Your other hand drifts beneath your skirt, pushing your panties aside, your fingers pressing into the slick wetness of your cunt."
                K "Haa... haa..."
                "His fingers fasten on her nipples, pinching and twisting."
                K "Oh! Yes! So... good..."
                "You follow his lead, pinching your own nipple while you hold back a moan of your own."
                "Kate moves faster, lifting herself up and rocking back down."
                "He drops one of her breasts, moving his hand down to her skirt and lifting it to her hips, revealing their merging bodies."
                "His cock disappears inside of her each time she lowers herself back onto his lap, reappearing slick with her fluids when she lifts herself again."
                "Plunging them into your pussy, you finger yourself in time with her movements."
                K "Touch me... please..."
                "He presses two fingers to her clit, moving them in slow circles."
                K "Yes! Oh yes..."
                "Her hips jerk against him; her eyes squeeze shut."
                K "Yes... yes..."
                "Fingers plunging in and out of your pussy, you twist your nipple hard, barely containing another moan."
                "His fingers move faster, rolling her clit beneath them."
                "It's more than Kate can take; her body shakes as she climaxes, quivering with pleasure."
                "The man lifts her up, thrusting into her a few times before reaching his own orgasm."
                show bg BKS3 with dissolve
                "Kate sinks back against him, dazed with pleasure and breathing heavily."
                "You want to finish - you can feel your own orgasm drawing close - but you don't want to get caught."
                "Adjusting your clothes, you back away from the stall and sneak out of the bathroom."
                show bg Bar with dissolve
                show chelsea at right with moveinright
                "Sighing, you look around the bar, shifting uncomfortably."
                "You're really horny, so you pull out your phone."
                show chelsea shocked
                pcname "2%% battery!?"
                "It's probably enough to text someone, but not to see their reply."
                show chelsea blank
                "If you want to be fucked, you'll have to find someone here."
                "Unfortunately, the only customers are the same two men."
                menu bar_scene2_kate_fucksomeone:
                    "Big tipper it is!" if True:
                        $ corruption += 5
                        "You approach the older man who's known for tipping well and lean over his table."
                        "The other guy is a little intimidating and, frankly, you don't have any other options."
                        show chelsea happy
                        pcname "Having a good time?"
                        "He looks up at you, staring straight down your shirt."
                        "Older man" "Better now, that's for sure."
                        "Older man" "Dan hires all the prettiest girls. Always has."
                        if club == "track":
                            pcname "You know it!"
                        elif club == "cheer":
                            pcname "Aww, thanks!"
                        elif club == "yearbook":
                            show chelsea embarrassed
                            "You giggle nervously."
                        "The cool air draws your attention back to your wet panties; you {i}really{/i} want to get off."
                        show chelsea happy
                        "Trailing your fingers down your cleavage, you lick your lips and smile."
                        if club == "track":
                            pcname "So... You like what you see then?"
                        elif club == "cheer":
                            pcname "Is looking all you want?"
                        elif club == "yearbook":
                            pcname "So... You like looking or...?"
                        pcname "Do you want to... touch?"
                        "He laughs, rubbing his legs and grinning."
                        "Older man" "I certainly like looking, little lady, but as for touching, well..."
                        show chelsea confused
                        "Older man" "Sorry to say that I have some trouble in that area, if you know what I mean."
                        "Older man" "Still like to come here and see you girls, but..."
                        "He shrugs and stands, grabbing his jacket."
                        "Older man" "Flattered anyway, of course."
                        show chelsea laugh
                        "You laugh and give him a wink. He drops a nice tip on the table, patting your ass as he leaves."
                        $ Cash += 20
                        show chelsea blank
                        "Kate's back at the bar, cleaning glasses. There's only one other guy in the bar..."
                        menu bar_scene2_muscles:
                            "Go for it!" if True:
                                pass
                            "Give up." if True:
                                "His aggression, the muscles... You feel like he could break you in half."
                                "Sighing, you walk back to the bar and help Kate clean up."
                                jump events_end_period
                    "Muscle-guy!" if True:
                        $ corruption += 5
                        pass
                "You approach the other table nervously."
                show chelsea happy
                if club == "track":
                    pcname "So, anything else I can get you tonight?"
                elif club == "cheer":
                    pcname "How are we doing over here?"
                elif club == "yearbook":
                    pcname "Did you... need anything else?"
                "He picks up his cup and swallows the rest of his beer, bringing the empty glass down with a {i}thunk{/i}."
                "Muscular Man" "Gotta head home soon. Work tomorrow."
                "His biceps ripple as he pushes himself up from the table. Your knees feel a little weak; he's so much bigger than you."
                if club == "track":
                    show chelsea embarrassed
                    pcname "Are you sure...? There's {i}nothing{/i} else you want?"
                elif club == "cheer":
                    pcname "Isn't there {i}anything{/i} else I can do for you?"
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "There isn't... {i}anything{/i} else...?"
                "He looks down at you with a confused expression, as if trying to figure out if he's hearing you right."
                "Muscular Man" "Have something in mind?"
                "You let your eyes wander down his body, staring pointedly at his pants."
                if club == "track":
                    pcname "I think you know what I want."
                elif club == "cheer":
                    pcname "Maybe I do..."
                elif club == "yearbook":
                    "Heat spreads over your face."
                    pcname "I might..."
                "He looks around the bar."
                "Muscular Man" "Somewhere we can go?"
                show chelsea blank
                pcname "Just the bathroom."
                "He shrugs, nodding toward the bathrooms."
                "You walk ahead of him, very aware of how he towers over you."
                "Leading him into the women's restroom, you turn to face him."
                "Muscular Man" "Well?"
                "You slip your panties aside."
                if club == "track":
                    show chelsea happy
                    pcname "Well?"
                elif club == "cheer":
                    show chelsea happy
                    pcname "Your turn."
                elif club == "yearbook":
                    show chelsea embarrassed
                    "You look away nervously, waiting to see what he'll do."
                hide chelsea with dissolve
                show bg black with dissolve
                show bg BMGS1 with dissolve
                "Smirking, he unzips his pants and draws his cock out."
                "You look around, trying to figure out the best place to do this, when suddenly he pushes you against the wall."
                pcname "Hey!"
                "Grabbing you by the waist, he slides you up the wall and hooks his arms under your knees, his hands grasping your ass and lifting you higher."
                "Muscular Man" "Problem?"
                "You shake your head, a little overwhelmed by his strength."
                "His cock presses against your thigh, hard and radiating heat."
                "He shifts his hips, pressing the thick tip to your opening."
                "Your pussy stretches around him as he carefully pushes his cock inside."
                "His biceps tense as he pulls back and enters you again, fucking you slowly."
                show bg BMGS2 with dissolve
                "Wrapping your arms around his neck, you lean back against the wall, trusting him to hold you up."
                "As you adjust to his girth, his thrusts grow deeper and quicker, his fingers digging into your ass as he pulls you tighter to him."
                "Muscular Man" "You like that?"
                if club == "track":
                    pcname "Harder!"
                elif club == "cheer":
                    pcname "Oh yes!"
                elif club == "yearbook":
                    pcname "Y-yes!"
                "He plunges into you over and over, his cock stretching your pussy wide."
                "You were already so horny and his control of your body is more thrilling than you expected."
                "As he drives his cock in and out of you, your breasts bounce with every thrust."
                "Suddenly he lifts you higher, changing the angle and you nearly shriek as his cock presses hard against your g-spot."
                if club == "track":
                    pcname "Fuck!"
                elif club == "cheer":
                    pcname "Oh yes! YES!"
                elif club == "yearbook":
                    pcname "Ah! That's... so good!"
                "Muscular Man" "Shhh..."
                "Every thrust hits your g-spot, sending sharp pangs of pleasure through you."
                "It's intense - almost too intense - but you don't want it to stop."
                if club == "track":
                    pcname "Oh, fuck yes... Fuck me... Fuck me-e-e..."
                elif club == "cheer":
                    pcname "Right there... Right there... Oh yesss..."
                elif club == "yearbook":
                    pcname "It's... too good... Ahh... Ahh..."
                show bg BMGS3 with dissolve
                "Your climax comes fast, surprising you."
                "Pinned against the wall, there's nothing you can do but quiver in his arms, his thrusting never ceasing while you shudder against him."
                "His cock pounds into your clenching pussy, never slowing."
                "As your orgasm subsides, his fingers dig into your ass and he slams into you a final time."
                "Muscular Man" "Fuck..."
                "He pulls out; you can feel his cum dripping from your cunt."
                "Untangling his limbs from yours, he slowly lowers you to the ground."
                "You're unsteady on your feet - your knees still feel weak - but you manage to stand."
                "Muscular Man" "Here, for my tab. Keep the rest."
                show bg black with dissolve
                $ Cash+=7
                "He hands you some folded bills. There's enough to cover his bill and a little more, but he definitely isn't tipping you extra."
                pcname "Thanks?"
                "Shrugging, he leaves the bathroom while you search for your discarded panties."
                "After fixing your clothes, you leave the bathroom and go back to work."
            "Leave them alone." if True:
                "You walk into the first stall and put the toilet paper in the dispenser."
                K "Ahh..."
                show chelsea happy
                "Smiling, you leave them to their fun and head back to check on your tables."
                jump events_end_period
    elif True:
        "As you put the toilet paper in the dispenser, you hear the door open behind you."
        show chelsea shocked
        "You turn around and, to your surprise, the familiar man from the bar is standing between you and the door."
        "Familiar Guy" "Don't act surprised. I saw the way you've been looking at me."
        show chelsea confused
        "He's cute, but there's clearly been a misunderstanding."
        show chelsea embarrassed
        "Still... It wouldn't be the first time you fucked a customer..."
        menu bar_scene2_bathroom:
            "Tell him to get out." if True:
                $ corruption -= 1
                if club == "track":
                    show chelsea confused
                    pcname "Look, I don't know what you're talking about, but if you don't leave I'm going to scream."
                elif club == "cheer":
                    show chelsea angry
                    pcname "That doesn't mean you can come into the women's bathroom!"
                    pcname "Get out!"
                elif club == "yearbook":
                    pcname "I... I'll scream if you don't leave!"
                "Familiar Guy" "Whoa, I'm leaving, I'm leaving! Fuck!"
                show chelsea blank
                "He backs away, hands in the air, and dashes out of the bathroom."
                "You wait a few minutes and take a deep breath before going back to work."
                jump events_end_period
            "Go along with it." if True:
                $ corruption += 1
                show chelsea happy
                if club == "track":
                    pcname "Yeah? What're you going to do about it?"
                elif club == "cheer":
                    pcname "Is that so? And what are you going to do?"
                elif club == "yearbook":
                    pcname "W-what are you going to do now?"
                "He grins, stepping into the stall and closing the toilet."
                "Familiar Guy" "I'm not going to do anything."
                "He takes a seat and unzips his pants. Pulling his cock free, he smiles up at you."
                "Familiar Guy" "You are."
                "You smile back, pulling your panties off."
                hide chelsea with dissolve
                show bg BRS1 with dissolve
                "Straddling him, you lift yourself up and reach back, grasping his dick."
                "Moving it into position, you lower yourself onto his lap, sliding his cock into your waiting hole."
                "Familiar Guy" "Fuck..."
                show bg BRS2 with dissolve
                "Over and over you bounce up and down, riding his cock."
                pcname "Oh... yes... You feel... so good..."
                "Bouncing faster and faster, moaning ecstatically until he clamps his hand over your mouth."
                "Your voice muffled, you ride him harder, your ass slapping against his thighs as your orgasm edges closer and closer."
                "It hits you in waves, each one building into the next as you rise and fall on his cock, until finally you sink against him, shuddering around him."
                "He presses you against him, hips bucking as he finds his own release, pouring himself into you with a moan."
                "His hand falls away from your face and you gasp, breathing heavily for a few moments."
                "As your senses return, you slowly stand, letting your skirt fall back into place."
                "Grabbing your panties off the floor, you slip them back on and fix your clothes."
                show bg Bar with dissolve
                show chelsea at right with dissolve
                "Familiar Guy" "That was fun. Maybe I'll see you around."
                show chelsea laugh
                "You laugh."
                show chelsea happy
                if club == "track":
                    pcname "Well, you know where to find me."
                elif club == "cheer":
                    pcname "I guess we'll see."
                elif club == "yearbook":
                    pcname "Probably..."
                "You watch him leave and then, after waiting a few minutes, head back to work."
                jump events_end_period
    jump events_end_period

label bar_scene3:
    show chelsea at right with moveinright
    "The bar is packed and you spend the night bouncing from table to table, filling drinks and bantering with customers."
    "The married couple is back, sitting in their regular booth. As usual, they mostly want to be left alone."
    "A couple of middle-aged men sit near the TV, watching sports and cheering raucously and ordering rounds of drinks at a time."
    "Other tables seat couples and groups, who come and go throughout the night, but your favorite is a group of fraternity brothers."
    "They take turns buying rounds of their favorite shots - including some of the ones meant to be challenging to swallow - laughing and carrying on."
    "One guy orders a round of Cement Mixers, which they all choke down, gagging and coughing as the milk curdles in their mouths."
    "The next guy, upping the ante, orders a round of Smoker's Cough."
    "Curious, you ask Daniel, whose tending the bar, about it."
    show chelsea confused
    show D Blank with dissolve
    pcname "What {i}is{/i} that?"
    show D Laugh
    Dan "Fucking disgusting, that's what."
    show D Happy
    show chelsea blank
    "He pours some dark liquor into a line of shot glasses before pulling a jar of mayonnaise out from under the bar."
    show D Neutral
    Dan "Jager and mayo. Looks normal, tastes like shit, but that's kinda the point."
    show D Blank
    "He spoons the mayo into the shot glasses, where it floats like thick, clotted cream."
    pcname "It almost looks good, but..."
    Dan "Like coffee and whipped cream. Until you try to swallow it."
    "You pile them onto a tray and carry them to the waiting guys."
    hide D Blank with dissolve
    "They grab their shots and count to three, downing them like pros - except for one guy."
    "Frat Guy 1" "C'mon! You can't be a pussy in front of a hot girl!"
    "Frat Guy 2" "Dude, that's fucking gross!"
    "Frat Guy 3" "Ugh, that was {i}vile{/i} man."
    "Frat Guy 4" "I don't think I can do it. I have jager and..."
    "The fourth guy shudders, staring down at the unassuming shot."
    "Frat Guy 2" "It's awful. Now drink it!"
    show chelsea happy
    "They start slapping the table, chanting."
    "Frat Guys" "Drink it! Drink it! Drink it!"
    "The fourth guy breaths in short puffs, building up his courage before picking up his shot glass and knocking it back."
    show chelsea laugh
    "He slaps it down on the table, gagging."
    "Frat Guy 4" "I'm gonna puke..."
    show D Blank with dissolve
    "He stumbles toward the bathroom - you can hear him vomiting before the door shuts."
    show D Neutral
    show chelsea happy
    Dan "Alright guys, I think that's enough for the night. And if he missed the toilet, you can help him clean it up."
    show D Blank
    "The guys laugh, taking being kicked out in good humor, and rush the bathroom, slapping the door and shouting at him."
    "Frat Guy 1" "C'mon, we gotta go!"
    "Frat Guy 3" "Your pussy ass got us kicked out!"
    "Frat Guy 2" "Fucking weak, dude!"
    "The fourth guy drags himself out of the bathroom and the others slap him on the back."
    show chelsea blank
    hide D Blank with dissolve
    "They leave in a loud huddle, and the rest of your shift seems a lot less interesting."
    "As you get ready to leave, you hear someone say it's raining outside."
    jump events_end_period

label bar_scene3_leaving:
    $ clothes, hair = casualwear
    show bg CityD with dissolve
    show chelsea at right with moveinright
    "You open the door to a downpour."
    show chelsea sad
    "Rain cascades from the sky like a wall of water. You won't make it three feet without being thoroughly drenched."
    show chelsea confused
    "Wife" "Well, look at that."
    show chelsea blank
    "You turn to see the couple standing behind you, arms around each other."
    "Husband" "Really coming down. Hope you're not walking."
    show chelsea sad
    "Your shoulders drop."
    "Husband" "Oh, that's not good."
    show chelsea blank
    "He glances at his wife, a question in his eyes. She nods, smiling softly."
    "Husband" "Why don't you get a ride with us?"
    menu bar_scene3_leaving_ride:
        "Go with them." if True:
            show chelsea happy
            pcname "That would be great... Thanks!"
            "He smiles down at you."
            "Husband" "Come on, our car is right over here."
            "You follow him and he opens the door for you while his wife gets into the driver's seat."
            show chelsea blank
            "He circles the car and, to your surprise, gets into the back seat with you."
            show chelsea confused
            "Wife" "Where do you live?"
            show chelsea blank
            "You give her your address and she pulls onto the road."
            "She drives slowly, carefully, her attention on the road and nothing else."
            show chelsea shocked
            "After a block or two, you hear a rustling on the seat beside you - and a zipper."
            "Glancing over, you see that the husband has pulled his dick out."
            "Shocked, you stare as he slowly strokes himself."
            "Wife" "Do you want to suck it?"
            pcname "What!?"
            "Wife" "Do you want to suck my husband's cock?"
            "Her eyes meet yours in the rear-view mirror; she raises her brows expectantly."
            "You look back at the man, who doesn't meet your eyes."
            menu bar_scene3_leave_bj:
                "Suck him off." if True:
                    $ corruption += 2
                    if club == "track":
                        show chelsea happy
                        pcname "Why not?"
                    elif club == "cheer":
                        show chelsea embarrassed
                        pcname "I think I do..."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        pcname "Y-yes..."
                    "Wife" "Well? Go ahead then."
                    "The air feels almost electric; the tension is uncomfortable, but thrilling."
                    scene bg BCS1 with dissolve
                    hide chelsea with dissolve

                    "Your heart quickens as you turn toward the man, leaning over to wrap your lips around the head of his cock."
                    "He moans as your lips tighten around him; you're surprised but gratified at such a strong reaction."
                    "Wife" "Do you like that?"
                    "Husband" "Yes..."
                    "His voice is husky, already thick with pleasure."
                    "You slide more of his cock into your mouth, bobbing your head, taking it inch-by-inch."
                    "Husband" "Her mouth feels so good..."
                    show bg BCS2 with dissolve
                    "You work your way down his shaft until your chin presses to his balls."
                    "Husband" "It's all in. She can take it all the way."
                    "Pulling back until your lips circle his tip, you flick it with your tongue and lower your head again."
                    "Your lips slide back down his shaft, settling at the base, and you tighten your cheeks around him."
                    "Husband" "Oh, fuck..."
                    "Wife" "Does it feel good?"
                    "Husband" "It feels amazing. She's so good at sucking dick..."
                    "Wife" "Better than me?"
                    "Husband" "{i}Way{/i} better than you. Fuck..."
                    "The exchange is a little weird, but you enjoy the compliment nonetheless."
                    "Bobbing your head, you swallow his cock over and over, until salty pre-cum coats your tongue."
                    "Husband" "Shit... I'm gonna cum already..."
                    "You press your lips down, tightening them around the base of his shaft and sucking hard."
                    show bg BCS3 with dissolve
                    "He moans, hips rocking as he fills your throat in hot spurts."
                    "You pull back, licking the last drops from the tip of his cock, and settle back on the seat."
                    "Looking around, you realize that you're parked in front of your apartment; you hadn't even felt the car stop."
                    "Wife" "Here you are... Too bad, we were just starting to have fun, weren't we?"
                    "Her eyes meet yours again, challenging you."
                    menu bar_scene3_leave_invite:
                        "Thank them for the ride." if True:
                            $ corruption += 1
                            if club == "track":
                                pcname "Thanks for the ride; it was... interesting."
                            elif club == "cheer":
                                pcname "Thanks for the ride; it was fun!"
                            elif club == "yearbook":
                                pcname "Thanks... I really appreciate the ride..."
                            "She unlocks the door and you jump out, running into the building and out of the rain."
                            "You're a little wet - and the ride was definitely different - but you're glad you didn't get soaked."
                            jump events_end_period
                        "Invite them inside." if True:
                            show bg black with dissolve
                            $ corruption += 5
                            if club == "track":
                                show chelsea happy at right with dissolve
                                pcname "We were. You know... You guys could come in, if you wanted."
                            elif club == "cheer":
                                show chelsea happy at right with dissolve
                                pcname "{i}Lots{/i} of fun... Wanna come in so we can have more fun?"
                            elif club == "yearbook":
                                show chelsea embarrassed at right with dissolve
                                pcname "Y-yeah, we were..."
                                pcname "Maybe you could... come in?"
                            "She smiles."
                            "Wife" "We'd like that, thanks."
                            "Shutting the car off, she unlocks the car doors and they follow you to your apartment."
                            hide chelsea with dissolve
                            show bg HomeN with dissolve
                            show chelsea blank with dissolve
                            "Your heart pounds as you open the door for them. They take a look around before turning toward you."
                            "The husband doesn't meet your eyes - looking anywhere but at you - while the wife eyes you hungrily."
                            "Wife" "So... Do you want to fuck my husband?"
                            "He shuffles his feet nervously."
                            menu bar_scene3_leave_fuck:
                                "Yes." if True:
                                    show chelsea happy
                                    $ corruption += 1
                                    if club == "track":
                                        pcname "Isn't that why you're here?"
                                    elif club == "cheer":
                                        pcname "You know, I think I do."
                                    elif club == "yearbook":
                                        pcname "I... Yeah, I do..."
                                    "Wife" "Good. Honey, do you want to fuck this pretty girl?"
                                    "He finally meets your eyes, nodding slowly."
                                    "Husband" "I really do..."
                                    "Smiling, you lead them to your bedroom."
                                    scene bg black with dissolve
                                    "The woman sits at your desk, spinning the chair to face you."
                                    "Wife" "Well? Clothes off, you two."
                                    show bg BCS4 with dissolve
                                    "She watches you pull your shirt off, eyes drawn to your breasts."
                                    "Wife" "Look how perky her boobs are. Nice and round... So much nicer than mine, don't you think?"
                                    "Confused, you turn to her husband, expecting him to reassure her. Instead, he agrees."
                                    "Husband" "They're perfect."
                                    show bg BCS5 with dissolve
                                    "As you unhook your bra and toss it aside, he reaches out and grabs one of your breasts, squeezing gently."
                                    "Husband" "They're so firm. Nothing like yours."
                                    pcname "Mmmm..."
                                    "He cups your other breast, lifting them both and running his thumbs across your nipples."
                                    "You gasp, shivering with pleasure."
                                    "Husband" "Heavy. And her nipples are already getting hard..."
                                    "Wife" "Do you like big boobs?"
                                    "Husband" "They're my favorite. I hate flat chests. Nothing to look at. Nothing to grab hold of..."
                                    "He gives your breasts another squeeze, as if to demonstrate."
                                    "To your surprise, his wife sighs happily."
                                    "Wife" "My boobs are so small..."
                                    "Husband" "Way too small."
                                    show bg BCS6 with dissolve
                                    "Leaning over, he presses his lips to your breast, capturing a nipple and sucking gently."
                                    "Tilting your head back, you moan, while a rush of wet heat fills your cunt."
                                    "Wife" "Look how much she likes that..."
                                    "He sucks your nipple for several minutes - sometimes hard, sometimes softly - while groping the other one, massaging the sensitive flesh."
                                    "It feels like your breasts swell at his touch, your nipples hardening to almost painful points."
                                    "The pleasure grows until it's an ache and he switches sides, taking your other nipple into his mouth and giving it the same treatment."
                                    "Your knees grow weak as he works; when he finally releases your nipples and steps back, you sway, barely able to stand on your own."
                                    "Wife" "Keep going..."
                                    "Her voice is thin and breathy, barely more than a whisper."
                                    "You drop your skirt and sit back on the bed, hands dropping to the waist of your panties."
                                    "Husband" "Let me."
                                    show bg BCS7 with dissolve
                                    "He kneels in front of you and pulls your panties down."
                                    "Husband" "Her pussy looks amazing."
                                    "Wife" "Do you want to taste it?"
                                    "Their interactions make you feel strange. They're so complimentary that you swell with pride; you feel gorgeous."
                                    "But at the same time... It's like you're a third wheel to something between them. Like you're a toy they're both using. "
                                    show bg BCS8 with dissolve
                                    "His lips press to your cunt, driving away all of your concerns."
                                    "His tongue laps at your pussy, pressing into its folds, slowly exploring you."
                                    "Wife" "I bet she tastes so good... Do you like how she tastes?"
                                    "Husband" "Mmmhmmm..."
                                    "His tongue strokes you over and over, teasing your opening without ever dipping inside."
                                    "Each stroke comes just short of your clit - tantalizingly close, but never close enough."
                                    "Wife" "Would you rather eat her pussy than mine?"
                                    "Her words are soft, breathless - passionate."
                                    "Husband" "Mmmhmmm..."
                                    show bg BCS9 with dissolve
                                    "Finally, he thrusts his tongue into you, wiggling it back and forth."
                                    "His tongue swirls inside of you, pushing in and out until you're thrashing beneath him, hands clutching the bedsheets."
                                    "It feels amazing, but it's not {i}enough{/i}. Your clit throbs, your nipples ache... You need {i}more{/i}."
                                    "Wife" "She's really enjoying that. You're making her feel so {i}good{/i}..."
                                    "He pulls away and you moan, pushing your hips toward him."
                                    if club == "track":
                                        pcname "Don't stop!"
                                    elif club == "cheer":
                                        pcname "Not yet!"
                                    elif club == "yearbook":
                                        pcname "Please, I..."
                                    "He pushes you further up the bed, crawling up between your legs and spreading them wide."
                                    "Wife" "Do you want to fuck her?"
                                    "Husband" "What do you think?"
                                    "Wife" "She wants you to. Don't you, honey?"
                                    if club == "track":
                                        pcname "Fuck yes..."
                                    elif club == "cheer":
                                        pcname "Yes... Please..."
                                    elif club == "yearbook":
                                        pcname "Y-yes..."
                                    show bg BCS10 with dissolve
                                    "He presses his cock against you, sliding it against your opening, lubing it with your juices."
                                    "Pushing the tip inside, he enters you with short tantalizingly slow thrusts."
                                    "Husband" "Fuck... She's so tight."
                                    "He pushes further with each excruciatingly slow thrust, until - finally - he's fully inside of you."
                                    show bg BCS11 with dissolve
                                    "You wrap your legs around him, squeezing him against you, trying to take a little more."
                                    "Wife" "Oh, she {i}likes{/i} that. She likes your dick..."
                                    "You glance her way; she's got her dress hiked up and her panties around her ankles."
                                    "Her fingers circle her clit slowly as she watches her husband fuck you."
                                    "Husband" "Of course she does; she knows how to take a dick."
                                    "He pulls back and thrusts again, no longer teasing you."
                                    show bg BCS12 with dissolve
                                    "Over and over, he thrusts into you, filling you in long, steady strokes."
                                    "Every thrust rocks you back and forth, followed by waves of pleasure."
                                    "You squeeze your eyes shut, focusing on the way his cock feels inside of you."
                                    "Wife" "Look how much she likes it..."
                                    "Husband" "She's a real woman. She knows how to fuck."
                                    "Wife" "Are you going to cum in her?"
                                    "Husband" "Maybe. Maybe I should."
                                    "The woman moans. Your eyes flutter open; she has her fingers buried in her cunt, fucking herself wildly."
                                    "Her other hand strokes her clit, frantically rubbing the sensitive flesh."
                                    show bg BCS13 with dissolve
                                    "Wife" "She deserves your cum more than I do. She... Oh... Oh fuck... I'm cumming... I--"
                                    "She shrieks, shuddering in your chair, eyes rolling back as she orgasms."
                                    "Her husband fucks you harder, spurred by his wife's pleasure."
                                    show bg BCS14 with dissolve
                                    "Eager for your own climax, you slide your hand down your belly, pressing your fingers to your clit and rubbing gently."
                                    "Husband" "Is that all it took to get you off?"
                                    "She breathes heavily, still coming down."
                                    "Wife" "I couldn't take anymore..."
                                    "Husband" "You can't cum when I fuck you but you'll cum from this?"
                                    "She whimpers, face red."
                                    "Wife" "I..."
                                    "Husband" "Shut up and watch. We're not done yet."
                                    show bg BCS15 with dissolve
                                    "He lifts your legs, thrusting into you harder and faster."
                                    "Your fingers jerk over your clit, rubbing faster and faster."
                                    "The new angle lets him thrust deeper, filling you more than you thought possible."
                                    "It's too much - you can't hold back any longer."
                                    show bg BCS16 with dissolve
                                    "Your legs stretch out, toes curling and knees shaking, as your climax sweeps through you."
                                    "He thrusts against your clenching cunt, moaning as you tighten around him, squeezing hard."
                                    "Husband" "Fuck!"
                                    show bg BCS17 with dissolve
                                    "A few more thrusts and he pulls out, shooting his load across your belly."
                                    "He sits back on his heels, breathing hard. You let your legs fall limply to the bed, a heaviness settling in your limbs."
                                    "After a moment, he pulls himself off the bed, circling to stand beside the chair."
                                    show bg BCS18 with dissolve
                                    "Husband" "Lick it clean."
                                    "She nods, licking your juices from his cock eagerly."
                                    "When he's satisfied, he steps back, smiling."
                                    "For a few moments, none of you speak. The mingled sounds of your breaths slowly quieting is all you can hear."
                                    "Finally, the woman pulls up her panties and straightens her dress."
                                    show bg black with dissolve
                                    "Wife" "Well, that was delightful, but we should get going."
                                    "Her husband dresses quickly, not meeting your eyes again."
                                    "Self-conscious, you pull your blankets over you. Now that you've cum, the dynamic seems a little strange again."
                                    "Wife" "Here, for showing us such a good time."
                                    "She tosses some bills on your desk."
                                    "Wife" "We'll let ourselves out. Have a good night, dear."
                                    "The man follows behind, once again the adoring husband."
                                    "You pick up the money; there's $300 there!"
                                    $ Cash += 300
                                    if club == "track":
                                        pcname "They're kinda weird, but damn..."
                                    elif club == "cheer":
                                        pcname "Well, that was interesting..."
                                    elif club == "yearbook":
                                        "You feel a little weird about the whole thing, but you have to admit it was kind of fun."
                                    jump events_end_period
                                "I've made a mistake." if True:
                                    show chelsea sad
                                    $ corruption -= 2
                                    if club == "track":
                                        pcname "Uh, actually... I think I made a mistake."
                                    elif club == "cheer":
                                        pcname "I don't know what I was thinking. This was a mistake."
                                    elif club == "yearbook":
                                        pcname "Um... Sorry, I think I made a mistake... You should..."
                                    "Sighing, the wife shakes her head."
                                    show chelsea blank
                                    "Wife" "That's too bad. Maybe another time."
                                    "They let themselves out and you change out of your uniform, wondering what exactly that was all about."
                                    jump events_end_period
                "Ask to be let out." if True:
                    $ corruption -= 3
                    show chelsea blank
                    if club == "track":
                        pcname "Actually, I want to walk home. Need to get some running in."
                    elif club == "cheer":
                        pcname "Um, no. Thanks. I'll just get out here, if that's okay."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        pcname "Can you just... let me out here?"
                    "She frowns; her husband stops stroking himself."
                    show chelsea blank
                    "Wife" "Suit yourself."
                    "She pulls over and unlocks the car door."
                    "You jump out, thanking them awkwardly, and they drive away."
                    "The walk home is miserable. You walk inside, dripping and cold, and peel the clothes from your body."
                    "That was weird... but a ride would've been really {i}nice{/i}."
                    jump events_end_period
        "Walk." if True:
            "As much as you don't want to, something about them makes you uncomfortable."
            pcname "Thanks but... I don't have far to go."
            "Wife" "Suit yourself. Come on, dear."
            "They hurry to their car and drive off."
            "The walk home is miserable. You walk inside, dripping and cold, and peel the clothes from your body."
            "You might've made the right choice - it's hard to tell - but a ride would've been really {i}nice{/i}."
            jump events_end_period

label bar_scene4:
    show bg CityD with dissolve
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "On your way to work, you stop at a food truck."
    show chelsea sad
    "It's a small taco stand, but the delicious smell makes your stomach growl."
    show chelsea shocked
    "As you look over the menu, someone suddenly bumps into you - hard - knocking you off balance."
    "You barely keep your footing and by the time you regain your balance, the man takes off running."
    if club == "track":
        show chelsea angry
        pcname "What an ass..."
    elif club == "cheer":
        show chelsea angry
        pcname "He didn't even apologize..."
    elif club == "yearbook":
        show chelsea sad
        pcname "That was scary..."
    show chelsea blank
    "Pulling your purse closer, you--"
    show chelsea shocked
    pcname "My purse..."
    "Realization strikes suddenly; he took your purse!"
    show chelsea angry
    if club == "track":
        "You take off after him, but he has a good lead."
    elif club == "cheer":
        "You take off after him, screaming that he's a thief."
    elif club == "yearbook":
        "You run after him, knowing it's hopeless but with no other option."
    "After a block, he tosses your purse into an alley and keeps running."
    if club == "track":
        "You make it to the alley and stop; there's no point chasing him further."
    elif club == "cheer":
        "You make it to the alley and stop, snatching your purse from the ground."
    elif club == "yearbook":
        "You make it to the alley and stop, gasping for breath."
    show chelsea blank
    pcname "At least he dropped it..."
    show chelsea shocked
    "You pull your purse open; there's only $20 left inside."
    $ Cash = 20
    if club == "track":
        show chelsea angry
        pcname "Shit!"
    elif club == "cheer":
        show chelsea angry
        pcname "That jerk!"
    elif club == "yearbook":
        show chelsea sad
        pcname "Oh no..."
    "You look around, but there's no sign of him."
    hide chelsea with moveoutright
    show bg black with dissolve
    if club == "track":
        "You walk the rest of the way to work, fuming with anger."
    elif club == "cheer":
        "You walk the rest of the way to work, tears of frustration stinging your eyes."
    elif club == "yearbook":
        "You walk the rest of the way to work, eyes brimming with tears."
    show bg Bar with dissolve
    $ clothes = 'bar'
    show chelsea sad at right with moveinright
    show D Neutral with dissolve
    Dan "Something wrong, Red?"
    show D Blank
    if club == "track":
        pcname "Some asshole grabbed my purse on my way here. Took almost all my money."
    elif club == "cheer":
        pcname "Someone robbed me on my way here. I only have $20 left."
    elif club == "yearbook":
        pcname "Someone took my money and I... I don't know what to do..."
    show D Neutral
    Dan "Damn, that sucks."
    show D Blank
    "He passes you a glass of water."
    show D Neutral
    Dan "You know... I told you before that if you needed more money, I could arrange something."
    menu bar_scene4_react:
        "You need something done at the bar?" if True:
            if club == "track":
                show chelsea confused
                pcname "You need extra work done around here?"
            elif club == "cheer":
                show chelsea blank
                pcname "I guess I can pull an extra shift or two..."
            elif club == "yearbook":
                pcname "I have school, though, so..."
            show D Laugh
            show chelsea blank
            "He laughs."
            Dan "Not here, Red."
        "You want to fuck me again?" if True:
            $ corruption += 1
            if club == "track":
                show chelsea confused
                pcname "Same as last time? $300?"
            elif club == "cheer":
                pcname "I'm not really horny now, but I guess we can."
            elif club == "yearbook":
                pcname "If you want to, I guess we can..."
            show D Laugh
            show chelsea blank
            "He holds his hands up."
            show D Smirk
            Dan "No, no, sorry."
            Dan "You're a lot of fun, Red, but I had something else in mind."
    show D Neutral
    Dan "Somewhere else. Somewhere private. And not with me."
    Dan "You'll make a lot of money fast."
    show D Smirk
    Dan "Interested?"
    show chelsea sad
    "You really need the money - for rent, if nothing else - but this sounds a little sketchy."
    menu bar_scene4_agree:
        "I'm in." if True:
            show chelsea blank
            $ barprostitution = True
            if club == "track":
                pcname "Why not? I'm in."
            elif club == "cheer":
                pcname "Sounds interesting. Let's do it."
            elif club == "yearbook":
                pcname "I... guess so?"
            show D Laugh
            Dan "Great. I knew you'd be game."
            show D Smirk
            Dan "After work, I'll give you a ride home and fill you in."
            if club == "track":
                show chelsea happy
                pcname "Sounds good!"
            elif club == "cheer":
                show chelsea happy
                pcname "Can't say no to a ride, can I?"
            elif club == "yearbook":
                pcname "O-okay."
            show chelsea happy
            "Giggling, you start your shift."
            show chelsea blank
            "It's hard to focus - you're distracted, thinking about all the money you lost and what Dan wants you to do."
            jump events_end_period
        "I don't think so." if True:
            $ corruption -= 1
            show chelsea blank
            show D Blank
            if club == "track":
                pcname "Yeah, thanks, but I'll pass."
            elif club == "cheer":
                pcname "I'll figure something out. Thanks for the offer though."
            elif club == "yearbook":
                pcname "I... I don't think so..."
            "He shrugs."
            show D Neutral
            Dan "Suit yourself. If you change your mind, just let me know."
            show D Blank
            hide D Blank with dissolve
            "You try to focus on work, but you can't stop worrying about that money."
            "What if you can't pay rent?"
            "By the time you leave, you still haven't come up with any ideas."
            jump events_end_period

label bar_scene4_prostitution:
    $ clothes, hair = casualwear
    show chelsea at right with dissolve
    "At the end of the day, you wait nervously while Daniel finishes a call."
    show D Neutral with dissolve
    Dan "Sorry about that, but we're all set. Let's get outta here."
    show D Blank at left with move
    show bg CityD with dissolve
    "You follow him to his car and get into the passenger's seat."
    "Daniel pulls a cigarette from behind his ear and lights it, taking a long drag before starting the car."
    "For a while you ride in silence. Daniel smokes his cigarette and you look out the window, wondering where you're going."
    show chelsea confused
    show D Neutral at left
    Dan "Here, take this."
    show D Blank at left
    "He passes you a card with the number 332 written on it."
    show chelsea blank
    show D Neutral at left
    Dan "That's your room number. You'll wait there for a client to knock."
    show D Smirk at left
    Dan "Let 'em in, take care of them, and I'll pick you up in a little while."
    show D Neutral at left
    Dan "Don't worry about the money; I'll pay you when I pick you up. No money changes hands with clients, you understand?"
    show D Blank at left
    show chelsea embarrassed
    "You have a pretty good idea what he wants you to do."
    "It's not like you haven't gotten money for sex before, but never so blatantly."
    show chelsea blank
    "This is actual prostitution. With guys you've never met."
    "He pulls over in front of a run-down hotel."
    show D Neutral at left
    Dan "Red? You got it?"
    menu bar_scene4_prostitution_agree:
        "Got it." if True:
            $ corruption += 2
            show chelsea happy
            if club == "track":
                pcname "Got it!"
            elif club == "cheer":
                pcname "I'm ready!"
            elif club == "yearbook":
                pcname "Y-yeah..."
        "I can't do this." if True:
            $ corruption -= 2
            if club == "track":
                show chelsea shocked
                pcname "Whoa, I'm not a whore!"
            elif club == "cheer":
                show chelsea sad
                pcname "I don't think I can do this."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I... I can't. I'm sorry!"
            show D Laugh at left
            "He laughs."
            show chelsea blank
            show D Smirk at left
            Dan "Too much for you, Red? I thought you {i}liked{/i} having fun?"
            show D Blank at left
            "Before you can answer, he holds up a hand."
            show D Neutral at left
            Dan "No worries. I won't ask again. Good luck with your money problems."
            show D Blank at left
            pcname "Thanks..."
            show D Neutral at left
            Dan "Hey, no offense, but I need you to get outta my car. Gotta go pick someone up; these guys will be showing up soon and I'm down a girl."
            show D Blank at left
            "You get out and close the door. He gives you a short wave and drives off."
            show chelsea sad
            "The whole way home, you wonder how you'll make back the money you lost."
            $ refuseprostitution = True
            jump events_end_period
    show D Smirk at left
    Dan "Good. See you in a while. Have fun, Red."
    hide D Smirk with dissolve
    "Getting out of the car, you enter the hotel."
    show bg black with dissolve
    "The receptionist doesn't even look up as you wander past the front desk and look for an elevator."
    "You find one in a dimly lit hallway and press the up arrow."
    "The elevator rattles as it ascends, shaking when it comes to a stop on the third floor."
    "You follow a long corridor to your room - 332 - and swipe the card."
    "A loud {i}click{/i} follows, and you turn the handle, swinging the door open wide."
    show bg hotel with dissolve
    show chelsea shocked
    "It's a small room, with a king-sized bed, dresser, and night stand crammed into the tiny space."
    show chelsea blank
    "Closing the door behind you, you flick a light on and look around."
    "The bed looks rumpled - as if someone already slept in it, or worse - and there's a large box of condoms on the night stand."
    "Climbing onto the bed, you turn the TV on and wait for someone to knock."
    "Twenty minutes pass as you flip through the channels."
    if club == "track":
        show chelsea confused
        pcname "No sports channels? Seriously?"
    elif club == "cheer":
        show chelsea angry
        pcname "Ugh, it's all reruns..."
    elif club == "yearbook":
        pcname "I guess there's nothing good on..."
    show chelsea shocked
    "{b}{i}THUD THUD THUD{/i}{/b}"
    "You jump, stifling a surprised yelp, and rush to the door."
    "A large, hairy and with a shaggy beard walks inside without greeting you."
    show chelsea embarrassed
    "Hairy Man" "Why the fuck do you have clothes on?"
    "Startled, you swallow back a nervous lump and try to smile at him. He's not unattractive, really, despite his attitude."
    pcname "Sorry, I'll just..."
    "You let your words trail off, hoping you sound seductive."
    "The man walks to the night stand and grabs a condom out, tearing the wrapper open."
    "Slipping your hands to the edge of your shorts, you slowly pull them down."
    "He drops his pants, pulling his boxers down with them, and rolls the condom over his cock."
    "You kick your panties aside and grab the bottom of your shirt."
    "Lifting it over your head, you give him a sexy smile and drop the shirt onto the bed."
    show chelsea confused
    "Hairy Man" "Still not naked?"
    show chelsea shocked
    "He circles the bed and grabs your shoulders, spinning you around and pushing you onto the bed."
    show chelsea happy
    "You giggle, propping yourself up on your elbows, but he doesn't seem to notice."
    scene bg BHS1 with dissolve
    "Grabbing your hips, he pulls you back and slams his cock into your pussy."
    pcname "Ah!"
    "More startled than hurt - luckily, the condoms are lubricated - you try to relax as he thrusts into you again and again, his hairy balls slapping loudly against your thighs."
    "His fingers dig into your hips as he slams into you, grunting with every thrust."
    "As your body adjusts, what started as an uncomfortable intrusion slowly grows pleasurable."
    "Your hands clench the bedsheets and you try to move with him, but he holds you firmly in place while he takes his own pleasure."
    "Suddenly his rhythm breaks, slowing, his thrusting erratic."
    "Hairy Man" "Fuck... Fuck..."
    "He lets out a strangled moan and releases your hips, letting you fall against the bed."
    "Flinging the used condom onto the bed next to you, he zips his pants and leaves."
    show bg hotel with dissolve
    $ clothes = 'underwear'
    show chelsea at right with dissolve
    "You don't know how to feel; you've never had someone use you quite like that."
    "He didn't even seem interested in you. You were just something for him to fuck."
    "Rolling off the bed, you walk into the bathroom and look in the mirror."
    if club == "track":
        pcname "Well that was weird..."
    elif club == "cheer":
        pcname "He could've at least got me off too..."
    elif club == "yearbook":
        pcname "Now what should I do...?"
    "You're not sure what you'd expected - seduction, maybe? To feel attractive? - but it definitely wasn't {i}that{/i}."
    "Behind you, the showerhead drips."
    pcname "I guess I should clean up."
    "Turning on the water, you strip off the rest of your clothes while you wait for the water to heat up."
    "It only sort of warms up, but you get in anyway and wash yourself quickly."
    "You don't feel particularly {i}dirty{/i}, but the shower does make you feel a little more normal."
    show chelsea shocked
    "Stepping out of the shower, you're surprised by a knock on the door."
    "You open it, expecting to see Daniel, but a bald man steps inside, glancing around nervously."
    show chelsea embarrassed
    "Bald Man" "Wow... You're really pretty."
    show chelsea shocked
    "Before you can react, he presses his lips to yours, kissing you sloppily."
    "His lips are fat and wet; he moves them over yours like a sponge he's using to wash a car."
    show chelsea blank
    "Trying to hide your disgust, you push away and force a smile."
    show chelsea happy
    pcname "Condoms are over there."
    "You point to the night stand and he undresses quickly before grabbing one."
    "This time you're happy to get it over with. You toss your towel aside and lay down on the bed, watching him struggle with the condom."
    "When he gets it on, he climbs on top of you, trailing wet kisses over your neck and chin."
    scene bg BHS1 with dissolve
    "Bald Man" "You're so pretty, Amanda. I've been waiting so long for this..."
    "You're not sure who Amanda is - did Daniel tell him to call you that?"
    "Bald Man" "I love you so much..."
    "He reaches down and fumbles with his cock, trying to find your entrance."
    "Bald Man" "I'm gonna make you feel so good. You're gonna love it."
    if club == "track":
        pcname "Yeah..."
    elif club == "cheer":
        pcname "I know..."
    elif club == "yearbook":
        pcname "Uh, yeah..."
    "He finally finds his way, pressing his cock against your pussy and moaning loudly."
    "Bald Man" "You feel so good..."
    "He's not even inside of you. You shift under him, raising your hips so that he slips inside."
    "Bald Man" "{i}Amanda{/i}..."
    "He humps you jerkily, without any rhythm or finesse. Occasionally, he slips out of you and has to stop until you help him back inside."
    "Bald Man" "Do you like that? Does it feel good?"
    "Not trusting yourself to speak, you moan, hoping to convince him."
    "Bald Man" "Shhh, not too loud. Mom would be so mad if she found out we were doing this."
    "{i}Mom...?{/i}"
    "Confused and a little concerned, you run your hands up and down his back, hoping he finishes quickly."
    "In spite of your discomfort - and his lack of skill - you find yourself reacting to being fucked."
    "Bald Man" "Amanda... Amanda... Oh god..."
    "He stiffens on top of you, and collapses with a moan."
    "His breath is hot and moist against your neck; when he finally rolls off of you, you breathe a sigh of relief."
    "He dresses quickly, glancing nervously in your direction."
    "Bald Man" "Uh, thanks..."
    show bg hotel with dissolve
    show chelsea happy at right with dissolve
    "You force a smile and he hurries to the door."
    show chelsea blank
    "To your disgust, you're actually really horny now. You let your hands run over chest and down your belly."
    "One hand on your breast, you press the other to your clit and--"
    show chelsea shocked
    "Another knock."
    if club == "track":
        pcname "Fuck..."
    elif club == "cheer":
        pcname "Ugh..."
    elif club == "yearbook":
        pcname "Oh!"
    show chelsea blank
    "You climb off the bed and walk to the door."
    show chelsea shocked
    "An old man steps inside, leaning on a cane."
    show chelsea confused
    "He looks you up and down before circling the bed and grabbing a condom."
    show chelsea blank
    "He peels it open and puts it on with shaking hands."
    "Without speaking, he gestures at the bed."
    scene bg BHS2 with dissolve
    "Trying not to grimace, you lay back on the bed and pull your legs up.."
    "He steps up to the bed slowly and presses his half-hard cock against your pussy."
    "Breathing hard already, he thrusts a few times without ever quite entering you, his hot, musty breath filling the air between you."
    "Turning away from his awful breath, you lie still while he thrusts some more."
    "His erection - half-hard from the start - never quite enters you, but he gasps anyway and steps back."
    "You're sure he hasn't cum, but he seems to be finished, stuffing his limp dick back into his pants and grabbing his cane."
    show bg hotel with dissolve
    show chelsea confused at right with dissolve
    "He leaves without ever speaking a word. For a moment, you wonder if he was even a client or just a random old man."
    "How would you even know?"
    "There's another knock on the door and you sit up, hoping it's Daniel."
    "Crossing the room, you open it slowly."
    "A young man hurries in, shutting the door behind him."
    "He looks around nervously before turning his attention to you."
    "Young Man" "Aw man, Silver's got himself a good one this time."
    "He runs his hands up and down your sides, then turns you around and grabs your ass."
    show chelsea shocked
    "Young Man" "Real nice..."
    show chelsea blank
    "He walks to the bed and flops down, casually reaching for a condom."
    "Pulling his cock out, he puts the condom on and tucks his hands behind his head."
    "Young Man" "Well?"
    if club == "track":
        show chelsea confused
        pcname "Well what?"
    elif club == "cheer":
        show chelsea confused
        pcname "What do you want me to do?"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Ummm...?"
    "He looks pointedly at his dick."
    "Young Man" "You gonna ride it or what?"
    show chelsea happy
    "Smiling, you climb onto the bed and straddle him."
    "Grabbing his cock, you give it a few strokes before rubbing it against your slit."
    scene bg BHS3 with dissolve
    "Shifting yourself forward, you press his tip to your pussy and lean back, taking him inside of you."
    "Settling onto him, you lift your hips and lower them again, slowly riding him."
    "After fucking several men without ever getting off, your body reacts quickly."
    "Each time you sink down onto his cock, you feel a familiar surge of pleasure filling you."
    "You close your eyes and tilt your head back, focusing on the feeling of him inside you."
    "Young Man" "C'mon, you can at least act like you like it."
    "Startled, your eyes flutter open."
    if club == "track":
        pcname "But I {i}am{/i}."
    elif club == "cheer":
        pcname "I {i}am{/i} enjoying it."
    elif club == "yearbook":
        pcname "I... I am."
    "He rolls his eyes."
    "Young Man" "Yeah, right. You're not even making a noise."
    if club == "track":
        "You wonder if he's ever fucked a girl who {i}did{/i} enjoy it, but figure it's not your problem."
        pcname "You want me to make more noise?"
        pcname "Oh yeah... You feel {i}so{/i} good..."
    elif club == "cheer":
        "You smile, willing to put on a show if it makes him happy."
        pcname "Ooooh... Your cock feels {i}so{/i} good... Ohhh..."
    elif club == "yearbook":
        "Feeling a little self-conscious, you try to think of something to say."
        pcname "Oh, yeah... I-it feels so good..."
    "Young Man" "That's more like it."
    "Rising and falling on his cock, you continue moaning and mumbling praise, barely hearing your own words."
    pcname "Ohhh... So good... Yeah! Yeah..."
    "The pleasure builds steadily until your clit throbs with desire. In spite of his opinion of your performance, you {i}really{/i} want to get off."
    "You ride him faster and faster, slapping your pussy down his cock with wild abandon."
    pcname "Oh! Oh yeah! Oh yeah... I need more..."
    "Young Man" "Fuck..."
    "You're so {i}close{/i} but it just isn't enough. Pressing a hand to your clit, you rub frantically, pushing yourself over the edge."
    "Your body pitches forward and you grab hold of his shoulders to steady yourself, quivering above him."
    "Young Man" "Don't stop!"
    "You can barely move while your orgasm rocks through your body."
    "Young Man" "Fucking cunt..."
    "He thrusts upward, fucking you hard."
    "Clutching his shoulders and weak from your orgasm, you cling to him as he fucks you."
    pcname "Oh yeah... oh... oh..."
    "He moans, thrusting a few final times before sinking back against the bed again."
    "Pushing you off of him, he gets up and tosses the condom in the trash."
    show bg hotel with dissolve
    "Young Man" "So... Do I get a discount for that?"
    show chelsea confused at right with dissolve
    if club == "track":
        pcname "What?!"
    elif club == "cheer":
        pcname "For what?"
    elif club == "yearbook":
        pcname "Uh... Why...?"
    "He throws his hands out, gesturing at the bed."
    "Young Man" "You got off, didn't you?"
    "You stare at him a moment as his meaning sinks in."
    if club == "track":
        show chelsea embarrassed
        pcname "I don't take money; ask someone else."
    elif club == "cheer":
        show chelsea blank
        pcname "You'll have to talk to Daniel about that."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "I... don't think so?"
    "Young Man" "Right, right... No money for this."
    show chelsea blank
    "He grins, pointing at you."
    "Young Man" "Good thinking, good thinking..."
    "Young Man" "Thanks, sweetie. I'll see you around."
    "Laying back on the bed, you sigh."
    show chelsea shocked
    "There's another knock on the door."
    show chelsea angry
    pcname "How many guys is he sending here...?"
    show chelsea shocked
    "To your surprise, the door swings open before you reach it, and Daniel steps inside."
    show chelsea blank
    show D Happy with dissolve
    "He smiles, eyeing you up."
    Dan "Hey, Red. Lookin' good."
    show D Smirk
    Dan "You ready to get out of here?"
    show bg black with dissolve
    hide chelsea with dissolve
    hide D Smirk with dissolve
    $ clothes = 'bar'
    "You dress quickly and follow him out to his car."
    show bg CityD with dissolve
    show D Smirk with dissolve
    show chelsea at right with dissolve
    Dan "So, how was it?"
    menu bar_scene4_prostitution_reaction:
        "Awful." if True:
            $ corruption -= 2
            show chelsea sad
            if club == "track":
                pcname "Those guys were creeps."
            elif club == "cheer":
                pcname "I feel... Dirty."
            elif club == "yearbook":
                pcname "It was... awful."
            show D Laugh
            "He laughs."
            show D Happy
            Dan "Lots of girls say that until they see the money."
        "Amazing." if True:
            $ corruption += 5
            show chelsea happy
            if club == "track":
                pcname "Honestly? I loved it."
            elif club == "cheer":
                pcname "It was amazing. All those guys {i}paying{/i} to have sex with me..."
            elif club == "yearbook":
                pcname "It was... really good, actually. Amazing."
            show D Laugh
            "He laughs."
            show D Smirk
            Dan "Wait 'til you see the money."
        "Not too bad." if True:
            $ corruption += 2
            if club == "track":
                pcname "It wasn't so bad."
            elif club == "cheer":
                pcname "Honestly, I thought it would be worse."
            elif club == "yearbook":
                pcname "It was... fine, I guess."
            show D Laugh
            "He laughs."
            show D Happy
            Dan "Don't worry; the money will make it better."
    show D Smirk
    Dan "Speaking of which..."
    show D Blank
    "He tosses you an envelope."
    show D Neutral
    Dan "Don't be shy; open it."
    show D Blank
    "You do, pulling out a stack of $20 bills."
    show chelsea confused
    pcname "Is this all for me?"
    show D Happy
    Dan "That's your share. You earned it."
    show chelsea shocked
    "Fanning them out, you count 60 bills... $1200!"
    $ Cash += 1200
    if club == "track":
        pcname "Holy shit..."
    elif club == "cheer":
        pcname "Oh, wow..."
    elif club == "yearbook":
        pcname "Are you... serious?"
    show D Laugh
    "He laughs, pulling out a cigarette and lighting up."
    show D Happy
    Dan "Not bad for one night, right?"
    show chelsea happy
    "You spend a few moments staring at the money before smiling."
    pcname "Yeah..."
    if corruption < 50:
        "It really wasn't bad for a few hours, but you'd rather not do it again anytime soon."
    elif True:
        "It really wasn't bad for a few hours. You almost wish it was your regular job."
    show D Blank at left with move
    "Daniel pulls up to your apartment and flicks his cigarette butt out the window."
    show D Neutral at left
    Dan "Here you are, Red. It's been fun, but get out."
    show D Blank at left
    "As you open the door and step out, he leans over toward you."
    show D Smirk at left
    Dan "And don't forget; if you're in trouble again, I can always find extra work for you."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
