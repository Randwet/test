label kate_puppies:
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "You take a stroll around town, taking in the fresh air and sunny skies."
    "It's a beautiful weekend and you're happy just to walk around a while."
    show chelsea happy
    "You walk past the park, smiling fondly at the memory of your picnic with Kate."
    if club == "track":
        "It was a great first date, despite the sugar situation."
    elif club == "cheer":
        "It was a beautiful day then too. And so was Kate."
    elif club == "yearbook":
        "Though you're still embarrassed about those sandwiches, Kate was so sweet about it..."
    "The smile lingers for several blocks. When you think of Kate, you really can't help it."
    if damienrelate == "dating":
        show chelsea blank
        "Your smile dims a little when you think of Damien."
        "You're not sure how you let this happen - or why you've let it get so far."
        "They're both {i}amazing{/i} people. You'd be lucky to have either of them."
        "But trying to have both... Your stomach sinks with the weight of your dread."
        "You'll have to hurt one of them eventually, won't you?"
        "You shake your head and force those thoughts away."
    if violetrelate == "Dom":
        show chelsea sad
        "Violet would be {i}furious{/i} if she knew you were hiding this from her."
        "You shiver at the thought of what she'd do to you as punishment..."
        "And if Kate knew about you and Violet...?"
        "You shake your head and force those thoughts away."
    elif violetrelate == "Sub":
        show chelsea blank
        "Your smile dims at the thought of Violet."
        "Kate would never be into something like that, would she?"
        "And Violet... She's doing her best to be a good sub, but she would be {i}furious{/i} if she knew about Kate..."
        "You shake your head and force those thoughts away."
    if defymatt == True:
        show chelsea blank
        "Your chest constricts painfully at the thought of Matt."
        "If he knew about Kate, who knows what {i}twisted{/i} things he would do..."
        "Would he try to use you to get to her too?"
        "Would she still like you if she knew the things he's made you do?"
        "You shake your head and force those thoughts away."
    elif mattsubmissive == True:
        show chelsea sad
        "Your chest constricts painfully at the thought of Matt."
        "What would he do to you if he found out? What would he do to {i}Kate{/i}?"
        "You don't know why, but there's something about the way Matt treats you that you {i}need{/i}."
        "A voice inside of you that tells you that's what you deserve."
        "When you're with Kate, you can almost tune the voice out. Her smile drives it away."
        "But the minute she's gone..."
        "You shake your head and force those thoughts away."
    show chelsea shocked
    "You're startled to realize that you're already several blocks away from the park."
    "Lost in your own thoughts, you hadn't been paying attention to where you were going."
    show chelsea confused
    "This isn't an area you're familiar with - you don't recognize the buildings or street signs."
    "As you try to get your bearings, someone steps out of the store behind you and you hear... barking?"
    show chelsea blank
    "Turning toward the sound, you find yourself face-to-face with five dogs of various breeds."
    "Their tails wag happily as they watch you through the glass window, bringing a smile to your face."
    "Looking up at the building, you see the name \"Heaven Dog Sanctuary\"."
    if club == "track":
        show chelsea happy
        pcname "Must be a rescue!"
        "Your smile widens as you look down at the dogs."
        "They probably came from awful homes, but they're still so happy to see people."
        pcname "We don't deserve dogs..."
    elif club == "cheer":
        pcname "A {i}rescue{/i}...?"
        "You scrunch your nose a little. The dogs are cute, but they probably came from bad homes."
        "It's not their fault, but you couldn't imagine dealing with all those problems."
        "They're really cute though..."
    elif club == "yearbook":
        show chelsea happy
        pcname "Oh, a rescue?"
        "You smile down at the dogs. Their tails are wagging so fast."
    if catadopt == True:
        pcname "[kittenname] probably wouldn't like it if I got a dog, but..."
    pcname "I bet Kate would love to see them."
    show chelsea blank
    "There's a restaurant next door. You could ask her to meet you there and surprise her..."
    menu kate_puppies_invite:
        "Text her." if True:
            call screen TextingScene("Kate",
            [
                TextMessage("Hey", sender = False),
                TextMessage("Wanna get lunch?", sender = False),
                TextMessage("Sure!!!"),
                TextMessage("When do you want to go?"),
                TextMessage("And where?"),
                TextMessage("Now? I'll send you the address", sender = False),
                TextMessage("Okay! I'll be right there!")
            ])
        "Maybe some other time." if True:
            show chelsea confused

            "You don't really know where you are, let alone how long it would take Kate to get here."

            show chelsea happy

            "Since you know the name of the rescue now, it'll be better to come back again some other time."
            "Plugging your address into your phone's GPS, you start walking toward more familiar streets."

            jump events_end_period

    hide chelsea with dissolve
    show bg black with dissolve
    "Twenty minutes pass while you wait in front of the restaurant. You start to wonder if you gave her the wrong address."
    show bg CityD with dissolve
    show chelsea at right with dissolve
    "Or maybe she got lost. She can be pretty ditzy sometimes."
    show chelsea confused
    pcname "Maybe I should text her...?"
    show chelsea shocked
    K "[pcname]!"
    show K Casual Laugh at left with moveinleft
    "Turning toward her voice, you see Kate jumping and waving from the next block over."
    show chelsea happy
    "Smiling, you wave back."
    show K Casual Laugh at right with move
    "She practically runs to you, crushing you against her in her excitement."
    K "I'm so glad you invited me out for lunch!"
    show K Casual Happy at midright with move
    "Releasing you, she looks up at the building behind you."
    show K Casual Blank
    K "Is this where we're going? Have you ever been here before?"
    K "It looks like Italian. Do they have stromboli?"
    show chelsea blank
    K "Oooh! Do you think they have cannolis? They're italian, right?"
    show K Casual Happy
    K "I tried some the other day and they were really good!"
    show chelsea laugh
    "You laugh; you can't get a word in anyway."
    show K Casual Blank
    K "Oh, sorry... I'm not letting you answer at all, am I? I'm just so happy to see you..."
    show chelsea happy
    show K Casual Happy
    "Smiling down at her, you pat her head."
    pcname "It's okay. I'm happy to see you too."
    pcname "I've never eaten here, so I'm not sure what they have. But..."
    show K Casual Blank
    if club == "track":
        "You shrug."
        pcname "We're not actually going out to eat."
    elif club == "cheer":
        "You lean in, as if sharing a secret."
        pcname "I actually have a different surprise for you."
        pcname "We're not eating here."
    elif club == "yearbook":
        show chelsea blank
        "Suddenly nervous, you look away."
        pcname "Actually, I... We're not eating here."
    K "We're not?"
    if club == "track":
        pcname "I needed an excuse to get you here so that I could show you something else."
    elif club == "cheer":
        pcname "Nope."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "No, I... Here..."
    show chelsea laugh
    pause 1.0
    show bg black
    hide chelsea
    hide K Casual Blank
    with dissolve
    "Taking her hand, you lead her toward the rescue."
    show bg CityD with dissolve
    show chelsea at right with moveinright
    show K Casual Blank at left with moveinleft
    pcname "{i}This{/i} is what I wanted you to see."
    show K Casual Laugh at left
    "Kate squeals with delight, dragging you closer to the window."
    "The dogs jump happily, wagging their tails even faster."
    show K Casual Blank at left
    K "Do you think they'll let us pet them?"
    show chelsea laugh
    pcname "Only one way to find out."
    show K Casual Happy at left
    "As soon as you open the door, Kate darts inside, squealing again."
    show chelsea happy
    K "[pcname], look at them!"
    "Inside, half the room is sectioned off for customers, while the other half is a gated play area for the dogs."
    "Her speech quickly turns to baby talk as she melts to the floor in front of them."
    show K Casual Laugh at left
    K "Wook at all the wittle puppies."
    "You look around for someone to talk to; an employee, a girl close to your age, hurries out from the back."
    hide chelsea with moveoutright
    hide K Casual Laugh with moveoutleft
    "Leaving Kate for a moment, you approach the girl."
    show chelsea at right with moveinright
    "Volunteer" "Were you looking to adopt?"
    pcname "We can't, sorry. But they were so cute and we were hoping we could play with them a bit?"
    show chelsea happy
    "Volunteer" "Of course! All the dogs in the play area are very friendly and they would love the extra attention."
    "Volunteer" "Just enter the gate over there and wait for me, okay?"
    show K Casual Happy at left with moveinleft
    "Returning to Kate, you tap her shoulder."
    pcname "Kate, do you want to meet them?"
    show K Casual Laugh at left
    K "Yes!"
    show K Casual Happy at left
    "She jumps to her feet and follows you to the gate."
    "You both step inside to the small pen and close the gate behind you."
    "The dogs crowd around the volunteer, excited by the prospect of meeting someone new."
    "Volunteer" "Alright, the door is shut?"
    K "Yep!"
    "Volunteer" "Awesome. Right this way then."
    "She swings the door to the play area open and two dogs dash into the pen with you."
    "Volunteer" "Dash, Gary, come!"
    "The dogs ignore her, bouncing around your feet."
    "Volunteer" "Just step into the play area and they'll follow. That's why we have the double-gated setup."
    "You and Kate step into the play area and are immediately swarmed by seven or eight happy dogs."
    "Kate sinks to her knees, trying to pet all of them at once."
    hide K Casual Happy with dissolve
    hide chelsea with dissolve
    show bg KateDogs with dissolve
    K "Awen't you just the cutest wittle things?"
    "She babbles to them in baby-talk, while they take turns licking her hands and face."
    menu kate_puppies_join:
        "Join her." if True:
            show chelsea laugh
            if catadopt == True:
                "You know [kittenname] won't like it if you come home smelling like a bunch of dogs, but they're too cute to resist!"
                "Laughing, you join Kate on the floor."
            elif True:
                "You can't resist those wagging tails. Laughing, you join her on the floor."
            pcname "Look how happy you are!"
            "The dogs crowd around you both, eager for attention."
            "After a lot of petting, they start to calm down."
            show chelsea happy
            "You and Kate spend over an hour playing with the dogs."
        "Just watch." if True:
            if catadopt == True:
                "They're cute, but [kittenname] would never forgive you if you came home smelling like dogs!"
            show chelsea laugh
            "You watch Kate's face, content to see how much {i}she{/i} is enjoying the dogs."
            "For a while, they crowd around her, vying for her attention. Eventually, though, they calm down enough to play games like fetch and tug-of-war."
            show chelsea happy
            "Kate spends over an hour playing with the dogs, occasionally smiling up at you."
    "Eventually, a family walks in with two children. As they talk to the volunteer, Kate stands up."
    show bg CityD with dissolve
    show chelsea at right with moveinright
    show K Casual Happy at left with moveinleft
    K "I hope they take one home..."
    show K Casual Blank at left
    K "We should probably get out of the way, though. I wouldn't want to discourage them from adopting one because we're playing with it."
    "Nodding, you follow Kate out into the gated area. Closing the first gate behind you, you open the second one and step out into the entryway."
    show K Casual Laugh at left
    show chelsea laugh
    "Little Boy" "Look at {i}that{/i} one! He has a fluffy tail!"
    "Little Girl" "I like the one with the floppy ears!"
    "Little Boy" "Can we get two, mom? Please?"
    show K Casual Happy at left
    show chelsea happy
    "Waving to the volunteer, you follow Kate outside."
    K "I really hope they do get two..."
    "She smiles wistfully, her eyes shining in the bright sunlight."
    K "Oh, look how silly I am!"
    "Smiling, you pull her in and hold her close."
    show K Casual Blank at left
    K "Oh..."
    "She nestles her face against your neck, hugging you tightly."
    "You stand that way a while, holding onto each other. Finally, she loosens her grip."
    show chelsea blank
    show K Casual Sad at left
    K "Sorry, I get a little sad sometimes."
    "She steps back, wiping a stray tear from her cheek."
    show chelsea sad
    if club == "track":
        pcname "Sorry, maybe it was a bad idea..."
    elif club == "cheer":
        pcname "I didn't mean to upset you, Kate."
    elif club == "yearbook":
        pcname "I understand. I shouldn't have..."
    show K Casual Laugh at left
    show chelsea blank
    K "No! It's okay! I had a lot of fun and they were {i}so{/i} cute!"
    show K Casual Happy at left
    K "I'm really glad you surprised me with puppies, [pcname]."
    show chelsea shocked
    "Rising up on her tip-toes, she brushes her lips over yours in a soft kiss."
    show chelsea happy
    K "I told Emma I'd take her shift tonight, so I should go home and get ready."
    show K Casual Laugh at left
    K "We should do this again sometime, okay?"
    if club == "track":
        show chelsea laugh
        pcname "The kiss? Or puppies?"
        "She giggles."
        K "Both!"
    elif club == "cheer":
        pcname "You can kiss me anytime you want, Kate."
        "She giggles."
        K "Now you're picking on me!"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Okay..."
        "Blushing, you lean down and kiss her quickly."
        "She blushes too, giggling."
        K "I meant the puppies but... That was nice too."
    show K Casual Sad
    "Suddenly, she frowns."
    show chelsea blank
    K "I really wish I didn't have to work tonight! I miss you when we're not together."
    show chelsea happy
    pcname "I miss you too, Kate. Try to have a good night at work, though!"
    K "I will..."
    show bg black with dissolve
    jump events_end_period

label kate_makeout:
    $ clothes = 'cafe'
    show chelsea at right with moveinright
    "The cafe is really busy and most of your night passes in a blur."
    "As you finish clearing your last table, you notice Harper and Zoey standing by the counter."
    show chelsea confused
    "They whisper back and forth, giggling occasionally."
    "Harper rolls her eyes and, though you're not sure why, you feel your stomach sink."
    "Are they talking about you?"
    show K Happy at left with moveinleft
    show chelsea happy
    K "Hey, [pcname]!"
    "You tear your eyes away from the other girls as Kate bounces up to you."
    K "Do you wanna come over after work tonight and watch a movie or something?"
    "She leans in close."
    show K Sad
    K "I know you have school tomorrow, but I really miss spending time with you."
    if club == "track":
        show chelsea laugh
        pcname "Sure! Just gotta finish up here."
    elif club == "cheer":
        pcname "I miss you too. Give me a couple of minutes and I'll be done."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Y-yeah, that would be nice..."
    show chelsea happy
    show K Laugh
    K "Yay! I have to take the garbage out and I'll be ready!"
    "Her smile is contagious; you find yourself smiling softly as you finish clearing the last of your tables."
    show bg black with dissolve
    hide chelsea with dissolve
    hide K Laugh with dissolve
    "After stacking the dishes in the washer, you go to the locker area and change your clothes."
    $ clothes, hair = casualwear
    show bg Cafe with dissolve
    show chelsea at right with moveinright
    show K Casual Happy at left with moveinleft
    K "Ready?"
    show chelsea happy
    pcname "Ready!"
    "Kate grins up at you."
    show K Casual Laugh
    K "Let's go!"
    show bg black with dissolve
    hide K Casual Laugh with dissolve
    hide chelsea with dissolve
    "You follow her out of the cafe and down the street."
    "As you walk, Kate babbles happily about her night."
    show bg CityE with dissolve
    show K Casual Happy at left with dissolve
    show chelsea at right with dissolve
    K "And then he asked if I was old enough to work there. Can you believe it?"
    menu kate_makeout_respond:
        "You {i}are{/i} really cute..." if True:
            if club == "track":
                show chelsea laugh
                pcname "Well you {i}are{/i} really cute, Kate."
            elif club == "cheer":
                pcname "You {i}are{/i} really cute, you know."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I mean... You {i}are{/i} really cute..."
            K "Hey! I--"
            show K Casual Laugh
            "She giggles."
            show K Casual Happy
            show chelsea laugh
            K "I don't know if I should be mad or happy."
        "What a jerk!" if True:
            show chelsea angry
            if club == "track":
                pcname "Ugh! What a jerk!"
            elif club == "cheer":
                pcname "Of {i}course{/i}. Why do they think it's funny to say that?"
            elif club == "yearbook":
                pcname "That's so mean!"
            show K Casual Blank
            K "Right??"
            show chelsea laugh
            pcname "Well, {i}I{/i} know you're not a little kid."
            show K Casual Mad
            K "That's right!"
    show K Casual Blank
    show chelsea confused
    "She goes quiet, and for a moment you wonder what you said wrong."
    show chelsea shocked
    show K Casual Embarrassed
    "Before you can ask, though, you feel her fingers take hold of your own."
    show chelsea happy
    "Silently, she slides her fingers between yours, giving your hand a little squeeze."
    "You walk the last few blocks hand-in-hand, neither of you willing to ruin the moment by breaking the silence."
    show K Casual Happy
    K "Oh, here we are!"
    show bg black with dissolve
    show chelsea blank
    "Kate leads you into her apartment, flicking on the lights and fluttering about the room to make sure everything is presentable."
    show bg CityN with dissolve
    K "So what do you want to watch?"
    "She grabs the remote and turns on Hizorflix."
    show K Casual Blank at left
    K "There's so many options... Sometimes I think that makes it harder to pick."
    "Nodding, you stare at the categories. Drama, horror, comedy, romance..."

    hide chelsea with dissolve
    hide K Casual Embarrassed with dissolve
    show bg black with dissolve
    scene bg KCCS1 with dissolve
    menu kate_makeout_movie:
        "Something funny!" if True:
            $ moviegenre = "comedy"
            K "Good idea. Don't wanna watch anything too serious."
            "As Kate finds a movie, you take a seat next to her on the couch."
            "The movie is about a set of brothers trying to impress the same girl."
            "They make a bet about which one she'll pick and then try to sabotage each other."
            "It's silly, and soon you're both laughing."
            "Your eyes meet after one particularly funny scene, and you realize that you want to be closer to her."
        "Something romantic?" if True:
            $ moviegenre = "romance"
            "Kate blushes."
            K "That... Sounds good..."
            "As Kate finds a movie, you take a seat next to her on the couch."
            "The movie is about a girl who goes back to her hometown for her brother's wedding."
            "She takes a male friend along so she doesn't look single in front of her family."
            "It's cute, but it makes you want to be closer to Kate too."
        "Something dramatic." if True:
            $ moviegenre = "drama"
            K "Yeah... Sometimes it's nice to watch something emotional."
            "As Kate finds a movie, you take a seat next to her on the couch."
            "In the first few scenes, you meet the main character and learn that her adoptive parents recently died."
            "Then, it's revealed that they never told her she was adopted."
            "Her emotions about her parents' deaths hits a little close to home, and you find yourself unexpectedly emotional."
            "Kate watches the screen, tears in her eyes, and you suddenly want to be closer to her."
    show bg KCCS2 with dissolve
    "A little nervous, you slip your arm behind her head and around her shoulders."
    "With a shy smile, Kate leans toward you, resting her head against your shoulder."
    "For a few minutes, you enjoy the comfort of your bodies pressing gently together."
    show bg KCCS3 with dissolve
    "Soon, though, you realize that Kate is fidgeting nervously - and trying very hard to hide it."
    "Suddenly, you realize why she's fidgeting; she's not sure where to put her free hand."
    "It rests awkwardly on her leg, bending her arm at an uncomfortable angle."
    "It would clearly be more comfortable if she rested it against you, but she seems hesitant."
    pcname "Kate... Give me your hand."
    "Embarrassed at being caught, she ducks her head as she offers you her hand."
    show bg KCCS5 with dissolve
    menu kate_makeout_hand:
        "Move it to your thigh." if True:
            "Taking her hand in yours, you lay it on your thigh."
            "Kate cuddles closer, sighing contentedly."
            "Her hand is warm against your thigh and, though you try to focus on the movie, you find yourself distracted."
            "Your attention is diverted further still when her fingers begin tracing small circles on your inner thigh."
            "You glance down at her face, but she doesn't seem to realize she's doing it."
        "Rest it on your chest." if True:
            "Taking her hand in yours, you lay it across your chest."
            "Kate blushes, but doesn't pull away."
            "Her hand is a warm weight and, though you try to focus on the movie, you find yourself distracted."
            "Your attention is diverted further still when her fingers begin rubbing absently over your breast."
            "You glance down at her face, but she doesn't seem to realize she's doing it."
    "You try to pay attention to the movie, but you can't stop thinking about her fingers."
    menu kate_makeout_kiss:
        "Kiss her." if True:
            pcname "Kate..."
            "Hearing her name, she tilts her head back and looks up at you questioningly."
            show bg KCCS6 with dissolve
            if club == "track":
                "Cupping her face with your free hand, you press your lips firmly to hers."
            elif club == "cheer":
                "Running your fingers over her cheek, you lean down and press your lips to hers."
            elif club == "yearbook":
                "Heat suffuses your cheeks as you lean toward her, your lips tentatively brushing hers."
            "She returns your kiss, sighing happily. Her lips, soft and warm, move slowly against your own."
            "Her hand moves to your face as you break the kiss, panting softly."
            "For a moment, you stare at each other, eyes filled with longing."
            show bg KCCS7 with dissolve
            "You both move together, shifting positions so that you lay on the couch and Kate lays over you with her legs between yours."
            "Her lips find yours again and she kisses you with unexpected passion."
            "You run your hands up her sides, drawing them up and down her ribs before wrapping one around to rest on her lower back."
            show bg KCCS8 with dissolve
            "Your other hand drifts upward, your thumb moving over her breast as you cup it in your palm."
            "Kate gasps against your lips, her hips pressing down against your own."
            "Her tongue flicks across your lips teasingly; you part your lips, your tongue darting to meet hers."
            "While your tongues dance between your mouths, you reach around Kate's back and unhook her bra."
            "She breaks the kiss a moment, struggling out of her bra and tossing it aside. Shivering, she kisses you again, hungrily."
            "Cupping her breast through her shirt, you're gratified to feel her nipple stiffening at your touch."
            "She arches her back, pushing her breasts toward you. Slipping her sleeve over her shoulder, you pull her neckline gently down."
            "Her lips press hard against yours, stifling a moan as you run your thumb over her taut, bared nipple."
            "Trembling above you, she grinds her hips against yours and moans again - this time breaking your kiss."
            K "[pcname]..."
            show bg KCCS9 with dissolve
            "Suddenly the room goes dark and Kate yelps."
            "The room illuminates again as the credits begin rolling."
            show bg KCCS10 with dissolve
            K "S-sorry. I guess the movie is over...?"
            "She sits up and fixes her shirt; her nipples poke out against the thin white fabric."
            K "It's pretty late and you have school tomorrow..."
            "You still feel a little breathless and warm."
            hide bg KCCS10
            show bg black
            with dissolve
        "Watch the movie." if True:
            "As the movie continues, her fingers widen their path."
            "You can feel their warmth through the fabric; your body answers with a growing warmth of its own."
            if corruption > 25:
                "Soon, you feel a familiar dampness soaking into your panties."
                "It's almost embarrassing that such an innocent gesture could turn you on, but Kate appears to have that affect on you."
            elif True:
                "To your surprise, you feel a growing dampness soaking into your panties."
                "Embarrassed, you try to ignore it."
            "You focus on the TV, trying to follow what's happening."
            if moviegenre == "comedy":
                "The brothers continue pursuing the girl and sabotaging each other."
                "It gets heated, and for a while it looks like the brothers are sabotaging their own chances as well."
                "But eventually the two brothers discover that the girl is actually {i}two{/i} identical twin girls who have been tricking the brothers the whole time."
                "After the reveal, they realize that there were signs all along."
                "One brother had actually noticed their only difference - a small scar on one of the sister's hands - while on a date, but she'd brushed it off at the time."
                "She says she fell in love with him right then. The sets of siblings pair off and everyone gets a happy ending."
            elif moviegenre == "romance":
                "At her brother's wedding, the girl quickly discovers that her brother's best man is in love with her."
                "She tells her date, who suddenly confesses his own feelings!"
                "But it turns out that, until very recently, the best man was having an affair with the bride."
                "The brother leaves her at the altar, and the girl's pretend date ends up being her real date."
            elif moviegenre == "drama":
                "The girl is furious that her parents kept such a secret from her."
                "Soon, though, her search for her biological parents leads to her learning more about her adoptive parents."
                "She learns how long they tried to have a baby, and how they ended up as foster parents."
                "She learns how they took in a baby girl who barely survived when she was born addicted to drugs and left in a dumpster."
                "And she learns how desperately they fought to keep her when her biological parents tried to get her back."
                "In the end, she understands why they kept her adoption a secret and loves them all the more for it."
            "As the credits roll, Kate looks up at you shyly."
            K "Um, [pcname]...?"
            pcname "Yeah, Kate?"
            K "I'd really like... to kiss you right now."
            "Your heart skips a beat; she's so sweet, you can hardly believe how lucky you are."
            pcname "Me too."
            show bg KCCS6 with dissolve
            "Lifting her head from your shoulder, Kate tilts her face toward yours and kisses you slowly."
            "The kiss is as sweet and innocent as she is, with her lips barely touching yours."
            "Turning toward her, you deepen the kiss, moving your lips over hers while you reach behind her and unclasp her bra."
            "Kate breaks the kiss with a startled gasp before quickly kissing you again, this time more passionately."
            "You press your lips hard against hers, using the embrace to press her back toward the other side of the couch."
            "She grabs your shoulders as you lower her to the couch, your body covering hers."
            "Tearing your lips from hers, you trail little kisses down her neck, stopping at her collar bone."
            K "Oh! [pcname]..."
            "Her hands press down on your shoulders, urging you to continue."
            "You kiss your way from one collar bone to the other, covering every inch of exposed skin in kisses."
            "You can see her pink nipples pressing against the white fabric of her shirt."
            "Sliding the neck of her shirt off one shoulder, you expose one of her breasts."
            "Her nipple hardens under your gaze, the areola darkening slightly as the stiffening tip stretches toward you."
            "You can't help yourself; you lower your head, flicking your tongue over her nipple."
            K "Ah!"
            "She yelps in surprise, but her hands clench around your shoulders, pulling you closer."
            "Her taut nipple presses teasingly against your lips."
            "Parting your lips, you suck her nipple gently between them."
            "Her body trembles with pleasure and she squirms beneath you, gasping as you flick your tongue across her nipple."
            "You suck her nipple hard and her fingers dig into your shoulder as she cries out again."
            K "Oooh!"
            "Reaching under her shirt, you cup her other breast and tweak her nipple."
            "She writhes under you, grinding her hips against you and arching her back so her breasts press closer to your hand and mouth."
            K "Ah... ah..."
            "Her breaths come in short gasps as you give her nipple one last flick of your tongue before releasing it."
            "You kiss her again, pressing your hips to hers and rolling her other nipple between your fingers."
            "She returns your kiss, thrusting her tongue against yours."
            K "Mmm... Mmmm..."
            "Suddenly, an up-beat pop song starts blaring from the table."
            "You sit up, startled, and watch as Kate scrambles to pick up her phone and silence the alarm."
            K "Sorry! I had an alarm set to remind myself to take the trash out before I go to bed!"
            "For a long moment, you stare at each other, both still breathing heavily."
            "Kate snaps out of it first, pulling her shirt up and looking away."
            K "I guess that means it's pretty late, huh? And you have school tomorrow..."
            hide bg KCCS6
            show bg black
            with dissolve
    if corruption > 25:
        show chelsea at right with moveinright
        show K Casual Embarrassed at left with moveinleft
        "You'd like to spend the night, but you can tell Kate isn't ready for that."
        "Her reaction to your touch... The way she trembled and moaned..."
        "You want her more than anything, but her innocence is precious too."
    elif True:



        show chelsea at right with moveinright
        show K Casual Embarrassed at left with moveinleft
        "For a moment, you consider suggesting you spend the night."
        if club == "track":
            "But Kate seems overwhelmed already, and you don't want to make her uncomfortable."
            show chelsea happy
            pcname "Yeah, I should probably get home."
        elif club == "cheer":
            "But none of your stuff is here. You don't have a toothbrush. You'd have to borrow her clothes, her hairbrush..."
            "Maybe next time."
            show chelsea happy
            pcname "It {i}is{/i} pretty late..."
        elif club == "yearbook":
            show chelsea embarrassed
            "But you're just too nervous. What if you're moving too fast for her?"
            pcname "Y-yeah..."
    show K Casual Happy
    show chelsea laugh
    pcname "This was a lot of fun. Thanks for inviting me over."
    show chelsea happy
    if club == "track":
        pcname "I really enjoyed... Everything."
    elif club == "cheer":
        pcname "I really enjoyed spending time with you."
    elif club == "yearbook":
        pcname "I really... enjoyed..."
        "You can't find the right words, but Kate seems to understand."
    show K Casual Embarrassed
    "Kate reddens, but manages to meet your eyes."
    K "Me too..."
    show K Casual Laugh
    K "Oh! I should let you up!"
    show K Casual Blank
    "Scrambling off the couch, Kate helps you to your feet."
    K "I'll go get the door."
    "Full of nervous energy, Kate hurries to the door and holds it open for you."
    show K Casual Laugh
    K "Be careful going home!"
    show K Casual Embarrassed
    show chelsea laugh
    "You can't help it. As you pass her, you lean in quick and steal one last kiss."
    "Startled, Kate presses her fingers to her freshly kissed lips."
    show chelsea happy
    show K Casual Happy
    "She smiles softly and slowly closes the door behind you."
    jump events_end_period

label kate_trouble1:
    $ clothes = 'cafe'
    show chelsea at right with moveinright
    "The night is going well when you go to break. You are making decent tips and the customers have all been pleasant."
    show chelsea confused
    "As you're getting ready to clock back in, two girls are standing at the time clock."
    "While you wait for them to clock out, you can't help but overhear their conversation."
    show Harper Neutral
    show Zoey Happy at midleft with dissolve
    "Harper" "She's just such a {i}baby{/i} though."
    show Harper Happy
    show Zoey Neutral
    "Zoey" "Yeah. Do you think she's even kissed a boy?"
    show Zoey Happy
    show Harper Laugh
    "Harper laughs."
    show Harper Neutral
    "Harper" "Do you think she knows {i}how{/i}?"
    show Harper Happy
    show Zoey Laugh
    "Zoey laughs too, glancing your way."
    "Zoey" "What do {i}you{/i} think, [pcname]? Has Kate ever kissed a boy?"
    show Zoey Happy
    show chelsea shocked
    "For a moment, you panic. Heart pounding, you wonder why they're talking about Kate - and why they're asking {i}you{/i}."
    menu kate_trouble1_kate:
        "Stand up for Kate." if True:
            show chelsea angry
            if club == "track":
                pcname "I don't see why it matters."
            elif club == "cheer":
                pcname "Why do you care?"
            elif club == "yearbook":
                pcname "S-so what if she didn't?"
            pcname "Kate's a really sweet girl. It doesn't matter if she's ever had a boyfriend or not!"
            show chelsea blank
            show Harper Laugh
            "Harper" "Yeah, Zoey. Maybe Kate likes girls better anyway."
            show Harper Happy
        "Remind them there's work to do." if True:
            show chelsea confused
            if club == "track":
                pcname "Don't you have work to do?"
            elif club == "cheer":
                pcname "Is this why you always finish closing so late? You just gossip the whole time?"
            elif club == "yearbook":
                pcname "I don't care... I just want to get my work done."
            show Zoey Laugh
            "Zoey" "Oh, I forgot! You two are {i}friends{/i}, aren't you?"
            show Zoey Blank
            show Harper Neutral
            "Harper" "Yeah, maybe Kate doesn't need a {i}boy{/i}friend with you around."
            show Harper Happy
    show EM Blank at left with moveinleft
    show chelsea blank
    "You don't like where this is going, but thankfully Emilia interrupts, popping her head around the corner."
    show Harper Blank
    show Zoey Blank
    show EM Neutral at left
    "Emilia" "Ladies, that's enough. Stop gossiping and get back to work."
    show EM Blank at left
    show Harper Neutral
    show Zoey Neutral
    "Harper and Zoey" "Yes, Emilia."
    hide EM Blank with dissolve
    hide Harper Neutral with dissolve
    hide Zoey Neutral with dissolve
    "Emilia disappears as quickly as she came and the girls walk away, laughing again."
    "Your heart is in your throat as you clock back in, but as you start waiting on your tables again, you soon forget about what happened."
    show chelsea happy
    "Just before your shift ends, you bump into Kate."
    show chelsea blank
    show K Sad at left with moveinleft
    K "Sorry! Oh, it's you, [pcname]."
    "She wipes tears from her eyes and you notice her uniform is covered in something dark."
    show chelsea sad
    pcname "Kate, what happened?"
    "She sniffles, trying to keep her composure."
    K "Oh, you know me... I'm just so clumsy..."
    "She sniffles again, rubbing her eyes with the back of her hand."
    "Your chest constricts painfully, heart aching for her; she's trying so hard not to cry."
    K "I was carrying a latte and I... I bumped into Zoey and it spilled all over me..."
    show chelsea angry
    "Your breath catches at the mention of Zoey's name. You can't help but wonder..."
    show chelsea confused
    menu kate_trouble1_really:
        "Ask if that's really what happened?" if True:
            if club == "track":
                pcname "Kate... are you sure that's what happened?"
            elif club == "cheer":
                pcname "Zoey can be a bitch. Are you sure it was an accident?"
            elif club == "yearbook":
                pcname "Is that... really what happened?"
            "Kate's eyes widen, filling with tears."
            K "What? Why would you say that?"
            "Tears streak down her cheeks. She rubs them away roughly and pushes past you."
            K "I'm glad you're worried, but I just want to change, okay?"
            hide K Sad with moveoutleft
            "She doesn't wait for you to answer before disappearing into the bathroom."
            show chelsea blank
            play sound PhoneVibration
            "As you get ready to leave, your phone vibrates."

            call screen TextingScene("Kate",
            [
                TextMessage("I'm sorry about earlier"),
                TextMessage("I'm sorry I worried you"),
                TextMessage("I'm sorry too", sender = False),
                TextMessage("You're not mad at me?"),
                TextMessage("No!", sender = False),
                TextMessage("You're really okay though?", sender = False),
                TextMessage("I'm great now"),
                TextMessage("I was so worried that I made you mad"),
                TextMessage("Can we just forget all about this?"),
            ])

            "You still think there's more to the situation, but you don't want to upset Kate any more than she already is."

            call screen TextingScene("Kate",
            [
                TextMessage("Forget what?", sender = False),
                TextMessage("About the argument"),
                TextMessage("oh"),
                TextMessage("Wait"),
                TextMessage("I get it!"),
                TextMessage("Thanks [pcname]! <3")
            ])

            "You tuck your phone away."
            "You're glad Kate's feeling better, but... Was it really an accident?"

            jump events_end_period
        "Try to cheer her up." if True:
            show chelsea happy
            "You wink at her."
            show chelsea laugh
            if club == "track":
                pcname "Well, good thing I like the smell of coffee, huh?"
            elif club == "cheer":
                pcname "Good thing I like my coffee sweet..."
            elif club == "yearbook":
                pcname "Even with the mess... You're still the prettiest girl here."
            show K Blank at left
            K "What...? Oh!"
            show chelsea happy
            show K Happy at left
            "She grins even as her cheeks begin pinkening."
            show K Sad at left
            K "I... I should go change..."
            "She steps past you, pausing at the bathroom door."
            show K Happy at left
            K "Thanks, [pcname]. I really needed that."
            show K Sad at left
            "She walks into the bathroom and you go to clock out."
            hide K Sad with moveoutleft
            show chelsea blank
            play sound PhoneVibration
            "As you get ready to leave, your phone vibrates."

            call screen TextingScene("Kate",
            [
                TextMessage("Thanks again [pcname]"),
                TextMessage("I was really feeling sorry for myself and you made me feel so much better"),
                TextMessage("I'm glad"),
                TextMessage("Sorry I cry so much"),
                TextMessage("Don't be sorry! I like you just the way you are", sender = False),
                TextMessage("You're really okay though?", sender = False),
                TextMessage("I'm great now"),
                TextMessage("Thanks to you"),
                TextMessage("I just didn't want you to worry about me"),
                TextMessage("I gotta get back to work"),
                TextMessage("Thanks again!"),
                TextMessage("Have a good night!", sender = False)
            ])

            "You tuck your phone away."
            "You're glad Kate's feeling better, but... Was it really an accident?"

            jump events_end_period

label kate_dating_phone_short1:

    play sound PhoneVibration
    "In your pocket, your phone vibrates."

    call screen TextingScene("Kate",
    [
        TextMessage("I miss you!"),
        TextMessage("T_T"),
        TextMessage("I miss you too", sender = False),
        TextMessage("I can't wait until we can hang out again"),
        TextMessage("Let's make plans soon, okay?", sender = False),
        TextMessage("YES!!!")
    ])

    "Smiling, you tuck your phone away."

    jump events_end_period

label kate_dating_phone_short2:


    "As you set your alarm, a notification pops up."
    play sound PhoneVibration

    call screen TextingScene("Kate",
    [
        TextMessage("[pcname]"),
        TextMessage("I can't sleep")
    ])

    menu katePhoneBedResponse:
        "What will you say?"
        "Why not?" if True:

            call screen TextingScene("Kate",
            [
                TextMessage("Aww, why?", sender = False),
                TextMessage("Dunno"),
                TextMessage("Tell me a bedtime story?"),
            ])

            menu kate_dating_phone_short2_story:
                "What will you say?"
                "One day there was a squirrel..." if True:

                    call screen TextingScene("Kate",
                    [
                        TextMessage("One day there was a squirrel", sender = False),
                        TextMessage("He invited his friends to a party", sender = False),
                        TextMessage("It was a squirrel party", sender = False),
                        TextMessage("They ran around and ate nuts until everyone had to go home", sender = False),
                        TextMessage("The end.", sender = False),
                        TextMessage("LOL"),
                        TextMessage("Thanks [pcname]"),
                        TextMessage("Good night <3"),
                        TextMessage("Good night Kate <3", sender = False)
                    ])
                "A long time ago, there was a kitten named [kittenname]..." if True:
                    call screen TextingScene("Kate",
                    [
                        TextMessage("A long time ago, there was a kitten named [kittenname]", sender = False),
                        TextMessage("He found a mouse in the kitchen", sender = False),
                        TextMessage("Eek!"),
                        TextMessage("He chased it around and around", sender = False),
                        TextMessage("When he caught it the mouse said", sender = False),
                        TextMessage("Don't eat me [kittenname]! We can be friends!", sender = False),
                        TextMessage("So [kittenname] didn't eat the mouse and they became friends", sender = False),
                        TextMessage("The end.", sender = False),
                        TextMessage("That's good! I'm glad he didn't eat him"),
                        TextMessage("Thanks [pcname]"),
                        TextMessage("Good night <3"),
                        TextMessage("Good night Kate <3", sender = False)
                    ])
                "Once there was a bunny..." if True:
                    call screen TextingScene("Kate",
                    [
                        TextMessage("Once there was a bunny who loved candy", sender = False),
                        TextMessage("He ate too much and got a stomachache", sender = False),
                        TextMessage("That's why most bunnies eat carrots", sender = False),
                        TextMessage("The end!", sender = False),
                        TextMessage("Aww, poor bunny! XD"),
                        TextMessage("Thanks [pcname]"),
                        TextMessage("Good night <3"),
                        TextMessage("Good night Kate <3", sender = False)
                    ])

            jump events_end_period
        "Ignore." if True:

            "You feel a little guilty, but you just want to go to sleep."

            jump events_end_period

label kate_dating_phone_short3:

    play sound PhoneVibration
    "As you walk out of the school, you feel your phone vibrate."

    call screen TextingScene("Kate",
    [
        TextMessage("You work tonight right!?"),
        TextMessage("Yep", sender = False),
        TextMessage("YAY!!!"),
        TextMessage("I can't wait to see you! I miss you sooooo much!"),
        TextMessage("Aww, I miss you too", sender = False),
        TextMessage("See you soon! <3 <3 <3")
    ])

    "You smile as you put your phone away."

    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
