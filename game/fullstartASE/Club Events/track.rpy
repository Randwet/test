label track_generic:
    $ genericevent1 = renpy.random.randint(1, 3)
    $ genericevent2 = renpy.random.randint(1, 3)

    if genericevent1 == 1:
        "On your way to practice, you trip on the curb and land on your ankle."
        "It doesn't seem like a bad injury, but it will definitely slow you down!"
    elif genericevent1 == 2:
        $ clothes = 'school'
        show chelsea at right with moveinright
        "As you walk to the school for practice, some guys driving past slow down to whistle and holler at you."
        menu trackgencatcalls:
            "Flip them off!" if True:
                show chelsea angry
                "They rev their engine and speed away, but you feel a little better."
                hide chelsea with dissolve
            "Ignore them." if True:
                "Their voices fade as you move farther away."
                "Even though you didn't do anything, you feel like you made a good decision."
            "Blow them a kiss!" if True:
                show chelsea happy
                "They whistle and yell even louder, but you kind of enjoy the attention."
                "When they finally drive away, you smile to yourself."
                hide chelsea with dissolve
    elif genericevent1 == 3:
        "The sun is bright and the birds are singing as you make your way to practice."
        "You can't help but think that it's going to be a great day."

    if genericevent2 == 1:
        "Despite your best efforts, you do very poorly today."
        "The coach isn't pleased with your times and questions whether you really want to be part of the team."
    elif genericevent2 == 2:
        "You have a great practice and your times are really good."
        "The coach even acknowledges your improvement!"
    elif genericevent2 == 3:
        "Near the end of practice, August and Ryan get into another argument."
        show Ryan Angry at left with moveinleft
        show August Angry at right with moveinright
        "August" "You haven't beat me yet!"
        "Ryan" "The way your times have been lately, the cheerleaders could probably outrun you!"
        show CC Happy with dissolve
        "Coach" "Save it for the track, lovebirds. Both of you: three laps for arguing! Go!"
        show CC Blank
        "They glare at each other and you can see that it's about to be another competition."
        "In the first lap, they're neck and neck around the entire track."
        "As they finish the second, though, Ryan takes a good lead."
        "The whole team watches as they enter the final lap."
        "At the halfway point, Ryan still has a decent lead - but as they enter the home stretch, August suddenly shoots forward and easily overtakes him."
        "The whole team erupts in cheers when they finish."
        hide Ryan Angry with dissolve
        hide August Angry with dissolve
        show CC Serious
        "Coach" "Quit showing off! Three more laps for all of you - get to it!"
        "By the end of the day, you're completely beat!"
    jump events_end_period

label track_first_meeting:
    "At first it seems a little weird to be at school on a [dayname], but a lot of your teammates are there already."
    "You head to the track and look around, noting the group of students in athletic clothing by the bleachers."
    show chelsea at right with moveinright
    pcname "Is this where Track meets?"
    show Ryan Happy at left with dissolve
    "Ryan" "That's us! Are you new?"
    show chelsea happy
    pcname "Yeah, I just signed up the other day."
    "Ryan" "Awesome! Well, I'm Ryan."
    "He smiles down at you - he has a great smile."
    show chelsea blank
    "Ryan" "Coach will be here soon, so--"
    hide Ryan Happy with moveoutleft
    show CC Serious with dissolve
    "Coach" "All right team, form up!"
    show chelsea shocked
    "Everyone gets up and stands in a line - almost like an army standing at attention."
    show CC Happy
    "You half expect the others to salute!"
    show chelsea blank
    "Coach" "Lots of familiar faces, and... You!"
    show chelsea shocked
    "He points at you and you already feel like running!"
    show CC Neutral
    "Coach" "Introduce yourself!"
    show CC Blank
    pcname "I-- I'm [pcname]!"
    show chelsea blank
    show CC Happy
    "Coach" "All right... I'm sure everybody has heard this before, so we'll keep it short and sweet."
    show CC Serious
    "Coach" "You will all show up to practice on time and ready to move!"
    "Coach" "You will all come in appropriate clothes and shoes!"
    "Coach" "There will be {i}no{/i} arguing, {i}no{/i} back talk, and {i}no{/i} bad attitudes!"
    show CC Confused
    "Coach" "Any questions?"
    "Team" "No, Coach!"
    show CC Happy
    "Coach" "Good! Now get on the track and start stretching while I talk to the newbie!"
    show CC Blank
    "As the line breaks apart, the coach approaches you."
    show CC Serious
    "Coach" "[pcname]!"
    show chelsea confused
    pcname "C-Coach?"
    show CC Happy
    "Coach" "Glad you decided to join us! Now, would you say you're more of a distance runner or a sprinter?"
    menu track_intro_group:
        "Definitely distance!" if True:
            show chelsea happy
            "Coach" "Glad to hear you have some idea of what you're good at!"
        "Probably a sprinter." if True:
            show chelsea blank
            "Coach" "Great! We can always use another one!"
        "I have no idea..." if True:
            show chelsea embarrassed
            show CC Neutral
            "Coach" "You need to work on confidence and self-awareness; they'll get you far!"
            show CC Blank
    show chelsea happy
    pcname "Th-Thanks, Coach!"
    "Coach" "Go stretch with the team and we'll get started."
    show chelsea blank
    hide CC Blank with dissolve
    hide CC Happy with dissolve
    "Joining the others on the track, you mimic their stretches as best you can and take an opportunity to look at each of them."
    show August Blank with dissolve
    "One particular girl catches your eye, since she looks {i}nothing{/i} like an athlete."
    "Her short hair is dyed black with purple highlights, which match her purple lipstick and eyes, which you can only assume are contacts."
    "She glances up at you."
    show August Confused
    "August" "Got a problem?"
    show chelsea embarrassed
    pcname "Just trying to figure out these stretches..."
    "August" "Pssh..."
    show chelsea blank
    hide August Confused with moveoutleft
    "Without another word, she walks away."
    show chelsea angry
    pcname "Wow... Not very friendly, is she?"
    "You're talking to yourself, so you're a little surprised when someone answers."
    show chelsea blank
    show Ryan Happy at left with dissolve
    "Ryan" "That's August. She's one of the fastest runners on the team - but no, she's not very friendly."
    show Ryan Laugh at left
    pcname "I can tell..."
    hide Ryan Laugh with dissolve
    show CC Serious with moveinleft
    "Coach" "All right, team, time for some warm-up laps! Get into position!"
    "Looking around, you imitate the others and approach a line on the track."
    "Coach" "Three laps on my whistle! Remember: the faster you finish, the longer you can rest!"
    "You barely have time for the words to sink in before he blows the whistle."
    "After the three laps, the coach makes everyone run the track for an hour."
    "By the time his whistle signals the end of practice, your lungs are on fire and your legs feel like jelly."
    show CC Happy
    "Coach" "Nice job, team. Next practice we'll do 45 on the track and then hit the weight room."
    "Coach" "[pcname], you might want to take it easy tonight. Those muscles are going to {i}hurt.{/i}"
    "Before you've even left the school, you realize that he's right: {i}everything{/i} hurts."
    scene bg black with dissolve
    "You're too tired to do anything else, so you draw yourself a warm bath and head to bed."
    $ acts=1
    jump bed2

label track_august_intro:
    "When you get to the track, some of your teammates are already stretching."
    "Since you didn't have much time to socialize at the last practice, you don't really know anyone."
    "Feeling a little awkward, you stand off to one side and start doing some stretches of your own."
    show chelsea shocked at right with moveinright
    "Suddenly, someone pushes a cool bottle against your chest. You instinctively grab hold of it."
    "Seeing that it's a bottle of water, you look up to see who gave it to you."
    show August Blank at left with dissolve
    "It's the girl with the purple hair: August."
    show chelsea blank
    show August Neutral at left
    "August" "Noticed last practice that you didn't bring one. You'll need it."
    show August Blank at left
    show chelsea happy
    pcname "Thanks!"
    "Her face matches her matter-of-fact tone; she doesn't even bother smiling."
    show chelsea blank
    show August Confused at left
    "August" "So... why are you here?"
    menu august_intro_convo:
        "I had to pick a club." if True:
            show August Disappointed at left
            "August" "And you picked Track?"
            "August" "This isn't a game - we're here to {i}work{/i}."
        "I like to run!" if True:
            show chelsea happy
            show August Neutral at left
            "August" "It's about more than just that."
            "August" "Races take control and perseverance. You'll push your limits every time."
        "I think I made a mistake." if True:
            show chelsea embarrassed
            show August Disappointed at left
            "She shakes her head."
            show August Confused at left
            "August" "So you're just wasting our time, then?"
    show chelsea blank
    show August Blank at left
    "Before you can respond, the coach blows his whistle."
    hide August Blank with moveoutleft
    show CC Serious with moveinright
    "Coach" "Alright, everyone stretched and ready?"
    "He doesn't wait for a response."
    "Coach" "Line up for warm-up laps. When you've done your three, head up to the weight room!"
    "Since you know what to expect, you're ready when he blows the whistle."
    hide CC Serious with dissolve
    "The laps don't seem as bad this time - and you actually finish earlier than last time!"
    "Then, you grab your water bottle and head inside."
    "When you enter the weight room, you see that the people who finished before you are chatting on the mats."
    "You join them, listening to their stories about track meets and heats."
    show CC Neutral with moveinleft
    "Coach" "You guys know the drill: squats, lunges, jump rope, sit-ups, planks, then crunches. Fifteen minutes each!"
    hide CC Neutral with dissolve
    "As you go through the squats, you notice that August seems to be watching you."
    menu august_intro_workout1:
        "Pace yourself." if True:
            "You ignore her and maintain a decent pace."
            $ trackperf += 1
        "Go all out!" if True:
            show chelsea angry
            "You really push yourself to do as many as you can."
    "The whistle blows, signaling the switch to lunges - and again, you feel August's eyes on you."
    menu august_intro_workout2:
        "Pace yourself." if True:
            show chelsea blank
            "You focus on your exercises and do your best to ignore her."
            $ trackperf += 1
        "Push yourself!" if True:
            show chelsea angry
            "You decide to show her what you're made of!"
    "The whistle blows again and everyone grabs a rope."
    "This time you're {i}sure{/i} August is watching you."
    menu august_intro_workout3:
        "Don't push too hard." if True:
            show chelsea blank
            "Keeping a steady pace, you focus on your breathing and rhythm."
            $ trackperf += 1
        "Jump as fast as you can!" if True:
            show chelsea angry
            "You push yourself hard, jumping as fast as you can!"
    "When it's time to switch exercises, you toss your rope on the pile and drop to the mat for your sit-ups."
    "You don't have to look her way to know that August is still keeping an eye on you."
    menu august_intro_workout4:
        "Focus." if True:
            show chelsea blank
            "Breathing in as you sit up and out as you lay back down, you silently count your sit-ups."
            $ trackperf += 1
        "Show off!" if True:
            show chelsea angry
            "Giving it your all, you quickly lose count of all your sit-ups!"
    "Another whistle and you roll over for the planks."
    menu august_intro_workout5:
        "Look at the floor." if True:
            show chelsea blank
            "With all of your focus on your muscles, you hold the position as long as you can."
            "When it becomes too much, you lower yourself to the floor and let your muscles rest a bit before getting back into position again."
            $ trackperf += 1
        "Stare August down!" if True:
            show chelsea blank
            "You get into position and catch August's attention."
            "Maintaining eye contact, you hold the position until your arms and legs are trembling."
            "And then you hold it some more..."
            "Finally, she lowers herself to the mat and you let yourself drop too."
    "You're relieved to hear the whistle blow. Only one exercise left!"
    "Rolling onto your back again, you start doing crunches."
    if trackperf <3:
        "You've pushed yourself too hard, though, and can barely force yourself to do more than twenty crunches before you give up..."
        "After the final whistle, August approaches you."
        show August Confused at left with moveinleft
        "August" "We're here to train; it's not a competition."
        "August" "Next time, pace yourself a little better and you'll actually be able to {i}finish{/i} all the exercises."
        hide August Confused with moveoutleft
        "You want to defend yourself, but you know she's right."
    elif True:
        "You're tired and your muscles feel even worse than last practice, but you manage to keep going until the whistle blows."
        "As you lay on the mat, exhausted, August approaches you."
        show August Happy at left with moveinleft
        "August" "I'm actually pretty impressed. You did a good job today."
        show August Blank at left
        "August" "Whatever your reason for joining the team, you might be able to keep up."
        show chelsea happy
        pcname "Thanks!"
    show CC Happy with moveinbottom
    "Coach" "Nice job, team! Next practice is sprints, so be prepared!"
    "You leave practice exhausted; Track sure is a lot of work!"
    jump events_end_period

label track_ryan_intro:
    "Walking onto the track, you start your stretches."
    "You still don't feel like you know anyone, but you don't feel as awkward either."
    "Turns out Track really is good for your confidence!"
    show chelsea at right with moveinright
    show Ryan Happy at left with moveinleft
    "Ryan" "You ready for sprints?"
    show chelsea confused
    pcname "I'm... not sure?"
    show Ryan Laugh
    "He gives a deep, hearty laugh."
    show Ryan Happy
    "Ryan" "You've never done track before, have you?"
    show chelsea happy
    "You can't help but smile back."
    pcname "No... you caught me!"
    "Ryan" "What made you decide to join the team?"
    menu ryan_intro_join:
        "I heard there were cute boys!" if True:
            $ corruption += 1
            show chelsea embarrassed
            show Ryan Laugh
            "He laughs again."
            show Ryan Happy
            "Ryan" "And were the rumors true?"
        "I just had to pick a club." if True:
            show chelsea blank
            show Ryan Worry
            "Ryan" "Yeah, I get why they make us, but..."
            "He shrugs, letting his words trail off."
            show Ryan Happy
            "Ryan" "I guess you'll have to make the best of it, huh?"
        "It seemed like fun..." if True:
            show Ryan Laugh
            "Ryan" "It's great! I love the way it feels when you run: the blood pumping through your limbs, the air filling your lungs."
            show Ryan Happy
            "Ryan" "You know what I mean?"
    show chelsea blank
    "Before you can answer his question, you hear the coach's whistle."
    hide Ryan Happy with dissolve
    show CC Serious with moveinright
    "Coach" "Sprint day! Warm-up laps and then take your positions!"
    "You follow Ryan to the line and get ready."
    "When the whistle blows, you take off running, but Ryan quickly pulls ahead of you."
    hide CC Serious with dissolve
    "It's unbelievable how fast he is!"
    "Before long, you've completely lost sight of him."
    "When you finish your three laps, you step off the track to catch your breath."
    show Ryan Angry at left with moveinleft
    "Ryan" "Damn! She beat me again!"
    "Glancing over, you see Ryan shaking his head."
    show chelsea confused
    pcname "What?"
    "He clenches a fist as he responds."
    "Ryan" "August!"
    pcname "It wasn't a race, though."
    "Ryan" "It's {i}always{/i} a race!"
    show chelsea shocked
    "He suddenly swallows his frustration and visibly relaxes."
    show chelsea blank
    show Ryan Worry
    "Ryan" "Sorry, I-I guess I take it a little too seriously sometimes..."
    menu ryan_intro_august:
        "It's fine." if True:
            show Ryan Happy
            "Ryan" "You weren't too bad out there, you know."
        "You'll beat her next time!" if True:
            show chelsea happy
            show Ryan Happy
            "Ryan" "Thanks..."
    "The whistle's shrill sound cuts through the air."
    show chelsea blank
    hide Ryan Happy with dissolve
    show CC Neutral with moveinleft
    "Coach" "Line up for sprints, team!"
    show CC Blank
    "As everyone takes their spots again, he explains what you're doing."
    show CC Neutral
    "Coach" "Fifteen 200 meter sprints! When you've finished, line up and wait for the next one!"
    "When the whistle sounds again, you take off."
    hide CC Neutral with dissolve
    "There's little time to talk, or do much more than catch your breath between sprints, but when you've finished the last one you see Ryan walking toward you."
    show Ryan Happy at left with moveinleft
    "Ryan" "How are you feeling?"
    menu ryan_intro_sprints:
        "Awesome!" if True:
            show chelsea happy
            show Ryan Laugh
            "He grins."
            show Ryan Happy
            "Ryan" "Makes you feel alive, huh?"
        "Tired." if True:
            show chelsea sad
            show Ryan Tired
            "Ryan" "Yeah, the first few times are pretty rough!"
            show Ryan Happy
        "Kind of sick..." if True:
            show chelsea sad
            show Ryan Laugh
            "He laughs."
            "Ryan" "That's pretty normal, actually. I usually vomit after races."
            show chelsea shocked
            pcname "Really?"
            show Ryan Happy
            "Ryan" "Yeah. It's a lot of stress on your body!"
    show chelsea blank
    show CC Happy with moveinright
    "Coach" "Alright! Nice job today, team! Everyone head home and rest up!"
    "Ryan" "It was nice chatting with you today, [pcname]. See you around?"
    pcname "Definitely!"
    "Walking home, you can't help but smile; it seems like you're finally part of the team!"
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
