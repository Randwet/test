label bakery_conflicts_school:
    if violetrelate == "Dom":
        show V School Annoyed at left with moveinleft
        show chelsea at right with moveinright
        "Violet approaches you at your locker."
        show chelsea shocked
        V "What the hell!?"
        "She grabs a handful of hair and shakes it in your face."
        V "Did you {i}ask{/i} if I liked blondes?"
        menu bakery_conflict_school_violet_dom_react:
            "Apologize." if True:
                show chelsea sad
                if club == "track":
                    pcname "Sorry, it was kind of sudden."
                elif club == "cheer":
                    pcname "Sorry, I guess it slipped my mind..."
                elif club == "yearbook":
                    pcname "I'm sorry! I just... I didn't..."
                V "So what? You {i}forgot{/i} I was your Dom?"
                "Scowling, she rolls her eyes in disgust."
            "Argue." if True:
                show chelsea confused
                if club == "track":
                    pcname "I didn't really think about it."
                elif club == "cheer":
                    pcname "I guess I didn't think I had to."
                elif club == "yearbook":
                    pcname "B-but... It's {i}my{/i} body."
                V "Seriously!?"
        show V School Pout at midright
        V "That's it. Come with me."
        show chelsea shocked
        "Grabbing your arm, she drags you into the restroom with her."
        show chelsea blank
        "Pushing you into the largest stall, she rifles through her purse until she finds a tiny velvet bag."
        show chelsea shocked
        V "{i}These{/i} are called ben wa balls. And you're going to wear them until lunch today."
        menu bakery_conflict_school_violet_dom_balls:
            "Beg forgiveness." if True:
                show chelsea sad
                if club == "track":
                    pcname "Please, I can't do that at school!"
                elif club == "cheer":
                    pcname "Please, I know what I did was wrong!"
                elif club == "yearbook":
                    pcname "P-please don't... I can't..."
                show V School Annoyed at left
                V "Oh, now you feel bad?"
                pcname "I should have asked you before I did it."
                pcname "I'm really sorry. Really!"
                show V School Pout at left
                "She stares at the balls a moment, considering."
                show V School Annoyed at left
                V "No, I think you need to be punished this time."
            "Accept punishment." if True:
                pass
        show V School Pout at left
        "Bending over, she reaches up your skirt and pulls your panties aside."
        show chelsea shocked
        "You gasp as her fingers spread your labia and she slips one of the balls inside of you."
        "It's cold and hard - and heavier than you expected."
        "As she presses the second one inside, you feel your pussy clench around them."
        V "There. You'll want to keep a firm grip on those or you might lose one."
        show V School Smile at left
        show chelsea embarrassed
        "She pulls your panties back into place and stands, smiling."
        V "Meet me back at your locker before lunch. Keep those in until then and {i}maybe{/i} I'll forgive you."
        $ benwa = True
        "She motions for you to leave the stall first, chuckling at your awkward steps."
        "As you move, the balls shift inside of you, pressing into sensitive spots and forcing you to keep your muscles tensed."
        hide V Smile with dissolve
        "Making your way to homeroom, you slowly adjust to the feeling - but every now and then, an unexpected pang of pleasure surprises you."
    if mattsubmissive:
        show chelsea blank at right with moveinright
        "Taking your seat in homeroom, you notice a few students glancing your way."
        "Matt walks in, laughing at something someone said in the hallway."
        if defymatt:
            show chelsea embarrassed
            "You look away, doing your best not to catch his eye."
        elif True:
            show chelsea sad
            "You look at your lap, hoping he'll notice your submissive posture."
        "He walks to his seat without speaking to you."
        show chelsea confused
        "Suddenly, your phone vibrates."
        show chelsea blank

        call screen TextingScene("Matt", [TextMessage("Did u switch rooms?")])

        if defymatt:
            "You roll your eyes."
        elif True:
            pcname "What...?"

        call screen TextingScene("Matt", [TextMessage("No", sender = False)])

        "As you're tucking your phone away, Matt walks around your desk, staring."
        show Matt Question at left with moveinleft
        m "What...?"
        show chelsea laugh
        "You almost laugh at his reaction - he seems completely stupefied!"
        show chelsea happy
        "His shock quickly turns to annoyance, however."
        show Matt Blank at left
        m "I didn't recognize you with that hair."
        show Matt Angry at left
        m "Why would you do that without asking me first?"
        if defymatt:
            show chelsea angry
            if club == "track":
                pcname "What!? You don't own me!"
            elif club == "cheer":
                pcname "Why? It's not like I care what you think."
            elif club == "yearbook":
                pcname "I... I don't care if you like it."
        elif True:
            if club == "track":
                show chelsea confused
                pcname "You don't like it?"
            elif club == "cheer":
                show chelsea happy
                pcname "Isn't it pretty though?"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I just... thought it would look nicer..."
        "Before he can react, Mr. Harvey walks into the room."
        T "Everyone, in your seats, please."
        "Matt glares at you one last time."
        show chelsea blank
        m "Whatever."
        hide Matt Angry with moveoutleft
        "As soon as he takes his seat behind you, you feel your phone vibrate again."

        call screen TextingScene("Matt", [TextMessage("Meet me at the football field after lunch")])

        if defymatt:
            call screen TextingScene("Matt", [TextMessage("Or u know what I'll do")])

        show chelsea shocked
        "Your stomach flutters; you know he plans to punish you."
        if defymatt:
            show chelsea blank
            "Part of you wonders if you should just let him give those pictures out - at least then you'd be free of him."
        "You're still considering it when the bell rings for first period."
    show chelsea happy
    "During your first class, you get a lot of compliments on your hair."
    if benwa:
        "It's hard to pay attention, though, because of the small metal balls shifting inside your pussy."
        "During chemistry, you have to walk around the room to gather supplies for your experiment."
        "It's not so bad until one of your classmates bumps into you."
        "Surprised, you tense - and then, naturally, relax."
        "You feel the balls shift, slipping from their position, and quickly clamp your muscles tightly around them."
        "You're surprised by a sudden wave of pleasure. You close your eyes, trying not to moan..."
        "Classmate" "Are you okay, [pcname]?"
        "Your eyes flutter back open and heat floods your cheeks."
        if club == "track":
            pcname "I'm fine! You just startled me!"
            "Your voice comes out a little louder than you'd meant, but you laugh it off."
        elif club == "cheer":
            show chelsea laugh
            pcname "Oh, yeah... Of course!"
            "You laugh, but it sounds forced."
        elif club == "yearbook":
            pcname "Y-yeah..."
            "You hurry back to your seat."
        show chelsea embarrassed
        "Worst, though, is gym class."
        "Since you're playing dodgeball, there's no way to avoid moving around, and you're especially aware of your body's grip on those little spheres."
        "You want to get hit so you can sit the rest of the game out, but after your reaction in Chemistry..."
        menu benwa_strategy:
            "Get hit." if True:
                "You figure you might as well get it over with, so the first time someone throws a ball your way you let it hit you."
                "This time you know it's coming, so you keep your pussy clenched tight around the benwa balls."
                "A familiar rush of pleasure fills you, but your growing arousal makes it so much more intense..."
                "Despite your best efforts, a small moan escapes you."
                "Your face is on fire as you take a seat on the sidelines, but thankfully nobody seems to have heard."
            "Try to win!" if True:
                show chelsea blank
                "At first, it's not so bad. There are plenty of other targets and you can avoid catching anyone's attention."
                "As the numbers dwindle, though, you find yourself becoming a target - and the more people sitting on the sidelines, the more eyes are on you."
                "Your arousal has been steadily building and now, with only two girls left on each team, you feel your clit throbbing between your legs."
                "The balls shift with every step, sending a thrill of pleasure through your body each time."
                "It's almost impossible to focus, but you're sure that if a ball hits you, you won't be able to hide your reaction."
                "You dodge another ball, barely holding back a cry of pleasure, while the other girl on your team gets hit."
                "Now, two against one, you know it's only a matter of time."
                "Holding a ball in both hands, you use it to knock their throws aside."
                "After they've both thrown their weapons, you wait for one to bend down and hurl your own ball at her."
                "Hit!"
                "With fair odds again, you eye up your opponent."
                "She's one of the less fit girls, who must have just gotten lucky this game."
                "You can definitely win, but you're {i}really{/i} distracted right now..."
                "Staring each other down, you both wait for the other to make a move."
                "As she raises her ball to lob it at you, you see your chance."
                "Flinging your ball toward her feet, you take a step to the left and narrowly dodge her throw."
                "Your own ball bounces off her knee and your team jumps up, cheering."
                show chelsea embarrassed
                "As they swarm around you, you feel the first ripple in your loins."
                "Squeezing your eyes shut, you plaster a smile on your face and try to hold back a cry of pleasure as your orgasm crashes over you."
                "As the other girls pull away, still congratulating you, you open your eyes and nod at each of them."
                "If anyone notices your flushed face, they must assume it's just from exertion."
        "After gym, you walk back to your locker and look for Violet."
        show V School Smile at left with moveinleft
        V "How has your day been?"
        "Your face flushes with embarrassment."
        show V School Pout at left
        V "Well?"
        if club == "track":
            pcname "I... came. In gym class."
        elif club == "cheer":
            pcname "Best gym class I ever had."
        elif club == "yearbook":
            pcname "In gym... I..."
        show V School Smile at left
        "She laughs, swinging your locker open."
        "Stepping between you and the locker door, she slides her hand up your thigh and pulls your panties aside."
        "You gasp as she slips two fingers inside of you, hooking one of the balls and pulling it out of you."
        "You glance around, but with the locker blocking her from view, nobody seems to have noticed."
        pcname "Violet..."
        V "Shhhh..."
        "Pressing her fingers inside you again, she pulls the other ball out and steps back."
        "Letting out a shaky breath, you sway on your feet."
        show V School Pout at left
        V "Did you learn your lesson?"
        show chelsea sad
        pcname "Yes..."
        show chelsea blank
        pcname "I won't do it again."
        show V School Annoyed at left
        V "You won't do what again?"
        pcname "I won't do anything without your permission."
        show V School Smile at left
        "She smiles."
        V "Good girl!"
        V "Now... I have an appointment, so I'm leaving early today."
        V "Don't miss me too much, okay?"
        "Winking, she walks down the hallway toward the office."
        hide V School Smile with moveoutleft
        show chelsea embarrassed
        "You sit alone at lunch, but your thoughts are full of Violet."
    if damienrelate == "dating":
        show chelsea happy at right with moveinright
        show bg Cafeteria with dissolve
        "Throughout the day, you feel various eyes on you as your classmates take in your new look."
        "You receive several compliments as you pass through the halls in between classes."
        "By the time you reach the cafeteria for lunch, you can't help but feel confident about your decision."
        "After you get your food, you take a seat at your lunch table beside Damien. He stares at you, bewildered."
        show Damien Shocked at left with moveinleft
        D "[pcname]?"
        D "You... You dyed your hair."
        show chelsea blank
        "He can't seem to wrap his head around it. You can't help but feel a little self-conscious under his gaze."
        show chelsea happy
        pcname "I did. Isn't it pretty?"
        show Damien Worry at left
        D "Er... Yeah..."
        show chelsea embarrassed
        pcname "Do you like it?"
        "He hesitates, unable to take his gaze away from your pale locks."
        D "Well..."
        show chelsea happy
        "Damien reaches out and lightly strokes your hair, twisting a small piece between his fingers."
        show Damien Neutral at left
        D "It's not {i}bad{/i}. It's just... different. I mean, it's your body, so..."
        show Damien Blank at left
        "You feel your confident smile falter."
        show chelsea blank
        if club == "track":
            pcname "So you want me to dye it back?"
        elif club == "cheer":
            pcname "Are you asking me to change it back?"
        elif club == "yearbook":
            pcname "I-If you want me to dye it back..."
        show Damien Shocked at left
        "Damien quickly shakes his head, his face burning with embarrassment and shame."
        D "Of course not! I'd never tell you what to do with your body! I just..."
        show Damien Happy at left
        D "It's just going to take some getting used to. That's all."
        show chelsea sad
        "You frown, your gaze dropping back to your lunch tray."
        "You didn't think dying your hair would be such a big deal to Damien."
        if club == "track":
            "You had even thought he would enjoy your more feminine change."
        elif club == "cheer":
            "You had even hoped he would find it a little sexy."
        elif club == "yearbook":
            "You had hoped he would enjoy your new display of confidence."
        show chelsea blank
        "You feel Damien's arm wrap around your shoulders and give you a tight squeeze. You glance up at him, discouraged."
        D "I'm really sorry. I know it's not fair of me to have an opinion."
        D "I don't {i}dislike{/i} it. I'm just... I'm confused. It kind of feels like this came out of nowhere. I mean, you didn't mention it to me or anything... Not that you have to! But, well, you know..."
        show Damien Worry at left
        "Damien looks away nervously, choosing to focus on a loose thread on the cuff of his uniform instead."
        menu bakery_conflict_damien_mentionkeith:
            "Well, Keith really likes it." if True:
                show chelsea blank
                show Damien Glare at left
                "His eyebrows furrow together, pinching above the bridge of his nose. He pulls back just a little bit."
                D "Keith?"
                show chelsea confused
                "You suddenly realize amidst his confusion that you've never actually told him who Keith was."
                show chelsea blank
                pcname "He's the manager at the bakery I work at."
                "Damien shifts beside you uneasily."
                show Damien Neutral at left
                D "Is he the reason you dyed your hair?"
                menu bakery_conflict_damien_keithdye:
                    "Yes." if True:
                        show Damien Glare at left
                        "It may not be what he wants to hear but you don't intend on lying to your boyfriend."
                        "Damien's lips press into a tight line, clearly bothered by your confession."
                        "He's quiet for a long moment, his fingers lightly trailing over your blonde hair."
                        show Damien Worry at left
                        D "You know, [pcname], you really don't have to try to impress your boss with something like this."
                        show chelsea sad
                        "You feel your heart tighten a little. Is he really only upset by your hair color?"
                        pcname "So you don't like it?"
                        show Damien Blank at left
                        "Damien shakes his head, rejecting the idea."
                        show Damien Neutral at left
                        D "It's not that. It just..."
                        show Damien Glare at left
                        "Damien takes a moment to pull his thoughts together. You wait anxiously at his side."
                        show Damien Blank at left
                        "Finally, he lets out a deep breath."
                        show Damien Neutral at left
                        D "It doesn't feel like {i}you{/i}."
                        D "If you're happy with it, though, then I am, too. I want to support you."
                        D "I just ask that you keep in mind that you shouldn't make drastic changes like that just for a job. Okay?"
                        pcname "Yeah... Of course."
                        show Damien Happy at left
                        "Damien smiles, a little comforted by your agreement."
                        D "Thank you."
                    "No." if True:
                        show Damien Glare at left
                        "Damien presses his lips together and glances away, not entirely convinced."
                        "He sighs."
                        show Damien Neutral at left
                        D "Well, just know that you don't need to impress anyone, okay?"
                        show Damien Happy at left
                        D "You're beautiful as you are."
                        "Damien tucks a strand of hair behind your ear before kissing your cheek."
                        show chelsea happy
                        D "But if you're happy with your new hair, then I am, too."
                show Damien Blank at left
                "He picks up a brownie from his tray and takes a small bite."
                show Damien Happy at left
                show chelsea happy
                D "Anyways, so I wanted to tell you about this new game I downloaded..."
                "You spend the rest of your lunch discussing a new video game that recently came out."
                "You're grateful for the change in subject and immediately latch onto the new topic, happy to have a break from discussing your hair."
            "I just really liked the color." if True:
                show Damien Glare at left
                "Damien's eyebrows furrow together. You can tell he doesn't entirely believe you, but thankfully he doesn't push it."
                show Damien Happy at left
                D "Well, as long as you're happy with it, [pcname], I am, too."
                show chelsea happy
                "He smiles and gives your shoulders another squeeze."
                show Damien Blank at left
                "He picks up a brownie from his tray and takes a small bite."
                show Damien Happy at left
                D "Anyways, so I wanted to tell you about this new game I downloaded..."
                "You spend the rest of your lunch discussing a new video game that recently came out."
                "You're grateful for the change in subject and immediately latch onto the new topic, happy to have a break from discussing your hair."
    elif violetrelate == "Sub":
        show chelsea at right with moveinright
        "By the time you walk into the cafeteria for lunch, you're full of confidence in your decision!"
        show V SubSchool Worried at left with moveinleft
        "Violet places your tray in front of you and takes her seat."
        "Her eyes dart around, looking at everything but you, while she waits for you to speak."
        "It's clear from her fidgeting that she has something to say."
        if club == "track":
            show chelsea confused
            pcname "Do you want to say something, Violet?"
            show chelsea happy
            "You smile, knowing the answer."
        elif club == "cheer":
            show chelsea confused
            pcname "Is something wrong, Violet?"
            show chelsea happy
            "You smile, watching her squirm."
        elif club == "yearbook":
            show chelsea embarrassed
            pcname "Violet?"
            "You smile tentatively."
        show V SubSchool Sad at left
        V "Your hair looks... nice."
        show V SubSchool Blank at left
        V "You must have a good stylist; he managed to get a shade without too much yellow."
        V "And blonde is really in right now."
        "She hesitates."
        show V SubSchool Worried at left
        V "Can I... say something else about it?"
        menu bakery_conflict_violet_sub_talk:
            "Let her." if True:
                show chelsea blank
                if club == "track":
                    pcname "Go ahead."
                elif club == "cheer":
                    pcname "Sure, go ahead."
                elif club == "yearbook":
                    pcname "You don't like it?"
                show V SubSchool Happy at left
                V "I liked the red better. You really stood out."
                V "It's one of the reasons I noticed you, actually."
                "All of the confidence you'd built up deflates as she speaks."
                show V SubSchool Blank at left
                "After all the compliments, you were sure everyone would like your new hair color..."
                "You know that you can't be insecure around Violet, however."
                pcname "Violet... I think you've forgotten something."
                show chelsea confused
                if club == "track":
                    pcname "I'm in charge, so your opinion doesn't matter."
                    pcname "{i}I{/i} like my hair like this and I've gotten a ton of compliments about it."
                elif club == "cheer":
                    pcname "{i}Your{/i} opinion means nothing."
                    pcname "If {i}I{/i} like my hair blonde, that's all that matters."
                elif club == "yearbook":
                    pcname "It's not up to you, is it?"
                    pcname "It doesn't matter what you think at all."
                show V SubSchool Worried at left
                "Her mouth falls open and, for a moment, you think she's going to argue with you."
                show V SubSchool Blank at left
                "But she closes it quickly, pressing her lips firmly together."
            "Refuse." if True:
                show chelsea blank
                if club == "track":
                    pcname "No, I don't think so. I don't need your opinion on it."
                elif club == "cheer":
                    pcname "No, it's not up for debate."
                elif club == "yearbook":
                    pcname "I'd rather you didn't..."
                "She looks down and lets out a heavy sigh. It's clear she wants to speak anyway, but she's trying to hold back."
                "She quickly loses the fight, blurting out:"
                hide V SubSchool Worried
                show V School Annoyed at left
                V "Why in the world would you choose {i}blonde{/i}?"
                V "Now you look the same as every other stupid twit."
                show chelsea angry
                "Her words immediately set off your temper - especially after all of the compliments you've gotten today!"
                show V School Pout at left
                if club == "track":
                    pcname "It doesn't matter if you like it or not. It's my choice."
                    pcname "If I want to shave my head {i}bald{/i}, I will."
                    pcname "And you'll tell me how much you {i}love{/i} it. Because {i}I say so{/i}."
                elif club == "cheer":
                    pcname "Seriously?"
                    pcname "Who's in charge here? What makes you think I care what {i}you{/i} think?"
                elif club == "yearbook":
                    pcname "I told you not to speak."
                    pcname "If it mattered, I would have asked you before I dyed it."
        "Taking a deep breath, you continue."
        show chelsea blank
        pcname "Clearly not everyone agrees with you. I've gotten a lot of compliments today."
        pcname "And everyone at the bakery thinks it's great - they both said I would look better blonde."
        pcname "Now drop it, or I'll have to punish you for being disrespectful."
        "As you eat, Violet picks at her food in silence."
        "After a few minutes, though, she looks up at you."
        show V School Blank at left
        V "Is that why you did it? To impress the people at work?"
        if club == "track":
            "Your thoughts shift to Keith's reaction; you're surprised by how much his praise means to you."
            pcname "That's not--"
        elif club == "cheer":
            "Your thoughts shift to Keith's reaction; the look on his face, the way it made you feel..."
            pcname "I don't-- I don't care what they think."
        elif club == "yearbook":
            "Your thoughts shift to Keith's reaction; he seemed to really {i}like{/i} you, for once."
            pcname "N-no, I just..."
        show V School Annoyed at left
        "Violet jumps to her feet, pressing her palms down on the table."
        V "It is, isn't it!?"
        V "I can't believe you care so much about their opinion of you that you dyed your hair without even mentioning it to me!"
        menu bakery_conflict_violet_sub_react:
            "Scold her." if True:
                "You shake your head."
                show chelsea angry
                if club == "track":
                    pcname "Sit down and shut up."
                elif club == "cheer":
                    pcname "Violet... Be a good girl, sit down, and shut up."
                elif club == "yearbook":
                    pcname "Stop it."
                    pcname "Just sit down and... and shut up!"
                show V School Pout at left
                show chelsea shocked
                "Surprised, Violet sinks back into her seat."
                show chelsea blank
                "You continue, speaking firmly."
                pcname "It doesn't matter why I did it."
                pcname "You're here to serve {i}me{/i}, remember?"
                "Your dominant tone seems to do the trick; she nods."
                hide V School Pout
                show V SubSchool Sad at left
                V "I... I'm sorry, okay?"
                V "I shouldn't have spoken to you like that."
                show chelsea angry
                pcname "No, you shouldn't have. And you clearly need to be taught a lesson."
                show chelsea blank
                pcname "Pick me up after work tonight and we'll see how sorry you are then."
                show V SubSchool at left
                "Gasping, Violet nods slowly - you can see the anticipation on her face."
            "Apologize." if True:
                show chelsea sad
                show V School Pout at left
                if club == "track":
                    pcname "No. Maybe. I don't know."
                elif club == "cheer":
                    pcname "I didn't think it would bother you this much!"
                elif club == "yearbook":
                    "You glance around the cafeteria, hoping nobody notices the scene she's making."
                    pcname "Sit down. Please."
                show chelsea blank
                show V School Blank at left
                "You take a deep breath as she sits back down."
                pcname "I'm sorry, Violet. I should have told you I was going to do it."
                pcname "Lisa made the appointment for me, so I didn't really think about it."
                show V School Pout at left
                "Her frown deepens. Then, shaking her head, she sighs."
                show V School Blank at left
                V "You really shouldn't give in to someone else so easily. You're supposed to be my {i}Dom{/i}."
                "Most of her anger seems to have dissipated, and something is still bothering you..."
                pcname "Well, as your Dom, I think I gave into {i}you{/i} too easily."
                pcname "And you need to be punished for questioning me."
                hide V School Blank
                show V SubSchool Worried at left
                "She opens her mouth as if to protest, but shuts it firmly."
                pcname "So you're going to pick me up after work tonight, and then you'll make it up to me."
                "Violet nods slowly - you can see the anticipation on her face."
        $ violetdateflag = True
    elif True:
        show chelsea at right with moveinright
        "By the time you walk into the cafeteria for lunch, you're full of confidence in your decision!"
        show chelsea happy
        "After a few more compliments in the lunch line, you start to wonder why you've never done something like this before."
        show chelsea blank
        "Maybe Lisa was right; you haven't been taking care of yourself as much as you could."
        "You think it over as you eat your lunch."
    if mattsubmissive:
        scene bg black with dissolve
        show bg Cafeteria with dissolve
        show chelsea at right with moveinright
        "As you're leaving the cafeteria, your phone vibrates."

        call screen TextingScene("Matt", [TextMessage("Football field")])

        menu bakery_conflicts_matt_meet:
            "Meet him." if True:
                $ corruption += 1
                pass
            "Refuse." if True:
                if defymatt:
                    "You tuck your phone away."
                    "You know what will happen, but you can't keep letting him blackmail you anymore."
                    $ endgame = True
                    $ mattblackmail = 2
                    jump events_end_period
                elif True:
                    "After a few minutes, when you don't respond, you get another text."

                    call screen TextingScene("Matt",
                    [
                        TextMessage("Remember those pics?"),
                        TextMessage("Get over here or the whole school sees them")
                    ])

                    show chelsea shocked
                    pcname "He wouldn't. Would he...?"
                    show chelsea embarrassed
                    "Heart pounding, you make your way to the football field."
                    $ defymatt = True
        show chelsea blank
        show bg black with dissolve
        pause 0.5
        show bg TrackD with dissolve
        show Matt Blank at left with moveinleft
        "When you reach the field, Matt steps out from behind the bleachers."
        m "So... What made you decide to dye your hair?"
        "You shrug."
        if club == "track":
            pcname "My manager and the other girl at work said it would look better, so..."
        elif club == "cheer":
            pcname "My manager at work said he thought it would attract more customers."
        elif club == "yearbook":
            pcname "At work, they said... They said it would look better, so..."
        show Matt Angry at left
        m "So you care more about what {i}they{/i} think?"
        show chelsea embarrassed
        m "You should be focused more on pleasing {i}me{/i}. Shouldn't you?"
        show chelsea sad
        pcname "I'm sorry. I thought you'd like it too..."
        m "I think you need a reminder of who's in charge here..."
        show Matt Blank at left
        "He walks under the bleachers and motions you over."
        m "Get over here, slut."
        show chelsea confused
        "Leading you into the shadows beneath the bleachers, he pulls out a set of handcuffs."
        pcname "What...?"
        show chelsea shocked
        "He fastens the handcuffs to your wrist behind a pole."
        scene bg MBCS1 with dissolve
        "Grabbing your other hand, he cuffs it to a different pole, leaving you standing with your arms stretched wide."
        "He looks at you a moment, deciding what to do next, and then starts unbuttoning your blouse."
        "He takes his time, unbuttoning it slowly, each one exposing another inch of your skin."
        "When he finishes, he pushes the blouse off your shoulders and reaches around you to unhook your bra."
        show bg MBCS2 with dissolve
        "He chuckles when your nipples stiffen in the open air, and reaches down to pinch them."
        pcname "Ah..."
        "Twisting them between his fingers, he smirks."
        m "Such a slut..."
        if defymatt:
            "You squeeze your eyes tightly shut, trying to hold back your reaction to his touch."
        elif True:
            "You gasp, enjoying the attention."
        "He releases your nipples, and grabs a breast in each hand, massaging them roughly."
        if defymatt:
            "You gasp, surprised at his roughness."
        elif True:
            pcname "Matt--"
        "He laughs at your reaction and gives them one last, hard squeeze."
        if defymatt:
            if club == "track":
                "You glare up at him defiantly, but he's focused on other things."
            elif club == "cheer":
                "You gasp, glancing around, but there's no one in sight."
            elif club == "yearbook":
                "Shocked, you barely notice the heat in your cheeks."
        show bg MBCS3 with dissolve
        "Standing beneath the bleachers, cuffed to the metal pole, you're helpless as he reaches out and begins stroking your pussy through your panties."
        if defymatt:
            "You're ashamed when your body immediately responds."
        "A rush of heat suffuses your lower half."
        m "Wet already?"
        "He runs his fingers up and down your cunt, pressing up into the growing dampness and occasionally circling your clit until you finally gasp."
        "Then, satisfied, he pulls the panties down as well, leaving you completely exposed."
        m "Now, get on your knees, slut."
        show bg MBCS4 with dissolve
        if defymatt:
            "You slowly sink to your knees, glaring up at him the whole time."
        elif True:
            "You sink to your knees and lick your lips, knowing what he has in mind."
        "The ground is hard and gritty under your knees, but you try to ignore it."
        "He unbuttons his pants, freeing his cock, and presses it toward you."
        show bg MBCS5 with dissolve
        m "You should be good at this by now. Go on."
        if defymatt:
            "Furious - at him and at yourself - you open your mouth for him."
        elif True:
            "Smiling, you part your lips and lick the tip of his cock."
        "He's just far enough away that you have to lean forward to reach him, pulling against the cuffs."
        "Swirling your tongue around his tip, you wrap your lips around it and begin bobbing your head."
        "He sighs and tilts his head back, letting you do the work."
        "You strain harder against the cuffs, leaning forward a little more to take him further into your mouth."
        if corruption > 20:
            "His cock hits the back of your throat, but you relax, taking him fully."
            if defymatt:
                "He moans and, despite your resentment, you feel a surge of pride in your own skills."
            elif True:
                "You can't help but feel proud of the way he moans in response."
            "Bobbing your head up and down the length of his cock, you continue deep-throating him as the taste of his precum fills your mouth."
            "Suddenly his hand grasps the back of your head and he thrusts against your face, fucking your mouth as you struggle not to gag."
            show bg MBCS6 with dissolve
            "Then he pulls his cock from your mouth, leaving you gasping, and shoots his load across your face."
        elif True:
            "His cock hits the back of your throat. You try to relax enough to deep-throat him, but almost immediately start gagging."
            m "How are you still so fucking bad at this?"
            if defymatt:
                "You tell yourself that you don't care what he thinks, but his words still sting."
            elif True:
                "Ashamed, you try again, but you just can't do it."
            "To make up for it, you bob your head faster, using a little more suction than normal."
            "You're soon rewarded with the salty-sweet taste of precum as his climax nears."
            show bg MBCS6 with dissolve
            "Suddenly he pulls his cock from your mouth and surprises you by shooting his load across your face."
        "You stare up at him, helpless as the cum runs down your face and drips from your chin, slattering across your breasts."
        m "Now... Who's in charge?"
        if defymatt:
            "Forcing down your pride, you grind out the words:"
            pcname "You are, Matt."
        elif True:
            "Smiling, you answer."
            pcname "{i}You{/i} are, Matt."
        m "Hmmm... I don't know if you've really learned your lesson yet."
        show bg MBCS7 with dissolve
        "He steps back, tucking his dick back into his pants and surveys you."
        if defymatt:
            "You're ashamed to realize that your own juices are running down your inner thigh; you hope he doesn't notice."
        elif True:
            "You're suddenly aware of your own arousal trickling down your inner thigh. Maybe he'll notice?"
        m "I think you should spend some time alone, thinking about who you belong to..."
        m "So I'm going to leave you here until I feel like coming back for you. Unless someone else finds you first."
        if defymatt:
            if club == "track":
                pcname "What!? You can't do that!"
            elif club == "cheer":
                pcname "Are you serious!?"
            elif club == "yearbook":
                pcname "W-what? No!"
        elif True:
            if club == "track":
                pcname "What? But I told you you're in charge!"
            elif club == "cheer":
                pcname "What? No, please, Matt!"
            elif club == "yearbook":
                pcname "B-but I told you. You're in charge, Matt! I belong to you!"
        "He laughs, stepping out from the shadows beneath the bleachers."
        m "Have fun, [pcname]. I'll see you later, if I don't forget about you."
        "You consider calling out to him, but you're afraid that someone else will hear."
        "As he fades from view, you look down at yourself; his cum has dripped down your chest, leaving thin trails across your breasts."
        if defymatt:
            "You wonder with growing panic if someone will notice you here. What would they think?"
            "What would they {i}do{/i}?"
        elif True:
            "The thought of someone finding you - mostly naked, handcuffed, and dripping cum - makes you feel..."
            "Panic? Arousal?"
            "Both?"
        "As minutes pass, grittiness of the dirt beneath your knees starts to annoy you, so you pull yourself back to your feet."
        "You try to ignore the wetness between your thighs, and the throbbing in your clit, to focus on your situation."
        "You spend some time pulling at the cuffs, trying to slip your hand out or find a release button, but eventually admit defeat."
        show bg MBCS8 with dissolve
        "Student" "Hey! Look at that!"
        "Heart in your throat, you look around, trying to figure out where the voice is coming from - and if they're talking about you."
        "Soon you see them; a gym class walking toward the field."
        "Student" "I found a $5 bill!"
        "He steps near the edge of the bleachers and bends to retrieve the bill."
        "Student" "Think there's any more around here?"
        "Your heart pounds against your ribcage as he looks around, but his eyes are focused on the ground."
        "Student" "I think there's one over there!"
        "He jogs away, followed by several other students."
        "You hold your breath as they file past the bleachers and start playing football on the field behind you."
        "Each time a voice gets closer, you feel your pulse quicken."
        if corruption > 30:
            "You can't help but think about what might happen if they found you here..."
            "You imagine a line of boys waiting to take their turns with you..."
            "Lifting your legs to plunge their cocks deep inside your cunt while you're helpless to stop them..."
            if defymatt:
                "You shake yourself from your thoughts, wondering if Matt's blackmail is warping your mind."
            elif True:
                "You shake yourself from your thoughts with a smile."
        "Two of the boys sit on the bleachers behind you, chatting while the others play."
        show bg MBCS9 with dissolve
        "Student" "So you have asthma?"
        "Other Student" "Yeah, and I can't find my inhaler so I couldn't play today."
        "Student" "That sucks. I hurt my shoulder at wrestling practice yesterday, so I have to rest it for a few days or I can't compete next week."
        "You focus on their conversation; it helps to distract you from your situation."
        "Student" "So you're dating one of the cheerleaders?"
        "Other Student" "Yeah..."
        if club == "cheer":
            "You wonder which cheerleader he's dating."
            "Student" "She any good?"
            "Other Student" "Oh, we haven't..."
            "Student" "What!? I heard the cheerleaders are all sluts."
            "Other Student" "I don't know about that..."
            "Student" "Know which one I'd like to fuck?"
            "Student" "[pcname]. Especially since she dyed her hair..."
            "Student" "I would blow her fucking mind."
            "Other Student" "She's cute..."
            "You can't help feeling flattered; you're sure he'd never say things like this to your face, after all."
        elif club == "track":
            "You don't know any cheerleaders, but you wonder which one he's dating."
            "Student" "She any good?"
            "Other Student" "Oh, we haven't..."
            "Student" "What!? I heard the cheerleaders are all sluts."
            "Other Student" "I don't know about that..."
            "Student" "I'm not really into cheerleaders anyway."
            "Student" "Know who I'd fuck? [pcname] from the track team."
            "Student" "She's thin but she's still {i}built{/i}, if you know what I mean."
            "Other Student" "She's cute..."
            "Student" "And now she's blonde. Man... if I could get with her I would blow her fucking mind."
            "You're shocked to hear him talk about you like that - you're not even sure if you've ever met him!"
        elif club == "yearbook":
            "You don't know any cheerleaders, but you wonder which one he's dating."
            "Student" "She any good?"
            "Other Student" "Oh, we haven't..."
            "Student" "What!? I heard the cheerleaders are all sluts."
            "Other Student" "I don't know about that..."
            "Student" "I'm not really into cheerleaders anyway."
            "Student" "Know who I'd fuck? [pcname] from that yearbook club."
            "Student" "I've seen her around taking pictures and, man, she's fucking hot."
            "You gasp, your cheeks warming at the way he's talking about you."
            "Other Student" "She seems kinda shy."
            "Student" "I think that's hot as hell."
            "Student" "And now she's blonde. Man... if I could get with her I would blow her fucking mind."
            "You don't know what to think - you don't even know who this guy is and he's talking like {i}that{/i}!"
        "The teacher blows his whistle, signalling for them to head back inside."
        "As they file past, you try to figure out which guy was talking about you, but you can't really tell."
        "A while later, as you shift your weight from foot to foot, trying to find a comfortable way to stand, you hear another voice."
        P "Over here, I noticed that some of the railings are getting loose."
        "You look over your shoulder - the principal is leading a maintenance man around the field."
        "They approach the bleachers, take a few steps up, and shake the railings."
        P "See what I mean?"
        "You can't hear the man's response, but he makes some notes on his clipboard."
        P "Under the bleachers could use a good cleaning too."
        "Your heart pounds as you watch them descend the steps and walk to the end of the bleachers."
        "At that moment, you {i}know{/i} they're going to walk back and see you."
        "Will you be suspended?"
        "Expelled?"
        if corruption > 35:
            "...Or will they take advantage of the situation?"
        P "We need to take a look at the plumbing to the concession stand too. I was told it's leaking."
        "You breathe a sigh of relief as they walk away, to the other side of the stadium."
        "A little while later, you hear footsteps behind you."
        show bg TrackD with dissolve
        show Matt Smirk
        m "So... Did you have a nice day?"
        if defymatt:
            "You try to keep your face composed so that he can't see your anger."
        elif True:
            "You nod at him, trying to look submissive."
        "He comes to stand in front of you, smirking."
        m "Tell me what you are."
        if defymatt:
            if club == "track":
                "Taking a deep breath, you grind the words out."
                pcname "I'm a slut."
            elif club == "cheer":
                "Batting your lashes, you tell him what he wants to hear."
                pcname "I'm a {i}slut{/i}."
            elif club == "yearbook":
                "Looking at the ground, you whisper:"
                pcname "I'm a... a slut..."
        elif True:
            "You bow your head."
            pcname "I'm a slut, Matt."
        show Matt Question
        m "And whose slut are you?"
        if defymatt:
            "You force the words out, hoping he'll uncuff you."
            pcname "I'm... your slut... Matt..."
        elif True:
            pcname "I'm {i}your{/i} slut, Matt."
        "He reaches out and pinches your nipple hard, twisting until you cry out."
        show Matt Smirk
        m "That's right. And you're going to remember that from now on, aren't you?"
        pcname "Yes, Matt."
        show Matt Pleased
        "He uncuffs your hands and watches as you quickly dress."
        "As you button your blouse, he speaks:"
        show chelsea sad at right with dissolve
        show Matt Happy at left
        m "Good. Because next time, I'll make sure some of my friends know where to find you."
        show chelsea shocked
        "Startled, you look up from your buttons, but he's already walking away."
        pcname "Would he really...?"
        "You walk back to the school and check the clock. School was dismissed thirty minutes ago - you have to hurry or you'll be late for work!"
    show bg black with dissolve
    jump events_end_period

label bakery_conflicts_violetsub:
    show bg black with dissolve
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "Stepping out of the bakery, you look around for Violet's car."
    "She's parked a few spaces down the street; as you walk closer, she jumps out to open your door for you."
    show bg CityN with dissolve
    show V SubCasual Happy at left with moveinleft
    V "I hope you had a good night at work?"
    "You ignore her, taking your seat in the car and waiting for her to close the door."
    hide V SubCasual Happy with dissolve
    "She gets in and drives in silence, occasionally glancing nervously in your direction."
    "When she parks in front of your apartment, she dutifully opens your door for you."
    show bg black with dissolve
    "Still ignoring her, you unlock your apartment and walk inside without waiting for her to catch up."
    show bg HomeN with dissolve
    show V SubCasual Sad at left
    V "Look, I'm sorry I freaked out, I--"
    pcname "Violet."
    "She stops speaking immediately."
    "You walk to the couch in silence and take a seat."
    if club == "track":
        pcname "Come here."
    elif club == "cheer":
        pcname "Sit with me."
    elif club == "yearbook":
        "You beckon her closer."
    "She hurries to obey."
    if club == "track":
        pcname "Now, it's time for your punishment."
    elif club == "cheer":
        pcname "You've been awfully disobedient, haven't you?"
    elif club == "yearbook":
        pcname "You were... very bad today, weren't you?"
    show V SubCasual Worried at left
    V "I didn't mean to misbehave, [pcname]. I was just surprised!"
    "Shaking your head, you give her instructions."
    if club == "track":
        pcname "Shirt and pants off."
    elif club == "cheer":
        pcname "Take off your shirt and pants first."
    elif club == "yearbook":
        "You bite your lip."
        pcname "Take off your shirt. And... your pants..."
    show V SubCasual Sad at left
    "She looks down and starts unbuttoning her pants."
    "You watch as she peels them off, standing in just her shirt and panties."
    "Then she lifts her shirt over her head and drops it at her feet, looking to you for further instruction."
    scene bg black with dissolve
    if club == "track":
        pcname "C'mon, lay across my knees."
    elif club == "cheer":
        pcname "Now lay across my lap."
    elif club == "yearbook":
        pcname "Lay down."
        "You motion to your lap; she gets the idea."
    "She lays across your lap, her lower back stretched over one leg, the curve of her ass hanging off the other."
    if club == "track":
        "Yanking her panties down, you raise your hand."
    elif club == "cheer":
        "Grabbing the top of her panties, you bare her ass and raise your hand."
    elif club == "yearbook":
        "Sliding her panties down, you look at her bare ass and raise your hand."
    "You bring your hand down on her right cheek; Violet gasps in surprise."
    "Raising your hand again, you slap the other cheek, evoking another gasp."
    "Over and over, you slap her ass, watching as the pale cheeks turn pink and then red."
    "Violet inhales sharply each time you strike her - and then she sighs when, between strikes, you gently run your hand over her sensitive flesh."
    pcname "Have you learned your lesson yet?"
    V "Y-yes, [pcname]."
    "You run your hand over her ass, feeling the heat radiating from her pink cheeks."
    pcname "And what did you learn?"
    V "Not to question you."
    "You run your fingers around the curve of one cheek, then slide them down her crack and under, over her labia."
    pcname "Good. Now... Apologize."
    "Voice breathy from your caresses, she stammers an apology."
    V "I'm really s-sorry, [pcname]. I'm sorry I argued with you... and questioned you... and..."
    pcname "You don't look {i}sorry{/i}, Violet... You look {i}aroused{/i}."
    "As you speak, you slide your fingers between her labia, stroking her slit and teasing her opening."
    "Her breath comes hard and fast; she squirms on your lap, her fingers digging into the couch cushions as she rocks her hips against your leg."
    pcname "Do you want something, Violet?"
    V "P-please... touch me..."
    "You know you're supposed to be punishing her, but the way she looks... You just {i}want{/i} her."
    "You run your other hand over her back, barely touching her exposed skin."
    "By the time you're done teasing her, she's trembling with excitement - her cunt dripping with arousal."
    pcname "I've been touching you, but you don't seem satisfied."
    V "P-pleeeeeaaasssee..."
    "You sink two fingers into her wet folds, eliciting a moan of pleasure."
    "Withdrawing your fingers, you slowly plunge them back into her."
    "Again - slowly, teasingly - you pull your fingers out and press them back into her."
    "She lifts her ass and gyrates her hips, trying desperately to get you to move deeper or faster."
    "Giggling, you pull your fingers out of her and slap her ass one last time."
    pcname "Sit up."
    "Violet moves quickly, eager to please you - and be pleased by you."
    "You pull her into a hard kiss, your hand slipping back between her legs."
    "She spreads them wide, giving you access to her pussy while her lips part for your tongue."
    "Fingering her harder and faster now, you thrust your tongue into her mouth, stroking her tongue with your own."
    "Your thumb rests against her clit, gently teasing it with every thrust of your fingers."
    "She moans against your mouth, grinding her hips against your hand."
    "You break off the kiss, pushing her back against the arm of the couch to give you a better view of her reactions."
    V "Oh... [pcname]..."
    "Her head falls back as she moans your name; she's spread before you, to do with as you like."
    "Dipping your head toward her, you take a stiff nipple into your mouth and suck hard."
    V "Ah!"
    "You stop thrusting; instead, you hook your fingers and massage the ridge of her g-spot while your thumb rubs back and forth over her clit."
    V "Yes! Oh fuck... Oh fuck!"
    "Releasing her nipple, you graze your teeth across it before moving to the other side."
    "Flicking your tongue across the hardened peak, you feel her muscles tightening around your fingers, signaling her approaching orgasm."
    "You take her nipple into your mouth, sucking hard while your fingers press hard against her g-spot."
    V "Right there! Oh fuck, right there!"
    "Her muscles clamp tight around you, her back arching as her legs start spasming."
    V "Oh {i}fuuuuuuuck{/i}!"
    "You watch as her orgasm rattles through her, leaving your hand covered in her fluids."
    "As the last of the tremors finish, you pull your hand free and smile down at her."
    pcname "Well?"
    V "Th-thank you, [pcname]."
    pcname "Too bad you didn't bring a change of clothes..."
    pcname "Or you could spend the night."
    "She shakes her head sadly."
    V "I didn't even think of it... Sorry."
    pcname "It's fine. It's late anyway."
    show bg HomeN with dissolve
    "She nods, gathering her clothing."
    show chelsea happy at right with dissolve
    show V SubCasual Happy at left with dissolve
    "After she's dressed, she walks to the door, smiling back at you."
    pcname "Next time, I won't go so easy on you."
    "She grins."
    V "Promise?"
    "You shake your head as she bounces out the door; you really should've been harder on her."
    $ acts-=1
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
