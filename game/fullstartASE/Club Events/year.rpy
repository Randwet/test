label year_generic:
    $ genericevent1 = renpy.random.randint(1, 3)
    $ genericevent2 = renpy.random.randint(1, 3)
    $ cloud = renpy.random.choice(['dog','cat','horse','whale','monkey','elephant','penis'])

    if genericevent1 == 1:
        "On your way to Yearbook, you see a cloud that looks like a [cloud]."
        "A huge [cloud]!"
        "You're so amused that you watch it the whole way to school."
    elif genericevent1 == 2:
        "As you walk to the school, you take your camera out and snap some pictures."
        "Some of them are actually pretty good!"
    elif genericevent1 == 3:
        "It's raining when you walk to the school."
        "A car speeding past hits a puddle, tossing water over the curb at you."
        "You manage to shield yourself with your umbrella, but your shoes still get soaked."
        "The rest of the walk, your soggy shoes make an awful squishing noise."

    if genericevent1 == 1:
        "When you arrive, you're practically pounced upon."
        "Levi" "Did you see them?"
        pcname "See who?"
        "He glances over your shoulder into the hallway, then pulls the door shut behind you."
        "Levi" "They're looking for me again."
        pcname "I didn't see anyone."
        "Levi" "Good."
        "He looks at you suspiciously."
        "Levi" "Of course, that's what they'd tell you to say..."
        "He slowly backs away from you, never turning around as he inches toward his chair."
        pcname "What a strange guy..."
    elif genericevent1 == 2:
        show chelsea at right with moveinright
        "When you enter the Art Room, you set out some of the photos you've taken."
        "As you're looking over them, you sense someone standing behind you."
        show MD Closed Smile with dissolve
        "Mr. Davis" "Nice work, [pcname]! These are lovely!"
        pcname "Th-Thanks, Mr. Davis..."
        "Draping an arm around your shoulders, he leans over you to take a closer look."
        show MD Laugh
        "Mr. Davis" "You really have a talent for photography!"
        "Your face warms at his praise."
        "Pulling you closer, he gives you a reassuring half-hug."
        show MD Open Smile
        "Mr. Davis" "We'll have to see if we can find some photography scholarships for you to apply for. Hmm..."
        "Lifting his arm from your shoulders, he walks away with a thoughtful expression."
    elif genericevent1 == 3:
        "Instead of going to the Art Room, you decide to take some pictures around the school."
        "You spend the afternoon taking candid shots of other students and looking for interesting angles."
    jump events_end_period


label year_first_meeting:
    "School is the last place you want to be on a [dayname], but you dutifully head off to your first Yearbook Club meeting."
    show chelsea at right with moveinright
    "Entering the Art Room, you see three other students have already arrived."
    "You look for someone to chat with, but none of them even look up from their work."
    menu yearbook_bored:
        "What would you like to do?"
        "Read a book." if True:
            "Taking a seat at an empty table, you pull a book from your bag and flip it open."
        "Sketch a picture." if True:

            $ activity = "sketching"
            "You find an empty seat and, sketchbook in hand, take out a pencil."
    "You've just started getting really engrossed in it when Mr. Davis comes in."
    show MD Laugh with dissolve
    "Mr. Davis" "Alright, it looks like we have quite a few new faces this year. Wonderful!"
    show MD Closed Smile
    "A glance around the room tells you there are about ten people overall."
    show MD Open Smile
    "Mr. Davis" "I'll be coming around to talk with each of you about your role in the club. Feel free to continue whatever you're doing until then."
    show MD Blank
    "Mr. Davis approaches a girl wearing a camera first. She's short, plain, and seems quite young."
    hide MD Blank with dissolve
    show chelsea confused
    "She nervously glances around the room when Mr. Davis leans over to chat with her."
    show chelsea shocked
    "Before you can listen in, a sudden argument across the room catches your attention."
    show Levi Shocked at left with dissolve
    "Levi" "If you knew what I was really capable of, you wouldn't say that!"
    show chelsea blank
    "The boy yelling is tall, with short black hair."
    "Daniel" "Yeah, yeah, we know: you're some kind of mutant or mage or something."
    show Levi Shocked
    "Levi" "We're called {i}Casters!{/i}"
    show MD Worried
    show chelsea shocked
    "Mr. Davis" "Levi, Daniel, quiet please! Others are trying to work."
    show chelsea blank
    show Levi Blank
    "The boys glare at each other, but the argument seems to be over before it truly began."
    show MD Closed Smile
    hide Levi Shocked with dissolve
    "Mr. Davis" "Sorry about that. I don't think I asked your name last time we met?"
    show chelsea embarrassed
    pcname "It's [pcname]."
    "He smiles and leans in close, speaking quietly."
    show MD Neutral
    "Mr. Davis" "Welcome to the Yearbook Club! Like I said, we have a lot of things going on here."
    show chelsea happy
    "Mr. Davis" "In the end, though, we {i}do{/i} have to make the yearbook, so we have to divide the work."
    show MD Closed Smile
    "Mr. Davis" "I was really hoping that you wouldn't mind being one of our photographers."
    show chelsea confused
    show MD Open Smile
    pcname "Photographer? I've used a camera, but I don't know if I'm good at it."
    show MD Laugh
    show chelsea blank
    "Mr. Davis" "Not a problem! We only have two this year, so we could really use another."
    show chelsea embarrassed
    show MD Open Smile
    pcname "I-I guess I can do that..."
    show MD Laugh
    show chelsea shocked
    "Mr. Davis" "Excellent! I've already met with Sophie and Andrew about the clubs they're covering."
    show chelsea blank
    "Mr. Davis" "Here's {i}your{/i} list."
    "He places a sheet of paper in front of you."
    "Mr. Davis" "You'll be responsible for going to each of these ten clubs during their meetings and taking pictures."
    show MD Closed Smile
    "Mr. Davis" "Does that sound all right to you?"
    pcname "I... guess I can do that."
    show MD Laugh
    "Mr. Davis" "Wonderful!"
    "He puts a hand on your shoulder and squeezes reassuringly."
    show MD Open Smile
    "Mr. Davis" "I think you'll be a wonderful addition to our club, [pcname]."
    "Mr. Davis" "Feel free to stick around if you want, but we're not doing much else today."
    "He smiles warmly at you before moving to speak to another student."
    hide MD Open Smile with dissolve
    menu year_intro_stay:
        "Stay here." if True:
            "It's mostly quiet and you have nothing better to do, so you go back to your [activity]."
        "Leave." if True:
            "It's too nice outside to stay indoors, so you pack your things up and head out!"
    jump events_end_period

label year_sophie_intro:
    show chelsea at right with moveinright
    "The Art Room is nearly empty when you arrive."
    "Setting your backpack down on the table, you take a look around."
    "A group of photographs in the corner of the room catches your attention."
    "You approach, gently hold out your hand, and examine them as gently as possible."
    show Sophie Shy at left with moveinleft
    "Sophie" "Did you... want to see some of my photographs...?"
    show chelsea shocked
    "Startled by the sudden voice so close to you, you jump with a yelp."
    show Sophie Embarrassed at left with dissolve
    "Sophie" "S-Sorry! I didn't mean to scare you!"
    "It's the young-looking girl you saw at the last meeting - the one with the camera."
    show chelsea happy
    pcname "Ah, no... I didn't hear you.!"
    show Sophie Neutral at left with dissolve
    "Sophie" "It's fine!"
    show Sophie Blank at left with dissolve
    show chelsea blank
    "Her words finally pierce the shock of her sudden presence."
    pcname "You took these? All of them?"
    show Sophie Shy at left with dissolve
    "She looks down shyly."
    "Sophie" "Y-Yes..."
    show chelsea happy
    show Sophie Embarrassed at left with dissolve
    pcname "They're amazing! How did you take this one?"
    "You pull out one that shows a couple sitting together, framed by the curl of a leaf."
    show Sophie Neutral at left with dissolve
    "Sophie" "Oh! That one was easy... They were sitting together watching their son play in the sandbox."
    "Sophie" "I just picked up a leaf I liked and held it in front of the camera while I took the picture."
    show Sophie Blank at left with dissolve
    "You stare at the photo, imagining her taking the shot."
    show chelsea blank
    pcname "I wouldn't have thought about that..."
    show Sophie Shy at left with dissolve
    "Sophie" "I can teach you some things. I-If you want...?"
    "She looks like she's about to crumble here and now."
    show Sophie Embarrassed with dissolve
    "Sophie" "You don't have to if you don't want to!"
    show chelsea happy
    pcname "No, no. That would be great! Thank you!"
    "She glances over your shoulder and backs away."
    show Sophie Sad at left with dissolve
    "Sophie" "Maybe next time we can go outside and practice..."
    show chelsea confused
    "Before you can respond, she scurries away."
    hide Sophie Sad with moveoutleft
    show chelsea blank
    show MD Laugh with dissolve
    "Mr. Davis" "[pcname]! Just the girl I was looking for!"
    "Turning, you see Mr. Davis holding something out to you."
    show MD Neutral
    "Mr. Davis" "I had this old camera at home and I thought maybe you'd like to use it?"
    show MD Blank
    show chelsea shocked
    pcname "Oh!"
    "You take the camera from him and slowly turn it over in your hands."
    "It looks nice - and really expensive."
    show MD Closed Smile
    "Mr. Davis" "I look forward to seeing what you can do with it!"
    show chelsea embarrassed
    pcname "Thank you, Mr. Davis. It's wonderful! But..."
    show MD Laugh
    "Mr. Davis" "I know you'll take good care of it. Please show me your work soon!"
    "Mr. Davis" "I have to meet with the students in charge of layout, so I'll let you familiarize yourself with the camera."
    "Mr. Davis" "If you have any questions, I'm sure Sophie is around here somewhere. She's an expert!"
    hide MD Laugh with dissolve
    show chelsea blank
    "He walks away, leaving you staring at the camera in your hands."
    show chelsea happy
    "You can't help wondering where Sophie ran off to, but you're excited for her to show you some photography techniques at the next meeting!"
    jump events_end_period


label year_levi_intro:
    show chelsea at right with moveinright
    "You walk into the Art Room and look for Sophie."
    "To your surprise, she's nowhere to be found."
    "Sitting at your usual spot, you pull out your camera and wait - but after nearly thirty minutes, there's still no sign of her."
    "You're tired of waiting, so you decide to ask around and see if anyone's seen her."
    show Levi Neutral at left with moveinleft
    "Levi" "Sophie? She went off with Mr. Davis a while ago."
    show chelsea confused
    pcname "She did?"
    show Levi HappyFix
    "Levi" "She's a bit of a teacher's pet, you know?"
    show Levi Blank
    show chelsea blank
    "He rolls his eyes."
    show Levi Happy
    "Levi" "If you want, you can join us."
    "He gestures at the table behind him. There's nobody there."
    show chelsea confused
    pcname "Us?"
    "Leaning in close, he whispers:"
    show Levi Shocked
    "Levi" "They're invisible."
    show chelsea shocked
    "You're so surprised, you can't do more than blink as you try to process it."
    show Levi Laugh
    "Levi" "C'mon, I'll explain over there."
    show chelsea blank
    show Levi Blank
    "Curiosity gets the best of you, so you follow him to his table."
    "He reaches into his backpack and pulls out a little box with a switch."
    "Flipping it, he looks around and nods at you."
    show Levi Neutral
    "Levi" "There. Now no one can hear us."
    show Levi Blank
    show chelsea confused
    pcname "What?"
    show Levi Neutral
    "Levi" "This is a special device that blocks psychic abilities. I don't want any Anti-Casters hearing us."
    show Levi Sad
    pcname "Anti-Casters?"
    show Levi Shocked
    "With a look of dismay, he throws his arms out in exaggerated shock."
    "Levi" "You don't know!?"
    "He's starting to make you a little nervous, but you're still too curious to walk away."
    pcname "Know what?"
    "He leans in again, glancing suspiciously around the room."
    show Levi Neutral
    "Levi" "Levi isn't my real name."
    pcname "Then... what is it?"
    show Levi Worried
    "Levi" "I can't tell you that! If anyone knew who I really was..."
    show Levi HappyFix
    "He trails off ominously."
    pcname "Why would anyone care?"
    show Levi Neutral
    "Levi" "I'm a {i}Caster.{/i}"
    pcname "A... what?"
    show Levi Shocked
    "Shaking his head, he stares at you disbelieving."
    "Levi" "There's no time to explain right now. I have to--"
    "He jumps back and looks around."
    "Levi" "They're close!"
    "Grabbing his box and bag, he jukes away from you and dashes toward the door."
    hide Levi Shocked with dissolve
    pcname "Okay then..."
    show chelsea blank
    pcname "What a weird guy..."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
