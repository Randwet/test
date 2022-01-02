label damien_lunchwviolet:
    show bg Cafeteria with fade
    show chelsea at right with moveinright
    show V School Blank at left with moveinleft
    "You sit at your usual spot with Violet, picking off pieces of your brownie to eat."
    "Violet carries on about some celebrity she ran into. You don't recognize the name, but it sounds like she had a good time."
    show V School Smile at left
    V "So what did you do last weekend?"
    menu damien_violetgossip:
        "I went out with Damien." if True:
            $ damienkeepquiet = False
            show V School Annoyed at left
            V "Damien?"
            "She scrutinizes the name, her face scrunching up as though it's left a bad taste in her mouth."
            if damienpays == False:
                pcname "Yeah. We just hung out at the movies."
                V "So was it a date?"
                pcname "No, we paid separately."
                "Violet looks as though she's been personally insulted."
                V "It doesn't matter if it's a date or not. He should have paid for you regardless."
            elif True:
                show chelsea happy
                pcname "Yeah. We went on a date together this weekend."
                show V School Blank at left
                "Her look of disgust falters. The probability of new gossip lightens her face and she leans forward."
                show V School Smile at left
                V "Tell me everything. What was he wearing? Did he pay? How far did you go?"
                pcname "Well..."
            if damienhandjob == True:
                menu damien_tellviolet:
                    "Tell her about the handjob." if True:
                        $ corruption += 1
                        if club == "track":
                            show chelsea happy
                            "You proudly recall your hand around his cock in the theater and how he had to muffle the sound of pleasure behind his hand."
                            pcname "I gave him a handjob."
                            show V School Suprised at left
                            "Violet blinks, then bursts out laughing."
                            show chelsea confused
                            pcname "What?"
                            show V School Smile at left
                            V "I can't believe you gave a nerd like him a handjob. Did he beg you for it?"
                            pcname "No, but he definitely didn't say no."
                            "Violet sniggers behind her hand."
                        elif club == "cheer":
                            show chelsea happy
                            "You think fondly of your hand around his cock in the darkened theater and how you might've liked things to escalate further."
                            pcname "I took care of some important needs."
                            show V School Suprised at left
                            "Violet gives you a puzzling look. You fwip your hand back and forth near your crotch under the table, giving her the idea."
                            show V Smile at left
                            "She lets out a laugh of muffled surprise behind her hand."
                            V "On the first date?"
                            V "What did he do?"
                            pcname "Isn't it obvious?"
                            show chelsea shocked
                            "You mimic Damien's face as he came into the popcorn bag. Violet laughs again."
                        elif club == "yearbook":
                            show chelsea embarrassed
                            "You flush at the memory of your hand around his cock in the middle of the crowded theater."
                            pcname "I... I may have... you know..."
                            show V School Pout at left
                            V "May have...?"
                            "You look down at your lap, embarrassed. It had felt so right at the time, but talking about it now..."
                            "Your voice drops down to a whisper before answering."
                            pcname "I-I gave him a... handjob."
                            show V School Suprised at left
                            "Her jaw drops."
                            V "{i}You?{/i}"
                            "You half expect her to go on some kind of tangent, criticizing you for your brazen behavior."
                            show V School Smile at left
                            "Instead, she laughs. Heat rushes up to your ears in a sudden wave of embarrassment."
                            show chelsea confused
                            pcname "W-What's funny about it?"
                            "Her laughter dies down, leaving behind a sharp grin."
                            V "I just didn't expect you to be able to do it. On a first date, no less. I'm impressed."
                            show chelsea happy
                            "A small sense of pride swells inside of you. You allow yourself a shy smile."
                        $ damientellviolethj = True
                    "Keep it clean." if True:
                        $ corruption -= 1
                        "You consider telling her about your raunchy adventures in the theater but decide against it. Some things are better left private."
                        show chelsea happy
                        pcname "We saw Space Warlord."
                        V "Ugh, really?"
                        show chelsea confused
                        pcname "Well, yeah."
                        show V School Blank at left
                        V "He's more of a loser than I thought. He could have at least taken you to see a {i}good{/i} movie..."
                        "It's clear by the look on her face that Violet was expecting something a little more gossip worthy."
            elif True:
                show chelsea happy
                pcname "We saw Space Warlord together."
                show V School Annoyed at left
                V "Ugh, really?"
                pcname "Yeah, it was a really good movie."
                show V School Blank at left
                V "He's more of a loser than I thought. He could have at least taken you to see a {i}good{/i} movie..."
        "Nothing much..." if True:
            show V School Pout at left
            V "Oh. That's boring."
            "There's hardly a pause before Violet kicks off her weekend story again, flying into another array of details you're convinced she might've already mentioned, but keep quiet about."
            $ damienkeepquiet = True
    show chelsea blank
    show V School Blank at left
    "You see Damien shuffle around at the end of the cafeteria line, searching. He catches your eye and waves, making his way to the table."
    show V School Annoyed at left
    "Violet shoots you a pointed look."
    V "Ugh. You didn't invite him, did you?"
    "You didn't, and although you're happy to see him join, you still feel a little guilty."
    show chelsea sad
    pcname "I--"
    show Damien Happy with moveinleft
    D "Hey, [pcname]."
    show chelsea happy
    pcname "Hey."
    "Damien sets his tray down across from you. You both share a smile."
    show chelsea blank

    if damienhandjob == False and damienkeepquiet == False:
        if damienpays == True:
            "Before you can even begin a conversation with Damien, Violet interjects."
            show V School Smile at left
            V "Space Warlord? Really?"
            show Damien Neutral
            "Damien flushes with embarrassment."
            D "Well, it's a really good movie."
            V "You call that a {i}good{/i} movie? Hardly. It's a disgrace to cinema."
            show Damien Glare
            D "Hey, that's a little harsh..."
            show Damien Neutral
            D "[pcname] enjoyed it, didn't you?"
            menu damien_moviechoice2:
                "Yeah, it was really good!" if True:
                    show chelsea happy
                    "Damien lights up, happy to have you on his side."
                    show Damien Happy
                    D "See? Even [pcname] thinks so. I can't wait for the sequel--"
                    show V School Annoyed at left
                    V "Ew. Stop talking before you infect me with your nerd germs."
                    show Damien Laugh
                    D "It's not contagious."
                    V "What did I say about talking?"
                "Eh, it was alright..." if True:
                    show Damien Worry
                    "Damien frowns, a little put out. Violet smirks confidently."
                    show V School Smile at left
                    V "Ha! See? I told you. It's a stupid movie."
                    show Damien Sad
                    D "I thought you liked it, [pcname]..."
                    show chelsea sad
                    pcname "Well..."
                    show V School Blank at left
                    V "Don't bother defending yourself, [pcname]. He just needs to accept his taste in just about everything is trash."
                    pcname "Violet..."
                    pcname "He asked {i}me{/i} out."
                    show V School Pout at left
                    "Violet seems to realize her error, but shrugs it off, brushing her dark hair over her shoulder in a fluid movement."
                    V "Except you."
                    show chelsea blank
                    pcname "Thanks..."
            show Damien Neutral
            show V School Blank at left
            show chelsea blank
            D "Anyways... Um, I was thinking... Well..."
            show Damien Glare
            "Damien casts a glance toward Violet, clearly wishing she wasn't there to hear. He takes a deep breath, gathering courage."
            show Damien Neutral
            D "Can we talk in private, [pcname]?"
            menu damien_privateconversation:
                "Yeah." if True:
                    show V School Pout at left
                    "You both pick up your trays. Violet shoots you a scathing glare."
                    V "You're just going to leave me behind?"
                    pcname "I'll see you in class."
                    show V School Annoyed at left
                    V "Hmph!"
                    "Violet turns her head away, immediately drawing her attention to her phone. You and Damien share an awkward glance and leave."
                    hide V Annoyed with dissolve
                    show Damien Blank at left with dissolve
                    "There's no room inside the bustling cafeteria, and you're forced to eat your lunches on a staircase in the hallway."
                    pcname "So what did you want to talk about?"
                    "Damien pokes at his food, a little flustered."
                    show Damien Neutral at left
                    D "Well, there's a festival coming up this weekend. I was, er, thinking we could go together. If you were interested."
                    show Damien Happy at left
                    "He casts a hopeful glance your way."
                    menu damien_festivallunch:
                        "I'd love to!" if True:
                            show chelsea happy
                            show Damien Laugh at left
                            "Damien's face lights up in excitement."
                            D "Really? I mean, ah, awesome. Cool. Yeah. I'll pick you up Sunday, then."
                            show Damien Happy at left
                            "The two of you finish finalizing plans for this weekend for the rest of lunch, occasionally sharing food with each other."
                            "When the bell rings, you both put your trays away, and Damien walks you to your classroom before heading off to his own."
                            $ damienfestivalflag = True
                            $ damiendate = True
                            jump events_end_period
                        "I have other plans..." if True:
                            $ corruption += 1
                            show Damien Worry at left
                            "Damien frowns, disappointed."
                            show Damien Sad at left
                            D "Oh. Um, maybe next time then."
                            "The rest of lunch is pretty awkward, and neither of you say a word until the bell rings. You collect your trays and give uncomfortable goodbyes, retreating to your respective classrooms."
                            jump events_end_period
                "I'd rather stay here." if True:
                    $ corruption += 1
                    show Damien Glare
                    "Damien shrinks a little. He was certainly hoping you wouldn't choose this."
                    "He takes another deep breath, steeling himself."
                    show Damien Neutral
                    D "Well, there's a festival coming up this weekend... I was wondering if you wanted to go with me?"
                    menu damien_festivallunch2:
                        "I'd love to!" if True:
                            $ corruption -= 1
                            show chelsea happy
                            show Damien Happy
                            $ damienfestivalflag = True
                            $ damiendate = True
                            "He sighs in relief, his courage visibly strengthening before you. It's sort of cute how eager he is."
                            D "Awesome! I mean, yeah. Cool. I'll pick you up Sunday then?"
                            pcname "Sure."
                            "Damien picks up his tray, giddier than you've ever seen him, and leaves."
                            hide Damien Happy with dissolve
                            show V School Blank at left
                            V "Did you just say that to make him leave you alone?"
                            show chelsea blank
                            pcname "No. I want to go out with him."
                            "Violet rolls her eyes, pressing her lips together in distaste."
                            V "If you say so..."
                            "Violet quickly resumes talking about her weekend, leaving no time for you to interject until lunch has finished."
                            "When the bell rings, Violet is the first to leave, and you're forced to clean up both trays before rushing back to class."
                            jump events_end_period
                        "I have other plans..." if True:
                            $ corruption += 1
                            show Damien Sad
                            D "Oh. Right. Ah..."
                            "Damien's face falls, evidently disappointed."
                            D "Well, maybe next time."
                            "Quickly, Damien picks up his tray, leaving the two of you behind."
                            hide Damien Sad with dissolve
                            show V School Smile at left
                            V "Did he honestly think he was getting another date after last time?"
                            V "Maybe he shouldn't be such a cheapskate and girls would like him more."
                            "You don't have much to say to this, and spend the rest of the lunch quietly listening to Violet's fifth rendition of how her weekend went."
                            "When the bell rings, indicating the end of lunch, you both clean up your trays and return to your respective classrooms."
                            jump events_end_period
        elif True:
            "Before you can even begin a conversation with Damien, Violet interjects."
            show V School Annoyed at left
            V "You didn't pay for her?"
            show Damien Neutral
            D "What?"
            "Damien is taken aback. He hasn't even been properly introduced, and she's already ready to jump on his faults."
            show V School Pout at left
            V "The movie. You didn't pay for her?"
            show Damien Worry
            D "Ah, she said she wanted us to pay separately..."
            "He casts an awkward glance toward you."
            pcname "It's true. I told him to."
            show V School Smile at left
            V "That's no excuse. If you were a real gentleman, you would've insisted on paying for her."
            show chelsea happy
            pcname "This is Violet, by the way. And this is Damien."
            show chelsea blank
            "You try to interject some sort of introduction, but neither party seems interested."
            show Damien Angry
            D "I am a real gentleman! I didn't realize you were expecting me to pay, [pcname]..."
            show chelsea shocked
            pcname "I wasn't!"
            show V School Pout at left
            show chelsea blank
            V "You should exceed expectations. Useless boy."
            show Damien Blank
            D "Well... Um... Speaking of paying..."
            "Damien clears his throat, gathering courage."
            show Damien Neutral
            D "Do you think we can talk in private, [pcname]?"
            menu damien_privateconversation2:
                "Sure." if True:
                    $ corruption -=1
                    "You glance at Violet, silently willing her to leave. She is not having it."
                    show V School Blank at left
                    show Damien Blank
                    V "I was here first. Get up and leave if you can't be bothered to include me."
                    "Awkwardly, you and Damien collect your trays and search around the crowded cafeteria for a secluded seat."
                    hide V School Blank with dissolve
                    "The room is packed tight, and you're both forced to sit in a stairway outside in the hallway."
                    "You balance your trays on your laps awkwardly, attempting to eat without spilling your meals."
                    "Damien doesn't say anything for a bit. You can sense his nervousness through his tense body language beside you."
                    "You try to prompt him forward."
                    pcname "So...?"
                    show Damien Shocked at left
                    "He gives a little jump, startled by the interruption of silence. You catch a faint blush on his face as he looks away."
                    show Damien Worry at left
                    D "Right. So, um..."
                    show Damien Blank at left
                    "He takes a deep breath, braving himself."
                    show Damien Neutral at left
                    D "There's a festival coming up this weekend. I was thinking... Well, would you like to go together?"
                    menu damien_festivallunch3:
                        "I'd love to!" if True:
                            $ corruption -= 1
                            show chelsea happy
                            $ damienfestivalflag = True
                            $ damiendate = True
                            show Damien Happy at left
                            "Damien visibly inflates with joy, letting out a held breath with relief."
                            D "Really? Ah, I mean, awesome! Cool. Yeah. I can pick you up Sunday?"
                            pcname "Yeah, that sounds great."
                            D "Cool. Yeah, cool."
                            "You both finalize plans to meet up over the rest of lunch."
                            "The bell rings, indicating the end of lunch. You both carry your trays to the cafeteria and clean them out. He accompanies you to your classroom before departing for his own."
                            jump events_end_period
                        "I have other plans..." if True:
                            $ corruption += 1
                            show Damien Sad at left
                            "Damien visibly deflates, unable to mask the disappointment in his voice."
                            D "Oh..."
                            D "Ah, that's okay. Maybe some other time."
                            "The rest of lunch is awkward. An uncomfortable silence fills up between you as you finish your meals."
                            "The bell rings, and after cleaning up your trays, you each leave to your respective classrooms."
                            jump events_end_period
                "I'd rather stay here." if True:
                    $ corruption += 1
                    show V School Smile at left
                    show chelsea blank
                    show Damien Glare
                    "Violet gives a smug grin, pleased to be included in your private conversation."
                    "It's clear that Damien had hoped against this. He casts awkward glances at Violet, as if looking at her will make her vanish."
                    show Damien Neutral
                    D "O-Oh, okay."
                    show Damien Blank
                    "Damien eats his meal quietly, his bravery quickly evaporating. Violet taps her long nails against the table."
                    V "Are you going to talk to her or not?"
                    show chelsea confused
                    "Damien flinches, looking back up at you awkwardly. You tilt your head curiously at him."
                    show Damien Neutral
                    show chelsea blank
                    D "Ah, right... Um, [pcname], there's a festival coming up this weekend..."
                    D "I was wondering if you... you know... might want to go with me...?"
                    menu damien_festivallunch4:
                        "I'd love to!" if True:
                            $ corruption -= 1
                            show chelsea happy
                            show Damien Happy
                            $ damienfestivalflag = True
                            $ damiendate = True
                            show V School Annoyed at left
                            "Damien grins, letting out a visible sigh of relief."
                            D "Really? Awesome! Ah, I mean, cool. Yeah. I'll pick you up Sunday."
                            show Damien Neutral
                            "He casts a glance toward Violet. His smile falters with her pursed lips of disgust."
                            D "Right. Ah. I'll see you Sunday."
                            show Damien Happy
                            "He picks up his tray, smiling at you once more before fumbling back into the crowded cafeteria. Violet scoffs."
                            hide Damien Happy with dissolve
                            show V School Pout at left
                            V "Please tell me you plan on standing him up."
                            show chelsea confused
                            pcname "Why would I do that?"
                            V "You don't plan to go out with that loser, do you?"
                            show V School Annoyed at left
                            show chelsea blank
                            V "Tch. What a waste of time."
                            show V School Pout at left
                            "Violet resumes tapping away on her phone. You eat your lunch, trying to play off the awkward silence."
                            hide V School Pout with dissolve
                            "The bell rings, indicating the end of lunch. Violet is up first and leaves for class. You're forced to clean up both trays and rush to your classroom."
                            jump events_end_period
                        "I have other plans..." if True:
                            $ corruption += 1
                            show Damien Sad
                            "Damien visibly deflates, the disappointment evident on his face."
                            D "O-Oh. Well, okay. Um, maybe next time then."
                            "He picks up his lunch tray, casting an uncomfortable glance between you and Violet before disappearing into the crowded lunch."
                            hide Damien Sad with dissolve
                            show V School Smile at left
                            "Violet smirks after him, pleased with this turnout."
                            V "What a loser. I can't believe he thought you'd go on another date with him."
                            V "You can do so much better than him."
                            "Violet spends the rest of the period talking about her weekend. When the bell rings, you both clean up your trays and return to your respective classes."
                            jump events_end_period

    elif damientellviolethj == True:
        show V School Smile at left
        "Violet smirks triumphantly at Damien, and his smile falters."
        show chelsea happy
        pcname "Damien, this is my friend Violet."
        "Violet holds out her hand, as though he should kiss it."
        V "How do you do?"
        show Damien Neutral
        D "H-Hey..."
        show Damien Blank
        show chelsea blank
        "Damien stares at the hand, unsure what to do. He shrinks back a little in his seat, intimidated by her fierce gaze."
        "Her hand lingers in the air for a moment longer. Violet pulls it back with a huff."
        V "So, [pcname] told me about your date."
        show Damien Neutral
        "Damien casts a nervous glance in your direction."
        show Damien Happy
        D "Yeah, it was a lot of fun."
        V "I'm sure it was. Tell me, what was louder? You or the movie?"
        show Damien Neutral
        D "I--What?"
        V "Well? Don't leave us hanging."
        "She looks to you."
        V "What was louder, [pcname]?"
        menu damien_louder:
            "Damien." if True:
                $ corruption += 1
                pcname "Damien was definitely louder."
                show chelsea laugh
                show V School Smile at left
                show Damien Worry
                "Violet laughs."
                "Heat rises to Damien's face. He looks away, unable to meet either of your gazes."
            "The movie." if True:
                show chelsea happy
                pcname "The movie was pretty loud. I don't think anyone heard him."
                show V School Pout at left
                V "If that's the case, you probably didn't do a good enough job."
                if damienconfidence > 50:
                    show Damien Happy
                    show chelsea shocked
                    D "I think she did a great job."
                    "Although he's clearly embarrassed, Damien shoots you a small, encouraging smile."
                    show chelsea blank
            "Neither." if True:
                pcname "I didn't really pay attention..."
                show Damien Blank
                "Damien lets out a small sigh of relief. Violet doesn't seem to notice. She continues to smirk, enjoying his discomfort."
        "Damien glances awkwardly at Violet. She leans toward him over the table, like a predator eyeing up her prey. He shifts away from her, attempting to keep his focus solely on you."
        show Damien Neutral
        D "Er, [pcname], can I talk to you in private?"
        menu damien_privateconversation3:
            "Sure." if True:
                show Damien Blank
                show chelsea happy
                "You look to Violet, silently pleading for her to give you some time alone. She remains planted in her seat, even cattier than usual."
                show chelsea blank
                show V School Pout at left with dissolve
                V "If you want to talk without me, then go. I'm not moving."
                "You and Damien share an uncomfortable glance but pick up your trays and leave."
                hide V School Pout with dissolve
                "The cafeteria is too crowded, and you're both forced to sit on a set of stairs in the hallway, balancing your trays on your laps."
                show Damien Blank at left with move
                "There's an awkward silence as you both quietly eat your meals, neither wanting to speak first."
                "After a while, you give in. It's clear that he isn't going to."
                show chelsea confused
                pcname "What did you want to talk about?"
                show Damien Sad at left
                show chelsea blank
                "Damien pokes at the nuggets on his plate with his fork, hesitating."
                D "I'm not really comfortable with your friends - or anyone, really - knowing about... you know..."
                pcname "Our date?"
                "He lets out a sigh, clearly not wanting to say it."
                show Damien Worry at left
                D "...The handjob."
                menu damien_HJapologize:
                    "Apologize." if True:
                        $ corruption -= 2
                        if club == "track":
                            show chelsea sad
                            "The high of confidence you felt in telling Violet about the date crashes. You'd been so focused on your own excitement about the event that you hadn't even considered how Damien might feel."
                            pcname "I'm sorry. I should've asked you if you were okay with me saying it first."
                            show Damien Neutral at left
                            D "I would've appreciated that, yeah."
                            "Damien sort of mumbles under his breath, directing his focus to a loose string on his jacket."
                            pcname "I just really had a good time. I thought it would be okay to tell Violet about everything. She's my best friend."
                            "He perks up a little."
                            D "I had a really good time, too. And I get that, I really do. It's just..."
                            pcname "...You want that stuff private. I understand. I won't talk about it anymore."
                            show Damien Happy at left
                            "Damien gives you a relieved, grateful smile. You return it, assuring him that everything is okay."
                            show chelsea happy
                            D "Thanks, [pcname]."
                            pcname "Sure."
                            $ corruption -= 2
                            $ damienconfidence +=1
                        elif club == "cheer":
                            "He looks so shy and cute, you can't help but feel a little bad for embarrassing him. Hopefully with experience, he'll be a little more open to talking about these things."
                            show chelsea happy
                            pcname "I'm sorry. Sometimes I can't help myself. It was such a good time, I thought it would be fun to share it."
                            show Damien Sad at left
                            "Damien bites his lip, clearly recalling his vulnerable moment."
                            show Damien Neutral at left
                            D "It-- It was a good time. But it's a good time that I want to just be kept between you and me. You know?"
                            "You rest your hand on his arm, stroking his muscle through the uniform jacket."
                            pcname "I understand. I won't tell anyone else about it... or anything else we do."
                            "You see the heat rise to his cheeks. He can't seem to look at you directly, but you don't miss the smile playing on his lips."
                            show Damien Happy at left
                            D "Thank you. I'd appreciate that."
                            $ corruption -=2
                            $ damienconfidence +=1
                        elif club == "yearbook":
                            "Of course he wouldn't be comfortable with you talking about it. You could barely bring yourself to say it in the first place."
                            show chelsea sad
                            pcname "I-I'm sorry. I didn't mean to hurt your feelings."
                            "You look down at your meal, your appetite lost. It was wrong to have told Violet about something so personal without talking to Damien about it first. How would you feel in his situation?"
                            show Damien Neutral at left
                            D "It's okay. I'm not, ah, mad or anything..."
                            "He scratches the back of his head absentmindedly."
                            D "I just sorta like that stuff private, you know?"
                            pcname "I understand. Of course. I'm sorry."
                            show Damien Happy at left
                            "Damien places his hand on top of yours, stroking along your fingers. When you gather the courage to look back up at him, he's smiling."
                            D "It's fine. I promise."
                            show chelsea happy
                            "You manage to smile back."
                            $ corruption -= 2
                            $ damienconfidence += 1
                    "Blow it off." if True:
                        $ corruption += 1
                        if club == "track":
                            show chelsea confused
                            "You don't understand what the big deal is. It isn't like you went into details."
                            pcname "Why does it matter?"
                            show Damien Shocked at left
                            D "Why?"
                            "He's taken aback, surprised by your answer."
                            show Damien Sad at left
                            D "Well, because-- it's, you know, private--"
                            show chelsea blank
                            pcname "The theater wasn't private. Someone probably saw us or heard us."
                            "His face flushes pink."
                            D "Still... That's..."
                            "His face burns a deeper shade as he fumbles with his words. He can't bring himself to look at you."
                            pcname "If you didn't want it, you should've told me to stop."
                            show Damien Neutral at left
                            D "I guess so..."
                            show Damien Blank at left
                            "He bites his lip, unwilling to argue. Neither of you can deny you both enjoyed it."
                            $ corruption +=2
                            $ damienconfidence -=1
                        elif club == "cheer":
                            "While you understand what he wants, there's something endearing about his embarrassment that just makes you want to tease him more."
                            show chelsea happy
                            pcname "Why not? Didn't I do a good job?"
                            show Damien Blank at left
                            "Heat rises to his cheeks as he quickly tries to revise his words."
                            show Damien Neutral at left
                            D "Of course you did! It isn't a question of if you were good at it or not..."
                            show chelsea confused
                            pcname "You liked it, didn't you?"
                            D "Well, I mean, yeah..."
                            show Damien Shocked at left
                            "You reach over and place your hand on his thigh. His body goes rigid. You can't help a small smile."
                            show chelsea happy
                            pcname "Then I don't see the problem. Do you?"
                            show Damien Blank at left
                            "He braves himself to look at you, his face red and flustered. He shakes his head slightly."
                            "You grin and pull your hand back, your attention drawn back to your meal."
                            $ corruption +=2
                            $ damienconfidence -=1
                        elif club == "yearbook":
                            show chelsea embarrassed
                            "You catch yourself rethinking the event in the theater, and a sudden panic grips you. Were you really so bad at it that he doesn't want you to talk about it?"
                            pcname "I-I thought you liked it."
                            show Damien Neutral at left
                            D "I did! I did. I just-- it's something that I kinda wanna keep between you and me, you know?"
                            show chelsea sad
                            pcname "Did I do something wrong? I-I can... I can do better..."
                            show Damien Shocked at left
                            "Realization hits him, and Damien quickly waves his hands in front of him, rejecting the idea."
                            show Damien Neutral at left
                            D "No, [pcname], you did a great job! A, um, a {i}really{/i} great job... I promise, it's not that..."
                            show chelsea embarrassed
                            "You twist a piece of your skirt fabric between your fingers nervously, staring down at your lap in embarrassment. Your stomach does anxious leaps, threatening to bring your lunch back up."
                            pcname "Then what...?"
                            D "You didn't do anything wrong. Really."
                            "Damien places his hand on top of yours and gives it a firm squeeze. You peek up at him to see he's also blushing. He gives you a reassuring smile, and you find yourself returning it."
                            $ corruption +=2
                            $ damienconfidence -=1
                show Damien Blank at left
                show chelsea blank
                "The bell rings, indicating the end of lunch. You both carry your trays to the cafeteria and empty them out."
                "Damien accompanies you back to your classroom but hesitates in the doorway."
                show Damien Worry at left
                D "So, I was thinking... There's a festival coming up in town. I was wondering if you might want to go with me?"
                menu damien_festivallunch5:
                    "I'd love to!" if True:
                        show chelsea happy
                        show Damien Happy at left
                        $ damienfestivalflag = True
                        $ damiendate = True
                        D "Ah-- Really?"
                        "His face lights up."
                        D "Awesome! I mean, great. Cool. I'll pick you up Sunday."
                        "He steps forward, and for a moment you think he's about to kiss you - perhaps that's what he meant to do - but he seems to realize his surroundings and quickly scurries off to class."
                        "You smile after him, watching him leave before walking back into your classroom."
                        jump events_end_period
                    "I have other plans..." if True:
                        show Damien Sad at left
                        D "Oh."
                        "His face droops in disappointment."
                        D "Well, maybe next time then."
                        hide Damien Sad with dissolve
                        "He quickly hurries off into the nearly empty hall, leaving you awkwardly behind."
                        jump events_end_period
            "Anything you say to me, you can say to Violet." if True:
                show V School Smile at left
                show chelsea blank
                show Damien Blank
                "Violet sidles herself closer to you, a smug grin spread across her face. She throws an arm around your shoulders, crushing you to her side."
                "Damien glances between the two of you uncomfortably. This was not how he hoped this would go."
                show Damien Neutral
                D "I'd really prefer--"
                show Damien Blank
                V "She'll tell me everything that you have to say anyway. You might as well spit it out."
                "He looks at you pleadingly. You show no intention of giving in."
                "He sighs."
                show Damien Neutral
                D "Well..."
                show Damien Glare
                "He shoots a look at Violet, clearly wishing she wasn't here to listen. Violet leans closer on the table, making her presence impossible to ignore."
                show Damien Worry
                D "I'm not really comfortable with you telling others about the..."
                show Damien Sad
                "He trails off, unable to say it out loud."
                show Damien Neutral
                V "The what, Damien?"
                show Damien Worry
                "Damien mumbles something under his breath, too quiet for either of you to hear."
                V "You need to speak a little louder, Damien. Oh, did you mean the {i}handjob?{/i}"
                "She says it loud enough to draw attention from a couple of nearby tables. Damien sits upright in his seat, his face blazing red. His response is so low you barely catch it."
                D "Y-Yes..."
                menu damien_mocking:
                    "Join in mocking." if True:
                        $ corruption += 3
                        if club == "track":
                            show chelsea happy
                            "You can't help but grin as Damien becomes more flustered. You feel a sense of empowerment over him. How far can you take it...?"
                        elif club == "cheer":
                            show chelsea happy
                            "You feel a thrill run through your body at Damien's flustered face. You want to see how much your words can make him squirm."
                        elif club == "yearbook":
                            show chelsea happy
                            "Although you know it's not kind, you can't help but get a sense of enjoyment out of seeing Damien's embarrassment. Does that make you a bad person?"
                            "You aren't sure, but you can't help yourself."
                        pcname "It's just a word, Damien. Go ahead. Say it."
                        show Damien Sad
                        "Damien glances around at the nearby tables. He's gathered even more attention now, several ears yearning to listen in on their conversation."
                        D "[pcname], I really don't want--"
                        V "It's just a {i}word{/i}. Are you so much of a coward that you can't say a single {i}word?{/i}"
                        D "That's not--"
                        V "Wow. He won't say it. I can't believe you went out with this loser."
                        V "Was he like this while you gave it to him, too?"
                        pcname "No, he definitely wasn't complaining when I gave it to him."
                        V "If he can get one, he might as well say it."
                        pcname "Yeah, Damien. Go on. Say it. {i}Handjob.{/i}"
                        V "{i}Handjob.{/i}"
                        pcname "{i}Handjob.{/i}."
                        show Damien Angry
                        D "HANDJOB!"
                        show Damien Sad
                        "You've seen embarrassment, but you've never seen the shade of red on a human face quite as vivid as Damien's. He almost looks like he'll cry."
                        "Violet lets out a high-pitched laugh. A couple of others join in before returning to their meals."
                        V "There. Was it that hard?"
                        if club == "track":
                            "Feeling bold, you throw in another jeer."
                        elif club == "cheer":
                            "You recall the girth of his cock around your hand and smirk."
                        elif club == "yearbook":
                            "Encouraged by your peers, you feel a confidence you've never felt before. You still have one more in you, and before you can take it back, it tumbles out of your mouth."
                        pcname "Not as hard as he was."
                        show Damien Glare
                        "You both fall into a small spasm of giggles. Damien picks up his tray, ready to go. You realize your mistake."
                        pcname "Where are you going? We were just joking."
                        show Damien Angry
                        show chelsea blank
                        D "It wasn't funny."
                        V "I thought it was hilarious."
                        show Damien Glare
                        "Damien hesitates, glaring at Violet, but drops his tray back on the table and sits down."
                        "He looks like he wants to say something, but his frustration holds him back. He takes a deep breath, and then--"
                        D "I was going to see if you wanted to go on another date, [pcname]."
                        V "Oh? Where are we going?"
                        "Damien shoots her a glare."
                        D "I was thinking of the festival. There's one coming up in town. I could pick you up this Sunday."
                        show V School Blank at left
                        "Violet opens her mouth, but Damien quickly shuts her down."
                        show Damien Angry
                        D "You're not invited."
                        show V School Pout at left
                        menu damien_festivallunch6:
                            "That sounds like fun." if True:
                                show chelsea happy
                                $ damienfestivalflag = True
                                $ damiendate = True
                                show Damien Happy
                                "Damien almost sighs in relief, a wide grin breaking through."
                                D "Awesome! Ah, I mean, yeah. Cool. I'll pick you up Sunday then."
                                show Damien Glare
                                "He spares another glance at Violet. She smirks at him, waving her manicured hand. Damien picks up his tray and leaves, refusing to acknowledge her."
                                hide Damien Glare with dissolve
                                "The bell rings, indicating the end of lunch. Violet leaves, forcing you to clean up both your tray and hers before heading to class."
                                jump events_end_period
                            "I've got other plans..." if True:
                                $ corruption += 1
                                show Damien Sad
                                "Damien's face drops in disappointment."
                                D "Oh."
                                "Violet swings her arm over your shoulder, interjecting."
                                show V School Smile at left
                                V "She's got plans with me. She has better priorities than wasting her time with you."
                                "Damien looks to you for some sort of answer, but you remain silent. He frowns, grabbing his tray and leaving."
                                hide Damien Sad with dissolve
                                "Violet waits until he's gone."
                                show V School Blank at left
                                V "That was smart. You don't want to waste your time on a loser like him."
                                pcname "So, did you want to hang out this weekend?"
                                V "What? No. I have plans."
                                "The bell rings, indicating the end of lunch. Violet leaves, and you're forced to clean both of your trays before heading back to class."
                                jump events_end_period
                    "Ask Violet to stop." if True:
                        $ corruption -= 2
                        show Damien Sad
                        show chelsea blank
                        "Damien looks thoroughly embarrassed. You don't feel right letting Violet tease him so ruthlessly."
                        pcname "Violet, you're going too far."
                        show V School Suprised at left
                        "Violet gives you an incredulous look."
                        show V School Annoyed at left
                        V "Are you seriously standing up for him?"
                        pcname "It's not nice to tease him about it. Please, let it go."
                        V "Who would want to interact with you two losers anyway?"
                        show V School Pout at left
                        "Violet scoffs, but picks up her phone, taking a greater interest in her screen than their conversation. You hope she'll get over it."
                        "You give Damien an apologetic smile."
                        pcname "I'm sorry."
                        show Damien Neutral
                        D "It's okay."
                        "Even though his words are reassuring, he shoots an uncomfortable glance at Violet, shifting in his seat."
                        show Damien Worry
                        D "So, I wanted to ask... Um, there's a festival coming up this weekend. I was thinking we could go together?"
                        menu damien_festivallunch7:
                            "I'd love to!" if True:
                                show chelsea happy
                                $ damienfestivalflag = True
                                $ damiendate = True
                                show Damien Happy
                                "Damien almost sighs in relief, a wide grin breaking through."
                                D "Awesome! Ah, I mean, yeah. Cool. I'll pick you up Sunday then."
                                "He spares another glance at Violet. She doesn't spare him her attention, busily texting on her phone. Damien takes this as a good sign and leaves."
                                "The bell rings, indicating the end of lunch. Violet leaves, forcing you to clean up both your tray and hers before heading to class."
                                jump events_end_period
                            "I have other plans..." if True:
                                show Damien Sad
                                "Damien frowns, disappointed."
                                D "Oh. Ah, okay. Well, maybe next time."
                                "He picks up his tray and spares a glance toward Violet. She promptly ignores him as he takes his leave, although the smug grin has returned."
                                V "What a loser. You can do so much better than him."
                                "The bell rings, indicating the end of lunch. You both clean up your trays and walk back to your respective classrooms."
                                jump events_end_period
                    "Stay quiet." if True:
                        show chelsea blank
                        "You bite your lip, not wanting to intervene between them. You know better than to cross Violet, and you're sure Damien can handle himself."
                        "At least, you hope so."
                        V "Yes what? You can't even say it?"
                        D "I shouldn't have to. You know what we're talking about..."
                        V "I want to hear you say it. Go on. {i}Handjob{/i}, Damien. It's not that hard. Use your words."
                        show Damien Neutral
                        "Damien looks to you for help. You quietly stare at your lap, pretending to be interested in a crease on your skirt."
                        show Damien Sad
                        D "Please stop..."
                        V "Handjob!"
                        "Damien looks around, flustered. People laugh from neighboring tables, picking up on the conversation."
                        show Damien Glare
                        D "Stop it! People can hear you!"
                        show V School Annoyed at left
                        V "I wouldn't be saying it if I didn't want them to, stupid. And {i}I'm{/i} not the one giving them out here."
                        show chelsea shocked
                        show Damien Blank
                        "You perk up, heat rising to your cheeks."
                        pcname "Violet!"
                        show V School Blank at left
                        V "What? I didn't name anyone."
                        show chelsea blank
                        show Damien Glare
                        "You and Damien both stare at your lunches, waiting for the interested classmates to go back to their normal conversations. Damien shoots Violet a glare."
                        show Damien Neutral
                        D "So..."
                        "You're surprised to hear Damien speak first. You look up, noticing that Violet has taken a greater interest in her phone than him."
                        "Her interest piques as he begins to speak, but Damien talks too quickly for her to get a comment in."
                        show Damien Worry
                        D "There's a festival coming up this weekend. I was wondering if you'd want to go with me?"
                        menu damien_festivallunch8:
                            "Sure!" if True:
                                show chelsea happy
                                $ damienfestivalflag = True
                                $ damiendate = True
                                show Damien Happy
                                "He sighs with relief. A wide grin spreads across his face."
                                D "Awesome! I mean, ah, cool. Yeah. I'll pick you up Sunday."
                                "He spares a glance at Violet, who rolls her eyes at him. Uncomfortable, Damien picks up his tray and leaves."
                                hide Damien Happy with dissolve
                                "Violet turns to you, just barely sparing enough attention over her phone."
                                show V School Pout at left
                                V "You need to get better taste."
                                "The bell rings, indicating the end of lunch. Violet leaves, and you are forced to clean up both of your trays before rushing to class."
                                jump events_end_period
                            "I have other plans..." if True:
                                show Damien Sad
                                D "Oh..."
                                "His demeanor visibly deflates. You almost feel bad but stick to your decision."
                                D "Well, maybe next time."
                                "Damien spares a glance at Violet. She smirks but says nothing to him. He picks up his tray and leaves."
                                hide Damien Sad with dissolve
                                show V School Smile at left
                                V "Don't waste your time on him. You can do so much better."
                                "The bell rings, indicating the end of lunch. Violet leaves for class, and you're forced to clean up both trays before you rush off yourself."
                                jump events_end_period
            "I'd rather just have lunch with Violet." if True:
                $ corruption += 1
                show Damien Sad
                "Damien looks rather put out. His shoulders hunch some, deflated."
                D "Oh. I see."
                show V School Smile at left
                "He glances at Violet, perhaps to show his dislike for her. However, Violet's shark-like grin causes him to shrink a little, intimidated. Damien picks up his tray and leaves, dejected."
                hide Damien Sad with dissolve
                V "Aw, do you think I hurt his feelings?"
                "Violet laughs, not feeling sorry in the slightest."
                "You join in a little."
                "Lunch ends sometime later, and after cleaning off both of your trays, you return to your respective classes."
                jump events_end_period


    elif damientellviolethj == False and damienkeepquiet == False:
        show Damien Blank
        "Damien tries to give Violet a friendly smile as well, but it falters under her look of contempt."
        pcname "Damien, this is my friend Violet. Violet, Damien."
        show V School Pout at left
        V "How do you do?"
        show Damien Neutral
        D "Er, hi."
        show Damien Blank
        show V School Annoyed
        "She holds out her hand as if to kiss it. Damien isn't sure what to do with it. It lingers in the air for a moment before Violet irritably pulls it back."
        show V School Blank at left
        show chelsea blank
        V "[pcname] was just telling me about your date."
        "Damien's gaze flickers to you briefly, a terrified look in his eyes. He tries to play it cool. Instead, he shows his nerves plainly."
        show Damien Worry
        D "Really? What'd she tell you?"
        V "Space Warlord? {i}Really?{/i} You chose {i}that{/i} as your first date? You might as well have taken her to a day care and played with blocks all night."
        show Damien Happy
        "Despite Violet's harsh criticism, Damien smiles, the relief visible on his face. He must have been worried you would tell about your little adventures in the theater seats..."
        D "It's a really great movie. We both had a great time. [pcname] loved it, didn't you?"
        menu damien_movielike:
            "Yeah, it was really good!" if True:
                show chelsea happy
                show V School Annoyed at left
                "Violet gives you a look of disgust."
                V "Then you're a bigger loser than I thought."
                show Damien Neutral
                D "How would you know if you've never seen it?"
                show V School Pout at left
                V "I don't have to see it. I can sense these things, and what I'm sensing right now is that you're both losers."
            "It was alright..." if True:
                $ corruption += 1
                show Damien Worry
                show V School Smile at left
                "Damien looks at you a little disheartened. Violet smirks, pleased to have been proven correct."
                V "See? It was stupid. Girls don't want to see movies like that."
                show Damien Sad
                D "Okay, well... It was still a really good movie..."
                show V School Blank at left
                V "I doubt that."
        show V School Pout at left
        show chelsea blank
        V "I don't need to be surrounded by nerds."
        show Damien Glare
        D "You can always leave."
        show V School Annoyed at left
        V "Are you suggesting I leave from my own table? Get lost!"
        menu damien_asktoleave:
            "Ask Violet to leave." if True:
                $ corruption -=1
                pcname "Violet, would you mind giving us some time alone?"
                show V School Suprised at left
                V "You can't be serious. I was here first!"
                pcname "Please?"
                show V School Annoyed at left
                V "No. If you want to talk without me, go somewhere else."
                show Damien Blank
                show V School Pout at left
                "Violet haughtily grabs the muffin from her tray and takes a bite as if to prove a point. You and Damien share an awkward look, but collect your trays, looking for somewhere else to sit."
                hide V School Pout with dissolve
                "The cafeteria is filled to the brim with bustling students, forcing you to take your trays to a staircase outside in the hallway."
                show Damien Blank at left
                "You both sit in silence for a bit, enjoying your meals."
                show Damien Neutral at left
                D "So..."
                "Damien's interruption catches you off guard. You swallow a bite of your brownie hard, giving him your full attention."
                show Damien Worry at left
                D "Just to make sure, ah, you didn't tell Violet about... well, you know..."
                if club == "track":
                    show chelsea confused
                    pcname "The handjob?"
                    show Damien Blank at left
                    "Damien winces at the word."
                    show Damien Worry at left
                    D "Ah, yeah..."
                elif club == "cheer":
                    show chelsea happy
                    "You smirk, enjoying his embarrassment. You lean forward, whispering it to him."
                    pcname "The handjob?"
                    show Damien Blank at left
                    "Heat rises to his cheeks. He nods."
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "W-What we did... in the theater...?"
                    show Damien Neutral at left
                    D "Ah, yeah... That..."
                    "Neither of you can bring yourselves to say it out loud, but you're relieved that it seems to be as good of a memory for him as it was for you."
                show chelsea blank
                pcname "No, I didn't tell her."
                show Damien Happy at left
                D "Oh. Thank you."
                "Damien lets out another sigh of relief, slouching back against the stairs. This must have really bothered him."
                "You both enjoy a little more of your lunch. Damien is evidently cheerier, going so far as to allow you a bite of the cupcake he snagged in the cafeteria."
                show chelsea happy
                pcname "Thank you."
                "You murmur the phrase behind your mouth, the moist cake sweet against your tongue. Damien smiles."
                D "You're welcome."
                D "Ah, I was thinking... There's a festival coming up this weekend. If you're free, maybe, you know... We could maybe go together?"
                menu damien_festivallunch9:
                    "I'd love to!" if True:
                        $ damienfestivalflag = True
                        $ damiendate = True
                        show Damien Laugh at left
                        "His smile spreads ear to ear, thrilled."
                        show Damien Happy at left
                        D "Really? I mean, awesome. Cool."
                        D "Um, I'll pick you up Sunday then."
                        pcname "Sure."
                        "You both enjoy the rest of lunch together. As he walks you back to your classroom, you can't help but look forward to this weekend."
                        jump events_end_period
                    "I have other plans..." if True:
                        show chelsea blank
                        show Damien Sad at left
                        D "Oh. That's okay."
                        D "Maybe some other time."
                        "Damien looks away, evidently disappointed."
                        "You both finish lunch in silence, parting your separate ways to class."
                        jump events_end_period
            "Ask Damien to leave." if True:
                pcname "Well, Violet was here first, so..."
                show V School Smile at left
                V "Ha! See? She doesn't want you here. Get lost."
                "Violet throws her arm around your shoulders, holding you against her side."
                show Damien Worry
                D "But I..."
                show Damien Neutral
                "Damien looks to you for some sort of help or explanation. You look away awkwardly, refusing to meet his gaze."
                show Damien Sad
                "Dejected, Damien grabs his tray and leaves."
                hide Damien Sad with dissolve
                V "What a loser. I can't believe he had the nerve to come up here and try to talk to you after that disaster of a date."
                "You wouldn't call it a disaster, but it seems like a lost cause to argue with her."
                pcname "It could've been better..."
                V "Exactly! Next time someone asks you out, make sure you know exactly where they're taking you."
                "Violet goes back to the discussion of her weekend, and when lunch ends, you both return to your respective classes."
                jump events_end_period
            "Try to make peace." if True:
                $ corruption -= 2
                show chelsea happy
                pcname "Why don't we all just have lunch together?"
                show V School Pout at left
                show chelsea blank
                "They both look at you, clearly displeased with your answer."
                show V School Annoyed at left
                V "Don't expect me to participate in your nerdy discussions."
                show Damien Glare
                show V School Pout at left
                "Damien takes some offense to this."
                D "No one would expect you to."
                "Violet whips out her phone again. Her manicured fingers clack against the glass screen rapidly, irritated."
                "After a moment, Damien turns to you."
                show Damien Neutral
                D "So--"
                V "Shh."
                D "What?"
                V "Shhh."
                show Damien Glare
                D "Violet--"
                show V School Annoyed at left
                V "What part of shut up don't you understand?"
                show Damien Angry
                D "I thought you weren't participating in our 'nerdy discussion'."
                V "I'm not."
                show Damien Glare
                D "Then why do you keep--"
                V "There can't be a nerdy discussion if you can't talk. So, shut up."
                show V School Pout at left
                "Violet resumes tapping on her screen. You can't tell if she's texting or playing a game."
                show Damien Blank
                pcname "Go ahead, Damien."
                show Damien Glare
                "Damien glances at Violet, fully expecting her interruption. When she doesn't look up from her phone, he continues."
                show Damien Neutral
                D "I was thi--"
                V "Sh."
                show Damien Glare
                D "Thinking that--"
                V "Shh."
                show V School Annoyed at left
                D "You could come--"
                V "Shhh."
                D "With me to--"
                V "Shut up."
                show Damien Angry
                D "A-festival-this-weekend."
                show Damien Glare
                "His last words are bundled together in hurried speech, trying to get them out before Violet can interrupt him again."
                show V School Smile at left
                "He casts a glare at her, but Violet smirks smugly back up at him."
                show V School Pout at left
                menu damien_festivallunch10:
                    "I'd love to go!" if True:
                        show chelsea happy
                        $ damienfestivalflag = True
                        $ damiendate = True
                        show Damien Happy
                        "Damien sighs in relief. You can't tell if he's happier you accepted or if it was due to the scowl on Violet's face."
                        "Either way, he seemed thrilled."
                        show Damien Laugh
                        D "Okay, awesome! I'll pick you up Sunday, then."
                        show Damien Happy
                        "Damien picks up his tray triumphantly, leaving the girls behind."
                        hide Damien Happy with dissolve
                        show V School Annoyed at left
                        V "You said yes? Are you out of your mind?"
                        "You shrug, happy with your decision. Violet rolls her eyes. She continues to berate you on your choice until the end of lunch."
                        "When the bell rings, Violet is the first to leave, forcing you to clean up both trays and rush off to class."
                        jump events_end_period
                    "I have other plans..." if True:
                        show Damien Sad
                        D "Oh."
                        show Damien Happy
                        show V School Smile at left
                        "Damien deflates a little, evidently disappointed. At Violet's smug grin, he forces a smile, refusing to give her any satisfaction."
                        D "That's okay. Maybe next time then."
                        hide Damien Happy with dissolve
                        "He picks up his tray and leaves."
                        show V School Pout at left
                        V "Good riddance."
                        "Violet flips her dark hair over her shoulder and goes off on another tangent about her weekend. You pretend to be interested until the end of lunch, when you both leave to your respective classrooms."
                        jump events_end_period

    elif damienkeepquiet == True:
        "You hadn't expected Damien to join you at lunch. If you'd known, maybe you would've told Violet about the date... But you really didn't want to have to talk about it..."
        show chelsea happy
        pcname "Ah, Violet, this is Damien. Damien, Violet."
        show V School Pout at left
        show Damien Blank
        "Violet scrutinizes Damien as if he's a disgusting creature that crawled out of the ground. Damien squirms under her gaze, uncomfortable."
        V "How do you know him?"
        show chelsea confused
        pcname "I told you about him a while ago..."
        show chelsea blank
        "She wrinkles her nose. He was clearly not worth her time to remember."
        V "Okay. What's he doing here? What do you want?"
        show chelsea sad
        "Damien looks at you, confused. You bite your lip, looking away."
        show Damien Neutral
        D "Well, I was hoping to talk to [pcname]-"
        show V School Blank at left
        show Damien Blank
        V "Then ask what you want and leave. You're invading our space."
        show Damien Neutral
        D "I was hoping to talk in private."
        "Damien looks to you hopefully."
        menu damien_talkalone:
            "Talk with Damien." if True:
                show chelsea happy
                pcname "Ah, sure. I'll be right back, Vi..."
                show V School Pout at left
                "Violet stares suspiciously in your direction, but a little notification pops up on her phone and she's distracted again."
                hide V School Pout with dissolve
                "You lead Damien outside into the hallway, out of earshot from the others."
                show Damien Neutral at left
                D "So, does she know about our date?"
                show chelsea confused
                pcname "Is she supposed to?"
                show Damien Worry at left
                D "I mean..."
                show chelsea blank
                pcname "No, I didn't tell her."
                show Damien Neutral at left
                D "Oh."
                show Damien Blank at left
                "Damien doesn't seem to really know what to do with this information. He shuffles his feet awkwardly, but sort of nods to himself, accepting it."
                D "Okay."
                "There's an awkward silence."
                pcname "Is that what you wanted to talk about?"
                show Damien Neutral
                D "Oh! Um, no, actually."
                "Damien scratches the back of his head, a nervous smile peering on his face."
                show Damien Happy at left
                D "I wanted to know if you wanted to come to the festival with me. There's one happening this Sunday in town."
                menu damien_festivallunch11:
                    "I'd love to!" if True:
                        show chelsea happy
                        $ damiendate = True
                        $ damienfestivalflag = True
                        "Damien grins, sighing in relief."
                        D "Awesome! Ah, cool. Yeah. I'll pick you up Sunday, then?"
                        pcname "Yeah, that sounds great."
                        "You both settle the details and return back to lunch. Damien picks up his tray and rejoins the biology club while you eat beside Violet."
                        hide Damien Happy at dissolve
                        show V School Blank at left with moveinleft
                        show chelsea blank
                        V "What was that about?"
                        menu damien_tellviolet1:
                            "I have a date with Damien." if True:
                                show V School Suprised at left
                                V "A date? Seriously?"
                                show V School Pout at left
                                "She looks heavily unimpressed."
                                show V School Blank at left
                                V "Whatever. Just don't let him get in the way of our friendship."
                                show V School Pout at left
                                "Violet picks up her phone again, clacking away while you eat your food in silence."
                                "When the bell rings, Violet is the first to leave, and you're forced to clean up both trays before rushing back to your classroom."
                                jump events_end_period
                            "Nothing important." if True:
                                show V School Pout at left
                                V "Hmph. I'm sure it wasn't."
                                "Even though she seems confident, Violet doesn't sound convinced. You don't push it, though, and enjoy the rest of your lunch together."
                                "When the bell rings, Violet is the first to leave, forcing you to clean up both trays before rushing back to your classroom."
                                jump events_end_period
                    "I have other plans..." if True:
                        show Damien Sad at left
                        D "Oh."
                        "His shoulders slouch with disappointment. He scratches the back of his head awkwardly."
                        show Damien Worry at left
                        D "Okay. Maybe next time."
                        show Damien Sad at left
                        "You both return to lunch. Damien quickly grabs his tray from the table without a word, leaving in the bustling crowd."
                        hide Damien Sad with dissolve
                        "Violet looks up from her phone."
                        show V School Blank at left with moveinleft
                        V "What was that about?"
                        menu damien_tellviolet2:
                            "He asked me on a date." if True:
                                show V School Suprised at left
                                V "A date? Seriously?"
                                pcname "I told him I already have plans..."
                                show V School Smile at left
                                V "Good. You can do better than that loser."
                                "The conversation changes back to Violet's weekend until lunch finishes. You both put your trays away and head back to your respective classes."
                                jump events_end_period
                            "Nothing important." if True:
                                show V School Pout at left
                                V "Hmph. I'm sure it wasn't."
                                "Even though she seems confident, Violet doesn't sound convinced. You don't push it, though, and enjoy the rest of your lunch together."
                                "When the bell rings, Violet leaves first, and you're forced to clean up both of your trays before rushing back to your classroom."
                                jump events_end_period
            "Stay with Violet." if True:
                show Damien Blank
                pcname "Sorry, I think I'd rather stay here with Violet..."
                "Damien looks between the two of you, as if searching for some other answer. Neither of you change your minds."
                show Damien Sad
                D "Oh. Okay."
                "Dejected, Damien picks up his tray of food and leaves."
                hide Damien Sad with dissolve
                show V School Blank at left
                V "What would a loser like that want with you anyway?"
                "You have a good idea but shrug, feigning innocence."
                show chelsea confused
                pcname "No idea."
                show chelsea blank
                "The two of you enjoy the rest of your lunch together."
                "When the bell rings, you both clean up your trays and carry on to your respective classrooms."
                jump events_end_period


label damien_lunchwvioletnegative:
    show bg Cafeteria with fade
    show chelsea at right with moveinright
    show V School Blank at left with moveinleft
    "You sit at your usual spot with Violet, picking off pieces of your brownie to eat."
    "Violet carries on about some celebrity she ran into. You don't recognize the name, but it sounds like she had a good time."
    show chelsea sad
    "Across the room, Damien sits with his friends in the biology club. He catches your eye and starts to rise from his table. You quickly look away, the thoughts of your disastrous date bubbling up inside of you."
    show chelsea blank
    "You try to focus on Violet's story more intently, pleased there is some sort of distraction."
    V "-And she showed me her new Malex and Mani that hasn't even been released yet. It's pretty tacky, if you ask me, but I'd never tell {i}her{/i} that..."
    pcname "Mhm..."
    show Damien Blank with moveinleft
    D "[pcname]?"
    "Damien stands a foot away behind you, as if he's afraid to step closer. His hands are stuffed deep into his pockets, a frown firmly set on his face."
    show V School Pout at left
    "You turn your back to him. Violet huffs, glaring up at him."
    show V School Annoyed at left
    V "You're interrupting my story."
    show Damien Neutral
    D "S-Sorry. I just wanted to know if I could talk to [pcname] alone, please...?"
    menu damien_privateconversation4:
        "Fine." if True:
            show Damien Blank
            if club == "track":
                "You decide that it's better to talk about this weekend privately than in a crowd. You stand up, your anger seeping out into your reply."
                pcname "Fine."
            elif club == "cheer":
                "Although you're still angry about this weekend, you can't ignore how pitiful he looks as he tries to compete for your attention. You sigh, standing up."
                pcname "Whatever. Make it quick."
            elif club == "yearbook":
                show chelsea embarrassed
                "Afraid he might try to mention the handjob in public, you quickly decide talking with him privately is the best decision. You can't imagine others hearing about the embarrassing things you've done!"
                pcname "I-I guess so..."
            show chelsea blank
            hide V School Annoyed with dissolve
            "Damien leads you out into the hallway, his shoulders slouched. He looks ashamed, and you take a secret pleasure in seeing him this way."
            show Damien Glare at left
            "Once you're out of earshot from the crowd, he turns to you, struggling to meet your gaze."
            show Damien Neutral at left
            D "I, um, wanted to apologize about this weekend. I shouldn't have implied you weren't a nice girl."
            if club == "track":
                show chelsea angry
                pcname "No, you shouldn't have."
                show Damien Blank at left
                "Damien flinches."
                show Damien Neutral at left
                D "Right. Um."
            elif club == "cheer":
                show chelsea angry
                pcname "Took you that long to figure it out?"
                show Damien Blank at left
                "Damien flinches."
                show Damien Neutral at left
                D "Ah, right... You are a really nice girl, [pcname]. I never meant..."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "But... I thought you hated me..."
                show Damien Shocked at left
                "Damien flinches."
                show Damien Neutral at left
                D "No! No, of course I don't."
            show chelsea blank
            show Damien Blank at left
            "He shifts his weight awkwardly, unsure of how to continue."
            show Damien Neutral at left
            D "So, um, I'm really sorry about this weekend. I was hoping, maybe, we could try to start over..."
            menu damien_apology:
                "Accept Apology." if True:
                    if club == "track":
                        "He seems genuinely apologetic, and your pride weakens a little. Perhaps he really didn't mean what he said..."
                        pcname "Fine. We can start over."
                        show Damien Happy at left
                        D "Really?"
                        "It seems by the startled look on his face that he hadn't thought you would accept his apology. A smile breaks out, and he lets out a sigh of relief."
                    elif club == "cheer":
                        "You feel a little bad for being so harsh on him. Perhaps if you could teach him more, he would be more comfortable with being intimate with you."
                        pcname "Alright. We can start over."
                        show Damien Shocked at left
                        "Damien's gaze finally meets yours, his look so shocked that it takes him a moment to gather his words."
                        D "R-Really?"
                        show Damien Happy at left
                        "You nod. He breaks out into a smile, letting out a held-in sigh of relief."
                    elif club == "yearbook":
                        "You mull the idea over in your head, avoiding his gaze. He really mustn't hate you if he wants to try to mend things..."
                        show chelsea embarrassed
                        pcname "O-Okay... We can try..."
                        show Damien Happy at left
                        "A smile cracks across Damien's face and he lets out a great sigh of relief."
                    D "Thank you, [pcname]. I promise you won't regret it!"
                    show chelsea blank
                    D "Well, um, since we're... starting over..."
                    D "I was thinking we could try for another date. There's a festival coming up this weekend, if you want to go together?"
                    menu damien_festivallunch12:
                        "Sure, I'll go." if True:
                            show chelsea happy
                            $ damienfestivalflag = True
                            $ damiendate = True
                            D "Really?"
                            "He sighs in relief, absolutely giddy."
                            D "Awesome! Ah, I mean, cool. Yeah. I can pick you up Sunday if that works?"
                            pcname "Sure. That sounds good."
                            "The two of you finalize plans for this weekend before returning to your respective lunch tables."
                            hide Damien Happy with dissolve
                            show chelsea blank
                            "Violet taps her nails against the table, impatient."
                            show V School Pout at left with moveinleft
                            V "What was that about?"
                            menu damien_tellviolet3:
                                "Tell Violet about Damien." if True:
                                    if club == "track":
                                        pcname "He wanted to see if I'd give him another chance."
                                        show V School Blank at left
                                        V "{i}Another{/i} chance? When did you give him a first?"
                                        pcname "This weekend. I gave him a handjob and he flipped out. He's lucky I forgave him."
                                        show V School Pout at left
                                        "Violet wrinkles her nose in disgust."
                                        V "Did you do it out of pity?"
                                        show chelsea confused
                                        pcname "No. I did it because I wanted to."
                                        show chelsea blank
                                        show V School Blank at left
                                        V "Hmph. If he flipped out, he didn't deserve it in the first place. How pathetic."
                                    elif club == "cheer":
                                        pcname "Someone reconsidered being upset about a certain handjob this weekend and came begging for me to forgive him."
                                        show V School Smile at left
                                        "Violet let out a malicious grin."
                                        V "He {i}begged?{/i} How pathetic."
                                        show chelsea happy
                                        pcname "Of course, I'm merciful enough to give him another chance."
                                        V "Hmph. More merciful than I'd suggest..."
                                    elif club == "yearbook":
                                        show chelsea embarrassed
                                        pcname "W-We went on a date this weekend... and it didn't go well..."
                                        V "So what did he want?"
                                        pcname "H-He wanted to try again. We're going to a festival this weekend..."
                                        show V School Blank at left
                                        V "You're wasting {i}more{/i} time on him? That's pathetic, [pcname]. You can do better than him."
                                        "You bite your lip, a little ashamed."
                                    show chelsea blank
                                    show V School Pout at left
                                    "Violet flips her dark hair over her shoulder and, as if the conversation with Damien never occurred, continues her story about this weekend."
                                    "When the bell rings, indicating the end of lunch, you both clean up your trays and return to your respective classrooms."
                                    jump events_end_period
                                "Keep Quiet." if True:
                                    if club == "track":
                                        pcname "None of your business."
                                        show V School Annoyed at left
                                        V "Excuse me? You're keeping secrets now?"
                                        "She looks pissed. You shrug it off."
                                        pcname "It's between me and Damien."
                                    elif club == "cheer":
                                        "You raise a finger to your lips, winking at her."
                                        show chelsea happy
                                        pcname "I don't kiss and tell."
                                        show V School Smile at left
                                        V "You should for me. Spill the tea."
                                        "You shake your head, smirking."
                                        pcname "Nope."
                                        show V School Pout at left
                                        V "Hmph."
                                    elif club == "yearbook":
                                        show chelsea embarrassed
                                        pcname "N-Nothing..."
                                        show V School Pout at left
                                        "Violet narrows her eyes at you suspiciously."
                                        V "It didn't {i}sound{/i} like nothing."
                                        pcname "Really... It's nothing important..."
                                    "She picks up her phone and types away on it, irritated. You don't let it bother you."
                                    "The bell rings, indicating the end of lunch. Violet leaves first, leaving you to clean up both trays before rushing to your classroom."
                                    jump events_end_period
                        "No thanks." if True:
                            if club == "track":
                                pcname "Uh, don't you think we need some time to recover after this weekend? I need some time to stop being pissed off at you."
                                show Damien Sad at left
                                "Damien frowns, staring back down at his feet."
                                D "O-Oh, right. Of course. Sorry."
                                D "Um, maybe next time, then."
                            elif club == "cheer":
                                "His idea of a next date is pretty sudden, especially after this disaster of a weekend. Even though you're willing to forgive him, you still need some time."
                                pcname "Maybe some other time. I'm really busy this weekend."
                                show Damien Neutral at left
                                D "O-Oh. Um, what kind of stuff are you doing? Maybe we can meet up--"
                                pcname "I'm doing it alone. Sorry."
                            elif club == "yearbook":
                                show chelsea sad
                                pcname "I-I'm sorry. I think it's a little soon after..."
                                show Damien Sad at left
                                "His face falls, but he struggles to put a smile back on, trying not to push his luck."
                                show Damien Happy at left
                                D "Right, right, of course. Maybe a little bit later, then."
                            hide Damien Happy with dissolve
                            hide Damien Neutral with dissolve
                            hide Damien Sad with dissolve
                            "He stands there for an uncomfortable moment longer before catching the hint and disappearing back into the crowded cafeteria."
                            show chelsea blank
                            "You rejoin Violet at your table, taking in a bite of your brownie."
                            show V School Blank at left with moveinleft
                            V "What was that about?"
                            menu damien_tellviolet4:
                                "Tell Violet about Damien." if True:
                                    if club == "track":
                                        pcname "He was apologizing for some stuff this weekend."
                                        V "Some stuff as in...?"
                                        pcname "I gave him a handjob and he flipped out. He wanted to go on another date already, but I'm still pretty pissed off."
                                        pcname "He's lucky I forgave him at all."
                                        V "Sounds like he doesn't deserve any of it."
                                        pcname "I'll be the judge of that."
                                        V "Hmph."
                                    elif club == "cheer":
                                        show chelsea angry
                                        pcname "He's trying to get another date out of me. I already went out with him this weekend. It's like he doesn't know when to stop."
                                        show chelsea blank
                                        "You brush your hair over your shoulder, smirking."
                                        pcname "I guess I can't blame him. But give me some time, you know?"
                                        V "I can't believe you went out with him in the first place. He's such a loser."
                                        pcname "He's not that bad. He's just... inexperienced. Nothing that can't be fixed."
                                        show chelsea happy
                                        "You let out a small giggle."
                                        show V School Smile at left
                                        V "What have you done with him so far?"
                                        "You glance around to make sure no one else is watching, then place your hand in a fist by your crotch under the table. You move it up and down, mimicking stroking a cock."
                                        "Violet lets out a laugh."
                                        V "On the first date? No wonder he's trying to go out with you again."
                                        pcname "What can I say? I know what he wants."
                                        V "More like what any boy wants."
                                    elif club == "yearbook":
                                        show chelsea embarrassed
                                        pcname "U-Um, he asked me out on a date..."
                                        show V School Pout at left
                                        V "That loser? You told him no, right?"
                                        pcname "I-I did... But it wouldn't be our first date..."
                                        V "You {i}already{/i} went out with him?"
                                        pcname "Well, er, yes. It didn't go that well, but, um... He apologized and... we're going to try again later..."
                                        V "You're wasting your time on him. You can do so much better."
                                        V "Whatever. As I was saying..."
                                    show V School Pout at left
                                    "Brushing her dark hair over her shoulder, Violet carries on about her weekend with the celebrity. You try to act a little more interested."
                                    "When the bell rings, indicating lunch is over, you both clean up your trays and return to your respective classrooms."
                                    jump events_end_period
                                "Keep Quiet." if True:
                                    if club == "track":
                                        pcname "None of your business."
                                        "Violet presses a manicured hand to her chest, offended."
                                        show V School Annoyed at left
                                        V "Seriously? You're keeping secrets from me?"
                                        "You shrug."
                                        pcname "It's a personal thing."
                                    elif club == "cheer":
                                        pcname "Oh, nothing."
                                        "You say it teasingly, unable to keep away the smirk on your lips."
                                        show V School Smile at left
                                        V "Really? What is it? You aren't going to keep a secret from me."
                                        show chelsea happy
                                        pcname "I don't kiss and tell."
                                        "You press a finger to your lips, winking."
                                    elif club == "yearbook":
                                        show chelsea embarrassed
                                        pcname "I-I don't really think it's for me to talk about..."
                                        V "Hmph. Whatever. I bet it wasn't that interesting anyway."
                                    "Irritated, Violet grabs her phone, typing away on it. You don't let it bother you."
                                    "The bell rings, indicating the end of lunch. Violet leaves first, forcing you to clean up both trays before rushing to your classroom."
                                    jump events_end_period
                "Reject Apology." if True:
                    $ corruption += 3
                    if club == "track":
                        show chelsea confused
                        pcname "After all that? No thanks. I have too much self-respect to go out with you again."
                        show Damien Sad at left
                        "The impact of your words seems to strike him. He finally looks up at you, crestfallen."
                        D "I really didn't mean that..."
                        pcname "Well you said it, didn't you? Good luck on your next date."
                    elif club == "cheer":
                        show chelsea confused
                        pcname "Do I need to spell this out for you? I'm not interested in you. I just felt bad for you, and you ruined it."
                        pcname "I don't date losers, Damien."
                        show Damien Sad at left
                        show chelsea blank
                        "Damien seems struck by your words. He shifts his weight uncomfortably, his mouth opening and closing in mortification. He struggles to get the words out."
                        show Damien Worry at left
                        D "If this is about what I said-"
                        pcname "Maybe learn to keep your mouth shut next time. Bye."
                    elif club == "yearbook":
                        pcname "I-I'm sorry, Damien, but I don't think I want to..."
                        show Damien Worry at left
                        D "I really didn't mean what I said-"
                        "You quickly bow, interrupting him."
                        pcname "I'm sorry."
                    show chelsea blank
                    hide Damien Worry with dissolve
                    hide Damien Sad with dissolve
                    "Without looking back, you walk back into the cafeteria and resume your seat beside Violet. She looks up at you, her eyes filled with a burning curiosity."
                    show V School Smile at left with moveinleft
                    V "So what was that about?"
                    menu damien_tellviolet5:
                        "Tell Violet about Damien." if True:
                            if club == "track":
                                pcname "I gave him a handjob this weekend, he flipped out, and had the nerve to come ask me to forgive him."
                                show V School Blank at left
                                V "For real? How pathetic."
                                V "I wouldn't have given him the time of day in the first place, but whatever..."
                                V "Not all of us can play hard to get."
                                "You bite your lip in irritation over her words but say nothing. You're sure she didn't mean it offensively... As least, you think she didn't."
                            elif club == "cheer":
                                show chelsea angry
                                pcname "I gave him the mercy of giving him a handjob this weekend and he repaid me by flipping out."
                                pcname "Then he had the nerve to try to apologize. As if I'd forgive him after that."
                                show chelsea blank
                                show V School Blank at right
                                V "How pathetic. He should be glad you went out with him in the first place. He should be worshipping the ground you step on."
                                show chelsea confused
                                pcname "I know, right?"
                                "You take an angry bite of your brownie, fed up."
                                show chelsea blank
                                V "So anyway--"
                            elif club == "yearbook":
                                pcname "I-I... well..."
                                show chelsea embarrassed
                                "You stare at your lap, heat rushing to your face. Just thinking about what you've done, especially after everything, is so embarrassing!"
                                pcname "I gave him a h-handjob on our date..."
                                "Violet bursts out laughing, startling you. You look up at her, relieved to see that she isn't judging you."
                                show chelsea blank
                                V "No wonder he came running back! Just like a dog. Don't give in again, even if he begs. You can do better than him."
                                show chelsea happy
                                "You find yourself smiling at Violet's encouragement."
                            show V School Blank at left
                            show chelsea blank
                            "Violet flips her dark hair over her shoulder, carrying on about her weekend again."
                            "The bell rings sometime later, indicating the end of lunch. You both clean up your trays and return to your respective classrooms."
                            jump events_end_period
                        "Keep Quiet." if True:
                            if club == "track":
                                pcname "Nothing."
                                show V School Blank at left
                                V "It definitely didn't sound like nothing."
                                pcname "Well, it was."
                                "Before Violet can push you further on the subject, you take another bite of your brownie."
                                pcname "So what happened next?"
                            elif club == "cheer":
                                show chelsea happy
                                pcname "Just a boy that's obsessed with me."
                                show V School Blank at left
                                show chelsea blank
                                V "How pathetic. Did he try to confess to you?"
                                pcname "Something like that."
                                show V School Pout at left
                                V "Ugh. Why is it always losers?"
                                pcname "Tell me about it."
                            elif club == "yearbook":
                                show chelsea embarrassed
                                pcname "I-It was nothing."
                                "You quickly shovel your food into your mouth, giving you an excuse not to talk. She wrinkles her nose in frustration, but otherwise drops the subject."
                            show chelsea blank
                            "Entirely forgetting about your discussion with Damien, Violet bursts off into another story about her weekend. You enjoy the distraction."
                            "The bell rings sometime later, indicating the end of your lunch break. Violet leaves before you, and you're forced to clean up both trays by yourself before rushing to class."
                            jump events_end_period
        "Get lost." if True:
            $ corruption += 5
            if club == "track":
                "The thoughts of your fight flood back into your mind, the anger bubbling up inside of you."
                show chelsea angry
                pcname "I thought I didn't have enough 'self-respect' for you to talk to me."
                show Damien Worry
                D "I didn't mean it like that. I just thought--"
                pcname "I thought I made it clear already: fuck off. I'm not interested."
            elif club == "cheer":
                "You recall his accusation of you not being a 'nice girl' and glare up at him, your chin held high. {i}Now{/i} he wants to apologize?"
                show chelsea confused
                pcname "I don't think so. You better go before your friends see you talking to 'that kind of girl'."
                show Damien Neutral
                D "That's not what I meant--"
                show chelsea angry
                pcname "What part of 'I felt sorry for you' do you not understand? I'm not interested. Leave me alone."
            elif club == "yearbook":
                "You're afraid that leaving with him will just result in more insults thrown at you. He's probably going to exclaim his hatred for you or threaten to spread news about your illicit activities in the theater."
                pcname "P-Please go away."
                show Damien Neutral
                D "Please? Just for a minute--"
                show V School Annoyed at left
                V "Didn't you hear her, loser? Get lost."
            show Damien Sad
            "Damien hesitates for a moment, ashamed. You don't bother to look at him as his footsteps recede back into the crowded cafeteria."
            hide Damien Sad with dissolve
            show V School Blank at left
            show chelsea blank
            V "What a loser. What was that about?"
            menu damien_tellviolet6:
                "Tell Violet about the handjob." if True:
                    $ corruption += 1
                    if club == "track":
                        pcname "I went out with him this weekend and gave him a handjob."
                        show V School Pout at left
                        V "And he said you had no self-respect?"
                        pcname "He wasn't saying that when he came in a popcorn bag."
                        show V School Smile at left
                        show chelsea happy
                        "Violet laughs, and you can't help but join in."
                        V "How pathetic! Screw him. He's just upset that you won't do it again."
                        "You grin, feeling a little better about the whole scenario."
                    elif club == "cheer":
                        pcname "I went on a date with him this weekend."
                        show V School Suprised at left
                        V "With {i}him?{/i} Seriously?"
                        pcname "I gave him a handjob and he's just obsessed with me now."
                        show V School Smile at left
                        V "Obviously. Who wouldn't be? You're way out of his league."
                        "You smile a little bit, encouraged by this remark."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        pcname "I-I... well..."
                        "You stare at your lap, heat rushing to your face. Just thinking about what you've done, especially after everything, is so embarrassing!"
                        pcname "I gave him a h-handjob on our date..."
                        show V School Smile at left
                        "Violet bursts out laughing, startling you. You look up at her, relieved to see that she isn't judging you."
                        V "No wonder he came running back! Just like a dog. Don't give in again, even if he begs. You can do better than him."
                        show chelsea happy
                        "You find yourself smiling at Violet's encouragement."
                    show V School Blank at left
                    show chelsea blank
                    "As if Damien had never interrupted, Violet resumes talking about her weekend. You're a little more invested in her story now."
                    "The bell rings, indicating the end of lunch. You both clean up your trays and return to your respective classrooms."
                    jump events_end_period
                "Keep quiet." if True:
                    $ corruption -= 1
                    if club == "track":
                        pcname "Nothing important, obviously."
                        show V School Pout at left
                        V "As if anyone like him has something important to say."
                    elif club == "cheer":
                        pcname "He's obsessed with me. He'll get over it."
                        show V School Pout at left
                        V "Hmph. If he tries to bother you again, just tell everyone he has herpes."
                    elif club == "yearbook":
                        pcname "I-It's nothing..."
                        show V School Pout at left
                        V "It didn't sound like nothing."
                        pcname "Really, it's-- it's nothing. I just want him to leave me alone."
                        show V School Blank at left
                        V "Hmph. Well, if he comes after you again, I'll tell everyone he has crabs."
                        show chelsea happy
                        "You surprise yourself by letting out a giggle."
                    "Violet brushes her hair over her shoulder and, as if Damien had never interrupted, continues talking about her weekend. You feel a little more invested."
                    "This continues until the bell rings, indicating the end of lunch. You both clean up your trays and return to your respective classrooms."
                    jump events_end_period

label damien_festivalmorning:
    $ clothes, hair = casualwear
    $ damiendate = False
    show bg RoomE with dissolve
    $ DamienAngry = "Characters/Damien/Casual/Angry.png"
    $ DamienBlank = "Characters/Damien/Casual/Blank.png"
    $ DamienGlare = "Characters/Damien/Casual/Glaring.png"
    $ DamienLaugh = "Characters/Damien/Casual/Laughing.png"
    $ DamienNeutral = "Characters/Damien/Casual/Neutral.png"
    $ DamienSad = "Characters/Damien/Casual/Sad.png"
    $ DamienShocked = "Characters/Damien/Casual/Shocked.png"
    $ DamienSmiling = "Characters/Damien/Casual/Smiling.png"
    $ DamienWorrying = "Characters/Damien/Casual/Worrying.png"
    "The late morning sun peeks in through the blinds, reminding you that it's the weekend."
    "You roll over in bed lazily. Your phone blinks with a new notification. You pick it up."

    call screen TextingScene("Damien",
    [
        TextMessage("Hey!"),
        TextMessage("I'm on my way over now. I'll be there around noon.")
    ])

    "You blink a couple of times, your eyes adjusting to the screen."
    "You look at the time."
    pcname "It's already 11:30!"
    show chelsea shocked at right with moveinright
    "You toss your blankets aside and throw yourself out of bed. You need to get ready!"
    hide chelsea with dissolve
    show bg black with fade
    pause 0.5
    show bg HomeE with dissolve
    show chelsea at right with moveinright
    "Damien should have been here already, but you try not to let it bother you as you finish getting ready."
    "As you finish applying your lip-gloss, you hear a knock at the door."
    "You open it to see Damien outside, checking over his phone nervously. He smiles as you appear in the doorway."
    show Damien Happy at left with moveinleft
    D "Oh! Good. I was hoping this was the right place...My GPS is sort of on the fritz lately."
    show Damien Blank at left
    "He holds up his cracked phone in embarrassment."
    show chelsea happy
    pcname "I'm glad you got here alright."
    "You step out of your living room to join him, locking the front door behind you. As you do so, you catch a glimpse of his outfit."
    show chelsea confused
    pcname "Are those... cargo shorts?"
    show Damien Happy at left
    "Damien looks down at his clothes and grins."
    show Damien Laugh at left
    D "Yeah. They're really comfortable. Let me know if you need me to hold anything."
    show chelsea happy
    "He gestures toward the cartoonishly large pockets on either side."
    if club == "track":
        "While you understand wanting to be comfortable, there is no denying how tacky they look on his slender frame."
        show chelsea confused
        pcname "Okay. If you're really into that, I guess..."
    elif club == "cheer":
        "You try to resist making a face. He notices."
    elif club == "yearbook":
        "Not wanting to hurt his feelings, you smile politely and try to avoid looking at them. Damien notices."
    show Damien Happy at left
    show chelsea blank
    D "What?"
    show chelsea confused
    pcname "You really like those?"
    show Damien Laugh at left
    D "Yeah. They're great! Very functional."
    show chelsea blank
    "You sigh, deciding to let his fashion atrocities go for today. You want to have a nice time, after all. You do, however, make a mental note to take him shopping sometime in the future."
    show Damien Happy at left
    "Damien offers his arm out to you."
    D "All set?"
    show chelsea happy
    if club == "track":
        "You take his arm forcefully and give a confident nod."
        pcname "Yeah!"
    elif club == "cheer":
        "You take his arm gratefully, resting close against him."
        pcname "Yeah."
    elif club == "yearbook":
        show chelsea embarrassed
        "You blush a little, taking his arm. He seems to be as nervous as you are but smiles through it. You can't help but return his grin."
        pcname "Y-Yes..."
    hide chelsea with dissolve
    hide Damien Happy with dissolve
    show bg black with fade
    jump damien_festival
label damien_festival:
    show bg FestD with fade
    show chelsea at right with moveinright
    show Damien Happy at left with moveinleft
    "As Damien escorts you downtown, you find yourself slowly surrounded by less of the city and more and more brightly colored tents."
    show chelsea shocked
    "He leads you into the center of it, and you're amazed by how large the event is."
    "The sidewalks are hidden behind massive tents of games, food, and other forms of entertainment."
    show chelsea happy
    "Delicious, savory scents waft in the air, and citizens bustle about in excitement, enjoying the festivities. It's more crowded than usual."
    D "So, what would you like to do first?"
    menu damien_festivalchoiceafternoon:
        "Eat." if True:
            $ damienafternoonfood = True
            "You're reminded of the breakfast you skipped this morning as your stomach growls."
            pcname "Let's get something to eat."
            D "Sure."
            "You both wander around the festival booths, enticed by the arrays of food in each stall. One delicious sweet catches your eye. You quickly pull Damien over to the stall."
            pcname "Ah! Taiyaki!"
            show Damien Neutral at left
            D "Oh, that stuff."
            show Damien Blank at left
            "Damien looks it over curiously. You glance up at him in surprise."
            show chelsea shocked
            pcname "You don't like it?"
            show Damien Neutral at left
            D "Ah, it's not that..."
            show Damien Happy at left
            D "I've never had it, actually."
            "The thought startles you. You can't imagine anyone being deprived of such a delicious treat."
            show chelsea happy
            pcname "Come on, let's try it."
            show Damien Blank at left
            "Damien dutifully follows you through the line, a little unsure of which flavor to choose when you reach the front."
            "A pleasant woman stands behind the cash register, a smile on her face."
            show GWaitress with dissolve
            "Stall Worker" "Welcome! What can I get for you today?"
            show chelsea blank
            pcname "I'd like..."
            menu damien_taiyakichoice:
                "Red Bean Paste, please!" if True:
                    show chelsea happy
                    "The woman marks down your order. She looks at Damien."
                    "Stall Worker" "And for you?"
                    show Damien Neutral at left
                    D "Ah, um..."
                    show Damien Blank at left
                    "Damien looks to you for help, unsure."
                    pcname "Red bean paste is really good. It is a little chewy, but it's still sweet."
                "Custard, please!" if True:
                    show chelsea happy
                    "The woman marks down your order. She looks at Damien."
                    "Stall Worker" "And for you?"
                    show Damien Neutral at left
                    D "Ah, um..."
                    show Damien Blank at left
                    "Damien looks to you for help, unsure."
                    pcname "I really like the custard. It's cool and creamy."
                "Chocolate, please!" if True:
                    show chelsea happy
                    "The woman marks down your order. She looks at Damien."
                    "Stall Worker" "And for you?"
                    show Damien Neutral at left
                    D "Ah, um..."
                    show Damien Blank at left
                    "Damien looks to you for help, unsure."
                    pcname "The chocolate is really sweet. It goes really well with the dough. I enjoy it a lot."
            "Damien nods, mulling it over."
            show Damien Happy at left
            D "I'll have what she's having."
            "Stall Worker" "That'll be $11. Your food will be ready in a moment!"
            show chelsea blank
            show Damien Blank at left
            "As you reach for your wallet to pay, Damien holds a hand out, already thrusting cash toward the woman. She accepts it."
            if club == "track":
                show chelsea happy
                pcname "Oh! Thanks."
                show Damien Happy at left
                D "You're welcome. I mean, we're on a date, after all..."
                "The way he phrases it sounds as though he's waiting for you to object. You smile brightly up at him and nod."
                pcname "Yep!"
                "Damien smiles back, visibly relieved. You make your way down to the end of the stall."
            elif club == "cheer":
                show chelsea happy
                pcname "Aw, thanks, Damien."
                show Damien Neutral at left
                D "You're welcome. I just thought, you know, since we're on a date..."
                "Damien says it hesitantly, as if he's afraid you'll object. You grab his arm and smile up at him encouragingly."
                pcname "Mhm."
                show Damien Happy at left
                "Damien smiles back, relieved. You make your way down to the end of the stall."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Y-You didn't have to do that."
                show Damien Neutral at left
                D "Well, we're on a date, aren't we?"
                "Damien phrases it in a way that waits for you to object. You tuck your hair behind your ear shyly, giving a small nod and a smile."
                show Damien Happy at left
                "Damien smiles back, both flustered and relieved. You make your way down to the end of the stall."
            show chelsea happy
            "Stall Worker" "Here you are. Thank you, and please come again!"
            "The woman holds out your taiyaki, a bright smile on her face. You both accept them, maneuvering back into the crowd."
            hide GWaitress with dissolve
            show chelsea blank
            "You take a bite of the sweet treat and let out a pleasant little noise. It's delicious!"
            show Damien Blank at left
            "You look to Damien, who hesitantly takes his first bite."
            show Damien Shocked at left
            "His eyes light up."
            show Damien Laugh at left
            show chelsea happy
            D "This is really good..."
            "He happily eats his taiyaki, enjoying it perhaps more than you're enjoying your own. You let out a small laugh. Damien glances at you, caught off guard."
            show Damien Happy at left
            D "What's funny?"
            "As he turns, you spot a small piece of filling by the edge of his lips."
            show chelsea blank
            menu damien_taiyakitaste:
                "Wipe it off." if True:
                    show Damien Blank at left
                    "Damien notices you staring at his face, becoming a little embarrassed."
                    show Damien Neutral at left
                    D "What is it?"
                    show Damien Blank at left
                    "Without answering him, you take a napkin from a nearby food stand and lightly brush it against his face, removing the filling."
                    show chelsea happy
                    pcname "You just had a little something there."
                    "You smile, pointing to a corner of your mouth. His cheeks tint pink."
                    show Damien Neutral at left
                    D "Y-You could've just, um, told me."
                    show Damien Happy at left
                    "He smiles despite himself, clearly not opposed to it. You smile back, tossing the napkin away in a nearby trashcan."
                    "You take his arm again and continue back into the crowd."
                    jump damien_festivalevening
                "Lick it off." if True:
                    show Damien Blank at left
                    "Damien notices you staring at his face, becoming a little embarrassed."
                    show Damien Neutral at left
                    D "What-"
                    show Damien Shocked at left
                    show chelsea happy
                    "Before he can get the words out, you lean forward, pressing against him. He goes quiet from the shock."
                    "You feel his face heat up as you stick your tongue out, lapping up the small amount of filling by his lips."
                    "Just as suddenly as you were there, you pull back, leaving behind a very flustered Damien. Redness rises up his face, tickling the end of his ears."
                    D "Wha-what-"
                    pcname "You had a little filling there."
                    show Damien Happy at left
                    "You lick your lips with a mischievous grin. Damien's face remains red, but he smiles a little as well. For once, he's able to meet your gaze as he does so."
                    "You take his arm again and continue through the crowd, enjoying your taiyaki along the way."
                    $ corruption +=2
                    $ damienconfidence -=1
                    jump damien_festivalevening
                "Mention it." if True:
                    show Damien Blank at left
                    "Damien notices you staring at his face, becoming a little embarrassed."
                    show Damien Neutral at left
                    D "What is it?"
                    "Hesitantly, you point to a spot near your lips, tapping it twice."
                    pcname "You have a little filling right there..."
                    show Damien Shocked at left
                    D "Oh!"
                    show Damien Blank at left
                    "Embarrassed, Damien searches around for a napkin. He takes one from a nearly booth, quickly rubbing the spot off his face. After a moment, he looks to you for approval."
                    pcname "It's gone."
                    show Damien Happy at left
                    "He smiles sheepishly, tossing the napkin away in a nearby trashcan."
                    D "Ah, thank you..."
                    pcname "You're welcome."
                    "You both share a small, embarrassed smile, before taking his arm and returning to the festivities."
                    $ corruption -= 2
                    $ damienconfidence += 1
                    show Damien Blank at left
                    show chelsea blank
                    jump damien_festivalevening
        "Play games." if True:
            $ damienafternoongames = True
            "The laughter of children playing festival games brings back a nostalgic feeling you can't ignore."
            show chelsea happy
            pcname "Let's play some games."
            "Damien smiles, enjoying your idea."
            D "That sounds great."
            show chelsea blank
            "You both wander around the exciting tents, peering from one game to another, unsure of which to try first."
            "As you're passing a bright yellow tent, you hear a child squeal with excitement."
            show chelsea confused
            "Festival Child" "Mama, mama! I caught one!"
            show chelsea blank
            "You look over to see the child excitedly holding up a goldfish in his net."
            "A large banner hangs over the tent: 'GOLDFISH SCOOPING!'"
            "You quickly tug Damien's hand, pulling him toward the booth."
            show chelsea happy
            pcname "Let's play this one!"
            "An elderly gentleman stands behind the booth, a set of nets in his hand. He smiles up at you both as you approach."
            "Goldfish Man" "Ah, would you like to play, too? It's $3 per net."
            pcname "Yes, please!"
            "As you reach for your wallet, Damien holds his hand out, extracting the cash from his own wallet and thrusting it toward the man."
            D "Don't worry, I've got it covered today."
            if club == "track":
                pcname "Oh! Thanks."
                show Damien Neutral at left
                D "Sure! I mean, since we're, you know, on a date, I'd like to pay..."
                show Damien Blank at left
                "He sounds like he's waiting for you to object. You smile up at him."
                pcname "Yeah! Thank you."
                show Damien Happy at left
                "Damien smiles back in relief."
            elif club == "cheer":
                pcname "Aw, thanks, Damien."
                show Damien Neutral at left
                D "Sure. I mean, we're on a date..."
                show Damien Blank at left
                "The way he says it sounds like he's waiting for you to object. You take his arm and smile up at him encouragingly."
                pcname "That's so sweet of you. Thanks."
                show Damien Happy at left
                "Damien smiles back, a little flustered."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Y-You don't have to do that..."
                show Damien Neutral at left
                D "I want to. I mean, we're on a date, aren't we?"
                show Damien Blank at left
                "Damien seems anxious to hear your answer. You shyly nod, tucking a piece of hair behind your ear, and smile up at him."
                show Damien Happy at left
                show chelsea happy
                "He smiles back."
            "The man exchanges the money for your nets. They're made of very thin wood and some soft string. You each take one and scoop."
            "You patiently swirl your net around, trying to capture one of the little fishes."
            "CRACK!"
            show Damien Blank at left
            "You glance over to see Damien's net has broken at the handle. Embarrassed, he quickly pays for another one and starts over."
            "You resume your attempts to capture a fish."
            "CRACK!"
            show Damien Glare at left
            "Another net broken. Damien exchanges money for a new one and starts over, his face red."
            "CRACK!"
            "CRACK!"
            show Damien Angry at left
            "CRACK!"
            show chelsea laugh
            show Damien Sad at left
            "You can't help but laugh as Damien's fifth net breaks, and he slumps in defeat."
            show chelsea happy
            show Damien Blank at left
            pcname "You need to be more patient. Here-"
            "You place your net in his hand and gently guide your hand over his, swirling the net gently in the water."
            "A fish presses into the net and you both quickly scoop it out."
            "A little goldfish wiggles in the new open air, flopping in your net."
            show Damien Laugh at left
            D "We caught one!"
            "Damien turns to you, thrilled. The elderly man peers over the tank, his hand held out for the net."
            "Goldfish Man" "Would you like to keep it?"
            show Damien Happy at left
            "Damien nods immediately."
            D "Yes please."
            "The gentleman takes your net and readies the fish in a plastic bag full of water. He passes it back to Damien and, with a smile, waves goodbye to the two of you."
            "As you both walk back through the festival, Damien admires the little fish. A sudden realization hits him."
            show Damien Shocked at left
            D "Ah, I'm sorry! I should have asked if you wanted it."
            show Damien Neutral at left
            "He quickly offers out the little fish, apologetic."
            menu damien_acceptgoldfish:
                "Accept goldfish." if True:
                    "You smile, accepting the little bag."
                    pcname "That's okay. Thank you."
                    "You look at the little fish as it swirls in its bag. You'll need to buy a lot of supplies to keep it alive. You hope that it'll live through your busy schedule."
                "Let him keep it." if True:
                    show chelsea blank
                    pcname "That's okay. I don't have anything to take care of it anyway."
                    show Damien Happy at left
                    show chelsea happy
                    "Damien gives a small smile, taking the goldfish back. You can't help but admire how adorable he looks admiring the little thing."
            D "What do you think we should name it?"
            $ goldfishname = renpy.input("What would you like to name the goldfish?", default="King Goldy", length=12)
            $ renpy.pause
            $ goldfishname = goldfishname.strip()
            if goldfishname == "":
                $ goldfishname = "King Goldy"
            pcname "[goldfishname]."
            "Damien grins."
            D "I love it! [goldfishname] it is, then."
            "You both admire [goldfishname] as it swirls around in its bag and carry on through the festival."
            jump damien_festivalevening
        "Watch shows." if True:
            $ damienafternoonshows = True
            "You notice a crowd gathered around near a more open space of the festival."
            show chelsea confused
            pcname "What's going on over there?"
            D "I'm not sure. Let's check it out."
            show chelsea blank
            show Damien Blank at left
            "Damien takes your hand and leads you over to the crowd. You both squeeze between a few people to get a better look."
            "You find yourself in front of a very large, cage-like structure. Metal bars hold up various swings and hoops high near the top. In the center, a performance starts."
            show Damien Happy at left
            show chelsea happy
            pcname "Acrobats!"
            "Sure enough, a group of performers in tight cyan costumes climb over each other, creating a tall, singular tower in the air."
            "You watch in amazement as they connect their limbs to make figures in the air, all supported by two sturdy people at the bottom."
            "You gasp as a girl at the very top is thrown into the air."
            "She grabs one of the swings with ease, her hands tight around the trapeze bar."
            "The other performers each dive off into somersaults off of the top of the formations, landing into the open arms of other acrobats."
            "The girl at the top swings the trapeze bar back and forth. Suddenly, several long, colorful silk ribbons drop down from the top of the structure."
            "She flips herself from the bar, catching herself by her leg around one of the silks."
            "The other performers scurry up the silk ribbons in a speed you thought not possible."
            "They twist and spin and flip between them, nothing to hold on to but the ribbons."
            "One performer flips onto the trapeze bar upside-down, his ankles hooked around the rope holding it up. He extends his hands downward."
            "A female performer throws herself into the air. He catches her by her ankle, twirling her body in midair."
            show chelsea shocked
            show Damien Shocked at left
            "You can't shake the terror that something might go wrong. You watch with an anticipation, unable to keep your eyes from the scene."
            "Damien clutches your hand beside you, equally tense."
            "The crowd, like you, stares up at the two performers in the air with baited breath."
            "He flips her around in the air with no restraint, leaving her no form of protection."
            "He tosses her into the air. You let out a scream as he shows no attempt to catch her. She falls."
            "Down between the performers on the silk, they band them together, using the silk to toss her between each ribbon in an elaborate performance."
            show Damien Happy at left
            show chelsea happy
            "She lands onto the ground with a small flip, her arms thrust upward in the air. The other performers dangle around her, and altogether, they give a great bow."
            "The crowd erupts into applause. You join them, your hands clapping together until they're red and swollen."
            pcname "That was amazing!"
            "You glance at Damien beside you. He looks faint with relief. He clearly, like you, thought the girl was a goner. His hands clap numbly."
            D "Wow... Just. Wow."
            pcname "Yeah."
            "You both seem to be at a loss for words as the crowd slowly disperses, your minds still focused on the amazing act."
            "After a moment, the crowd is gone, and the performers begin to clean up and prepare for the next show."
            "Without much thought, you approach them."
            show Damien Neutral at left
            show chelsea blank
            D "What are you doing?"
            "Damien follows behind curiously."
            if club == "track":
                show Damien Blank at left
                pcname "They were amazing, weren't they? Look at all that energy! I want to see how they keep it up."
                show Damien Happy at left
                D "I already think you're pretty energetic as it is."
                show chelsea happy
                pcname "But all that athleticism! It was awesome! I have to ask what they're doing."
                "Damien smiles, amused at your excitement. You grin back."
                "You both approach the lead female performer and eagerly ask her about her routine."
                "She's happy to oblige and gives you some great training advice!"
            elif club == "cheer":
                pcname "I'm going to ask how they did some of those tricks. I want to use some with the squad."
                show Damien Shocked at left
                D "You want to know how to {i}do{/i} them? They're professionals! Some of those moves looked really dangerous..."
                show chelsea happy
                pcname "Maybe I like to live on the edge."
                show Damien Happy at left
                "You give Damien a little wink. His face tinges pink, but he smiles, following you toward the performers."
                "You approach the lead female performer and ask her about some of the tricks she did."
                "She happily gives you some pointers and even lets you practice a few!"
            elif club == "yearbook":
                "You begin to take out your cellphone from your handbag."
                pcname "I was thinking of taking some pictures. Maybe, um, asking them if I can get an interview..."
                show chelsea embarrassed
                pcname "Something to give to the yearbook committee..."
                show Damien Happy at left
                "Damien smiles, surprised by your small boost in confidence."
                D "That's a great idea."
                show chelsea happy
                "He gives your hand an encouraging squeeze. You both share a smile before you approach one of the performers: the girl who had fallen through the air."
                "She's more than happy to give you an interview, and even repeats some of the stunts for your pictures!"
            jump damien_festivalevening
label damien_festivalevening:
    scene bg FestE with fade
    show chelsea at right with moveinright
    show Damien Happy at left with moveinleft
    "As you and Damien walk through the festival, the sun lowers, beginning to fade."
    D "What would you like to do now?"
    menu damien_festivalchoiceevening:
        "Eat." if True:
            "Your stomach rumbles loudly. You quickly place your hands over top of it, embarrassed."
            if club == "track":
                pcname "I'm starving."
            elif club == "cheer":
                pcname "I guess I could go for some food."
            elif club == "yearbook":
                pcname "Ah, I might be a little hungry..."
            "Damien smiles, taking your hand."
            D "Sure. Let's go find a booth."
            "You both peer through the colorful booths, keeping your eyes peeled for something that would suffice for dinner."
            "Something fried wafts in your direction, and you quickly lead Damien to a nearby booth."
            "Two stall workers hurriedly prep and serve small brown cartons full of takoyaki. The little wheat balls are filled with minced octopus, and a glossy brown glaze settles on top."
            "Your stomach growls again."
            "Without question, Damien steps in the long line beside you. You both patiently wait until you reach the front of the line."
            "A frenzied stall worker gives you a weak smile."
            show GWaitress with dissolve
            "Takoyaki Worker" "Welcome! What can I get for you this evening?"
            show Damien Neutral at left
            D "Ah, can we get two--"
            show Damien Blank at left
            "As he begins, you quickly interrupt."
            show chelsea happy
            pcname "Just one takoyaki, please."
            show chelsea blank
            show Damien Shocked at left
            "Damien looks at you in surprise, but the stall worker is almost relieved. She quickly types it into her register and Damien hands the money to pay."
            show Damien Blank at left
            "Takoyaki Worker" "Thank you! It will be ready for you in just a moment."
            "She turns, and her coworker quickly thrusts a brown carton into her hands. She offers it to you with her forced smile."
            "Takoyaki Worker" "Thank you! Please come again."
            hide GWaitress with dissolve
            "Damien accepts the carton. You both quickly evacuate the area, allowing the poor woman to deal with the next customer as quickly as possible."
            "A small family leaves a nearby bench, and you both quickly occupy it in their absence."
            "Looking down at the food, Damien seems to understand why you asked for one."
            show Damien Neutral at left
            D "Ah, this is huge!"
            pcname "That isn't why I asked for one."
            show Damien Blank at left
            "Damien looks at you, puzzled, as you pop one of the takoyaki into your mouth. It softens as it meets your tongue, and you savor the flavor."
            "He watches you as you eat, waiting for more. When you don't say anything, he takes it upon himself to ask."
            show Damien Neutral at left
            D "Then why?"
            show Damien Blank at left
            show chelsea happy
            pcname "Because it tastes better coming from you."
            show Damien Happy at left
            "Damien smiles, a pink tinge to his face. He takes one of the takoyaki and pops it into his mouth, avoiding your eyes in embarrassment."
            D "You just like it because you didn't have to pay for it."
            "But even as he says it, there is no denying the flushed, happy grin stretched out on his face."
            "You share the rest of the takoyaki together. You understand now why the line was so long: it was delicious. As soon as you'd gotten it, it was practically gone."
            "Once finished, Damien kindly throws out the empty cardboard container. By now, the sun has disappeared, and a nighttime chill settles over the air."
            $ damieneveningfood = True
            jump damien_festivalnighttime
        "Play games." if True:
            "As the sun just slightly makes it dark enough, bright lights pop up around the festival tents, illuminating what would have been dark corners in the crowded street."
            "Among the bright lights and colorful tents, you see a tiny plush frog dangling from a small white string."
            show chelsea happy
            pcname "It's adorable!"
            "You both approach the string lottery booth, your eyes unable to leave the tiny frog as it dangles helplessly in the air."
            pcname "I want it..."
            "As you reach for your wallet in your desperation to pay, Damien quickly hands the cash to a young, college-aged boy behind the booth."
            "String Lottery Worker" "Choose any string you'd like."
            menu damien_choosestring:
                "Right string." if True:
                    show chelsea blank
                    "You stare between the frog and the tangled strings, unsure."
                    "You choose a string on the far right, your heart hammering."
                    show chelsea sad
                    "You pull a small bag of shrimp chips from its place on the string. The worker unhooks it and passes you your prize. You look down at it in disappointment."
                    show Damien Blank at left
                    "Noticing your displeasure, Damien pushes a little more money to the worker."
                    show Damien Happy at left
                    D "We'll try again."
                    menu damien_choosestring1:
                        "Middle string." if True:
                            show chelsea happy
                            "Grateful for Damien's attempt to help you win, you survey the remaining strings, a little more nervous in your choice."
                            "You tug a string in the middle, your fingers crossed at your side."
                            "A pink cat keychain rises on the end of the string. The worker unhooks it and passes it to you."
                            "Without prompting, Damien places more money on the tabletop."
                            D "We'll try again."
                            show chelsea sad
                            "A little defeated, you pick the left string."
                            "The string quivers, lifting up..."
                            show chelsea confused
                            pcname "A brain?"
                            "You frown as a squishy brain lifts from the string. The worker unhooks it from the string and passes it to you. Holding it in your hand, you realize it's a stress ball. You squeeze it fiercely, frustrated."
                        "Left string." if True:
                            show chelsea happy
                            "Grateful for Damien's attempt to help you win, you survey the remaining strings, a little more nervous in your choice."
                            "You tug a string in on the left, your fingers crossed at your side."
                            "A squishy brain lifts from the string. The worker removes it and passes it to you."
                            "With one squeeze, you realize it's a stress ball."
                            "You're ready to give up, but Damien slams another round of money onto the counter."
                            show Damien Neutral at left
                            D "Let's try again."
                            show Damien Blank at left
                            "A little defeated, you glance between the large array of strings."
                            "Taking one in the middle, you tug..."
                            "A little pink keychain jingles from the end of the string. The worker removes it and passes it to you."
                "Middle string." if True:
                    show chelsea blank
                    "Hoping for the best, you pull on a string in the middle."
                    "A little pink keychain dangles up into the air. The worker pulls it off the hook and hands it to you."
                    "You frown down at the keychain. While it's cute, it's not what you wanted..."
                    "Sensing your disappointment, Damien sets more money on the countertop."
                    show Damien Neutral at left
                    D "Let's try again."
                    show Damien Blank at left
                    "Grateful for Damien's attempt to help you win, you survey the remaining strings, a little more nervous in your choice."
                    menu damien_choosestring2:
                        "Left string." if True:
                            "You tug a string in on the left, your fingers crossed at your side."
                            "A squishy brain lifts from the string. The worker removes it and passes it to you."
                            "With one squeeze, you realize it's a stress ball."
                            show chelsea sad
                            "You're ready to give up, but Damien slams another round of money onto the counter."
                            show Damien Neutral at left
                            D "Let's try again."
                            show Damien Blank at left
                            "A little defeated, you glance between the large array of strings."
                            "Taking one on the far right, you tug..."
                            "A bag of shrimp chips bounces on the end of the string. The worker removes it and passes it to you."
                        "Right string." if True:
                            "You tug a string in on the right, your fingers crossed at your side."
                            "A bag of shrimp crackers bounces up from the end of the string. The worker removes it and passes it to you."
                            show chelsea sad
                            "You're ready to give up, but Damien slams another round of money onto the counter."
                            show Damien Neutral at left
                            D "Let's try again."
                            show Damien Blank at left
                            "A little defeated, you glance between the large array of strings."
                            "Taking one on the left, you tug..."
                            "A squishy brain lifts from the string. The worker removes it and passes it to you."
                            "With one squeeze, you realize it's a stress ball."
                "Left string." if True:
                    show chelsea blank
                    "Your eyes glued to the frog, you yank hard on a string to your left."
                    "A squishy brain almost goes flying. The worker holds the string still and unhooks it, passing it to you."
                    "With a squeeze, you realize the brain is a stress ball. You can't help but be disappointed."
                    "Seeing the frown on your face, Damien places more money onto the counter."
                    D "We'll try again, please."
                    menu damien_choosestring3:
                        "Right string." if True:
                            "You tug a string in on the right, your fingers crossed at your side."
                            "A bag of shrimp crackers bounces up from the end of the string. The worker removes it and passes it to you."
                            show chelsea sad
                            "You're ready to give up, but Damien slams another round of money onto the counter."
                            show Damien Neutral at left
                            D "Let's try again."
                            show Damien Blank at left
                            "A little defeated, you glance between the large array of strings."
                            "Taking one in the middle, you tug..."
                            "A little pink keychain dangles up in to the air. The worker removes it and passes it to you."
                            "You frown down at the keychain. While it's cute, it's not what you wanted..."
                        "Middle string." if True:
                            "Hoping for the best, you pull on a string in the middle."
                            "A little pink keychain dangles up into the air. The worker pulls it off the hook and hands it to you."
                            show chelsea sad
                            "You frown down at the keychain. While it's cute, it's not what you wanted..."
                            show Damien Neutral at left
                            D "Let's try again."
                            show Damien Blank at left
                            "A little defeated, you glance between the large array of strings."
                            "You tug a string in on the right, your fingers crossed at your side."
                            "A bag of shrimp crackers bounces up from the end of the string. The worker removes it and passes it to you."
            show chelsea blank
            show Damien Blank at left
            "Damien has already begun to place money on the counter."
            show Damien Neutral at left
            D "Once more-"
            if club == "track":
                pcname "Don't bother. This game is stupid anyway."
            elif club == "cheer":
                pcname "It's fine. I didn't want it that badly anyway."
            elif club == "yearbook":
                pcname "Y-You don't have to, Damien..."
            "You turn, ready to move onto the next booth."
            show Damien Happy at left
            "Damien taps your shoulder. You glance over."
            "He offers out the small plush frog."
            show chelsea shocked
            pcname "What?! How?!"
            "You stare up at the tangled array of strings at the top of the booth, at a complete loss as to how he had managed to defeat the game."
            "Pouting a little, you accept the small frog, holding it close to your chest."
            show Damien Laugh at left
            show chelsea happy
            D "That is the one you wanted, right?"
            "A part of you stubbornly wants to shake your head. Instead, you admit defeat."
            show chelsea sad
            pcname "Yes."
            D "Then why do you look so upset?"
            "The answer is childish, and you feel as much saying it out loud."
            pcname "I wanted to win it myself."
            show Damien Laugh at left
            "Damien blinks, then quietly chuckles behind his hand. Your pout deepens."
            show chelsea confused
            pcname "What?"
            show Damien Happy at left
            D "You're just so cute."
            if club == "track":
                show chelsea embarrassed
                "Your cheeks burn a little. You shove him lightly, playfully. Damien is unbothered by this."
                pcname "Shut up."
            elif club == "cheer":
                show chelsea happy
                "Enjoying the attention, you look away, your face a little pink."
                pcname "I know I am."
            elif club == "yearbook":
                show chelsea embarrassed
                "You look away, embarrassed."
                pcname "Y-You... think I'm cute?"
            "Damien smiles. He places an arm around your shoulder. You press into him a little, allowing him to lead you away."
            show chelsea happy
            D "Do you have a name picked out for your frog?"
            $ frogname = renpy.input("What would you like to name your frog?", default="Ribster", length=12)
            $ renpy.pause
            $ frogname = frogname.strip()
            if frogname == "":
                $ frogname = "Ribster"
            pcname "[frogname]."
            show Damien Laugh at left
            "Damien grins again, hiding a chuckle."
            show chelsea confused
            pcname "What? What's so funny?"
            D "[frogname]... It's just cute. You're so cute."
            "You speak before thinking."
            show chelsea happy
            pcname "So are you."
            show Damien Happy at left
            "Neither of you say anything as you walk through the festival, but you both grin from ear to ear, your arm around his waist and his around your shoulder, enjoying the small moment between you."
            $ damieneveninggames = True
            jump damien_festivalnighttime
        "Watch shows." if True:
            "You continue to walk through the festival, debating the question. You aren't very hungry right now, and none of the games are standing out to you either."
            "Suddenly, a heat erupts behind you. You turn as several men and women in tight red nylon clothes dance in two straight lines through the middle of the festival."
            "Their hands toss something warm and glowing in the air, and it takes you a moment to register that they are indeed throwing thick batons of fire between each other."
            show chelsea happy
            "You and several others gasp, stopping in your path to watch the spectacle."
            "You're sure tossing fire as such in the air so close to all of these people and tents can't be safe, but like the pied piper, they lead you through the festival until they've stopped at a large open stage at the very end."
            "A crowd gathers. You all stop at once when they form into a large circle on the stage, their heads bowed."
            "There is a silence. And then-"
            "Music BLARES. The dancers thrust their heads up on the first note, and the flames soar through the air."
            "Clubs of flames toss between other dancers, and some manage to juggle several clubs at once. The entire stage is lit up in a flickering orange glow."
            "You and Damien can do nothing but stare in amazement at the show."
            "At the end, a single man steps into the center of the circle, allowing the others to juggle to open flames above him."
            "The performers catch their clubs in a sudden halt. The man in the center opens his mouth and places the end of one of the lit clubs into his mouth."
            "You gasp. Damien grips your sleeve."
            "He pulls the club away, the flame extinguished."
            "With a sudden burst, he blows the flames out of his mouth, like a dragon emerging from his cave."
            show Damien Laugh at left
            "The crowd breaks out into applause. You and Damien clap your hands, chilly without the heat of the lit flames."
            "The performers bow. The man in the center bows twice as the applause refuses to relent."
            show Damien Happy at left
            "Briefly, you imagine what it would be like up there, juggling flames for the crowd's pleasure."
            show chelsea blank
            "Glancing at Damien, you can't imagine him in such a spot. The thought of him even attempting something so dangerous is almost laughable."
            "You gently nudge his shoulder, teasing."
            show chelsea happy
            pcname "You should go ask him if you can try."
            show Damien Shocked at left
            "Damien turns to you, taken aback."
            D "W-What?"
            show chelsea laugh
            "You laugh, gently nudging him."
            pcname "Go on. I bet you'd be great at it."
            "Damien seems to pick up on your teasing and lets out a small, shy smile."
            show Damien Happy at left
            D "Nah. I think I'll save that for the professionals."
            show chelsea sad
            pcname "Aw, not even for me?"
            show Damien Glare at left
            "Damien seems to actually consider this, much to your surprise."
            show Damien Happy at left
            D "Well... Maybe for you."
            show chelsea happy
            "His voice is so soft you almost miss it. By now the sun has descended far over the horizon, leaving a brilliant inky sky in its wake. Damien takes your hand, leading you back into the festival."
            $ damieneveningshows = True
            jump damien_festivalnighttime

label damien_festivalnighttime:
    scene bg FestN with fade
    show chelsea at right with moveinright
    show Damien Happy at left with moveinleft
    "As nighttime descends, many of the festival booths try to gather as many customers as they can before the event ends."
    if damienafternoonfood == True and damieneveningfood == True:
        jump damien_festivalshavedice
    elif damienafternoongames == True and damieneveninggames == True:
        jump damien_festivalfireworks
    elif damienafternoonshows == True and damieneveningshows == True:
        jump damien_festivalringtoss
    elif damienafternoonfood == True and damieneveninggames == True:
        jump damien_festivalfireworks
    elif damienafternoonshows == True and damieneveninggames == True:
        jump damien_festivalshavedice
    elif damienafternoongames == True and damieneveningfood == True:
        jump damien_festivalfireworks
    elif damienafternoonfood == True and damieneveningshows == True:
        jump damien_festivalringtoss

label damien_festivalfireworks:
    "Most of the people attending the festival have begun to clear out from the main street, creating a new, denser crowd at a park adjacent to the street."
    "You and Damien follow the others, leaving behind the bright festival and venturing out into the grassy fields of the park, where several others have set out blankets and gathered in excited groups."
    "As if reading your curiosity, Damien speaks up."
    show Damien Neutral at left
    D "It's almost time for the fireworks. There was a poster about it on one of the tents."
    show Damien Happy at left
    show chelsea shocked
    pcname "Oh."
    show chelsea happy
    "The idea of fireworks sounds pleasant to you. It's been a long time since you've had the chance to enjoy them."
    show Damien Worry at left
    show chelsea confused
    "Damien leads you out on top of a grassy hill in the park, a little bit away from the crowd. As you go to sit down, Damien gently pulls you down onto his lap. You look at him curiously, but he blushes, looking elsewhere."
    D "I don't want your clothes to get dirty."
    show chelsea happy
    show Damien Happy at left
    "You relax against him.. Heat radiates off of him and you lean closer into his touch."
    "There is still some more chatter from the crowd below. You smile, enjoying the quiet from above."
    scene bg black with dissolve
    show bg DKS3 with dissolve
    "Suddenly, the first firework goes off, and the crowd jeers. The sky illuminates in a bright blue, shortly surrounded by another row of white, and then green."
    "You stare up at the lights and your mouth opens just a little in awe. It would've been harder to enjoy them surrounded by so many others, but up on this hill, away from the crowd, you get a perfect view of them against the backdrop of the city."
    "Neither of you speak for some time, content to enjoy the fireworks as they brighten the sky in an array of glorious colors and sparks."
    "Damien sighs lightly. Peering up at him, you see that he isn't staring at the fireworks at all. Instead, his attention is solely focused on you, a gentle smile on his face."
    "He glances away in embarrassment at having been caught, but it isn't long before he's glancing back in your direction with a small smile."
    pcname "Are you enjoying the show?"
    D "Mhm."
    "Even though he agrees, it does not seem to you that he's even paid attention to the show since it began."
    "His eyes do not leave yours, and you find it difficult to pay attention to the fireworks anymore."
    "You feel his heart beat against your back, a steady rhythm under his shirt. You feel warm and comfortable in his arms, enjoying the heat of his body against the chilly night."
    D "Hey, [pcname]...?"
    "You bite your lip, anticipating his question."
    D "Will you be my girlfriend?"
    menu damien_girlfriend1:
        "Accept." if True:
            $ corruption -= 1
            "A smile spreads across your lips, betraying the nervousness of your heart hammering in your chest."
            if club == "track":
                pcname "Absolutely!"
            elif club == "cheer":
                pcname "Totally!"
            elif club == "yearbook":
                "Y-Yes!"
            "Damien smiles, relieved. He almost lets out a laugh, and his arms tighten stronger around your waist as he buries his face into your hair."
            show bg DKS4 with dissolve
            "You clutch onto him, then turn around to straddle him."
            if damienconfidence > 50:
                "Before you get the chance to, Damien presses his lips against yours fervently, his tongue slipping between your lips."
                "You feel his hands wander across your back, resting just above your ass. You adjust a little so they fall lower. He doesn't seem to mind."
                "His kissing is inexperienced, but you don't mind as his eagerness easily makes up for it. His tongue roams the inside of your mouth, pressing deeply, and you react in full, brushing your tongue underneath his in encouragement."
                "He rolls on top of you. The ground feels cold against your back, but you don't mind, simply entwining your legs with his to capture his warmth."
                "You grip his hair, and he returns in full, his lips moving against yours in a steady, excited rhythm."
                "Just as suddenly as it had started, Damien pulls away, gasping for breath. You do the same, finally acknowledging the heat that has risen to your cheeks."
                "Damien smiles at you and bows his head against yours, nuzzling your noses together. You smile back."
                "He rolls onto his side and pulls you against his chest. You cuddle up to him close and watch the rest of the fireworks in silence, your breathing slowing down and your faces paling back to normal."
            elif True:
                "You thrust your arms around Damien's shoulders and yank him close to you, forcing your lips on his. He lets out a little squeal of surprise, but slowly melts into your embrace, trying to keep up."
                "His kissing is inexperienced, but he makes it up with his eagerness. You shove your tongue deeply into his mouth, teasing his with small traces and strokes. He moans a little, wrapping his arms tightly around your waist."
                "You grab his hands, forcing them against your ass. His fingers shake, as though he will pull away, but you hold them there firmly until you're sure he'll let them stay, never once taking your mouth away from him."
                "When you release his hands, they remain where they are, but make no attempt to grope. That's fine. This can always be remedied later."
                "You push him down against the grass until he's flat on his back. His hands roam across your body as you continue your fervent assault on his mouth."
                "With a slight gasp, you pull away. Based on the slight movement of his lips you know he wanted more, but he twists them into a smile, equally breathless as you."
                "Rolling onto your side, you cuddle up against his chest, intertwining your legs as much as your skirt will allow."
            "The finale lights up the sky like daytime before you. Damien kisses you again. You almost lose yourself in him, but as soon as the booming ends, he pulls away, offering you his hand. You take it."
            D "We should get you home."
            "As much as you want to stay here, nestled beside him under the stars for the rest of the night, the chilling air warns you against it."
            pcname "Alright."
            $ damienrelate = "dating"
            jump damien_afterfestival
        "Reject." if True:
            $ corruption += 1
            show chelsea blank
            "Damien brushes a piece of your loose hair behind your ear. Without waiting for your answer, he leans in to kiss you."
            "You duck your head away, having nothing else to look at but the exploding sky above. While you cannot see his face, you feel Damien's grip on you loosen, pulling away some."
            show chelsea sad
            pcname "I'm sorry."
            show chelsea blank
            "You aren't sure what else to say. The idea of committing yourself to Damien feels wrong somehow. You don't know how to explain it, and you hope that you don't have to."
            "Damien says nothing, pulling away. You slide off of his lap, a little disappointed by the cold, hard ground against your ass instead of his warm lap, but you don't object."
            "You both stare up at the fireworks as they finish their finale, your ears a little numb to the sound."
            "Neither of you move as soon as it ends. You wait a bit, and then, Damien quietly gets up. You follow him, brushing the dirt off of your clothes."
            D "We should go now."
            pcname "Yeah..."
            "The walk back to your apartment is quiet and awkward. You aren't really sure what to say, if you should say anything at all."
            "Damien doesn't walk with you up to your door but lingers behind."
            D "I'll see you at school."
            "He slumps down the sidewalk, rejection weighing him down."
            pcname "See you then."
            "You aren't sure if he heard you, but it doesn't really matter. You enter the apartment and allow the night to come to an end."
            hide chelsea with dissolve
            $ damiendate = False
            jump events_end_period
label damien_festivalringtoss:
    "The flashing lights of festival game booths blink brightly in the night, and you find yourself craving one last game before the festival ends."
    show chelsea happy
    "Taking Damien's hand, you lead him through the crowd, searching for the right one."
    show Damien Shocked at left
    "As you search, you feel Damien stiffen at your side. You look back at him, concerned, only to find him frozen in a sort of awe."
    "You follow his gaze and find a large, stuffed gray hippo hanging from one of the tent's roofs, surrounded by other giant stuffed animals of similar nature."
    show Damien Happy at left
    "An excited girl, no older than you, runs the ring toss booth that the hippo belongs to, hanging out small rings and stepping out of the way for customers to toss them in the air."
    "A loud bell rings as a small child gets their ring around a specifically labeled bottle. The child jumps in the air, triumphant."
    show GCBoy with dissolve
    "Ring Toss Worker" "Congrats! Choose anything from the top!"
    "He gestures toward the row where the hippo resides. The child contemplates, staring at each of them seriously. Damien squeezes your hand as the child stares at the hippo."
    "Ring Toss Child" "The zebra!"
    show Damien Neutral at left
    "Damien sighs in relief as the worker takes down the zebra and passes it to the child."
    show Damien Happy at left
    "Ring Toss Worker" "Thanks for playing! Come again!"
    "He waves the child goodbye. Damien spares a longing glance in your direction, but you're already leading him to the booth."
    "The worker smiles at you, energetic despite the late hour."
    "Ring Toss Worker" "Welcome! Would you like to play?"
    pcname "Yes, please."
    "As you reach for your wallet, Damien shoves money into her hand, his eagerness showing. You smile as he accepts a set of three rings, staring out over the row of glass bottles."
    show chelsea blank
    "Some bottles have blue pieces of tape around their lips. Others have red, and the rest yellow. You see a sign nearby that indicates their meanings: Blue is small, yellow is medium, and red is large."
    "You glance up at the hippo. It's definitely the largest stuffed animal there, perhaps aside from the stretching giraffe next to it."
    "Damien adjusts himself behind the counter, staring at the set of bottles with an intensity you did not know he was capable of. Swinging his arm back, he tosses the first ring."
    show Damien Sad at left
    "It smacks against the lip of one of the plain glass bottles, falling between them. Damien frowns."
    "Ring Toss Worker" "Two more to go!"
    show Damien Glare at left
    "Damien adjusts himself, standing upright, as if it was his posture that prevented him from getting the right bottle. He releases the second ring."
    "It circles the top of a yellow bottle before promptly falling over, out of range."
    "Ring Toss Worker" "One more!"
    show Damien Blank at left
    "His words seem like a countdown. Damien takes a deep breath and swings."
    show Damien Worry at left
    "It hits the back wall of the booth, nowhere near the table. He slumps in defeat."
    show Damien Sad at left
    "Ring Toss Worker" "Aww, too bad!"
    pcname "I'd like to try."
    show Damien Blank at left
    "Damien places the money on the counter and the guy smiles brightly, passing the rings to you this time."
    "Ring Toss Worker" "Good luck!"
    "He steps out of the way, giving you plenty of room to throw."
    "You take a deep breath, angling yourself, and toss the first ring."
    show chelsea angry
    "It lands between a blue bottle and a yellow one, stuck in the middle. You let out a breath of frustration."
    "Ring Toss Worker" "One down, two to go!"
    show chelsea blank
    "You adjust yourself slightly, flicking the next ring across with your wrist."
    "It smacks against the top of one of the red bottles, bouncing off onto a clear one. You mutter under your breath."
    "Ring Toss Worker" "Last one!"
    "You find yourself annoyed at the worker as you try to best position yourself across from the bottles. His and Damien's eyes are on you, waiting to see what will happen."
    "You release the last ring."
    "It makes a loud round of clinks as it falls directly around the red-rimmed bottle."
    show chelsea happy
    show Damien Laugh at left
    "You and Damien let out a whoop of excitement as the game's bell dings loudly for the crowd to know."
    "Ring Toss Worker" "Congrats! You can pick anything from the top row."
    "He gestures toward the large stuffed animals. You don't need to even consider it."
    show Damien Happy at left
    pcname "The hippo, please."
    "The worker pulls down the hippo from the ceiling and places it in your arms. You grin, passing it to Damien. He looks as giddy as a child."
    "Ring Toss Worker" "Thank you for playing! Come again!"
    "He waves, and you both carry on through the festival. Many of the booths are closing at this point, and you catch the first boom of fireworks as they rise up into the sky."
    D "Thank you."
    "Damien presses the hippo to your cheek and mimics a kiss. You laugh."
    pcname "Sure. Have you given it a name yet?"
    D "No, not yet. What do you think we should name it?"
    $ hipponame = renpy.input("What would you like to name the hippo?", default="Helga", length=12)
    $ renpy.pause
    $ hipponame = hipponame.strip()
    if hipponame == "":
        $ hipponame = "Helga"
    pcname "[hipponame]."
    "Damien gives a soft smile, clutching the hippo close."
    D "I like that."
    "As the fireworks go off in the distance, you notice Damien staring at you, a dreamy look in his eyes. The colors reflect in the hippo's eyes."
    show Damien Neutral at left
    D "Hey, [pcname]...?"
    pcname "Yeah?"
    "The fireworks feel faraway as you stare into each other's eyes. You know what he's about to ask, but you don't dare interrupt."
    D "Will you be my girlfriend?"
    show chelsea shocked
    show Damien Blank at left
    menu damien_girlfriend2:
        "Accept." if True:
            $ corruption -= 1
            "Your heart hammers in your ears, and you struggle to get an answer out."
            show chelsea happy
            if club == "track":
                pcname "Absolutely!"
            elif club == "cheer":
                pcname "Totally!"
            elif club == "yearbook":
                pcname "Y-Yes!"
            show Damien Happy at left
            "Damien lets out a deep sigh of relief, his death grip on the hippo lessened. Neither of you seemed to have noticed before just how hard he was clutching it."
            "He stares at your lips, hesitating, before he leans in."
            show Damien Laugh at left
            "You snatch the hippo and press it against his face. Damien blinks, surprised, before bursting into laughter."
            show Damien Happy at left
            scene bg DKS2 with dissolve
            if damienconfidence > 50:
                "Damien shoves the hippo away and grabs you by the waist, pulling you into a deep and sudden kiss."
                "You nearly drop the hippo as you throw your arms around his shoulders, allowing him to pull you further into his embrace. His fingers dig into your waist desperately, clutching you to him."
                "While his kiss is inexperienced, there is no mistaking the adoration and desperation he has for you. You melt against him, allowing his tongue to trace inside of your mouth, against your teeth, brushing the inside of your cheeks."
            elif True:
                "You tuck the hippo under your arm and grab Damien's shirt, yanking him into a deep kiss. He's startled for a moment, but slowly wraps his arms around your waist, melting into your touch."
                "His kissing is inexperienced, but neither of you seem to mind as you lead him with your tongue, tracing the inside of his mouth as deeply as he will allow."
            "You both remain as such for a moment, desperately clinging to each other in a frenzy. Then, you part, breathless and happy."
            "The finale of the fireworks takes you back to reality, filling your ears with enormous bangs and crashes of light in the sky. You both glance up at it, neither willing to remove your arms from around each other."
            show bg black with dissolve
            D "I guess we should get back then."
            "You don't want this moment to end, but the walk back with him by your side doesn't seem like it truly will."
            pcname "Alright."
            $ damienrelate = "dating"
            jump damien_afterfestival
        "Reject." if True:
            $ corruption += 1
            "You find yourself speechless for a moment. Then a moment longer. And longer still."
            "Unsure of what to make of this, Damien leans forward for a kiss."
            show chelsea laugh
            "You grab the hippo and press it to his face. He blinks, startled, and pulls back. You press the hippo into his arms and give an awkward laugh."
            pcname "You already have a girlfriend!"
            show chelsea sad
            "You try to play it off, but the hurt is evident on his face. Your laughter dies uncomfortably. You give an awkward cough."
            D "You can just say no, if you don't want to."
            "You hesitate, bracing yourself."
            pcname "...No. I don't want to be your girlfriend."
            "Damien nods, clearly struggling with this rejection. You both stand there uncomfortably for a moment before he turns."
            D "We should get you home."
            show chelsea blank
            pcname "Yeah..."
            "The walk home is quiet, the magic of the day worn off. You reach your door. He doesn't follow."
            D "See you at school."
            "He turns, making his way back down the sidewalk. His shoulders are slumped, hands stuffed deeply in his pockets, as if he can disappear."
            pcname "See you then."
            hide Damien Sad with dissolve
            "You're sure he hasn't heard you, but it doesn't matter. You go back inside, putting the night to an end."
            hide chelsea with dissolve
            $ damiendate = False
            jump events_end_period

label damien_festivalshavedice:
    "As the festival comes to the end, you find yourself craving something sweet to finish off the night."
    "Lucky for you, you happen to pass quite a few people with large paper bowls filled with colorful shaved ice."
    "Following the crowd, you and Damien approach the stand, listening to the sound of machines whir as they crank out as many shaved ice cones as they can."
    D "I haven't had this in so long."
    show chelsea happy
    pcname "Let's get some, then."
    "You both approach the cash register. As the end of the night approaches, the line isn't very long at all, and you're up to the counter in no time."
    "A kind, middle-aged woman stands behind the register, a tired smile on her face."
    "Shaved Ice Worker" "Welcome! What can I get for you today?"
    menu damien_shavediceflavors:
        "Cherry." if True:
            "The woman inputs your order into her computer. Damien passes over the money, and shortly after, she returns with your cups of shaved ice."
            "Shaved Ice Worker" "Thank you! Have a lovely night!"
            "You both find a free bench not too far away and take occupancy there, settling the shaved ice on your laps."
            "Damien looks at yours curiously as you take a large mouthful. The red dye makes your lips just a little bit redder."
            pcname "What flavor did you get?"
            "You look at his light pink ice. You don't recall anything like that being on the menu."
            D "Strawberry."
            "You must have missed it. Shrugging it off, you take another bite of your ice."
            "On your next scoop, you offer it to Damien's lips."
            pcname "Here, try some."
            "Damien gives the shaved ice a curious look, tempted by your offer."
            D "Nah, I shouldn't. It's yours."
            "You shove the spoon closer to him."
            pcname "I insist."
            "He hesitates for a moment, then covers the spoon with his mouth."
            "A smile curls on his lips. He pulls back, licking his lips. They're also a little more red."
            D "That was really good..."
            "Damien looks down at his own shaved ice, a little disappointed. You secretly feel pleased at your decision."
            "You both eat in silence for a little bit, most of the crowd gone home or rushing to catch one of the last-minute performances."
            "He takes out a spoonful after a bit, offering it to you."
            D "Here. Try mine."
            "Without hesitation, you take the spoon into your mouth, pulling the flavored ice in. It's sweet and only slightly tangy. It still doesn't compete with your cherry, though."
            "You resume eating your ice, refusing any further offers."
            D "Well?"
            pcname "It's good."
            D "Only good?"
            "You stick your tongue out, showing off the bright red color."
            pcname "Only good."
            show chelsea shocked
            show Damien Shocked at left
            "Damien chuckles. A sudden boom causes you both to jump, and looking up, you immediately find the cause."
        "Orange." if True:
            "The woman inputs your order into her computer. Damien passes over the money, and shortly after, she returns with your cups of shaved ice."
            "Shaved Ice Worker" "Thank you! Have a lovely night!"
            "You both find a free bench not too far away and take occupancy there, settling the shaved ice on your laps."
            "Damien looks at yours curiously as you take a large mouthful. The orange is almost sickeningly sweet, but you take in the citrus flavor with pleasure."
            pcname "What flavor did you get?"
            "You look at his light pink ice. You don't recall anything like that being on the menu."
            D "Strawberry."
            "You must have missed it. Shrugging it off, you take another bite of your ice."
            "On your next scoop, you offer it to Damien's lips."
            pcname "Here, try some."
            "Damien gives the shaved ice a curious look, tempted by your offer."
            D "Nah, I shouldn't. It's yours."
            "You shove the spoon closer to him."
            pcname "I insist."
            "He hesitates for a moment, then covers the spoon with his mouth."
            "A smile curls on his lips. He pulls back, licking his lips. You notice a small squirt of orange syrup drip down his chin."
            D "That was really good..."
            "Damien looks down at his own shaved ice, a little disappointed. You secretly feel pleased at your decision."
            "You both eat in silence for a little bit, most of the crowd gone home or rushing to catch one of the last-minute performances."
            "He takes out a spoonful after a bit, offering it to you."
            D "Here. Try mine."
            "Without hesitation, you take the spoon into your mouth, pulling the flavored ice in. It's sweet and only slightly tangy. It still doesn't compete with your orange, though."
            "You resume eating your ice, refusing any further offers."
            D "Well?"
            pcname "It's good."
            D "Only good?"
            "You stick your tongue out, showing off the light orange color."
            pcname "Only good."
            show chelsea shocked
            show Damien Shocked at left
            "Damien chuckles. A sudden boom causes you both to jump, and looking up, you immediately find the cause."
        "Lemon." if True:
            "The woman inputs your order into her computer. Damien passes over the money, and shortly after, she returns with your cups of shaved ice."
            "Shaved Ice Worker" "Thank you! Have a lovely night!"
            "Damien wrinkles his nose at your ice as you both nestle down on a nearby bench to enjoy your dessert."
            pcname "What flavor did you get?"
            "You peer at his plain pink shaved ice curiously."
            D "Strawberry."
            pcname "I didn't even see that on there."
            "Damien looks back at your dessert, bemused. The top of the ice is steeped in a deep yellow and faces out to white, like rays of the sun. Damien doesn't seem to share your opinion."
            pcname "What?"
            D "Well..."
            "You take a small mouthful, letting the tart lemon flavor sink into your taste buds. Damien makes a sour face."
            D "Doesn't it look... gross?"
            pcname "Gross?"
            D "Like..."
            "You stare at the ice, a sort of understanding between you. He thought it looked like piss. You couldn't blame him exactly. Yellow snow is just that. But still..."
            "You offer a spoonful to Damien."
            pcname "Here, try some."
            "Damien makes no attempt to disguise his disgust."
            D "I'm good..."
            "You push the spoon closer to his lips."
            pcname "No, really. Come on. Just a taste."
            "Damien stares down at the shaved ice, a little squeamish."
            "Finally, he takes a bite."
            "His face immediately twists and wrenches in disgust. It takes all he can not to spit it out on the ground. You try to hold back your laughter as he is forced to swallow it."
            "He releases a hacking cough once he's finished taking in the bitter flavor. This only makes you giggle harder."
            D "You... You really like that...?"
            pcname "Doesn't it taste better than urine?"
            D "Not... particularly..."
            pcname "Are you suggesting you've {i}tried{/i} urine?"
            D "No! Of course not!"
            "You both laugh, Damien eagerly scooping up his strawberry ice into his mouth to get rid of the taste."
            "He takes out a spoonful after a bit, offering it to you."
            D "Here. Try mine."
            "Without hesitation, you take the spoon into your mouth, pulling the flavored ice in. It's sweet and only slightly tangy. It isn't bad, but you prefer the tartness of your lemon ice- no matter how ill it appears."
            pcname "It's good."
            D "Only good?"
            pcname "Only good."
            show chelsea shocked
            show Damien Shocked at left
            "Damien shrugs, accepting this. A sudden boom causes you both to jump, and looking up, you immediately find the cause."
        "Blue raspberry." if True:
            "The woman inputs your order into her computer. Damien passes over the money, and shortly after, she returns with your cups of shaved ice."
            "Shaved Ice Worker" "Thank you! Have a lovely night!"
            "You both find a free bench not too far away and take occupancy there, settling the shaved ice on your laps."
            "Damien looks at yours curiously as you take a large mouthful. The blue dye makes your lips just a little bit purple."
            pcname "What flavor did you get?"
            "You look at his light pink ice. You don't recall anything like that being on the menu."
            D "Strawberry."
            "You must have missed it. Shrugging it off, you take another bite of your ice."
            "On your next scoop, you offer it to Damien's lips."
            pcname "Here, try some."
            "Damien gives the shaved ice a curious look, tempted by your offer."
            D "Nah, I shouldn't. It's yours."
            "You shove the spoon closer to him."
            pcname "I insist."
            "He hesitates for a moment, then covers the spoon with his mouth."
            "A smile curls on his lips. He pulls back, licking his lips. They're also a little bluer."
            D "That was really good..."
            "Damien looks down at his own shaved ice, a little disappointed. You secretly feel pleased at your decision."
            "You both eat in silence for a little bit, most of the crowd gone home or rushing to catch one of the last-minute performances."
            "He takes out a spoonful after a bit, offering it to you."
            D "Here. Try mine."
            "Without hesitation, you take the spoon into your mouth, pulling the flavored ice in. It's sweet and only slightly tangy. It still doesn't compete with your blue raspberry, though."
            "You resume eating your ice, refusing any further offers."
            D "Well?"
            pcname "It's good."
            D "Only good?"
            "You stick your tongue out, showing off the bright blue dye that's settled there."
            pcname "Only good."
            show chelsea shocked
            show Damien Shocked at left
            "Damien chuckles. A sudden boom causes you both to jump, and looking up, you immediately find the cause."
        "Grape." if True:
            "The woman inputs your order into her computer. Damien passes over the money, and shortly after, she returns with your cups of shaved ice."
            "Shaved Ice Worker" "Thank you! Have a lovely night!"
            "Damien gives your shaved ice a quizzical look as you both nestle down on a nearby bench to enjoy your dessert."
            pcname "What flavor did you get?"
            "You peer at his plain pink shaved ice curiously."
            D "Strawberry."
            pcname "I didn't even see that on there."
            "Damien looks back at your dessert, bemused. The way the dark purple dye fades over the pale ice makes it look more like a geode than desert."
            "You take a small mouthful, letting the bitter grape flavor sink into your taste buds."
            "You offer a spoonful to Damien."
            pcname "Here, try some."
            "Damien eyes the shaved ice with not nearly as much adventurous interest as you had in ordering it."
            D "I'm good..."
            "You push the spoon closer to his lips."
            pcname "No, really. Come on. Just a taste."
            "Damien stares down at the shaved ice with knitted eyebrows."
            "Finally, he takes a bite."
            "His face immediately twists and wrenches in disgust. It takes all he can not to spit it out on the ground. You try to hold back your laughter as he is forced to swallow it."
            "He releases a hacking cough once he's finished taking in the bitter flavor. This only makes you giggle harder."
            D "You... You really like that...?"
            pcname "You don't like grape?"
            D "Not... particularly..."
            "You shrug and resume eating your shaved ice. Damien does the same."
            "He takes out a spoonful after a bit, offering it to you."
            D "Here. Try mine."
            "Without hesitation, you take the spoon into your mouth, pulling the flavored ice in. It's sweet and only slightly tangy. It isn't bad, but you prefer the bitter flavor of your grape ice."
            pcname "It's good."
            D "Only good?"
            pcname "Only good."
            show chelsea shocked
            show Damien Shocked at left
            "Damien shrugs, accepting this. A sudden boom causes you both to jump, and looking up, you immediately find the cause."
        "All of the above." if True:
            "It's your final snack of the night, and you decide to throw caution to the wind."
            pcname "All of the flavors, please."
            "The worker gives you a blank, confused look, but types it into her computer without objection. She's clearly ready for the night to be over."
            "Damien gives you an equally confused look but passes her the money. After a few moments, she brings back your cups of shaved ice."
            "Shaved Ice Worker" "Thank you! Have a lovely night!"
            "Damien gives your shaved ice a quizzical look as you both nestle down on a nearby bench to enjoy your dessert."
            pcname "What flavor did you get?"
            "You peer at his plain pink shaved ice curiously."
            D "Strawberry."
            pcname "I didn't even see that on there."
            "Damien looks back at your dessert, bemused. The faint pallor of the ice is gone, drenched in so much syrup that it appears to be a murky purple."
            D "Well, I'm sure you'll taste some of it."
            "You take a small mouthful, letting the flavors battle each other in your mouth. It reminds you of a sickeningly sweet fruit punch."
            "You offer a spoonful to Damien."
            pcname "Here, try some."
            "Damien eyes the shaved ice with not nearly as much adventurous interest as you had in ordering it."
            D "I'm good..."
            "You push the spoon closer to his lips."
            pcname "No, really. Come on. Just a taste."
            "Damien stares down at the shaved ice as if it is poison. You watch the internal struggle to be polite as well as his disgust battle on his face."
            "Finally, he takes a bite."
            "His face immediately twists and wrenches in disgust. It takes all he can not to spit it out on the ground. You try to hold back your laughter as he is forced to swallow it."
            "He releases a hacking cough once he's finished taking in the flavors. This only makes you giggle harder."
            D "You can't possibly like that."
            "You prove him wrong by taking a large scoopful into your mouth. You make a loud hum, pretending to savor the flavors far more than you actually do."
            "Damien shakes his head, thoroughly amused, and resumes eating his own shaved ice."
            "He takes out a spoonful after a bit, offering it to you."
            D "Here. Try mine."
            "Without hesitation, you take the spoon into your mouth, pulling the flavored ice in. It's sweet and only slightly tangy. You hate to admit it, but the solid flavor might be just a little bit better than your mixed chaos."
            "Damien seems to notice this, as he cannot take the smirk off of his face. You try not to give him the satisfaction of knowing how good it actually is."
            pcname "It's good."
            D "Only good?"
            pcname "Only good."
            show chelsea shocked
            show Damien Shocked at left
            "Damien chuckles. A sudden boom causes you both to jump, and looking up, you immediately find the cause."
    show chelsea happy
    show Damien Happy at left
    "Bright flashes appear above the tents as the festival's fireworks go off, casting an array of colors across the dark sky."
    "They light up the entire street, reflecting their colors across your faces."
    "You both watch the fireworks in a dazed silence, taking in the beautiful scene and the sweet taste of syrup on your lips."
    "Gently, Damien's hand clasps over yours. You peer over to find him staring not at the fireworks, but at you directly."
    D "[pcname], I've had a really great time today. And, well, I want to have more times like this with you..."
    show Damien Worry at left
    "He hesitates, and it's clear he has more to say. Gathering his courage, he continues."
    show Damien Neutral at left
    D "Will you be my girlfriend?"
    show chelsea shocked
    menu damien_girlfriend3:
        "Accept." if True:
            $ corruption -= 1
            "Your heart beats fast in your ears. For a moment, you're stunned into silence. You struggle to gather yourself before he becomes discouraged."
            if club == "track":
                show chelsea happy
                pcname "Absolutely!"
            elif club == "cheer":
                show chelsea happy
                pcname "Um, yes!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Y-Yes!"
            show Damien Happy at left
            "Damien breaks out into a relieved grin. His hand tightens over yours, thrilled."
            D "Really? Great! I mean, er, wow..."
            "Just as you had been shocked upon hearing the question, he's equally stunned to hear your answer."
            "He hesitates for a moment, staring at your syrup-stained lips."
            scene bg DKS1 with dissolve
            if damienconfidence > 50:
                "He leans forward, kissing you on the lips. He's ill-practiced, but he does it with such excitement that you can't complain."
                "He pulls you close against him, forcing your chest to meet his as his tongue slips deeper."
            elif True:
                "You push yourself forward, forcing your lips onto his. He lets out a startled noise, but you press yourself against him, hoping he will take the hint."
                "Slower than you would like, he wraps his hands around your waist and finds the strength to kiss you back. He's inexperienced and that much is clear, but you take control of the situation, forcing him to follow your pace. He quickly catches on."
            "Wrapping your hands in his hair, you encourage him, using your tongue to lead him properly with your mouth. You can taste the mingled flavors of both of your shaved ice coming together."
            "For some time, there is nothing else in the world except for your warm tongues and the colorful flashes in the sky."
            "Then, somehow, you manage to slow your kisses, pulling away a little more each time until they are nothing more than soft pecks."
            "You both pull back, smiling at each other, breathless and excited."
            "Several booms erupt in the sky, signaling the fireworks' finale. You sit back and watch together, his arm around your waist and your head perched on his shoulder. Nothing could make you happier."
            show bg black with dissolve
            $ damienrelate = "dating"
            jump damien_afterfestival
        "Reject." if True:
            $ corruption += 1
            show chelsea blank
            "As lovely as this day has been, something nags in the back of your head, and you can't bring it in yourself to commit to him."
            "He waits with baited breath on your response, but as the time lengthens, his shoulders slump with lack of encouragement. He seems to understand."
            "You aren't sure what else to say."
            show chelsea sad
            pcname "I'm sorry..."
            "Damien takes his hand away, grasping his shaved ice tightly. He stares back up at the fireworks, and while it's difficult to see, you catch sight of the embarrassment across his face."
            D "It's fine. I understand."
            show chelsea blank
            "Neither of you say a word, even long after the fireworks have ended. Damien walks you back to your apartment in a thick, awkward silence. You haven't even had the courage to look at each other."
            "Once you reach your front door, you both stand there for a moment, stiff and tense."
            D "I guess I'll see you at school."
            "You're so startled to hear his voice after so long that you lapse into momentary speechlessness."
            "Damien has already turned and begun walking back up the street, his shoulders slumped with rejection."
            pcname "See you then."
            "You aren't even sure he's heard you, but you're fine with that."
            hide Damien Sad with dissolve
            "You step into your apartment, bidding the night an end."
            hide chelsea with dissolve
            $ damiendate = False
            jump events_end_period

label damien_afterfestival:
    scene bg CityN with fade
    show chelsea happy at right with moveinright
    show Damien Happy at left with moveinleft
    if damienrelate == "dating":
        "The walk back to your apartment is blissful. Damien is never a touch away from you, his hand either clasped in yours or his arm trailing from over your shoulder to around your waist."
        "You talk the entire way back, your sentences each bouncing off of each other into whole new conversations. You have never seen him smile so much at once, and the sight warms your heart."
        show chelsea confused
        pcname "And what does that have to do with your scar?"
        show chelsea blank
        "You point to the little scar on his left cheek mid-conversation. He had just been telling an elaborate story on his childhood that he managed to sidetrack one too many times."
        D "Oh! Right. Well, like I said, I was trying to dig a hole under my neighbor's fence, see? And I was small enough that I sort of army-crawled underneath to get through."
        D "Well, I didn't know that they had just gotten a new dog. This thing was tiny, but she yapped up a storm. As soon as she saw my face pop up under her face, she darted right over."
        D "I tried to crawl out of there, but she bit into my arm. Not very hard, the scar is gone now, but she went again at my face, and it got pretty deep. I had to get stitches and everything."
        show chelsea sad
        pcname "That's terrible..."
        pcname "What happened to the dog?"
        show Damien Sad at left
        "Damien looks guiltily at his feet. This part bothered him most."
        D "Well... She got put down. I didn't want it to happen, but my parents caused a big fuss, and, well..."
        D "I feel really bad about it now. It wasn't her fault. I was the one trying to trespass on her new territory, you know?"
        pcname "Yeah..."
        show chelsea blank
        show Damien Blank at left
        "The return to your front door is too short and bittersweet. You turn regretfully on your doorstep, wishing this moment could last longer..."
    menu damien_stayafterfestival:
        "Ask to stay the night." if True:
            show Damien Happy at left
            D "Well, I guess I should get going..."
            "As he turns, you grab his sleeve. He stops."
            if club == "track":
                "You'd hate to see this night end already. The words pour out of you before you have a chance to think it over."
                show chelsea happy
                pcname "It's pretty late. You could stay the night if you'd like."
            elif club == "cheer":
                "He looks just as miserable to leave as you are to see him go. It wouldn't hurt to spend a little more time together."
                show chelsea happy
                pcname "Why don't you sleep over tonight?"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I-I was thinking... maybe... It's a long walk home, after all..."
                pcname "Y-You could stay the night... if you want to..."
                "You feel embarrassed saying it, but you can't help but hope that he'll accept."
            "Even through the darkness, you can see the faint blush on his cheeks."
            show chelsea blank
            show Damien Neutral at left
            D "Ah, stay over?"
            show Damien Blank at left
            pcname "You don't have to stay in my room if you aren't comfortable with it. You can sleep on the couch."
            show Damien Shocked at left
            D "Oh, no! The couch would be fine! I wouldn't dream of intruding."
            if damienknowsaboutfamily==False:
                show Damien Neutral at left
                show chelsea sad
                D "But won't your parents mind? I mean, a boy staying over..."
                menu damien_parentssleepover:
                    "My parents are dead." if True:
                        "You hesitate, the familiar pain rising in your chest at the thought of your parents."
                        "You didn't want to ruin your nice date, but you can't exactly lie to Damien, especially now that you're his girlfriend."
                        pcname "My parents... They're, um, they passed away, actually."
                        "You can barely get the words past the lump in your throat. It still feels too soon to talk about."
                        show Damien Shocked
                        D "Dead?"
                        show Damien Sad
                        D "I'm so sorry, [pcname]. I... I had no idea..."
                        show Damien Blank
                        pcname "It's okay. I don't really like to talk about it..."
                        pcname "But... Yeah. It would just be you and me inside."
                        show Damien Sad
                        D "I see..."
                        show Damien Neutral
                        D "Well, okay then. I'll stay. It must get really lonely being by yourself in there all the time, anyway."
                        pcname "Well, sometimes. Yeah."
                        $ damienknowsaboutfamily=True
                    "They're away on vacation." if True:
                        "You feel a pang in your chest at the reminder of your parents, but you aren't about to ruin your nice date with the mention of their deaths."
                        "He'll find out about it... someday. Now isn't the time."
                        show chelsea happy
                        pcname "O-Oh, no, it'll be fine!"
                        show chelsea laugh
                        pcname "My parents are... they're away on vacation. I've got the whole place to myself."
                        show Damien Shocked
                        show chelsea blank
                        D "O-Oh. All to yourself...?"
                        show Damien Worry
                        D "And they won't mind me being there...?"
                        show Damien Blank
                        pcname "Nah, they're cool. You'll be fine."
                        show Damien Happy
                        D "Okay... Well, if you say so. Sure, I can stay."
            elif True:
                pass
            show Damien Shocked
            D "J-Just the two of us... Alone... In the apartment..."
            show chelsea happy
            show Damien Blank at left
            "Damien glances between you and the door, obviously flustered. You giggle a little, enjoying his reaction."
            show chelsea blank
            "You open the door. He follows you inside."
            show bg HomeN with fade
            "As you glance around at a few items scattered about, you wish you had thought about this ahead of time. You don't want him to think you're a slob."
            show chelsea happy
            pcname "I'll get you some blankets and pillows from my room."
            "You try to subtly clean up as you talk, tucking magazines into neat stacks and bringing leftover dishes to the sink."
            "Damien doesn't seem to notice. He peers around your apartment cautiously, as though afraid of being scolded for every step he takes."
            pcname "You can relax. Make yourself at home."
            show Damien Neutral at left
            D "Ah, right."
            show Damien Blank at left
            "Even as he says so, his posture seems to stiffen even more."
            pcname "Do you want anything to drink?"
            D "Some water would be nice. Thank you."
            "You make your way to the kitchen and gather him a cup. When you return, he's sitting on the couch. You offer him the drink."
            show Damien Happy at left
            D "Thank you."
            pcname "I'll be right back."
            show chelsea blank
            "You duck into your bedroom and shut the door. The clothes of the day feel heavy and tiresome by now. You slip out of them quickly, exchanging them for some cotton shorts and a tank top."
            "Gathering some extra blankets and pillows from your closet, you return to the living room."
            "Damien seems to have settled into his environment, and instead of looking around in curiosity, his eyes are focused on you. Rather, your legs."
            if corruption > 10:
                show chelsea happy
                "You grin, enjoying the attention."
                pcname "Like what you see?"
                show Damien Worry at left
                "Damien bites his lip, forcing his gaze away in embarrassment."
            elif True:
                show chelsea embarrassed
                "You shift under his gaze, a blush creeping onto your cheeks."
                "He forces himself to look you in the face, but you catch glimpses of his gaze flickering back to your body."
            show chelsea blank
            show Damien Blank at left
            "You offer the soft bundle into his arms."
            pcname "If you need anything else, just let me know."
            show Damien Happy at left
            D "Thank you."
            "Damien stands and you help him set up the couch as a makeshift bed."
            "When you're finished, he grabs the edge of his shirt to remove it on instinct, but quickly pauses, glancing your way."
            show Damien Blank at left
            show chelsea happy
            pcname "You don't need to worry about me. Sleep comfortably."
            "He understands, and, a little more self-consciously, removes his shirt. You intake a sharp breath at the sight of his chest. Although he's a dork, he certainly keeps himself in shape."
            "A part of you wonders what the rest of him looks like under his clothes."
            show chelsea blank
            "You force yourself to turn away and make your way back to your bedroom."
            pcname "Goodnight, Damien."
            "He settles onto the blanket mass."
            show Damien Happy at left
            D "Goodnight, [pcname]."
            hide Damien Happy with dissolve
            "You retreat into your bedroom and gently shut the door behind you."
            show bg RoomN with fade
            "After brushing your teeth and settling yourself into your bed, the exhaustion of the day weighs down on you."
            "You roll on your side, trying not to let your mind wander too much on Damien's body."
            hide chelsea with dissolve
            $ damienstaythenight == True
            jump damien_dream01
        "Kiss goodnight." if True:
            show chelsea happy
            show Damien Happy at left
            "You press your lips against him, lightly at first, but the taste of him draws you in deeper. As you begin to clutch onto his shirt, Damien gently removes your hands, pulling back. You pout up at him, but he smiles, planting a kiss onto your forehead."
            D "Goodnight, [pcname]."
            pcname "Goodnight."
            "You both pull away regretfully, his touch lingering on your skin. You watch him leave, smiling as he casts glances in your direction until he's too far to see."
            hide Damien Happy with dissolve
            "With a small smile, you enter your apartment, allowing the night to draw to a close."
            hide chelsea with dissolve
            $ damiendate = False
            $ DamienAngry = "Characters/Damien/School Uniform/Angry.png"
            $ DamienBlank = "Characters/Damien/School Uniform/Blank.png"
            $ DamienGlare = "Characters/Damien/School Uniform/Glaring.png"
            $ DamienLaugh = "Characters/Damien/School Uniform/Laughing.png"
            $ DamienNeutral = "Characters/Damien/School Uniform/Neutral.png"
            $ DamienSad = "Characters/Damien/School Uniform/Sad.png"
            $ DamienShocked = "Characters/Damien/School Uniform/Shocked.png"
            $ DamienSmiling = "Characters/Damien/School Uniform/Smiling.png"
            $ DamienWorrying = "Characters/Damien/School Uniform/Worrying.png"
            jump endday

label damien_dream01:
    $ acts = 4
    $ day = 1
    $ daycount += 1
    $ skippedwork = False
    $ skippedschool = False
    $ wenttoschool = False
    $ wenttowork = False
    $ wenttoclub = False
    $ goingto = ""
    call events_end_day from _call_events_end_day_2
    call dayeval from _call_dayeval_1
    "In a few moments, you manage to fall asleep."
    show bg ClassroomE with fade
    $ clothes = 'school'
    show chelsea at right with dissolve
    "Or did you? When you open your eyes again, you're back in your classroom."
    show chelsea shocked
    "Did you fall asleep during class? How did you get here?"
    "You try to recall the events of the previous day, but everything is a haze. You remember a festival... Did that really happen?"
    show chelsea blank
    "As you contemplate your whereabouts, a strong hand brushes your hair over your shoulder."
    show Damien Happy with dissolve
    "You turn in your chair and look up at Damien."
    "He smiles down at you, but instead of his school uniform, he's dressed casually in a t-shirt and... Ugh. You wrinkle your nose at his cargo shorts."
    show chelsea confused
    pcname "Cargo shorts again..."
    D "You don't like them?"
    show chelsea blank
    pcname "I hate them."
    show Damien Sad at left with move
    "He frowns down at them for a moment."
    D "Would you like me to get rid of them?"
    "Before you can answer, he reaches for the zipper and pulls them down."
    "His bulge pokes out from a pair of blue boxers. You can't help but stare."
    show Damien Happy at left
    D "Is that better?"
    show chelsea happy
    if club == "track":
        "You nod, satisfied with the change. Perhaps more than satisfied."
        pcname "Yep."
    elif club == "cheer":
        "You bite your lip, your lips drawn into a small smile as you admire his package."
        pcname "Much better."
    elif club == "yearbook":
        "You feel your cheeks inflame. You try to pry your gaze away in shame, but it keeps drawing you back."
        pcname "Y-Yes..."
        "He steps forward, his groin at level with your face. You turn in your seat to face him fully. It's larger than you had expected."
        if corruption > 10:
            "His fingers intertwine into your hair, pulling you toward it. He rubs his groin against your face, pressing his bulge against your lips."
            D "Will you help me out, [pcname]?"
    elif True:
        show Damien Worry at left
        "Damien hesitates, looking down at you shyly."
        D "Ah... I was thinking..."
        D "Maybe... you could..."
        "He looks away, embarrassed. You don't need to be told anything to know what he wants."
    show Damien Happy at left
    "Your fingers slip beneath his underwear, slowly pulling them down. His cock stands erect, the tip brushing lightly against your cheek. He grins down at the sight."
    "You feel heat build up between your thighs. You adjust in your seat, grinding against the plastic chair a little."
    "Licking your lips, you meet his gaze as you press a hard kiss against his tip. He lets out a little gasp, his hips thrusting a little in your direction."
    "You wrap your mouth around his cock, taking him in a little bit at a time. He moans, pressing himself further."
    D "Ah... You... You're really good at this..."
    "You move your mouth against his cock more eagerly, your tongue lapping against his sensitive skin."
    "The wetness between your legs builds, dampening your panties."
    "You pull your mouth away with a sudden {i}pop{/i}, leaving Damien shuddering and disappointed."
    show Damien Sad at left
    D "Why'd you stop?"
    show Damien Happy at left
    hide chelsea with dissolve
    hide Damien Happy with dissolve
    if corruption > 10:
        "He grips your hair tighter, thrusting your face back toward his groin. He leaves you no choice."
        "You take him into your mouth again. He holds your head steady as he thrusts into your mouth. You grind against the chair in succession, your clit rubbing hard against the plastic base between your panties."
        "As he fucks your face, you press your fingers against your panties, rubbing against the damp spot."
        "Unable to take it, you manage to pull back with a whimper."
        pcname "Please... Take care of me, too."
        "You press your hand into your panties, gathering some of the moisture on your fingers. You pull them back out as evidence."
        "Damien stares down at your fingers for a moment before bowing his head to them. He pulls them into his mouth, sucking them off."
        "You let out a small gasp. He pulls them out slowly, his tongue tracing lines between your fingers to make sure he got everything."
        D "I did this to you...?"
        "You nod, squirming a little in your seat. You can feel your moisture leaking out of your panties and onto the seat."
        D "Get on the desk."
        "You follow his orders obediently, propping yourself up on the edge of the hard desk. Damien looks down at the puddle on the seat and grins."
    elif True:
        "You stand from your chair and hoist yourself up onto the desk. He glances down at the small puddle you've left on your seat and blushes."
        "Slowly, you slip out of your panties, taking in his longing expression as you twirl the silk between your fingers."
        pcname "Look what you've done to me."
        "You toss the panties at him. Damien catches them clumsily. He feels the wet patch. His erection hardens."
        D "I did this...?"
        "You nod."
        pcname "And now they're all dirty. {i}I'm{/i} all dirty. How are you going to make it up to me?"
        "You cock your head to the side, a smirk playing on your lips. Damien hesitates, squishing the panties between his fingers eagerly."
    "Taking off his shirt, he lays it over the chair and sits down. You look over his chest eagerly, taking in his lean muscles with interest."
    "Without a word, Damien flips your skirt up and presses his lips against your inner thigh. You shudder slightly, feeling his warm tongue trail in messy kisses across your skin."
    "You grip his hair in your hand, the other steadying yourself on the desk. His hands come to rest on your hips, his thumb rolling in small circles over your jutting bone."
    "He hesitates for a moment. Then you feel the slick pressure of his tongue against the folds of your vagina."
    "You let out a soft noise, jutting your hips in his direction."
    "His tongue plays against your lips, threatening to slip between them. You press your lips together, trying to contain a moan."
    if corruption > 10:
        "His tongue pierces suddenly between your folds and you let out an audible gasp."
        "Your thighs clench around his head on instinct. He grabs your legs, keeping them firmly over his shoulders."
    elif True:
        "Unable to take it anymore, you grip his hair and force his face further between your legs."
        pcname "What are you waiting for?"
        "Sensing your impatience, Damien presses his tongue between your folds. You let out an audible gasp."
        "Your thighs clench around his head, keeping him in place."
    pcname "Ah...! Damien!"
    if mattchain >= 3:
        m "Damien?"
        "You freeze at the sound of Matt's voice."
        "He stands over your shoulder, his cold blue eyes glaring down at you."
        "This does not seem to deter Damien at all, who only presses his tongue further into you, licking up your wetness eagerly."
        "Your arch your back, moaning."
        "Matt grabs your shoulders, forcing you flat on your back onto the desk."
        m "You really are a little whore."
        "You flush, glancing between the two boys. Damien doesn't seem to be aware of Matt at all, as though he can't see him."
        "Matt unzips his own pants, pulling himself out. You stare up at the erect cock and feel a little thrill."
        m "Well? Are you just going to let him have all the fun?"
        "He holds up his phone, showing off the pictures of you from the locker room."
        m "Or do I need to show him these?"
        "Your heart hammers in your chest. Damien grips your hips, forcing his tongue deeper into you. You moan, grinding against his face."
        "Matt turns your head onto its side, pressing his cock against your lips. You open wide, taking him in."
        m "There's a good whore."
        "Matt intertwines his fingers in your hair, rougher than you had anticipated, and forces himself deeper inside."
        if corruption > 15:
            "You feel his cock press against the back of your throat and let out a pleasurable moan. The noise reverberates against his dick, and he thrusts eagerly into your mouth, his balls smacking against your face."
        elif True:
            "You're unable to fit it entirely in your mouth but suck as much of his member that you can manage. You sense his disappointment, but pump his shaft with your hand, hoping this will make up for it."
        D "[pcname]..."
        "Damien pulls away from your pussy, his lips covered in your cum. You feel a thrill of pleasure as his tongue laps against it, cleaning up his face."
        "With your mouth preoccupied with Matt's cock, you're only able to give a strangled noise of an answer."
        "Damien rises from the chair and adjusts himself between your legs. You feel the hardness of his cock brush against your thigh."
        if corruption > 10:
            "Gripping your hips between his fingers, Damien inserts himself into you. Your pussy welcomes him, allowing him to slip easily between your folds."
        elif True:
            "Damien grips your thighs but hesitates."
            "Unable to contain yourself anymore, you thrust your hips toward him. Taking the hint, Damien inserts himself."
        "You let out another moan around Matt's cock. The two men take you from either end, coating their members in your cum and saliva."
        "Damien is not as rough fucking you as Matt is. He moves methodically inside of you, taking the time to move your hips against him in a wave-like motion. It's a different sort of pleasure than the kind Matt gives you, more attentive to your needs."
        "Matt notices your trouble to keep up with your blowjob as Damien fucks you. Matt yanks himself out your mouth, leaving only the taste of his salty precum behind."
        m "Switch him."
        "Matt's words leave no room for argument. You look down at Damien, a sense of pleasure rippling through your body at the sight of his obvious pleasure."
        "He gasps and thrusts inside of you, his lips pressed into a tight line in an attempt to quiet his moaning."
        "Matt tightens his grip on your hair: a warning."
        pcname "D-Damien..."
        "He meets your gaze, slowing down. You try to resist the urge to buck against him and pick up the speed again."
        "You motion him forward, and he happily obliges, walking past Matt to reach your face. He brushes a few strands of hair gently from your cheek, his fingers lingering at your neck."
        "You hardly have a moment to enjoy the touch before Matt thrusts deeply into you. You let out a sudden gasp, pleased to be filled again."
        "Damien runs his thumb across your lips. You part them slightly, allowing his member to press into your mouth."
        "The men fuck you again from both ends, their movements noticeably different."
        "Matt fucks you hard, gripping onto your legs to keep his thrusts rough and sudden. Damien is slower, taking his time to enjoy each movement into your mouth."
        "Your hips move instinctively with Matt's thrusts, each of your pace growing quicker by the second."
        "Damien thrusts himself deeper into your mouth, forcing himself against the back of your throat. They begin to pant."
        "You thrust against Matt harder, your mouth working eagerly on Damien."
        "A wave of pleasure shudders through you as Matt pounds against your gspot. You feel so close-"
        $ damienmattthreesomedream = True
    elif violetscenes >= 5:
        V "Damien?"
        "You freeze at the sound of Violet's voice."
        "Hesitantly, you peer over your shoulder. Violet stands behind the desk, her arms crossed and a scowl on her face."
        if corruption >= 20:
            V "Why didn't you come get me?"
            "You feel a surge of guilt run through you. How could you have forgotten her?"
            "Damien pulls his tongue out slightly, only enough to move up to your clit. You let out a moan as he rubs his tongue against it."
            pcname "Come here."
            "She hesitates, watching jealously as Damien pleases you."
            pcname "Now."
            V "Yes, mistress."
            "Violet steps to the side of the desk, glancing between you and Damien with a pout."
            pcname "Don't give me that look. You shouldn't have walked in on us."
            V "I-I'm sorry, mistress."
            "Violet looks away, biting her lip. You feel a thrill of pleasure at seeing her so weak against your words."
            pcname "You realize I'll have to punish you."
            "Damien pulls back from your pussy, his interest piqued."
            V "But-"
            pcname "Turn around. Bend over."
            "Violet does so obediently, fidgeting with her hands in front of her. You have a clear view of her silky panties under her skirt."
            pcname "Damien, remove those."
            "You point at the panties. Damien turns in his chair and slips his fingers underneath the edge of the lace. Violet lets out a small noise as he exposes her."
            "You stare at the firm curve of her ass, and you catch Damien staring, too."
            pcname "If you want to look at it so badly, you might as well touch it."
            "Damien and Violet both look back in surprise at your words. Their faces burn bright."
            V "M-Mistress?"
            D "Ah, [pcname]..."
            pcname "Mistress."
            D "Mistress... I don't know if I-"
            pcname "I wasn't asking. Do it."
            "Damien hesitates, but presses his hand against her ass, caressing the soft skin. You feel a sense of joy as they follow your orders without question."
            pcname "Doesn't that feel good, Damien?"
            D "Yes, mistress."
            pcname "And you, Violet?"
            "She bites her lip and gives a slow nod."
            V "Y-yes..."
            pcname "Good."
            "You rise from the desk and take Damien's hand. He watches you silently as you bring it back and slap her hard against the ass."
            V "Oh!"
            "Violet jerks at the touch. You grin, wind his hand back again, and slap her ass."
            "Again. And again. And again."
            "There's a bright red mark left where Damien's hand had been, and you pause, admiring your work."
            pcname "Damien, fuck her."
            "Damien follows your orders and adjusts himself behind Violet, grinding against her from behind. Violet lets out a soft whimper."
            "You climb onto the desk Violet bends in front of and spread your legs."
            pcname "You've been a bad girl, Violet. Do you understand?"
            "You give a small nod to Damien. He thrusts inside of her. Violet lets out a small noise and nods."
            V "I-I do, mistress."
            pcname "And you know that getting fucked by my boyfriend isn't going to fix it, right?"
            "She nods again."
            V "Please let me make it up to you, mistress. I'll do anything."
            pcname "I know you will."
            "You let your legs relax, falling on either side of her. Violet's breasts bounce as Damien thrusts inside of her. You take a moment to enjoy the image of your two favorite people in such pleasure."
            pcname "Then take care of me."
            "Violet needs no goading. She presses hard kisses against your pussy, letting her tongue slip out a little more each time."
            "You arch against her, grinding against her mouth."
            pcname "You can do better than that."
            "Flushed, Violet licks against your clit, her tongue rough against the hardening nub."
            "You moan. Damien thrusts into Violet harder, as though he needed your voice to approve his actions. Violet reacts with quick flicks of her tongue."
            "You watch in satisfaction as Violet squirms beneath Damien, focusing on giving you as much attention as she can muster under his thrusts."
            "You feel your hips begin to jerk outward toward Violet with each flick of her tongue, a wave of pleasure overcoming you."
            "You grab Violet's hair and grind against her tongue, unable to take it anymore-"
        if corruption <= 20:
            V "It's {i}my{/i} name you should be screaming."
            "She turns her attention to Damien. He pulls his tongue from your cunt, leaving you dripping and disappointed."
            D "I'm sorry, Violet. It's all my fault."
            "Even as he says so, Damien's fingers press against your clit, rubbing the small nub. You feel it harden under his touch."
            pcname "Please forgive us."
            "Violet steps around to the side of the desk, observing you. You bite your lip, trying to keep your moans quiet lest she be more upset."
            "She glares at Damien and grips his hair. You think for a moment that she'll pull him away, but instead, she shoves his face harder against you."
            V "You're doing it all wrong. Are you an idiot?"
            "Damien mumbles something of an apology, but his mouth is preoccupied with your clit. He moves his head with Violet's grip, his tongue tracing circles around the nub. You arch your back toward him, letting out a soft whimper."
            V "That's more like it."
            "She directs her attention to you. You shrink a little but feel the desire to make things up to her swell inside of you."
            pcname "I'm so sorry, Violet-"
            V "Mistress."
            pcname "Mistress. I-I'm sorry. Please, allow me to make it up to you."
            V "You will."
            "Violet climbs on top of you over the desk, straddling you. Your nipples harden against the stiff fabric of your blouse as she squeezes your breasts."
            "Her nimble fingers unbutton your blouse, freeing your breasts from their confines. You hadn't noticed you weren't wearing a bra, but it hardly matters now."
            "She bends over and takes your right breast into her mouth, sucking hard."
            pcname "M-Mistress..."
            "Damien pulls back from your clit to admire Violet's work. Her mouth bounces between both breasts, giving each nipple the right amount of attention as her hand massages your other breast."
            "Noticing your lack of moaning, she sits upright and glares back at him."
            V "Did I say you could stop?"
            D "N-No, mistress."
            "Damien hurriedly presses his face back into your pussy, and you feel pleasure warm you again as his tongue flicks your clit."
            "Letting go of your breasts, Violet scoots herself up further until her crotch hovers over your face. You stare up at her silky panties and bite your lip in anticipation."
            V "You better make it up to me."
            "You nod obediently, pulling the panties to the side. You feel the moisture between her folds as you brush against them."
            "She stares down at you hard, waiting."
            "You begin to press your finger against her clit."
            "She grabs your wrist."
            V "Does it look like that is enough?"
            "You spare a glance back down at Damien, understanding."
            pcname "No, mistress."
            "Grabbing onto her ass for leverage, you pull Violet closer, slipping your tongue between her slit. She inhales sharply, but otherwise gives no indication of her pleasure."
            "You take your time sliding your tongue between her folds, probing your tongue deeper into her pussy until all you can taste is the saltiness of her cum."
            "She grips your hair and forces your head forward, a sign you're doing it right."
            "Eager to please, you lap your tongue against her juices, thrusting it eagerly in and out of her folds."
            "Damien does the same to you, taking in every ounce of dripping liquid he can. You moan into Violet's pussy, thrusting to match his speed."
            "Violet does the same, her cunt grinding against your face. Your mouth is covered with your cum, yet you can't help but want more."
            V "Ngh... [pcname]..."
            "Her fingers pierce into your scalp as she shudders against your mouth, her hips thrusting violently against you."
            "You feel a similar pressure building as Damien moves to your clit, his tongue fast against the hard nub. You let out a moan-"
            $ damienvioletthreesomedream = True
    elif True:
        "Encouraged by your moan, Damien laps his tongue further into you, taking in your cum in swift, slick motions."
        "You lay back on the cool, hard desk, holding Damien in place with your thighs."
        "As he eats you out, Damien's hands slide up your sides under your blouse and cup your breasts, his fingers toying lightly with your perky nipples."
        "You remove your blouse eagerly, your nipples hardening at the sudden cold air."
        "With a gasp, Damien pulls his head out from your dripping cunt. You let out a moan of disappointment."
        pcname "Come back."
        D "I will."
        if damienconfidence > 10:
            "Damien yanks you off of the desk and into his lap, grasping at your ass. You wind your legs around his waist, steadying yourself."
            "His hands move to your hips and, after a moment's hesitation, he thrusts inside of you."
            "You place a hand over your mouth to silence the moan, the other grasping his shoulder."
        elif True:
            "You climb off of the desk and slip into his lap, securing your legs around his waist."
            "His cock feels hard against your pussy, pressing into you."
            "You adjust yourself on top of him and slowly insert him into you."
            "Damien let's out a muffled moan behind his hand, his hips jerking in your direction."
        "You ride on top of him, each thrust quicker and wetter than the last. He slips in easily in no time at all."
        "Your panting mingles together as you grasp wherever your hands can reach, the chair rattling against the floor as you both thrust against each other."
        "You feel a pressure building up in your lower belly as Damien hits your gspot. Your legs become weak and shaky, while he seems to grow sturdier and more confident as he pounds inside of you."
        pcname "Damien...!"
        "Your vision becomes hazy as you begin to hit your climax-"
        $ damiensexdream = True
    "There's a knock on the door."
    "You open your eyes, dazed."
    $ clothes = 'naked'
    hide bg ClassroomE with dissolve
    show bg RoomE with dissolve
    "The classroom is gone."
    "You find yourself settled on your bed, your blankets bundled between your thighs."
    "You blush, realizing what you've been doing."
    "Another knock at the door."
    D "Ah, [pcname]?"
    "For a moment, you consider the events of last night to be real. Then, you're reminded of the festival, and your date."
    "You almost let out a breath of disappointment."
    show chelsea embarrassed at right with dissolve
    pcname "Um, yeah?"
    D "Oh, I'm sorry. Did I wake you?"
    "You can hear the panic in his voice. Untangling yourself from the blankets, you sit up and stretch."
    pcname "N-No. I've been up for hours."
    "If he doesn't believe you, he's considerate enough to pretend he does."
    D "Oh. Well, um, I'm going to get going soon. I have to pick up some stuff on the way home..."
    pcname "Sure! Yeah. Let me make you breakfast before you go. Just give me a few minutes."
    D "Thanks. I'd appreciate that."
    "You wait until Damien's footsteps fade back into the living room before falling back onto your bed."
    if club == "track":
        "You pout up at your ceiling, annoyed."
        pcname "I can't believe I didn't get to cum."
    if club == "cheer":
        show chelsea angry
        pcname "Of course I woke up before I came."
        "Frustrated, you stuff your hand into your pajama bottoms, intending to finish the job."
    if club == "yearbook":
        "Mortified, you stuff your head under your pillow and let out a long, muffled scream."
    hide chelsea with dissolve
    show bg black with fade
    $ clothes = 'school'
    pause 0.5
    show bg HomeE with dissolve
    show chelsea at right with moveinright
    "After a few minutes, you step out into the living room, dressed for the day."
    "Damien waits by the kitchen doorway, nervously fixing the sleeve of his hoodie."
    show Damien Blank at left with moveinleft
    "He has already folded up your blankets. They sit in a pile on the edge of the couch."
    show chelsea happy
    pcname "Oh, you didn't have to do that. Thanks."
    show Damien Happy at left
    D "It was no problem."
    "He gives you a small smile, and you return the favor. Your eyes trail down to his cargo shorts. You bite your lip, recalling the start of your dream."
    show Damien Neutral at left
    D "Everything okay?"
    pcname "Yeah. I'm fine."
    show Damien Blank at left
    "You hurry past him into the kitchen and open up the fridge."
    show Damien Happy at left
    D "Did you sleep okay?"
    "You try to avoid his gaze as you prepare to make pancakes."
    pcname "I slept fine. You?"
    D "I slept okay. Your couch is really comfy."
    "You can't imagine sleeping on a couch was that comfortable, but you take the compliment."
    pcname "I'm glad. I was worried it would ruin your back."
    D "Nah, I'm fine."
    "There's a short pause as you make pancakes over the oven. Then-"
    show Damien Neutral at left
    D "Did you have a nightmare last night?"
    show chelsea shocked
    show Damien Blank at left
    "Startled, you nearly drop your spatula. You shake your head, gathering yourself."
    show chelsea confused
    pcname "No. Why?"
    show Damien Neutral at left
    D "You were moaning a lot in your sleep. That's... Well, that's why I woke you up... I was worried..."
    show chelsea embarrassed
    "You stare down intently at the burning pancakes over your oven. If you turn to face him now, you're sure the fiery blush on your face will give you away."
    pcname "Ah... yeah... Sorry about that. It was... a bad dream..."
    "But all the right kinds of bad, you can't help but think."
    show Damien Happy at left
    D "I'm sorry. At least you're awake now, though."
    pcname "Yeah. At least I'm awake now."
    show chelsea happy
    "You finish the pancakes and set the table, taking your mind off of the dream."
    "You enjoy a nice breakfast with Damien, ignoring his taunts about your excessive use of syrup before he leaves."
    hide Damien Happy with dissolve
    hide chelsea with dissolve
    $ damiendate = False
    $ DamienAngry = "Characters/Damien/School Uniform/Angry.png"
    $ DamienBlank = "Characters/Damien/School Uniform/Blank.png"
    $ DamienGlare = "Characters/Damien/School Uniform/Glaring.png"
    $ DamienLaugh = "Characters/Damien/School Uniform/Laughing.png"
    $ DamienNeutral = "Characters/Damien/School Uniform/Neutral.png"
    $ DamienSad = "Characters/Damien/School Uniform/Sad.png"
    $ DamienShocked = "Characters/Damien/School Uniform/Shocked.png"
    $ DamienSmiling = "Characters/Damien/School Uniform/Smiling.png"
    $ DamienWorrying = "Characters/Damien/School Uniform/Worrying.png"
    show bg black with dissolve
    jump newday
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
