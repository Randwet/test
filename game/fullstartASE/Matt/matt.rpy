label matt_scene1:
    "You enter your classroom and notice that the seat behind you is empty."
    "Taking your seat, you find a piece of paper on your chair."
    "You glance over it--it's a note from Matt."
    "It reads: {i}Wait 5 mins and come to the men's room.{/i}"
    "Your heart thumps in your chest. The men's room?"
    "Watching the clock, five minutes go by quickly."
    menu matt_scene1follow:
        "Go to the men's room" if True:
            show chelsea at right with moveinright
            $ corruption += 1
            "You stand, glancing around nervously."
            pcname "Excuse me, [T]... May I use the restroom?"
            T "Yes, go ahead."
            show bg SchoolRestroom with dissolve
            hide chelsea with moveoutright
        "Stay in the classroom" if True:
            "Ignoring his message, you focus on the lesson."
            "The rest of the day, you can't help but wonder what he had planned."
            $ defymatt = True
            jump events_end_period
    "Your heart is racing as you walk down the hall to the nearest men's room."
    "Nervously, you check the hall to make sure nobody is watching, then duck inside."
    "Matt is standing by the mirror, looking bored."
    show chelsea at right with moveinright
    show Matt Blank at left with moveinleft
    m "About time. Come here."
    menu matt_scene1come:
        "Approach him" if True:
            $ corruption += 1
            "You walk over to him immediately."
        "Ask what he wants" if True:
            if club == "track":
                show chelsea confused
                pcname "Why did you want me to meet you here?"
            elif club == "cheer":
                show chelsea confused
                pcname "Did you need something?"
            elif club == "yearbook":
                pcname "W-why?"
            "He frowns."
            show Matt Question at left
            m "Why do you think? Now get over here."
            "You approach him slowly."
    show chelsea blank
    show Matt Blank at left
    m "Turn around."
    "You turn slowly, aware of his eyes on you."
    show Matt Pleased at left
    m "Your ass is kinda small, but you have nice tits."
    show chelsea embarrassed
    "Your cheeks burn as he bluntly assesses your body."
    show Matt Smirk at left
    m "Lift your skirt up."
    menu matt_scene1lift:
        "Lift your skirt" if True:
            "You lift your skirt hesitantly, afraid that someone might walk in."
            $ corruption += 2
        "Refuse" if True:
            if club == "track":
                show chelsea angry
                pcname "Someone could walk in!"
                m "So what? Aren't you going to do what I want?"
            elif club == "cheer":
                show chelsea angry
                pcname "What!? No way!"
                m "Why'd you come here if you're not going to do what I tell you?"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I-I can't..."
                m "Pssh. What are you good for?"
            menu matt_scene1lift2:
                "Give in" if True:
                    show chelsea sad
                    "Looking down at the floor, you slowly raise your skirt."
                "Refuse again" if True:
                    pcname "I... I can't!"
                    "Matt shakes his head in disappointment."
                    show Matt Angry at left
                    m "I thought you might actually be interesting... What a disappointment."
                    "He storms passed you, leaving you alone in the men's room."
                    "You go back to class and try to pay attention to the lecture."
                    $ defymatt = True
                    jump events_end_period
    show Matt Blank at left
    $ mattchain+=1
    "He watches you, still looking bored."
    m "Not bad."
    scene bg black with fade
    show bg MBat1 with dissolve
    "Reaching out, he runs a hand up the inside of your thigh."
    "His fingers pause as he reaches your underwear."
    show bg MBat2 with dissolve
    "Slowly, he trails his fingers over your panties, stroking you through them."
    "You can't help but gasp."
    if club == "track":
        pcname "W-what are you doing!"
    elif club == "cheer":
        pcname "Ohhh..."
    elif club == "yearbook":
        pcname "M-Matt..."
    "His fingers stroke slowly upwards, brushing your clit before sliding back down."
    "Your eyes drift shut as heat spreads through you, following his touch."
    m "You're already getting wet!"
    "He pulls his fingers away."
    "You take a deep breath, trying to slow your pounding heartbeat."
    "Suddenly, he laughs."
    "You blink your eyes open, shocked to see him holding his phone up."
    m "I knew you were a dirty slut."
    "His words are harsh, but he sounds pleased."
    menu matt_scene1defend:
        "Defend yourself!" if True:
            if club == "track":
                pcname "What!?"
            elif club == "cheer":
                pcname "I'm not a... a slut!"
            elif club == "yearbook":
                pcname "I... I'm not..."
            "He smirks."
            m "You're letting a guy you barely know feel you up in a bathroom."
            m "What do {i}you{/i} call that?"
            show bg MBat3 with dissolve
            "You push your skirt back down and glare."
        "Look down." if True:
            if club == "track":
                "You look down, hiding your defiance."
            elif club == "cheer":
                "You look down, pretending not to enjoy the word."
            elif club == "yearbook":
                "You look down meekly, humiliated."
            m "Put your skirt back down, slut."
            $ corruption +=3
            show bg MBat3 with dissolve
            "Face burning with shame, you lower your skirt."
    show bg black with dissolve
    show Matt Pleased at left with dissolve
    show chelsea embarrassed at right with dissolve
    if club == "track":
        pcname "What were you doing with your phone?"
    elif club == "cheer":
        pcname "Were you taking a picture?"
    elif club == "yearbook":
        pcname "Why did you have your phone out...?"
    m "Oh, that?"
    m "That was for later."
    m "You can go now. I'll let you know when I want to see you... privately... again."
    "You turn to go, unsure of how to feel."
    show Matt Smirk at left
    m "Wait a sec."
    "Turning, you see him smiling at you."
    m "Take off your panties and give them to me."
    menu matt_scene1panties:
        "Do as he says" if True:
            scene bg black with fade
            show bg MBat4 with dissolve
            $ corruption += 1
            if club == "track":
                "Amused, you do as he tells you."
            elif club == "cheer":
                "Aroused by the idea, you do as he tells you."
            elif club == "yearbook":
                "Heart pounding, you do as he tells you."
            "Reaching up your skirt, you pull your panties down, stepping out of them one leg at a time."
            "As you pass them to Matt, you can't help but notice the wet spot your arousal caused."
            m "Now you'll think about me all day. I bet that skirt'll be drafty without these."
            "You leave the bathroom and make your way back to class."
            show bg black with fade
            show bg ClassroomD with dissolve
            "It doesn't take long for you to realize that Matt was right."
            "You spend the rest of the day thinking about your missing panties, torn between embarrassment and arousal."
        "Refuse" if True:
            if club == "track":
                show chelsea angry
                pcname "I'm not giving you my underwear!"
            elif club == "cheer":
                show chelsea blank
                pcname "Forget it!"
            elif club == "yearbook":
                show chelsea sad
                pcname "I-I can't do that!"
            "He laughs."
            hide Matt Smirk with dissolve
            show bg black with fade
            show bg ClassroomD with dissolve
            "You leave the bathroom and make your way back to class."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
