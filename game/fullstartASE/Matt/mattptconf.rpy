label conference_intro:
    hide GSGirl with dissolve
    show bg School with fade
    "As you're leaving school, an announcement plays over the loudspeaker."
    "Loudspeaker" "Attention students. This is a reminder that parent teacher conferences will be held Wednesday afternoon."
    "Loudspeaker" "Emails will be sent to remind your parents or guardians."
    show chelsea sad with dissolve
    "A queasy feeling tugs at your belly."
    "You'd almost forgotten about parent-teacher conferences."
    "Will they make you attend alone? Do you even have to go?"
    "For a moment, you consider asking Mr. Harvey."
    if club == "track":
        "But you push the thought away."
        show chelsea happy
        "So what if you have to go alone? Who cares?"
    elif club == "cheer":
        "But you really don't feel like talking about it."
        "The school knows your situation. Surely they'll let you know before then, right?"
    elif club == "yearbook":
        show chelsea shocked
        "But you lose your nerve almost immediately."
        show chelsea sad
        "You don't want to talk about it. Maybe you'll just go home sick that day..."
    hide chelsea with dissolve
    jump events_end_period

label ptconference:
    "When you get to homeroom, you immediately notice a paper on your desk."
    show chelsea confused with dissolve
    pcname "What's this...?"
    "Flipping it over, you skim the page."
    show chelsea shocked
    "{i}Parent-Teacher Conference schedule change...{/i}"
    "There's a chart listing the adjusted class schedule, ending three hours before the end of the school day."
    "For the last three hours, it only has Mr. Harvey's room number listed."
    show chelsea sad
    if club == "track":
        pcname "Shit. I forgot about the conferences..."
    elif club == "cheer":
        pcname "Ugh! I forgot those were today..."
    elif club == "yearbook":
        pcname "Oh no... I forgot..."
    show Harley Neutral at midright with dissolve
    T "Alright, students. On your desks are your adjusted class schedules for today."
    T "As you can see, you'll meet back here in the afternoon."
    T "I'll be meeting with each of you and your parents to talk about your progress this year, so please be prepared."
    hide Harley with dissolve
    hide chelsea with dissolve
    show black with fade
    "Homeroom ends and you go to your next class."
    "All of your classes are much shorter than normal, so your teachers seem more interested in preparing for the conferences than lecturing."
    "As you move quickly through the day's classes, your stomach twists in knots."
    "Lots of parents won't even bother coming, right?"
    "So nobody will notice that yours aren't there either. They won't ask about it."
    "Will they?"
    "You turn it over in your mind, fretting as you walk to the cafeteria for lunch."
    hide black
    show cafeteria
    with fade
    if damienrelate=='dating':
        show Damien Happy with dissolve
        "After grabbing your tray of food, you meet Damien at your usual table, sliding into the empty seat beside him."
        show chelsea at midright with dissolve
        show Damien Worry
        "You zone out as you stare at your tray, too anxious to eat. Maybe you shouldn't have gotten food at all."
        show chelsea shocked
        "You feel Damien's hand gently land on your shoulder, pulling you away from your thoughts."
        D "Is everything okay, [pcname]?"
        show chelsea sad
        pcname "Oh, I..."
        "You feel sick to your stomach. The last thing you want to do is start crying in the middle of the cafeteria."
        "Damien watches you struggle and gently pets your hair, pulling you closer into his side."
        show Damien Neutral
        D "It's okay, [pcname]. Let's talk about it. You can tell me anything."
        if damienknowsaboutfamily==True:
            "Your chest tightens. Damien already knows about your parents, but having to admit their loss is bothering you is hard."
            pcname "Parent teacher conference."
            show Damien Shocked
            "You mumble the words out, barely forcing them past the lump in your throat."
            show Damien Sad
            "Damien blinks in surprise, then recognition crosses his features as he realizes what this means for you."
            D "Oh... Right. I'm sorry, [pcname]. This must be really hard for you."
            show chelsea embarrassed
            "He leans his head against yours, continuing to caress your hair and hold you close. His gentle touch is a bigger comfort than you thought."
            show Damien Worry
            D "Is there anything I can do?"
            pcname "No... Not really. This is nice, though."
            show Damien Sad
            "Damien nods and, although you don't ask for it, he places his cupcake onto your tray and takes away the packet of carrots you don't like."
            "There isn't much he can do, but even that small gesture is enough to make you feel a little better."
        elif True:
            "Your chest tightens. You haven't told Damien about your parents yet, but he's going to find out one way or another."
            "Now is probably the best time to tell him."
            show Damien Blank
            "You just hope he doesn't pity you."
            pcname "Parent teacher conference."
            show Damien Shocked
            "You mumble the words out, barely forcing them past the lump in your throat."
            show Damien Blank
            "He blinks in surprise but nods."
            D "Oh, yeah... My mom's coming, but my dad's at work. Are your parents not able to make it?"
            "You shake your head. You can feel tears brimming at the corners of your eyes, but you hold them back."
            show Damien Shocked
            pcname "My parents... they're dead."
            "You can't bear to look at Damien's face as he registers what you said."
            show Damien Sad
            D "They're... Oh, [pcname], I'm so sorry. I didn't-- I had no idea--"
            "You shake your head. This is exactly what you didn't want."
            if club == "track":
                show chelsea embarrassed
                pcname "Don't pity me, Damien."
            elif club == "cheer":
                show chelsea embarrassed
                pcname "Please, Damien, I don't want your pity..."
            elif club == "yearbook":
                pcname "P-Please don't pity me. I-I... I can't..."
            show Damien Shocked
            D "Oh, no, [pcname], of course not! I'm so sorry. I just... I had no idea."
            show chelsea sad
            show Damien Sad
            D "This must be really hard for you... I understand now."
            "He carefully pulls you closer into his side and holds you, his fingers gently caressing your hair."
            show chelsea embarrassed
            "Although you don't ask for it, Damien places his cupcake onto your tray and takes away the packet of carrots you don't like."
            "There isn't much he can do, but even that small gesture is enough to make you feel a little better."
    elif violetrelate=='Sub':
        show chelsea sad at midright with dissolve
        "Taking your seat at the table, you worry over it again, furrowing your brows."
        show V SubSchool Worried with dissolve
        V "You really shouldn't do that. You'll get wrinkles."
        show V SubSchool Blank
        "She sets your tray in front of you, carefully arranging your fork and spoon before taking her own seat."
        show chelsea shocked
        "You spend several minutes staring at your tray, lost in thought, before you realize Violet is waiting for you to start eating."
        show chelsea sad
        pcname "Oh, sorry. You can eat. I'm... not really hungry."
        show V School Suprised
        "Violet's eyes widen in surprise; you always make her wait for you to start eating."
        show V SubSchool Worried
        V "What's the matter?"
        "Sighing, you shake your head."
        pcname "I..."
        show V SubSchool Sad
        "The words sit like a lump in your throat. You want to force them out, but..."
        "What will Violet think? She expects you to be the strong one."
        show chelsea shocked
        show V SubSchool Worried
        V "Do you want to talk about it?"
        show V SubSchool Sad
        show chelsea embarrassed
        "Her empathy catches you off guard, and you find yourself nodding."
        show chelsea sad
        pcname "Parent teacher conferences are today."
        show V School Blank
        V "Yeah, I know. My parents are 'too busy' to come. Seriously, sometimes I think I might as well not have parents at--"
        "Her mouth hangs open but she never finishes the sentence."
        show V School Suprised
        "Her eyes widen as she realizes what she was about to say - and who she was saying it to."
        show chelsea shocked
        show V SubSchool Sad
        V "Oh no, I forgot. I'm so sorry, [pcname]."
        "To your surprise, she seems genuinely concerned."
        show chelsea embarrassed
        pcname "It's fine..."
        show chelsea sad
        show V SubSchool Worried
        V "This must be really hard for you..."
        if club == "track":
            "You shrug, uncomfortable talking about such sensitive topics."
        elif club == "cheer":
            show chelsea embarrassed
            "You shrug, trying to play it off with a half-hearted smile."
            show chelsea sad
        elif club == "yearbook":
            "You shrug, but you can't help the tears that fill your eyes."
        "Violet reaches across the table, taking your hand in hers and smiling."
        show V SubSchool Happy
        V "It's going to be okay."
        show chelsea embarrassed
        "You nod, overcome by her concern."
        "Forcing your lips into a reassuring smile, you pick up your fork and begin eating."
        "While you're glad to know she cares, you don't want to worry her too much."
    elif violetrelate=='Dom':
        "You grab your tray and Violet's, barely looking at the food you pile onto the trays."
        show V School Pout with dissolve
        "As you return to your table, you set Violet's tray in front of her and find your own chair."
        show chelsea at midright with dissolve
        "Staring down at your plate, you wonder why you bothered getting yourself anything. You're {i}really{/i} not hungry right now."
        show chelsea shocked
        show V School Annoyed
        V "{i}Excuse{/i} me. Are you ignoring me!?"
        "Violet's outraged tone cuts through your thoughts."
        show chelsea sad
        if club == "track":
            pcname "What? Shit, I'm sorry..."
        elif club == "cheer":
            pcname "Huh? Oh... I'm so sorry, Violet."
        elif club == "yearbook":
            pcname "I-- No, of course not, I just..."
        show V School Pout
        "She rolls her eyes."
        show V School Blank
        V "Whatever. I should punish you, but I really don't feel like it right now."
        show V School Annoyed
        V "Can you believe my parents aren't even coming for the conferences?"
        "She waves her hand as she talks."
        show chelsea embarrassed
        V "My mother doesn't even have a job, you know. So shopping is more important than me, I guess."
        "You try to muster some sympathy, but your own dread weighs heavily on your heart."
        V "So I'll probably be the {i}only{/i} person in my homeroom whose parents don't show. Can you believe it?"
        show V School Pout
        "Violet looks at you expectantly, awaiting your reaction."
        show chelsea sad
        show V School Suprised
        pcname "I..."
        "All at once, you see her face fall as the realization strikes."
        show V SubSchool Sad
        V "Oh, right... I guess your parents..."
        show chelsea embarrassed
        "You bite your lip. The last thing you want right now is pity."
        show chelsea shocked
        show V School Smile
        V "Well, at least they have a good excuse, right?"
        "You blink, stunned by her words. And then, you can't help it..."
        show chelsea laugh
        show V SubSchool Happy
        "You start giggling."
        "Maybe it's a little hysterical, but you can't stop. Giggles turn to laughter, and soon you're wiping tears from your eyes."
        show chelsea embarrassed
        pcname "Sorry..."
        "You gasp the word out, struggling to catch your breath."
        show V SubSchool Blank
        V "Feel better?"
        show chelsea happy
        "Smiling tremulously, you nod."
        show chelsea embarrassed
        pcname "I think so."
        show V School Blank
        V "Good. Now eat your lunch; you're making me feel fat."
        "Grabbing your fork, you pick at your food."
        "You're still not very hungry, but it feels like a weight has been lifted off your chest."
    elif True:
        "Like a zombie, you shamble through the lunch line, barely noticing what you put on your tray."
        "Taking a seat, you stare down at your food."
        show chelsea with dissolve
        "You're not even sure why you bothered getting a lunch; you're not hungry anyway."
        "Dread fills your stomach, leaving no room for food."
        "When the bell rings, your lunch sits untouched on the tray."
    "After lunch, you return to your homeroom with heavy feet."
    hide chelsea with dissolve
    if damienrelate == "dating":
        hide Damien with dissolve
    elif True:
        hide V with dissolve
    show black with fade
    "Though you try to convince yourself that nobody will notice that your parents aren't there, you can't quite believe it."
    "As you approach the classroom door, you see that some of the parents have already arrived."
    hide black
    hide cafeteria
    show classroom
    with fade
    "Your chest constricts as you catch yourself searching the room for your parents' faces."
    if mattsubmissive:
        show chelsea shocked with dissolve
        "A sudden voice cuts through your thoughts."
        show GCGirl at midright with dissolve
        "Ms. Miyagawa" "Oh, [pcname], dear! It's so nice to see you again."
        "Startled from your reverie, you turn toward the sweet voice."
        "Matt's mom stands behind you - where, you realize with a start, you've gathered a line since you've been blocking the doorway."
        "Ms. Miyagawa" "Come, dear, let's go in and you can show me where you sit."
        "Dazed, you allow her to usher you into the room, momentarily forgetting your distress."
        "Ms. Miyagawa" "So which one is yours?"
        show chelsea sad
        "Your eyes brim with tears, which you hastily wipe away."
        pcname "Sorry, I--"
        "Ms. Miyagawa" "No need to explain, sweetie. So this one is yours?"
        "You glance down at the desk she's gesturing toward. There is a folded paper with your name printed on the outside."
        show chelsea embarrassed
        pcname "Yeah, that's me."
        "Ms. Miyagawa" "Let's take a look then."
        "She picks up the paper and unfolds it, smiling softly."
        "You wait while she reads, feeling oddly anxious."
        if defymatt:
            "You can't stand Matt, but right now a little motherly attention is exactly what you need."
        elif True:
            "You want Matt's mother to like you. And, truthfully, you appreciate the mothering."
        if intelligence > 40:
            "She smiles approvingly."
            "Ms. Miyagawa" "Well done! I wish Matt would bring home grades like this."
        elif intelligence > 20:
            "She nods."
            "Ms. Miyagawa" "It looks like you're passing all of your classes. That's wonderful."
        elif True:
            show chelsea sad
            "She tries to hold her smile, but you can see it waver."
            "Ms. Miyagawa" "Well, I'm sure you're doing your best."
        "As she passes the paper back to you, you see her eyes dart over your shoulder."
        show chelsea sad
        "Ms. Miyagawa" "Matt! There you are!"
        "Your head sinks low; you know Matt will be angry."
        show Matt Angry at left with dissolve
        m "What's {i}she{/i} doing here?"
        "He folds his arms over his chest."
        "Ms. Miyagawa" "I was just looking over her progress report. Would you like to show me yours?"
        "Matt grimaces, mumbling."
        m "You probably already saw it."
        if intelligence < 40:
            "Ms. Miyagawa" "I think you should study with [pcname]. You two could help each other!"
        elif True:
            "Ms. Miyagawa" "I think you should start studying with [pcname]. She could help you bring those grades up."
        show Matt Pleased
        "Shrinking further, you resist the urge to look at Matt, dreading his reaction."
        m "Yeah, maybe we'll do that. What do you think, [pcname]? I can come over tonight."
        "Ms. Miyagawa" "That would be wonderful!"
        if defymatt:
            show chelsea blank
            pcname "I'm busy tonight. Sorry."
        elif True:
            show chelsea embarrassed
            pcname "If you want to..."
        show Matt Happy
        "Matt laughs, ignoring you."
        m "I have plans with Alex, mom."
        show Matt Smirk
        "Ms. Miyagawa" "Well maybe some other time..."
        show chelsea embarrassed
        "She smiles up at you."
        "Ms. Miyagawa" "I'd like it if my Matty spent more time with a sweet girl like you..."
        show Matt Angry
        "Matty" "Mom!"
        show chelsea laugh
        show Matt Blank
        "You can't help but giggle, earning yourself a glare from Matt."
        show chelsea embarrassed
        show Harley Happy at right with dissolve
        T "Mrs. Miyagawa, so nice to see you."
        show Harley Neutral
        "Ms. Miyagawa" "Oh, please, it's Ms. Miyagawa now."
        show Harley Question
        T "My apologies. Do you have a few minutes to talk about your son's progress?"
        "Ms. Miyagawa" "Of course, Mr. Harvey."
        show Harley Neutral
        "She turns to you."
        "Ms. Miyagawa" "Please keep Matt company while I talk to your teacher."
        show chelsea shocked
        hide GCGirl with dissolve
        hide Harley with dissolve
        "To your surprise, she winks as she walks away."
        show chelsea embarrassed
        if defymatt:
            "Matt's the {i}last{/i} person you want to talk to, but his mom..."
            "You glance down at your desk, thinking of her trying to be supportive."
        elif True:
            "You glance down at your desk, not wanting to meet Matt's eyes."
            "Your gaze lands on your progress report, and you can't help thinking of Ms. Miyagawa's kindness."
        "Who would have thought Matt's mom would be so sweet?"
        show chelsea blank
        show Matt Angry
        m "I told you not to talk to my mom, slut."
        show chelsea angry
        if club == "track":
            pcname "It's not {i}my{/i} fault. She approached me!"
        elif club == "cheer":
            pcname "I can't help it that she likes me!"
        elif club == "yearbook":
            pcname "But I didn't-- She started talking to me and..."
        show chelsea blank
        show Matt Question
        m "So you're blaming her?"
        show Matt Blank
        "He crosses his arms over his chest, looking down his nose at you."
        m "I'm not going to tell you again. Don't talk to my mom or you'll regret it."
        if defymatt:
            show chelsea angry
            pcname "Don't worry. I don't want anything to do with you {i}or{/i} your mom."
        elif True:
            show chelsea sad
            pcname "I understand, Matt."
        show Matt Smirk
        "Before Matt can respond, Ms. Miyagawa returns."
        show chelsea blank
        show GCGirl at midright with dissolve
        show Matt Blank
        "Ms. Miyagawa" "What a nice man, that Mr. Harvey."
        "She smiles at both you and Matt, looking between you both."
        "Ms. Miyagawa" "It's too bad Matty won't be home for dinner tonight. We would love to have you over."
        "Ms. Miyagawa" "I keep telling him that he needs a girlfriend..."
        show chelsea laugh
        show Matt Angry
        m "Mom!"
        "Her smile widens as she waves him off."
        show chelsea embarrassed
        "Ms. Miyagawa" "What? She's a sweet girl!"
        show Matt Blank
        "Ms. Miyagawa" "Promise you'll come have dinner sometime soon, dear?"
        if defymatt:
            "You don't want to spend more time with Matt than you have to, but his mother has been so kind to you."
        elif True:
            show chelsea sad
            "Torn between Matt's orders and his mother's kindness, you hesitate."
        show chelsea sad
        pcname "I... I don't..."
        "She smiles, taking your hesitation as agreement."
        show Matt Angry
        "Ms. Miyagawa" "Oh, it will be lovely to have one of Matty's friends over again."
        "Ms. Miyagawa" "I'll figure out Matt's schedule and invite you soon, okay?"
        show chelsea embarrassed
        "Smiling weakly, you nod your head."
        pcname "Sounds... great."
        "Ms. Miyagawa" "Well, we should be going, dear. We'll talk soon, though."
        show Matt Blank
        "Matt glares at you one last time before his mother leads him away."
        hide GCGirl with dissolve
        hide Matt with dissolve
        "Heaving a sigh of relief, you wonder if she'll really follow through with that invitation."
        hide chelsea with dissolve
    elif True:
        show chelsea sad with dissolve
        "Though you knew they couldn't possibly be here, their absence strikes like a punch to the gut."
        "Tears fill your eyes and, all at once, you realize you can't do this."
        show chelsea at exitScene(0.5, -0.5, 0.35, 0.25)
        "Dashing down the hallway, you burst into the bathroom."
        show black with fade
        "There, you finally give in to your despair, sobbing loudly."
        "For a while, all you can do is hold yourself as you cry."
        "Eventually the sobbing subsides and, drained, you dry your face and pull yourself together."
        "But you still can't face that room, full of your classmates and their parents, so you hide out in the bathroom until the end of the day."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
