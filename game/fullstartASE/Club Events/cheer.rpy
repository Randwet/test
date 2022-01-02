label cheer_first_meeting:
    $ cheerfirst1 = False
    "It seems a little strange walking into the school on a [dayname], but you shake the feeling off quickly."
    "Opening the locker room door, you're struck by a cacophony of voices."
    "Girls line the benches, giggling with each other as they wait for practice to start."
    "A tall girl approaches you, smiling. Her long, blonde hair is pulled up in a high ponytail - but what really catches your attention is her eyes: one green, one blue."
    show chelsea at right with moveinright
    show Tracy Blank at left with moveinleft
    "Tracy" "I'm Tracy, the Cheer Captain. You're one of the new girls, right?"
    "She barely gives you a moment to nod before she continues."
    show Tracy Smile at left
    "Tracy" "Take a seat at an empty locker and we'll get started soon. Today, we're mostly just going over the rules and handing out uniforms."
    show Tracy Blank at left
    "Tracy" "Let me know if you have any questions, okay?"
    show chelsea happy
    pcname "Thanks!"
    show chelsea blank
    hide Tracy Blank with moveoutleft
    "Glancing around the room, you see a few open spots."
    "Since you don't know anyone yet, you figure it doesn't really matter; you take the one closest to you."
    "Slipping your things inside, you close the door and take another look around."
    "The girl next to you - a lovely brunette - gives a shy smile."
    show Olivia Happy at left with moveinleft
    "Olivia" "Hi, I'm Olivia."
    show chelsea happy
    "You smile back."
    pcname "I'm [pcname]. I just moved here."
    show chelsea blank
    show Olivia Laughing at left
    "Olivia" "Really? Me too!"
    "You open your mouth to say more, but a sudden rhythmic clapping draws your attention to the front of the room."
    hide Olivia Laughing with moveoutleft
    show MV Laugh at left with moveinleft
    "Ms. Vicky" "See how quickly you can draw attention with a little noise and rhythm?"
    show MV Smile at left
    "Ms. Vicky" "Chants, cheers, motions, and facials--"
    "Her speech is interrupted by a few, barely-smothered giggles."
    "Ms. Vicky" "--are all really important parts of what we cheerleaders do!"
    "Ms. Vicky" "Do you think anyone would be excited if you did your cheers like this?"
    show MV Tired at left
    "She demonstrates a quick cheer, frowning and barely extending her arms."
    "Squad" "No, Ms. Vicky!"
    show MV Smile at left
    "Ms. Vicky" "Exactly! But do it like this--"
    show MV Laugh at left
    "This time she performs the same routine, but with a big smile and confident motions."
    show MV Laugh at left
    "Ms. Vicky" "--and you'll see a big difference!"
    show MV Smile at left
    "Ms. Vicky" "Alright, so let's get started!"
    "As she speaks, she claps occasionally to emphasize her points."
    show MV Blank at left
    "Ms. Vicky" "As part of the team, you're expected to come to all practices."
    "Ms. Vicky" "Since the school district has made clubs mandatory, we're not allowed to kick you out if you miss practice."
    "Ms. Vicky" "However, you {i}will{/i} sit on the bench during sporting events and competitions if you don't do your share of the work!"
    "Ms. Vicky" "You must also wear appropriate clothing for practice."
    "Ms. Vicky" "This means athletic shoes and socks - no flip flops or sandals!"
    "Ms. Vicky" "Your hair must be up and out of your face, too."
    "Ms. Vicky" "And you must bring a {i}positive attitude{/i}!"
    "Ms. Vicky" "Any questions?"
    "Squad" "No, Ms. Vicky!"
    show MV Smile at left
    "She grins as she looks around the room."
    show MV Laugh at left
    "Ms. Vicky" "Then let's pass out uniforms and get started!"
    show MV Smile at left
    "Everyone quickly forms a line from one side of the room to the other. When each girl reaches the front, Ms. Vicky looks her over and gives out a uniform."
    "As you near the front, you hear her chatting with each girl."
    "Ms. Vicky" "Rebecca! Looks like you've filled out a little more - only where it counts! Promise!"
    "Ms. Vicky" "Ashley, your highlights look {i}great!{/i}"
    "Stepping up for your own uniform, you feel a little uncomfortable as she looks you over."
    "Ms. Vicky" "I remember you! [pcname], right?"
    show chelsea happy
    pcname "That's me!"
    show chelsea blank
    "Ms. Vicky" "Cute smile and a nice figure! I'm sure I have your size..."
    "She picks up a skirt from one pile and holds up a shirt from another."
    "Discarding that top, she chooses a different one and lays it across her arm."
    "Adding a pair of bloomers to the pile, she hands it all over."
    "Ms. Vicky" "There we go! All set!"
    show chelsea confused
    pcname "But I didn't even tell you my size..."
    "Ms. Vicky winks at you and grins."
    "Ms. Vicky" "After all the girls I've outfitted, I probably know your size better than you do!"
    show chelsea blank
    show MV Blank at left
    "Ms. Vicky" "Go get changed and we'll run through some of the basics."
    hide chelsea with moveoutright
    $ clothes = 'cheer'
    hide MV Blank with moveoutleft
    show chelsea at right with moveinright
    "You go back to your locker and put your new uniform on; just as she said, she knew your sizes perfectly!"
    "Tracy" "New girl! Do you need a hair tie?"
    show Tracy Smile at left with moveinleft
    "You turn to see Tracy, her mismatched eyes watching you."
    pcname "Oh! I forgot about that..."
    show Tracy Blank at left
    "Tracy" "Here you go!"
    "She tosses a hair tie at you."
    "Tracy" "Keep it with your uniform and you'll never forget one."
    hide chelsea with dissolve
    $ hair = 'ponytail'
    show chelsea happy at right with dissolve
    pcname "Thanks!"
    show chelsea blank
    hide Tracy Blank with moveoutleft
    hide chelsea with dissolve
    show bg Gym with fade
    show chelsea at right with moveinright
    "As soon as everyone is ready, you head out into the gymnasium for practice."
    "Ms. Vicky instructs everyone on the differences between chants and cheers, then goes over the basic positions."
    show MV Smile at left with moveinleft
    "Ms. Vicky" "Okay, girls. Now I'll sort you into your stunt groups. Each group must have four members: a flyer, two bases, and a backspotter."
    "Ms. Vicky" "You'll be assigned a position and a group, then we'll practice some easy lifts."
    show chelsea confused
    "You wait, listening as she calls out names you don't recognize."
    show chelsea blank
    show MV Blank at left
    "Ms. Vicky" "[pcname], group 4, backspotter!"
    "You walk to where she points, joining the other two girls - Lindsay and Ashley."
    "Ms. Vicky" "Olivia, group 4, flyer!"
    show Olivia Happy with moveinleft
    "As Olivia joins you, you flash her a quick smile."
    show Olivia Blank
    "Olivia" "I don't know if I can be a flyer... That seems so scary!"
    "Lindsay" "It's okay. We'll make sure you don't fall!"
    "Ashley" "Just don't flail around; last year I got a black eye!"
    show Olivia Confused
    "Olivia" "I-I'll try not to..."
    "Ms. Vicky" "Alright, girls! Tracy's group will show you how to do a thigh stand!"
    "The rest of practice is spent going over different types of stands and lifts."
    "It's a lot more work than you expected, but you have a good time."
    jump events_end_period

label cheer_tracy_intro:
    "As you change into your uniform, someone taps your shoulder."
    show chelsea at right with moveinright
    show Tracy Smile at left with moveinleft
    "When you turn around, you see Tracy; you're struck again by her mismatched eyes and her long, golden hair."
    show Tracy Blank at left
    "Tracy" "Hey, [pcname], right?"
    show chelsea happy
    pcname "Yep, that's me!"
    show chelsea blank
    show Tracy Blank at left
    "Tracy" "I know I introduced myself last practice, but we didn't have much time to talk."
    "Tracy" "As captain, I like to get to know everyone a little bit."
    "Tracy" "So what made you decide to join the team?"
    menu cheer_tracy_join:
        "I just had to pick a club." if True:
            show Tracy Question at left
            "Tracy" "I was afraid of that. Every year we get a few girls who join because they think it'll be easy."
        "It looked like fun." if True:
            show chelsea happy
            show Tracy Laugh at left
            "Tracy" "It is! But it's not {i}just{/i} fun..."
        "I thought I'd look good in the uniform!" if True:
            $ corruption += 1
            show chelsea embarrassed
            show Tracy Laugh at left
            "She laughs."
            "Tracy" "Oh, you do! But it's about more than looking good."
    show chelsea blank
    show Tracy Angry at left
    "Tracy" "Cheerleading is {i}work.{/i} If you don't think you can handle that, this isn't the place for you."
    show chelsea happy
    pcname "I can handle it!"
    "She nods."
    show Tracy Smile at left
    "Tracy" "Good!"
    "She turns to walk away, but hesitates."
    show Tracy Blank at left
    "Tracy" "I have to ask... Is that your natural hair color?"
    pcname "Sure is!"
    show Tracy Laugh at left
    "Tracy" "I love it! Red hair always looks better when it's natural."
    pcname "Thanks!"
    show Tracy Smile at left
    "Tracy" "I'll see you around. Do your best today!"
    hide Tracy smile with moveoutleft
    "She walks over to another group of girls and starts chatting."
    show chelsea blank
    "It seems that everyone on the team knows and likes Tracy, so she'll probably be a good friend to have."
    jump events_end_period

label cheer_olivia_intro:
    "You get to practice a little early, so there aren't very many girls in the locker room while you change."
    show chelsea at right with moveinright
    "Olivia" "Um, could you help me?"
    show Olivia Blank at left with moveinleft
    "You turn to the girl next to you. She's managed to get the back of her top stuck in her bra straps."
    "Olivia" "I think I'm stuck..."
    show chelsea happy
    "Giggling, you reach over and pull her shirt free."
    "Olivia" "Thanks... My shirt is really tight until I get it down farther."
    show chelsea blank
    "She turns toward you and you immediately see the problem: even though she's a fairly petite girl, her breasts are {i}huge.{/i}"
    menu cheer_olivia_boobs:
        "I can see why!" if True:
            show chelsea shocked
            show Olivia Embarrassed at left
            "She blushes a little and turns away."
        "No problem." if True:
            show Olivia Happy at left
            "She smiles at you."
    show Olivia Happy at left
    "Olivia" "I usually wear loose tops so people can't really see, but..."
    show chelsea embarrassed
    pcname "Yeah, these shirts are pretty tight."
    "She nods."
    show chelsea blank
    show Olivia Blank at left
    "Olivia" "And the skirts are way shorter than anything I'd normally wear."
    show chelsea sad
    pcname "So why join the team if you don't like the uniform?"
    show Olivia Embarrassed at left
    "Olivia" "I..."
    show chelsea blank
    "She glances away from you and bites her lip."
    show Olivia Sad at left
    "Olivia" "All the girls here seem so sure of themselves... and their bodies."
    "Olivia" "I've never liked the attention and I'm not very confident."
    "Olivia" "I thought if I joined..."
    "Olivia" "Well, why did {i}you{/i} join?"
    menu cheer_olivia_join:
        "I like the uniform." if True:
            $ corruption += 1
            show chelsea happy
            show Olivia Confused at left
            "Olivia" "Really? I feel so exposed..."
        "I didn't like the other options." if True:
            show Olivia Happy at left
            "Olivia" "Right? When I found out I had to join a club, there were only three left."
            pcname "Me too!"
        "I always wanted to be a cheerleader!" if True:
            show chelsea happy
            show Olivia Blank at left
            "Olivia" "I think every girl does..."
    show Olivia Blank
    show MV Laugh with moveinleft
    show chelsea blank
    "Ms. Vicky" "Okay, girls, let's get outside and warm up!"
    "Putting your stuff away, you quickly follow the other girls out of the locker room."
    jump events_end_period


label cheer_generic:
    $ genericevent1 = renpy.random.randint(1, 3)
    $ genericevent2 = renpy.random.randint(1, 3)

    if genericevent1 == 1:
        "As you walk to cheer practice, the sky darkens."
        "And by the time you reach the school, you feel the first drops of rain."
        "So it comes as no surprise when Ms. Vicky decides to hold practice indoors."
    elif genericevent1 == 2:
        if catadopt:
            "Walking to the school, you find yourself daydreaming about getting another pet."
        elif True:
            "Walking to the school, you find yourself daydreaming about getting a pet."
        "A dog would be nice, but your apartment is so small..."
        if catadopt:
            "Maybe another cat? But the litter box would fill up pretty quickly and stink up the house..."
        elif True:
            "Maybe another cat? But then there's the litter box..."
        "Something unique would be fun. Like a ferret..."
        "You're so caught up in your own thoughts that you miss a turn."
        "You make it to practice on time, but it's a close call!"
    elif genericevent1 == 3:
        "One of the other girls stops and offers you a ride to the school."
        "Since you're there early, you have a chance to socialize a little more before practice starts!"

    if genericevent2 == 1:
        show bg Gym with fade
        "As practice begins, Ms. Vicky's phone rings."
        show MV Blank with moveinleft
        "Ms. Vicky" "Sorry, girls, but I have to take this call. Tracy, can you take over?"
        show Tracy Laugh at left with moveinleft
        "Tracy" "Of course, Ms. Vicky!"
        hide MV Blank with moveoutleft
        show Tracy Smile
        "Tracy moves to the front of the group and calls out the next cheer."
        "As the team moves in and out of formations, Tracy makes corrections and offers advice."
        "In some ways, she's probably a better coach than Ms. Vicky!"
    elif genericevent2 == 2:
        show bg Gym with fade
        show MV Smile with moveinleft
        "Ms. Vicky" "Today we're going to practice lifts and tosses! Is everyone ready?"
        "Cheer Squad" "Yeah!"
        show MV Laugh
        "Ms. Vicky" "Alright! Get in your groups and get in formation!"
        show MV Smile
        "You're the back-spotter for your group, so you get into position behind Olivia, the flyer."
        "Tracy counts off in sets of 4. On one, the two girls on either side of Olivia get into position with their hands crossed and joined."
        "Olivia grabs their shoulders and you hold onto Olivia's waist."
        "On two, you lift Olivia, putting her feet on their hands, and move your hands under her buttocks."
        "As Tracy calls out three, all three of you push Olivia up into the air."
        "She hangs in the air for a moment, giving the three of you time to brace before she falls back down on the count of four."
        "Ms. Vicky" "Great job, girls! Lindsay, make sure you keep your arms at your sides!"
        "Ms. Vicky" "Again!"
        "You spend most of practice doing the same 4-count barrel tosses."
        "It's fun, but a lot of work."
    elif genericevent2 == 3:
        show bg Gym with fade
        show MV Smile at left with moveinleft
        "Ms. Vicky" "Alright, girls! Today we're working on synch--"
        show MV Blank at left
        "Ms. Vicky" "Synch..."
        "She giggles."
        show MV Laugh at left
        "Ms. Vicky" "On doing everything at the same time!"
        "Ms. Vicky" "Let's get started with some chants, Tracy!"
        show MV Smile at left
        "Tracy leads you through some chants - short, repeated phrases - while Ms. Vicky gives feedback."
        "Ms. Vicky" "Okay! Great job, girls!"
        "Ms. Vicky" "Now some cheers, Tracy!"
        "You spend the rest of practice doing the longer cheers."
        "It's not the most interesting way to spend time, but by the end of the day you can see some improvement!"
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
