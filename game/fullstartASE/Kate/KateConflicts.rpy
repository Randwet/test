label KateConflicts_Violet:
    "The cafe is bustling as you step in, and you're quickly ushered into the fray."
    show chelsea laugh with dissolve
    "Your cheeks hurt from forced smiling as you greet each customer, making sure to swish your skirt and laugh at their jokes."
    show chelsea blank
    pause 1.5
    show chelsea embarrassed
    pause 1.0
    show chelsea at center, exitScene(0.5, 0.0, 0.4, 0.4)
    "But it's all worth it for that sweet stack of tips at the end of your shift."
    scene bg Cafe
    show chelsea at left
    with fade
    pause 1.0
    show EM Blank with dissolve
    "As you finish dropping off a tray of desserts at one of your tables, Emilia meets your gaze and gestures you forward."
    show chelsea confused
    pcname "Everything okay?"
    show EM Neutral
    show chelsea shocked
    "Emilia" "Yeah. Table nine requested you."
    show EM Blank
    "You follow her gaze to the table, surprised to find Violet leaning back in her chair with a menu in hand."
    if violetrelate == "Dom":
        $ violetAttire(1)
        scene bg Cafe
        show V Casual Pout
        with fade
        pause 1.3
        show V Casual Smile
        "Violet catches your eye and smirks, her long fingers running through her hair in an enticing manner."
        "A blush creeps onto your face, and you feel a little weak at the knees as you walk toward her."
        show chelsea embarrassed at center, moveSprite(0.2, 0.2, 0.0) with dissolve
        pcname "Good afternoon, mistress. What can I get for you today?"
        show V Casual Pout
        "You smile demurely as Violet looks you over with hungry eyes, leaning forward to rest her chin in her palm."
        show V Casual Smile
        V "I can't seem to find what I want on the menu, so I guess I'll need to settle for something a little less {i}satisfying.{/i}"
        show V Casual Pout
        "Her gaze trails up and down your body before she looks back at the menu."
        show V Casual Smile
        V "I'll take the--"
    elif True:
        $ violetAttire()
        scene bg Cafe
        show V Casual Pout
        with fade
        pause 1.3
        show V SubCasual Happy
        "Violet catches your eye and smiles, waving at you shyly from her spot."
        "Your heart skips a beat as you stride toward her, a smirk playing on your lips."
        show chelsea embarrassed at center, moveSprite(0.2, 0.2, 0.0) with dissolve
        show V Casual Suprised
        pcname "Good afternoon, mistress. What can I get for you today?"
        show V SubCasual Worried
        "You lean forward subtly, your breasts at eye level with Violet."
        show V SubCasual Sad
        "She glances at them, a look of desire flickering in her eyes before peering back up at you."
        show V SubCasual Blank
        V "What do you recommend? I can't decide."
        show chelsea happy
        show V Casual Pout
        pcname "The choco-kitty sundae is the most popular, but I prefer the straw-beary parfait."
        show chelsea embarrassed
        show V Casual Smile
        V "Hm. They both look really good."
        show V Casual Pout
        "Violet purses her lips as she glances between the pictures of the desserts on the menu."
        show V SubCasual Happy
        V "I'll try the--"
    pause 1.0
    show chelsea shocked
    show V Casual Suprised
    K "[pcname]!!"
    "Violet's words are cut off as your name rings through the air, followed by two thin arms embracing you from behind."
    show chelsea embarrassed
    show K Happy at left with dissolve
    "Kate snuggles into your back before swinging around your side, a bright smile on her cute face as she clings to you."
    show V Casual Pout
    "Violet's smile drops."
    show K Laugh
    "You smile awkwardly as Kate beams at Violet. It's not unusual for Kate to cling to you around customers-- it is part of her act, after all--but having her do it in front of Violet seems... troublesome."
    show K Happy
    K "Hi, mistress! Welcome to--"
    show K Blank
    show V Casual Annoyed
    "She stops, quickly recognizing Violet from her previous visit."
    show K Laugh
    K "Oh! Welcome back, mistress!"
    K "Let me know if I can get you anything, hee-hee!"
    hide K with dissolve
    pause 1.0
    show chelsea laugh
    pause 1.0
    show chelsea sad
    "Kate finally releases you, skipping off to greet another customer at the door. You chuckle, the laughter dying on your tongue when you see Violet's face."
    if violetrelate == "Dom":
        show V Casual Blank
        V "What was that?"
        show V Casual Annoyed
        "All humor is gone from her face. Violet glares up at you, her arms crossed tightly over her chest."
        show chelsea confused
        pcname "What do you mean?"
        show chelsea shocked
        show V Casual Blank
        V "Don't play dumb. I saw the way she looked at you, touching you all over..."
        show V Casual Annoyed
        show chelsea sad
        "Violet's lip curls in disgust. You glance away awkwardly, not sure how to respond."
        show chelsea embarrassed
        pcname "...It's not like that--"
        show V Casual Blank
        show chelsea sad
        V "What did I say about playing dumb?"
        show V Casual Annoyed
        "You bite down on your lip, an awkward silence stretching between you."
        show V Casual Pout
        "Violet scrutinizes your face, her long nails clacking against the tabletop."
        show V Casual Blank
        show chelsea shocked
        V "If you have something going on with her, end it. I'm not playing around with some other girl, got it?"
        show V Casual Annoyed
        show chelsea sad
        "Before you can answer, Violet thrusts her menu at you."
        show V Casual Blank
        V "Give me the choco-kitty sundae."
        scene black with fade
        "You nod, quickly gathering her menu before leaving to place her order."
    elif True:
        show V Casual Pout
        "Violet stares at you suspiciously, occasionally glancing toward Kate across the room."
        show chelsea blank
        "It's not hard to tell she suspects something. You clear your throat, directing her attention back to you."
        show chelsea happy
        pcname "Sorry about that. What did you want to order?"
        "You force a bright smile, hoping your cheery attitude will distract her."
        show V Casual Blank
        show chelsea embarrassed
        V "...Right. I'll take the choco-kitty sundae."
        show V Casual Annoyed
        "Violet passes her menu back to you with a little more force than necessary."
        show chelsea happy
        show V Casual Pout
        pcname "I'll bring that right out."
        scene black with fade
        "You quickly leave to place her order."
    scene bg Cafe
    show V Casual Pout
    with fade
    "When you return with the sundae, Violet doesn't bother to look up at you."
    "Her long nails clack against the tabletop, her lip pressed into a tight line as she stares at Kate."
    show chelsea laugh at left with dissolve
    pcname "Enjoy!"
    hide chelsea with dissolve
    "Your smile hurts your face as you leave Violet with her dessert."
    "She takes her time eating it-- over an hour later and she's still picking at the meal, her gaze following yours and Kate's every movement throughout the cafe."
    scene black with fade
    "You're extra careful to keep your distance from Kate, picking up extra tasks around the cafe to keep you busy."
    "A painful wrenching seizes your chest as you scrub the dishes, a slow realization dawning on you."
    "You won't be able to keep up your double life with these girls for much longer. You're going to need to make a decision between them-- and soon."
    jump events_end_period

label KateConflicts_Matt:
    "The sun beats in through the large cafe windows as you make your rounds around the tables."
    "Ketchup needed at table eight. Table three needs drinks. Table four is ready to put their order in."
    show chelsea at center, enterScene(0.8, 0.5, 0.3, 0.3)
    "You check off each mental task as you greet your tables, making runs for them as necessary."
    pause 1.0
    show chelsea happy
    pause 1.5
    show chelsea at center, exitScene(0.5, 0.2, 0.3, 0.3)
    "It's been a busy day, but it'll be all worth it for that stack of tips at the end of your shift."
    scene black with fade
    "As you lean over to bus one of the dirty tables, the front door's bell chimes, capturing your attention."
    "Automatically, you rush to the door and start your greeting."
    scene bg Cafe
    show chelsea laugh
    with fade
    pcname "Welcome, master!"
    pause 1.0
    show chelsea sad
    "It's only after the words are out that you realize who it is: Matt."
    if defymatt:
        show chelsea happy
        "Your heart sinks a little, but you keep a professional smile on your face as his gaze trails over your uniform."
    elif True:
        show chelsea embarrassed
        pause 1.0
        show chelsea happy
        "Your heart races a little, but you keep a professional smile on your face as his gaze trails over your uniform."
    show Matt Casual Smirk at right with dissolve
    m "{i}Master.{/i} I could get used to that."
    show Matt Casual Blank
    show chelsea blank
    m "I've got something for you to try on. Meet me in the bathroom."
    show chelsea angry
    show Matt Casual Pleased
    pcname "Wait, I'm--"
    hide Matt with dissolve
    show chelsea sad
    "Matt ignores you, already walking toward the bathrooms. You glance nervously at your tables before following after him."
    scene black with fade
    "You find him leaning against one of the sinks with a smirk on his face."
    scene bg SchoolRestroom
    show chelsea sad at right, moveSprite(0.8, 0.8, 0.0)
    with fade
    pcname "I don't have a lot of time. My customers are going to wonder where I am."
    show chelsea blank
    show Matt Casual Smirk at right with dissolve
    "Your gaze trails down from his face to the object in his hand; a little purple vibrator."
    show chelsea embarrassed
    "You swallow hard."
    show Matt Casual Blank
    show chelsea blank
    m "Well? Get over here, whore. You're going to wear this for the rest of the day."
    show Matt Casual Smirk
    "Matt beckons you over with his finger while he turns the device on. It sounds even louder with the acoustics of the tile."
    if defymatt:
        show chelsea confused
        show Matt Casual Question
        pcname "You can't be serious..."
        show chelsea angry
        pcname "I can't wear that at work. I could get fired."
        show Matt Casual Happy
        show chelsea blank
        "Matt scoffs, twirling the pleasurable device in his hand."
        show Matt Casual Pleased
        m "Does it look like I care?"
        show Matt Casual Angry
        m "Over here. Now."
    elif True:
        show chelsea embarrassed
        "Heat rushes to your face as you eye the little buzzing device."
        "It {i}would{/i} be pretty exciting to wear something like this while you work, especially since Matt won't be the only one getting off on it this time."
        show chelsea confused
        "But is a little excitement like this worth the risk of getting fired?"
    menu matt_cafevibrator:
        "Refuse to wear it." if True:
            if defymatt:
                "You shake your head and stand your ground."
                "There are a lot of things Matt can do, but show up at your job and order you around like this isn't one of them."
                if club == "track":
                    show chelsea angry
                    show Matt Casual Blank
                    pcname "No. I'm not doing it."
                    pcname "Now are we done here? I have customers to take care of."
                elif club == "cheer":
                    show chelsea sad
                    show Matt Casual Blank
                    pcname "Come on, Matt. I'm not seriously risking my job for this."
                    pcname "You'll need to find something else to do today."
                elif club == "yearbook":
                    show chelsea sad
                    show Matt Casual Blank
                    pcname "N-No... I'm sorry, I... I can't..."
            elif True:
                show chelsea sad
                "As tempting as it is, playing along with Matt definitely isn't worth losing your job over."
                if club == "track":
                    show chelsea angry
                    show Matt Casual Blank
                    pcname "I can't do that stuff at work. I'm not getting fired over something like this."
                elif club == "cheer":
                    show chelsea sad
                    show Matt Casual Blank
                    pcname "You know I want to, Matt, but I'm not risking my job here. So, no."
                elif club == "yearbook":
                    show chelsea sad
                    show Matt Casual Blank
                    pcname "I-I really can't get fired, Matt... I'm sorry..."
            show chelsea blank
            "Matt glares at you and grips the vibrator in his palm."
            show Matt Casual Question
            m "Are you fucking serious?"
            show Matt Casual Angry
            m "You're such a whore any other time, but now you're too good for something like this?"
            show Matt Casual Smirk
            "He turns the vibrator up again. It's louder, and you're sure if anyone walked by that they'd hear it. How would you explain that to your boss?"
            show Matt Casual Blank
            "Matt stares at you, waiting for you to submit. When you don't, he shuts the device off and shoves it into his pocket with a huff."
            show Matt Casual Angry
            m "Don't think I'll forget about this, [pcname]."
            hide Matt with dissolve
            "Matt pushes past you on his way out of the bathroom."
            show chelsea sad
            "You take a shuddering breath, working to calm your nerves before you walk out after him."
            scene black with fade
            pause 1.0
            scene bg Cafe with fade
            "By the time you step into the cafe, Matt is already gone."
        "Go along with it." if True:
            $ vibrator=True
            if defymatt:
                show chelsea sad
                "You stare at the vibrator in his hand with a heavy heart."
                "As much as you want to defy him, what choice do you have?"
                show Matt Casual Pleased
                "Biting back your resistance, you walk towards him."
                show Matt Casual Happy
                m "That's what I thought."
                show chelsea shocked
                show Matt Casual Smirk
                "You reach for the vibrator, but Matt pulls it back."
            elif True:
                show chelsea embarrassed
                "Staring at the vibrator in his hand, you can't help yourself. The excitement of doing something naughty at work is too tempting to turn down."
                "You walk toward him and reach for the vibrator. Matt pulls it back."
            show Matt Casual Blank
            show chelsea embarrassed
            m "Move your panties out of the way."
            hide Matt with dissolve
            "Licking your lips, you move your panties to the side. Matt reaches down, his fingers caressing your pussy as he slides the vibrator in."
            show Matt Casual Smirk at right with dissolve
            "You restrain a soft moan as the vibrations send a wave of pleasure through your body. Matt smirks, stepping back to admire his work."
            show Matt Casual Pleased
            m "I'll take that back during class. You better have it ready for me."
            hide Matt with dissolve
            "He glances down once more at your pussy before stepping out of the bathroom."
            scene black with fade
            pause 1.0
            scene bg Cafe with fade
            "Moving your panties back into place, you quickly adjust yourself and follow after him. By the time you step into the cafe, he's gone."
    show GSBoy with dissolve
    "Customer" "Miss? Where's my drink?"
    "One of your customers waves you over with an annoyed look on his face."
    show chelsea embarrassed at right with dissolve
    pcname "Sorry! Coming right up!"
    if vibrator == True:
        scene black with fade
        "You maneuver through the rest of your shift to the best of your ability, trying to ignore the faint buzz you hear whenever your legs spread too far apart."
        if corruption >= 30:
            "No one else seems to notice, which sends a pleasant thrill through your body as the vibrator pulses inside of you."
            "There's something exciting about feeling sexual pleasure when you aren't supposed to, especially with a vibrator rubbing against you at every bend and turn."
            scene bg Lockeroom with fade
            "Near the end of your shift, your cunt is dripping, soaking through your panties with each wave of pleasure the toy gives you."
            "It's hard to resist reaching under your skirt to finish the job."
        elif True:
            "Although no one else seems to notice, you can't stop the rush of heat to your face as you shuffle around the cafe in embarrassment."
            "Even if a little part of you had been excited to feel it inside of you, that feeling easily wears off as you're forced to look customers in the eye with a smile as you deliver their food."
            scene bg Lockeroom with fade
            "As your shift comes to a close, you practically flee to the dressing room, eager to remove the device from your now soaked pussy."
        show chelsea embarrassed with dissolve
        "Making sure you're alone, you slip the vibrator out with a moan."
        show K Blank at right, moveSprite(0.9, 0.9, 0.0) with dissolve
        K "[pcname]?"
        show chelsea shocked
        show K Embarrassed
        pcname "Kate!"
        show chelsea embarrassed
        "You jump, startled, and hide the vibrator in your skirt as you turn around to face her, making sure to turn it off as discreetly as possible."
        show chelsea sad
        "Kate lingers by the closed door, a look of concern on her face."
        K "S-sorry! I didn't mean to scare you..."
        show K Blank
        show chelsea confused
        K "Are you okay? You seemed a little weird out there today."
        show K Embarrassed
        show chelsea shocked
        "She catches herself, eyes widening as she waves her hands back and forth in panic."
        show chelsea blank
        K "N-Not that you're weird or anything! No! You're totally cute!"
        K "I just meant, um, you seemed like something was off, maybe?"
        show chelsea sad
        show K Sad
        pcname "Ah..."
        show K Blank
        "You glance down at the vibrator bundled up in your skirt. Kate's gaze follows, her little brows pinching together in confusion."
        show chelsea blank
        "There's no use hiding it now. You pull out the vibrator and show it to her."
        show K Embarrassed
        "Kate gapes at you in shock."
        show chelsea sad
        K "I-Is that--?"
        pcname "Yeah..."
        show chelsea blank
        "She blinks once. Twice. The confusion never leaves her face."
        show chelsea sad
        K "But... {i}why?{/i} I don't..."
        "Kate scratches her head, bewildered. If you didn't feel so awkward, you might find it endearing."
    elif True:
        scene black with fade
        "As you hurry back to work, you can't stop thinking about Matt and his request-- and the furious look on his face when you told him no."
        "But what were you supposed to say? There's no way you could go along with that and just {i}hope{/i} no one found out."
        "Worries of what Matt might do plague you as you take care of your customers, and no matter how much you force a smile, you can't bring yourself to fully relax."
        scene bg Lockeroom with fade
        "It's a relief when the end of your shift comes, and you waste no time rushing to the dressing room to check your phone."
        show chelsea confused with dissolve
        "No texts from Matt. You aren't sure whether that's a good thing or not."
        show K Blank at right, moveSprite(0.9, 0.9, 0.0) with dissolve
        K "[pcname]?"
        show K Sad
        show chelsea shocked
        pcname "Kate!"
        show chelsea blank
        "You jump, startled, and turn around to face her."
        "Kate lingers by the closed door, a look of concern on her face."
        K "S-sorry! I didn't mean to scare you..."
        show K Blank
        show chelsea confused
        K "Are you okay? You seemed a little weird out there today."
        show K Embarrassed
        show chelsea shocked
        "She catches herself, eyes widening as she waves her hands back and forth in panic."
        show chelsea blank
        K "N-Not that you're weird or anything! No! You're totally cute!"
        show K Blank
        K "I just meant, um, you seemed like something was off, maybe?"
        show chelsea sad
        show K Embarrassed
        pcname "Ah..."
        show K Blank
        "You glance down at your previous texts with Matt. Kate's gaze follows, her little brows pinching together in confusion."
        show chelsea blank
        "You shove the phone back into your pocket before she can read them."
        show K Embarrassed
        K "What was that?"
        show chelsea embarrassed
        show K Sad
        pcname "Nothing. Don't worry about it."
        show chelsea sad
        K "...Something's bothering you, [pcname]. I can't just not worry about it, even if you tell me to."
        K "Please tell me what's going on. I want to help."
    menu confessaboutmatt:
        "Tell her about Matt." if True:
            "Her pleading eyes, the look of dismay on her face..."
            show chelsea embarrassed
            "How can you keep a secret from a girl like that?"
            show chelsea sad
            show K Blank
            pcname "...There's this guy at my school. His name is Matt."
            show K at center, moveSprite(0.9, 0.7, 0.35)
            pause 1.0
            scene black with fade
            "Kate sits beside you as you tell her about him, the words pouring from your mouth faster than your brain can keep up."
            "Before you know it, you've confessed everything about your relationship with him, down to his request this afternoon."
            "Kate is silent for a long time, biting down on her lip as she soaks everything in."
            "Then, her hand lays on top of yours."
            scene bg Lockeroom
            show K Sad at center, moveSprite(0.7, 0.7, 0.0)
            show chelsea sad
            with fade
            K "Thank you for telling me, [pcname]. I know that mustn't have been easy..."
            show chelsea shocked
            show K Laugh
            K "I want to help you, okay? So I'll do everything I can to get you out of this!"
            show K Blank
            pcname "Ah, Kate... You don't have to--"
            show chelsea blank
            show K Happy
            "But Kate shakes her head, a small smile on her face."
            show K Laugh
            show chelsea embarrassed
            K "I'll find a way to help, okay? So don't worry about it."
            show chelsea blank
            show K Sad
            pause 1.0
            show K Laugh
            "There's a slight painfulness to her eyes as she makes her promise, but Kate smiles at you and gives your hand a squeeze before changing out of her uniform."
            show chelsea embarrassed
            show K Happy
            "You're touched by her determination, but a part of you wonders if you {i}want{/i} to get out of your situation with Matt. Do you even deserve it?"
            scene black with fade
            "Biting your lip, you get changed as well, mulling over these thoughts as you prepare to head home for the night."
            jump events_end_period
        "Make up an excuse." if True:
            "Your heart thuds unevenly in your chest as you consider spilling everything you've been through with Matt."
            "But what would Kate say? You know confessing to her would only hurt her, and that's the last thing you want to do."
            "Forcing another smile, you wave it off."
            show chelsea laugh
            show K Sad
            if vibrator == True:
                if club == "track":
                    pcname "Don't worry about it. I was just trying something new- it's nothing."
                elif club == "cheer":
                    pcname "I just wanted to have a little fun. Don't make a big deal out of it."
                elif club == "yearbook":
                    pcname "I-I was just... trying something. It's nothing..."
            elif True:
                pcname "It's nothing. Don't worry about it."
            show chelsea shocked
            "You expect Kate to let it go, but instead, she stares up at you in frustration."
            show K Blank
            K "It's not {i}nothing{/i}. And it's not just this, I..."
            show K Sad
            show chelsea blank
            K "I saw you go into the bathroom with a boy. I don't... What's going on?"
            show chelsea sad
            "Crap. She saw that? You didn't realize anyone was paying attention during the rush, especially Kate."
            show chelsea embarrassed
            show K Blank
            pcname "It's not what you think. He's just a guy from my school."
            show chelsea blank
            K "So why won't you tell me about him?"
            show chelsea angry
            pcname "Because it's not important."
            show K Mad
            show chelsea shocked
            K "You're hiding something from me, [pcname]."
            show K Sad at right, moveSprite(0.9, 1.0, 0.2)
            show chelsea sad
            "Kate's tone is accusatory and hurt. She takes a step back, obviously upset."
            K "I don't like secrets. I don't want anything being kept from me."
            show chelsea embarrassed
            show K Blank
            pcname "Kate, I promise, it's nothing. You're making this a bigger deal than it is."
            show K Sad
            show chelsea sad
            "She doesn't look like she believes you."
            hide K with dissolve
            "Instead of arguing further, Kate turns around and starts to get changed."
            show chelsea embarrassed
            pcname "Kate..."
            show chelsea sad
            show K Casual Sad at right with dissolve
            K "It was a really busy day. I need to go home and rest."
            hide K with dissolve
            "There's a dejected undertone to her voice as Kate finishes changing and scurries from the dressing room."
            "You watch her go, conflicted."
            scene black with fade
            "This isn't going to work anymore, you realize. You're going to need to make a choice between Kate and Matt-- and soon."
            jump events_end_period

label KateConflicts_Damien:
    "It's a busy day at work as you flit from table to table, stacks of sugar-coated desserts filling the large trays in your arms."
    "It seems everyone has been going crazy for your cafe's choco-kitty sundaes, and word has spread far and wide to fill up every seat in the establishment."
    "You deliver another couple of them at a nearby table, the chocolate-made cats staring up at you cutely before you turn them toward your patrons."
    show chelsea happy with dissolve
    pcname "Enjoy!"
    show chelsea blank
    "You barely have time to bow before you hear your manager calling to you from across the store."
    show EM Neutral at left with dissolve
    "Emilia" "[pcname]! Can you grab table seven?"
    hide EM with dissolve
    "Glancing back, you see Emilia has her own hands full trying to unbox a recent shipment that arrived late."
    show chelsea laugh
    pcname "Sure!"
    hide chelsea with dissolve
    "Putting on your brightest smile, you rush toward the table, making sure to flounce your skirt to appease the guests."
    show chelsea happy at right with dissolve
    pcname "Hello, master! Welcome to-- Damien?"
    show chelsea shocked
    "Shock crosses your face as your customer puts his menu down, revealing Damien's shy yet charming smile."
    $ damienAttire(2)
    show Damien Happy at center, moveSprite(0.65, 0.65, 0.0) with dissolve
    D "Hey, [pcname]."
    show chelsea happy
    "You recover quickly, your smile a little forced as you realize the situation you've been put in."
    show chelsea embarrassed
    show Damien Blank
    pcname "What are you doing here?"
    show Damien Laugh
    D "My mom's getting her haircut nearby, so I figured I'd stop in for a bite to eat."
    show Damien Worry
    show chelsea blank
    D "I didn't realize you guys would be so busy, though... Maybe I should've come another time..."
    show Damien Sad
    "You can't help looking over your shoulder, paranoid that Kate might be lurking around the corner."
    "Thankfully, she isn't anywhere near you-- you catch a glimpse of her bouncing in front of some of her customers, too engrossed in her job to pay attention to you."
    show chelsea embarrassed
    "Your shoulders relax. There's nothing to worry about-- she can't be upset at you for taking care of a customer, right?"
    show chelsea sad
    show Damien Shocked
    pcname "Well, we are pretty busy..."
    show chelsea blank
    show Damien Worry
    "You hope it's enough for Damien to pick up the hint, but the pitiful look he gives you feels like a stab to the heart."
    show chelsea happy
    show Damien Happy
    pcname "But it's okay-- the rush is slowing down, anyway."
    show chelsea embarrassed
    "Damien smiles in relief."
    show Damien Laugh
    D "You sure? Cool."
    show Damien Blank
    show chelsea blank
    "He glances around the cafe, amused by the recent hand-made advertisements for the choco-kitty sundae promotion."
    show Damien Neutral
    D "That looks really good."
    show chelsea laugh
    pcname "Why don't you try one? They're our special of the month right now."
    show Damien Happy
    show chelsea embarrassed
    D "Sure. Whatever you think is best, [pcname]."
    "Damien passes his menu back with a grin."
    show Damien Laugh
    D "This place is really cute. I was curious to see where my girlfriend worked-- it suits you."
    show Damien Happy
    show chelsea blank
    pause 1.0
    show Damien Worry
    "You notice his gaze linger on the maid's uniform a few moments too long before a blush colors his cheeks and he looks away."
    show chelsea shocked
    show Damien Shocked
    "{i}CRASH!{/i}"
    "You both jump at the sound of breaking glass."
    show K Blank at center, moveSprite(0.4, 0.4, 0.0) with dissolve
    show Damien Blank
    "Kate stares at you from a table nearby, the choco-kitty sundae on her tray now a messy, chocolate lump of glass shards on the floor."
    show chelsea sad
    show K Sad
    "Your heart sinks."
    show Damien Neutral
    show K Embarrassed
    pause 1.0
    hide K with dissolve
    "Kate glances away from you, a vibrant blush making its way up her neck as she bends down to clean the mess up."
    show K Embarrassed at center, moveSprite(0.4, 0.4, 0.0) with dissolve
    K "S-Sorry, master. Let me make you a new one."
    scene black with fade
    "You bend down beside her to help."
    scene bg Cafe
    show chelsea blank
    with fade
    pcname "Here Kate, let me--"
    show K Mad at center, moveSprite(0.3, 0.3, 0.0) with Dissolve(0.1)
    show chelsea shocked at center, moveSprite(0.5, 0.7, 0.1)
    K "I'm fine."
    "Her words come out sharp and harsh. You flinch, stumbling back."
    show K Sad
    pause 1.0
    hide K with dissolve
    "You feel numb as you watch her clean up the mess and rush to the kitchen without a word."
    show Damien Neutral at right, moveSprite(0.8, 0.8, 0.0) with dissolve
    D "Everything okay, [pcname]?"
    show chelsea sad
    show Damien Blank
    "Damien glances up at you with genuine concern, his fingers lightly brushing against your fingers in comfort."
    show chelsea embarrassed
    "Your throat tightens."
    pcname "Y-Yeah. I'm just going to go check on her-- I'll be right back with your sundae."
    scene black with fade
    "You can't bring yourself to look back at Damien as you rush back to the kitchen."
    show K Mad at left with dissolve
    "Kate stands near the back of the kitchen, angrily dumping glass into a cardboard box before taping it up and dumping it into the trash."
    "As you step closer, you can see the shimmer of tears down her cheeks, the way her shoulders quake with quiet tears."
    "Swallowing hard, you place a light hand on her shoulder."
    show chelsea sad at left, moveSprite(0.2, 0.2, 0.0) with dissolve
    show K Sad
    pcname "Kate...? Are you okay?"
    "Kate shrugs your hand off and spins on you, her face bright red and eyes puffy. The sight of her heartbreak hurts you more than you expected."
    if KateDamienConfession == True:
        show K Mad
        K "I thought you were breaking up with him!"
        show chelsea embarrassed
        show K Sad
        pcname "I am. Kate, it's complicated--"
        show chelsea shocked
        show K Mad
        K "It's not! I told you, I want to be the only one you're dating, [pcname]. I thought you understood that!"
        show chelsea sad
        show K Sad
        "Her voice cracks and Kate swiftly rubs her eyes with the back of her hand, struggling not to burst into tears."
        pcname "I-I do understand that. I'm sorry, I just..."
        show K Embarrassed
        show chelsea shocked
        K "Are you breaking up with me?"
        show K Sad
        "It comes out like a heartbroken squeal. More tears fall down her cheeks, breaking your heart in two."
        show K Blank
        show chelsea angry
        pcname "No! Of course not!"
        show K Mad
        show chelsea sad
        K "Then what are you doing?"
        show chelsea shocked
        K "I can't date you while you're still seeing him, [pcname]. I want you to break it off-- cut off all ties."
        show K Sad
        show chelsea sad
        K "I can't-- I can't {i}do{/i} this."
        "Her shoulders shake as another sob racks through her body. She struggles to hide her face from you, embarrassed."
        pause 1.0
        show chelsea embarrassed
        pcname "...What are you saying, Kate?"
        "She takes a deep breath, her small frame quivering with the heavy motion."
        show chelsea sad
    elif True:
        show K Mad
        K "What does he mean his {i}girlfriend?{/i} I thought {i}I{/i} was your girlfriend, [pcname]!"
        show chelsea embarrassed
        show K Sad
        pcname "You are! You {i}are{/i} my girlfriend, Kate--"
        show K Mad
        show chelsea sad at left, moveSprite(0.2, 0.3, 0.1)
        K "So then what is he? Your {i}boyfriend?{/i}"
        show K Sad
        "You wince, shrinking back under her harsh tone. You've never seen Kate so angry, so heartbroken, so... betrayed."
        "You need to take control of the situation. But how can you do that without lying to her?"
        show chelsea embarrassed
        show K Blank
        pcname "It's not like that. It's not... We're not that serious--"
        show K Mad
        show chelsea shocked
        K "So he {i}is{/i} your boyfriend!"
        show chelsea sad
        show K Sad
        "It's the wrong thing to say; you realize that as soon as Kate cuts you off, her tone bitter."
        show K Mad
        show chelsea shocked
        K "I should be the only one you're dating, [pcname]! I never agreed to an open relationship!"
        show K Sad
        show chelsea embarrassed
        "She sniffles, wiping the tears from her eyes hastily."
        "You bite your lip, shame heating up your own face as Kate takes a moment to compose herself."
        show chelsea sad
        "She's right; it's not fair of you to do this to her. How did things get so complicated so quickly?"
        "Kate takes a deep breath, her whole body shuddering with a fresh set of tears. You can tell she's barely keeping them back as she speaks."
    show K Blank
    K "If-If you want us to stay together, you have to break up with him. Cut off ties completely."
    show K Sad
    show chelsea shocked
    K "Until you do that, I... I don't think I want to see you."
    show chelsea sad
    "She looks down at her feet, refusing to meet your gaze."
    pause 1.0
    show K Blank
    show chelsea embarrassed
    pcname "...Can't we talk about this? Kate, I'm--"
    show K Sad
    show chelsea shocked
    K "Tell Emilia I'm not feeling well and decided to go home."
    show chelsea sad
    pcname "Kate--"
    K "Let me know what your decision is."
    show K at left, exitScene(0.0, -0.1, 0.1, 0.1)
    "She doesn't look at you as she shuffles her way to the dressing room, her gaze kept down to hide her tears from any prying eyes."
    scene black with fade
    "You watch her go with a sudden emptiness in your heart."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
