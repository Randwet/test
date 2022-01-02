label kate_intro:
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "Feeling a little nervous, you walk into the cafe ready to start your first shift!"
    "The cafe is still mostly empty and, though you see one girl waiting tables, nobody seems to notice you."
    show K Casual Happy at left with moveinleft
    K "You're the new girl, right?"
    "You turn to see a young blonde entering the Cafe behind you."
    if club == "track":
        show chelsea happy
        pcname "That's me! I'm [pcname]."
        show K Casual Laugh at left
        K "I'm Kate!"
    elif club == "cheer":
        show chelsea confused
        pcname "I guess so?"
        show K Casual Blank at left
        K "Oh, sorry! I'm Kate!"
        pcname "[pcname]."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "H-Hi..."
        show K Casual Blank at left
        K "Did I surprise you?"
        K "Sorry! My name's Kate!"
        show chelsea happy
        pcname "It's okay. I'm [pcname]."
    show chelsea blank
    if pcname == "Kate":
        K "Really? That's soo cool that we have the same name!"
        K "It'll probably drive Emilia crazy."
        K "And maybe some of the customers who try to remember our names..."
    show K Casual Laugh at left
    K "I'm actually your trainer!"
    show K Casual Blank at left
    K "Did Emilia tell you that? She probably did..."
    K "So, it's your first day..."
    show K Casual Happy at left
    K "Has anyone shown you around yet?"
    K "Is this your first job?"
    show chelsea shocked
    show K Casual Laugh at left
    K "I really like your hair!"
    "Head spinning, you struggle to follow what she's saying."
    show K Casual Blank at left
    "Suddenly her face falls into a cute pout."
    show chelsea blank
    K "Sowwy... I have a habit of talking too much..."
    if club == "track":
        show chelsea happy
        pcname "It's fine. So what should I be doing?"
    elif club == "cheer":
        show chelsea happy
        pcname "That's okay, Kate! I'm just nervous to get started."
    elif club == "yearbook":
        show chelsea sad
        pcname "D-Don't feel bad!"
    show chelsea blank
    show K Casual Happy at left
    "She perks up, smiling again."
    K "Follow me! I'll show you where to change."
    show chelsea shocked
    "Grabbing your hand, she leads you back through the kitchen and into a small room."
    hide K Casual Happy with moveoutleft
    hide chelsea with moveoutleft
    pause 0.5
    show K Casual Happy at left with moveinleft
    show chelsea shocked at right with moveinleft
    K "This is the crew lounge, but since it's only us girls we usually just change in here."
    show chelsea blank
    if club == "track":
        pcname "Like a locker room. Got it."
    elif club == "cheer":
        show chelsea happy
        pcname "Guess I'll have to wear my nice underwear to work..."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "O-oh."
        show K Casual Blank at left
        K "If you're uncomfortable, you can always use the bathroom."
    show chelsea blank
    show K Casual Blank at left
    K "So {i}is{/i} this your first job?"
    pcname "Pretty much. I just moved into an apartment, so..."
    show K Casual Happy at left
    K "Your first apartment? That must be so exciting!"
    menu kate_intro_apartment:
        "I guess so..." if True:
            if club == "track":
                pcname "I guess so...?"
            elif club == "cheer":
                pcname "Yeah, I guess."
            elif club == "yearbook":
                show chelsea sad
                pcname "I... I guess...?"
            show K Casual Blank at left
            K "You're not?"
            K "Oh! When I got my apartment I was so scared living alone..."
        "Not really..." if True:
            if club == "track":
                pcname "No, not really."
            elif club == "cheer":
                pcname "Ugh, no!"
            elif club == "yearbook":
                show chelsea sad
                pcname "Uh... not... Not really."
            show K Casual Blank at left
            K "No?"
            show K Casual Happy at left
            K "I was really excited when I moved into my apartment..."
            show K Casual Blank at left
            K "But... It was scary too..."
        "Yeah, it's great!" if True:
            if club == "track":
                show chelsea happy
                pcname "I love it!"
            elif club == "cheer":
                show chelsea happy
                pcname "It's been awesome."
            elif club == "yearbook":
                show chelsea happy
                pcname "Yeah. It's been nice..."
            show K Casual Blank at left
            K "Do you get nervous living alone?"
            K "I couldn't sleep my first week in my apartment."
    show chelsea blank
    show K Casual Laugh at left
    "She laughs nervously."
    K "Sorry, I'm talking too much again..."
    pcname "It's okay!"
    show K Casual Blank at left
    K "Do you have any questions?"
    menu kate_intro_questions:
        "How's the job?" if True:
            show chelsea happy
            pcname "So how {i}is{/i} working here?"
            K "It's pretty good. You get some handsy customers sometimes, but that's anywhere."
            "She shrugs, giving you a \"What can you do?\" face."
        "How are the other girls?" if True:
            pcname "Are the other girls nice?"
            show K Casual Happy at left
            K "Everyone gets along well, for the most part. It's like a little family!"
            "She shuffles her feet, clearly struggling not to talk more."
        "No, I'm good." if True:
            pass
    show chelsea shocked
    show K Casual Blank at left
    pcname "So we just... change here?"
    show K Casual Laugh at left
    K "Yep! Oh... Shoot!"
    show chelsea blank
    show K Casual Blank at left
    K "We should hurry up and get ready!"
    hide K Casual Blank with fade
    "In seconds, her shorts are on the floor and she's pulling her shirt over her head."
    "Her petite frame makes her look quite young, though you know she must be a few years older than you."
    "And you're amused to see that her underwear for today are black and white--closely resembling the maid uniforms."
    show chelsea shocked
    K "Oh! Your uniform!"
    "She bounces across the room and grabs a stack of clothes."
    show chelsea happy
    K "Emilia said she'd have one ready for you!"
    show chelsea blank
    "Passing the uniform to you, she turns away and starts to dress."
    if club == "track":
        hide chelsea with dissolve
        $ clothes = 'underwear'
        "You quickly do the same; it's a lot like the locker room at school."
        show chelsea at right with moveinright
    elif club == "cheer":
        hide chelsea with dissolve
        $ clothes = 'underwear'
        "You quickly do the same, wishing you'd worn nicer underwear today."
        show chelsea at right with moveinright
    elif club == "yearbook":
        hide chelsea with dissolve
        $ clothes = 'underwear'
        "You hesitantly do the same, wishing you had her confidence."
        show chelsea at right with moveinright
    pause 0.2
    hide chelsea with dissolve
    $ clothes = 'cafe'
    show chelsea at right with moveinright
    "As you finish adjusting your skirt, you notice Kate looking at you."
    show K Happy at left with moveinleft
    K "Alright! Looks like we're ready to get started!"
    K "Today, you'll be shadowing me, so just follow me and I'll explain everything!"
    show chelsea happy
    pcname "I can do that..."
    show K Laugh at left
    "She grins up at you."
    K "This is going to be fun! I think we're going to get along great!"
    "Twirling toward the door, she practically skips back through the kitchen."
    "You follow her around, noting that the customers seem to appreciate her cheerful demeanor and energetic personality."
    "But they don't tip her nearly as well as the more flirty maids."
    "Still, she's a great trainer and before you leave, she suggests you exchange phone numbers in case you need anything!"
    $ chelseaContacts.contactsListed["Kate"] = "Kate"
    hide K Laugh with dissolve
    hide chelsea with dissolve
    jump events_end_period

label kate_picked_on:
    "As you head back to the crew lounge to get ready, you hear laughter."
    show chelsea at right with moveinright
    show K Sad at left with moveinleft
    show Harper Laugh with dissolve
    show Emma Laugh at midleft with dissolve
    show Zoey Laugh at midright with dissolve
    "Emma" "My little sister is taller than you and she's in elementary school!"
    "There are three girls standing near the corner. You can't see who they're talking too, but they're all laughing."
    "Harper" "It's like you never hit puberty at all. Why do you bother wearing a bra?"
    "As they break into another fit of laughter, you see Kate standing in front of them."
    "Her face has fallen into her typical pout."
    "Zoey" "And she still pouts like a baby too!"
    "Emma" "Do the baby voice now!"
    "Harper" "\"Sowwy!\""
    show K Laugh at left
    "They laugh at her imitation of Kate, who laughs along with them."
    K "That's not how I sound!"
    "Zoey" "It is! You do that all the time!"
    "Kate laughs even louder, waving them off."
    "Emma" "Okay, okay. If you tease her too much she'll tell her mommy!"
    K "I will not! Take it back!"
    "Still laughing, they turn your way."
    show K Sad at left
    show Harper Neutral
    "Harper" "Sorry, [pcname], we have to go clock out."
    show Emma Happy
    show Zoey Happy
    "You step out of the doorway to let them out of the lounge."
    hide Zoey with moveoutright
    hide Harper with moveoutright
    hide Emma with moveoutright
    "As they file out, you notice that Kate's face has fallen. She's not laughing anymore."
    menu kate_picked_on_response:
        "Cheer up, Kate!" if True:
            if club == "track":
                show chelsea happy
                pcname "Don't let them get to you!"
            elif club == "cheer":
                show chelsea happy
                pcname "Aww, cheer up, Kate!"
            elif club == "yearbook":
                show chelsea sad
                pcname "It's okay, Kate..."
        "You shouldn't let them talk to you like that!" if True:
            if club == "track":
                show chelsea sad
                pcname "I can't believe you let them talk to you like that..."
            elif club == "cheer":
                show chelsea angry
                pcname "Those girls weren't very nice. You should stand up for yourself!"
            elif club == "yearbook":
                show chelsea sad
                pcname "I know it's hard, but..."
                pcname "You should tell them not to say things like that."
    show K Laugh at left
    show chelsea blank
    "She grins and waves you off."
    K "Oh, no, we were just having fun!"
    show K Blank at left
    K "Besides; I really do look like a little kid!"
    show K Laugh at left
    K "Customers tell me that all the time!"
    "She laughs, mimicking them."
    K "\"Are you sure you're old enough to work here?\""
    show K Sad
    K "\"Shouldn't you be in school, little girl?\""
    show K Happy at left
    K "I'm used to it, you know?"
    "Her smile looks forced, but she clearly wants you to believe she's okay."
    menu kate_picked_on_reassure:
        "I think you're cute!" if True:
            if club == "track":
                show chelsea happy
                pcname "That's okay; I think you're cute!"
            elif club == "cheer":
                show chelsea happy
                pcname "Awww, I like how you look! You're so {i}cute{/i}!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I think you're cute, though..."
            show K Laugh at left
            K "Awww, thanks, [pcname]!"
        "If you're sure..." if True:
            if club == "track":
                pcname "I don't like it, but if you're sure you're okay..."
            elif club == "cheer":
                pcname "I can't complain if it doesn't bother {i}you{/i}, I guess."
            elif club == "yearbook":
                pcname "I guess it's fine if you don't mind..."
            K "I'm great! You don't have to worry about me!"
    show K Embarrassed at left
    show chelsea sad
    K "Oh no! If they're clocking out, that means we're going to be late!"
    "Kate rushes out the door and you hurry to change."
    hide K Embarrassed with moveoutleft
    hide chelsea with moveoutright
    jump events_end_period

label kate_ice_cream:
    "You clock in and start waiting tables."
    "As you deliver omelette rice topped with hearts drawn in ketchup, you notice Kate struggling with a heavy tray."
    show chelsea confused at right with moveinright
    pcname "Kate, are you okay?"
    show K Blank at left with moveinleft
    K "Uhhh..."
    show chelsea blank
    "The arms wobble under the tray, which tips from side to side."
    show K Laugh at left
    K "Maybe?"
    show K Blank at left
    "Her typical pout belies her words and you step closer to help."
    show chelsea happy
    pcname "How about I take this side..."
    "Grabbing one side of the tray, you hold it steady as she changes her grip."
    pcname "...and you take that one?"
    show K Happy at left
    K "Thanks, [pcname]!"
    show K Blank at left
    "Moving carefully, you each carry one side of the tray over to a table of college-aged guys."
    "Customer" "Wow, look--we ordered so much stuff that we got another maid!"
    show K Happy at left
    K "Oh, Master! There's just too many of you for me to serve by myself!"
    "Sitting the tray on a nearby table, you watch as Kate cheerfully serves the group."
    show K Laugh at left
    "Giggling at their jokes, blushing as if on cue..."
    "She's adorable!"
    show K Happy at left
    K "Now, may I put a charm on your food to make it {i}extra{/i} delicious, Masters?"
    "As she makes a heart shape with her hands and waves it around, you realize you should get back to your own customers."
    hide chelsea with moveoutright
    hide K Happy with fade
    pause 0.2
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "Later, as you're getting ready to leave, Kate approaches you."
    show K Casual Happy at left with moveinleft
    K "Hey, [pcname]! I didn't get a chance to thank you!"
    K "You really saved me!"
    show K Casual Laugh at left
    K "That tray was sooooooooo heavy!"
    show K Casual Happy at left
    K "Oh! I know! Come get ice cream with me; my treat!"
    show chelsea happy
    if club == "track":
        pcname "I think we've earned it!"
    elif club == "cheer":
        pcname "I really shouldn't but... Okay!"
    elif club == "yearbook":
        pcname "That would be really nice... Thanks!"
    show K Casual Laugh at left
    K "Yay!!!"
    "She bounces ahead, turning to face you as she reaches the doorway."
    show chelsea blank
    show K Casual Happy at left
    K "There's a little place not far from here!"
    show chelsea happy
    if club == "track":
        pcname "Wanna race?"
        show K Casual Blank at left
        K "Oh! No way..."
        show K Casual Laugh at left
        K "Even if you weren't on the track team, I'm way too clumsy!"
    elif club == "cheer":
        pcname "Lead the way!"
    elif club == "yearbook":
        "Her smile is contagious; you find yourself grinning back at her."
    show chelsea blank
    show K Casual Laugh at left
    "Hooking her arm in yours, she pulls you out the door and down the sidewalk."
    hide chelsea
    hide K Casual Laugh
    show bg CityE with fade
    show K Casual Blank at left with moveinleft
    show chelsea at right with moveinright
    K "This place is great; I love stopping by on my way home!"
    K "It's probably good that I walk so much, now that I think about it..."
    K "Though, maybe I should cut back a little..."
    show K Casual Laugh at left
    "She laughs, glancing your way."
    menu kate_ice_cream_lookinggood:
        "Compliment her." if True:
            if club == "track":
                show chelsea happy
                pcname "You look great!"
            elif club == "cheer":
                show chelsea happy
                pcname "I wish I could eat like that and look like you!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I think you look good..."
        "Laugh with her." if True:
            show chelsea laugh
            "Unsure of what to say, you laugh along with her."
    show chelsea blank
    show K Casual Blank at left
    K "So how was work tonight? I had an {i}awful{/i} customer before you got there."
    K "He complained about {i}everything{/i}. His food was too hot. His water was too cold..."
    "She sighs."
    show K Casual Sad at left
    K "It's hard to keep smiling sometimes, you know?"
    menu kate_ice_cream_meancust:
        "I know what you mean." if True:
            if club == "track":
                pcname "I know what you mean. It's tough to be positive all the time."
            elif club == "cheer":
                pcname "I have to smile so much between work and cheerleading that I think my lips are going to fall off!"
            elif club == "yearbook":
                show chelsea sad
                pcname "I know... When they're mean, I just want to hide..."
            K "Exactly!"
        "I'm used to it." if True:
            if club == "track":
                pcname "I guess I'm just used to it..."
            elif club == "cheer":
                pcname "I have to do it for cheerleading; so I'm pretty used to it."
            elif club == "yearbook":
                pcname "It was hard at first, but I've gotten used to it..."
            K "You're so good at everything..."
    show chelsea blank
    show K Casual Happy at left
    K "Oh, we're here!"
    "She pulls you into a nearby building before you can get a good look at the exterior."
    show bg DatePlace with dissolve
    "Inside, there are several tables. A menu board hangs above the counter, where an older man waits."
    show GHCMan with dissolve
    "Cashier" "Kate! Nice to see you again!"
    show K Casual Laugh at left
    K "I told you I come here a lot..."
    "Giggling, she pulls you to the counter."
    "Cashier" "Mudslide sundae with extra fudge?"
    show K Casual Blank at left
    K "You know me! And whatever [pcname] wants too."
    "Cashier" "You got it! What can I get you, miss?"
    menu kate_ice_cream_order:
        "A vanilla cone." if True:
            pcname "A vanilla cone, please."
            $ order = "cone"
        "A caramel sundae." if True:
            pcname "A caramel sundae, please."
            $ order = "sundae"
        "A strawberry milkshake." if True:
            pcname "A strawberry shake, please."
            $ order = "shake"
    "Cashier" "Okay, then... That's $6.50."
    "Kate pays him and grabs some napkins. By the time she's done fighting the napkin dispenser, your order is ready."
    "Cashier" "I don't know, Kate... I think the napkins are winning. Here..."
    "He pulls some napkins free and passes them to her."
    show K Casual Laugh at left
    K "Thanks..."
    show chelsea laugh
    if club == "track":
        pcname "I got the tray."
    elif club == "cheer":
        pcname "Maybe I should get the tray?"
    elif club == "yearbook":
        pcname "I can carry the tray, if you want..."
    show K Casual Happy at left
    K "That might be for the best."
    hide GHCMan with dissolve
    hide chelsea laugh dissolve
    "You find a table and sit the tray down, passing her sundae to her."
    scene bg KDScene3 with dissolve
    K "It looks so good... So does yours!"
    if order == "cone":
        K "I never get a cone. All the sundaes and shakes look too good, but I really like waffle cones..."
    elif order == "sundae":
        K "Maybe I'll get caramel next time too..."
    elif order == "shake":
        K "I usually get chocolate shakes, though."
    "For a few minutes, you both quietly eat your desserts."
    scene bg KDScene1 with dissolve
    K "[pcname], I know I already thanked you for earlier, but..."
    "She shifts nervously in her chair."
    K "I guess... I just want to thank you for being so nice to me all the time..."
    if club == "track":
        pcname "We're friends! Of course I'm nice to you!"
    elif club == "cheer":
        pcname "That's what friends {i}do{/i}, isn't it?"
    elif club == "yearbook":
        pcname "O-Of course I'm nice... We're friends. Aren't we?"
    K "Right. It's just..."
    K "I've always had a hard time making friends, I guess."
    pcname "What? But you're always so nice!"
    K "I don't know why, really. I try to be nice to everyone, but..."
    scene bg KDScene2 with dissolve
    K "I'm not really confident, you know? And I have trouble telling people no, so..."
    "She looks down, staring at the table."
    K "Most of the time I feel like people only like me because I'm so easy to take advantage of."
    pcname "What do you mean?"
    scene bg KDScene1 with dissolve
    K "Like Emma. We used to be really close..."
    K "But then I realized that she only texts me outside of work when she needs to borrow money."
    pcname "Oh, Kate..."
    if club == "track":
        pcname "You can't let people treat you that way."
        pcname "You have to start standing up for yourself!"
    elif club == "cheer":
        pcname "You don't need people like that!"
        pcname "From now on, you need to start telling them no!"
    elif club == "yearbook":
        pcname "I know it's hard, but..."
        pcname "You should try to be more confident."
    K "I... I know you're right, but..."
    K "I hate letting people down..."
    pcname "It's not fair to you, though."
    "Her eyes dart back up to your face."
    K "You're right, but... I'll try, okay?"
    scene bg KDScene3 with dissolve
    "You nod, smiling. She smiles back."
    K "You really are a good friend. Thanks again!"
    "You finish your [order] feeling good about the conversation."
    K "That was good..."
    K "I guess I'll see you at work, then?"
    pcname "Yep! Thanks for the ice cream!"
    K "We should do it again sometime..."
    pcname "Definitely!"
    scene bg black with dissolve
    jump events_end_period


label kate_stands_up:
    show chelsea at right with moveinright
    "While you're talking to a customer, a sudden movement catches your attention."
    show K Blank with moveinleft
    "You turn just in time to see Kate trip on her own foot, spilling coffee all over a customer's table."
    hide K Blank with moveoutleft
    "She quickly cleans it up and hurries back to the kitchen."
    "As soon as you have a chance, you head into the kitchen to see if she's okay."
    show K Sad with dissolve
    show Emma Laugh at midleft with dissolve
    show Zoey Laugh at midright with dissolve
    "Emma and Zoey are standing on either side of her as she fills a new coffee cup."
    "Emma" "Clumsy Kate spills another one!"
    "Zoey" "How can someone be {i}that{/i} clumsy anyway?"
    show K Laugh at left with moveinleft
    "Though she's trying to laugh it off, you see the tears welling in her eyes."
    "Just as you're trying to decide what to say, Kate looks up and sees you standing there."
    show K Sad at left
    "As your eyes meet, she draws herself up and takes a deep breath."
    show K Mad at left
    K "That's enough. I don't appreciate being teased like this all the time."
    show Emma Worried
    show Zoey Worried
    K "So if you don't have anything nice to say, just leave me alone."
    "Emma" "Oh, Kate, don't take it so personally."
    "Zoey" "Yeah, we were just joking around."
    "Her lips quiver, but she stands her ground."
    K "I understand that you think it's funny, but picking on people is hurtful and unkind."
    show K Sad at left
    K "And I... I would appreciate it if you wouldn't do it anymore. Please."
    show Emma Angry
    "Emma" "Ugh, fine. You don't have to be so serious about it!"
    show Zoey Neutral
    show Emma Blank
    "Zoey" "Yeah, we didn't mean anything. Sorry."
    show Zoey Blank
    hide Emma Blank with moveoutleft
    hide Zoey Blank with moveoutleft
    "As the girls walk away, Kate lets out the breath she was holding and rushes to you."
    show K Happy at left
    K "Did you see that!?"
    show chelsea happy
    if club == "track":
        pcname "That was great!"
    elif club == "cheer":
        pcname "Good job!"
    elif club == "yearbook":
        pcname "That was very brave of you..."
    pcname "I'm glad you stood up for yourself!"
    show K Laugh at left
    K "I... I am too, actually."
    show K Happy at left
    K "I was so scared they would be mad at me, but I'm glad I did it."
    show K Blank at left
    K "I have to take this coffee out. I'll talk to you later, okay?"
    "You smile as she rushes out--almost tripping again in her haste."
    hide K Blank
    hide chelsea
    jump events_end_period


label kate_friendship_end:

    "As you're leaving work, Kate approaches you."
    show chelsea at right with moveinright
    show K Casual Sad at left with moveinleft
    K "Hey, I... I wanted to talk to you."
    K "The other day, I was really upset and..."
    if club == "track":
        pcname "And mean?"
    elif club == "cheer":
        pcname "And rude?"
    elif club == "yearbook":
        pcname "And?"
    K "I just..."
    K "I thought we were friends, but you keep doing all of these things with customers."
    K "Things that you told me {i}not{/i} to do."
    K "And I realized how hypocritical that is."
    if club == "track":
        pcname "You're just too sweet to act like that, Kate."
    elif club == "cheer":
        pcname "You're too nice, Kate. That's what I like about you."
    elif club == "yearbook":
        pcname "It's just that... I like you the way you are."
    K "See, that's just it!"
    "She continues, despite the tears slowly filling her eyes."
    K "For a while, I thought you were perfect; I wanted to be just like you."
    K "But you taught me to be confident and I..."
    K "I realized that I {i}don't{/i} want to be like that."
    K "And I don't want to be friends with someone like that."
    show chelsea sad
    pcname "Kate..."
    "Shaking her head, she wipes the tears from her cheeks."
    K "I'm sorry; I just can't be friends with you anymore."
    "Grabbing her coat, she flees before you have a chance to respond."
    hide chelsea
    hide K Casual Sad
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
