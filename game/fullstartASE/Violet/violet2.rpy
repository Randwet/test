label violetlunch4:
    show bg Cafeteria with fade
    $ violetscenes += 1
    show chelsea at right with moveinright
    show V School Blank at left with moveinleft
    "At lunch, you sit in your normal spot with Violet."
    if violetdate1place == "apartment":
        V "So I've been meaning to tell you..."
        show V School Pout at left
        V "You really need a better mattress! My back has been so sore since I slept at your place..."
        if club == "track":
            show chelsea confused
            pcname "Maybe next time you should try the couch?"
        elif club == "cheer":
            show chelsea happy
            pcname "I know what you mean..."
        elif club == "yearbook":
            pcname "Oh! Sorry..."
    elif True:
        show V School Smile at left
        V "So I've been meaning to ask what you thought of the restaurant?"
        menu violetlunch4prevdate:
            "It was great!" if True:
                show chelsea happy
                pcname "I had a great time!"
                V "I {i}knew{/i} you'd like it!"
            "It was expensive!" if True:
                show chelsea sad
                pcname "It was really expensive..."
                show V School Pout at left
                V "Oh, don't tell me you're still caught up on {i}that{/i}..."
    show chelsea blank
    show V School Smile at left
    V "Anyway, I was thinking we should hang out again."
    if violetdate1place == "apartment":
        V "There's this restaurant I've been dying to try..."
    elif True:
        V "It's another restaurant, so I can pay you back for last time!"
    menu violetlunch4seconddate:
        "Sure, why not?" if True:
            show chelsea happy
            V "Perfect!"
        "Actually, I already have plans." if True:
            "Violet waves her hand dismissively."
            show V School Blank at left
            V "Please, whatever it is, you know you'll have more fun with me."
    show V School Smile at left
    V "I'll text you the address on Saturday."
    show V School Annoyed at left
    V "Hopefully by then we'll have a new housekeeper."
    show chelsea confused
    pcname "A new housekeeper?"
    show V School Blank at left
    show chelsea blank
    V "We had to fire the old one and it's been {i}awful{/i}."
    show chelsea confused
    pcname "Was she stealing or something?"
    show V School Smile at left
    V "Oh, no, nothing like that..."
    show chelsea blank
    show V School Pout at left
    V "She just kept calling off. I think her kid was in the hospital or something."
    menu violetlunch4maid:
        "Why would you fire her for that!?" if True:
            show chelsea shocked
            show V School Pout at left
            V "{i}I{/i} didn't fire her - my father did."
            show V School Blank at left
            V "Besides, it's not our fault the kid was sick, and the house still needs cleaned!"
        "That makes sense; what did she expect?" if True:
            $ violetmaid = False
            show V School Suprised at left
            V "I know!"
            show V School Pout at left
            V "The worst part was that my mother {i}insisted{/i} I figure out how to do laundry."
            show V School Annoyed at left
            V "So I actually had to go online and watch a {i}video{/i} just to figure it out."
            V "And then I had to {i}touch{/i} all of that dirty laundry!"
            V "I did one batch and then {i}refuse{/i} to do any more. Ugh!"
    show chelsea blank
    pcname "Unbelievable..."
    show V School Blank at left
    V "Anyway, I'm sure we'll have a new maid soon, so it should be fine."
    "You pick at your food, imagining what it must be like to have Violet's problems."
    $ violetdateflag = True
    jump events_end_period


label violetdate2:
    $ violetscenes += 1
    $ clothes, hair = casualwear
    show bg CityD with dissolve
    show chelsea at right with moveinright
    play sound PhoneVibration
    "As you step out of your apartment, you feel your phone vibrate."
    play sound PhoneVibration
    $ violetdateflag = False
    call screen TextingScene("Violet",
    [
        TextMessage("Gokana @ 313 E Beaufort St"),
        TextMessage("See you soon!")
    ])
    "You punch the address into your GPS - it's pretty far away."
    menu violetdate2go:
        "Go to lunch." if True:
            pass
        "Make an excuse." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("Sorry I have the flu", sender = False),
                TextMessage("Maybe some other time?", sender = False)
            ])
            "A few minutes go by with no response, so you put your phone away and head out."
            jump events_end_period
    "Sighing, you walk back into your apartment."
    hide chelsea with moveoutright
    show bg HomeE with dissolve
    "Walking to the restaurant will take a while, so there's no point in going anywhere now."
    "Turning on the TV, you flip through the channels for a while, but nothing seems interesting."
    "There are some dishes in the sink, so you wash those quick and then tidy up the rest of the apartment."
    "When you finish, you look around and feel a sense of accomplishment; it's nice to live in a clean space."
    "Glancing at your clock, you decide to start walking to the restaurant now. It's a long walk, after all."
    show bg CityD with fade
    "Almost an hour later, you're glad you got an early start; it took even longer than you expected."
    "According to your GPS, you should be almost there, so you start looking at the buildings more closely."
    "Across the street is a modern looking place with very dark windows - you're not even sure if they're actually open, but the sign says Gokana."
    "A second glance at the GPS confirms that you've found it, so you cross the street and tentatively try the door."
    "You're almost surprised when it opens."
    show chelsea at right with moveinright
    "Stepping inside, you realise it's a very fancy sushi bar."
    show bg DatePlace with dissolve
    "Hostess" "Name?"
    if club == "track":
        show chelsea shocked
        pcname "Oh, um... I'm not sure if we have a reservation..."
    elif club == "cheer":
        show chelsea confused
        pcname "Mine?"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Uh..."
    "Hostess" "I apologize, but we serve by reservation {i}only{/i}."
    show chelsea blank
    pcname "Oh... My friend Violet told me to meet her here..."
    "Hostess" "Hm."
    "She scans a list on her podium, smiling after a moment."
    "Hostess" "Ah, I see. Your name is [pcname]?"
    if club == "track":
        show chelsea happy
        pcname "That's me!"
    elif club == "cheer":
        show chelsea happy
        pcname "It is."
    elif club == "yearbook":
        show chelsea happy
        pcname "Yes...?"
    "Hostess" "Excellent. Right this way, miss."
    show chelsea blank
    "She leads you through the restaurant. You can tell by the decor that you were right; it's going to be very expensive."
    if club == "track":
        "You can't help feeling a little nervous and out of place."
    elif club == "cheer":
        "In some ways, that makes you feel excited - you've never been somewhere like this before."
    elif club == "yearbook":
        "You glance about nervously, certain that everyone can tell you don't belong here."
    "As you near the back of the restaurant, you're relieved to recognize Violet's dark hair."
    "She's sitting alone, looking at her phone, but she looks up as you reach the table."
    "Hostess" "Your guest, miss."
    "She motions for you to take a seat."
    "Hostess" "Your server will be with you momentarily. Please look over the menu at your convenience."
    hide chelsea with dissolve
    show bg VDScene2 with dissolve
    "As she retreats, Violet sighs loudly."
    V "It took you long enough! I was fashionably late, but you're just {i}late{/i}."
    if club == "track":
        pcname "I guess I could've run here, but I didn't think this was the kind of place where you can show up sweaty."
    elif club == "cheer":
        pcname "This place looks great, but it was a {i}long{/i} walk."
    elif club == "yearbook":
        pcname "Sorry... I didn't realize how long it took to walk here..."
    V "I forgot you walk. You should've made me pick you up. We could've pretended I was your chauffer."
    "With a whimsical wave, she watches your reaction."
    menu violetdate2_chauffer:
        "I'd like that." if True:
            "She smiles as if you just told her a secret."
            $ violetsubdom -= 1
        "You didn't offer." if True:
            show bg VDScene3 with dissolve
            "She laughs."
            V "You can't expect me to remember that you walk everywhere. Who {i}does{/i} that?"
        "Wouldn't you rather I was the chauffer?" if True:
            "Her smile deepens; she clearly likes the idea."
            $ violetsubdom += 1
    show bg VDScene1 with dissolve
    V "So what are you having?"
    "You glance over the menu, which doesn't appear to have the prices listed."
    show bg VDScene3 with dissolve
    if violetdate1place == "apartment":
        V "Oh, don't worry about the prices; I'm paying!"
        "You feel like you should put up more of a fight, but you have a strong suspicion you can't afford to."
        if club == "track":
            pcname "Wow, thanks!"
        elif club == "cheer":
            pcname "Aww, you're spoiling me!"
        elif club == "yearbook":
            pcname "Th-Thank you..."
    elif True:
        V "Don't forget it's my treat today!"
        if club == "track":
            pcname "Right! How could I forget?"
        elif club == "cheer":
            pcname "Aww, you're spoiling me!"
        elif club == "yearbook":
            pcname "Right..."
    show bg VDScene1 with dissolve
    "You read over the menu slowly, taking in all of the descriptions."
    "Words like \"lavish\" and \"adorned\" fill the page. One item is even described as having a \"spectrum of surprising yet pleasant flavors\"."
    show bg VDScene2 with dissolve
    V "Hmmm... I just can't decide."
    V "Maybe you could pick for me?"
    "She tilts her head, smiling sheepishly at you."
    menu violetdate2_order:
        "Sure, no problem!" if True:
            $ violetchoosefood = False
            $ violetsubdom -= 1
            show bg VDScene3 with dissolve
            V "Great!"
            "You browse the menu more intently, determined to find the perfect dish for each of you."
            show bg VDScene1 with dissolve
            "Near the bottom, you see an \"omakase\" option and an explanation that the chef will choose the best of their offerings for you."
            "It feels like cheating, but it seems like a safe bet."
            "Server" "I've brought water for you, ladies."
            "She sets the glasses on the table and smiles."
            "Server" "What will we be having this afternoon?"
            pcname "The omakase, please. For both of us."
        "You're more experienced. Why don't you order for us?" if True:
            $ violetchoosefood = True
            $ violetsubdom += 1
            show bg VDScene1 with dissolve
            V "If that's what you want..."
            "She sets the menu aside. Despite what she said, she clearly knows what she wants."
            "She sets the glasses on the table and smiles."
            "Server" "What will we be having this afternoon?"
            V "We'll each have the omakase, but please tell the chef that we don't want any mackerel."
    "Server" "Excellent choice; the best of everything."
    "Server" "I'll let the chef know and he'll be right with you."
    V "The omakase is the most expensive thing on the menu."
    if club == "track":
        pcname "Really? I couldn't tell."
    elif club == "cheer":
        pcname "Oh, really?"
    elif club == "yearbook":
        pcname "O-Oh! I didn't realize..."
    show bg VDScene3 with dissolve
    V "It's what I usually order."
    show bg VDScene1 with dissolve
    "A man arrives at the table and bows to each of you."
    "Chef" "Hello, ladies. I am Sakai and I will be personally preparing the best we have to offer for you today."
    "Chef" "First I have our dark miso soup with littleneck clams and nameko mushrooms."
    "He places a small bowl before you; it smells delicious."
    "Chef" "Please enjoy."
    "He bows again and leaves the table."
    show bg VDScene3 with dissolve
    V "We're here for lunch, so he's only a junior chef, but he usually has good taste."
    "The soup tastes even better than it smells. You savor each spoonful."
    show bg VDScene1 with dissolve
    "Just as you set the empty bowl aside, the chef returns."
    "Chef" "Next will be a palate awakener of steamed monkfish liver with our house ponzu sauce."
    "He sets a wooden box in the middle of the table. Inside rests two small bowls, each with a decorative drizzle of sauce and a dollop of pinkish-orange... something."
    "Chef" "Please eat in small bites and enjoy the delicate, fatty texture of the liver."
    "He leaves you with another bow. You look at Violet uncertainly."
    show bg VDScene3 with dissolve
    V "It's like foie gras and caviar had a baby; it's delicious!"
    "She grabs her own bowl and digs in, closing her eyes and sighing happily with the first bite."
    "Curious but still hesitant, you do the same, taking a very small bite."
    show bg VDScene1 with dissolve
    "You're pleasantly surprised by the flavor - creamy, buttery, but with an oceany taste you can't quite describe."
    show bg VDScene3 with dissolve
    V "See? It's amazing..."
    "Once again, you're so engrossed in the experience that you eat in silence, both lost in the flavors of the food."
    "Chef" "I see you're finished. How was the monkfish?"
    V "Superb. I always {i}love{/i} that one."
    "Chef" "Excellent! Now, I've brought I selection of sashimi for you to try."
    "He goes over the fish briefly, telling you the best qualities of each of them. It's clear that he puts a lot of thought into the foods he serves."
    "Chef" "Please enjoy. I will bring dessert when you're finished."
    V "Oh, try the sea urchin first!"
    "Violet leads you in trying each of the fish - or, in some cases, fish eggs. You like all of them, though you're not sure you'd order them again."
    show bg VDScene1 with dissolve
    V "By the way, that housekeeper I was telling you about kept calling my father, {i}begging{/i} for her job back."
    if violetmaid == True:
        V "You'll be happy to know that my father gave in."
        pcname "That's great!"
    elif True:
        show bg VDScene2 with dissolve
        V "Can you believe my father actually let her come back?"
        pcname "Seriously?"
    show bg VDScene1 with dissolve
    "Chef" "Ladies, I see you're still enjoying the food?"
    "Suddenly, Violet scrunches up her face."
    show bg VDScene2 with dissolve
    V "Eww, this is {i}definitely{/i} mackerel!"
    "Looking very concerned, the Chef looks down at the plate."
    show bg VDScene1 with dissolve
    "Chef" "Oh, I apologize. That fish is called Houbou and to some palates it can be quite similar to mackerel."
    V "Ugh, it's fine..."
    "Chef" "I apologize again. I will bring your desserts next. Today I've selected gourmet mochi ice cream with plum wine jelly."
    "As he walks away, Violet grimaces again."
    show bg VDScene2 with dissolve
    V "He should've known better. I said no mackerel; why would he send something that tastes like mackerel!?"
    if violetchoosefood == False:
        menu violetdate2playerchose:
            "Apologize to her." if True:
                show bg VDScene1 with dissolve
                $ violetsubdom += 1
                if club == "track":
                    pcname "Sorry. I guess I shouldn't have picked the omakase..."
                elif club == "cheer":
                    pcname "Guess I should apologize too; I ordered for you."
                elif club == "yearbook":
                    pcname "S-Sorry you didn't like what I ordered..."
            "Tell her she's being rude." if True:
                show bg VDScene1 with dissolve
                $ violetsubdom -= 1
                if club == "track":
                    pcname "Come on! It seems like an honest mistake, and he clearly cares what he serves!"
                elif club == "cheer":
                    pcname "That was really rude of you. Everything was delicious!"
                elif club == "yearbook":
                    pcname "But it {i}wasn't{/i} mackerel. And you were really rude..."
    elif violetchoosefood == True:
        menu violetdate2playerchoose:
            "Agree with her." if True:
                show bg VDScene3 with dissolve
                $ violetsubdom += 1
                if club == "track":
                    pcname "Guess that's what happens when you get the junior chef..."
                elif club == "cheer":
                    pcname "And that excuse about \"some palates\" thinking they're similar? Seriously?"
                elif club == "yearbook":
                    pcname "I'm glad you spoke up; I have a really hard time with that."
            "Tell her she's being rude." if True:
                $ violetsubdom -= 1
                if club == "track":
                    pcname "Come on! It seems like an honest mistake, and he clearly cares what he serves!"
                elif club == "cheer":
                    pcname "That was really rude of you. Everything was delicious!"
                elif club == "yearbook":
                    pcname "But it {i}wasn't{/i} mackerel. And you were really rude..."
    show bg VDScene2 with dissolve
    V "Ugh, whatever... At least the rest of the meal was good."
    "The chef returns a few minutes later with two plates."
    "Chef" "There are three flavors of ice cream: mango ginger, matcha, and strawberry basil. On the side is our signature plum wine jelly, cubed with mint leaves."
    "He bows one last time."
    "Chef" "It was my pleasure serving you this evening. I hope you've enjoyed your meals."
    "Violet rolls her eyes as he walks away."
    show bg VDScene1 with dissolve
    V "I've had this before; it's really good."
    "She's right; the flavors are perfect. And the jelly - small cubes of gelatin, served with whipped cream and mint leaves - is surprisingly flavorful too"
    "When the server brings the check, Violet slides her card inside without looking at it."
    show bg VDScene3 with dissolve
    V "I'd offer you a ride home, but I'm not headed that way. My mom is {i}insisting{/i} I go shopping with her."
    show bg VDScene2 with dissolve
    V "Apparently, her therapist says we need a \"mother-daughter day\" so we can \"bond\"."
    V "I tried to tell her I had plans, but she said I'd have more fun spending the day with her."
    "At least you know where she gets it from, you suppose."
    V "When I tried to argue with {i}that{/i}, she threatened to forget to deposit my allowance in my account this month."
    show bg VDScene1 with dissolve
    "Sighing loudly, she grabs her phone off the table."
    "You follow her lead, certain that you'd never find your way out on your own."
    V "So off I go! This was fun!"
    pcname "Yeah, thanks for lunch!"
    "She smiles."
    V "My pleasure!"
    show bg black with dissolve
    "As she gets into her car, you pull up your GPS and try to find your way home."
    $ acts = 1
    jump events_end_period

label violethomeroom1:
    $ violetscenes += 1
    "You walk into homeroom and take your seat."
    show chelsea at right with moveinright
    "As usual, Violet isn't there when the first bell rings."
    "A few minutes later, she strolls into the classroom. You try to wave, but she doesn't seem to notice."
    "She sits down in front of you and holds up her cell phone, using the front camera to check her makeup."
    "Smiling to yourself, you pull out your english book. You didn't start the assigned readings yet, so you figure you might as well look them over."
    show V School Smile at left with moveinleft
    V "[pcname]."
    "You glance up; Violet has turned to face you."
    show V School Pout at left
    V "Look how tired my skin looks. I really need a spa day..."
    "You're not sure what she means - her skin looks perfect, as always."
    if club == "track":
        pcname "I've always wondered what that would be like..."
    elif club == "cheer":
        show chelsea happy
        pcname "I would {i}love{/i} to go just once..."
    elif club == "yearbook":
        show chelsea confused
        pcname "Is it really worth it?"
    show V School Suprised at left
    show chelsea blank
    V "Wait. Hold on. You've {i}never{/i} been to the spa!?"
    if club == "track":
        pcname "It's never really been my thing, I guess."
    elif club == "cheer":
        pcname "I've always wanted to, but..."
    elif club == "yearbook":
        pcname "N-No..."
    show V School Blank at left
    "Shaking her head, she turns back around and pulls out her phone."
    "You're not sure what to make of that, so you go back to your reading."
    show V School Smile at left
    V "Okay, that's it."
    show chelsea confused
    "Startled, you look back up to see that Violet's turned back toward you."
    V "Cancel your plans for tonight because we're going to the spa!"
    menu violethomeroom1_spa:
        "You can't just make plans without telling me!" if True:
            show chelsea angry
            show V School Annoyed at left
            "Rolling her eyes, Violet sneers."
            V "You have {i}got{/i} to be more spontaneous, [pcname]!"
        "But I can't miss work!" if True:
            show chelsea shocked
            show V School Pout at left
            "She looks perplexed, like you suddenly spoke different languages."
            V "Just call off. What's the big deal?"
        "Really? That's amazing!" if True:
            show chelsea happy
            show V School Smile at left
            "She smiles smugly."
            V "I know; I'm the best!"
    menu violethomeroom1_spa2:
        "I guess I can call off this once..." if True:
            show V School Smile at left
            show chelsea happy
            V "Yes!"
            V "Alright, meet me by my car after school!"
            $ wenttowork = True
            jump violetdate3
        "Thanks, but I really can't miss work..." if True:
            show chelsea blank
            show V School Pout at left
            V "Seriously?"
            show V School Annoyed at left
            V "Fine, but you're the one missing out!"
            "You can tell she's annoyed, but what did she expect?"
            scene bg black
            "You sit together at lunch, but she barely says a word."
            "She'll get over it eventually, you're sure, but until then it looks like lunch will be a lot quieter..."
            jump events_end_period

label violetdate3:
    scene bg black
    show bg CityD with dissolve
    $ clothes, hair = casualwear
    "After school, you call the [job] and tell them you won't be in."
    $ skippedwork = True
    "You feel guilty, but Violet insisted..."
    "Just as you start to wonder where Violet is, you hear the car doors unlock."
    show chelsea at right with moveinright
    "She strolls up to the car and grins."
    show V Casual Smile at left with moveinleft
    V "Well, come on!"
    "You get in and buckle up, looking around her car."
    "It has every convenience feature you can think of - which doesn't really surprise you anymore."
    V "I'm so excited to be the one to introduce you to spa treatments!"
    V "You're in for some much-need self-care, [pcname]!"
    if club == "track":
        "\"Self-care\" always sounded like an excuse for spending way to much money on yourself, but you have to admit you're excited too."
    elif club == "cheer":
        show chelsea happy
        pcname "I can't wait!"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Okay..."
    show V Casual Blank at left
    show chelsea blank
    "You look around while she drives, listening as she points out some of her favorite places."
    show V Casual Smile at left
    V "Here we are!"
    show V Casual Blank at left
    "She swings into a parking space, and you step out to stretch while she gathers her purse and her cell phone."
    show V Casual Smile at left
    V "Ready?"
    show chelsea happy
    pcname "Ready!"
    hide chelsea with moveoutright
    hide V Casual Smile with moveoutleft
    show bg black with dissolve
    "She leads you inside, barely giving you a moment to take in the large waterfall fountain in the entrance before approaching the front desk."
    "Receptionist" "Good evening, Miss Violet. We were expecting you. Please, right this way."
    "The receptionist steps around the counter and leads you through a set of doors. Inside, the rooms look like they belong in a palace."
    show bg Spa with dissolve
    "The air is warm and humid, but not stiflingly so."
    "You don't have much time to look around because you're quickly led into a side room."
    "Expecting something small, you're surprised to find yourself in a huge room with a raised dais in the center."
    "Either side of the room is lined with small, private alcoves with gauzy curtains and plush chairs."
    "Receptionist" "Your aesthetician will be by in about an hour, Miss Violet. Please enjoy the facilities until then."
    show V Casual Smile at left with moveinleft
    show chelsea happy at right with moveinright
    V "Sounds great!"
    show V Casual Blank at left
    "Receptionist" "Let me know if there's anything you need."
    hide V Casual Blank with moveoutleft
    pause 0.5
    show V Topless Blank at left with moveinleft
    "The receptionist excuses herself and, as soon as the doors shut behind her, Violet peels off her shirt and begins unhooking her bra."
    menu violetdate3_undress:
        "Follow her lead." if True:
            "Pulling your own shirt off, you watch as Violet continues stripping."
            "She pulls off her bra and tosses it on the bench next to her."
            "Next, she pulls her pants down and steps out of them."
            show chelsea shocked
            "Then, to your surprise, she peels her underwear off as well."
            "Unabashedly naked, she casually organizes her clothes on the bench and takes a robe from the wall."
            show chelsea blank
            "Wrapping herself in the robe, she glances at you and scowls."
            V "What are you waiting for?"
        "Ask what she's doing." if True:
            if club == "track":
                show chelsea confused
                pcname "So this is like a locker room?"
            elif club == "cheer":
                show chelsea confused
                pcname "So we just... strip?"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "W-What are we doing...?"
            "She sighs."
            V "Nobody is getting in the water with their clothes on, are they?"
            "Grabbing a robe from the hook, she tosses it toward you."
            V "Don't be weird about it; everyone gets naked here."
    show chelsea blank
    "Not wanting to embarrass yourself, you quickly strip and put on your robe."
    show chelsea at moveSprite(1.0, 1.5, 0.5)
    pause 1.0
    $ clothes = "naked"
    show chelsea at moveSprite(1.5, 1.0, 0.5)
    V "Let's start with the pool."
    hide V Topless Blank with moveoutleft
    "Making her way up to the platform in the middle of the room, she casually drops her robe and steps down into the water."
    if club == "track":
        pcname "What was the point in the robe?"
    elif club == "cheer":
        pcname "I guess we're going to be naked a lot..."
    elif club == "yearbook":
        pcname "I don't know about this..."
    "You say it quietly, shaking your head, and follow her lead."
    hide chelsea with dissolve
    scene bg black with dissolve
    show bg Spa11 with dissolve
    "The water is very warm - almost like a giant bathtub - and smells faintly of flowers."
    "As you step down into it, you realize it's deeper than you thought."
    "Though it's not deep enough to swim in, it goes almost to your chin when you sit on the middle step."
    "Violet tilts her head back and sighs; you find yourself quickly relaxing as well, despite your nudity."
    "Despite your first impression, it's not much like a bathtub at all."
    show bg Spa12 with dissolve
    "There's so much more water and, sitting rather than laying down, you're suddenly aware of how buoyant your breasts are."
    "In the water, they're almost weightless - as if someone else is holding them up for you."
    "You can almost imagine warm, soft hands wrapping around you and lifting them gently..."
    V "So what do you think of the soaking pool?"
    show bg Spa13 with dissolve
    "Your eyes flutter open - when did you close them? - and you see Violet looking at you expectantly."
    menu violetdate3_react:
        "It's amazing!" if True:
            show bg Spa14 with dissolve
            V "I know, right? Honestly, it might be my favorite part..."
        "It's a little weird being naked..." if True:
            show bg Spa15 with dissolve
            "She laughs."
            V "You're adorably uncultured, you know."
    show bg Spa16 with dissolve
    "She stands suddenly, water running down her body and settling around her hips."
    V "I'm a little thirsty, though. Do you need a drink?"
    menu violetdate3_drink:
        "I can get it for you." if True:
            $ violetsubdom += 1
            $ violetgetsdrink = "False"
            show bg black with dissolve
            "Stepping nervously out of the pool, you notice a stack of towels."
            menu violetdate3_towel:
                "Use a towel." if True:
                    "Grabbing one from the top, you quickly wrap yourself up and walk down the steps."
                "Don't bother." if True:
                    "Not wanting to seem uncomfortable, you ignore the towels and descend the stairs."
            "On the other side of the dais are two tables, one with snacks and one with drinks."
            "Approaching the drink table, you see that there are several pitchers of water, each with different fruits and herbs."
            "One has lemons, another has watermelon, and a third has cucumbers. You can't tell what the green leaves are, but there's some in each as well."
            pcname "Which one would Violet like..."
            "They all seem fine to you. Water with lemon is probably too common for Violet though..."
            "The cucumbers seem a little odd, but maybe that means they're fancier?"
            "Watermelon seems fine but it's mostly water already, so it couldn't have much flavor, could it?"
            if club == "track":
                pcname "Cucumber it is. She should've told me if she wanted something specific."
            elif club == "cheer":
                pcname "Hope she likes watermelon, I guess..."
            elif club == "yearbook":
                pcname "Lemon seems safe, right...?"
            "Pouring yourself a glass as well, you carry them both toward the pool."
            "There's something about the situation - the lavish scenery, perhaps - that makes you feel like you're a commoner serving an Empress."
            "You're surprised at how that makes you feel: both worthless and important all at once."
            "And, of course, Violet already acts like royalty..."
            "Passing her a glass, you step back into the pool."
        "Yes, thanks." if True:
            show bg black with dissolve
            $ violetsubdom -= 1
            $ violetgetsdrink = "True"
            "Smiling, Violet turns and ascends the steps, slowly revealing the rest of her wet, glistening skin."
            "Your eyes are drawn to her long, shapely legs and, as she turns back toward you, her perky breasts and pink nipples."
            "Now that she's out of the warm water, her nipples harden quickly, standing out from her skin and darkening slightly."
            "She walks to a table on the other side of the dais."
            "Selecting a pitcher, she carefully pours two glasses of water."
            "As always, she moves with a natural grace and confidence that you can't help but admire."
            "And, while she makes her way back to the pool, you also can't help but think about how nice it is to have Violet doing something for {i}you{/i} for once."
            V "Here you go!"
            "She passes you a glass and steps back down into the pool."
            V "Mmm, it's even warmer after the air hits your skin."
        "I'm okay." if True:
            show bg black with dissolve
            $ violetgetsdrink = "Null"
            "Smiling, Violet turns and ascends the steps, slowly revealing the rest of her wet, glistening skin."
            "Your eyes are drawn to her long, shapely legs and, as she turns back toward you, her perky breasts and pink nipples."
            "Now that she's out of the warm water, her nipples harden quickly, standing out from her skin and darkening slightly."
            "She walks to a table on the other side of the dais."
            "Selecting a pitcher, she carefully pours herself a glass of water."
            "As always, she moves with a natural grace and confidence that you can't help but admire."
            "You watch as she makes her way back to the pool, admiring the curve her waist and the way she sways her hips as she walks."
            "Catching yourself, you blush. What's gotten into you?"
            if katerelate == "girlfriend":
                "What about Kate?"
            if damienrelate == "love":
                "What would Damien think of you checking out another girl?"
            if mattsubmissive == True and defymatt == False:
                "What would Matt do if he found out?"
            "Dragging your eyes away, you try to focus on anything else until she's back in the pool."
    V "I wish we had more time today, but since we had to come after school there was only enough time to schedule facials."
    V "I hope you don't mind?"
    pcname "No, this is great!"
    V "Still... Oh!"
    V "Maybe we could give each other massages instead?"
    menu violetdate3_massage:
        "Sure, you go first." if True:
            $ violetgivesmassage = True
            $ violetsubdom -= 1
            "Violet moves up a step, bringing her nipples just above the waterline."
            "Wading to Violet's side of the pool, you sit beside her and turn away, uncomfortably aware that your own nipples are now exposed."
            show bg Spa21 with dissolve
            "She begins with your shoulders and neck, rubbing her thumb in smooth circles over your muscles."
            "Almost immediately, you feel the tension draining out of you."
            show bg Spa22 with dissolve
            "Minutes pass as she digs her fingers and thumbs into your back, massaging along your spine and across your hips."
            "When she finishes your lower back, she runs her hands up your sides, splaying her fingers around your sides and gently massaging your obliques."
            show bg Spa23 with dissolve
            "As her fingers travel up your ribs, you feel them graze the sides of your breasts, brushing gently against them."
            "She can't see it, but each time her fingers caress your sides, your nipples dip down into the water and back out again."
            "The competing sensations of the air and the warm water feel like tongues gently lapping across both nipples simultaneously."
            "A sudden heat radiates between your legs, making you grateful for the water. Without it, your arousal would be obvious."
        "Sure, I'll give you a massage." if True:
            $ violetgivesmassage = False
            $ violetsubdom += 1
            "Violet moves up a step as you wade to her side of the pool, bringing her nipples just above the waterline."
            show bg Spa251 with dissolve
            "As you sit beside her, she turns her back to you."
            "Starting with her neck, you rub your thumbs in small circles."
            "Violet relaxes under your fingers, occasionally humming or moaning softly when you find a good spot."
            V "Mmm, that's nice..."
            show bg Spa273 with dissolve
            "Working your way down her back, you feel your fingers graze the top of her ass. Blushing, you..."
            menu violetdate3_daring:
                "Test the waters." if True:
                    show bg Spa262 with dissolve
                    "...keep working the muscles. The butt is a muscle too, right?"
                    "She sighs happily as you rub the top of her cheeks, letting your thumbs dip in the very top of her crack."
                    "Your heart skips a beat; you feel like you're getting away with something you shouldn't."
                    "Working your way out, you massage her hips and slowly make your way up her sides."
                    show bg Spa284 with dissolve
                    "Pausing just beneath her breasts, you work your hands around a little further, occasionally brushing them against the underside of her breasts."
                    "Her breasts are so soft and smooth, you can't help but imagine how they would feel cupped in your hands."
                    "You're tempted to find out, but you don't want to push your luck."
                "Keep it friendly." if True:
                    "...move back to safer territory."
                    "You spend some more time working the muscles in her back and shoulders, but she doesn't seem very tense at all."
    if violetgivesmassage == True:
        show bg Spa24 with dissolve
    if violetgivesmassage == False:
        show bg Spa295 with dissolve
    "A knock on the door startles you both. It swings open an inch or two and someone speaks:"
    "Aesthetician" "Sorry to disturb you, but I wanted to let you know I'm almost ready to start your facials."
    "Aesthetician" "I'll be back in a few minutes, so please take your time getting ready on the couch."
    show bg black with dissolve
    "As she closes the door, you and Violet turn to face each other and laugh."
    "Still giggling, you move back to your side of the pool and get out."
    "Drying off, you each put your robe back on and step down from the dais."
    "Grabbing a cookie from the table, Violet takes a seat on the couch."
    if violetgivesmassage == False:
        V "I guess I owe you a massage later, huh?"
    elif True:
        V "Guess my massage will have to wait, huh?"
    pcname "I guess so!"
    V "Don't worry; I won't forget."
    "Another knock and the door swings open. The aesthetician steps inside with a small cart."
    show bg Spa31 with dissolve
    "Wheeling it to where you and Violet are sitting, she smiles down at you."
    "Aesthetician" "Ready for your facials, girls?"
    "Violet giggles while you nod."
    "Aesthetician" "Alright, then let's get started."
    "Aesthetician" "Make yourselves comfortable while I get the towels ready."
    "Following her instructions, you lean back against the cushions and tilt your head back a little, closing your eyes."
    "Aesthetician" "Perfect. Now, we're going to start with a steamed towel..."
    "She lays one across your face. It's very hot, but quickly cools to a pleasant warmth."
    show bg Spa32 with dissolve
    "Aesthetician" "And here's one for you."
    "Though you can't see her, you hear Violet sigh."
    "Aesthetician" "Let that sit for a few minutes and open up those pores!"
    "Aesthetician" "Then we're going to do a chemical peel to exfoliate any dead skin."
    "Aesthetician" "After that I'll give you each a nice, relaxing facial massage, followed by a face mask."
    "Aesthetician" "And we'll finish up with a nice moisturizer to seal all of our treatments in."
    "Aesthetician" "How does that sound?"
    pcname "Good!"
    V "Great!"
    show bg black with dissolve
    show bg Spa with dissolve
    "Aesthetician" "Perfect! Now then, I'll start with you."
    "Speaking softly, she gives you instructions in a gentle, soothing voice."
    "Aesthetician" "Just keep your eyes shut and relax. This might be a little cold..."
    "She removes the hot towel and gently applies the peel."
    "Despite her warning, the gel she smooths onto your face is just a little cool."
    "After the hot towel, it's a welcome sensation."
    "She spreads the gel over your face quickly and steps away."
    "Aesthetician" "And now you. Like I said, it might be a little cold..."
    "With your eyes shut, your other senses seem magnified. You're more aware of the air hitting the gel, and of its flowery, herbal scent."
    "You hear a faint rhythm and realize for the first time that they have music playing softly in the background."
    "Aesthetician" "Okay, now it's time to exfoliate. I'm going to gently wipe the peel off with a warm towel."
    "After minutes of cool air hitting the liquid on your face, the warmth of the towel feels wonderful."
    "She drags it over your face in long, gentle strokes, until all of the peel is gone."
    "Aesthetician" "Let your skin relax a moment while I take care of her."
    "There's a tightness to your skin now, as if it's stretched too far across your face."
    "It doesn't hurt, but it does feel strange. You wonder if it looks different."
    "Aesthetician" "Alright, now I'll apply a light oil and massage it into your skin."
    "Aesthetician" "This will replace the natural oils that the chemical peel removed with the dead skin cells."
    "Her gloved fingers move across your face with the lightest of touches."
    "It feels almost like she's afraid to touch you."
    "Slowly, though, her fingers press into your face, manipulating muscles you didn't realize you had."
    "She massages the bridge of your nose, relieving pressure from your sinus cavity."
    "Until the pressure is gone, you never realized how bad it felt."
    "Again and again she finds aches and pains you never recognized, soothing them away effortlessly."
    "When she's finished, you're filled with equal parts disappointment and contentment."
    "Aesthetician" "Now it's your turn."
    "You're so relaxed that you barely notice the passage of time as she massages Violet's face."
    "Only when she steps back to smooth on a sweet, citrus-scented moisturizer do you realize that several minutes must have passed."
    "Aesthetician" "Now, you won't want to get back in the water after this. Try to leave the moisturizer on as long as possible."
    "She steps away from you again, and you sigh contentedly. You've never felt so relaxed."
    "Aesthetician" "Alright, girls. Take your time getting up and dressing. I hope you enjoyed your facials?"
    "Violet murmurs her approval while you blink your eyes open a few times. Despite the dim lighting, the room seems very bright."
    pcname "It was great..."
    "You sit up slowly as the aesthetician leaves, begrudgingly pulling yourself out of your stupor."
    V "So, [pcname]..."
    if violetgivesmassage == True:
        V "I never asked if you liked your massage earlier."
    elif violetgivesmassage == False:
        V "Did you like giving me that massage earlier?"
    menu violetdate3_getmassagereact:
        "I like doing things for you." if True:
            $ violetsubdom += 1
            V "Is that so...?"
        "I like when you do things for me." if True:
            $ violetsubdom -= 1
            V "Is that so...?"
        "The whole day's been great." if True:
            "She frowns."
            V "Yeah, it's been really nice..."
    show V Topless Blank at left with moveinleft
    show chelsea at right with moveinright
    V "So, actually, I've been meaning to ask you something..."
    V "Do you have any... kinks?"
    show chelsea embarrassed
    "Blushing, you try to decide how to answer."
    menu violetdate3_kink:
        "I prefer to be served." if True:
            show chelsea happy
            $ violetsubdom -= 1
            $ violetrelate = "Sub"
            $ violetscenes += 1
        "I like being told what to do." if True:
            show chelsea embarrassed
            $ violetsubdom += 1
            $ violetrelate = "Dom"
            $ violetscenes += 1
        "None that I can think of." if True:
            show chelsea blank
    V "Really? See, I've been thinking and..."
    if violetsubdom > 6:
        jump violetbeyourdom
    elif violetsubdom < 3:
        jump violetbeyoursub

label violetbeyourdom:
    V "I really want someone to be my slave. I want someone who will do {i}whatever{/i} I tell them to do, just because it makes me happy."
    V "Does that... interest you?"
    menu violetdate3_behersub:
        "Definitely." if True:
            show chelsea happy
            $ violetrelate = "Dom"
            $ unlock_ach(kinkygf)
            if club == "track":
                "You already know that Violet is good at getting what she wants and you're happy to oblige."
            elif club == "cheer":
                "There's something about her natural confidence that really appeals to you."
                "You'll happily let her tell you what to do."
            elif club == "yearbook":
                "The thought of someone taking control and making all the decisions for you makes you feel... free."
            show V Topless Suprised at left
            V "Oh. Wow. I didn't think you'd actually say yes."
            show V Topless Blank at left
            V "We'll talk more about this later, okay?"
            hide V Topless Blank with dissolve
            hide chelsea with dissolve
            $ clothes, hair = casualwear
            "You get dressed in silence, neither of you sure what to say now."
            "Just as you're getting ready to leave, though, Violet speaks."
            show V Casual Pout at left with moveinleft
            show chelsea at right with moveinright
            V "Well? Don't just stand there, open the door for me!"
            show chelsea shocked
            pause 1.0
            show chelsea happy
            show V Casual Smile at left
            "Your heart jumps at her command; you think you're going to like this."
            scene bg CityN with fade
            "You open all of the doors for her as you leave the building. When you get to the parking lot, she tosses you her keys."
            show V Casual Smile at left with dissolve
            show chelsea happy with dissolve
            V "You'll drive me back to your apartment."
            hide chelsea with dissolve
            "Rushing to the passenger's side door, you start to open it for her."
            show V Casual Annoyed at left
            V "What? No, I'll be sitting in the back."
            "Switching to the back door, you hold it open while she climbs inside."
            show V Casual Smile at left
            V "You're being a very good girl, [pcname]. I'll have to think of a way to reward you."
            "You're surprised by how good her words make you feel, and the feeling lasts the whole way home."
            $ violetscenes += 1
        "I'd rather just be friends." if True:
            $ violetrelate = "Friends"
            V "Right. That's fine. I wasn't really interested in {i}you{/i} anyway, just the idea."
            "You get dressed in silence, neither of you sure what to say now."
            "The car ride back to your apartment is awkward, and you're relieved when she drops you off."
        "I don't want to talk about this." if True:
            $ violetrelate = "Enemies"
            V "Geez, you don't have to be like that."
            V "It's a pretty normal kink."
            "She exhales loudly."
            V "I don't know why I waste my time with you; we're nothing alike."
            "You get dressed in silence, broken occasionally by her complaints about you."
            "The car ride back to your apartment is awkward, and you're relieved when she drops you off."
            "You're pretty sure you'll have to find a new place to sit at lunch."
    $ acts = 1
    $ violetdateflag = False
    jump events_end_period

label violetbeyoursub:
    hide V Topless Blank
    show V SubTopless Happy at left
    V "I really want someone who can take charge. I want someone who will tell me {i}exactly{/i} what to do, and punish me if I don't."
    show V SubTopless Worried at left
    V "Does that... interest you?"
    menu violetdate3_beherdom:
        "Definitely." if True:
            show chelsea happy
            $ violetrelate = "Sub"
            if club == "track":
                "You've thought for a while that Violet needed to be put in her place, and you're more than happy to do it."
            elif club == "cheer":
                "Spoiled and rich, Violet is everything you've always wanted. And now she's offering to be {i}whatever{/i} you want."
            elif club == "yearbook":
                "The thought of taking charge makes you nervous, but imagining controlling someone like {i}Violet{/i}..."
                "{i}That{/i} makes you feel confident. Powerful."
                "It's a nice feeling."
            show V SubTopless Happy at left
            V "Oh. Wow. I didn't think you'd actually say yes."
            V "We'll talk more about this later, okay?"
            "You get dressed in silence, neither of you sure what to say now."
            scene bg Spa with fade
            $ clothes, hair = casualwear
            "Just as you're getting ready to leave, though, Violet speaks."
            show V SubCasual Blank at left with moveinleft
            show chelsea at right with moveinright
            V "Should I open the doors for you?"
            if club == "track":
                pcname "Of course."
            elif club == "cheer":
                show chelsea confused
                pcname "Did you have to ask?"
            elif club == "yearbook":
                pcname "I... Yes. Of course."
            show chelsea blank
            show V SubCasual Happy at left
            "She drops her eyes as she opens the door, her usually confident demeanor forgotten."
            scene black with dissolve
            "She opens all of the doors for you, including your car door, and drives you home."
            "By the time she opens the car door to let you out, you feel {i}important{/i}."
            show bg CityE with dissolve
            show V SubCasual Sad with dissolve
            V "I'll... see you at school?"
            show V SubCasual Blank
            show chelsea embarrassed at left with dissolve
            "Her sudden lack of confidence is exhilarating; you have all of the control."
            show chelsea blank
            "At the same time, you feel a certain responsibility now. This new dynamic depends entirely on you to maintain it."
            show V SubCasual Happy
            if club == "track":
                pcname "Let me think about what I want and we'll talk about this soon."
            elif club == "cheer":
                pcname "Of course. I'll let you know if I need anything before then."
            elif club == "yearbook":
                pcname "Right. That's good."
            scene black with fade
            "You walk into your apartment, your head swimming with ideas."
            $ violetscenes += 1
        "I'd rather just be friends." if True:
            $ violetrelate = "Friends"
            V "Right. That's fine. I wasn't really interested in {i}you{/i} anyway, just the idea."
            "You get dressed in silence, neither of you sure what to say now."
            "The car ride back to your apartment is awkward, and you're relieved when she drops you off."
        "I don't want to talk about this." if True:
            $ violetrelate = "Enemies"
            V "Geez, you don't have to be like that."
            V "It's a pretty normal kink."
            "She exhales loudly."
            V "I don't know why I waste my time with you; we're nothing alike."
            "You get dressed in silence, broken occasionally by her complaints."
            "The car ride back to your apartment is awkward, and you're relieved when she drops you off."
            "You're pretty sure you'll have to find a new place to sit at lunch."
    $ acts = 1
    $ violetdateflag = False
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
