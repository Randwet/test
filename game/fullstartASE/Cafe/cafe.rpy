label cafe:
    if acts <= 1:
        scene bg CafeN
        "The Cafe is closed for the day!"
        jump city2
    elif True:
        scene bg Cafe
    $ goingto = "work"
    stop music fadeout 3.6

    if cafeshirt >= 4:
        $ clothes = 'cafecorrupt'
    elif True:
        $ clothes = 'cafe'

    call generatetips from _call_generatetips
    call eventengine from _call_eventengine_3

    "Today you made $[tips] in tips!"

    $ Cash += tips

    if tips < 16:
        if tipsnotification == 0:
            "Some of the other waitresses seem to be making much more money than you."
            "Maybe there's something else you could be doing to please your customers?"
            $ tipsnotification += 1
        elif tipsnotification == 5:
            "You're still not making very good tips..."
            "There must be something else you could try..."
            $ tipsnotification += 1
        elif tipsnotification == 15:
            "You've decided to live with the poor tips."
            "The other girls can flirt with all the men they want; you have your pride!"
            $ tipsnotification += 1
        elif tipsnotification == 16:
            pass
        elif True:
            $ tipsnotification += 1

    if payday:
        if caferaise:
            $ paychecktotal = 21 * daysworked
        elif not caferaise:
            $ paychecktotal = 17 * daysworked

        "Before you left work, you picked up your paycheck."
        "You made [paychecktotal] dollars!"

        $ Cash += paychecktotal
        $ daysworked = 0

    $ goingto = "textwork"
    $ TextCheck = True

    call events_run_period from _call_events_run_period_2

    $ TextCheck = False

    jump city2

label generatetips:
    if tipweight == 0:
        $ tips = renpy.random.randint(13,18)
    elif tipweight == 1:
        $ tips = renpy.random.randint(18,24)
    elif True:
        $ tips = renpy.random.randint(22,32)
    return

label caferandom01:
    "You head into work and begin your shift."
    show EM Happy at left with dissolve
    "The boss notices you doing a pretty good job and compliments you on your performance!"
    hide EM Happy with dissolve
    "Work goes by slowly after that, since nothing else happens."
    jump events_end_period

label caferandom02:
    "Uh oh, you dropped some plates today! Looks like it's coming out of your tips."
    $ varrandomcash = 10
    $ tips -= varrandomcash
    "At least the rest of the day goes by smoothly."
    jump events_end_period

label caferandom03:
    "You head to work and begin your shift."
    "A customer loved your service and told the manager what a good job you did."
    $ varrandomcash = renpy.random.randint(2,10)
    "He tipped [varrandomcash] dollars!"
    $ tips += varrandomcash
    jump events_end_period

label cafeworker:
    scene black with dissolve
    "You head into work."
    "After putting on your uniform, you feel a pair of hands roughly grope your breasts from behind."
    show bg CafeGrope with dissolve
    "Kate" "Whoa! These things are huge! What do you eat!?"
    if club == "track":
        "Somehow, you feel more concerned that she snuck up on you..."
        pcname "K-Kate! You can’t just sneak up on people like that!"
    elif club == "cheer":
        pcname "Are you calling me fat!?"
        "Kate" "What? Of course not!"
    elif club == "yearbook":
        "With a shriek, you twist around and stumble away from her, gasping for breath."
        pcname "K-Kate... You... scared... me..."
    show bg Cafe with dissolve
    show K Blank at left with moveinleft
    "Kate" "Sowwie... "
    show chelsea at right with moveinright
    "Kate makes an apologetic face to go along with her baby imitation."
    pcname "It's okay..."
    "After a quick conversation, you both head into the lobby and start working."
    hide K Blank with dissolve
    hide chelsea with dissolve
    jump events_end_period

label cafe_event1:
    "You enter the cafe and change for work, but you can't help but feel discouraged."
    show chelsea sad at right with moveinright
    pcname "Tips have been really lousy lately..."
    show chelsea confused
    pcname "What am I doing wrong?"
    "As you're waiting tables, one of your customers leaves a note on your table."
    show chelsea blank
    "{i}Show some tits and you'll be worth more!{/i}"
    "Under the note is less than a dollar in change."
    if club == "track":
        show chelsea angry
        "Furious, you storm off to the bathroom."
        pcname "That asshole! Who does he think he is!?"
        "Looking at your reflection in the mirror, though, you wonder if he's right."
    elif club == "cheer":
        show chelsea angry
        "Frustrated, you excuse yourself to the bathroom."
        show chelsea blank
        pcname "I should show off my assets, huh?"
        "Looking at your reflection in the mirror, you consider it."
    elif club == "yearbook":
        show chelsea sad
        "Mortified, you flee to the bathroom."
        pcname "How could he write that..."
        "You wipe your eyes and look at yourself in the mirror."
        show chelsea embarrassed
        pcname "I couldn't..."
    menu cafe_event1_shirt:
        "Pull your neckline down." if True:
            $ renpy.block_rollback()
            $ corruption += 4
            $ clothes = 'cafecorrupt'
            $ cafeshirt += 4
            $ cafecorrupt += 1
            $ cafeprog += 1
            if club == "track":
                show chelsea happy at right with dissolve
                pcname "Maybe that will help!"
                "A little nervous, you head out and start checking on your tables."
            elif club == "cheer":
                show chelsea happy at right with dissolve
                pcname "I don't know why I didn't think of this sooner..."
                "Pleased, you head out and start checking on your tables."
            elif club == "yearbook":
                show chelsea embarrassed at right with dissolve
                pcname "I don't think I can do this..."
                "Nervous, you head out and start checking on your tables."
        "You're not that desperate!" if True:
            pcname "No way. I can't even believe I thought about it!"
            $ cafeshirt += 1
            jump events_end_period
    show chelsea embarrassed
    "You feel a little exposed, but it's kind of exciting - and the tips are definitely better!"
    $ tipweight += 1
    jump events_end_period

label cafe_kate1:
    "As you're changing for work, Kate approaches you."
    show K Blank at left with moveinleft
    "Kate" "Hey, [pcname]... Can I talk to you for a minute?"
    show chelsea at right with moveinright
    pcname "Of course!"
    "Kate" "I noticed you've been getting a lot of tips lately..."
    "Kate" "And you haven't been here for very long, so..."
    show K Happy at left
    "Kate" "I just want to know how you're doing it!"
    "Kate" "I work really hard, but I barely get anything - even from my regulars!"
    if club == "track":
        pcname "Oh, I just do this..."
        show chelsea happy
        "You pull your neckline down a little bit, exposing your cleavage."
        show K Laugh at left
        "Kate" "Wow, your boobs look great!"
        show K Embarrassed at left
        "Kate" "But-- mine aren't that big..."
    elif club == "cheer":
        pcname "Oh, that's easy... I just do {i}this{/i}!"
        show chelsea happy
        "You pull your neckline down, exposing your cleavage."
        show K Laugh at left
        "Kate" "Wow, your boobs look great!"
        show K Embarrassed at left
        "Kate" "But-- mine aren't that big..."
    elif club == "yearbook":
        pcname "Oh, I..."
        "Kate" "Do you have a secret?"
        pcname "I... I just..."
        show chelsea embarrassed
        "Looking away, you pull your neckline down a little bit, exposing your cleavage."
        show K Laugh at left
        "Kate" "Wow, your boobs look great!"
        show K Embarrassed at left
        "Kate" "But-- mine aren't that big..."
    pcname "Don't worry, Kate. I'm sure you'll think of something."
    pcname "Who can resist that smile?"
    show K Happy at left
    "She tries to give you one - but it doesn't look very convincing."
    show K Laugh at left
    "Kate" "Yeah, let's both do our best. Okay?"
    $ katedream = True
    jump events_end_period

label cafe_event2:
    show chelsea at right with moveinright
    "As you're waiting tables, a middle-aged man calls you over."
    "Man" "What's your name, little lady?"
    show chelsea happy
    pcname "[pcname], Master. How may I be of service?"
    "Man" "I can tell you've been working really hard..."
    "Man" "Why don't you sit down and take a little break?"
    "He smiles up at you and pats his knee."
    "You've seen this guy around - though you don't usually wait on him."
    "He's known to be a really big tipper."
    menu cafe_event2_sit:
        "Sit on his lap." if True:
            $ corruption += 2
            if club == "track":
                pcname "I {i}could{/i} use a little break..."
                "Drawing up your courage, you sit on his lap and smile."
            elif club == "cheer":
                pcname "Oh, you're too kind!"
                "You sit in his lap with your breasts just under his face."
            elif club == "yearbook":
                pcname "Oh, I--"
                "You could really use the money..."
                pcname "I suppose I could..."
                "Before you can change your mind, you take a seat on his lap."
            hide chelsea with dissolve
            $ cafelap = True
            $ cafecorrupt += 1
            $ tipweight += 1
        "Make an excuse." if True:
            show chelsea embarrassed
            pcname "Oh, don't worry about me! I'm used to it!"
            "You scurry away, hoping the creep doesn't call you over again."
            jump events_end_period
    if cafecorrupt == 2:
        show bg CL5 with dissolve
    elif True:
        show bg CL1 with dissolve
    "Man" "That's a good girl!"
    "Man" "Tell me, do you like working here?"
    pcname "It's not too bad. The owner's really nice..."
    if cafecorrupt == 2:
        show bg CL6 with dissolve
    elif True:
        show bg CL2 with dissolve
    "As you talk, you feel something hard beneath you... He has an erection!"
    menu cafe_event2_erection:
        "Jump up." if True:
            if cafecorrupt == 2:
                show bg CL7 with dissolve
            elif True:
                show bg CL3 with dissolve
            "You shoot up out of his lap, blushing furiously."
            pcname "S-Sorry, but I have to go service other customers!"
            "He laughs as you scurry away. When you clean his table, you see that he left a decent tip."
            $ tips += 10
            jump events_end_period
        "Wiggle around." if True:
            if cafecorrupt == 2:
                show bg CL8 with dissolve
            elif True:
                show bg CL4 with dissolve
            $ corruption += 3
            if club == "track":
                "You've come this far; you might as well see it through!"
            elif club == "cheer":
                "Thrilled by his reaction, you encourage him."
            elif club == "yearbook":
                "You freeze a moment, unsure of yourself."
                "You're not sure what you were expecting; you should have known this would happen."
                "And now that you've led him on, you can't get out of it, can you?"
    pcname "And all of the customers have been so kind..."
    "You shift your weight forward and back, rubbing your ass along the length of his cock."
    "He sucks in a shaky breath, clearly enjoying what you're doing."
    "Man" "You like serving them, then?"
    if club == "track":
        pcname "Oh, yeah!"
        "You continue moving back and forth, as if trying to find a comfortable position."
        pcname "I've met so many nice men here too!"
        "Man" "Is that so?"
        "He shifts beneath you, pressing his cock against you a little harder."
        "Gasping, you move a little faster."
        pcname "Oh yeah..."
    elif club == "cheer":
        pcname "Oh, {i}yes{/i}..."
        "You continue moving back and forth, as if trying to find a comfortable position."
        pcname "I've met {i}so{/i} many nice men here."
        "Man" "Is that so?"
        "He shifts beneath you, pressing his cock against you a little harder."
        "Gasping, you rock faster against him, highly aware that only your thin skirt and panties separate you from that hard cock."
        pcname "Oh... yes..."
    elif club == "yearbook":
        pcname "O-oh! I... yes..."
        "You continue moving back and forth - nervously - as if trying to find a comfortable position."
        pcname "And... I-I've met so many nice men here."
        "Man" "Is that so?"
        "He shifts beneath you, pressing his cock harder against you."
        "Gasping, you freeze, trembling on top of him."
        pcname "I..."
    "Kate" "[pcname], could you help me over here?"
    if cafecorrupt == 2:
        show bg CL7 with dissolve
    elif True:
        show bg CL3 with dissolve
    "You jump up, blushing."
    show bg Cafe with dissolve
    show chelsea embarrassed at right with moveinright
    pcname "S-Sorry... It looks like I'm needed."
    "Man" "Of course! I'm sure I'll see you again soon."
    "He winks."
    hide chelsea with moveoutright
    "When you come back to clean off his table, you see that he left a huge tip!"
    $ tips += 30
    jump events_end_period

label cafe_kate2:
    "During your break, Kate approaches you."
    show K Blank at left with moveinleft
    show chelsea at right with moveinright
    "Kate" "So, [pcname], I've been thinking about what you said..."
    show K Happy at left
    "Kate" "And I think I'm going to try getting more attention too."
    menu cafe_kate2_moralchoice:
        "Encourage her." if True:
            $ corruptkate = True
            $ corruption += 3
            show chelsea happy
            if club == "track":
                pcname "Really? Hmmm..."
                "You reach over and undo the top two buttons of her shirt."
                show K Embarrassed at left
                "Kate" "Oh, I don't know if I can work like that!"
                pcname "Don't worry - you look good!"
                pcname "Besides, you want better tips, right?"
                "Kate nods, still looking uncomfortable."
            elif club == "cheer":
                pcname "Awesome! I had a few ideas for you..."
                "You reach over and undo the top two buttons of her shirt."
                show K Embarrassed at left
                "Kate" "Oh, I don't know if I can work like that!"
                pcname "Don't be silly! You'll get used to it in no time."
                pcname "Besides, you want better tips, right?"
                "Kate nods, still looking uncomfortable."
            elif club == "yearbook":
                pcname "Oh! Well, if you wanted to... maybe..."
                "You reach over hesitantly and undo the top two buttons of her shirt."
                show K Embarrassed at left
                "Kate" "Oh, I don't know if I can work like that!"
                pcname "I was really nervous at first too, but..."
                pcname "I mean... You want better tips, right?"
                "Kate nods, still looking uncomfortable."
        "Discourage her." if True:
            pcname "Actually, Kate, I think you're great the way you are."
            show K Blank at left
            "Kate" "Yeah, but..."
            pcname "Trust me, you {i}don't{/i} want that kind of attention."
            show K Laugh at left
            "Kate" "Maybe you're right. Thanks, [pcname]!"
    jump events_end_period

label cafe_event3:
    show chelsea at right with moveinright
    "You change into your work uniform."
    "Suddenly, you have another idea..."
    menu cafe_event3_panties:
        "Take off your panties." if True:
            $ corruption += 3
            hide chelsea with dissolve
            show bg CPS1 with dissolve
            if club == "track":
                "Reaching under your skirt, you pull your panties down and kick them away."
                pcname "I can't believe I'm doing this..."
            elif club == "cheer":
                "Reaching under your skirt, you pull your panties down and kick them away."
                pcname "Breezy!"
            elif club == "yearbook":
                "Reaching under your skirt, you pull your panties down and kick them away."
                pcname "Oh... I don't know if I can do this..."
            $ cafepanties = True
            $ cafecorrupt += 1
            $ tipweight += 1
        "Keep them on." if True:
            show chelsea embarrassed
            pcname "N-No way, I can't work like that!"
            "Laughing at yourself, you check on your first table."
            jump events_end_period
    show bg Cafe with dissolve
    show chelsea happy with dissolve
    "The air against your skin makes you extremely aware of your missing clothes as you approach your first customer."
    pcname "Are you enjoying your meal?"
    "Customer" "Yeah, thanks."
    "He glances at you, his gaze lingering on your cleavage."
    menu cafe_event3_drop:
        "Drop something." if True:
            if club == "track":
                pcname "Can I get you anything else?"
                "Customer" "No, I--"
                hide chelsea with dissolve
                show bg CPS2 with dissolve
                "Before he can finish, you \"accidentally\" drop your pen."
                pcname "Oops!"
                "Turning away, you bend over to pick it up - which lifts your skirt to show off your exposed ass."
                "When you turn back around, the man's eyes are wide."
                pcname "Sorry about that! Did you want anything else?"
            elif club == "cheer":
                pcname "Can I get you {i}anything{/i} else?"
                "Customer" "No, I--"
                hide chelsea with dissolve
                show bg CPS2 with dissolve
                "Before he can finish, you \"accidentally\" drop your pen."
                pcname "Oops!"
                "Turning away, you bend over to pick it up - which lifts your skirt to show off your exposed ass."
                "When you turn back around, the man's eyes are wide."
                pcname "Sorry about that! Did you want anything {i}else{/i}?"
            elif club == "yearbook":
                pcname "Can I get you anything else?"
                "Customer" "No, I--"
                hide chelsea with dissolve
                show bg CPS2 with dissolve
                "Before he can finish, you \"accidentally\" drop your pen."
                pcname "Oh! Oops..."
                "Turning away, you bend over to pick it up - which lifts your skirt to show off your exposed ass."
                "You turn back around, blushing profusely, and the man's eyes are wide."
                show chelsea embarrassed
                pcname "S-Sorry about that! C-Can I get you anything else?"
            $ corruption += 2
            "Customer" "No, I'm {i}great.{/i}"
        "Check the next table." if True:
            pass
    show bg Cafe with dissolve
    show chelsea happy with dissolve
    "Leaving him with a smile, you move on to the next customer."
    pcname "Hello! Can I start you with something to drink?"
    "Customer" "Just water, please."
    if club == "track":
        "You feel the air caressing your exposed pussy and ass. It's surprisingly freeing!"
    elif club == "cheer":
        "It's thrilling to feel the air against your exposed pussy and ass. In fact, you feel a little bit of heat starting to build up..."
    elif club == "yearbook":
        "Cool air licks across your pussy and ass. You glance around nervously, wondering how many people have noticed."
    pcname "Of course! I'll be back in just a minute!"
    menu cafe_event3_turn:
        "Turn quickly." if True:
            $ corruption += 2
            hide chelsea with dissolve
            show bg CPS3 with dissolve
            "You turn away quickly, causing your skirt to flare up."
            if club == "track":
                "Several customers turn to stare as you walk to the beverage station."
            elif club == "cheer":
                "You feel the heat of many eyes following you as you walk to the beverage station."
            elif club == "yearbook":
                "Your cheeks burn as several customers turn to stare."
                "Walking quickly and lowering your gaze, you hurry to the beverage station."
        "Turn slowly." if True:
            "You turn away slowly, careful not to move your skirt too much."
    show bg Cafe with dissolve
    show chelsea with dissolve
    "You return to your customer with their order."
    if club == "track":
        pcname "There you go! Would you like something else?"
        "He blinks, finally glancing back up at your face."
        "Customer" "Oh, I... I think I need a few more minutes..."
        pcname "No problem. I'll check back with you soon."
        "You check on your other tables, {i}very{/i} aware of how exposed you are when you move certain ways."
        "As time goes on, you notice that your customers are aware too."
    elif club == "cheer":
        pcname "There you go! Would you like something {i}else{/i}?"
        "He blinks, finally glancing back up at your face."
        "Customer" "Oh, I... I think I need a few more minutes..."
        pcname "No problem. I'll check back with {i}you{/i} soon."
        "You check on your other tables, {i}very{/i} aware of how exposed you are when you move certain ways."
        "As time goes on, you're pleased to see that your customers are aware too."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Th-There you go! Would you... like something else?"
        "He blinks, finally glancing back up at your face, but you can't meet his eyes."
        "Customer" "Oh, I... I think I need a few more minutes..."
        pcname "No problem. I'll... check back with you soon?"
        "You check on your other tables, {i}very{/i} aware of how exposed you are when you move certain ways."
        "As time goes on, you realize that many of your customers are aware too."
    jump events_end_period

label cafe_kate3:
    "As you prepare for work, Kate stops you."
    show K Blank at left with moveinleft
    show chelsea at right with moveinright
    "Kate" "Hey, [pcname], about what we talked about before..."
    "Kate" "I saw what you did the other day. Not wearing panties under your skirt?"
    if corruptkate:
        show K Laugh at left
        show chelsea happy
        "Kate" "I think it's hilarious! How do you come up with stuff like that?"
        if club == "track":
            pcname "I don't know! And, honestly? It's kind of fun!"
            show K Happy at left
            "Kate" "What! Oh [pcname]!"
            pcname "No, seriously... It's thrilling knowing how many guys were looking at me."
            show K Embarrassed at left
            "Kate" "Ohhh, that does sound exciting! Maybe I should try it..."
        elif club == "cheer":
            pcname "I don't know! And, honestly? It kind of turned me on..."
            show K Happy at left
            "Kate" "What! Oh [pcname]!"
            pcname "No, seriously... Every time I bent over I wondered how many guys were looking at me."
            show K Embarrassed at left
            "Kate" "Ohhh, that does sound hot! Maybe I should try it..."
        elif club == "yearbook":
            pcname "I don't know! It was so embarrassing, and yet..."
            show K Happy at left
            "Kate" "What! Oh, [pcname]! You enjoyed it, didn't you!?"
            pcname "I don't-- There were so many men looking at me, and I was so {i}exposed{/i}..."
            show K Embarrassed at left
            "Kate" "Ohhh, that sounds so dirty! Maybe I should try it..."
        show K Laugh at left
        "She giggles."
        $ corruption += 1
        "Kate" "I better get back to work. Let's talk more later!"
    elif True:
        show K Mad at left
        "Kate" "How could you do that!?"
        show chelsea angry
        if club == "track":
            pcname "It's none of your business what I do, Kate!"
            "Kate" "You're disgusting! I can't believe I thought we could be friends."
            pcname "I wouldn't want to be friends with someone as closed-minded as you anyway."
            "She turns away quickly - but not before you see the tears welling up in her eyes."
            "Kate" "Do whatever you want. I don't care if you want to be a slut!"
            "She storms off before you have a chance to respond."
            pcname "A slut!? I'm just having fun..."
        elif club == "cheer":
            pcname "It's none of your business how I earn my tips, Kate!"
            "Kate" "You're disgusting! I can't believe I thought we could be friends."
            pcname "I wouldn't want to be friends with someone as closed-minded as you anyway."
            "She turns away quickly - but not before you see the tears welling up in her eyes."
            "Kate" "Do whatever you want. I don't care if you want to be a slut!"
            "She storms off before you have a chance to respond."
            pcname "What a frigid bitch..."
        elif club == "yearbook":
            pcname "Kate, I--"
            "Kate" "You're disgusting! I can't believe I thought we could be friends."
            pcname "Why are you mad at me!? I'm just--"
            "She turns away quickly - but not before you see the tears welling up in her eyes."
            "Kate" "Do whatever you want. I don't care if you want to be a slut!"
            "She storms off before you have a chance to respond."
            pcname "But I'm not... Am I?"
        $ katerelate = "enemy"
    jump events_end_period

label cafe_event4:
    "Near the end of the night, Kate approaches you."
    show chelsea at right with moveinright
    if corruptkate:
        show K Happy at left with moveinleft
        "Kate" "Hey, there's a guy asking for you. He's that big tipper who comes by sometimes."
        "She winks as she points him out to you. It's the guy who asked you to sit on his lap."
        show K Laugh at left
        "Kate" "Have fun!"
        hide K Laugh
    elif True:
        show K Blank at left with moveinleft
        "Kate" "It's that sleazy guy who hits on all the girls. I guess I know why he wants you."
        "She rolls her eyes and walks away."
        hide K Blank with dissolve
    show chelsea happy
    "With a smile on your face, you walk to his table."
    "Man" "[pcname], it's good to see you again."
    pcname "Kate said you were asking for me, sir?"
    "Man" "You get off work soon, right?"
    if club == "track":
        pcname "Yes, but I have time for one of my favorite customers!"
        "Man" "That's great..."
    elif club == "cheer":
        pcname "Yes, but I have plenty of time to take care of {i}you.{/i}"
        "Man" "That's what I like to hear."
    elif club == "yearbook":
        pcname "Y-yes, I do..."
    "He looks around, making sure there's no one else nearby before sliding $50 across the table."
    "Man" "Why don't you meet me in my car when you get off? I have something I'd like you to take care of..."
    show chelsea blank
    menu cafe_event4_car:
        "Agree." if True:
            $ corruption += 3
            show chelsea happy
            if club == "track":
                "You have a pretty good idea what he has in mind."
                pcname "I think I can do that..."
                "Smiling, you tuck the money into your bra."
                "Man" "Glad to hear it. I'll be waiting."
            elif club == "cheer":
                "You have a pretty good idea what he has in mind."
                pcname "I can't disappoint my favorite customer, can I?"
                "Smiling, you tuck the money into your bra."
                "Man" "I didn't think you would. I'll be waiting."
            elif club == "yearbook":
                "You wonder... Is he suggesting what you think he is?"
                pcname "I... I guess I could..."
                "Picking it up in a trembling hand, you tuck the money into your bra."
                "Man" "I knew you wouldn't let me down. I'll be waiting."
            $ cafeblowjob = True
            $ cafecorrupt += 1
            $ tipweight += 1
            $ Cash += 50
        "Make up an excuse." if True:
            show chelsea embarrassed
            pcname "I'm sorry, but I promised Kate I'd help her close up tonight."
            pcname "I'll be getting out later than usual."
            "He frowns, picking up the bill and tucking it back into his wallet."
            "Man" "That's too bad..."
            jump events_end_period
    hide chelsea
    show bg black with fade
    "After your shift, you walk out to the parking lot."
    "There's a really nice car parked at the far end."
    "As you get closer, you see the man sitting inside. He waves you over."
    "Man" "I was starting to wonder if you were coming."
    "He smiles."
    "Man" "Go ahead, get in."
    "You walk to the passenger's side, open the door, and climb in."
    show bg Car1 with dissolve
    "Man" "You're such a pretty girl..."
    "As he speaks, he unzips his pants."
    "Man" "And I love redheads {i}so much...{/i}"
    "He pulls his cock free and leans back in his seat."
    if cafelap:
        "Man" "Go on. You're already acquainted, right?"
    elif True:
        "Man" "What are you waiting for?"
    if club == "track":
        "Your heart thunders in your chest - you can't believe you're really doing this!"
    elif club == "cheer":
        "The sight of his cock warms you - especially in a certain area..."
    elif club == "yearbook":
        "Drawing a shaky breath, you swallow back your nerves."
    show bg Car2 with dissolve
    "Licking your lips, you lean across the console and trail your tongue along the head of his cock."
    "Man" "Oh, yeah..."
    show bg Car3 with dissolve
    "Flicking your tongue across his slit, you wrap your hand around him and stroke him slowly."
    "He rests his hand on your head, the weight of it pressing your lips against his tip."
    show bg Car4 with dissolve
    "Opening your mouth, you take him in slowly."
    "Bobbing your head up and down, you lube him with your spit, taking more of him in each time."
    "Man" "Fuck, you're good at this..."
    "His cock leaks salty pre-cum across your tongue, which you swallow happily."
    "His fingers twist in your hair, grasping a fistful and using it to pull you closer."
    if corruption > 20:
        "You open your throat, taking him in completely."
        "Man" "Holy shit..."
        show bg Car5 with dissolve
        "He releases your hair, letting you pull back to his tip before plunging your mouth back down his cock."
        "You hold your face tight against him, letting the muscles of your throat massage him."
        "Pulling back, you suck in a deep breath through your nose and swallow his cock again."
        "Man" "Fuck... I can't..."
        show bg Car7 with dissolve
        "His hips jerk against you as he cums, sending a stream of hot cum down your throat."
        "You suck him hard as you pull back, releasing his cock with a {i}pop{/i}."
    elif True:
        show bg Car6 with dissolve
        "You struggle not to gag as he hits the back of your throat."
        "He pulls your head back and forth, fucking your face."
        "You look up at him through your eye lashes, watching his expression as he uses your mouth."
        "Man" "You like sucking cock, don't you?"
        pcname "Mmmhmmm..."
        "Pre-cum coats your tongue as he pulls your head up and down on his cock."
        show bg Car9 with dissolve
        "Suddenly he pulls your head back, shooting his load across your face."
        "You lick the cum from your lips and smile up at him."
    show bg black with dissolve
    "Man" "Holy shit. That was amazing."
    if club == "track":
        "Grinning, you sit back up in your seat."
        pcname "Glad to hear it!"
        "Giddy with excitement, you swing the car door open and jump out."
        pcname "Have a good night!"
    elif club == "cheer":
        "You giggle."
        pcname "Anything for a customer!"
        "You wink as you leave the car."
    elif club == "yearbook":
        "Suddenly, the reality of what you've done hits you."
        pcname "I-- I have to go!"
        "Dashing out of the car, you hurry toward your apartment."
        "A few blocks away, you stop and touch your lips."
        "You can still taste his cum."
        "You're not sure how to feel, but it {i}was{/i} exciting..."
    $ acts-=1
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
