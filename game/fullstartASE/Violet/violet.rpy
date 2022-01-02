label violetlunch1:
    $ violetscenes += 1
    show bg Cafeteria with fade
    "At lunch, you sit at your usual table with Violet."
    show chelsea at right with moveinright
    show V School Blank at left with moveinleft
    "The two of you are chatting away amicably - until Violet suddenly scrunches her face and gags."
    "At first you think it might be the food, but then she looks away."
    show V School Pout at left
    V "Ew, look who it is!"
    "Following her gaze across the crowded room, you find the person she's talking about..."
    "Matt."
    V "That guy is such a creep!"
    if mattsubmissive == True and mattblackmail == False:
        pcname "He doesn't seem too bad..."
        show V School Blank at left
        V "You're entitled to your opinion."
        "She turns back to you, shaking her head."
        show V School Annoyed at left
        V "He thinks he's something special, but I really don't know why."
        "You glance in his direction again; he doesn't seem to have noticed you."
    elif mattslap > 0:
        show chelsea happy
        pcname "He's left me alone since I slapped him."
        "Laughing, Violet turns back toward you."
        show V School Smile at left
        V "That was seriously the best thing I've ever seen."
    elif gangrape == True:
        "A cold chill sweeps through your body, taking root in the pit of your stomach."
        pcname "I... don't want to talk about him..."
        "She quirks a brow."
        show V School Blank at left
        V "You don't {i}like{/i} him, do you?"
        "You shake your head profusely."
        pcname "N-No; it's nothing like that."
    elif True:
        if club == "track":
            pcname "Yeah, I'm not a fan."
        elif club == "cheer":
            pcname "Yeah, he seems pretty gross..."
        elif club == "yearbook":
            pcname "I... don't really like him..."
        show V School Annoyed at left
        V "He's honestly the {i}worst{/i}!"
    V "Hey, let's not let him ruin our appetites."
    show V School Smile at left
    V "I think I was telling you about my new shoes..."
    "Turning your attention back to your food, you listen idly while she resumes a {i}fascinating{/i} story about the clothes she bought last weekend."
    jump events_end_period

label violetlunch2:
    $ violetscenes += 1
    show bg Cafeteria with fade
    show chelsea at right with moveinright
    show V School Blank at left with moveinleft
    "The morning goes by quickly, and before you know it you're sitting down at your regular lunch table."
    show V School Smile at left
    V "You know, [pcname], I've been thinking about getting a part-time job."
    V "You have one, right?"
    show chelsea happy
    pcname "Yeah, I work at a [job]."
    V "Really? A [job]?"
    V "Do you like it?"
    if job == "cafe":
        menu violetlunch2cafe:
            "I like my coworkers." if True:
                show V School Blank at left
                V "Well, that doesn't sound too bad..."
            "More tips would be nice..." if cafepanties == False:
                show V School Pout at left
                V "Ugh, you get paid in tips?"
            "I make really good tips!" if cafepanties == True:
                V "Really? Hmmm..."
            "I {i}always{/i} satisfy my customers..." if cafeblowjob == True:
                show V School Annoyed at left
                V "Ugh, that sounds like too much work..."
    if job == "bakery":
        menu violetlunch2bakery:
            "My manager is really mean..." if bakerychain == 2:
                show V School Annoyed at left
                V "I wouldn't put up with that; I'd just quit!"
            "The customers are pretty rude." if True:
                show V School Annoyed at left
                V "That sounds like the worst!"
            "I'm getting better at it now." if bakerychain == 3:
                show V School Blank at left
                V "Oh? Were you really bad at first?"
                pcname "My manager had to correct me a lot..."
            "A job's a job!" if True:
                show V School Pout at left
                V "I guess that's true...?"
    show V School Blank at left
    V "Actually, now that I think about it..."
    V "I don't really want one. It sounds like too much work."
    show chelsea blank
    pcname "Isn't that kind of the point?"
    show V School Smile at left
    "Violet laughs."
    V "I'll just have to get my parents to up my allowance."
    if job == "cafe":
        show V School Pout at left
        V "I mean, there's no way I'm begging for tips!"
    elif job == "bakery":
        show V School Annoyed at left
        V "I couldn't put up with rude customers, after all!"
    menu violetlunchconfront:
        "Some of us don't have a choice." if True:
            "She glances your way and slowly shakes her head."
            show V School Smile at left
            V "True. But I do!"
        "I guess that's fair..." if True:
            show V School Blank at left
            "She nods, looking thoughtful."
    V "Now, how can I convince them..."
    V "I could threaten to tell my mom about my dad's affair, but I was trying to hold onto that to get a new car..."
    "Shaking your head, you let her scheme while you finish your meal."
    jump events_end_period

label violetlunchoption1:
    show bg Cafeteria with fade
    show chelsea at right with moveinright
    show V School Smile at left with moveinleft
    "You're sitting with Violet at lunch when she suddenly starts laughing."
    show chelsea confused
    pcname "What's so funny?"
    V "Someone just tripped that guy over there."
    "She points across the cafeteria and you turn to look."
    show chelsea blank
    "It's Damien."
    menu violetlunchoption1react:
        "That's my friend!" if damienevents > 2:
            show chelsea angry
            show V School Suprised at left
            V "Seriously? Sorry about your luck, then."
            show chelsea happy
            pcname "He's a really nice guy."
            show V School Pout at left
            V "Yeah... I'm sure."
            show chelsea blank
            pcname "No, he really is. I hope he's okay..."
            "Violet rolls her eyes."
        "I helped him out the other day..." if bullytelloff > 0:
            show V School Smile at left
            V "Looks like he needs all the help he can get."
            V "There's no way I'd ever waste time on someone who can't take charge."
            "She glances your way with a mischievous smirk."
            V "You know?"
        "What a loser..." if True:
            show V School Smile at left
            V "Definitely."
            V "I prefer someone a little more... bold."
        "I have a story to tell you about him!" if damientelloff == True:
            show V School Smile at left
            V "Oh? Sounds juicy!"
            show chelsea happy
            pcname "I actually hung out with him for a little while..."
            show V School Suprised at left
            V "Ew, {i}really{/i}?"
            "You shrug."
            if club == "track":
                show chelsea blank
                pcname "I didn't know many people yet and I was bored."
                show V School Blank at left
                pcname "Anyway, we went to the movies and I was feeling a little frisky..."
                show V School Suprised at left
                V "Oh! You {i}didn't!{/i}"
                "Shrugging, you continue."
                show chelsea happy
                pcname "So I reached over and gave him a handjob."
                show V School Smile at left
                V "Oh. My. God..."
                show chelsea angry
                pcname "He didn't argue at the time, but when we get back to my place..."
                pcname "He had the nerve to {i}lecture{/i} me about how he didn't think I was \"that kind of girl\"!"
            elif club == "cheer":
                show chelsea blank
                pcname "I didn't know many people yet and I was bored."
                show V School Blank at left
                pcname "Anyway, we went to the movies and I wasn't really into it, so I thought I'd have some fun..."
                show V School Suprised at left
                V "Oh! You {i}didn't!{/i}"
                "Laughing, you continue."
                show chelsea happy
                pcname "So I reach over and give him the best handjob he's ever had - which I can almost guarantee, since I think it was his first!"
                show V School Smile at left
                V "Oh. My. God..."
                show chelsea angry
                pcname "And then, when we get back to my place, he has the nerve to {i}lecture{/i} me about how he didn't think I was \"that kind of girl\" or something!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I didn't know many people yet and I thought he was nice..."
                show V School Blank at left
                pcname "So we went to the movies and I wanted to impress him..."
                show V School Suprised at left
                V "You are {i}too{/i} nice..."
                "Smiling a little, you continue."
                show chelsea happy
                pcname "So I reached over and... touched him."
                show V School Smile at left
                V "Oh. My. God..."
                show chelsea sad
                pcname "And... when we get back to my place... he was mad at me!"
                pcname "He thought I was... I don't know... Slutty or something?"
            V "What an idiot!"
    show chelsea blank
    show V School Blank at left
    V "Oh! I almost forgot to tell you!"
    show chelsea confused
    pcname "Tell me what?"
    V "Did you hear that Avery is {i}pregnant{/i}!?"
    "You're not sure who Avery is, but you let her tell the story anyway."
    "It seems to go on forever, and by the time Violet's finished, so is lunch."
    jump events_end_period

label violetwork1:
    $ violetscenes += 1
    if job == "bakery":
        "You're working the register when you hear the door open."
        show chelsea happy at right with moveinright
        pcname "Hi, how can I--"
        "Violet approaches the counter."
        show V Casual Blank at left with moveinleft
        V "Wow, that outfit is..."
        show V Casual Pout at left
        "She looks you up and down."
        if bakerychain > 1:
            show V Casual Suprised at left
            "Her eyes widen when she sees your breasts; clearly, the push-up bra is doing its job!"
        show V Casual Blank at left
        V "It looks really good on you, but I don't think it would suit someone like me."
        pcname "Um... thanks?"
        show V Casual Smile at left
        V "So... What's good here?"
        menu violetwork1bakerysuggestion:
            "Baguettes." if True:
                pcname "The sweets are good, but honestly? The baguettes are the best!"
                show V Casual Pout at left
                V "Just... bread?"
                pcname "They're really versatile! You can toast them, dip them in soup, or--"
                show V Casual Blank at left
                V "Yeah... I think I'll get some cookies."
            "Cookies." if True:
                pass
            "Tarts." if True:
                pcname "You should try our fruit tarts. We make them with fresh, organic fruit and--"
                show V Casual Blank at left
                V "Actually, I'll just get some cookies."
        pcname "We make some {i}amazing{/i} cookies. The salted caramel are my favorite!"
        show V Casual Smile at left
        V "Hmmm... That {i}does{/i} sound good. And I'll have a white chocolate macadamia nut one too."
        "You carefully bag her cookies and lay them on the counter."
        V "This doesn't seem so bad. At least it smells good in here."
        V "Be careful not to eat too much, though. You'll be a whale."
        show chelsea laugh
        "You laugh. She swipes a credit card and presses a few buttons when you tell her the total."
        show chelsea happy
        pcname "Everything is really good here, so it's {i}really{/i} tempting."
        "You pass her the receipt and her bag."
        pcname "There you go, can I--"
        show V Casual Pout at left
        show chelsea shocked
        "You're interrupted by a voice from the back."
        BM "[pcname]! Where did you put the new pans!?"
        show chelsea blank
        show V Casual Annoyed at left
        V "Wow, what a dick."
        if club == "track":
            pcname "I know, right? But he's the boss..."
        elif club == "cheer":
            "You can't help but giggle."
        elif club == "yearbook":
            pcname "Shhh. I gotta go..."
        show V Casual Blank at left
        V "I guess I'll see you at school. Good luck with that asshole."
        "Glancing toward the back, you give her a quick smile and wave goodbye."
    elif job == "cafe":
        "You're waiting tables when Kate approaches you."
        if katerelate == "friend":
            show K Blank at left with moveinleft
            show chelsea at right with moveinright
            K "Hey, [pcname], there's a girl requesting you as her server."
            if corruptkate:
                K "She looks kind of prissy..."
            pcname "Thanks, I'll take care of her in a minute."
            hide K Blank with moveoutleft
            if corruptkate:
                show K Laugh at left
                K "I bet you will!"
                "She giggles as she walks away."
                hide K Laugh
            pcname "Huh... We don't get many female customers. I wonder who it is?"
        if katerelate == "enemy":
            show K Blank at left with moveinleft
            show chelsea at right with moveinright
            K "There's a girl requesting you as her server."
            pcname "Oh?"
            show K Mad at left
            K "I doubt you can flirt your way into a big tip with this one, so good luck I guess."
            "Rolling your eyes, you head to see who it is."
            hide K Mad
        if katerelate == "girlfriend":
            show K Embarrassed at left with moveinleft
            show chelsea at right with moveinright
            K "Um, [pcname]? There's a girl asking for you to wait on her..."
            "She looks down."
            show chelsea confused
            pcname "Me?"
            show K Blank at left
            K "Yeah. She asked for you by name."
            "Kate walks away, clearly bothered by this newcomer."
            pcname "Who in the world..."
            hide K Blank
        show chelsea happy
        "When you approach the table... it's Violet!"
        show V Casual Smile at left with moveinleft
        V "Wow, look at you!"
        "She gives you a full once-over."
        if cafeshirt >= 4:
            V "I think you missed a few buttons!"
        V "That maid outfit looks good on you, but I don't think it would suit {i}me{/i}."
        show chelsea confused
        pcname "Thanks... I think."
        show V Casual Blank at left
        show chelsea blank
        V "There are a lot of guys here, aren't there?"
        pcname "Yeah, we get a lot of male customers - but there are plenty of girls too."
        if katerelate == "girlfriend":
            show V Casual Pout at left
            V "You know, that other maid girl keeps looking at us."
            "She points across the room to where Kate stands, blushing profusely and trying to look busy."
            show chelsea happy
            pcname "That's Kate. She's amazing..."
            V "At staring, maybe."
        V "So do you make a lot in tips?"
        if tipweight == 0:
            pcname "Not really, but it's still a nice place to work."
        elif tipweight == 1:
            pcname "I think I do alright."
        elif tipweight > 1:
            pcname "I make the highest tips of anyone here!"
        show V Casual Pout at left
        V "But that outfit..."
        "She shakes her head."
        V "A school uniform is bad enough. I can't {i}stand{/i} wearing the same clothes as everyone else."
        pcname "It's not so bad..."
        "Violet rolls her eyes and looks at the menu."
        V "I guess I'll have a tall caramel latte. Iced, almond milk, extra foam, and add whipped cream."
        "You scribble her order down as quickly as she rattles it off."
        show chelsea happy
        pcname "Sounds good! I'll bring that right out to you."
        show V Casual Smile at left
        V "Oh, I'll have it to go. I just wanted to stop by and see you."
        pcname "Oh! Well... thanks."
        V "Oh, and light on the ice; I want it cold, but not watered down."
        pcname "Right..."
        "You quickly make her drink, then deliver it."
        show V Casual Blank at left
        V "Oh, here... Keep the change."
        "She tosses some bills on the table."
        V "I guess I'll see you at school."
        pcname "Sure! Thanks for stopping by!"
        "You pick up the money and count it out. She left you a $10 tip!"
        hide V Casual Blank with dissolve
        hide chelsea with dissolve
        $ tips += 10
    scene bg black with dissolve
    jump events_end_period

label violetlunch3:
    show bg Cafeteria with fade
    $ violetscenes += 1
    $ violetdate = True
    show chelsea at right with moveinright
    "By the time you make it to lunch, you're ready to go home for the day..."
    "It only gets worse, though, when you discover they've run out of pizza and are serving fish sticks instead."
    "As you take your seat across from Violet, she grimaces."
    show V School Blank at left with moveinleft
    V "Ew, you got fish sticks?"
    "She has two slices of pizza on her plate."
    pcname "Yeah... They ran out of pizza."
    V "Oh, that sucks!"
    "She takes a big bite of her slice. Sighing, you pick up a fish stick."
    V "So, I was thinking, [pcname]... We never hang out."
    show chelsea confused
    pcname "What? We sit together every day!"
    "Violet rolls her eyes."
    V "Well, yeah - but we never do anything together {i}outside{/i} of school."
    V "Why don't we do something this weekend?"
    show chelsea blank
    menu violetlunch3plans:
        "You could come over to my place..." if True:
            show chelsea happy
            $ violetdate1place = "apartment"
            V "Are you sure your parents won't mind?"
            pcname "No, they--"
            pcname "I have my own apartment."
            show V School Suprised at left
            V "What!?"
            V "Why didn't you tell me that sooner?"
            show chelsea blank
            pcname "I don't know... It never came up?"
            show V School Smile at left
            V "Text me your address and I'll be there Saturday evening!"
            call screen TextingScene("Violet",
            [
                TextMessage("2237 Westwood Ave", sender = False),
                TextMessage("thx!! <3")
            ])
        "We could go out to eat?" if True:
            $ violetdate1place = "restaurant"
            $ violetdateflag = True
            V "Yeah, that'll do, I guess."
            show chelsea happy
            pcname "Anywhere you want to try?"
            show V School Smile at left
            V "Oh, we should go to that new Italian place!"
            V "It's called \"Chiaro di Luna\". It's supposed to be {i}amazing{/i}."
            pcname "Well, \"amazing\" sounds good to me!"
            V "Let's meet there Saturday evening, okay?"
            pcname "Sounds good to me!"
    "Violet stands and picks up her tray. There's still an untouched slice of pizza on it."
    show V School Blank at left
    V "Guess I shouldn't have bought an extra piece, huh?"
    "Before you can respond, she heads off to the trash cans."
    show chelsea blank
    if club == "track":
        pcname "Ugh, she can be so self-absorbed sometimes!"
        pcname "But she's a good friend, I guess..."
    elif club == "cheer":
        pcname "Ugh, she can be such a bitch sometimes!"
        pcname "But it's not her fault, I guess..."
    elif club == "yearbook":
        pcname "She's... not very nice, sometimes..."
        pcname "But... at least she wants to be friends, I guess..."
    jump events_end_period

label violetdate1apart:
    show bg HomeD
    $ violetscenes += 1
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "As you slip your shoes on, you remember that Violet is supposed to be coming over this evening."
    "Looking around your apartment, you see a few things you'd like to clean before she arrives."
    "You start by folding the laundry you'd left piled up on a chair, then you move on to the bathroom."
    "Later - as you finish drying the dishes - there's a knock on your door."
    show chelsea happy
    pcname "Be right there!"
    show chelsea blank
    show V Casual Smile at left with moveinleft
    "You open the door to find Violet with a suitcase and matching tote."
    pcname "What's all that?"
    V "What do you mean?"
    pcname "The... bags?"
    show V Casual Blank at left
    "She brushes past you, leaving her suitcase in the hallway."
    V "Well, how else am I supposed to pack for a sleep-over?"
    "Clearly making herself at home, she wanders around the apartment while you bring her luggage inside."
    V "It's... kinda small, don't you think?"
    pcname "It's just me, so..."
    V "Yeah! How did you {i}ever{/i} convince your parents to let you get your own place?"
    menu violetdate1apartparents:
        "Tell the truth..." if True:
            show chelsea sad
            pcname "Um... actually..."
            show V Casual Smile at left
            V "I knew it! It's not really just you here, is it?"
            pcname "That's not..."
            "Taking a deep breath, you tell her the truth."
            pcname "My parents died in a car accident; that's why I moved here."
            show V Casual Suprised at left
            V "Oh!"
            show V Casual Pout at left
            "For once, she actually looks concerned."
            V "I... had no idea. I'm sorry, [pcname]."
            pcname "It's fine. Really, I... Let's just talk about something else, okay?"
        "Avoid the question." if True:
            "You shrug and quickly change the subject."
            show chelsea happy
            pcname "So what do you want to do?"
    show V Casual Blank at left
    V "Well, it doesn't look like there's much to do here..."
    V "I {i}guess{/i} we could stream a movie or something."
    show chelsea happy
    pcname "Sure. Make yourself at home and I'll grab some popcorn."
    hide V Casual Blank with moveoutleft
    "Without hesitation, Violet flops onto the couch and picks up the remote."
    "While she flips through the options, you toss a bag of popcorn into the microwave."
    show chelsea blank
    V "I guess you have the really basic cable package, huh?"
    if club == "track":
        pcname "I don't have much time for TV, really."
    elif club == "cheer":
        pcname "I'm not home much, so..."
    elif club == "yearbook":
        pcname "I don't watch much TV, honestly."
    V "Guess not. Hmmmm..."
    "The microwave {i}dings{/i} and you pull the popcorn out, then empty the bag into a large bowl."
    "Food in hand, you join Violet on the couch. She's flipping through the new releases on Hizorflix."
    V "Well, I guess this will have to do..."
    hide V Casual Blank
    hide chelsea with dissolve
    show bg VFlix with fade
    "She settles on a romantic comedy about twin sisters who accidentally start dating the same guy."
    "Near the middle of the movie - just as the two sisters discover the mix-up - Violet leans against you, resting her cheek on your shoulder."
    if club == "track":
        "It's silly, but... Having her cuddled against you makes you feel strong and important."
    elif club == "cheer":
        "The contact makes you even more aware of how pretty she is..."
    elif club == "yearbook":
        "Her closeness makes you nervous, but... you kind of like it too?"
    "She stays like that until the film ends. Then, standing and stretching, she yawns."
    show bg HomeE with dissolve
    show V Casual Blank at left with moveinleft
    V "I guess it's getting late..."
    V "I brought some spa supplies - wanna put on face masks and relax?"
    show chelsea at right with moveinright
    menu violetdate1apartspa:
        "Sounds like fun!" if True:
            if club == "track":
                "You're not usually into face masks and stuff, but it might be nice to relax..."
            elif club == "cheer":
                "You're sure she's brought some expensive stuff!"
            elif club == "yearbook":
                "You don't want to disagree when you're getting along so well..."
            show chelsea happy
            show V Casual Smile at left
            V "Awesome!"
            "She digs through her tote, only to produce a variety of jars and tubes."
            V "This one is a facial cleanser; we'll start with that."
            hide chelsea with dissolve
            hide V Casual Smile with dissolve
            show bg black with dissolve
            "Leading the way to the bathroom, you grab two towels."
            show bg VSpa1 with dissolve
            V "Wash your face and pat it dry, then we'll put on the masks."
            "You do as she instructs; the facial cleanser smells pleasantly of fruit."
            "As you dab the towel against your face, Violet passes you a jar."
            V "That's a clay mask. It's best for... oily skin."
            "You notice that she watches your reaction closely - almost as if she wants to see if her veiled insult bothers you."
            "Instead of saying anything, you take the jar and look over the label."
            V "Just smear it around and wait for it to dry. It's not difficult."
            "Again, she seems to be trying to goad you. When you don't react, she begins applying her own mask."
            "Just as you finish applying it, you hear her gasp."
            "Glancing over, you see that she's gotten some of the strange goo on her shirt."
            V "No, no, no! This is my favorite outfit!"
            show bg VSpa2 with dissolve
            "Without warning, she unbuttons the shirt and tosses it in the sink."
            if club == "track":
                "You're used to seeing other girls change, but..."
            elif club == "cheer":
                "After her earlier comments, you wonder if karma is on your side. And..."
            elif club == "yearbook":
                "You divert your eyes, trying not to look, but..."
            "You can't help but notice how her breasts almost bounce out of her lacy, black bra as she scrubs the stain from her top."
            V "{i}Phew!{/i} I think I got it off in time..."
            "She looks down at herself, only now realizing she's topless."
            V "I guess I'll have to wait until I wash the mask off to put a new shirt on..."
            "Glancing at you, she pokes one of her breasts."
            V "Do you think my bra fits right?"
            if club == "track":
                pcname "Huh?"
            elif club == "cheer":
                pcname "What?"
            elif club == "yearbook":
                pcname "I... W-What?"
            V "Do you think they look alright? I read somewhere that most girls don't buy the right size..."
            "Your eyes are drawn down to her breasts, which bulge against her bra. It barely holds them; you can almost see the edge of her nipples."
            menu violetdate1apartbra:
                "It looks great!" if True:
                    "She smiles."
                    V "Thanks. I'm glad you like them."
                "I wouldn't know." if True:
                    "She pouts."
                    V "But do they look okay?"
                    pcname "I guess?"
            menu violetdate1apartboobs:
                "They're really nice." if True:
                    "She glances down at yours."
                    V "Yours aren't bad either."
                "I guess so?" if True:
                    V "{i}Tsk{/i}, you really don't know how to pay a compliment, do you?"
            "Turning back toward the mirror, Violet taps her face mask."
            V "I think mine's about dry. How's yours?"
            show bg VSpa3 with dissolve
            "Before you can answer, she leans toward you. Your eyes dart down to her breasts again."
            "She runs her finger down the edge of your jaw and taps it against your chin."
            V "Yep, looks like you're about ready too."
            pcname "I--"
            V "Now we wash them off. Just make sure you don't rub your face afterwards - just dab it with the towel."
            "She washes her face clean and presses the towel to it, stepping away from the sink so that you can do the same."
            show bg black with dissolve
            "Once you're both out of the bathroom, she looks around."
            show bg HomeN with dissolve
            show V Casual Smile at left with moveinleft
            show chelsea with moveinright
            V "Much better! Now..."
        "Actually, I'm pretty tired..." if True:
            show V Casual Pout at left
            "Violet pouts."
            V "You're no fun. Fine..."
            show V Casual Blank at left
    V "Where's the guest room?"
    pcname "Oh, um... This is just a one-bedroom apartment, so..."
    show V Casual Suprised at left
    V "You don't have a guest room!?"
    menu violetdate1apartbed:
        "Offer to sleep on the couch." if True:
            show V Casual Blank at left
            V "I mean, obviously you should offer but..."
            V "How big is the bed? Maybe we could just share it?"
        "Offer her the couch." if True:
            V "The {i}couch{/i}!?"
            "She folds her arms over her chest."
            show V Casual Blank at left
            V "Can't we at least share the bed!?"
    menu violetdate1apartbed2:
        "We can try." if True:
            hide chelsea
            hide V Casual Blank
            show bg black with dissolve
            V "Perfect. Just let me change into my night-clothes then!"
            "Grabbing her bag, she slips inside and closes the bedroom door behind her."
            "A few minutes later, the door swings open and Violet steps out wearing a long, silky nightshirt."
            "Her nipples press against the thin fabric, drawing your gaze and making it obvious that she's wearing nothing underneath."
            V "Ready for bed?"
            pcname "Uh... yes..."
            "Heat floods your face; you can't help but imagine her body pressed against yours with nothing but that thin shirt between you."
            V "What are you wearing to bed?"
            pcname "I... usually sleep naked."
            "She giggles."
            V "Well, that would be awkward, wouldn't it?"
            "You're not sure it would make much of a difference, considering what she's wearing - but you keep that to yourself."
            pcname "I have shorts and a tank top I can wear."
            "Pulling them from your dresser, you hurry to the bathroom and change."
            "By the time you return to the bedroom, Violet is already laying in bed."
            V "It's a little chilly in here. Hurry up!"
            show bg Sleep1 with dissolve
            "Slipping in beside her, you pull the blankets up."
            V "Mmm, you're warm!"
            "She cuddles up against you, pressing her body tight to yours."
            show bg Sleep2 with dissolve
            "After a minute, Violet drapes an arm over your chest and presses her face into your shoulder."
            "The contact makes you flush all over, filling you with an unexpected heat."
            V "Much better... This feels nice..."
            "You're {i}incredibly{/i} aware of how soft and warm she is, but she seems oblivious."
            if club == "track":
                "Doesn't she realize how this seems?"
            elif club == "cheer":
                "Is she... coming onto you?"
            elif club == "yearbook":
                "You flush, wondering how either of you could sleep like this..."
            show bg Sleep3 with dissolve
            "Minutes later, though, she's asleep. It takes you {i}much{/i} longer."
            show bg black with dissolve
        "I'll sleep on the couch." if True:
            V "Suit yourself..."
            "Sauntering into the bedroom, she closes the door behind her."
            "You settle in on the couch, anticipating a long, restless night."
            hide chelsea
            hide V Casual Blank
            show bg black with fade
            pause
            show bg HomeE
    if skippedschool:
        if havehomework:
            $ intelligence -= 5
        $ intelligence -= 1
    $ acts = 4
    $ day += 1
    $ daycount += 1
    $ skippedwork = False
    $ skippedschool = False
    $ wenttoschool = False
    $ wenttowork = False
    $ wenttoclub = False
    $ goingto = ""
    call events_end_day from _call_events_end_day_1
    call dayeval from _call_dayeval_2
    show bg RoomE with dissolve
    "In the morning, you wake up with a start."
    "The bed is empty; it seems Violet woke up early and let herself out."
    "As you make yourself breakfast, you find a note."
    "{i}Forgot I had a hair appointment. Had to run, but we should do that again sometime.{/i}"
    pcname "She's constantly forgetting things..."

    jump newday

label violetdate1rest:
    $ violetscenes += 1
    $ violetdateflag = False
    $ clothes, hair = casualwear
    "Looking at your phone, you realize that it's almost time to meet Violet for dinner."
    "You type the address into your phone and head to the restaurant."
    show bg black with dissolve
    pause 0.5
    show bg CityD with dissolve
    show chelsea at right with moveinright
    pcname "\"Chiaro di Luna\", huh? Sounds expensive..."
    "As soon as you see the building, you know that you were right."
    "Feeling a little intimidated, you enter the building and look around."
    show bg DatePlace with dissolve
    "The place is immaculate and the decor looks like it costs a small fortune."
    "Hostess" "Welcome to \"Chiaro di Luna\". Will you be dining alone this evening?"
    "Her face remains impassive, but you get the feeling you're underdressed."
    pcname "I'm meeting a friend here. We, uh... don't have a reservation or anything, though."
    "Hostess" "I see. Would you like to wait in the lobby or would you like me to seat you?"
    pcname "I guess... I'll sit down?"
    "Hostess" "Excellent. Right this way."
    "She gestures for you to follow her through the entryway and leads you to a small table for two."
    "Hostess" "Your server will be with you momentarily."
    "Even more intimidated now that you've seen the inside, you nervously glance around."
    "The waitress fills a glass with water and tells you the specials; they're all in Italian, so you have no idea what they really are."
    pcname "I'm actually waiting for someone..."
    "Waitress" "My apologies. I'll check back with you in a few minutes then."
    "When she returns a few minutes later, Violet still isn't there."
    "Waitress" "Still waiting?"
    "Your discomfort has only grown, but you try to put on a smile."
    show chelsea happy
    pcname "She'll be here soon, I'm sure."
    "Waitress" "Of course."
    show chelsea angry
    "Finally, Violet shows up - almost 20 minutes late!"
    hide chelsea with dissolve
    show bg VDScene1 with dissolve
    V "Sorry, sorry..."
    "She sits down, gesturing for the waitress to fill her glass with water."
    V "I completely forgot I'd already made plans with some guy in my study hall! I had to bail on him."
    show chelsea shocked with dissolve
    if club == "track":
        pcname "You cancelled your plans with him?"
        V "More or less..."
    elif club == "cheer":
        pcname "Aww, you picked me over him? I hope he wasn't too upset."
        V "Oh, I don't know..."
    elif club == "yearbook":
        pcname "I hope he wasn't upset..."
        V "I wouldn't know."
    "She laughs."
    show chelsea blank
    V "He's been texting me all day and I haven't bothered to respond. He'll get the hint."
    menu violetdate1restguy:
        "That's kind of rude..." if True:
            show bg VDScene2 with dissolve
            "She frowns."
            V "Would you rather I left to see him?"
            pcname "N-No..."
            V "I thought so."
        "I'm glad you didn't cancel on me." if True:
            show chelsea happy
            V "Of course!"
    V "Besides... he wasn't really worth my time."
    V "The only reason I agreed to go out with him is because he offered to pay - and we were going somewhere {i}really{/i} expensive."
    V "I figured if he wanted to buy me dinner, why not?"
    "Her expression turns playful."
    show bg VDScene3 with dissolve
    V "You know, if you wanted to pay for my meal we could consider {i}this{/i} a date."
    show chelsea embarrassed
    menu violetdate1restdate:
        "What? No!" if True:
            pass
        "If you want to..." if True:
            pass
    "Before you can answer, she laughs."
    V "You should see your face!"
    "Waitress" "Pardon me, ladies, but were you ready to order?"
    show bg VDScene1 with dissolve
    show chelsea blank
    V "Do you know what you want?"
    "You glance down at the menu again, but you really have no idea what anything is."
    pcname "Umm... What do you think?"
    show bg VDScene3 with dissolve
    "With a dismissive wave of her hand, Violet orders for both of you."
    V "I'll have the {i}Strangozzi al Tartufo Nero{/i} with extra grated truffle. And she'll have..."
    V "The {i}Paglia e Fieno{/i}, I think. Does that sound good to you?"
    if club == "track":
        pcname "Whatever you say!"
    elif club == "cheer":
        pcname "That sounds perfect!"
    elif club == "yearbook":
        pcname "Uh... sure?"
    "Waitress" "Excellent choices."
    "As the waitress walks away, Violet leans toward you."
    V "Don't you feel more important when your meal has such an impressive name?"
    menu violetdate1restimport:
        "Kind of..." if True:
            show chelsea happy
            V "I thought so."
        "I don't know what any of that meant!" if True:
            "She laughs."
            V "Oh [pcname]... You really are uncultured, aren't you?"
    show chelsea blank
    "Your meal is brought out in several courses. It's all very good, but to you it's still just pasta."
    show bg VDScene1 with dissolve
    V "So, I've been wondering, [pcname]..."
    V "Is there anyone you're interested in?"
    menu violetdate1restinterest:
        "Matt." if mattsubmissive == True:
            V "Ew, that creep? How embarrassing..."
        "Damien." if damienevents > 2:
            show bg VDScene2 with dissolve
            V "But he's so... boring!"
        "Someone at work..." if katerelate == "love" or bakerychain > 2:
            if job == "cafe":
                V "It's that girl I saw, right? The little blonde?"
                pcname "I--"
                show bg VDScene2 with dissolve
                V "She was {i}so{/i} annoying though..."
            elif job == "bakery":
                V "Really?"
                "She rolls her eyes."
        "It's Violet!" if True:
            pcname "Just you..."
            show bg VDScene3 with dissolve
            V "Me?"
            "She laughs, holding a hand to her chest."
            V "Oh, that's a good one!"
        "I don't have time for that." if True:
            show bg VDScene2 with dissolve
            "She shakes her head in disappointment."
            V "That's just a lie lonely people tell themselves to feel better..."
    show bg VDScene1 with dissolve
    "You chat a little while longer as you finish your meals, and then the waitress brings your checks."
    V "Oh no! I'm so forgetful!"
    "Violet rummages through her clutch briefly before smiling at you."
    show bg VDScene3 with dissolve
    V "I was in such a rush that I forgot my cards..."
    V "You don't mind covering mine, right?"
    show chelsea confused
    menu violetdate1restpay:
        "Of course I mind!" if True:
            show chelsea shocked
            if club == "track":
                pcname "This place is {i}really{/i} expensive!"
            elif club == "cheer":
                pcname "I can't believe this!"
            elif club == "yearbook":
                pcname "I-I don't..."
            show bg VDScene1 with dissolve
            "She pouts and passes you her bill anyway."
            V "I'm sorry! I didn't mean to leave my cards at home..."
        "I guess not..." if True:
            V "I knew you wouldn't. I owe you one!"
            "She winks as she passes you her bill."
    if Cash > 98:
        "You put your money inside the billfold and lay it on the table."
        "It's a lot of money, but at least you can afford it."
        $ Cash = Cash - 98
    elif Cash < 98:
        show chelsea shocked
        pcname "I don't even {i}have{/i}--"
        "Violet's phone rings."
        V "Sorry, I have to take this. I'll see you tomorrow!"
        hide V Casual Smile with moveoutleft
        hide V Casual Pout with moveoutleft
        "Without giving you a chance to protest, she answers her phone and walks toward the exit."
        "After a lot of arguing, you give the restaurant manager what you have and leave."
        show chelsea angry
        "You're {i}definitely{/i} not welcome back."
        $ Cash = 0
    $ acts = 1
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
