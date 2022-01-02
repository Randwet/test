label violetdom1:
    show bg Cafeteria with fade
    show V School Pout at left with moveinleft
    show chelsea at right with moveinright
    if club == "track":
        "At lunch, you approach your normal table with Violet feeling less confident than normal."
    elif club == "cheer":
        "At lunch, you approach your normal table with Violet feeling giddy and nervous."
    elif club == "yearbook":
        "At lunch, you approach your normal table with Violet wondering what you've gotten yourself into."
    "Violet doesn't even glance your way when you sit down, leaving you wondering if you've done something wrong."
    "Maybe she's rethinking her offer?"
    if club == "track":
        "You consider bringing it up, but if she's supposed to be in charge..."
    elif club == "cheer":
        "The giddiness is fading as you try to figure out what to do."
    elif club == "yearbook":
        show chelsea sad
        "Sadness sweeps over you; the idea of letting her take control of everything was so nice..."
    show chelsea blank
    "Suddenly, Violet clears her throat."
    show V School Blank at left
    V "Well?"
    menu violetdom1_well:
        "Apologize." if True:
            show chelsea sad
            if club == "track":
                pcname "I-- I'm sorry?"
            elif club == "cheer":
                pcname "I'm sorry, Violet. What can I--"
            elif club == "yearbook":
                pcname "I-- I'm sorry! I... I..."
        "Ask what's wrong." if True:
            show chelsea confused
            if club == "track":
                pcname "Did I do something wrong?"
            elif club == "cheer":
                pcname "Um, I'm not sure what you want me to do...?"
            elif club == "yearbook":
                pcname "W-What...?"
            $ violetapproval -= 1
    show chelsea blank
    show V School Annoyed at left
    V "Ugh, do I really have to tell you to get my lunch?"
    show V School Pout at left
    "She tosses some cash at you, rattling off her order."
    show V School Blank at left
    V "I want bottled water, a ham sandwich with extra swiss, hold the mayo..."
    V "And for dessert... A fruit cup, unless they have something chocolate."
    show V School Pout at left
    "Relieved, you practically jump from the table to get her food."
    hide V School Pout with moveoutleft
    "The line for sandwiches is shortest, so you start there."
    "When the cafeteria worker asks what you want, you tell her:"
    menu violetdom1_sandwich:
        "Ham and swiss, no swiss and extra mayo." if True:
            pass
        "Ham and swiss, extra swiss and no mayo." if True:
            $ violetlunchsandwich = True
        "Ham and swiss, no ham and extra swiss." if True:
            pass
    "Sandwich in hand, you pick out a drink on your way to the dessert bar."
    menu violetdom1_drink:
        "Fruit punch." if True:
            pass
        "Chocolate milk." if True:
            pass
        "Bottled water." if True:
            $ violetlunchdrink = True
    "And then, looking over the dessert bar, you pick up..."
    menu violetdom1_dessert:
        "Fruit cup." if True:
            $ violetlunchdessert = True
        "Vanilla pudding." if True:
            pass
        "Carrot cake." if True:
            pass
    "Looking over your selections as you pay for her food, you feel pretty good about your choices."
    show chelsea happy
    if club == "track":
        pcname "Grinning, you deliver her tray."
    elif club == "cheer":
        pcname "Smiling, you deliver her tray."
    elif club == "yearbook":
        pcname "With a nervous smile, you deliver her tray."
    show chelsea blank
    "She looks over it critically, as if expecting you to get it wrong."
    show V School Pout at left with moveinleft
    V "Hmmm..."
    if violetlunchsandwich == True and violetlunchdrink == True and violetlunchdessert == True:
        $ violetapproval += 1
        show V School Smile at left
        V "Not bad."
        V "You're actually pretty good at this, [pcname]."
        show chelsea happy
        "You're surprised how happy that small praise makes you feel."
        "As you lay her change on the table, she shakes her head."
        show V School Blank at left
        V "Keep it. I hate small bills."
        show chelsea shocked
        pcname "Oh! Thanks..."
        show chelsea blank
        V "Go get yourself something to eat, since you did a nice job."
        $ Cash += 10
    elif True:
        $ violetapproval -= 1
        show V School Annoyed at left
        V "Seriously!?"
        if violetlunchsandwich == False:
            V "I said ham, extra swiss, and no mayo. How am I supposed to eat this?"
        if violetlunchdrink == False:
            V "I wanted {i}water{/i}. Ugh!"
        if violetlunchdessert == False:
            V "This isn't chocolate {i}or{/i} a fruit cup!"
        V "You really are useless, messing up the first task I give you..."
        show V School Smile at left
        "She smirks."
        V "I think I'll have to punish you to make a point."
        menu violetdom1_punishyou:
            "Tell her you deserve it." if True:
                show chelsea sad
                $ violetapproval += 1
                if club == "track":
                    pcname "I deserve it; that should have been easy!"
                elif club == "cheer":
                    pcname "Yes, please, I deserve it..."
                elif club == "yearbook":
                    pcname "I-I think you should..."
            "Tell her you'll do better." if True:
                show chelsea sad
                $ violetapproval -= 1
                if club == "track":
                    pcname "No! I'll do better next time!"
                elif club == "cheer":
                    pcname "But it's the first time I've messed up..."
                elif club == "yearbook":
                    pcname "N-No! I-- I'll--"
        show V School Blank at left
        V "Hmmm... Since it {i}is{/i} the first time, and it was {i}such{/i} an easy thing to do..."
        show V School Smile at left
        V "I think you should get down on your knees and apologize to me."
        show chelsea confused
        "You glance around the crowded cafeteria."
        if club == "track":
            show chelsea shocked
            pcname "Here?"
        elif club == "cheer":
            show chelsea shocked
            pcname "In front of all these people?"
        elif club == "yearbook":
            show chelsea embarrassed
            pcname "I-I don't..."
        show V School Annoyed at left
        V "Are you sorry or not?"
        menu violetdom1_knees:
            "Do it." if True:
                $ violetapproval += 1
                show chelsea embarrassed
                show V School Smile at left
                if club == "track":
                    "Swallowing your pride, you sink to your knees beside her."
                elif club == "cheer":
                    "Flushing, you sink to your knees beside her, trying desperately to pretend you're alone."
                elif club == "yearbook":
                    "Shaking, you sink to your knees beside her."
                "You try to think of what to say, but your mind is blank."
                "It feels as though {i}everyone{/i} must be watching you."
                show V School Blank at left
                V "Well?"
                show chelsea sad
                if club == "track":
                    pcname "I'm sorry I messed up. I'll do better next time."
                elif club == "cheer":
                    pcname "I'm sorry I got your order wrong, Violet. Please forgive me?"
                elif club == "yearbook":
                    pcname "I-I'm sorry! Please forgive me, Violet!"
                show V School Smile at left
                "Smiling, she nods."
                V "That will do. You can get up."
                "Standing quickly, you glance around. Nobody seems to be looking your way."
                "You're relieved, but strangely excited too. It's almost like you got away with doing something naughty in public."
            "Beg for mercy." if True:
                $ violetapproval -= 1
                show chelsea confused
                "Glancing around the crowded room, you shake your head."
                show V School Annoyed at left
                if club == "track":
                    pcname "Isn't that a little too much?"
                elif club == "cheer":
                    show chelsea shocked
                    pcname "Here? In front of everyone?"
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "B-But... I don't think I can..."
                "She rolls her eyes."
                show V School Pout at left
                V "Fine, I'll let it go this once..."
                show V School Annoyed at left
                V "But next time, you won't get off so easily."
        show V School Pout at left
        show chelsea blank
        V "Now go get yourself something to eat."
    "You pick your own food out quickly and hurry back to your table."
    "Violet is just finishing up her sandwich."
    show V School Blank at left
    V "So I was thinking of getting a new phone."
    show chelsea confused
    pcname "Didn't you just get that one?"
    show V School Pout at left
    V "Yeah, but... I don't really like the color."
    pcname "But you have a case on it."
    show V School Blank at left
    show chelsea blank
    V "I know, but I {i}know{/i} what it looks like under it."
    "You nod, eating while you listen."
    V "Anyway, my mom says I should wait because the newest one is coming out later this year, but I {i}really{/i} don't like this color..."
    "She slides her tray away, rolling her eyes."
    V "So I think I'm going to throw my phone on the driveway when I get home today."
    V "If it's broken, I'll {i}have{/i} to get a new one."
    "Just {i}thinking{/i} of dropping your phone makes you queasy."
    V "So I'm trying to decide what color I'm getting next."
    "Violet glances at her tray, then looks around the cafeteria."
    menu violetdom1_tray:
        "Dump her tray." if True:
            show chelsea happy
            $ violetapproval += 1
            if club == "track":
                pcname "Are you done with that?"
            elif club == "cheer":
                pcname "Can I dump that for you?"
            elif club == "yearbook":
                pcname "If you're done..."
            show V School Smile at left
            "She smiles."
            V "Oh. Yeah, you can dump it."
            "Carrying both of your trays to the garbage cans, you dump them and stack them neatly on the pile."
            "When you return to the table, Violet glances up from her phone."
            V "I'm glad you're taking this seriously, [pcname]."
            "Smiling, you nod."
            show chelsea embarrassed
            pcname "I want to make you happy."
            "The bell rings for the end of lunch, and Violet stands."
            show V School Blank at left
            show chelsea blank
            V "We'll have to compare schedules so you can carry my books for me too."
            "You nod again, imagining yourself walking her to all of her classes..."
            V "Bring a copy with you tomorrow."
            "As she saunters away, you grab your stuff and hurry to your next class."
        "Wait for her to tell you." if True:
            $ violetapproval -= 1
            "After a few more minutes of color debate, she waves her hand at the tray."
            show V School Annoyed at left
            V "Are you just going to let that sit there?"
            V "Ugh, why do I have to tell you to do {i}everything{/i}?"
            show chelsea sad
            "Carrying both of your trays to the garbage cans, you dump them and stack them neatly on the pile."
            "When you return to the table, Violet glances up from her phone."
            V "I don't think you're taking this seriously, [pcname]."
            "Startled, you shake your head."
            show chelsea shocked
            pcname "I'm trying!"
            "The bell rings for the end of lunch, interrupting your protests, and Violet stands."
            show chelsea blank
            V "Whatever. We'll have to compare schedules so you can carry my books for me too."
            "You nod again, imagining yourself walking her to all of her classes..."
            V "Bring a copy with you tomorrow."
            "As she saunters away, you grab your stuff and hurry to your next class."
    jump events_end_period

label violetdom2:
    if acts == 4:
        scene bg CityE with fade
    elif acts == 2 or acts == 3:
        scene bg CityD with fade
    elif acts <= 1:
        scene bg CityN with fade
    play sound PhoneVibration
    "As you're leaving work, you see a notification on your phone."
    "It's a text from Violet."
    call screen TextingScene("Violet",
    [
        TextMessage("I'm picking you up from work"),
        TextMessage("I'm here")
    ])
    "You walk outside and glance around, quickly spotting her car."
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    show V Casual Blank at left with moveinleft
    if club == "track":
        "As you approach, she gets out and tosses you the keys."
        "Snagging them out of the air, you peer at her questioningly."
    elif club == "cheer":
        "As you approach, she gets out and tosses you the keys."
        "Catching them with a startled yelp, you tilt your head quizzically."
    elif club == "yearbook":
        "As you approach, she gets out and tosses you the keys."
        "You try to catch them, but end up retrieving them from the ground as she laughs."
    V "You're going to drive me to the mall."
    "She stands by the back door until you open it for her."
    "Sliding in, she nods for you to close it."
    "You get in and buckle up, a little nervous about driving her expensive car so far."
    show V Casual Pout at left
    V "So, I have some rules for you to follow from now on..."
    menu violetdom2_rules:
        "Sounds interesting." if True:
            $ violetapproval += 1
            pass
        "I don't think so." if True:
            show V Casual Annoyed at left
            $ violetapproval -= 1
            V "You haven't even heard them yet!"
    show V Casual Pout at left
    V "First, if we're going somewhere, we're going like this. You're my chauffer."
    V "Second, you treat me like a lady. You open doors for me, pull my chair out... Things like that."
    "You glance at her in the rear-view mirror; her hand is waving in the air as she goes through her list."
    V "Third, you have to thank me for things - even when you're being punished."
    V "And last, you have to follow {i}all{/i} of my orders."
    V "If you don't like something I tell you to do, you have to ask me for mercy."
    V "And, of course, if you don't follow the rules, I'll have to punish you."
    V "Understood?"
    menu violetdom2_agree:
        "Agree." if True:
            show chelsea happy
            if club == "track":
                pcname "You got it."
            elif club == "cheer":
                pcname "Sounds good!"
            elif club == "yearbook":
                pcname "I can do that..."
        "Argue." if True:
            show V Casual Annoyed at left
            show chelsea confused
            $ violetapproval = 0
            if club == "track":
                pcname "I don't think so."
            elif club == "cheer":
                pcname "No, I don't like those rules."
            elif club == "yearbook":
                pcname "I... I don't think..."
            V "Seriously!? This is basic stuff!"
            pcname "I just--"
            V "Pull over!"
            show chelsea blank
            "You do as she says, pulling into the nearest parking space."
            "She bails out of the car and opens your door."
            V "Get out of the car."
            show chelsea confused
            "Startled and confused, you get out and watch as she slips behind the wheel."
            V "We'll talk about this later. Have a {i}great day{/i}!"
            "She slams the car door shut and drives off, leaving you staring after her."
            show chelsea blank
            if club == "track":
                pcname "Guess I'll get some running in today..."
            elif club == "cheer":
                pcname "Ugh, now I have to walk home?"
            elif club == "yearbook":
                show chelsea sad
                pcname "She was really mad..."
            "Thankfully, you're not too far from home, but you feel bad for how things went."
            "You're sure Violet will be angry for a while..."
            $ acts = 0
            jump events_end_period
    show V Casual Smile at left
    show chelsea happy
    V "Good."
    show chelsea blank
    show V Casual Pout at left
    "While you navigate to the mall, Violet taps away on her phone, mostly ignoring you."
    "It really does feel like you're her chauffer - almost beneath her notice."
    "When you pull into the mall and find a parking space, Violet doesn't look up, even as you get out of the car."
    menu violetdom2_car:
        "Get her door." if True:
            $ violetapproval += 1
            $ violetdatescore += 1
            show chelsea happy
            "Walking around the car, you open her door with a smile."
            show V Casual Smile at left
            V "Good. Glad you're taking this seriously."
            pcname "Thank you."
            "She smiles up at you and climbs out of the car."
            "You follow her to the mall, holding that door open as well."
            V "You're doing well at this, [pcname]."
            "A happy, giddy warmth fills your chest."
        "Wait for her to finish." if True:
            $ violetapproval -= 1
            $ violetdatescore -= 1
            "After a while, she glances up at you and swings the car door open."
            show V Casual Annoyed at left
            V "Seriously? We just talked about this!"
            "She climbs out of the car, slamming the door behind her."
            if club == "track":
                show chelsea sad
                pcname "You were on your phone, so--"
            elif club == "cheer":
                pcname "I was waiting for you to--"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Sorry, I--"
            show V Casual Pout at left
            V "Whatever. Let's go."
            "She walks ahead of you to the mall, heading toward the entrance."
            "You could rush ahead and get the door, but she seems like she's going to get it herself."
            menu violetdom2_door:
                "Get the door." if True:
                    $ violetapproval += 1
                    $ violetdatescore += 1
                    show chelsea happy
                    "Dashing in front of her, you push the door open."
                    show V Casual Smile at left
                    V "That's better!"
                "Let her do it." if True:
                    $ violetdatescore -= 1
                    show V Casual Annoyed at left
                    "She pauses in front of the door, glaring at you."
                    V "Are you going to get it?"
                    "You barely get the door open before she brushes past you."
    show chelsea blank
    show V Casual Blank at left
    show bg Shop with fade
    V "So... Where to start..."
    "You spend a few hours walking around the mall with her."
    "After each store, she passes you her bags to carry."
    "At first it's not too bad, but by the time you've covered half the mall it gets harder to juggle them all."
    "And, having already worked your shift at work, your feet are killing you."
    "Just when you think you can't carry one more bag, Violet turns to you."
    V "Alright, I think we're done now."
    "With a sigh of relief, you follow her toward the exit."
    "As you near the doors, you realize that your hands are completely full of bags; there's no way you'll be able to open the door."
    menu violetdom2_exit:
        "Try to get the door." if True:
            $ violetdatescore += 1
            if club == "track":
                "Gritting your teeth, you manage to lift your hand high enough to grab the door handle."
            elif club == "cheer":
                "Groaning with effort, you manage to grab the handle and ease it open."
            elif club == "yearbook":
                "Obviously struggling, you shuffle the bags around and heave them up until you can grab the handle."
            show V Casual Smile at left
            V "Very good, [pcname]."
            "Despite the heavy bags and your sore feet, her words fill you with pride."
        "Tell her you're carrying too much." if True:
            show chelsea embarrassed
            $ violetdatescore -= 1
            if club == "track":
                pcname "I don't think I can lift these enough to--"
            elif club == "cheer":
                pcname "Maybe if I put these down a sec..."
            elif club == "yearbook":
                pcname "Um, I don't..."
            show V Casual Annoyed at left
            V "Fine, whatever."
            "She pushes the door open herself, not bothering to hold it open for you."
            "You barely catch it with your foot and follow her out to the car."
    show chelsea blank
    show V Casual Blank at left
    if acts == 4:
        scene bg CityE with fade
    elif acts == 2 or acts == 3:
        scene bg CityD with fade
    elif acts <= 1:
        scene bg CityN with fade
    "After you've loaded the car up with her bags, you open her door for her."
    V "I'm going to order pizza; let's head back to your place."
    "While you start the car and drive home, Violet taps away on her phone."
    "You drive in silence while she orders your food. It's easy to imagine you're driving around a movie star."
    "You picture yourself driving Violet between appointments, helping her in and out of the car, and shielding her from all of the people eager to get a look at her."
    "Being able to be so close to someone other people are dying to just {i}see{/i}, even if you're basically a servant..."
    V "Finally."
    "Her voice cuts through your thoughts - you're practically home."
    "Since you don't usually drive, it feels a little strange to park at your apartment. Almost like it isn't yours."
    "You walk around the car to open Violet's door; she smiles at you."
    if acts == 4:
        scene bg CityE with fade
    elif acts == 2 or acts == 3:
        scene bg CityD with fade
    elif acts <= 1:
        scene bg CityN with fade
    "As you unlock the door to your apartment, Violet saunters in ahead of you and turns around."
    V "The pizza should be here soon, and we have to talk about your performance today."
    if violetdatescore > 1:
        show V Casual Smile at left
        "She smiles, pulling a small box from her bag."
        V "You were great!"
        if violetdatescore == 3:
            show V Casual Smile at left
            V "Honestly, you were better than great."
        show chelsea happy
        "She holds the box towards you."
        V "And since you were so good, I have a little reward for you."
        "You're surprised by how giddy you feel as you take the box from her."
        pcname "Thank you, Violet."
        V "Very good! Now, open it!"
        "Opening it gingerly, you see a lacey choker with a bow in the middle."
        "Beneath the bow, two small charms dangle: a lock and a key."
        V "I thought it was cute. And it kind of looks like a collar, if you know what I mean."
        "You feel heat rising to your cheeks."
        V "If things keep going so well between us, I'll get you a better one later."
        "She winks suggestively, making you blush even more."
        V "Well, put it on already."
        "You feel her eyes on you as you pull it from the box and secure it snugly around your neck."
        show chelsea embarrassed
        "She's right; it {i}feels{/i} like a collar."
        V "Now every time you see it, you'll remember who you belong to."
        "It's the first time she's spoken of you so possessively..."
        show chelsea happy
        if club == "track":
            "You're surprised by how much you like it!"
        elif club == "cheer":
            "You feel a familiar warmth - and {i}not{/i} in your cheeks!"
        elif club == "yearbook":
            "It makes you feel safe. Secure."
        "Above all, you want to continue feeling this way. You want to continue pleasing her."
        "A sudden knock at the door startles you both."
        show V Casual Blank at left
        V "I paid with my card, so just sign for it."
        show chelsea embarrassed
        "You're a little nervous to talk to someone; what if they know what the choker means?"
        "Thankfully, the delivery guy is friendly, but not very talkative."
        "Gathering plates and cups, you serve Violet her food and wait patiently for her to start eating."
        "She smiles, clearly pleased at your subservience, and takes a bite."
        show chelsea happy
        "It's as if something tiny bursts inside of you - like you were holding your breath and could finally release it."
        if club == "track":
            "It reminds you of when you're waiting for a race to start. The anticipation, the focus..."
        elif club == "cheer":
            "It reminds you of those few seconds during a toss when you're bracing to catch the flyer..."
        elif club == "yearbook":
            "It's as if a weight is being lifted off of you. You no longer have to make decisions and you're not {i}alone{/i}."
        "After you've both eaten, Violet stands and stretches."
        V "This was nice, but I really need to get home..."
        show V Casual Smile at left
        V "I really hope I can sleep over again soon, though."
        V "I have a {i}lot{/i} of ideas."
        "A familiar blush creeps across your cheeks."
        if club == "track":
            pcname "Sounds like fun..."
        elif club == "cheer":
            pcname "I can't wait!"
        elif club == "yearbook":
            pcname "Oh..."
        "Giggling, she walks to the door and pauses. You hurry to open it for her, making her smile."
        V "You're so good at this. I think you deserve another reward..."
        scene bg VDomKiss with dissolve
        "Wrapping her hand around the back of your neck, she cups the back of your head and pulls you to her."
        "Her lips meet yours - soft and full - pressing firmly together."
        "As her lips move against yours, her tongue darts across your lower lip, teasing you."
        "It's a short but passionate kiss; when she pulls away, you sway toward her, wanting more."
        show bg HomeN with dissolve
        show V Casual Smile at left with dissolve
        show chelsea embarrassed at right with dissolve
        V "See you at school, [pcname]..."
        "You watch her go, touching your tingling lips self-consciously."
        $ acts-=1
        jump events_end_period
    elif True:
        show V Casual Annoyed at left
        V "Were you even trying?"
        "She shakes her head, pulling a small box from her bag."
        V "If you're not going to follow the rules, you get punished. Here."
        "Taking the box, you open it slowly. At first, you're not sure what you're looking at..."
        if club == "track":
            show chelsea confused
            pcname "A... black clown nose?"
            "She laughs."
            show V Casual Smile at left
            V "It's a ball gag!"
        elif club == "cheer":
            show chelsea confused
            pcname "A... ball gag?"
            show V Casual Smile at left
            "She smirks."
            V "Exactly."
        elif club == "yearbook":
            show chelsea confused
            pcname "Um... What is it?"
            "She rolls her eyes."
            V "It's a ball gag!"
        show V Casual Pout at left
        show chelsea blank
        V "Here, I'll put it on you."
        "She walks behind you and lines the rubber ball up with your lips."
        show V Casual Blank at left
        V "Open up!"
        "You open your mouth and she pushes it in, securing the straps around your head."
        "You're not uncomfortable, but being unable to talk makes you feel a lot more attentive to Violet."
        show V Casual Smile at left
        V "That's perfect, now..."
        "She's interrupted by a knock at the door."
        V "I ordered by card, so just sign for it."
        "She waves toward the door, smiling."
        "Shaking your head, you plead with your eyes."
        show chelsea embarrassed
        V "This is your punishment. Go get the pizza."
        "Heart pounding and cheeks on fire, you walk to the door and open it."
        "Pizza Boy" "Hey there-- Oh!"
        "He passes you the receipt, his face almost as red as yours."
        "Pizza Boy" "Just, uh, sign that..."
        "You've never felt so mortified, and you can't even explain yourself to him!"
        "Pizza Boy" "Alright. Here you go, then..."
        "He passes you the pizza, unwilling to meet your eyes."
        "Pizza Boy" "Have, uh, have a good night?"
        "You close the door quickly; Violet is laughing behind you."
        V "Are you sorry you misbehaved today?"
        show chelsea shocked
        "You nod your head, eyes wide."
        V "I like the way you look with that gag on though."
        V "I think we'll use it for other things later..."
        show chelsea embarrassed
        "Despite the embarrassment, your body reacts to her suggestion."
        V "Well? Get the plates and serve me my pizza."
        "She takes a seat and watches. Gathering plates and cups, you pass her her food."
        "As you sit down with your own plate, you realize that you can't eat with the gag on."
        show V Casual Blank at left
        V "You can eat when I'm done."
        "Your jaw begins to ache as you watch her take bite after bite of the pizza."
        "It smells delicious, leaving your mouth watering."
        "For some reason - perhaps because you can't do much else - you find her lips fascinating."
        "You find yourself watching the way they part as she takes a bite."
        "The way her tongue darts across them, leaving them glistening."
        "You want to touch them almost as much as you want the pizza. Maybe more."
        "She dabs a napkin to her lips and stands, breaking your focus."
        V "I have to get home now, but I want to spend the night soon."
        V "This is just a little bit of what I have planned."
        "Strolling toward the door, she pauses, laughing as you rush to open it for her."
        V "You can take that off when I'm gone and eat your dinner. Put it in your bedroom for later."
        "Blushing, you nod."
        show V Casual Smile at left
        V "See you at school!"
        "You close the door behind her and undo the buckle on the gag."
        "As it falls out of your mouth, you move jaw up and down to sooth the aching muscles."
        "The pizza is barely warm, but - after all the anticipation - it still tastes {i}amazing{/i}."
        $ acts-=1
        jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
