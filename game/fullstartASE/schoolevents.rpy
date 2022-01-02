label schoolevents:
    $ clothes = "school"
    stop music fadeout 3.6
    show black with dissolve
    if clubday == True and daycount > 1:
        if wenttoclub == False and acts == 4:
            $ goingto = "club"

            if club == "track":
                $ clothes = 'track'
                scene bg TrackD with fade

            if club == "cheer":
                if cheerfirst1 == True:
                    pass
                elif True:
                    $ clothes = 'cheer'
                    $ hair = 'ponytail'

                scene bg Cheerlocker with fade

            if club == "yearbook":
                scene bg Art with fade

            call eventengine from _call_eventengine_6

            jump city2
        elif wenttoclub == False and acts < 4:
            "You've missed the club activities today."
            jump city2
        elif True:
            "You've already been to your club meeting today!"
            jump city2
    elif schoolday == False:
        "There's no school on weekends!"
        jump city2

    $ goingto = "school"

    if daycount == 1:
        pass
    if daycount == 43 and MafiaFavorMatt:
        call MattMafiaResolution3 from _call_MattMafiaResolution3
    elif wenttoschool:
        scene bg ClassroomE with dissolve
    elif True:
        scene bg ClassroomD with dissolve
        $ intelligence -= 1

    if defymatt == True and endgame == True:
        jump matt_blackmail_endgame

    if wenttoschool == False:
        if havehomework and not completehomework:
            "As soon as you sit down, you realize you forgot to do your homework."
            "Despite your various excuses, the teacher gives you an F; your grades suffer."
            $ intelligence -= 4
            $ havehomework = False
            $ homeworkgirls = False
        elif havehomework and completehomework:
            "You turned in your homework. Good job! This will keep your grades up!"
            $ intelligence += 5
            $ homeworkgirls = True
            $ completehomework = False
            $ havehomework = False

    call eventengine from _call_eventengine_1

    $ goingto = "textschool"
    $ TextCheck = True

    call events_run_period from _call_events_run_period_3

    $ TextCheck = False
    $ wenttoschool = True
    $ homeworkgirls = False
    $ varhomework = renpy.random.randint(1, 7)

    if daycount > 1:
        if varhomework < 3:
            $ havehomework = True
        if havehomework:
            show bg black with dissolve
            "You were assigned homework at school today. It's waiting for you at home."

    jump city2


label schoolintro:
    show bg School with fade
    "You approach the school and see a large crowd of students pouring in. Many of them stop to stare at you."
    pcname "Alright, so first off..."
    scene bg black with fade
    "You wade through the crowd and walk to the one place you've been before: the principal's office."
    "You approach the door and knock."
    P "Come in."
    show bg Office with fade
    "You do as you're told. The office smells slightly like coconuts, and everything feels like it's been methodically arranged."
    show P Blank at left with moveinleft
    P "Ah, good. You're here. Did you find it okay?"
    show chelsea at right with moveinright
    menu:
        "Yeah, no problem." if True:
            show chelsea happy
            P "Glad to hear it!"
        "I had a bit of trouble..." if True:
            show chelsea embarrassed
            P "Really? Well, I'm sure that won't be an issue for long."
    $ renpy.block_rollback()
    P "So, are you ready for your first day? Did you bring spare clothes, a toothbrush, some lunch?"
    show chelsea confused
    "You raise an eyebrow."
    pcname "You make it sound like I'll be living here..."
    P "Did you not read the handbook?"
    show chelsea shocked
    "You feel a momentary swell of confusion, until..."
    "The principal sees this and laughs, adjusting the lapels of his suit."
    show P Laugh at left
    P "I'm joking, of course."
    show chelsea happy
    "You smile; you almost believed him."
    show P Blank at left
    P "Alright, let's get down to business..."
    scene bg black with dissolve
    "The principal goes over the rules with you and makes sure all of your paperwork is in order."
    "Once you're finished, he calls in your homeroom teacher: Mr. Harley."
    scene bg Office with dissolve
    show Harley Blank at left with moveinleft
    show P Blank with dissolve
    show chelsea blank at right with dissolve
    P "Alright, you're all set."
    P "Mr. Harley, could you show [pcname] to her classroom, please?"
    show Harley Neutral at left
    T "Of course! Not a problem."
    scene bg black with fade
    "[T] escorts you down the hall and to the classroom."
    scene bg ClassroomD with dissolve
    show Harley Blank at left with moveinleft
    show chelsea blank at right with moveinright
    "You walk into the room together. All eyes are on you..."
    show Harley Happy at left
    T "Everyone, we have a new student joining us today."
    "He looks expectantly at you."
    show Harley Neutral at left
    T "Go ahead, introduce yourself."
    show Harley Blank at left
    menu:
        "Be confident." if True:
            show chelsea happy
            pcname "Hello everyone, my name is [pcname] and I recently moved here from Anastar. I look forward to getting to know you all!"
        "Be shy." if True:
            show chelsea embarrassed
            pcname "H-Hello... I'm [pcname]. I'm new here, as you know... Um... it's nice to meet all of you."
            $ greeting = False
    $ renpy.block_rollback()
    show chelsea blank
    show Harley Neutral at left
    T "Alright, [pcname]. How about you take the empty seat in the back - right in front of Matt?"
    show Harley Blank at left
    "It doesn't take you long to find your seat, directly in front of a leering young man."
    hide Harley Blank with moveoutleft
    "You set your backpack down and notice that Matt is {i}still{/i} staring."
    show chelsea confused
    "At this rate, he might burn a hole in the back of your skull!"
    show Harley Neutral at left with dissolve
    T "Okay class, we're going to start with some basics to refresh your memory about..."
    hide Harley Neutral with dissolve
    show chelsea blank
    "The entire class shifts their attention towards Mr. Harley as he starts his lecture."
    "You listen intently - until you feel something brush your left side."
    scene bg MattGrab with fade
    "Matt's hand slowly moves up, then pauses momentarily to cup your left breast."
    "You're too surprised to react... but then he gives it a firm squeeze."
    menu:
        "Slap him!" if True:
            $ mattslap = 1
            $ unlock_ach(ouch)
            scene bg MattSlap with dissolve
            $ mattsubmissive = False
            "On instinct, you shoot up from your desk. With a quick spin of your hips, you feel your hand connect with Matt's face - {i}hard.{/i}"
            "Everyone in the room turns in unison and stares."
            "Matt gently cradles his injury, seemingly trying not to cry."
            show bg ClassroomD with fade
            show Matt Angry at left with moveinleft
            show Harley Question with dissolve
            m "What the fuck was that for!?"
            show Harley Angry
            T "It's only been five min-- *Sigh* Fine. Both of you to the principal's office! I'll be there in a bit."
            scene bg black with dissolve
            "After a harsh scolding from the principal, Matt is given detention and you're let off with a stern warning not to slap any other students."
            "At the very least, you have a feeling you won't be hearing from Matt again."
        "Scream!" if True:
            $ mattsubmissive = False
            scene bg MattScream with dissolve
            "You cover your breasts with your hands and let out a loud scream. Almost everyone in class jumps at the sudden sound."
            show bg ClassroomD with fade
            show Harley Question
            T "What on Earth was that about!?"
            pcname "P-Pervert!"
            "As soon as the words leave your mouth, you drop your eyes to your desk in embarrassment."
            show Harley Angry
            "[T] looks between you and Matt - who is trying (and failing) to seem as shocked as everyone else."
            T "Matt! To the principal's office. {i}Now!{/i}"
            show Matt Angry at left with moveinleft
            m "I didn't even do anything, Mr. H!"
            T "Don't question me!"
            m "Fine... {size=14}{i}Bullshit...{/i}{/size}"
            show Harley Neutral
            T "Right. Now, back to the lesson."
            show Harley Blank
            "You raise your head and try to follow along."
            "In the end, though, all you can think of is that Matt probably won't be bothering you again."
        "Do nothing." if True:
            scene bg MattAccept with dissolve
            if greeting:
                m "Heh, I look forward to getting to know you too."
            elif True:
                m "Hmm, it's nice to meet you too..."
            "He continues to fondle you, running his fingers over your stiffening nipples."
            scene bg MattGrab with dissolve
            "You try to follow along with the lesson, pretending everything is normal."
            "After a minute, Matt releases you - seemingly satisfied."
            $ corruption += 1
            show bg ClassroomD with fade
    $ mattchain +=1
    $ renpy.block_rollback()
    hide Matt Angry with dissolve
    "The rest of the day goes pretty well. Eventually, school is let out and you head home."
    scene bg black with fade
    pause 0.2
    scene bg HomeD with dissolve
    $ clothes, hair = casualwear
    "You change into something a bit more casual."
    show chelsea blank at right with moveinright
    pcname "I guess I better go and see if I can find a job..."
    $ wenttoschool = True
    hide chelsea with dissolve
    jump events_end_period

label schooleventback:
    if mattsubmissive == True:
        "You enter the classroom, ready for your second day of school. You spot your seat - as well as Matt, who is obviously undressing you with his eyes."
        "He opens his mouth to speak, but the bell cuts him off and class begins."
    elif mattsubmissive == False:
        "You enter the classroom, ready for your second day of school. You stride over to your seat and notice that the guy behind you is absent today."
        "That's probably a good thing."
        "After the bell rings, the teacher gets everyone to quiet down so that he can begin."
    "The class goes over the basics from the previous day; the teacher does his best to keep everyone's attention."
    "You're working on a worksheet Mr. Harley handed out when the bell finally rings."
    T "Alright, bring your sheets to the front and hand them in - even if you didn't finish."
    "You sling your bag over your right shoulder and head to the front like everyone else; Mr. Harley smiles at you when you do so."
    "You're walking to your next class when you see a familiar face flag you down in the hallway."
    show P Blank at left with moveinleft
    show chelsea at right with moveinright
    if mattslap == 1:
        P "Hello there, [pcname]. I hope you haven't had the urge to slap any boys today."
        show P Laugh at left
        "He gives a hearty laugh."
        menu:
            "He deserved it." if True:
                show P Blank at left
                P "Yes, well... even though he {i}did{/i} assault you, we cannot condone violence. Today's slap could be tomorrow's food fight."
                "Come to think of it, a food fight {i}does{/i} have its appeal..."
                pass
            "Not yet!" if True:

                show P Blank at left
                P "Well, the next time you have the urge to slap someone so hard it leaves a bruise, please come and tell me instead. Okay?"
                pcname "Okay..."
                P "Great! Now that we have that settled..."
                pass

    elif mattslap == 0:
        P "Hello there [pcname]. I hope your second day of school has turned out to be a delightful one."
        menu:
            "It has so far." if True:
                show chelsea happy
                P "That's great to hear. It's so good to see a student enjoying themselves; I would say that's rare these days."
                pass
            "It's school. How is that delightful?" if True:

                P "Well, school is often said to be the happiest years of one's life. Students enjoy coming here to meet with friends, and I think that schools should be a perfect blend of enjoyment and education."
                P "Speaking of enjoyment..."
                pass
    P "Could I speak to you in my office for a moment? There's something that we need to discuss."
    show chelsea happy
    pcname "Sure."
    P "Great, come with me."
    hide chelsea
    hide P Blank
    show bg black
    "You follow the principal to his office."
    show bg Office with fade
    "When you enter, that same scent of coconut wafts into your nose. He motions for you to take a seat across from his desk."
    show P Blank at left with moveinleft
    show chelsea at right with moveinright
    P "Now, [pcname] I'll get right to it: one of our policies is that a student has to join a club. The school board believes it will help cultivate the students' personalities, social lives, and talents."
    P "Since you're new here, you'll need to join one as soon as possible. Today is club orientation - so after school I'd like you to visit each and determine which is right for you."
    menu:
        "What if I don't like any of them?" if True:
            P "You'll have to settle, then. I'm afraid we can't make any exceptions."
        "Do I really need to?" if True:
            show chelsea confused
            P "Yes. I'm afraid those are the rules, but you have my condolences..."
    show chelsea blank
    "Shortly after his explanation, he pulls a sheet of paper from one of his drawers and hands it to you."
    P "That's the sign-up form; I've highlighted the clubs whose rosters aren't full."
    P "Take it with you and fill it out when you decide on one you like."
    pcname "I will."
    P "Great! That's all I have for you. Also, watch out for my pet snake on your way out; he's slithering around here somewhere..."
    show chelsea shocked
    "The principal's face lights up once he sees your reaction."
    show P Laugh at left
    P "I'm joking! You should have seen the look on your face."
    P "Anyway, please enjoy the rest of your day."
    show chelsea angry
    "He really gets on your nerves sometimes..."
    hide P laugh
    hide chelsea
    show bg ClassroomD
    "But now you have to think about what club you want to join. You'll have to visit them once school is over for the day."
    "Classes seem to drag on forever; you suppose that's how it is when you have a lot to think about."
    "Eventually, the final bell rings and it's time for you to go check out each of the clubs for yourself."
    show chelsea at right with moveinright
    "You pull out the sign-up sheet and look it over."
    show chelsea shocked
    pcname "What!? There are only three clubs highlighted!"
    pcname @ sad "I guess the rest are all full..."
    show chelsea blank
    "Sighing, you look over your options."
    pcname "Track... Cheerleading... and..."
    pcname "Yearbook."
    pcname "Guess I should go check them out."
    hide chelsea with moveoutright
    if persistent.clubseen == True:
        menu skipcluborientation:
            "Would you like to skip learning about the clubs and choose one now?"
            "Yes" if True:
                jump clubchoice
            "No" if True:
                pass
    elif True:
        pass
    "The form says that orientation will be held in the gym, so you quickly make your way there."
    show bg black with fade
    show bg GymClub with fade
    "The room is full of people. Each club has a banner or sign, with a few directing you to other meeting places."
    show chelsea at right with moveinright
    pcname "Guess they couldn't fit {i}everyone{/i} in here."
    pcname "There's the sign for Track. Guess I'll see what they're like first."
    "As you approach the banner, you're met by a tall, intimidating man."
    show CC Neutral with dissolve
    "Coach" "You look like a runner for sure."
    show chelsea confused
    pcname "I guess so?"
    show CC Serious
    "Coach" "Confidence is key in sports. It's not enough to {i}want{/i} to win; you've got to {i}know{/i} you will."
    show chelsea blank
    pcname "What if you can't?"
    show CC Blank
    "He shakes his head."
    show CC Happy
    "Coach" "It's all about the attitude. I'm Coach Carrigan. Were you thinking of joining us?"
    menu trackteam:
        "Maybe." if True:
            pcname "I was hoping to get a feel for all of my options before I make a decision."
            "Coach" "Always good to make an informed choice, then give it everything you've got!"
            show CC Neutral
            "Coach" "We're going to get started. Stick around if you want."
        "Definitely!" if True:
            show chelsea happy
            "Coach" "I like your confidence! You'll make a great addition to the team."
            show chelsea blank
        "Probably not..." if True:
            show CC Neutral
            "Coach" "You've gotta be confident to succeed with us!"
    show CC Blank
    "He moves to stand in front of several sitting students."
    show CC Happy
    "Coach" "Glad to see all of you back this year - and better to see a few new faces."
    "He nods at a few of the assembled students before continuing."
    "Coach" "We're set to have a great year. With hard work and a positive attitude, we'll take district championships for the fourth year in a row."
    "It sounds like a lot of work, but with a record like that it should be worthwhile!"
    "You want to see all of the options, though, so you look around for the other two clubs."
    hide CC Happy with dissolve
    "Ms. Vicky" "Okay, girls, are you ready for another great year!?"
    "You follow the voice, which - you can already tell from the upbeat tone - must belong to the Cheer Squad's coach."
    "A young woman stands before a group of smiling girls. Your gaze catches her attention and she looks your way."
    show MV Smile at left with moveinleft
    "Ms. Vicky" "A new face! Give me just a minute, ladies."
    "She approaches you, practically bouncing with energy."
    "Ms. Vicky" "You're so cute! And that body!"
    show chelsea embarrassed
    "She looks you up and down."
    "Ms. Vicky" "You look {i}quite{/i} mature for your age. The boys must go crazy over you!"
    show MV Blank at left
    "Tilting her head, she gives you a knowing look."
    show chelsea blank
    pcname "I--"
    show MV Laugh at left
    "Ms. Vicky" "Don't be shy! You're thinking of joining the Cheer Squad, right?"
    pcname "I wanted to come see--"
    show MV Smile at left
    "Ms. Vicky" "Well, you'll have to get used to male attention~"
    "Ms. Vicky" "Boys just can't keep their eyes off a girl with a nice smile and a short skirt."
    "She winks at you."
    show chelsea confused
    pcname "Right. Yeah."
    show chelsea blank
    "Ms. Vicky" "I'm the {i}Cheer Leader~{/i}"
    show MV Laugh at left
    "She pauses to laugh at her own pun."
    "Ms. Vicky" "Get it? But, yeah, I'm Ms. Vicky."
    pcname "I'm [pcname]."
    show MV Smile at left
    "Ms. Vicky" "Ohhh, cute!"
    show MV Blank at left
    "Ms. Vicky" "Well, if you're here to learn more about Cheer, I guess I can fill you in."
    "Ms. Vicky" "We're always looking for girls who aren't afraid to show off their best assets."
    show chelsea confused
    pcname "Got it. Thanks!"
    show chelsea blank
    show MV Smile at left
    "Ms. Vicky" "I don't want to, but I've gotta go; we're picking out some new cheers for this season."
    "Ms. Vicky" "Hopefully we'll see you this weekend?"
    hide MV Smile with moveoutleft
    "She bounces off with a quick wave."
    show chelsea happy
    pcname "At least she seems nice..."
    "You watch the other girls for a few minutes. They all seem happy and enthusiastic."
    show chelsea blank
    pcname "Okay, one more to go..."
    "You look around for a while, but can't find the Yearbook Club."
    "Just as you're about to give up, you see a small table without a sign."
    "Approaching it, you notice a flyer laying flat on the surface."
    "{i}Yearbook Club in the Art Room{/i} has been scrawled in a hurried, nearly-illegible scribble."
    pcname "Guess I have no choice."
    hide chelsea with moveoutright
    show bg black with fade
    "As you walk down the hallway, you think about the other two clubs."
    "Track seems like a lot of work - and the coach seems really demanding - but they have a great record."
    "Cheerleading seems like more fun, but Ms. Vicky is really obsessed with appearances. At least she seems to like you, though."
    "You're still mulling it over when you open the Art Room's door."
    show bg Art with fade
    "Walking inside, you take a look around. Students are spread throughout the room, but you can't tell which group is having a club meeting."
    "There's a group of students sitting around a table, rolling dice."
    "A few are spread out reading books, and others are working on paintings and sketches."
    "One student is wearing a camera - but before you can approach her, a teacher stops you."
    show chelsea at right with moveinright
    show MD Closed Smile with dissolve
    "Mr. Davis" "Why hello there! Did you need something?"
    show chelsea confused
    pcname "I was looking for Yearbook."
    show chelsea blank
    show MD Neutral
    "Mr. Davis" "The-- Oh!"
    show MD Open Smile
    "He spreads his arms out and smiles."
    show MD Laugh
    "Mr. Davis" "Here we are!"
    show chelsea confused
    show MD Blank
    pcname "Isn't it a little... disorganized?"
    show MD Laugh
    "He laughs."
    show chelsea blank
    show MD Neutral
    "Mr. Davis" "To be honest, a lot of students join because they're not very sociable."
    show MD Closed Smile
    "Mr. Davis" "And budget cuts forced us to combine a few clubs, so we have a pretty diverse group of people."
    show chelsea confused
    pcname "Budget cuts?"
    show MD Neutral
    "Mr. Davis" "Indeed. This year they cut funding to the Photography Club, so most of them have joined us."
    show MD Worried
    "Mr. Davis" "The year before that, the Roleplaying Club fell below the membership minimum, so they lost funding as well."

    show MD Open Smile
    "Mr. Davis" "I was the teacher in charge of that club too, so they joined Yearbook and continued meeting here."
    show chelsea happy
    pcname "Wow... So everyone here is in the club?"
    show MD Laugh
    "He laughs again."
    show chelsea blank
    show MD Neutral
    "Mr. Davis" "I'm afraid so. For the most part, we split the work and let everyone do their own thing."
    "Mr. Davis" "It's a little disorganized - but as long as everything gets done, the principal doesn't complain."
    show MD Closed Smile
    "He puts a hand on your shoulder."
    show MD Neutral
    "Mr. Davis" "You seem disappointed."
    show MD Blank
    show chelsea embarrassed
    pcname "No, no. It's just... I have to pick a club and this is one of the only three left."
    "He nods sympathetically."
    show MD Neutral
    "Mr. Davis" "I understand. I hate that they force students to choose, but if the others don't appeal to you, you're welcome to join us."
    show chelsea happy
    show MD Closed Smile
    "His smile is warm and genuine. You can't help but smile back."
    show MD Open Smile
    "Mr. Davis" "Sorry to kick you out, but it's almost time for us to leave."
    show chelsea blank
    "Glancing over his shoulder, he leans in conspiratorially."
    show MD Closed Smile
    "Mr. Davis" "And it's always difficult to get the roleplayers out of character and away from their campaign."
    show MD Blank
    pcname "I bet."
    show MD Neutral
    "Mr. Davis" "Maybe we'll see you again soon?"
    pcname "Maybe."
    show MD Laugh
    "He laughs and gives your shoulder a squeeze before releasing you."
    show MD Open Smile
    "With a final look around, you step back into the hallway."
    hide MD Open Smile with dissolve
    hide chelsea with dissolve
    show bg black with fade
    pcname "Okay, well, that's all of them..."
    "Pulling the form from your backpack, you grab a pencil."
    jump clubchoice

label clubchoice:
    menu chooseaclub:
        "Which club would you like to join?"
        "Track" if True:
            pcname "Track seems active and that coach was all about being confident."
            pcname "Is that really the best choice for me?"
            menu confirmtrack:
                "Definitely!" if True:
                    $ club = "track"
                "Maybe not..." if True:
                    jump clubchoice
        "Cheerleading" if True:
            pcname "Everyone on the Cheer Squad seemed happy, and Ms. Vicky was really nice."
            pcname "Though... she seemed pretty concerned about appealing to boys..."
            pcname "Maybe I could be happy in that club?"
            menu confirmcheer:
                "Definitely!" if True:
                    $ club = "cheer"
                "Maybe not..." if True:
                    jump clubchoice
        "Yearbook" if True:
            pcname "Yearbook was really different. I wouldn't have to socialize if I don't want to..."
            pcname "Maybe that would be the best option?"
            menu confirmyearbook:
                "Definitely!" if True:
                    $ club = "yearbook"
                "Maybe not..." if True:
                    jump clubchoice
    "Making a check next to your choice, you take the paper back to the principal's office and leave it in his mailbox."
    pcname "Alright... I guess I have plans this weekend..."
    $ persistent.clubseen = True
    hide chelsea with moveoutright
    jump events_end_period


label schoolrandom01:
    "You didn't get a lot of sleep last night and you show up to class pretty tired."
    menu:
        "Catch up on sleep and skip the lesson?"
        "Yes..." if True:
            "You sleep through most of the period, but you feel refreshed when you wake up."
            $ intelligence -=3
        "No." if True:
            $ intelligence += 1
            "You don't want to fall behind, so you try your best to stay awake."
            "As hard as it may be to keep your eyes open, you somehow manage."
    jump events_end_period


label schoolbully:
    "On your way into the school, you see some kids crowded around two male students. One is taller and clearly more intimidating; the other is cowering underneath him."
    show Alex Angry with dissolve
    show Damien Sad at left with moveinleft
    menu schoolbullyhelp:
        "Help." if True:
            $ bullytelloff = 1
            "You push your way through the crowd."
            show chelsea at right with moveinright
            if club == "track":
                show Damien Neutral at left
                pcname "Hey, leave him alone!"
                "The crowd gasps."
                "The taller boy looks surprised. He glares down at you."
                "Tall Boy" "Fine. I’ve got better things to do than fight a girl anyway."
                hide Alex Angry with moveoutright
                "He storms off, pushing his way through the crowd."
                show Damien Worry at left
                "Short Boy" "Th-Thanks."
                show chelsea blank
                pcname "No problem. I can’t stand guys like that."
                show Damien Happy at left
                "Short Boy" "Better get going or we’ll both be late for class."
                "He’s right. The crowd has already dispersed."
                show chelsea happy
                pcname "Alright. Good luck!"
                "He smiles at you and hurries off."
                "As you watch him go, you realize you forgot to ask his name."
            if club == "cheer":
                show Damien Neutral at left
                pcname "Oh, you're such a big, strong man! Picking on a kid half your size!"
                "The crowd gasps."
                show Alex Serious
                "The taller boy looks surprised. He glares down at you."
                show Alex Neutral
                "Tall Boy" "Yeah? I’ve got better things to do than fight a girl anyway."
                hide Alex Neutral with moveoutright
                "He storms off, pushing his way through the crowd."
                show Damien Worry at left
                "Short Boy" "Th-Thanks. I think."
                show chelsea blank
                pcname "No problem. I can’t stand guys like that."
                show Damien Happy at left
                "Short Boy" "Better get going or we’ll both be late for class."
                "He’s right. The crowd has already dispersed."
                show chelsea happy
                pcname "Alright. Good luck!"
                "He smiles at you and hurries off."
                "As you watch him go, you realize you forgot to ask his name."
            if club == "yearbook":
                "Swallowing your fear, you take a deep breath and..."
                show Damien Neutral at left
                pcname "H-hey! St-stop it!"
                "The crowd gasps."
                show Alex Serious
                "The taller boy looks surprised. He glares down at you."
                "Tall Boy" "Oh n-no! Sh-She's going to b-beat me up!"
                show Alex Laugh
                "He laughs, clearly not intimidated."
                show Alex Serious
                "Tall Boy" "Don't worry; I'm not going to fight a {i}girl{/i}."
                hide Alex Serious with moveoutright
                "He walks away, pushing through the crowd."
                show Damien Worry at left
                "Short Boy" "Th-Thanks..."
                show chelsea blank
                pcname "You're... welcome. I can't believe I just did that..."
                show Damien Happy at left
                "Short Boy" "Better get going or we’ll both be late for class."
                "He’s right. The crowd has already dispersed."
                show chelsea happy
                pcname "R-Right. Good luck!"
                hide Damien Happy with moveoutleft
                "He smiles at you and hurries off."
                "As you watch him go, you realize you forgot to ask his name."
        "Stay out of it." if True:
            "It's none of your business."
            "You skirt around the crowd and make your way to your first class."
            "The rest of your day is boring in comparison to that."
    jump events_end_period


label schoollunchtacos:
    "Today is Taco Tuesday!"
    "Lunch is delicious, but by the end of the day your stomach is in knots."
    "You can only wonder how the janitors feel..."
    jump events_end_period

label schoolrainyday:
    show bg CityE with dissolve
    "As you walk to school, it begins to rain."
    show chelsea at right with moveinright
    pcname "I forgot my umbrella!"
    "You could go home and get one, but then you’ll definitely be late."
    menu schoolrainydayumbrella:
        "Walk in the rain." if True:
            $ intelligence += 1
            "You continue to school despite the weather."
            "Although you arrive on time, your wet hair and clothes make you uncomfortable."
        "Go get an umbrella." if True:
            "You head back home to change and grab an umbrella."
            "By the time you make it to school, you’ve missed a few classes - but at least you’re not soaked!"
            $ intelligence -=1
        "Just skip school." if True:
            pcname "If I’m going to miss part of the day, what’s the point?"
            $ intelligence -=5
            "You head back home to change."
            $ skippedschoolcounter += 1
            $ skippedschool = True
            $ havehomework = False
    jump events_end_period

label schoolfriends01:
    show bg Cafeteria with fade
    show chelsea at right with moveinright
    "During lunch, after you’ve gotten your plate, you’re flagged down by a black-haired girl."
    "Her long hair is quite messy - in an oddly familiar way."
    "Then it hits you: she sits in front of you in homeroom. Her name is Violet, if you recall correctly."
    "You sit down in the empty seat across from her."
    show V School Smile at left with moveinleft
    "Violet" "Hey, new girl! Thanks for coming over. Figured you hadn’t made many friends yet, so I thought I’d introduce myself."
    if club == "track":
        pcname "Oh, yeah. I'm [pcname]."
        pcname "You're Violet, right?"
        V "So you {i}do{/i} remember!"
    elif club == "cheer":
        show chelsea happy
        pcname "Violet, right? I'm [pcname]!"
        V "That's me; I'm glad you remembered."
    elif club == "yearbook":
        pcname "Oh... My name is [pcname]."
        "She watches you a moment, as if waiting for something. You shift uncomfortably."
        show V School Blank at left
        V "Since you don't seem to remember... I'm Violet."
        show chelsea embarrassed
        pcname "Oh! No, I... I remember you."
    show chelsea blank
    if pcname == "Violet":
        show V School Pout at left
        V "That's interesting though. Really. What's your name?"
        pcname "Seriously, it's Violet."
        show V School Smile at left
        V "Hmph. I guess your parents had good taste."
    show V School Smile at left
    V "Anyway, I thought I'd let you eat at my table since you don't have anywhere else to go."
    if club == "track":
        "You can't help feel a little put off by her presumption, but you decide to let it go and take a seat."
    elif club == "cheer":
        "Sliding into the chair across from her, you shrug."
        pcname "If you insist."
    elif club == "yearbook":
        "Grateful, you take a seat."
        pcname "Thanks."
    if mattslap > 0:
        V "By the way... I {i}love{/i} that you slapped that creep."
        if club == "track":
            pcname "He definitely deserved it."
        elif club == "cheer":
            pcname "He just groped me all of a sudden. Who {i}does{/i} that!?"
        elif club == "yearbook":
            show chelsea embarrassed
            pcname "I was so angry... I've never done anything like that before..."
        V "The look on his face..."
        "She lets out a contented sigh."
    elif mattsubmissive == False:
        V "By the way... I'm {i}so{/i} glad you didn't take Matt's crap."
        if club == "track":
            pcname "He's a real creep, isn't he?"
        elif club == "cheer":
            pcname "I can't believe he thought I'd just {i}let{/i} him grope me like that."
        elif club == "yearbook":
            show chelsea embarrassed
            pcname "It was so embarrassing, but... I didn't know what else to do..."
        V "He's the {i}worst{/i}."
    show chelsea blank
    "She raises a hand, flipping it at the wrist as if she's holding a tray."
    "As she speaks, she twists it from side to side, as if to emphasize her words."
    V "Anyway, you've probably already heard, but my father's pretty important around here."
    "You hadn't heard."
    V "It's no big deal, but he's sort of the City Manager. It's like being the mayor, basically."
    if club == "track":
        pcname "Sounds important."
    elif club == "cheer":
        show chelsea shocked
        pcname "Oh, wow."
    elif club == "yearbook":
        show chelsea shocked
        pcname "...oh..."
    show chelsea blank
    show V School Blank at left
    V "Yeah, so a lot of people are intimidated by me, I guess."
    "You're not sure that's what they're intimidated by, but you think better of saying so."
    show V School Smile at left
    V "Anyway, if we're going to be friends, you should give me your phone number."
    if club == "track":
        show chelsea laugh
        "Shaking your head, you laugh."
        show chelsea confused
        pcname "Are we going to be friends?"
        V "I might change my mind, but for now: yes."
    elif club == "cheer":
        pcname "I don't know..."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Oh, right... Sure."
    show chelsea blank
    "She reaches over and grabs your phone."
    "Almost as fast as you can process what she's doing, she passes it back to you."
    $ chelseaContacts.contactsListed["Violet"] = "Violet<3"
    V "There we go!"
    call screen TextingScene("Violet", [TextMessage("Thx V", sender = False)])
    if club == "track":
        pcname "Yeah... Thanks."
    elif club == "cheer":
        pcname "Right..."
    elif club == "yearbook":
        pcname "Oh. Okay..."
    V "Anyway! I'll fill you in on {i}everything{/i} you need to know..."
    "It looks like - whether you like it or not - you've made a new friend!"
    $ violetscenes += 1
    jump events_end_period

label teacherstain:
    show chelsea at right with moveinright
    "During study hall, you see your teacher rubbing a napkin on his desk."
    T "How did that get there?"
    "Suddenly, you realize what he's looking at: the stain you left on his desk when Matt and Alex..."
    if defymatt:
        "A fresh wave of nausea floods you."
        if club == "yearbook":
            "You don't want to think about that anymore!"
            "Face burning with shame, you watch as he vigorously rubs at the flat surface."
        elif club == "track":
            "You sway in your seat, watching uneasily."
            "He rubs vigorously, but the stain remains."
        elif club == "cheer":
            "You shake your head, trying to clear the memory from your mind."
            "Despite his... {i}vigorous{/i}... rubbing, the stain remains."
    elif True:
        if club == "yearbook":
            show chelsea embarrassed
            "You don't want to think about that anymore!"
            "Face burning with embarrassment, you watch as he vigorously rubs at the flat surface."
        elif club == "track":
            show chelsea embarrassed
            "You flush at the memory."
            "He rubs vigorously, but the stain remains."
        elif club == "cheer":
            show chelsea happy
            "You smile at the memory."
            "Despite his... {i}vigorous{/i}... rubbing, the stain remains."
    T "Must have left some soda there or something..."
    show chelsea blank
    "He continues for another minute or two, then moves some papers to cover up the stain."
    T "I guess I'll have to talk to the janitor..."
    "Behind you, Matt lets out a low chuckle."
    jump events_end_period

label booksknockoff:
    "Walking to your next class, someone's shoulder hits yours - knocking the papers and books you were carrying to the floor."
    if club == "track":
        show chelsea angry at right with moveinright
        pcname "Hey! Watch where you're going!"
    elif club == "yearbook":
        show chelsea sad at right with moveinright
        pcname "Oh!"
    elif club == "cheer":
        show chelsea angry at right with moveinright
        pcname "Hey! Rude!!"
    "You turn to face the culprit, but they've already disappeared into the crowd."
    show chelsea blank
    "Sighing, you kneel down to collect the scattered sheets. Students pass by you like ants avoiding a fallen twig."
    if violetscenes > 1:
        "???" "[pcname]?"
        "Before you can look up, the person who called your name has already gotten down to help - it's Violet!"
        show chelsea happy
        show V School Blank at left with moveinleft
        pcname "Oh, hey! Thanks for the help... Some jerk bumped into me and my stuff went everywhere."
        show V School Annoyed at left
        V "I can see that..."
        show V School Smile at left
        V "Don't worry about it, though. It's happened to everyone at least once."
        show chelsea blank
        pcname "Everyone's just so pushy."
        "Before long, you've gathered your things."
        pcname "Thanks a lot, Violet!"
        V "Don't mention it. I'll see you later!"
        "She waves as she heads to her next class. Speaking of which, you need to hurry too."
        "Somehow, you make it just in time!"
        jump events_end_period
    elif True:
        pass
    "Picking up everything takes longer than you thought - especially with people trampling or scattering the papers."
    $ intelligence -= 5
    "Thanks to whoever hit you, you're going to be late now. Great..."
    jump events_end_period

label schoolrainygym:
    $ gymchoice = renpy.random.randint(1,2)
    show chelsea at right with dissolve
    show bg Gym with fade
    "Thunder echoes overhead and the rain beats hard against the gymnasium windows."
    "You sit with the other students on the bleachers and finish tying your gym shoes."
    "Coach Phillips" "Alright, class. Listen up!"
    "Your coach claps his hands together, gathering your attention."
    "Coach Phillips" "Looks like we won't be able to have class outside today. I got a couple of substitutes in mind."
    "Coach Phillips" "I'll be calling out a couple of activities to do. Raise your hands and we'll go with the highest vote."
    menu rainygymchoice:
        "What would you like to play?"
        "Dodgeball." if True:
            show chelsea happy
            "You raise your hand when Coach Phillips calls out dodgeball."
            "Coach Phillips counts the set of hands."
            "Coach Phillips" "Alright! Dodgeball it is!"
            "He walks across the gymnasium floor and wheels over a large bin filled with sturdy red balls."
            show chelsea blank
            "Coach Phillips" "Everyone grab one and spread out!"
            if club == "track":
                "You grab one of the balls and stand confidently near the center of the gym."
            elif club == "cheer":
                "You pick up one of the balls and step to the side, readying yourself."
            elif club == "yearbook":
                "You take one of the balls and step to the back of the gym, out of the way."
            "Coach Phillips blows his whistle."
            "Coach Phillips" "Go!"
            "There's a pause as your classmates glance around, daring each other to go first."
            "Then the first ball flies."
            "It knocks a girl in the chest."
            "Coach Phillips points to the bleachers. She's out."
            "The balls fly in full force."
            show chelsea blank
            "You spot a couple of boys open nearby."
            menu dodgeball1:
                "Throw left." if True:
                    "You wind your arm back and toss your ball to the boy on the left."
                    if gymchoice == 1:
                        show chelsea sad
                        "The boy dodges to the right, slipping past your throw."
                        "Your ball bounces sadly against the ground."
                    elif gymchoice == 2:
                        show chelsea happy
                        "The boy attempts to dodge, but your ball smacks him against his shoulder."
                        "Coach Phillips waves him over to the bleachers. He's out."
                "Throw right." if True:
                    "You wind your arm back and toss your ball to the boy on the right."
                    if gymchoice == 1:
                        show chelsea sad
                        "The boy dodges to the left, slipping past your throw."
                        "Your ball bounces sadly against the ground."
                    elif gymchoice == 2:
                        show chelsea happy
                        "The boy attempts to dodge, but your ball smacks against his leg."
                        "Coach Phillips waves him over to the bleachers. He's out."
            show chelsea shocked
            "When you turn, you see a ball flying in your direction."
            if club == "yearbook":
                "You shriek and hold up your arm in defense."
                "The ball smacks against it. Coach Phillips gestures you toward the bleachers. You're out."
                show chelsea sad
                pcname "Oh..."
                "You sigh, silently relieved to be out of the fray as you take your seat on the bleachers."
                "You spend the rest of class doodling in your notebook as the dangerous game carries on."
                jump events_end_period
            elif True:
                show chelsea blank
                "You spot a discarded ball on the floor."
                menu dodgeballgrab:
                    "Grab it." if True:
                        show chelsea blank
                        "You grab it, holding it up just in time to deflect the ball coming at you."
                        show chelsea happy
                        "You feel a rush of adrenaline as it bounces to the floor."
                    "Leave it." if True:
                        "You leave it and try to duck instead. The incoming ball bounces off the back of your head."
                        "Coach Phillips" "That's a foul!"
                        show chelsea sad
                        "You huff, grabbing another ball from the ground. You're not out, but that still hurt."
                show chelsea blank
                "You search for your next target. Several of the students are out by now, clearing up the gymnasium floor."
                "A girl bounces back and forth on the edge of her toes, ready to dodge."
                "Across from her, two boys use their balls as shields in an attempt to knock incoming balls away from each other."
                "A shorter girl on your right ducks underneath incoming balls, jumping over ones aimed at her feet. She's just small enough for it to work."
                menu dodgeballhit:
                    "Hit the bouncing girl." if True:
                        "You toss your ball at the first girl that bounces on her feet."
                        if gymchoice == 1:
                            show chelsea happy
                            "She tries to throw herself to the ground, but instead throws herself directly in your path."
                            "Your ball strikes her against the chest. She gives out a little cry, moping back to the bleachers."
                        elif gymchoice == 2:
                            "She throws herself to the ground, just barely missing your throw."
                            show chelsea shocked
                            "The short girl winds her arm back, tossing her ball in your direction as you recover."
                            "It hits against your arm."
                            show chelsea sad
                            "You join the others on the bleachers, miserable at your loss."
                            "Better luck next time!"
                            jump events_end_period
                    "Hit the two boys." if True:
                        "It's a long shot, but you wind your arm back and toss it in the boys' direction."
                        if gymchoice == 1:
                            "The boys are so busy trying to deflect a throw the short girl aimed at them that they don't notice your ball until it's too late."
                            show chelsea happy
                            "The ball strikes right between their shoulders, knocking them both out."
                            "They let out groans of frustration as they slump back to the bleachers."
                        elif gymchoice == 2:
                            "You think they might be distracted as the short girl throws a ball their way, but the boy on the left turns your way, deflecting the throw with his ball."
                            show chelsea shocked
                            "The girl bouncing on her feet manages to toss a ball in your direction, hitting you square in the chest."
                            show chelsea blank
                            "You let out a grunt of pain, trying not to show your frustration as you slump back to the bleachers."
                            "Better luck next time!"
                            jump events_end_period
                    "Hit the short girl." if True:
                        "You squint at the short girl, trying to gauge her next move before you toss your ball in her direction."
                        if gymchoice == 1:
                            "The short girl anticipates your move and tries to jump."
                            show chelsea happy
                            "However, her foot catches on her shoelace, and she falls directly into your ball!"
                            "Coach Phillips motions towards the bleachers as she flops on the ground, rubbing her chin angrily."
                            "She huffs, dusting off her legs before joining the others."
                        elif gymchoice == 2:
                            "The short girl anticipates your move and jumps."
                            "She stumbles a little on her shoelace but catches herself just in time to avoid your throw."
                            show chelsea shocked
                            "The bouncing girl throws a ball in your direction, knocking you out by your leg."
                            show chelsea angry
                            "You give a look of annoyance as you join the rest of your classmates on the bleachers."
                            show chelsea blank
                            "Better luck next time!"
                            jump events_end_period
                show chelsea blank
                "As the game progresses, it comes down to you and one other student. You both face each other at the center of the gym, a red ball in each hand."
                "You try to anticipate which direction he'll go as you prepare to throw."
                menu dodgeballfinale:
                    "Throw left." if True:
                        "You wind your arm back and throw left."
                        if gymchoice == 1:
                            "The boy clutches the ball against his chest and slides to the right."
                            show chelsea shocked
                            "Before you can recover from your mistake, he throws his ball, knocking you in the chest."
                            show chelsea blank
                            "You let out a grunt as the students rise from the bleachers and cheer."
                            "Coach Phillips" "Good game, everyone! Alright, hit the lockers."
                            "You slump off to the lockers, miserable at your loss."
                            "Oh well. Better luck next time!"
                            jump events_end_period
                        elif gymchoice == 2:
                            "The boy clutches the ball against his chest and slides toward the left."
                            show chelsea happy
                            "He gasps as your ball smacks against his arm, knocking him out."
                            show chelsea laugh
                            "Students rise from the bleachers and cheer."
                            "Coach Phillips" "Good game, everyone! Alright, hit the lockers."
                            show chelsea happy
                            "You walk back to the lockers feeling a little more confident."
                            jump events_end_period
                    "Throw right." if True:
                        "You wind your arm back and throw right."
                        if gymchoice == 1:
                            "The boy clutches the ball against his chest and slides to the left."
                            show chelsea shocked
                            "Before you can recover from your mistake, he throws his ball, knocking you in the chest."
                            show chelsea blank
                            "You let out a grunt as the students rise from the bleachers and cheer."
                            "Coach Phillips" "Good game, everyone! Alright, hit the lockers."
                            "You slump off to the lockers, miserable at your loss."
                            "Oh well. Better luck next time!"
                            jump events_end_period
                        elif gymchoice == 2:
                            "The boy clutches the ball against his chest and slides toward the right."
                            show chelsea happy
                            "He gasps as your ball smacks against his arm, knocking him out."
                            show chelsea laugh
                            "Students rise from the bleachers and cheer."
                            show chelsea happy
                            "Coach Phillips" "Good game, everyone! Alright, hit the lockers."
                            "You walk back to the lockers feeling a little more confident."
                            jump events_end_period
        "Basketball." if True:
            "You raise your hand when Coach Phillips calls out basketball."
            "It takes a moment for him to tally the results."
            "Coach Phillips" "Alright! Basketball it is!"
            "Coach Phillips retreats to a net full of various sports-related balls across the gymnasium and pulls out a basketball."
            "He tosses it to your group. A short girl up front catches it."
            "Coach Phillips throws his hands down the middle of the group."
            "Coach Phillips" "Alright! Split up! Seven here, seven here!"
            "You each divide onto the correct side of the court. Coach Phillips takes a seat on the bleachers and blows his whistle."
            "Coach Phillips" "Go!"
            "The short girl throws the ball against the ground and dribbles it across the court."
            if club == "track":
                show chelsea angry
                "You chase after her, determined to steal it from her."
            elif club == "cheer":
                "You chase her alongside a few other classmates as they attempt to take it from her. If the ball goes in your direction, you'll catch it."
            elif club == "yearbook":
                "You hang back as your classmates rush toward her in an attempt to steal it."
            show chelsea blank
            "She throws it in the air, scoring a basket."
            "Her team lets out encouraging shouts. Someone from your team takes the ball, dribbling it to the other end of the court."
            "A couple of opposing teammates surround her, blocking her ability to score a basket."
            "Teammate" "[pcname]!"
            "Your classmate tosses the ball in your direction."
            if club == "track":
                "You reach your hands up for the ball instinctively."
                if gymchoice == 1:
                    show chelsea happy
                    "You catch it easily, dribbling it across the court. You manage to score a basket!"
                elif gymchoice == 2:
                    "The ball just slips from your fingers as an opposing teammate nudges you out of the way, taking the ball."
                    "You grit your teeth as they manage to score a basket with your ball."
            elif club == "cheer":
                "You quickly snap your attention toward the ball as it comes toward you."
                if gymchoice == 1:
                    show chelsea happy
                    "You raise your arms up, somehow catching it in time. You quickly dribble it across the court toward the opposing team's basket."
                    "You manage to score a basket! Awesome!"
                elif gymchoice == 2:
                    "You raise your arms up too late. It slips from your grasp, bouncing into the hands of an opposing teammate."
                    "You give the teammate a dirty look as they manage to score a basket."
            elif club == "yearbook":
                show chelsea shocked
                "You look too late up at the ball as it falls toward you."
                "The ball slams against your face, smashing into your nose. You let out a cry, instinctively reaching for your face."
                show chelsea sad
                "Teammate" "Oh my god, she's bleeding!"
                "Sure enough, as you pull your hand away from your nose, blood splotches your fingers."
                "Coach Phillips" "Time out!"
                "Coach Phillips approaches you, gently prying your hand away to get a good look at your nose."
                "Coach Phillips" "It doesn't look broken, but you should go see the nurse."
                "Coach Phillips" "Mia, go with [pcname] to the nurse's office."
                show chelsea embarrassed
                "Your teammate nods, quickly taking your arm. She escorts you out of the room and to the nurse's office."
                "You spend the rest of your class with cotton up your nose to stop the bleeding."
                "How embarrassing!"
                jump events_end_period
            show chelsea blank
            "The game continues, and near the end of class, your teams are tied."
            "You dribble the ball across the court, your gaze focused on the opposing team's basket."
            "Surrounding classmates try to surround you and steal the ball. You hold your arm out, blocking them."
            "Time is ticking down. You can see Coach Phillips glancing between you and the timer on his phone."
            "One of your teammates waves to get your attention."
            "Teammate" "[pcname]! Pass me the ball!"
            menu basketballpass:
                "Pass him the ball." if True:
                    "You glance at the crowd around you. There's too many. You won't be able to get a good shot in this way..."
                    "You toss the ball toward your teammate."
                    if gymchoice == 1:
                        "Your teammate leaps up, catching it. Before the opposing team can switch members, he throws the ball into the air."
                        "It lands into the basket easily, breaking the tie."
                        show chelsea happy
                        "Your team won!"
                        "You all shout in excitement at your win, gathering around your teammate as the opposing team saunters off to the locker rooms."
                        jump events_end_period
                    elif gymchoice == 2:
                        "Your teammate leaps up, catching it. Before the opposing team can switch members, he throws the ball into the air."
                        "It bounces against the edge of the basket, falling back into the court."
                        "An opposing team member steals the ball, dribbling it back on your side of the court."
                        show chelsea sad
                        "You race after him, but you aren't fast enough. He scores the winning basket."
                        show chelsea blank
                        "Although your team is unhappy with you for tossing him the ball, you can't help but glare at your teammate."
                        "You never should've given him the ball."
                        jump events_end_period
                "Shoot the basket." if True:
                    "You fake the ball towards your teammate, driving a couple of the students off your back as they turn in your teammate's direction."
                    "Your teammate gapes at you, disappointed by your choice."
                    "You bend your knees and shoot."
                    if gymchoice == 1:
                        "The ball slides into the basket. Coach Phillips's phone goes off. The game is over."
                        show chelsea happy
                        "You've won!"
                        show chelsea laugh
                        "Your teammates crowd around you, cheering in exhilaration as the opposing team sulks off to the lockers."
                        "You feel more confident about your decision as you join your team in the lockers after class."
                        jump events_end_period
                    elif gymchoice == 2:
                        show chelsea sad
                        "The ball bounces off the edge of the board."
                        show chelsea blank
                        "An opposing teammate grabs the ball, dribbling it across the court."
                        show chelsea sad
                        "You try to catch him, but he manages to make a basket before time is up."
                        show chelsea blank
                        "Coach Phillips's phone goes off. The game is over."
                        "As you walk back to the lockers with your team, your teammate glares at you."
                        "Teammate" "You should've just given me the ball."
                        "Yeah, maybe you should have."
                        jump events_end_period
        "Kickball." if True:
            "You raise your hand when Coach Phillips calls out kickball."
            "After he tallies the results, Coach Phillips claps his hands together."
            "Coach Phillips" "Alright! Kickball it is! Try not to hit the ceiling too hard!"
            "Coach Phillips walks to the back of the gymnasium and grabs a red ball out of a large bin."
            "Coach Phillips" "Separate in half! Seven versus seven. Choose your sides!"
            "You each shuffle into a group. You stand with the others in line to kick first."
            "Coach Phillips drops down some plastic mats for bases."
            "The others take places around the gym, guarding the bases."
            "Coach Phillips takes a seat on the bleachers and blows his whistle."
            "Coach Phillips" "First up!"
            if club == "track":
                show chelsea happy
                "You step up to the plate, feeling pumped up and ready!"
            elif club == "cheer":
                "You step up to the plate and get into position, making sure your pose is perfect."
            elif club == "yearbook":
                show chelsea embarrassed
                "You hesitantly step up to the plate, glancing around at your teammates nervously. You feel bad for them getting stuck with you on their team."
            show chelsea blank
            "The pitcher winds up, then rolls the ball across the gymnasium floor."
            if club == "track":
                "You wind your leg back and swing in full force!"
                if gymchoice == 1:
                    "As the ball makes impact with your foot, it flies outward, smacking against the ceiling. You race across the bases, landing on second base!"
                elif gymchoice == 2:
                    "As the ball makes impact with your foot, it flies outward, right into the hands of the pitcher."
                    "Classmate" "You're out!"
                    "You let out a groan, retreating to the back of the line of your teammates."
            elif club == "cheer":
                "You've positioned your leg perfectly. As it approaches, you let out a wide kick!"
                if gymchoice == 1:
                    show chelsea happy
                    "As the ball makes impact with your foot, it flies outward into the crowd of students."
                    "Several classmates throw themselves toward the ball as you manage to steal first base!"
                elif gymchoice == 2:
                    "As the ball makes impact with your foot, it flies outward into the crowd of students."
                    "Before you can run, the second base player catches it in their hands, raising it above their head."
                    "Classmate" "You're out!"
                    "You let out an exaggerated sigh, retreating to the back of your team's line."
            elif club == "yearbook":
                "As the ball approaches, you nervously jut out your leg."
                if gymchoice == 1:
                    show chelsea happy
                    "The ball bounces off to the side."
                    "Coach Phillips" "Ball! That's a walk."
                    "You hurry to the first base, shocked that you haven't managed to hurt yourself yet."
                elif gymchoice == 2:
                    "As the ball makes an impact with your foot, it knocks right back up into your face."
                    "You gasp, falling backward."
                    "A couple of other classmates gasp and giggle as Coach Phillips rushes up to you."
                    "He holds up a couple of fingers in front of your face."
                    "Coach Phillips" "[pcname], you okay? How many fingers am I holding up?"
                    pcname "A-Ah... Three..."
                    "Coach Phillips" "That's right. Hm. Why don't you go sit down on the bleachers, [pcname]? Mia, go grab her some ice from the nurse's office."
                    "A girl on your team nods, rushing out."
                    "Coach Phillips helps you to the bleachers. When Mia returns, you press the ice against your aching forehead where a bump is forming."
                    "The rest of the game carries on without consequence. It does nothing for your embarrassment."
                    jump events_end_period
            show chelsea blank
            "The game continues for a few more rounds. Your team manages to score 7 points!"
            "Coach Phillip" "Alright! Time to switch!"
            "You all switch positions on the field. You're given first base."
            if club == "track":
                "You bounce on the balls of your feet over the plate, eager for the first ball to come your way."
            elif club == "cheer":
                "You don't expect to be doing much from here, unfortunately. You inspect your nails, waiting for the game to continue."
            elif club == "yearbook":
                "You shift nervously on the plate, hoping that a ball will not come in your direction."
            "You manage to avoid any balls flying your way until the end of the game. Your points are tied, and this last kicker will decide if your team wins or not!"
            "The final opposing teammate steps up to the plate. As he kicks the ball, it flies in your direction!"
            if club == "track":
                "You jump toward it, ready to catch it."
                "The ball falls into your hands, but the teammate has already begun to race toward the second base!"
            elif club == "cheer":
                "You manage to look away from your nails long enough to catch it"
                "Unfortunately, the teammate has already begun to race toward the second base by the time it falls in your hands."
            elif club == "yearbook":
                show chelsea shocked
                "You shriek, placing your hands in front of yourself to avoid its impact."
                "Miraculously, the ball falls into your grasp. You're so shocked that you don't even realize that the teammate has begun to head to second base!"
            "Your teammate yells at you from the pitcher's stand."
            show chelsea blank
            "Teammate" "Throw it!"
            menu kickballthrow:
                "Throw it at the opposing teammate." if True:
                    if club == "track":
                        "You wind your arm back and throw it with full force toward the opposing teammate!"
                        if gymchoice == 1:
                            show chelsea happy
                            "The ball slams against the opposing teammate's back, sending him falling face first against the ground."
                            "Opposing Teammate" "Ah, shit!"
                            "He stands up, placing a hand on his back as he walks back to the back of his team's line. Your team gives out a small cheer!"
                            "The rest of the game goes just as well, and your team wins by a hair!"
                            "It's a good thing you managed to hit that player!"
                            jump events_end_period
                        elif gymchoice == 2:
                            "The ball flies toward the opposing teammate's back. He dives, landing on top of the plate before it can hit him."
                            show chelsea angry
                            "Coach Phillips" "He's safe!"
                            show chelsea blank
                            "The opposing team gives out a cheer while yours mumbles some choice words under their breaths."
                            "The rest of the game goes just as miserably, and your team loses by a point."
                            "If only you'd managed to hit that player."
                            jump events_end_period
                    elif club == "cheer":
                        "You toss the ball toward the opposing teammate!"
                        if gymchoice == 1:
                            show chelsea happy
                            "The ball smacks against the opposing teammate's back. He stumbles, caught off guard."
                            "He lets out a groan, returning to the back of his team's line."
                            "Your team gives out a small cheer!"
                            "The rest of the game goes just as well, and your team wins by a hair!"
                            "It's a good thing you managed to hit that player!"
                            jump events_end_period
                        elif gymchoice == 2:
                            "The ball flies toward the opposing teammate's back, but just barely misses as he dives down onto the plate."
                            "Coach Phillips" "He's safe!"
                            "You roll your eyes as the opposing team gives out a cheer."
                            "The rest of the game goes just as miserably, and your team loses by a point."
                            "If only you'd managed to hit that player."
                            jump events_end_period
                    elif club == "yearbook":
                        pcname "Y-Yes!"
                        "You throw the ball as hard as you can toward the opposing teammate!"
                        if gymchoice == 1:
                            show chelsea happy
                            "Although it's shaky, the ball still manages to hit the opposing teammate on the back of his leg."
                            "He stumbles, surprised, but sighs, returning to the back of his team's line."
                            "Your pitcher gives you a thumbs up before winding up for the next player."
                            "The rest of the game goes just as well, and your team wins by a hair!"
                            "It's a good thing you managed to hit that player!"
                            jump events_end_period
                        elif gymchoice == 2:
                            show chelsea sad
                            "Your throw is too shaky. It bounces off of the ground, feet away from where the opposing teammate is. He stops at second base, pleased with his steal."
                            "The pitcher rolls his eyes at you before winding up for the next player."
                            "The rest of the game goes just as miserably, and your team loses by a point."
                            show chelsea blank
                            "The pitcher is not happy with you, and it isn't until you've hidden yourself in the locker room that you manage to avoid his glare."
                            "If only you'd managed to hit that player."
                            jump events_end_period
                "Throw it to the second baseman." if True:
                    if club == "track":
                        "You wind your arm back and throw it with full force toward the second baseman!"
                        if gymchoice == 1:
                            show chelsea happy
                            "The second baseman catches it easily, tapping it against the opposing teammate's shoulder."
                            "Opposing Teammate" "Ah, shit!"
                            "He grumbles something under his breath as he walks back to the back of his team's line. Your team gives out a small cheer!"
                            "The rest of the game continues, and your team manages to win by a hair!"
                            "It's a good thing he caught that ball!"
                            jump events_end_period
                        elif gymchoice == 2:
                            "The ball flies toward the second baseman. As he tries to catch it, the opposing teammate dives forward, landing on the base first."
                            show chelsea sad
                            "Coach Phillips" "He's safe!"
                            "The opposing team gives out a cheer while yours mumbles some choice words under their breaths."
                            show chelsea blank
                            "You try to focus for the rest of the game, but nothing else comes your way. When the game ends, you've just barely lost."
                            "You walk off to the lockers, irritated. If only he'd caught that ball!"
                            jump events_end_period
                    elif club == "cheer":
                        "You toss the ball toward the second baseman!"
                        if gymchoice == 1:
                            show chelsea happy
                            "The second baseman stumbles a bit, caught off guard, but catches it and taps it against the opposing teammate's shoulder."
                            "The opposing teammate lets out a groan, returning to the back of his team's line."
                            show chelsea laugh
                            "Your team gives out a small cheer!"
                            "The rest of the game continues, and your team manages to win by a hair!"
                            "It's a good thing he caught that ball!"
                            jump events_end_period
                        elif gymchoice == 2:
                            "The ball flies toward the second baseman, who is caught entirely off guard. He stumbles to catch it, falling over. The opposing teammate steals second base with ease."
                            "Coach Phillips" "He's safe!"
                            "You roll your eyes as the opposing team gives out a cheer."
                            "You try to focus for the rest of the game, but nothing else comes your way. When the game ends, you've just barely lost."
                            "You walk off to the lockers, annoyed. If only he'd caught that ball!"
                            jump events_end_period
                    elif club == "yearbook":
                        pcname "Y-Yes!"
                        "You throw the ball as hard as you can toward second base!"
                        if gymchoice == 1:
                            show chelsea happy
                            "Although it's shaky, the second baseman manages to catch your ball in time to tap it against the opposing teammate's shoulder."
                            "He stumbles, surprised, but sighs, returning to the back of his team's line."
                            "Your pitcher gives you a thumbs up before winding up for the next player."
                            "The rest of the game continues, and your team manages to win by a hair!"
                            "It's a good thing he caught that ball!"
                            jump events_end_period
                        elif gymchoice == 2:
                            show chelsea sad
                            "Your throw is too shaky. It bounces off of the ground, feet away from where the second baseman is. The opposing teammate stops at second base, pleased with his steal."
                            "The pitcher rolls his eyes at you before winding up for the next player."
                            show chelsea blank
                            "You try to focus for the rest of the game, but nothing else comes your way. When the game ends, you've just barely lost."
                            "You walk off to the lockers, ashamed. If only he'd caught that ball!"
                            jump events_end_period
        "Fake sick." if True:
            show chelsea sad
            "You let out a heavy cough into your arm, feigning weak."
            "Coach Phillips" "You alright, [pcname]?"
            pcname "I'm not feeling so well, coach..."
            "You force some more coughs into your arm."
            pcname "Can I go see the nurse?"
            "Coach Phillips hesitates, but nods."
            show chelsea blank
            "Coach Phillips" "Alright. Feel better, [pcname]."
            "A couple of students that can tell you're faking give you dirty looks as you escape into the hallway."
            "You spend the rest of class taking a nap in the nurse's office."
            $ intelligence -=5
            jump events_end_period

label schoolmacbeth:
    show chelsea at right with moveinright
    "As English class begins, you all drag your desks in a circle around the room."
    "Mrs. Earl sits in front of the chalkboard, passing out thin books around the room: Macbeth."
    "Mrs. Earl" "Today we will be starting on a new section. Has anyone read Macbeth before?"
    "A couple of students raise their hands."
    "Mrs. Earl" "Excellent! Instead of reading chapters, I'll be picking volunteers to read the parts as we go along."
    "Mrs. Earl takes out a sheet of paper and a pen from her desk, scribbling down names from the play."
    "Mrs. Earl" "Alright, who would like to volunteer to read?"
    menu macbethread:
        "Raise your hand." if True:
            if club == "track":
                show chelsea happy
                "You thrust your hand into the air excitedly. Being able to show off like this pumps you up!"
            elif club == "cheer":
                show chelsea happy
                "You raise your hand into the air, a smile on your lips. This could be fun."
            elif club == "yearbook":
                show chelsea embarrassed
                "You shyly raise your hand into the air, looking away from the other students."
            "Mrs. Earl" "Perfect! Let's go down the list..."
            "Mrs. Earl recites her assigned roles. When she gets to you, she gives a mischievous grin."
            show chelsea blank
            "Mrs. Earl" "And [pcname], you will be Lady Macbeth."
            "Mrs. Earl" "Alright, class! Scene one, act one. Go."
            "Everyone is a little awkward getting into their roles, yourself included."
            "As you work through the first act, you feel a little more comfortable with Shakespearian dialogue."
            $ intelligence +=3
            $ Macbethread = True
            jump events_end_period
        "Keep your hand down." if True:
            "You keep your hands on top of the desk, watching the other students get assigned roles."
            "When all the roles are given, Mrs. Earl starts the reading."
            "Mrs. Earl." "Alright, class! Scene one, act one. Go."
            "You watch your fellow students awkwardly stumble through the Shakespearian language, working their way through the first act."
            "While it looks fun, you're relieved you didn't have to go through that!"
            $ intelligence -=1
            jump events_end_period

label schoolmacbeth2:
    show chelsea at right with moveinright
    "As English class begins, you all drag your desks in a circle around the room."
    "Mrs. Earl sits in front of the chalkboard, passing out thin books around the room: Macbeth."
    "Mrs. Earl" "Alright, class. We'll be picking up on Act II today."
    "Mrs. Earl" "Who would like to volunteer to read?"
    menu macbethread2:
        "Raise your hand." if True:
            if club == "track":
                show chelsea happy
                "You thrust your hand into the air excitedly. Being able to show off like this pumps you up!"
            elif club == "cheer":
                show chelsea happy
                "You raise your hand into the air, a smile on your lips. This could be fun."
            elif club == "yearbook":
                show chelsea embarrassed
                "You shyly raise your hand into the air, looking away from the other students."
            "Mrs. Earl" "Perfect! Let's go down the list..."
            "Mrs. Earl recites her assigned roles."
            if Macbethread == True:
                "When she gets to you, she gives a little wink."
                "Mrs. Earl" "And of course we have our Lady Macbeth."
                "You grin. You must have done a good job last time for her to give you the same role!"
            elif True:
                "When she gets to you, she gives a mischievous grin."
                "Mrs. Earl" "And [pcname], you will be Lady Macbeth."
            "Mrs. Earl" "Alright, class! Scene two, act one. Go."
            show chelsea happy
            "Everyone feels a little more at ease this time around as they get into their roles, yourself included."
            "Some of your classmates even move their hands around to get in character!"
            if Macbethread == True:
                "As you work through the second act, you start to feel more comfortable with your lines, as well as acting in front of your fellow students."
            elif True:
                "As you work through the second act, you feel a little more comfortable with Shakespearian dialogue."
            $ intelligence +=3
            jump events_end_period
        "Keep your hand down." if True:
            "You keep your hands on top of the desk, watching the other students get assigned roles."
            "When all the roles are given, Mrs. Earl starts the reading."
            "Mrs. Earl." "Alright, class! Scene two, act one. Go."
            "You watch your fellow students work through the Shakespearian language. Some of them even act!"
            "While it looks fun, you're relieved you didn't have to go through that!"
            $ intelligence -=2
            jump events_end_period

label schoolmacbeth3:
    show chelsea at right with moveinright
    "As English class begins, you all drag your desks in a circle around the room."
    "Mrs. Earl sits in front of the chalkboard, passing out thin books around the room: Macbeth."
    "Mrs. Earl" "Alright, class. We'll be picking up on Act II today."
    "Mrs. Earl" "Who would like to volunteer to read?"
    menu macbethread3:
        "Raise your hand." if True:
            if club == "track":
                show chelsea happy
                "You thrust your hand into the air excitedly. Being able to show off like this pumps you up!"
            elif club == "cheer":
                show chelsea happy
                "You raise your hand into the air, a smile on your lips. This could be fun."
            elif club == "yearbook":
                show chelsea embarrassed
                "You shyly raise your hand into the air, looking away from the other students."
            "Mrs. Earl" "Perfect! Let's go down the list..."
            show chelsea blank
            "Mrs. Earl recites her assigned roles."
            if Macbethread == True:
                "When she gets to you, she gives a little wink."
                "Mrs. Earl" "And of course we have our Lady Macbeth."
                "You grin. You must have done a good job last time for her to give you the same role!"
            elif True:
                "When she gets to you, she gives a mischievous grin."
                "Mrs. Earl" "And [pcname], you will be Lady Macbeth."
            "Mrs. Earl" "Alright, class! Scene two, act one. Go."
            show chelsea happy
            "Everyone is really getting into their roles today! Some students even stand up to act out the scene, cast in the same roles as before."
            if Macbethread == True:
                "You stand up with them, inspired in your role."
                pcname "'Naught's had, all's spent. Where our desire is got without content. 'Tis safer to be that which we destroy than by destruction dwell in doubtful joy.'"
                "The class watches in anticipation as you and your classmates continue to act out the scene."
                "When it's over, they applaud."
                "You feel a real sense of what Shakespeare was going for!"
            elif True:
                "As you work through the second act, you feel a little more comfortable with Shakespearian dialogue."
            $ intelligence +=3
            jump events_end_period
        "Keep your hand down." if True:
            "You keep your hands on top of the desk, watching the other students get assigned roles."
            "When all the roles are given, Mrs. Earl starts the reading."
            "Mrs. Earl." "Alright, class! Scene three, act one. Go."
            "Your class really gets into the scene, even jumping up to act some of it out!"
            "You're really impressed with their work, and a part of you considers joining them next time."
            $ intelligence -=3
            jump events_end_period

label schoolhistoryfieldtrip:
    show chelsea at right with moveinright
    "When you head into history class, the other students all chat excitedly by the door."
    "Ms. Maureen stands by the board, taking roll call as you all secure your lunches."
    "Ms. Maureen" "Alright, class! It's time for our field trip! Start heading out!"
    "That's right! Today is field trip day!"
    "You join the others in line to the bus outside. How exciting!"
    hide chelsea with dissolve
    show bg black with fade
    pause 0.5
    show bg CityD with dissolve
    show chelsea shocked
    show chelsea at right with dissolve
    pcname "Wow...!"
    show chelsea happy
    "The history museum is {i}amazing!{/i}"
    "You admire the old artifacts with glee as your class steps inside."
    "As Ms. Maureen begins her lecture, you notice a couple of girls with their phones out near the back."
    "They pose with some of the artifacts, shooting funny videos on their phones."
    show chelsea blank
    menu goofoff:
        "Listen to the lecture." if True:
            "You ignore them. They'll get in their own trouble later."
            "You follow Ms. Maureen as she gives her lecture."
            "History is so much fun to learn!"
            $ intelligence +=3
            jump events_end_period
        "Goof off." if True:
            "You're pretty sure you've heard this lecture a million times by now."
            show chelsea happy
            "You join the girls posing with artifacts and take turns swapping your phones to take ridiculous videos."
            "The trip was pretty fun, but you didn't learn much."
            $ intelligence -=3
            jump events_end_period

label schoolhistorydocumentary:
    show chelsea at right with moveinright
    "As you take your seat in history class, Ms. Maureen sets up the projector."
    "Ms. Maureen" "For class today, we're going to watch a documentary. Make sure to take notes!"
    "She dims the lights. The film begins."
    "Even after a few minutes, you feel your eyes begin to droop. You're so, so tired..."
    menu documentarynap:
        "Nap." if True:
            "You suppose it can't hurt to sleep a little bit. You won't be missing... much... zzz..."
            hide chelsea with dissolve
            show bg black with fade
            pause 0.5
            show bg ClassroomD with dissolve
            show chelsea at right with dissolve
            "The lights flash back on in the room, blinding you."
            "Ms. Maureen" "Alright, class! Pop quiz!"
            show chelsea shocked
            "Students at the front pass back pieces of paper. You stare at the questions, panic seeping in."
            if club == "track":
                pcname "Fuck..."
            elif club == "cheer":
                pcname "Damn it..."
            elif club == "yearbook":
                pcname "O-Oh no..."
            show chelsea blank
            "Ms. Maureen" "You have until the end of class to finish. Turn them in at the desk when you're done."
            "Ms. Maureen sits down at her desk and begins to grade old homework."
            "You stare at the quiz and try your best."
            "You turn it in on the desk at the end of the period. You don't think you've done very well this time..."
            $ intelligence -=5
            jump events_end_period
        "Force yourself awake." if True:
            "Although your eyes beg for sleep, you force them open, focusing on the documentary."
            "It feels like forever, but it finally ends, and you let out a sigh of relief."
            "Ms. Maureen flicks the lights on, flooding the room."
            "Ms. Maureen" "Alright, class! Pop quiz!"
            "Students at the front pass back pieces of paper."
            show chelsea happy
            "You look over the questions, a sense of relief overcoming you."
            "You answer them easily and manage to finish the quiz before the end of class!"
            "After turning in the quiz, you sit back in your seat. Thank goodness you stayed awake!"
            $ intelligence +=3
            jump events_end_period


label schoolbullieshomework:
    $ homeworkgirls=False
    show chelsea at right with moveinright
    "You step into your science class and take your usual seat. The teacher hasn't arrived yet, but you're sure he'll be there shortly."
    "Three pretty girls in your class make their way to your desk, surrounding it on all sides."
    show GSGirl with dissolve
    "The middle one, a pretty blonde girl, leans forward on your desk. You vaguely recognize her as Kenzie."
    "Kenzie" "Hey, [pcname]. You completed today's homework, right?"
    show chelsea confused
    if club == "track":
        pcname "Well, yeah."
    elif club == "cheer":
        pcname "Yeah, what's up?"
    elif club == "yearbook":
        pcname "A-Ah, yeah..."
    show chelsea blank
    "Kenzie" "Do you think we can copy off of you?"
    "One of the girls at her side, Silone, a brunette with a high ponytail, leans in."
    "Silone" "Yeah, we totally forgot about it! Pretty please?"
    menu copyhomework:
        "Sure." if True:
            show chelsea happy
            if club == "track":
                pcname "Sure, I guess."
            elif club == "cheer":
                pcname "Sure, whatever."
            elif club == "yearbook":
                pcname "Ah, um, y-yes..."
            "You pull out today's assignment from your folder and pass it over to them. The girls sigh in relief."
            "Silone" "Thanks, [pcname]! You're a lifesaver."
            "Kenzie" "Yeah. We owe you one."
            show chelsea blank
            "Kenzie winks. The girls all pull out their homework, quickly copying your answers down."
            "You know it isn't the right thing to do, but it can't be that bad if it's just this once."
            $ copyhomework = True
            $ corruption +=1
            jump events_end_period
        "No." if True:
            if club == "track":
                show chelsea confused
                pcname "Uh, no. You should've done it yourself."
                show chelsea blank
            elif club == "cheer":
                show chelsea confused
                pcname "Sorry, no. Make sure to do it next time."
                show chelsea blank
            elif club == "yearbook":
                show chelsea sad
                pcname "S-Sorry, but... no..."
            "All friendly demeanor is gone. The girls glare at you, defensive."
            "Silone" "Are you serious? We asked nicely."
            show chelsea blank
            "You shake your head. They share a look. Kenzie's lackeys turn away first, returning to their seats."
            "Kenzie" "Big mistake, sweetie."
            "Kenzie follows suit. She makes sure to send plenty of glares your way throughout class!"
            jump events_end_period

label schoolbullieshomework2:
    $ homeworkgirls=False
    show chelsea at right with moveinright
    "As you sit down for science class, Kenzie and her friends approach you again."
    show GSGirl with dissolve
    "Kenzie" "Hey, [pcname]."
    "Kenzie leans on your desk, a smile on her pretty red lips."
    "Kenzie" "Can we copy off of you again? I got so busy last night, I didn't have time at all..."
    menu copyhomework2:
        "Sure." if True:
            show chelsea happy
            "You pull out your homework from your bag and pass it over to Kenzie."
            "She grabs it greedily, giving you a big smile."
            "Kenzie" "Thanks, [pcname]! You're so sweet."
            "The girls pass it between themselves, copying down the answers."
            show chelsea blank
            "Kenzie returns it to you afterward and they resume their seats in the classroom."
            "You probably shouldn't make a habit of letting them copy your homework, but if they were really that busy, it would be a shame to let their grades suffer."
            $ corruption +=1
            jump events_end_period
        "No." if True:
            if club == "track":
                show chelsea angry
                pcname "No. I let you copy last time."
                show chelsea blank
            elif club == "cheer":
                pcname "Sorry, no. I already let you copy once."
            elif club == "yearbook":
                show chelsea sad
                pcname "S-Sorry, but... no..."
            "All friendly demeanor is gone. The girls glare at you, defensive."
            "Silone" "Are you serious? You let us copy last time."
            "Kenzie" "I even asked nicely."
            show chelsea blank
            "You shake your head. They share a look. Kenzie's lackeys turn away first, returning to their seats."
            "Kenzie" "Big mistake, sweetie."
            "Kenzie follows suit. She makes sure to send plenty of glares your way throughout class!"
            $ copyhomework = False
            jump events_end_period

label schoolbullieshomework2_steal:
    show chelsea at right with moveinright
    $ homeworkgirls=False
    "As you sit down for science class and rummage through your bag, you realize you can't find your homework!"
    show GSGirl with dissolve
    "Kenzie" "Looking for something?"
    "Kenzie and her friends stand in front of your desk, dangling your homework in front of you."
    "You reach out to grab it, but Kenzie lifts it out of your reach."
    "Kenzie" "I don't think so."
    "Kenzie" "If you want it back, you need to give us something in return."
    "She holds her hand out, demanding."
    "Kenzie" "What've you got?"
    menu homeworkbarter:
        "Ask for it back." if True:
            if club == "track":
                "You stand up from your seat, holding your hand out."
                pcname "Give it back, Kenzie!"
            elif club == "cheer":
                "You stand up from your seat, flipping your hair over your shoulder."
                pcname "I don't have time for this, Kenzie. Just give me my homework."
            elif club == "yearbook":
                show chelsea sad
                "You lean forward in your seat, reaching for your homework."
                pcname "P-Please give that back!"
            "Kenzie and her troupe laugh, pulling away."
            "Kenzie" "As if. Next time learn to help out your friends."
            "The girls continue to laugh as the bell rings, taking their seats."
            "Your teacher is less than pleased to see you have nothing to turn in and gives you an F!"
            $ intelligence -=6
            jump events_end_period
        "Offer to help on next project." if True:
            if club == "track":
                show chelsea angry
                "You hate being forced to give in to these girls, but you need that assignment back."
                show chelsea blank
            elif club == "cheer":
                show chelsea angry
                "You scowl up at them, clicking your tongue in annoyance."
                show chelsea blank
            elif club == "yearbook":
                show chelsea sad
                "You shift uncomfortably in your seat. You don't have much to offer, but..."
            pcname "I can help you on our next assignment."
            "Kenzie considers this. With the flick of her hand, she drops the paper onto your desk."
            show chelsea blank
            "Kenzie" "Alright. You better keep to your word."
            "She gives you a malicious smile, returning to her seat. Silone and the dark-haired girl beside her, Mia, laugh at you."
            "Mia" "We've already copied it for today anyways."
            "Silone" "Next time just make things easy and let us copy right away."
            "The girls return to their seats. You're upset at how easily they used you, but at least you have your homework back."
            $ corruption +=1
            $ intelligence +=5
            jump events_end_period

label schoolpeprally:
    show bg Gym with dissolve
    "You walk through the halls toward the gymnasium, following the large crowd of students."
    "When you enter the gym, bright streamers in school colors and the marching band greet you!"
    "It's a pep rally!"
    if club == "track":
        show chelsea at right with moveinright
        "You join your other track teammates to the side, waiting for the rest of the crowd to fill in."
    elif club == "cheer":
        show chelsea blank
        $ clothes = 'cheer'
        show chelsea at right with moveinright
        "You join the rest of your cheer squad to the side, waiting for the rest of the crowd to fill in."
    elif club == "yearbook":
        show chelsea at right with moveinright
        "You follow the other students up the bleachers, taking a seat near the back as the rest of your classmates fill in."
    "The band plays triumphantly in the middle of the gym, starting the pep rally off."
    if club == "track":
        show chelsea happy
        "You run out onto the gymnasium floor with your teammates, waving and whooping in encouragement."
        "They love it! You're starting to feel really pumped!"
    elif club == "cheer":
        show chelsea happy
        "As the sports teams run out onto the floor, you join your squad in the middle of the gym."
        "The band starts up a new song, and you jump into action, ready to perform!"
    elif club == "yearbook":
        show chelsea happy
        "You watch the sports teams run out to the sides of the gym, yelling and hollering encouragement up at the audience."
        "The crowd yells back in return, getting pumped up."
        "The band starts to play, and the cheer squad gets into formation in the center of the gym. They perform some exciting school cheers. You hear the audience cheer along!"
    "After the pep rally ends, everyone seems to be in much better moods heading back to class!"
    jump events_end_period

label schoolfiredrill:
    show chelsea at right with moveinright
    "You're sitting in your math class when a fire alarm goes off."
    "Your teacher sighs and heads to the door, counting your heads as you march in a neat line to the nearest fire exit."
    show bg School with fade
    "Several other students crowd outside, everyone marching along with their current classmates. The teachers give a head count, making sure everyone is there."
    "Principal Tanner strolls out, waving to gather everyone's attention."
    show P Blank at left with moveinleft
    "Principal" "The fire drill is over now! Thank you for your safe practice. You may resume classes now!"
    "The teachers round their classes up and begin to head inside. As you follow your fellow classmates, you glance across the near empty parking lot."
    hide P with moveoutleft
    menu firedrillditch:
        "Ditch school." if True:
            "No one will really notice you missing, anyway."
            "When your teacher isn't looking, you step to the side as the fire exit doors close."
            "Shoving your hands in your pockets, you walk across the parking lot and straight out of the school."
            "That was easier than you thought!"
            $ intelligence -=6
            $ corruption +=1
            jump events_end_period
        "Return to class." if True:
            "Someone will definitely notice if you walk off in the middle of the day."
            show bg ClassroomD with fade
            "You follow behind your fellow classmates back to your classroom."
            $ intelligence +=3
            jump events_end_period

label schoollunchcupcake:
    show bg Cafeteria with dissolve
    show chelsea at right with moveinright
    "You push your tray across the lunch line, debating what kind of dessert you want to accompany your meal today."
    "As you approach the desserts, a chocolate cupcake with bright blue icing stands out to you. It's the last one, too!"
    "It looks delicious!"
    show GSBoy at left with moveinleft
    "You reach forward but notice the boy in line behind you also reach for it at the same time."
    "You both retract your arms for a moment, awkward."
    menu cupcake:
        "Take the cupcake." if True:
            $ corruption +=1
            show chelsea confused
            "Well, if he isn't going to take it..."
            show chelsea blank
            "You pluck the cupcake from line and set it on your tray."
            hide GSBoy with moveoutleft
            "As you sit down to eat, you take a big bite out of it."
            "You were right: it {i}is{/i} delicious!"
            jump events_end_period
        "Offer him the cupcake." if True:
            "You can always find something else to eat."
            show chelsea happy
            "You gesture toward the cupcake, allowing him to place it on his tray. He gives you a thankful grin and walks off."
            hide GSBoy with moveoutleft
            "Well, at least someone got to enjoy it."
            $ corruption -=1
            jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
