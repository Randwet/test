label bakery_uniform:
    show L Blank at left with moveinleft
    show chelsea at right with moveinright
    L "What a busy day!"
    "Lisa approaches you behind the counter, a dirty rag in hand. You remain crouched down behind one of the display cases, sweeping out the excess crumbs."
    pcname "Keith said he's coming in early tomorrow to get a head start on restocking."
    L "That'll be helpful."
    "Lisa lingers behind you. Her fingers brush along your blonde locks gently."
    show L Happy at left
    L "I can't get over your blonde hair. It looks {i}so{/i} good on you, [pcname]."
    if club == "track":
        show chelsea happy
        pcname "It {i}feels{/i} good! I feel pumped whenever I look in the mirror!"
        L "I'm so happy to hear that, [pcname]!"
    elif club == "cheer":
        show chelsea happy
        pcname "Thanks, Lisa. It's actually so much easier to buy clothes now. Blonde hair goes with everything!"
        L "I know, right?"
        L "I guess that gives us another excuse to go back to the mall!"
        "She lets out a small laugh. You smile at the idea."
    elif club == "yearbook":
        show chelsea embarrassed
        "You sheepishly toy with a piece of your hair and smile."
        pcname "T-Thank you. I've really grown to like it."
        L "See? I told you trying new things would be fun."
    "As you finish sweeping the rest of the crumbs into a small trash can, Keith approaches you behind the counter."
    show Keith Neutral with dissolve
    show L Blank at left
    show chelsea blank
    BM "When you're done cleaning up, both of you come to my office for a meeting."
    show chelsea confused
    show Keith Blank
    "You glance at Lisa in confusion, but she gives Keith a pleasant smile."
    show L Happy at left
    show chelsea blank
    L "Sure thing, Keith."
    pcname "Alright."
    hide Keith Blank with moveoutleft
    "Keith walks back to his office and shuts the door behind him."
    show chelsea confused
    pcname "A meeting? Do you know what it's about?"
    show L Blank at left
    L "You know Keith. He's probably trying to find another way to bring in new customers."
    show L Happy at left
    L "Although, a lot of people have been leaving good reviews. I bet it's because of your hair."
    L "The guys that come in can't get enough of it."
    show chelsea happy
    "She plays with a strand of your hair again, teasing. You smile."
    if bakery_flirtwkeith == True:
        show L Happy at left
        L "So, has Keith been any friendlier toward you?"
        show chelsea blank
        "She gives you a suggestive smile. You know she's referring to your attempts to flirt with him."
        show chelsea embarrassed
        pcname "A little bit, yeah."
        pcname "I haven't found a lot of chances to improve on that, though..."
        show chelsea blank
        L "You just have to make your own chances. Sometimes just giving him a smile and agreeing with him is enough."
    elif True:
        L "You've been doing a great job lately, [pcname], but just remember that a happy boss makes for a happy employee."
        "You can tell by her suggestive look that she means her earlier suggestion to flirt with Keith."
        show chelsea blank
        pcname "I don't know about that, Lisa..."
        L "It doesn't take much. Sometimes just giving him a smile and agreeing with him is enough."
    show L Blank at left
    L "Men like to feel smart, you know."
    "You nod in understanding."
    show L Happy at left
    L "Well, everything looks good out here. Let's see what Keith wants."
    show L Blank at left
    "You finish replacing the trash bag in the bin and, after washing your hands, follow Lisa into Keith's office."
    hide L Blank with moveoutleft
    hide chelsea with moveoutleft
    show bg BakeryOffice with dissolve
    "You both take your seats across from his desk and wait patiently for him to speak."
    show L Blank at left with moveinright
    show chelsea at right with moveinright
    show Keith Neutral with dissolve
    BM "Alright. I know you girls want to go home, so let's try to make this quick."
    show Keith Blank
    "Keith pulls out a binder from behind his desk and opens it up."
    show Keith Neutral
    BM "Sales have been doing pretty well so far. We have a few new seasonal items coming out, so make sure to memorize their ingredients and suggest them to customers."
    BM "But I still want to try a few new changes around here. So, I have a surprise for you."
    show Keith Blank
    "Keith flips through the binder until he finds what he's looking for. He turns the binder so you both can get a good look at it."
    show Keith Neutral
    show chelsea confused
    BM "Starting next week, you'll be getting a new uniform."
    show Keith Blank
    "There is a collage of clothes on the page that make up your new uniform including a low-cut blouse with a cupcake embroidered on the right side, a tight pencil-skirt that barely reaches your knees, and heels. The new apron only covers the skirt."
    show chelsea blank
    if club == "track":
        "As you try to picture yourself in the new uniform, you realize how constricting it's going to be to your movement. How are you going to serve customers in heels and a tight skirt?"
        "Still, it's not as though you hate it. Maneuvering in this outfit could be a new challenge, and you like challenges."
    elif club == "cheer":
        "As you try to picture yourself in the new uniform, you realize just how revealing it will be. You can already hear the comments from customers as you bend over to wrap up their desserts."
    elif club == "yearbook":
        "You can't help but blush as you try to picture yourself in the new uniform. You're going to be so exposed in this!"
    "Keith looks to you, trying to gauge your reaction."
    show Keith Confused
    BM "You look like you want to say something, [pcname]."
    menu bakery_uniformreact:
        "I love it!" if True:
            $ corruption += 2
            show chelsea happy
            show Keith Blank
            if club == "track":
                "You think back to your stilettos at home. They weren't comfortable to move around in either, but now you can walk around in them no problem!"
                "You're sure you can learn to move around with ease in this new uniform, too."
            elif club == "cheer":
                "You stare at the new uniform, a small smile curling on your lips. This outfit will show off all of your best assets, and it looks a lot more mature than your current uniform."
            elif club == "yearbook":
                "Normally you would shy away from this type of outfit, but you think about what a huge change dying your hair had been and how nicely it turned out..."
                "The idea of being seen in such a revealing uniform is terrifying, but it could also turn out to be fun!"
            show L Happy at left
            L "I was thinking the same thing! This uniform is just the change we need, Keith."
            L "I can't wait to try it on!"
            show Keith Happy
            BM "That's great to hear."
            BM "I expect them to arrive tomorrow, but that'll depend on the shipping company. Whenever they do get here, they'll be hanging up in the back for you."
            BM "Make sure to wear them as soon as they get here. The change will start immediately."
            "Keith pulls back the binder and puts it away behind his desk."
            show Keith Neutral
            BM "Well, that's all. You're free to go."
            L "Thank you, Keith."
            pcname "Thanks."
            scene bg black with dissolve
            "You join Lisa outside of Keith's office and make your way to the back to change out of your uniforms."
            "You both express your excitement for the new uniforms as you change and leave for the night."
            $ bakeryuniformagree = True
            $ bakeryagree +=1
            jump events_end_period
        "Isn't it a little revealing?" if True:
            show chelsea confused
            show L Disappoint at left
            show Keith Confused
            if club == "track":
                "You can't imagine trying to complete basic daily tasks in this new uniform. You'd be too worried about flashing someone while you try to bend over to get desserts out of the display case!"
                "Not to mention how many blisters those heels will give you..."
            elif club == "cheer":
                "While you'd like to try a more mature, sexy look, there's a time and place for it. This outfit seems too revealing for work."
            elif club == "yearbook":
                "You feel horribly embarrassed at the idea of wearing such an exposing outfit. People already stare at your hair- imagine what they'll think of you in this new uniform!"
            "Both Lisa and Keith frown at you."
            BM "Revealing? Nah. This is perfectly normal, [pcname]."
            BM "Have you seen what the girls down at Le Petite Bakery wear? This doesn't come {i}close{/i} to the skirts they have their girls strut around in."
            show L Happy at left
            L "Besides, we'll look so cute in these uniforms, [pcname]. Just look at those shirts! The cupcake was a great choice, Keith."
            show Keith Happy
            BM "Thanks. I thought we could use a little more work on our branding."
            show L Blank at left
            menu uniformreact2:
                "I'm not comfortable with this outfit." if True:
                    show chelsea blank
                    show Keith Angry
                    show L Disappoint at left
                    "Keith and Lisa look to each other impatiently, displeased with your answer."
                    "Keith gives you a stern look and jabs a finger at the uniform in the binder."
                    BM "It's not up for debate, [pcname]. This is the new uniform."
                    "Keith slams the binder shut and shoves it back in place behind the desk."
                    BM "I expect you both to wear the uniforms as soon as they come in."
                    show L Happy at left
                    L "Of course, Keith."
                    show Keith Blank
                    "Keith gives you one last glare before turning his attention to his computer."
                    "You awkwardly stand up from your chair and follow Lisa out of the room."
                    if bakeryagree >= 7:
                        L "It's not going to be that bad, [pcname]. I'm sure you'll change your mind once you actually put it on."
                    elif True:
                        L "You should get used to changes like this, [pcname]. You're being pretty ungrateful for the hard work Keith put in to get us new uniforms."
                    L "I've been wearing the same uniform for years. I'm happy for the change."
                    "Neither of you speak any longer as you get changed and head home for the night."
                    $ bakeryagree -=1
                    jump events_end_period
                "Well, if other girls dress like this, I guess it can't be so bad." if True:
                    $ corruption += 1
                    show chelsea embarrassed
                    show Keith Blank
                    show chelsea blank
                    "Keith relaxes back into his chair. He shuts the binder and places it back behind the desk."
                    show Keith Happy
                    BM "I knew you'd come around, [pcname]."
                    show Keith Neutral
                    BM "The new uniform change is actually going to help save us some money, too. That might mean some raises in your futures."
                    show Keith Blank
                    show chelsea happy
                    show L Happy at left
                    "You and Lisa share an eager smile."
                    show Keith Neutral
                    BM "The new uniforms should be in this week depending on the shipping company. Hoping to have them tomorrow, but we'll see."
                    BM "That's all for tonight. You're free to go."
                    show Keith Blank
                    L "Thank you, Keith."
                    pcname "Thanks."
                    scene bg black with dissolve
                    "You follow Lisa out of Keith's office and into the back."
                    "As you're changing, you and Lisa share your thoughts about the new uniforms before heading home for the night."
                    $ bakeryuniformagree = True
                    $ bakeryagree +=1
                    jump events_end_period

label bakery_stuffing:
    show chelsea confused at right with moveinright
    "As you step into the bakery, you're surprised to see Keith opening a large cardboard box at the counter. Lisa takes out plastic packages beside him and organizes them to the side."
    show Keith Neutral with dissolve
    BM "Ah, [pcname]. You're here."
    show chelsea blank
    BM "The new uniforms just came in. Grab a pile and try them on in the back."
    show Keith Blank
    if bakeryuniformagree == True:
        show chelsea happy
        pcname "Oh! Sure!"
    elif True:
        show chelsea sad
        pcname "Oh... Okay..."
        show chelsea blank
    "You and Lisa each grab one of the plastic piles and take them to the back."
    pause 1.0
    hide Keith Blank with dissolve
    show bg black with dissolve
    hide chelsea with dissolve
    show bg Bakery with dissolve

    $ LHappy = "Characters/Lisa/Uniform 2/Happy.png"
    $ LBlank = "Characters/Lisa/Uniform 2/Blank.png"
    $ LQuestion = "Characters/Lisa/Uniform 2/Questioning.png"
    $ LDisappoint = "Characters/Lisa/Uniform 2/Disappointed.png"
    $ LSad = "Characters/Lisa/Uniform 2/Sad.png"
    pause 0.1
    $ bakerycorrupt = 2
    $ clothes = 'bakerynew'
    show chelsea shocked at right with dissolve
    "As you both slip into the outfit, you realize just how tight the new skirt is on you. Even bending over, it barely covers your ass."
    show L Happy at left with dissolve
    "Lisa notices you examining the outfit and lets out a small laugh."
    L "It really doesn't leave much to the imagination, does it?"
    "She steps behind you and helps you tie the apron around your waist securely."
    L "You look great, [pcname]. This new uniform suits you!"
    if bakeryuniformagree == True:
        if club == "track":
            show chelsea happy
            "You smile, turning to examine yourself in the mirror at every angle. You look great and you {i}feel{/i} great, too!"
            "As you turn a little, you notice just how big of a gap there is in your shirt."
        elif club == "cheer":
            show chelsea happy
            "You smile, posing in the mirror to see yourself at every angle. You definitely feel a little more mature in your new outfit."
            "But..."
        elif club == "yearbook":
            show chelsea embarrassed
            "You smile, unable to contain your blush as you sheepishly try to tug the skirt down a little lower."
            "As you turn to see how the top looks at another angle, you notice what a big gap there is between your chest and the fabric."
    elif True:
        show chelsea blank
        "You frown, turning to examine the new uniform in the mirror. It's every bit as revealing and uncomfortable as you thought it would be."
    pcname "Lisa, does the top look a little weird to you?"
    show chelsea blank
    show L Question at left
    L "What do you mean?"
    "You take some of the fabric in front of your bust and hold it out. The fabric hangs loosely, open where your breasts should fill it out."
    show L Blank at left
    L "Hmm..."
    show L Sad at left
    L "Now that you mention it, you don't really have the bust to fill this sort of top out, do you?"
    show chelsea sad
    "You glance at Lisa's bust with a frown and notice how perfectly she fits in this new uniform. Her tits are practically ready to pop out of the fabric."
    show L Disappoint at left
    L "We can't really have you looking like that at work. You look like a child playing dress-up."
    show L Blank at left
    "Lisa thinks for a moment, tapping her chin. Suddenly, an idea hits her."
    show chelsea shocked
    show L Happy at left
    L "I know! What if you tried stuffing your bra?"
    show chelsea blank
    if club == "track":
        pcname "Stuffing my bra? With what?"
        L "Well, tissue and toilet paper used to be common when I was in school, but I have something that might work better."
    elif club == "cheer":
        pcname "You really think I need to go that far?"
        L "Well, you may not be an ironing board, but you're fairly small-chested compared to most women."
        show chelsea sad
        "You examine your chest in the mirror, a little discouraged. You had thought your breasts were a nice size, but seeing their failure to fit your new uniform shirt you suddenly feel childish in comparison."
        "Especially when compared to Lisa's..."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "S-Stuff my {i}bra?{/i}"
        L "Yeah. It's not that big of a deal, [pcname]. A lot of girls do it."
    show L Blank at left
    L "I have some extra silicone bra inserts in my purse. You can have them if you'd like."
    show chelsea confused
    if club == "track":
        pcname "They make those?"
    elif club == "cheer":
        pcname "That might not be a bad idea..."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "I-I'm not sure...They seem a bit much..."
        show L Happy at left
        L "There's nothing to be embarrassed about, [pcname]. You won't know until you try it."
    show L Blank at left
    L "Do you want to try them out?"
    show chelsea blank
    menu bakery_stuffingbra:
        "Stuff your bra." if True:
            $ corruption += 1
            if club == "track":
                pcname "Yeah, I guess I could give it a try."
            elif club == "cheer":
                pcname "Yeah. Stuff me up."
            elif club == "yearbook":
                pcname "Well... I-If you really think it'll help..."
            show L Happy at left
            L "Great! I'll go grab them."
            hide L Happy with moveoutleft
            "Lisa steps out for a moment to retrieve her purse."
            show chelsea sad
            "You take the moment by yourself to stare at your bust in the mirror. Your boobs look so small, practically lost, in your shirt fabric."
            show chelsea happy
            "Stuffing your bra will definitely help fix it."
            show chelsea blank
            "Lisa returns shortly after with two packs of silicone bra inserts. She passes them to you."
            show L Blank at left with moveinleft
            L "I thought you could use some extras, just in case."
            show chelsea happy
            pcname "Thank you."
            "You slip the inserts into your bra and adjust your boobs accordingly."
            show L Happy at left
            L "There! That looks so much better, [pcname]."
            L "Maybe you should wear those all the time."
            show L Blank at left
            "You definitely feel like you fit into your top a little more. Glancing in the mirror, you see that your breasts look better, too."
            show L Happy at left
            L "Let's go show Keith how the new uniforms look."
            hide chelsea with moveoutleft
            $ bakeryagree +=1
            $ bakerystuffing = True
        "Don't stuff." if True:
            show chelsea blank
            if club == "track":
                pcname "Thanks, but no thanks, Lisa. I'll feel even sillier with those things in my bra."
            elif club == "cheer":
                "You consider it for a moment, then shake your head."
                pcname "Ah... No thanks, Lisa. I'll figure out another way to make this work."
            elif club == "yearbook":
                show chelsea sad
                pcname "U-Um... I- No thank you, Lisa. I-I'd rather just stay like this..."
                show L Disappoint at left
                L "{i}Really?{/i}"
            "Lisa wrinkles her nose in distaste."
            show L Question at left
            L "Well, it's your choice, but just know that you look {i}incredibly{/i} silly."
            L "I doubt Keith is going to be okay with you looking like that."
            show L Blank at left
            "She sighs, adjusting herself in the mirror."
            show L Happy at left
            show chelsea blank
            L "Well, let's go show him how the new uniforms look."
            hide chelsea with moveoutleft
            $ bakeryagree -=1
    hide L Happy with moveoutleft
    scene bg black with dissolve
    "You follow Lisa back out to the front of the bakery."
    show bg Bakery with dissolve
    show L Happy at left with moveinleft
    show chelsea at right with moveinleft
    show Keith Happy
    "Keith eyes Lisa over, nodding in approval as she gives a spin in her new uniform."
    BM "Very nice..."
    show Keith Blank
    "He turns his attention to you."
    if bakerystuffing == True:
        show chelsea happy
        show Keith Confused
        BM "Huh. [pcname]..."
        "Keith gives your body a once-over, pausing slightly at your shirt."
        show Keith Happy
        BM "I'm not sure what you did, but there's something different about you."
        BM "Whatever it is, keep it up."
        if club == "track":
            "You straighten your shoulders, confident under his approval."
        elif club == "cheer":
            "You smile coquettishly, pressing your arms together slightly. Your cleavage looks a little more pronounced."
        elif club == "yearbook":
            "You feel your cheeks heat up a little and shyly look down at your exposed cleavage."
        "Out of the corner of your eye, you see Lisa give you a sly smile and a wink. You return her gesture with your own grin."
        BM "Alright! Looks like the uniforms are a success."
        BM "Now let's get to work."
    elif True:
        show Keith Angry
        BM "What the hell is that?"
        show chelsea sad
        pcname "Well, the shirt is a little big..."
        BM "You look fucking ridiculous!"
        BM "You can't represent the bakery looking like that!"
        if club == "track":
            pcname "I'll figure something out."
            BM "You'd better!"
        elif club == "cheer":
            pcname "I'll fix it."
            BM "Damn right you will!"
        elif club == "yearbook":
            pcname "I-I know. I'll, um... um..."
            BM "'Um, um'-"
            "Keith mocks your stammering. You shrink, embarrassed."
            BM "I'm not taking any excuses! Figure something out!"
        "Irritated, Keith glares between you and Lisa."
    show Keith Neutral
    show chelsea blank
    BM "[pcname], clean up this mess then take over the register."
    show Keith Blank
    show L Blank at left
    "Keith gestures toward the empty cardboard box and other packaging around it."
    show Keith Neutral
    BM "Lisa, get started on baking the muffins. I have a list on the counter for you."
    show Keith Blank
    L "Yes, sir."
    pcname "Yes, sir."
    hide Keith Blank with moveoutleft
    "Keith retreats to his office, leaving you and Lisa alone."
    if bakerystuffing == True:
        show L Happy at left
        L "Stuffing your bra was definitely a good idea. You look so much better now."
        L "Just make sure to keep it up, okay?"
        show chelsea happy
        "Lisa gives you a smile before walking off and starting her work on the muffins."
        "You clean up the packaging and take your position behind the register."
        "You receive several compliments on your new uniform."
        "You're sure the extra padding has something to do with it, but it's a great confidence boost either way!"
    elif True:
        show L Disappoint at left
        "Lisa sighs and shakes her head."
        L "I told you he'd have a problem with this."
        "She gestures toward your ill-fitted shirt."
        L "Try to fix that before we get customers."
        show chelsea sad
        "Lisa walks off to handle the muffins while you clean up the packaging and take your position behind the register."
        "You receive several comments on your new uniform, some good, some bad, but many seem to agree that the top looks a little weird."
        "You'll need to find a solution to that..."
    jump events_end_period

label bakery_implants:
    show chelsea at right with moveinright
    "As you come into work for the day, you notice that Lisa seems to be manning the store by herself. Keith is noticeably absent."
    pcname "What happened to Keith?"
    show L Blank at left with moveinleft
    L "He has the day off."
    show chelsea shocked
    pcname "Day off?"
    "It never occurred to you that Keith would take a day off, but now you feel a little foolish for thinking otherwise."
    show chelsea blank
    "Everyone needs some time away from work sometimes. Even Keith."
    L "Yeah. I think he mentioned something about needing to wait for a repairman for his refrigerator."
    show chelsea confused
    pcname "Huh. Okay."
    "It's hard to picture Keith's life outside of the bakery. A part of you almost thought that he lived in his office."
    show chelsea blank
    if bakeryagree >= 10:
        "You shrug and walk to the back to get changed into your new uniform. It'll be extra work with only the two of you today, but you're sure that you and Lisa can handle it."
    elif True:
        "You smile to yourself as you walk to the back and get changed. Not dealing with him for the day will be a nice change."
    "Once changed, you walk back to the front of the bakery and join Lisa behind the counter."
    "Lisa finishes up with a customer at the register. The bakery is unusually dead today. Once the customer leaves, you're the only two in the store."
    if bakerystuffing == True:
        show L Happy at left
        "Lisa turns to you with a smile."
        L "So, have you gotten used to the new uniforms yet?"
        show chelsea happy
        if club == "track":
            pcname "Mostly, but this top is so {i}annoying{/i}. I hate having to pad my bra every day."
        elif club == "cheer":
            pcname "For the most part, but padding is such a pain. My boobs start to get all sweaty if I wear them for too long. It's {i}so{/i} gross."
        elif club == "yearbook":
            pcname "W-Well, yes, but..."
            "You adjust your cleavage a little, uncomfortable. One of the silicone cups peeks out of your bra. You tuck it back in."
            show chelsea embarrassed
            pcname "Keeping the pads hidden is, um, difficult."
        show L Blank at left
        "Lisa nods sympathetically."
        L "That does sound pretty difficult."
        show L Happy at left
        show chelsea confused
        L "You know, if you hate stuffing your bra so much, there are {i}other{/i} options."
    elif True:
        show L Disappoint at left
        "Lisa turns to you. Her smile falters when she views your ill-fitting shirt."
        L "I see you still haven't fixed the top..."
        if club == "track":
            show chelsea angry
            "You cross your arms over your chest defensively."
            pcname "It's not like I haven't been trying. This stupid shirt is cut weird."
        elif club == "cheer":
            "You let out a loud sigh, leaning on the counter with your elbow. You rest your chin in your palm, exasperated."
            pcname "I've tried {i}everything.{/i} My boobs just won't cooperate."
        elif club == "yearbook":
            show chelsea sad
            pcname "I-It's hard... I'm just not big enough..."
            "You cup your hands over your chest, trying to pull the shirt over your cleavage a little more. It doesn't work."
        show L Happy at left
        L "You know, if you really don't want to stuff your bra, there are {i}other{/i} options."
    show chelsea confused
    pcname "Other options? Like what?"
    show L Blank at left
    L "Something a little more permanent."
    L "Have you ever considered getting breast implants, [pcname]?"
    if club == "track":
        show chelsea laugh
        "You burst out laughing. She can't be serious, right?"
        pcname "No way. That's for like, cheap trophy wives and prostitutes!"
        pcname "Not to mention how hard it would be to run track with two balloons smacking into my face. No thanks."
        show L Disappoint at left
        L "Is that what you think? Oh, [pcname], those are just bad stereotypes."
        show L Question at left
        L "I promise, getting implants isn't anything like that."
        show chelsea happy
        pcname "Well, maybe not, but it's not like I make enough money for that stuff."
    elif club == "cheer":
        "You tilt your head to the side, considering her suggestion. It's not something you had thought of before, but the idea appeals to you."
        pcname "Not really. That's a lot of work to put into fitting in a uniform, though."
        show L Happy at left
        L "But imagine how much more mature you'll look than the other girls at school."
        L "They'd be so jealous. Not to mention, you could get any boy you want."
        show chelsea happy
        pcname "I guess I {i}would{/i} look pretty hot..."
        L "Exactly!"
        show chelsea sad
        pcname "But even if I {i}wanted{/i} to do it, I have no idea how I'd get the money for it."
    elif club == "yearbook":
        show chelsea shocked
        "You're so shocked by her suggestion that you don't say anything for a few moments."
        show chelsea embarrassed
        "You feel the heat rise up your neck, through your cheeks, and up to the tips of your ears. Your entire face must be bright red."
        pcname "I-I-I-"
        pcname "N-No! Of- Of course not!"
        show L Question at left
        L "Why not? It sounds like it would help a lot."
        show L Sad at left
        L "There's no shame in making changes to your body."
        show L Happy at left
        L "In fact, a lot of girls feel even more confident after cosmetic surgery."
        "You bite your lip. More self confidence is tempting, but to make such a big change... Especially to your... {i}your...{/i}"
        pcname "I-I...I couldn't! I-I don't even know how I'd... how I'd even afford..."
    show L Blank at left
    L "I'm sure we could find some affordable options."
    show L Happy at left
    L "You should really consider it, [pcname]. I'd be happy to look into it for you."
    show chelsea blank
    menu bakery_considerimplants:
        "I'll think about it." if True:
            show chelsea happy
            "Lisa claps her hands together in excitement."
            L "Wonderful! I'll help you look into the whole process. I'll be with you every step of the way."
            pcname "I didn't say I'm definitely doing it..."
            "Lisa waves you off, barely paying attention. She pulls up her phone, already looking up websites and information."
            show L Blank at left
            L "I know, I know. But you still need to know everything about it, right?"
            show L Happy at left
            L "You're going to look so hot, [pcname]!"
            show chelsea blank
            "You sigh and let her go. Nothing you say will stop her now."
            show chelsea happy
            "At least she's excited about it..."
            show chelsea blank
            "A customer enters the bakery and you begin the rest of your work day."
            $ bakeryagree +=1
            jump events_end_period
        "I'm not really interested." if True:
            show L Disappoint at left
            "Lisa frowns, clearly disappointed."
            L "Aw, are you sure? You would look so hot, [pcname]..."
            show L Sad at left
            L "And I really wouldn't mind looking into it for you."
            pcname "I'm sure. I don't think cosmetic surgery is for me."
            "Lisa sighs and picks up her phone."
            L "Well, if you change your mind..."
            "Lisa absorbs herself in her phone. You sigh and take your place behind the register."
            "A customer enters the bakery and you begin the rest of your work day."
            $ bakeryagree -=1
            jump events_end_period

label bakery_loan:
    "Halfway through your shift, a shipment of take-out supplies and bulk ingredients arrives."
    "Keith signs the invoice and you all help the deliverer carry the boxes inside."
    "Once all is said and done, Keith turns to you and Lisa."
    show chelsea at right with moveinright
    show L Blank at left with moveinleft
    show Keith Neutral with dissolve
    BM "Lisa, I need you to clean out the stock room so [pcname] can put this stuff away."
    show Keith Blank
    show L Happy at left
    L "Yes, sir."
    show Keith Neutral
    BM "[pcname], take care of the boxes out front and watch for customers. When you're done restocking, break down these boxes and toss them in the dumpster out back."
    show L Blank at left
    show Keith Blank
    pcname "Alright."
    hide Keith Blank with moveoutleft
    "Keith nods and retreats to his office."
    "Lisa steps into the stock room as you begin to cut open the boxes. She returns shortly after and helps you unload the supplies."
    show chelsea confused
    pcname "I thought you had to clean out the stock room?"
    show chelsea blank
    L "There isn't much to clean out. It'll be easier to organize once I have everything together, anyway."
    "You shrug, passing one of the open boxes to Lisa. While she unloads the supplies, you work on cutting and breaking down the boxes."
    "You both work like this for a while in silence, occasionally bringing up sales around the mall or a new fashion trend that's sprung up in town."
    show L Happy at left
    "After a moment, Lisa turns to you with a smile."
    L "So, have you thought about our conversation the other day?"
    show chelsea confused
    pcname "Our conversation...?"
    show L Blank at left
    L "About the boob job."
    show chelsea shocked
    pcname "{i}Oh!{/i}"
    menu bakery_boobthoughts:
        "Yeah, I've thought about it." if True:
            show chelsea blank
            show L Happy at left
            "Lisa beams, pleased to hear that you've considered her suggestion."
            L "That's great! What do you think?"
            menu bakery_boobthoughts2:
                "It's tempting, but I really don't have the money." if True:
                    show L Blank at left
                    "Lisa nods enthusiastically."
                    L "I thought it might interest you! Don't worry, money is something we can always figure out."
                    L "I actually have something that might help your decision."
                    show chelsea confused
                    "You tilt your head to the side, curious. Lisa leans forward, her excitement contagious."
                    pcname "What is it?"
                    $ bakeryagree +=1
                "I'm not really sure it's for me..." if True:
                    show chelsea sad
                    show L Disappoint at left
                    "You catch a glimpse of disappointment on her face, but it quickly vanishes with a smile."
                    show L Blank at left
                    L "Well, maybe I have something that can persuade you."
                    show chelsea confused
                    "You can't help but give her a skeptical look. She doesn't seem to mind."
                    $ bakeryagree -=1
        "No, not really..." if True:
            show chelsea blank
            show L Question at left
            "Lisa frowns, clearly disappointed."
            show L Blank at left
            L "Well, I had been hoping you would take some time to think it over seriously..."
            L "Maybe I have something that can persuade you."
            show chelsea confused
            "You give her a skeptical look. Lisa tries to ignore it, but you can tell she's bothered by your attitude."
            $ bakeryagree -=1
    L "I did a little research at home recently on local cosmetic surgeons."
    show chelsea blank
    L "I know your primary concern was money, so I made sure to look into some with great reviews that also wouldn't break the bank."
    L "I have a whole sheet on it for you to look over."
    "You open your mouth to speak, but Lisa holds up a hand to stop you."
    L "Wait right here."
    hide L Blank with moveoutleft
    "Before you have a chance to voice your opinions, Lisa rushes to the back."
    "You continue to break down the cardboard boxes and stock them in a pile to the side while you wait."
    show L Happy at left with moveinleft
    "Lisa returns a few moments later with a folded piece of paper in her hands."
    "She offers it to you."
    "You accept the sheet and set it down on the counter, glancing at it occasionally between cutting open the boxes."
    show L Blank at left
    L "There are some really great surgeons nearby, [pcname]. I bet we could find one in your budget that'll do a great job."
    show Keith Angry with dissolve
    BM "Lisa!"
    show chelsea shocked
    "Lisa jumps in surprise as Keith enters from the back. You didn't even hear him leave his office, so his presence catches you both off guard."
    show L Sad at left
    show chelsea blank
    L "Yes, sir?"
    BM "Didn't I tell you to clean out the stock room? And instead I find you out here chatting it up with [pcname]."
    "Lisa bows her head, her cheeks flushed with shame."
    L "I'm so sorry, sir. It won't happen again."
    BM "It better not. I expect you to follow orders, Lisa. I'm very disappointed in your behavior."
    L "Of course, sir. I'm sorry, sir."
    show Keith Blank
    "Keith sends a glance your way, as though finally acknowledging your presence. You stand there awkwardly, unsure of what to do. Keith sighs."
    show Keith Neutral
    BM "We'll talk about it later."
    show Keith Blank
    "Lisa gives a quick nod."
    L "Yes, sir."
    "Keith glances her over, then begins to walk past you both toward his office. He pauses when he sees the paper on the counter."
    show Keith Confused
    BM "What's this?"
    show L Blank at left
    L "Oh, sir, that's..."
    show Keith Blank
    "Keith picks up the paper and looks it over."
    show Keith Neutral
    BM "Cosmetic surgeons? One of you considering surgery?"
    show Keith Blank
    L "I typed it up for [pcname], sir. We've been talking about her getting a boob job recently."
    "Keith gives your body a once-over, his eyes lingering at your breasts."
    show Keith Confused
    BM "Really? You're considering plastic surgery, [pcname]?"
    menu bakery_boobthoughts3:
        "If I had the money I would." if True:
            show chelsea embarrassed
            show Keith Happy
            "Keith nods and gives you an approving look, setting the paper back down on the counter."
            show chelsea blank
            BM "I think that would be a great idea. You know, I admire the effort you've been putting into your looks."
            BM "It's great to see someone your age really care about their appearance. It's a refreshing change."
            if bakeryagree >=10:
                if club == "track":
                    show chelsea happy
                    "You can't help but beam at his compliment. Hearing a compliment from Keith is rare, but you're glad he seems to notice the effort you've put in to embrace your femininity."
                    pcname "Thanks! I'm glad you've noticed."
                elif club == "cheer":
                    show chelsea happy
                    "You smile, pleased that he's noticed your efforts. You toy with a piece of your blonde hair, coy."
                    pcname "Well, I have certain standards to meet, you know, being on the cheer squad. We have to look ready for every occasion."
                    pcname "I aim to always look my best."
                    BM "And you're doing a good job at it."
                elif club == "yearbook":
                    show chelsea embarrassed
                    "You aren't sure you've ever heard a real compliment from Keith before. Your cheeks heat up in embarrassment at the thought."
                    pcname "A-Ah, thank you..."
            elif True:
                if club == "track":
                    show chelsea shocked
                    "You've never heard a compliment from Keith before. Hearing one now feels weird."
                    pcname "Uh, yeah. Thanks."
                elif club == "cheer":
                    "Hearing a compliment from Keith somehow feels strange, and maybe a little creepy. You aren't sure what to make of it."
                    pcname "Uh, right. Thanks."
                elif club == "yearbook":
                    show chelsea shocked
                    "You aren't sure you've ever heard a compliment from Keith before. You can't help but think he's mocking you in some way you don't understand."
                    show chelsea embarrassed
                    pcname "U-Um, thank you..."
            show Keith Neutral
            show L Happy at left
            BM "You know, if you need a loan, I'm sure we could work something out."
            if bakeryagree >= 10:
                BM "I don't mind helping out my more hardworking employees."
            elif True:
                BM "I don't mind helping out my employees, but only as long as they prove they're capable."
            show Keith Blank
            "Keith gives the paper a final glance before heading back into his office."
            hide Keith Blank with moveoutleft
        "I'm not really interested." if True:
            show Keith Blank
            "Keith frowns, giving your breasts a quick glance. He shakes his head in disappointment."
            if bakeryagree >= 10:
                show chelsea sad
                "You glance down at your chest with a frown. Are they really that small?"
            elif True:
                show chelsea sad
                "You pull the edges of your blouse a little tighter over your cleavage, uncomfortable under his gaze."
            show Keith Neutral
            BM "That's a real shame, [pcname]. I think you'd look great with a fresh set."
            show Keith Blank
            "He looks over the paper again, his eyes trailing along the set of reviews."
            show Keith Confused
            BM "On a budget? You know, if money is what's holding you back, I could consider giving you a loan."
            show Keith Neutral
            BM "Would hate to see Lisa's hard work go to waste."
            show Keith Blank
            "Keith sets the paper back down on the counter and disappears into his office."
            hide Keith Blank with moveoutleft
    show L Blank at left
    show chelsea blank
    "Lisa approaches the counter, reading over her long list of locations and reviews."
    show L Happy at left
    L "That was very kind of Keith to offer a loan for this. Not a lot of bosses would do that."
    show chelsea shocked
    pcname "I can't think of any that would."
    show L Blank at left
    show chelsea blank
    "You collect the boxes off of the ground, holding them awkwardly in your arms as you carry them out to the dumpster in the back."
    "When you return, Lisa is still mulling over the paper."
    "You lean on the counter beside her and look the sheet over. It looks like she put a lot of work into this."
    L "What if we just set you up for a consultation?"
    L "You wouldn't be pressured to go through with it or anything, but at least you'd know more about it."
    L "What do you think?"
    menu bakery_consultsuggestion:
        "Accept." if True:
            if club == "track":
                "Getting a boob job is a big step you never thought you'd take in your life, but you've found that you've begun to love the new you."
                "Lisa's advice thus far has really helped you find strength in a part of yourself that you didn't know existed. It wouldn't hurt to at least look into what she's suggesting."
                pcname "Yeah, I'll go. No harm in hearing what it's all about."
            elif club == "cheer":
                "A boob job is a huge change, but as you struggle to fit in with your younger peers, you feel that making a more adult change might be the right thing for you."
                "After all, you're not a kid anymore, and you'd like to embrace that change sooner rather than later."
                pcname "That sounds good to me, Lisa. I wouldn't mind hearing more about it."
            elif club == "yearbook":
                show chelsea sad
                "You're terrified at the prospect of cosmetic surgery, but Lisa has been right so far, and you {i}do{/i} feel more confident after all of the changes she's encouraged you to make."
                "Plus she put so much work into her research for you..."
                pcname "I-I guess I could, um, go to a consultation... I-if you think it would be best..."
            show L Happy at left
            show chelsea blank
            L "Wonderful! You won't need to worry about a thing. I'll set up the appointment and keep you updated."
            L "I'll be there for you every step of the way, [pcname]."
            show chelsea happy
            "You smile, a little relieved to have her on your side."
            show L Sad at left
            L "I better clean the stock room before Keith goes in there again."
            hide L Sad with moveoutleft
            show chelsea blank
            "Lisa turns, disappearing into the back. You wait until she's done cleaning before you bring her the extra stock supplies and carry on with the rest of your shift."
            $ bakeryagree +=1
            $ bakeryconsultagree = True
            show bg black with dissolve
            hide chelsea with dissolve
            jump events_end_period
        "Refuse." if True:
            if club == "track":
                "Lisa has done a lot to help you embrace your femininity, and while you appreciate her efforts, you can't bring yourself to seriously take the next step and commit to cosmetic surgery."
                pcname "I think I'm going to have to pass. A boob job is a bit much."
            elif club == "cheer":
                "While you appreciate the sentiment, the idea of actually going to a consultation with a real cosmetic surgeon feels a little rushed."
                "Even if you're older than your peers, you're still in high school. You can't imagine any of the other cheerleaders on your squad going through such a serious procedure."
                pcname "That sounds nice and all, but I'm not ready for that sort of thing."
            elif club == "yearbook":
                "While you appreciate everything Lisa has done to help you become more confident in yourself, you can't imagine taking such an expensive, permanent step."
                show chelsea sad
                "The idea of going under the knife terrifies you, almost as much as all the stares you'll receive on your breasts afterward!"
                pcname "I-I don't think I-I'm ready for that. I'm sorry..."
            show L Disappoint at left
            "Lisa sighs, tapping her nails across the review sheet."
            show chelsea blank
            if bakeryagree >= 10:
                show L Happy at left
                L "Why don't you take the sheet home with you and look it over some? Consider it a little while longer."
                L "You might change your mind if you think about it a little more."
            elif True:
                show L Question at left
                L "It's only a consultation, [pcname]. It's not like they're going to hold you down and force you to get them."
                show L Happy at left
                L "Take the sheet home and look it over. You might change your mind."
            hide L Happy with moveoutleft
            "Lisa walks to the back without another word, holing herself up in the stock room."
            "Feeling awkward, you wait a while before you start to bring her the excess supplies and resume the rest of your shift."
            $ bakeryagree -=1
            show bg black with dissolve
            hide chelsea with dissolve
            jump events_end_period

label bakery_consultationsetup:
    show chelsea happy at right with moveinright
    show L Happy at left with moveinleft
    pcname "Enjoy the rest of your day!"
    L "Please come again!"
    "You and Lisa hold up your fake smiles until the last customer in the bakery leaves, ducking out into the storm outside."
    show chelsea blank
    show L Blank at left
    "The rain has brought spurts of customers searching for shelter from the storm, but mostly it's warded everyone from leaving their own homes."
    show chelsea sad
    "You can't blame them: you'd rather be curled up in a blanket on your couch right now."
    show chelsea blank
    "It had only started drizzling when your shift started, but now it's pouring down with no signs of letting up."
    "Luckily, you still have another two hours before the end of your shift. Hopefully the rain clears up by then."
    "Both of your smiles drop once the store is empty."
    L "Do you mind if I run to the bathroom for a minute?"
    show chelsea happy
    pcname "Yeah, sure."
    show L Happy at left
    L "Thanks."
    show L Blank at left
    hide L Blank with moveoutleft
    "Lisa ducks into the back, leaving you alone in the store. The lights flicker overhead, followed by a loud clap of thunder."
    show powerout with fade
    show chelsea shocked
    "Everything powers down at once. The lights, the registers, and the coolers turn off, leaving you surrounded in darkness."
    show chelsea blank
    BM "Damn it!"
    "You hear Keith yell from inside of his office."
    "You look around the bakery for a flashlight or a candle, something to keep you from standing there in the dark."
    show chelsea sad
    "You fumble around the counters but it's hard to see anything. With a sigh, you knock on Keith's office door."
    show chelsea blank
    BM "Come in."
    hide chelsea with dissolve
    show bg BakeryOffice with dissolve
    "You step into his office, trying to peer around the dark room. It's even harder to look around than the front of the shop. It gives you the creeps."
    show chelsea at right with moveinright
    pcname "Keith, do you know where the flashlights are?"
    show chelsea shocked
    show Keith Blank with dissolve
    hide powerout
    "As soon as you say it, the lights flicker on, flooding the office and bakery with light. Machines whir loudly as they try to reboot their systems."
    show chelsea blank
    "Keith leans back against his chair, his arms propped behind his head. He glares at his computer in frustration."
    show Keith Confused
    BM "Shouldn't you know that already? What the hell did I train you for?"
    if bakeryagree >= 10:
        show chelsea sad
        "You know for a fact that he didn't train you, but you bite the remark down."
        pcname "I forgot. Could you show me?"
    elif True:
        pcname "You didn't train me."
        show Keith Angry
        BM "The fuck I didn't."
    show chelsea blank
    show Keith Blank
    "Keith hoists himself out of his chair and strides to the front of the bakery. He opens a drawer underneath the register and pulls out a flashlight, dropping it into your hand."
    show bg Bakery with dissolve
    BM "Remember that next time."
    pcname "Okay."
    "You set the flashlight aside in case of another power outage."
    "Keith leans against the counter, looking out over the empty bakery."
    show Keith Angry
    BM "Damn storm. Business is always bad in the rain."
    show Keith Blank
    "He picks up the waste sheet and scribbles something down before picking up a bagel from the display case. He takes a large bite."
    show Keith Neutral
    BM "Haven't had a chance to check up on you recently. You're still in school, right [pcname]? How's that going?"
    show Keith Blank
    if intelligence >= 40:
        show chelsea happy
        pcname "I've been doing really well, actually. I have some of the highest grades in my class."
        "You beam, proud of your academic accomplishments. Keith rolls his eyes and takes another bite out of his bagel."
        show Keith Neutral
        BM "Brains are useful some of the time, [pcname], but they aren't gonna getcha anywhere if you don't have the looks to go with it."
        show Keith Blank
        show chelsea confused
        pcname "What do you mean?"
        show Keith Neutral
        show chelsea blank
        BM "I mean that you should focus more on your appearance and how you come across to others instead of what you 'know'."
        BM "A lot of dumbasses succeed in higher positions 'cause they look good and get noticed."
    elif intelligence >= 30:
        "You shrug. Your grades are nothing to brag about, but it's not like you're failing."
        pcname "It's not bad. Things are pretty average."
        "Keith nods, taking another bite out of his bagel."
        show Keith Neutral
        BM "You know, [pcname], nothin' wrong with being average. Hell, there's nothing wrong with being {i}below{/i} average. When it comes to book smarts, that is."
        show Keith Blank
        show chelsea confused
        pcname "What do you mean?"
        show Keith Neutral
        BM "I mean that you should focus more on your appearance and how you come across to others instead of what you 'know'."
        BM "A lot of dumbasses succeed in higher positions 'cause they look good and get noticed."
    elif intelligence >= 20:
        show chelsea sad
        pcname "It's... okay. It's hard to balance life and school at once."
        "You look away, trying not to let it bother you. School hasn't been your top priority as of late and your grades show it."
        show Keith Neutral
        BM "Not so great, huh?"
        show Keith Laugh
        "Keith lets out a laugh, taking another bite of his bagel."
        show Keith Smirk
        BM "You should really consider that boob job then, [pcname]."
        show Keith Neutral
        BM "With brains like that, you're gonna need it."
    elif True:
        show chelsea sad
        pcname "It's... going."
        "You don't want to admit that you're failing classes, but it's clear Keith got the hint."
        show Keith Confused
        BM "That bad? Shit, [pcname]."
        show Keith Laugh
        "Keith laughs, taking another bite of his bagel."
        show Keith Happy
        BM "You better get that boob job, then."
        show Keith Smirk
        BM "With brains like that, you're gonna need all the help you can get."
    show Keith Blank
    show chelsea blank
    "Keith glances at the register as it finishes booting up. He mumbles something about his computer being back up and retreats to his office."
    hide Keith Blank with dissolve
    "After a few more minutes, Lisa emerges from the back."
    show L Happy at left with moveinleft
    L "Thanks for watching the register."
    show chelsea happy
    pcname "Yeah, no problem."
    show chelsea shocked
    show L Blank at left
    "Another loud clap of thunder causes both of you to jump. You and Lisa laugh a little and stare out at the storm."
    show chelsea blank
    "After a long moment of silence, Lisa gasps."
    show L Happy at left
    L "Oh! I almost forgot."
    "She pulls out her phone and redirects to her e-mail. She looks over one of her e-mails with satisfaction."
    L "I set up an appointment for the consultation. It'll be Saturday at eleven in the morning."
    if bakeryconsultagree == False:
        if club == "track":
            show chelsea angry
            pcname "Wait, I never agreed to go! You can't just book things without asking me first!"
        elif club == "cheer":
            show chelsea angry
            pcname "Hold on, Lisa. I told you I wasn't going. You can't just book this without talking to me first."
        elif club == "yearbook":
            show chelsea confused
            pcname "W-Wait! I-I said no! You... You can't just..."
        show L Blank at left
        L "I know, I know, but you really won't know how it is until you go to it!"
        L "I promise, I'll stop bringing it up if you come."
        show L Sad at left
        L "Please, [pcname]?"
    menu bakery_schoolconflict:
        "I have club at that time..." if True:
            show L Question at left
            L "It's only high school, [pcname]. Skipping one club meeting isn't going to hurt."
            L "Besides, this is almost the same thing as a doctor's appointment."
            if bakeryconsultagree == True:
                "You consider her words, mulling them over in your head."
                "It really {i}would{/i} be the same thing as a doctor's appointment, if you think about it. And schools don't mind if you skip clubs to go to {i}those{/i}."
                "Plus, you had already agreed to go to the consultation. It would be rude to back out now."
                show chelsea happy
                pcname "Well, I guess I can miss club for this."
                show L Happy at left
                "Lisa beams."
            elif True:
                show chelsea confused
                pcname "I don't know, Lisa..."
                show L Sad at left
                L "I promise, if you go to this, I'll stop harassing you about it."
                L "Just come to the consultation and see."
                show chelsea blank
                "You bite your lip, hesitating. You really want to tell her no, but you have a feeling she'll find another way to get you to go."
                pcname "I... Okay."
                show L Happy at left
                "Lisa beams. A part of you regrets going along with it."
            L "Perfect! I'll pick you up first thing in the morning."
            L "Make sure to set an alarm!"
            "Lisa tucks her phone away and walks off to clean up an incoming puddle of water forming under the door to the bakery."
            if bakeryconsultagree == True:
                show chelsea happy
                "You smile and get back to work."
                "Skipping club this once won't hurt, and you're a little excited to see what the consultation is all about."
            elif True:
                show chelsea blank
                "You sigh and bury your face in your hands. You just want this consultation to be over and done with already."
            $ bakeryagree -=1
            jump events_end_period
        "Sure, I can go." if True:
            show chelsea happy
            show L Happy at left
            L "Perfect! I'll pick you up first thing in the morning."
            L "Make sure to set an alarm!"
            "Lisa tucks her phone away and walks off to clean up an incoming puddle of water forming under the door to the bakery."
            "You take out your own phone and set up a reminder. Maybe it won't be so bad to see what it's all about."
            "Who knows? Maybe you'll even like it."
            $ bakeryconsultagree2 = True
            $ bakeryagree += 1
            jump events_end_period

label bakery_consultation:
    $ LHappy = "Characters/Lisa/Casual/Happy.png"
    $ LBlank = "Characters/Lisa/Casual/Blank.png"
    $ LQuestion = "Characters/Lisa/Casual/Questioning.png"
    $ LDisappoint = "Characters/Lisa/Casual/Disappointed.png"
    $ LSad = "Characters/Lisa/Casual/Sad.png"
    show chelsea blank
    $ clothes = 'naked'
    show chelsea at right with dissolve
    "Your alarm goes off first thing in the morning, startling you awake. You groggily reach out of your blanket to turn it off."
    "As you glance at your phone, you see that it's 10:00. Lisa should already be on her way to pick you up for your consultation."
    hide chelsea with moveoutright
    pcname "Guess I better get ready..."
    show chelsea blank
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "You rummage through your wardrobe quickly and get changed. By the time you've finished brushing your teeth and applying makeup, you hear Lisa's car horn beep outside."
    hide chelsea
    show bg black with dissolve
    pause 0.3
    show bg CityD with dissolve
    show chelsea at right with moveinright
    "You hurry to meet her outside. Pop music plays on the radio as you climb into the passenger seat of her car."
    show L Happy at left with dissolve
    L "Hey, [pcname]! Ready to go?"
    if bakeryconsultagree == True:
        show chelsea happy
        pcname "Yep! All set."
    elif True:
        pcname "I guess..."
    L "Great! Let's get going then."
    show L Blank at left
    "Lisa drives off, humming along to a tune on the radio."
    "You stare out the window and watch the buildings grow closer and taller as Lisa drives further downtown."
    "You can't help but feel a little nervous as she pulls into the parking lot of a large white building."
    "Plain signs direct patients to different parts of the building. You see one with a large arrow beside the words 'COSMETIC SURGERY & LASER CENTER'."
    "Lisa parks close to the entrance and reaches for her purse in the backseat of her car. A few magazines pop out."
    show L Happy at left
    L "Ready?"
    if bakeryconsultagree == True:
        show chelsea embarrassed
        "You give her a nervous smile."
        pcname "Yep!"
    elif True:
        show chelsea sad
        "You don't bother hiding your discomfort as you glance toward the building."
        pcname "Uh, sure..."
    show chelsea blank
    show L Blank at left
    "You climb out of the car and follow Lisa into the building."
    show bg surgery with dissolve
    "The lobby is surprisingly nicer than a normal doctor's office. Everything has a modern luxurious feel to it."
    "While the setup is the same, the chairs are more plush and brick and wood make up the check-in desk."
    "As you take it all in, Lisa places a hand on your shoulder."
    hide L Blank with moveoutleft
    L "I'm going to check you in. Find a seat and relax."
    pcname "Okay."
    "You find an empty pair of seats and glance around the room. The modern artwork on the walls are accompanied by framed posters of smiling women and slogans such as 'ENHANCE YOUR CONFIDENCE' and 'LOOK YOUR BEST'."
    "Several women sit around the room, flipping through magazines and brochures. Many of them are attractive and talk openly to each other, clearly having been through the process before, while clear newcomers nervously keep to themselves."
    show L Blank at left with moveinleft
    "Lisa returns to your side and offers you a clipboard with a blank sheet of medical information. A brochure sits on top."
    L "You'll need to fill this out, but I picked this up at the front desk. I thought reading through it might calm you down."
    show chelsea embarrassed
    "You offer a weak smile. You must look as nervous as the other newcomers."
    pcname "Thanks."
    show chelsea blank
    "You quickly fill out the medical sheet. Lisa takes it once you're done and drops it off at the check-in desk before returning to her seat beside you."
    "You flip through the brochure, admiring the models' beautiful faces and plump breasts. They all look beautiful, happy, and confident."
    "You pause at a fold labeled 'FACTS' at the top and read through."
    "The brochure lists ideal candidates for the procedure, what to expect, the risks, and the typical lifespan of the breast augmentation."
    "Beside the 'FACTS' fold, another fold labeled 'OPTIONS' goes further in depth on the different type of implants you can get, what sort of effect they will have on the appearance of your breasts, their lifespan, and side effects."
    "Lisa peers over your shoulder, glancing over the 'OPTIONS' fold."
    show L Happy at left
    L "You won't have to worry about these."
    "She points to the description of the silicone implants."
    show L Blank at left
    L "You're too young for them. You'll have to get the saline ones."
    L "But if you would prefer silicone, you can always switch to them once the saline ones need replaced."
    show chelsea confused
    pcname "Isn't this a lot of money for something that's going to need to be replaced every few years?"
    L "Maintaining your appearance costs money. It's all worth it, in my opinion."
    show L Happy at left
    L "Besides, the saline ones last around eight to ten years. You'll get a {i}lot{/i} of use out of them before they need replaced."
    show chelsea blank
    show L Blank at left
    L "Have you looked at the different shapes yet?"
    "You glance down at the brochure. You didn't even know there were different shapes, but looking it over now you see how the positions of the inserts create different shapes of the breasts."
    L "I would recommend the round ones. They're the most popular for a reason. They look the best!"
    "Cosmetic Patient" "Are you getting a breast implant, too?"
    show GCGirl with dissolve
    "You and Lisa both glance to the side. An attractive young woman sits beside you, a brochure in hand. She smiles warmly."
    show L Happy at left
    L "[pcname] here is thinking about it. We're about to go into her consultation."
    "Cosmetic Patient" "How exciting! I'm about to go into mine as well."
    "Cosmetic Patient" "Is this your first time here?"
    pcname "Yeah."
    "Cosmetic Patient" "Welcome! I'm sort of a regular. I had my nose done last time. Isn't it cute?"
    "She wrinkles her nose a little. It's cute as a button."
    "Cosmetic Patient" "Now I just need a little adjustment to my boobs and I'll get the look I want."
    "Cosmetic Patient" "I can't decide how big I want to go. I guess that's what the consultation is for, right?"
    "She lets out a little laugh. She seems so at ease here, you can't help but smile along with her."
    show L Blank at left
    "Cosmetic Patient" "How about you? Do you know how big you're going?"
    if club == "track":
        pcname "No idea. I'm not even sure if I'm going through with it."
        "Cosmetic Patient" "Really? I think you'd look really good with a new set!"
        "Cosmetic Patient" "But, you know, to each their own."
    elif club == "cheer":
        show chelsea embarrassed
        pcname "Not yet. This is a lot more complicated than I thought it would be."
        "She laughs."
        "Cosmetic Patient" "Yeah, there are a lot of options. It can be confusing sometimes."
        "Cosmetic Patient" "I've always found that I feel better once I go through with it, though."
    elif club == "yearbook":
        show chelsea sad
        pcname "I-I'm not sure...If I'm going to..."
        "Cosmetic Patient" "Really? You know, I always feel better about myself after surgery."
        "Cosmetic Patient" "It's nice to feel as good as you look."
        show chelsea embarrassed
        "She gives you a little wink. You blush, glancing down at your breasts."
    show chelsea shocked
    "Surgeon" "[pcname]?"
    show chelsea blank
    "You glance up toward one of the doors to the rest of the medical facility. A middle-aged man in a lab coat smiles and waves you forward."
    show chelsea happy
    "Cosmetic Patient" "Ah, guess it's time! Have fun!"
    hide GCGirl with dissolve
    show chelsea blank
    "She gives you a little wave as you and Lisa join your surgeon. You smile, a little more at ease as you follow the surgeon to his office."
    if bakeryconsultagree == True:
        show chelsea happy
        "You can't help but feel a little better about your decision to go to the consultation. Maybe going through with this would be a good thing?"
    elif True:
        show chelsea sad
        "You can't help but wonder if getting breast implants might be a good thing?"
    show chelsea blank
    show DW Happy with dissolve
    "Surgeon" "Please, have a seat."
    show DW Blank
    "You and Lisa both take a seat in the plush blue chairs across from his desk. Several posters and infographics hang on the walls, each displaying confident testimonials and basic information on cosmetic procedures."
    "Your surgeon offers you and Lisa a handshake before he takes a seat across from you and adjusts the small round glasses on his face."
    show DW Neutral
    "Surgeon" "It's a pleasure to meet you both. I'm Dr. White, one of the surgeons at this facility."
    show L Happy at left
    show DW Blank
    L "The pleasure is all ours, Dr. White."
    show L Blank at left
    show DW Confused
    "Dr. White" "I hear you're interested in breast augmentation, correct?"
    show DW Blank
    pcname "Yes."
    show DW Happy
    "Dr. White" "Excellent. Now, let's go over your medical history a bit and get these basics out of the way."
    show DW Blank
    "You review your medical history, drug allergies, and other conditions with Dr. White. He looks over the clipboard you filled out in the lobby and types away on his computer, securing all of the information."
    "As he approaches the subject of your family medical history, you falter."
    "While you remember some of it from previous doctor visits, there are many that leave you stumped."
    show DW Confused
    "Dr. White" "Any history of heart attack or heart conditions in your family?"
    pcname "Um..."
    show DW Blank
    "You try to recall any mention from your parents before their passing, but nothing comes to mind."
    pcname "I'm not sure..."
    show DW Neutral
    "Dr. White" "Alright. Substance abuse?"
    show DW Blank
    pcname "Ah..."
    pcname "I'm not sure about that either..."
    "You bite your lip. There aren't going to be many questions you can answer without the aid of your parents."
    "You take a deep breath."
    show chelsea sad
    if club == "track":
        pcname "Look, I'm sorry. I don't know a lot about my medical history."
        show DW Shocked
        pcname "My parents died in a car crash recently. All that information kind of left with them..."
        "Your chest swells at the thought. You hadn't considered it before, but there's a lot you don't know about your family."
        "Now you'll never get to find out."
    elif club == "cheer":
        pcname "I'm sorry."
        pcname "My parents..."
        show DW Shocked
        pcname "They recently died in a car crash. I don't know much about my family medical history."
        "Your chest tightens in pain at the memory. There's still so much you don't know, and now you'll never have the chance to find out."
    elif club == "yearbook":
        pcname "S-Sorry..."
        pcname "M-My parents, they... They passed away..."
        show DW Shocked
        pcname "There was a car crash and..."
        "You feel your throat catch. You can't manage to choke out the rest of your words, but it appears you don't need to. Dr. White understands."
    show DW Neutral
    "Dr. White" "I'm sorry to hear that, [pcname]. I offer you my deepest condolences."
    "Dr. White" "My parents are no longer with me as well. I can understand the difficulty you're going through."
    "Dr. White" "Allow us to move on."
    show DW Blank
    "Dr. White scrolls a little on his computer, his eyes trailing toward another section to fill out."
    "Dr. White" "And your relationship to... I'm sorry, what is your name, dear?"
    show L Happy at left
    L "Lisa."
    show chelsea shocked
    "Lisa hooks an arm around yours, surprising you. She pulls you close against her side."
    L "We're best friends. We're practically family, even. She's like a little sister to me."
    "You feel your chest swell at her words. You try to find something to say, but you're stunned into silence."
    show chelsea blank
    "You had no idea that Lisa felt that way about you. Her confession touches you deeper than you could have imagined."
    show chelsea happy
    "Tears prick at the corner of your eyes, but you blink them back, unable to contain the smile on your face."
    "Dr. White notices the emotional impact Lisa's words have on you, but thankfully decides not to embarrass you by pointing it out."
    "Instead, he moves on."
    show DW Neutral
    "Dr. White" "Alright. And what are you looking to have done exactly? What are your goals?"
    show chelsea blank
    show DW Blank
    pcname "Uh..."
    "It takes a moment for you to focus back on why you're here. You hadn't even thought of any goals for your breasts. You didn't even know you were supposed to have any."
    "You look to Lisa, a little lost. She picks up on your confusion and opens up the brochure in your hands, pointing out the options you had read over."
    L "We were looking these options over together in the lobby. We were thinking that a round set would be best. Since she's too young for silicone, we'd have to go with the saline inserts."
    "Dr. White looks to you for confirmation. You nod along."
    show DW Confused
    "Dr. White" "And what size were you thinking of going to?"
    "This time Lisa looks to you, waiting for an answer."
    show DW Blank
    if club == "track":
        show chelsea confused
        pcname "Honestly, I have no clue."
    elif club == "cheer":
        pcname "I'm not sure. I don't really know what will look good on me."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "I-I'm not... not sure..."
    show DW Neutral
    "Dr. White" "I see. Well, I suppose we can move on to your current measurements and I can make some recommendations if you'd like?"
    show L Happy at left
    show DW Blank
    L "I think that would be best."
    show L Blank at left
    show DW Neutral
    "Dr. White" "Alright. [pcname], if you would kindly remove your shirt and bra and have a seat on my stool over here."
    show DW Blank
    "Dr. White grabs a tall stool from the corner of the room and drags it to the center."
    if club == "track":
        show L Question at left
        "You give Lisa a skeptical look. She nods for you to undress."
        show L Happy at left
        L "He has to check your breasts somehow, [pcname]."
        show chelsea blank
        "With a sigh, you yank your shirt over your head and unclasp your bra. You feel your nipples stiffen at the cold, air-conditioned room."
        "You climb up onto the stool, uncomfortable under their gazes."
    elif club == "cheer":
        show chelsea shocked
        "You blink in surprise. Of course, it makes sense that he would need to examine your breasts, but the thought of undressing had never occurred to you."
        show chelsea blank
        "You pull your shirt over your head and unclasp your bra. You feel your nipples stiffen at the cold, air-conditioned room."
        "You climb up onto the stool easily and relax against the seat."
    elif club == "yearbook":
        show chelsea embarrassed
        "A flush sweeps over your face and you look to Lisa for help, clutching the edges of your shirt."
        show L Question at left
        L "What are you waiting for?"
        pcname "I-I..."
        show DW Happy
        "Dr. White" "There's nothing to be nervous about. It's a simple examination."
        show DW Neutral
        "Dr. White" "If you're uncomfortable, I can bring in a female assistant? Or, if it's your friend's presence bothering you, we can escort her outside."
        show DW Blank
        pcname "N-No... I-I'm okay..."
        show L Blank at left
        "You hesitantly pull your shirt up over your head and unclasp your bra. Your nipples stiffen at the cold, air-conditioned room."
        "You stare at the ground, your face burning with embarrassment as you climb on top of the stool."
    "Dr. White adjusts his glasses again, pulls on a set of latex gloves, and grabs a spool of measuring tape from his desk."
    "He approaches you and begins to measure the different aspects of your breasts, jotting notes down on his clipboard."
    if club == "track":
        "You tap your fingers against the edge of the stool, trying to ignore the feel of your surgeon's fingers brushing against your breasts and the cold tape measurer over your nipples."
        "Your nipples tighten as he cups your left breast to measure its side. You can't help but feel annoyed by your body's obvious reaction."
    elif club == "cheer":
        "You watch Dr. White as he measures and takes notes, all too aware of the feel of his gloved fingers against your breasts and the cold tape measurer pressing against your nipples."
        "Your nipples tighten as he cups your left breast to measure its side. This is in no way a sexual situation, but you can't help your body's reaction."
    elif club == "yearbook":
        "You bite your lip as his gloved fingers brush against your breasts, the cold tape measurer pressing against your nipples."
        "Your nipples tighten as he cups your left breast to measure its side. You can't help but feel embarrassed by your body's sensitive reaction."
    show DW Neutral
    "Dr. White" "Well, at a first glance, you have these perfect nipples, but they're a little large for your current breast size. I would recommend going up to at least a D-cup to help balance them out."
    show DW Blank
    "He cups your right breast and measures it thoroughly."
    show DW Neutral
    "Dr. White" "Additionally, your left breast is smaller than your right, but augmentation will fix that easily."
    show DW Confused
    "Dr. White" "You see here?"
    show DW Blank
    "He lightly taps the skin above your nipples."
    show chelsea confused
    show DW Neutral
    "Dr. White" "The tissue here lays flat, creating a sort of slope down to your nipples. We'll be able to fix this so your breasts look perkier and more full."
    show DW Blank
    "You watch, confused, as Dr. White returns to his desk and pulls out a camera. A white stick-on label lists the hospital name on the side."
    show DW Neutral
    "Dr. White" "I'm going to take some photos now. They're only for review for the surgery, nothing more. They won't go outside of his hospital."
    show DW Blank
    show chelsea blank
    if club == "track":
        "You understand why he would need photographs, but you still feel a little uncomfortable with it. You glance at Lisa and she nods encouragingly."
        pcname "Okay, I guess."
    elif club == "cheer":
        "You sit up a little straighter, trying your best to give him a clear view of your breasts."
        pcname "Of course."
    elif club == "yearbook":
        show chelsea embarrassed
        "You shrink a little in your seat, your face bright red. His explanation makes sense, but still..."
        "You look to Lisa for help. She nods in encouragement."
        pcname "U-Um, o-okay..."
    "Dr. White circles you, snapping away photographs of your bare breasts."
    "After a few moments, Dr. White pulls away, sets the camera down, and removes his gloves."
    show DW Happy
    "Dr. White" "You're good to get dressed now, [pcname]."
    show DW Blank
    if club == "track":
        "With a sigh of relief, you hop off of the stool and pull your bra and shirt back on."
    elif club == "cheer":
        "You slip off of the stool, taking your time to put your bra and shirt back on. Now that you've adjusted to the cold of the office, your clothes feel too warm."
    elif club == "yearbook":
        "You scurry off of the stool and hurry to put on your bra and shirt. You're relieved to no longer be under his scrutiny."
    "Your surgeon resumes his seat behind his desk, attaching the camera to his computer via USB cord."
    show chelsea blank
    show DW Happy
    "Dr. White" "Alright. Thank you for your patience with that, [pcname]. I know a lot of people get embarrassed, but I assure you, this is all necessary to make sure everything turns out perfectly."
    show DW Neutral
    "Dr. White" "Now, the procedure itself will take about two to three hours, plus about an hour or two for recovery time. You'll undergo anesthesia for the duration of it, so you won't remember a thing."
    "Dr. White" "We'll prescribe you some pain medication, but you'll start feeling normal after a couple of days."
    "Dr. White" "I would just recommend limiting the amount of heavy lifting and exercise you do for a few weeks after."
    show DW Blank
    pcname "But at work-"
    show L Happy at left
    L "Keith will understand. He isn't going to make you do hard work while you're recovering."
    show L Blank at left
    show DW Neutral
    "Dr. White" "Now that's all said and done, how about we set up a date for the surgery?"
    show DW Blank
    show chelsea blank
    "Lisa looks at you intently, waiting for your answer."
    if mattsubmissive == True:
        if defymatt == True:
            "You hate that the first thing to come to mind is what Matt would think of this sort of change."
            "He certainly didn't approve this change, but would he? Would this upset or please him? Would he leak those photos if you went through with it, or would he like the change?"
            "You aren't sure, but you do know it frustrates you to no end that his opinion has even factored into this decision."
        elif True:
            "The first thing to come to mind is what Matt might think if he saw you with a new set of boobs. Is this the sort of thing he would approve of?"
    elif True:
        "You can't help but wonder what others at school might think of you should you commit to a change like this. Would they be jealous and aroused like Lisa suggests, or would they be silently judging you?"
    show DW Confused
    "Dr. White" "Well? [pcname]?"
    menu bakery_boobjobsetup:
        "Ready!" if True:
            show chelsea happy
            if club == "track":
                pcname "Yeah, that sounds great."
            elif club == "cheer":
                pcname "Yeah. How soon can we make it?"
            elif club == "yearbook":
                pcname "I... Y-Yes, please."
                show L Happy at left
            "Out of the corner of your eye you see Lisa visibly relax, a bright, excited smile on her face."
            "Dr. White scrolls a bit on his computer, pulling up a new program."
            show DW Neutral
            "Dr. White" "Since you're in such good health, I have an availability next Saturday if that would work for you? Does 11:00am work for you again?"
            show DW Blank
            pcname "Yeah, that'll be fine."
            show DW Happy
            "Dr. White" "Excellent. I'll send this over now and you'll be able to pick up notes on our consultation as well as view the appointment for next week at the front desk."
            show DW Neutral
            "Dr. White" "The receptionist will also have an ASPS booklet for you to go over leading up to the surgery."
            show DW Happy
            "Dr. White" "It was lovely to meet both of you."
            show chelsea blank
            show L Blank at left
            hide DW Happy with dissolve
            "You shake hands again, Dr. White sends a few files over on the computer, and you and Lisa exit back into the lobby."
            "After signing out and picking up your papers, Lisa hooks her arm around yours and beams, leading you out of the building."
            show L Happy at left
            L "You better get ready, [pcname]! All of your little school friends are going to be {i}so{/i} jealous!"
            show chelsea laugh
            "You both laugh and climb into Lisa's car. She drives back to your house and drops you off with a promise to take you to your surgery next week."
            scene bg black with dissolve
            "When she leaves, you realize you're still clutching the brochure in your hands. You smile and tuck it into your back pocket before heading inside."
            $ bakeryboobjobapprove = True
            $ acts-= 1
            $ bakeryagree +=1
            $ LHappy = "Characters/Lisa/Uniform 2/Happy.png"
            $ LBlank = "Characters/Lisa/Uniform 2/Blank.png"
            $ LQuestion = "Characters/Lisa/Uniform 2/Questioning.png"
            $ LDisappoint = "Characters/Lisa/Uniform 2/Disappointed.png"
            $ LSad = "Characters/Lisa/Uniform 2/Sad.png"
            jump events_end_period
        "I changed my mind." if True:
            show chelsea sad
            "You shake your head. You just can't go through with it."
            if club == "track":
                "Sorry for wasting your time, Dr. White, but I don't think this is for me."
            elif club == "cheer":
                pcname "I'm sorry. I can't go through with it."
            elif club == "yearbook":
                pcname "I-I'm sorry. I can't!"
            show L Disappoint at left
            "Lisa's face falls."
            L "[pcname]-"
            show DW Neutral
            "Dr. White" "That's quite fine. I understand. Cosmetic surgery isn't for everyone."
            show DW Happy
            "Dr. White" "If you ever change your mind, feel free to call. I'd be happy to schedule an appointment."
            hide DW Happy with dissolve
            "You nod and stand up quickly from your chair, nearly toppling it backwards. You hurry out of the room and into the hallway, desperate to get out there."
            show L Blank at left
            L "[pcname], wait!"
            "Lisa catches up to you in the hall and grabs your elbow. You stop in place."
            show L Sad at left
            L "Just give it another thought, [pcname]. You saw all those girls in the lobby, didn't you?"
            L "They were so hot! Don't you want to look like them?"
            menu _boobjobsetup2:
                "Stay firm." if True:
                    show chelsea blank
                    "You gently pull your elbow out of her grasp."
                    pcname "I don't want to look like those other girls, Lisa. I want to look like me."
                    show L Disappoint at left
                    if bakeryagree >= 10:
                        "You want Lisa to be understanding. You want her to be the friend you've made along the way, to nod in understanding and accept your decision."
                        "It hurts when, instead, she huffs and rolls her eyes, pushing past you toward the front lobby."
                        "You follow feebly behind, unsure of what to say. She's the one that got her hopes up, but did you lead her on? You aren't sure."
                    elif True:
                        "You aren't surprised when Lisa's demeanor drops into frustration. She rolls her eyes at you and pushes past, storming toward the front lobby."
                        "You follow behind, resolving to keep up the uncomfortable game of cold shoulder. She's the one that got her hopes up, anyway."
                    scene bg black with dissolve
                    "Lisa says nothing to you as you climb into her car, during the drive back, or when she drops you off at home. As soon as you close the car door, she's off, leaving you behind."
                    $ bakeryagree -=1
                    $ acts-= 1
                    $ LHappy = "Characters/Lisa/Uniform 2/Happy.png"
                    $ LBlank = "Characters/Lisa/Uniform 2/Blank.png"
                    $ LQuestion = "Characters/Lisa/Uniform 2/Questioning.png"
                    $ LDisappoint = "Characters/Lisa/Uniform 2/Disappointed.png"
                    $ LSad = "Characters/Lisa/Uniform 2/Sad.png"
                    jump events_end_period
                "Give in." if True:
                    show chelsea blank
                    "You open your mouth to object, then close it. You aren't sure {i}what{/i} it is you want."
                    show L Blank at left
                    "You think back to the beautiful women in the lobby, to the woman that talked to you before her own consultation."
                    "She was so happy and excited to get her own boob job. Don't you want to feel that way, too?"
                    pcname "I... I do."
                    show L Happy at left
                    L "I thought so. Then you should get in there and schedule for surgery."
                    L "I know it's scary, but I'm with you every step of the way. Okay?"
                    L "You aren't alone."
                    show chelsea happy
                    "Lisa takes your hand and gives it a squeeze. You take a deep breath, drawing in comfort from her touch."
                    "Lisa has been a wonderful friend to you since you've started working. She's helped you so much and simply wants to see you grow into a more confident, happier person."
                    "Tossing aside your worries about others' opinions, you follow Lisa back into Dr. White's office."
                    "He looks up from his computer in surprise."
                    show DW Confused with dissolve
                    "Dr. White" "I wasn't expecting to see you back so soon."
                    show L Blank at left
                    show chelsea blank
                    show DW Blank
                    L "She just had some nerves."
                    "You nod in agreement."
                    pcname "I want to go through with it."
                    show DW Confused
                    "Dr. White" "And you're sure about this? I'm not forcing you. I want to make sure you're absolutely, positively 100 percent sure of your decision."
                    "You take a deep breath. You aren't 100 percent sure, but 90 is close enough, right?"
                    pcname "I am. I'd like to schedule for the surgery."
                    show DW Neutral
                    "Dr. White" "Well, alright then."
                    show DW Blank
                    "Dr. White scrolls a bit on his computer, pulling up a new program."
                    show DW Neutral
                    "Dr. White" "Since you're in such good health, I have an availability next Saturday if that would work for you? Does 11:00am work for you again?"
                    pcname "Yeah, that'll be fine."
                    show DW Happy
                    "Dr. White" "Excellent. I'll send this over now and you'll be able to pick up notes on our consultation as well as view the appointment for next week at the front desk."
                    show DW Neutral
                    "Dr. White" "The receptionist will also have an ASPS booklet for you to go over leading up to the surgery."
                    show DW Happy
                    "Dr. White" "It was lovely to meet both of you."
                    show chelsea happy
                    "You shake hands again, Dr. White sends a few files over on the computer, and you and Lisa exit back into the lobby."
                    hide DW Happy with dissolve
                    show L Happy at left
                    "After signing out and picking up your papers, Lisa hooks her arm around yours and beams, leading you out of the building."
                    L "You better get ready, [pcname]! All of your little school friends are going to be {i}so{/i} jealous!"
                    "You smile, trying to ignore the nervous flap of butterflies in your stomach as you climb back into Lisa's car."
                    "She won't stop talking about plans to go shopping for new clothes after the surgery. She keeps up this conversation the entire way home."
                    scene bg black with dissolve
                    "When she drops you off, she promises to pick you up again next week for your surgery. With a thanks and a wave, she drives off."
                    "You look down and realize you're still clutching the brochure in your hands. Hopefully you've made the right decision."
                    $ bakeryboobjobapprove = True
                    $ bakeryagree +=1
                    $ acts-= 1
                    $ LHappy = "Characters/Lisa/Uniform 2/Happy.png"
                    $ LBlank = "Characters/Lisa/Uniform 2/Blank.png"
                    $ LQuestion = "Characters/Lisa/Uniform 2/Questioning.png"
                    $ LDisappoint = "Characters/Lisa/Uniform 2/Disappointed.png"
                    $ LSad = "Characters/Lisa/Uniform 2/Sad.png"
                    jump events_end_period

label bakery_consultationresult:
    show chelsea happy at right with moveinright
    "Your shift goes by steadily. You smile and wave at customers as you ring them up and help wrap baked goods."
    show L Blank at left with moveinleft
    "As the evening begins to settle in and business slows down, you catch Lisa staring at your bosom from behind the display case."
    show chelsea confused
    pcname "...Do I have something on me?"
    "You examine your uniform, checking for any stray frosting or cookie crumbs."
    if bakeryboobjobapprove == True:
        show L Happy at left
        "Lisa laughs and shakes her head."
        L "I'm just thinking of how you would look with your new rack."
        L "We might even need to get you a new uniform. Your boobs might really pop out of this shirt."
        show chelsea blank
        if club == "track":
            "You glance down at your cleavage."
            if bakerystuffing == True:
                "Your breasts are already pretty well defined since you've started stuffing your bra. How much bigger can they get?"
            elif True:
                "Your breasts look lost inside of your shirt uniform. Maybe popping out would be better than how flat you currently look."
            pcname "I guess I won't complain."
            "Lisa laughs."
        elif club == "cheer":
            "You peer at your reflection in the display case, imagining yourself with more voluptuous breasts."
            if bakerystuffing == True:
                show chelsea happy
                "Lisa might be right. Your boobs already fill out the new uniform pretty well since you've stuffed them, but the shirt is going to be {i}really{/i} tight with a boob job."
            elif True:
                "You hold out the shirt a little bit, trying to imagine your boobs filling up the empty space. It seems a little exaggerated that they'll pop out, but it's not {i}impossible{/i}."
            "You smile a little to yourself. You wouldn't {i}hate{/i} showing off your body properly in your tight uniform."
            pcname "They'll really look good, won't they?"
            L "Of course! You're going to look {i}so{/i} sexy."
        elif club == "yearbook":
            show chelsea embarrassed
            "You blush, glancing down at your cleavage."
            if bakerystuffing == True:
                "Your breasts are already pretty noticeable since you've begun stuffing your bra for work. Would a boob job really make them that much bigger?"
            elif True:
                "Your breasts hardly fit in your uniform as it is. While it would be nice to fill the outfit out properly, you can't help but feel a little embarrassed thinking about the attention you will get."
            pcname "D-Do you really think it'll... be that noticeable?"
            "Lisa giggles."
            L "Well, yeah. That's the point."
    elif True:
        show L Disappoint at left
        "Lisa rolls her eyes and shakes her head."
        show chelsea blank
        L "I'm just thinking of this weekend."
        show L Question at left
        L "It was a complete waste of my time."
        if bakeryconsultagree or bakeryconsultagree2 == True:
            if club == "track":
                pcname "They would've gotten in the way of my club. You know how hard it is to exercise with big boobs?"
                pcname "Besides. It's my body, my decision."
                show L Happy at left
                L "You're right. It's your decision to look like a boy for the rest of your life."
                show L Blank at left
                "You grit your teeth, prepared to bark back a snide remark, but the sound of Keith's office door opening stops you."
            elif club == "cheer":
                "You avoid her gaze and instead focus on cleaning a few crumbs off of the counter."
                pcname "I never said for sure I would go through with it."
                pcname "It was just, like, fun to think about."
                show L Disappoint at left
                L "That sounds like a child's excuse."
                "Lisa sighs."
                show L Blank at left
                L "I guess you just aren't as mature as I thought you were."
                "Her words sting. You bite your lip and look away."
            elif club == "yearbook":
                show chelsea embarrassed
                "You stare at your feet, guilty and ashamed."
                pcname "I... I'm happy with how... how I look..."
                show L Disappoint at left
                L "You sure? Cause you don't sound so confident about that."
                "You flinch. Her sharp tone cuts right through you."
        elif True:
            if club == "track":
                show chelsea angry
                pcname "I told you I didn't want to go from the start."
                pcname "It's your own fault for getting your hopes up."
                show L Question at left
                L "I was trying to {i}help{/i} you."
                show L Disappoint at left
                L "You clearly need it."
                show chelsea confused
                pcname "What's that supposed to mean?"
                show L Blank at left
                L "Just look at you. Without me, you would have been running around looking like a boy."
                show L Question at left
                L "No date would {i}ever{/i} take you seriously looking like that."
                show L Happy at left
                L "But who am I kidding? I doubt they ever will."
                show L Blank at left
                show chelsea blank
                "You grit your teeth but bite your tongue. You want to snap back at her, but the sound of Keith's office door opening catches your attention. He won't be happy if you cause a scene in the middle of the store."
            elif club == "cheer":
                show chelsea blank
                pcname "Well, that makes two of us."
                pcname "I didn't want to go in the first place."
                show L Disappoint at left
                L "Maybe if you had thought about it seriously in the first place, you wouldn't have wasted my time."
                L "But I guess I can't expect much more from a stubborn child."
                show chelsea angry
                "Her remark stings. You bite your tongue and look away, holding in a harsh response."
            elif club == "yearbook":
                show chelsea sad
                "You can't find the courage to meet her gaze. You stare at the floor instead, pretending to find the tiles interesting."
                pcname "I- I didn't ask you to make the appointment..."
                show L Question at left
                L "Like you would have done it yourself?"
                show L Disappoint at left
                L "You always need someone else to do something for you. You can't even look me in the eye while we're talking."
                L "Pathetic."
                "You flinch, hurt by her harsh tone."
    show chelsea blank
    show L Blank at left
    show Keith Blank with dissolve
    "Keith steps out of his office and glances around the bakery. It's currently empty."
    "He looks between you and Lisa, taking a moment to stretch his muscles after a long session of sitting."
    show Keith Confused
    BM "Am I interrupting something here?"
    if bakeryboobjobapprove == True:
        show L Happy at left
        "Lisa beams, shaking her head."
        L "No, sir. Not at all."
    elif True:
        show L Disappoint at left
        "Lisa gives him a sour look, sparing a glance in your direction."
        L "No, not at all."
    show L Blank at left
    L "We were just talking about [pcname]'s consultation."
    show Keith Happy
    BM "Oh! You go to that already?"
    "You nod."
    show Keith Neutral
    BM "Well, what's the final verdict?"
    show Keith Blank
    if bakeryboobjobapprove == True:
        show L Happy at left
        "Lisa throws an arm over your shoulders, squeezing you against her side with a broad smile."
        show chelsea happy
        "Her excitement is contagious. You can't help but grin as well."
        L "She's scheduled for surgery on Saturday!"
        show Keith Happy
        BM "Really? That's great, [pcname]."
        BM "I'm glad. It's nice to see you taking the initiative."
        "Keith reaches into his back pocket and pulls out his wallet. He fumbles through a few flaps before pulling out a shiny black card."
        "He passes it to Lisa."
        BM "Just have them charge it to that."
        show chelsea shocked
        if club == "track":
            pcname "Are you sure this is okay? I don't have the money to pay that back."
        elif club == "cheer":
            pcname "And this is really okay with you, Keith? I don't have the money for something like this on my own, but..."
        elif club == "yearbook":
            pcname "B-But... I don't know how I can pay you back..."
        show chelsea blank
        "Keith waves his hand as though brushing your worries aside."
        BM "We'll worry about that later. Right now just focus on getting through that surgery."
        show chelsea happy
        pcname "Thank you, Keith."
        BM "Yeah, yeah. Don't thank me yet. Get it done first, then we'll talk."
        BM "Just make sure your surgeon does a good job. I'm expecting my money to be well spent."
        show Keith Laugh
        "He laughs a little and heads back into his office."
        show Keith Happy
        "Lisa happily pockets his credit card, tucking it into her bra."
        L "Looks like that's all settled!"
        L "God, [pcname], you're going to look so hot."
        "She giggles."
        L "You might even make me jealous."
        "Lisa gives you an eager smile before picking up a broom to sweep behind the counter."
        "You smile a little to yourself and clean up the crumbs on the countertop."
        scene bg black with dissolve
        "Everyone at work has been so supportive. You can't help but be excited yourself."
        $ bakeryagree +=1
        jump events_end_period
    elif True:
        show L Disappoint at left
        "Lisa looks to you, her hand pressed firmly on her hip. They both wait patiently for your answer."
        show L Blank at left
        if club == "track":
            pcname "I'm not doing it."
            "You look Keith in the eye, challenging and firm. You dare him to try to fight with you on this."
        elif club == "cheer":
            "You sigh, already fed up with Lisa's dramatics regarding your decision. You don't feel like putting up with Keith's reaction either."
            pcname "I decided against it. It isn't right for me."
        elif club == "yearbook":
            show chelsea sad
            "You feel like a rock is slowly sinking to the pit of your stomach. You feel incredibly self-conscious under their scrutiny."
            pcname "I... I can't... go through with it..."
            "You squeeze your eyes shut, afraid to face either of them."
        "Keith is quiet for a moment, registering your response."
        "Then he goes off."
        show Keith Angry
        BM "What the fuck do you mean you're not going through with it?"
        show chelsea shocked
        if intelligence <= 20:
            show chelsea sad
            BM "You're a fucking dumbass! How the hell do you expect to get anywhere like this?! You dumb, ugly bitch!"
            BM "You're not even smart enough to take help when you goddamn need it!"
        BM "Look at that uniform! You look like a goddamn toddler playing dress-up!"
        BM "How the fuck am I supposed to run a business when one of my employees is running around looking like she belongs in pre-school?!"
        BM "That shirt looks like a fucking tent on you!"
        if bakerystuffing == True:
            show chelsea sad
            pcname "But I tried to fix it! I-"
            BM "You think throwing a few plastic molds in your bra is going to fix this?!"
        show chelsea sad
        BM "You should've gone through with the damn boob job, [pcname]. You need all the fucking help you can get!"
        show L Disappoint at left
        "On instinct, you look to Lisa for help. She glares at you, shaking her head in disappointment."
        "For once, you truly feel alone."
        BM "Lisa! Office! {i}Now!{/i}"
        if club == "track":
            "Angry tears prick your eyes as Keith storms into his office, slamming the door shut loudly behind him."
        elif club == "cheer":
            "Tears sting your eyes as Keith storms into his office, slamming the door shut loudly behind him."
        elif club == "yearbook":
            "Tears well up your eyes as Keith storms into his office, slamming the door shut loudly behind him."
        hide Keith angry with moveoutleft
        "Lisa scoffs, muttering something under her breath before joining him inside."
        hide L Disappoint with moveoutleft
        "A surge of panic runs through you."
        pcname "Is he going to fire me over this...?"
        menu bakery_eavesdrop_postconsult:
            "Continue Working." if True:
                if club == "track":
                    "You take in a shaky breath and go to the back. You feel antsy. You need to move. Now."
                    "You can't go for a run or do most exercises at work, especially in this uniform, but you need to do something."
                    "Grabbing some of the cleaning supplies, you scrub away at the grime that's collected on the back walls near the ovens."
                    "The consistent arm movements help you feel a little more active and take the anxiety off of your shoulders."
                    "Not to mention Keith will be pleased to see how clean the back room is."
                    "When you've exhausted yourself of cleaning, you return to the register and keep an eye out for customers. You feel a little less tense, at least."
                elif club == "cheer":
                    "You take in a deep, shaky breath and pull out your compact mirror to adjust your makeup."
                    "If they want to fire you, you won't give them the satisfaction of seeing you cry."
                    "You take up the position behind the register and put on a pleasant smile, awaiting the next customer."
                elif club == "yearbook":
                    "Unable to hold it in any longer, you dip behind the counter and weep quietly into your knees, smearing the makeup over your skirt."
                    "You feel humiliated, but nothing can be as demeaning as how Keith treated you."
                    "Once you've cried all you can, you wash up in the back and return to your position behind the register. Even after sobbing your eyes out, though, your stomach twists with anxiety."
                show L Blank at left with moveinleft
                "Lisa exits Keith's office a little while later, her apron wrinkled and dirty."
                if bakery_eavesdrop == True:
                    "You notice the slight off-color stains on the edges of her shirt collar and suddenly understand why Keith wanted Lisa in his office."
                elif True:
                    "You wait for Keith to call you in and fire you, but Lisa shuts the door behind her and resumes working without a word."
                "The rest of your shift goes by in a tense fog of silence. You're relieved when you finally get to clock out and leave."
                jump events_end_period
            "Eavesdrop." if True:
                scene bg black with dissolve
                "You hesitate outside of Keith's door, your heart hammering in your chest. There's no way you can continue to afford living on your own if they decide to fire you."
                "Maybe if you can listen in, you can come up with a better reasoning as to why they should keep you."
                "You reach for the door knob and open the door slightly enough for you to peek in."
                show bg KL1 with dissolve
                "You're shocked to find Keith's hand tangled in Lisa's hair, yanking her down onto her knees in front of the desk. Lisa whimpers but allows him to push her around. Her gaze remains locked on the floor, ashamed."
                BM "You're fucking {i}useless{/i}. You know that?"
                show bg KL2 with dissolve
                if bakery_eavesdrop == True:
                    "You feel a sense of deja vu hit you as Keith unbuttons his pants and presses his half-hard cock to her lips."
                elif True:
                    "You have to hold in an audible gasp as Keith unbuttons his pants and presses his half-hard cock to her lips."
                    if club == "track":
                        "You stare at them, stunned."
                        pcname "Is he really going to...?"
                    elif club == "cheer":
                        "Your jaw drops a little. It's like a dumpster fire: you can't look away."
                        pcname "Oh... my God."
                    elif club == "yearbook":
                        "You feel the heat rush to your face as you realize what's happening."
                        pcname "W-What...?"
                show bg KL3 with dissolve
                "Lisa opens her mouth to take him in, but Keith yanks her hair back. She lets out a small cry."
                BM "Does it look like I'm ready for that yet?!"
                show bg KL4 with dissolve
                "Lisa shakes her head quickly. She sticks her tongue out, creating slow strokes along his erection."
                "Keith loosens his tight grip on her hair, spreading his fingers over her scalp. He scowls down at her."
                BM "Is her stupidity infectious? Huh? Did you catch it, too, you fucking idiot?"
                BM "You're a goddamn failure. You aren't even worth {i}this.{/i}"
                "He thrusts against her face, smacking his hardening cock against her chin. Lisa bends with his movements, running her tongue against his length."
                BM "How fucking hard is it to befriend that brat? Huh? How hard is it to make her go through with a simple {i}boob job?!{/i}"
                "...Boob job?"
                BM "There's no fucking point in keeping her now! My fucking boss won't look twice at her with those flat tits, and I sure as hell don't want to!"
                "His boss?"
                "Doesn't Keith own the bakery? What other business is he a part of?"
                "You feel your hand slip from the doorknob as the reality of the situation hits you."
                "Is this all you were to them? Some pretty-looking girl they could manipulate for their own desires?"
                "Is that why Lisa went out of her way to try to befriend you? Because she was told to?"
                "You think back to her kind words at the consultation. She said you were like her sister. Was all of that a lie?"
                "Is this why Keith was so mean when you tried to study or express your own opinion?"
                "You internally kick yourself for your stupidity."
                "Of course there was an ulterior motive to all of this."
                "There's no way someone like Keith or Lisa would care about your well-being."
                "Your stomach twists in anxious knots. Keith continues to yell at Lisa as she tries to please him with her tongue."
                menu bakery_continuewatching:
                    "Continue watching." if True:
                        $ corruption +=1
                        pass
                    "Leave." if True:
                        show bg black with dissolve
                        "Unable to take anymore, you shut the door as quietly as you can and take up your position behind the register."
                        show bg Bakery with dissolve
                        show chelsea blank at right with dissolve
                        "You feel sick to your stomach and struggle to put on a pleasant facade for the next few customers that come in."
                        show L Blank at left with moveinleft
                        "Lisa comes out of Keith's office some time later, her apron wrinkled and dirty. You notice small stains around her collar."
                        "She heads into the back without a word, returning with a new apron and shirt."
                        "A part of you wonders how often this happens that she would need an extra uniform on hand."
                        "Neither of you speak to each other for the rest of the shift. Keith doesn't call you in to his office either, so you can only assume your job is safe."
                        "For now, anyway."
                        "You're relieved when evening rolls in and you're able to clock out and leave."
                        jump events_end_period
                "Despite your own anxieties, you can't seem to look away."
                "Something about watching Keith force Lisa to lick his cock pleases you."
                "Could it be because you're hurt and upset at them?"
                "Or could it be something else?"
                if bakery_eavesdrop == True:
                    "You felt this way last time, too..."
                BM "You had one fucking job, and you couldn't even do that right!"
                "Lisa whimpers as Keith pulls back and smacks her lips with his cock."
                L "I... I'm sorry, sir."
                "She focuses on the tip, licking her lips and sucking gently on the skin."
                BM "Sorry? You're sorry?"
                BM "Well, so am I."
                BM "I'm sorry I fucking trusted such a {i}simple{/i} task to a complete {i}dumbass{/i} like you!"
                show bg KL5 with dissolve
                "Keith shoves his cock into her mouth suddenly. Lisa's eyes widen in surprise, but she takes his length down her throat easily."
                BM "You know, he likes dumb girls. Maybe you'll work, huh, Lis?"
                "Lisa whimpers in response."
                "Keith yanks his cock out and shoves it back down her throat forcefully."
                "He repeats this process, his thrusts becoming more frenzied."
                "You feel your panties dampen with arousal. You cross your legs, but this only furthers your desire."
                show bg KL6 with dissolve
                "As Keith fucks Lisa's face, his speech comes out quicker, as though trying to get it all out in one breath."
                BM "That's all you're fucking good for, Lis. Sucking cock and playing dumb."
                BM "And he loves girls that can suck a good cock. Is that what you want, Lis? You want some other guy's dick down your throat?"
                "Lisa shakes her head a little, trying to keep up with his harsh thrusts."
                BM "I can't {i}hear{/i} you!"
                "She whimpers frantically, working harder to take him in her throat as deeply as he'll fit."
                BM "Maybe I'll need to hire another girl. Is that what I should do? Replace your fat ass?"
                "Lisa grips Keith's thighs, her fingers digging into his pants fabric as she sticks her tongue out underneath his cock."
                "She laps her tongue eagerly on the underside of his balls, prodding the sensitive skin."
                BM "Fuck..."
                "Keith's grip on her hair tightens. He presses her face closer to his groin, giving her easier access to his balls."
                "Lisa moans, eager to please him."
                BM "Unless you think you can train her. But how the fuck am I supposed to trust you with that?"
                BM "You couldn't even train this whore!"
                BM "You're fucking stupid! A stupid fucking slut!"
                "You watch as Keith comes close to a climax, his movements quicker and more forceful in her mouth."
                "You shift your weight a little, your thighs rubbing together."
                "You almost want to touch yourself, but resist the urge."
                "You shouldn't be watching this. Despite that, you can't look away. You don't {i}want{/i} to look away."
                "You realize with a flush of embarrassment that {i}knowing{/i} you shouldn't be witnessing this makes it even more exciting."
                "Keith grunts out a few more words before pulling out of Lisa's mouth."
                "His cum splatters over her face, dripping onto her glasses."
                show bg KL7 with dissolve
                "Lisa gasps for air, coughing into her sleeve. She removes her glasses and cleans them up on her apron. It's not an effective method, but there's no longer globs of cum on her glasses anymore."
                show bg black with dissolve
                "Afraid that one of them will turn and see you, you quietly shut the door and resume your position behind the register."
                show bg Bakery with dissolve
                show chelsea embarrassed at right with moveinright
                "You feel your clit throb, begging for attention. You take deep breaths, trying to calm down."
                "But how are you supposed to calm down from {i}that?{/i}"
                show L Blank at left with moveinleft
                "Lisa comes out sometime later, her apron wrinkled and dirty. She takes a moment to step in the back and change into a spare uniform."
                "A part of you wonders how often this must happen for her to have a spare uniform on hand."
                "Neither of you speak to each other for the rest of your shift, but all thoughts of being fired have fled your mind."
                "You're relieved when your shift ends and you can clock out."
                $ corruption +=1
                jump events_end_period

label bakery_surgery:
    $ clothes, hair = casualwear
    $ LHappy = "Characters/Lisa/Casual/Happy.png"
    $ LBlank = "Characters/Lisa/Casual/Blank.png"
    $ LQuestion = "Characters/Lisa/Casual/Questioning.png"
    $ LDisappoint = "Characters/Lisa/Casual/Disappointed.png"
    $ LSad = "Characters/Lisa/Casual/Sad.png"
    show chelsea at right with moveinright
    "Lisa arrives to your apartment late in the morning, beeping her car horn out front to let you know she's there."
    show bg CityD with dissolve
    "You step out of your apartment and join her in the passenger seat."
    show L Happy at left with dissolve
    "Even in the morning, pop music blares on the radio. She has a new frappuccino in the cup holder and a bagel in her hand."
    "Your stomach growls. You haven't been able to eat or drink anything since yesterday afternoon in preparation for the surgery."
    L "Ready?"
    menu bakery_surgerynerves:
        "Yep!" if True:
            show chelsea happy
            L "Great!"
        "I'm feeling kind of nervous..." if True:
            show chelsea sad
            L "That's okay. Everyone feels nervous before surgery. It's totally normal."
            L "You'll feel way better once it's over. I promise."
    show L Blank at left
    show chelsea blank
    "Lisa pulls out from in front of your apartment and starts driving toward downtown."
    "During the drive, you pull out the ASPS booklet you got at the end of your consultation and begin reading it over."
    "There are a lot of rules for prepping for the surgery. You double-check the list, making sure you haven't made any small mistakes that might disrupt the surgery."
    "Lisa pulls into the parking lot of the cosmetic surgery building and parks the car."
    "You both climb out and walk into the lobby."
    show bg surgery with dissolve
    "A receptionist smiles up at you both as you approach the front desk."
    "Receptionist" "Hi there! Checking in?"
    show chelsea happy
    pcname "Yes. I'm [pcname], I have an appointment with Dr. White at 11."
    "The receptionist nods, scrolling through her computer."
    "Receptionist" "Surgery for breast augmentation?"
    show chelsea blank
    pcname "Yeah."
    "She clicks a few tabs on her computer."
    "Receptionist" "And do you have a card we can put on file?"
    show L Happy at left
    L "Yup!"
    "Lisa pulls out her wallet and hands the receptionist Keith's card. The receptionist types the information into the computer before passing the card back."
    "Receptionist" "Excellent! You're all checked in."
    "Receptionist" "Just wait one moment."
    show L Blank at left
    "The receptionist pulls out a filing cabinet drawer under her desk and thumbs through a few files. She pulls out a series of papers and attaches them to a clipboard."
    "Receptionist" "We'll just need you to sign these beforehand. You can turn them back in up here or just hand them to your nurse when you're called in."
    pcname "Thank you."
    "You accept the clipboard and a pen from the receptionist and take a seat in one of the empty chairs. Lisa sits beside you, peering over your shoulder at the papers."
    L "Looks like waivers. Those are pretty standard."
    "You nod, reading over the papers before signing your name at the bottom."
    "Once you've gone through them all, you return the clipboard to the front desk and sit back down."
    "Lisa passes you a fashion magazine from her purse, pulling out a separate one for her to go over while you both wait."
    "Although you try to read the magazine, you struggle to concentrate. At least the pictures are nice."
    "Nurse" "[pcname]?"
    "You look up to see a friendly nurse in the doorway. She waves you forward."
    "You and Lisa collect your things and follow her into a hall, passing several other examination rooms."
    "The nurse leads you into a room near the end of the hall. You take a seat on the edge of the hospital bed while Lisa lounges in one of the nearby chairs."
    "The nurse goes over your basic health information and checks your vitals to make sure everything is ready for surgery."
    "Shortly after the nurse leaves, Dr. White enters."
    show DW Happy with dissolve
    "Dr. White" "Ah, [pcname]. Good to see you again."
    "Dr. White" "Are you excited?"
    menu bakery_surgeryexcitement:
        "I can't wait!" if True:
            show chelsea happy
            show L Happy at left
            "Dr. White" "I'm glad to hear it! It's an exciting time."
        "I'm kind of nervous..." if True:
            show chelsea embarrassed
            "Dr. White nods in understanding."
            show DW Neutral
            "Dr. White" "That's a perfectly normal reaction. Everyone gets nervous before they have to go into surgery."
            show DW Happy
            "Dr. White" "But I can assure you, the process we have here is the {i}safest{/i}. You don't have anything to worry about."
    show chelsea blank
    show L Blank at left
    show DW Neutral
    "Dr. White" "Now, let's just review a few things and then I'll start to mark your breasts for surgery."
    show DW Blank
    "Dr. White turns to an open laptop on a nearby table. He adjusts his glasses, peering over the lens to get a better view."
    show DW Neutral
    "Dr. White" "Alright, it seems you've followed all the steps in the ASPS booklet. That's a good start."
    "Dr. White" "Again, the surgery itself will take from two to three hours. You'll be here in recovery for about an hour, and then you can go home. I'm assuming your friend here is your driver?"
    show DW Blank
    show L Happy at left
    L "Yes, I'll be taking her home."
    show L Blank at left
    show DW Neutral
    "Dr. White" "Good, good."
    "Dr. White" "Now, you'll need some time to recover, so it'll take a couple of weeks before you can return to work."
    "Dr. White" "You can expect some leaking from the incisions, but it'll stop once they're healed. We'll provide a fabric bra for you to wear. Make sure you wear it day and night for about two weeks."
    "Dr. White" "You can take it off to wash, but avoid any bras with wire underlining for a few months."
    "You feel your head begin to spin as Dr. White prattles on. It's a lot of information to hold in at once."
    show DW Blank
    "He looks up from his computer and notices your confusion."
    show DW Happy
    "Dr. White" "Ah, sorry. This is a lot of information to take in."
    show DW Neutral
    "Dr. White" "Don't worry. This will all be written down for you to take home."
    "Dr. White" "Well, let's start marking the breasts. Would you remove your shirt for me?"
    scene bg black with dissolve
    "You nod, stripping from the waist up. Dr. White pulls on a set of gloves and grabs a tape measurer."
    "He takes a clipboard with a list of your previous measurements and refers to it as he measures your breasts again, using a black marker to mark where the adjustments will be made."
    "Once he's finished, Dr. White puts everything away and takes off his gloves."
    show DW Happy with dissolve
    "Dr. White" "Alright, [pcname]. A nurse will be in shortly and we'll get started."
    "Dr. White" "I'll see you soon."
    hide DW Happy with dissolve
    show bg surgery with dissolve
    "Dr. White steps out of the room, leaving you and Lisa alone."
    "You look down at the black markings on your breasts. There has been such a focus on your boobs recently that they almost feel alien to you now."
    "Lisa notices your rapt attention on your breasts and sets her magazine aside."
    show chelsea at right with dissolve
    show L Question at left with dissolve
    L "What're you thinking about, [pcname]?"
    show powerout with dissolve
    "You can't shake the feeling that there's no going back once this is done. Do you really want to go through with this?"
    menu bakery_surgerychoice:
        "Commit to surgery." if True:
            hide powerout with dissolve
            $ corruption += 5
            show chelsea embarrassed
            pcname "I'm... nervous, but excited."
            show L Happy at left
            "Lisa smiles. It fills you with a sense of encouragement."
        "Back out." if True:
            hide powerout with dissolve
            show chelsea sad
            "You continue to stare down at your breasts. An uneasy feeling settles in your stomach as you realize the permanence of your decision."
            if club == "track":
                pcname "I... I change my mind. I can't do this."
            elif club == "cheer":
                pcname "This... I can't do this. No way."
            elif club == "yearbook":
                pcname "I-I changed my mind! I want to go home!"
            "You grab for your shirt and hurriedly yank it on, desperate to get dressed and leave this place."
            "Lisa rushes to your side and grabs your wrists, pulling your hands away from your shirt fabric."
            show L Sad at left
            L "[pcname]. [pcname]! Calm down."
            L "It's just nerves, I promise. You're going to be fine."
            L "You're already so close. Everyone has already put so much time and effort into getting this ready for you. You might as well just go through with it."
            L "Besides, aren't you excited to look super hot?"
            menu bakery_surgerychoice2:
                "Stay" if True:
                    "You bite your lip, thinking it over."
                    "Maybe it really is just nerves. It's a huge change, after all. Everyone has been telling you that your nerves are normal."
                    "And everyone did put a lot of time and effort into this. It would be rude to just walk out..."
                    pcname "I... okay."
                    pcname "Yeah. I'll go through with it."
                    show L Blank at left
                    "Lisa sighs in relief, squeezing your shoulders."
                    show L Happy at left
                    L "See? Just nerves."
                    L "Don't worry. It'll be over before you know it."
                "Go" if True:
                    show L Disappoint at left
                    pcname "No. I don't care anymore. I just want to go home."
                    "Before Lisa can answer, the door opens."
                    "The nurse from before steps into the room. She rolls in a small cart that you assume is carrying the anesthesia."
                    "She notices the panicked expression on your face and pauses."
                    "Nurse" "Is everything okay, honey?"
                    "Before Lisa can open her mouth to argue, you quickly speak up."
                    pcname "I changed my mind. I want to go home. Please."
                    "The nurse nods, a little put off by the change of plans."
                    "Nurse" "Are you sure, honey? It's okay to be a little nervous."
                    show L Question at left
                    "You can tell that Lisa is about to try to agree with the nurse, but you remain resolute."
                    show chelsea blank
                    pcname "No. I want to go home."
                    "Nurse" "Alright. If that's what you would like."
                    "Nurse" "I'll let the doctor know. You can get dressed and pick up your papers at the front desk."
                    "The nurse takes her cart and wheels it back outside, shutting the door behind her."
                    show L Disappoint at left
                    L "I can't believe you."
                    L "You've wasted everyone's time here. And you were going to look so hot, too..."
                    "Lisa plops back down in her chair and flips open her magazine with more force than necessary. She glares down at the pages. You aren't entirely sure she's reading it."
                    "You finish getting dressed and walk back out to the front desk to collect your papers."
                    scene bg black with dissolve
                    "Lisa doesn't speak to you during the walk to her car, during the drive home, or even when she stops in front of your apartment to drop you off."
                    if club == "track":
                        pcname "Thanks for the ride."
                    elif club == "cheer":
                        pcname "Thank you for driving me."
                    elif club == "yearbook":
                        pcname "T-Thank you..."
                    "Lisa clicks open the locks to the car doors without a word. You awkwardly climb out of the car and watch her speed away from your home as soon as the door is shut."
                    "You dread to think of how work will be from now on."
                    $ bakeryagree -=1
                    "End of Bakery Route."
                    $ LHappy = "Characters/Lisa/Uniform 2/Happy.png"
                    $ LBlank = "Characters/Lisa/Uniform 2/Blank.png"
                    $ LQuestion = "Characters/Lisa/Uniform 2/Questioning.png"
                    $ LDisappoint = "Characters/Lisa/Uniform 2/Disappointed.png"
                    $ LSad = "Characters/Lisa/Uniform 2/Sad.png"
                    jump events_end_period
    show L Blank at left
    "You take a moment to practice some deep breathing exercises and relax."
    "You really are happy with your decision to go through with this."
    "You look up as the door opens."
    "The nurse from before steps into the room. She rolls in a small cart that you assume is carrying the anesthesia."
    "She gives you a pleasant smile, stopping the cart beside the bed."
    "Nurse" "Hi, [pcname]. Are we all set?"
    show chelsea sad
    "You look to Lisa for encouragement and give a small nod."
    if club == "track":
        show chelsea happy
        pcname "Ready as I'll ever be."
    elif club == "cheer":
        show chelsea happy
        pcname "Yup. Let's do this."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "R-Ready..."
    "Nurse" "Glad to hear it. Now, just lay back for me."
    show chelsea blank
    "You follow her instructions, reclining into a comfortable position on the bed."
    "Nurse" "I'm going to put this mask over your face and I want you to count back from one-hundred, okay?"
    "Nurse" "You won't feel a thing. By the time you wake up, you won't even realize you left the room."
    "The nurse places a soft mask over your nose and mouth. You begin counting backwards aloud."
    pcname "One-hundred. Ninety-nine. Ninety-eight. Ninety... seven..."
    "As you count, you feel your eyelids grow heavy. Everything in your body feels as though it's pulling you under."
    pcname "Ninety... six... Ninety...fi..."
    "You close your eyes and fall into darkness."
    scene bg black with dissolve
    show chelsea with dissolve
    pause 1.0
    hide chelsea with dissolve
    pause 3.0
    $ implants = True
    show chelsea with dissolve
    "The first thing you're aware of is a heavy weight on your chest."
    "You struggle to open your eyes, blinking in the bright fluorescent lights of your recovery room."
    show bg surgery with dissolve
    show L Happy at left with dissolve
    "Lisa sits next to you, admiring your body."
    show chelsea confused
    L "Oh! [pcname], you're awake!"
    show chelsea shocked
    L "The surgery went by really quickly! I was surprised."
    L "Just wait until everyone gets a load of these!"
    show chelsea laugh
    "She giggles, grinning down at your breasts. You peer down, noticing your swollen bosom. This will take some getting used to."
    show chelsea happy
    "A nurse steps into the room."
    "Nurse" "Oh, good! You're awake."
    "Nurse" "The surgery went well, [pcname]. You just relax and rest here until you feel well enough to move around."
    "Nurse" "If there's anything you need, have your friend here grab one of us and we'll get it for you."
    "The nurse steps back out into the hallway."
    show chelsea blank
    "You spend another hour relaxing in bed before you feel up to walking around."
    "Once you're all set, Dr. White discharges you. Lisa helps grab your papers from the front desk and drives you home."
    "You climb out once you reach your apartment. She winds the window down to talk to you."
    show chelsea happy
    L "If there's anything else you need me to get you, [pcname], just shoot me a text."
    L "I can't wait to see how you look recovered!"
    "She gives you a broad smile and a little wave before driving off."
    hide chelsea with dissolve
    pause 0.5
    hide L Happy with dissolve
    show bg black with dissolve
    $ acts -= 3
    "For the next couple of weeks you focus on recovering. Lisa stops by once in a while to help take care of you and pick up your antibiotics and medicine from the pharmacy."
    "After about two weeks, you start to feel closer to normal and have gotten used to your new breasts."
    "The pain has subsided for the most part and your breasts are settling into their new look."
    if intelligence >= 40:
        "Despite your recovery time, you've made sure to keep up your grades and complete all of the assigned homework you've been given."
        "At times it even felt great to have as a distraction from your recovery."
    elif intelligence >= 30:
        "Although it may be difficult, you've made sure to keep up with your homework as much as you can afford. While it hasn't been your priority, your grades have been okay, so you can't complain."
    elif intelligence >= 20:
        "You haven't had much time to focus on studying, but you've made sure to keep a passing grade at least."
    elif True:
        "With so much focus on your recovery, there's hardly been any time to make up your homework. You've desperately fallen behind and you're not sure how you're going to make it up."
    "You try to push thoughts of school aside as you ready yourself for tomorrow."
    "Tomorrow will be your first time back to work since the surgery."
    "As you spend the night getting your uniform ready, you can't help but feel a little excited and nervous regarding what everyone's reactions will be when they see you with your new breasts for the first time."
    $ bakeryroutelock = True
    $ LHappy = "Characters/Lisa/Uniform 2/Happy.png"
    $ LBlank = "Characters/Lisa/Uniform 2/Blank.png"
    $ LQuestion = "Characters/Lisa/Uniform 2/Questioning.png"
    $ LDisappoint = "Characters/Lisa/Uniform 2/Disappointed.png"
    $ LSad = "Characters/Lisa/Uniform 2/Sad.png"
    jump bed2

label bakery_routelock:
    $ corruption += 10
    show bg Bakery with dissolve
    show chelsea at right with moveinright
    "Walking into work feels surreal after taking so much time off. You change into your uniform in the back and walk out to the front."
    "Keith and Lisa chat behind the counter, as though waiting for you. They both turn as you enter in from the back, their eyes immediately drawn to your chest."
    show Keith Happy with dissolve
    show L Happy at left with dissolve
    BM "Oh, {i}wow{/i}."
    BM "[pcname], you look {i}great!{/i}"
    L "I told you! Doesn't she look amazing?"
    L "[pcname], pose for us!"
    scene bg black with dissolve
    if club == "track":
        show chelsea happy
        show bg BRL1 with dissolve
        "You place your hand on your hip, striking some confident poses."
    elif club == "cheer":
        show chelsea happy
        show bg BRL2 with dissolve
        "You turn, striking some flirtatious poses. You bend over and press your cleavage together, giving them a good view of your new breasts."
    elif club == "yearbook":
        show chelsea embarrassed
        show bg BRL3 with dissolve
        "You shyly turn and make cute poses, trying not to focus on your breasts too much."
    "They can't take their eyes off of you."
    BM "Damn. It's a good look, [pcname]."
    L "I love it. You look {i}so{/i} hot!"
    if club == "track":
        "You can't help but grin, flattered by their encouragement."
    elif club == "cheer":
        "You smile coquettishly and toy with a piece of your hair, reveling in the attention."
    elif club == "yearbook":
        "You blush, embarrassed by their flattery."
    "As they continue to bathe you in compliments, the bell over the front door chimes."
    show bg Bakery with dissolve
    if mattrouteend == True:
        call bakery_conflict2_matt2 from _call_bakery_conflict2_matt2
    show chelsea happy
    hide L Happy with dissolve
    hide Keith Happy with dissolve
    show GCBoy with dissolve
    "A customer steps up to the counter. You hurry behind the register, prepared to take his order."
    pcname "Welcome! What can I get for you today?"
    "The man seems to take a moment to register that you're speaking. His gaze is fixed solidly on your breasts."
    "Customer" "Yeah... Uh... Uh..."
    "Customer" "A bagel."
    pcname "Sure thing!"
    "You step over to one of the baskets on display."
    pcname "Which one would you like?"
    "He's silent for a moment."
    if corruption >= 30:
        "Noticing his distraction, you turn your shoulders a little, giving him a better view of your cleavage."
    pcname "Sir?"
    "Customer" "Right! I'm so sorry."
    "Customer" "Just a cinnamon raisin. Cream cheese too, if it's not too much trouble."
    pcname "Not at all!"
    "You bend over, your breasts squeezing in the open space between your shirt's uniform as you place his bagel in a bag and grab a small container of cream cheese from the fridge."
    "His eyes follow your body's every move."
    "You set the bag down on the counter and step behind the register."
    pcname "That'll be $3.00, please."
    "Customer" "Of course. Thank you so much for getting that for me."
    pcname "It's no trouble! That's what I'm here for."
    "You give him a polite smile. He beams back at you and passes you a twenty."
    "As you start to grab his change, he quickly puts a hand over yours."
    "Customer" "Don't worry about it. That's for you."
    show chelsea shocked
    "You blink in surprise, then smile widely."
    show chelsea happy
    pcname "Thank you so much, sir! That's very kind of you."
    $ Cash += 17
    "Customer" "No, no, it's no trouble at all. No trouble for a sweet thing like you."
    "Customer" "You're gorgeous, sweetie. You should really think about getting into modelling."
    if club == "track":
        show chelsea laugh
        "You laugh. The idea sounds absolutely ridiculous, but you appreciate his intentions."
        pcname "Thanks. I don't know if I could be that graceful, though."
        "Customer" "Oh, I have no doubt you can."
    elif club == "cheer":
        "You bite your lip and smile, leaning a little on the counter. Your breasts rest on the edge in clear view."
        pcname "Thank you, sir. That's so sweet of you to say."
        "Customer" "It's the truth, sweetie. Really."
    elif club == "yearbook":
        show chelsea embarrassed
        "Your face brightens with a blush. You smile nervously, trying to hide behind your hair."
        pcname "T-Thank you, but I don't know about that..."
        "Customer" "I mean it, sweetie. You would knock half those girls out of the park."
    "Before you have a chance to respond, he gives your body another once-over and takes his bagel, leaving the store."
    show L Happy at left with moveinleft
    "Lisa steps up beside you, a small smirk on her lips."
    L "You better get used to guys saying things like that more often."
    "You look down at the extra money in your hand and smile. You could get used to more attention like this."
    scene bg black with dissolve
    pause 0.5
    "Bakery Route Locked In."
    "You've reached the end of the Bakery Route in this version! Thank you for playing, keep and eye out for more content every month!"
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
