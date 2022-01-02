label matt_intro:
    show chelsea at right with moveinright
    T "Okay, class, today we'll be doing a small group project."
    "He divides the class into groups of three. You're paired with Matt and a girl named Susan."
    "Susan leaves her seat to join you and Matt, since you're already seated together."
    show Matt Blank at left with moveinleft
    m "You two better be willing to put in the effort. I'm not doing all of the work."
    T "One person from each group, please come up to my desk and pick up the project outline and a dry erase board."
    m "I've got it."
    hide Matt Blank with moveoutleft
    "Matt's clearly taking charge. As he walks away, you see Susan shaking her head."
    show GSGirl with dissolve
    "Susan" "What an asshole."
    if club == "track":
        show chelsea angry
        pcname "Tell me about it!"
        pcname "You don't like him either?"
    elif club == "cheer":
        pcname "He does seem a little... controlling."
        pcname "I take it you don't like him?"
    elif club == "yearbook":
        pcname "He doesn't seem very nice..."
    show chelsea blank
    "Susan" "He's always telling people what to do and how to do it."
    "Susan" "Honestly, he's just a bully."
    "Susan" "And the way he treats girls?"
    "Susan" "It's like we're pieces of meat to him."
    if club == "track":
        "That matches your experience with him pretty well, actually."
    elif club == "cheer":
        "Meat? You remember your first day. Toys, maybe..."
    elif club == "yearbook":
        "Being treated like a piece of meat..."
        show chelsea embarrassed
        "You blush at the thought."
    show chelsea blank
    "Susan" "Ugh, here he comes. Watch, he'll order us around the whole time."
    show Matt Blank at left with moveinleft
    m "Here's the outline. There's a copy for each of us."
    "He hands you one. It's a simple project using Venn diagrams."
    "You have to give your answers to a list of either-or questions, then make a diagram based on how each of you answered."
    m "And Susan, Mr. Harvey wants to talk to you about making up the test you missed yesterday."
    "Susan" "Shit! I forgot about that..."
    show Matt Angry at left
    m "Don't take too long; we're not doing the work for you!"
    hide GSGirl with moveoutleft
    "She storms away, glaring back at Matt."
    show Matt Smirk at left
    m "So, [pcname]..."
    m "About the other day..."
    menu matt_intro_apology:
        "What about it?" if True:
            if club == "track":
                show chelsea confused
                pcname "What about it?"
            elif club == "cheer":
                "You smile slowly."
                pcname "Yes...?"
            elif club == "yearbook":
                show chelsea embarrassed
                "You look away."
                pcname "Um, w-what about it?"
            pass
        "Going to apologize?" if True:
            if club == "track":
                pcname "Are you finally going to apologize?"
            elif club == "cheer":
                pcname "No need to apologize, if that's what you're doing."
            elif club == "yearbook":
                show chelsea shocked
                pcname "You're apologizing?"
                show Matt Pleased at left
            m "Pssh. Like you didn't enjoy it? You just let me feel you up!"
    show chelsea blank
    show Matt Smirk at left
    m "Seems like you're into being groped by a stranger."
    show Matt Blank at left
    m "So what else are you into?"
    menu matt_intro_intothat:
        "I heard you like being in control..." if True:
            if club == "track":
                show chelsea embarrassed
                pcname "I kinda like being told what to do, actually."
            elif club == "cheer":
                pcname "I heard you like being in control...?"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I... W-Whatever... you want..."
        "None of your business!" if True:
            if club == "track":
                show chelsea angry
                pcname "Who says I'm into that!?"
            elif club == "cheer":
                pcname "That's really none of your business."
            elif club == "yearbook":
                show chelsea shocked
                pcname "I-- I don't want to talk about this!"
    show chelsea blank
    m "Yeah? Well--"
    show GSGirl with moveinleft
    "Susan" "What did I miss?"
    "She flops into her chair, looking between you."
    "Matt draws three intersecting circles on the dry erase board, labeling each with a group member's name."
    m "We're just getting ready to give our answers to the questions."
    m "Question 1: chocolate or vanilla?"
    m "Mine's vanilla."
    "Susan" "Chocolate."
    menu matt_intro_question1:
        "Agree with Matt." if True:
            $ corruption += 1
            pcname "Vanilla."
            show Matt Smirk at left
            m "So that one goes here."
            "He writes \"Vanilla\" in the overlap between your circle and his, and \"Chocolate\" in Susan's circle."
        "Agree with Susan." if True:
            pcname "Chocolate."
            show Matt Blank at left
            m "Hmmm."
            "He writes \"Vanilla\" in his own circle, and \"Chocolate\" in the overlap between your circle and Susan's."
    show Matt Blank at left
    m "Question 2: dogs or cats?"
    "Susan" "Dogs!"
    m "Dogs."
    menu matt_intro_question2:
        "Dogs!" if True:
            show chelsea happy
            pcname "Dogs!"
            "Matt puts \"Dogs\" in the middle."
        "Cats!" if True:
            show chelsea happy
            pcname "Cats!"
            "Matt puts \"Dogs\" in the overlap between his circle and Susan's, and \"Cats\" in your circle."
    show chelsea blank
    m "Question 3: Do you prefer to be a leader or follower?"
    m "That one's easy: leader."
    "Susan" "Same."
    "He looks at you; there's a challenge in his eyes. You can tell this is about more than just the diagram."
    menu matt_intro_question3:
        "Leader." if True:
            if club == "track":
                show chelsea happy
                pcname "Definitely a leader!"
            elif club == "cheer":
                show chelsea happy
                pcname "I'd rather be in charge."
            elif club == "yearbook":
                show chelsea sad
                pcname "L-leader?"
            show Matt Question at left
            "Frowning, Matt writes \"Leader\" in the middle."
        "Follower." if True:
            $ corruption += 1
            if club == "track":
                pcname "I'm used to following orders, I guess."
            elif club == "cheer":
                pcname "Leading's too much work!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "F-follower..."
            show Matt Smirk at left
            "Smirking, Matt writes \"Follower\" in your circle, and \"Leader\" between Susan's and his own."
    show chelsea blank
    show Matt Blank at left
    m "Question 4: Would you rather be too hot or too cold?"
    m "Hot."
    "Susan" "Really? I can always put more clothes on - I'd rather be too cold!"
    m "[pcname]?"
    "He watches you intensely, as if willing you to side with him."
    menu matt_intro_question4:
        "Hot!" if True:
            $ corruption += 1
            "You meet his eyes."
            if club == "track":
                pcname "Hot."
            elif club == "cheer":
                show chelsea happy
                pcname "Definitely... hot."
            elif club == "yearbook":
                show chelsea sad
                pcname "H-hot?"
            show Matt Pleased at left
            "He marks down \"Hot\" between your circles, and \"Cold\" in Susan's."
        "Cold!" if True:
            if club == "track":
                pcname "I'm with Susan; cold."
            elif club == "cheer":
                show chelsea confused
                pcname "You said hot? Cold."
            elif club == "yearbook":
                pcname "C-cold, I guess."
            show Matt Angry at left
            "Shaking his head, he writes \"Hot\" in his own circle, and \"Cold\" between yours and Susan's."
    show chelsea blank
    show Matt Blank at left
    m "Question 5: Do you prefer peaches or bananas?"
    m "Peaches. But you girls probably like bananas, right?"
    "Susan" "Gross! You're such a pervert, Matt!"
    m "What about you, [pcname]? Like bananas?"
    menu matt_intro_question5:
        "Peaches." if True:
            if club == "track":
                pcname "I'll stick with peaches."
            elif club == "cheer":
                pcname "Not yours."
            elif club == "yearbook":
                pcname "P-peaches."
            "He puts \"Peaches\" in the middle."
        "Bananas." if True:
            $ corruption += 1
            if club == "track":
                pcname "They're my favorite."
            elif club == "cheer":
                pcname "The bigger the better."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "...y-yes..."
            m "I thought so..."
            "Susan" "[pcname]! He was talking about something else!"
            "Putting \"Peaches\" between himself and Susan, he writes \"BANANAS\" in your circle."
            if club == "track":
                "You roll your eyes, but let him have his fun."
            elif club == "cheer":
                "You can't help but smile."
            elif club == "yearbook":
                "You blush, but let him continue."
    show chelsea blank
    show Matt Happy at left
    m "Alright... Question 6: Do you prefer anal or oral?"
    "Susan" "What!? Shut up!"
    "Susan" "Was that the end of the questions? Because I need to use the bathroom."
    show Matt Blank at left
    m "Go ahead. That was it."
    "Rolling her eyes, she stands up and stretches."
    "Susan" "Want to come with me so you're not stuck with this pervert, [pcname]?"
    menu matt_intro_leave:
        "I'm fine here." if True:
            if club == "track":
                show chelsea happy
                pcname "I can handle him."
            elif club == "cheer":
                pcname "Don't worry about me!"
            elif club == "yearbook":
                pcname "I-I'm okay..."
            "Susan" "Suit yourself..."
            hide GSGirl with moveoutright
            show chelsea blank
            "As she walks away, Matt watches you."
            show Matt Smirk at left
            m "So... Are you going to answer the question?"
            menu matt_intro_question6:
                "Not answering." if True:
                    if club == "track":
                        pcname "No way!"
                    elif club == "cheer":
                        pcname "You wish..."
                    elif club == "yearbook":
                        show chelsea sad
                        pcname "N-No..."
                    m "Heh. We'll see."
                    show GSGirl with moveinright
                "Whichever he wants?" if True:
                    show chelsea embarrassed
                    if club == "track":
                        pcname "Depends what you tell me to do, doesn't it?"
                    elif club == "cheer":
                        pcname "I think that's up to you, isn't it?"
                    elif club == "yearbook":
                        pcname "I... I'll do whatever you want..."
                    m "That's what I like to hear..."
                    show chelsea blank
                    show GSGirl with moveinright
                    "Susan returns just as it's time to turn in your dry erase boards."
        "I'll go with you." if True:
            if club == "track":
                pcname "Yeah, I've had enough."
            elif club == "cheer":
                pcname "Yeah, who does he think he is?"
            elif club == "yearbook":
                pcname "Th-Thanks!"
            hide Matt Blank at left with moveoutleft
            hide GSGirl with moveoutright
            hide chelsea with moveoutright
            show bg black with dissolve
            "You follow her to the bathroom, returning just as Mr. Harvey asks everyone to turn in their dry erase boards."
            show bg ClassroomD with dissolve
            show GSGirl with moveinright
            show chelsea at right with moveinright
            show Matt Blank at left with moveinleft
    T "The bell will be ringing soon. Please have one member of the group bring the boards up to the front of the room."
    m "[pcname], you take it up."
    "He watches your reaction as he orders you around; it seems like another test."
    "Susan" "She doesn't have to listen to you. Let him take it up, [pcname]!"
    menu matt_intro_board:
        "Do what he wants." if True:
            $ corruption += 1
            if club == "track":
                "You know what he's looking for, so you do what he tells you."
            elif club == "cheer":
                "You've decided that you're kind of into being ordered around, so you do what he says."
            elif club == "yearbook":
                show chelsea sad
                "Looking down, you follow his orders."
        "Refuse." if True:
            if club == "track":
                pcname "Susan's right; do it yourself."
            elif club == "cheer":
                pcname "I'm not into following orders."
            elif club == "yearbook":
                "Shaking your head, you refuse to move."
            show Matt Angry at left
            m "Whatever. I'll do it myself."
    show chelsea blank
    "The bell rings, releasing you for the day."
    pcname "He really likes to order people around..."
    $ mattchain += 1
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
