
label kate_cupcakes:
    show bg Cafe with dissolve
    $ clothes = 'cafe'
    show chelsea at right with moveinright
    "When you arrive at the cafe, Kate's already there."
    show K Laugh at left with moveinleft
    K "Hey, [pcname]!"
    "She's got a dusting of flour on her chin and nose, but it's the smudge of chocolate on her cheek that draws your eye."
    if corruption > 30:
        "You imagine licking it off... The scent of her and the taste of chocolate..."
    show K Blank at left
    K "Is everything okay?"
    show chelsea happy
    "Blinking thoughts of Kate and chocolate away, you smile."
    pcname "Oh, yeah. What are {i}you{/i} doing though?"
    show K Laugh at left
    K "Oh!"
    "She giggles, beaming at you."
    K "Emilia asked me to come in early today and make some cupcakes. Well, a lot of cupcakes."
    "She leans in."
    K "She said that since I'm so creative, she thought I'd enjoy decorating them."
    if club == "track":
        pcname "I bet she's right; you'll be great at it!"
    elif club == "cheer":
        show chelsea laugh
        pcname "Aww, I'm sure you'll make the cutest cupcakes ever!"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "That's great, Kate!"
    "Kate grins again - as usual, it's contagious."
    K "Anyway, I have a {i}lot{/i} of work to get done. I'll talk to you later, okay?"
    show chelsea happy
    hide K Laugh with moveoutleft
    pcname "Have fun!"
    "Your chest swells with happiness at seeing Kate so excited."



    if damienrelate == "dating":
        show chelsea blank
        "Your first customer is a quiet young man. In a way, he reminds you of Damien."
        "He smiles shyly when you talk to him - and unlike a lot of other guys, he actually looks at your {i}face{/i} when you're talking to him."
        "Customer" "So, um, this might be a little forward, but..."
        if club == "track":
            show chelsea confused
            "Seeing where this is going, you hold up a finger."
            pcname "Let me guess! You wanted extra whipped cream, right Master?"
            "He seems to take the hint, nodding."
            "Customer" "R-right. Thanks."
            show chelsea happy
            pcname "Of course, Master. I'll get that for you right away!"
            "When you bring the drink back, he smiles."
            "Customer" "Thanks; that's perfect."
        elif club == "cheer":
            show chelsea embarrassed
            "You can guess where this is going..."
            pcname "Oh, Master, you'll embarrass me!"
            show chelsea laugh
            pcname "We have some strict policies about talking to customers outside of work, but I hope you'll come see me here?"
            "He nods, his cheeks slightly pink."
            "Customer" "Yeah... Of course."
        elif club == "yearbook":
            show chelsea embarrassed
            "Sensing where this is going, you blurt out the first thing you can think of."
            pcname "I'm dating someone!"
            "He flushes immediately."
            "Customer" "Oh, no, I... I wasn't..."
            "Flushing just as deeply, you shake your head."
            pcname "Oh, I'm so sorry! I thought..."
            "He chuckles uncomfortably, looking away."
            "Customer" "I just wanted to say that you're really pretty. That's all."
            pcname "Oh, um... Thank you..."
        show chelsea blank
        "As you leave his table, you feel a certain... emptiness."
        show chelsea sad
        "He seemed really nice. Just like Damien..."
        "Or Kate."
        "Your chest tightens when you think about both of them. They're amazing people."
        "So warm and compassionate... You can only imagine what would happen if they found out about each other."
        "You know it's wrong to string both of them along; you'll have to break it off with one of them eventually."
        "But the though of hurting one of them... How do you choose between two amazing people?"
    elif violetrelate == "Sub" or violetrelate == "Dom":
        show chelsea blank
        "Your first customer is a snobby girl with dark hair."
        "Normally, you'd dislike her instantly. But there's something about the way she holds herself that you find appealing."
        "After a few minutes, you realize what it is. She reminds you of Violet."
        "Customer" "Excuse me, but I asked for nonfat milk and this is {i}not{/i} nonfat."
        "She flips her hand over the same way Violet does."
        if violetrelate == "Sub":
            show chelsea angry
            "You open your mouth to rebuke her, barely catching yourself in time."
            show chelsea blank
            "Violet might not be able to talk to you like that, but this lady {i}isn't{/i} Violet."
        elif violetrelate == "Dom":
            "You nod submissively."
            pcname "Sorry, Mistress."
            "She reminds you so much of Violet, but for some reason her attitude bothers you."
        "Customer" "Well? Fix it!"
        "You take the latte back to the counter and, even though you made it right the first time, quickly remake it."
        "Carrying an exact replica of her original latte back to her table, you place it in front of her."
        "Customer" "About time."
        show chelsea happy
        "Smiling and giving her a little bow, you hurry away before she can complain anymore."
        "She reminds you so much of Violet, but somehow you can't stand her."
        "Maybe it's just that she's {i}not{/i} Violet. Or maybe it's just that after talking to Kate..."
        show chelsea blank
        "You pause clearing off a dirty table, shocked by your own thoughts."
        show chelsea sad
        "What would Kate think of Violet? Of your... agreement with Violet?"
        if violetrelate == "Sub":
            "You and Violet aren't {i}technically{/i} dating, but the things she does to you..."
            "Shuddering a little, you force those thoughts away."
        elif violetrelate == "Dom":
            "While you and Violet aren't {i}technically{/i} dating, the things you do to her aren't exactly platonic."
            show chelsea happy
            "Smiling to yourself, you try not to think about it at work."
        "One thing's for sure, though... Kate would never understand."
        "Sweet, innocent, pure... Kate is everything that Violet isn't."
        "Not that Violet doesn't have her charms. They're just so different from Kate's..."
        show chelsea sad
        "Guilt gnaws at your ribs. You don't want to break things off with Kate, but she'll never give you what Violet can."
        "And though you know you should choose, it's so tempting just to keep getting different things from each."
        "No one's getting hurt... So far, at least."
    elif True:
        show chelsea blank
        "As you wait on your tables, you can't help but think of your parents."
        "Would they have liked Kate?"
        show chelsea sad
        "As much as you'd like to think that they'd love Kate, the truth is... You're just not sure."
        "Kate's amazing, but she still works at a cafe. Your parents always talked about college - and the type of man they thought you'd marry."
        "Would they approve?"
        "You try to shake off your concern, telling yourself that it doesn't matter."
        "But part of you longs to know what advice your mother would have given you."
    if mattsubmissive == True:
        show chelsea blank
        "A young man is seated in your section. His dark hair obscures his eyes and for a moment you think you recognize him."
        if defymatt:
            show chelsea sad
            "Your heart drops. Matt."
            "For a moment, you consider asking someone else to take the table."
            "Kate would do it. She's always willing to help--"
            "Ice floods your veins as you realize what you're thinking."
            "If Matt knew about you and Kate... If he even suspected..."
            "You can't help the images that flood your mind. Images of him using Kate the way he's used you..."
            "Kate kneeling naked before him. Kate tied to naked to a chair. Kate bent over a desk."
            "Fighting back a sudden wave of nausea, you stumble against a chair."
            "The man looks up. For a few moments, you can't process what you're seeing, but you eventually heave a sigh of relief."
            "It's not Matt."
        elif True:
            "Matt."
            "A familiar calmness settles over you, even as your pulse begins to race."
            "You know he's terrible. The things he does are terrible. The things he makes {i}you{/i} do are terrible..."
            "But at least if he's the one in control, you don't have to feel so terrible for {i}wanting{/i} to do them."
            "As you take a step toward his table, you steel yourself for whatever he's going to make you do."
            show chelsea shocked
            "Kate giggles somewhere in the back. Her voice cuts through your thoughts and you freeze in place."
            "Kate doesn't think that you're a bad person. She doesn't see the darkness inside of you."
            "And while Matt feeds that darkness, Kate..."
            "Some part of you almost believes Kate could light that darkness."
            "Torn with indecision, you stand frozen, staring at the dark head bent over the menu."
            "You want Matt's darkness. While you're with him, you can let it engulf your own."
            "He degrades you. Uses you. But, twisted as it seems, you know it's what you want."
            "But with Kate... For a little while, you can imagine you're a person who {i}doesn't{/i} deserve Matt."
            "The dark head rises and you know he'll be able to see what you're thinking."
            show chelsea sad
            "But... It's not Matt."
    show Zoey Happy with dissolve
    "While you wrestle with your thoughts, Zoey approaches you."
    show Zoey Neutral
    "Zoey" "Hey, Harper is on break. Can you load the dishwasher? I'll watch your tables for you."
    show chelsea blank
    pcname "Sure. No problem."
    show chelsea shocked
    hide Zoey Happy with dissolve
    show K Sad at left with moveinleft
    "As soon as you enter the kitchen, though, you find Kate crying."
    "In front of her, two big cupcake pans are full of burnt cake."
    if club == "track":
        show chelsea sad
        pcname "That doesn't look good..."
    elif club == "cheer":
        show chelsea confused
        pcname "Oh, no, Kate... What happened?"
    elif club == "yearbook":
        show chelsea sad
        pcname "Oh, no... Kate..."
    "Kate looks up at you, dashing the tears from her eyes."
    K "I don't know what happened. I {i}know{/i} I set the oven to 325, but when I went to check them it was at 425."
    "She sniffles, trying to regain control of her emotions."
    menu kate_cupcakes_react:
        "You {i}are{/i} kinda ditzy sometimes..." if True:
            show chelsea sad
            "Her eyes widen and her lower lip trembles."
            K "I... I know I am, but..."
            "Tears spill over, trailing down her cheeks."
            K "I guess you're right. Clumsy Kate is at it again..."
            pcname "Kate..."
            "Shaking her head, she wipes her face dry again."
        "What do you think happened?" if True:
            show chelsea sad
            "Her face scrunches up."
            K "I don't know. I just... I {i}know{/i} I set it right."
            K "I'm just glad you believe me. Everyone else thinks I'm just silly, clumsy Kate."
            pcname "Kate..."
            "Shaking her head, she dumps the cupcakes into the trash."
    show K Happy at left
    K "Don't worry, [pcname]. I'll be fine. I just need to make another batch!"
    hide K Happy with moveoutleft
    "She puts on a smile and walks into the stock room."
    show chelsea blank
    "You finish filling the dish washer and head back to your tables."
    "While you were in the back, a group of guys came in. Zoey has their orders taken, so you help her get the drinks and deliver the food."
    "They're a boisterous group, but fairly well behaved. By the time they leave, it's time for your break."
    "As soon as you clock out, you pop into the kitchen to check on Kate."
    "She has several trays of freshly decorated cupcakes on the table in front of her, and a few still waiting to be iced."
    "Some look like cats or dogs, while others are giant flowers."
    "You have to admit it; she's really good at this."
    show chelsea happy
    pcname "Wow, Kate, those look amazing!"
    show K Embarrassed at left with moveinleft
    "Kate yelps."
    K "Ahh! Sorry... I was so focused..."
    show K Laugh at left
    show chelsea laugh
    "Laughing together, you're pleased to see that she's recovered her spirits."
    show chelsea happy
    pcname "Seriously, though... These look so good."
    show K Happy at left
    K "Thanks! I've been working really hard."
    if club == "track":
        pcname "I can tell. It's really paying off."
    elif club == "cheer":
        show chelsea laugh
        pcname "Don't work too hard."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "I see that..."
    show chelsea embarrassed
    "Kate grins and your stomach flutters."
    show chelsea happy
    "You spend your break chatting with Kate as you watch her decorate the cupcakes."
    "Her technique is amazing. Each time she begins, you wonder how she'll make this one come to life."
    hide K Happy with moveoutleft
    show chelsea blank
    "Your break flies past and soon you have to go back to work."
    "Thankfully, the rest of your shift goes almost as fast."
    "You clock out, popping by the kitchen to check on Kate before you change."
    show K Happy at left with moveinleft
    K "[pcname], look! It's the last tray!"
    "Shining with pride, she directs your gaze to the table, which holds a large tray of cupcakes."
    show chelsea happy
    pcname "Wow! They're amazing!"
    "Kate giggles, looking sheepishly pleased."
    K "Are you leaving? Wait up! I just have to put these in the cooler and I'll walk home with you!"
    pcname "That would be great."
    hide K Happy with moveoutleft
    "Still smiling, you walk to the crew room, passing Zoey and Harper."
    "You try not to listen in, but still catch a few words."
    show Zoey Laugh at midright with moveinright
    show Harper Happy with dissolve
    "Zoey" "You aren't really going to do it are you?"
    show Harper Laugh
    "You don't hear Harper's response - just giggling as they leave the room."
    hide Harper Laugh with dissolve
    hide Zoey Laugh with dissolve
    show chelsea blank
    "Even though the night went by fast, you feel exhausted."
    "Between your customers and Kate's troubles, you--"
    K "WAAAHHHH~!"
    show K Sad at left with moveinleft
    "Dashing into the kitchen, you see Kate standing over an upended tray. Frosting covers the floor, sprinkled with bits of mangled cake."
    show chelsea confused
    pcname "Kate, what happened?"
    show chelsea sad
    "Sinking to her knees, Kate sobs."
    K "I-I was carrying the tray and I-I tripped on something..."
    "She glances behind her, but there's nothing there."
    show Harper Laugh with dissolve
    "Harper" "Clumsy Kate tripping over her own two feet again?"
    show Harper Happy
    show Zoey Happy at midright with dissolve
    "Kate's lip trembles as she stares miserably at the mess."
    "Imitating Kate's baby-talk, Zoey teases her too."
    show Zoey Laugh
    "Zoey" "Don't cwy, Kate. It's gonna be okay."
    show Zoey Happy
    show Harper Laugh
    "Harper" "I guess Emilia shouldn't ask someone so clumsy to do something so important, huh?"
    "Harper" "I could have told her you'd screw it up."
    show Harper Happy
    show Zoey Laugh
    "Zoey" "After she burnt so many earlier too..."
    show chelsea angry
    show Zoey Happy
    "Your blood starts to boil as they continue speaking, but Kate meets your gaze and shakes her head, silently imploring you not to speak."
    show Harper Laugh
    "Harper" "Have fun cleaning all that up, wittle Kate."
    show Harper Happy
    hide Harper Happy with moveoutright
    hide Zoey Happy with moveoutright
    "Their laughter fades as they leave the kitchen."
    K "I can't believe I did that..."
    show chelsea sad
    K "It'll take forever to clean this up. And I won't have enough time to make more before tomorrow..."
    "Lifting the tray, she stares down at the smashed cakes."
    K "Just... Go home, [pcname]. I need to clean up..."
    menu kate_cupcakes_help:
        "Help her clean up." if True:
            show chelsea blank
            "You drop to your knees across from her and begin picking the cupcake liners from the mess."
            K "You don't have to do that. I--"
            pcname "Kate... I want to help. Please."
            "Smiling tremulously, she nods."
            K "Th-thanks. You're the best..."
            "Between the two of you, it doesn't take long to get the mess cleaned up."
            hide K Sad
            hide chelsea with dissolve
            "When you're done, Kate changes and you walk her home."
            show bg CityE with dissolve
            "She's quiet and withdrawn, close to tears the whole way."
            $ clothes, hair = casualwear
            show chelsea at right with moveinright
            show K Casual Sad at left with moveinleft
            K "Thanks for walking with me, [pcname]. I just... I'm going to go to bed."
            K "Is it okay if I don't invite you in?"
            if club == "track":
                show chelsea happy
                pcname "Of course. You just take care of yourself!"
            elif club == "cheer":
                show chelsea happy
                pcname "Don't worry about me. You just take a hot bath and relax."
            elif club == "yearbook":
                show chelsea sad
                pcname "O-of course it's fine."
            "She smiles faintly."
            show K Casual Happy at left
            K "Thanks... You really are the best."
        "Stay and make cupcakes." if True:
            $ acts -= 1
            show chelsea blank
            "You drop to your knees across from her and begin picking the cupcake liners from the mess."
            K "You don't have to do that. I--"
            pcname "I do if we're going to make more cupcakes."
            show K Blank at left
            "Her eyes fly to your face, wide and hopeful."
            K "What? You're going to help me remake them?"
            show chelsea happy
            pcname "I couldn't just leave you here, could I?"
            show K Happy at left
            "A slow smile creeps over her lips."
            K "You're amazing, you know that?"
            if club == "track":
                show chelsea laugh
                "You grin back."
                pcname "Yeah, but you can keep saying it."
            elif club == "cheer":
                "You wink."
                pcname "Not why I imagined you'd say that, but I'll take it."
            elif club == "yearbook":
                show chelsea embarrassed
                "You feel your cheeks pinkening."
                pcname "I-- I don't know about that..."
            "Kate giggles."
            "It doesn't take long for the both of you to get everything cleaned up."
            show chelsea happy
            "With Kate giving you directions, you have the cupcakes in the oven in no time."
            "While they bake, you help Kate whip up some frosting, watching as she expertly dyes it in batches."
            K "I'll put them in the cooler so they cool off faster."
            pcname "Shouldn't we frost them first?"
            K "Nope! If you frost them while they're warm, it'll all melt."
            pcname "Oh. I hadn't thought of that..."
            "After about 15 minutes in the cooler, Kate decides they're ready to be decorated."
            "You do your best to mimic her, but when you're done with the first cupcake, Kate grimaces."
            show K Blank at left
            show chelsea sad
            K "That's... a good first try. How about you just pass me the colors I need?"
            show K Laugh at left
            show chelsea laugh
            "Kate giggles as you pretend to pout, and soon you're laughing together again."
            "When the cakes are frosted, you help Kate carry them into the cooler."
            show K Happy at left
            K "Thanks! I was so nervous after last time..."
            show chelsea blank
            pcname "No problem! Oh, we forgot some..."
            "On the table are two cupcakes: one that Kate decorated and one that you did."
            K "No, those are ours!"
            "Snatching up the cupcakes, Kate holds out the one that she frosted."
            show K Laugh at left
            K "I made this one just for you!"
            "The cupcake has three mini-roses on top of a bed of leaves. It's gorgeous."
            "Kate grins as you take the cupcake from her."
            if club == "track":
                show chelsea happy
                pcname "It almost looks too good to eat!"
            elif club == "cheer":
                show chelsea laugh
                pcname "Kate... it's beautiful. I don't want to eat it!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "But it's so pretty..."
            K "Hopefully it tastes as good as it looks!"
            "You glance at the cupcake you made. It was supposed to be a flower, but..."
            show chelsea sad
            pcname "You should have kept a better one for yourself."
            K "What? No! I love this one!"
            "She holds the cupcake closer to herself."
            show K Happy at left
            K "It's the only one you decorated. Nobody else gets to have it!"
            show chelsea happy
            "You can't help but smile as you look down at your cupcake."
            pcname "It really is too pretty to eat though."
            K "Mmmm..."
            "Glancing up, you see Kate happily munching on her cupcake."
            "Clearly she wasn't having the same problem."
            "Unwrapping it carefully, you hesitantly take a bite."
            "The chocolate cake tastes amazing, with a hint of strawberry that pairs perfectly with the buttercream frosting."
            K "Well? Do you like it?"
            "Kate's cupcake is already gone. She looks up at you expectantly."
            if club == "track":
                pcname "It's incredible!"
            elif club == "cheer":
                show chelsea laugh
                pcname "Good thing you only saved me one... I could eat a ton of these!"
            elif club == "yearbook":
                pcname "It's... It's the best I've ever had!"
            K "Awww..."
            "She squeezes her arms against her sides, giddy from your praise."
            K "I guess we should get going, huh?"
            hide K Sad
            hide chelsea
            with dissolve
            "While you finish your cupcake, Kate changes her clothes."
            $ clothes, hair = casualwear
            show bg CityE with dissolve
            show chelsea at right with moveinright
            show K Casual Happy at left with moveinleft
            "As you walk her home, Kate talks excitedly about how she used freeze-dried strawberries to flavor the cake."
            K "So you have to grate them up into a powder then, but it's worth it because it doesn't change the texture of the cake and you still get all that flavor!"
            "You barely understand what she's talking about; you're just happy to see she's back to her cheerful self."
            K "Well... Here we are..."
            "Kate pauses at her door, turning to look at you."
            K "Oh, look!"
            "She's standing on the first step, putting her at the same height as you."
            K "Anyway... Thanks for tonight. I was going to give up and go home, but you..."
            "She smiles softly."
            K "You snapped me out of it. I really appreciate that, [pcname]."
            "Leaning forward, she kisses you quickly."
            K "I'd invite you in, but... It's pretty late, and you have school tomorrow."
    K "But... if you're not doing anything on Saturday, maybe we could do something together?"
    if club == "track":
        show chelsea laugh
        pcname "I have track in the morning, but I'm yours after that."
    elif club == "cheer":
        show chelsea happy
        pcname "I'm free in the afternoon. What did you have in mind?"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "S-sure. I'm free all afternoon?"
    K "How about... the zoo? It always cheers me up!"
    "You can't help but smile."
    show chelsea happy
    pcname "It's a date."
    hide K Casual Happy
    hide chelsea
    with dissolve
    jump events_end_period

label kate_zoodate:
    $ clothes, hair = casualwear
    show bg RoomE with dissolve
    show chelsea at right with moveinright
    play sound PhoneVibration
    "As you get ready to leave, your phone vibrates."

    call screen TextingScene("Kate",
    [
        TextMessage("I'm so excited!!!"),
        TextMessage("Are you ready?"),
        TextMessage("Should we meet at the zoo?"),
        TextMessage("Sounds good! I'm leaving now", sender = False),
        TextMessage("I can't wait!!! <3"),
    ])

    show chelsea happy
    "Chuckling to yourself, you slip your phone away."
    "Kate must really have been looking forward to this."
    "Since the zoo is a few miles away, you decide to take the bus."
    hide chelsea with dissolve
    show bg CityD with dissolve
    "As you get on the bus, your phone vibrates again."
    show chelsea shocked at right with moveinright
    pcname "Wow, Kate must really be excited..."

    if violetrelate == "Dom":
        show chelsea blank
        $ zoobusscene = "Violet"

        call screen TextingScene("Violet",
        [
            TextMessage("[pcname]"),
            TextMessage("I'm coming to pick you up"),
        ])

        "For a moment, you panic."

        call screen TextingScene("Violet",
        [
            TextMessage("I'm not home", sender = False),
            TextMessage("What? Why not??"),
            TextMessage("I'm meeting someone at the zoo", sender = False),
            TextMessage("The zoo?? Why????"),
            TextMessage("We made plans. I didn't know you wanted to see me today", sender = False),
            TextMessage("UGHHH"),
            TextMessage("Fine")
        ])

        "You debate what to do a moment, but Violet never mentioned doing something this weekend, and Kate seemed so excited..."
        "Violet might take it out on you later, but you can't cancel your trip with Kate now even if you wanted to."
    elif violetrelate == "Sub":
        show chelsea blank
        $ zoobusscene = "Violet"

        call screen TextingScene("Violet",
        [
            TextMessage("[pcname]"),
            TextMessage("Are you busy today?"),
            TextMessage("I'm meeting someone at the zoo", sender = False),
            TextMessage("The zoo??"),
            TextMessage("Yes. Is everything okay?", sender = False),
            TextMessage("Oh. Yeah. I just wanted to see you"),
            TextMessage("You'll just have to think about me I guess", sender = False),
            TextMessage("Oh. I can do that")
        ])

        show chelsea sad

        "You can't help but feel guilty for flirting with Violet on your way to see Kate."
        "Things with Violet aren't {i}romantic{/i}, but..."
        "Sighing, you tuck your phone away."
        "You know things can't continue like this, but what can you do? You're already in too deep with both of them..."
    elif damienrelate == "dating":
        show chelsea blank
        $ zoobusscene = "Damien"

        call screen TextingScene("Damien",
        [
            TextMessage("Hey"),
            TextMessage("Are you busy today?"),

        ])

        show chelsea sad

        "You stare at your phone, guilt gnawing at you as you wonder what to say."

        call screen TextingScene("Damien",
        [
            TextMessage("I guess you must be"),
            TextMessage("I'll catch up with you later then. Have a great day!")
        ])

        "You breathe a sigh of relief. At least you didn't have to lie."
        "Still, the heaviness of your guilt weighs on your shoulders."
        "You have to break things off with one of them - and soon. But how can you pick?"
    elif mattsubmissive == True:
        show chelsea blank
        $ zoobusscene = "Matt"
        call screen TextingScene("Matt", [TextMessage("Taking the bus today?")])
        show chelsea confused
        "You stare at your phone in confusion. How does he know...?"
        "Suddenly, someone takes a seat next to you."
        show Matt Casual Smirk at left with moveinleft
        m "Well look who it is..."
        if defymatt:
            show chelsea shocked
            "Your stomach sinks. If he sees Kate..."
            "You begin to panic. You have to cancel. Or ask her to meet you inside the zoo. But what if he decides to join you?"
            "It doesn't matter; you can't text her now or he'll see."
        elif True:
            "A familiar feeling begins to suffuse your body. You wait to see what Matt wants from you."
            show chelsea shocked
            "And then, suddenly, you begin to panic."
            "What if Matt sees Kate?"
            "He might be what you deserve, but Kate doesn't deserve him."
        "You have to cancel. Or ask her to meet you inside the zoo. But what if he decides to join you?"
        "It doesn't matter; you can't text her now or he'll see."
        m "You don't look happy to see me."
        if defymatt:
            if club == "track":
                show chelsea angry
                pcname "When am I ever?"
            elif club == "cheer":
                show chelsea sad
                pcname "Should I be?"
            elif club == "yearbook":
                show chelsea confused
                pcname "I... I..."
            "Matt smirks."
        elif True:
            if club == "track":
                show chelsea sad
                pcname "You surprised me."
            elif club == "cheer":
                show chelsea confused
                pcname "Don't I? Sorry, I guess I'm just surprised to see you."
            elif club == "yearbook":
                show chelsea sad
                pcname "Oh, I... I am."
        show Matt Casual Pleased at left
        m "Didn't expect to see me here, huh?"
        m "I was walking down the street and caught that red hair..."
        show Matt Casual Happy at left
        m "Thought I'd get on and say hello."
        "As he speaks, his hand covers your thigh."
        if defymatt:
            show chelsea sad
            "You want to push him away, but he has those pictures..."
            "And you can't help but hope that if you do what he wants, he'll leave you alone when you get off the bus."
        elif True:
            show chelsea sad
            "Just that little bit of contact makes you quiver in your seat."
            "He owns you and you know it."
            "But Kate..."
        m "Aren't you going to say hello to me?"
        "Unsure what he means, you stare at his cruel grin."
        "He glances around. There are quite a few people on the bus, but they're all keeping to themselves."
        show Matt Casual Smirk at left
        m "Too many people for a blowjob. But you can use your hand, right?"
        "He props his bag on his right leg, blocking his lap from view."

        hide chelsea
        hide Matt Casual Smirk
        with dissolve
        show bg black with dissolve

        show bg MattBusScene1 with dissolve
        "Unzipping his pants, he pulls his cock free of his boxers, obscuring it beneath the bottom of his hoodie."
        if defymatt:
            "Despite your feelings towards him, you find your heart beating hard in your chest."
            "Doing this so publicly... It's as exciting as it is degrading."
        elif True:
            "His confidence eliminates any hesitancy on your part."
            "And the thrill of doing this in a public place makes your heart begin to race."
        m "Well? If you'd rather blow me I won't stop you, but..."
        "Eyes widening at the thought, you slip your hand under his hoodie and grasp his cock."
        "It's only half erect, but quickly responds to your touch."
        "As you stroke him, he leans back in the seat, his breath catching in his throat."
        m "Mmmm, just like that..."
        "You can only hope that if you do what he wants now, he'll let you get off the bus in peace."
        "Stroking him slowly and firmly, you try not to look suspicious."
        "Can anyone see you? Are they watching? You're too embarrassed to find out."
        "To your surprise, you can sense when Matt is growing close to his climax."
        "Something about his breathing, maybe, or even the way his cock feels as he gets closer..."
        if defymatt:
            "The realization sends your mind reeling. You're so familiar with his body - his cock - that you know when he's going to cum?"
            show chelsea sad
            "Shame fills you, but there's also a touch of something else. Pride?"
            "You hate him, but you've gotten {i}good{/i} at making him cum."
            "You push those thoughts away. You don't want to enjoy anything about this."
        elif True:
            "Pride surges within you. You're so familiar with his body - so accustomed to serving him - that you can feel when he's going to cum."
            "He's right; you're a slut. But you're {i}good{/i} at it."
        m "Stop."
        "You obey immediately, without thinking."
        m "I can't walk home with a stain, can I?"
        "Unsure what he wants you to do, you stare at him, hand still wrapped around his cock."
        show bg MattBusScene2 with dissolve
        m "Swallow it all and make it quick. Unless you {i}want{/i} someone to see..."
        "Heart pounding, you lower your head to his lap and slip the tip of his dick into your mouth."
        "It's already salty with pre-cum and the flavor coats your tongue as you stroke him again."
        "You were right; he was very close, and soon his cum floods your mouth."
        "Swallowing hastily, you sit back up and wipe your mouth."

        show bg CityD with dissolve
        show chelsea at right with moveinright
        "He tucks his cock away and turns toward you."
        show Matt Casual Smirk at left with moveinleft
        m "Do you think anyone was watching?"
        show chelsea sad
        "You look down, afraid to know the answer."
        "Matt laughs."
        m "Don't worry. I'm sure they could already tell you were a slut."
        m "I could the first time I saw you, after all."
        "You want to protest, but you {i}did{/i} let him grope you that first day..."
        m "So where are you going? Maybe I'll join you."
        "Numbness settles over your body as you struggle to think of an answer."
        "Where wouldn't he want to go? Where couldn't he make you do things..."
        "Suddenly, he laughs."
        show Matt Casual Happy at left
        m "Actually, I'm meeting up with Alex soon anyway."
        if deskstain == True:
            show chelsea embarrassed
            "You flush at the thought of Alex, remembering that day in the classroom."
        m "Maybe next time, I'll bring you along to hang out with him."
        "He stands up as the bus comes to a stop."
        m "Maybe not. I guess you'll have to wait and see."
        hide Matt Casual Happy with moveoutleft
        show chelsea sad
        "As Matt leaves, you heave a sigh of relief."
    elif True:
        show chelsea happy

        call screen TextingScene("Kate",
        [
            TextMessage("I'm at the gate waiting for you!"),
            TextMessage("Almost there", sender = False),
            TextMessage("YOU CAN SEE THE GIRAFFES FROM HERE")
        ])

        "Laughing, you tuck your phone away."
    show chelsea blank
    "It's not much further before your stop. As the bus pulls up in front of the zoo, you stand and make your way down the aisle."
    if zoobusscene == "Matt":
        "Matt's cum still coats your mouth. You'll have to buy a drink when you get inside."
    "As soon as you get off the bus, Kate flags you down."
    show K Casual Happy at left with moveinleft
    K "Do you see the giraffe!?"
    "She points excitedly at the Zoo fence. You can just barely make out the shape of a giraffe through the fence and vegetation."
    show chelsea happy
    pcname "I... think so?"
    K "It's there! I've been watching!"
    "Smiling at her exuberance, you let her take your hand and lead you to the gate."
    "Gate Person" "Two tickets?"
    K "Yes please!"
    "Gate Person" "Okay, that's $47."
    if Cash < 47:
        K "Don't worry, [pcname]. I got it!"
    elif True:
        $ Cash -= 47
    "The gate keeper passes you each a ticket stub and Kate pulls you into the zoo."
    K "What do you want to do first?"

    menu kate_zoo_first:
        "Let's go see that giraffe!" if 'giraffe' in zoo_options:
            $ zooseen.remove("giraffe")
            $ zoo_options.remove("giraffe")
            call kate_zoo_giraffe from _call_kate_zoo_giraffe
        "Do they have penguins?" if 'penguin' in zoo_options:
            $ zooseen.remove("penguin")
            $ zoo_options.remove("penguin")
            call kate_zoo_penguin from _call_kate_zoo_penguin
        "Why don't we just walk around?" if 'goat' in zoo_options:
            $ zooseen.remove("goat")
            $ zoo_options.remove("goat")
            call kate_zoo_goat from _call_kate_zoo_goat
    scene bg CityD with dissolve
    show K Casual Blank at left with dissolve
    K "I'm kinda hungry. Wanna get something to eat?"
    show chelsea shocked at right with dissolve
    "Your stomach growls before you can answer."
    show K Casual Laugh at left
    show chelsea embarrassed
    "Kate giggles."
    show chelsea happy
    K "I guess that answers that question!"
    K "I think there was a food court on our way over here..."
    show chelsea blank
    "Kate presses a finger to her lips as she tries to remember."
    K "Oh! Right, I think it was... This way!"
    "She bounces off in what you hope is the direction of the food court."
    "Luckily, it appears she's right; soon you can see the brightly colored food stalls."
    "There's a hotdog stand, burger and sandwich stalls, and even a lemonade booth."
    "But a sign catches your attention: \"Today Only: Local Favorites!\""
    show K Casual Happy at left
    K "Oh... It looks like some local restaurants have stands today."
    "She's right. A local cafe is pouring out cups of cold brew coffee, while a pizzeria is extolling the virtues of its homemade sauce."
    "Kate's attention is on a bakery stand."
    K "Look at those cookies! They look like the animals!"
    "She practically skips to the stall, squealing about the cute cookies."
    "Behind the counter, a dark-haired woman smiles."
    show L Happy with dissolve
    L "Hello there. I'm Lisa and I'm selling pastries from the \"Sugar Bliss\" Bakery."
    show K Casual Laugh
    K "They're so cute~!"
    show K Casual Happy
    L "Thanks! We bake everything fresh daily."
    "As Kate looks over the display, Lisa smiles down at her."
    show L Blank
    L "Are you interested in baking?"
    show K Casual Laugh
    K "I love it! I don't know if I'm good enough to make things like {i}these{/i} though."
    if club == "track":
        show chelsea laugh
        pcname "But your cupcakes were amazing! You could definitely make cookies like these."
    elif club == "cheer":
        show chelsea happy
        pcname "Oh, don't be so modest! You make gorgeous cupcakes."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "I think you could! Your cupcakes were beautiful..."
    show K Casual Laugh at left
    "Kate smiles, her cheeks turning pink as she takes in the compliment."
    K "Thanks, [pcname]..."
    "Glancing between the two of you, Lisa smiles again."
    show L Happy
    L "Well, if you're ever looking for work, I'm sure we could use a cute girl like you at the bakery."
    show K Casual Happy at left
    K "Oh, thank you, but... I have a job at Emilia's Maid Cafe and I really like it there."
    "Lisa nods, sunlight glinting off her glasses."
    show L Blank
    L "She's lucky to have you, but if you ever change your mind come talk to me, okay?"
    "Kate nods, leaning back over the cookies."
    K "They all look so good... I don't know how to pick one!"
    show chelsea happy
    menu kate_zoo_cookie:
        "I want a lion." if True:
            show K Casual Laugh
            K "And give me a tiger!"
        "I'll take a monkey." if True:
            show K Casual Laugh
            K "Then I think... a giraffe!"
        "I think I want a zebra." if True:
            show K Casual Laugh
            K "Maybe I'll get an elephant. Look at the trunk!"
    "The woman packs up your cookies and passes them over the counter."
    show L Happy
    L "That's $5 then. Thank you both!"
    hide L Happy with dissolve
    "Cookies in hand, you order sandwiches and drinks from the other stands and find a table to eat at."
    K "That was so good. Where do you want to go next?"
    menu kate_zoo_second:
        "Let's go see that giraffes!" if 'giraffe' in zoo_options:
            $ zooseen.remove("giraffe")
            $ zoo_options.remove("giraffe")
            call kate_zoo_giraffe from _call_kate_zoo_giraffe_1
        "Do they have penguins?" if 'penguin' in zoo_options:
            $ zooseen.remove("penguin")
            $ zoo_options.remove("penguin")
            call kate_zoo_penguin from _call_kate_zoo_penguin_1
        "Maybe just walk around?" if 'goat' in zoo_options:
            $ zooseen.remove("goat")
            $ zoo_options.remove("goat")
            call kate_zoo_goat from _call_kate_zoo_goat_1
    K "I guess there's only one area left to go though, huh?"
    if 'giraffe' in zoo_options:
        $ zooseen.remove("giraffe")
        call kate_zoo_giraffe from _call_kate_zoo_giraffe_2
    elif 'penguin' in zoo_options:
        $ zooseen.remove("penguin")
        call kate_zoo_penguin from _call_kate_zoo_penguin_2
    elif 'goat' in zoo_options:
        $ zooseen.remove("goat")
        call kate_zoo_goat from _call_kate_zoo_goat_2
    K "It's getting kinda late. I guess we should go home, huh?"
    pcname "If you're ready to go."
    "She looks around."
    K "Actually... Can we go one more place first?"
    show chelsea laugh
    pcname "Lead the way!"
    "Taking your hand, Kate pulls you back through the zoo and into the gift shop."
    K "You always do nice things for me, so I want to do something for you!"
    if club == "track":
        show chelsea happy
        pcname "Awww, Kate, you don't have to..."
    elif club == "cheer":
        show chelsea laugh
        pcname "I mean, if you insist..."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "B-but, you don't have to do that..."
    K "I do! I {i}insist{/i}!"
    "She motions towards the stuffed animals."
    K "So you pick your favorite one and I'm going to buy it for you!"
    show chelsea happy
    "Despite yourself, you're excited to get a gift from Kate."
    "They have all sorts of animals. One for almost every exhibit at the zoo."
    "You find yourself drawn to the three you spent the most time with though."
    menu kate_zoo_gift:
        "The giraffe." if True:
            pcname "Well, since it's the first one we saw from outside the zoo, how about a giraffe?"
            "Kate scoops it up."
            K "Giraffe it is!"
        "The penguin." if True:
            pcname "Meeting the penguins was a lot of fun, so how about a penguin?"
            "Kate scoops it up."
            K "Penguin it is! But I don't think this one will want anchovies."
        "The goat." if True:
            pcname "Look! This one looks just like the goat I brushed."
            "Kate scoops it up."
            K "It's meant to be!"
    "She carries the plushie to the counter like a trophy and, after paying for it, presents you with the bag."
    K "For you! Thanks for cheering me up when I'm sad. Now, if you're sad, you'll have something to remind you of happy times!"
    "Her words bring a smile to your face. She's always so positive and thoughtful."
    "It's amazing that someone like her exists at all, and you're dating her!"
    "Kate walks out of the zoo with you, holding your hand and chatting away."
    K "I'll see you at work on Monday, right?"
    pcname "I'll be there!"
    show K Casual Sad at left
    K "Okay... You know, I miss you when we don't work together. Tomorrow is going to be so long without you..."
    "Cupping her cheek in your hand, you smile down at her."
    show chelsea embarrassed
    pcname "I'll miss you too."
    show K Casual Happy at left
    "Just like that, her pout is replaced with another smile."
    K "That's okay then. We'll both be thinking of each other! And you can cuddle your plushie and think of me!"
    "Smiling back, you nod."
    hide K Casual Happy
    hide chelsea
    with dissolve
    jump events_end_period

label kate_zoo_giraffe:
    show chelsea happy
    K "Yeah!"
    "She bounces over to a park map and begins searching for the giraffes."
    K "There they are! Let's go!"
    "On your way to the giraffes, Kate stops to stare at every enclosure."
    "You pass flamingos and ostriches, rhinos, and some kind of antelope called a sitatunga."
    "Beside the giraffes is a large cheetah exhibit. Inside, two cheetahs are chasing each other."
    show K Casual Laugh at left
    K "Look at them playing! [pcname], look!"
    "While she watches them play, you take a look around."
    "There's a photo booth near the giraffes, and a vending machine."
    if zoobusscene == "Violet":
        "And next to the cheetah exhibit, a plaque catches your eye."
        "It reads: \"Donated by the Atwood family\"."
        pcname "Atwood... Atwood... Where do I...?"
        show chelsea sad
        "The realization strikes you with a new wave of guilt."
        "Violet."
        "Kate's voice interrupts your troubled thoughts."
    K "Look, they have a place for you to feed the giraffes!"
    "Indeed, the giraffe enclosure has a park employee stationed with cups of small branches."
    "Employee" "Would you like to feed them? It's $3 for a cup of leaves."
    "Kate's eyes shine with excitement as she fishes the money out of her bag."
    show K Casual Happy at left
    K "How do I do it?"
    "Employee" "Just grab the stem and hold it up."
    "Kate takes the cup and glances nervously at the giraffes."
    K "Here, [pcname], you do it first!"
    "She hands you a small branch covered in broad leaves."
    scene black with dissolve
    "It's about as long as your forearm, but light and supple."
    show bg KZD1 with dissolve
    "Taking the thicker end between your fingers, you hold it up toward the giraffes."
    "One of the large beasts steps forward, extending its dark tongue and encircling the branch."
    show bg KZD2 with dissolve
    "Using its tongue, it gently pulls the branch from your fingers and into its mouth."
    K "Oh, wow! Look, they have black tongues!"
    show bg KZD3 with dissolve
    "You take turns holding up branches to the waiting giraffes."
    K "That was so cool..."
    return

label kate_zoo_penguin:
    show chelsea happy
    K "Let's find a map and see if they have them."
    "She quickly locates a map, dragging you along after her."
    K "They do! African penguins. Ohhh! There's even a meet and greet with the penguins! We {i}have{/i} to go!"
    "You walk past polar bears, snow leopards, and an arctic fox exhibit on your way to the penguins."
    if zoobusscene == "Damien":
        "As you pass the snow leopards, a guy's shirt catches your attention."
        "\"Overpopulation is a sexually transmitted disease,\" it reads."
        show chelsea confused
        "You've seen that shirt somewhere before..."
        "Your heart leaps as your eyes dart up to his face, but it's not Damien's eyes that meet yours."
        show chelsea blank
        "Glancing away, you scan the crowd, pretending that you weren't just caught staring."
        show chelsea sad
        "If that had been Damien, what would you have done? What {i}could{/i} you have done?"
    show K Casual Laugh at left
    K "Oh, look!"
    "Kate points a few yards ahead, where two elephants are playing with a giant ball."
    K "Wow..."
    show chelsea happy
    pcname "Yeah, I didn't know they played like that..."
    "You watch a few more minutes, as the two elephants hit the ball with their trunks before chasing after it again."
    K "The penguins are on the other side of the elephants. Let's go!"
    "As you near the exhibit, you can see a zookeeper standing by the gate."
    "Zookeeper" "You ladies are just in time for the meet and greet. Do you want to come in and meet the penguins?"
    "Kate's eyes widen."
    show K Casual Happy at left
    K "Yes! This is amazing, [pcname]!"
    "Zookeeper" "It's pretty neat. Just sanitize your hands over there and we'll go in."
    show K Casual Laugh at left
    "Taking turns, you both sanitize your hands. Kate grins up at you."
    "Zookeeper" "Okay, here we go."
    scene bg KZD5 with dissolve
    "He swings open the gate and ushers you both in. Following him through another door, you find yourselves in an open area next."
    "Zookeeper" "Now they {i}are{/i} birds, so they tend to peck the things they're curious about. Don't be surprised if they peck at your shoelaces or something."
    "Kate practically dances with excitement as he opens a small door and about a dozen penguins rush inside."
    "One of them zips between your legs, flapping its arms, while another eyes up your shoes."
    "Zookeeper" "Here, let's give them some treats."
    "He pulls out a bucket full of tiny fish."
    "Zookeeper" "These are anchovies and they {i}love{/i} them."
    "You watch as the penguins gather around him. He tosses an anchovy in the air and they sway beneath it, like girls trying to catch a wedding bouquet."
    "Squawking and flapping their arms, they push each other out of the way as he throws more fish at them."
    K "They {i}do{/i} like them!"
    "After their snack, the penguins go back to examining you and Kate."
    pcname "They're smaller than I thought they'd be."
    "Zookeeper" "African penguins are only about two feet tall. They live along the coast of South Africa."
    K "Is it cold there?"
    "Zookeeper" "It's cool, but not cold. They prefer their water around 50 to 70 degrees fahrenheit."
    pcname "Really?"
    "Zookeeper" "Most penguins are actually smaller than people imagine. Many people imagine Emperor Penguins when they think of them."
    "Zookeeper" "Now {i}those{/i} can grow over four feet tall."
    "You nod; those are definitely what you were thinking of."
    "Zookeeper" "Okay, let's go see if there are other guests waiting to meet them."
    "Kate nods and you both follow him out of the enclosure."
    "As he leads the next group in, Kate smiles up at you."
    K "That was amazing. I'm so glad we got to see them up close!"
    scene bg CityD with dissolve
    show chelsea happy at right with dissolve
    show K Casual Happy at left with dissolve
    return

label kate_zoo_goat:
    show chelsea happy
    "You walk into the next area, looking at each of the exhibits."
    "There are otters, bobcats, owls, and even a raven."
    "The otters catch your attention the most, diving in and out of a large pool and floating on their backs."
    "They're definitely fun to watch."
    "As you continue walking, there's a small petting zoo with some barnyard animals."
    show K Casual Laugh at left
    K "Oh, look! We can brush the goats!"
    if zoobusscene == "Matt":
        play sound PhoneVibration
        "As Kate dashes excitedly into the petting zoo, you feel your phone vibrate."

        call screen TextingScene("Matt",
        [
            TextMessage("Hey slut"),
            TextMessage("Can you still taste my cum?")
        ])

        show chelsea sad
        "You glance up at Kate, heart racing."
        "She's blithely engrossed in brushing a goat, but she sees you looking at her."
        K "Don't you want to brush one?"
        pcname "Yep! Just a sec!"
        "You know what he wants to hear and, if you allow yourself to think about it, you {i}can{/i} still remember the salty cum coating your mouth on the bus."

        call screen TextingScene("Matt",
        [
            TextMessage("Yes", sender = False),
            TextMessage("I told Alex you'd say that")
        ])

        if deskstain == True:
            show chelsea embarrassed
            "You flush again at the memory of your last encounter with Alex."

        call screen TextingScene("Matt",
        [
            TextMessage("He gave me some great ideas"),
            TextMessage("I can't wait to try them on you"),
            TextMessage("See you at school")
        ])

        if defymatt:
            show chelsea sad
            "You tuck your phone away, shuddering as you try not to imagine what he has planned."
        elif True:
            show chelsea embarrassed
            "You tuck your phone away, shivering at the implications."
        K "Hey are you okay?"
        "You barely noticed Kate approaching you."
        show chelsea sad
        pcname "Oh, yeah... Um..."
        if club == "track":
            show chelsea happy
            pcname "A guy from school needed help with the homework."
        elif club == "cheer":
            show chelsea blank
            pcname "Just someone from school."
        elif club == "yearbook":
            show chelsea sad
            pcname "Someone changed their number and I didn't recognize it..."
        show K Casual Blank at left
        K "Oh, okay. You just looked so upset for a minute..."
        show chelsea happy
        "Forcing a smile, you touch her cheek."
        pcname "Thanks but... You don't have to worry about me. I'm good!"
        "She nods, still looking concerned"
        K "You should come brush a goat with me!"
    "Following her into the petting zoo, you are each given a brush and directed to the goats."
    "There are close to twenty goats, of all sizes and colors."
    "Kate begins brushing a small white goat, while a reddish-brown one approaches you and begins bleating."
    scene bg KZD4 with dissolve
    pcname "I guess you picked me, huh?"
    "The goat bleats again and you laugh, leaning down to brush it."
    "As you smooth the brush over its coarse, wiry coat, the goat closes its eyes happily."
    K "Aw, it likes you!"
    pcname "Yeah, I guess it does."
    "After a while, the goats seem to lose interest, walking away to climb on their play area."
    K "Well, I guess they're ready to play, huh?"
    pcname "Time to get dirty so someone else can brush them clean!"
    "Kate giggles."
    pcname "Speaking of which..."
    "You hold your hands out; they're covered in a layer of dust."
    K "Ew, yeah... Let's wash our hands."
    "After washing your hands, Kate turns towards you."
    K "I know goats aren't that different - not like elephants, or zebras, or anything like that - but it was still exciting to get to touch them."
    scene bg CityD with dissolve
    show chelsea happy at right with dissolve
    show K Casual Happy at left with dissolve
    return

label kate_buttons:
    $ clothes, hair = casualwear
    show bg Cafe with dissolve
    show chelsea at right with moveinright
    show K Sad at left with moveinleft
    "As you walk into the crew room to change, Harper and Emma are standing around Kate."
    pcname "Hey, Kate, whats--"
    "Kate turns towards you, clutching the top of her shirt."
    "Emma" "Don't worry, Katie. It's not like you have anything to show off anyway!"
    "Harper" "We might get complaints though. People will think we let a boy work here!"
    "Kate stares up at you, eyes brimming with tears."
    if club == "track":
        show chelsea angry
        pcname "What's going on?"
    elif club == "cheer":
        show chelsea blank
        pcname "Kate, what's wrong?"
    elif club == "yearbook":
        show chelsea sad
        pcname "H-hey, what's the matter here?"
    "Kate shakes her head, silently imploring you not to say anything."
    "Emma" "Katie's shirt is missing some buttons and she's upset about it."
    "Harper" "We tried to tell her that nobody will notice, but she's too embarrassed."
    menu kate_buttons_react:
        "Stand up for her." if True:
            show chelsea angry
            pcname "You mean you were bullying her about it."
            "Zoey" "What? No! We were just joking, right, Kate?"
            "Kate looks at the floor."
            K "Yeah... They didn't mean anything by it."
            "Emma" "See? Watch who you call a bully."
            "Pushing past you, Emma and Zoey leave the crew room."
        "Ignore them." if True:
            show chelsea sad
            "Kate watches you, relieved when you say nothing."
            "Emma" "C'mon, Zoey. We have work to do."
    "As they leave, Kate releases her shirt. The top two buttons are missing, leaving her shirt hanging wide open."
    show chelsea sad
    if club == "track":
        pcname "What happened to your shirt?"
    elif club == "cheer":
        pcname "Oh no, your shirt!"
    elif club == "yearbook":
        pcname "Oh... That's not good..."
    "Kate sniffles, blinking back tears."
    K "I d-don't know..."
    "Drawing a deep breath, she forces down a sob."
    K "W-what am I g-going to do? I c-can't work like this..."
    menu kate_buttons_fix:
        "We'll switch shirts." if True:
            show chelsea blank
            $ kateshirtswitch = True
            "Kate's eyes widen."
            K "But [pcname]... My shirt will be even tighter on {i}you{/i}."
            "She's right, but if it will make her feel better..."
            if club == "track":
                "Striking a confident pose, you smile."
                show chelsea happy
                pcname "Not a problem! Here, take mine."
            elif club == "cheer":
                "Putting on a saucy smile, you bat your lashes at her."
                show chelsea happy
                pcname "Maybe I'll get better tips then."
            elif club == "yearbook":
                "With more confidence than you feel, you shake your head."
                show chelsea happy
                pcname "It's fine. Nothing to worry about."
            "Handing her your shirt, you take hers."
            $ clothes = 'cafecorrupt'
            "It's definitely smaller; you have to stretch it over your breasts, where it pulls open almost to your bra."
            show K Embarrassed at left
            K "Oh, wow..."
            "Pink creeps over Kate's cheeks as she stares at your chest."
            if club == "track":
                show chelsea laugh
                pcname "Looks good, right?"
            elif club == "cheer":
                show chelsea happy
                pcname "Well? How do I look?"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Is it... bad?"
            K "No. I mean yes. I mean..."
            K "You have {i}really{/i} nice boobs. Eep!"
            "She covers her mouth, as if shocked by what she just blurted out."
            show chelsea laugh
            K "Thanks! I have to go to work now!"
            hide K Embarrassed with moveoutleft
            "You laugh as she dashes from the room."
            if club == "track":
                "While you don't like to show off your body this much, it doesn't really bother you."
            elif club == "cheer":
                "The top is tight, but it doesn't really bother you. And maybe you {i}will{/i} get better tips like this."
            elif club == "yearbook":
                show chelsea embarrassed
                "Glancing at yourself in the mirror, your cheeks flood with heat."
                "You don't mind doing it for Kate, but you feel really exposed."
            "Like it or not, though, you've made your choice."
            "Walking out into the cafe, you almost immediately notice a difference."
            show chelsea blank
            "At your very first table, the man's eyes dart from your cleavage to your face, and back down again."
            "Man" "I'll have, um... Let's see... Um..."
            "It takes a bit of prodding, but eventually you get his order from him."
            "Similar situations play out at other tables. Only one table gives you any trouble."
            "Three young guys sit together, gawking at all of the girls. When you approach, one of them leans back and crosses his arms in front of him."
            "Guy" "Look, this one's got her tits out."
            "Other Guy" "Are they real?"
            "Guy" "Let's find out. C'mon, honey, give us a feel."
            if club == "track":
                show chelsea happy
                "Biting your tongue, you plaster a smile on your face."
            elif club == "cheer":
                show chelsea laugh
                "Giggling, you wag a finger at them."
            elif club == "yearbook":
                show chelsea embarrassed
                "Blushing, you shake your head nervously."
            pcname "I'm sorry, masters, but that isn't allowed here."
            pcname "It would be my pleasure to take your order, though."
            "Guy" "Aw, c'mon. We're paying customers."
            show chelsea happy
            pcname "I know, master, and thank you for business. But I really can't-"
            "Third Guy" "Cool it, guys. The lady's just trying to do her job."
            "Grateful, you flash him a smile."
            "Third Guy" "I'd like a \"Chocolate Cherry Lovely Latte\" and a cheese pastry."
            "Guy" "Sounds like a pussy drink to me."
            "The third guy shrugs."
            "Third Guy" "It's good. What about you losers?"
            "Chagrined, the other guys give you their orders too."
            "In the end, it's not a bad night. And you {i}do{/i} get better tips dressed like this."
            $ tips += 20
        "I think you look great!" if True:
            $ kateshirtswitch = False
            K "You do...?"
            "She turns to the mirror and stares at herself."
            K "You don't think they're right about my chest?"
            if club == "track":
                show chelsea happy
                pcname "Kate... What do you want me to say? That I like your chest?"
            elif club == "cheer":
                show chelsea happy
                pcname "I mean, {i}I{/i} think your chest is perfect, of course."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "N-no, of course not. I think your chest is... It's really nice."
            show K Embarrassed at left
            "Kate flushes even as she smiles."
            K "Maybe it's okay... I mean, for one night..."
            pcname "You'll be fine. You look great and I bet you'll get some really good tips too!"
            "Her confidence slowly building, Kate nods."
            show K Happy at left
            K "Right! It's only one night. I can do this!"
            hide K Happy with moveoutleft
            "With a determined face, she marches out into the cafe."
            show chelsea blank
            "Throughout the night you catch glimpses of her waiting on customers."
            "None of the men seem to give her trouble, until she's given a group of three college-aged guys."
            "Guy" "This one's showing some skin."
            "Other Guy" "Lean over here, sweetheart. I want a better look."
            show K Embarrassed at left with moveinleft
            "Kate turns pinker than you've ever seen her as she tries to redirect them."
            K "Oh, masters, you're teasing me!"
            "Guy" "Oh, I think you're teasing {i}me{/i}."
            K "W-what...?"
            "Seeing where this is going, you start walking towards the table, hoping to help."
            "Third Guy" "That's enough, losers. You're making her uncomfortable."
            "Pausing, you wait to see what they'll do next."
            "Guy" "Whatever. She shouldn't dress like that then."
            "Third Guy" "You dress like shit. Want me to shove you into the toilet?"
            "The third guy looks back to Kate, smiling."
            "Third Guy" "I'd like a \"Chocolate Cherry Lovely Latte\" and a cheese pastry."
            "Third Guy" "And your number, if you don't mind."
            "As you watch, Kate's eyes widen and her mouth falls open."
            K "Oh! {i}Ohhh{/i}! I, um... I'm dating someone already..."
            "The third guy shrugs."
            "Third Guy" "Had to try. Should've known a pretty girl like you wouldn't still be single."
            "Third Guy" "What are you idiots waiting for? Give her your orders."
            "Chagrined, the other guys give her their orders too."
            "By the end of the night, Kate seems perfectly comfortable, chatting easily with customers."
            show K Laugh at left
            K "[pcname]! Look!"
            "She shoves a bunch of bills in your face: her tips for the night."
            K "That's a lot more than I normally get!"
            show chelsea happy
            pcname "Wow, that's great!"
            "She smiles up at you, her eyes softening."
            K "Thanks for the pep talk earlier. I was freaking out and it really helped calm me down."
            pcname "Of course. That's what your girlfriend is supposed to do, right?"
            show K Embarrassed at left
            "Blushing, Kate looks down."
            K "R-right..."
            K "Anyway, thank you. And have a good night!"
    hide K Embarrassed
    hide chelsea
    with dissolve
    jump events_end_period

label kate_sleepover:

    show bg CafeN with dissolve
    "It's a busy Friday night and you barely have a moment to yourself."
    "After clearing your tables, you head to the crew room to change."
    $ clothes = 'underwear'
    show chelsea at right with moveinright
    "As you're taking off your shirt, you hear a faint--"
    show K Casual Laugh at left with moveinleft
    K "{b}BOO!{/b}"
    show chelsea confused
    "You jump, too surprised even to shout."
    "Kate's laughter fills the room as you struggle to get out of your own shirt."
    K "Haha... Sorry, [pcname]... Haha... I couldn't help it... Haha..."
    $ clothes, hair = casualwear
    "Finally escaping the shirt, you find Kate standing in front of you and grinning from ear to ear."
    K "You should've seen how you flailed..."
    show K Casual Embarrassed at left
    "As her giggling subsides, she looks... nervous?"
    show chelsea blank
    pcname "What's the matter?"
    K "Nothing! Why would you say that?"
    pcname "You just look worried."
    K "Oh, no, I just..."
    K "Would you want to... have a sleepover?"
    pcname "A sleepover?"
    "She glances away, idly kicking the floor."
    K "Yeah. We could... do stuff. And I got you a gift, so..."
    show chelsea embarrassed
    pcname "A gift? You didn't have to do that."
    pcname "You just bought me a stuffed animal, remember?"
    K "I know, I just... I wanted to."
    K "So will you come over?"
    "She bites her lip, waiting for your answer."
    pcname "I didn't really pack, but..."
    show chelsea happy
    if club == "track":
        pcname "Sure, why not?"
    elif club == "cheer":
        pcname "Of course. It'll be fun!"
    elif club == "yearbook":
        pcname "That's okay. Let's go!"
    show K Casual Happy at left
    K "Really? Okay! Yeah!"
    hide K Casual Happy
    hide chelsea with dissolve
    show bg black with dissolve
    $ paychecktotal = 20*daysworked
    "Before you left work, you picked up your paycheck."
    "You made [paychecktotal] dollars!"
    $ Cash += paychecktotal
    $ daysworked = 0
    show bg CityN with dissolve
    show K Casual Happy at left with moveinleft
    show chelsea at right with moveinright
    "As you walk home with her, she chatters excitedly about anything and everything."
    "You barely get a word in until she pauses, staring up at her building."
    show K Casual Laugh at left
    pcname "Everything okay? Did you forget your keys?"
    "She laughs."
    K "No, no... I was just thinking about something. C'mon!"
    "She leads you into her apartment, full of nervous energy."
    K "So, um, do you want a drink or...?"
    pcname "I'm fine, thanks."
    show K Casual Embarrassed at left
    K "R-right. Okay. So, what should we do..."
    K "We could paint each other's nails?"
    K "Er, actually, I'm really bad at that."
    "Giggling nervously, she looks around the room."
    show chelsea blank
    pcname "Kate, what's the matter?"
    K "Nothing! I'm just trying to think of something we can do..."
    K "Oh! We could braid each other's hair!"
    K "Though... I guess that's kind of silly, huh?"
    pcname "We can braid hair if you want to."
    K "No! No, I just, um... I didn't really plan anything..."
    "Her fingers twist anxiously together as she looks around the room."
    pcname "Didn't you say you had a gift for me?"
    "She looks down at her fidgeting fingers."
    K "I'll just... go get it then. Wait right here, okay?"
    hide K Casual Embarrassed with moveoutleft
    "She disappears into the bedroom, leaving you alone in the living room."
    "You hear her moving around in the other room, then a surprised yelp."
    show chelsea confused
    pcname "Are you okay?"
    K "Yes! No peeking!"
    "More movement on the other side of the door, and the faint sounds of Kate talking to herself, though you can't understand her words."
    "Finally, the door opens a hair's breadth and Kate's eye fills the crack."
    K "O-okay... It's ready, I just..."
    "You laugh, though it's laced with concern."
    pcname "You're making me nervous! What is it?"
    "Slowly, the door opens and Kate steps out from behind it."
    scene bg KCM1 with dissolve
    "Pink lace cups her pert breasts, while folds of soft, sheer voile cascade to the tops of her thighs."
    "As she steps toward you, the fabric parts to reveal a pair of matching panties."
    K "Do... Do you like it...?"
    "She stares at you wide-eyed, her cheeks flushed and her lower lip caught between her teeth."
    "Your eyes sweep over her lithe figure, roaming from her collar bones to the polish on her toes, and back again."
    K "[pcname]... Say something."
    if club == "track":
        pcname "Shit. Yeah. I like it."
    elif club == "cheer":
        pcname "Of {i}course{/i} I like it. You look amazing!"
    elif club == "yearbook":
        pcname "I... Yes...? You look really pretty."
    "Kate smiles sheepishly."
    if kateshirtswitch == True:
        K "I saw how confident you were the other day. My shirt was so small on you, but you looked so good in it..."
        K "I just... I wanted to look pretty for you. And I wanted you to see me... the way I saw you."
    elif True:
        K "When you told me how good I looked with those missing buttons the other night, I thought..."
        K "Maybe you'd like to see me like this more often...?"
    scene black with dissolve
    show chelsea happy at right with dissolve
    show K Under Embarrassed at left with dissolve
    "Reining in your wandering eyes, you return her smile."
    if club == "track":
        pcname "You're gorgeous, Kate."
    elif club == "cheer":
        pcname "You look {i}amazing{/i}."
    elif club == "yearbook":
        pcname "It's perfect. You look so good..."
    show K Under Laugh at left
    "Kate giggles, shifting nervously from foot to foot."
    K "Do you... want to see my bedroom?"
    "Nodding, you slowly approach her."
    "She tilts her head back, gazing up at you."
    show K Under Embarrassed at left
    K "I've... never really done this before."
    if corruption > 30:
        "Part of you is thrilled by the prospect of teaching her about pleasure, while another part wants to preserve her innocence for as long as possible."
        pcname "Don't worry; I'll teach you."
    elif True:
        pcname "I think we can figure it out together."
    "She nods, licking her lips slowly."
    show chelsea embarrassed
    "You lower your face to hers, your hand caressing the back of her head as your tongue slips between her lips."
    K "Mmmmm..."
    "She melts against you, sinking into your kiss."
    "After several minutes, you pull apart, both flushed and gasping."
    K "The bed's over here..."
    "As expected, her bed is covered in stuffed animals, which she carefully places on her desk."
    "Glancing anxiously about, she takes a seat on the edge of the bed."
    K "So...?"
    hide K Under Embarrassed
    hide chelsea
    with dissolve

    scene bg KCM2 with dissolve

    "Smiling, you stand before her and lean down, pressing your lips to hers."
    "Using gentle pressure, you slowly guide her back onto the bed, where she lays beneath you, cupping your face in her hands."
    "Without breaking the kiss, you run your hand up her side. The fabric is soft and thin; you can feel her warmth through it."
    "Her nipples stand taut against the sheer material, but at the touch of your thumb they stiffen further still."
    K "Mmmmm..."
    "She moans her pleasure as you caress her breasts, paying particular attention to the sensitive tips of her nipples."
    "Unable to resist, you pull your lips from hers, leaving her gasping, and kiss your way down to the lingerie's lacy top."
    show bg KCM3 with dissolve
    "Slipping it down, you reveal one perfect rosy nipple, which you promptly cover with your mouth."
    "As you swirl your tongue around the hard nub, Kate thrusts her hips upward, grinding them against you."
    "Her head tips back and she moans your name with a surprised gasp."
    K "Ahh! [pcname]..."
    "Her hands curl into your hair, cradling you against her bosom."
    show bg KCM4 with dissolve
    "As your tongue circles her nipple, you slip your hand between your bodies, trailing it up her inner thigh."
    "Her sex is hot and wet, even through her lacy panties. Pressing your fingers between her labia, you stroke her opening through the thin fabric."
    "Releasing her nipple, you move your lips to the other, drawing it into your mouth."
    "Kate writhes under you, arching her back and pushing her nipple further into your mouth while her hips thrust rhythmically against your fingers."
    "Suckling her nipple, you draw wet circles over her panties."
    K "Hnnn... Mmmm... Ahhh..."
    "Pulling your head back, you use your lips to tug at her nipple until it pulls free of your mouth with a wet pop."
    K "Ahhh!"
    "Panting, she looks up at you, her eyelids heavy with desire."
    "Her fingers fumble with your shirt as she struggles to undress you."
    "Sitting up, you pull your shirt off and fling it aside."
    "While Kate pushes your bra off your shoulders, you reach behind your back and unhook it."
    show bg KCM5 with dissolve
    "As it falls away, Kate takes one breast in each of her hands and squeezes gently."
    "Sighing with pleasure, she massages your breasts until your nipples press into her palm, demanding her attention."
    "Smiling at the way your body responds, she rubs her thumbs over the stiff peaks."
    "Gasping, you take her nipples between your fingers and thumbs, twisting them gently."
    K "[pcname]..."
    pcname "Kate..."
    "Her eyes squeeze shut as you toy with her nipples. Her fingers dig into your breasts, squeezing hard."
    K "Not fair... It's my turn to touch you..."
    "Chuckling, you release her nipples and lean down to kiss her."
    "She kisses you hard before pulling you further up the bed, until her face is between your breasts."
    "Turning her head to one side, she captures your nipple and sucks hard."
    "Sharp pangs of pleasure radiate from your nipples, charging their way to your pussy like a jolt of electricity."
    pcname "Ahh!"
    "Releasing that nipple, she turns to the other one, doing the same to it."
    pcname "Kate!"
    "She turns her head again, freeing your other nipple with a wet {i}smack{/i}."
    K "What about the rest of your clothes...?"
    "Sitting upright again, you unzip your shorts and kick them off. Your panties follow soon after."
    K "Should I take this off?"
    pcname "No, leave it."
    show bg KCM6 with dissolve
    "Covering her body with your own, you kiss her again, your tongue slipping between her parted lips."
    "Her tongue rushes to meet yours and they roll together, first in her mouth and then in yours."
    "When you draw back again, panting, you roll off of her so that you're lying side-by-side."
    "Tracing your fingers down her side, you hook your fingers under the edge of her moistening panties and slip them aside."
    K "Ah!"
    "Her shaved pussy is incredibly soft, like the skin of a peach."
    "Running your fingers over her labia, you gently caress the sensitive flesh."
    K "[pcname]... I... Ohhh..."
    "As her anticipation builds, you tease her slit with the tip of your finger, never quite pressing inside."
    "Her hips undulate against your hand; she gasps each time your fingers reach her clit."
    K "P-please, I need... I..."
    "She presses her lips to yours, moaning against you as you press two fingers into her cunt."
    "Her fingers dig into your breast, squeezing hard as she thrusts her hips toward you."
    "Working your fingers in and out of her, you slowly lubricate them with her juices."
    "Then, curling them slightly, you search for the tell-tale ridge of her g-spot."
    "When she arches her back with a shocked moan of pleasure, you know you've found the right spot."
    K "[pcname]!"
    "Drawing your fingers back and forth over the ridge, you massage her most sensitive place."
    K "Ahhh... ahhh..."
    "Mindless with pleasure, she thrashes beside you, deaf to her own cries of pleasure."
    K "Y-yes... Ohhhh... OHHHH!"
    "Twisting your hand, you press your thumb against her clit, working it in slow circles while you continue curling your fingers."
    K "Ahhh!"
    K "Hnnn... Hnnnnn... Ohhhhhhh..."
    show bg KCM7 with dissolve
    "Kate's body stiffens, her pussy clamping down on your fingers as she shudders with pleasure."
    K "C-cumming..."
    "Her body trembles in the throes of her orgasm. Her eyes roll back; her lips move soundlessly."
    "Slowly her breathing slows and her body stills. Her pussy releases its hold on your fingers and you slowly withdrawal them from her."
    K "W-wow... That was..."
    "She opens her eyes, smiling dreamily, and kisses you slowly."
    K "I feel like I'm floating..."
    "Her fingers move over your breasts again, trailing over your nipples, absently pinching and twisting."
    "She presses her leg between yours, and slips her tongue into your mouth."
    "Whatever confidence she lacked before, her orgasm has driven away her modesty."
    show bg KCM8 with dissolve
    "Releasing your nipple, she trails her hand down your belly and between your legs."
    "You can hear the wetness as she presses her fingers between your labia, sliding them easily into your pussy."
    "Your gasp breaks the kiss and Kate giggles."
    K "You're {i}so{/i} wet..."
    "Blushing, you press your lips hard against hers. Her fingers slide in and out of your cunt, fucking you slowly."
    "Her inexpert fingering is pleasant, but not pleasant enough."
    "Rocking your hips, you meet her gentle thrusts, your pussy eagerly swallowing her fingers."
    "Following your lead, she fingers you harder and faster, until her knuckles slap against your labia with every thrust."
    "It's still not enough. Sensing this, she presses her thumb to your clit and imitates what you did to her."
    "Gasping, you break the kiss and tilt your head back. You're getting closer, but it's still not enough."
    "Kate dips her head to your nipple, sucking hard."
    "Tremors of pleasure run between your nipple and cunt, which begins to tighten as your climax nears."
    pcname "K-Kate... Ahhh!"
    "She rubs her thumb hard against your clit, her fingers pressing upward into your g-spot as she uses her teeth to nibble on your throbbing nipple."
    "All at once, your body explodes with sensation, almost convulsing with the force of your orgasm."
    "For several minutes you can barely think beyond the pleasure running over your body."
    "And then your eyes flutter open. Kate stares at you, a sleepy smile on her face."
    K "Was it good?"
    "You giggle, still feeling giddy from your climax."
    pcname "It was {i}really{/i} good."
    show bg KCM9 with dissolve
    "She giggles too, cuddling close. You roll onto your back, pulling her tight against you."
    "Her hand settles over your left breast, cupping it gently, while she buries her face against the right one."
    K "I feel so heavy now..."
    "Kissing the top of her head, you close your eyes and drift to sleep."
    scene bg black with dissolve


    $ acts = 4
    $ day += 1
    $ daycount += 1
    $ wenttoschool = False
    $ wenttowork = False
    $ wenttoclub = False
    $ goingto = ""
    call events_end_day from _call_events_end_day_3
    call dayeval from _call_dayeval_3

    show bg CityD with dissolve
    "In the morning, you wake up with Kate still nestled against you."
    "You shift around, trying not to wake her."
    show chelsea at right with moveinright
    show K Casual Blank at left with moveinleft
    K "Mmmmm. Don't wanna get up yet..."
    show chelsea laugh
    "You giggle and her eyes flutter open."
    show K Casual Embarrassed at left
    K "Oh. [pcname]..."
    "You can see the moment she remembers the previous night; her eyes widen and her cheeks flood with color."
    K "Oh! It's light out!"
    "Drawing the covers up to her chin, she pulls away from you."
    K "Sorry, I..."
    if club == "track":
        show chelsea happy
        pcname "Relax, Kate. I've seen it all already."
    elif club == "cheer":
        pcname "You don't have to be so nervous."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "I-it's okay!"
    "She turns redder still."
    K "Sorry! I... I just... Last night was amazing but..."
    pcname "But...?"
    K "I don't know! I just didn't plan this far!"
    "Laughing, you turn to face her."
    show chelsea embarrassed
    pcname "So you planned the rest of it?"
    show chelsea shocked
    "Faking surprise you cover your mouth with your hand."
    show chelsea confused
    pcname "Kate... Did you {i}seduce{/i} me?"
    show chelsea embarrassed
    K "[pcname]! Don't say that! You're picking on me!"
    pcname "Well you said you planned it..."
    K "I didn't! I mean... I didn't know if you would..."
    "She lowers her eyes."
    K "I really like you. Like... {i}really{/i} like you. And I've never been with anyone like {i}this{/i} before."
    K "I wanted it to be special."
    "Taking her hand in yours, you give it a squeeze."
    show chelsea happy
    pcname "It {i}was{/i} special, Kate."
    "She lifts her eyes to yours, blinking back the growing wetness."
    K "[pcname], I... I..."
    K "...I think I love you..."
    "Your chest aches with the force of your emotions."
    pcname "I love you too, Kate."
    "Her eyes shine in the morning light; her lips slowly lifting into a grin."
    show K Casual Happy at left
    K "I should make breakfast!"
    "Pulling away, she hurries out of bed and pulls on some less interesting pajamas."
    K "How about pancakes?"
    "Without waiting for an answer, she rushes out of the bedroom and into the kitchen."
    "You dress and, as she cooks, her nervous energy slowly fades."
    "While she makes pancakes - with chocolate chips, of course - you chat with her about work and school."
    "After breakfast, she fusses over the dishes, clearly trying to keep herself busy."
    pcname "Kate, you seem nervous."
    if club == "track":
        show chelsea laugh
        pcname "Do you want me to go home now?"
        K "No!"
    elif club == "cheer":
        show chelsea happy
        pcname "Are you okay?"
        K "Yes!"
    elif club == "yearbook":
        show chelsea sad
        pcname "Are you... upset?"
        K "No!"
    show K Casual Embarrassed at left
    K "Sorry, I just... Things feel different now, you know?"
    menu kate_sleepover_morningafter:
        "I know." if True:
            K "Y-yeah, so... I just don't know how I'm supposed to act now..."
        "Not really." if True:
            K "Really? You don't think so?"
            K "I guess I'm just being silly, huh?"
    show chelsea happy
    "Approaching her, you drop a kiss on her forehead."
    K "Sorry for worrying you."
    pcname "Nothing's {i}really{/i} changed. We're still us."
    K "I know, I know..."
    "She smiles up at you."
    show K Casual Happy at left
    K "It's weird. I'm so nervous, but I don't want you to go home either."
    "Her laugh is exaggerated and giddy, but she seems to be calming."
    K "I promised to pick up a shift for Emma, though. So I guess I should start getting ready."
    K "We should... do this again soon though, okay?"
    "Smiling, you nod."
    pcname "I'd like that."
    hide K Casual Happy
    hide chelsea
    with dissolve
    jump events_end_period


label kate_handholding:
    show bg CafeN with dissolve
    "After another busy night at work, Kate approaches you."
    $ clothes, hair = casualwear
    show K Casual Sad at left with moveinleft
    show chelsea at right with moveinright
    K "I barely got to see you tonight..."
    "She pouts, sticking her lower lip out."
    if club == "track":
        show chelsea laugh
        pcname "I guess I'll have to walk you home then, huh?"
    elif club == "cheer":
        show chelsea happy
        pcname "I know! We could walk home together though, if you want?"
    elif club == "yearbook":
        show chelsea happy
        pcname "Aww, don't be sad! Want me to walk you home?"
    "Grinning, Kate hugs your arm."
    show K Casual Happy at left
    K "Yes!"
    "She releases you with a happy giggle and grabs her bag."
    K "Let's go!"
    hide K Casual Happy
    hide chelsea
    with dissolve
    show bg CityN with dissolve
    show K Casual Happy at left with moveinleft
    show chelsea at right with moveinright
    "After a block or two, Kate steps closer, taking your hand in hers."
    "Twining her fingers between your own, she squeezes your hand and sighs happily."
    K "We haven't had much time to talk since the other night..."
    if club == "track":
        show chelsea sad
        pcname "Sorry, it's been really busy at work."
    elif club == "cheer":
        pcname "Yeah, our schedules haven't really lined up, have they?"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "R-right. We should talk about it..."
    K "It's okay, I'm not upset or anything."
    show K Casual Embarrassed at left
    K "I just... wanted you to know that I had a really nice time."
    "She looks away, cheeks turning faintly pink in the dim light."
    show chelsea embarrassed
    pcname "Me too."
    "Suddenly, Kate pulls her hand from yours, stepping away from you."
    show chelsea confused
    pcname "Kate? What's the matter?"
    "She ignores you, staring straight ahead and putting on a forced smile."
    show K Casual Happy at left
    show Emma Blank
    K "Emma! How's your day off going?"
    "Turning from Kate in confusion, you look back up the street ahead of you."
    "Emma is slowly walking toward you, looking at her phone. Hearing her name, she glances up."
    show Emma Neutral
    "Emma" "Oh, hey Kate. Hi [pcname]. I'm good, how about you?"
    show chelsea blank
    K "Oh, ju-just walking home!"
    "Brows furrowing with confusion, Emma looks between you and Kate."
    show Emma Laugh
    "Emma" "I kind of figured. Well, have a good night."
    show Emma Blank
    "Looking back down at her phone, Emma steps around you and continues down the street."
    hide Emma Blank with moveoutright
    "As soon as she's out of sight, Kate grabs your hand again."
    show K Casual Blank at left
    "You can feel her tension - even in her fingers, which don't relax against yours."
    "Unsure of what to say, you try to sort through your own thoughts as you walk the final block to Kate's apartment."
    show K Casual Embarrassed at left
    K "Well, here we are... Um, do you want to come in for a bit?"
    if club == "track":
        show chelsea happy
        pcname "Yeah, sure."
    elif club == "cheer":
        show chelsea happy
        pcname "I'd love to!"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Um... Yeah."
    "Following her inside, you glance around the now-familiar living room."
    show K Casual Blank at left
    K "I'm thirsty. Do you want something? There's water, apple juice..."
    pcname "Water's fine."
    "Kate shuffles around the kitchen."
    "You know her well enough now to see that she's trying to keep moving because she's anxious about something."
    show chelsea blank
    pcname "Kate, about earlier..."
    pcname "Why did you stop holding my hand?"
    "Kate drops a plastic cup onto the counter, where it tips over and rolls onto the floor."
    show K Casual Embarrassed at left
    K "Shoot!"
    "Scooping it up, Kate puts it in the sink and turns back to the cupboard."
    K "I just... didn't want Emma to see, you know...?"
    menu kate_handholding_emma:
        "So you're ashamed of us?" if True:
            show chelsea sad
            K "What? No! I just..."
            K "The girls at work pick on me a lot, and I figure if they know about us they'll pick on you too."
            if club == "track":
                show chelsea angry
                pcname "They can try."
            elif club == "cheer":
                show chelsea confused
                pcname "Who cares what they think?"
            elif club == "yearbook":
                show chelsea sad
                pcname "Y-yeah, that would suck, but..."
            K "But I'm not ashamed of you! I'm so glad that we're together and I don't want anything to mess it up."
            show K Casual Sad at left
            K "I just feel like... If they don't like it they can make things really hard for us."
        "I can understand that." if True:
            "She sighs with relief."
            show K Casual Sad at left
            K "I'm so glad you're not upset. I just... They pick on me a lot and..."
            K "I don't want them to treat {i}you{/i} any differently because of me."
            show chelsea sad
            pcname "Kate..."
    K "I would rather just keep it between us for now, okay?"
    menu kate_handholding_hide:
        "I don't want to hide." if True:
            if club == "track":
                show chelsea blank
                pcname "I don't want to hide our relationship, Kate."
            elif club == "cheer":
                show chelsea sad
                pcname "Hiding it from them just makes it seem like we're doing something wrong, though."
            elif club == "yearbook":
                show chelsea sad
                pcname "But, I don't {i}want{/i} to pretend we're not together."
            K "I know, I know, but..."
        "Maybe just for now." if True:
            K "Thank you..."
    show K Casual Happy at left
    "Crossing the room, she fidgets with your shirt, trying to smile."
    K "I didn't ask you to come up to talk about that..."
    "Though you aren't happy, you let her distract you with a kiss."
    "As the kiss deepens, she pulls you over to the couch."
    hide K Casual Happy
    hide chelsea
    with dissolve
    show bg black with dissolve

    show bg KSS1 with dissolve
    "Pulling away, she giggles and pushes you gently down onto the couch."
    "As soon as you're seated, she climbs onto your lap, straddling you."
    "Kissing you again, she runs her tongue over your lips, teasing you."
    "Parting your lips, you meet her tongue with your own."
    "The kiss seems to last forever as you lose yourself in the sensations."
    "Her hot, wet tongue in your mouth. The weight of her on your lap. Her hands clinging to your shoulders."
    "When she eventually leans back, softly gasping for breath, you lower your lips to her neck."
    "Gently kissing and sucking, you make your way down the curve of her neck and over her collar bones, pausing at the neck of her shirt."
    if club == "track":
        pcname "Clothes are in the way..."
    elif club == "cheer":
        pcname "Why is this still on..."
    elif club == "yearbook":
        pcname "Can I...?"
    "She pulls her shirt off and tosses it aside, eager for you to continue kissing her."
    "You kiss along the edge of her bra, surprised at how different the skin of her breasts feels. It's so soft and supple..."
    "You run your tongue over it to taste the salty sweetness."
    menu kate_handholding_sex1:
        "Take off her bra." if True:
            show bg KSS2 with dissolve
            "Burying your face against her breasts, you wrap your arms around her and, grabbing the hooks of her bra, deftly unhook it."
            "Grasping the front of her bra, you toss it aside and nuzzle her soft, warm breasts."
            K "[pcname]..."
            "You trail kisses around each of her breasts, carefully avoiding the nipples."
            "Kate shivers with anticipation each time your lips pass over her rising nipples, sighing each time you don't touch them."
            "Impatient, she arches her back, pressing her nipple to your lips."
            "Smiling, you take it into your mouth, gratified by her soft, pleased exhalation."
            K "Haaa..."
            "You flick your tongue back and forth across her nipple until she's squirming beneath you."
            "Then, you switch your focus to her other nipple."
            K "Ahhh... [pcname]..."
            "Releasing her nipple, you look up at her."
            "Her cheeks are pink, her lips parted as she sighs happily."
            K "Don't stop..."
            "Running your hands up her sides, you wrap your arms around her and pull her breasts against your face again, sucking each of her nipples in turn."
            "As you move back and forth, nibbling, licking, and sucking at her nipples, Kate tilts her head back and arches her chest toward you."
            K "Ah, [pcname]..."
            "You continue your ministrations until she's writhing in your lap, panting with pleasure."
            K "Haa... Haa... Haa..."
        "Take off your own shirt." if True:
            show bg KSS3 with dissolve
            "Drawing back from her breasts, you grab the hem of your shirt and pull it over your head."
            "Kate giggles and reaches behind you, unhooking your bra and tossing it over the back of the couch."
            "As she kisses her way down your neck, her hands move over your breasts, massaging them gently."
            "Your breath catches in your throat when she pinches your nipples, alternating between them."
            "Meanwhile, her tongue slides up your neck to your ear, where she gently nips at your earlobe."
            "Working your nipples between her fingers, she teases you until you're panting with pleasure."
            pcname "Kate... Haa... Haa..."
            "You wrap your hands around her back and unhook her bra; she lets it slide down her arms and tosses it aside."
            "Her fingers find your nipples again, twisting and tugging the sensitive nubs."
            "As she does this, she raises herself up so that her breasts hover in front of your face."
            "Pressing her chest forward, she presses her nipple to your lips."
            "Closing your eyes, you suck hard, drawing a surprised gasp from her throat."
            K "[pcname]!"
            "She arches her back, pressing her breast tighter to your mouth. Her fingers dig into your nipple, sending a shock of nearly painful pleasure through you."
            "You switch to her other nipple, teasing it with your teeth before sucking firmly."
            K "Ahhh..."
            "Her cries are punctuated by another hard twist of your nipples."
            pcname "Ahhh..."
            "Suddenly she releases your nipples and sits back on your lap, pulling her nipple from your mouth with a wet pop."
    "For a moment, you stare into each others eyes - both heavy-lidded with desire."
    menu kate_handholding_sex2:
        "Go down on her." if True:
            pcname "Stand up a second."
            "She does so, blushing and holding her arms over her chest as you pull her shorts down."
            "Her silky panties are dark with moisture. You trace your finger over them, smiling."
            if club == "track":
                pcname "Want something, Kate?"
            elif club == "cheer":
                pcname "Are you enjoying yourself, Kate?"
            elif club == "yearbook":
                pcname "You're so wet..."
            "Kate's cheeks turn pinker still and she looks away."
            K "D-don't pick on me..."
            "Slipping your finger under the edge of her panties, you draw them down to reveal her moist, pink pussy."
            K "[pcname]..."
            "Quickly removing your own clothes, you take a seat on the couch again."
            "With your hands on her hips, you guide her toward you."
            pcname "Lay down onto the couch."
            show bg KSS4 with dissolve
            "On shaky legs, she does as you instruct. You guide her down, until her sex is practically in your face, then lift her knee."
            "Unable to resist, you run your tongue over the mounds of her labia, licking the moisture from their curves."
            "Kate gasps in surprise, her fingers digging into the back of the couch."
            "Her musk fills your nose as you slip your tongue between her folds."
            K "Oh!"
            "Running your tongue up and down her slit, you tease her opening."
            "Kate gasps each time your tongue dips into her cunt, and soon you can't resist tasting her more deeply."
            "Slipping your tongue inside, you slowly penetrate her."
            "Her hips gyrate, pressing her pussy against your face and your tongue deeper into her."
            "Tilting your head back a bit, you explore the hot cavity."
            K "Oh! Ohhh!"
            "Kate continues swaying against you, her fingers clenched around the back of the couch."
            "Your clit throbs with arousal. Running your hand down your belly, you press your fingers to your clit, rubbing in slow circles."
            K "Ahhh... [pcname]..."
            "As her pleasure builds, you withdraw your tongue and tilt your head back further, pressing your lips to her swollen clit."
            K "Ahh!"
            "She shudders as your tongue flicks back and forth across the sensitive nub, crying out when you fasten your lips around it and suck gently."
            K "Ohhh! AHH!"
            "Your fingers move faster and faster on your clit, edging you closer to your own climax."
            show bg KSS5 with dissolve
            "Kate's cries of pleasure fill the room, and as she grinds her pussy against your face, a rush of fluid coats your chin."
            "Releasing her clit, you cry out too, shuddering in the throes of your own orgasm."
            "As her climax subsides, she lowers her leg from the back of the couch and sinks onto your lap."
            K "That was..."
            "She buries her face against your neck, sighing with contentment."
            "You hold her for a while, feeling her breathing - and your own - slowly return to normal."
            "Eventually, she leans back and crawls off of your lap."
        "Let her take the lead" if True:
            "Kate kisses you hard, nearly bruising your lips with her own, before standing."
            "Blushing, she takes your hand and pulls you up from the couch."
            K "Can you... take those off?"
            "As you strip, she takes her own clothes off as well, carefully avoiding meeting your eyes."
            K "Could you... lay down on the couch?"
            show bg KSS6 with dissolve
            "Smiling, you do as she asks. When you've settled comfortably, Kate climbs onto the couch too, with her face just above your pussy - and your face just below hers."
            "Lowering her face, she uses her tongue to gently stroke your labia. Each time, she starts at your clit and slowly licks the length of your pussy lips."
            "Grabbing her hips, you draw her down towards your face. Tilting your head back, you lick her slit from clit to taint."
            "You feel her breath on your pussy as she gasps. Then she licks you again, slipping her tongue between your cleft."
            "Tilting your forward and back, you lick her cunt like you would an ice cream cone - running it over each curve."
            "She moves her tongue inside of you, stroking your opening until you moan with pleasure."
            pcname "Mmmmmmmm..."
            "You flick your tongue back and forth across her clit, her hips rocking in time with your tongue."
            K "Nnnn... Mmm... Nnnn..."
            "She draws her tongue out of you, licking the length of your pussy before delving inside again."
            "Fucking you with her tongue, she continues moaning each time you flick your tongue over her clit."
            K "Mmmm... Nnnn... Nn! Nn!"
            "She pulls her head back, gasping. Giving her clit a break, you lick the juices from her slit, slipping your tongue inside of her."
            "Lowering her mouth to your pussy, she circles your clit with her tongue before pressing her lips around it and sucking gently."
            "Waves of intense pleasure flood out from your clit, overwhelming your mind for a moment."
            "Pulling your face back, you return your attention to her clit, trying to push her as close to her climax as you are to yours."
            "While she gently sucks on your clit, you flick your tongue over hers, both moaning with pleasure."
            show bg KSS7 with dissolve
            "She lifts her head, pressing her fingers to your clit and rubbing it in circles."
            K "Ahh! I-I'm cumming..."
            "Fluid drips down her pussy and her hips begin to jerk against your face. As her climax leaves her shuddering above you, her fingers quickly bring you to your own."
            "Pulling your head back, you cry out as jolts of pleasure course out from your clit."
            "Kate sinks forward, lying half on you and half on the couch. For a while, you lie like that for some time, until each of you catches her breath."
            "Eventually, Kate pulls herself up and crawls off of you."


    show bg CityN with dissolve
    show K Casual Embarrassed at left with moveinleft
    show chelsea embarrassed at right with moveinright
    K "I... guess you need to go home soon, huh?"
    "You glance at your phone."
    pcname "I don't want to, but I probably should."
    K "Yeah, it's too bad you don't live closer..."
    "Nodding, you start looking for your clothes."
    K "How'd my shirt get over here...?"
    show chelsea laugh
    show K Casual Laugh at left
    "By the time you're dressed, you're both laughing."
    K "That was... really nice."
    "Her face turns bright red as she speaks."
    show K Casual Embarrassed at left
    K "You should come over more often."
    if club == "track":
        show chelsea happy
        pcname "Yeah, I'd like that."
    elif club == "cheer":
        pcname "That would be {i}really{/i} nice."
    elif club == "yearbook":
        show chelsea embarrassed
        "You're sure your face matches hers."
        pcname "Y-yeah..."
    K "Oh, I hate saying goodbye!"
    "She hugs you hard, clinging for a few moments."
    show K Casual Happy at left
    K "Okay, you can go home now. But I'll really miss you!"
    show chelsea happy
    "Smiling, you kiss her forehead."
    pcname "I'll miss you too."
    hide K Casual Happy
    hide chelsea
    with dissolve
    $ acts -= 1
    jump events_end_period

label kate_hickey:
    $ clothes = 'cafe'
    show bg Cafe with dissolve
    "When you walk into the crew room, you hear Kate's voice coming from the kitchen."
    show K Embarrassed with dissolve
    K "It's nothing! I... I just..."
    show chelsea at right with moveinright
    "Concerned, you strip quickly, shoving your clothes into your locker and grabbing your uniform."
    show Harper Laugh at midleft
    show Emma Happy at midright
    "Harper" "Let me see it!"
    show Harper Happy
    K "No! You don't need to; it's nothing!"
    "Yanking your uniform on, you rush into the kitchen."
    show Harper Laugh
    "Harper" "I knew it! It's a hickey!"
    show chelsea angry
    show Harper Happy
    "You enter the kitchen to see Kate blushing furiously and clutching at her neck. Her eyes are wide and brimming with tears."
    "Harper and Emma stand around her, laughing cruelly."
    show Emma Laugh
    "Emma" "How'd Katie get a {i}hickey{/i}?"
    "Emma" "Who's the lucky guy?"
    show Harper Neutral
    show Emma Happy
    "Harper" "I doubt it's a guy at all."
    show Harper Laugh
    "Harper" "Did you give it to yourself? Is that why you're so embarrassed?"
    show Harper Happy
    show K Sad
    K "Please, stop. I... I..."
    "Kate sees you and shakes her head."
    show Emma Laugh
    "Emma" "How'd you do it, Katie? A vacuum?"
    K "I didn't do anything. Why can't you just stop picking on me?"
    show Emma Happy
    show Harper Happy
    "Harper glances over her shoulder and sees you."
    show Harper Laugh
    "Harper" "Come on, Emma. She's getting {i}upset{/i}."
    show Harper Happy
    hide Emma Happy with moveoutleft
    hide Harper Happy with moveoutleft
    "Fuming, you approach Kate."
    if club == "track":
        pcname "That's it! I've had enough!"
    elif club == "cheer":
        pcname "Okay, this {i}has{/i} to stop!"
    elif club == "yearbook":
        pcname "They can't treat you like this!"
    pcname "I'm sick of seeing how much they upset you. And I'm tired of hiding our relationship."
    show K Sad
    K "No, [pcname], please! If you say something, it'll only get worse."
    K "Nobody needs to know. And... and they've always picked on me..."
    K "If you tell them about us, they'll pick on you too."
    pcname "This isn't {i}picking{/i}, Kate. It's bullying. It's {i}harassment{/i}."
    K "{i}Please{/i}, don't make things worse..."
    menu kate_hickey_react:
        "If you're so afraid, maybe this was a mistake." if True:
            if club == "track":
                show chelsea sad
                pcname "If that's how you feel, maybe this was a mistake."
            elif club == "cheer":
                show chelsea angry
                pcname "We don't need to hide anything if there's nothing to hide."
            elif club == "yearbook":
                show chelsea sad
                pcname "Maybe this was a mistake then..."
            K "What...?"
            "Her lower lip trembles."
            pcname "If you'd rather nobody knew, then I won't tell them."
            pcname "But I can't keep hiding."
            "Kate slowly nods, tears spilling down her cheeks."
            K "I understand..."
            K "I'm s-sorry for wasting your time, but I... I just can't tell them yet."
            K "I hope we can st-still be friends...?"
            "You take a deep breath, your heart breaking as her words sink in."
            show chelsea sad
            if club == "track":
                pcname "That might take some time. I don't know if I can just pretend things are okay."
            elif club == "cheer":
                pcname "We can try, but I think it might be harder that way."
            elif club == "yearbook":
                pcname "M-maybe..."
            hide K Casual Sad with moveoutleft
            "Sniffling, Kate dashes from the room."
            "Dabbing the tears away from your own eyes, you force a smile on and start your shift."
            hide chelsea
            with dissolve
            jump events_end_period
        "I care more about you than what they think." if True:
            if club == "track":
                show chelsea sad
                pcname "I don't care what they think. I care about {i}you{/i}."
            elif club == "cheer":
                show chelsea angry
                pcname "You matter more to me. Who cares what they think?"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "S-so what if they don't like it?"
            pcname "Besides, what more can they do? They're already so awful to you."
            K "Thanks, but... I'm scared, [pcname]."
            "Her voice is almost a whisper. As she speaks, you hear the other girls coming back."
            pcname "I know, but we're in this together. I'll protect you and you'll protect me."
            "She nods, smiling tremulously."
            show Harper Laugh at midleft with moveinleft
            "Harper" "Aww, look. Are we interrupting something here?"
            show Harper Happy
            show Emma Happy at midright with moveinleft
            "Emma" "Did Katie show you her hickey, [pcname]?"
            show chelsea angry
            "Fists clenched, you glare at them both."
            show Harper Laugh
            "Harper" "Oh, I think she--"
            if club == "track":
                pcname "I've heard {i}enough{/i}."
            elif club == "cheer":
                pcname "That's enough from both of you."
            elif club == "yearbook":
                pcname "Stop!"
            show Harper Neutral
            "Harper's mouth hangs open in shock."
            show Harper Blank
            show Emma Neutral
            "Emma" "You can't talk to her like that!"
            show Emma Worried
            pcname "I don't like the way you've been treating my {i}girlfriend{/i}."
            pcname "If you keep it up, I'll {i}make{/i} you stop."
            show Emma Neutral
            show Harper Happy
            "Emma" "Your girlfriend? You're dating!?"
            show Emma Blank
            "Emma glances to Harper and back to you, but Harper's eyes never leave your face."
            "Her eyes harden. For a moment, you think she's going to say something."
            "But she merely lifts her nose and turns away."
            show Harper Neutral
            "Harper" "Come on, Emma. Let's go."
            show Harper Happy
            "Emma watches Harper retreat, obviously bewildered, and then follows her out."
            hide Harper Happy with moveoutleft
            hide Emma Blank with moveoutleft
            K "They... left."
            show chelsea blank
            "You nod, sighing with relief. As angry as you were, you really didn't want to start something at work."
            K "Was it really that easy?"
            show chelsea happy
            "You don't have an answer, but you try to smile reassuringly anyway."
            pcname "I guess so. Do you feel better now?"
            "She smiles uneasily."
            show K Happy at left
            K "I'm glad we don't have to hide anymore."
            pcname "Me too."
            "Glancing at the clock, you gasp."
            show chelsea shocked
            if club == "track":
                pcname "Shit! I need to clock in!"
            elif club == "cheer":
                pcname "Oh no, I didn't clock in yet!"
            elif club == "yearbook":
                pcname "I'm going to be late clocking in!"
            "Kate giggles as you rush to the time clock."
            "You start your shift, knowing you'll have time to talk to her later."
            hide K Happy
            hide chelsea
            with dissolve
            jump events_end_period

label kate_routelock:
    show bg CityD with dissolve
    $ clothes = 'cafe'
    show chelsea happy at right with moveinright
    show K Casual Happy at left with moveinleft
    "When you get to work, Kate's waiting outside, a smile on her face."
    K "I figure since everyone knows, there's no reason I can't wait out here for you!"
    "You smile back."
    pcname "That's true!"
    "Still grinning, she grabs your hand and pulls you inside."
    hide chelsea
    hide K Casual Happy
    with dissolve
    show bg Cafe with dissolve
    show chelsea at right with moveinright
    show K Casual Happy at left with moveinleft
    K "I was thinking, this weekend, maybe we could--"
    "Her voice drops off as you walk into the crew room."
    K "We could..."
    show chelsea sad
    show K Casual Sad at left
    scene black with dissolve
    "Your mouth hangs open in shock. Two lockers - yours and Kate's - are covered in unsavory words."
    show bg CLRS1 with dissolve
    "\"Dyke\", \"carpet muncher\", \"homo\"..."
    "Glancing at Kate, you see her eyes once again brimming with tears."
    K "Who would... Why would they..."
    show bg CLRS2 with dissolve
    "Harper" "Did you decide to decorate your lockers? How appropriate."
    "Turning, you see Harper, Zoey, and Emma standing in the doorway."
    "Harper wears her familiar grin, while Zoey and Emma seem just as shocked as you and Kate."
    "Harper" "What's the matter? Aren't you {i}proud{/i} of your relationship?"
    "She walks further into the room, laughing. The other girls follow her in, spreading out to stand on either side of her."
    "Harper" "Are you crying again, Kate? Doesn't your girlfriend make you happy anymore?"
    show bg CLRS3 with dissolve
    "As shock gives way to anger, you open your mouth to speak - just in time to see Emilia pause in the doorway."
    if club == "track":
        pcname "You think this is funny, Harper?"
    elif club == "cheer":
        pcname "Oh, you sure got us. Very clever of you."
    elif club == "yearbook":
        pcname "Don't worry, Kate. She's just a bully..."
    "Harper" "What, you don't like the decorations?"
    "Harper" "But I worked so hard on them!"
    "Emilia's eyes narrow."
    if club == "track":
        pcname "Like when you ruined Kate's cupcakes?"
    elif club == "cheer":
        pcname "Oh, it's very clever. Just like with Kate's cupcakes..."
    elif club == "yearbook":
        pcname "I bet she's the reason your cupcakes were destroyed too!"
    "Harper laughs."
    "Harper" "It's not {i}my{/i} fault Kate's so clumsy."
    "Harper" "So what if I might've left the broom on the floor? She should look where she's going."
    "Emilia takes a step closer, her arms crossed over her chest."
    "Harper" "Besides, Emilia should've asked {i}me{/i} to make those cupcakes."
    if club == "track":
        pcname "And you pulled those buttons off her shirt too, didn't you?"
    elif club == "cheer":
        pcname "What about her shirt. Was that you too?"
    elif club == "yearbook":
        pcname "And her shirt...?"
    "Harper laughs again."
    "Harper" "The look on her face..."
    "Emilia" "I think that's enough."
    "Zoey and Emma turn toward the doorway, faces pale."
    "Harper stares straight ahead, eyes wide with shock."
    show bg CLRS4 with dissolve
    "Emilia" "I've heard all I need to."
    "Emilia" "Harper, this is no way for one of my employees to act."
    "Emilia" "Bullying your coworkers, purposefully sabotaging them, wasting inventory..."
    "She motions to the lockers."
    "Emilia" "And now defacing company property?"
    "Emilia" "Come to my office and sign your termination slip. You're done working here."
    "Harper spins around, nearly sobbing."
    "Harper" "But... But Emilia, I--"
    "Emilia" "I said I've heard enough. Follow me. {i}Now.{/i}"
    scene bg Cafe with dissolve
    "As Emilia and Harper leave the room, Zoey and Emma rush forward."
    show K Casual Sad at left with dissolve
    show chelsea sad at right with dissolve
    show Emma Worried at midright with dissolve
    show Zoey Worried at midleft with dissolve
    "Zoey" "Here, let us help you clean this up!"
    "Zoey grabs a cloth and Emma grabs some cleaning spray."
    "Emma" "Yeah, Katie, we're really sorry! I can't believe she did this..."
    show chelsea angry
    pcname "But you're her friends. You've always went along with everything she said or did."
    "Zoey" "I know, but..."
    show chelsea blank
    show Emma Neutral
    "Emma" "You don't understand, [pcname]. You're still pretty new here."
    "Emma" "Harper has always run the show here. If she didn't like someone, she made {i}sure{/i} they quit."
    show Emma Blank
    show Zoey Angry
    "Zoey" "Yeah! There was no {i}way{/i} anyone could stand up to her. And then... Well, you {i}did{/i}."
    show Zoey Blank
    "As they speak, they begin washing the paint from the lockers."
    show Emma Laugh
    "Emma" "Yeah, that was {i}amazing{/i}! You really put her in her place!"
    show Emma Happy
    show Zoey Laugh
    "Zoey" "And right in front of Emilia too!"
    show Zoey Happy
    "With the paint gone, they stand back and smile at both of you."
    show Zoey Laugh
    "Zoey" "Things will be great around here now that she's gone."
    show Zoey Blank
    show Emma Worried
    "Emma" "And we're really sorry, Katie. We didn't like seeing you cry but..."
    show Zoey Worried
    "Zoey" "We didn't want her to treat us that way too. It's awful, but you understand, right?"
    show K Casual Blank
    "Kate glances at you, then nods."
    show K Casual Embarrassed
    show chelsea happy
    K "I understand. I didn't want [pcname] to get involved because I thought she'd be bullied too."
    "They nod their heads sympathetically."
    show Emma Neutral
    "Emma" "We better get out there and check on our tables. But... We can all be friends now, right?"
    show K Casual Happy
    "Kate nods."
    show K Casual Happy at left
    K "Of course!"
    "As Emma and Zoey leave, Kate turns toward you."
    K "I'm sorry I kept asking you not to say anything before."
    K "I didn't realize everyone else was just afraid of Harper... If you hadn't stood up for us, she'd still be terrorizing everyone."
    show K Casual Laugh at left
    "She grins."
    K "I think things are going to be a lot better now. We don't have to hide anything and nobody is going to say anything about it!"
    "Jumping toward you, she wraps her arms around your back and presses her face against your neck."
    K "Let's get to work. It's going to be a great night!"
    "Congrats! You've Reached the end of Kate Romance Route! There is more to come so stay tuned on our Patreon!"
    hide K Casual Laugh
    hide chelsea
    with dissolve
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
