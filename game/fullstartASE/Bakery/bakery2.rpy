label bakery_study:
    show chelsea at right with moveinright
    "You arrive to work a little earlier than usual."
    "As you prepare for your shift, you think about the test coming up in your class. You glance at the time on your phone."
    show chelsea happy
    pcname "I guess I have a little time to study..."
    hide chelsea with moveoutright
    show chelsea at right with moveinright
    "After changing into your uniform, you take a seat near the back and open up your textbook."
    "As you begin to take notes, you hear someone clear their throat beside you."
    show Keith Neutral at left with moveinleft
    show chelsea shocked
    BM "What the hell do you think you're doing?"
    show Keith Blank at left
    show chelsea confused
    "You glance up at Keith. He glares down between you and your books with utter disdain."
    "You can't imagine what's gotten him in such a terrible mood."
    show chelsea blank
    pcname "I was just doing some homework."
    "You tilt your notebook in his direction so he can see your notes. Keith scoffs."
    show Keith Angry at left
    BM "You aren't getting paid to study. You're getting paid to work!"
    if intelligence >= 20:
        show chelsea confused
        pcname "I haven't even clocked in yet."
        show chelsea blank
        "You glance at the time on your phone, hoping you haven't lost track of time."
        pcname "I don't start for another twenty minutes."
        show Keith Confused at left
        "If it throws him off, it's only for a moment before Keith composes himself, finding another excuse."
        show Keith Blank at left
    elif True:
        show chelsea sad
        "You shrink a little in your seat. Even if you haven't clocked in, you consider what it must look like to have a uniformed employee sitting in the middle of the bakery."
    BM "If you have time to be reading your books, you ought to be using it to clean yourself up a little."
    BM "We have expectations here. You're better off making yourself look presentable, because that brain of yours isn't going to get you anywhere."
    show chelsea shocked
    menu bakery_talkback:
        "Talk back." if True:
            "You're so stunned by his harsh insult that you almost aren't sure what to say."
            if club == "track":
                show chelsea angry
                pcname "Excuse me? You can't talk to me like that!"
            elif club == "cheer":
                show chelsea happy
                pcname "I don't know what you mean. Maybe I'm too stupid to understand."
                "Your words come out sarcastic and bitter."
            elif club == "yearbook":
                show chelsea sad
                pcname "Th-That isn't okay for you to say!"
            BM "Watch that attitude of yours, [pcname]. You're on thin ice around here."
            hide Keith Angry with moveoutleft
            "Keith storms back to his office, slamming the door behind him."
            $ bakeryagree -=1
        "Apologize." if True:
            $ corruption += 2
            "You're so stunned by his harsh insult that you almost aren't sure what to say."
            show chelsea sad
            pcname "I'm sorry..."
            show Keith Blank at left with dissolve
            "Keith takes a breath, his angry expression relaxing slightly."
            show Keith Neutral at left
            BM "You're part of our team, [pcname]. We want what's best for you."
            hide Keith Neutral with moveoutleft
            "Keith walks back off to his office, shutting the door behind him."
            $ bakeryagree +=1
    show chelsea blank
    "You try to refocus on your textbook, but you can't seem to get into it anymore. You close your textbook, dejected."
    show L Blank at left with moveinleft
    "Lisa walks up to you from around the counter."
    show L Happy at left
    L "You're here early, [pcname]."
    pcname "Yeah."
    if club == "track":
        "You toss your textbook in your bag, irritated."
        pcname "I was going to study, but Keith threw a fit. He said I should 'focus on my looks, because my brain won't get me anywhere.'"
        show chelsea angry
        pcname "Can you believe he said that?"
    elif club == "cheer":
        "You set your books aside, bitter."
        pcname "Well, I was going to do some homework, but Keith said I should be using my time to focus on my looks instead of my brains."
        "You look down at your uniform. There isn't anything out of place with it, which only infuriates you further."
        show chelsea angry
        pcname "There's nothing wrong with me. I look fine."
    elif club == "yearbook":
        show chelsea sad
        pcname "Well, I was going to study... But Keith..."
        "You glance down at your uniform. It looks perfectly fine."
        pcname "He said I should focus more on my looks, because my brain isn't going to get me anywhere."
        pcname "B-But that's not true... I thought I looked fine..."
    show L Blank at left
    "Lisa sighs, leaning on a chair opposite from you."
    show L Disappoint at left
    show chelsea blank
    L "He has a point..."
    menu bakery_upset:
        "What's that supposed to mean?" if True:
            show chelsea angry
            show L Happy at left
            "Lisa holds her hands up in defense, but you can see the annoyance clear on her face."
            L "I'm just saying. It's okay to not be smart. There are plenty of girls out there that get by on their appearance."
            show L Blank at left
            $ bakeryagree -=1
        "What do you mean?" if True:
            show chelsea confused
            show L Blank at left
            "Lisa steps beside you, pressing a comforting hand over your shoulder."
            show L Happy at left
            L "Not everyone is smart, [pcname]. And that's okay. There are plenty of girls out there that get by just on appearances."
            $ bakeryagree +=1
    L "It's nothing to be ashamed of."
    show chelsea blank
    show L Happy at left
    L "At least, Keith thinks you're pretty enough to get ahead that way. Don't you think so?"
    menu bakery_looks:
        "I don't care what Keith thinks." if True:
            if intelligence >= 40:
                show chelsea angry
                pcname "I'm proud of my grades. Keith doesn't know what he's talking about."
            elif intelligence >= 30:
                pcname "I'm doing well in school. I want to keep it up."
            elif intelligence >= 20:
                "Even if your grades aren't the best, you don't want to give Keith the satisfaction of being right."
            elif True:
                show chelsea sad
                "Although you're tempted by Lisa's suggestion, you refuse to let them know how horribly you're struggling in school."
            show chelsea blank
            "You reopen your textbook and begin to jot down notes."
            show L Disappoint at left
            "Lisa sighs, shaking her head."
            L "I'm only trying to help you, [pcname]. It'd be a lot easier on all of us if you weren't so stubborn..."
            "She turns on her heel and returns to work."
            hide L Disappoint with moveoutleft
            $ bakeryagree -= 1
            $ intelligence += 3
            jump events_end_period
        "I guess so..." if True:
            "Lisa smiles and gives your shoulder an encouraging squeeze."
            L "See? Now let's put these books away. I'll help do your hair before you need to clock in."
            show chelsea embarrassed
            "You bite your lip and nod, tossing your books back into your bag before following Lisa into the back room."
            if intelligence >= 40:
                show chelsea sad
                "You feel horrible about skipping out on your studies and make a mental note to study as soon as you get home."
            if intelligence >= 30:
                "You're a little reluctant about skipping out on your studies, but one bad grade isn't the end of the world, right?"
            if intelligence >= 20:
                show chelsea sad
                "You don't feel great about skipping out on your studies, but you can't deny that Keith has certainly treated you better when you put your looks first."
            elif True:
                "Your grades haven't been that great anyway. Missing out on some studying isn't going to make that much of a difference."
            show chelsea happy
            "Lisa braids your hair in the back room, and all thoughts of studying are gone when Keith, as well as a few customers, compliment your appearance throughout your shift."
            "Maybe you {i}can{/i} just get by on looks..."
            $ bakeryagree += 1
            $ lisa_agree = True
            $ corruption += 1
            $ intelligence -= 3
            scene bg black with dissolve
            jump events_end_period

label bakery_test:
    "You arrive to work earlier than usual."
    "As you begin to change in the dressing room, a sudden thought hits you."
    show chelsea shocked
    pcname "Crap! I have a test tomorrow!"
    "You've been so busy, you completely forgot!"
    hide chelsea with moveoutright
    show chelsea at right with moveinright
    "You quickly finish putting on your uniform and carry your backpack out to a seat in the back of the bakery."
    "As you begin to set up your textbook on the table, you pause, recalling what Keith and Lisa said the last time you tried to study before work."
    if lisa_agree == True:
        pcname "Get by on my looks, huh..."
    elif True:
        show chelsea embarrassed
        pcname "But Keith was so angry last time..."
    menu bakery_looks2:
        "Study." if True:
            show chelsea blank
            "You shake your head and pull out your notebook."
            show chelsea happy
            pcname "I need to do well on this test."
            if intelligence >= 40:
                "If you want to keep up your perfect grades, you need to study consistently."
            elif intelligence >= 30:
                "If you want any chance of improving your grades, you need to study hard."
            elif intelligence >= 20:
                "If you want any chance of passing your classes, you need to study."
            elif True:
                "Despite your horrible grades, you don't actually want to keep failing your classes, right?"
            "You set an alarm on your phone and jump straight into studying."
            show Keith Blank at left with dissolve
            "As you work, you catch a glimpse of Keith watching you from behind the counter. He shakes his head in disappointment."
            show Keith Neutral at left
            BM "You're wasting your own damned time, [pcname]. You should quit while you're ahead."
            show Keith Blank at left
            hide Keith Blank with moveoutleft
            "He walks off into his office. You try to put his comment out of your mind as you prepare for the test."
            $ bakeryagree -= 1
            $ intelligence += 5
            scene bg black with dissolve
            jump events_end_period
        "Put textbooks away." if True:
            $ corruption += 2
            show chelsea blank
            "You consider Keith and Lisa's suggestion and stuff your textbook back into your bag."
            if intelligence >= 20:
                "The test is tomorrow, anyway. It's not like you could study efficiently for it."
            elif True:
                "Your grades haven't been that great to begin with. Skipping out on one test isn't going to make that much of a difference."
            show Keith Blank at left with dissolve
            "You catch a glimpse of Keith watching you put away your homework from behind the counter. As he approaches, you fully expect him to criticize you for bringing your homework to work again."
            show Keith Neutral at left
            BM "Ah, [pcname]. I almost forgot."
            show Keith Blank at left
            show chelsea shocked
            "He holds out a $50 bill. You stare at it, dumbfounded."
            show Keith Happy at left
            BM "Consider it a bonus. You've been doing a good job lately. I hope you keep up the good work."
            "You hesitantly take the money from his hand, almost not sure of what to say."
            show chelsea embarrassed
            pcname "Ah... Thank you."
            hide Keith Happy with moveoutleft
            "Keith nods in approval before returning to his office. You stare at the $50 in your hands, surprised."
            pcname "Usually he's so mean..."
            show chelsea happy
            "You smile, tucking the money into your apron. Maybe you're doing something right after all."
            $ Cash += 50
            $ bakeryagree += 1
            $ intelligence -= 5
            scene bg black with dissolve
            jump events_end_period

label bakery_muffins:
    "You head into work and get changed in the back."
    show chelsea at right with moveinright
    "As you step out to the front and clock in, you notice a businessman yelling at Lisa over the counter."
    show GHCMan with dissolve
    show L Sad at left with moveinleft
    "Muffin Man" "Look at it! {i}Look{/i} at this shit! I paid for a dozen muffins! And there are {i}eleven{/i}!"
    show chelsea shocked
    "Muffin Man" "Are you fucking stupid?!"
    "The man slams the box of muffins down on the counter. From over Lisa's shoulder, you count twelve muffins."
    show chelsea confused
    L "Are there, sir? Oh no! I'm so sorry. I've messed up again..."
    "Muffin Man" "This happens every time I come in here! Don't any of you know how to count?! Are you bred stupid? Huh? Does your boss just pick you off a fucking idiot farm?"
    L "Yes, sir. I'm so sorry. I wasn't paying attention."
    "Muffin Man" "Clearly! It's your job to pay attention! You fucking moron!"
    L "I know, sir. I'm so stupid sometimes. Really, I don't mean to be. I just can't help it."
    L "Please, let me make it up to you."
    "The man considers this. He looks Lisa over skeptically, almost as if she'll rescind her offer."
    "Muffin Man" "You better make it up to me."
    L "Of course, sir."
    "Lisa gives an apologetic bow and hurries to the case of muffins, nudging you out of the way. You try to whisper to her."
    pcname "What's going on? I counted the muffins, there's definitely-"
    show chelsea shocked
    show L Disappoint at left
    L "Hush!"
    show chelsea blank
    show L Blank at left
    "Lisa shushes you quickly. She digs in the case, pulling out another muffin as well as a few more expensive specialty cupcakes."
    "She rushes back over to the gentleman and places the muffin in the box before boxing up the cupcakes."
    show L Sad at left
    L "I'm so sorry again, sir. I just don't know what goes on in my brain sometimes."
    show chelsea confused
    "As she says this, you notice her arms press her cleavage together a little bit more. The businessman notices, too."
    "Muffin Man" "Right. Well, we all make mistakes."
    show chelsea blank
    show L Happy at left
    L "Please, take some of these. They're on the house."
    "She gives the man a little wink, offering the specialty cupcakes."
    L "Thank you for letting me know about my mistake, sir. I hope it didn't ruin your day."
    "Muffin Man" "No. Just remember next time."
    show chelsea confused
    "The businessman takes the boxes of muffins and cupcakes and leaves, definitely happier than when you had first seen him."
    "Confused, you approach Lisa."
    pcname "What was that about?"
    show L Blank at left
    "Lisa shrugs, writing down the cupcakes on a nearby waste sheet."
    L "Nothing, really. He comes in here all the time. He likes to say I messed something up just so he can yell at me for it."
    show chelsea shocked
    "Your jaw drops."
    if club == "track":
        show chelsea angry
        pcname "And you let him get away with it?!"
    elif club == "cheer":
        show chelsea angry
        pcname "What an asshole!"
    elif club == "yearbook":
        show chelsea sad
        pcname "That- That's horrible!"
    show L Happy at left
    L "Really, [pcname], it's fine. It's not that big of a deal."
    L "If it makes him feel better, I don't see a real problem with it. After all, he leaves a happy customer, doesn't he?"
    show L Blank at left
    show chelsea blank
    L "I don't mind acting a little bit dumber if it helps improve our business."
    menu bakery_dumb:
        "I don't think I could let someone treat me that way..." if True:
            if club == "track":
                "You don't want to admit it, but you have too much pride to stand being treated that way."
            elif club == "cheer":
                show chelsea angry
                pcname "I don't care how happy he is. I'm not an object to yell your insecurities at."
            elif club == "yearbook":
                show chelsea sad
                pcname "It's just so mean... You should never treat someone so horribly, no matter the reason."
            show L Disappoint at left
            "Lisa sighs, rolling her eyes."
            show chelsea blank
            L "You're completely missing the point. If you want to keep working here, you'll need to accept that a customer's happiness is more important than your ego."
            "Shaking her head, Lisa leaves to clean one of the sinks in the back."
            hide L Disappoint with moveoutleft
            "You watch her go, trying to wrap your head around her suggestion."
            $ bakeryagree -=1
            jump events_end_period
        "Well, if it's helping business..." if True:
            $ corruption += 1
            show L Happy at left
            "Lisa grins."
            L "See? It's really not so bad after all."
            L "After all, a customer's happiness is more important than our egos. Don't you think?"
            pcname "Yeah... I guess you're right. I never really thought about it that way before."
            show chelsea happy
            "Lisa presses a hand on your shoulder and gives an encouraging squeeze. You smile back up at her."
            L "You're learning so much already. You'll go far with this kind of attitude."
            "Pleased with the compliment, you take your place behind the register, giving Lisa a break to go clean some of the baking equipment."
            "You'll have to remember her advice the next time you deal with a difficult customer."
            $ bakeryagree +=1
            scene bg black with dissolve
            jump events_end_period

label bakery_actdumb:
    show chelsea shocked at right with moveinright
    show L Happy at left with moveinleft
    "The bakery is surprisingly busy today as you start your shift."
    "You rush between the counter and the customers, delivering out baked goods as fast as you can while Lisa rings them up."
    "Keith pops his head out from his office."
    show Keith Neutral with dissolve
    BM "Lisa. Meeting. Now."
    show Keith Blank
    hide Keith Blank with dissolve
    show chelsea blank
    "Keith disappears back into his office, ignoring the chaos of the bakery."
    show L Blank at left
    L "Oh-Yes, right. I'll be right there."
    show L Happy at left
    "Lisa throws on a smile as she finishes ringing up an elderly woman."
    L "Ah- Thank you, ma'am, please come again."
    L "[pcname]."
    "You finish handing off a cake to a waiting customer before turning to Lisa."
    show L Blank at left
    L "I have a meeting with Keith. Can you man the register for a while?"
    "You glance back at the waiting line of customers. It's pretty long..."
    menu bakery_anothertime:
        "Sure." if True:
            show chelsea happy
            pcname "Yeah, I can do that."
            show L Happy at left
            L "Thanks, [pcname]!"
            hide L Happy with moveoutleft
            $ bakeryagree +=1
        "Can't you reschedule for another time?" if True:
            show chelsea confused
            show L Disappoint at left
            "Lisa gives you an irritated look."
            L "No, I can't. Why can't you just do what you're told?"
            show chelsea blank
            pcname "It's just that we're pretty busy..."
            L "Ugh. Just take care of the register. I'll be right back."
            hide L Disappoint with moveoutleft
            $ bakeryagree -=1
    "You hurry behind the register as Lisa pops into Keith's office and shuts the door."
    show chelsea blank
    show GCBoy at left with moveinleft
    "Line Guy" "Hey, what's the hold up?!"
    "You can already hear people murmuring their impatience from the back of the line."
    show chelsea happy
    "A group of teenagers right out of school wait behind the counter. You smile politely and begin to work through the line as quickly as you can."
    "A lot of the customers your age seem to give you an easier time. One even compliments you for the hard work you've done by yourself!"
    pcname "Thank you so much! Please come again!"
    "It takes a little while to box everything up accordingly, but you manage to get through the line relatively quickly."
    "Line Guy" "What was the hold up? C'mon, I've been waiting almost an hour here!"
    "A lot of the older customers, however, have been less patient."
    pcname "I'm so sorry. Here's your bagels, sir."
    hide GCBoy with moveoutleft
    "You pass him over a paper bag with his bagels. He grumbles, but walks off."
    "You plaster on a fake smile and work through it."
    pcname "I'll take the next guest here, please!"
    show GHCMan at left with moveinleft
    "Muffin Man" "Who the hell let you on a register alone?"
    show chelsea blank
    "You frown as you recognize Lisa's troublesome customer step up to the counter."
    show chelsea happy
    pcname "What can I get for you today, sir?"
    "Muffin Man" "Dozen blueberry muffins. And make it quick, sweetheart, I have a meeting to go to."
    pcname "Yes, sir. Right away."
    show chelsea blank
    "You walk over to the case of muffins and carefully select twelve blueberry muffins. You even count them twice to make sure it's correct."
    "Muffin Man" "What the hell are you doing over there? I said I was in a rush, I'm in a rush! What, you don't know how to count?"
    show chelsea happy
    "You bite back a remark and set the box on the counter in front of him, a smile plastered on your face."
    pcname "That'll be fifteen dollars, sir."
    "The businessman flips open the box, the lid landing with a loud {i}smack{/i} against the counter."
    "Muffin Man" "The hell you take me for?!"
    show chelsea confused
    pcname "Pardon?"
    "Muffin Man" "There's only eleven in here! What the fuck!"
    show chelsea happy
    pcname "There must be some mistake, sir. I definitely counted twelve-"
    "Muffin Man" "Are you trying to argue with me?! Look! {i}Look!{/i} Count these! There are {i}eleven{/i}, you stupid slut!"
    show chelsea angry
    pause 1.0
    show chelsea blank
    "As you open your mouth to argue, you recall what Lisa did to appease him last time."
    menu bakery_actdumb2:
        "Act Dumb." if True:
            $ corruption += 2
            "Well, if it worked for Lisa..."
            "You take your time counting the muffins aloud."
            show chelsea sad
            pcname "Seven... eight... ten..."
            "Muffin Man" "You skipped nine! See what you just did there? You skipped nine!"
            show chelsea shocked
            "You bat your eyes, your lips falling into an open 'o' of shock."
            pcname "Did I really, sir?"
            show chelsea sad
            "Muffin Man" "Yes, you idiot! No wonder you can't get shit right. You can't even count to ten!"
            pcname "Oh, sir, I'm so sorry, sir. You're right. I can't do anything right."
            "The businessman nods, looking smug and satisfied."
            "Muffin Man" "Clearly! Now get me my other muffin!"
            show chelsea happy
            pcname "Of course, sir. I hope you'll forgive me. I don't know where my brain is sometimes."
            "You grab another muffin from the case and place it in his box, struggling to put the lid on top."
            "Muffin Man" "Give me that."
            "The businessman grabs your tape dispenser from over the counter and tapes the lid shut. You put on a show of amazement."
            pcname "Wow, sir, you're so smart!"
            pcname "Is there anything else I can do for you to make up for my stupidity?"
            "As you talk, you lean forward a little, pushing your breasts together. He notices and grins."
            "Muffin Man" "No. Not today, anyway. You can't help it. You're just a woman."
            pcname "Yes, sir. Thank you for understanding."
            "You turn back to the register."
            pcname "That'll be fifteen dollars, sir."
            "The man pulls out a twenty from his wallet and insists on helping you count out the correct change despite the register listing it in front of you."
            "Muffin Man" "And this is for you."
            show chelsea shocked
            "He passes you $2 dollars."
            "Muffin Man" "Be careful with your counting next time."
            show chelsea happy
            pcname "Of course, sir. Thank you!"
            "The businessman nods, takes his muffins, and leaves."
            hide GHCMan with moveoutleft
            "You watch him go, pleasantly surprised. Maybe Lisa's advice was good after all!"
            $ Cash +=2
            $ bakeryagree +=1
        "Tell him off." if True:
            show chelsea angry
            "You briefly consider putting on a show, but quickly leave the thought behind. You aren't about to let this guy talk to you like that!"
            if club == "track":
                show chelsea blank
                "You lean over the box of muffins, holding your fingers out to count."
                show chelsea happy
                pcname "Let's see. Two. Four. Six. Eight. Ten. Twelve. Yup, looks like they're all here to me."
                "As you look back up, you notice the man's face has turned a deep shade of red. He glares at you, yanking the box of muffins toward his chest."
                "Muffin Man" "Wrong! {i}Wrong!{/i}"
                pcname "I don't know what's so wrong about it. I counted them right here in front of you."
                pcname "Or don't you know how to count, 'sweetheart'?"
                "Muffin Man" "{i}Excuse{/i} me?! Do you know who I am?!"
                show chelsea blank
                "To you, he looks like every other businessman that walks by you on the street. Perhaps a bit more pungent."
                "You shake your head no."
                "You can visibly see his face turn a deeper shade of red in his anger. You half expect him to throw the muffins on the floor and storm out."
                "What he says it worse."
                show chelsea shocked
                "Muffin Man" "Manager! I want to speak to your manager!"
                show chelsea blank
                if bakeryagree >= 5:
                    "A shot of fear runs up your back. Despite how often this customer has ripped off the bakery, you know Keith wouldn't take your side on any sort of argument."
                    "You try to keep your cool and authority."
                elif True:
                    "You nearly roll your eyes. You could care less what Keith will say."
                pcname "Listen, sir-"
                "Muffin Man" "No! Get me your manager! {i}Now!{/i}"
                pcname "He's in a meeting right now. He's unavailable."
                "Muffin Man" "Ridiculous. Utterly ridiculous!"
            elif club == "cheer":
                show chelsea happy
                pcname "I counted them twice already, sir. There are a dozen in that box."
                "Muffin Man" "No there are {i}not!{/i} See? One, two, three, four, five--"
                "You watch as his finger intentionally jumps over one of the muffins."
                show chelsea blank
                pcname "You skipped over that muffin there, sir. I stack them in rows of four."
                "His face turns a deeper shade of red, furious."
                "Muffin Man" "Where's your manager?! I want to speak to him! Now!"
                if bakeryagree >= 5:
                    "You feel a tinge of regret as you think of what Keith might say when he hears of this, but try to keep yourself composed."
                elif True:
                    "You've heard the line a million times. You doubt Keith is going to magically fix whatever this guy wants."
                show chelsea happy
                pcname "He's in a meeting right now. Can I take a message?"
            elif club == "yearbook":
                show chelsea blank
                "You take a deep breath, summoning as much courage as you can. In truth, your legs quake behind the counter, but he doesn't need to know that."
                show chelsea sad
                pcname "That-That's a horrible thing to call someone, sir."
                "You point to each muffin, struggling to keep your voice even as you count them aloud."
                pcname "There are twelve there, sir. See? P-Perhaps you miscounted..."
                "Muffin Man" "This is an outrage! A complete outrage! What happened to the customer's always right, huh? Didn't your manager ever teach you that?!"
                show chelsea embarrassed
                "You flinch as his voice grows louder. A few other customers begin to stare at the scene. You avoid their stares, your cheeks flushed with embarrassment."
                pcname "N-No, sir..."
                "Muffin Man" "Then where is he?! Where's your manager?! I want to have a word with him!"
                show chelsea shocked
                if bakeryagree >= 5:
                    "Your heart skips a beat as you think of having to drag Keith from his meeting to deal with his angry customer. And you were doing so well..."
                elif True:
                    "You aren't sure whether to be more nervous about the man in front of you or Keith berating you again for ruining his business. Either way, you feel sick to your stomach and can't meet the businessman's gaze."
                show chelsea sad
                pcname "I-I'm so sorry, sir, but he's in a m-meeting. If... If you could come back another time..."
                "Muffin Man" "And waste my time walking all the way back here?! Are you fucking stupid?!"
            show chelsea blank
            "The man snatches his box of muffins from the counter."
            "Muffin Man" "I am not paying for these, and I'll be giving the store a call later and talk to the manager about your attitude!"
            "Muffin Man" "You'll be lucky if you still have a job by the end of the day!"
            "You watch him storm out of the store and suddenly feel a little foolish."
            hide GHCMan with moveoutleft
            "Nothing has quite worked out as you thought it would, and now you are probably going to hear a mouthful from Keith when he hears about this."
            $ bakeryagree -=1
    show L Blank at left with moveinleft
    show chelsea blank
    "Lisa steps out of Keith's office a few minutes later, adjusting her glasses. You notice a small stain on the cuff of her blouse that you're pretty sure wasn't there before, but say nothing of it."
    show L Happy at left
    L "Sorry, that took longer than I expected."
    "Lisa smiles and begins to wipe the counter down."
    L "You know, [pcname], I was thinking..."
    show L Blank at left
    L "Do you want to go shopping with me this weekend? I haven't been to the mall in a while and I was thinking we could have a girl's day."
    menu bakery_gotomall:
        "I'd love to!" if True:
            show chelsea happy
            show L Happy at left
            L "Great! I'll pick you up on Sunday, then. Does noon work for you?"
            pcname "Yeah, that would be fine."
            L "Perfect!"
            show L Blank at left
            "Lisa rips out a piece of blank receipt paper and grabs a pen."
            L "Just write down your address."
            "You copy down your address and pass it back to her. Lisa tucks the paper into her pocket."
            show L Happy at left
            L "Thanks! I'm looking forward to it."
            "You smile, and both of you resume helping customers and cleaning around the bakery for the rest of the evening."
            $ lisa_gotomall = True
            $ lisadate = True
            $ bakeryagree +=1
            jump events_end_period
        "Maybe some other time..." if True:
            show L Question at left
            "Lisa gives you an odd look, as though she's unconvinced you'll bother to find time another day to go out with her."
            L "Oh. Okay."
            show L Blank at left
            L "Well, you have my number, whenever you want to hang out. Don't be a stranger."
            hide L Blank with moveoutleft
            "Lisa walks off to wipe down a few of the cases. Neither of you talk much for the rest of your shift."
            $ bakeryagree -=1
            scene bg black with dissolve
            jump events_end_period

label bakery_mall:
    $ LHappy = "Characters/Lisa/Casual/Happy.png"
    $ LBlank = "Characters/Lisa/Casual/Blank.png"
    $ LQuestion = "Characters/Lisa/Casual/Questioning.png"
    $ LDisappoint = "Characters/Lisa/Casual/Disappointed.png"
    $ LSad = "Characters/Lisa/Casual/Sad.png"
    $ lisadate = False
    $ clothes, hair = casualwear
    show bg black with dissolve
    $ acts -= 1
    "Lisa picks you up at noon as promised and you both head to the mall."
    show bg Shop with dissolve
    show chelsea at right with moveinright
    show L Blank at left with moveinleft
    "It's pretty packed between the kids out of school and the families off from work, but you both manage to find your way to a feminine, upscale store: \"VOLEE\"."
    "You're immediately bombarded by a mix of floral perfumes and tight, bodycon dresses."
    show L Happy at left
    L "This is one of my favorite stores. They sell Black Opal. It's to die for."
    show chelsea confused
    pcname "Black Opal...?"
    show L Blank at left
    L "It's a perfume. Here, try it."
    show chelsea blank
    "Lisa leads you over to one of the perfume stands and picks up a wide, shiny black bottle. When the light hits it, you can see various shades of blue and purple glittering in the glass."
    L "Give me your wrist."
    "Lisa sprays a little bit on your skin, rubbing your wrists together before holding one up to your nose."
    "Scents of freesia and fresh rain fill your nostrils, reminding you of springtime."
    show L Happy at left
    L "Isn't it great?"
    show chelsea happy
    if club == "track":
        "It's more feminine than you traditionally go for, but you find yourself enjoying the scent. It's a nice change of pace."
    elif club == "cheer":
        "This type of perfume is right up your alley. You feel a sense of gratefulness at Lisa for showing it to you."
    elif club == "yearbook":
        "While you enjoy the scent, you feel a little flustered from the attention Lisa gives you."
    pcname "How much is it?"
    show L Blank at left
    "Lisa turns over the bottle."
    L "Fifty."
    show chelsea confused
    pcname "{i}Fifty?{/i}"
    "You stare at the bottle. It's half the size of your palm."
    show L Happy at left
    L "But it smells so, {i}so{/i} nice, [pcname]. Don't you think? And it lasts forever. I wear this stuff all the time."
    show L Blank at left
    show chelsea blank
    menu bakery_perfume:
        "Well, if it lasts a while, I guess I can get it. ($50)" if Cash >= 50:
            show chelsea happy
            show L Happy at left
            "Lisa beams, thrusting a sealed box of the perfume into your hands."
            L "Perfect! You'll smell wonderful, [pcname]. Make sure to wear it at work. People will notice."
            L "Let's go look at the clothes!"
            $ Cash -=50
            $ bakeryagree +=1
        "That's too expensive. I think I'll pass." if True:
            if bakeryagree >= 5:
                show chelsea embarrassed
                show L Disappoint at left
                "Lisa frowns, her fingers tapping the glass bottle."
                show L Question at left
                show chelsea blank
                L "Are you sure? We both thought it smelled really good. And it suits you so well..."
                menu bakery_perfume2:
                    "Well, if you really think so, I guess it can't hurt to get it. ($50)" if Cash >= 50:
                        show L Happy at left
                        show chelsea happy
                        "Lisa beams, thrusting a sealed box of the perfume into your hands."
                        L "See? I knew you'd come around. Come on, let's go look at clothes next."
                        $ Cash -=50
                        $ bakeryagree +=1
                    "I wish I could, but I don't have enough money." if True:
                        show chelsea sad
                        show L Disappoint at left
                        "Lisa clicks her tongue in disappointment, setting the bottle back on the counter."
                        L "That's a shame. You should really save up for it sometime. Let's go look at clothes, then."
                        $ bakeryagree -=1
            elif True:
                show L Disappoint at left
                "Lisa frowns, tapping the glass of the bottle."
                L "You just agreed it smelled great. And everyone at work will notice if you wear it."
                L "You'll get tipped a lot more if you smelled nice for a change."
                menu bakery_perfume3:
                    "You think I don't smell nice?" if True:
                        show chelsea confused
                        show L Blank at left
                        L "Perfume just makes such a huge difference. I think you'll really stand out with this on."
                        menu bakery_perfume4:
                            "I guess I could give it a try. ($50)" if Cash >= 50:
                                show chelsea happy
                                show L Happy at left
                                "Lisa smiles and quickly hands you one of the sealed boxes of perfume."
                                L "See? I knew you would come around."
                                L "Come on, let's go look at clothes."
                                $ Cash -=50
                                $ bakeryagree +=1
                            "I really don't have the money. I'm sorry." if True:
                                show chelsea sad
                                show L Disappoint at left
                                "Lisa scowls, placing the bottle back on the counter."
                                show L Blank at left
                                show chelsea blank
                                L "Fine. But you should really consider saving up for it. You would attract a lot more attention with it."
                                $ bakeryagree -=1
                    "What's that supposed to mean?" if True:
                        show chelsea confused
                        show L Blank at left
                        L "Deodorant doesn't do enough at work, [pcname]. How do you think I keep myself smelling nice all day?"
                        show L Happy at left
                        show chelsea blank
                        L "I'm just saying that sometimes you need an extra boost."
                        menu bakery_perfume5:
                            "I guess I could try it... ($50)" if Cash >= 50:
                                show chelsea blank
                                show L Happy at left
                                "Lisa lets out a sigh of relief, placing a sealed box of the perfume in your hands."
                                L "See? You won't regret it, [pcname]. This stuff will do wonders for you."
                                L "Let's go take a look at the clothes."
                                $ Cash -=50
                                $ bakeryagree +=1
                            "I don't have the money for it." if True:
                                show L Disappoint at left
                                "Lisa scowls, placing the bottle back on the counter."
                                show L Blank at left
                                L "Alright. You really should consider saving up for it, though. You'll attract way more attention with it."
                                L "Let's go take a look at the clothes."
                                $ bakeryagree -=1
    show chelsea blank
    show L Blank at left
    "Lisa leads you through several racks of dresses and skirts, picking out a few of her favorites."
    show L Happy at left
    L "I think you would look really nice in these."
    "Lisa holds up a few hangers: one long dress with a slit, a halter top and mini skirt, and a mini dress with a flared skirt."
    L "You should try them on!"
    menu bakery_mallclothes:
        "Sure!" if True:
            label malldecide:
                show chelsea happy
                show L Blank at left
                "Lisa carries the hangers to the dressing room, placing them in one of the stalls before she steps outside."
                show L Question at left
                L "Make sure to show them to me when you try them on!"
                show L Happy at left
                show chelsea embarrassed
                hide L Happy with dissolve
                "What outfit would you like to try on first?"
                menu bakery_mallclothes_tryon:
                    "Slit Dress." if SlitDressSeen == False:
                        hide chelsea with dissolve
                        show bg black with dissolve
                        "You hold up the maxi length dress, admiring the small gold decals along the edges."
                        "It's a pretty dress, but as you start to strip out of your clothes and pull the fabric over your head, you realize it has two slits that go right up your hip."
                        if club == "track":
                            "You frown at the high slit and deep neckline of the gown, trying to fathom how anyone could be comfortable in something like this."
                            "The fabric hangs limply between your thighs, barely covering your genitals, let alone allowing you to move freely without having to adjust yourself."
                            pcname "People actually wear these things? How am I supposed to walk around?"
                        elif club == "cheer":
                            "You look down at yourself and examine the high slit and deep neckline. Your breasts feel even more exposed than usual, and if you twist the wrong way, you're sure they'll pop right out."
                            pcname "Well that's certainly scandalous... I'll need to be really careful of what underwear I wear with this, if any at all..."
                        elif club == "yearbook":
                            "You feel your face heat up as you feel the cold air brush against your exposed hips and legs."
                            "There's no doubt others would be able to see your panties in this dress. Not to mention just how far down the neckline goes..."
                            pcname "I-I can't wear something like this outside...!"
                        "A knock at the stall door startles you from your thoughts."
                        L "[pcname]! I have some shoes for you to try on!"
                        pcname "Ah, just a minute!"
                        L "Just hold your arms out!"
                        "Without warning, Lisa tosses a pair of black strapped sandals over the stall door. You catch them clumsily, fumbling a little with the straps as you attach them to your feet."
                        L "Are you dressed yet?"
                        if club == "track":
                            "Looking down at the outfit, it isn't bad per say, but you can't bring yourself to feel any real excitement about it."
                            pcname "Yeah, I'm coming out now..."
                        elif club == "cheer":
                            "Looking down at the outfit, it feels a little too sexy, even for you. Still, if Lisa really wants to see it..."
                            pcname "Coming!"
                        elif club == "yearbook":
                            "The thought of having to step outside of the dressing room stall in this dress fills your stomach with anxiety."
                            "Still, Lisa was nice enough to pick everything out for you..."
                            pcname "C-Coming!"
                        show bg BMC1 with dissolve
                        "You step out of your stall. Lisa greets you immediately, her eyes lighting up with delight as she takes in your outfit."
                        L "This is even better than I imagined, [pcname]! You look {i}so{/i} hot!"
                        L "Ah! Wait a sec, try this on, too!"
                        "Lisa materializes a beaded bracelet and slips it onto your wrist. While you're busy admiring the jewelry, she clasps her hands together and lets out a small squeal of delight."
                        L "Perfect! You look absolutely perfect, [pcname]!"
                        if club == "track":
                            pcname "You think so? I don't know... It's kind of hard to move around."
                            L "You don't usually wear dresses, do you, [pcname]?"
                            pcname "No, not really."
                            L "That's why it feels so weird. It's really easy once you get used to it!"
                            L "Not to mention how powerful you look in this. No one would be able to object to you in this dress!"
                        elif club == "cheer":
                            pcname "You don't think it's a little {i}too{/i} revealing? I'm all for a sexy dress, but even this seems a bit much..."
                            L "Not at all! Just look at how well it compliments you! You have the perfect body for this outfit, [pcname]!"
                        elif club == "yearbook":
                            pcname "R-Really?"
                            "Her compliment instills you with a little more confidence, but with each swish of the dress, you become blatantly aware of just how much skin is showing."
                            pcname "It-It shows a lot of skin... I don't know if I can wear this kind of thing..."
                            L "You're just not used to showing off, [pcname]. You have a gorgeous body and it works perfectly with this dress."
                        L "Why don't you take a look in the mirror and see for yourself?"
                        "With a small nod, you make your way to the dressing room mirror."
                        pcname "I... I..."
                        "There's no denying it: this dress really does compliment your body in all the right ways."
                        "Even with the plunging neckline and high slit, you can't help but feel a little more comfortable and even confident as you check yourself out in the mirror."
                        "The fabric hugs you in all the right spots and shows off everything else with stylish flair."
                        L "Well? What do you think?"
                        menu bakery_mallclothesthoughts1:
                            "I love it!" if True:
                                if club == "track":
                                    "Your initial reluctance towards the dress melts way as you strike a few poses in front of the mirror, admiring the way the fabric twists around your body."
                                    "With the sandals, it's easier to move around than you thought."
                                    pcname "Oh... shit. This looks really good!"
                                elif club == "cheer":
                                    "Looking at the dress again through the perspective of the mirror, you realize exactly what Lisa means: you really do look hot."
                                    "You pose a little in the mirror, admiring the way the dress shows off your breasts and hips."
                                    pcname "I love it! This looks amazing."
                                elif club == "yearbook":
                                    "Looking at the dress through the mirror, you feel even more embarrassed as you realize just how much of your body is revealed."
                                    "Do people really dress like this? How can a woman walk around so-so exposed?"
                                    pcname "I-I... Um..."
                                    L "Turn around. Take a look at how it looks from behind."
                                    "You do as instructed, twisting around to better view how it looks."
                                    "The dip in the back is even worse, exposing so much of your back, but... but..."
                                    pcname "...I-I like it."
                                    "It's mortifying to admit, but you can't help it. Despite how much of your body is exposed, you can't help feeling a little more confident in this gown."
                                L "See? I told you! You look amazing, [pcname]."
                                "You look back at Lisa, touched by her encouragement."
                                pcname "Thank you."
                                "Lisa's eyes rove over your body, every curve accented by the thin black fabric."
                                L "You have to buy this one, [pcname]! It's perfect on you!"
                                if club == "track":
                                    pcname "Ah, I'm not sure yet. I have the others to try on still..."
                                elif club == "cheer":
                                    pcname "You think so? It's really cute, but I want to see what the others look like, too!"
                                elif club == "yearbook":
                                    pcname "I-I'm not even sure how much it costs... And there's other ones to try on..."
                                    "Although, just looking at what Lisa had picked out for you, you can already imagine how tight and short the others will be..."
                                L "Oh, you're right! There's still so much to see!"
                                L "I think I really like this one the best, though..."
                                L "Well don't wait up. I can't wait to see the others!"
                                "You nod and slip back into the dressing room."
                                $ SlitDressSeen = True
                                show bg black with dissolve
                                jump bakery_mallclothes_tryon
                            "This is too much." if True:
                                if club == "track":
                                    "You twist and turn in the mirror, noticing how deep even the back of the dress drops to your waist."
                                    "There's no way you can be really active in this kind of clothing."
                                    pcname "...It's just not practical."
                                    "Lisa frowns."
                                    L "What's wrong with it? You can walk just fine in the sandals, can't you?"
                                    pcname "Well, yeah, but the dress... I can't do anything in this. I can't barely walk, I can't run-"
                                    L "Well you shouldn't be running it in anyway..."
                                elif club == "cheer":
                                    "You observe yourself in the mirror, frowning at the way the dress moves against your body."
                                    "It's flattering, but... but..."
                                    pcname "No. I think it's too much."
                                    L "Too much?"
                                    "Lisa raises her eyebrows in shock."
                                    L "But you look so sexy, [pcname]! We can't let that hot body go to waste..."
                                    pcname "I don't think it would go to {i}waste{/i}, but this is definitely... too much."
                                    pcname "Sorry."
                                elif club == "yearbook":
                                    "Looking at yourself in the mirror, it's even worse than you imagined."
                                    "Sure, the curves of your body look... look..."
                                    "You blush just thinking of how attractive you appear. But even so, there's no way you could bring yourself to wear something like this outside!"
                                    pcname "I-I'm still not sure... It just seems like so much..."
                                    L "Oh, but you look so sexy, [pcname]!"
                                    pcname "T-That's the problem..."
                                    L "You should really be more confident in yourself, [pcname]. You're a very beautiful girl. You should show it off!"
                                    pcname "I-I... I..."
                                    "You shake your head, too embarrassed to speak."
                                "Lisa sighs, shaking her head."
                                L "Well, let's try on the other outfits at least."
                                "Lisa gestures toward the dressing room. You nod and step back inside."
                                $ SlitDressSeen = True
                                show bg black with dissolve
                                jump bakery_mallclothes_tryon
                    "Halter Outfit." if HalterDressSeen == False:
                        hide chelsea with dissolve
                        show bg black with dissolve
                        "Your gaze falls onto a halter top and a pair of tiny black shorts displayed on two separate hangers."
                        "As you start to strip out of your clothes and pull the outfit on, you realize just how tight and short the clothes are on you."
                        if club == "track":
                            "While you were initially excited to see the shorts among the pile of clothes, you realize now just how tight they are and hard to move around in."
                            "It feels like they're trying to give your crotch a hug."
                            "You uncomfortably try to peel them down a little more and adjust yourself."
                            pcname "These are so damn tight... How does anyone move in these?"
                        elif club == "cheer":
                            "Looking down at yourself, you can't help but notice just how tightly the halter top presses against your breasts and how tiny the shorts ride up over your thighs."
                            "You run your hands down your body, feeling just how prominent your curves are."
                            pcname "There's really no hiding anything in this, is there...?"
                        elif club == "yearbook":
                            "You look down at yourself, your face flushing as you realize just how tight your clothes fit against your body."
                            "There's nothing to hide the curves of your body, the flat panes of your stomach, your thighs..."
                            pcname "I-I can't go out there looking like this!"
                        "A knock at the stall door startles you from your thoughts."
                        L "[pcname]! I have some shoes for you to try on!"
                        pcname "Ah, just a minute!"
                        L "Just hold your arms out!"
                        "Without warning, Lisa tosses a pair of black boots over the stall door. You catch them clumsily, fumbling a little with the laces as you tie them on."
                        L "Are you dressed yet?"
                        if club == "track":
                            pcname "Ah, yeah! Coming out now!"
                            "You waddle uncomfortably out of the dressing room, trying to ignore the discomfort of the shorts riding up your crotch as you move."
                        elif club == "cheer":
                            pcname "Coming~!"
                            "You walk out of the dressing room, fully aware of just how your shorts just barely conceal your ass."
                        elif club == "yearbook":
                            pcname "J-Just a minute!"
                            "With some reluctance, you shuffle out of the dressing room, arms wrapped around the bare skin of your stomach."
                        show bg BMC2 with dissolve
                        "Lisa grins as you exit, waiting for you outside of the dressing room."
                        L "Oh, [pcname], this is even better than I imagined! You look {i}so{/i} hot! I knew that halter top was a good choice!"
                        L "And just look at the shorts! You have legs for days!"
                        if club == "track":
                            pcname "Well, yeah, but it's kind of hard to walk in..."
                            L "Oh don't you worry about that! It just takes some time getting used to it."
                        elif club == "cheer":
                            pcname "Thanks! This outfit doesn't leave much to the imagination, does it?"
                            L "Ha! Not at all, but that makes it even sexier, doesn't it?"
                        elif club == "yearbook":
                            pcname "I-I-- T-Thank you."
                            "You stammer, your face heating up as you take in Lisa's compliment."
                            "You can't help but feel a little more confident with Lisa cheering you on."
                        L "Well don't just stand there, [pcname]! Why don't you take a look in the mirror?"
                        "You nod and walk to the floor-length mirror in the dressing room."
                        "Lisa's compliments are warranted, you realize; now that you have the full view of your body in the reflection, you see just how tight the shorts and halter top press against your curves."
                        "Little black laces crawl up the sides of your thighs, barely holding the stretched denim fabric of your shorts together, while your halter top shows off the long stretch of your torso."
                        if club == "track":
                            "You adjust your shorts again to a comfortable position and admire yourself in the mirror."
                            "Even with the shorts riding up your crotch, you start to feel more comfortable in the outfit. More confident, even."
                        elif club == "cheer":
                            "You grin at yourself in the mirror and pose a little, admiring how well the outfit compliments your body."
                        elif club == "yearbook":
                            "With some embarrassment, you turn around in the mirror to view every angle of your body."
                            "It's... There's no denying you look attractive, but even admitting that to yourself feels shameful."
                        "Lisa looks at you from over your shoulder, a bright smile on her face."
                        L "So? What do you think?"
                        menu bakery_mallclothesthoughts2:
                            "I love it!" if True:
                                if club == "track":
                                    "You spin around a couple of times, admiring the sound of the boots as you walk."
                                    "They look great with the outfit, and the shorts... Sure, maybe they're a little uncomfortable, but the style boosts you with a refreshing energy."
                                    pcname "Oh... shit. This looks really good!"
                                elif club == "cheer":
                                    "Looking at the outfit again through the perspective of the mirror, you can't deny that you feel sexy and admirable in these new clothes."
                                    "You pose a little in the mirror, admiring the way the halter top and shorts show off your breasts and hips."
                                    pcname "I love it! These clothes are really sexy."
                                elif club == "yearbook":
                                    "Looking at the outfit through the mirror, you feel even more embarrassed as you realize just how little they leave to the imagination."
                                    "Do people really dress like this? How can a woman walk around so-so exposed?"
                                    pcname "I-I... Um..."
                                    L "Turn around. Take a look at how it looks from behind."
                                    "You do as instructed, twisting around to better view how it looks."
                                    "The curve of your ass is impossible to ignore, but... but..."
                                    pcname "...I-I like it."
                                    "It's mortifying to admit, but you can't help it. Despite how tight the clothes are, you can't help feeling a little more confident in this gown."
                                L "See? I told you! You look amazing, [pcname]."
                                "You look back at Lisa, touched by her encouragement."
                                pcname "Thank you."
                                "Lisa's eyes rove over your body, every curve accented by the tight black fabric."
                                L "You have to buy this one, [pcname]! It's perfect on you!"
                                if club == "track":
                                    pcname "Ah, I'm not sure yet. I have the others to try on still..."
                                elif club == "cheer":
                                    pcname "You think so? It's really cute, but I want to see what the others look like, too!"
                                elif club == "yearbook":
                                    pcname "I-I'm not even sure how much it costs... And there's other ones to try on..."
                                    "Although, just looking at what Lisa had picked out for you, you can already imagine how tight and short the others will be..."
                                L "Oh, you're right! There's still so much to see!"
                                L "I think I really like this one the best, though..."
                                L "Well don't wait up. I can't wait to see the others!"
                                "You nod and slip back into the dressing room."
                                $ HalterDressSeen = True
                                show bg black with dissolve
                                jump bakery_mallclothes_tryon
                            "This is too much." if True:
                                if club == "track":
                                    "You twist and turn in the mirror, noticing how high the shorts ride up into your ass and crotch."
                                    "There's no way you can be really active in this kind of clothing."
                                    pcname "...It's just not practical."
                                    "Lisa frowns."
                                    L "What's wrong with it? You can walk just fine in the boots, can't you?"
                                    pcname "Well, yeah, but the shorts... I can't do anything in this. I can't barely walk, I can't run-"
                                    L "Well you shouldn't be running it that kind of outfit anyway..."
                                elif club == "cheer":
                                    "You observe yourself in the mirror, frowning at the way the shorts ride up into your ass."
                                    "It's flattering, but... but..."
                                    pcname "No. It's too uncomfortable."
                                    L "Uncomfortable?"
                                    "Lisa raises her eyebrows in shock."
                                    L "But you look so sexy, [pcname]! We can't let that hot body go to waste..."
                                    pcname "I don't think it would go to {i}waste{/i}, but I don't want to be picking my shorts out of my ass all day."
                                    pcname "Sorry."
                                elif club == "yearbook":
                                    "Looking at yourself in the mirror, it's even worse than you imagined."
                                    "Sure, the curves of your body look... look..."
                                    "You blush just thinking of how attractive you appear. But even so, there's no way you could bring yourself to wear something like this outside!"
                                    pcname "I-I'm still not sure... It just seems like so much..."
                                    L "Oh, but you look so sexy, [pcname]!"
                                    pcname "T-That's the problem..."
                                    L "You should really be more confident in yourself, [pcname]. You're a very beautiful girl. You should show it off!"
                                    pcname "I-I... I..."
                                    "You shake your head, too embarrassed to speak."
                                "Lisa sighs, shaking her head."
                                L "Well, let's try on the other outfits at least."
                                "Lisa gestures toward the dressing room. You nod and step back inside."
                                $ HalterDressSeen = True
                                show bg black with dissolve
                                jump bakery_mallclothes_tryon
                    "Mini Dress." if MiniDressSeen == False:
                        hide chelsea with dissolve
                        show bg black with dissolve
                        "A cobalt blue mini dress dangles from the first hanger, its collar giving off nautical vibes."
                        "It's cute- a very simple sort of gown- but as you strip out of your clothes and pull the dress over your body, you realize just how short it is."
                        if club == "track":
                            "You bend over a couple of times, frowning at just how much your body is exposed as you move; your cleavage nearly spills out of the top while the skirt flashes anyone nearby a perfect view of your panties."
                            pcname "This is so impractical..."
                        elif club == "cheer":
                            "You smile a little to yourself as the fabric fits tightly against your body, barely reaching down past your ass."
                            "It's cute, but it would be cuter if it didn't have these childish puffed sleeves added on..."
                            pcname "It's like they can't decide if they want to be sexy or girlish... It isn't a good mix."
                        elif club == "yearbook":
                            pcname "T-This barely covers my butt!"
                            "You try to yank the skirt further down your thighs, but each tug pulls the thin fabric lower against your breasts, exposing your cleavage."
                            pcname "How am I supposed to wear this?!"
                        "A knock at the stall door startles you from your thoughts."
                        L "[pcname]! I have some shoes for you to try on!"
                        pcname "Ah, just a minute!"
                        L "Just hold your arms out!"
                        "Without warning, Lisa tosses a pair of white heels over the stall door. You catch them clumsily, fumbling a little with the straps as you attach them to your feet."
                        L "Are you dressed yet?"
                        if club == "track":
                            pcname "Yeah! Coming out now!"
                            "You walk out of the dressing room, struggling to balance in the heels."
                        elif club == "cheer":
                            pcname "Coming~!"
                            "You strut out of the dressing room, keeping a perfect posture in your heels as the skirt rides up against your thighs."
                        elif club == "yearbook":
                            pcname "J-Just a minute!"
                            "You hesitantly walk out of the dressing room, continuously tugging down the skirt of your dress while simultaneously covering your breasts with your other hand."
                        show bg BMC3 with dissolve
                        "Lisa waits on the other side of the stall, a bright smile on her face as she takes in your dress."
                        L "God, [pcname], this is so cute! I knew it would suit you as soon as I saw it on the rack."
                        L "You look amazing in this dress! It compliments your body so well!"
                        if club == "track":
                            "Feeling more confident by her encouragement, you flash Lisa a grin."
                            pcname "Thanks."
                            pcname "It's kind of short though, don't you think?"
                            L "That's the style nowadays. It really helps compliment your figure, don't you think? Now you can show off those strong thighs!"
                            "Glancing down, you see what she means; there's no hiding your muscles in this kind of dress. Honestly, you kind of like it."
                        elif club == "cheer":
                            pcname "Aw, thanks, Lisa!"
                            pcname "But don't you think these sleeves look a little... childish?"
                            "Lisa taps her chin in thought, then shakes her head."
                            L "Not at all! It helps bring out a sort of innocent vibe in addition to all of the sexiness you have going on."
                            L "You want to leave {i}some{/i} things to the imagination!"
                            "You don't really understand how hiding your shoulders would leave much to the imagination when so much of your body is already well displayed, but maybe the sleeves aren't {i}that{/i} bad..."
                        elif club == "yearbook":
                            "Feeling a little more confident from Lisa's encouragement, you give her a shy smile."
                            pcname "T-Thank you..."
                            pcname "But don't you think this dress is a bit much? I-I can barely cover myself...!"
                            L "No, no, [pcname]! It looks adorable! This dress really does suit you!"
                            L "It's really not {i}that{/i} short at all! I can barely tell."
                            "You bite your lip, uncertain. If she says it's not that bad, maybe your fears really are just in your head..."
                            "But that doesn't make you feel any less exposed."
                        L "Well don't just stand there, [pcname]! Why don't you take a look in the mirror?"
                        "You nod and walk to the floor-length mirror in the dressing room."
                        "Looking at yourself in the mirror, you really understand where Lisa's compliments are coming from."
                        "The blue of the dress pops out against your vibrant red hair, and the style reminds you of those old 1940's cartoons you used to watch as a child."
                        "It's a very vintage-inspired dress and, somehow, you look fantastic in it."
                        if club == "track":
                            "You grin at yourself in the mirror, careful to move slowly so you don't trip over yourself in those heels. They really compliment the outfit, but they're definitely hard to walk in!"
                        elif club == "cheer":
                            "You smirk at yourself in the mirror, giving a little twirl to admire each angle and curve of your body."
                        elif club == "yearbook":
                            "Your face flushes as you take in your reflection in the mirror; breasts nearly popping out of the top, the skirt barely reaching past your ass..."
                            "And yet, you find yourself admiring the girl in the mirror, entranced by how beautiful she looks in that dress."
                            "You can't help but stand up a little straighter, a new confidence flooding through you."
                        "Lisa looks at you from over your shoulder, a bright smile on her face."
                        L "So? What do you think?"
                        menu bakery_mallclothesthoughts3:
                            "I love it!" if True:
                                if club == "track":
                                    "You take some time getting used to walking and turning in the heels, your confidence rising with each step."
                                    "Maybe it won't be so hard to walk like this. Hell, maybe you could even learn to run in them!"
                                    pcname "Damn... This looks great!"
                                elif club == "cheer":
                                    "You continue to check yourself out in the mirror, running your hands through your hair and down the curves of your body."
                                    "This dress really shows everything off- and you {i}love{/i} it!"
                                    pcname "It's perfect! I love it, Lisa!"
                                elif club == "yearbook":
                                    "Your face burns as you continue to stare at your reflection. So much of your body is exposed but... but..."
                                    pcname "...I-I like it."
                                    "You give Lisa a small, shy smile through the mirror."
                                L "See? I told you! You look amazing, [pcname]."
                                "You look back at Lisa, touched by her encouragement."
                                pcname "Thank you."
                                "Lisa's eyes rove over your body, every curve accented by the thin blue fabric."
                                L "You have to buy this one, [pcname]! It's perfect on you!"
                                if club == "track":
                                    pcname "Ah, I'm not sure yet. I have the others to try on still..."
                                elif club == "cheer":
                                    pcname "You think so? It's really cute, but I want to see what the others look like, too!"
                                elif club == "yearbook":
                                    pcname "I-I'm not even sure how much it costs... And there's other ones to try on..."
                                    "Although, just looking at what Lisa had picked out for you, you can already imagine how tight and short the others will be..."
                                L "Oh, you're right! There's still so much to see!"
                                L "I think I really like this one the best, though..."
                                L "Well don't wait up. I can't wait to see the others!"
                                "You nod and slip back into the dressing room."
                                $ MiniDressSeen = True
                                show bg black with dissolve
                                jump bakery_mallclothes_tryon
                            "This is too much." if True:
                                if club == "track":
                                    "You twist and turn in the mirror, frowning at the difficulty of the heels and the impracticality of the dress."
                                    "If you ever drop something, it's going to be a real pain to bend over and try to pick it up."
                                    "Not to mention how hard it would be to run in this sort of thing..."
                                    pcname "...I'm just not feeling it."
                                    L "What? I thought you liked it."
                                    pcname "I mean, it's cute, but it's not practical at all. It's just not for me. Sorry."
                                elif club == "cheer":
                                    "You observe yourself in the mirror, your lips drawing into a frown every time you look back at those ridiculous sleeves."
                                    "The dress itself is so cute, but why does it have to have those sleeves?"
                                    pcname "No. I just can't get behind these sleeves. They're too childish."
                                    L "Really? But the dress itself is so cute. Those sleeves really aren't that bad."
                                    pcname "I just keep thinking I look like a toddler every time I look in the mirror."
                                    pcname "This one just isn't for me. Sorry, Lisa!"
                                elif club == "yearbook":
                                    "You can't contain the blush on your face as you realize just how much skin you're showing off. There's no way you could wear this outside!"
                                    pcname "I... N-No. I can't wear this!"
                                    L "Huh? Why not? You look so sexy, [pcname]!"
                                    pcname "T-That's the problem..."
                                    L "You should really be more confident in yourself, [pcname]. You're a very beautiful girl. You should show it off!"
                                    pcname "I-I... I..."
                                    "You shake your head, too embarrassed to speak."
                                "Lisa sighs, shaking her head."
                                L "Well, let's try on the other outfits at least."
                                "Lisa gestures toward the dressing room. You nod and step back inside."
                                $ MiniDressSeen = True
                                show bg black with dissolve
                                jump bakery_mallclothes_tryon
                    "I'm done wearing all the outfits!" if SlitDressSeen == True and HalterDressSeen == True and MiniDressSeen == True:
                        pass
                show bg black with dissolve
                "You slip in and out of the other outfits, realizing just how tight they shape to your body."
                "As you try them on, Lisa runs back and forth from the shoe department, giving you a correct pair for each outfit."
                if club == "track":
                    "These outfits are definitely more feminine than the type you typically go for, but you can't deny that Lisa sure has a good sense of style."
                    "You definitely feel more confident in these outfits."
                elif club == "cheer":
                    show chelsea happy
                    "You adore Lisa's sense of style, and make extra efforts to check yourself out in the mirror a little more with each outfit."
                    "You can't help but feel sexier all dressed up like this."
                elif club == "yearbook":
                    "Checking yourself out in the mirror, you can't disguise the embarrassment that comes over you with each slit and revealing cut of clothing."
                    "Deep down, though, a part of you loves how you look in these types of outfits."
                    "The thought only embarrasses you further."
                "After changing back into your regular clothes, Lisa greets you outside of the stall."
                show chelsea happy at right with moveinright
                show bg Shop with dissolve
                show L Happy at left with moveinleft
                L "You looked fantastic, [pcname]!"
                L "They looked stunning on you. You should get one of them!"
                show chelsea blank
                show mallchoose with dissolve
                "You saw the price tags in the dressing room. Clothes like these don't come cheap."
                show chelsea happy
                "But Lisa said how great you look. And the shoes really bring the whole thing together..."
                show L Blank at left
                hide chelsea with dissolve
                hide L Blank with dissolve
                show mallchoose with dissolve
                $ bakeryagree +=1
                menu bakery_mallclothes2:
                    "Buy the slit dress. ($100)" if Cash >= 100:
                        $ corruption += 3
                        show chelsea happy at right with dissolve
                        "It's pretty expensive, but you have to splurge once in a while, right?"
                        hide mallchoose with dissolve
                        $ dressList.dresses[12].bought = True
                        "You hold up the slit dress."
                        pcname "I like this one best."
                        show L Happy at left
                        L "Perfect!"
                        "Lisa hangs up the remaining clothes on the rack."
                        show L Blank at left
                        L "Now how about we check out some makeup?"
                        "Lisa takes your arm and leads you to the makeup counter."
                        $ Cash -=100
                        $ bakeryagree +=1
                    "Buy the halter outfit. ($75)" if Cash >= 75:
                        $ corruption += 2
                        $ dressList.dresses[9].bought = True
                        show chelsea happy at right with dissolve
                        show L Blank at left with dissolve
                        "It's expensive, but you have to splurge once in a while, right?"
                        hide mallchoose with dissolve
                        "You hold up the halter top and the skirt."
                        pcname "I think I'm going to get this outfit."
                        show L Happy at left
                        L "Perfect!"
                        "Lisa hangs up the remaining clothes on the rack."
                        show L Blank at left
                        L "How about we check out some makeup?"
                        "She takes your arm and leads you to the makeup counter."
                        $ Cash -=75
                        $ bakeryagree +=1
                    "Buy the mini dress. ($50)" if Cash >= 50:
                        $ corruption += 1
                        $ dressList.dresses[10].bought = True
                        show chelsea happy at right with dissolve
                        show L Blank at left with dissolve
                        "It's not too bad price wise, and you have to splurge once in a while, right?"
                        hide mallchoose with dissolve
                        "You hold up the mini dress."
                        pcname "I really like this one."
                        show L Happy at left
                        L "Perfect!"
                        "Lisa hangs up the remaining clothes on the rack."
                        show L Blank at left
                        L "Let's go check out the makeup then!"
                        "Lisa takes your arm and leads you to the makeup counter."
                        $ bakeryagree +=1
                        $ Cash -=50
                    "Buy nothing." if True:
                        hide mallchoose with dissolve
                        show chelsea at right with dissolve
                        show L Blank at left with dissolve
                        pcname "I think I'm good, actually. I don't need any of this stuff."
                        show L Question at left
                        "Not to mention everything Lisa picked out was outrageously expensive."
                        if bakeryagree >= 5:
                            L "But you looked so good in them, [pcname]! I urge you to reconsider."
                            L "Just one outfit? You looked so cute."
                            hide L Question with dissolve
                            hide chelsea with dissolve
                            show mallchoose with dissolve
                            menu bakery_mallclothes3:
                                "Buy the slit dress. ($100)" if Cash >= 100:
                                    $ corruption += 3
                                    $ dressList.dresses[12].bought = True
                                    "You're pretty tempted by her words. You felt really attractive in that slit dress..."
                                    show chelsea happy at right with dissolve
                                    pcname "Alright. I'll get this one."
                                    hide mallchoose with dissolve
                                    show L Happy at left with dissolve
                                    "Lisa beams, thrilled."
                                    L "That's wonderful, [pcname]! You looked fabulous in that."
                                    "You set the remaining clothes on the rack."
                                    L "Now let's go check out the makeup counter. There's some eyeshadow that has my name written all over it."
                                    $ Cash -= 100
                                    $ bakeryagree +=1
                                "Buy the halter outfit. ($75)" if Cash >=75:
                                    $ corruption += 2
                                    $ dressList.dresses[9].bought = True
                                    "You're pretty tempted by her words. You felt really cute in that halter outfit..."
                                    show chelsea happy at right with dissolve
                                    pcname "Okay. I'll get this outfit."
                                    hide mallchoose with dissolve
                                    show L Happy at left with dissolve
                                    "Lisa beams, thrilled."
                                    L "Perfect! I think that outfit suited you best, anyway."
                                    "You set the remaining clothes on a nearby rack."
                                    L "Let's go check out the makeup counter. There's some eyeshadow I've been dying to get."
                                    "You follow Lisa across the store to the makeup department."
                                    $ Cash -=75
                                    $ bakeryagree +=1
                                "Buy the mini dress. ($50)" if Cash >=50:
                                    $ corruption += 1
                                    $ dressList.dresses[10].bought = True
                                    "You're pretty tempted by her words. You felt really good in that mini dress, and it wasn't too expensive..."
                                    show chelsea happy at right with dissolve
                                    pcname "Alright. I'll get this one."
                                    hide mallchoose with dissolve
                                    show L Happy at left with dissolve
                                    "Lisa beams, thrilled."
                                    L "That's perfect for you! Your legs looked amazing in that."
                                    "You set the remaining clothes on a nearby rack."
                                    L "Now let's check out the makeup counter. They have this really cute eyeshadow I've been dying to get!"
                                    $ Cash -=50
                                    $ bakeryagree +=1
                                "Buy nothing." if True:
                                    hide mallchoose with dissolve
                                    show chelsea sad at right with dissolve
                                    pcname "I'm sorry, Lisa. They're just not really in my budget right now."
                                    pcname "Maybe next time?"
                                    show L Disappoint at left with dissolve
                                    "Lisa frowns, put out by your decision. She sets the clothing back on the rack."
                                    if bakeryagree >= 5:
                                        show L Blank at left
                                        L "I'm sorry to hear that, [pcname]. You should really save up for clothes like these. You looked so good..."
                                    elif True:
                                        L "You should really budget for things like this, [pcname]. Your appearance is just as important as everything else in your life."
                                    show L Happy at left
                                    L "I guess we can go straight to the makeup counter, then."
                                    "Lisa leads you through the store to the makeup department."
                                    $ bakeryagree -=1
        "They're not really my style..." if True:
            show L Question at left
            L "But you would look so cute in them, [pcname]. Just try them on and see."
            menu bakery_mallclothes4:
                "If you really want me to..." if True:
                    show chelsea embarrassed
                    show L Happy at left
                    "Lisa grins and passes the clothes into your arms."
                    L "You're going to look so cute! Trust me."
                    show chelsea happy
                    "You both make your way to the dressing room and claim one of the stalls."
                    jump malldecide
                "I'm not interested. Sorry." if True:
                    if bakeryagree >= 5:
                        show L Disappoint at left
                        "Lisa frowns, putting the array of clothing back onto their proper racks."
                        L "I can't say I'm not disappointed, [pcname]. You should be more of a team player."
                        L "I guess we can go straight to the makeup counter then."
                        $ bakeryagree -=1
                    elif True:
                        show L Disappoint at left
                        "Lisa clicks her tongue, putting the array of clothing back onto their proper racks."
                        L "What's the point of going shopping with someone if they won't try on anything?"
                        L "I guess we can go straight to the makeup counter then."
                        $ bakeryagree -=1
    show chelsea shocked
    show L Blank at left
    "The makeup counter at \"VOLEE\" is perhaps the largest you've ever seen. Each section is separated by makeup artists and their brands. Every color imaginable is on display."
    show chelsea blank
    "As Lisa leads you toward an array of lipsticks, one of the male workers walks up to you."
    show GHCMan with dissolve
    "VOLEE Worker" "Hello, ladies. How are we doing today?"
    show L Happy at left
    "Lisa turns and smiles."
    L "We're doing fine, how are you?"
    "VOLEE Worker" "Wonderful, thank you for asking. Is there anything I can help you ladies find today?"
    L "Oh, no, we're fine. Thank you."
    hide GHCMan with moveoutleft
    "The male worker smiles at both of you and nods, walking off to greet another customer. Lisa's gaze lingers for a moment, then returns to the makeup in front of her."
    show L Blank at left
    L "What did you think of him?"
    show chelsea confused
    pcname "Hm?"
    L "Of the worker. What did you think of him?"
    pcname "Oh. He seemed nice. Helpful."
    if bakeryagree >= 5:
        show L Happy at left
        "Lisa giggles, rolling her eyes."
    elif True:
        show L Disappoint at left
        "Lisa rolls her eyes, impatient."
    L "I meant his appearance. Did you find him attractive?"
    menu bakery_mallattractive:
        "I guess he was sort of cute." if True:
            show chelsea blank
            show L Happy at left
            L "So would you say that's your type?"
            if club == "track":
                "You look back at the worker. You notice that he's pretty slim and not very athletic. You can't imagine taking him out running or doing any fun sports with him."
                pcname "Not really."
            elif club == "cheer":
                "You look back at the worker. He's attractive in his own way, but not necessarily the kind of person you go for."
                pcname "Not really."
            elif club == "yearbook":
                show chelsea embarrassed
                "You look back at the worker, hoping to avoid catching his eye. He seems pretty extroverted. You aren't sure you would be comfortable with all that attention."
                pcname "N-Not really..."
        "I didn't really notice..." if True:
            show chelsea blank
            show L Blank at left
            L "Well, take a look at him."
            "You glance back at the worker as he helps out a struggling mother."
            if club == "track":
                "You can't help but notice how bad his posture is. It would take a lot to get him in shape."
                pcname "Nah. He looks weak."
            elif club == "cheer":
                "He's attractive, you guess, but not your type."
                pcname "He's okay, I guess, but not really my type."
            elif club == "yearbook":
                "Based on how active he is with his customers, you feel a little intimidated. You're not sure you could handle all of that energy and attention."
                show chelsea embarrassed
                pcname "I-I don't really think he's my type..."
    show L Blank at left
    show chelsea blank
    L "So what kind of guy {i}do{/i} you find attractive?"
    show chelsea shocked
    "As Lisa talks, she passes you different bottles of makeup: lipsticks, mascara, eyeliner, highlighter... You struggle to keep them balanced in your hands."
    show chelsea blank
    if mattchain > 1:
        if defymatt == True:
            show chelsea angry
            "You hate that the first thing to come to mind is Matt. There's no way you could find him {i}attractive{/i}, especially not after all he's done to you."
        elif True:
            show chelsea embarrassed
            "A shiver of excitement runs through you as Matt comes to mind. You aren't sure if that's something you want to explain to Lisa, though."
    if violetrelate == "Sub":
        show chelsea happy
        "Your mind immediately jumps to Violet, whimpering and submissive. You're not really sure that's something you want to tell Lisa, though."
    if violetrelate == "Dom":
        show chelsea embarrassed
        "Your mind immediately jumps to Violet towering over you with dominance and control. You're not really sure that's something you want to tell Lisa, though."
    if damienrelate == "dating":
        show chelsea embarrassed
        "You smile a little as Damien comes to mind. He's so sweet and nerdy, you can't help but feel a little embarrassed thinking about it."
        "You aren't sure if that's something you want to gush about to Lisa, though."
    show chelsea blank
    "You try to think over people you've found attractive in your past."
    "What {i}is{/i} your type?"
    menu bakery_mallattractive2:
        "Super romantic." if True:
            if club == "track":
                show chelsea happy
                "You hate to admit it, but there's something about a fairytale prince-type of person that's always appealed to you."
                "You'd love to rescue him from an ivory tower and be the one to slay the dragon."
                pcname "I guess I like someone prince-like."
                "Lisa seems surprised by your answer."
                L "Really? I never thought {i}you{/i} would choose someone like that..."
            elif club == "cheer":
                show chelsea happy
                "As you think about it, the image of a prince-like figure comes to mind, escorting you to a rooftop restaurant they privately reserved with a view of the city."
                "They would be a perfect gentleman on the surface, but a beast in the bedroom."
                pcname "Someone that can sweep me off my feet would be nice."
            elif club == "yearbook":
                show chelsea embarrassed
                "It's a little embarrassing, but you can't help imagining a handsome prince-like figure with a large bouquet of roses outside of your doorstep."
                pcname "I-I suppose... someone very romantic would be nice..."
            show L Disappoint at left
            L "That's pretty cliche, don't you think? Not very exciting..."
        "Tall, dark, and handsome." if True:
            if club == "track":
                show chelsea happy
                "The image of a tall, dark, and handsome person comes to mind, someone who can be just as reckless and confident about their decisions as you are."
                pcname "Tall, dark, and handsome isn't so bad."
            elif club == "cheer":
                show chelsea happy
                "Bad boys have always been part of the female fantasy, and you're no exception. There's just something about a reckless, mysterious man that you want to know more about."
                pcname "Someone a little mysterious would be fun."
            elif club == "yearbook":
                show chelsea happy
                "There's something about the idea of a tall, dark, handsome person that you can try to help see the good in the world appeals to you."
                pcname "I, um, guess someone a little... dark and troubled. Someone I could help, maybe..."
            L "Hmm. How typical."
        "Dominant." if True:
            if club == "track":
                show chelsea happy
                "Although you're used to being loud and confident, you find the idea of someone else being in charge sort of appealing..."
                show chelsea embarrassed
                pcname "I wouldn't {i}hate{/i} someone else being in charge for a change, I guess..."
            elif club == "cheer":
                show chelsea happy
                "The thought of someone taking control of the relationship and giving you orders sends a thrill up your spine."
                pcname "I like someone that doesn't mind dominating me a little."
            elif club == "yearbook":
                show chelsea embarrassed
                "The idea of being in charge in a relationship puts you on edge. Yes, you would definitely want someone else to handle that sort of thing."
                pcname "I-I like someone else to, um, be in charge."
            show L Happy at left
            "Lisa gives you a small smirk."
            L "Oh, I can relate."
        "Submissive." if True:
            if club == "track":
                show chelsea happy
                "You enjoy the idea of taking control of the relationship and having someone that will heed your every order. It's almost like being a team captain, but better!"
                pcname "I like someone that lets me be in charge."
            elif club == "cheer":
                show chelsea happy
                "You can't help but toy around with the idea of pushing someone around until they submit to you."
                pcname "I like someone that doesn't mind being submissive."
            elif club == "yearbook":
                show chelsea embarrassed
                "The thought of being in charge of someone makes you nervous, but also excites you a little."
                show chelsea happy
                pcname "I-I think... I would like to hold the pants in the relationship..."
            L "Really? That's surprising."
            show L Happy at left
            "She lets out a soft laugh."
            show L Blank at left
            L "I didn't expect you to be a little dominatrix."
        "I'm not sure." if True:
            show chelsea confused
            pcname "I'm not really sure I have a type."
            show L Disappoint at left
            L "Really? That's disappointing."
            show L Happy at left
            L "Maybe we just need to find you the right kind of person."
    "Lisa smiles and reaches out toward you. Her fingers brush the side of your face as she tucks a strand of your hair behind your ear."
    L "I'm partial to redheads myself."
    show chelsea embarrassed
    "You're unable to contain the light blush that spreads over your cheeks."
    "Lisa looks you over, her lips pursed."
    show L Blank at left
    L "But, you know, I think I'm becoming more interested in blondes."
    show L Happy at left
    "She giggles, pulling away."
    L "Part your lips. I want you to try this on."
    show chelsea blank
    "You comply. Lisa brushes the lipstick onto a sample tool and runs it over your lips."
    show chelsea embarrassed
    "You're suddenly hyper aware of the feel of the tool against your lips, caressing your skin softly as Lisa applies the lipstick."
    if club == "track":
        "You feel an urge of excitement at her gentle strokes."
    elif club == "cheer":
        "Just the touch makes you want to kiss something."
    elif club == "yearbook":
        "You're unable to contain the embarrassing blush that forms on your face."
    show L Blank at left
    L "Okay. Take a look."
    scene bg Mall1 with dissolve
    "You turn toward one of the mirrors on the edge of the display and admire the light shade of pink. It's subtle, with a little bit of glitter to really make it pop."
    show bg Mall2 with dissolve
    pcname "That's really cute!"
    L "Right?"
    L "Come here. I want to apply some foundation."
    show bg black with dissolve
    "Lisa continues to apply makeup to your face. You sit there, obeying her every order as she meticulously paints your face."
    L "Okay! Take a look."
    show bg Mall3 with dissolve
    "It takes you a moment to adjust to the change in the mirror."
    "You've rarely worn full-face makeup, and everything about your facial features seemed to glow. Your eyes pop, your lips look sultry, and even the blush on your cheeks give you a soft, feminine appeal."
    L "What do you think?"
    menu bakery_mallmakeup:
        "I love it!" if True:
            show bg Mall4 with dissolve
            if bakeryagree >= 5:
                L "I knew you would! You look amazing, [pcname]."
                L "Let's go check out then!"
            elif True:
                "Lisa looks surprised for a moment, then beams."
                L "Really? That's great! I hoped you would."
                L "Let's go check out then."
            show bg black with dissolve
            show chelsea blank at right with dissolve
            show bg Shop with dissolve
            "You look at the pile of makeup and application tools in her hands. They all look very nice and very expensive."
            show chelsea sad
            pcname "That seems like a lot..."
            show L Blank at left with dissolve
            L "Oh. It does, but honestly, you need everything to pull the whole look together."
            show chelsea blank
            menu bakery_mallmakeup2:
                "Buy it all. ($200)" if Cash >= 200:
                    "You glance back at your reflection in the mirror. You really do look attractive."
                    pcname "Well, if I need everything..."
                    show L Happy at left
                    if bakeryagree >= 5:
                        L "It all really brings the whole look together. And wow, you look amazing!"
                    elif True:
                        L "You do. Trust me."
                    "Lisa takes your arm and leads you to the check-out counter."
                    show L Blank at left
                    show chelsea happy
                    "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                    "You leave feeling really confident about your purchase!"
                    $ Cash -=200
                    $ bakeryagree +=2
                    $ bakerymakeup = True
                    $ makeup=True
                    $ makeupbutton=True
                    $ acts -= 2
                    scene bg black with dissolve
                    $ LHappy = "Characters/Lisa/Happy.png"
                    $ LBlank = "Characters/Lisa/Blank.png"
                    $ LQuestion = "Characters/Lisa/Questioning.png"
                    $ LDisappoint = "Characters/Lisa/Disappointed.png"
                    $ LSad = "Characters/Lisa/Sad.png"
                    jump events_end_period
                "Buy the necessities. ($100)" if Cash >= 100:
                    "You look over the stuff in her arms then back at your reflection. You see what she means, but you can't imagine spending all that money on makeup."
                    pcname "I'll buy the lipstick, eyeliner, and a couple other things, but I can't get all of it."
                    if bakeryagree >= 5:
                        show L Disappoint at left
                        "Lisa frowns, glancing back down at the makeup in her arms."
                        show L Question at left
                        L "Are you sure you don't want to get everything? It won't look the same otherwise..."
                    elif True:
                        show L Disappoint at left
                        L "You really should consider getting everything. You don't want to do this half-assed."
                    menu bakery_mallmakeup3:
                        "Change your mind. ($200)" if Cash >= 200:
                            "You look back at yourself in the mirror. You {i}do{/i} look really attractive..."
                            pcname "Well... You have a point..."
                            show chelsea happy
                            pcname "I guess I'll buy it all."
                            show L Happy at left
                            "Lisa grins, passing you the stack of makeup items."
                            L "Perfect! I'll send you some tutorials on how to apply everything. You should wear it all the time, [pcname]. You'll look amazing."
                            "Lisa takes your arm and leads you to the check-out counter."
                            "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                            "You leave feeling really confident about your purchase!"
                            $ bakerymakeup = True
                            $ makeup=True
                            $ makeupbutton=True
                            $ Cash -=200
                            $ bakeryagree +=2
                            $ acts -= 2
                            scene bg black with dissolve
                            $ LHappy = "Characters/Lisa/Happy.png"
                            $ LBlank = "Characters/Lisa/Blank.png"
                            $ LQuestion = "Characters/Lisa/Questioning.png"
                            $ LDisappoint = "Characters/Lisa/Disappointed.png"
                            $ LSad = "Characters/Lisa/Sad.png"
                            jump events_end_period
                        "Stick to your decision. $100." if True:
                            pcname "I'm sure. Ready to check out?"
                            if bakeryagree >= 5:
                                show L Disappoint at left
                                "Lisa frowns, slowly putting a couple of the extra items back."
                                L "I guess so..."
                            elif True:
                                show L Disappoint at left
                                "Lisa rolls her eyes, sighing."
                                L "Yeah. I suppose."
                            show L Blank at left
                            "You join Lisa at the check-out counter and make your purchase."
                            "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                            show chelsea sad
                            "Maybe you {i}should{/i} have gotten the whole thing..."
                            $ bakeryhalfmakeup = True
                            $ makeup=True
                            $ makeupbutton=True
                            $ Cash -=100
                            $ bakeryagree +=1
                            $ acts -= 2
                            scene bg black with dissolve
                            $ LHappy = "Characters/Lisa/Happy.png"
                            $ LBlank = "Characters/Lisa/Blank.png"
                            $ LQuestion = "Characters/Lisa/Questioning.png"
                            $ LDisappoint = "Characters/Lisa/Disappointed.png"
                            $ LSad = "Characters/Lisa/Sad.png"
                            jump events_end_period
                "Buy nothing." if True:
                    show chelsea shocked
                    "You look over the stack of makeup in her arms. You just can't justify to yourself purchasing all of that."
                    show chelsea embarrassed
                    pcname "It looks nice, but I think I'll pass."
                    if bakeryagree >= 5:
                        show L Question at left
                        "Lisa cocks her head, confused."
                        L "But you look {i}amazing{/i}, [pcname]. I really think you should get it."
                    elif True:
                        show L Disappoint at left
                        "Lisa gives a deep sigh. You can see her struggling not to roll her eyes."
                        L "It's important to try new things, [pcname]. I know it's different, but you'll adjust."
                    show chelsea blank
                    menu bakery_makeup4:
                        "Change your mind and buy it all. $200." if Cash >= 200:
                            "You look back at your reflection. You can't deny that you look attractive."
                            show chelsea happy
                            pcname "I guess I could buy it... If only just to try them all out..."
                            if bakeryagree >= 5:
                                show L Happy at left
                                "Lisa grins."
                                L "I knew you'd come around!"
                            elif True:
                                show L Blank at left
                                "Lisa sighs in relief."
                                show L Happy at left
                                L "See? You just needed to adjust."
                            "Lisa takes your arm and leads you to the check-out counter."
                            show L Blank at left
                            "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                            "You leave feeling really confident about your purchase!"
                            $ bakerymakeup = True
                            $ makeup = True
                            $ Cash -= 200
                            $ makeup = True
                            $ makeupbutton = True
                            $ bakeryagree += 2
                            $ acts -= 2
                            scene bg black with dissolve
                            $ LHappy = "Characters/Lisa/Happy.png"
                            $ LBlank = "Characters/Lisa/Blank.png"
                            $ LQuestion = "Characters/Lisa/Questioning.png"
                            $ LDisappoint = "Characters/Lisa/Disappointed.png"
                            $ LSad = "Characters/Lisa/Sad.png"
                            jump events_end_period
                        "Change your mind and buy only the necessities. $100." if Cash >= 100:
                            "You glance at your reflection and then at the makeup in Lisa's arms. It wouldn't hurt to buy {i}some{/i} of it, right?"
                            pcname "I guess I can buy a few necessities...Not the whole thing, though."
                            if bakeryagree >= 5:
                                "Lisa smiles tightly, clearly disappointed, but it's outweighed by the relief on her face."
                                L "Oh. Well, I guess some is better than none..."
                                L "You'll have to come back and get the rest sometime soon, though. You'll really see what a difference it makes."
                            elif True:
                                L "I guess that's better than nothing..."
                                L "You really should come back and get the rest sometime, though. It makes a huge difference. You'll learn..."
                            show bg black with dissolve
                            show L Blank at left with dissolve
                            show bg Shop with dissolve
                            "You join Lisa at the check-out counter and make your purchase."
                            show chelsea happy at right with dissolve
                            "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                            "Maybe you {i}should{/i} have gotten the whole thing..."
                            $ bakeryhalfmakeup = True
                            $ makeup = True
                            $ makeupbutton = True
                            $ Cash -= 100
                            $ bakeryagree += 1
                            $ acts -= 2
                            scene bg black with dissolve
                            $ LHappy = "Characters/Lisa/Happy.png"
                            $ LBlank = "Characters/Lisa/Blank.png"
                            $ LQuestion = "Characters/Lisa/Questioning.png"
                            $ LDisappoint = "Characters/Lisa/Disappointed.png"
                            $ LSad = "Characters/Lisa/Sad.png"
                            jump events_end_period
                        "Stick to your decision." if True:
                            show chelsea sad
                            pcname "I really don't have the money. I'm sorry..."
                            if bakeryagree >= 5:
                                show L Disappoint at left
                                "Lisa frowns, disappointed."
                                show L Question at left
                                L "Aw. I'm sorry to hear that, [pcname]. I really think you should save up for it, though. It's really worth it."
                                "She sighs, placing the makeup back into their correct compartments."
                                show L Blank at left
                                L "I guess it's time for us to go, then."
                            elif True:
                                show L Disappoint at left
                                "Lisa scoffs, putting the makeup back into their correct compartments."
                                L "I can never rely on you, can I? You really ought to be saving up for these kinds of things. Your appearance is important."
                                L "Come on. Let's get you home."
                                show L Blank at left
                            show chelsea happy
                            "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                            show chelsea blank
                            "You consider what Lisa said about saving up as she drives you home."
                            $ bakeryagree -= 1
                            $ acts -= 2
                            scene bg black with dissolve
                            $ LHappy = "Characters/Lisa/Happy.png"
                            $ LBlank = "Characters/Lisa/Blank.png"
                            $ LQuestion = "Characters/Lisa/Questioning.png"
                            $ LDisappoint = "Characters/Lisa/Disappointed.png"
                            $ LSad = "Characters/Lisa/Sad.png"
                            jump events_end_period
        "I kind of like how I always look..." if True:
            L "But isn't this better? Just look how your eyes stand out. You look {i}amazing.{/i}"
            "You look back at your reflection. It {i}is{/i} pretty, but..."
            pcname "I'm just not sure it's really {i}me{/i}, you know?"
            L "I think you just need time to adjust to it. It's different, I know, but you really do look amazing, [pcname]."
            "You consider her words as you look over yourself in the mirror again."
            L "So? Thoughts?"
            menu bakery_mallmakeup5:
                "Buy it all. ($200)" if Cash >= 200:
                    "You glance back at your reflection in the mirror. You really do look attractive."
                    pcname "I guess I do look pretty good..."
                    if bakeryagree >= 5:
                        show L Happy at left
                        L "Right? See. You just needed some time to adjust."
                    elif True:
                        L "You do. Trust me."
                    show bg black with dissolve
                    "Lisa takes your arm and leads you to the check-out counter."
                    "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                    "You leave feeling really confident about your purchase!"
                    $ Cash -= 200
                    $ bakeryagree += 2
                    $ bakerymakeup = True
                    $ makeupbutton = True
                    $ makeup = True
                    $ acts -= 2
                    scene bg black with dissolve
                    $ LHappy = "Characters/Lisa/Happy.png"
                    $ LBlank = "Characters/Lisa/Blank.png"
                    $ LQuestion = "Characters/Lisa/Questioning.png"
                    $ LDisappoint = "Characters/Lisa/Disappointed.png"
                    $ LSad = "Characters/Lisa/Sad.png"
                    jump events_end_period
                "Buy the necessities. ($100)" if Cash >= 100:
                    "You look over the stuff in her arms then back at your reflection. You see what she means, but you can't imagine spending all that money on makeup."
                    pcname "I guess I can buy a few things..."
                    if bakeryagree >= 5:
                        "Lisa frowns, glancing back down at the makeup in her arms."
                        L "Are you sure you don't want to get everything? It won't look the same otherwise..."
                    elif True:
                        L "You really should consider getting everything. You don't want to do this half-assed."
                    menu bakery_mallmakeup6:
                        "Change your mind. ($200)" if Cash >= 200:
                            "You look back at yourself in the mirror. You {i}do{/i} look really attractive..."
                            pcname "Well... You have a point..."
                            pcname "I guess I'll buy it all."
                            "Lisa grins, passing you the stack of makeup items."
                            L "Perfect! I'll send you some tutorials on how to apply everything. You should wear it all the time, [pcname]. You'll look amazing."
                            show bg black with dissolve
                            "Lisa takes your arm and leads you to the check-out counter."
                            "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                            "You leave feeling really confident about your purchase!"
                            $ bakerymakeup = True
                            $ makeupbutton = True
                            $ makeup = True
                            $ Cash -= 200
                            $ bakeryagree += 2
                            $ acts -= 2
                            scene bg black with dissolve
                            $ LHappy = "Characters/Lisa/Happy.png"
                            $ LBlank = "Characters/Lisa/Blank.png"
                            $ LQuestion = "Characters/Lisa/Questioning.png"
                            $ LDisappoint = "Characters/Lisa/Disappointed.png"
                            $ LSad = "Characters/Lisa/Sad.png"
                            jump events_end_period
                        "Stick to your decision. ($100)" if True:
                            pcname "I'm sure. Ready to check out?"
                            if bakeryagree >= 5:
                                "Lisa frowns, slowly putting a couple of the extra items back."
                                L "I guess so..."
                            elif True:
                                "Lisa rolls her eyes, sighing."
                                L "Yeah. I suppose."
                            show bg black with dissolve
                            "You join Lisa at the check-out counter and make your purchase."
                            show bg Shop with dissolve
                            show chelsea blank at right with dissolve
                            show L Blank at left with dissolve
                            "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                            "Maybe you {i}should{/i} have gotten the whole thing..."
                            $ bakeryhalfmakeup = True
                            $ makeupbutton = True
                            $ makeup = True
                            $ Cash -= 100
                            $ bakeryagree += 1
                            $ acts -= 2
                            scene bg black with dissolve
                            $ LHappy = "Characters/Lisa/Happy.png"
                            $ LBlank = "Characters/Lisa/Blank.png"
                            $ LQuestion = "Characters/Lisa/Questioning.png"
                            $ LDisappoint = "Characters/Lisa/Disappointed.png"
                            $ LSad = "Characters/Lisa/Sad.png"
                            scene bg black with dissolve
                            jump events_end_period
                "Buy nothing." if True:
                    "You look over the stack of makeup in her arms. You just can't justify to yourself purchasing all of that, especially if you weren't a big fan of it to begin with."
                    pcname "It looks nice, but I think I'll pass."
                    show bg black with dissolve
                    show bg Shop with dissolve
                    show chelsea blank at right with dissolve
                    if bakeryagree >= 5:
                        show L Question at left with dissolve
                        "Lisa cocks her head, confused."
                        L "But you look {i}amazing{/i}, [pcname]. I really think you should get it."
                    elif True:
                        show L Disappoint at left with dissolve
                        "Lisa gives a deep sigh. You can see her struggling not to roll her eyes."
                        L "It's important to try new things, [pcname]. I know it's different, but you'll adjust."
                    menu bakery_makeup5:
                        "Change your mind and buy it all. ($200)" if Cash >=200:
                            "You look back at your reflection. It's a big change, but maybe she has a point."
                            show chelsea happy at right with dissolve
                            pcname "I guess I could buy it... If only just to try them all out..."
                            if bakeryagree >= 5:
                                show L Happy at left
                                "Lisa grins."
                                L "I knew you'd come around!"
                            elif True:
                                show L Blank at left with dissolve
                                "Lisa sighs in relief."
                                show L Happy at left
                                L "See? You just needed to adjust."
                                L "You should try to be less stubborn and trust others a little more."
                            "Lisa takes your arm and leads you to the check-out counter."
                            show L Blank at left
                            "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                            "You leave feeling really confident about your purchase!"
                            $ bakerymakeup = True
                            $ makeupbutton=True
                            $ makeup=True
                            $ Cash -=200
                            $ bakeryagree +=2
                            $ acts -= 2
                            scene bg black with dissolve
                            $ LHappy = "Characters/Lisa/Happy.png"
                            $ LBlank = "Characters/Lisa/Blank.png"
                            $ LQuestion = "Characters/Lisa/Questioning.png"
                            $ LDisappoint = "Characters/Lisa/Disappointed.png"
                            $ LSad = "Characters/Lisa/Sad.png"
                            jump events_end_period
                        "Change your mind and buy only the necessities. ($100)" if Cash >=100:
                            "You glance at your reflection and then at the makeup in Lisa's arms. It wouldn't hurt to buy {i}some{/i} of it, right?"
                            pcname "I guess I can buy a few necessities...Not the whole thing, though."
                            if bakeryagree >= 5:
                                show L Disappoint at left
                                "Lisa smiles tightly, clearly disappointed, but it's outweighed by the relief on her face."
                                show L Blank at left
                                L "Oh. Well, I guess some is better than none..."
                                L "You'll have to come back and get the rest sometime soon, though. You'll really see what a difference it makes."
                            elif True:
                                show L Disappoint at left
                                L "I guess that's better than nothing..."
                                L "You really should come back and get the rest sometime, though. It makes a huge difference. You'll learn..."
                            "You join Lisa at the check-out counter and make your purchase."
                            show chelsea happy
                            "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                            "Maybe you {i}should{/i} have gotten the whole thing..."
                            $ bakeryhalfmakeup = True
                            $ makeupbutton = True
                            $ makeup = True
                            $ Cash -= 100
                            $ bakeryagree += 1
                            $ acts -= 2
                            scene bg black with dissolve
                            $ LHappy = "Characters/Lisa/Happy.png"
                            $ LBlank = "Characters/Lisa/Blank.png"
                            $ LQuestion = "Characters/Lisa/Questioning.png"
                            $ LDisappoint = "Characters/Lisa/Disappointed.png"
                            $ LSad = "Characters/Lisa/Sad.png"
                            jump events_end_period
                        "Stick to your decision." if True:
                            show chelsea sad
                            pcname "I just don't really have the money for it. I'm sorry..."
                            show L Disappoint at left
                            if bakeryagree >= 5:
                                "Lisa frowns, disappointed."
                                L "Aw. I'm sorry to hear that, [pcname]. I really think you should save up for it, though. It's really worth it."
                                "She sighs, placing the makeup back into their correct compartments."
                                L "I guess it's time for us to go, then."
                                show L Blank at left
                            elif True:
                                "Lisa scoffs, putting the makeup back into their correct compartments."
                                L "I can never rely on you, can I? You really ought to be saving up for these kinds of things. Your appearance is important."
                                L "Come on. Let's get you home."
                            show chelsea blank
                            "As you leave the mall, you receive plenty of compliments from passer-bys on your makeup."
                            "You consider what Lisa said about saving up as she drives you home."
                            $ acts -= 2
                            $ bakeryagree -=1
                            $ shopmakeup=True
                            scene bg black with dissolve
                            $ LHappy = "Characters/Lisa/Happy.png"
                            $ LBlank = "Characters/Lisa/Blank.png"
                            $ LQuestion = "Characters/Lisa/Questioning.png"
                            $ LDisappoint = "Characters/Lisa/Disappointed.png"
                            $ LSad = "Characters/Lisa/Sad.png"
                            jump events_end_period

label bakery_makeup:
    show chelsea at right with moveinright
    "The bakery is surprisingly slow today. As the last customer steps out, Lisa pulls out her phone from behind the counter."
    show L Blank at left with moveinleft
    "You peer over her shoulder."
    pcname "What are you looking at?"
    L "Checking on my shipment. I ordered some new panties this week. Wanna see?"
    show chelsea happy
    pcname "Sure."
    show LPhone1 with dissolve
    "Lisa scrolls through her phone and pulls up a picture of her order. Three pairs of panties load on the screen, each one lacy and mature."
    pcname "Those are cute!"
    show L Happy at left
    L "Right? They should be here in a couple of days. Just a matter of waiting."
    hide LPhone1 with dissolve
    show L Blank at left
    "She glances at you, then pulls open her browser. She scrolls through an array of panties, stopping on a sexy black pair."
    show LPhone2 with dissolve
    L "I think you might like these."
    show L Happy at left
    L "I'll send you the link. This place has some really cute stuff, and they're pretty inexpensive, too."
    pcname "Thanks!"
    "Lisa smiles, closing out of the page as Keith steps out of his office."
    hide LPhone2 with dissolve
    show chelsea blank
    show L Blank at left
    if bakerymakeup == True:
        show Keith Blank with moveinleft
        "Keith pauses as he stops beside Lisa, taking a moment to look you over. His gaze lingers on your face."
        show chelsea confused
        if club == "track":
            pcname "Can I help you?"
        elif club == "cheer":
            pcname "What is it?"
        elif club == "yearbook":
            pcname "Y-Yes?"
        show Keith Happy
        show chelsea shocked
        BM "You look nice today. Keep it up. Customers like that."
        show chelsea blank
        "Keith turns to Lisa and gestures toward his office."
        BM "Lisa, I need to speak to you for a moment."
        show Keith Blank
        "He glances in your direction before walking back to his office. You get the feeling he doesn't want you to overhear their conversation."
        show L Happy at left
        L "Of course."
        L "[pcname], keep an eye on the register for me."
    elif bakeryhalfmakeup == True:
        show Keith Blank with moveinleft
        "Keith looks you over briefly as he steps up to Lisa, his gaze lingering on your face."
        show Keith Neutral
        BM "Nice lipstick."
        show chelsea shocked
        show Keith Blank
        "He turns to Lisa and gestures toward his office."
        show chelsea blank
        show Keith Neutral
        BM "Lisa. A word?"
        show Keith Blank
        "He glances to you as he speaks. You get the feeling he doesn't want you to hear what he's about to say."
        show L Happy at left
        L "Sure."
        "Keith steps back into his office."
        L "[pcname], watch the register for a bit, okay?"
    elif True:
        show Keith Confused with moveinleft
        show chelsea confused
        "Keith gives you a disgruntled look as he stops to examine you. You glance at Lisa in confusion."
        BM "Lisa. My office. Now."
        "Keith gives you a warning glance as he speaks. You get the feeling he doesn't want you eavesdropping."
        hide Keith Confused with moveoutleft
        show L Sad at left
        "He steps back into his office, slamming the door behind him. Lisa sighs."
        L "Keep an eye on the register, [pcname]."
    hide L Sad with moveoutleft
    show chelsea blank
    "Lisa steps into Keith's office, shutting the door behind her."
    menu bakery_eavesdrop:
        "Eavesdrop on their conversation." if True:
            "You glance around the empty bakery, making sure there are absolutely no customers before tiptoeing to Keith's office door."
            "You press your ear against the solid wood and listen in."
            if bakerymakeup == True:
                BM "You're doing a fantastic job, Lisa. I love the progress you've been making."
                if bakeryagree >= 7:
                    L "Thank you, sir. I aim to please you."
                elif True:
                    L "Thank you, sir. It hasn't been easy."
                "There's a pause, then the squeak of Keith's chair. You can hear his footsteps as he walks around the room."
                BM "I think such hard work deserves a reward."
                L "Y-Yes, sir. Thank you, sir."
            elif bakeryhalfmakeup == True:
                BM "You can do better than this, Lisa. I know you can."
                L "Yes, sir. I know."
                BM "I can't stand for a half-assed job. It's a nice start, but I want to see more results. You hear me?"
                L "Yes, sir. Of course."
                "There's a pause, then a sigh."
                BM "Come here. You've earned a small reward for your effort so far."
                "You hear the clacking of Lisa's heels as she walks around the room."
            elif True:
                BM "What the fuck is {i}that{/i}, Lisa? Well? Do you have anything to say for yourself?"
                L "I-I'm sorry, sir. I can do better."
                BM "I would hope so, because your efforts so far have been useless. You're goddamn useless, Lisa."
                L "Yes, sir. I know I am."
                "There's a pause, then the squeak of Keith's chair. You can hear his footsteps as he walks around the room."
                BM "I can't let this just go by, you understand."
                L "Yes, sir. I understand."
            show chelsea confused
            "There's some shuffling and a sound of movement. You can't quite make out what it is."
            menu bakery_eavesdrop2:
                "Crack open the door." if True:
                    $ corruption += 2
                    show chelsea blank
                    if club == "track":
                        "You know it's wrong, but your curiosity has gotten the best of you. You silently twist the door knob and peek inside."
                    elif club == "cheer":
                        "Unable to resist the urge, you silently twist the knob and peek inside."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        "This is wrong! So, so very wrong. But you're too afraid they'll notice something if you shut the door and leave now..."
                        "You silently twist the knob and peek inside, unable to contain your curiosity."
                    scene bg black with dissolve
                    if bakerymakeup == True or  bakeryhalfmakeup == True:
                        show bg KL11 with dissolve
                        "Lisa leans back on top of Keith's desk naked from the waist down except for the panties hooked loosely around her ankle. Her shirt is open, exposing her voluptuous breasts. What appears to be a lacy bra sits haphazardly on the side of the desk."
                        "Keith leans over her, his cock erect in his hand."
                    elif True:
                        show bg KL21 with dissolve
                        "Lisa kneels on the office floor, her collar shirt unbuttoned halfway down. Keith stands in front of her, his cock erect."
                    if club == "track":
                        "You stare in shock. This can't be happening, right?"
                    elif club == "cheer":
                        "Your eyebrows raise, but you can't tear your gaze away."
                    elif club == "yearbook":
                        "You almost can't believe what you're seeing and need to press a hand over your mouth to muffle the noise of surprise that nearly gives you away."
                        "You know you should leave, but you're afraid that they'll see you if you make any movements."
                    if bakerymakeup == True or  bakeryhalfmakeup == True:
                        "Keith runs a hand up her stomach to her breast and gives it a hard squeeze. She lets out a small whimper, squirming in delight."
                        BM "There we go. Feels good, doesn't it?"
                        "Lisa nods eagerly as he continues to toy with her nipple, squeezing the hard nub between his fingers."
                        show bg KL12 with dissolve
                        "He presses his cock to her cunt, grinding against the slit as his other hand joins the assault on her breasts."
                        L "Yes, sir."
                        "Lisa thrusts her hips in his direction, grinding against his erection. Keith leans forward and bites down on one of her breasts."
                        "Lisa tilts her head back in a soft moan."
                        BM "Not so loud. [pcname] will hear you."
                        show bg KL13 with dissolve
                        if bakeryagree >= 7:
                            "Your breathing hitches at the sound of your name. You press your lips together, hoping to keep quiet, but desperately wanting to hear it again."
                            "You become aware of the moisture growing between your thighs and squirm a little, trying to resist the urge to touch yourself lest a customer come in and see."
                        elif True:
                            "The sound of your name in such an intimate moment startles you. You grip the door handle and hold your breath, unable to look away."
                        "Lisa nods in understanding, pressing her lips together tightly."
                        show bg KL14 with dissolve
                        "Keith begins to push himself into her, increasing the frequency of her whimpers."
                        BM "You like that, slut? Is that what you needed?"
                        L "Y-Yes, sir. Oh, God."
                        "Lisa throws her head back as Keith thrusts deeply into her, rocking her against the edge of the desk."
                        "You hear the wet slap of his cock as he pounds in her. A part of you realizes just how wet and wanting she is, how she must have been for some time for him to be able to slip into her so easily."
                        "Keith seems to realize it, too."
                        BM "Fuck..."
                        show bg KL15 with dissolve
                        "The desk creaks as Keith picks up the pace. His fingers dig into Lisa's thighs for leverage. You're sure they'll leave bruises."
                        "Lisa squeezes her eyes tightly. She grips Keith's arms for support."
                        L "Yes, yes, yes, yes, {i}yes-{/i}"
                        if bakerymakeup == True:
                            show bg KL16 with dissolve
                            "Lisa arches her back with a muffled cry as she orgasms, her hips bucking frantically against Keith."
                            "He continues to slam into her, rocking the desk with his movements."
                            "Keith's veins are visible from his arms as he grasps Lisa's thighs, his body quivering slightly as he finishes inside of her with a few grunts."
                            "It takes him much longer to finish than Lisa, but she doesn't seem to mind, moaning and grinding under him with every thrust."
                            "Eventually his body quivers, and Keith finishes inside of her with a few sharp grunts."
                        elif True:
                            show bg KL17 with dissolve
                            "As Lisa begins to arch her back toward Keith, he pulls out, leaving her hips bucking the air. She lets out a moan of disappointment."
                            L "But sir-"
                            BM "Work harder and maybe next time I'll let you cum."
                            "Lisa pouts, but nods in understanding."
                            L "Yes, sir."
                            show bg black with dissolve

                            "She starts to rise from the desk. Keith presses a hand on her breasts, pushing her down on her back against the hard desk surface."
                            BM "Did I say you could leave?"
                            "Keith grabs her by her ankles and yanks her to the very edge of the desk. He stands over her, his cock dripping with precum and Lisa's fluids."
                            BM "Finish the job."
                            "Lisa, eager to please, grabs Keith's cock in one hand, stroking the thick erection. Her other hand cups his balls and massages them between her manicured fingers."
                            BM "Mmph. Fuck. Yeah, like that."
                            "Keith grinds against her touch, his hands busy with groping and massaging her breasts."
                            "They remain like that for some time, Lisa's hands eagerly pleasing his cock and balls while Keith squeezes and pinches her breasts."
                            "He grasps Lisa's tits tightly, squeezing the soft flesh as his erection quivers between Lisa's fingers, spurting white cum across her belly."
                    elif True:
                        BM "I guess you really are only good for one thing."
                        "Keith grabs Lisa by her hair, bending her head back to look at him."
                        BM "What? You just gonna sit there?"
                        show bg KL25 with dissolve
                        "Lisa, as if struck, jumps forward, kissing Keith's cock and balls."
                        "Her tongue traces over his thick erection slowly, leaving a trail of saliva over the throbbing shaft."
                        show bg KL23 with dissolve
                        "She dips her head to his balls, taking the sensitive skin into her mouth. She sucks lightly, her lips massaging the skin. Keith lets out a low moan from the back of his throat."
                        "Her tongue laps over the balls and up the backside of his erection, coating each inch in her saliva."
                        show bg KL22 with dissolve
                        "Unable to take it anymore, Keith yanks her back by her hair. Lisa lets out a cry. It's quickly muffled as he thrusts his cock inside of her mouth."
                        show bg KL25 with dissolve
                        "Lisa stares up at him as she slowly takes his cock further into her mouth, inch by inch, until it's settled deep in her throat."
                        "Keith lets out a sharp breath."
                        BM "Oh, fuck..."
                        "Still grasping her hair, Keith thrusts inside of her mouth."
                        "You watch as his balls slap against her chin while he fucks her face."
                        "Lisa clenches and unclenches her throat around his cock, taking in his thickness with ease."
                        "Keith crushes her face against him as he bucks against her mouth. Her moans are muffled around his cock."
                        show bg KL26 with dissolve
                        "He lets out a soft grunt as he cums in her throat."
                        show bg KL27 with dissolve
                        "As Keith pulls out, some cum trails from his tip, dripping onto Lisa's collar."
                        "Keith shoves himself back into his pants as Lisa swallows his load."
                        show bg black with dissolve
                    $ bakery_eavesdrop == True
                    show bg Bakery with dissolve
                    show chelsea embarrassed at right with dissolve
                    "While they catch their breath, you hear the bell over the front door ring and rush to the register, hoping neither noticed you watching them."
                    "It's only after you've finished with the customer and they've left that Lisa steps out of Keith's office."
                    show L Blank at left with moveinleft
                    "She resumes her place at the register, using her phone's camera to fix herself up."
                    if bakerymakeup == True:
                        show L Happy at left
                        "Once she's decent, Lisa gives you a pleasant smile."
                        L "You really do look amazing, [pcname]. That makeup does wonders for you!"
                        show chelsea happy
                        "You can't help but smile at her compliment."
                    elif bakeryhalfmakeup == True:
                        "Once she's decent, Lisa glances you over."
                        show L Happy at left
                        L "You look nice, [pcname], but I think maybe we should get you the full set next time."
                        L "It'll really make all the difference. Trust me."
                        "You aren't sure whether she meant for it to be a compliment or not. You simply nod."
                    elif True:
                        "Once she's decent, Lisa looks you over, scrutinizing your appearance. She brushes your hair behind your ear, her fingers trailing across your jawline."
                        show L Question at left
                        L "It's such a shame, [pcname]. You have such a nice bone structure, but you're wasting it."
                        L "You would look so much nicer with the makeup we were looking at, [pcname]. I really think you should consider putting more effort into your appearance."
                        L "Looks will get you far in life. Trust me, I know."
                    show L Blank at left
                    show chelsea blank
                    "There's an awkward pause as Lisa glances around the bakery, making sure everything is clean and in order before returning to her phone."
                    menu bakery_lisaconfront_choice:
                        "Confront Lisa about the manager." if True:
                            if club == "track":
                                pcname "So, I saw what happened."
                                L "Hm?"
                                pcname "I saw you two fucking in the office."
                            elif club == "cheer":
                                show chelsea confused
                                pcname "So. You and Keith, huh?"
                                L "What?"
                                "You nod your head back toward the office."
                                pcname "Keith? Really?"
                            elif club == "yearbook":
                                show chelsea confused
                                pcname "S-So, um, Lisa... You and Keith...?"
                                L "Hm?"
                                pcname "I saw what happened, um, in the office. Just now."
                            "Lisa's hands freeze on her phone, the color draining from her face at once."
                            show L Question at left
                            L "...You saw?"
                            show chelsea blank
                            pcname "...Yeah."
                            show L Blank at left
                            "Lisa clears her throat, tossing her hair over her shoulder. A flush of color rushes to her face."
                            L "You know, [pcname], women have needs, too. We're allowed to have our sexual desires met just like anyone else."
                            L "Don't you ever have those needs, [pcname]?"
                            if club == "track":
                                show chelsea confused
                                pcname "Er, I guess so, but-"
                            elif club == "cheer":
                                pcname "Of course I do!"
                            elif club == "yearbook":
                                show chelsea embarrassed
                                pcname "W-Well- I-I- Um-"
                            L "Then why be so shy about it? Are they not being met? It's nothing to be ashamed of. We all need to let loose sometimes."
                            show L Happy at left
                            show chelsea blank
                            L "Don't you agree?"
                            menu bakery_lisaagree:
                                "I guess you have a point." if True:
                                    $ corruption +=1
                                    if bakerymakeup == True:
                                        "Lisa reaches out to touch your cheek. She caresses the skin lightly before pulling away."
                                        L "See? I knew you'd agree with me."
                                        show L Blank at left
                                        L "You look so hot in that makeup already. I'm sure it won't be long until someone else realizes it, too."
                                        L "Men really can't resist a pretty face."
                                        show L Happy at left
                                        "She laughs a little, returning to her phone."
                                    elif bakeryhalfmakeup == True:
                                        "Lisa smiles."
                                        L "See? What I have- what {i}you{/i} have- are both very normal reactions."
                                        show L Blank at left
                                        L "If you focus a little more on your appearance, I'm sure someone will help you meet your needs, too."
                                        "Lisa gives you another smile before returning to her phone."
                                    elif True:
                                        show L Blank at left
                                        "Lisa's eyes flicker over your facial features."
                                        show L Happy at left
                                        L "See? It's natural to want our needs met."
                                        L "If you focus more on your appearance, I'm sure you'll be able to have yours met, too."
                                        "Lisa gives you a little wink before returning to her phone."
                                    show L Blank at left
                                    "Throughout the rest of your shift, you think about what Lisa said, not to mention what you saw her do with Keith."
                                    "You can't even bring yourself to look Keith in the eye when he sends you both home for the night."
                                    "Still, perhaps there's some truth to what Lisa said. After all, it's normal to have needs and want them met, right?"
                                    $ bakeryagree +=2
                                    $ bakery_lisaconfront = True
                                    scene bg black with dissolve
                                    jump events_end_period
                                "No. You were being really inappropriate." if True:
                                    show chelsea angry
                                    if bakeryagree >= 5:
                                        show L Question at left
                                        L "Inappropriate? This isn't like you, [pcname]..."
                                        L "I can't help it if our manager wants me. And who am I to say no to him?"
                                        show L Blank at left
                                        show chelsea blank
                                        L "After all. He must want me for a reason."
                                        "She glances pointedly at your face before walking off toward the back in search of more work to do."
                                    elif True:
                                        show L Disappoint at left
                                        "Lisa rolls her eyes."
                                        L "You're so naive, [pcname]."
                                        L "Maybe if you were prettier and someone actually wanted you that way, you'd understand..."
                                        show chelsea angry
                                        "Lisa sighs, walking off toward the back to find something to do."
                                        show chelsea blank
                                        "You watch her go, awkward and uncomfortable."
                                        show L Blank at left
                                    "You avoid looking at both Lisa and Keith throughout the rest of your shift and are grateful when the time comes to go home."
                                    $ bakeryagree -=2
                                    $ bakery_lisaconfront = True
                                    scene bg black with dissolve
                                    jump events_end_period
                        "Keep quiet." if True:
                            "As much as you want to bring up what happened, you aren't sure how best to approach it."
                            "Maybe it's better to pretend it never happened anyway. You could get into some big trouble if they knew you'd listened in on them."
                            "Although, you're sure they would get into just as much, if not more trouble, if something like this were to get out."
                            "You refrain from mentioning it for the rest of your shift, although you can't bring yourself to look either of them in the eye."
                            scene bg black with dissolve
                            jump events_end_period
                "Stop eavesdropping." if True:
                    "Maybe it's best to leave before they find you outside of the door."
        "Man the register." if True:
            pass
    "You step behind the register and await customers, trying to ignore any noise that comes from Keith's office."
    "You can only imagine the trouble you would get into if they caught you eavesdropping. Besides, it's none of your business."
    "Their meeting takes longer than you thought."
    show L Blank at left with moveinleft
    if bakerymakeup == True:
        "Lisa emerges from Keith's office nearly an hour later, her hair messier than you remember. She notices your staring and quickly combs her fingers through the strands."
    elif bakeryhalfmakeup == True:
        "Lisa emerges from Keith's office thirty minutes later, a slight pout on her lips."
    elif True:
        show L Sad at left with moveinleft
        "Lisa emerges from Keith's office twenty minutes later, her eyes red and swollen, as though she's been crying. You ignore the small stain on the collar of her shirt."
    menu bakery_ask:
        "Ask her about the meeting." if True:
            show chelsea happy
            pcname "How did the meeting go?"
            if bakerymakeup == True:
                show L Blank at left
                "Lisa seems taken aback at first, but smiles."
                show L Happy at left
                L "It was fine. We were just discussing some exciting changes that are coming to the bakery."
                "Her gaze lingers on your face as she talks. Her smile widens."
                show chelsea confused
                pcname "Changes? What kind?"
                "Lisa presses a finger to her lips."
                L "That's a secret."
            elif bakeryhalfmakeup == True:
                show L Blank at left
                "Lisa seems surprised by your question, but shrugs."
                L "It was alright. Just discussing some changes to be made around the bakery."
                "Her gaze lingers on your face as she talks. She smiles slightly."
                show chelsea confused
                pcname "Changes? What kind?"
                L "Oh, nothing yet. I'm sure you'll find out eventually."
            elif True:
                show L Disappoint at left
                "Lisa sighs."
                L "It was fine. We just talked about some changes that need to be made around the bakery."
                "Her gaze lingers on your face as she talks. Her lips are set in a deep frown."
                show chelsea confused
                pcname "Changes? What kind?"
                L "Keith wants his employees to maintain a certain image. I'm sure you'll hear about it soon enough."
        "Keep quiet." if True:
            "You consider asking about the meeting for a brief moment but decide against it. It's really none of your business."
    "Lisa reclaims her position at the register and fixes herself up on her phone."
    if bakerymakeup == True:
        show L Happy at left
        "Once she's decent, Lisa gives you a pleasant smile."
        L "You really do look amazing, [pcname]. That makeup does wonders for you!"
        show chelsea happy
        "You can't help but smile at her compliment."
    elif bakeryhalfmakeup == True:
        "Once she's decent, Lisa glances you over."
        show L Happy at left
        L "You look nice, [pcname], but I think maybe we should get you the full set next time."
        L "It'll really make all the difference. Trust me."
        show L Blank at left
        "You aren't sure whether she meant for it to be a compliment or not. You simply nod."
    elif True:
        "Once she's decent, Lisa looks you over, scrutinizing your appearance. She brushes your hair behind your ear, her fingers trailing across your jawline."
        show L Question at left
        L "It's such a shame, [pcname]. You have such a nice bone structure, but you're wasting it."
        show L Disappoint at left
        L "You would look so much nicer with the makeup we were looking at, [pcname]. I really think you should consider putting more effort into your appearance."
        show L Happy at left
        L "Looks will get you far in life. Trust me, I know."
    show L Blank at left
    "Lisa looks back at her phone, scrolling through one of the apps. You can't seem to find any other work to do around the bakery, so you join her, peering down at your own social media."
    show L Happy at left
    L "So, [pcname], do you have a boyfriend?"
    show chelsea shocked
    if damienrelate == "dating":
        show chelsea embarrassed
        pcname "Yeah, I do."
        L "Aw, how sweet."
        show L Blank at left
        L "I'm glad to see you aren't ashamed of your desires."
        "She gives you a little wink before returning to her phone."
    elif violetrelate == "Sub" or violetrelate == "Dom":
        pcname "I have a girlfriend, actually."
        "Lisa smiles."
        L "Really? How progressive."
        show L Blank at left
        L "I'm happy to see you aren't ashamed of your desires at least."
        "She gives you a little wink before returning to her phone."
    elif mattchain > 1:
        if defymatt == True:
            show chelsea blank
            "Your stomach twists at the thought of Matt. You press your lips together and look away."
            "Lisa seems to misunderstand your reaction."
        elif True:
            show chelsea embarrassed
            pcname "I wouldn't call him that."
            "Lisa smirks."
        show L Blank at left
        L "Interesting."
        L "Well, I'm glad you aren't ashamed of your desires at least."
        show L Happy at left
        show chelsea blank
        "She gives you a little wink."
    elif True:
        show chelsea blank
        pcname "No, I'm not seeing anyone at the moment."
        show L Question at left
        L "Really? I'm surprised. You're so pretty..."
        show L Blank at left
        L "Well, their loss, I suppose."
        L "Even if you don't have anyone to share them with, you shouldn't be afraid to show your desires, [pcname]."
        show L Happy at left
        L "Sex is important, even outside of a relationship."
        show chelsea confused
        "You give her a slightly confused look."
        pcname "Where's that coming from?"
        "Lisa shrugs, smiling."
        L "Just thought it should be said. That's all."
    show chelsea blank
    show L Blank at left
    "Lisa's words hang in the back of your mind throughout the rest of your shift."
    "There's nothing wrong with having desires, right? Maybe you shouldn't be so shy about them."
    scene bg black with dissolve
    jump events_end_period

label bakery_catalogue:
    show chelsea embarrassed at right with moveinright
    "Your shift has gone by in a flash. The bakery has been busy all day and you've hardly had a moment to yourself."
    show chelsea blank
    "As the store winds down for the night, you finish cleaning the last load of dishes in the back before stepping out to the counter."
    "Lisa seems to have finished cleaning the rest of the store. Everything is left squeaky clean and presentable for tomorrow."
    pcname "Thanks for taking care of the front, Lisa."
    show L Happy at left with moveinleft
    "Lisa sits in a seat near the counter, flipping through a catalogue. She smiles up at you."
    L "No problem. Thank you for getting the dishes."
    show L Blank at left
    L "Come over here, [pcname]. I have something I want to show you."
    "You take a seat beside Lisa as she moves the catalogue between you. Various shades of lipstick and eyeshadow jump out at you from the page."
    L "See anything you like?"
    "You flip through the makeup section of the catalogue. There's plenty to grab your attention."
    show chelsea happy
    pcname "Yeah. These are pretty cute."
    "You point out a couple shades of lipstick and eyeshadow from the catalogue. Lisa nods."
    show L Happy at left
    show chelsea blank
    L "They are, but I think you'd look better in something more like this."
    "Lisa points to a more sultry set of red lipsticks."
    show chelsea confused
    pcname "Wouldn't they clash with my hair?"
    show L Blank at left
    show chelsea blank
    "Lisa purses her lips, taking a strand of your hair between her fingers."
    L "Hmm. Well, it {i}would{/i} go better with {i}blonde{/i} hair..."
    show L Happy at left
    L "But that doesn't mean you wouldn't look amazing anyways!"
    L "You should get them and try them out. I bet you'll look super cute."
    show L Blank at left
    L "Maybe we can get something for your eyes, too. These eyeliners look really nice. And this mascara does wonders- I use it all the time."
    L "And of course you can't go wrong with some good foundation."
    show L Happy at left
    "Lisa giggles."
    show L Blank at left
    L "So, what do you say?"
    pcname "Well..."
    menu bakerymakeupcatalogue:
        "Purchase makeup. $200." if Cash >= 200:
            "You look over the set of lipsticks as well as the other makeup Lisa pointed out. It wouldn't hurt to try them out, would it?"
            show chelsea happy
            pcname "Okay. Yeah, I guess I can try them out."
            if bakeryagree >= 7:
                show L Happy at left
                "Lisa claps her hands excitedly."
                L "Wonderful! I'll put an order in for you. That'll come to..."
            elif True:
                "Lisa looks surprised for a moment, then quickly catches herself."
                L "Sorry. I just didn't expect you to agree so fast..."
                L "Let me just get you a total. It'll be..."
            show L Blank at left
            show chelsea blank
            "Lisa begins circling the makeup she chose, writing down a balance on the back of the catalogue."
            L "Two-hundred dollars."
            "You nod, fishing out your wallet and passing her the cash. Your wallet suddenly feels so much lighter."
            show L Happy at left
            L "You're going to look amazing, [pcname]. I can't wait to see the result!"
            show chelsea happy
            if club == "track":
                "You smile back at her. It's your first time buying makeup, and you're feeling pretty excited about it!"
            elif club == "cheer":
                "You smile back at her. You can't wait to see how sexy you look in your new makeup!"
            elif club == "yearbook":
                "You smile back, trying to hide your nerves. You hope you'll look as cute as she says you will..."
            $ bakeryagree +=1
            $ Cash -=200
            $ makeupbutton=True
            $ bakerymakeup2 = True
        "Pass." if True:
            show chelsea sad
            "As you look over the catalogue, you realize just how pricy everything is. You can't really justify spending all that money on makeup."
            show chelsea blank
            pcname "I think I'm going to pass."
            if bakeryagree >= 7:
                show L Disappoint at left
                "Lisa frowns in disappointment."
                show L Question at left
                L "How come?"
            elif True:
                "Lisa looks unimpressed. She must have been anticipating your answer."
                L "Figures."
                show L Disappoint at left
                L "What's your reason this time?"
            show chelsea sad
            pcname "It's just really expensive."
            show L Question at left
            L "That's it?"
            show L Blank at left
            L "Here, I can pay for it."
            show chelsea shocked
            pcname "What? No, Lisa, I can't ask you to do that-"
            L "You're not asking. I'm offering."
            pcname "That's like, over a hundred dollars worth of-"
            L "Two-hundred."
            pcname "Two-hundred?!"
            L "Relax. You can make it up to me."
            show chelsea confused
            pcname "How?"
            L "Hmm..."
            "Lisa taps her chin, thinking it over."
            show chelsea blank
            if bakeryagree >= 7:
                L "You have to wear it all the time, from the moment it comes in. No ifs, ands, or buts!"
            elif True:
                L "In addition to wearing it all the time from the moment it comes in, you also have to detail clean all of the baking equipment for a month, no matter who's side work it is."
            show chelsea embarrassed
            pcname "I don't think that's really worth two-hundred dollars..."
            show chelsea shocked
            L "Do you want me to tack on more?"
            show chelsea sad
            pcname "Well... Not really..."
            L "Then it's settled."
            show L Happy at left
            L "You're going to look so cute, [pcname]. Trust me."
            pcname "If you say so..."
            show chelsea blank
            "Lisa circles items in the catalogue, making a list for herself. You're not comfortable with the situation, but if she wants you to wear it that badly, you aren't going to put up a fuss..."
            $ bakeryagree -=1
            $ bakerymakeup2 = True
    show chelsea blank
    show L Blank at left
    "Keith calls you both over for a final end-of-the-night meeting before dismissing you both from work."
    "All in all, it wasn't a bad day."
    scene bg black with dissolve
    jump events_end_period

label bakery_shoppingwLisaA:
    $ shoppingwlisa = True
    jump bakery_shoppingwLisa

label bakery_shoppingwLisaB:
    $ shoppingwlisa = True
    jump bakery_shoppingwLisa

label bakery_shoppingwLisaC:
    $ shoppingwlisa = True
    jump bakery_shoppingwLisa

label bakery_shoppingwLisa:
    $ shoppingwlisa = True
    $ LHappy = "Characters/Lisa/Casual/Happy.png"
    $ LBlank = "Characters/Lisa/Casual/Blank.png"
    $ LQuestion = "Characters/Lisa/Casual/Questioning.png"
    $ LDisappoint = "Characters/Lisa/Casual/Disappointed.png"
    $ LSad = "Characters/Lisa/Casual/Sad.png"
    show chelsea happy at right with moveinright
    "The town seems busy today, lively with people as you meander through the crowd."
    "Before you can decide where to go, a familiar voice calls out to you."
    L "[pcname]!"
    "You turn around to find Lisa bracing through the crowd, making her way toward you."
    show L Happy at left with moveinleft
    show chelsea shocked
    pcname "Oh! Hey, Lisa."
    show chelsea happy
    pcname "I didn't expect to see you here."
    L "I live a couple of blocks away. I was actually just about to head out to the mall."
    L "Would you like to join me?"
    if bakeryagree >= 5:
        "You smile and nod, a little excited to spend more time with Lisa."
    elif True:
        "You try to think of an excuse, but nothing comes to mind. Against your better judgement, you shrug."
    pcname "Sure."
    L "Great!"
    show L Blank at left
    show chelsea blank
    "Lisa leads you back to her car. You join her, enjoying the upbeat pop music she blasts over the car stereo."
    "You both find yourselves singing along to one of the catchy beats until she parks outside and leads you toward the widespread building."
    "The mall is equally lively, filled with eager shoppers as they make their rounds through the upscale stores."
    "Lisa guides you through a few of the stores, pointing out cute skirts, tops, and other items she finds attractive while you both shop."
    "You both find yourself inside of a classy shoe store. Brand name heels, sandals, and flats decorate the luminescent white shop."
    "You sit and watch as Lisa tries on a few pairs of heels, admiring them on her slender legs."
    "Suddenly, she looks up, a pair catching her eye."
    L "[pcname], why don't you try those on?"
    show chelsea shocked
    "You turn to find a striking pair of bright red stilettos. They're far taller than anything you've worn before, and a part of you wonders how anyone can walk comfortably in those."
    show chelsea embarrassed
    pcname "They're really... impressive."
    show chelsea blank
    "Lisa surveys your feet for a moment before plucking a box off of the shelf, pulling out one of the red heels."
    show L Happy at left
    L "Try it on! It'll be fun."
    "You shrug, taking off your shoes. If it'll make her happy, why not?"
    "You place the red heels on your feet and stand. You're a little wobbly at first, but you grow used to them the longer you walk around in them."
    show L Blank at left
    L "Wow..."
    show L Happy at left
    L "Those look stunning! [pcname], you have to get them."
    "You turn a little in them, reluctant."
    show chelsea sad
    pcname "I'm not sure..."
    L "Go look at yourself in the mirror. Your calves look {i}amazing{/i}."
    show chelsea blank
    "You follow her advice, walking over to one of the full-length mirrors beside a display of fashionable sandals."
    "Although you're hesitant to admit it, you can't deny that you feel a surge of confidence run through you at the sight of your reflection."
    "The heels definitely help bring out the slender curve of your calves. They make your legs appear longer, too."
    show L Blank at left
    show chelsea happy
    if club == "track":
        "You strut a little in front of the mirror, enjoying the feel of confidence as you strike small poses in the reflection."
        "They're definitely more feminine than you're used to, but you've kind of grown to like that. Maybe you can be confident {i}and{/i} feminine at the same time?"
    elif club == "cheer":
        "You strike a few sultry poses in the mirror, admiring how sexy your legs appear in these new heels."
    elif club == "yearbook":
        "You almost want to pose in the mirror to see how you might look in other positions, but push the thought back with slight embarrassment."
    "Lisa steps into the reflection behind you, her eyes trailing over your legs."
    show L Happy at left
    L "You look so sexy, [pcname]. You {i}have{/i} to get them!"
    show chelsea embarrassed
    pcname "I do look really good..."
    show chelsea blank
    L "Right?! Let's go buy them!"
    menu bakeryheels:
        "Purchase heels. ($100)" if Cash >= 100:
            $ corruption += 1
            "You glance at the price tag on the box. They're pretty expensive, but you can't bare to part yourself from these heels."
            show chelsea happy
            pcname "Alright."
            show chelsea sad
            show L Blank at left
            "With a slight sadness, you remove the heels, placing them back in the box before putting on your old shoes. They just don't feel as impressive compared to the heels."
            show chelsea happy
            "You purchase them at the check-out counter, your mind wandering to all of the outfits at home you can pair them with."
            "You follow Lisa out of the store, swinging the bag happily over your arm."
            $ Cash -=100
        "Don't purchase heels." if True:
            show chelsea sad
            "Reluctantly, you look back at the price tag on the box with a frown. $100 is pretty steep for a pair of heels, especially ones you won't wear all the time..."
            pcname "Ah... No, it's okay. I'll get them some other time."
            "A little sad, you return to one of the plush sitting chairs and remove the heels from your feet."
            show L Question at left
            L "What? Why?"
            show chelsea embarrassed
            "You look back at the price tag, embarrassed."
            pcname "I mean, they're pretty expensive. I don't really have the money for them right now."
            show L Disappoint at left
            show chelsea confused
            L "Oh, is that all?"
            show chelsea shocked
            "Before you can put the lid back over the heels, removing them from your sight forever, Lisa plucks the box from your hands."
            if bakeryagree >= 7:
                show L Happy at left
                L "I'll buy them for you. Don't worry about it."
            elif True:
                show L Blank at left
                L "I'll buy them."
            "You look up at her, shocked and a little embarrassed."
            pcname "What? No, Lisa. I can't ask you to do that..."
            if bakeryagree >= 7:
                L "You're not asking. I'm insisting. This is what friends do, right?"
                "She gives you a warm smile, placing the lid back on top of the box."
            elif True:
                L "You're not. You should really prioritize your appearance more, [pcname]. Consider this a sort of loan."
                L "You can make it up to me by focusing more on how you look. Okay?"
                show L Disappoint at left
                "She scrutinizes your current shoes a little as you put them back on. She places the lid back over the box of heels."
            show L Blank at left
            show chelsea blank
            "Noticing your reluctance, Lisa crouches down beside you."
            if club == "track":
                L "You know, [pcname], there's a lot to be said about strength in femininity."
                L "A lot of people look down on us for wanting to look good, but there is a lot of work that goes into appearances."
                show L Happy at left
                L "In fact, a lot of very strong women- politicians, athletes, what have you- still dress up in heels and dresses and makeup on a daily basis."
                L "There's nothing wrong with embracing your femininity, so I don't want you to feel bad for doing it. Okay?"
            elif club == "cheer":
                L "You know, [pcname], even though you're still in high school, you're older than a lot of the other girls in your class."
                L "They might not have reached a maturing point yet, but it feels like you have. It's only natural for you to want to be a little more grown up than the other girls."
                show L Happy at left
                L "Instead of trying to be like the rest of the crowd, you should embrace this change. The transition into womanhood is an exciting time. You should enjoy it to the fullest."
            elif club == "yearbook":
                L "You know, [pcname], I think that trying out new things- makeup, clothes, shoes- is all very brave."
                L "I know change is always hard to live with, but being able to embrace it despite your fears is an act of true courage."
                show L Happy at left
                L "Making big changes to your appearance can be scary, but the more you do it, I hope you'll find that it can be a lot of fun, too."
                L "You're doing a wonderful job, [pcname]."
            show chelsea embarrassed
            "You can't help but feel touched at her kind words toward you. You find yourself rendered speechless, unsure of how to thank her properly."
            "Lisa smiles, seeming to understand. She stands back up, motioning for you to join her."
            show L Blank at left
            L "Come on. Let's check out."
            show chelsea happy
            "You follow behind, both surprised and grateful as Lisa pays for the heels and passes the shopping bag into your hand."
            pcname "Thank you so much, Lisa. This was very kind of you."
            if bakeryagree >= 7:
                show L Happy at left
                L "Don't mention it! I'm happy to help a friend out."
                "You smile, holding the bag of shoes to your chest."
            elif True:
                show chelsea blank
                L "Just remember what I said. I only did it to help you out."
                "You nod in understanding."
    show chelsea blank
    show L Blank at left
    "You both gracefully make your way out of the mall."
    "Upon stepping outside you're greeted with dark clouds looming overhead. The smell of damp air surrounding you."
    L "It's getting pretty late. I guess I should drive you home now, huh?"
    pcname "Oh, you don't have to. I can get a cab--"
    show L Question at left
    L "Absolutely not! Let me drive you home. I insist."
    pcname "Well, okay. If that's okay with you."
    show L Happy at left
    show chelsea shocked
    "Lisa smiles. She hooks arms with you, leading you back out to the parking lot. As you step out, a crash of thunder causes you to jump."
    L "Of course it is. I can't let you wait in this weather."
    show chelsea blank
    show L Blank at left
    "Luckily, you both reach the car before the rain really starts to come down. Lisa turns up the heat and starts the GPS as she begins to drive you home."
    L "So, how are you liking work so far?"
    menu bakerywork:
        "I like it!" if True:
            show chelsea happy
            show L Happy at left
            "Lisa smiles."
            L "I'm glad to hear that! We really want you to fit in here, [pcname]."
            if bakery_eavesdrop == True:
                show chelsea blank
                "As you think back to what happened in Keith's office, you begin to wonder what that means."
            elif True:
                "You smile, happy to feel included in the bakery's little family."
        "It's work." if True:
            show L Disappoint at left
            "Lisa frowns."
            show L Question at left
            L "Has something been bothering you at work, [pcname]?"
            if bakery_eavesdrop == True:
                "You think back to what happened in Keith's office."
            elif True:
                "You shrug."
                pcname "Just rude customers and stuff. You know."
                show L Blank at left
                "Lisa nods in understanding."
    if bakery_eavesdrop == True and bakery_lisaconfront == False:
        show chelsea blank
        show L Blank at left
        "You didn't want to bring it up at work, but now..."
        if club == "track":
            pcname "So I saw what happened with you and Keith."
            "Lisa tilts her head in confusion."
            show chelsea embarrassed
            if bakerymakeup == True or bakeryhalfmakeup == True:
                pcname "I saw him fucking you in his office the other day."
            elif True:
                pcname "I saw you giving him a blowjob in his office the other day."
        elif club == "cheer":
            pcname "So..."
            pcname "You and Keith, huh?"
            "Lisa tilts her head a little in confusion."
            pcname "I saw you two in his office the other day. Him? Really?"
        elif club == "yearbook":
            show chelsea embarrassed
            pcname "S-So, um..."
            pcname "I saw... you and Keith..."
            "Lisa tilts her head to the side. You bite your lip, wishing she would understand your thoughts instead of having to elaborate aloud."
            pcname "I saw you both, um, doing... sexual things... in his office..."
        L "Oh."
        "She nods to herself."
        show L Happy at left
        L "Well, we all have needs, [pcname]. Sexual desires and whatnot. It's nothing to be ashamed of."
        show chelsea confused
        pcname "But at work?"
        show L Blank at left
        L "We don't always get to choose the time or place, you know."
        show L Happy at left
        L "Besides, it's not like Keith is unattractive."
        "She gives a small smile at the thought."
    show chelsea blank
    show L Blank at left
    "Lisa pauses at a red light, an inquisitive look on her face. Before you can ask her about it, she turns toward you."
    L "[pcname], what do you think of Keith?"
    show chelsea confused
    pcname "Like, as a manager? Or as a person?"
    L "As a person, I guess. Do you find him attractive?"
    menu bakery_keithattractive:
        "Yes." if True:
            $ corruption += 1
            show chelsea embarrassed
            if bakery_eavesdrop == True:
                if bakerymakeup == True or bakeryhalfmakeup == True:
                    "The image of Keith that comes to mind is naked, bent over Lisa as he fucks her against his desk. It's a side of him you haven't seen before."
                elif True:
                    "The image of Keith that comes to mind is him standing over Lisa, his thick cock shoved deeply down her pulsing throat. It's a side of him you haven't seen before."
                "Maybe it's a side you'd like to see again."
            elif True:
                "An image of Keith pops up in the back of your mind, assertive but handsome as he orders you around the bakery, degrading you when you mess up."
                "Although you know you shouldn't, you can't deny that something about it feels exciting. Sexy, even."
            if club == "track":
                pcname "Sure, I guess."
            elif club == "cheer":
                pcname "Mm, yeah. He's pretty cute."
            elif club == "yearbook":
                pcname "I-I... well, yes..."
            show L Happy at left
            "Lisa smiles knowingly, picking up speed when the light flashes green."
            L "Why don't you flirt with him a little, then?"
            if bakery_eavesdrop == True:
                show chelsea shocked
                "You look at her in surprise."
                pcname "But aren't you two-?"
                L "I won't mind. I doubt Keith will, either. In fact, I think he'll appreciate it."
            show L Blank at left
            show chelsea blank
            L "If you find someone attractive, you should go for it. There's no sense in denying your own desires, is there?"
            "You take a moment to consider her words. You aren't sure if these circumstances should apply to your manager, but the thought of flirting with Keith gives you a little thrill."
            pcname "I guess so."
            show L Happy at left
            "Lisa grins, pleased with herself."
        "No." if True:
            if bakery_eavesdrop == True:
                if bakerymakeup == True or bakeryhalfmakeup == True:
                    "The image of Keith that comes to mind is naked, bent over Lisa he fucks her against his desk. You can't get the image out of your mind, no matter how badly you try."
                elif True:
                    "The image of Keith that comes to mind is him standing over Lisa, his cock shoved deeply down her throat. You can't get the image out of your mind, no matter how badly you try."
                "It isn't a memory you want to keep."
            elif True:
                "When you picture Keith, you see him standing over you, degrading your every suggestion and move. You can't help but find yourself irritated at the thought of him."
            pcname "Um, not really. He isn't really my type."
            if bakeryagree >= 7:
                show L Question at left
                "Lisa's eyebrows raise in surprise."
                L "Really? [pcname], I thought you had good taste in men."
            elif True:
                show L Disappoint at left
                "Lisa scoffs under her breath."
                L "That doesn't surprise me. You must truly have terrible taste in men, [pcname]."
            show L Blank at left
            L "Well, I think you should try flirting with him anyway. Men are easier to be around when you're stroking their egos a little."
            if bakery_eavesdrop == True:
                if bakerymakeup == True or bakeryhalfmakeup == True:
                    show chelsea angry
                    "A part of you wants to ask if that's why she let him fuck her over his desk, but you keep your mouth shut."
                elif True:
                    show chelsea angry
                    "A part of you wants to ask if that's why she let him shove his cock down her throat, but you keep your mouth shut."
            elif True:
                "You have trouble imagining yourself flirting with Keith, but maybe Lisa has a point. Especially if he would be easier to be around..."
                pcname "Thanks. I'll, uh, think about it."
                show L Happy at left
                "Lisa smiles, pleased to have reached through to you."
                L "Please do."
    show chelsea blank
    show L Blank at left
    "A few minutes later, she pulls up to your apartment."
    "Luckily, the rain has mostly cleared up, leaving only a little drizzle. You hold the plastic bag of your shoes over your head, protecting your hair from the rain."
    if bakerymakeup2 == True:
        show L Question at left
        L "Oh! I almost forgot!"
        "Lisa turns to the back seat of her car, rummaging around."
        show L Blank at left
        L "Before you go..."
        "She pulls out a small shipment box and passes it to you. You open it to find the makeup she ordered."
        show chelsea shocked
        pcname "Right! I almost forgot about this!"
        show L Happy at left
        L "Make sure to wear it from now on. With those shoes, too."
        "You nod, tucking the box into your bag."
    L "I'll see you at work, [pcname]."
    show chelsea happy
    L "Thanks for shopping with me!"
    $ makeupbutton = True
    scene bg black with dissolve
    "Lisa waits until you've reached your apartment door before beeping her car goodbye and driving off."
    $ LHappy = "Characters/Lisa/Happy.png"
    $ LBlank = "Characters/Lisa/Blank.png"
    $ LQuestion = "Characters/Lisa/Questioning.png"
    $ LDisappoint = "Characters/Lisa/Disappointed.png"
    $ LSad = "Characters/Lisa/Sad.png"
    jump events_end_period

label bakery_flirtwkeith:
    show chelsea happy at right with moveinright
    pcname "Please come again!"
    "Your last customer of the day gives a small wave before stepping out onto the street."
    "Keith pulls the door closed behind them, locking up."
    show chelsea blank
    show L Disappoint at left with moveinleft
    "You hear Lisa give an exhausted sigh beside you. Your aching muscles agree with her."
    L "That was busier than usual. I wonder if there's some sort of event in town or something."
    show L Blank at left
    "You shrug. It had certainly been crowded in the bakery today. You barely had time for a break as you ran between display cases, wrapping up treats while Lisa rung them up."
    "Even Keith stepped out of his office to bake extras in the back. The day was nothing short of chaotic."
    "Keith makes his way toward both of you. You can see the irritation and exhaustion plain on his face."
    show Keith Neutral with dissolve
    BM "If you have time to stand around and gossip, you have time to clean up."
    BM "Get to work, ladies."
    show Keith Blank
    "Keith steps behind the counter and opens the register, counting up the money."
    hide Keith with dissolve
    show L Happy at left
    if bakerymakeup2 == True and bakeryagree <= 7:
        L "Hey, [pcname]. Remember our deal?"
        show chelsea sad
        "You grimace, thinking of the mile high baking equipment that needs cleaned in the back. A part of you wonders if getting the makeup was really worth such a deal."
        pcname "Yeah, I'm on it..."
    elif True:
        L "[pcname], would you mind taking care of the dishes? I can clean up out here."
        if bakeryagree >= 7:
            pcname "Sure, I can do that."
        elif True:
            show chelsea sad
            "You grimace, thinking of the mile high baking equipment that needs cleaned in the back. You'd rather not, but you're too tired to put up an argument."
            pcname "Sure, I guess."
    show chelsea blank
    show L Blank at left
    "The pile isn't as bad as you imagined, but your muscles protest regardless as you spend the next thirty minutes scrubbing them clean."
    "After placing the equipment in their proper places and removing your cleaning gloves, you step back out into the shop. You notice that Keith is absent."
    show chelsea confused
    pcname "Aren't we having a meeting tonight?"
    "Lisa, crouched down to detail clean the cake cooler, glances up at you."
    show chelsea blank
    L "No, everyone's too exhausted. Keith just said to go home when we're finished."
    pcname "Oh. Okay."
    "You turn, ready to leave."
    L "{i}But-{/i}"
    "You pause. Lisa glances towards Keith's office, lowering her voice."
    show L Happy at left
    L "Remember what we talked about in the car? About flirting with Keith?"
    L "It's been a rough day. I bet he would be appreciative if you stroked his ego a little."
    "She nods toward his office, then pushes her breasts together, giving you a clear view of her cleavage."
    if club == "track":
        show chelsea embarrassed
        "You get a clear idea of what she's trying to suggest."
    elif club == "cheer":
        "It doesn't take a genius to understand what she's suggesting."
    elif club == "yearbook":
        show chelsea embarrassed
        "You feel your face heat up and quickly look away, embarrassed by her suggestion."
    menu bakeryflirt:
        "Go home." if True:
            show chelsea blank
            show L Blank at left
            pcname "I'd rather not. I think I'm just going to go home."
            show L Question at left
            L "Oh, don't run away, [pcname]. It's all in good fun."
            L "Besides, Keith will be a lot nicer to you if you do it."
            L "Don't you want to be on the manager's good side?"
            menu bakeryflirt2:
                "Stand by your decision." if True:
                    show chelsea angry
                    pcname "I shouldn't have to flirt with Keith for him to treat me nicely."
                    show chelsea blank
                    pcname "I'm going home."
                    if bakeryagree >= 7:
                        show L Blank at left
                        L "I'm surprised at you, [pcname]. Usually you're so agreeable..."
                    elif True:
                        show L Disappoint at left
                        L "Tsk. You're so stubborn, [pcname]. It's like talking to a wall."
                    show L Blank at left
                    L "Oh well. It's your loss. If you {i}really{/i} want Keith to keep treating you poorly, be my guest."
                    "You head to the back and get changed. As you walk home, you can't help but think about what Lisa said."
                    "You'd rather not have to deal with a difficult manager at work, but that doesn't mean you should have to flirt with him..."
                    "...Right?"
                    $ bakeryagree -= 1
                    scene bg black with dissolve
                    jump events_end_period
                "Give in." if True:
                    $ corruption += 3
                    pcname "Well... I guess it couldn't hurt..."
                    show L Happy at left
                    "Lisa smiles, pleased with your decision."
                    L "I knew you'd come around. I think you'll learn that a little goes a long way."
        "Flirt with Keith." if True:
            $ corruption += 3
            pass
    $ bakery_flirtwkeith = True
    show chelsea blank
    hide L Happy with moveoutleft
    if club == "track":
        "You walk over to Keith's office door and give a solid knock."
    elif club == "cheer":
        "Popping another one of your shirt buttons open, you stride to Keith's office door and knock."
    elif club == "yearbook":
        "A little timid, you summon the courage to walk over to Keith's office door and give a small knock."
    BM "Come in."
    hide chelsea with moveoutright
    scene bg black with dissolve
    show bg BakeryOffice with dissolve
    show chelsea at right with moveinright
    "You step inside to find Keith at his desk, paperwork strewn about around him. He stables receipts to the end of one of the packets, then adds some data into the computer."
    show Keith Neutral at left with moveinleft
    BM "What do you want? I said you could go home when you're finished."
    show Keith Blank at left
    "You make your way to his desk, pressing your hands against the edge. You lean over slightly, positioning your breasts between your arms to give him a good view."
    show chelsea embarrassed
    if club == "track":
        pcname "I was just checking to see if there's anything else I can get you."
    elif club == "cheer":
        pcname "Is there anything else I can get you before I go?"
    elif club == "yearbook":
        "You struggle to look at him as you speak."
        pcname "I-Is there anything e-else I can, um, get you?"
        "Keith doesn't so much as glance in your direction, entirely focused on his paperwork."
        BM "I'm fine."
    if corruption >= 20:
        "You lean forward just a little bit more."
        if club == "track":
            pcname "You're sure there's {i}nothing{/i} I can do for you?"
        elif club == "cheer":
            pcname "Are you sure? I'll get you {i}anything{/i} you need."
        elif club == "yearbook":
            pcname "A-Are you sure? I can get you... anything..."
        show Keith Smirk at left
        "Keith glances at your breasts for just a moment before returning to his work."
        show Keith Neutral at left
        BM "I made too many extra cookies today. They're just going to go on the waste sheet, so feel free to take some."
        show chelsea shocked
        "You're taken by surprise at his suddenly kind offer. You pull back from the desk."
        show chelsea happy
        if club == "track":
            pcname "Thanks!"
        elif club == "cheer":
            pcname "Thank you, Keith."
        elif club == "yearbook":
            pcname "T-Thank you!"
        hide chelsea with moveoutright
        scene bg black with dissolve
        show bg Bakery with dissolve
        show chelsea happy at right with moveinright
        "When you step back out into the bakery, Lisa is already gone for the night. You take a little baggy of extra cookies from the back and get changed."
        "On your way home, as you munch on some of the cookies, you think over Lisa's advice."
        "Maybe flirting with Keith {i}does{/i} have its benefits!"
        $ bakeryagree +=1
        scene bg black with dissolve
        jump events_end_period
    elif True:
        "He continues to stare at his computer."
        show Keith Neutral at left
        BM "Don't forget to clock out."
        show Keith Blank at left
        if club == "track":
            show chelsea sad
            "A little discouraged at being brushed off so easily, you pull back from the desk."
            pcname "Alright. Night."
            "You step out of his office, dejected."
        elif club == "cheer":
            show chelsea blank
            "You pull back from the desk, a little miffed at how easily Keith brushed you off."
            pcname "Well, if that's all."
            "You step out of his office, annoyed."
        elif club == "yearbook":
            show chelsea sad
            "You pull back from the desk quickly, ashamed."
            pcname "Y-Yes, sir."
            "You hurry from his office, afraid to look back."
        hide chelsea with moveoutright
        scene bg black with dissolve
        show bg Bakery with dissolve
        show chelsea sad at right with moveinright
        show L Blank at left with moveinleft
        "You meet Lisa in back as you both change out of your uniforms."
        L "How'd it go?"
        pcname "Poorly. He didn't even look at me."
        "She gives your shoulder an encouraging squeeze."
        show L Happy at left
        L "Give it time. After all, the more attention you give him, the more attention he'll give you."
        show L Blank at left
        "Lisa steps aside, pulling her bag over her shoulder."
        show chelsea blank
        L "Goodnight, [pcname]. Get home safe."
        pcname "You, too."
        "You give her a small wave and finish changing. On the walk home, you consider Lisa's advice. Maybe you should try again sometime."
        $ bakeryagree +=1
        scene bg black with dissolve
        jump events_end_period

label bakery_blondemeeting:
    show chelsea angry at right with moveinright
    "At the end of your shift, you find yourself surrounded by a giant pile of dishes yet again."
    "As you're midway through scrubbing them clean, Keith steps into the back."
    show Keith Neutral at left with moveinleft
    show chelsea blank
    BM "[pcname], I need to have a word with you in my office."
    show Keith Blank at left
    "You glance back at the dishes in your hands."
    show Keith Angry at left
    BM "Now."
    "He seems more serious than usual. You try to think of something you could have possibly done to upset him."
    show chelsea sad
    pcname "Ah, yes, Keith."
    show Keith Blank at left
    "Setting the dishes aside and removing your gloves, you follow Keith back to his office."
    hide Keith Blank with moveoutleft
    hide chelsea with moveoutleft
    show bg black with dissolve
    show bg BakeryOffice with dissolve
    show L Blank at left with dissolve
    show Keith Blank with moveinright
    show chelsea sad at right with moveinleft
    "Lisa sits in one of the wooden chairs across his desk, her hands folded neatly on her lap. You begin to wonder why she's here."
    show Keith Neutral
    BM "Take a seat."
    show Keith Blank
    "Keith gestures to the remaining empty chair as he reclines back in his desk chair. Your legs suddenly feel a little shaky as you sit down."
    "You feel your heart hammer in your chest as they both look at you for a moment. Your mind reels over every interaction you've had with them for the past few weeks, searching for something damning."
    if bakery_eavesdrop == True and bakerymakeup == True:
        "You think back to when you watched Keith and Lisa fuck in his office. Yes, that is certainly damning."
        "You glance at Lisa nervously. Had she told him about that? Is that what this is about?"
    if bakery_eavesdrop == True and bakeryhalfmakeup == True:
        "You think back to when you watched Lisa give Keith a blowjob in his office. Yes, that is certainly damning."
        "You glance at Lisa nervously. Had she told him about that? Is that what this is about?"
    show Keith Neutral
    BM "You know, [pcname], I hired you because I think you have a lot of potential."
    show Keith Blank
    "Your mouth feels too dry to speak. You nod numbly."
    show Keith Neutral
    BM "But there are still some things you can improve on."
    show Keith Blank
    "An image of yourself, homeless, living out of a cardboard box and begging for change comes to mind. You can't handle being fired."
    pcname "What can I fix?"
    show Keith Neutral
    BM "I don't think you care a lot about your appearance."
    show Keith Blank
    show chelsea confused
    pcname "But I shower every day-"
    show chelsea sad
    "Keith waves his hand, quickly cutting you off. You shrink in your seat."
    show Keith Neutral
    BM "That's not what I'm talking about. It takes more than a shower and brushing your hair. We have an image we're trying to keep, and you're not meeting our standards."
    BM "So, I'm wondering what we can do about that."
    show Keith Blank
    show L Happy at left
    "Lisa perks up at your side."
    show chelsea confused
    L "You know, I've always thought [pcname] would make a cute blonde, especially with the new lipsticks we bought."
    show L Blank at left
    L "And, you know, it {i}is{/i} a pretty popular color amongst guys, who are the majority of our customers. I think they would appreciate the change."
    "Keith considers the idea."
    show Keith Happy
    BM "Blonde hair... You know, that's not a bad idea, Lisa."
    show L Happy at left
    L "I could also dye my hair blonde if you think that would help."
    show Keith Blank
    "Keith dismisses her suggestion with the wave of his hand."
    show L Blank at left
    show Keith Neutral
    BM "No, no. I prefer how you look now."
    show Keith Happy
    BM "We need some diversity in our girls, after all."
    show Keith Neutral
    BM "[pcname] on the other hand..."
    show chelsea blank
    "While they continue to gush over the idea, you slowly calm down and try to absorb what they're saying."
    "That's what this is about?"
    if bakeryagree >=7:
        show chelsea happy
        "You can't help but lean back in your chair and sigh in relief. You were sure they were trying to fire you!"
    elif True:
        if club == "track":
            show chelsea angry
            "As the reality of the situation settles in, anger boils in your veins. What you do with your hair is none of their business! Where do they come off trying to get you to change your hair?!"
        elif club == "cheer":
            "As the reality of the situation settles in, you play around with the idea of blonde hair. It {i}is{/i} a rather popular look, but this is hardly an appropriate topic of discussion for your manager to bring up in a meeting."
        elif club == "yearbook":
            show chelsea sad
            "As the reality of the situation settles in, you almost want to cry from relief. You had been so certain that Keith was going to fire you, that any other suggestion seems silly in comparison."
            "But even so, you can't help but feel a little hurt that they would make such a big deal about your appearance."
    show chelsea blank
    if bakeryagree >= 7:
        show Keith Happy
        BM "What do you think, [pcname]? We're really trying to draw in more customers, and I think this might be the best way to do it."
        BM "You'd honestly be doing me a huge favor."
        show L Happy at left
        L "Not to mention how gorgeous you would look! You'd be irrestistable!"
    elif True:
        show Keith Happy
        BM "What do you think, [pcname]? We need everyone on board while we try to get new customers in. We work together as a team, and I think this would really show to us that you're willing to do your part."
        show L Happy at left
        L "You'd honestly make a better blonde than a redhead anyway. Not many can pull of red hair, natural or not."
        L "And it would match up really well with your new shoes and makeup, too. Guys will be lining up just to see you!"
    menu bakery_blondesuggestion:
        "Refuse." if True:
            if club == "track":
                show chelsea angry
                "You shake your head firmly."
                pcname "Absolutely not. I like my hair."
            elif club == "cheer":
                "You consider it a moment longer, then shake your head. As popular as it is, you don't think it would feel like {i}you{/i}."
                pcname "I have to pass. I like my current hair color."
            elif club == "yearbook":
                "As you think more about their suggestion, your nerves return. You've always had red hair. You can't imagine changing that. The mere thought of it scares you."
                pcname "B-But I like my hair..."
            show Keith Angry
            show L Blank at left
            show chelsea blank
            "Keith opens his mouth to interject, but Lisa holds up her hand, taking over. Keith sits back, allowing her to address you."
            show Keith Blank
            L "It's not that big of a change, [pcname]. I think it would be a lot of fun, actually. You and I can make a whole day out of it."
            show L Happy at left
            L "Besides, think of all the things you could do with it! You don't have to worry about avoiding certain shades of colors anymore. You'd have the freedom to wear whatever you want."
            L "I'll even take you to the mall to celebrate. So what do you say?"
            menu bakery_blondesuggestion2:
                "Refuse." if True:
                    "You glance between Keith and Lisa, uncomfortable under their pressuring stares."
                    if club == "track":
                        pcname "I said no already."
                    elif club == "cheer":
                        pcname "I told you no. That's my final answer."
                    elif club == "yearbook":
                        show chelsea sad
                        "You hold a strand of your red hair tightly, as though they will hold you down and dye it here and now."
                        pcname "I-I'm sorry, but no. I'm not dying my hair."
                    show L Disappoint at left
                    show Keith Angry
                    "Keith and Lisa share a quick look of discontent. Keith's eyebrows knit together, stern."
                    show Keith Neutral
                    BM "Well, I was wrong. You don't have potential in this company."
                    show Keith Blank
                    "Before you can ask what he means, Keith stands up."
                    show Keith Angry
                    BM "Get back to work. Those dishes better be spotless when I come back there."
                    hide Keith Angry with dissolve
                    hide L Disappoint with dissolve
                    show bg black with dissolve
                    "You nod, quickly rising to your feet. As you make your way to the door, you hear Lisa mumble something to him."
                    if bakeryagree >= 10:
                        L "I really thought she would be more agreeable..."
                    elif True:
                        L "I warned you about her..."
                    hide chelsea with moveoutright
                    "You hear the door slam on your way out."
                    show bg Bakery with dissolve
                    show chelsea at right with moveinright
                    "Once you finish cleaning up the rest of the dishes, you get changed and head home."
                    "Despite sticking to your decision, you feel that life at work is going to be a lot harder from now on."
                    scene bg black with dissolve
                    $ bakery_end = True
                    scene bg black with dissolve
                    jump events_end_period
                "Go blonde." if True:
                    "You consider Lisa's words carefully. It {i}would{/i} make clothes shopping much less of a pain. And blonde {i}is{/i} a cute hair color..."
                    show chelsea confused
                    pcname "You really think it would suit me...?"
                    L "Of course! You would look amazing, [pcname]. I can't think of anyone else it would look better on."
        "Go blonde." if True:
            "Note: Chelsea's Character will be blonde, but may cause consistency problems with some CG Scenes. "
            pass
    $ corruption += 2
    show chelsea blank
    show L Blank at left
    show Keith Blank
    if club == "track":
        "Despite your initial anger, you think it over again. Maybe it wouldn't be so bad..."
        pcname "I guess I can give it a try."
    elif club == "cheer":
        "You think it over for a moment, then nod."
        pcname "Yeah. It'll look really cute."
    elif club == "yearbook":
        "You think it over nervously. You've never dyed your hair before, and the thought of such a big change terrifies you."
        "But if it means you won't get fired..."
        pcname "O-Okay. I'll do it."
    show L Happy at left
    show Keith Happy
    "Keith and Lisa both grin in approval. You're not sure you've ever seen Keith look so approving of anything."
    L "Great! I'll call up the salon and get a session booked. You don't have to worry about a thing, [pcname]."
    BM "Sounds like it's all settled then. That's good to hear."
    BM "You can both go back to work."
    hide Keith Happy with dissolve
    hide chelsea with moveoutright
    hide L Happy with moveoutright
    scene bg black with dissolve
    show bg Bakery with dissolve
    show chelsea happy at right with moveinleft
    show L Happy at left with moveinleft
    "Lisa joins you as you return to the back and begin scrubbing the dishes. Pulling on some gloves, she assists you."
    "As she talks eagerly about the plans for the salon, you can't help but get excited as well!"
    $ bakery_bimbo1 = True
    $ bakeryagree +=3
    scene bg black with dissolve
    jump events_end_period

label bakery_salon:
    show chelsea at right with moveinright
    "As you walk into work, you're surprised to find Lisa waiting for you by the front door with a mischievous grin."
    show L Happy at left with dissolve
    "That look makes you a little nervous."
    show chelsea happy
    pcname "What's up, Lisa?"
    L "Do you have any plans after work?"
    show chelsea blank
    "Yup. Definitely nervous."
    show chelsea happy
    pcname "None that I can think of."
    L "Good! I have a surprise for you. Make sure you wait for me, okay?"
    show chelsea confused
    "A little taken aback, you nod."
    pcname "Okay."
    show chelsea blank
    "Lisa smiles again before walking back to the front of the shop. You quickly change into your uniform and get to work."
    hide L Happy with moveoutleft
    hide chelsea with dissolve
    show bg black with dissolve
    pause 0.5
    "While you spent the beginning of your shift trying to guess what sort of surprise Lisa has in store for you, your thoughts were quickly derailed when the bakery grew busy with customers."
    "Your shift goes by relatively quickly, and you manage to get out at a reasonable hour."
    $ clothes, hair = casualwear
    "You meet Lisa at the front of the bakery once your shift has ended and you've changed into comfortable clothes."
    $ LHappy = "Characters/Lisa/Casual/Happy.png"
    $ LBlank = "Characters/Lisa/Casual/Blank.png"
    $ LQuestion = "Characters/Lisa/Casual/Questioning.png"
    $ LDisappoint = "Characters/Lisa/Casual/Disappointed.png"
    $ LSad = "Characters/Lisa/Casual/Sad.png"
    show bg CityE with dissolve
    show L Happy at left with dissolve
    show chelsea at right with moveinright
    L "Follow me."
    "Lisa turns and walks down the street. You easily match her pace."
    show L Blank at left
    "You've been practicing walking in the stilettos at home, and walking in them has become second nature now."
    "Lisa leads you to a cute little salon a block away. You're surprised to find their lights still on. Glancing at their hours, you notice that they're actually closed."
    pcname "Lisa-"
    "Lisa knocks on the glass door."
    show L Happy at left
    L "Ricky? We're here!"
    show L Blank at left
    "A hair stylist with short purple hair appears at the front door. He unlocks it, allowing you and Lisa inside."
    show bg HairSalon with dissolve
    "Ricky" "Lisa, honey!"
    "Ricky and Lisa share quick cheek kisses before Ricky turns to you."
    "Ricky" "Ooh, is this the little apprentice?"
    "Lisa gives him a sharp look, but Ricky smiles."
    show chelsea happy
    "Ricky" "Nice to meet you, [pcname]. Lisa here's told me all about you. Don't worry, you're in safe hands."
    show chelsea confused
    "You give Lisa a questioning look."
    L "I've been seeing Ricky for years. He owns this salon."
    show chelsea blank
    "You nod in understanding. That explains why he's willing to work for her after close."
    "Ricky touches a strand of your hair."
    "Ricky" "Oh, honey, you're going to look fabulous. Come with me."
    "Ricky leads you to one of the styling chairs and drapes a large black cloth over you."
    "Ricky" "So what are we looking at? Platinum, honey, lemon?"
    show chelsea confused
    "You're momentarily confused until you notice him showing off a little sample of hair dye colors to Lisa."
    "Lisa scrutinizes your hair, then points to one in the middle."
    show chelsea blank
    "Ricky holds out the same sample to you. Several shades of blonde and yellow hair stick out from the end."
    "Ricky" "And what about you, [pcname]? Which do you like?"
    "You glance over the array of colors, unsure. You hadn't exactly expected to get your hair dyed so soon, let alone have to choose a shade."
    show chelsea happy
    pcname "Well, this one is kind of cute."
    show chelsea blank
    show L Disappoint at left
    "Lisa makes a face as you point to one near the end of the stick."
    show L Blank at left
    L "It has too much yellow going on in it, don't you think? You want something a little more natural."
    L "I think this one would suit you best, [pcname]."
    "Lisa points to a soft blonde in the middle. It reminds you of something an old-fashioned movie starlet might have."
    show chelsea happy
    pcname "Okay. I'll go with that one."
    "Ricky" "You got it."
    show chelsea blank
    "Ricky turns back to you and begins brushing through your hair."
    show L Question at left
    L "Have you ever been to a salon before, [pcname]?"
    "Before you can answer, Ricky cuts in."
    show L Blank at left
    "Ricky" "If she has, it's been a long time. You okay with me cutting some of these dead ends, [pcname]?"
    show chelsea happy
    if club == "track":
        pcname "Yeah, that's fine."
    elif club == "cheer":
        pcname "Would you? Yes, please!"
    elif club == "yearbook":
        pcname "S-sure."
    "After he's finished brushing, Ricky steps in the back momentarily before returning with a few bottles, a brush, a bowl, and some sheets of aluminum foil."
    show chelsea blank
    "He puts some gloves on and, with the brush, applies the fluid to your hair. He parts your hair as he applies it, folding the strands in the tin sheets."
    if bakeryagree >=5:
        "As he brushes closer to the scalp, you feel a mild irritation, but try to push it aside."
    elif True:
        "As he brushes closer to your scalp, you feel a burning sensation."
        show chelsea confused
        pcname "Is it supposed to burn?"
        "Ricky" "That's normal, honey, but I'll try to be careful."
        "You glance at Lisa, who nods in agreement. Your scalp feels like it's on fire, but you clasp your hands together tightly to prevent yourself from itching it."
    show chelsea blank
    "After what feels like, and may have been, hours of small talk while Ricky applies the bleach, he steps back."
    "Ricky" "Alright. We're going to give it thirty minutes. I'll keep checking up on it. You girls need anything to drink?"
    pcname "Ah, water, please."
    L "A water too, please."
    "Ricky steps in the back."
    show L Happy at left
    L "Are you enjoying this so far, [pcname]?"
    menu bakery_salonenjoy:
        "Yes!" if True:
            show chelsea happy
            "Lisa beams."
            L "I'm glad to hear it! You're going to look great. I can't wait to see the result."
        "Not really." if True:
            show L Question at left
            "Lisa frowns."
            show L Blank at left
            L "Well, don't worry. I know it can get boring, but we're just starting. My favorite part is when he washes my hair at the end. I think you'll enjoy that."
    show L Blank at left
    show chelsea blank
    "Ricky returns with two bottles of water and a mug of coffee for himself. As you accept your bottle of water, it takes everything you can not to dump it on your head and alleviate the burning."
    "The three of you get to chatting, with Ricky occasionally peeking at the status of your hair."
    "After thirty minutes, he reapplies his gloves and removes the tin foil."
    "Ricky" "Alright! Look at that!"
    show chelsea confused
    "You look in the mirror. Your reflection looks like a light-haired drowned mouse. You aren't sure what to make of it."
    show chelsea blank
    "Ricky" "Don't worry, it won't stay this way. We'll give you more of a golden blonde in a second."
    "Ricky" "Up, up, let's go. We gotta rinse this out."
    "Ricky leads you to a set of small tubs. He sits you down and tilts your head back, pouring warm water into the basin."
    "You relax as he rinses the bleach from your hair. The burning on your scalp subsides as it washes away, replaced with the gentle warm water."
    "Once he's finished rinsing, Ricky wraps your hair in a towel and leads you back to the salon chair."
    "He pulls out a blow dryer and quickly waves it over your hair, his other hand brushing out any forming tangles."
    "Once your hair is no longer damp, he mixes a few of the other bottles and starts applying the new liquid to your hair and patting it up in foil again."
    show L Happy at left
    L "Oh! [pcname], I just realized you're wearing the heels. No wonder your legs look so good today!"
    "Lisa gives a small laugh."
    L "How do you like them?"
    show chelsea happy
    pcname "They're great! I'm really getting used to walking in them."
    show L Blank at left
    L "That's good to hear! We should get you a few more pairs like those then. They look amazing."
    "Ricky peers over your shoulder."
    "Ricky" "Oh, damn, those are cute! Gonna stab a man's eye out with those things."
    "Ricky" "I'm making you do a little model walk for us when we're done!"
    "After he's finished, Ricky leads you to a set of large hair dryers. You take a seat while he lowers and adjusts the dryer over your hair."
    "Ricky" "I'll be back when it's done."
    "He gives you a smile before walking off. Lisa takes a seat beside you, pulling out some magazines from her purse."
    show L Happy at left
    L "I thought you might not be prepared."
    show chelsea blank
    show L Blank at left
    "You barely hear her over the dryer. Lisa passes you a few fashion magazines, taking one for herself. She relaxes beside you, flipping it open."
    "You take one of the magazines and peer through as well."
    show chelsea happy
    if club == "track":
        "You struggle to find anything of real interest until you come across a page of fashionable workout clothes."
    elif club == "cheer":
        "You read the magazine front to back, pointing out the cute celebrities to Lisa, who does the same in return."
    elif club == "yearbook":
        "While peering through the magazine, you stumble upon small quizzes to fill out and articles promising confidence. You read them over and take their advice to heart."
    "After you've browsed through about four magazines, the dryer comes to the end of its cycle, and Ricky lifts it up."
    "Ricky" "Alright, let's see how we did!"
    show chelsea blank
    hide L Blank with dissolve
    "Ricky again leads you toward the hair washing station. After he removes the tin foil, you feel yourself relaxing under his touch."
    "He rinses out the excess hair dye and massages the shampoo into your hair, rinsing it out with a little spray hose and repeating the act with conditioner."
    "His strong fingers massage the water against your scalp, rinsing your hair thoroughly."
    "You almost want to object when he turns the water off and wraps your hair in a towel. Ricky leads you back to the salon chair and pulls out a pair of scissors."
    "Ricky" "This won't take long."
    "He combs through your hair gently and grabs the scissors, clipping small pieces off of the ends of your hair."
    "Once he's satisfied, he pulls out the blow dryer."
    "You can vaguely hear Lisa and Ricky chatting, but you can't make out any of the words over the sound of the blow dryer. He runs another brush through your hair as it dries, untangling any forming knots."
    "He brushes through your hair one final time once the dryer is off, then grabs a bit of hair mousse from the station. He runs it through your hair."
    "Ricky" "Just a bit of added volume and... Voila!"
    show bg black with dissolve
    hide chelsea with dissolve
    pause 1.0
    $ haircolor = 'blonde'
    show chelsea with dissolve
    show chelsea shocked
    "When you look up at your reflection, you hardly recognize yourself. It's you, but all of the red hair is gone, replaced with glistening waves of blonde."
    "You turn your head at various angles, adjusting to the sight."
    "Lisa jumps out of her seat, hurrying to your side."
    show L Happy at left with moveinleft
    L "Wow... [pcname], you're a bombshell!"
    pcname "Really?"
    L "Of course! Oh, just look at you. You're so {i}hot!{/i} The hair, the heels, the makeup- just wait until we go out again. No one's going to be able to look away from you."
    if club == "track":
        show chelsea happy
        "You feel a surge of confidence at her words, grinning at yourself in the mirror."
        pcname "Thank you, Ricky!"
    elif club == "cheer":
        show chelsea happy
        "Her words make you feel {i}sexy{/i}. You can't help but admire your new look in the mirror."
        pcname "Thank you, Ricky! I love it."
    elif club == "yearbook":
        show chelsea embarrassed
        "You feel a little embarrassed at the thought and hide behind your new hair. You take small comfort in the realization that your hair won't make the blush on your cheeks stand out as much as your red hair did."
        pcname "T-Thank you, Ricky."
        show chelsea happy
    "Ricky" "No problem at all, honey. I wish I could pull that color off."
    "Ricky helps you out of the chair and walks to the register. As you reach for your wallet, Lisa waves it off."
    L "It's a work expense. I'll have Keith pay me back."
    "Lisa gives you a smile as she pays for the hair services."
    "You play with a strand of your new hair, admiring the look in another nearby reflection."
    "Ricky" "Ahem. Little lady."
    show chelsea blank
    show L Blank at left
    "You turn toward Ricky."
    "Ricky" "Make sure you call and book another appointment with me soon. We'll want to upkeep that, okay?"
    "Ricky" "Don't worry- it won't be as long as this visit was."
    show chelsea laugh
    "You give a small laugh. Lisa takes your arm, leading you out onto the street."
    "Lisa offers to drive you home, and you accept, laughing some as she continues to gush about your hair the entire drive back."
    if club == "track":
        "As you strut into your apartment, you feel like a brand new person. You can't wait to show yourself off to your track team!"
    elif club == "cheer":
        "As you enter your apartment and admire the new look in the mirror, you can't help but feel a little excitement at how jealous the other girls at school will be when they see it."
    elif club == "yearbook":
        "You struggle through both excitement and nervousness as you play with a piece of your new hair. You can't wait to see how everyone reacts to it at school!"
    $ bakery_blonde = True
    scene bg black with dissolve
    $ LHappy = "Characters/Lisa/Happy.png"
    $ LBlank = "Characters/Lisa/Blank.png"
    $ LQuestion = "Characters/Lisa/Questioning.png"
    $ LDisappoint = "Characters/Lisa/Disappointed.png"
    $ LSad = "Characters/Lisa/Sad.png"
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
