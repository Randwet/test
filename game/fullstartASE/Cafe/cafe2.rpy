label cafe_event5:
    show chelsea happy at right with moveinright
    "As you check on each of your tables, Kate approaches you."
    show K Blank at left with moveinleft
    show chelsea blank
    K "You have another table, [pcname]. He requested you by name."
    "She points him out to you; he's a decent looking guy, but you've never seen him before."
    if corruptkate:
        show K Happy at left
        K "Guess he heard {i}you{/i} have the best {i}specials{/i}, huh?"
        show K Laugh at left
        "She giggles as she walks away."
    if club == "track":
        show chelsea happy
        "You walk directly to his table, giving him a quick smile."
        pcname "I don't think we know each other. Do we, Master?"
    elif club == "cheer":
        show chelsea happy
        "You saunter to his table and smile down at him."
        pcname "So, you asked for me, Master? I don't think we've met."
    elif club == "yearbook":
        show chelsea embarrassed
        "You give him a nervous smile as you approach his table."
        pcname "I-- I don't think we've met... Master?"
    "Man" "No, but I've hear you're the best girl here."
    "He leans toward you, speaking low."
    "Man" "Especially if you tip well."
    menu cafe_event5_encourage:
        "Encourage him." if True:
            $ corruption += 1
            "You realize what he's getting at and smile."
            if club == "track":
                pcname "Does that mean you tip well?"
                "Man" "I tip {i}very{/i} well when someone pleases me."
            elif club == "cheer":
                pcname "That depends how {i}well{/i} you tip..."
                "Man" "I tip {i}very{/i} well when someone pleases me."
            elif club == "yearbook":
                pcname "I... That's me."
                "Man" "Perfect..."
        "Act confused." if True:
            show chelsea confused
            "You furrow your brows, frowning."
            if club == "track":
                pcname "What's that supposed to mean, Master?"
            elif club == "cheer":
                pcname "I don't think I understand, Master..."
            elif club == "yearbook":
                pcname "W-what?"
            "He blinks up at you, shaking his head slowly."
            "Man" "My mistake. Don't worry about it."
            show chelsea blank
            "You take his order and go about your business, though you can't help but wonder how - and what - he'd heard about you."
            jump events_end_period
    show chelsea blank
    "You take his order and check on your other tables."
    "When his food is ready, you deliver it with a smile."
    show chelsea happy
    pcname "Is there {i}anything{/i} else I can do for you right now, Master?"
    "Man" "No, thanks, this looks great."
    "His eyes are on you, not the food, but you're still disappointed by his response."
    show chelsea confused
    "Is he interested in you or not?"
    show chelsea blank
    "You make the rounds again while he eats. When you make your way back to his table, though, there's a twenty on the table."
    "Man" "Miss, it seems there's a mess in the men's room. One of you girls should really clean it up."
    "He looks down at the twenty and back up at you, raising a brow."
    show chelsea happy
    pcname "Yes, Master. I will take care of that for you personally."
    "You ask one of the other girls to check on your tables while you take care of the bathroom."
    "She smiles sympathetically and agrees."
    "Grabbing the maintenance sign and a mop, you hang the sign on the door and slip inside."
    "As you expected, the man is waiting inside."
    "Locking the door behind you, you give him a smile and sink to your knees."
    show chelsea confused
    "Man" "No, no. Stand up."
    "Confused, you do as he says. He motions to the toilet."
    show chelsea blank
    "Man" "Sit down."

    scene bg black with dissolve
    "Surprised, you step past him and sit on the toilet. It feels a little awkward with clothes on."
    show bg CBS1 with dissolve
    "Grinning, he reaches down and unbuttons your top."
    "Man" "Take your bra off."
    "You reach back and unhook your bra. Slipping it off your shoulders, you pull it out through one of your sleeves and drop it on the floor."
    show bg CBS2 with dissolve
    "Man" "Very nice..."
    show bg CBS3 with dissolve
    "He takes one breast in each hand, squeezing gently."
    "Man" "Your tits are perfect..."
    show bg CBS4 with dissolve
    "You gasp as he plays with them, running his thumbs lightly over your nipples."
    "He continues playing with you, bouncing and massaging the soft mounds of flesh, and teasing your nipples until they're hard and sensitive."
    "You tilt your head back, moaning quietly under his touch."
    "Man" "I can't believe this is happening..."
    "You smile up at him; his surprise and happiness spark a warmth in your chest."
    "Releasing your breasts, he unzips his pants, letting his erection spring free."
    show bg CBS5 with dissolve
    "It's surprisingly large - you're almost happy he didn't want a blowjob."
    if corruption > 20:
        "Though, the challenge might have been fun..."
    "He spits on his palms and quickly lubes his cock."
    show bg CBS6 with dissolve
    "Pushing your breasts together, he slides his cock between them."
    "Surprised, you watch as he thrusts his cock up and down between your breasts."
    if corruption > 20:
        "For a moment, you're not sure what to do, but soon the heat and hardness of his cock against your soft flesh fills you with longing."
        "You can't help but think about taking him into your cunt - his long, hard dick pressing deep inside of you."
        "Reaching down, you slide two fingers over your clit and down into the hot wet folds of your pussy."
    "Each thrust brings his tip almost to your chin, so you tilt your head down and open your mouth."
    show bg CBS7 with dissolve
    "When he thrusts again, his tip slips between your lips and you suck gently."
    "He moans and pulls back, leaving your mouth with a {i}pop{/i}."
    "Man" "Oh fuck..."
    "Each time his cock reaches your mouth, you suck the tip until he pulls back."
    "His thrusts grow faster and faster as his climax nears, and you suck just a little harder each time."
    "Precum and saliva trail down his shaft, lubricating your breasts even more."
    if corruption > 20:
        "You plunge your fingers in and out of your pussy, using your other hand to rub your clit in large circles."
    show bg CBS8 with dissolve
    "He jerks back suddenly, moaning as he shoots his load."
    show bg CBS9 with dissolve
    "Long strings of cum stretch from your lips to your breasts; you look up at him, smiling as you lick your lips clean."
    show bg CBS10 with dissolve
    if corruption > 20:
        "He steps back, watching you finger yourself."
        "Man" "Go on."
        "Closing your eyes, you focus on your throbbing clit, rubbing it hard as you work your fingers in and out of your dripping pussy."
        "You feel your muscles begin to tense as your climax nears and you bite down on your lip to hold back your cries of pleasure."
        "Shuddering, you push yourself over the edge."
    show bg Cafe with dissolve
    show chelsea happy at right with dissolve
    "Man" "That was great..."
    "He tucks his cock back into his pants and zips them."
    "Man" "I'll let you finish cleaning up in here."
    "Laughing to himself, he leaves the bathroom while you grab some toilet paper and wipe the cum from your chin and chest."
    "You fix your uniform quickly and step out of the bathroom, pulling the maintenance sign down as you go."
    "As you put the mop and sign away, you notice the man walking toward the door."
    pcname "Thank you, Master! Please cum again!"
    if club == "track":
        "You smile at your own joke and wave."
    elif club == "cheer":
        "You smile, knowing nobody else will know what you {i}really{/i} meant."
    elif club == "yearbook":
        "You blush a little, though nobody else could understand your double meaning."
    jump events_end_period

label cafe_event6:
    show chelsea with dissolve
    "It's a slow night and you're really bored."
    "Your only two tables are teenage boys who can barely speak when they see you."
    "Instead of torturing them with your presence, you take a little break in the crew room."
    if corruptkate:
        show K Happy at left with moveinleft
        K "Oh... [pcname]!"
        "You look up from your phone and see Kate standing in the doorway, glancing around the room."
        show chelsea happy
        pcname "Hi, Kate!"
        "She bounces toward you, grinning."
        show K Laugh at left
        show chelsea confused
        K "Did you have fun the other day?"
        "For a moment, you're not sure what she means."
        show K Happy at left
        K "Come again?"
        if club == "track":
            show chelsea happy
            "You laugh, realizing that she must have heard you with that customer."
        elif club == "cheer":
            show chelsea happy
            "You grin."
            pcname "Always glad to welcome back a good customer!"
        elif club == "yearbook":
            show chelsea embarrassed
            "You blush; did she really understand that comment?"
        show K Blank at left
        K "I wish I could be as confident as you..."
        show chelsea blank
        show K Embarrassed at left
        K "There's a customer who keeps asking me to meet him after work. I'm {i}sure{/i} he wants me to do something... naughty..."
        show K Sad at left
        K "I just... I've never..."
        show chelsea sad
        pcname "{i}Never{/i}?"
        show K Embarrassed at left
        "She blushes, looking down."
        K "I mean... Not really..."
        show chelsea happy
        if club == "track":
            pcname "Oh, Kate... It's not that big of a deal!"
        elif club == "cheer":
            pcname "Oh, sweetie... You have {i}got{/i} to be more adventurous."
        elif club == "yearbook":
            pcname "Oh, I mean, I'm not that confident... I just {i}like{/i} it."
        K "I mean, I {i}want{/i} to. I think..."
        pcname "Then why not try it?"
        show chelsea blank
        "Suddenly a face appears in the doorway."
        show Zoey Neutral at right with moveinright
        show K Blank at left
        "Zoey" "Kate, you have a table. He requested you."
        hide Zoey Blank with moveoutright
        "Zoey disappears and Kate looks up at you with wide eyes."
        show K Embarrassed at left
        K "That must be him. He's always here on Mondays..."
        show K Sad at left
        K "I just... Would you go with me?"
        menu cafe_scene6_joinher:
            "Of course!" if True:
                $ corruption += 1
                show chelsea happy
                show K Happy at left
                K "I knew you would! Thanks, [pcname]!"
                "You follow her out and glance at your tables."
                hide K Happy with moveoutleft
                show chelsea blank
                "The teens are gone, so you clean up and pocket their sad tips."
                show Zoey Blank at right with dissolve
                "Since you don't have any tables, you help Zoey carry out her trays."
                "A few minutes later, Kate approaches you."
                show K Embarrassed at left with moveinleft
                K "Um, [pcname], there's a lot of trash in the back. Could you... help me with it?"
                show chelsea happy
                "You glance at Zoey, giving her an amused look."
                show Zoey Laugh
                "Zoey" "Poor wittle Kate can't lift the heavy stuff. Give her a hand; I've got this."
                show K Happy at left
                K "Thanks, Zoey!"
                "Zoey" "No problem. It's the only way I'll get any tips tonight."
                hide Zoey Laugh with moveoutright
                show K Blank at left
                show chelsea blank
                "You follow Kate to the back and grab some trash bags."
                pcname "Grab the cardboard and follow me."
                "As soon as you get outside, Kate giggles nervously."
                show K Embarrassed at left
                K "I... I told him to meet us out back... Oh! There he is."
                "You see a middle-aged businessman waiting at the edge of the parking lot."
                show GHCMan at right with dissolve
                "Man" "I thought you'd changed your mind, little Kate."
                show chelsea happy
                K "N-no! I just needed an excuse to come outside."
                "Man" "If we step around the corner, I don't think anyone will see us."
                "You and Kate step around the side of the building with him, exchanging nervous smiles."
                "Man" "So you finally agreed to meet me?"
                K "I... I'm not sure what I'm doing, but..."
                K "Is it okay if [pcname] tells me what to do?"
                "Surprised, the man looks between the two of you."
                "Man" "That's fine with me. Whatever you girls want!"
                K "O-okay... good!"

                scene bg black with dissolve
                "Man" "You always like it when I bring you candy... So how about a lollipop to suck on?"
                "As he speaks, the man unbuttons his pants and frees his erection."
                "It's average sized and slightly curved, but you don't think Kate will have too hard of a time with it."
                K "Oh!"
                "Kate blushes furiously, looking down at the ground."
                "Man" "Is it too big for you, little Kate?"
                K "I... I don't..."
                "You can see she's getting nervous; you know she'll change her mind soon, if you don't help her."
                if club == "track":
                    pcname "Well? Get on your knees, Kate."
                elif club == "cheer":
                    pcname "Kate, what are you waiting for? Get on your knees."
                elif club == "yearbook":
                    pcname "Kate... Maybe you should get on your knees...?"
                show bg CASK1 with dissolve
                "Kate's eyes widen a little, but she does as you tell her."
                "Kneeling on the ground in front of him, Kate looks up at him with wide eyes, her lips slightly parted."
                "You have to admit that the contrast between her innocent appearance and what she's about to do is really tempting."
                menu cafe_scene6_katebj_start:
                    "Tell her to open up." if True:
                        pcname "Open your mouth, Kate."
                        "She parts her lips, her wide eyes still staring up at the businessman."
                        show bg CASK2 with dissolve
                        "He steps forward, pressing his cock between her lips."
                        "She lets out a surprised sound and closes her lips around his shaft, sucking gently."
                        "The man exhales loudly and presses himself further into her mouth."
                        show bg CASK3 with dissolve
                        "Instinctively, she raises her hand to grasp his shaft, preventing him from gagging her."
                    "Tell her to use her hand." if True:
                        pcname "Start with your hand, Kate."
                        show bg CASK4 with dissolve
                        "She nods, grasping his shaft with her hand and stroking it hesitantly."
                        "The man clearly enjoys her inexperience, moaning loudly at her tentative touch."
                        K "Are you okay?"
                        "Man" "Great..."
                        "Encouraged, she strokes him faster."
                        show bg CASK2 with dissolve
                        "As she relaxes, she lowers her mouth to his cock and slips the tip inside."
                "You're suddenly aware of your own body when a sudden surge of warmth between your legs draws your attention to your wet panties."
                "Licking your lips, you tell her what to do next."
                menu cafe_scene6_katebj_middle:
                    "Play with his balls." if True:
                        $ corruption +=1
                        if club == "track":
                            pcname "Play with his sack, Kate."
                        elif club == "cheer":
                            pcname "Show his balls a little love too, Kate."
                        elif club == "yearbook":
                            pcname "T-try touching his... his balls."
                        show bg CASK5 with dissolve
                        "Sliding her other hand up his leg, she gently cups his balls and rolls them in her hand."
                        "Man" "Oh, fuck..."
                        "His reaction inspires her to bob her head as she massages his balls, using her other hand to pump his shaft."
                        "You're surprised - she's not usually coordinated enough for something like this!"
                        "After a minute or two, she releases his balls and focuses on taking him further into her mouth."
                    "Touch herself." if True:
                        if club == "track":
                            pcname "You can touch yourself too, Kate."
                        elif club == "cheer":
                            pcname "Don't be shy, Kate. Touch yourself."
                        elif club == "yearbook":
                            pcname "You can... touch yourself too."
                        show bg CASK6 with dissolve
                        "Obediently, she slides her hand up her skirt, stroking herself through her panties."
                        "Man" "Are you that horny, little Kate?"
                        "She nods, the movement pressing his cock in and out of her mouth."
                        "Continuing the motion, she bobs her head and strokes his shaft, while her other hand presses harder against the growing wetness of her panties."
                        "For a few minutes, she really gets into it, moaning with pleasure as she teases herself and him."
                        "Eventually, though, her own pleasure is too distracting - she focuses her attention on taking him further into her mouth."
                show bg CASK3 with dissolve
                "Still stroking his shaft, she bobs her head up and down his cock, taking as much as she can each time."
                "What she lacks in experience, she makes up for with enthusiasm, and the man is soon on the edge of orgasm."
                "You're not sure if Kate's prepared to swallow his load - or if she even knows what to expect."
                menu cafe_scene6_katebj_end:
                    "Let him finish in her mouth." if True:
                        show bg CASK6 with dissolve
                        "You want to see her face when he fills her mouth with his load, so you stay quiet."
                        "She continues bobbing her head on his cock, her eyes half-shut with arousal."
                        show bg CASK7 with dissolve
                        "He drops his hand to the back of her head and you know he's almost there."
                        "Suddenly, Kate's eyes go wide as the man stiffens, his hips jerking forward."
                        "She pulls back, gasping, and cum dribbles over her lips and down her chin."
                        K "Oh!"
                    "Tell her to finish him with her hand." if True:
                        pcname "Kate, finish him with your hand."
                        "Her brows furrow as she pulls her head back, releasing his cock with a wet {i}pop{/i}."
                        "You smile."
                        pcname "Just... trust me."
                        show bg CASK8 with dissolve
                        "She strokes his cock with her hand, staring up at him with wide green eyes, her lips still slightly parted."
                        show bg CASK9 with dissolve
                        "Suddenly his hips jerk forward and he moans, his cock spurting his load across her face."
                        show bg CASK10 with dissolve
                        "She touches her face reflexively, staring at her fingers."
                show bg CASK10 with dissolve
                "She glances at you - you smile, nodding."
                "She smiles back and licks the cum from her lips, looking up at him for approval."
                "As his breathing slows, he tucks his cock away and smiles down at her."
                show bg Cafe with dissolve
                show GHCMan with dissolve
                show chelsea happy at right with dissolve
                show K Happy at left with dissolve
                "Man" "That was great, little Kate. Here..."
                "He pulls out his wallet and hands her some bills."
                "Man" "I hope you'll be here next week?"
                K "Of course!"
                "Man" "Oh, and here..."
                "He passes her his handkerchief and walks away."
                hide GHCMan with dissolve
                "Kate quickly wipes his cum from her face, giggling."
                K "[pcname], I did it!"
                if club == "track":
                    pcname "And? Was it fun?"
                elif club == "cheer":
                    pcname "And did you like it?"
                elif club == "yearbook":
                    pcname "You did! Did you... like it?"
                K "I think I did..."
                K "Did you see his face? I've never seen a man look like that before..."
                pcname "Horny?"
                "She giggles."
                K "That too."
                K "We'd better go back inside or Zoey will be upset!"
                "She bounces toward the back door, then spins around again."
                K "Oh, here! I couldn't have done it without you!"
                "She passes you a $50 bill."
                pcname "But, Kate, you did all of the work..."
                K "I insist! I would {i}never{/i} have done anything like this without your encouragement."
                "You smile, slipping the money into your pocket as she bounces back into the cafe."
                $ Cash += 50
                show black with dissolve
                $ clothes, hair = casualwear
                jump events_end_period
            "You don't need me!" if True:
                show K Embarrassed at left
                show chelsea happy
                K "I... I hope you're right."
                show K Happy at left
                "She smiles up at you."
                K "Thanks, [pcname]! I'll do my best!"
                "You wave her off with a grin."
                pcname "Have fun!"
                hide K Happy with moveoutleft
                show chelsea blank
                "Putting your phone away, you go out and check on your tables."
                "The teens are gone, so you clean the tables and pocket the sad tips they left behind."
                show Zoey Blank at right with dissolve
                "Bored, you help Zoey with her tables, pausing a moment to look at Kate's customer."
                "He's a middle-aged businessman, from the looks of it - not bad looking, but nothing special."
                "He's obviously {i}very{/i} interested in Kate, though. His eyes never leave her."
                hide Zoey Blank with dissolve
                "A little while later, Kate approaches you."
                show K Embarrassed at left with moveinleft
                K "Um, [pcname], I'm going to... to take the trash out. Could you keep an eye on my section?"
                "She looks nervous, but excited."
                show chelsea happy
                pcname "Sure... take your time, Kate."
                hide K Embarrassed with moveoutleft
                "She grins and bounces into the back. You notice that her customer isn't at his table anymore."
                show chelsea blank
                "Thirty minutes later, as you finish dusting a cocoa heart onto a hot chocolate, you hear Kate:"
                show K Laugh at left with moveinleft
                show chelsea sad
                K "Oh, that's my favorite! I love making the hearts on top!"
                show chelsea happy
                "You glance over at her, smiling."
                pcname "All done taking out the trash?"
                show K Embarrassed at left
                "She blushes immediately, and you notice there's a little smear of dirt on her cheek."
                K "Yeah, thanks for covering me."
                "She leans in close and whispers:"
                K "I... I gave him a blowjob!"
                "You giggle at her excitement."
                pcname "Did you?"
                show K Happy at left
                "She nods, giggling too."
                K "And he gave me $100, so I must have done a good job!"
                show chelsea sad
                pcname "Wow, really? That's great!"
                show chelsea happy
                show K Laugh at left
                K "I'm gonna get back to work. Thanks, [pcname]!"
                "You can't help but smile at her excitement."
                "Grabbing the hot chocolate, you go back to work."
                show black with dissolve
                $ clothes, hair = casualwear
                jump events_end_period
    elif True:
        show K Blank at left with dissolve
        show Zoey Blank at right with dissolve
        "Playing with your phone, you overhear Kate talking to Zoey."
        show K Embarrassed
        K "He's the guy out there in the business suit..."
        show Zoey Neutral
        "Zoey" "The middle-aged guy?"
        show K Mad
        K "Yeah, that's him. He comes in every Monday and asks me to meet him after work."
        show Zoey Worried
        "Zoey" "Ew, really? What a creep!"
        show K Sad
        show Zoey Laugh
        K "I know, but what can I do?"
        "Kate pouts and Zoey laughs."
        show Zoey Neutral
        "Zoey" "Not much. Ugh, I hate guys like that..."
        show chelsea shocked
        show K Blank
        "You're surprised that anyone would proposition Kate like that - she's so sweet and innocent."
        if club == "track":
            show chelsea happy
            "You could help her out by distracting him, you suppose."
        elif club == "cheer":
            show chelsea happy
            "Nothing like {i}you{/i}."
        elif club == "yearbook":
            show chelsea embarrassed
            "Maybe you could help her?"
        "You wonder if he'd be interested in meeting you? You could slip him a note and see..."
        show K Laugh
        show Zoey Laugh
        menu cafe_event6_note:
            "Slip him a note." if True:
                $ corruption += 2
                show chelsea happy
                "Smiling, you write a short note telling him that you're more fun than Kate and to come talk to you."
                hide K Laugh with dissolve
                hide Zoey Laugh with dissolve
                "As you pass by his table, you drop it on his lap and keep going."
            "Ignore it." if True:
                "After the way Kate's reacted in the past, you decide to let her deal with him on her own."
                jump events_end_period
        "You try to catch his eye after that, but he doesn't seem to notice you."
        show chelsea angry
        "Annoyed, you go back to your tables, cleaning them and pocketing the sad tips those teens left."
        show chelsea sad
        "A tap on your shoulder startles you."
        show chelsea blank
        show GHCMan with dissolve
        "Man" "You're not really my type, but since little Kate is playing hard to get..."
        "Man" "I guess you'll have to do. If you want to have some fun, meet me outside."
        hide GHCMan with dissolve
        "Walking into the kitchen, you find Zoey."
        show Zoey Blank at right with dissolve
        pcname "I'm going to take the trash out. Can you watch my tables?"
        show Zoey Neutral
        "Zoey" "Why not? They're all empty anyway..."
        show Zoey Blank
        show chelsea happy
        pcname "Thanks, Zoey!"
        hide Zoey Blank with dissolve
        show chelsea blank
        "Grabbing the trash bags, you walk out to the dumpster and throw them inside."
        show GHCMan with dissolve
        "Man" "Why don't you step around the corner here?"
        "You turn to see the businessman standing around the side of the building, well out of sight."
        show chelsea happy
        "Smiling, you walk over to him."
        "Man" "Like I said, you're not really my type, but since little Kate isn't interested..."
        "He unbuttons his pants and pulls out his cock - it's average sized and slightly curved."
        show chelsea blank
        "Man" "I want you to act as shy and innocent as you can, and I'll give you a lollipop to suck on."
        menu cafe_scene6_youlldo:
            "No way!" if True:
                $ corruption -= 2
                if club == "track":
                    show chelsea angry
                    pcname "What? Fuck off!"
                elif club == "cheer":
                    show chelsea blank
                    pcname "No thanks. I don't encourage pedos."
                elif club == "yearbook":
                    show chelsea sad
                    pcname "W-what? No thank you!"
                "Scowling, the man tucks his cock back into his pants"
                "Man" "Waste of time..."
                hide GHCMan with dissolve
                "You roll your eyes and go back to work."
                show black with dissolve
                $ clothes, hair = casualwear
                jump events_end_period
            "Sounds good!" if True:
                $ corruption += 1
                if club == "track":
                    show chelsea happy
                    pcname "I think I can do that."
                elif club == "cheer":
                    show chelsea happy
                    pcname "Sure. Whatever you want, Master."
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "O-okay."

                scene bg black with dissolve
                show bg CASC1 with dissolve
                "Doing your best impression of Kate, you stare up at him with wide eyes and sink to your knees."
                pcname "H-how should I do it, Master?"
                "Man" "Just act like you're sucking a lollipop, little..."
                "He pauses, as if only now realizing he never asked your name."
                show bg CASC2 with dissolve
                pcname "You can call me Kate if you want, Master."
                "He nods, smiling down at you, and presses his cock to your lips."
                "Man" "Go on and open up, little Kate."
                show bg CASC3 with dissolve
                "Nodding slowly, you open your lips and suck his tip into your mouth."
                "Man" "There you go. That's my good girl."
                show bg CASC6 with dissolve
                "Slowly pumping his shaft with one hand, you watch his face as you suck the tip of his cock."
                "Man" "Can you take a little more?"
                show bg CASC7 with dissolve
                "You nod your head, staring up at him through your lashes, and slowly take him further into your mouth."
                "Man" "Is that too much, little Kate? Am I too big for you?"
                "You moan softly, as if struggling to handle him, while you bob your head up and down his cock."
                "To your surprise, you're a little turned on by the act - the idea of being corrupted by a strange man has its own appeal."
                "You can't help but wonder if that's why he's interested in Kate, and what it would be like to see Kate doing this."
                "Moaning around his cock, you refocus your attention on your act."
                show bg CASC8 with dissolve
                "When you start tasting precum, you pull back and let his cock fall from your lips, still stroking him with your hand."
                pcname "Am I doing it right, Master?"
                "Man" "Don't stop! Just keep sucking, and I'll give you a tasty treat."
                show bg CASC7 with dissolve
                "Suppressing a laugh, you swallow his cock again, bobbing your head eagerly."
                "It's not long before you feel his balls draw up and his thighs tense."
                show bg CASC9 with dissolve
                "As his hips begin jerking, you pull back and suck his tip hard, swallowing his load."
                "Man" "Oh {i}fuck{/i}..."
                show bg CASC10 with dissolve
                "Releasing his cock, you sit back on your heels and look up at him, licking your lips."
                pcname "Th-thank you, Master. It was delicious."
                "Breathing heavily, he stuffs his cock back into his pants and fishes around for his wallet."
                show bg Cafe with dissolve
                show GHCMan with dissolve
                show chelsea happy with dissolve
                "Man" "That was great, girl. Here."
                "He presses some bills into your hand and tucks his wallet away."
                "Man" "Maybe I'll have to start requesting the redhead instead..."
                hide GHCMan with dissolve
                "As he walks away, you glance down at the money - two $50 bills! - and pocket them quickly."
                pcname "Thank you, Master. I'll serve you anytime!"
                "Straightening your clothes, you walk back inside with a grin."
                $ Cash += 100
                show black with dissolve
                $ clothes, hair = casualwear
                jump events_end_period

label cafe_event7:
    show chelsea at right with moveinright
    "As you're cleaning a table, Emilia approaches you."
    show EM Neutral at left with moveinleft
    "Emilia" "[pcname], dear... Zoey went home sick and she was supposed to be closing the store with Emma tonight."
    show EM Happy at left
    "Emilia" "Would you mind staying and helping her close? Normally I would do it, but I have a dinner reservation."
    show EM Blank at left
    "You don't really want to, but you don't have any reason not to either."
    "And Emilia can be very hard to say no to."
    pcname "Sure, Emilia, I'll do it."
    show EM Happy at left
    "Emilia" "Perfect. I knew you'd help out!"
    "Emilia" "Emma can show you what to do, so just ask her if you have any questions."
    hide EM Happy with moveoutleft
    "As Emilia walks away, a new customer in your section calls you over."
    show D Smirk with dissolve
    "Man" "Hey, sweetheart. Sounds like you're working late tonight, huh?"
    show D Blank
    show chelsea happy
    pcname "Guess so! How can I serve you, Master?"
    show D Happy
    "Man" "I've been looking forward to seeing you, actually. I've heard great things about the redhead at this cafe..."
    if club == "track":
        "You smile, knowing what he must have heard."
    elif club == "cheer":
        show chelsea laugh
        "You laugh and give him a wink."
    elif club == "yearbook":
        show chelsea embarrassed
        "You blush, knowing what he must have heard."
    show D Neutral
    "Man" "When I heard you were closing up shop tonight, it gave me an idea..."
    show chelsea sad
    show D Smirk
    "Man" "If you can sneak me in after hours and show me a good time, I'll make it worth your while."
    show D Blank
    "Surprised, you wonder out loud:"
    show chelsea confused
    pcname "How much?"
    show chelsea sad
    show D Happy
    "Man" "Three hundred. And an extra three if you can find another girl to join."
    show D Smirk
    "For a second, all you can do is stare; that's a lot of money!"
    show D Neutral
    "Man" "Well? What do you think?"
    menu cafe_scene7_sneak:
        "I'll do it!" if True:
            $ corruption += 1
            show chelsea happy
            $ cafesex = True
            pcname "Sure, I'll do it."
        "I can't..." if True:
            show chelsea sad
            show D Blank
            pcname "Sorry, I can't."
            show chelsea blank
            show D Neutral
            "Man" "Ah well... It was worth a try."
            show D Blank
            "You take his order and go back to work."
            hide D Blank with dissolve
            "Though he doesn't mention it again, you wonder what would have happened if you'd taken him up on his offer."
            jump events_end_period
    show D Laugh
    "Man" "Great! I'll wait in the parking lot. Just let me know when the coast is clear."
    hide D Laughing with dissolve
    "You take his order and go back to work."
    if corruptkate:
        show chelsea blank
        "When you get the chance, you approach Kate."
        show K Blank at left with moveinleft
        pcname "So, um... One of my customers offered me $300 to sneak him in after close tonight."
        show K Embarrassed at left
        K "Seriously? Are you going to do it?"
        show chelsea laugh
        "You laugh."
        show chelsea happy
        pcname "Of course! And he said he'd pay double if another girl wanted to join us..."
        show K Blank at left
        "Kate's mouth forms a surprised O."
        K "You want {i}me{/i} to join you?"
        pcname "Only if you want to. $300 is a lot of money..."
        show K Embarrassed at left
        K "Wh-what would I have to do?"
        "You shrug."
        pcname "He just said we'd have to show him a good time."
        K "I don't know..."
        pcname "Don't worry - it'll be fun! You don't have to do anything you don't want to!"
        "Kate bites her lip."
        K "I... I'll do it!"
        pcname "Great! Let's ask Emma if you can cover her tonight..."
        scene bg black with dissolve
        "Emma is surprised, but quickly agrees since she hates closing the cafe."
        "At the end of the night, you and Kate wash the dishes, sweep and mop, and then take out the trash."
        "As Kate tosses the last bag of trash into the dumpster, you scan the parking lot for the man's car."
        "Motioning for him to follow you, you and Kate walk inside, leaving the back door slightly ajar."
        "He follows you through the kitchen and out into the lobby, nodding his head at the equipment and supplies."
        show bg Cafe with dissolve
        show chelsea happy at right with moveinright
        show K Embarrassed at left with moveinleft
        show D Happy with dissolve
        "Man" "Not a bad place. Always wondered what it looked like back here."
        "Kate giggles nervously."
        K "Can I get you anything, Master?"
        show D Smirk
        "The man cracks a half-smile and shakes his head."
        show D Neutral
        "Man" "You don't have to call me Master. It's after hours and that's not really my thing anyway."
        show K Sad at left
        K "Oh! S-sorry, I..."
        show D Smirk
        "He shakes his head."
        show K Blank at left
        show chelsea blank
        show D Happy
        scene bg black with dissolve
        show bg CT1 with dissolve
        "Man" "Don't worry about it. Okay, Red, you gonna show me what you got?"
        "Smiling, you begin taking off your uniform, one piece at a time."
        "The man leans against a table, arms crossed, watching."
        show bg CT2 with dissolve
        "Stripping off your bolero, apron, blouse, and skirt, you grab the top of your left stocking."
        "Man" "Nah, leave the stockings on. I kinda like 'em."
        show bg CT3 with dissolve
        "Smiling, you unhook your bra and toss it aside."

        show bg CT4 with dissolve
        "He looks at Kate."
        "Man" "So, is Blondie just gonna watch? I don't mind, but I'm not paying for that."
        show bg CT5 with dissolve
        "You glance at Kate and give her a nod; she turns bright red, but follows your lead."
        "She unties her bolero and lays it aside. Then her apron."
        "She hesitates before pulling off her blouse, crossing her arms shyly over herself."
        "When she looks at you, you nod your encouragement and give her a smile."
        show bg CT6 with dissolve
        "As she pulls her skirt down, the man sighs."
        "Man" "Too bad. I was hoping those were crotchless panties so you could leave the garters on."
        "Somehow, Kate turns even pinker. She turns away to take her bra off, crossing her arms over her chest as she turns back around."
        show bg CT7 with dissolve
        "Man" "All right... Not bad, not bad..."
        "He looks you and Kate up and down, nodding his approval."
        "Man" "So, is that it?"
        "Smiling, you motion for Kate to come closer."
        show bg CT8 with dissolve
        "Sinking to your knees, you unzip his pants and free his erection, giving it a slow, casual stroke."
        show bg CT9 with dissolve
        "Kate reaches out to cup his balls, massaging them gently."
        "Man" "There you go..."
        show bg CT10 with dissolve
        "Lowering your lips to his tip, you swirl your tongue around it slowly."
        show bg CT11 with dissolve
        "Kate follows suit, releasing his balls to trail her tongue up and down his shaft."
        "You shift to the other side, mirroring her movements."
        show bg CT12 with dissolve
        "When you both reach his tip, your tongues meet, caressing each other and the tip of his cock."
        "Kate closes her eyes, teasing your tongue with her own."
        show bg CT13 with dissolve
        "Wrapping your hand around his shaft, you slowly stroke his cock while you meet Kate's lips with your own."
        "She moans softly against you as you slip your tongue past her lips."
        show bg CT14 with dissolve
        "You kiss her deeply, exploring her mouth as you stroke the man's cock."
        "When you finally pull away, her face is pink and your eyes are heavy with arousal."
        show bg CT15 with dissolve
        "You smile and nod towards his cock; she lowers her lips to it without hesitation."
        show bg CT16 with dissolve
        "While you stroke his shaft, she gently bobs her head up and down, swallowing as much of him as she can."
        show bg CT17 with dissolve
        "Once, she goes too deep, gagging and pulling back, her eyes moist."
        show bg CT18 with dissolve
        "You take over, wrapping your hand around his cock while lowering your mouth around it."
        "More experienced than Kate, you bob your head up and down his cock easily."
        "Man" "Fuck..."
        show bg CT19 with dissolve
        "Suddenly, you feel Kate's arms sliding around you. She cups one breast in her hand, bouncing it gently."
        "While you suck the man off, Kate fondles your breasts, trailing her fingers over their curves and running her thumbs over your stiffening nipples."
        show bg CT20 with dissolve
        "She takes one nipple between her fingers, rolling it gently. Ripples of pleasure course through you, making your clit throb in response."
        show bg CT21 with dissolve
        "Releasing that nipple, she does the same with the other. All the while, you draw your lips up and down the man's cock, swallowing him hungrily."
        "You're so focused on Kate's fingers that you barely notice his muscles clenching."
        show bg CT22 with dissolve
        "You're surprised when he climaxes, filling your mouth and throat with hot, salty fluid."
        "Pulling back, you swallow convulsively, trying not to choke on his load."
        "Man" "I'm gonna need a couple minutes. Why don't you girls keep going?"
        "Kate blushes, suddenly shy again, but quickly presses her lips to yours."
        show bg CT14 with dissolve
        "You open your mouth, letting her taste him on your lips and tongue."
        "While your tongues mingle, you caress her breasts, pinching each nipple until she moans."
        "Suddenly, she pulls back."
        K "I don't... I've never done anything like this with a girl..."
        pcname "That's okay. Just do whatever feels good."
        "She presses her lips to yours again before running her hands over your breasts."
        "Lost in the sensations, your tongues twirl around each other, while you pinch each others nipples, rolling them between your fingers."
        "While one hand fondles her breast, you trail the other lower, over her pussy."
        "Lightly, you drag your fingertip across the front of her panties, until you reach the tell-tale wetness at her opening."
        "Dragging your finger back upward, you find the swollen nub of her clit and draw tiny circles."
        "She gasps against your mouth, moaning as your fingertip gently teases her most sensitive bit of flesh."
        "Abruptly, fingers press between your ass cheeks, sliding between your lower lips."
        "Man" "You're hot and ready, aren't ya?"
        "You press your hips back toward him, sliding his finger inside of you."
        "Kate whimpers, disappointed by your distraction. You swirl your finger over her clit again, while the man behind you slowly fingers your pussy."
        "Man" "Don't worry, Blondie, you'll both be satisfied soon."
        "Withdrawing his finger, he turns you to face him and points to the counter."
        "Man" "Bend over the counter."
        "Smiling at Kate, you do as he says, sauntering to the counter."
        "Man" "You too, Blondie."
        "Kate scrambles to her feet"
        "Biting her lip, she slowly approaches the counter and bends over it, facing you."
        show bg CT23 with dissolve
        "Man" "Now, which one first... What do you think, Red?"
        menu cafe_scene7_kate_first:
            "Me!" if True:
                if club == "track":
                    pcname "I'm ready and waiting!"
                elif club == "cheer":
                    pcname "Me, please. I really want to be fucked..."
                elif club == "yearbook":
                    pcname "I... I really want..."
                "Man" "Well, how could I refuse?"
                show bg CT24 with dissolve
                "Pushing your legs apart, he slides the tip of his cock against your opening, lubricating himself with your juices."
                "Without hesitation, he presses himself inside, stretching you slowly but steadily until he's fully sheathed inside of you."
                pcname "Ohhhhh..."
                show bg CT25 with dissolve
                "Suddenly, a hand grabs yours, squeezing gently."
                "You open your eyes to see Kate, smiling nervously at you."
                "You smile back - and then gasp as he pulls back and thrusts into you again."
                "Man" "You like that, Red?"
                if club == "track":
                    pcname "Oh yeah..."
                elif club == "cheer":
                    pcname "Yes... Please... Don't stop!"
                elif club == "yearbook":
                    pcname "Y-yes..."
                "Pleased, he grabs your hips and thrusts into you again. And again, and again."
                show bg CT26 with dissolve
                "Gasping with every thrust, you press your hand under you, running it down your stomach and between your legs."
                "While he fucks you, you rub the swollen nub of your clit, edging yourself toward your own climax."
                show bg CT27 with dissolve
                "Suddenly, he stops, withdrawing his cock from your hungry, eager hole."
                "You open your eyes, whimpering your disappointment."
                "Man" "Can't let you have {i}all{/i} the fun, Red."
                show bg CT28 with dissolve
                "He steps behind Kate, spreading her legs and pressing his cock against her."
                "Her eyes widen, her nervousness obvious; you smile, giving her a reassuring nod."
                "You watch her face as he enters her - her eyes widening further before squeezing shut, her mouth forming a surprised O."
                show bg CT29 with dissolve
                "Her hand clenches yours as he moves against her, rocking her body back and forth against the counter."
                K "So... So big..."
                "She faces you, her eyes half open and unfocused, and she moans with every thrust."
                "Despite her initial trepidation, it's clear that she's enjoying herself now."
                K "P-please... I need... I..."
                "Your clit throbs, reminding you of your own arousal. Still focused on Kate, you absently rub your fingers back and forth over your swollen sex."
                K "Oh! Ohhh! I... I..."
                "He stops, withdrawing from her and moving back to you."
                "Kate whimpers, pressing her free hand between her legs."
                "You watch her face as she pleasures herself - even as the man presses his cock back inside of you."
            "Kate!" if True:
                if club == "track":
                    pcname "I think Kate needs broken in, don't you?"
                elif club == "cheer":
                    pcname "Ready, Kate? You could use the practice..."
                elif club == "yearbook":
                    pcname "K-Kate?"
                "Man" "Here that, Blondie?"
                show bg CT28 with dissolve
                "He steps behind Kate, spreading her legs and pressing his cock against her."
                "Her eyes widen, her nervousness obvious; you smile, giving her a reassuring nod."
                show bg CT29 with dissolve
                "She moves her hand closer to yours. Taking it in your own, you give it a gentle squeeze."
                "You watch her face as he enters her - her eyes widening further before squeezing shut, her mouth forming a surprised O."
                "Man" "You like that, Blondie?"
                K "I... I..."
                "He fucks her slowly, while she stares at you wide-eyed."
                "Her eyes squeeze tight and she clenches your hand - for a moment you're concerned."
                K "H-harder... please... I..."
                "Her body rocks back and forth against the counter as he fucks her."
                "Each thrust is met with a cry of pleasure; you smile at her sudden sensuality."
                "Your clit throbs, drawing your attention to your own arousal."
                "Just as you slip your free hand down between your legs, Kate whimpers in disappointment."
                K "I... I..."
                "Man" "Don't be selfish, Blondie. Red needs some attention too."
                "He steps behind you, spreading your legs and pressing his cock against you."
                show bg CT30 with dissolve
                "Man" "Fuck you're wet..."
                "Still slick with Kate's juices, he presses his cock inside of you, filling you in a single thrust."
                "Man" "Guess you really did need some attention, huh?"
                if club == "track":
                    pcname "I need you to fuck me!"
                elif club == "cheer":
                    pcname "Oh... Fuck yes..."
                elif club == "yearbook":
                    pcname "Y-yeah... I..."
                "He grabs your hips, using them for leverage as he fucks you hard and fast."
                "You cry out, pressing your fingers hard against your clit and rubbing frantically."
                show bg CT31 with dissolve
                "Just as you near your own climax, he pulls out of you, letting your juices run down your inner thigh."
                "Your eyes flutter open in surprise - beside you, Kate watches your face, gasping as she pleasures herself."
                "He steps behind Kate again. She rocks her hips toward him, eager to be filled again."
        "Man" "Which one of you will make me blow it, huh?"
        show bg CT26 with dissolve
        "He continues alternating between you and Kate, fucking each of you for a minute or two before switching again."
        "While one of you is being fucked, the other watches, her fingers rubbing frantically at her own clit, eyes half glazed with arousal."
        show bg CT30 with dissolve
        "You climax twice - once while he fucks you, and again shortly after, watching Kate's face as he fucks her."
        show bg CT29 with dissolve
        "Finally, as he pumps himself in and out of Kate, she cries out and he stiffens, his hips bucking erratically."
        "Her body shakes with her own climax and you watch as he steps away from her, his load oozing from her cunt."
        show bg CT32 with dissolve
        "You sigh and stand, pleased but still aroused."
        "Man" "Sorry, Red. Looks like Blondie wins."
        "He stuffs his cock back into his pants. Meanwhile, Kate slowly starts to come to her senses."
        "Pulling her hand from yours, she pushes herself up from the counter."
        K "That was..."
        "She smiles sleepily, worn out from the exertion."
        "You smile back."
        show bg CafeN with dissolve
        show D Happy with dissolve
        show chelsea happy at right with dissolve
        show K Happy at left with dissolve
        "Man" "Here you go... $300 each."
        "Man" "And take this too. It's my card."
        "He passes you each a stack of bills with a business card on top."
        "It reads: {i}Cock and Crow Lounge, Daniel Silver, Owner.{/i}"
        show K Blank at left
        show chelsea confused
        pcname "You... own a bar?"
        show D Smirk
        Dan "Sure do. Honestly, I could use some carefree girls like the two of you."
        Dan "If you're ever looking for something new, call me."
        show chelsea happy
        "You stare at the card a moment and smile."
        pcname "Thanks."
        show D Neutral
        Dan "Anyway, this was fun, but I should let you girls clean up."
        Dan "Mind if I let myself out the back?"
        hide D Neutral with dissolve
        show chelsea blank
        "Since you're both still mostly naked - and dripping fluids - you both agree."
        "Kate slips her clothes back on and grabs a cleaning cloth."
        "She wipes down the counter while you dress, tossing it into the dirty towel hamper."
        show K Embarrassed at left
        K "That was..."
        "She looks down, blushing."
        show chelsea embarrassed
        if club == "track":
            pcname "Sure was!"
        elif club == "cheer":
            pcname "Really good? Yeah..."
        elif club == "yearbook":
            pcname "Y-yeah... It was."
        show K Happy at left
        K "I should get home. See you soon?"
        hide K Happy with moveoutleft
        show chelsea happy
        pcname "Me too. See ya!"
        "You walk home, highly aware of the wetness beneath your skirt."
        $ Cash += 300
        hide chelsea with dissolve
        show bg black with fade
        jump events_end_period
    elif True:
        show chelsea blank
        show Emma Happy at right with dissolve
        "At the end of the night, you and Emma finish washing the dishes and put everything away."
        "When the floors are swept and mopped, Emma tells you she'll finish taking the trash out if you want to go."
        show chelsea happy
        pcname "That's okay! Why don't you let me do it and you can get out of here?"
        show Emma Laugh
        "Emma" "Oh... Sure! Thanks, [pcname]!"
        pcname "No problem. I don't normally close, so I don't mind helping out."
        "Emma grabs her things as you take the trash out, waving goodbye as you toss the bags into the dumpster."
        hide Emma Laugh
        show chelsea blank
        "When she's gone, you scan the parking lot, quickly finding the man's car."
        "Motioning for him to follow you, you leave the back door ajar and walk inside."
        show D Happy with dissolve
        "He follows you through the kitchen and out into the lobby, nodding his head at the equipment and supplies."
        "Man" "Not a bad place. Always wondered what it looked like back here."
        show D Smirk
        "Man" "So... Ready to show me what you can do?"
        scene bg black with dissolve
        if club == "track":
            "With a cocky grin, you sink to your knees and unbutton his pants."
        elif club == "cheer":
            "Giggling, you sink to your knees and unbutton his pants, looking up at him through your lashes."
        elif club == "yearbook":
            "Blushing, you sink to your knees and unbutton his pants."
        show bg CCD1 with dissolve
        "Freeing his cock from his boxers, you lick your lips and wrap them around the tip of his cock."
        "Bobbing your head, you work him in and out of your mouth, lubricating his shaft as you slowly take more of him."
        if corruption > 25:
            "When he hits the back of your throat, you push down the urge to gag and swallow his cock until his balls slap against your chin."
            "You pull back, sucking hard until you reach the tip. Relaxing your throat, you swallow his cock again."
            "Over and over, you deep throat him, breathing through your nose when you get the chance."
            "As he gets closer, he wraps his hand in your hair, tugging gently as you suck him off."
            "Then his muscles tense and you know he's close, but he pulls back, releasing your hair as his cock slips from your lips."
        elif True:
            "He hits the back of your throat and you gag, pulling back and wrapping the rest of his shaft in your fist."
            "You suck him off, making up for your inability to deep throat with pure enthusiasm."
            "Bobbing your head and stroking him with your hand, you use your other hand to massage his balls."
            "Man" "Fuck..."
            "He pulls back suddenly, his cock leaving your mouth with a wet {i}pop{/i}."
        "Man" "Don't want to finish too fast."
        "Man" "Gonna take the uniform off, Red?"
        "Smiling, you begin taking off your clothes one piece at a time."
        "The man leans against a table, arms crossed, watching."
        show bg CCD2 with dissolve
        "Stripping off your bolero, apron, blouse, and skirt, you grab the top of your left stocking."
        "Man" "Nah, leave the stockings on. I kinda like 'em."
        "Smiling, you unhook your bra and toss it aside."
        "Finally, you pull your panties down and kick them away, standing before him in nothing but your stockings."
        "His lazy smile puts you at ease."
        "Man" "Not bad... Those tits are great."
        if club == "track":
            "You smile, looking down at them."
        elif club == "cheer":
            "You smile."
            pcname "Want a closer look?"
        elif club == "yearbook":
            "You blush, resisting the urge to cross your arms over your chest."
        "He motions with one hand, beckoning you."
        "Man" "Get over here."
        "You approach him slowly, enjoying the heaviness of his gaze, almost like a physical caress."
        "As you near him, he reaches out and pinches your left nipple, his smile widening as you gasp."
        "His other hand covers your right breast, squeezing gently."
        "Man" "{i}Really{/i} great."
        "His hands roam over your body, caressing your breasts and rubbing your nipples until your knees feel weak."
        "Man" "Want something, Red?"
        if club == "track":
            pcname "Fuck me..."
        elif club == "cheer":
            pcname "I want your cock inside of me..."
        elif club == "yearbook":
            pcname "P-please, I want..."
            "You look down at his cock, hard and already wet with your saliva."
        "Man" "Sit on the table."
        "You walk to the table, turn to face him, and lift yourself up onto the table."
        "Man" "Lay down."
        show bg CCD3 with dissolve
        "As soon as your back touches the table, he pushes your legs apart and presses his cock to your opening, entering you slowly."
        "Hooking his hands under your thighs, he lifts your legs into the air and presses further into you."
        "When he's fully sheathed inside your cunt, he pulls back and, hands hooked under your knees, thrusts back into you."
        "He thrusts a few more times, then lifts your legs higher."
        "With your hips elevated further, his next thrust rubs right across your g-spot, making you cry out."
        "Man" "Like that, Red?"
        "He thrusts again; pleasure shoots through your abdomen, wringing another cry from your lips."
        "Again and again he thrusts into you, until you're screaming in response."
        if club == "track":
            pcname "Fuck!"
            pcname "Ohhhh fuck!"
        elif club == "cheer":
            pcname "Yes! OH YES!"
            pcname "Yeeeeessss!"
        elif club == "yearbook":
            pcname "Oh! OHHH!"
            pcname "Oh, please! PLEASE!"
        "You thrust your hand down and rub your clit frantically, desperate to get off."
        "Man" "Oh fuck..."
        "He thrusts harder and faster, pounding your pussy until you clench around him, your toes curling as your orgasm sweeps over you."
        show bg CCD4 with dissolve
        "He stiffens, managing a few final thrusts as he empties himself into your spasming cunt."
        "Pulling out of you, he tucks himself back into his pants and fishes for his wallet."
        show bg Cafe with dissolve
        show D Happy with dissolve
        show chelsea sad at right with dissolve
        "Man" "Here you go... $300."
        show D Neutral
        show chelsea happy
        "Man" "And take this too. It's my card."
        "You smile, mind still foggy with pleasure."
        "He passes you a stack of bills with a business card on top."
        "It reads: {i}Cock and Crow Lounge, Daniel Silver, Owner.{/i}"
        show chelsea confused
        pcname "You... own a bar?"
        show D Happy
        Dan "Sure do. Honestly, I could use a carefree girl like you."
        Dan "If you're ever looking for something new, call me."
        show D Blank
        "You stare at the card a moment before sitting up."
        show D Neutral
        Dan "Anyway, this was fun, but I should let you clean up."
        Dan "Mind if I let myself out the back?"
        hide D Neutral with dissolve
        "Since you're still mostly naked - and dripping fluids - you agree."
        "You dress, pocketing the card and the cash, and clean up hastily."
        "As you walk home, you smile to yourself, acutely aware of the fluid running down your thigh."
        $ Cash += 300
        hide chelsea with dissolve
        show bg black with fade
    jump events_end_period

label cafe_event8:
    show chelsea at right with moveinright
    "You walk into the cafe and head into the crew room."
    "Just as you begin lifting your shirt to change, you hear a voice."
    show EM Serious at left with dissolve
    "Emilia" "[pcname], I've been waiting for you."
    "Emilia" "Please, join me in my office."
    hide EM Serious with dissolve
    show chelsea happy
    "Lowering your shirt, you smile and follow her."
    if corruptkate:
        show K Casual Sad at left with dissolve
        "The first thing you notice is Kate. She's sitting in a chair with her face in her hands, sobbing."
        show chelsea confused
        pcname "Kate... what's the matter?"
    elif True:
        show K Casual Blank at left
        "The first thing you notice is Kate, sitting in a chair and looking everywhere but at you."
    show EM Serious with dissolve
    "Emilia" "[pcname], I've heard something very concerning about your performance here."
    show chelsea blank
    show EM Blank
    if club == "track":
        pcname "Is that so?"
    elif club == "cheer":
        pcname "I can't imagine what..."
    elif club == "yearbook":
        pcname "Y-you have?"
    "Emilia's lips purse as she watches you; she shakes her head."
    show EM Serious
    "Emilia" "Is it true that you've been serving our customers sexually?"
    show EM Blank
    if corruptkate:
        "You glance at Kate, but she doesn't lift her head."
    elif True:
        show chelsea confused
        "You glance at Kate. What could she have told Emilia?"
    if club == "track":
        pcname "Emilia, I wouldn't--"
    elif club == "cheer":
        pcname "Oh, come on, like I would--"
    elif club == "yearbook":
        pcname "I-- I've never--"
    "She raises a hand, halting your denial."
    show EM Serious
    "Emilia" "There is a witness, [pcname]."
    show chelsea blank
    if corruptkate:
        "Emilia" "Someone saw you and Kate fucking a customer in the dining area after hours."
    elif True:
        "Emilia" "Kate saw you fucking a customer in the dining area after hours."
    show EM Blank
    "She sighs, shaking her head."
    show EM Serious
    "Emilia" "I really can't tolerate this kind of behavior..."
    if corruptkate:
        "Emilia" "From either of you."
    "Emilia" "Tell me... Why shouldn't I fire you right now?"
    show EM Blank
    "Your mind whirls. You {i}need{/i} a job - you can't get fired!"
    "But you can't imagine what would excuse your behavior."
    "You could try begging, you suppose..."
    "And yet..."
    "That man, Daniel, offered you a job working at his bar."
    "It wouldn't be as nice as the maid cafe, but it would be {i}something{/i}..."
    menu cafe_scene8_quit:
        "Beg." if True:
            show chelsea sad
            $ corruption -= 10
            if club == "track":
                pcname "Emilia, please, I {i}need{/i} this job."
                pcname "I'm really sorry. I figured I could make extra money on the side, but I know it was wrong."
                pcname "{i}Please{/i} don't fire me."
            elif club == "cheer":
                pcname "I shouldn't have done it, I'm {i}so{/i} sorry, Emilia."
                pcname "I really need this job. Please, {i}please{/i} don't fire me!"
            elif club == "yearbook":
                pcname "I... I..."
                "Tears well up in your eyes."
                pcname "I just... needed the extra money."
                pcname "It won't happen again. I promise!"
            pcname "I--"
            show EM Serious
            "Emilia" "Enough, enough..."
            show EM Blank
            "She sighs again, rubbing her eyes."
            show EM Serious
            "Emilia" "Fine, I won't fire you."
            "Emilia" "But this is the {i}last{/i} chance you're getting. Understand?"
            show EM Blank
            pcname "Yes, Emilia."
            if corruptkate:
                show EM Serious
                "Emilia" "Both of you, go back to work."
                show EM Blank
                "Wiping her eyes, Kate stands."
                show K Casual Happy at left
                K "Th-thank you, Emilia."
                "Emilia waves you off, still shaking her head in disbelief."
                hide EM Blank with dissolve
                "Kate barely looks at you as you go about your shift; her eyes are still red, though she puts on a smile for the customers."
                "Ultimately, you just feel lucky to have a job."
                "You end your shift, resigned to stop flirting and meeting up with men."
                "While the extra money was nice, it's not worth losing your job over."
            elif True:
                show EM Serious
                "Emilia" "All right then. You can go back to work."
                show EM Blank
                "You stand, finally exhaling a breath you didn't know you were holding."
                show chelsea happy
                pcname "Thank you, Emilia."
                "Emilia waves you off, still shaking her head in disbelief."
                hide EM Blank with dissolve
                "You get changed and start your shift in a bit of a daze."
                "Ultimately, you just feel lucky to have a job."
                "By the end of your shift, you've resigned to stop flirting and meeting up with men."
                "While the extra money was nice, it's not worth losing your job over."
        "Quit." if True:

            $ job = "bar"
            "You shake your head in disbelief."
            pcname "I'm not going to {i}beg{/i} for my job, Emilia."
            pcname "Honestly, I was going to quit anyway. I have a {i}better{/i} job offer."
            "Emilia shakes her head."
            show EM Serious
            "Emilia" "Suit yourself; I'm not going to stop you."
            show EM Blank
            if corruptkate:
                "Kate stares at you, her eyes wide with shock."
                pcname "He offered you a job too, Kate."
                show K Casual Embarrassed at left
                "She bites her lip and nods."
                K "R-right! I'm quitting too!"
                show EM Serious
                "Emilia" "Kate... Don't let her drag you down with her."
                "Emilia" "You've been here for years and I've never had any trouble from you."
                "Emilia" "Once she's gone, I'm sure you'll be happier, you'll see."
                show EM Blank
                "Kate looks at you for a long moment."
                menu cafe_scene8_encouragekate:
                    "Come on, Kate." if True:
                        $ corruption += 1
                        show chelsea happy
                        K "[pcname] is my friend and we don't need this place."
                        "You smile."
                        "Emilia shakes her head again, her shoulders sinking."
                        show EM Serious
                        "Emilia" "Leave your uniforms in the crew room and go, then."
                        show EM Blank
                        "Kate marches out the door, leaving you trailing behind."
                        show EM Serious
                        "Emilia" "You're ruining her. I hope you know that."
                        if club == "track":
                            pcname "Kate can make her own choices."
                        elif club == "cheer":
                            pcname "She's learning to have some fun. There's nothing wrong with that."
                        elif club == "yearbook":
                            pcname "We're friends."
                        "Turning away, you walk into the crew room."
                        hide EM Serious with dissolve
                        "Grabbing your uniform, you drop it into a pile on the floor and walk out."
                        show bg CityD with dissolve
                        $ clothes, hair = casualwear
                        "Outside, Kate's waiting for you."
                        show K Casual Happy at left
                        K "I can't believe we did that!"
                        pcname "I know... Now, I need to call Daniel and get us new jobs!"
                    "Maybe she's right." if True:
                        $ corruption -= 1
                        show chelsea blank
                        show K Casual Blank at left
                        K "What? You don't want me to go with you?"
                        pcname "It was all my idea. Don't quit just because of me."
                        show K Casual Sad at left
                        K "But... I..."
                        show EM Serious
                        "Emilia" "Kate, you were happy here before this, and this behavior isn't like you at all."
                        show EM Blank
                        K "I... I know, I just..."
                        "Kate looks down."
                        K "[pcname], I'm scared. This was my first job and... I like it here."
                        show chelsea happy
                        pcname "You should stay, Kate. I'll be fine."
                        "Kate nods, still staring at the floor, unwilling to meet your eyes."
                        show chelsea blank
                        "You leave Emilia's office alone and you walk into the crew room."
                        hide EM Blank with dissolve
                        hide K Casual Sad with dissolve
                        "Grabbing your uniform, you drop it into a pile on the floor and walk out."
                        show bg black with dissolve
                        show bg CityD with dissolve
                        $ corruptkate = False
                        "You pull out your phone and his business card, dialing the number."
                        Dan "Cock and Crow, what can I do for ya?"
                        pcname "Is this Daniel Silver?"
                        Dan "Unless you're a bill collector. What do ya need?"
                        pcname "This is [pcname]. We met at Emilia's Maid Cafe?"
                        Dan "Red! How's it going?"
                        pcname "Well... I was hoping that job offer was still good."
                        Dan "Yeah, yeah, of course. Come down and I'll get you taken cafe of."
                        Dan "Uniform, schedule, and a quick tour. You can start tomorrow, if you want."
                        show chelsea happy
                        pcname "That would be great! I'll see you soon."
                        scene bg black with dissolve
                        jump events_end_period
            elif True:
                show EM Serious
                $ job = "bar"
                "Emilia" "Leave your uniform."
                show EM Blank
                "You leave Emilia's office alone and you walk into the crew room."
                hide EM Blank with dissolve
                "Grabbing your uniform, you drop it into a pile on the floor and walk out."
                "As you reach the front door, someone grabs your arm."
                show K Casual Blank at left with moveinleft
                K "[pcname], wait!"
                "You turn to stare at Kate, clutching your arm."
                K "I... I didn't think it would go like this!"
                K "I thought if I told Emilia, you'd change."
                K "You'd stop doing... those {i}things{/i} with those gross men..."
                "She shakes her head, as if denying everything that just happened."
                K "Come back. Tell Emilia you didn't mean it!"
                K "We... we were friends, weren't we?"
                "You shake your head."
                pcname "A friend would have talked to me, not told my boss."
                show K Casual Sad at left
                pcname "It's fine. It's better this way."
                "Kate's lower lip quivers; her eyes brim with tears."
                K "I'm s-sorry, I--"
                "You pull your arm from her grip."
                pcname "I was sick of this place anyway."
                pcname "Honestly, I'm kind of glad you told Emilia."
                K "But--"
                menu cafe_scene8_kateend:
                    "Have a good life, Kate." if True:
                        "You turn away as a tear trickles down her cheek."
                    "Maybe I'll see you around." if True:
                        "She nods, sniffling."
                        show chelsea happy
                        "You offer her one last smile and turn away."
            scene bg black with dissolve
            pause 1.0
            show bg CityD with dissolve
            show chelsea blank at right with moveinright
            if corruptkate:
                show K Casual Blank at left with moveinleft
            "Outside, you pull out your phone and his business card, dialing the number."
            Dan "Cock and Crow, what can I do for ya?"
            show chelsea confused
            pcname "Is this Daniel Silver?"
            Dan "Unless you're a bill collector. What do ya need?"
            show chelsea happy
            pcname "This is [pcname]. We met at Emilia's Maid Cafe?"
            Dan "Red! How's it going?"
            show chelsea embarrassed
            pcname "Well... I was hoping that job offer was still good."
            show chelsea happy
            Dan "Yeah, yeah, of course. Come down and I'll get you taken cafe of."
            if corruptkate:
                Dan "Your friend too?"
                pcname "Yeah, Kate too."
                Dan "Even better. Stop down and I'll get you girls some uniforms and a schedule."
                pcname "That would be great! I'll see you soon."
                "You hang up, smiling."
                K "Well?"
                pcname "Let's head to the Cock and Crow and get our new uniforms."
                show K Casual Laugh at left
                K "Yes! This is going to be great, [pcname]!"
            elif True:
                Dan "Uniform, schedule, and a quick tour. You can start tomorrow, if you want."
                pcname "That would be great! I'll see you soon."
    scene bg black with dissolve
    jump events_end_period

label cafe_raise:
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    show bg Cafe with dissolve
    "You enter the cafe and go about your usual routing; heading into the locker room to get dressed."
    "You haven't been here very long, but with everything that has happened it feels as though you been working here for months."
    hide chelsea with dissolve
    show bg black with dissolve
    $ clothes = 'cafe'
    show bg Cafe with dissolve
    show EM Blank with dissolve
    show chelsea confused at right with moveinright
    "As you begin to leave the locker room you're stopped by Emilia who blocks the exit."
    show chelsea blank
    "Emilia" "Hey, [pcname]. How have you enjoyed being a maid these past few weeks?"
    menu maidfeelings:
        "It's been fun!" if True:
            show chelsea happy
            show EM Happy
            "Emilia" "Glad to hear it! That sort of enthusiasm is a bit of why I'm here."
        "Defintely a unique experience." if True:
            "Emilia" "True. It's a one of a kind experience in all of Uni!"
        "It pays the bills." if True:
            "Emilia" "I understand. Can't eat without making money."
    show EM Serious
    show chelsea blank
    "Emilia" "You've been a hard worker here and I wanted to reward you for that."
    show chelsea shocked
    pcname "Wait, do you mean..?"
    show EM Happy
    "Emilia" "Yep! [pcname], I'm giving you a raise. Enjoy it."
    pcname "Wow, thank you!"
    "Emilia" "Just keep doing your best. That's all I ask."
    hide EM Happy with dissolve
    show chelsea happy
    "With that Emilia turns around and heads back to her office. At least now you should be able to spend more than usual!"
    $ caferaise = True
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
