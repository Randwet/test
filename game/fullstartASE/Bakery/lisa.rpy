
label lisa_event1:
    "The walk to work is warm and sunny; you feel like it's going to be a great day!"
    "Your manager seems preoccupied with paperwork, so you ask Lisa what you should do first."
    show L Blank at left with moveinleft
    show chelsea at right with moveinright
    L "Why don't you grab some gloves and help me with these tarts?"
    if club == "track":
        show chelsea happy
        pcname "Sure!"
    elif club == "cheer":
        show chelsea confused
        pcname "Is it messy?"
        L "That's what gloves are for!"
    elif club == "yearbook":
        show chelsea happy
        pcname "I think I can do that..."
    show chelsea blank
    L "Just grab a lump of dough off that ball and press it flat with your hands."
    "She demonstrates as she talks, pulling some dough off a large ball on the counter and pressing it out on the table."
    L "When you have a circle a little bigger than your tin, you lift it up and lay it in the tin..."
    show L Happy at left
    L "...and then you press gently to fill along the edges and side. See?"
    show L Blank at left
    "She smooths her finger around the inside of the tart tin, easily pressing the dough into the crease and up the sides."
    "She pulls her hands away to reveal a perfect crust."
    show L Happy at left
    L "Now you try!"
    show L Blank at left
    "She watches as you pull some dough from the ball and work it with your gloved fingers."
    show chelsea embarrassed
    "Before you've realized you don't have enough dough, she's already passing you a little more."
    if club == "track":
        show chelsea happy
        pcname "Thanks; I didn't grab enough, I guess."
    elif club == "cheer":
        show chelsea shocked
        pcname "Oops!"
    elif club == "yearbook":
        pcname "Th-Thanks..."
    show chelsea blank
    L "No problem. It'll get easier to judge how much you need."
    "When your dough looks mostly round, you lift it gently and put it in a tin - but a large crack appears!"
    L "That's okay; it'll still work fine. Just smooth the crack back together with your finger."
    "Following her instructions, you mend the crack and finish pressing the dough into the edges of the tin."
    "It's far from perfect, but it looks like a passable crust!"
    show L Happy at left
    L "That will do. You'll get better with some practice."
    if club == "track":
        show chelsea happy
        pcname "The next one will look better!"
    elif club == "cheer":
        pcname "It's not as hard as I thought it would be."
    elif club == "yearbook":
        pcname "I'll keep trying..."
    show chelsea blank
    show L Blank at left
    "The two of you work in silence for a few minutes; all of your focus is on the dough you're working."
    L "So, [pcname]... Do you have a boyfriend?"
    menu lisaboyfriend:
        "I hang out with a guy sometimes..." if mattsubmissive == True:
            show L Happy at left
            L "\"Hang out\", huh?"
            if club == "track":
                pcname "He's kind of a jerk, but..."
            elif club == "cheer":
                pcname "We're not dating or anything, but..."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "...something like that..."
        "His name is Damien." if damienevents > 3:
            show chelsea happy
            show L Blank at left
            L "Hmmm..."
        "Not a \"boyfriend\"..." if violetscenes > 2:
            show L Happy at left
            L "Oh? A girl, then?"
            if club == "track":
                "You shrug, trying to hold back a smile as you think of a particular girl..."
            elif club == "cheer":
                show chelsea happy
                pcname "What can I say?"
            elif club == "yearbook":
                show chelsea embarrassed
                "Blushing, you can't seem to think of what to say..."
        "There's nobody yet." if True:
            show L Question at left
            L "Nobody at all? We need to do something about that!"
    show L Happy at left
    show chelsea blank
    "Lisa laughs. The ball of dough has gotten smaller as you talk; it's about half the size of when you started."
    if club == "track":
        show chelsea confused
        pcname "Well? What about you?"
    elif club == "cheer":
        show chelsea happy
        pcname "So who are {i}you{/i} dating?"
    elif club == "yearbook":
        show chelsea embarrassed
        "You're desperate to shift the focus off of yourself."
        pcname "W-What about you?"
    show L Blank at left
    show chelsea blank
    L "Me? Oh, nobody right now..."
    L "Actually..."
    L "Well, I {i}was{/i} married once. It was my last real {i}relationship{/i}."
    show chelsea shocked
    pcname "You were?"
    "You can't help the surprised tone in your voice; you had no idea she'd been married."
    L "We were married for two years when my husband lost his job."
    L "He found one quickly, but since he took a pay cut we decided I would get a job too."
    show L Happy at left
    show chelsea blank
    "She smiles."
    L "That's how I ended up working here, actually!"
    show chelsea confused
    pcname "So what happened?"
    show L Blank at left
    "She waves her hand dismissively."
    show chelsea blank
    L "Oh, you know... Sometimes people just grow apart!"
    L "Shortly after I started working here, things just sort of fell apart between us..."
    "She shrugs. She seems so unaffected that you're not quite sure how to respond."
    show chelsea confused
    pcname "Oh. I'm sorry?"
    show L Happy at left
    L "Don't worry; it's all in the past!"
    show chelsea blank
    show Keith Neutral with moveinleft
    BM "Lisa, if you're done with those tarts I need to see you!"
    "She perks up immediately."
    L "Just finishing them now, sir!"
    hide Keith Neutral with dissolve
    show L Happy at left
    L "[pcname], can you finish the last few and move these trays back to the walk-in?"
    "The ball of dough is almost gone - you might be able to make two more."
    if club == "track":
        show chelsea happy
        pcname "Yeah, no problem!"
    elif club == "cheer":
        pcname "I guess so..."
    elif club == "yearbook":
        show chelsea happy
        pcname "S-sure. I got it."
    show L Blank at left
    L "Great. I'll be back soon."
    show chelsea blank
    hide L Blank with moveoutleft
    "She takes her gloves off and strolls into the manager's office."
    BM "Close the door. There's something we need to discuss."
    "You hear the door click shut."
    "As you make the last few tarts, you can't help but think about Lisa's reactions."
    if club == "track":
        show chelsea angry
        pcname "The manager is so bossy; I don't know how she can stand him!"
    elif club == "cheer":
        show chelsea happy
        pcname "She's so young to be tied down; I wouldn't want to be married either!"
    elif club == "yearbook":
        show chelsea sad
        pcname "It must be sad to be alone at her age..."
    show chelsea blank
    "After carrying the trays to the refrigerator, you grab a cloth and start cleaning up the work area."
    "By the time you've swept and mopped as well, you've forgotten all about your conversation."
    jump events_end_period

label lisa_event2:
    "There's nobody around when you enter the bakery, so you clock in and wait near the front counter."
    show chelsea at right with moveinright
    show L Blank at left with moveinleft
    L "Oh, it's just you, [pcname]."
    show chelsea shocked
    "Startled, you turn to see Lisa approaching - her eyes are red, as if she was crying."
    show chelsea confused
    pcname "Are you okay?"
    show L Happy at left
    "Lisa waves you off, smiling."
    L "I'm just fine. Would you mind sweeping up while I check on the sourdough?"
    show chelsea happy
    pcname "No problem!"
    hide L Happy with moveoutleft
    show chelsea blank
    "Grabbing the broom, you carefully sweep the floor."
    "No matter how often you clean, there's always flour on the floor - it never ceases to amaze you."
    show L Disappoint at left with moveinleft
    "Lisa returns a few minutes later, scowling down at her phone."
    show chelsea confused
    pcname "Are you sure everything's okay, Lisa?"
    show chelsea blank
    "She rolls her eyes and tucks her phone back in her pocket."
    show L Happy at left
    L "Everything's fine. It's just my ex-husband whining at me again."
    show L Blank at left
    L "You know, [pcname], there's nothing worse than a wimpy man."
    L "Even after all these years, he can't make a decision on his own."
    L "Honestly, I don't know what I ever saw in him..."
    if club == "track":
        show chelsea happy
        pcname "I'm sure there was something you liked."
    elif club == "cheer":
        show chelsea shocked
        pcname "It sounds like it's good that you split up."
    elif club == "yearbook":
        show chelsea sad
        pcname "I... I don't know..."
    show L Happy at left
    show chelsea blank
    "She laughs."
    show L Blank at left
    L "I was young and naive; I didn't know what I {i}really{/i} wanted in a man."
    L "I thought that he was a nice guy and that would be good enough..."
    L "But sometimes, you just really need a strong man who knows what he wants, you know?"
    if club == "track":
        show chelsea happy
        pcname "I do appreciate confidence..."
    elif club == "cheer":
        pcname "I think I know what you mean..."
    elif club == "yearbook":
        pcname "I guess so...?"
    show chelsea blank
    L "Oh, shoot! It's getting late."
    show chelsea confused
    pcname "It is?"
    L "Keith is letting me leave early today, since..."
    "You're surprised to realize that you never knew the manager's name was Keith."
    $ BM = "Keith"
    L "Since my work is all done. Have a good night, okay?"
    show chelsea happy
    pcname "You too!"
    hide L Blank with moveoutleft
    "She grabs her purse and hurries out the door."
    "After she leaves, you spend the evening working the register; it's a boring night."
    jump events_end_period

label lisa_event3:
    show chelsea at right with moveinright
    show L Happy at left with moveinleft
    "As soon as you enter the bakery, Lisa pops her head around the corner."
    L "[pcname]! Good!"
    L "I have some errands to run for the manager - he had to leave early today."
    L "Keep an eye on the register while I'm gone, please."
    pcname "No problem."
    hide L Happy with moveoutleft
    "You take a look at the stock in the display case, carefully rearranging the muffins to fill in some empty space."
    "As you're finishing, the door opens."
    "First Kid" "Look, Joey!"
    "Two kids dash into the bakery, eagerly pressing their hands to the display case as they peer inside."
    "You wince, knowing you'll have to clean their fingerprints off the glass, but it's hard to be mad when they're so excited."
    "Joey" "Carl! They have cupcakes, Carl!"
    show chelsea happy
    pcname "Do you guys like cupcakes?"
    "Joey and Carl" "Yeah!"
    "Carl" "How much is it for two of them?"
    pcname "Hmmm... Two of the regular sized would be $6."
    "Joey" "Did mom give you enough?"
    "Carl" "Hold on a sec. Let me count..."
    "He lays his money out on the counter slowly, counting out loud as he goes."
    "Carl" "One... Two... Three..."
    "Carl" "Four... Five..."
    "Joey" "That's not enough!"
    "Carl" "Just hold on! I have some change too..."
    "He dumps a handful of change on the counter while Joey dances impatiently around him."
    "Carl" "There's some quarters..."
    "He carefully picks four quarters out of the pile and puts them with his dollar bills."
    "Carl" "That's enough, right?"
    if club == "track":
        pcname "It sure is! Good job!"
    elif club == "cheer":
        pcname "It's perfect."
    elif club == "yearbook":
        "You nod, smiling down at them."
    "Joey" "Cupcakes!"
    "Slipping the money into the drawer, you pull out a box and package their pastries."
    pcname "There you go, guys!"
    "Carl" "Thank you, ma'am!"
    "Smiling at his politeness, you pass them the box as the door swings open."
    pcname "Have a good day, you two."
    "Joey" "You too! C'mon, Carl, let's go!"
    show GHCMan with dissolve
    "A man walks in as they dash towards the door. He smiles at their excitement, but seems quite sad."
    show chelsea blank
    pcname "How can I help you?"
    "Man" "Is Lisa here?"
    show chelsea confused
    pcname "Lisa? Um... No, she's not here right now."
    "Man" "Oh."
    "His shoulders drop and he looks at the floor."
    if club == "track":
        show chelsea happy
        pcname "I can help you though!"
    elif club == "cheer":
        pcname "Is there something I can do for you?"
    elif club == "yearbook":
        pcname "C-Can I help you?"
    show chelsea blank
    "Man" "No, I just..."
    "Man" "Do you know when she'll be back?"
    pcname "She didn't say..."
    "Man" "Okay..."
    "He turns away as if he's going to leave, but turns back suddenly."
    "Man" "Look, I'm her ex-husband and I've been trying to reach her."
    "Man" "Are you sure you don't know when she'll be back?"
    "Surprised, you aren't sure what to say for a moment."
    if club == "track":
        pcname "Honestly? She's been avoiding you."
    elif club == "cheer":
        show chelsea shocked
        pcname "Her ex? Why are you still hung up on her?"
        "Man" "I'm not!"
    elif club == "yearbook":
        show chelsea sad
        pcname "I... I'm sure she's been busy..."
    show chelsea blank
    "He sighs."
    "Man" "We have a mutual friend who's getting married next month."
    "Man" "I just want to know if she's going so I know how to respond to the RSVP."
    "Man" "I... Never mind."
    "Man" "Thank you for your time. I'm sorry to have bothered you at work."
    hide GHCMan with dissolve
    "As he shuffles out the door, you can't help feeling sorry for him."
    if club == "track":
        pcname "He seemed nice. Why wouldn't she just tell him if she's going to the wedding?"
    elif club == "cheer":
        pcname "He didn't seem so bad. She should just text him back so he doesn't show up like that..."
    elif club == "yearbook":
        pcname "Poor guy... It would be easier if she didn't ignore him."
    pcname "It doesn't sound like he really {i}wants{/i} to see her anyway."
    "You feel bad, but it doesn't last long."
    "As more customers come in, you quickly forget about Lisa's ex-husband."
    jump events_end_period


label lisa_event4:
    show L Blank at left with moveinleft
    show chelsea at right with moveinright
    "While you cover the register, Lisa makes pretzels."
    "Watching her, you're a little in awe of how fast she makes them."
    "Taking a ball of dough, she quickly rolls it out into a thick rope, lifts the ends, twists, and sets a fully-formed pretzel on the baking sheet."
    "You watch her make a tray full before you realize you're staring."
    pcname "So what makes pretzels turn brown?"
    show L Happy at left
    L "Oh. That's the next step."
    show L Blank at left
    "She grabs a steaming pot from the stove and sets it next to the baking tray."
    "Lifting a pretzel, she carefully drops it in the hot water."
    "After a few seconds, she uses a wire mesh scoop to lift it out of the water and back onto the tray."
    show chelsea confused
    pcname "What is that?"
    L "It's a lye solution. That's what makes the pretzels turn brown and shiny."
    show chelsea blank
    "As she picks up another pretzel, her phone vibrates on the counter."
    show L Disappoint at left
    L "Ugh. Why doesn't he get the hint?"
    menu lisa_event4_reaction:
        "Tell her about her ex." if True:
            if club == "track":
                show chelsea shocked
                pcname "Oh, I almost forgot to tell you that your ex-husband came by the other day."
                pcname "He was looking for you."
            elif club == "cheer":
                show chelsea confused
                pcname "Is it your ex again? He came here looking for you the other day."
            elif club == "yearbook":
                show chelsea sad
                pcname "Oh... Right... Your ex came by the other day..."
            "She glances toward the office."
            show chelsea blank
            show L Blank at left
            L "He knows he's not welcome here..."
        "Keep quiet." if True:
            pass
    show L Blank at left
    L "I haven't even been reading his texts."
    if club == "track":
        pcname "Maybe you should be more direct?"
    elif club == "cheer":
        pcname "Maybe if you answer him he'll stop?"
    elif club == "yearbook":
        pcname "Maybe it's important?"
    show L Happy at left
    "She laughs."
    show L Question at left
    L "No, he's just hopeless. He wasn't man enough to keep me, so now he just hangs around like a stray dog."
    show chelsea sad
    "You wince at her description; it definitely fits, but it seems so... {i}cruel{/i}."
    show chelsea confused
    pcname "Is he really so bad?"
    show L Blank at left
    "She shrugs."
    show chelsea blank
    L "We were high school sweethearts, actually. Things were good at first, but..."
    L "I had to get a part-time job because he wasn't making enough money."
    L "That's when things started falling apart."
    show chelsea shocked
    pcname "Oh?"
    "As she talks, she continues dipping the pretzels."
    show chelsea blank
    L "I started noticing other men. I wasn't looking to cheat or anything, I just..."
    L "I realized that the things I found attractive in other men were all the things my husband {i}wasn't{/i}."
    L "Confident, commanding... He was a nice guy, but he never made me feel like he was in charge."
    L "And I realized that I {i}like{/i} a man who takes charge."
    if club == "track":
        pcname "I guess I can understand that..."
    elif club == "cheer":
        pcname "Oh, definitely."
    elif club == "yearbook":
        show chelsea sad
        pcname "...oh..."
    show chelsea blank
    L "So I left. Keith let me take on more hours, and I've managed well enough."
    L "Anyway, I need to get these in the oven."
    "As she carries the tray into the back, the door swings open."
    "There's little time for talking after that; you spend the rest of the evening waiting on customers and cleaning up."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
